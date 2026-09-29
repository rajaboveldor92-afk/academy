import 'package:academy/core/providers.dart';
import 'package:academy/database/seed_data.dart';
import 'package:academy/features/parent/child_report.dart';
import 'package:academy/features/parent/child_report_screen.dart';
import 'package:academy/features/session/progress_controller.dart';
import 'package:academy/learning/content/content_provider.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/mastery.dart';
import 'package:academy/learning/engine/spaced_repetition.dart';
import 'package:academy/models/child_progress.dart';
import 'package:academy/models/subject.dart';
import 'package:academy/services/audio_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

/// 9-bosqich: ota-ona uchun batafsil hisobot.
void main() {
  late ContentRepository content;
  final now = DateTime(2026, 9, 26, 18);

  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    content = await ContentRepository.load();
  });

  group('Hisobot hisob-kitobi', () {
    test('bo‘sh progress: barcha yoqilgan fanlar 0%, tavsiya bor', () {
      final profile = SeedData.muhammadjon(DateTime(2026));
      final r = ChildReport.build(profile: profile, progress: ChildProgress.empty(profile.id), content: content, now: now);
      expect(r.subjects.length, Subject.forProfile(profile).length);
      for (final s in r.subjects) {
        expect(s.mastery, 0, reason: s.subject.id);
        expect(s.accuracy, isNull);
        expect(s.topics.every((t) => t.topic.ageSuffix == '4'), isTrue);
        expect(s.current, isNotNull);
      }
      expect(r.accuracy, isNull);
      expect(r.reviewsDue, 0);
      expect(r.tips, isNotEmpty);
      expect(r.tips.first, contains('Bugungi dars'));
    });

    test('o‘chirilgan fan hisobotda ko‘rinmaydi; 6 yosh — 6 yosh dasturi', () {
      final profile = SeedData.azamjon(DateTime(2026)).copyWith(disabledSubjects: ['chess', 'russian']);
      final r = ChildReport.build(profile: profile, progress: ChildProgress.empty(profile.id), content: content, now: now);
      expect(r.subjects.any((s) => s.subject.id == 'chess' || s.subject.id == 'russian'), isFalse);
      expect(r.subjects.first.topics.first.topic.ageSuffix, '6');
    });

    test('egallangan va qiynalayotgan mavzular, fan foizi, takrorlash navbati', () {
      final profile = SeedData.muhammadjon(DateTime(2026));
      final topics = content.curriculum('math', '4')!.topics;
      final a = topics[0], b = topics[1];
      var p = ChildProgress.empty(profile.id)
          .withSkill(a.id, SkillStat(level: a.maxLevel, ema: 100, lessons: 5, lastPracticed: now, lastAccuracy: 100))
          .withSkill(b.id, SkillStat(level: 1, ema: 40, lessons: 2, lastPracticed: now, lastAccuracy: 40))
          .recordAnswer(subjectId: 'math', isCorrect: true, now: now)
          .recordAnswer(subjectId: 'math', isCorrect: true, now: now)
          .recordAnswer(subjectId: 'math', isCorrect: true, now: now)
          .recordAnswer(subjectId: 'math', isCorrect: false, now: now);
      var q = SpacedRepetition.record(const {}, topicId: b.id, concept: 'x', firstTry: false, now: now.subtract(const Duration(days: 1)));
      q = SpacedRepetition.record(q, topicId: b.id, concept: 'y', firstTry: false, now: now);
      p = p.withReviews(q);

      final r = ChildReport.build(profile: profile, progress: p, content: content, now: now);
      final math = r.subjects.firstWhere((s) => s.subject.id == 'math');
      expect(math.topics.first.status, TopicStatus.mastered);
      expect(math.topics[1].status, TopicStatus.needsHelp);
      expect(math.mastered, 1);
      expect(math.started, 2);
      expect(math.accuracy, 75);
      final expected = ((100 + const SkillStat(level: 1, ema: 40, lessons: 2).mastery(3)) / topics.length).round();
      expect(b.maxLevel, 3);
      expect(math.mastery, expected);
      expect(math.current!.topic.id, b.id);
      expect(r.strengths.map((t) => t.topic.id), [a.id]);
      expect(r.needsHelp.map((t) => t.topic.id), [b.id]);
      expect(r.reviewsDue, 1);
      expect(r.reviewsWeek, 1);
      expect(r.reviewsTotal, 2);
      expect(r.accuracy, 75);
      expect(r.tips.any((t) => t.contains(b.title.uz)), isTrue);
      expect(r.tips.any((t) => t.contains('takrorlash')), isTrue);
    });
  });

  testWidgets('Hisobot ekrani: tavsiyalar, takrorlash va fanlar (mavzular ochiladi)', (tester) async {
    TestDb? t;
    await tester.runAsync(() async {
      t = TestDb.memory();
      await SeedData.ensureSeeded(t!.db);
    });
    addTearDown(() => t?.dispose());
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    final c = ProviderContainer(overrides: [
      databaseProvider.overrideWithValue(t!.db),
      audioServiceProvider.overrideWithValue(SilentAudioService()),
      contentProvider.overrideWith((ref) => content),
    ]);
    addTearDown(c.dispose);
    final first = content.curriculum('math', '6')!.topics.first;
    final second = content.curriculum('math', '6')!.topics[1];
    await tester.runAsync(() => c.read(progressProvider.notifier).update(
          'azamjon',
          (p) => p.withSkill(first.id, SkillStat(level: first.maxLevel, ema: 100, lessons: 4, lastPracticed: DateTime.now(), lastAccuracy: 100)),
        ));
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: ChildReportScreen(childId: 'azamjon')),
    ));
    for (var i = 0; i < 20 && find.byKey(const Key('report_tips')).evaluate().isEmpty; i++) {
      await tester.pump(const Duration(milliseconds: 50));
    }
    expect(find.byKey(const Key('report_tips')), findsOneWidget);

    final list = find.byKey(const Key('report_list'));
    await tester.scrollUntilVisible(find.byKey(const Key('report_reviews')), 300, scrollable: find.descendant(of: list, matching: find.byType(Scrollable)).first);
    expect(find.byKey(const Key('report_reviews')), findsOneWidget);
    await tester.scrollUntilVisible(find.byKey(const ValueKey('report_subject_math')), 300, scrollable: find.descendant(of: list, matching: find.byType(Scrollable)).first);
    expect(find.byKey(const ValueKey('report_subject_line_math')), findsOneWidget);
    // Fan yopiq paytda uning mavzulari ro'yxati ko'rinmaydi.
    expect(find.byKey(ValueKey('report_topic_${second.id}')), findsNothing);
    await tester.tap(find.text(Subject.math.title));
    await tester.pumpAndSettle();
    expect(find.byKey(ValueKey('report_topic_${second.id}')), findsOneWidget);
    expect(find.byKey(ValueKey('report_topic_${first.id}')), findsWidgets);
  });

  testWidgets('Maktab o‘quvchisi: hisobotda nazorat ishlari baholari', (tester) async {
    TestDb? t;
    await tester.runAsync(() async {
      t = TestDb.memory();
      await SeedData.ensureSeeded(t!.db);
    });
    addTearDown(() => t?.dispose());
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    final c = ProviderContainer(overrides: [
      databaseProvider.overrideWithValue(t!.db),
      audioServiceProvider.overrideWithValue(SilentAudioService()),
      contentProvider.overrideWith((ref) => content),
    ]);
    addTearDown(c.dispose);
    final test1 = content.topic('math_g5.test1')!;
    final test2 = content.topic('math_g5.test2')!;
    await tester.runAsync(() => c.read(progressProvider.notifier).update(
          'akramjon',
          (p) => p
              .withSkill(test1.id, SkillStat(level: 2, ema: 95, lessons: 1, lastPracticed: DateTime.now(), lastAccuracy: 95))
              .withSkill(test2.id, SkillStat(level: 2, ema: 72, lessons: 1, lastPracticed: DateTime.now(), lastAccuracy: 72)),
        ));
    await tester.pumpWidget(UncontrolledProviderScope(
      container: c,
      child: const MaterialApp(home: ChildReportScreen(childId: 'akramjon')),
    ));
    for (var i = 0; i < 20 && find.byKey(const Key('report_tips')).evaluate().isEmpty; i++) {
      await tester.pump(const Duration(milliseconds: 50));
    }
    final list = find.byKey(const Key('report_list'));
    await tester.scrollUntilVisible(find.byKey(const Key('report_marks')), 300, scrollable: find.descendant(of: list, matching: find.byType(Scrollable)).first);
    expect(find.byKey(const Key('report_marks')), findsOneWidget);
    expect(find.text('O‘rtacha baho: 4,5'), findsOneWidget);
    expect(find.descendant(of: find.byKey(ValueKey('report_mark_${test1.id}')), matching: find.text('5')), findsOneWidget);
    expect(find.descendant(of: find.byKey(ValueKey('report_mark_${test2.id}')), matching: find.text('4')), findsOneWidget);
  });
}
