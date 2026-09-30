import 'dart:math' as math;

import '../../models/exercise.dart';
import '../../models/visual.dart';
import '../generator_base.dart';
import 'school_base.dart';

/// 6–8-sinf matematikasi: butun sonlar, darajalar, bo'linish, algebraik ifodalar, tenglamalar,
/// proporsiya, koordinatalar, aylana, Pifagor teoremasi, chiziqli funksiya, tenglamalar sistemasi,
/// kvadrat tenglama, kvadrat ildiz, tengsizliklar, statistika, yuzalar, qisqa ko'paytirish formulalari.
///
/// Har bir generator darajadagi `modes` ro'yxatidan bittasini tanlaydi. `meta` — testlar uchun
/// mustaqil tekshiruv ma'lumoti (`op` va parametrlar).
class MathUpper {
  MathUpper._();

  static final Map<String, ExerciseGenerator> generators = {
    'integers': integers,
    'powers': powers,
    'divisibility': divisibility,
    'expr': expr,
    'linear_eq': linearEq,
    'proportion': proportion,
    'coords': coords,
    'circle': circle,
    'pythagoras': pythagoras,
    'linear_func': linearFunc,
    'system': system,
    'quadratic': quadratic,
    'roots': roots,
    'inequality': inequality,
    'stats': stats,
    'polygon_area': polygonArea,
    'abridged': abridged,
    'polygon_angles': polygonAngles,
    'decimal_ops': decimalOps,
  };

  static const String minus = '−';

  /// Manfiy son belgisi bilan: −7.
  static String sg(int v) => v < 0 ? '$minus${-v}' : '$v';

  /// Amaldan keyin manfiy son qavsda: 5 + (−3).
  static String par(int v) => v < 0 ? '(${sg(v)})' : '$v';

  /// Hadni ishorasi bilan: " + 5", " − 5" (birinchi haddan keyin).
  static String term(int v, [String x = '']) {
    if (v == 0) return '';
    final abs = v.abs();
    final body = x.isEmpty ? '$abs' : (abs == 1 ? x : '$abs$x');
    return v < 0 ? ' $minus $body' : ' + $body';
  }

  /// Birinchi had: "3x", "−x", "5".
  static String lead(int v, [String x = '']) {
    if (x.isEmpty) return sg(v);
    if (v == 1) return x;
    if (v == -1) return '$minus$x';
    return '${sg(v)}$x';
  }

  static String _mode(GenContext g, List<String> fallback) => g.pick(g.pl('modes').isEmpty ? fallback : g.pl('modes'));

  static int _nz(GenContext g, int max) {
    final v = g.range(1, max);
    return g.chance(0.5) ? -v : v;
  }

  static Exercise _answer(GenContext g, String q, int answer, String concept, String hint, String expl, Map<String, Object> meta,
          {ExerciseVisual? visual, String unit = ''}) =>
      g.numberAnswer(
        question: q,
        answer: answer,
        concept: concept,
        input: g.useInput(),
        visual: visual,
        unit: unit,
        hint: hint,
        explanation: expl,
        meta: meta,
      );

  // ------------------------------------------------------------ butun sonlar

  static Exercise integers(GenContext g) {
    final mode = _mode(g, const ['add', 'sub']);
    final max = g.p('max', 20);
    switch (mode) {
      case 'compare':
        final a = _nz(g, max);
        var b = _nz(g, max);
        if (b == a) b = -a == a ? a + 1 : -a;
        final big = math.max(a, b);
        return g.textChoice(
          question: 'Qaysi son katta: ${sg(a)} yoki ${sg(b)}?',
          answer: sg(big),
          wrong: [sg(math.min(a, b))],
          concept: 'int:cmp:$a:$b',
          options: 2,
          hint: 'Son o‘qida o‘ngroqda turgan son katta. Har qanday musbat son manfiydan katta.',
          explanation: '${sg(big)} > ${sg(math.min(a, b))}',
          meta: {'a': a, 'b': b, 'op': 'max_int', 'answer': sg(big)},
        );
      case 'abs':
        final a = _nz(g, max * 5);
        return _answer(g, '${sg(a)} sonining moduli nechaga teng?', a.abs(), 'int:abs:$a', 'Modul — sonning noldan uzoqligi, u manfiy bo‘lmaydi.',
            '${sg(a)} ning moduli ${a.abs()}', {'a': a, 'op': 'abs'});
      case 'mul':
        final a = _nz(g, 12), b = _nz(g, 12);
        return _answer(g, '${sg(a)} · ${par(b)} = ?', a * b, 'int:mul:$a:$b', 'Ishoralari bir xil bo‘lsa — musbat, har xil bo‘lsa — manfiy.',
            '${sg(a)} · ${par(b)} = ${sg(a * b)}', {'a': a, 'b': b, 'op': '*'});
      case 'div':
        final b = _nz(g, 12), q = _nz(g, 12);
        final a = b * q;
        return _answer(g, '${sg(a)} : ${par(b)} = ?', q, 'int:div:$a:$b', 'Bo‘lishda ham ishoralar qoidasi ko‘paytirishdagidek.',
            '${sg(a)} : ${par(b)} = ${sg(q)}', {'a': a, 'b': b, 'op': 'div_int'});
      case 'chain':
        final a = _nz(g, max), b = _nz(g, max), c = _nz(g, max);
        final r = a + b - c;
        return _answer(g, '${sg(a)} + ${par(b)} $minus ${par(c)} = ?', r, 'int:chain:$a:$b:$c',
            'Ayirishni qarama-qarshi sonni qo‘shish bilan almashtiring: − (−5) = + 5.', '${sg(a)} + ${par(b)} $minus ${par(c)} = ${sg(r)}',
            {'a': a, 'b': b, 'c': c, 'op': 'chain_int'});
      case 'sub':
        final a = _nz(g, max), b = _nz(g, max);
        return _answer(g, '${sg(a)} $minus ${par(b)} = ?', a - b, 'int:sub:$a:$b', 'Ayirish = qarama-qarshi sonni qo‘shish: a − b = a + (−b).',
            '${sg(a)} $minus ${par(b)} = ${sg(a)} + ${par(-b)} = ${sg(a - b)}', {'a': a, 'b': b, 'op': 'sub_int'});
      default:
        final a = _nz(g, max), b = _nz(g, max);
        return _answer(g, '${sg(a)} + ${par(b)} = ?', a + b, 'int:add:$a:$b',
            'Ishoralari bir xil — modullarni qo‘shing; har xil — kattasidan kichigini ayirib, kattasining ishorasini qo‘ying.',
            '${sg(a)} + ${par(b)} = ${sg(a + b)}', {'a': a, 'b': b, 'op': '+'});
    }
  }

