import 'dart:convert';

import 'package:hive_ce/hive.dart';

import '../core/utils/map_utils.dart';
import '../models/app_settings.dart';
import '../models/child_profile.dart';
import '../models/child_progress.dart';

/// Mahalliy ma'lumotlar bazasi (Hive CE).
///
/// Barcha yozuvlar oddiy JSON-mos `Map` ko'rinishida saqlanadi, shuning
/// uchun kod generatsiyasi (adapter) talab qilinmaydi va backup/import
/// juda sodda bo'ladi.
///
/// Box'lar:
/// * `profiles` — kalit: profil id, qiymat: [ChildProfile.toMap]
/// * `progress` — kalit: profil id, qiymat: [ChildProgress.toMap]
/// * `settings` — kalit: `app`, qiymat: [AppSettings.toMap]
class LocalDatabase {
  LocalDatabase._(this._profiles, this._progress, this._settings);

  /// Xotiradagi baza (fayl yozmaydi) — widget testlar va ilovani diskka tegmasdan tekshirish uchun.
  /// Qiymatlar JSON orqali nusxalanadi, shuning uchun saqlash/o'qish Hive bilan bir xil ishlaydi.
  factory LocalDatabase.memory() => LocalDatabase._(_MemoryStore(), _MemoryStore(), _MemoryStore());

  static const String profilesBox = 'profiles';
  static const String progressBox = 'progress';
  static const String settingsBox = 'settings';
  static const String _settingsKey = 'app';
  static const int backupVersion = 1;

  final _Store _profiles;
  final _Store _progress;
  final _Store _settings;

  /// Box'larni ochadi. `Hive.init(...)` yoki `Hive.initFlutter()` avval
  /// chaqirilgan bo'lishi kerak.
  static Future<LocalDatabase> open() async {
    final profiles = await Hive.openBox<dynamic>(profilesBox);
    final progress = await Hive.openBox<dynamic>(progressBox);
    final settings = await Hive.openBox<dynamic>(settingsBox);
    return LocalDatabase._(_HiveStore(profiles), _HiveStore(progress), _HiveStore(settings));
  }

  // ---------------------------------------------------------------- Profiles

  List<ChildProfile> getProfiles() {
    final list = <ChildProfile>[];
    for (final value in _profiles.values) {
      final map = MapUtils.asStringMap(value);
      if (map['id'] == null) continue;
      list.add(ChildProfile.fromMap(map));
    }
    list.sort((a, b) => a.createdAt.compareTo(b.createdAt));
    return list;
  }

  ChildProfile? getProfile(String id) {
    final value = _profiles.get(id);
    if (value == null) return null;
    return ChildProfile.fromMap(MapUtils.asStringMap(value));
  }

  Future<void> saveProfile(ChildProfile profile) => _profiles.put(profile.id, profile.toMap());

  /// Profilni va unga tegishli statistikani o'chiradi.
  Future<void> deleteProfile(String id) async {
    await _profiles.delete(id);
    await _progress.delete(id);
  }

  // ---------------------------------------------------------------- Progress

  ChildProgress getProgress(String childId) {
    final value = _progress.get(childId);
    if (value == null) return ChildProgress.empty(childId);
    return ChildProgress.fromMap(MapUtils.asStringMap(value));
  }

  Map<String, ChildProgress> getAllProgress() {
    final result = <String, ChildProgress>{};
    for (final key in _progress.keys) {
      result[key.toString()] = getProgress(key.toString());
    }
    return result;
  }

  Future<void> saveProgress(ChildProgress progress) =>
      _progress.put(progress.childId, progress.toMap());

  // ---------------------------------------------------------------- Settings

  AppSettings getSettings() {
    final value = _settings.get(_settingsKey);
    if (value == null) return const AppSettings();
    return AppSettings.fromMap(MapUtils.asStringMap(value));
  }

  Future<void> saveSettings(AppSettings settings) =>
      _settings.put(_settingsKey, settings.toMap());

  // ---------------------------------------------------------------- Backup

  /// Butun bazani `academy_backup.json` formatidagi matnga aylantiradi.
  String exportJson({DateTime? now}) {
    final data = <String, dynamic>{
      'app': 'academy',
      'version': backupVersion,
      'exportedAt': (now ?? DateTime.now()).toIso8601String(),
      'settings': getSettings().toMap(),
      'profiles': getProfiles().map((p) => p.toMap()).toList(),
      'progress': getAllProgress().values.map((p) => p.toMap()).toList(),
    };
    return const JsonEncoder.withIndent('  ').convert(data);
  }

  /// Backup matnini tiklaydi. Noto'g'ri fayl bo'lsa [FormatException] tashlaydi
  /// va mavjud ma'lumotlarga tegmaydi.
  Future<void> importJson(String source) async {
    final decoded = jsonDecode(source);
    if (decoded is! Map || decoded['app'] != 'academy') {
      throw const FormatException('Bu Academy backup fayli emas');
    }
    final data = MapUtils.asStringMap(decoded);
    final profiles = (data['profiles'] as List? ?? const [])
        .map((e) => ChildProfile.fromMap(MapUtils.asStringMap(e)))
        .toList();
    final progress = (data['progress'] as List? ?? const [])
        .map((e) => ChildProgress.fromMap(MapUtils.asStringMap(e)))
        .toList();
    final settings = AppSettings.fromMap(MapUtils.asStringMap(data['settings']));

    await _profiles.clear();
    await _progress.clear();
    for (final p in profiles) {
      await saveProfile(p);
    }
    for (final p in progress) {
      await saveProgress(p);
    }
    await saveSettings(settings.copyWith(seeded: true));
  }

  Future<void> close() async {
    await _profiles.close();
    await _progress.close();
    await _settings.close();
  }
}

/// Kalit-qiymat ombori: Hive box yoki xotira.
abstract class _Store {
  dynamic get(String key);
  Future<void> put(String key, dynamic value);
  Future<void> delete(String key);
  Iterable<dynamic> get keys;
  Iterable<dynamic> get values;
  Future<void> clear();
  Future<void> close();
}

class _HiveStore implements _Store {
  _HiveStore(this._box);

  final Box<dynamic> _box;

  @override
  dynamic get(String key) => _box.get(key);

  @override
  Future<void> put(String key, dynamic value) => _box.put(key, value);

  @override
  Future<void> delete(String key) => _box.delete(key);

  @override
  Iterable<dynamic> get keys => _box.keys;

  @override
  Iterable<dynamic> get values => _box.values;

  @override
  Future<void> clear() async {
    await _box.clear();
  }

  @override
  Future<void> close() => _box.close();
}

class _MemoryStore implements _Store {
  final Map<String, String> _data = {};

  @override
  dynamic get(String key) {
    final raw = _data[key];
    return raw == null ? null : jsonDecode(raw);
  }

  @override
  Future<void> put(String key, dynamic value) async => _data[key] = jsonEncode(value);

  @override
  Future<void> delete(String key) async => _data.remove(key);

  @override
  Iterable<dynamic> get keys => _data.keys.toList();

  @override
  Iterable<dynamic> get values => [for (final k in _data.keys) get(k)];

  @override
  Future<void> clear() async => _data.clear();

  @override
  Future<void> close() async {}
}
