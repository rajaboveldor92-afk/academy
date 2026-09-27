import 'dart:math';

import 'package:academy/core/providers.dart';
import 'package:academy/database/seed_data.dart';
import 'package:academy/features/home/achievements_screen.dart';
import 'package:academy/features/home/home_screen.dart';
import 'package:academy/features/home/subject_screen.dart';
import 'package:academy/features/lesson/lesson_screen.dart';
import 'package:academy/features/profiles/profiles_controller.dart';
import 'package:academy/features/session/progress_controller.dart';
import 'package:academy/learning/content/content_provider.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/rewards.dart';
import 'package:academy/learning/ui/choice_view.dart';
import 'package:academy/learning/ui/option_card.dart';
import 'package:academy/models/subject.dart';
import 'package:academy/router/app_router.dart';
import 'package:academy/services/audio_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

/// Fan → mavzular → dars oqimi (haqiqiy kontent bilan).
void main() {
  TestDb? t;
  late ContentRepository content;
  late SilentAudioService audio;

  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    content = await ContentRepository.load();
  });

  tearDown(() async {
    await t?.dispose();
    t = null;
  });

  Future<ProviderContainer> setup(WidgetTester tester, String childId) async {
    await tester.runAsync(() async {
      t = await TestDb.open();
      await SeedData.ensureSeeded(t!.db);
    });
    tester.view.physicalSize = const Size(1080, 2100);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    final container = ProviderContainer(overrides: [
      databaseProvider.overrideWithValue(t!.db),
      audioServiceProvider.overrideWithValue(audio = SilentAudioService()),
      // Kontent oldindan yuklangan (test muhitida aktivlarni fon rejimida o'qish sekin).
      contentProvider.overrideWith((ref) => content),
    ]);
    addTearDown(container.dispose);
    container.read(activeChildIdProvider.notifier).select(childId);
    return container;
  }

  Future<void> pumpUntil(WidgetTester tester, Finder f) async {
    for (var i = 0; i < 50 && f.evaluate().isEmpty; i++) {
      await tester.runAsync(() => Future<void>.delayed(const Duration(milliseconds: 20)));
      await tester.pump(const Duration(milliseconds: 50));
    }
  }

  testWidgets('Muhammadjon: matematika mavzulari va "Davom etamiz"', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(
        home: SubjectScreen(subject: Subject.math),
        onGenerateRoute: AppRouter.onGenerateRoute,
      ),
    ));
    await pumpUntil(tester, find.byKey(const Key('continue_topic')));
    expect(find.byKey(const Key('continue_topic')), findsOneWidget);
    expect(find.text('Bir va ko‘p'), findsWidgets);
    // Kichik yoshda mavzu kodi (M1) ko'rsatilmaydi.
    expect(find.text('M1'), findsNothing);
  });

  testWidgets('Azamjon: mantiq mavzularida kodlar ko‘rinadi', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(
        home: SubjectScreen(subject: Subject.logic),
        onGenerateRoute: AppRouter.onGenerateRoute,
      ),
    ));
    await pumpUntil(tester, find.byKey(const Key('continue_topic')));
    expect(find.text('L1'), findsOneWidget);
  });

  testWidgets('Xotira fani: mavzular ochiladi', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: SubjectScreen(subject: Subject.memory), onGenerateRoute: AppRouter.onGenerateRoute),
    ));
    await pumpUntil(tester, find.byKey(const Key('continue_topic')));
    expect(find.byKey(const Key('continue_topic')), findsOneWidget);
    expect(find.text('X1'), findsOneWidget);
  });

  testWidgets('Ota-ona bilan: faoliyat kartasi va "Bajardik!" tugmasi', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'family4.life', random: Random(1))),
    ));
    await pumpUntil(tester, find.byKey(const ValueKey('activity_done')));
    expect(find.byKey(const ValueKey('activity_done')), findsOneWidget);
    expect(find.text('Bajardik!'), findsOneWidget);
  });

  testWidgets('Dars ochiladi: ko‘rsatma, 🔊 tugma va variantlar', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'math4.count_1_3', random: Random(5))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
    expect(find.byKey(const Key('lesson_instruction')), findsOneWidget);
    expect(find.byKey(const Key('lesson_speak')), findsOneWidget);
  });

  testWidgets('Azamjon: o‘zbek tili mavzulari (U1…U14)', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(
        home: SubjectScreen(subject: Subject.uzbek),
        onGenerateRoute: AppRouter.onGenerateRoute,
      ),
    ));
    await pumpUntil(tester, find.byKey(const Key('continue_topic')));
    expect(find.byKey(const Key('continue_topic')), findsOneWidget);
    expect(find.text('U1'), findsOneWidget);
  });

  testWidgets('Yozish darsi: barmoq bilan yozish maydoni ochiladi', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'writing6.letters', random: Random(2))),
    ));
    await pumpUntil(tester, find.byKey(const ValueKey('trace_area')));
    expect(find.byKey(const ValueKey('trace_area')), findsOneWidget);
    expect(find.byKey(const Key('lesson_instruction')), findsOneWidget);
  });

  testWidgets('O‘zbek tili darsi: gap tuzish (bo‘laklar) ochiladi', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'uzbek6.build_sentence', random: Random(2))),
    ));
    await pumpUntil(tester, find.byKey(const ValueKey('tile_0')));
    expect(find.byKey(const ValueKey('slot_0')), findsOneWidget);
  });

  testWidgets('English darsi: ko‘rsatma inglizcha aytiladi, o‘zbekcha yordamchi bor', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'english4.animals', random: Random(3))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
    expect(find.text('Listen and find'), findsOneWidget);
    expect(find.byKey(const Key('lesson_instruction_uz')), findsOneWidget);
    expect(audio.log.any((l) => l.startsWith('speak:en:Find the ')), isTrue, reason: audio.log.join('\n'));
  });

  testWidgets('Русский darsi: ruscha ovoz', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'russian6.alphabet', random: Random(3))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
    expect(audio.log.any((l) => l.startsWith('speak:ru:Найди букву')), isTrue, reason: audio.log.join('\n'));
  });

  testWidgets('3 tilda: so‘zlar uch tilda ketma-ket aytiladi', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'trilingual4.fruits', random: Random(3))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
    final parts = audio.log.where((l) => l.startsWith('parts:')).toList();
    expect(parts, isNotEmpty, reason: audio.log.join('\n'));
    expect(parts.first.contains('|ru:') && parts.first.contains('|en:') && parts.first.endsWith('|uz:Qaysi rasm?'), isTrue,
        reason: parts.first);
  });
  testWidgets('Bosh sahifa: ▶ BUGUNGI DARSim kunlik aralash darsni ochadi', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: HomeScreen(), onGenerateRoute: AppRouter.onGenerateRoute),
    ));
    await pumpUntil(tester, find.byKey(const Key('daily_lesson_button')));
    expect(find.text('BUGUNGI DARSim'), findsOneWidget);
    expect(find.text('6 ta qiziqarli mashq'), findsOneWidget);
    await tester.tap(find.byKey(const Key('daily_lesson_button')));
    await pumpUntil(tester, find.byKey(const Key('lesson_subject')));
    // Kunlik darsda har bir mashq ustida fan nomi ko'rinadi.
    expect(find.byKey(const Key('lesson_subject')), findsOneWidget);
    expect(find.byKey(const Key('lesson_speak')), findsOneWidget);
  });

  testWidgets('Bosh sahifa: bugungi dars bajarilgani ko‘rsatiladi', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.runAsync(() => c.read(progressProvider.notifier).completeDailyLesson('azamjon', const []));
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: HomeScreen(), onGenerateRoute: AppRouter.onGenerateRoute),
    ));
    await pumpUntil(tester, find.byKey(const Key('daily_lesson_subtitle')));
    expect(find.text('Bugun bajarding! Yana bir marta?'), findsOneWidget);
  });

  testWidgets('Xato qilingan mashq shu darsda qayta so‘raladi (dars bittaga uzayadi)', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'math4.count_1_3', random: Random(5))),
    ));
    await pumpUntil(tester, find.byType(ChoiceExerciseView));
    final ex = tester.widget<ChoiceExerciseView>(find.byType(ChoiceExerciseView)).exercise;
    final n = ex.options.length;
    double progressValue() => tester.widget<LinearProgressIndicator>(find.byType(LinearProgressIndicator)).value!;
    expect(progressValue(), 0);
    await tester.tap(find.byType(OptionCard).at((ex.correctIndex + 1) % n));
    await tester.pump();
    await tester.tap(find.byType(OptionCard).at(ex.correctIndex));
    await tester.pump();
    // 6 ta mashq + 1 ta qayta so'rash; birinchisi bajarildi.
    expect(progressValue(), closeTo(1 / 7, 0.0001));
    // Javob bazaga yozilib bo'lishini kutamiz (test oxirida baza yopiladi).
    for (var i = 0; i < 10; i++) {
      await tester.runAsync(() => Future<void>.delayed(const Duration(milliseconds: 20)));
      await tester.pump(const Duration(milliseconds: 20));
    }
    expect(c.read(childProgressProvider('muhammadjon')).wrongAnswers, 1, reason: 'birinchi urinishda xato');
    expect(c.read(childProgressProvider('muhammadjon')).scoreOf('math').total, 1);
  });

  testWidgets('Yutuqlarim: bog‘, sovg‘a qutisi, medallar va kuboklar', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.runAsync(() => c.read(progressProvider.notifier).update(
          'muhammadjon',
          (p) => p.addStars(Rewards.starsPerGift + 5).completeLesson().completeLesson().addMedal('first_lesson'),
        ));
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: AchievementsScreen()),
    ));
    await pumpUntil(tester, find.byKey(const Key('garden')));
    expect(find.descendant(of: find.byKey(const Key('garden')), matching: find.text('🌱')), findsOneWidget);

    // Sovg'a qutisi: har doim bir xil tartibda (tasodifiy "loot box" yo'q).
    await tester.tap(find.byKey(const Key('open_gift')));
    await pumpUntil(tester, find.byKey(const Key('gift_dialog')));
    expect(find.text(Rewards.collection.first.name), findsOneWidget);
    await tester.tap(find.byKey(const Key('gift_ok')));
    await pumpUntil(tester, find.byKey(const Key('gift_progress')));
    expect(find.byKey(const Key('open_gift')), findsNothing);
    expect(c.read(childProgressProvider('muhammadjon')).giftsOpened, 1);

    await tester.scrollUntilVisible(find.byKey(const ValueKey('medal_first_lesson')), 300, scrollable: find.byType(Scrollable).first);
    expect(find.text('Birinchi dars'), findsOneWidget);
    await tester.scrollUntilVisible(find.byKey(const ValueKey('cup_math')), 300, scrollable: find.byType(Scrollable).first);
    expect(find.byKey(const ValueKey('cup_math')), findsOneWidget);
  });
}
