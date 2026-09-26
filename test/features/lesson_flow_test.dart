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
      audioServiceProvider.overrideWithValue(SilentAudioService()),
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

  testWidgets('Hali kontenti yo‘q fan uchun xabar', (tester) async {
    final c = await setup(tester, 'azamjon');
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: SubjectScreen(subject: Subject.chess)),
    ));
    await pumpUntil(tester, find.text('Tez orada!'));
    expect(find.text('Tez orada!'), findsOneWidget);
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
}
