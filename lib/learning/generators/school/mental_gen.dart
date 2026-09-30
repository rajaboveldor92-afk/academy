import 'dart:math' as math;

import '../../models/exercise.dart';
import '../../models/visual.dart';
import '../generator_base.dart';
import 'school_base.dart';

/// Mental arifmetika (1–8-sinf): abakus (soroban), kichik va katta do'stlar, aralash formula,
/// zanjirli hisob, flesh-anzan va tez hisoblash usullari.
///
/// Mavzu darajasi parametrlari:
/// * `abacus_read`, `abacus_set`: `rods` (ustunlar soni), `expr` (misol bilan so'rash ehtimoli, %);
/// * `friends5`, `friends10`: `types` (`pair`, `how`, `calc`, `chain`, `mixed`), `plus` (faqat qo'shish), `n`;
/// * `chain`, `flash`: `n` (sonlar soni), `digits` (xonasi), `rule` (`simple`, `five`, `ten`, `any`),
///   `plus` (faqat qo'shish), `neg` (manfiy natija ham bo'lishi mumkin), `ms` (flesh tezligi);
/// * `tricks`: `kinds` — usullar ro'yxati (`x11`, `sq5`, `pct` ...).
class MentalGen {
  MentalGen._();

  static Map<String, ExerciseGenerator> get generators => {
        'abacus_read': abacusRead,
        'abacus_set': abacusSet,
        'friends5': friends5,
        'friends10': friends10,
        'chain': chain,
        'flash': flash,
        'tricks': tricks,
      };

  static const String minus = '−';

  static String signed(int b) => b < 0 ? '$minus${-b}' : '+$b';

  /// Ifoda matni: `12 + 7 − 5`.
  static String expr(List<int> terms) {
    final b = StringBuffer('${terms.first}');
    for (final t in terms.skip(1)) {
      b.write(t < 0 ? ' $minus ${-t}' : ' + $t');
    }
    return b.toString();
  }

  static int _pow10(int n) => math.pow(10, n).toInt();

  // ------------------------------------------------------------ abakus qoidalari (bir ustun)

  /// Pastki/yuqori munchoqlar bo'sh bo'lsa — to'g'ridan-to'g'ri qo'shish.
  static bool isSimpleAdd(int a, int b) => a + b <= 9 && !(a >= 5 && b >= 5) && a % 5 + b % 5 <= 4;

  /// Kerakli munchoqlar to'singa surilgan bo'lsa — to'g'ridan-to'g'ri ayirish.
  static bool isSimpleSub(int a, int b) => a - b >= 0 && !(a < 5 && b >= 5) && a % 5 >= b % 5;

  /// Birlar ustunida `total` turganda `b` ni (ishorasi bilan, |b| ≤ 9) qo'shish usuli:
  /// `null` — oddiy; aks holda formula (`+4 = +5 − 1`, `+7 = +10 − 3`, `+6 = +1 − 5 + 10`).
  static String? formula(int total, int b) {
    final a = total % 10;
    final m = b.abs();
    if (m == 0 || m > 9 || total < 0) return null;
    if (b > 0) {
      if (a + m <= 9) return isSimpleAdd(a, m) ? null : '+$m = +5 $minus ${5 - m}';
      final c = 10 - m;
      if (isSimpleSub(a, c)) return '+$m = +10 $minus $c';
      return '+$m = +${5 - c} $minus 5 + 10';
    }
    if (a - m >= 0) return isSimpleSub(a, m) ? null : '$minus$m = ${minus}5 + ${5 - m}';
    final c = 10 - m;
    if (isSimpleAdd(a, c)) return '$minus$m = ${minus}10 + $c';
    return '$minus$m = ${minus}10 + 5 $minus ${5 - c}';
  }

  /// Formula matnidagi amallarni qo'llash (testlar uchun): `+5 − 1` → 4.
  static int applyFormula(String f) {
    var sum = 0;
    for (final m in RegExp('([+$minus]) ?(\\d+)').allMatches(f)) {
      final v = int.parse(m[2]!);
      sum += m[1] == '+' ? v : -v;
    }
    return sum;
  }

  // ------------------------------------------------------------ abakus

  static int _abacusValue(GenContext g, int rods) => rods == 1 ? g.range(1, 9) : g.range(_pow10(rods - 1), _pow10(rods) - 1);

  /// Abakusda adashtiradigan sonlar: 5 li munchoq, ±1 munchoq, teskari tartib.
  static List<int> _confusions(GenContext g, int value, int rods) {
    final limit = _pow10(rods);
    final digits = AbacusVisual.digitsOf(value, rods);
    final out = <int>{};
    for (var i = 0; i < rods; i++) {
      final place = _pow10(rods - 1 - i);
      final d = digits[i];
      out.add(d >= 5 ? value - 5 * place : value + 5 * place);
      if (d < 9) out.add(value + place);
      if (d > 0) out.add(value - place);
    }
    final reversed = int.parse(digits.reversed.join());
    out.add(reversed);
    out.removeWhere((v) => v <= 0 || v >= limit || v == value);
    final list = out.toList()..shuffle(g.rng);
    var guard = 0;
    while (list.length < 4 && guard++ < 100) {
      final v = _abacusValue(g, rods);
      if (v != value && !list.contains(v)) list.add(v);
    }
    return list;
  }