  // ------------------------------------------------------------ darajalar

  static const List<String> _sup = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'];

  static String sup(int n) => n.toString().split('').map((d) => _sup[int.parse(d)]).join();

  static int ipow(int a, int n) => math.pow(a, n).toInt();

  static Exercise powers(GenContext g) {
    final mode = _mode(g, const ['value']);
    switch (mode) {
      case 'neg_base':
        final a = -g.range(2, 5), n = g.range(2, a == -2 ? 5 : 3);
        return _answer(g, '(${sg(a)})${sup(n)} = ?', ipow(a, n), 'pow:neg:$a:$n', 'Manfiy son juft darajada — musbat, toq darajada — manfiy.',
            '(${sg(a)})${sup(n)} = ${sg(ipow(a, n))}', {'a': a, 'b': n, 'op': 'pow'});
      case 'mul_rule':
        final a = g.range(2, 9), m = g.range(2, 9), n = g.range(2, 9);
        return _answer(g, '$a${sup(m)} · $a${sup(n)} = $a ning nechanchi darajasi?', m + n, 'pow:mul:$a:$m:$n',
            'Asoslari bir xil darajalar ko‘paytirilganda ko‘rsatkichlar qo‘shiladi.', '$a${sup(m)} · $a${sup(n)} = $a${sup(m + n)}',
            {'a': m, 'b': n, 'op': '+'});
      case 'div_rule':
        final a = g.range(2, 9), n = g.range(2, 7), m = n + g.range(1, 8);
        return _answer(g, '$a${sup(m)} : $a${sup(n)} = $a ning nechanchi darajasi?', m - n, 'pow:div:$a:$m:$n',
            'Asoslari bir xil darajalar bo‘linganda ko‘rsatkichlar ayiriladi.', '$a${sup(m)} : $a${sup(n)} = $a${sup(m - n)}',
            {'a': m, 'b': n, 'op': '-'});
      case 'pow10':
        final n = g.range(2, 6);
        return _answer(g, '10${sup(n)} = ?', ipow(10, n), 'pow:10:$n', '10 ning n-darajasi — 1 dan keyin n ta nol.', '10${sup(n)} = ${fmtNum(ipow(10, n))}',
            {'a': 10, 'b': n, 'op': 'pow'});
      default:
        final a = g.range(2, 10);
        final n = a <= 3 ? g.range(2, 6) : (a <= 5 ? g.range(2, 4) : g.range(2, 3));
        return _answer(g, '$a${sup(n)} = ?', ipow(a, n), 'pow:value:$a:$n', '$a${sup(n)} — $a ni o‘ziga $n marta ko‘paytirish.',
            '${List.filled(n, '$a').join(' · ')} = ${fmtNum(ipow(a, n))}', {'a': a, 'b': n, 'op': 'pow'});
    }
  }

  // ------------------------------------------------------------ bo'linish, EKUB, EKUK

  static bool isPrime(int n) {
    if (n < 2) return false;
    for (var d = 2; d * d <= n; d++) {
      if (n % d == 0) return false;
    }
    return true;
  }

  static List<int> factors(int n) {
    final out = <int>[];
    var v = n;
    for (var d = 2; v > 1; d++) {
      while (v % d == 0) {
        out.add(d);
        v ~/= d;
      }
    }
    return out;
  }

  static Exercise divisibility(GenContext g) {
    final mode = _mode(g, const ['gcd', 'lcm']);
    switch (mode) {
      case 'prime':
        final p = g.pick([for (var v = 11; v < 100; v++) if (isPrime(v)) v]);
        final wrong = <int>{};
        while (wrong.length < 3) {
          final v = g.range(10, 99);
          if (!isPrime(v)) wrong.add(v);
        }
        return g.textChoice(
          question: 'Qaysi son tub?',
          answer: '$p',
          wrong: [for (final w in wrong) '$w'],
          concept: 'div:prime:$p:${wrong.join(',')}',
          hint: 'Tub son faqat 1 ga va o‘ziga bo‘linadi. 2, 3, 5, 7 ga bo‘linishini tekshiring.',
          explanation: '$p — tub son. ${[for (final w in wrong) '$w = ${factors(w).join(' · ')}'].join('; ')}',
          meta: {'answer': p, 'op': 'prime'},
        );
      case 'divisors':
        final n = g.pick(const [6, 8, 10, 12, 15, 16, 18, 20, 24, 28, 30, 36, 40, 42, 45, 48]);
        final ds = [for (var d = 1; d <= n; d++) if (n % d == 0) d];
        return _answer(g, '$n sonining nechta natural bo‘luvchisi bor?', ds.length, 'div:count:$n', '1 va sonning o‘zini ham sanang.',
            '$n ning bo‘luvchilari: ${ds.join(', ')} — ${ds.length} ta', {'a': n, 'op': 'divisors'});
      case 'factor':
        final n = g.pick(const [12, 18, 20, 24, 28, 30, 36, 40, 42, 45, 48, 50, 54, 56, 60, 63, 66, 70, 72, 75, 78, 84, 88, 90, 98]);
        final f = factors(n);
        return _answer(g, '$n ni tub ko‘paytuvchilarga ajrating. Eng katta tub ko‘paytuvchi qaysi?', f.last, 'div:factor:$n',
            'Eng kichik tub sondan boshlab bo‘lib boring: 2, 3, 5, 7 …', '$n = ${f.join(' · ')}', {'a': n, 'op': 'max_factor'});
      case 'lcm':
        final d = g.range(2, 6), x = g.range(2, 7), y = g.range(2, 7);
        if (x == y || gcd(x, y) != 1) return divisibility(g);
        final a = d * x, b = d * y;
        final l = a * b ~/ gcd(a, b);
        return _answer(g, '$a va $b ning eng kichik umumiy karralisini toping.', l, 'div:lcm:$a:$b',
            'Kattaroq sonning karralilarini yozing va birinchi bo‘lib ikkinchisiga bo‘linadiganini tanlang.',
            'EKUK = $a · $b : ${gcd(a, b)} = $l', {'a': a, 'b': b, 'op': 'lcm'});
      default:
        final d = g.range(2, 12), x = g.range(1, 9), y = g.range(2, 9);
        if (x == y || gcd(x, y) != 1) return divisibility(g);
        final a = d * x, b = d * y;
        return _answer(g, '$a va $b ning eng katta umumiy bo‘luvchisini toping.', d, 'div:gcd:$a:$b',
            'Ikkala sonni tub ko‘paytuvchilarga ajrating va umumiylarini ko‘paytiring.',
            '$a = $d · $x, $b = $d · $y → EKUB = $d', {'a': a, 'b': b, 'op': 'gcd'});
    }
  }

