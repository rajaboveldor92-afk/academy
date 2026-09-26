import 'dart:math';

import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/constants/app_constants.dart';
import '../../core/providers.dart';
import '../../models/child_profile.dart';

/// Profil yaratish/tahrirlashdagi tekshiruv xatolari.
class ProfileValidationException implements Exception {
  const ProfileValidationException(this.message);
  final String message;

  @override
  String toString() => message;
}

/// Barcha bola profillari ro'yxati.
class ProfilesNotifier extends Notifier<List<ChildProfile>> {
  final Random _random = Random();

  @override
  List<ChildProfile> build() => ref.read(databaseProvider).getProfiles();

  /// Ism va yoshni tekshiradi; muammo bo'lsa [ProfileValidationException].
  static void validate({required String name, required int age, String fullName = ''}) {
    final trimmed = name.trim();
    if (trimmed.isEmpty) {
      throw const ProfileValidationException('Qisqa ismni kiriting');
    }
    if (trimmed.length > AppConstants.maxNameLength) {
      throw const ProfileValidationException('Ism juda uzun');
    }
    if (fullName.trim().length > AppConstants.maxFullNameLength) {
      throw const ProfileValidationException("To'liq ism juda uzun");
    }
    if (age < AppConstants.minAge || age > AppConstants.maxAge) {
      throw const ProfileValidationException('Yosh 3 dan 8 gacha bo\'lishi kerak');
    }
  }

  String _newId() =>
      'c${DateTime.now().microsecondsSinceEpoch}${_random.nextInt(9999).toString().padLeft(4, '0')}';

  Future<ChildProfile> create({
    required String name,
    required int age,
    required String avatar,
    int? colorIndex,
    String fullName = '',
    String greeting = '',
    String? photoPath,
  }) async {
    validate(name: name, age: age, fullName: fullName);
    final profile = ChildProfile.create(
      id: _newId(),
      name: name,
      fullName: fullName,
      greeting: greeting,
      photoPath: photoPath,
      age: age,
      avatar: avatar,
      colorIndex: colorIndex ?? state.length,
      now: ref.read(clockProvider)(),
    );
    await ref.read(databaseProvider).saveProfile(profile);
    state = [...state, profile];
    return profile;
  }

  Future<void> updateProfile(ChildProfile profile) async {
    validate(name: profile.name, age: profile.age, fullName: profile.fullName);
    await ref.read(databaseProvider).saveProfile(profile);
    state = [
      for (final p in state) p.id == profile.id ? profile : p,
    ];
  }

  Future<void> delete(String id) async {
    for (final p in state) {
      if (p.id == id) await ref.read(profilePhotoServiceProvider).delete(p.photoPath);
    }
    await ref.read(databaseProvider).deleteProfile(id);
    state = state.where((p) => p.id != id).toList();
    if (ref.read(activeChildIdProvider) == id) {
      ref.read(activeChildIdProvider.notifier).clear();
    }
  }

  /// Backup import qilingandan keyin bazadan qayta o'qish.
  void reload() => state = ref.read(databaseProvider).getProfiles();
}

final profilesProvider =
    NotifierProvider<ProfilesNotifier, List<ChildProfile>>(ProfilesNotifier.new);

/// Hozir o'ynayotgan bola id'si.
class ActiveChildNotifier extends Notifier<String?> {
  @override
  String? build() => null;

  void select(String id) => state = id;

  void clear() => state = null;
}

final activeChildIdProvider =
    NotifierProvider<ActiveChildNotifier, String?>(ActiveChildNotifier.new);

/// Tanlangan bola profili (yoki `null`).
final activeProfileProvider = Provider<ChildProfile?>((ref) {
  final id = ref.watch(activeChildIdProvider);
  if (id == null) return null;
  for (final p in ref.watch(profilesProvider)) {
    if (p.id == id) return p;
  }
  return null;
});
