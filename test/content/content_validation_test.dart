import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/puzzles.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/models/topic.dart';
import 'package:academy/learning/models/visual.dart';
import 'package:flutter_test/flutter_test.dart';

/// KONTENTNI AVTOMATIK TEKSHIRISH (spetsifikatsiya 31-band).
///
/// Har bir mavzu × daraja uchun ko'p sonli mashq generatsiya qilinadi va
/// quyidagilar tekshiriladi: bo'sh savol/variant, dublikat variantlar,
/// to'g'ri javob variantlar ichida va yagona, matematik to'g'rilik,
/// yoshga moslik (son chegaralari), Android 9 da ko'rinmaydigan emoji,
/// tarjimalar to'liqligi, har darajada kamida 15 ta turli savol.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  /// Android 9 (Emoji 11) da yo'q emoji'lar — kontentda uchramasligi kerak.
  const unsupportedEmoji = [
    '🪜', '🫥', '🪙', '🪶', '🧍', '🧃', '🪑', '🧼', '🪥', '🪁', '🧅', '🧄', '🫐', '🦫', '🪴', '🛝',
  ];

  const samplesPerLevel = 120;

  int ageFor(Topic t) => t.ageSuffix == '4' ? 4 : 6;

  /// Variantlar tartibiga bog'liq bo'lmagan "ma'no" kaliti.
  String semanticKey(Exercise e) {
    final opts = e.options.map((o) => o.describe()).toList()..sort();
    final pairs = e.pairs.map((p) => '${p.left.describe()}=${p.right.describe()}').toList()..sort();
    return [
      e.instruction.uz,
      e.visual?.describe() ?? '',
      opts.join('|'),
      pairs.join('|'),
      e.sort?.items.map((i) => i.describe()).join('|') ?? '',
      e.maze?.describe() ?? '',
      e.sudoku?.describe() ?? '',
      e.coding?.describe() ?? '',
      e.previewVisual?.describe() ?? '',
    ].join('#');
  }

  Iterable<String> allText(Exercise e) sync* {
    yield e.instruction.uz;
    yield e.instruction.en;
    yield e.instruction.ru;
    yield e.visual?.describe() ?? '';
    yield e.previewVisual?.describe() ?? '';
    for (final o in e.options) {
      yield o.describe();
    }
    for (final p in e.pairs) {
      yield p.left.describe();
      yield p.right.describe();
    }
    final s = e.sort;
    if (s != null) {
      for (final o in [...s.bins, ...s.items]) {
        yield o.describe();
      }
    }
    if (e.maze != null) yield '${e.maze!.hero}${e.maze!.target}';
    if (e.sudoku != null) yield e.sudoku!.symbols.join();
    if (e.coding != null) yield '${e.coding!.hero}${e.coding!.target}';
  }

  /// Matematik to'g'rilikni meta ma'lumotlar orqali mustaqil tekshiradi.
  void checkMath(Exercise e) {
    final m = e.meta;
    final a = m['a'], b = m['b'], answer = m['answer'];
    final op = m['op'];
    if (a is int && b is int && answer is int && op == '+' && !m.containsKey('form')) {
      if (m.containsKey('total')) {
        expect(a + answer, m['total'], reason: '${e.topicId}: $a + ? = ${m['total']}');
      } else {
        expect(answer, a + b, reason: '${e.topicId}: $a + $b');
      }
    }
    if (a is int && b is int && answer is int && op == '-' && !m.containsKey('form')) {
      expect(answer, a - b, reason: '${e.topicId}: $a - $b');
      expect(answer, greaterThanOrEqualTo(0));
    }
    if (op == 'cmp') {
      final x = a as int, y = b as int;
      expect(answer, x > y ? '>' : (x < y ? '<' : '='), reason: e.topicId);
    }
    if (m.containsKey('form')) {
      final aa = m['a'] as int, bb = m['b'] as int, cc = m['c'] as int;
      expect(aa + bb, cc);
      final expected = switch (m['form']) {
        '?+b=c' => aa,
        'a-?=b' => bb,
        '?-a=b' => cc,
        _ => bb,
      };
      expect(answer, expected, reason: '${e.topicId} ${m['form']}');
    }
    if (m.containsKey('start') && m.containsKey('step') && m.containsKey('index')) {
      expect(answer, (m['start'] as int) + (m['step'] as int) * (m['index'] as int) - (e.topicId.contains('by_') ? 0 : 0),
          reason: '${e.topicId} sequence');
    }
    if (m.containsKey('groups') && m.containsKey('step')) {
      expect(answer, (m['groups'] as int) * (m['step'] as int));
    }
    if (m.containsKey('count') && e.visual is SceneVisual) {
      final items = (e.visual! as SceneVisual).items.where((i) => i.kind == SceneKind.emoji).length;
      expect(items, m['count'], reason: '${e.topicId}: sahnadagi narsalar soni');
    }
    if (m.containsKey('coins')) {
      final sum = (m['coins'] as String).split('+').map(int.parse).fold<int>(0, (s, v) => s + v);
      expect(sum, answer);
    }
    if (m.containsKey('tens')) {
      expect(answer, (m['tens'] as int) * 10 + (m['ones'] as int));
    }
    if (m.containsKey('hour') && m.containsKey('minute')) {
      expect(m['hour'] as int, inInclusiveRange(1, 12));
      expect(m['minute'], anyOf(0, 30));
    }
  }

  /// To'g'ri variant meta'dagi javobga mos va yagona bo'lishi kerak.
  void checkCorrectOption(Exercise e) {
    final answer = e.meta['answer'];
    if (e.options.isEmpty) return;
    final correct = e.options[e.correctIndex];
    if (answer is int && correct.text != null && int.tryParse(correct.text!) != null) {
      expect(correct.text, '$answer', reason: '${e.topicId}: to‘g‘ri variant');
      final same = e.options.where((o) => o.text == '$answer').length;
      expect(same, 1, reason: '${e.topicId}: bir nechta to‘g‘ri javob');
    }
    if (answer is int && (correct.text ?? '').endsWith('so‘m')) {
      expect(correct.text, '$answer so‘m');
    }
    if (answer is String && e.meta['op'] == 'cmp') {
      expect(correct.text, answer);
    }
    if (e.meta.containsKey('hour') && answer is String) {
      expect(correct.text, answer);
    }
  }

  test('lug‘at: ID noyob, uch tilda to‘liq', () {
    final ids = <String>{};
    for (final e in content.lexicon.entries) {
      expect(ids.add(e.id), isTrue, reason: 'dublikat ${e.id}');
      expect(e.word.isComplete, isTrue, reason: e.id);
      expect(e.emoji.trim(), isNotEmpty, reason: e.id);
      for (final bad in unsupportedEmoji) {
        expect(e.emoji.contains(bad), isFalse, reason: '${e.id}: $bad');
      }
    }
    expect(content.lexicon.entries.length, greaterThanOrEqualTo(200));
    for (final c in content.lexicon.colors) {
      expect(c.name.isComplete, isTrue);
    }
    for (final s in content.lexicon.shapes) {
      expect(s.name.isComplete, isTrue);
    }
  });

  test('ko‘rsatmalar: uch tilda, o‘rinbosarlar mos', () {
    final ph = RegExp(r'\{(\w+)(?::\w+)?\}');
    for (final key in content.instructions.keys) {
      final t = content.instructions.template(key)!;
      for (final lang in ['uz', 'en', 'ru']) {
        expect((t[lang] ?? '').trim(), isNotEmpty, reason: '$key/$lang');
      }
      Set<String> names(String s) => ph.allMatches(s).map((m) => m.group(1)!).toSet();
      expect(names(t['en']!), names(t['uz']!), reason: '$key en');
      expect(names(t['ru']!), names(t['uz']!), reason: '$key ru');
    }
  });

  test('dasturlar: mavzular noyob, generatorlar mavjud, oldingi mavzular to‘g‘ri', () {
    final ids = <String>{};
    for (final t in content.allTopics) {
      expect(ids.add(t.id), isTrue, reason: 'dublikat ${t.id}');
      expect(t.title.isComplete, isTrue, reason: t.id);
      expect(t.maxLevel, 3, reason: '${t.id}: 3 daraja bo‘lishi kerak');
      expect(GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator), isNotNull,
          reason: '${t.id}: generator ${t.generator}');
    }
    for (final t in content.allTopics) {
      for (final p in t.prerequisites) {
        expect(ids.contains(p), isTrue, reason: '${t.id} -> $p');
      }
    }
    expect(content.curriculum('math', '4')!.topics.length, 15);
    expect(content.curriculum('math', '6')!.topics.length, 20);
    expect(content.curriculum('logic', '4')!.topics.length, 15);
    expect(content.curriculum('logic', '6')!.topics.length, 15);
  });

  test('barcha mashqlar: to‘g‘ri, yagona javobli, yoshga mos, xilma-xil', () {
    final report = <String, int>{};
    for (final topic in content.allTopics) {
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      var topicUnique = 0;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 7919 + topic.id.hashCode);
        final unique = <String>{};
        for (var i = 0; i < samplesPerLevel; i++) {
          final ctx = GenContext(rng: rng, content: content, topic: topic, level: level, age: ageFor(topic));
          final Exercise e;
          try {
            e = gen(ctx);
          } catch (err) {
            fail('${topic.id} L$level: generator xatosi: $err');
          }
          final where = '${topic.id} L$level';
          expect(ExerciseValidator.isPlayable(e), isTrue, reason: '$where: o‘ynab bo‘lmaydi');
          expect(e.instruction.isComplete, isTrue, reason: '$where: tarjima');
          expect(e.instruction.uz.contains('{'), isFalse, reason: '$where: ${e.instruction.uz}');
          expect(RegExp(r'\d').hasMatch(e.speech), isFalse, reason: '$where: ovozda raqam: ${e.speech}');
          for (final text in allText(e)) {
            for (final bad in unsupportedEmoji) {
              expect(text.contains(bad), isFalse, reason: '$where: $bad');
            }
          }
          checkMath(e);
          checkCorrectOption(e);
          // Yoshga moslik: 4 yosh — 10 gacha, 6 yosh — 100 gacha.
          final ans = e.meta['answer'];
          if (topic.subject == 'math' && ans is int) {
            expect(ans, inInclusiveRange(0, topic.ageSuffix == '4' ? 10 : 100), reason: where);
          }
          if (e.kind == ExerciseKind.sudoku) {
            expect(PuzzleFactory.isValidSudoku(e.sudoku!), isTrue, reason: where);
          }
          if (e.kind == ExerciseKind.coding) {
            expect(PuzzleFactory.solveCoding(e.coding!), isNotNull, reason: where);
          }
          if (e.kind == ExerciseKind.maze) {
            expect(e.maze!.shortestPath(), isNotNull, reason: where);
          }
          unique.add(semanticKey(e));
        }
        expect(unique.length, greaterThanOrEqualTo(15),
            reason: '${topic.id} L$level: faqat ${unique.length} ta turli savol');
        topicUnique += unique.length;
      }
      final key = '${topic.subject}_${topic.ageSuffix}';
      report[key] = (report[key] ?? 0) + topicUnique;
    }
    // Spetsifikatsiya 29-band: minimal kontent hajmi.
    expect(report['math_4']!, greaterThanOrEqualTo(250));
    expect(report['logic_4']!, greaterThanOrEqualTo(200));
    expect(report['math_6']!, greaterThanOrEqualTo(500));
    expect(report['logic_6']!, greaterThanOrEqualTo(300));
    // ignore: avoid_print
    print('Kontent hisoboti (turli savollar soni): $report');
  });

  test('har bir mavzu va daraja uchun to‘liq dars tuziladi', () {
    for (final topic in content.allTopics) {
      final c = content.curriculum(topic.subject, topic.ageSuffix)!;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final lesson = LessonBuilder.build(
          content: content,
          topic: topic,
          level: level,
          count: c.lessonSize,
          age: ageFor(topic),
          rng: Random(level),
        );
        expect(lesson.length, c.lessonSize, reason: '${topic.id} L$level');
        expect(lesson.map(LessonBuilder.signatureHash).toSet().length, lesson.length,
            reason: '${topic.id} L$level: darsda takror');
      }
    }
  });

  test('takrorlanmaslik: avval ko‘rilgan savollar chetlab o‘tiladi', () {
    final topic = content.topic('math6.add_10')!;
    final first = LessonBuilder.build(content: content, topic: topic, level: 2, count: 10, age: 6, rng: Random(1));
    final seen = first.map(LessonBuilder.signatureHash).toSet();
    final second = LessonBuilder.build(
      content: content, topic: topic, level: 2, count: 10, age: 6, rng: Random(2), avoid: seen,
    );
    final repeats = second.where((e) => seen.contains(LessonBuilder.signatureHash(e))).length;
    expect(repeats, 0);
  });
}