  // ------------------------------------------------------------ algebraik ifodalar

  static Exercise expr(GenContext g) {
    final mode = _mode(g, const ['eval', 'like_terms']);
    switch (mode) {
      case 'like_terms':
        final count = g.range(3, 4);
        final cs = [for (var i = 0; i < count; i++) _nz(g, 9)];
        final sum = cs.fold(0, (s, v) => s + v);
        if (sum == 0) return expr(g);
        final text = '${lead(cs.first, 'x')}${cs.skip(1).map((c) => term(c, 'x')).join()}';
        return _answer(g, 'Soddalashtiring: $text. x oldidagi koeffitsiyent nechaga teng?', sum, 'expr:like:$text',
            'O‘xshash hadlarning koeffitsiyentlarini qo‘shing.', '$text = ${lead(sum, 'x')}', {'coefs': cs.join(','), 'op': 'sum_list'});
      case 'expand':
        final a = g.range(2, 9) * (g.chance(0.3) ? -1 : 1), b = _nz(g, 12);
        final inside = 'x${term(b)}';
        return _answer(g, 'Qavslarni oching: ${lead(a)}($inside) = ${lead(a, 'x')} + ?', a * b, 'expr:expand:$a:$b',
            'Qavs oldidagi sonni qavs ichidagi har bir hadga ko‘paytiring.', '${lead(a)}($inside) = ${lead(a, 'x')}${term(a * b)}',
            {'a': a, 'b': b, 'op': '*'});
      default:
        final a = _nz(g, 6), b = _nz(g, 6);
        final p = g.range(2, 5), q = _nz(g, 5);
        final value = p * a + q * b;
        final text = '${p}a${term(q, 'b')}';
        return _answer(g, 'a = ${sg(a)}, b = ${sg(b)} bo‘lsa, $text ifodaning qiymatini toping.', value, 'expr:eval:$text:$a:$b',
            'Harflar o‘rniga sonlarni qo‘ying; manfiy sonni qavsga oling.', '$p · ${par(a)}${q < 0 ? ' $minus ' : ' + '}${q.abs()} · ${par(b)} = ${sg(value)}',
            {'a': a, 'b': b, 'p': p, 'q': q, 'op': 'pa_qb'});
    }
  }

  // ------------------------------------------------------------ chiziqli tenglama

  static Exercise linearEq(GenContext g) {
    final mode = _mode(g, const ['one']);
    final neg = g.pb('neg');
    final x = neg ? _nz(g, 10) : g.range(1, 15);
    switch (mode) {
      case 'paren':
        final a = g.range(2, 9), b = _nz(g, 9);
        final c = a * (x + b);
        final text = '$a(x${term(b)}) = ${sg(c)}';
        return _answer(g, 'Tenglamani yeching: $text. x = ?', x, 'eq:paren:$text', 'Ikkala tomonni $a ga bo‘ling, keyin ${sg(b)} ni o‘tkazing.',
            'x${term(b)} = ${sg(c ~/ a)} → x = ${sg(x)}', {'answer': x, 'eq': 'paren', 'a': a, 'b': b, 'c': c});
      case 'both':
        final a = g.range(2, 9);
        var c = g.range(1, 8);
        if (c == a) c = a + 1;
        final b = _nz(g, 15);
        final d = a * x + b - c * x;
        final text = '${a}x${term(b)} = ${lead(c, 'x')}${term(d)}';
        return _answer(g, 'Tenglamani yeching: $text. x = ?', x, 'eq:both:$text', 'x li hadlarni bir tomonga, sonlarni ikkinchi tomonga o‘tkazing.',
            '${lead(a - c, 'x')} = ${sg(d - b)} → x = ${sg(x)}', {'answer': x, 'eq': 'both', 'a': a, 'b': b, 'c': c, 'd': d});
      default:
        final a = g.range(2, 9) * (neg && g.chance(0.3) ? -1 : 1), b = _nz(g, 20);
        final c = a * x + b;
        final text = '${lead(a, 'x')}${term(b)} = ${sg(c)}';
        return _answer(g, 'Tenglamani yeching: $text. x = ?', x, 'eq:one:$text', 'Avval ${sg(b)} ni o‘ng tomonga o‘tkazing, keyin ${sg(a)} ga bo‘ling.',
            '${lead(a, 'x')} = ${sg(c - b)} → x = ${sg(x)}', {'answer': x, 'eq': 'one', 'a': a, 'b': b, 'c': c});
    }
  }

  // ------------------------------------------------------------ proporsiya

  static Exercise proportion(GenContext g) {
    final mode = _mode(g, const ['solve', 'direct']);
    switch (mode) {
      case 'direct':
        final kg = g.range(2, 6), price = g.range(3, 25) * 1000, want = g.range(2, 9);
        if (want == kg) return proportion(g);
        return _answer(g, '$kg kg olma ${fmtNum(kg * price)} so‘m turadi. $want kg olma qancha turadi?', want * price, 'prop:direct:$kg:$price:$want',
            'To‘g‘ri proporsiya: avval 1 kg narxini toping.', '1 kg — ${fmtNum(price)} so‘m; $want · ${fmtNum(price)} = ${fmtNum(want * price)} so‘m',
            {'a': kg, 'b': price, 'c': want, 'op': 'direct'});
      case 'inverse':
        for (;;) {
          final w1 = g.range(2, 12), d1 = g.range(2, 12), w2 = g.range(2, 12);
          if (w1 == w2 || (w1 * d1) % w2 != 0) continue;
          return _answer(g, '$w1 ishchi ishni $d1 kunda bajaradi. Shu ishni $w2 ishchi necha kunda bajaradi?', w1 * d1 ~/ w2,
              'prop:inverse:$w1:$d1:$w2', 'Teskari proporsiya: ishchilar ko‘paysa, kunlar kamayadi. Butun ish: $w1 · $d1.',
              '$w1 · $d1 = ${w1 * d1} kishi-kun; ${w1 * d1} : $w2 = ${w1 * d1 ~/ w2} kun', {'a': w1, 'b': d1, 'c': w2, 'op': 'inverse'});
        }
      case 'scale':
        final (scale, km) = g.pick(const [('100 000', 1), ('200 000', 2), ('500 000', 5), ('1 000 000', 10)]);
        final cm = g.range(2, 12);
        return _answer(g, 'Xarita masshtabi 1 : $scale. Xaritada ikki shahar orasi $cm sm. Haqiqiy masofa necha km?', cm * km,
            'prop:scale:$scale:$cm', 'Xaritadagi 1 sm haqiqatda $km km ga teng.', '$cm · $km = ${cm * km} km', {'a': cm, 'b': km, 'op': '*'});
      default:
        final a = g.range(1, 9), b = g.range(2, 9), k = g.range(2, 9);
        if (a == b) return proportion(g);
        return _answer(g, 'Proporsiyani yeching: $a : $b = ${a * k} : x. x = ?', b * k, 'prop:solve:$a:$b:$k',
            'Proporsiyaning chetki hadlari ko‘paytmasi o‘rta hadlari ko‘paytmasiga teng.', '$a · x = $b · ${a * k} → x = ${b * k}',
            {'a': a, 'b': b, 'c': a * k, 'op': 'prop'});
    }
  }

