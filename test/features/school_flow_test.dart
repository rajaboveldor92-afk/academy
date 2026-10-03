import 'dart:math';

import 'package:academy/core/providers.dart';
import 'package:academy/database/seed_data.dart';
import 'package:academy/features/home/home_screen.dart';
import 'package:academy/features/home/subject_screen.dart';
import 'package:academy/models/subject.dart';
import 'package:academy/learning/ui/choice_view.dart';
import 'package:academy/learning/ui/option_card.dart';
import 'package:academy/features/lesson/lesson_screen.dart';
import 'package:academy/features/profiles/profiles_controller.dart';
import 'package:academy/learning/content/content_provider.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/ui/input_view.dart';
import 'package:academy/router/app_router.dart';
import 'package:academy/services/audio_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

/// Maktab o'quvchisi (Jasmina, 3-sinf; Akramjon, 5-sinf): sinf dasturi, qoida → mashq, javobni yozish.
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

  Future<ProviderContainer> setup(WidgetTester tester, String childId, {int? grade}) async {
    await tester.runAsync(() async {
      t = TestDb.memory();
      await SeedData.ensureSeeded(t!.db);
      if (grade != null) {
        await t!.db.saveProfile(t!.db.getProfile(childId)!.copyWith(grade: grade, age: grade + 6));
      }
    });
    tester.view.physicalSize = const Size(1080, 2100);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    final container = ProviderContainer(overrides: [
      databaseProvider.overrideWithValue(t!.db),
      audioServiceProvider.overrideWithValue(audio = SilentAudioService()),
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

  testWidgets('Jasmina (3-sinf): bosh sahifada sinfi va 3-sinf fanlari', (tester) async {
    final c = await setup(tester, 'jasmina');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: HomeScreen(), onGenerateRoute: AppRouter.onGenerateRoute),
    ));
    await pumpUntil(tester, find.byKey(const Key('home_grade')));
    expect(find.text('3-sinf'), findsOneWidget);
    expect(find.byKey(const Key('tile_math')), findsOneWidget);
    // Maktabgacha fanlar maktab o'quvchisiga ko'rsatilmaydi.
    expect(find.byKey(const Key('tile_trilingual')), findsNothing);
    expect(find.byKey(const Key('tile_motor')), findsNothing);
  });

  for (final child in ['jasmina', 'akramjon']) {
    for (final subject in [Subject.logic, Subject.english, Subject.russian, Subject.onatili, Subject.reading, Subject.science, Subject.informatics]) {
      testWidgets('$child ${subject.id}: fan → qoida → mashq', (tester) async {
        final c = await setup(tester, child);
        await tester.pumpWidget(UncontrolledProviderScope(container: c,
          child: MaterialApp(home: SubjectScreen(subject: subject), onGenerateRoute: AppRouter.onGenerateRoute)));
        await pumpUntil(tester, find.byKey(const Key('continue_topic')));
        expect(find.byKey(const Key('continue_topic')), findsOneWidget);
        await tester.tap(find.byKey(const Key('continue_topic')));
        await pumpUntil(tester, find.byKey(const Key('theory_start')));
        await tester.tap(find.byKey(const Key('theory_start')));
        await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
        expect(find.byKey(const Key('lesson_instruction')), findsOneWidget);
        expect(tester.takeException(), isNull);
      });
    }
  }

  for (final child in ['jasmina', 'akramjon']) {
    testWidgets('$child: Technology direction is shown on the subject page', (tester) async {
      final c = await setup(tester, child);
      await tester.pumpWidget(UncontrolledProviderScope(container: c,
        child: const MaterialApp(home: SubjectScreen(subject: Subject.technology))));
      await pumpUntil(tester, find.byKey(const Key('technology_track_banner')));
      expect(find.text(child == 'jasmina' ? 'Servis va hunarmandchilik' : 'Texnik loyihalash'), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  }

  for (final grade in [2, 8]) {
    testWidgets('g$grade new reading: small phone, theory, answer and explanation', (tester) async {
      final c = await setup(tester, 'akramjon', grade: grade);
      tester.view.physicalSize = const Size(360, 640);
      tester.view.devicePixelRatio = 1;
      await tester.pumpWidget(UncontrolledProviderScope(container: c,
        child: MaterialApp(home: LessonScreen(topicId: 'reading_g$grade.unit1', random: Random(8)))));
      await pumpUntil(tester, find.byKey(const Key('theory_start')));
      await tester.tap(find.byKey(const Key('theory_start')));
      await pumpUntil(tester, find.byType(ChoiceExerciseView));
      final ex = tester.widget<ChoiceExerciseView>(find.byType(ChoiceExerciseView)).exercise;
      final correct = find.byWidgetPredicate((w) => w is OptionCard && w.option.text == ex.correctOption!.text);
      await tester.ensureVisible(correct);
      await tester.tap(correct);
      await tester.pump();
      await pumpUntil(tester, find.byKey(const Key('lesson_explanation')));
      expect(find.byKey(const Key('lesson_explanation')), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  }

  testWidgets('Small phone: reading text and long answers remain usable', (tester) async {
    final c = await setup(tester, 'akramjon');
    tester.view.physicalSize = const Size(360, 640);
    tester.view.devicePixelRatio = 1;
    await tester.pumpWidget(UncontrolledProviderScope(container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'reading_g5.understand', random: Random(8)))));
    await pumpUntil(tester, find.byKey(const Key('theory_start')));
    await tester.tap(find.byKey(const Key('theory_start')));
    await pumpUntil(tester, find.byType(ChoiceExerciseView));
    expect(find.byType(ChoiceExerciseView), findsOneWidget);
    expect(tester.takeException(), isNull);
    final ex = tester.widget<ChoiceExerciseView>(find.byType(ChoiceExerciseView)).exercise;
    final correct = find.byWidgetPredicate((w) => w is OptionCard && w.option.text == ex.correctOption!.text);
    await tester.ensureVisible(correct);
    await tester.tap(correct);
    await tester.pump();
    await pumpUntil(tester, find.byKey(const Key('lesson_explanation')));
    expect(find.byKey(const Key('lesson_explanation')), findsOneWidget);
    expect(tester.takeException(), isNull);
  });

  testWidgets('Maktab darsi: avval qoida, keyin mashq; ko‘rsatma avtomatik aytilmaydi', (tester) async {
    final c = await setup(tester, 'jasmina');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'math_g3.add', random: Random(2))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_theory_card')));
    expect(find.byKey(const Key('lesson_theory_card')), findsOneWidget);
    expect(find.textContaining('Ustun usulida qo‘shish'), findsOneWidget);
    await tester.tap(find.byKey(const Key('theory_start')));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 50));
    expect(find.byKey(const Key('lesson_instruction')), findsOneWidget);
    // Qoidani dars davomida ham ochish mumkin.
    expect(find.byKey(const Key('lesson_theory')), findsOneWidget);
    expect(audio.log.where((l) => l.startsWith('speak:') || l.startsWith('parts:')), isEmpty, reason: audio.log.join('\n'));
  });

  testWidgets('Akramjon (5-sinf): javobni klaviaturada yozish', (tester) async {
    final c = await setup(tester, 'akramjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'math_g5.frac_mul', random: Random(3))),
    ));
    await pumpUntil(tester, find.byKey(const Key('theory_start')));
    await tester.tap(find.byKey(const Key('theory_start')));
    await tester.pump();
    await pumpUntil(tester, find.byType(InputExerciseView));
    final ex = tester.widget<InputExerciseView>(find.byType(InputExerciseView)).exercise;
    for (final ch in ex.input!.answer.split('')) {
      await tester.tap(find.byKey(ValueKey('key_$ch')));
      await tester.pump();
    }
    await tester.tap(find.byKey(const ValueKey('input_check')));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 50));
    expect(c.read(profilesProvider).firstWhere((p) => p.id == 'akramjon').grade, 5);
    expect(find.byKey(const Key('lesson_explanation')), findsOneWidget);
  });
}