  static Exercise abacusRead(GenContext g) {
    final rods = g.p('rods', 1);
    final value = _abacusValue(g, rods);
    final count = g.p('options', 4);
    final wrong = _confusions(g, value, rods).take(count - 1).toList();
    const hint = 'Yuqori munchoq to‘singa tushgan bo‘lsa — 5, har bir ko‘tarilgan pastki munchoq — 1.';
    final digits = AbacusVisual.digitsOf(value, rods);
    final expl = rods == 1
        ? _digitWords(value)
        : [for (var i = 0; i < rods; i++) '${_placeName(rods - 1 - i)}: ${digits[i]}'].join(', ');
    if (g.chance(0.5)) {
      return g.choice(
        say: g.ask('Abakusda qaysi son qo‘yilgan?'),
        options: [Opt.text('$value'), for (final w in wrong) Opt.text('$w')],
        concept: 'mental:abacus:$value',
        visual: AbacusVisual(value, rods: rods),
        hint: hint,
        explanation: '$expl → $value',
        meta: {'answer': value, 'op': 'abacus'},
      );
    }
    return g.choice(
      say: g.ask('Qaysi abakusda $value soni qo‘yilgan?'),
      options: [
        ExerciseOption(visual: AbacusVisual(value, rods: rods)),
        for (final w in wrong) ExerciseOption(visual: AbacusVisual(w, rods: rods)),
      ],
      concept: 'mental:abacus:$value',
      hint: hint,
      explanation: '$value: $expl',
      meta: {'answer': value, 'op': 'abacus_pick'},
    );
  }

  static String _digitWords(int d) {
    if (d == 0) return 'Hech bir munchoq to‘singa surilmagan';
    if (d < 5) return '$d ta pastki munchoq';
    if (d == 5) return 'Yuqori munchoq (5)';
    return 'Yuqori munchoq (5) va ${d - 5} ta pastki munchoq';
  }

  static String _placeName(int power) => const ['birlar', 'o‘nliklar', 'yuzliklar', 'minglar', 'o‘n minglar'][power];

