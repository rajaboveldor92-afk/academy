import '../models/child_profile.dart';
import 'local_database.dart';

/// Ilova birinchi marta ochilganda standart profillarni yaratadi.
///
/// Faqat bir marta ishlaydi (`AppSettings.seeded`), shuning uchun ota-ona
/// profilni o'chirsa, u qayta paydo bo'lmaydi.
class SeedData {
  SeedData._();

  static Future<void> ensureSeeded(LocalDatabase db, {DateTime? now}) async {
    final settings = db.getSettings();
    if (settings.seeded) return;

    if (db.getProfiles().isEmpty) {
      final base = now ?? DateTime.now();
      await db.saveProfile(ChildProfile.create(
        id: 'azamjon',
        name: 'Azamjon',
        age: 6,
        avatar: '🦁',
        colorIndex: 0,
        now: base,
      ));
      await db.saveProfile(ChildProfile.create(
        id: 'muhammadjon',
        name: 'Muhammadjon',
        age: 4,
        avatar: '🐻',
        colorIndex: 1,
        now: base.add(const Duration(milliseconds: 1)),
      ));
    }
    await db.saveSettings(settings.copyWith(seeded: true));
  }
}
