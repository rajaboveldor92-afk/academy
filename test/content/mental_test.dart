import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/generators/school/mental_gen.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/models/visual.dart';
import 'package:academy/models/child_profile.dart';
import 'package:academy/models/subject.dart';
import 'package:flutter_test/flutter_test.dart';

/// MENTAL ARIFMETIKA (1–8-sinf): abakus qoidalari, flesh-anzan va tez hisob usullari to'g'riligi.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  test('abakus formulalari: kichik, katta do‘st va aralash formula', () {
    expect(MentalGen.formula(2, 2), isNull);
    expect(MentalGen.formula(7, -2), isNull);
    expect(MentalGen.formula(3, 4), '+4 = +5 − 1');
    expect(MentalGen.formula(6, -3), '−3 = −5 + 2');
    expect(MentalGen.formula(8, 7), '+7 = +10 − 3');
    expect(MentalGen.formula(13, -8), '−8 = −10 + 2');
    expect(MentalGen.formula(5, 6), '+6 = +1 − 5 + 10');
    expect(MentalGen.formula(11, -6), '−6 = −10 + 5 − 1');
    expect(MentalGen.applyFormula('+1 − 5 + 10'), 6);
    expect(MentalGen.applyFormula('−10 + 5 − 1'), -6);
    // Har qanday holat uchun formula natijasi aynan b ga teng va ustunda amalga oshiriladi.
    for (var total = 0; total <= 99; total++) {
      for (var b = -9; b <= 9; b++) {
        if (b == 0 || total + b < 0) continue;
        final f = MentalGen.formula(total, b);
        if (f == null) continue;
        expect(MentalGen.applyFormula(f.split(' = ').last), b, reason: '$total, $b: $f');
      }
    }
    expect(AbacusVisual.digitsOf(407, 3), [4, 0, 7]);
    expect(AbacusVisual.digitsOf(7, 2), [0, 7]);
  });

  test('ketma-ketliklar qoidaga mos: oddiy, kichik do‘st, katta do‘st', () {
    final topic = content.topic('mental_g1.flash_simple')!;
    for (final rule in ['simple', 'five', 'ten']) {
      for (var i = 0; i < 300; i++) {
        final g = GenContext(rng: Random(i), content: content, topic: topic, level: 1, age: 7);
        final list = MentalGen.terms(g, n: 4, digits: 1, rule: rule);
        expect(list.length, 4);
        var total = list.first;
        var special = false;
        for (final t in list.skip(1)) {
          final next = total + t;
          expect(next, greaterThanOrEqualTo(0));
          final simple = t > 0 ? MentalGen.isSimpleAdd(total % 10, t) : MentalGen.isSimpleSub(total % 10, -t);
          if (rule == 'simple') expect(simple, isTrue, reason: '$list');
          if (rule != 'ten') expect(next, lessThanOrEqualTo(9), reason: '$list');
          if (rule == 'five' && !simple) special = true;
          if (rule == 'ten' && total ~/ 10 != next ~/ 10) special = true;
          total = next;
        }
        if (rule != 'simple') expect(special, isTrue, reason: '$rule $list');
      }
    }
  });

  test('1–8-sinf dasturlari: 4 chorak, qoidalar, nazorat ishlari', () {
    final kid = ChildProfile.create(id: 'k', name: 'Ali', age: 7, avatar: '🦁');
    for (var grade = 1; grade <= 8; grade++) {
      final c = content.curriculum('mental', 'g$grade');
      expect(c, isNotNull, reason: 'mental_g$grade');
      final chapters = c!.topics.map((t) => t.chapter).toSet();
      expect(chapters.length, 4, reason: 'mental_g$grade');
      expect(c.topics.where((t) => t.isTest).length, 5);
      for (final t in c.topics.where((t) => !t.isTest)) {
        expect(t.theoryIn('uz')!.length, greaterThan(80), reason: t.id);
      }
      expect(Subject.mental.suffixFor(kid.copyWith(grade: grade)), 'g$grade');
    }
    expect(Subject.mental.isFor(kid.copyWith(grade: 3)), isTrue);
    expect(Subject.mental.isFor(kid), isFalse, reason: 'maktabgacha yoshda ko‘rinmaydi');
  });

  test('har bir mashq javobi mustaqil tekshiriladi', () {
    final kinds = <String>{};
    var flashes = 0, abacus = 0;
    for (final topic in content.allTopics.where((t) => t.subject == 'mental' && !t.isTest)) {
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 131 + topic.id.hashCode);
        for (var i = 0; i < 150; i++) {
          final e = gen(GenContext(rng: rng, content: content, topic: topic, level: level, age: 10));
          final where = '${topic.id} L$level: ${e.instruction.uz}';
          expect(ExerciseValidator.isPlayable(e), isTrue, reason: where);
          expect(e.hint, isNotNull, reason: where);
          expect(e.explanation, isNotNull, reason: where);
          final m = e.meta;
          final answer = m['answer'];
          if (m['kind'] != null) kinds.add('${m['kind']}');
          if (e.kind == ExerciseKind.input) {
            final t = e.input!;
            if (answer != null) expect(t.answer, '$answer', reason: where);
            if (t.flash.isNotEmpty) {
              flashes++;
              final sum = t.flash.map((s) => int.parse(s.replaceAll('−', '-').replaceAll('+', ''))).fold(0, (a, b) => a + b);
              expect('$sum', t.answer, reason: '$where ${t.flash}');
              expect(t.flashMs, inInclusiveRange(500, 3000));
            }
            if (t.isAbacus) {
              abacus++;
              expect(t.answer.length, lessThanOrEqualTo(t.rods), reason: where);
            }
          } else if (answer != null && e.options.isNotEmpty) {
            final correct = e.options[e.correctIndex];
            if (correct.text != null) expect(correct.text, '$answer', reason: where);
          }
          final terms = m['terms'];
          if (terms is List) expect(terms.cast<int>().fold(0, (a, b) => a + b), answer, reason: where);
          final a = m['a'], b = m['b'];
          switch (m['op']) {
            case '+':
              expect(answer, (a as int) + (b as int), reason: where);
            case '-':
              expect(answer, (a as int) - (b as int), reason: where);
            case '*':
              expect(answer, (a as int) * (b as int), reason: where);
            case '/':
              expect((a as int) % (b as int), 0, reason: where);
              expect(answer, a ~/ b, reason: where);
            case 'pct':
              expect((a as int) * (b as int) % 100, 0, reason: where);
              expect(answer, a * b ~/ 100, reason: where);
            case 'pct_up':
              expect(answer, (a as int) + a * (b as int) ~/ 100, reason: where);
            case 'pct_down':
              expect(answer, (a as int) - a * (b as int) ~/ 100, reason: where);
            case 'frac':
              expect((a as int) % (m['den'] as int), 0, reason: where);
              expect(answer, a ~/ (m['den'] as int) * (m['num'] as int), reason: where);
            case 'pow':
              expect(answer, pow(a as int, b as int), reason: where);
            case 'sqrt':
              expect((answer as int) * answer, a, reason: where);
            case 'cube':
              expect(answer, (a as int) * a * a, reason: where);
            case 'gauss':
              expect(answer, (a as int) * (a + 1) ~/ 2, reason: where);
            case 'divisible':
              expect((answer as int) % (b as int), 0, reason: where);
              for (var j = 0; j < e.options.length; j++) {
                if (j != e.correctIndex) expect(int.parse(e.options[j].text!) % b, isNot(0), reason: where);
              }
            case 'abacus':
              expect((e.visual! as AbacusVisual).value, answer, reason: where);
            case 'abacus_pick':
              expect((e.options[e.correctIndex].visual! as AbacusVisual).value, answer, reason: where);
              for (var j = 0; j < e.options.length; j++) {
                if (j != e.correctIndex) expect((e.options[j].visual! as AbacusVisual).value, isNot(answer), reason: where);
              }
          }
          final formula = m['formula'];
          if (formula is String) {
            expect(MentalGen.applyFormula(formula), b, reason: where);
            expect(MentalGen.formula(a as int, b as int)!.split(' = ').last, formula, reason: where);
            expect(e.options[e.correctIndex].text, formula, reason: where);
          }
          if (m.containsKey('pair')) expect((m['n'] as int) + (answer as int), m['pair'], reason: where);
        }
      }
    }
    expect(flashes, greaterThan(1000));
    expect(abacus, greaterThan(200));
    expect(kinds, containsAll(['x11', 'sq5', 'pct', 'near100', 'sqrt', 'gauss', 'divisible', 'pow2', 'frac_of']));
  });
}
