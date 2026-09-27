import 'dart:math';

import 'package:academy/core/providers.dart';
import 'package:academy/database/seed_data.dart';
import 'package:academy/features/home/subject_screen.dart';
import 'package:academy/features/lesson/lesson_screen.dart';
import 'package:academy/features/profiles/profiles_controller.dart';
import 'package:academy/learning/content/content_provider.dart';
import 'package:academy/learning/content/content_repository.dart';
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

  Future<ProviderContainer> setup(WidgetTester tester, String childId,
      {int? age, bool preload = true}) async {
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
      if (preload) contentProvider.overrideWith((ref) => content),
    ]);
    addTearDown(container.dispose);
    container.read(activeChildIdProvider.notifier).select(childId);
    if (age != null) {
      await tester.runAsync(() => container
          .read(profilesProvider.notifier)
          .updateProfile(
              container.read(activeProfileProvider)!.copyWith(age: age)));
    }
    return container;
  }

  Future<void> pumpUntil(WidgetTester tester, Finder f) async {
    for (var i = 0; i < 50 && f.evaluate().isEmpty; i++) {
      await tester.runAsync(
          () => Future<void>.delayed(const Duration(milliseconds: 20)));
      await tester.pump(const Duration(milliseconds: 50));
    }
  }

  for (final age in [3, 4, 5, 6, 7, 8]) {
    for (final subject in [Subject.math, Subject.logic]) {
      testWidgets('$age yosh ${subject.id}: haqiqiy asset → mavzu → dars',
          (tester) async {
        final c = await setup(tester, 'muhammadjon', age: age, preload: false);
        await tester.pumpWidget(UncontrolledProviderScope(
          container: c,
          child: MaterialApp(
              home: SubjectScreen(subject: subject),
              onGenerateRoute: AppRouter.onGenerateRoute),
        ));
        await pumpUntil(tester, find.byKey(const Key('continue_topic')));
        expect(find.text('Tez orada!'), findsNothing);
        expect(find.textContaining('$age yosh'), findsOneWidget);
        expect(find.byKey(const Key('continue_topic')), findsOneWidget);
        await tester.tap(find.byKey(const Key('continue_topic')));
        await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
        expect(find.byKey(const Key('lesson_instruction')), findsOneWidget);
        expect(tester.takeException(), isNull);
      });
    }
  }

  testWidgets('Yosh profil ichida o‘zgarsa, fan dasturi ham yangilanadi',
      (tester) async {
    final c = await setup(tester, 'muhammadjon', age: 3);
    await tester.pumpWidget(UncontrolledProviderScope(
        container: c,
        child: const MaterialApp(home: SubjectScreen(subject: Subject.math))));
    await pumpUntil(tester, find.textContaining('3 yosh'));
    expect(find.textContaining('3 yosh'), findsOneWidget);
    await tester.runAsync(() => c
        .read(profilesProvider.notifier)
        .updateProfile(c.read(activeProfileProvider)!.copyWith(age: 8)));
    await pumpUntil(tester, find.textContaining('8 yosh'));
    expect(find.textContaining('8 yosh'), findsOneWidget);
    expect(find.textContaining('3 yosh'), findsNothing);
  });

  testWidgets('Yuklash xatosi yashirilmaydi va qayta urinish kontentni ochadi',
      (tester) async {
    final c = await setup(tester, 'muhammadjon');
    var attempts = 0;
    c.updateOverrides([
      databaseProvider.overrideWithValue(t!.db),
      audioServiceProvider.overrideWithValue(SilentAudioService()),
      contentProvider.overrideWith((ref) {
        if (attempts++ == 0) throw StateError('test asset load failure');
        return content;
      }),
    ]);
    await tester.pumpWidget(UncontrolledProviderScope(
        container: c,
        child: const MaterialApp(home: SubjectScreen(subject: Subject.math))));
    await pumpUntil(tester, find.byKey(const Key('retry_content')));
    expect(find.text('Tez orada!'), findsNothing);
    expect(find.byKey(const Key('retry_content')), findsOneWidget);
    await tester.tap(find.byKey(const Key('retry_content')));
    await pumpUntil(tester, find.byKey(const Key('continue_topic')));
    expect(find.byKey(const Key('continue_topic')), findsOneWidget);
  });

  testWidgets('Muhammadjon: matematika mavzulari va "Davom etamiz"',
      (tester) async {
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

  testWidgets('Hali kontenti yo‘q fan uchun xabar', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: SubjectScreen(subject: Subject.memory)),
    ));
    await pumpUntil(tester, find.text('Tez orada!'));
    expect(find.text('Tez orada!'), findsOneWidget);
  });

  testWidgets('Dars ochiladi: ko‘rsatma, 🔊 tugma va variantlar',
      (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(
          home: LessonScreen(topicId: 'math4.count_1_3', random: Random(5))),
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
}
