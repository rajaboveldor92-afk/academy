import 'dart:math';

import 'package:academy/database/seed_data.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/daily_planner.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/models/child_progress.dart';
import 'package:academy/models/subject.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;
  setUpAll(() async => content = await ContentRepository.load());

  test('every visible subject opens for Jasmina and Akramjon', () {
    for (final profile in [SeedData.jasmina(DateTime(2026)), SeedData.akramjon(DateTime(2026))]) {
      final subjects = Subject.forProfile(profile);
      expect(subjects, containsAll([Subject.logic, Subject.english, Subject.russian]));
      for (final subject in subjects) {
        final c = content.curriculum(subject.id, subject.suffixFor(profile));
        expect(c, isNotNull, reason: '${profile.name}: ${subject.id}');
        expect(c!.topics, isNotEmpty);
        final first = c.topics.first;
        final lesson = LessonBuilder.build(content: content, topic: first, level: 1, count: 6, age: profile.age, rng: Random(21));
        expect(lesson.length, 6, reason: first.id);
      }
      for (var day = 1; day <= 14; day++) {
        final plan = DailyPlanner.build(content: content, age: profile.age, grade: profile.grade,
          progress: ChildProgress.empty(profile.id), isEnabled: profile.isSubjectEnabled,
          now: DateTime(2026, 9, day), rng: Random(day));
        expect(plan.length, 10);
        expect(plan.every((x) => subjects.any((s) => s.id == x.topic.subject)), isTrue);
      }
    }
  });

  test('authored banks: unique questions, one correct answer, explanation and full coverage', () {
    expect(content.banks.length, greaterThanOrEqualTo(20));
    for (final entry in content.banks.entries) {
      final topic = content.topic(entry.key)!;
      final items = entry.value;
      expect(items.length, greaterThanOrEqualTo(15), reason: entry.key);
      expect(items.map((x) => x['id']).toSet().length, items.length);
      expect(items.map((x) => x['question']).toSet().length, items.length);
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      final seen = <String>{};
      final rng = Random(19);
      for (var i = 0; i < 700; i++) {
        final e = gen(GenContext(rng: rng, content: content, topic: topic, level: 3, age: 11));
        final source = items.singleWhere((x) => x['id'] == e.meta['bankId']);
        expect(ExerciseValidator.isPlayable(e), isTrue);
        expect(e.correctOption!.text, source['answer']);
        expect(e.explanation, source['explanation']);
        expect(e.speechLang, source['lang']);
        seen.add(source['id'] as String);
      }
      expect(seen.length, items.length, reason: entry.key);
    }
  });

  test('logic and century answers agree with independent calculations', () {
    for (final id in ['logic_g3.sequence', 'logic_g5.sequence', 'logic_g5.sets', 'history_g5.centuries']) {
      final topic = content.topic(id)!;
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      final rng = Random(81);
      for (var i = 0; i < 150; i++) {
        final e = gen(GenContext(rng: rng, content: content, topic: topic, level: 3, age: 11));
        final m = e.meta;
        if (m.containsKey('ruleStart')) {
          final start = m['ruleStart'] as int, step = m['ruleStep'] as int;
          expect(m['answer'], m['multiply'] == true ? start * pow(step, 4).toInt() : start + 4 * step);
        } else if (m.containsKey('setA')) {
          expect(m['answer'], (m['setA'] as int) + (m['setB'] as int) - (m['intersection'] as int));
        } else {
          final year = m['year'] as int, century = m['answer'] as int;
          expect(year, inInclusiveRange((century - 1) * 100 + 1, century * 100));
        }
      }
    }
  });
}
