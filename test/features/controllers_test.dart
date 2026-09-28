import 'package:academy/features/parent/settings_controller.dart';
import 'package:academy/features/profiles/profiles_controller.dart';
import 'package:academy/features/session/progress_controller.dart';
import 'package:academy/features/session/session_controller.dart';
import 'package:academy/services/parent_pin_service.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

void main() {
  late TestDb t;
  late FakeClock clock;
  late ProviderContainer c;

  setUp(() async {
    t = await TestDb.open();
    clock = FakeClock(DateTime(2026, 9, 26, 10));
    c = makeContainer(t.db, clock: clock);
  });

  tearDown(() async {
    c.dispose();
    await t.dispose();
  });

  group('Profillar', () {
    test('profil yaratish bazaga yoziladi', () async {
      final p = await c.read(profilesProvider.notifier).create(
            name: 'Kamola',
            age: 5,
            avatar: '🦄',
          );
      expect(c.read(profilesProvider).single.id, p.id);
      expect(t.db.getProfile(p.id)?.name, 'Kamola');
    });

    test('bo\'sh ism va noto\'g\'ri yosh rad etiladi', () async {
      final n = c.read(profilesProvider.notifier);
      await expectLater(
        n.create(name: '  ', age: 5, avatar: '🦄'),
        throwsA(isA<ProfileValidationException>()),
      );
      await expectLater(
        n.create(name: 'Ali', age: 17, avatar: '🦄'),
        throwsA(isA<ProfileValidationException>()),
      );
      expect(c.read(profilesProvider), isEmpty);
    });

    test('profil tanlash va o\'chirish', () async {
      final n = c.read(profilesProvider.notifier);
      final a = await n.create(name: 'Azamjon', age: 6, avatar: '🦁');
      final b = await n.create(name: 'Muhammadjon', age: 4, avatar: '🐻');

      c.read(activeChildIdProvider.notifier).select(b.id);
      expect(c.read(activeProfileProvider)?.name, 'Muhammadjon');

      await n.delete(b.id);
      expect(c.read(activeProfileProvider), isNull);
      expect(c.read(profilesProvider).map((p) => p.id), [a.id]);
    });

    test('yosh o\'zgarsa kontent guruhi avtomatik o\'zgaradi', () async {
      final n = c.read(profilesProvider.notifier);
      final p = await n.create(name: 'Muhammadjon', age: 4, avatar: '🐻');
      expect(p.ageGroup.suffix, '4');
      await n.updateProfile(p.copyWith(age: 6));
      expect(c.read(profilesProvider).single.ageGroup.suffix, '6');
    });
  });

  group('Progress', () {
    test('javob yulduz beradi va bazada saqlanadi', () async {
      await c.read(progressProvider.notifier).recordAnswer(
            childId: 'k1',
            subjectId: 'math',
            isCorrect: true,
            rewardStars: 2,
          );
      expect(c.read(childProgressProvider('k1')).stars, 2);

      // Yangi konteyner = ilovani qayta ochish.
      final c2 = makeContainer(t.db, clock: clock);
      addTearDown(c2.dispose);
      expect(c2.read(childProgressProvider('k1')).stars, 2);
    });
  });

  group('Sessiya va kunlik limit', () {
    test('vaqt yig\'iladi va limit tugaganda to\'xtaydi', () async {
      final p = await c.read(profilesProvider.notifier).create(
            name: 'Muhammadjon',
            age: 4,
            avatar: '🐻',
          );
      await c.read(profilesProvider.notifier).updateProfile(p.copyWith(dailyLimitMinutes: 1));

      final session = c.read(sessionProvider.notifier);
      await session.start(p.id);
      expect(c.read(sessionProvider).running, isTrue);
      expect(c.read(childProgressProvider(p.id)).streak, 1);

      clock.advance(const Duration(seconds: 30));
      await session.flush();
      expect(c.read(childProgressProvider(p.id)).secondsOn(clock.now), 30);
      expect(c.read(sessionProvider).limitReached, isFalse);

      clock.advance(const Duration(seconds: 30));
      await session.flush();
      expect(c.read(sessionProvider).limitReached, isTrue);
      expect(c.read(sessionProvider).running, isFalse);

      // Qayta kirishga urinish — limit hali ham tugagan.
      await session.stop();
      await session.start(p.id);
      expect(c.read(sessionProvider).limitReached, isTrue);

      // Ertasi kuni yana o'ynash mumkin.
      await session.stop();
      clock.advance(const Duration(days: 1));
      await session.start(p.id);
      expect(c.read(sessionProvider).limitReached, isFalse);
      expect(c.read(childProgressProvider(p.id)).streak, 2);
    });

    test('ilova fonda qolib ketsa bir qadamda ko\'pi bilan 60 s qo\'shiladi', () async {
      final p = await c.read(profilesProvider.notifier).create(
            name: 'Azamjon',
            age: 6,
            avatar: '🦁',
          );
      final session = c.read(sessionProvider.notifier);
      await session.start(p.id);
      clock.advance(const Duration(hours: 2));
      await session.flush();
      expect(c.read(childProgressProvider(p.id)).secondsOn(clock.now), SessionNotifier.maxStepSeconds);
    });

    test('pauza vaqtida vaqt hisoblanmaydi', () async {
      final p = await c.read(profilesProvider.notifier).create(
            name: 'Azamjon',
            age: 6,
            avatar: '🦁',
          );
      final session = c.read(sessionProvider.notifier);
      await session.start(p.id);
      clock.advance(const Duration(seconds: 20));
      await session.pause();
      clock.advance(const Duration(minutes: 10));
      session.resume();
      clock.advance(const Duration(seconds: 10));
      await session.flush();
      expect(c.read(childProgressProvider(p.id)).secondsOn(clock.now), 30);
    });

    test('limitni oshirish sessiyani qayta ochadi', () async {
      final n = c.read(profilesProvider.notifier);
      final p = await n.create(name: 'Azamjon', age: 6, avatar: '🦁');
      await n.updateProfile(p.copyWith(dailyLimitMinutes: 1));
      final session = c.read(sessionProvider.notifier);
      await session.start(p.id);
      clock.advance(const Duration(seconds: 60));
      await session.flush();
      expect(c.read(sessionProvider).limitReached, isTrue);

      await n.updateProfile(p.copyWith(dailyLimitMinutes: 20));
      session.recheckLimit();
      expect(c.read(sessionProvider).limitReached, isFalse);
      expect(c.read(sessionProvider).running, isTrue);
    });
  });

  group('Ota-ona PIN', () {
    test('PIN almashtiriladi va saqlanadi', () async {
      final s = c.read(settingsProvider.notifier);
      expect(c.read(settingsProvider).parentPin, '1234');
      final bad = await s.changePin(oldPin: '0000', newPin: '5678', confirmPin: '5678');
      expect(bad, PinChangeResult.wrongOldPin);
      expect(c.read(settingsProvider).parentPin, '1234');

      final ok = await s.changePin(oldPin: '1234', newPin: '5678', confirmPin: '5678');
      expect(ok, PinChangeResult.success);
      expect(t.db.getSettings().parentPin, '5678');
    });
  });
  group('Kunlik dars va yutuqlar', () {
    ExerciseResult r(String topic, String concept, bool ok, {bool retry = false}) =>
        ExerciseResult(topicId: topic, concept: concept, firstTry: ok, signature: concept.hashCode, retry: retry);

    test('kunlik dars: mavzular hisobga olinadi, xato takrorlash navbatiga tushadi', () async {
      final n = c.read(progressProvider.notifier);
      final p = await n.completeDailyLesson('a', [
        r('math4.count_1_3', 'n:3', true),
        r('math4.count_1_3', 'n:4', false),
        r('english4.animals', 'cat', true),
        // Shu darsning o'zida qayta so'ralgan — mastery va navbatga ta'sir qilmaydi.
        r('math4.count_1_3', 'n:4', true, retry: true),
      ]);
      expect(p.dailyLessons, 1);
      expect(p.completedLessons, 1);
      expect(p.dailyDoneOn(clock.now), isTrue);
      expect(p.skillOf('math4.count_1_3').lessons, 1);
      expect(p.skillOf('math4.count_1_3').attempts, 2);
      expect(p.skillOf('math4.count_1_3').firstTryCorrect, 1);
      expect(p.skillOf('english4.animals').started, isTrue);
      expect(p.reviews.keys.toList(), ['math4.count_1_3|n:4']);
      expect(p.recentOf('math4.count_1_3').length, 2);
      expect(p.counter('perfect_lesson'), 0);
      // Bazaga yozilgan.
      expect(t.db.getAllProgress()['a']!.dailyLessons, 1);
    });

    test('xatosiz kunlik dars — "perfect" hisoblagichi; medallar bir marta beriladi', () async {
      final n = c.read(progressProvider.notifier);
      await n.completeDailyLesson('a', [r('math4.count_1_3', 'n:1', true), r('logic4.odd', 'x', true)]);
      expect(n.of('a').counter('perfect_lesson'), 1);
      final medals = await n.awardMedals('a');
      expect(medals.map((m) => m.id).toSet(), {'first_lesson', 'daily_1', 'perfect'});
      expect(n.of('a').medals.toSet(), {'first_lesson', 'daily_1', 'perfect'});
      expect(await n.awardMedals('a'), isEmpty);
    });

    test('ertasi kuni takrorlash to‘g‘ri bajarilsa keyingi bosqichga o‘tadi', () async {
      final n = c.read(progressProvider.notifier);
      await n.recordReviews('a', [r('math4.count_1_3', 'n:4', false)]);
      expect(n.of('a').reviews.values.single.stage, 0);
      clock.advance(const Duration(days: 1));
      await n.recordReviews('a', [r('math4.count_1_3', 'n:4', true)]);
      expect(n.of('a').reviews.values.single.stage, 1);
    });

    test('sovg‘a qutisi faqat yulduz yetganda ochiladi', () async {
      final n = c.read(progressProvider.notifier);
      expect(await n.openGift('a'), isNull);
      await n.update('a', (p) => p.addStars(35));
      final gift = await n.openGift('a');
      expect(gift, isNotNull);
      expect(n.of('a').giftsOpened, 1);
      expect(await n.openGift('a'), isNull);
    });

    test('yutuq hisoblagichi (shaxmat g‘alabasi, puzzle)', () async {
      final n = c.read(progressProvider.notifier);
      await n.addCounter('a', 'chess_win');
      await n.addCounter('a', 'puzzle_25');
      final medals = await n.awardMedals('a');
      expect(medals.map((m) => m.id).toSet(), containsAll(['chess_win', 'puzzle_master']));
    });
  });
}
