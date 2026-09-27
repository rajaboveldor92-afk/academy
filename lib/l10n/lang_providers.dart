import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../features/parent/settings_controller.dart';
import '../features/profiles/profiles_controller.dart';

/// Umumiy ekranlar (profil tanlash, ota-ona bo'limi) tili.
final appLangProvider = Provider<String>((ref) => ref.watch(settingsProvider).appLanguage);

/// Tanlangan bolaning tili (bola ekranlari va mashqlar). Bola tanlanmagan bo'lsa — umumiy til.
final childLangProvider = Provider<String>((ref) {
  final profile = ref.watch(activeProfileProvider);
  return profile?.language ?? ref.watch(appLangProvider);
});
