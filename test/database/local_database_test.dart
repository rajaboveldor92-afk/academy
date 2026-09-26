import 'package:academy/database/seed_data.dart';
import 'package:academy/models/app_settings.dart';
import 'package:academy/models/child_profile.dart';
import 'package:academy/models/child_progress.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

void main() {
  late TestDb t;

  setUp(() async => t = await TestDb.open());
  tearDown(() async => t.dispose());

  test('seed Azamjon (6) va Muhammadjon (4) ni bir marta yaratadi', () async {
    await SeedData.ensureSeeded(t.db);
    var profiles = t.db.getProfiles();
    expect(profiles.map((p) => p.name), ['Azamjon', 'Muhammadjon']);
    expect(profiles.map((p) => p.age), [6, 4]);
    expect(profiles.map((p) => p.fullName),
        ['Odilbekov Azamjon Eldorovich', 'Odilbekov Muhammadjon Eldorovich']);
    expect(profiles.first.colorIndex, isNot(profiles.last.colorIndex));
    expect(t.db.getSettings().dataVersion, SeedData.currentDataVersion);

    // O'chirilgan profil qayta paydo bo'lmasligi kerak.
    await t.db.deleteProfile('muhammadjon');
    await SeedData.ensureSeeded(t.db);
    profiles = t.db.getProfiles();
    expect(profiles.map((p) => p.name), ['Azamjon']);
  });

  test('profil saqlanadi va qayta o\'qiladi', () async {
    final p = ChildProfile.create(id: 'k1', name: 'Kamola', age: 5, avatar: '🦄');
    await t.db.saveProfile(p);
    expect(t.db.getProfile('k1'), p);
    await t.db.saveProfile(p.copyWith(age: 6));
    expect(t.db.getProfile('k1')!.age, 6);
    expect(t.db.getProfiles().length, 1);
  });

  test('progress saqlanadi va profil bilan birga o\'chadi', () async {
    final now = DateTime(2026, 9, 26, 10);
    final progress = ChildProgress.empty('k1')
        .registerVisit(now)
        .addSeconds(now, 300)
        .recordAnswer(subjectId: 'math', isCorrect: true, now: now, rewardStars: 3);
    await t.db.saveProfile(ChildProfile.create(id: 'k1', name: 'Kamola', age: 5, avatar: '🦄'));
    await t.db.saveProgress(progress);

    final loaded = t.db.getProgress('k1');
    expect(loaded.stars, 3);
    expect(loaded.secondsOn(now), 300);
    expect(loaded.scoreOf('math').correct, 1);

    await t.db.deleteProfile('k1');
    expect(t.db.getProgress('k1').stars, 0);
  });

  test('sozlamalar: standart PIN 1234', () async {
    expect(t.db.getSettings().parentPin, '1234');
    await t.db.saveSettings(const AppSettings(parentPin: '4321', soundEnabled: false));
    final s = t.db.getSettings();
    expect(s.parentPin, '4321');
    expect(s.soundEnabled, isFalse);
  });

  test('backup eksport → import to\'liq tiklaydi', () async {
    await SeedData.ensureSeeded(t.db);
    final now = DateTime(2026, 9, 26);
    await t.db.saveProgress(
      ChildProgress.empty('azamjon').recordAnswer(
        subjectId: 'math',
        isCorrect: true,
        now: now,
        rewardStars: 5,
      ),
    );
    final json = t.db.exportJson(now: now);

    await t.db.deleteProfile('azamjon');
    await t.db.deleteProfile('muhammadjon');
    expect(t.db.getProfiles(), isEmpty);

    await t.db.importJson(json);
    expect(t.db.getProfiles().length, 2);
    expect(t.db.getProgress('azamjon').stars, 5);
  });

  test('noto\'g\'ri backup fayli rad etiladi va ma\'lumot saqlanib qoladi', () async {
    await SeedData.ensureSeeded(t.db);
    await expectLater(t.db.importJson('{"foo": 1}'), throwsFormatException);
    expect(t.db.getProfiles().length, 2);
  });

  test("v1 o'rnatmasi v2 ga migratsiya qilinadi (to'liq ism, salom, mavzu)", () async {
    // Eski versiya: profil faqat qisqa ism bilan, sozlamalar seeded=true, dataVersion=1.
    await t.db.saveProfile(
      ChildProfile.create(id: 'azamjon', name: 'Azamjon', age: 6, avatar: '🦁'),
    );
    await t.db.saveSettings(const AppSettings(seeded: true));
    await SeedData.ensureSeeded(t.db);
    final a = t.db.getProfile('azamjon')!;
    expect(a.fullName, 'Odilbekov Azamjon Eldorovich');
    expect(a.welcomeSubtitle, 'Bugun birga o‘rganamiz!');
    expect(a.colorIndex, SeedData.azamjonTheme);
    expect(t.db.getSettings().dataVersion, SeedData.currentDataVersion);

    // Ota-ona keyin o'zgartirsa, migratsiya qayta ustiga yozmaydi.
    await t.db.saveProfile(a.copyWith(fullName: 'Azamjon Odilbekov'));
    await SeedData.ensureSeeded(t.db);
    expect(t.db.getProfile('azamjon')!.fullName, 'Azamjon Odilbekov');
  });
}