  static Exercise abacusSet(GenContext g) {
    final rods = g.p('rods', 1);
    final limit = _pow10(rods) - 1;
    final useExpr = g.range(1, 100) <= g.p('expr', rods == 1 ? 50 : 30);
    if (useExpr) {
      for (var guard = 0; guard < 100; guard++) {
        final sub = g.chance(0.4);
        final a = _abacusValue(g, rods);
        final b = rods == 1 ? g.range(1, 8) : g.range(1, math.max(2, _pow10(rods - 1) * 3));
        final v = sub ? a - b : a + b;
        if (v < 1 || v > limit) continue;
        final text = '$a ${sub ? minus : '+'} $b';
        return g.custom(
          say: g.ask('Abakusda $text natijasini qo‘ying.'),
          kind: ExerciseKind.input,
          concept: 'mental:set:$v',
          visual: TextVisual(text),
          input: InputTask(answer: '$v', keys: 'abacus', rods: rods),
          hint: 'Avval natijani toping: $text = ?. Keyin munchoqlarni to‘singa suring.',
          explanation: '$text = $v',
          meta: {'answer': v, 'a': a, 'b': b, 'op': sub ? '-' : '+'},
        );
      }
    }
    final v = _abacusValue(g, rods);
    return g.custom(
      say: g.ask('Abakusda $v sonini qo‘ying.'),
      kind: ExerciseKind.input,
      concept: 'mental:set:$v',
      visual: TextVisual('$v'),
      input: InputTask(answer: '$v', keys: 'abacus', rods: rods),
      hint: 'Munchoqni bosing — u to‘singa suriladi. Yuqori munchoq — 5, pastkilari — 1 dan.',
      explanation: rods == 1 ? '$v: ${_digitWords(v)}.' : '$v: ${[
          for (var i = 0; i < rods; i++) '${_placeName(rods - 1 - i)} — ${AbacusVisual.digitsOf(v, rods)[i]}'
        ].join(', ')}.',
      meta: {'answer': v},
    );
  }

  // ------------------------------------------------------------ kichik va katta do'stlar

  static Exercise friends5(GenContext g) {
    final types = g.pl('types');
    final type = g.pick(types.isEmpty ? const ['pair', 'how', 'calc'] : types);
    final plus = g.pb('plus');
    switch (type) {
      case 'pair':
        final n = g.range(1, 4);
        return g.choice(
          say: g.ask('$n ning kichik do‘sti qaysi son?'),
          options: [Opt.text('${5 - n}'), for (final w in g.sample([for (var v = 1; v <= 5; v++) if (v != 5 - n) v], 3)) Opt.text('$w')],
          concept: 'mental:friend5:$n',
          visual: TextVisual('$n + ? = 5'),
          hint: 'Kichik do‘stlar birga 5 ni tashkil qiladi.',
          explanation: '$n + ${5 - n} = 5',
          meta: {'answer': 5 - n, 'pair': 5, 'n': n},
        );
      case 'how':
        final sub = !plus && g.chance(0.4);
        final int a, b;
        if (sub) {
          b = g.range(1, 4);
          a = 5 + g.range(0, b - 1);
        } else {
          b = g.range(1, 4);
          a = g.range(5 - b, 4);
        }
        final f = formula(a, sub ? -b : b)!.split(' = ').last;
        final wrong = sub
            ? ['${minus}5 $minus ${5 - b}', '${minus}10 + ${10 - b}', '+5 $minus ${5 + b}']
            : ['+5 + ${5 - b}', '+10 $minus ${10 - b}', '${minus}5 + ${5 + b}'];
        return g.textChoice(
          question: 'Abakusda $a turibdi. $b ni qanday ${sub ? 'ayiramiz' : 'qo‘shamiz'}?',
          answer: f,
          wrong: wrong,
          concept: 'mental:how5:${sub ? '-' : '+'}$b',
          options: g.p('options', 4),
          visual: AbacusVisual(a),
          hint: sub ? 'Pastda $b ta munchoq yo‘q: 5 ni olib, ortiqchasini qaytaramiz.' : 'Pastda joy yetmaydi: 5 ni qo‘shib, ortiqchasini olamiz.',
          explanation: '${sub ? minus : '+'}$b = $f: $a ${sub ? minus : '+'} $b = ${sub ? a - b : a + b}',
          meta: {'a': a, 'b': sub ? -b : b, 'formula': f},
        );
      case 'chain':
        return chainWith(g, n: g.p('n', 3), digits: 1, rule: 'five', plus: plus);
      default:
        final sub = !plus && g.chance(0.4);
        final b = g.range(1, 4);
        final a = sub ? 5 + g.range(0, b - 1) : g.range(5 - b, 4);
        final answer = sub ? a - b : a + b;
        final f = formula(a, sub ? -b : b)!;
        return g.numberAnswer(
          question: '$a ${sub ? minus : '+'} $b = ?',
          answer: answer,
          concept: 'mental:calc5:$a${sub ? '-' : '+'}$b',
          input: g.useInput(),
          hint: 'Kichik do‘st yordam beradi: ${f.split(' = ').first} = ${f.split(' = ').last}.',
          explanation: '$f. $a ${sub ? minus : '+'} $b = $answer',
          meta: {'a': a, 'b': b, 'op': sub ? '-' : '+'},
        );
    }
  }

  static Exercise friends10(GenContext g) {
    final types = g.pl('types');
    final type = g.pick(types.isEmpty ? const ['pair', 'how', 'calc'] : types);
    final plus = g.pb('plus');
    final big = g.p('max', 20) > 20;
    switch (type) {
      case 'pair':
        final n = g.range(1, 9);
        return g.choice(
          say: g.ask('$n ning katta do‘sti qaysi son?'),
          options: [Opt.text('${10 - n}'), for (final w in g.sample([for (var v = 1; v <= 9; v++) if (v != 10 - n) v], 3)) Opt.text('$w')],
          concept: 'mental:friend10:$n',
          visual: TextVisual('$n + ? = 10'),
          hint: 'Katta do‘stlar birga 10 ni tashkil qiladi.',
          explanation: '$n + ${10 - n} = 10',
          meta: {'answer': 10 - n, 'pair': 10, 'n': n},
        );
      case 'how':
      case 'mixed':
        for (var guard = 0; guard < 200; guard++) {
          final sub = !plus && type == 'how' && g.chance(0.4);
          final b = g.range(1, 9);
          final a = sub ? g.range(10, big ? 89 : 18) : g.range(1, big ? 89 : 9);
          final f = formula(a, sub ? -b : b);
          if (f == null) continue;
          final isMixed = f.split(' ').length > 5;
          final isTen = f.contains('10');
          if (!isTen || isMixed != (type == 'mixed')) continue;
          final rhs = f.split(' = ').last;
          final c = 10 - b;
          final five = b > 5 ? '5 + ${b - 5}' : (b == 5 ? '5 + 5' : '5 $minus ${5 - b}');
          final wrong = sub
              ? ['${minus}10 $minus $c', '+10 $minus $c', '$minus$five', '${minus}10 + $b']
              : ['+10 + $c', '${minus}10 + $c', '+10 $minus $b', '+$five'];
          if (type == 'mixed') wrong.insert(0, '+10 $minus $c');
          final result = sub ? a - b : a + b;
          return g.textChoice(
            question: 'Abakusda $a turibdi. $b ni qanday ${sub ? 'ayiramiz' : 'qo‘shamiz'}?',
            answer: rhs,
            wrong: wrong,
            concept: 'mental:how10:${sub ? '-' : '+'}$b:${a % 10}',
            options: g.p('options', 4),
            visual: AbacusVisual(a, rods: 2),
            hint: type == 'mixed'
                ? 'Birlar ustunida $c ni olib bo‘lmaydi: kichik do‘st ham yordamga keladi.'
                : sub
                    ? 'Birlarda $b yo‘q: o‘nlikdan 1 ni olib, katta do‘st $c ni qaytaramiz.'
                    : 'Birlarda joy yetmaydi: o‘nliklarga 1 qo‘shib, katta do‘st $c ni olamiz.',
            explanation: '$f: $a ${sub ? minus : '+'} $b = $result',
            meta: {'a': a, 'b': sub ? -b : b, 'formula': rhs},
          );
        }
        return friends10(g);
      case 'chain':
        return chainWith(g, n: g.p('n', 3), digits: 1, rule: 'ten', plus: plus);
      default:
        for (var guard = 0; guard < 200; guard++) {
          final sub = !plus && g.chance(0.45);
          final b = g.range(2, 9);
          final a = sub ? g.range(11, big ? 99 : 18) : g.range(2, big ? 89 : 9);
          final answer = sub ? a - b : a + b;
          if ((a ~/ 10) == (answer ~/ 10) || answer < 0) continue;
          final f = formula(a, sub ? -b : b) ?? '';
          return g.numberAnswer(
            question: '$a ${sub ? minus : '+'} $b = ?',
            answer: answer,
            concept: 'mental:calc10:$a${sub ? '-' : '+'}$b',
            input: g.useInput(),
            hint: 'Katta do‘st: ${sub ? '$b ni ayirish = 10 ni ayirib, ${10 - b} ni qo‘shish' : '$b ni qo‘shish = 10 ni qo‘shib, ${10 - b} ni ayirish'}.',
            explanation: '${f.isEmpty ? '' : '$f. '}$a ${sub ? minus : '+'} $b = $answer',
            meta: {'a': a, 'b': b, 'op': sub ? '-' : '+'},
          );
        }
        return friends10(g);
    }
  }

  // ------------------------------------------------------------ zanjir va flesh-anzan

  /// Qoida bo'yicha sonlar ketma-ketligi (birinchisi musbat, qolganlari ishorasi bilan).
  static List<int> terms(GenContext g, {required int n, required int digits, required String rule, bool plus = false, bool neg = false}) {
    final lo = digits == 1 ? 1 : _pow10(digits - 1);
    final hi = _pow10(digits) - 1;
    final oneRod = rule == 'simple' || rule == 'five';
    final maxTotal = oneRod ? 9 : (digits == 1 ? 99 : _pow10(digits + 1) - 1);
    final minTotal = neg ? -hi : 0;
    for (var attempt = 0; attempt < 300; attempt++) {
      final list = <int>[oneRod ? g.range(1, 9) : g.range(lo, hi)];
      var total = list.first;
      var special = false;
      var negative = false;
      for (var i = 1; i < n; i++) {
        var added = false;
        for (var tries = 0; tries < 40 && !added; tries++) {
          final b = g.range(lo, hi);
          final sub = !plus && g.chance(neg ? 0.5 : 0.45);
          final next = sub ? total - b : total + b;
          if (next < minTotal || next > maxTotal) continue;
          switch (rule) {
            case 'simple':
              if (!(sub ? isSimpleSub(total, b) : isSimpleAdd(total, b))) continue;
            case 'five':
              if (!(sub ? isSimpleSub(total, b) : isSimpleAdd(total, b))) special = true;
            case 'ten':
              if (total ~/ 10 != next ~/ 10) special = true;
          }
          if (next < 0) negative = true;
          list.add(sub ? -b : b);
          total = next;
          added = true;
        }
        if (!added) break;
      }
      if (list.length < n || total == 0) continue;
      if ((rule == 'five' || rule == 'ten') && !special) continue;
      if (neg && !negative && attempt < 200) continue;
      return list;
    }
    return [2, 2];
  }

  static String _steps(List<int> list) {
    final parts = <String>[];
    var total = list.first;
    for (final t in list.skip(1)) {
      final next = total + t;
      final f = t.abs() <= 9 && total >= 0 && next >= 0 ? formula(total, t) : null;
      parts.add('$total ${t < 0 ? minus : '+'} ${t.abs()} = $next${f == null ? '' : ' ($f)'}');
      total = next;
    }
    return parts.join('; ');
  }

  static Exercise chain(GenContext g) => chainWith(
        g,
        n: g.p('n', 3),
        digits: g.p('digits', 1),
        rule: g.ps('rule', 'any'),
        plus: g.pb('plus'),
        neg: g.pb('neg'),
      );

  static Exercise chainWith(GenContext g, {required int n, required int digits, required String rule, bool plus = false, bool neg = false}) {
    final list = terms(g, n: n, digits: digits, rule: rule, plus: plus, neg: neg);
    final answer = list.fold(0, (s, v) => s + v);
    final text = expr(list);
    final input = g.useInput() || neg;
    final hint = switch (rule) {
      'simple' => 'Munchoqlarni birma-bir suring: avval ${list.first}, keyin qolganlari.',
      'five' => 'Pastda joy yetmasa — kichik do‘st: +4 = +5 − 1, −3 = −5 + 2.',
      'ten' => 'Ustunda joy yetmasa — katta do‘st: +7 = +10 − 3, −8 = −10 + 2.',
      _ => 'Chapdan o‘ngga: oraliq natijani xayolda saqlab boring.',
    };
    if (input) {
      return g.custom(
        say: g.ask('$text = ?'),
        kind: ExerciseKind.input,
        concept: 'mental:chain:$text',
        input: InputTask(answer: '$answer', keys: neg ? 'signed' : 'digits'),
        hint: hint,
        explanation: _steps(list),
        meta: {'answer': answer, 'terms': list},
      );
    }
    return g.numberAnswer(
      question: '$text = ?',
      answer: answer,
      concept: 'mental:chain:$text',
      input: false,
      hint: hint,
      explanation: _steps(list),
      meta: {'terms': list},
    );
  }

  static Exercise flash(GenContext g) {
    final neg = g.pb('neg');
    final list = terms(g, n: g.p('n', 3), digits: g.p('digits', 1), rule: g.ps('rule', 'any'), plus: g.pb('plus'), neg: neg);
    final answer = list.fold(0, (s, v) => s + v);
    final shown = ['${list.first}', for (final t in list.skip(1)) signed(t)];
    return g.custom(
      say: g.ask('Sonlarni diqqat bilan kuzating va natijani yozing.'),
      kind: ExerciseKind.input,
      concept: 'mental:flash:${shown.join()}',
      input: InputTask(answer: '$answer', keys: neg ? 'signed' : 'digits', flash: shown, flashMs: g.p('ms', 1500)),
      hint: 'Har bir sonni ko‘z oldingizdagi abakusga qo‘shib boring.',
      explanation: '${expr(list)} = $answer',
      meta: {'answer': answer, 'terms': list},
    );
  }

  // ------------------------------------------------------------ tez hisoblash usullari

  static Exercise tricks(GenContext g) {
    final kinds = g.pl('kinds');
    final kind = g.pick(kinds.isEmpty ? const ['x10', 'x5'] : kinds);
    if (kind == 'divisible') return _divisible(g);
    final t = _trick(g, kind);
    return g.numberAnswer(
      question: t.question,
      answer: t.answer,
      concept: 'mental:$kind:${t.question}',
      input: g.useInput(),
      hint: t.hint,
      explanation: t.explanation,
      meta: {...t.meta, 'kind': kind},
    );
  }

  static _Trick _trick(GenContext g, String kind) {
    String n(int v) => fmtNum(v);
    switch (kind) {
      case 'table':
        final a = g.range(2, 9), b = g.range(2, 9);
        return _Trick('$a × $b = ?', a * b, 'Karra jadvalini eslang: $a × $b = $b × $a.', '$a × $b = ${a * b}', _mul(a, b));
      case 'x10':
        final a = g.range(12, 999), b = g.pick(const [10, 100]);
        return _Trick('$a × $b = ?', a * b, '$b ga ko‘paytirishda son oxiriga ${b == 10 ? 'bitta' : 'ikkita'} nol yoziladi.',
            '$a × $b = ${n(a * b)}', _mul(a, b));
      case 'x5':
        final a = g.range(12, 98);
        return _Trick('$a × 5 = ?', a * 5, '× 5 = × 10 : 2 — avval 10 ga ko‘paytiring, keyin yarmini oling.',
            '$a × 10 = ${a * 10}; ${a * 10} : 2 = ${a * 5}', _mul(a, 5));
      case 'div5':
        final a = 5 * g.range(7, 99);
        return _Trick('$a : 5 = ?', a ~/ 5, ': 5 = × 2 : 10 — ikkilantirib, 10 ga bo‘ling.',
            '$a × 2 = ${a * 2}; ${a * 2} : 10 = ${a ~/ 5}', {'a': a, 'b': 5, 'op': '/'});
      case 'x9':
        final a = g.range(12, 89);
        return _Trick('$a × 9 = ?', a * 9, '× 9 = × 10 − sonning o‘zi.', '$a × 10 = ${a * 10}; ${a * 10} − $a = ${a * 9}', _mul(a, 9));
      case 'x4':
        final a = g.range(13, 99);
        return _Trick('$a × 4 = ?', a * 4, '× 4 — ikki marta ikkilantiring.', '$a × 2 = ${a * 2}; ${a * 2} × 2 = ${a * 4}', _mul(a, 4));
      case 'x8':
        final a = g.range(12, 60);
        return _Trick('$a × 8 = ?', a * 8, '× 8 — uch marta ikkilantiring.',
            '$a → ${a * 2} → ${a * 4} → ${a * 8}', _mul(a, 8));
      case 'plus9':
        final a = g.range(11, 89), b = g.pick(const [9, 8]);
        return _Trick('$a + $b = ?', a + b, '+$b = +10 − ${10 - b}.', '$a + 10 = ${a + 10}; ${a + 10} − ${10 - b} = ${a + b}',
            {'a': a, 'b': b, 'op': '+'});
      case 'double':
        final a = g.range(13, 499);
        final tens = a - a % 10;
        return _Trick('$a × 2 = ?', a * 2, 'Bo‘laklab ikkilantiring: avval o‘nliklar, keyin birliklar.',
            '$tens × 2 = ${tens * 2}; ${a % 10} × 2 = ${a % 10 * 2}; ${tens * 2} + ${a % 10 * 2} = ${a * 2}', _mul(a, 2));
      case 'half':
        final a = 2 * g.range(12, 499);
        final big = a ~/ 20 * 20;
        final rest = a - big;
        return _Trick('$a : 2 = ?', a ~/ 2, 'Sonni juft bo‘laklarga ajratib, har birining yarmini oling.',
            rest == 0 ? '$a : 2 = ${a ~/ 2}' : '$a = $big + $rest; ${big ~/ 2} + ${rest ~/ 2} = ${a ~/ 2}', {'a': a, 'b': 2, 'op': '/'});
      case 'x11':
      case 'x11c':
        for (;;) {
          final a = g.range(12, 99);
          final d1 = a ~/ 10, d2 = a % 10;
          final s = d1 + d2;
          if (kind == 'x11' && s > 9) continue;
          final expl = s <= 9
              ? '$d1 _ $d2: o‘rtaga $d1 + $d2 = $s → ${a * 11}'
              : '$d1 + $d2 = $s: o‘rtaga ${s % 10}, $d1 ga 1 qo‘shiladi → ${a * 11}';
          return _Trick('$a × 11 = ?', a * 11, 'Raqamlarni ajrating va o‘rtasiga ularning yig‘indisini yozing.', expl, _mul(a, 11));
        }
      case 'x25':
        final a = 4 * g.range(3, 30);
        return _Trick('$a × 25 = ?', a * 25, '× 25 = × 100 : 4.', '$a : 4 = ${a ~/ 4}; ${a ~/ 4} × 100 = ${n(a * 25)}', _mul(a, 25));
      case 'x15':
        final a = 2 * g.range(6, 49);
        return _Trick('$a × 15 = ?', a * 15, '× 15 = × 10 + uning yarmi.', '$a × 10 = ${a * 10}; ${a * 10} + ${a * 5} = ${n(a * 15)}', _mul(a, 15));
      case 'x99':
        final a = g.range(12, 99);
        return _Trick('$a × 99 = ?', a * 99, '× 99 = × 100 − sonning o‘zi.', '$a × 100 = ${n(a * 100)}; ${n(a * 100)} − $a = ${n(a * 99)}', _mul(a, 99));
      case 'x125':
        final a = 8 * g.range(2, 40);
        return _Trick('$a × 125 = ?', a * 125, '× 125 = × 1000 : 8.', '$a : 8 = ${a ~/ 8}; ${a ~/ 8} × 1000 = ${n(a * 125)}', _mul(a, 125));
      case 'plus99':
        final a = g.range(101, 899), b = g.pick(const [99, 98, 97, 999]);
        final round = b > 100 ? 1000 : 100;
        return _Trick('$a + $b = ?', a + b, '+$b = +$round − ${round - b}.',
            '$a + $round = ${n(a + round)}; ${n(a + round)} − ${round - b} = ${n(a + b)}', {'a': a, 'b': b, 'op': '+'});
      case 'minus99':
        final a = g.range(150, 999), b = g.pick(const [99, 98, 97, 95]);
        return _Trick('$a − $b = ?', a - b, '−$b = −100 + ${100 - b}.', '$a − 100 = ${a - 100}; ${a - 100} + ${100 - b} = ${a - b}',
            {'a': a, 'b': b, 'op': '-'});
      case 'x2d1d':
        final a = g.range(12, 99), b = g.range(3, 9);
        final t = a - a % 10;
        return _Trick('$a × $b = ?', a * b, 'Sonni o‘nlik va birlikka ajrating: ($t + ${a % 10}) × $b.',
            '$t × $b = ${t * b}; ${a % 10} × $b = ${a % 10 * b}; ${t * b} + ${a % 10 * b} = ${a * b}', _mul(a, b));
      case 'x3d1d':
        final a = g.range(102, 999), b = g.range(2, 9);
        final h = a - a % 100, r = a % 100;
        return _Trick('$a × $b = ?', a * b, 'Yuzliklarni alohida, qolganini alohida ko‘paytiring.',
            '$h × $b = ${n(h * b)}; $r × $b = ${r * b}; jami ${n(a * b)}', _mul(a, b));
      case 'x2d2d':
        final a = g.range(12, 49), b = g.range(11, 19);
        return _Trick('$a × $b = ?', a * b, '$a × $b = $a × 10 + $a × ${b - 10}.',
            '$a × 10 = ${a * 10}; $a × ${b - 10} = ${a * (b - 10)}; ${a * 10} + ${a * (b - 10)} = ${a * b}', _mul(a, b));
      case 'sq5':
        final k = g.range(1, 9);
        final a = 10 * k + 5;
        return _Trick('$a × $a = ?', a * a, 'O‘nliklar sonini keyingi songa ko‘paytirib, oxiriga 25 yozing.',
            '$k × ${k + 1} = ${k * (k + 1)} → ${n(a * a)}', _mul(a, a));
      case 'sq50':
        final d = g.pick(const [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
        final a = 50 + d;
        final head = 25 + d, tail = d * d;
        return _Trick('$a × $a = ?', a * a, '50 dan farqni 25 ga qo‘shing (yuzlar) va farqning kvadratini oxiriga yozing.',
            '25 ${d < 0 ? '−' : '+'} ${d.abs()} = $head → ${head * 100}; ${d.abs()} × ${d.abs()} = $tail; ${head * 100} + $tail = ${n(a * a)}',
            _mul(a, a));
      case 'sq2d':
        final a = g.range(11, 99);
        final t = a - a % 10, o = a % 10;
        return _Trick('$a × $a = ?', a * a, '($t + $o) × ($t + $o) = $t × $t + 2 × $t × $o + $o × $o.',
            '${t * t} + ${2 * t * o} + ${o * o} = ${n(a * a)}', _mul(a, a));
      case 'cube':
        final a = g.range(2, 12);
        return _Trick('$a × $a × $a = ?', a * a * a, 'Avval $a × $a = ${a * a}, keyin yana $a ga ko‘paytiring.',
            '$a × $a = ${a * a}; ${a * a} × $a = ${n(a * a * a)}', {'a': a, 'op': 'cube'});
      case 'diffsq':
        final m = 10 * g.range(2, 9), d = g.range(1, 4);
        final a = m - d, b = m + d;
        return _Trick('$a × $b = ?', a * b, 'Ikkala son $m dan bir xil uzoqlikda: ($m − $d) × ($m + $d) = $m × $m − $d × $d.',
            '${n(m * m)} − ${d * d} = ${n(a * b)}', _mul(a, b));
      case 'near100':
        final a = g.range(91, 99), b = g.range(91, 99);
        final da = 100 - a, db = 100 - b;
        final tail = da * db;
        return _Trick('$a × $b = ?', a * b, '100 dan farqlarini toping: $da va $db.',
            '$a − $db = ${a - db} (boshi); $da × $db = ${tail.toString().padLeft(2, '0')} (oxiri) → ${n(a * b)}', _mul(a, b));
      case 'pct_easy':
      case 'pct':
      case 'pct_hard':
        final p = g.pick(switch (kind) {
          'pct_easy' => const [10, 50],
          'pct' => const [10, 50, 25, 20],
          _ => const [5, 75, 1, 15, 30],
        });
        final unit = switch (p) { 10 || 30 => 10, 50 => 2, 25 || 75 => 4, 20 => 5, 5 || 15 => 20, _ => 100 };
        final a = unit * g.range(p == 1 ? 2 : 3, p == 1 ? 60 : (unit >= 20 ? 40 : 90));
        final answer = a * p ~/ 100;
        final how = switch (p) {
          10 => '10% — sonning o‘ndan biri: $a : 10 = $answer',
          50 => '50% — yarmi: $a : 2 = $answer',
          25 => '25% — to‘rtdan biri: $a : 4 = $answer',
          20 => '20% — beshdan biri: $a : 5 = $answer',
          5 => '5% — 10% ning yarmi: $a : 10 = ${a ~/ 10}; ${a ~/ 10} : 2 = $answer',
          75 => '75% — to‘rtdan uchi: $a : 4 = ${a ~/ 4}; ${a ~/ 4} × 3 = $answer',
          15 => '15% = 10% + 5%: ${a ~/ 10} + ${a ~/ 20} = $answer',
          30 => '30% — 10% ning 3 barobari: ${a ~/ 10} × 3 = $answer',
          _ => '1% — sonning yuzdan biri: $a : 100 = $answer',
        };
        return _Trick('$a ning $p% ini toping.', answer, 'Avval 10% yoki 1% ni toping, keyin kerakli qismini oling.', how,
            {'a': a, 'b': p, 'op': 'pct'});
      case 'pct_up':
      case 'pct_down':
        final p = g.pick(const [10, 20, 25, 50, 5, 15]);
        final unit = switch (p) { 10 => 10, 50 => 2, 25 => 4, 20 => 5, _ => 20 };
        final a = unit * g.range(3, unit >= 20 ? 30 : 60);
        final part = a * p ~/ 100;
        final up = kind == 'pct_up';
        return _Trick('$a ni $p foizga ${up ? 'oshiring' : 'kamaytiring'}.', up ? a + part : a - part,
            'Avval $a ning $p foizini toping, keyin ${up ? 'qo‘shing' : 'ayiring'}.',
            '$a ning $p% i = $part; $a ${up ? '+' : '−'} $part = ${up ? a + part : a - part}', {'a': a, 'b': p, 'op': up ? 'pct_up' : 'pct_down'});
      case 'frac_of':
        final den = g.pick(const [2, 3, 4, 5, 8, 10]);
        final top = g.range(1, den - 1);
        if (gcd(top, den) != 1) return _trick(g, kind);
        final a = den * g.range(3, 40);
        return _Trick('$a ning $top/$den qismini toping.', a ~/ den * top, 'Avval $den ga bo‘ling, keyin $top ga ko‘paytiring.',
            '$a : $den = ${a ~/ den}; ${a ~/ den} × $top = ${a ~/ den * top}', {'a': a, 'num': top, 'den': den, 'op': 'frac'});
      case 'pow2':
        final k = g.range(2, 12);
        final v = 1 << k;
        return _Trick('2 ning $k-darajasi nechaga teng?', v, 'Har safar oldingi sonni ikkilantiring: 2, 4, 8, 16 …',
            [for (var i = 1; i <= k; i++) 1 << i].join(' → '), {'a': 2, 'b': k, 'op': 'pow'});
      case 'sqrt':
        final r = g.range(11, 30);
        return _Trick('Qaysi sonning kvadrati ${r * r} ga teng?', r,
            'Oxirgi raqamga va yaxlit o‘nliklarning kvadratlariga qarang (20 × 20 = 400, 30 × 30 = 900).',
            '$r × $r = ${r * r}', {'a': r * r, 'op': 'sqrt'});
      case 'gauss':
        final last = 10 * g.range(1, 10) + g.pick(const [0, 0, 0, 5]);
        final sum = last * (last + 1) ~/ 2;
        return _Trick('1 + 2 + 3 + … + $last = ?', sum, 'Chetdagi sonlarni juftlang: 1 + $last, 2 + ${last - 1} …',
            last.isEven
                ? '1 + $last = ${last + 1}; juftlar soni ${last ~/ 2}; ${last + 1} × ${last ~/ 2} = ${n(sum)}'
                : '($last × ${last + 1}) : 2 = ${n(sum)}',
            {'a': last, 'op': 'gauss'});
      default:
        throw StateError('Noma’lum usul: $kind');
    }
  }

  static Map<String, Object> _mul(int a, int b) => {'a': a, 'b': b, 'op': '*'};

  /// Bo'linish belgilari: variantlardan aynan bittasi [k] ga qoldiqsiz bo'linadi.
  static Exercise _divisible(GenContext g) {
    final k = g.pick(const [3, 9, 4, 6]);
    final answer = k * g.range(100 ~/ k + 1, 999 ~/ k);
    final wrong = <int>{};
    while (wrong.length < 3) {
      final v = g.range(101, 999);
      if (v % k != 0 && v != answer) wrong.add(v);
    }
    final digits = '$answer'.split('').map(int.parse).toList();
    final sum = digits.fold(0, (s, v) => s + v);
    final why = switch (k) {
      4 => 'Oxirgi ikki raqam ${answer % 100} — 4 ga bo‘linadi.',
      6 => '$answer — juft va raqamlari yig‘indisi $sum — 3 ga bo‘linadi.',
      _ => 'Raqamlar yig‘indisi ${digits.join(' + ')} = $sum — $k ga bo‘linadi.',
    };
    return g.choice(
      say: g.ask('Qaysi son $k ga qoldiqsiz bo‘linadi?'),
      options: [Opt.text('$answer'), for (final w in wrong) Opt.text('$w')],
      concept: 'mental:divisible:$k',
      hint: switch (k) {
        4 => '4 ga bo‘linish: oxirgi ikki raqamga qarang.',
        6 => '6 ga bo‘linish: son juft va 3 ga bo‘linishi kerak.',
        _ => '$k ga bo‘linish: raqamlar yig‘indisini toping.',
      },
      explanation: why,
      meta: {'answer': answer, 'b': k, 'op': 'divisible', 'kind': 'divisible'},
    );
  }
}

class _Trick {
  const _Trick(this.question, this.answer, this.hint, this.explanation, this.meta);

  final String question;
  final int answer;
  final String hint;
  final String explanation;
  final Map<String, Object> meta;
}
