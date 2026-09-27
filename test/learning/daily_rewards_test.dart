import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/daily_planner.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/engine/mastery.dart';
import 'package:academy/learning/engine/rewards.dart';
import 'package:academy/learning/engine/spaced_repetition.dart';
import 'package:academy/models/child_progress.dart';
import 'package:flutter_test/flutter_test.dart';

/// 8-bosqich: kunlik dars, takrorlash (spaced repetition) va o'yinlashtirish.
void main() {
  late ContentRepository content;
  final day = DateTime(2026, 9, 26, 10);

  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    content = await ContentRepository.load();
  });

  group('Takrorlash navbati (spaced repetition)', () {
    test('xato → ertaga; to‘g‘ri takrorlash → 3 kun → 7 kun → o‘rganildi', () {
      var q = SpacedRepetition.record(const {}, topicId: 't', concept: 'c', firstTry: false, now: day);
      var item = q.values.single;
      expect(item.stage, 0);
      expect(item.due, DateTime(2026, 9, 27));
      expect(item.isDue(day), isFalse);
      expect(SpacedRepetition.due(q, day), isEmpty);

      final d1 = DateTime(2026, 9, 27, 9);
      expect(SpacedRepetition.due(q, d1).length, 1);
      q = SpacedRepetition.record(q, topicId: 't', concept: 'c', firstTry: true, now: d1);
      item = q.values.single;
      expect(item.stage, 1);
      expect(item.due, DateTime(2026, 9, 30));

      final d2 = DateTime(2026, 9, 30, 18);
      q = SpacedRepetition.record(q, topicId: 't', concept: 'c', firstTry: true, now: d2);
      item = q.values.single;
      expect(item.stage, 2);
      expect(item.due, DateTime(2026, 10, 7));

      q = SpacedRepetition.record(q, topicId: 't', concept: 'c', firstTry: true, now: DateTime(2026, 10, 8));
      expect(q, isEmpty, reason: '7 kunlik takrorlashdan keyin tushuncha o‘rganilgan');
    });

    test('muddatidan oldin to‘g‘ri javob navbatni o‘zgartirmaydi', () {
      final q = SpacedRepetition.record(const {}, topicId: 't', concept: 'c', firstTry: false, now: day);
      final same = SpacedRepetition.record(q, topicId: 't', concept: 'c', firstTry: true, now: day);
      expect(same.values.single.stage, 0);
      expect(same.values.single.due, DateTime(2026, 9, 27));
      // Navbatda bo'lmagan tushunchaga to'g'ri javob — hech narsa qo'shilmaydi.
      expect(SpacedRepetition.record(const {}, topicId: 't', concept: 'x', firstTry: true, now: day), isEmpty);
    });

    test('takrorlashda xato → yana ertasi kundan', () {
      var q = SpacedRepetition.record(const {}, topicId: 't', concept: 'c', firstTry: false, now: day);
      q = SpacedRepetition.record(q, topicId: 't', concept: 'c', firstTry: true, now: DateTime(2026, 9, 27));
      expect(q.values.single.stage, 1);
      q = SpacedRepetition.record(q, topicId: 't', concept: 'c', firstTry: false, now: DateTime(2026, 9, 30));
      expect(q.values.single.stage, 0);
      expect(q.values.single.due, DateTime(2026, 10, 1));
    });

    test('navbat hajmi cheklangan', () {
      var q = <String, ReviewItem>{};
      for (var i = 0; i < SpacedRepetition.maxItems + 15; i++) {
        q = SpacedRepetition.record(q, topicId: 't', concept: 'c$i', firstTry: false, now: day);
      }
      expect(q.length, SpacedRepetition.maxItems);
    });

    test('ReviewItem toMap/fromMap', () {
      final r = ReviewItem(topicId: 'a', concept: 'b|c', stage: 2, due: DateTime(2026, 10, 3));
      final back = ReviewItem.fromMap(r.toMap());
      expect(back.topicId, 'a');
      expect(back.concept, 'b|c');
      expect(back.stage, 2);
      expect(back.due, DateTime(2026, 10, 3));
      expect(back.key, r.key);
    });
  });

  group('Mastery: kunlik darsdagi mashq', () {
    test('daraja o‘zgarmaydi, mavzu "boshlangan" bo‘ladi', () {
      const s = SkillStat(level: 2, ema: 50, lessons: 3);
      final p = s.practiced(correct: 1, total: 1, now: day);
      expect(p.level, 2);
      expect(p.ema, closeTo(65, 0.001));
      expect(p.lessons, 4);
      expect(p.lastPracticed, day);
      final fresh = const SkillStat().practiced(correct: 1, total: 2, now: day);
      expect(fresh.started, isTrue);
      expect(fresh.level, 1);
      expect(fresh.ema, closeTo(25, 0.001));
      expect(identical(s.practiced(correct: 0, total: 0, now: day), s), isTrue);
    });
  });

  group('Yutuqlar', () {
    test('medallar: noyob id, emoji Android 9 da ko‘rinadi, faqat shartda beriladi', () {
      expect(Rewards.medals.map((m) => m.id).toSet().length, Rewards.medals.length);
      expect(Rewards.newMedals(ChildProgress.empty('a')), isEmpty);
      var p = ChildProgress.empty('a').completeLesson();
      expect(Rewards.newMedals(p).map((m) => m.id), ['first_lesson']);
      p = p.addMedal('first_lesson').completeDaily(day).addCounter('perfect_lesson');
      expect(Rewards.newMedals(p).map((m) => m.id).toSet(), {'daily_1', 'perfect'});
      expect(Rewards.medal('chess_win')!.earned(p.addCounter('chess_win')), isTrue);
      expect(Rewards.medal('puzzle_master')!.earned(p.addCounter('puzzle_9', 2)), isFalse);
      expect(Rewards.medal('puzzle_master')!.earned(p.addCounter('puzzle_9', 3)), isTrue);
      expect(Rewards.medal('puzzle_master')!.earned(p.addCounter('puzzle_25')), isTrue);
      for (final m in Rewards.medals) {
        expect(m.hint.trim(), isNotEmpty, reason: m.id);
        expect(m.title.trim(), isNotEmpty, reason: m.id);
      }
    });

    test('sovg‘a qutisi: tasodif yo‘q, har 30 yulduzga bittadan, tartib doim bir xil', () {
      var p = ChildProgress.empty('a').addStars(65);
      expect(Rewards.giftsAvailable(p), 2);
      expect(Rewards.starsToNextGift(p), 25);
      expect(Rewards.nextGift(p).emoji, Rewards.collection[0].emoji);
      p = p.openGift();
      expect(Rewards.giftsAvailable(p), 1);
      expect(Rewards.nextGift(p).emoji, Rewards.collection[1].emoji);
      p = p.openGift();
      expect(Rewards.giftsAvailable(p), 0);
      expect(Rewards.collected(p).map((c) => c.emoji), [Rewards.collection[0].emoji, Rewards.collection[1].emoji]);
      expect(Rewards.collection.map((c) => c.emoji).toSet().length, Rewards.collection.length);
    });

    test('o‘suvchi bog‘: har 2 darsda niholcha, darslar bilan o‘sadi', () {
      ChildProgress withLessons(int n) {
        var p = ChildProgress.empty('a');
        for (var i = 0; i < n; i++) {
          p = p.completeLesson();
        }
        return p;
      }

      expect(Rewards.garden(withLessons(1)), isEmpty);
      expect(Rewards.garden(withLessons(2)), ['🌱']);
      final g = Rewards.garden(withLessons(12));
      expect(g.length, 6);
      expect(g.first, isNot(anyOf('🌱', '🌿')), reason: 'eng birinchi o‘simlik ulg‘aygan');
      expect(g.last, '🌱');
      expect(Rewards.garden(withLessons(200)).length, Rewards.maxPlants);
    });

    test('Android 9 da ko‘rinmaydigan emoji yo‘q', () {
      const unsupported = ['🪜', '🫥', '🪙', '🪶', '🧍', '🧃', '🪑', '🧼', '🪥', '🪁', '🧅', '🧄', '🫐', '🦫', '🪴', '🛝', '🥱', '🫖', '🪟', '🟢', '🟠', '🟫', '🫧', '🪐', '🧊', '🪆'];
      final all = [
        ...Rewards.medals.map((m) => m.emoji),
        ...Rewards.collection.map((c) => c.emoji),
        for (var n = 0; n < 60; n += 2) ...Rewards.garden(ChildProgress(childId: 'a', completedLessons: n)),
      ];
      for (final e in all) {
        for (final bad in unsupported) {
          expect(e.contains(bad), isFalse, reason: e);
        }
      }
    });

    test('fan kubogi mavzularni egallashga qarab o‘sadi', () {
      var p = ChildProgress.empty('a');
      expect(Rewards.cup(p, content, 'math', 4), CupTier.none);
      final topics = content.curriculum('math', '4')!.topics;
      for (final t in topics) {
        p = p.withSkill(t.id, SkillStat(level: t.maxLevel, ema: 100, lessons: 3));
      }
      expect(Rewards.cup(p, content, 'math', 4), CupTier.gold);
      // Boshqa yosh dasturi alohida hisoblanadi.
      expect(Rewards.cup(p, content, 'math', 6), CupTier.none);
    });
  });

  group('▶ BUGUNGI DARSim (kunlik reja)', () {
    bool all(String _) => true;

    test('4 va 6 yosh: to‘liq, aralash, yoshga mos reja', () {
      for (final age in [4, 6]) {
        final plan = DailyPlanner.build(
          content: content,
          age: age,
          progress: ChildProgress.empty('a'),
          isEnabled: all,
          now: day,
          rng: Random(7),
        );
        expect(plan.length, DailyPlanner.sizeFor(age), reason: 'yosh $age');
        final suffix = age <= 5 ? '4' : '6';
        for (final it in plan) {
          expect(it.topic.ageSuffix, suffix);
          expect(DailyPlanner.skipGenerators.contains(it.topic.generator), isFalse, reason: it.topic.id);
          expect(ExerciseValidator.isPlayable(it.exercise), isTrue, reason: it.topic.id);
          expect(it.review, isFalse);
        }
        expect(plan.map((e) => e.topic.id).toSet().length, plan.length, reason: 'bir mavzu bir marta');
        expect(plan.map((e) => e.topic.subject).toSet().length, greaterThanOrEqualTo(age <= 5 ? 5 : 8));
      }
    });

    test('har kuni boshqa fandan boshlanadi', () {
      final firsts = <String>{};
      for (var d = 0; d < 6; d++) {
        final plan = DailyPlanner.build(
          content: content,
          age: 6,
          progress: ChildProgress.empty('a'),
          isEnabled: all,
          now: day.add(Duration(days: d)),
          rng: Random(d),
        );
        firsts.add(plan.first.topic.subject);
      }
      expect(firsts.length, greaterThanOrEqualTo(4));
    });

    test('ota-ona o‘chirgan fanlar kunlik darsga kirmaydi', () {
      final plan = DailyPlanner.build(
        content: content,
        age: 4,
        progress: ChildProgress.empty('a'),
        isEnabled: (s) => s != 'math' && s != 'english',
        now: day,
        rng: Random(3),
      );
      expect(plan, isNotEmpty);
      expect(plan.any((e) => e.topic.subject == 'math' || e.topic.subject == 'english'), isFalse);
    });

    test('vaqti kelgan takrorlashlar kiradi (boshqa ko‘rinishda), lekin darsning uchdan biridan oshmaydi', () {
      var queue = <String, ReviewItem>{};
      for (final id in ['math4.count_1_3', 'english4.animals', 'russian4.alphabet', 'logic4.odd']) {
        final t = content.topic(id)!;
        final ex = LessonBuilder.build(content: content, topic: t, level: 1, count: 1, age: 4, rng: Random(1)).single;
        queue = SpacedRepetition.record(queue, topicId: id, concept: ex.conceptKey, firstTry: false, now: day);
      }
      expect(queue, isNotEmpty);
      final progress = ChildProgress.empty('a').withReviews(queue);
      final tomorrow = day.add(const Duration(days: 1));
      final plan = DailyPlanner.build(content: content, age: 4, progress: progress, isEnabled: all, now: tomorrow, rng: Random(2));
      final reviews = plan.where((e) => e.review).toList();
      expect(reviews, isNotEmpty);
      expect(reviews.length, lessThanOrEqualTo(DailyPlanner.sizeFor(4) ~/ 3));
      expect(plan.first.review, isFalse, reason: 'dars yangi mashq bilan boshlanadi');
      expect(plan.length, DailyPlanner.sizeFor(4));
      final queuedTopics = {for (final q in queue.values) q.topicId};
      for (final r in reviews) {
        expect(queuedTopics, contains(r.topic.id));
      }
      // Bugun (muddati kelmagan) — takrorlash yo'q.
      final today = DailyPlanner.build(content: content, age: 4, progress: progress, isEnabled: all, now: day, rng: Random(2));
      expect(today.any((e) => e.review), isFalse);
    });

    test('keyingi mavzu: egallanganlar o‘tkazib yuboriladi, eng uzoq mashq qilinmagani tanlanadi', () {
      final topics = content.curriculum('math', '4')!.topics;
      final empty = DailyPlanner.nextTopic(topics, ChildProgress.empty('a'), Random(1))!;
      expect(empty.prerequisites.isEmpty, isTrue, reason: 'avval boshlang‘ich mavzu: ${empty.id}');

      final first = topics.first;
      var p = ChildProgress.empty('a').withSkill(first.id, SkillStat(level: first.maxLevel, ema: 100, lessons: 4, lastPracticed: day));
      final next = DailyPlanner.nextTopic(topics, p, Random(1))!;
      expect(next.id, isNot(first.id));

      // Hammasi egallangan bo'lsa ham mavzu topiladi (takrorlash uchun).
      for (final t in topics) {
        p = p.withSkill(t.id, SkillStat(level: t.maxLevel, ema: 100, lessons: 4, lastPracticed: day));
      }
      expect(DailyPlanner.nextTopic(topics, p, Random(1)), isNotNull);
    });
  });
}
