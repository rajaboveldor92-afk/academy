import '../core/app_edition.dart';
import '../models/child_profile.dart';
import 'local_database.dart';

/// Standart profillar va ma'lumotlar migratsiyasi.
///
/// * Birinchi ochilishda Azamjon, Muhammadjon (maktabgacha), Jasmina (3-sinf) va Akramjon (5-sinf)
///   profillari yaratiladi (bir marta — ota-ona o'chirsa qayta paydo bo'lmaydi).
/// * `dataVersion` bo'yicha eski o'rnatmalar yangi maydonlar bilan to'ldiriladi.
class SeedData {
  SeedData._();

  /// Joriy ma'lumotlar versiyasi.
  /// 2 — to'liq ism, salomlashuv matni va profil mavzulari qo'shildi.
  /// 3 — maktab o'quvchilari: Jasmina (3-sinf) va Akramjon (5-sinf).
  /// 4 — profil jinsi va ota-ona tanlaydigan texnologiya yo‘nalishi.
  static const int currentDataVersion = 4;

  static const String azamjonId = 'azamjon';
  static const String muhammadjonId = 'muhammadjon';
  static const String jasminaId = 'jasmina';
  static const String akramjonId = 'akramjon';

  /// Mavzu indekslari (`ProfileThemes.all`): 4 — Koinot 🚀, 1 — Quyosh ☀️.
  static const int azamjonTheme = 4;
  static const int muhammadjonTheme = 1;

  /// 5 — Konfet 🍭, 0 — Okean 🌊.
  static const int jasminaTheme = 5;
  static const int akramjonTheme = 0;

  static ChildProfile azamjon(DateTime now) => ChildProfile.create(
        id: azamjonId,
        name: 'Azamjon',
        gender: 'boy',
        fullName: 'Odilbekov Azamjon Eldorovich',
        age: 6,
        avatar: '🦁',
        colorIndex: azamjonTheme,
        greeting: ChildProfile.defaultGreetingSenior,
        now: now,
      );

  static ChildProfile muhammadjon(DateTime now) => ChildProfile.create(
        id: muhammadjonId,
        name: 'Muhammadjon',
        gender: 'boy',
        fullName: 'Odilbekov Muhammadjon Eldorovich',
        age: 4,
        avatar: '🐻',
        colorIndex: muhammadjonTheme,
        greeting: ChildProfile.defaultGreetingJunior,
        now: now,
      );

  static ChildProfile jasmina(DateTime now) => ChildProfile.create(
        id: jasminaId,
        name: 'Jasmina',
        gender: 'girl',
        fullName: 'Odilbekova Jasmina Temurbekovna',
        age: 9,
        grade: 3,
        avatar: '🦄',
        colorIndex: jasminaTheme,
        greeting: ChildProfile.defaultGreetingSchool,
        now: now,
      );

  static ChildProfile akramjon(DateTime now) => ChildProfile.create(
        id: akramjonId,
        name: 'Akramjon',
        gender: 'boy',
        fullName: 'Odilbekov Akramjon Temurbekovich',
        age: 11,
        grade: 5,
        avatar: '🦊',
        colorIndex: akramjonTheme,
        greeting: ChildProfile.defaultGreetingSchool,
        now: now,
      );

  static Future<void> _addSchoolChildren(LocalDatabase db, DateTime base) async {
    if (AppEditionConfig.isKids) return;
    if (db.getProfile(jasminaId) == null) await db.saveProfile(jasmina(base.add(const Duration(milliseconds: 2))));
    if (db.getProfile(akramjonId) == null) await db.saveProfile(akramjon(base.add(const Duration(milliseconds: 3))));
  }

  static Future<void> ensureSeeded(LocalDatabase db, {DateTime? now}) async {
    var settings = db.getSettings();
    final base = now ?? DateTime.now();

    if (!settings.seeded) {
      if (db.getProfiles().isEmpty) {
        if (!AppEditionConfig.isSchool) {
          await db.saveProfile(azamjon(base));
          await db.saveProfile(muhammadjon(base.add(const Duration(milliseconds: 1))));
        }
        await _addSchoolChildren(db, base);
      }
      settings = settings.copyWith(seeded: true, dataVersion: currentDataVersion);
      await db.saveSettings(settings);
      return;
    }

    if (settings.dataVersion < 2) {
      await _migrateToV2(db);
    }
    // v2 → v3: maktab o'quvchilari bir marta qo'shiladi.
    if (settings.dataVersion < 3) {
      await _addSchoolChildren(db, base);
    }
    if (settings.dataVersion < 4) {
      for (final id in [azamjonId, muhammadjonId, jasminaId, akramjonId]) {
        final profile = db.getProfile(id);
        if (profile != null && profile.gender == 'unspecified') {
          await db.saveProfile(profile.copyWith(gender: id == jasminaId ? 'girl' : 'boy'));
        }
      }
    }
    if (settings.dataVersion < currentDataVersion) {
      await db.saveSettings(settings.copyWith(dataVersion: currentDataVersion));
    }
  }

  /// v1 → v2: standart profillarga to'liq ism, salom matni va mavzu beriladi.
  static Future<void> _migrateToV2(LocalDatabase db) async {
    final a = db.getProfile(azamjonId);
    if (a != null && a.fullName.isEmpty) {
      await db.saveProfile(a.copyWith(
        fullName: 'Odilbekov Azamjon Eldorovich',
        greeting: ChildProfile.defaultGreetingSenior,
        colorIndex: azamjonTheme,
      ));
    }
    final m = db.getProfile(muhammadjonId);
    if (m != null && m.fullName.isEmpty) {
      await db.saveProfile(m.copyWith(
        fullName: 'Odilbekov Muhammadjon Eldorovich',
        greeting: ChildProfile.defaultGreetingJunior,
        colorIndex: muhammadjonTheme,
      ));
    }
  }
}
