import 'package:academy/database/local_database.dart';
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

  test('seed Azamjon (6), Muhammadjon (4), Jasmina (3-sinf) va Akramjon (5-sinf) ni bir marta yaratadi', () async {
    await SeedData.ensureSeeded(t.db);
    var profiles = t.db.getProfiles();
    expect(profiles.map((p) => p.name), ['Azamjon', 'Muhammadjon', 'Jasmina', 'Akramjon']);
    expect(profiles.map((p) => p.age), [6, 4, 9, 11]);
    expect(profiles.map((p) => p.grade), [0, 0, 3, 5]);
    expect(profiles.map((p) => p.fullName), [
      'Odilbekov Azamjon Eldorovich',
      'Odilbekov Muhammadjon Eldorovich',
      'Odilbekova Jasmina Temurbekovna',
      'Odilbekov Akramjon Temurbekovich',
    ]);
    expect(profiles.map((p) => p.colorIndex).toSet().length, 4);
    expect(t.db.getSettings().dataVersion, SeedData.currentDataVersion);

    // O'chirilgan profil qayta paydo bo'lmasligi kerak.
    await t.db.deleteProfile('muhammadjon');
    await SeedData.ensureSeeded(t.db);
    profiles = t.db.getProfiles();
    expect(profiles.map((p) => p.name), ['Azamjon', 'Jasmina', 'Akramjon']);
  });

  test('v2 o‘rnatmasiga Jasmina va Akramjon bir marta qo‘shiladi', () async {
    await t.db.saveProfile(SeedData.azamjon(DateTime(2026)));
    await t.db.saveSettings(const AppSettings(seeded: true, dataVersion: 2));
    await SeedData.ensureSeeded(t.db);
    expect(t.db.getProfile('jasmina')!.grade, 3);
    expect(t.db.getProfile('akramjon')!.grade, 5);
    expect(t.db.getProfile('akramjon')!.dailyLimitMinutes, 40);
    expect(t.db.getSettings().dataVersion, SeedData.currentDataVersion);
    await t.db.deleteProfile('jasmina');
    await SeedData.ensureSeeded(t.db);
    expect(t.db.getProfile('jasmina'), isNull);
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

    for (final p in t.db.getProfiles()) {
      await t.db.deleteProfile(p.id);
    }
    expect(t.db.getProfiles(), isEmpty);

    await t.db.importJson(json);
    expect(t.db.getProfiles().length, 4);
    expect(t.db.getProgress('azamjon').stars, 5);
  });

  test('noto\'g\'ri backup fayli rad etiladi va ma\'lumot saqlanib qoladi', () async {
    await SeedData.ensureSeeded(t.db);
    await expectLater(t.db.importJson('{"foo": 1}'), throwsFormatException);
    expect(t.db.getProfiles().length, 4);
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
  test('xotiradagi baza Hive bilan bir xil saqlaydi va o‘qiydi', () async {
    final db = LocalDatabase.memory();
    await SeedData.ensureSeeded(db);
    expect(db.getProfiles().map((p) => p.name), ['Azamjon', 'Muhammadjon', 'Jasmina', 'Akramjon']);
    final progress = ChildProgress.empty('azamjon')
        .addStars(12)
        .completeDaily(DateTime(2026, 9, 26, 9))
        .addCounter('chess_win');
    await db.saveProgress(progress);
    final back = db.getProgress('azamjon');
    expect(back.stars, 12);
    expect(back.dailyLessons, 1);
    expect(back.counter('chess_win'), 1);
    expect(db.getAllProgress().keys, contains('azamjon'));
    // Eksport → boshqa xotira bazasiga import.
    final copy = LocalDatabase.memory();
    await copy.importJson(db.exportJson());
    expect(copy.getProgress('azamjon').stars, 12);
    expect(copy.getProfiles().length, 4);
    await db.deleteProfile('azamjon');
    expect(db.getProfile('azamjon'), isNull);
    expect(db.getAllProgress().containsKey('azamjon'), isFalse);
  });
}
