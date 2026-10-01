import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:academy/database/seed_data.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/content/uz_numbers.dart';
import 'package:academy/learning/engine/daily_planner.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/generators/school/math_school.dart';
import 'package:academy/learning/generators/school/school_base.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/models/child_progress.dart';
import 'package:academy/models/subject.dart';
import 'package:flutter_test/flutter_test.dart';

/// MAKTAB DASTURLARI (1–8-sinf): tuzilma, qoidalar va matematik to'g'rilik.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  test('index.json maktab papkasidagi barcha dastur va banklarni sanab o‘tadi', () {
    final names = Directory('assets/data/school')
        .listSync()
        .whereType<File>()
        .map((f) => f.uri.pathSegments.last)
        .where((n) => n.endsWith('.json') && n != 'index.json')
        .map((n) => n.substring(0, n.length - 5))
        .toSet();
    final index = jsonDecode(File('assets/data/school/index.json').readAsStringSync()) as Map<String, dynamic>;
    final listed = {...(index['curricula'] as List).cast<String>(), ...(index['banks'] as List).cast<String>()};
    expect(listed, names, reason: 'python3 tool/content/school/build_index.py');
    for (final name in (index['curricula'] as List).cast<String>()) {
      final parts = name.split('_g');
      expect(content.curriculum(parts[0], 'g${parts[1]}'), isNotNull, reason: name);
    }
  });

  test('3 va 5-sinf matematika dasturi: bo‘limlar, qoidalar, nazorat ishlari', () {
    for (final grade in [3, 5]) {
      final c = content.curriculum('math', 'g$grade');
      expect(c, isNotNull, reason: 'math_g$grade');
      final topics = c!.topics;
      expect(topics.length, greaterThanOrEqualTo(25));
      final ids = topics.map((t) => t.id).toSet();
      for (final t in topics) {
        expect(t.isSchool, isTrue);
        expect(t.chapter, isNotEmpty, reason: t.id);
        if (t.isTest) {
          for (final level in t.levels) {
            for (final id in (level['topics'] as List)) {
              expect(ids.contains(id), isTrue, reason: '${t.id} → $id');
              expect(content.topic('$id')!.isTest, isFalse);
            }
          }
        } else {
          expect(t.theoryIn('uz'), isNotNull, reason: '${t.id}: qoida yo‘q');
          expect(t.theoryIn('uz')!.length, greaterThan(60), reason: t.id);
          // Rus/ingliz tilidagi bola ham qoidani ko'radi (hozircha o'zbekcha).
          expect(t.theoryIn('ru'), isNotNull);
        }
      }
      expect(topics.where((t) => t.isTest).length, greaterThanOrEqualTo(4));
    }
  });

  test('matematik to‘g‘rilik: har bir mashq javobi mustaqil tekshiriladi', () {
    var inputs = 0, choices = 0;
    for (final topic in content.allTopics.where((t) => t.isSchool && t.subject == 'math')) {
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 31 + topic.id.hashCode);
        for (var i = 0; i < 150; i++) {
          final e = gen(GenContext(rng: rng, content: content, topic: topic, level: level, age: 10));
          final where = '${topic.id} L$level: ${e.instruction.uz}';
          expect(ExerciseValidator.isPlayable(e), isTrue, reason: where);
          expect(e.hint, isNotNull, reason: where);
          expect(e.explanation, isNotNull, reason: where);
          final m = e.meta;
          final answer = m['answer'];
          if (e.kind == ExerciseKind.input) {
            inputs++;
            final t = e.input!;
            expect(t.isCorrect(t.answer), isTrue, reason: where);
            expect(t.isCorrect('${t.answer}9'), isFalse, reason: where);
            if (answer is int) expect(t.answer, '$answer', reason: where);
            for (final ch in InputTask.normalize(t.answer).split('')) {
              expect('0123456789/,-'.contains(ch), isTrue, reason: '$where: klaviaturada yo‘q belgi “$ch”');
            }
            if (t.answer.contains('/')) expect(t.keys, anyOf('fraction', 'fraction_decimal'), reason: where);
            if (t.answer.contains(',')) expect(t.keys, anyOf('decimal', 'fraction_decimal'), reason: where);
          } else {
            choices++;
            if (answer is int && e.options.isNotEmpty) {
              expect(e.options[e.correctIndex].text, '$answer', reason: where);
            }
          }
          final a = m['a'], b = m['b'];
          if (a is int && b is int && answer is int) {
            switch (m['op']) {
              case '+':
                expect(answer, a + b, reason: where);
              case '-':
                expect(answer, a - b, reason: where);
                expect(answer, greaterThanOrEqualTo(0), reason: where);
              case '*':
                expect(answer, a * b, reason: where);
              case '/':
                expect(a % b, 0, reason: where);
                expect(answer, a ~/ b, reason: where);
              case 'mod':
                expect(answer == a % b || answer == a ~/ b, isTrue, reason: where);
            }
          }
        }
      }
    }
    expect(inputs, greaterThan(1000));
    expect(choices, greaterThan(1000));
  });

  test('yordamchilar: son formati, o‘nli kasr, Rim raqamlari, so‘z bilan', () {
    expect(fmtNum(1234567), '1 234 567');
    expect(fmtNum(45302), '45 302');
    expect(fmtNum(999), '999');
    expect(fmtDec(0.75), '0,75');
    expect(fmtDec(2.5), '2,5');
    expect(fmtDec(3), '3');
    expect(gcd(12, 18), 6);
    expect(MathSchool.toRoman(14), 'XIV');
    expect(MathSchool.toRoman(39), 'XXXIX');
    expect(MathSchool.toRoman(49), 'XLIX');
    expect(MathSchool.words(304502), 'uch yuz to‘rt ming besh yuz ikki');
    expect(MathSchool.words(4305020), 'to‘rt million uch yuz besh ming yigirma');
    expect(MathSchool.words(1000), 'bir ming');
    const t = InputTask(answer: '3/4', accept: ['6/8']);
    expect(t.isCorrect('3/4'), isTrue);
    expect(t.isCorrect('6/8'), isTrue);
    expect(t.isCorrect('3/5'), isFalse);
    const d = InputTask(answer: '0,75', accept: [',75']);
    expect(d.isCorrect('0.75'), isTrue);
    expect(d.isCorrect(',75'), isTrue);
    expect(const InputTask(answer: '12345').isCorrect('12 345'), isTrue);
  });

  test('ovoz: katta sonlar, kasrlar, soat, birliklar va belgilar so‘z bilan', () {
    expect(UzNumbers.word(1000), 'ming');
    expect(UzNumbers.word(1001), 'ming bir');
    expect(UzNumbers.word(2026), 'ikki ming yigirma olti');
    expect(UzNumbers.word(45302), 'qirq besh ming uch yuz ikki');
    expect(UzNumbers.word(1000000), 'bir million');
    expect(UzNumbers.word(3500000), 'uch million besh yuz ming');
    expect(schoolSpeech('3344 : x = 8. x = ?'), 'uch ming uch yuz qirq to‘rt bo‘luv x teng sakkiz. x teng ?');
    expect(schoolSpeech('12 345 + 1 000 = ?'), contains('o‘n ikki ming uch yuz qirq besh qo‘shuv ming'));
    expect(schoolSpeech('3/4 ni toping'), 'to‘rtdan uchni toping');
    expect(schoolSpeech('2,05 · 10 = ?'), 'ikki butun yuzdan besh ko‘paytiruv o‘n teng ?');
    expect(schoolSpeech('Dars 8:05 da boshlandi'), 'Dars soat sakkizdan besh minut o‘tganda boshlandi');
    expect(schoolSpeech('Dars 9:00 da boshlandi'), 'Dars soat to‘qqizda boshlandi');
    expect(schoolSpeech('Yuzi necha sm²?'), 'Yuzi necha kvadrat santimetr?');
    expect(schoolSpeech('200 ning 25% ini toping'), 'ikki yuzning yigirma besh foizini toping');
    expect(schoolSpeech('Soatiga 5 km/soat'), contains('besh kilometr soatiga'));
    expect(schoolSpeech('17 // 5 = ?'), 'o‘n yetti butun bo‘luv besh teng ?');
    expect(schoolSpeech('−7 + 12 − 3 = ?'), 'minus yetti qo‘shuv o‘n ikki ayiruv uch teng ?');
    expect(schoolSpeech('x² − 9 = 0'), 'x kvadrat ayiruv to‘qqiz teng nol');
    expect(schoolSpeech('√49 = ?'), 'kvadrat ildiz qirq to‘qqiz teng ?');
    expect(schoolSpeech('3x − 5 ≤ 16'), 'uch x ayiruv besh kichik yoki teng o‘n olti');
    expect(schoolSpeech('2⁵ = ?'), 'ikkining beshinchi darajasi teng ?');
    expect(schoolSpeech('17 % 5 = ?'), 'o‘n yetti qoldiqli bo‘luv besh teng ?');

    // Barcha maktab mashqlarida ovozda raqam qolmaydi (xatolar birdaniga ko'rsatiladi).
    final bad = <String>{};
    for (final topic in content.allTopics.where((t) => t.isSchool)) {
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 97 + topic.id.hashCode);
        for (var i = 0; i < 80; i++) {
          final e = gen(GenContext(rng: rng, content: content, topic: topic, level: level, age: 10));
          if (RegExp(r'[\d{}·%°²³/]').hasMatch(e.speech)) bad.add('${topic.id} L$level: ${e.instruction.uz} → ${e.speech}');
        }
      }
    }
    expect(bad.take(30).toList(), isEmpty);
  });

  test('maktab o‘quvchisi: fanlar va kunlik dars sinf dasturidan', () {
    final jasmina = SeedData.jasmina(DateTime(2026));
    final akramjon = SeedData.akramjon(DateTime(2026));
    expect(jasmina.grade, 3);
    expect(akramjon.grade, 5);
    final subjects = Subject.forProfile(jasmina).map((s) => s.id).toList();
    expect(subjects, containsAll(['math', 'onatili', 'english', 'russian', 'science', 'technology']));
    expect(subjects, isNot(contains('trilingual')));
    expect(subjects, isNot(contains('history')));
    expect(Subject.forProfile(akramjon).map((s) => s.id), contains('technology'));
    expect(Subject.forProfile(akramjon).map((s) => s.id), isNot(contains('history')));
    expect(Subject.math.suffixFor(jasmina), 'g3');
    expect(Subject.chess.suffixFor(jasmina), '6');
    expect(Subject.reading.titleForGrade('uz', 5), 'Adabiyot');
    expect(Subject.reading.titleForGrade('uz', 3), 'O‘qish');

    for (final p in [jasmina, akramjon]) {
      final plan = DailyPlanner.build(
        content: content,
        age: p.age,
        grade: p.grade,
        progress: ChildProgress.empty(p.id),
        isEnabled: p.isSubjectEnabled,
        now: DateTime(2026, 9, 28),
        rng: Random(1),
      );
      expect(plan, isNotEmpty);
      for (final item in plan) {
        expect(item.topic.isTest, isFalse);
        expect(item.topic.ageSuffix, item.topic.subject == 'chess' ? '6' : 'g${p.grade}', reason: item.topic.id);
      }
    }
  });

  test('nazorat ishi: savollar dasturdagi mavzulardan, dars to‘liq tuziladi', () {
    final topic = content.topic('math_g3.test1')!;
    final lesson = LessonBuilder.build(content: content, topic: topic, level: 2, count: 10, age: 9, rng: Random(4));
    expect(lesson.length, 10);
    final sources = (topic.levels[1]['topics'] as List).toSet();
    for (final e in lesson) {
      expect(sources.contains(e.topicId), isTrue, reason: e.topicId);
    }
  });
}
