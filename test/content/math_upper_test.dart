import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/generators/school/math_upper.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:flutter_test/flutter_test.dart';

/// MATEMATIKA 1–8-SINF: har bir sinf dasturi bor; 6–8-sinf mashqlarining javobi mustaqil hisoblanadi.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  test('yordamchilar: ishorali hadlar, darajalar, tub sonlar', () {
    expect(MathUpper.sg(-7), '−7');
    expect(MathUpper.par(-3), '(−3)');
    expect(MathUpper.trinomial(1, -5, 6), 'x² − 5x + 6');
    expect(MathUpper.trinomial(2, 1, -3), '2x² + x − 3');
    expect(MathUpper.sup(12), '¹²');
    expect(MathUpper.factors(60), [2, 2, 3, 5]);
    expect(MathUpper.isPrime(97), isTrue);
    expect(MathUpper.isPrime(91), isFalse);
    expect(MathUpper.dec(125, 2), '1,25');
    expect(MathUpper.dec(250, 2), '2,5');
  });

  test('1–8-sinf matematika dasturlari: 4 chorak, qoidalar, nazorat ishlari', () {
    for (var grade = 1; grade <= 8; grade++) {
      final c = content.curriculum('math', 'g$grade');
      expect(c, isNotNull, reason: 'math_g$grade');
      expect(c!.topics.map((t) => t.chapter).toSet().length, 4, reason: 'math_g$grade');
      for (final t in c.topics.where((t) => !t.isTest)) {
        expect(t.theoryIn('uz')!.length, greaterThan(60), reason: t.id);
      }
    }
  });

  test('6–8-sinf: har bir javob mustaqil tekshiriladi', () {
    final ops = <String>{};
    for (final topic in content.allTopics.where((t) => t.subject == 'math' && t.isSchool && !t.isTest)) {
      if (!MathUpper.generators.containsKey(topic.generator)) continue;
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 53 + topic.id.hashCode);
        for (var i = 0; i < 150; i++) {
          final e = gen(GenContext(rng: rng, content: content, topic: topic, level: level, age: 13));
          final where = '${topic.id} L$level: ${e.instruction.uz}';
          expect(ExerciseValidator.isPlayable(e), isTrue, reason: where);
          final m = e.meta;
          final String answer = e.kind == ExerciseKind.input ? e.input!.answer : e.options[e.correctIndex].text!;
          int ans() => int.parse(answer.replaceAll('−', '-').replaceAll(' ', ''));
          int p(String k) => m[k] as int;
          final op = (m['op'] ?? (m.containsKey('eq') ? 'eq_${m['eq']}' : '')) as String;
          ops.add(op);
          List<int> list() => (m['list'] as String).split(',').map(int.parse).toList();
          switch (op) {
            case '+':
              expect(ans(), p('a') + p('b'), reason: where);
            case '-':
              expect(ans(), p('a') - p('b'), reason: where);
            case '*':
              expect(ans(), p('a') * p('b'), reason: where);
            case '/':
              expect(p('a') % p('b'), 0, reason: where);
              expect(ans(), p('a') ~/ p('b'), reason: where);
            case 'sub_int':
              expect(ans(), p('a') - p('b'), reason: where);
            case 'div_int':
              expect(p('a') % p('b'), 0, reason: where);
              expect(ans(), p('a') ~/ p('b'), reason: where);
            case 'chain_int':
              expect(ans(), p('a') + p('b') - p('c'), reason: where);
            case 'abs':
              expect(ans(), p('a').abs(), reason: where);
            case 'max_int':
              expect(answer, MathUpper.sg(max(p('a'), p('b'))), reason: where);
            case 'pow':
              expect(ans(), pow(p('a'), p('b')), reason: where);
            case 'divisors':
              expect(ans(), [for (var d = 1; d <= p('a'); d++) if (p('a') % d == 0) d].length, reason: where);
            case 'max_factor':
              expect(p('a') % ans(), 0, reason: where);
              expect(MathUpper.isPrime(ans()), isTrue, reason: where);
              for (var d = ans() + 1; d <= p('a'); d++) {
                if (p('a') % d == 0) expect(MathUpper.isPrime(d), isFalse, reason: where);
              }
            case 'gcd':
              expect(p('a') % ans() + p('b') % ans(), 0, reason: where);
              for (var d = ans() + 1; d <= min(p('a'), p('b')); d++) {
                expect(p('a') % d == 0 && p('b') % d == 0, isFalse, reason: where);
              }
            case 'lcm':
              expect(ans() % p('a') + ans() % p('b'), 0, reason: where);
              for (var v = max(p('a'), p('b')); v < ans(); v++) {
                expect(v % p('a') == 0 && v % p('b') == 0, isFalse, reason: where);
              }
            case 'prime':
              expect(MathUpper.isPrime(ans()), isTrue, reason: where);
              for (var j = 0; j < e.options.length; j++) {
                if (j != e.correctIndex) expect(MathUpper.isPrime(int.parse(e.options[j].text!)), isFalse, reason: where);
              }
            case 'sum_list':
              expect(ans(), (m['coefs'] as String).split(',').map(int.parse).fold(0, (a, b) => a + b), reason: where);
            case 'pa_qb':
              expect(ans(), p('p') * p('a') + p('q') * p('b'), reason: where);
            case 'eq_one':
              expect(p('a') * ans() + p('b'), p('c'), reason: where);
            case 'eq_paren':
              expect(p('a') * (ans() + p('b')), p('c'), reason: where);
            case 'eq_both':
              expect(p('a') * ans() + p('b'), p('c') * ans() + p('d'), reason: where);
            case 'direct':
              expect(ans(), p('b') * p('c'), reason: where);
            case 'inverse':
              expect(ans() * p('c'), p('a') * p('b'), reason: where);
            case 'prop':
              expect(p('a') * ans(), p('b') * p('c'), reason: where);
            case 'quadrant':
              final q = p('a') > 0 ? (p('b') > 0 ? 'I' : 'IV') : (p('b') > 0 ? 'II' : 'III');
              expect(answer, '$q chorak', reason: where);
            case 'dist':
              expect(ans(), (p('a') - p('b')).abs(), reason: where);
            case 'mid':
              expect(ans() * 2, p('a') + p('b'), reason: where);
            case 'sym':
              final nx = p('axis') == 0 ? p('a') : -p('a'), ny = p('axis') == 1 ? p('b') : -p('b');
              expect(ans(), p('x') == 1 ? nx : ny, reason: where);
            case 'circle_area' || 'circle_length':
              expect(answer, MathUpper.dec(p('hund'), 2), reason: where);
              expect(p('hund'), (op == 'circle_area' ? 314 * p('r') * p('r') : 628 * p('r')), reason: where);
            case 'circle_d':
              expect(ans() * 314, p('hund'), reason: where);
            case 'hyp':
              expect(ans() * ans(), p('a') * p('a') + p('b') * p('b'), reason: where);
            case 'leg':
              expect(ans() * ans(), p('a') * p('a') - p('b') * p('b'), reason: where);
            case 'pyth_check':
              expect(answer == 'Ha', p('a') * p('a') + p('b') * p('b') == p('c') * p('c'), reason: where);
            case 'value':
              expect(ans(), p('k') * p('x') + p('b'), reason: where);
            case 'root':
              expect(p('k') * ans() + p('b'), 0, reason: where);
            case 'intercept':
              expect(ans(), p('b'), reason: where);
            case 'slope':
              expect(ans() * (p('x2') - p('x1')), p('y2') - p('y1'), reason: where);
            case 'sumdiff':
              final x = (p('s') + p('d')) ~/ 2, y = (p('s') - p('d')) ~/ 2;
              expect(x + y, p('s'), reason: where);
              expect(ans(), p('x') == 1 ? x : y, reason: where);
            case 'elim':
              final x = (p('p') - p('q')) ~/ (p('a') - 1), y = p('q') - x;
              expect(p('a') * x + y, p('p'), reason: where);
              expect(ans(), p('x') == 1 ? x : y, reason: where);
            case 'vieta_sum':
              expect(ans(), -p('b'), reason: where);
            case 'vieta_prod':
              expect(ans(), p('c'), reason: where);
            case 'disc':
              expect(ans(), p('b') * p('b') - 4 * p('a') * p('c'), reason: where);
            case 'root_max' || 'root_min':
              final x = ans();
              expect(x * x + p('b') * x + p('c'), 0, reason: where);
              // Ikkinchi ildiz: Viyet bo'yicha −b − x.
              final other = -p('b') - x;
              expect(op == 'root_max' ? x >= other : x <= other, isTrue, reason: where);
            case 'sqrt':
              expect(ans() * ans(), p('a'), reason: where);
            case 'sqrt_between':
              final n = int.parse(answer.split(' ').first);
              expect(n * n < p('a') && p('a') < (n + 1) * (n + 1), isTrue, reason: where);
            case 'sqrt_simplify':
              expect(ans() * ans() * p('b'), p('a'), reason: where);
            case 'sqrt_product':
              expect(ans() * ans(), p('a') * p('b'), reason: where);
            case 'count_int':
              final lo = p('lo') + p('sl'), hi = p('hi') - p('sh');
              expect(ans(), hi - lo + 1, reason: where);
            case 'ineq_max':
              final x = ans();
              bool ok(int v) => p('s') == 1 ? p('a') * v + p('b') < p('c') : p('a') * v + p('b') <= p('c');
              expect(ok(x) && !ok(x + 1), isTrue, reason: where);
            case 'ineq_min':
              final x = ans();
              bool ok(int v) => p('s') == 1 ? p('a') * v + p('b') > p('c') : p('a') * v + p('b') >= p('c');
              expect(ok(x) && !ok(x - 1), isTrue, reason: where);
            case 'median':
              final s = list()..sort();
              expect(ans(), s[s.length ~/ 2], reason: where);
            case 'mode':
              final l = list();
              final counts = {for (final v in l) v: l.where((x) => x == v).length};
              final best = counts.values.reduce(max);
              expect(counts.values.where((c) => c == best).length, 1, reason: where);
              expect(counts[ans()], best, reason: where);
            case 'range':
              expect(ans(), list().reduce(max) - list().reduce(min), reason: where);
            case 'mean':
              expect(ans() * list().length, list().fold(0, (a, b) => a + b), reason: where);
            case 'trapezoid':
              expect(ans() * 2, (p('a') + p('b')) * p('h'), reason: where);
            case 'rhombus':
              expect(ans() * 2, p('a') * p('b'), reason: where);
            case 'diff_sq':
              expect(ans(), p('a') * p('a') - p('b') * p('b'), reason: where);
            case 'regular_angle':
              expect(ans() * p('a'), (p('a') - 2) * 180, reason: where);
            case 'tri_angle':
              expect(ans() + p('a') + p('b'), 180, reason: where);
              expect(ans(), greaterThan(0), reason: where);
            case 'poly_sum':
              expect(ans(), (p('a') - 2) * 180, reason: where);
            case 'dec_add' || 'dec_sub' || 'dec_mul' || 'dec_div':
              final a = p('a'), b = p('b');
              final expected = switch (op) {
                'dec_add' => a + b,
                'dec_sub' => a - b,
                'dec_mul' => a * b,
                _ => a ~/ b,
              };
              if (op == 'dec_div') expect(a % b, 0, reason: where);
              expect(p('m'), expected, reason: where);
              expect(answer, MathUpper.dec(p('m'), p('scale')), reason: where);
            default:
              fail('Tekshirilmagan amal: "$op" ($where)');
          }
        }
      }
    }
    expect(ops, containsAll(['sub_int', 'pow', 'gcd', 'lcm', 'eq_both', 'hyp', 'root_max', 'disc', 'sqrt_simplify', 'median', 'dec_div']));
  });
}
