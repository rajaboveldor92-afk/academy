import 'dart:math';

import 'package:academy/core/providers.dart';
import 'package:academy/database/seed_data.dart';
import 'package:academy/features/home/home_screen.dart';
import 'package:academy/features/lesson/lesson_screen.dart';
import 'package:academy/features/parent/child_settings_screen.dart';
import 'package:academy/features/parent/parent_home_screen.dart';
import 'package:academy/features/parent/settings_controller.dart';
import 'package:academy/features/profiles/profiles_controller.dart';
import 'package:academy/l10n/lang_providers.dart';
import 'package:academy/l10n/tr.dart';
import 'package:academy/learning/content/content_provider.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/content/number_words.dart';
import 'package:academy/learning/ui/choice_view.dart';
import 'package:academy/learning/ui/option_card.dart';
import 'package:academy/models/subject.dart';
import 'package:academy/router/app_router.dart';
import 'package:academy/services/audio_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

/// Har bir bolaga alohida til: bola ekranlari va mashqlar bolaning tilida,
/// ota-ona bo'limi — umumiy ilova tilida.
void main() {
  TestDb? t;
  late ContentRepository content;
  late SilentAudioService audio;
  final cyrillic = RegExp('[а-яА-ЯёЁ]');

  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    content = await ContentRepository.load();
  });

  tearDown(() async {
    await t?.dispose();
    t = null;
  });

  Future<ProviderContainer> setup(WidgetTester tester, String childId, {String lang = 'ru'}) async {
    await tester.runAsync(() async {
      t = TestDb.memory();
      await SeedData.ensureSeeded(t!.db);
      final p = t!.db.getProfile(childId)!;
      await t!.db.saveProfile(p.copyWith(language: lang));
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

  testWidgets('Ruscha profil: bosh sahifa ruscha, salom qurilma ovozida', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: HomeScreen(), onGenerateRoute: AppRouter.onGenerateRoute),
    ));
    await pumpUntil(tester, find.byKey(const Key('daily_lesson_button')));
    expect(find.text('УРОК ДНЯ'), findsOneWidget);
    expect(find.text('6 интересных заданий'), findsOneWidget);
    expect(find.text('Muhammadjon, добро пожаловать!'), findsOneWidget);
    expect(find.text(Subject.math.titleIn('ru')), findsWidgets);
    expect(audio.log, contains('speak:ru:Muhammadjon, добро пожаловать! Готов играть и учиться?'));
    expect(audio.log.any((l) => l.contains('clip:')), isFalse, reason: audio.log.join('\n'));
  });

  testWidgets('Ruscha profil: matematika darsi, dalda va maqtov ruscha', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'math4.count_1_3', random: Random(5))),
    ));
    await pumpUntil(tester, find.byType(ChoiceExerciseView));
    final ex = tester.widget<ChoiceExerciseView>(find.byType(ChoiceExerciseView)).exercise;
    expect(ex.speechLang, 'ru');
    expect(tester.widget<Text>(find.byKey(const Key('lesson_instruction'))).data, ex.instruction.ru);
    // Ko'rsatma bolaning tilida — qo'shimcha tarjima qatori kerak emas.
    expect(find.byKey(const Key('lesson_instruction_uz')), findsNothing);

    final n = ex.options.length;
    await tester.tap(find.byType(OptionCard).at((ex.correctIndex + 1) % n));
    await tester.pump();
    expect(audio.log, contains('encourage:ru'));
    await tester.tap(find.byType(OptionCard).at(ex.correctIndex));
    await tester.pump();
    final answer = ex.meta['answer'] as int;
    final counted = [for (var i = 1; i <= answer; i++) 'ru:${NumberWords.word(i, 'ru')}'].join('|');
    expect(audio.log, contains('parts:$counted|ru:Правильно!'));
    expect(find.text('Правильно!'), findsOneWidget);
    expect(audio.log.any((l) => l.contains('clip:')), isFalse, reason: audio.log.join('\n'));
  });

  testWidgets('Ruscha profil: o‘zbek tili darsida ko‘rsatma o‘zbekcha, tarjimasi ruscha', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'uzbek6.build_sentence', random: Random(2))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
    final helper = tester.widget<Text>(find.byKey(const Key('lesson_instruction_uz'))).data!;
    expect(cyrillic.hasMatch(helper), isTrue, reason: helper);
    final main = tester.widget<Text>(find.byKey(const Key('lesson_instruction'))).data!;
    expect(cyrillic.hasMatch(main), isFalse, reason: main);
  });

  testWidgets('Ruscha profil: English darsi — "Слушай внимательно." va inglizcha ko‘rsatma', (tester) async {
    final c = await setup(tester, 'muhammadjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen(topicId: 'english4.animals', random: Random(3))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_instruction')));
    expect(find.text('Listen and find'), findsOneWidget);
    final helper = tester.widget<Text>(find.byKey(const Key('lesson_instruction_uz'))).data!;
    expect(cyrillic.hasMatch(helper), isTrue, reason: helper);
    expect(audio.log.any((l) => l.startsWith('parts:ru:Слушай внимательно.|en:Find the ')), isTrue, reason: audio.log.join('\n'));
  });

  testWidgets('Inglizcha profil: kunlik dars inglizcha', (tester) async {
    final c = await setup(tester, 'azamjon', lang: 'en');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(home: LessonScreen.daily(random: Random(4))),
    ));
    await pumpUntil(tester, find.byKey(const Key('lesson_subject')));
    final label = tester.widget<Text>(find.byKey(const Key('lesson_subject'))).data!;
    final subject = Subject.values.firstWhere((s) => label.contains(s.titleIn('en')));
    expect(label, contains(subject.emoji));
  });

  testWidgets('Ota-ona: bola tili va umumiy ilova tili tanlanadi', (tester) async {
    final c = await setup(tester, 'azamjon', lang: 'uz');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: ChildSettingsScreen(childId: 'azamjon')),
    ));
    await tester.pump();
    expect(find.text('Ilova tili (bola ekranlari va mashqlar)'), findsOneWidget);
    await tester.tap(find.byKey(const Key('child_lang_ru')));
    await tester.pump();
    await tester.pump();
    expect(c.read(profilesProvider).firstWhere((p) => p.id == 'azamjon').language, 'ru');
    expect(t!.db.getProfile('azamjon')!.language, 'ru');

    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: MaterialApp(
        builder: (context, child) => Consumer(
          builder: (context, ref, _) => LangScope(lang: ref.watch(appLangProvider), child: child!),
        ),
        home: const ParentHomeScreen(),
        onGenerateRoute: AppRouter.onGenerateRoute,
      ),
    ));
    // Baland ekran: sozlamalar bo'limi aylantirmasdan ko'rinadi.
    tester.view.physicalSize = const Size(1080, 8000);
    await tester.pumpAndSettle();
    expect(find.text('Bolalar'), findsOneWidget);
    await tester.ensureVisible(find.byKey(const Key('app_lang_en')));
    await tester.pumpAndSettle();
    await tester.tap(find.byKey(const Key('app_lang_en')));
    await tester.pump();
    await tester.pump();
    expect(c.read(settingsProvider).appLanguage, 'en');
    expect(find.text('Parents'), findsOneWidget);
    expect(find.text('Settings'), findsWidgets);
  });
}