  // ------------------------------------------------------------ koordinatalar

  static const List<String> _quarters = ['I chorak', 'II chorak', 'III chorak', 'IV chorak'];

  static Exercise coords(GenContext g) {
    final mode = _mode(g, const ['quadrant', 'symmetric']);
    final x = _nz(g, 9), y = _nz(g, 9);
    switch (mode) {
      case 'quadrant':
        final q = x > 0 ? (y > 0 ? 0 : 3) : (y > 0 ? 1 : 2);
        return g.textChoice(
          question: 'A nuqtaning koordinatalari: x = ${sg(x)}, y = ${sg(y)}. U qaysi chorakda yotadi?',
          answer: _quarters[q],
          wrong: [for (var i = 0; i < 4; i++) if (i != q) _quarters[i]],
          concept: 'coord:quad:$x:$y',
          hint: 'I chorak: x > 0, y > 0; II: x < 0, y > 0; III: x < 0, y < 0; IV: x > 0, y < 0.',
          explanation: 'x ${x > 0 ? '> 0' : '< 0'}, y ${y > 0 ? '> 0' : '< 0'} → ${_quarters[q]}',
          meta: {'a': x, 'b': y, 'op': 'quadrant', 'answer': _quarters[q]},
        );
      case 'distance':
        final a = _nz(g, 12);
        var b = _nz(g, 12);
        if (a == b) b = a + g.range(1, 5);
        return _answer(g, 'Son o‘qida A nuqta ${sg(a)} da, B nuqta ${sg(b)} da. AB masofa nechaga teng?', (a - b).abs(), 'coord:dist:$a:$b',
            'Masofa = kattasidan kichigini ayirish (modul).', '${sg(math.max(a, b))} $minus ${par(math.min(a, b))} = ${(a - b).abs()}',
            {'a': a, 'b': b, 'op': 'dist'});
      case 'midpoint':
        final a = _nz(g, 12), d = g.range(1, 8);
        final b = a + 2 * d;
        return _answer(g, 'Son o‘qida A nuqta ${sg(a)} da, B nuqta ${sg(b)} da. AB kesma o‘rtasining koordinatasi nechaga teng?', a + d,
            'coord:mid:$a:$b', 'O‘rtasi = (a + b) : 2.', '(${sg(a)} + ${par(b)}) : 2 = ${sg(a + d)}', {'a': a, 'b': b, 'op': 'mid'});
      default:
        final axis = g.range(0, 2);
        final askX = g.chance(0.5);
        final nx = axis == 0 ? x : -x, ny = axis == 1 ? y : -y;
        final name = const ['OX o‘qiga', 'OY o‘qiga', 'koordinata boshiga'][axis];
        return _answer(g, 'A nuqta: x = ${sg(x)}, y = ${sg(y)}. Unga $name nisbatan simmetrik nuqtaning ${askX ? 'x' : 'y'} koordinatasi nechaga teng?',
            askX ? nx : ny, 'coord:sym:$x:$y:$axis:$askX',
            'OX ga nisbatan — y ishorasi, OY ga nisbatan — x ishorasi, boshiga nisbatan — ikkalasining ishorasi o‘zgaradi.',
            'Simmetrik nuqta: x = ${sg(nx)}, y = ${sg(ny)}', {'a': x, 'b': y, 'axis': axis, 'x': askX ? 1 : 0, 'op': 'sym'});
    }
  }

  // ------------------------------------------------------------ aylana (π ≈ 3,14)

  /// Yuzdan birliklarda berilgan sonni yozish: 3140 → "31,4".
  static String hund(int h) => fmtDec(h / 100);

  static Exercise circle(GenContext g) {
    final mode = _mode(g, const ['length', 'area']);
    final r = g.range(1, 10);
    String ans(int h) => hund(h);
    switch (mode) {
      case 'area':
        final h = 314 * r * r;
        return g.textAnswer(
          question: 'Doira radiusi $r sm. Doira yuzini toping. π ≈ 3,14 deb oling.',
          answer: ans(h),
          keys: 'decimal',
          unit: 'sm²',
          concept: 'circle:area:$r',
          hint: 'S = π · r · r',
          explanation: '3,14 · $r · $r = ${ans(h)} sm²',
          meta: {'r': r, 'op': 'circle_area', 'hund': h},
        );
      case 'diameter':
        final d = 2 * r;
        return _answer(g, 'Aylana uzunligi ${ans(314 * d)} sm. Uning diametri necha santimetr? π ≈ 3,14 deb oling.', d, 'circle:d:$r',
            'C = π · d, demak d = C : π.', '${ans(314 * d)} : 3,14 = $d sm', {'hund': 314 * d, 'op': 'circle_d'});
      default:
        final h = 628 * r;
        return g.textAnswer(
          question: 'Aylana radiusi $r sm. Aylana uzunligini toping. π ≈ 3,14 deb oling.',
          answer: ans(h),
          keys: 'decimal',
          unit: 'sm',
          concept: 'circle:length:$r',
          hint: 'C = 2 · π · r',
          explanation: '2 · 3,14 · $r = ${ans(h)} sm',
          meta: {'r': r, 'op': 'circle_length', 'hund': h},
        );
    }
  }

  // ------------------------------------------------------------ Pifagor teoremasi

