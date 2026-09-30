import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/generators/school/logic_school.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:flutter_test/flutter_test.dart';

/// MAKTAB MANTIQI (1–8-sinf): har bir jumboqning javobi yagona va to'g'ri ekanini mustaqil tekshiramiz.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  int gcdOf(int a, int b) => b == 0 ? a : gcdOf(b, a % b);

  /// "🍎 + 🍌 × 🍒" kabi ifodani qiymatlar bilan hisoblaydi (× avval).
  int evalLine(String expr, Map<String, int> values) {
    var s = expr;
    values.forEach((k, v) => s = s.replaceAll(k, '$v'));
    final tokens = s.split(' ').where((t) => t.isNotEmpty).toList();
    // Avval ko'paytirish.
    final reduced = <String>[];
    for (var i = 0; i < tokens.length; i++) {
      if (tokens[i] == '×') {
        final left = int.parse(reduced.removeLast());
        reduced.add('${left * int.parse(tokens[++i])}');
      } else {
        reduced.add(tokens[i]);
      }
    }
    var total = int.parse(reduced.first);
    for (var i = 1; i < reduced.length; i += 2) {
      final v = int.parse(reduced[i + 1]);
      total += reduced[i] == '+' ? v : -v;
    }
    return total;
  }

  test('rostgo‘y va yolg‘onchi: yechuvchi to‘g‘ri ishlaydi', () {
    // A: «Ikkalamiz ham yolg'onchimiz» → A yolg'onchi, B rostgo'y.
    final s = LogicSchool.solveKnights(2, [(0, (k) => !k[0] && !k[1])]);
    expect(s, [
      [false, true],
    ]);
    // A: «B — yolg'onchi», B: «A — yolg'onchi» → ikki yechim.
    expect(LogicSchool.solveKnights(2, [(0, (k) => !k[1]), (1, (k) => !k[0])]).length, 2);
    expect(LogicSchool.solveTable(3, [(0, 0, false), (0, 1, false), (1, 1, false)]).length, 1);
    expect(LogicSchool.isMagic([2, 7, 6, 9, 5, 1, 4, 3, 8]), isTrue);
    expect(LogicSchool.choose(5, 2), 10);
    expect(LogicSchool.andList(['Ali', 'Vali', 'Zarina']), 'Ali, Vali va Zarina');
  });

  test('1–8-sinf dasturlari: 4 chorak, qoidalar, nazorat ishlari; eski kalitlar saqlangan', () {
    for (var grade = 1; grade <= 8; grade++) {
      final c = content.curriculum('logic', 'g$grade');
      expect(c, isNotNull, reason: 'logic_g$grade');
      expect(c!.topics.map((t) => t.chapter).toSet().length, 4);
      expect(c.topics.where((t) => t.isTest).length, 5);
      for (final t in c.topics.where((t) => !t.isTest)) {
        expect(t.theoryIn('uz')!.length, greaterThan(80), reason: t.id);
      }
    }
    for (final id in ['logic_g3.sequence', 'logic_g3.ordering', 'logic_g3.matrix2', 'logic_g3.coding', 'logic_g3.sudoku',
      'logic_g5.sequence', 'logic_g5.ordering', 'logic_g5.sets', 'logic_g5.matrix3', 'logic_g5.coding', 'logic_g5.sudoku']) {
      expect(content.topic(id), isNotNull, reason: id);
    }
  });

  test('har bir jumboq javobi mustaqil tekshiriladi', () {
    final seen = <String, int>{};
    for (final topic in content.allTopics.where((t) => t.subject == 'logic' && t.isSchool && !t.isTest)) {
      if (!const ['seq', 'knights', 'magic', 'emoji_eq', 'table_logic', 'number_think', 'combin', 'ages', 'calendar', 'pigeonhole']
          .contains(topic.generator)) {
        continue;
      }
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 71 + topic.id.hashCode);
        for (var i = 0; i < 120; i++) {
          final e = gen(GenContext(rng: rng, content: content, topic: topic, level: level, age: 11));
          final where = '${topic.id} L$level: ${e.instruction.uz}';
          expect(ExerciseValidator.isPlayable(e), isTrue, reason: where);
          expect(e.hint, isNotNull, reason: where);
          expect(e.explanation, isNotNull, reason: where);
          seen[topic.generator] = (seen[topic.generator] ?? 0) + 1;
          final m = e.meta;
          final String answer = e.kind == ExerciseKind.input ? e.input!.answer : e.options[e.correctIndex].text!;
          int ans() => int.parse(answer);
          switch (topic.generator) {
            case 'seq':
              final list = (m['seq'] as List).cast<int>();
              expect(ans(), list[m['index'] as int], reason: where);
              switch (m['kind']) {
                case 'arith' || 'arith_down':
                  expect({for (var j = 1; j < list.length; j++) list[j] - list[j - 1]}.length, 1, reason: '$where $list');
                case 'geom':
                  expect({for (var j = 1; j < list.length; j++) list[j] ~/ list[j - 1]}.length, 1, reason: '$where $list');
                case 'fib':
                  for (var j = 2; j < list.length; j++) {
                    expect(list[j], list[j - 1] + list[j - 2], reason: '$where $list');
                  }
                case 'squares':
                  for (final v in list) {
                    expect(sqrt(v).round() * sqrt(v).round(), v, reason: '$where $list');
                  }
              }
            case 'knights':
              expect(m['solutions'], 1, reason: where);
            case 'magic':
              final sq = (m['square'] as List).cast<int>();
              expect(LogicSchool.isMagic(sq), isTrue, reason: '$where $sq');
              expect(sq.take(3).fold(0, (a, b) => a + b), m['sum'], reason: where);
              expect(ans(), sq[m['missing'] as int], reason: where);
            case 'emoji_eq':
              final values = {
                for (final pair in (m['values'] as String).split(','))
                  pair.split('=')[0]: int.parse(pair.split('=')[1]),
              };
              final lines = (m['lines'] as List).cast<String>();
              for (final line in lines) {
                final parts = line.split(' = ');
                final lhs = evalLine(parts[0].replaceAll('−', '-'), values);
                if (parts[1] == '?') {
                  expect(ans(), lhs, reason: '$where $lines');
                } else {
                  expect(lhs, int.parse(parts[1]), reason: '$where $line');
                }
              }
            case 'table_logic':
              final perm = (m['perm'] as String).split(',').map(int.parse).toList();
              final clues = [
                for (final c in (m['clues'] as String).split(';'))
                  (int.parse(c.split(':')[0]), int.parse(c.split(':')[1]), c.split(':')[2] == '1'),
              ];
              final solutions = LogicSchool.solveTable(perm.length, clues);
              expect(solutions.length, 1, reason: where);
              expect(solutions.first, perm, reason: where);
              expect(e.options.length, perm.length, reason: where);
            case 'number_think':
              var v = ans();
              for (final op in (m['ops'] as String).split(',')) {
                final k = int.parse(op.substring(1));
                switch (op[0]) {
                  case '+':
                    v += k;
                  case '-':
                    v -= k;
                  case '*':
                    v *= k;
                  default:
                    expect(v % k, 0, reason: where);
                    v ~/= k;
                }
              }
              expect(v, m['result'], reason: where);
            case 'combin':
              int p(String k) => m[k] as int;
              final expected = switch (m['kind']) {
                'outfit' => p('a') * p('b') * p('c'),
                'handshake' || 'choose2' => p('n') * (p('n') - 1) ~/ 2,
                'tournament' => p('twice') == 1 ? p('n') * (p('n') - 1) : p('n') * (p('n') - 1) ~/ 2,
                'digits' => p('repeat') == 1 ? p('k') * p('k') : p('k') * (p('k') - 1),
                'queue' => [for (var j = 1; j <= p('k'); j++) j].fold(1, (a, b) => a * b),
                'routes' => p('a') * p('b') + p('c'),
                'paths' => LogicSchool.choose(p('w') + p('h'), p('h')),
                _ => null,
              };
              if (m['kind'] == 'chance') {
                final d = gcdOf(p('fav'), p('total'));
                expect(answer, '${p('fav') ~/ d}/${p('total') ~/ d}', reason: where);
                expect(e.input!.isCorrect('${p('fav')}/${p('total')}'), isTrue, reason: where);
              } else {
                expect(ans(), expected, reason: where);
              }
            case 'ages':
              int p(String k) => m[k] as int;
              switch (m['kind']) {
                case 'simple':
                  expect(ans(), p('a') + p('back') + p('fwd'), reason: where);
                case 'later':
                  expect(ans(), p('target') + p('diff'), reason: where);
                case 'sum_diff':
                  expect(ans(), p('old') == 1 ? p('y') + p('d') : p('y'), reason: where);
                case 'times_future':
                  expect(p('a') + ans(), p('k') * (p('b') + ans()), reason: where);
                  expect(ans(), greaterThan(0));
                case 'times_past':
                  expect(p('a') - ans(), p('k') * (p('b') - ans()), reason: where);
                  expect(ans(), inInclusiveRange(1, p('b') - 1));
              }
            case 'calendar':
              switch (m['kind']) {
                case 'weekday' || 'weekday_back' || 'yesterday':
                  final r = (((m['d'] as int) + (m['n'] as int)) % 7 + 7) % 7;
                  expect(answer, LogicSchool.weekdays[r], reason: where);
                case 'time_add':
                  expect(answer, LogicSchool.hm((m['start'] as int) + (m['dur'] as int)), reason: where);
                case 'duration':
                  expect(ans(), (m['end'] as int) - (m['start'] as int), reason: where);
              }
            case 'pigeonhole':
              if (m['kind'] == 'months') {
                expect(ans(), const [13, 8, 25, 15][m['variant'] as int], reason: where);
              } else {
                final counts = (m['counts'] as String).split(',').map(int.parse).toList();
                final k = m['k'] as int;
                final expected = switch (m['kind']) {
                  'one_color' => counts.fold(0, (a, b) => a + b) - counts[0] + 1,
                  'two_color' => max(counts[0], counts[1]) + 1,
                  'three_same' => 2 * k + 1,
                  _ => k + 1,
                };
                expect(ans(), expected, reason: where);
              }
          }
        }
      }
    }
    expect(seen.keys.toSet(), {'seq', 'knights', 'magic', 'emoji_eq', 'table_logic', 'number_think', 'combin', 'ages', 'calendar', 'pigeonhole'});
  });
}