  static const List<(int, int, int)> _triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)];

  static Exercise pythagoras(GenContext g) {
    final mode = _mode(g, const ['hyp', 'leg']);
    final t = g.pick(_triples);
    final k = t.$3 > 20 ? 1 : g.range(1, t.$3 > 13 ? 2 : 4);
    final a = t.$1 * k, b = t.$2 * k, c = t.$3 * k;
    switch (mode) {
      case 'check':
        final right = g.chance(0.5);
        final c2 = right ? c : c + 1;
        return g.textChoice(
          question: 'Tomonlari $a, $b va $c2 bo‘lgan uchburchak to‘g‘ri burchaklimi?',
          answer: right ? 'Ha' : 'Yo‘q',
          wrong: [right ? 'Yo‘q' : 'Ha'],
          concept: 'pyth:check:$a:$b:$c2',
          options: 2,
          hint: 'Ikki kichik tomon kvadratlari yig‘indisi eng katta tomon kvadratiga tengmi?',
          explanation: '$a · $a + $b · $b = ${a * a + b * b}; $c2 · $c2 = ${c2 * c2}',
          meta: {'a': a, 'b': b, 'c': c2, 'op': 'pyth_check', 'answer': right ? 'Ha' : 'Yo‘q'},
        );
      case 'leg':
        final swap = g.chance(0.5);
        final known = swap ? b : a, unknown = swap ? a : b;
        return _answer(g, 'To‘g‘ri burchakli uchburchakning gipotenuzasi $c sm, bir kateti $known sm. Ikkinchi katetini toping.', unknown,
            'pyth:leg:$c:$known', 'Katet kvadrati = gipotenuza kvadrati − ikkinchi katet kvadrati.',
            '$c · $c $minus $known · $known = ${unknown * unknown} → $unknown sm', {'a': c, 'b': known, 'op': 'leg'}, unit: 'sm');
      default:
        return _answer(g, 'To‘g‘ri burchakli uchburchakning katetlari $a sm va $b sm. Gipotenuzasini toping.', c, 'pyth:hyp:$a:$b',
            'Gipotenuza kvadrati = katetlar kvadratlari yig‘indisi.', '$a · $a + $b · $b = ${c * c} → $c sm', {'a': a, 'b': b, 'op': 'hyp'},
            unit: 'sm');
    }
  }

  // ------------------------------------------------------------ chiziqli funksiya

  static Exercise linearFunc(GenContext g) {
    final mode = _mode(g, const ['value', 'root']);
    final k = _nz(g, 6), b = _nz(g, 10);
    final f = 'y = ${lead(k, 'x')}${term(b)}';
    switch (mode) {
      case 'root':
        final x0 = _nz(g, 8);
        final bb = -k * x0;
        final f2 = 'y = ${lead(k, 'x')}${term(bb)}';
        return _answer(g, '$f2 funksiya grafigi OX o‘qini qaysi nuqtada kesadi? x = ?', x0, 'func:root:$k:$bb',
            'OX o‘qida y = 0: ${lead(k, 'x')}${term(bb)} = 0 tenglamani yeching.', 'x = ${sg(-bb)} : ${par(k)} = ${sg(x0)}',
            {'k': k, 'b': bb, 'op': 'root'});
      case 'intercept':
        return _answer(g, '$f funksiya grafigi OY o‘qini qaysi nuqtada kesadi? y = ?', b, 'func:icpt:$k:$b', 'OY o‘qida x = 0.',
            'x = 0 → y = ${sg(b)}', {'k': k, 'b': b, 'op': 'intercept'});
      case 'slope':
        final x1 = g.range(-5, 3), dx = g.range(1, 4);
        final x2 = x1 + dx;
        final y1 = k * x1 + b, y2 = k * x2 + b;
        return _answer(g, 'To‘g‘ri chiziq A nuqta x = ${sg(x1)}, y = ${sg(y1)} va B nuqta x = ${sg(x2)}, y = ${sg(y2)} orqali o‘tadi. Burchak koeffitsiyenti k nechaga teng?',
            k, 'func:slope:$x1:$y1:$x2:$y2', 'k = (y₂ − y₁) : (x₂ − x₁).', 'k = (${sg(y2)} $minus ${par(y1)}) : ($x2 $minus ${par(x1)}) = ${sg(k)}',
            {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'op': 'slope'});
      default:
        final x = _nz(g, 6);
        return _answer(g, '$f funksiyada x = ${sg(x)} bo‘lsa, y nechaga teng?', k * x + b, 'func:value:$k:$b:$x', 'x o‘rniga ${sg(x)} ni qo‘ying.',
            'y = ${sg(k)} · ${par(x)}${term(b)} = ${sg(k * x + b)}', {'k': k, 'b': b, 'x': x, 'op': 'value'});
    }
  }

  // ------------------------------------------------------------ tenglamalar sistemasi

  static Exercise system(GenContext g) {
    final mode = _mode(g, const ['sumdiff', 'elim']);
    final x = g.range(1, 15), y = g.range(1, 12);
    final askX = g.chance(0.5);
    switch (mode) {
      case 'word':
        final big = math.max(x, y) + 5, small = math.min(x, y);
        return _answer(g, 'Ikki sonning yig‘indisi ${big + small}, ayirmasi ${big - small}. ${askX ? 'Kattasini' : 'Kichigini'} toping.',
            askX ? big : small, 'sys:word:$big:$small', 'Yig‘indi va ayirmani qo‘shsangiz, katta sonning ikki barobari chiqadi.',
            '(${big + small} + ${big - small}) : 2 = $big; $small', {'s': big + small, 'd': big - small, 'x': askX ? 1 : 0, 'op': 'sumdiff'});
      case 'elim':
        final a = g.range(2, 5);
        return _answer(g, 'Sistemani yeching: ${a}x + y = ${a * x + y}, x + y = ${x + y}. ${askX ? 'x' : 'y'} = ?', askX ? x : y,
            'sys:elim:$a:$x:$y', 'Birinchi tenglamadan ikkinchisini ayiring — y yo‘qoladi.',
            '${a - 1 == 1 ? '' : a - 1}x = ${(a - 1) * x} → x = $x, y = $y', {'a': a, 'p': a * x + y, 'q': x + y, 'x': askX ? 1 : 0, 'op': 'elim'});
      default:
        final big = math.max(x, y) + 3, small = math.min(x, y);
        return _answer(g, 'Sistemani yeching: x + y = ${big + small}, x $minus y = ${big - small}. ${askX ? 'x' : 'y'} = ?', askX ? big : small,
            'sys:sd:$big:$small', 'Tenglamalarni qo‘shing: 2x = …', '2x = ${2 * big} → x = $big, y = $small',
            {'s': big + small, 'd': big - small, 'x': askX ? 1 : 0, 'op': 'sumdiff'});
    }
  }

  // ------------------------------------------------------------ kvadrat tenglama

  /// x² + bx + c ko'rinishidagi uchhad matni.
  static String trinomial(int a, int b, int c) => '${lead(a, 'x²')}${term(b, 'x')}${term(c)}';

  static Exercise quadratic(GenContext g) {
    final mode = _mode(g, const ['roots']);
    final p = _nz(g, 9);
    var q = _nz(g, 9);
    if (q == p) q = p + 1 == 0 ? p + 2 : p + 1;
    final b = -(p + q), c = p * q;
    final eq = '${trinomial(1, b, c)} = 0';
    switch (mode) {
      case 'vieta_sum':
        return _answer(g, '$eq tenglama ildizlarining yig‘indisi nechaga teng?', p + q, 'quad:sum:$b:$c', 'Viyet teoremasi: x₁ + x₂ = −b.',
            'x₁ + x₂ = ${sg(-b)}', {'b': b, 'c': c, 'op': 'vieta_sum'});
      case 'vieta_prod':
        return _answer(g, '$eq tenglama ildizlarining ko‘paytmasi nechaga teng?', c, 'quad:prod:$b:$c', 'Viyet teoremasi: x₁ · x₂ = c.',
            'x₁ · x₂ = ${sg(c)}', {'b': b, 'c': c, 'op': 'vieta_prod'});
      case 'disc':
        final a = g.range(1, 3), bb = _nz(g, 9), cc = _nz(g, 9);
        return _answer(g, '${trinomial(a, bb, cc)} = 0 tenglamaning diskriminantini toping.', bb * bb - 4 * a * cc, 'quad:disc:$a:$bb:$cc',
            'D = b · b − 4 · a · c', 'D = ${par(bb)} · ${par(bb)} $minus 4 · $a · ${par(cc)} = ${sg(bb * bb - 4 * a * cc)}',
            {'a': a, 'b': bb, 'c': cc, 'op': 'disc'});
      case 'incomplete':
        final n = g.range(2, 12);
        if (g.chance(0.5)) {
          return _answer(g, 'x² $minus ${n * n} = 0 tenglamaning musbat ildizini toping.', n, 'quad:inc1:$n', 'x² = ${n * n}.', 'x = $n yoki x = $minus$n',
              {'b': 0, 'c': -n * n, 'op': 'root_max'});
        }
        return _answer(g, 'x²${term(-n, 'x')} = 0 tenglamaning noldan farqli ildizini toping.', n, 'quad:inc2:$n', 'x ni qavsdan chiqaring: x(x − $n) = 0.',
            'x = 0 yoki x = $n', {'b': -n, 'c': 0, 'op': 'root_max'});
      default:
        final big = g.chance(0.5);
        return _answer(g, '$eq tenglamaning ${big ? 'katta' : 'kichik'} ildizini toping.', big ? math.max(p, q) : math.min(p, q),
            'quad:roots:$b:$c:$big', 'Viyet teoremasi: yig‘indisi ${sg(-b)}, ko‘paytmasi ${sg(c)} bo‘lgan ikki sonni toping.',
            'x₁ = ${sg(math.min(p, q))}, x₂ = ${sg(math.max(p, q))}', {'b': b, 'c': c, 'op': big ? 'root_max' : 'root_min'});
    }
  }

  // ------------------------------------------------------------ kvadrat ildiz

  static Exercise roots(GenContext g) {
    final mode = _mode(g, const ['sqrt', 'estimate']);
    switch (mode) {
      case 'estimate':
        final n = g.range(2, 14);
        final v = n * n + g.range(1, 2 * n);
        return g.textChoice(
          question: '√$v qaysi ikki ketma-ket butun son orasida joylashgan?',
          answer: '$n va ${n + 1}',
          wrong: ['${n - 1} va $n', '${n + 1} va ${n + 2}', '${n + 2} va ${n + 3}'],
          concept: 'root:est:$v',
          hint: '$v ga eng yaqin to‘liq kvadratlarni toping.',
          explanation: '$n · $n = ${n * n} < $v < ${(n + 1) * (n + 1)} = ${n + 1} · ${n + 1}',
          meta: {'a': v, 'op': 'sqrt_between', 'answer': '$n va ${n + 1}'},
        );
      case 'simplify':
        final k = g.range(2, 9), m = g.pick(const [2, 3, 5]);
        return _answer(g, '√${k * k * m} ni a√$m ko‘rinishida yozing. a = ?', k, 'root:simp:$k:$m', 'Ildiz ostidan to‘liq kvadratni chiqaring.',
            '√${k * k * m} = √(${k * k} · $m) = $k√$m', {'a': k * k * m, 'b': m, 'op': 'sqrt_simplify'});
      case 'product':
        final m = g.pick(const [2, 3, 5]), a = g.range(1, 4), b = g.range(1, 4);
        final x = m * a * a, y = m * b * b;
        return _answer(g, '√$x · √$y = ?', m * a * b, 'root:prod:$x:$y', '√a · √b = √(a · b).', '√${x * y} = ${m * a * b}',
            {'a': x, 'b': y, 'op': 'sqrt_product'});
      default:
        final n = g.range(2, 25);
        return _answer(g, '√${n * n} = ?', n, 'root:sqrt:$n', 'Qaysi sonning kvadrati ${n * n} ga teng?', '$n · $n = ${n * n}',
            {'a': n * n, 'op': 'sqrt'});
    }
  }

  // ------------------------------------------------------------ tengsizliklar

  static Exercise inequality(GenContext g) {
    final mode = _mode(g, const ['min_int', 'max_int']);
    switch (mode) {
      case 'count':
        final lo = -g.range(0, 6), hi = g.range(1, 7);
        final strictLo = g.chance(0.5), strictHi = g.chance(0.5);
        final count = (hi - lo + 1) - (strictLo ? 1 : 0) - (strictHi ? 1 : 0);
        return _answer(g, '${sg(lo)} ${strictLo ? '<' : '≤'} x ${strictHi ? '<' : '≤'} $hi qo‘sh tengsizlikni qanoatlantiradigan nechta butun son bor?',
            count, 'ineq:count:$lo:$hi:$strictLo:$strictHi', '“<” — chegara kirmaydi, “≤” — chegara ham kiradi.',
            '${[for (var v = lo + (strictLo ? 1 : 0); v <= hi - (strictHi ? 1 : 0); v++) sg(v)].join(', ')} — $count ta',
            {'lo': lo, 'hi': hi, 'sl': strictLo ? 1 : 0, 'sh': strictHi ? 1 : 0, 'op': 'count_int'});
      case 'max_int':
        final a = g.range(2, 6), bound = _nz(g, 8), b = _nz(g, 12);
        final strict = g.chance(0.5);
        final c = a * bound + b;
        final answer = strict ? bound - 1 : bound;
        return _answer(g, '${a}x${term(b)} ${strict ? '<' : '≤'} ${sg(c)} tengsizlikning eng katta butun yechimini toping.', answer,
            'ineq:max:$a:$b:$c:$strict', 'Tenglamadagidek yeching, lekin belgini saqlang.', 'x ${strict ? '<' : '≤'} ${sg(bound)} → ${sg(answer)}',
            {'a': a, 'b': b, 'c': c, 's': strict ? 1 : 0, 'op': 'ineq_max'});
      default:
        final a = g.range(2, 6), bound = _nz(g, 8), b = _nz(g, 12);
        final strict = g.chance(0.5);
        final c = a * bound + b;
        final answer = strict ? bound + 1 : bound;
        return _answer(g, '${a}x${term(b)} ${strict ? '>' : '≥'} ${sg(c)} tengsizlikning eng kichik butun yechimini toping.', answer,
            'ineq:min:$a:$b:$c:$strict', 'Tenglamadagidek yeching, lekin belgini saqlang.', 'x ${strict ? '>' : '≥'} ${sg(bound)} → ${sg(answer)}',
            {'a': a, 'b': b, 'c': c, 's': strict ? 1 : 0, 'op': 'ineq_min'});
    }
  }

  // ------------------------------------------------------------ statistika

  static Exercise stats(GenContext g) {
    final mode = _mode(g, const ['mean', 'median']);
    switch (mode) {
      case 'median':
        final count = g.pick(const [5, 7]);
        final list = [for (var i = 0; i < count; i++) g.range(1, 40)];
        final sorted = [...list]..sort();
        final med = sorted[sorted.length ~/ 2];
        return _answer(g, 'Sonlar: ${list.join(', ')}. Medianani toping.', med, 'stat:median:${list.join(',')}',
            'Sonlarni o‘sish tartibida yozing va o‘rtadagisini oling.', '${sorted.join(', ')} → $med', {'list': list.join(','), 'op': 'median'});
      case 'mode':
        final m = g.range(1, 20);
        final others = <int>{};
        while (others.length < 4) {
          final v = g.range(1, 20);
          if (v != m) others.add(v);
        }
        final list = [m, m, m, ...others]..shuffle(g.rng);
        return _answer(g, 'Sonlar: ${list.join(', ')}. Modani toping.', m, 'stat:mode:${list.join(',')}', 'Moda — eng ko‘p takrorlangan son.',
            '$m — 3 marta takrorlangan', {'list': list.join(','), 'op': 'mode'});
      case 'range':
        final list = [for (var i = 0; i < 6; i++) g.range(1, 60)];
        final r = list.reduce(math.max) - list.reduce(math.min);
        return _answer(g, 'Sonlar: ${list.join(', ')}. Qatorning kengligini toping.', r, 'stat:range:${list.join(',')}',
            'Kenglik = eng katta son − eng kichik son.', '${list.reduce(math.max)} $minus ${list.reduce(math.min)} = $r', {'list': list.join(','), 'op': 'range'});
      default:
        final n = g.range(4, 6), mean = g.range(10, 40);
        final list = [for (var i = 0; i < n - 1; i++) mean + g.range(-8, 8)];
        list.add(mean * n - list.fold(0, (s, v) => s + v));
        if (list.last < 1) return stats(g);
        list.shuffle(g.rng);
        return _answer(g, 'Sonlar: ${list.join(', ')}. O‘rta arifmetigini toping.', mean, 'stat:mean:${list.join(',')}',
            'Hamma sonlarni qo‘shib, sonlar soniga bo‘ling.', '${list.join(' + ')} = ${mean * n}; ${mean * n} : $n = $mean',
            {'list': list.join(','), 'op': 'mean'});
    }
  }

  // ------------------------------------------------------------ yuzalar

  static Exercise polygonArea(GenContext g) {
    final mode = _mode(g, const ['parallelogram', 'trapezoid']);
    switch (mode) {
      case 'trapezoid':
        final a = g.range(3, 20), b = g.range(2, 15), h = 2 * g.range(1, 8);
        return _answer(g, 'Trapetsiyaning asoslari $a sm va $b sm, balandligi $h sm. Yuzini toping.', (a + b) * h ~/ 2, 'area:trap:$a:$b:$h',
            'S = (a + b) : 2 · h', '($a + $b) : 2 · $h = ${(a + b) * h ~/ 2} sm²', {'a': a, 'b': b, 'h': h, 'op': 'trapezoid'}, unit: 'sm²');
      case 'rhombus':
        final d1 = 2 * g.range(2, 10), d2 = g.range(3, 20);
        return _answer(g, 'Rombning diagonallari $d1 sm va $d2 sm. Yuzini toping.', d1 * d2 ~/ 2, 'area:rhomb:$d1:$d2', 'S = d₁ · d₂ : 2',
            '$d1 · $d2 : 2 = ${d1 * d2 ~/ 2} sm²', {'a': d1, 'b': d2, 'op': 'rhombus'}, unit: 'sm²');
      default:
        final a = g.range(3, 25), h = g.range(2, 15);
        return _answer(g, 'Parallelogrammning asosi $a sm, unga tushirilgan balandligi $h sm. Yuzini toping.', a * h, 'area:par:$a:$h',
            'S = a · h', '$a · $h = ${a * h} sm²', {'a': a, 'b': h, 'op': '*'}, unit: 'sm²');
    }
  }

  // ------------------------------------------------------------ qisqa ko'paytirish formulalari

  static Exercise abridged(GenContext g) {
    final mode = _mode(g, const ['square_sum', 'factor']);
    switch (mode) {
      case 'diff_num':
        final m = 10 * g.range(3, 9), d = g.range(1, 9);
        final a = m + d, b = m - d;
        return _answer(g, '$a² $minus $b² = ?', a * a - b * b, 'abr:diffnum:$a:$b', 'a² − b² = (a − b)(a + b)',
            '($a $minus $b) · ($a + $b) = ${a - b} · ${a + b} = ${fmtNum(a * a - b * b)}', {'a': a, 'b': b, 'op': 'diff_sq'});
      case 'factor':
        final n = g.range(2, 12);
        return _answer(g, 'Ko‘paytuvchilarga ajrating: x² $minus ${n * n} = (x $minus $n)(x + ?)', n, 'abr:factor:$n', 'a² − b² = (a − b)(a + b)',
            'x² $minus ${n * n} = (x $minus $n)(x + $n)', {'a': n * n, 'op': 'sqrt'});
      case 'square_num':
        final base = 10 * g.range(2, 9), d = g.range(1, 4) * (g.chance(0.5) ? -1 : 1);
        final a = base + d;
        return _answer(g, '($base${term(d)})² ni hisoblang.', a * a, 'abr:sqnum:$base:$d', '(a ± b)² = a² ± 2ab + b²',
            '${base * base}${term(2 * base * d)} + ${d * d} = ${fmtNum(a * a)}', {'a': a, 'b': a, 'op': '*'});
      default:
        final n = _nz(g, 9);
        return _answer(g, '(x${term(n)})² = x²${n < 0 ? ' $minus ' : ' + '}?x + ${n * n}. ? o‘rniga qaysi son?', 2 * n.abs(), 'abr:sqsum:$n',
            '(a + b)² = a² + 2ab + b²', '2 · x · ${n.abs()} = ${2 * n.abs()}x', {'a': 2, 'b': n.abs(), 'op': '*'});
    }
  }

  // ------------------------------------------------------------ ko'pburchak burchaklari

  static Exercise polygonAngles(GenContext g) {
    final mode = _mode(g, const ['sum', 'regular']);
    switch (mode) {
      case 'regular':
        final n = g.pick(const [3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20]);
        final angle = (n - 2) * 180 ~/ n;
        return _answer(g, 'Muntazam $n burchakli ko‘pburchakning har bir ichki burchagi necha gradus?', angle, 'ang:reg:$n',
            'Ichki burchaklar yig‘indisini burchaklar soniga bo‘ling.', '($n $minus 2) · 180° : $n = $angle°', {'a': n, 'op': 'regular_angle'});
      case 'exterior':
        final n = g.pick(const [3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36]);
        return _answer(g, 'Muntazam $n burchakli ko‘pburchakning tashqi burchagi necha gradus?', 360 ~/ n, 'ang:ext:$n',
            'Tashqi burchaklar yig‘indisi har doim 360°.', '360° : $n = ${360 ~/ n}°', {'a': 360, 'b': n, 'op': '/'});
      case 'triangle':
        final a = g.range(20, 100), b = g.range(20, 150 - a);
        return _answer(g, 'Uchburchakning ikki burchagi $a° va $b°. Uchinchi burchagi necha gradus?', 180 - a - b, 'ang:tri:$a:$b',
            'Uchburchak burchaklari yig‘indisi 180°.', '180° $minus $a° $minus $b° = ${180 - a - b}°', {'a': a, 'b': b, 'op': 'tri_angle'});
      default:
        final n = g.range(4, 14);
        return _answer(g, '$n burchakli qavariq ko‘pburchak ichki burchaklarining yig‘indisi necha gradus?', (n - 2) * 180, 'ang:sum:$n',
            'Yig‘indi = (n − 2) · 180°.', '($n $minus 2) · 180° = ${(n - 2) * 180}°', {'a': n, 'op': 'poly_sum'});
    }
  }

  // ------------------------------------------------------------ o'nli kasrlar bilan amallar

  /// [m] / 10^[scale] ni o'nli kasr ko'rinishida: dec(125, 2) → "1,25".
  static String dec(int m, int scale) => fmtDec(m / ipow(10, scale));

  static Exercise _decAnswer(GenContext g, String q, int m, int scale, String concept, String hint, String expl, Map<String, Object> meta) {
    final answer = dec(m, scale);
    final fixed = (m / ipow(10, scale)).toStringAsFixed(scale).replaceAll('.', ',');
    return g.textAnswer(
      question: q,
      answer: answer,
      accept: [fixed, if (answer.startsWith('0,')) answer.substring(1)],
      keys: 'decimal',
      concept: concept,
      hint: hint,
      explanation: '$expl = $answer',
      meta: {...meta, 'm': m, 'scale': scale},
    );
  }

  static Exercise decimalOps(GenContext g) {
    final mode = _mode(g, const ['add', 'sub']);
    final s = g.range(1, 2);
    switch (mode) {
      case 'mul':
        final a = g.range(11, 999), k = g.range(2, 9);
        final q = '${dec(a, s)} · $k = ?';
        return _decAnswer(g, q, a * k, s, 'decop:mul:$a:$k:$s', 'Vergulga e’tibor bermay ko‘paytiring, keyin vergulni $s xona chapga qo‘ying.',
            '${dec(a, s)} · $k', {'a': a, 'b': k, 'op': 'dec_mul'});
      case 'div':
        final r = g.range(11, 999), k = g.range(2, 9);
        final q = '${dec(r * k, s)} : $k = ?';
        return _decAnswer(g, q, r, s, 'decop:div:$r:$k:$s', 'Butun songa bo‘lganday bo‘ling; butun qism tugaganda bo‘linmaga vergul qo‘ying.',
            '${dec(r * k, s)} : $k', {'a': r * k, 'b': k, 'op': 'dec_div'});
      case 'sub':
        final a = g.range(50, 999), b = g.range(11, a - 1);
        final q = '${dec(a, s)} $minus ${dec(b, s)} = ?';
        return _decAnswer(g, q, a - b, s, 'decop:sub:$a:$b:$s', 'Vergulni vergul tagiga yozing, bo‘sh xonaga 0 qo‘yib ayiring.',
            '${dec(a, s)} $minus ${dec(b, s)}', {'a': a, 'b': b, 'op': 'dec_sub'});
      default:
        final a = g.range(11, 999), b = g.range(11, 999);
        final mixed = g.pb('mixed') && g.chance(0.5);
        if (mixed) {
          final q = '${dec(a, 1)} + ${dec(b, 2)} = ?';
          return _decAnswer(g, q, a * 10 + b, 2, 'decop:addmix:$a:$b', 'Verguldan keyingi xonalarni tenglashtiring: 2,5 = 2,50.',
              '${dec(a, 1)} + ${dec(b, 2)}', {'a': a * 10, 'b': b, 'op': 'dec_add'});
        }
        final q = '${dec(a, s)} + ${dec(b, s)} = ?';
        return _decAnswer(g, q, a + b, s, 'decop:add:$a:$b:$s', 'Vergulni vergul tagiga yozib, butun sonlardagidek qo‘shing.',
            '${dec(a, s)} + ${dec(b, s)}', {'a': a, 'b': b, 'op': 'dec_add'});
    }
  }
}
