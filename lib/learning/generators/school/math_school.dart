import '../../content/uz_numbers.dart';
import '../../models/exercise.dart';
import '../generator_base.dart';
import 'school_base.dart';

/// Maktab matematikasi (1–8-sinf): sonlar, amallar, o'lchov birliklari, geometriya, kasrlar,
/// foiz, nisbat, tenglamalar va matnli masalalar. Har bir mashq tasodifiy, javob hisoblab topiladi.
///
/// Darajadagi umumiy parametrlar: `mode` — `input` (javobni yozish), `choice` (tanlash) yoki aralash.
class MathSchool {
  MathSchool._();

  static final Map<String, ExerciseGenerator> generators = {
    'add_sub': addSub,
    'mul_table': mulTable,
    'mul_div': mulDiv,
    'order_ops': orderOps,
    'place_value': placeValue,
    'compare': compare,
    'round': roundNum,
    'units': units,
    'perimeter_area': perimeterArea,
    'volume': volume,
    'word_problem': wordProblem,
    'fraction_part': fractionPart,
    'fraction_ops': fractionOps,
    'fraction_decimal': fractionDecimal,
    'mixed_numbers': mixedNumbers,
    'decimals': decimals,
    'ratio': ratio,
    'percent': percent,
    'average': average,
    'triangle_area': triangleArea,
    'angles': angles,
    'equation': equation,
    'roman': roman,
    'time_calc': timeCalc,
    'sets': sets,
  };

  static const List<String> names = ['Ali', 'Zarina', 'Bobur', 'Madina', 'Sardor', 'Nodira', 'Jasur', 'Malika', 'Aziz', 'Dilnoza'];

  /// Katta sonni so'z bilan: 304502 → "uch yuz to‘rt ming besh yuz ikki".
  static String words(int n) {
    if (n == 0) return 'nol';
    final parts = <String>[];
    final m = n ~/ 1000000, t = (n ~/ 1000) % 1000, r = n % 1000;
    if (m > 0) parts.add('${UzNumbers.word(m)} million');
    if (t > 0) parts.add('${UzNumbers.word(t)} ming');
    if (r > 0) parts.add(UzNumbers.word(r));
    return parts.join(' ');
  }

  // ------------------------------------------------------------ Qo'shish va ayirish
  static Exercise addSub(GenContext g) {
    final min = g.p('min', 100), max = g.p('max', 999);
    final ops = g.pl('ops').isEmpty ? const ['+', '-'] : g.pl('ops');
    final op = g.pick(ops);
    int a, b, answer;
    if (op == '+') {
      a = g.range(min, max);
      b = g.range(min, max);
      answer = a + b;
    } else {
      a = g.range(min, max);
      b = g.range(min ~/ 2, a);
      answer = a - b;
    }
    final sign = op == '+' ? '+' : '−';
    return g.numberAnswer(
      question: '${fmtNum(a)} $sign ${fmtNum(b)} = ?',
      answer: answer,
      input: g.useInput(),
      concept: 'addsub:${op == '+' ? 'add' : 'sub'}:${'$max'.length}',
      hint: op == '+'
          ? 'Sonlarni xonama-xona ustma-ust yozing va birlardan boshlab qo‘shing. 10 dan oshsa — keyingi xonaga 1 o‘tadi.'
          : 'Birlardan boshlab ayiring. Yetmasa — keyingi xonadan 1 o‘nlik oling.',
      explanation: '${fmtNum(a)} $sign ${fmtNum(b)} = ${fmtNum(answer)}',
      meta: {'a': a, 'b': b, 'op': op},
    );
  }

  // ------------------------------------------------------------ Ko'paytirish jadvali
  static Exercise mulTable(GenContext g) {
    final lo = g.p('min', 2), hi = g.p('max', 9);
    final a = g.range(lo, hi), b = g.range(2, 9);
    final div = g.pb('division') && g.chance(0.5);
    if (div) {
      final p = a * b;
      return g.numberAnswer(
        question: '$p : $b = ?',
        answer: a,
        input: g.useInput(),
        concept: 'table:div:$b',
        hint: 'Bo‘lish — ko‘paytirishga teskari amal: $b ni nechaga ko‘paytirsak $p chiqadi?',
        explanation: '$p : $b = $a, chunki $a · $b = $p',
        meta: {'a': p, 'b': b, 'op': '/'},
      );
    }
    return g.numberAnswer(
      question: '$a · $b = ?',
      answer: a * b,
      input: g.useInput(),
      concept: 'table:mul:$a',
      hint: '$a ni $b marta qo‘shing yoki ko‘paytirish jadvalini eslang.',
      explanation: '$a · $b = ${a * b}',
      meta: {'a': a, 'b': b, 'op': '*'},
    );
  }

  // ------------------------------------------------------------ Ko'paytirish va bo'lish
  static Exercise mulDiv(GenContext g) {
    final aMin = g.p('aMin', 10), aMax = g.p('aMax', 99);
    final bMin = g.p('bMin', 2), bMax = g.p('bMax', 9);
    final modes = g.pl('modes').isEmpty ? const ['mul', 'div'] : g.pl('modes');
    final mode = g.pick(modes);
    switch (mode) {
      case 'pow10':
        final k = g.pick(const [10, 100, 1000]);
        if (g.chance(0.5)) {
          final a = g.range(aMin, aMax);
          return g.numberAnswer(
            question: '${fmtNum(a)} · ${fmtNum(k)} = ?',
            answer: a * k,
            input: g.useInput(),
            concept: 'pow10:mul',
            hint: '10 ga ko‘paytirishda son oxiriga bitta 0, 100 ga — ikkita, 1000 ga — uchta 0 yoziladi.',
            explanation: '${fmtNum(a)} · ${fmtNum(k)} = ${fmtNum(a * k)}',
            meta: {'a': a, 'b': k, 'op': '*'},
          );
        }
        final q = g.range(aMin, aMax);
        return g.numberAnswer(
          question: '${fmtNum(q * k)} : ${fmtNum(k)} = ?',
          answer: q,
          input: g.useInput(),
          concept: 'pow10:div',
          hint: 'Oxiri nollar bilan tugagan sonni 10, 100, 1000 ga bo‘lishda oxiridan shuncha 0 olib tashlanadi.',
          explanation: '${fmtNum(q * k)} : ${fmtNum(k)} = ${fmtNum(q)}',
          meta: {'a': q * k, 'b': k, 'op': '/'},
        );
      case 'remainder':
        final b = g.range(bMin.clamp(2, 99).toInt(), bMax);
        final q = g.range((aMin ~/ b).clamp(1, 100000).toInt(), (aMax ~/ b).clamp(2, 100000).toInt());
        final r = g.range(1, b - 1);
        final a = q * b + r;
        final askRemainder = g.chance(0.5);
        return g.numberAnswer(
          question: askRemainder
              ? '${fmtNum(a)} ni $b ga qoldiqli bo‘ling. Qoldiq nechaga teng?'
              : '${fmtNum(a)} ni $b ga qoldiqli bo‘ling. To‘liqsiz bo‘linma nechaga teng?',
          answer: askRemainder ? r : q,
          input: g.useInput(),
          concept: 'div:remainder',
          hint: 'Qoldiq har doim bo‘luvchidan kichik bo‘ladi: $a = ? · $b + qoldiq.',
          explanation: '${fmtNum(a)} = ${fmtNum(q)} · $b + $r → bo‘linma ${fmtNum(q)}, qoldiq $r',
          meta: {'a': a, 'b': b, 'op': 'mod'},
        );
      case 'div':
        final b = g.range(bMin, bMax);
        final q = g.range((aMin ~/ b).clamp(1, 1000000).toInt(), (aMax ~/ b).clamp(2, 1000000).toInt());
        return g.numberAnswer(
          question: '${fmtNum(q * b)} : $b = ?',
          answer: q,
          input: g.useInput(),
          concept: 'div:${'$bMax'.length}',
          hint: 'Burchak usulida bo‘ling: chapdan boshlab har bir xonani bo‘luvchiga bo‘ling.',
          explanation: '${fmtNum(q * b)} : $b = ${fmtNum(q)}, chunki ${fmtNum(q)} · $b = ${fmtNum(q * b)}',
          meta: {'a': q * b, 'b': b, 'op': '/'},
        );
      default:
        final a = g.range(aMin, aMax), b = g.range(bMin, bMax);
        return g.numberAnswer(
          question: '${fmtNum(a)} · $b = ?',
          answer: a * b,
          input: g.useInput(),
          concept: 'mul:${'$bMax'.length}',
          hint: 'Birlardan boshlab har bir xonani $b ga ko‘paytiring, o‘nliklarni keyingi xonaga o‘tkazing.',
          explanation: '${fmtNum(a)} · $b = ${fmtNum(a * b)}',
          meta: {'a': a, 'b': b, 'op': '*'},
        );
    }
  }

  // ------------------------------------------------------------ Amallar tartibi
  static Exercise orderOps(GenContext g) {
    final max = g.p('max', 20);
    final parens = g.pb('parens', true);
    for (var attempt = 0; attempt < 40; attempt++) {
      final a = g.range(2, max), b = g.range(2, max), c = g.range(2, 9);
      final form = g.range(0, parens ? 5 : 2);
      String expr;
      int? v;
      switch (form) {
        case 0:
          expr = '$a + $b · $c';
          v = a + b * c;
        case 1:
          expr = '$a · $c − $b';
          v = a * c >= b ? a * c - b : null;
        case 2:
          expr = '${a * c} : $c + $b';
          v = a + b;
        case 3:
          expr = '($a + $b) · $c';
          v = (a + b) * c;
        case 4:
          expr = '($a − $b) · $c';
          v = a > b ? (a - b) * c : null;
        default:
          expr = '${(a + b) * c} : ($a + $b)';
          v = c;
      }
      if (v == null) continue;
      return g.numberAnswer(
        question: 'Hisoblang: $expr = ?',
        answer: v,
        input: g.useInput(),
        concept: 'order:${parens ? 'parens' : 'plain'}',
        hint: 'Avval qavs ichidagi amal, keyin ko‘paytirish va bo‘lish, oxirida qo‘shish va ayirish bajariladi.',
        explanation: '$expr = $v',
      );
    }
    return orderOps(g);
  }

  // ------------------------------------------------------------ Xona birliklari
  static const List<String> _places = [
    'birlar', 'o‘nlar', 'yuzlar', 'minglar', 'o‘n minglar', 'yuz minglar', 'millionlar',
  ];

  static Exercise placeValue(GenContext g) {
    final max = g.p('max', 99999);
    final minN = g.p('min', 1000);
    final modes = g.pl('modes').isEmpty ? const ['place', 'write', 'expanded', 'count'] : g.pl('modes');
    final mode = g.pick(modes);
    final n = g.range(minN, max);
    final digits = '$n';
    switch (mode) {
      case 'write':
        return g.numberAnswer(
          question: 'Raqamlar bilan yozing: ${words(n)}',
          answer: n,
          input: true,
          concept: 'place:write',
          hint: 'Avval minglar sinfini, keyin birlar sinfini yozing. Bo‘sh xonaga 0 yoziladi.',
          explanation: '${words(n)} — ${fmtNum(n)}',
        );
      case 'expanded':
        final parts = <String>[];
        for (var i = 0; i < digits.length; i++) {
          final d = int.parse(digits[i]);
          if (d == 0) continue;
          parts.add(fmtNum(d * _pow10(digits.length - 1 - i)));
        }
        if (parts.length < 2) return placeValue(g);
        return g.numberAnswer(
          question: '${parts.join(' + ')} = ?',
          answer: n,
          input: g.useInput(),
          concept: 'place:expanded',
          hint: 'Xona qo‘shiluvchilarini birlashtiring: har bir raqam o‘z xonasiga yoziladi.',
          explanation: '${parts.join(' + ')} = ${fmtNum(n)}',
        );
      case 'count':
        final unit = g.pick(const [10, 100, 1000]);
        final unitName = switch (unit) { 10 => 'o‘nlik', 100 => 'yuzlik', _ => 'minglik' };
        return g.numberAnswer(
          question: '${fmtNum(n)} sonida jami nechta to‘liq $unitName bor?',
          answer: n ~/ unit,
          input: g.useInput(),
          concept: 'place:count',
          hint: 'Sonni $unit ga bo‘ling (oxiridagi ${'$unit'.length - 1} ta raqamni tashlab yuboring).',
          explanation: '${fmtNum(n)} : $unit = ${fmtNum(n ~/ unit)} (qoldiq ${n % unit})',
        );
      default:
        // Faqat bir marta uchraydigan raqamning xonasini so'raymiz.
        final candidates = [
          for (var i = 0; i < digits.length; i++)
            if (digits.split('').where((c) => c == digits[i]).length == 1) i,
        ];
        if (candidates.isEmpty) return placeValue(g);
        final i = g.pick(candidates);
        final place = digits.length - 1 - i;
        return g.textChoice(
          question: '${fmtNum(n)} sonida ${digits[i]} raqami qaysi xonada turibdi?',
          answer: _places[place],
          wrong: [for (var p = 0; p < digits.length && p < _places.length; p++) if (p != place) _places[p]],
          concept: 'place:name',
          hint: 'Xonalarni o‘ngdan chapga sanang: birlar, o‘nlar, yuzlar, minglar …',
          explanation: '${fmtNum(n)}: ${digits[i]} — ${_places[place]} xonasida',
        );
    }
  }

  static int _pow10(int k) {
    var v = 1;
    for (var i = 0; i < k; i++) {
      v *= 10;
    }
    return v;
  }

  // ------------------------------------------------------------ Taqqoslash
  static Exercise compare(GenContext g) {
    final min = g.p('min', 1000), max = g.p('max', 99999);
    final a = g.range(min, max);
    int b;
    if (g.chance(0.15)) {
      b = a;
    } else {
      // Bitta xonasi farq qiladigan son: bola xonama-xona taqqoslashni o'rganadi.
      final digits = '$a'.split('');
      final i = g.range(0, digits.length - 1);
      final d = int.parse(digits[i]);
      var nd = d;
      while (nd == d || (i == 0 && nd == 0)) {
        nd = g.range(0, 9);
      }
      digits[i] = '$nd';
      b = int.parse(digits.join());
    }
    final answer = a > b ? '>' : (a < b ? '<' : '=');
    return g.textChoice(
      question: 'Taqqoslang: ${fmtNum(a)} ○ ${fmtNum(b)}',
      answer: answer,
      wrong: const ['>', '<', '='],
      options: 3,
      concept: 'compare:numbers',
      hint: 'Avval xonalar sonini, keyin chapdan boshlab raqamlarni solishtiring.',
      explanation: '${fmtNum(a)} $answer ${fmtNum(b)}',
      meta: {'a': a, 'b': b, 'op': 'cmp', 'answer': answer},
    );
  }

  // ------------------------------------------------------------ Yaxlitlash
  static Exercise roundNum(GenContext g) {
    final max = g.p('max', 9999);
    final places = g.pl('places').isEmpty ? const ['10', '100', '1000'] : g.pl('places');
    final unit = int.parse(g.pick(places));
    final n = g.range(unit + 1, max);
    final rounded = ((n + unit ~/ 2) ~/ unit) * unit;
    final name = switch (unit) { 10 => 'o‘nlar', 100 => 'yuzlar', _ => 'minglar' };
    return g.numberAnswer(
      question: '${fmtNum(n)} ni $name xonasigacha yaxlitlang',
      answer: rounded,
      input: g.useInput(),
      concept: 'round:$unit',
      hint: 'Keyingi xona raqami 5 yoki undan katta bo‘lsa — yuqoriga, 5 dan kichik bo‘lsa — pastga yaxlitlanadi.',
      explanation: '${fmtNum(n)} ≈ ${fmtNum(rounded)}',
    );
  }

  // ------------------------------------------------------------ O'lchov birliklari
  static const Map<String, List<(String, String, int)>> _units = {
    'length': [('km', 'm', 1000), ('m', 'sm', 100), ('m', 'dm', 10), ('dm', 'sm', 10), ('sm', 'mm', 10), ('m', 'mm', 1000)],
    'mass': [('kg', 'g', 1000), ('t', 'kg', 1000), ('sentner', 'kg', 100), ('t', 'sentner', 10)],
    'time': [('soat', 'minut', 60), ('minut', 'sekund', 60), ('sutka', 'soat', 24), ('yil', 'oy', 12), ('hafta', 'kun', 7)],
    'area': [('m²', 'dm²', 100), ('dm²', 'sm²', 100), ('ar', 'm²', 100), ('gektar', 'ar', 100), ('km²', 'gektar', 100)],
    'volume': [('l', 'ml', 1000), ('m³', 'dm³', 1000), ('dm³', 'sm³', 1000)],
  };

  static Exercise units(GenContext g) {
    final kinds = g.pl('kinds').isEmpty ? const ['length', 'mass', 'time'] : g.pl('kinds');
    final kind = g.pick(kinds);
    final (big, small, f) = g.pick(_units[kind]!);
    final maxA = g.p('max', 9);
    final modes = g.pl('modes').isEmpty ? const ['simple', 'compound', 'reverse'] : g.pl('modes');
    final mode = g.pick(modes);
    final a = g.range(1, maxA);
    switch (mode) {
      case 'compound':
        final b = g.range(1, f - 1);
        return g.numberAnswer(
          question: '$a $big $b $small = ? $small',
          answer: a * f + b,
          input: g.useInput(),
          unit: small,
          concept: 'units:$kind',
          hint: '1 $big = ${fmtNum(f)} $small. Avval $a $big ni $small ga aylantiring, keyin $b ni qo‘shing.',
          explanation: '$a $big $b $small = ${fmtNum(a * f)} + $b = ${fmtNum(a * f + b)} $small',
        );
      case 'reverse':
        return g.numberAnswer(
          question: '${fmtNum(a * f)} $small = ? $big',
          answer: a,
          input: g.useInput(),
          unit: big,
          concept: 'units:$kind',
          hint: '1 $big = ${fmtNum(f)} $small. Sonni ${fmtNum(f)} ga bo‘ling.',
          explanation: '${fmtNum(a * f)} : ${fmtNum(f)} = $a $big',
        );
      default:
        return g.numberAnswer(
          question: '$a $big = ? $small',
          answer: a * f,
          input: g.useInput(),
          unit: small,
          concept: 'units:$kind',
          hint: '1 $big = ${fmtNum(f)} $small.',
          explanation: '$a · ${fmtNum(f)} = ${fmtNum(a * f)} $small',
        );
    }
  }

  // ------------------------------------------------------------ Perimetr va yuza
  static Exercise perimeterArea(GenContext g) {
    final max = g.p('max', 12);
    final modes = g.pl('modes').isEmpty ? const ['perimeter', 'area', 'square', 'inverse'] : g.pl('modes');
    final mode = g.pick(modes);
    final unit = g.pick(const ['sm', 'dm', 'm']);
    switch (mode) {
      case 'square':
        final a = g.range(2, max);
        final perimeter = g.chance(0.5);
        return g.numberAnswer(
          question: perimeter ? 'Kvadratning tomoni $a $unit. Uning perimetri necha $unit?' : 'Kvadratning tomoni $a $unit. Uning yuzi necha $unit²?',
          answer: perimeter ? 4 * a : a * a,
          input: g.useInput(),
          unit: perimeter ? unit : '$unit²',
          concept: perimeter ? 'geom:square_p' : 'geom:square_s',
          hint: perimeter ? 'Kvadrat perimetri: P = a · 4' : 'Kvadrat yuzi: S = a · a',
          explanation: perimeter ? 'P = $a · 4 = ${4 * a} $unit' : 'S = $a · $a = ${a * a} $unit²',
        );
      case 'inverse':
        if (g.chance(0.5)) {
          final side = g.range(2, max);
          return g.numberAnswer(
            question: 'Kvadratning perimetri ${4 * side} $unit. Uning tomoni necha $unit?',
            answer: side,
            input: g.useInput(),
            unit: unit,
            concept: 'geom:inverse',
            hint: 'Kvadratning 4 ta tomoni teng: tomoni = P : 4',
            explanation: '${4 * side} : 4 = $side $unit',
          );
        }
        final a = g.range(2, max), b = g.range(2, max);
        return g.numberAnswer(
          question: 'To‘g‘ri to‘rtburchakning yuzi ${a * b} $unit², bo‘yi $a $unit. Eni necha $unit?',
          answer: b,
          input: g.useInput(),
          unit: unit,
          concept: 'geom:inverse',
          hint: 'S = a · b bo‘lgani uchun b = S : a',
          explanation: '${a * b} : $a = $b $unit',
        );
      case 'area':
        final a = g.range(2, max), b = g.range(2, max);
        return g.numberAnswer(
          question: 'To‘g‘ri to‘rtburchakning bo‘yi $a $unit, eni $b $unit. Uning yuzi necha $unit²?',
          answer: a * b,
          input: g.useInput(),
          unit: '$unit²',
          concept: 'geom:rect_s',
          hint: 'To‘g‘ri to‘rtburchak yuzi: S = a · b',
          explanation: 'S = $a · $b = ${a * b} $unit²',
        );
      default:
        final a = g.range(2, max), b = g.range(2, max);
        return g.numberAnswer(
          question: 'To‘g‘ri to‘rtburchakning bo‘yi $a $unit, eni $b $unit. Uning perimetri necha $unit?',
          answer: 2 * (a + b),
          input: g.useInput(),
          unit: unit,
          concept: 'geom:rect_p',
          hint: 'Perimetr — barcha tomonlar yig‘indisi: P = (a + b) · 2',
          explanation: 'P = ($a + $b) · 2 = ${2 * (a + b)} $unit',
        );
    }
  }

  // ------------------------------------------------------------ Hajm
  static Exercise volume(GenContext g) {
    final max = g.p('max', 10);
    final modes = g.pl('modes').isEmpty ? const ['cuboid', 'cube', 'edges'] : g.pl('modes');
    final mode = g.pick(modes);
    switch (mode) {
      case 'cube':
        final a = g.range(2, max);
        return g.numberAnswer(
          question: 'Kubning qirrasi $a sm. Uning hajmi necha sm³?',
          answer: a * a * a,
          input: g.useInput(),
          unit: 'sm³',
          concept: 'volume:cube',
          hint: 'Kub hajmi: V = a · a · a',
          explanation: 'V = $a · $a · $a = ${a * a * a} sm³',
        );
      case 'edges':
        final a = g.range(2, max);
        return g.numberAnswer(
          question: 'Kubning qirrasi $a sm. Uning barcha qirralari uzunliklari yig‘indisi necha sm?',
          answer: 12 * a,
          input: g.useInput(),
          unit: 'sm',
          concept: 'volume:edges',
          hint: 'Kubning 12 ta qirrasi bor va ular teng.',
          explanation: '$a · 12 = ${12 * a} sm',
        );
      case 'liters':
        final a = g.range(2, max), b = g.range(2, max), c = g.range(2, max);
        return g.numberAnswer(
          question: 'Akvariumning ichki o‘lchamlari: uzunligi $a dm, eni $b dm, balandligi $c dm. Unga necha litr suv sig‘adi?',
          answer: a * b * c,
          input: g.useInput(),
          unit: 'l',
          concept: 'volume:liters',
          hint: '1 dm³ = 1 litr. Avval hajmni toping: V = a · b · c',
          explanation: '$a · $b · $c = ${a * b * c} dm³ = ${a * b * c} l',
        );
      default:
        final a = g.range(2, max), b = g.range(2, max), c = g.range(2, max);
        return g.numberAnswer(
          question: 'Kuboidning uzunligi $a sm, eni $b sm, balandligi $c sm. Uning hajmi necha sm³?',
          answer: a * b * c,
          input: g.useInput(),
          unit: 'sm³',
          concept: 'volume:cuboid',
          hint: 'Kuboid (to‘g‘ri burchakli parallelepiped) hajmi: V = a · b · c',
          explanation: 'V = $a · $b · $c = ${a * b * c} sm³',
        );
    }
  }

  // ------------------------------------------------------------ Matnli masalalar
  static const List<(String, int, int)> _goods = [
    ('daftar', 2000, 6000),
    ('ruchka', 1500, 5000),
    ('kitob', 15000, 40000),
    ('non', 3000, 5000),
    ('kg olma', 8000, 15000),
    ('qalam', 1000, 3000),
    ('shar', 2000, 6000),
  ];

  static Exercise wordProblem(GenContext g) {
    final kinds = g.pl('kinds').isEmpty ? const ['sum', 'diff', 'speed', 'price', 'work', 'times'] : g.pl('kinds');
    final kind = g.pick(kinds);
    final max = g.p('max', 1000);
    final name = g.pick(names);
    switch (kind) {
      case 'sum':
        final a = g.range(max ~/ 10, max), b = g.range(max ~/ 10, max);
        return g.numberAnswer(
          question: 'Kutubxonaning birinchi javonida ${fmtNum(a)} ta kitob, ikkinchisida ${fmtNum(b)} ta kitob bor. Ikki javonda hammasi bo‘lib nechta kitob bor?',
          answer: a + b,
          input: g.useInput(),
          concept: 'problem:sum',
          hint: '“Hammasi bo‘lib” — qo‘shish kerak.',
          explanation: '${fmtNum(a)} + ${fmtNum(b)} = ${fmtNum(a + b)} ta',
          meta: {'a': a, 'b': b, 'op': '+'},
        );
      case 'diff':
        final a = g.range(max ~/ 5, max), b = g.range(max ~/ 20, a - 1);
        return g.numberAnswer(
          question: 'Do‘konda ${fmtNum(a)} kg kartoshka bor edi. Kun davomida ${fmtNum(b)} kg sotildi. Necha kilogramm kartoshka qoldi?',
          answer: a - b,
          input: g.useInput(),
          unit: 'kg',
          concept: 'problem:diff',
          hint: '“Qoldi” — bor edi miqdoridan sotilganini ayiramiz.',
          explanation: '${fmtNum(a)} − ${fmtNum(b)} = ${fmtNum(a - b)} kg',
          meta: {'a': a, 'b': b, 'op': '-'},
        );
      case 'speed':
        final v = g.range(4, 90), t = g.range(2, 8);
        final s = v * t;
        final ask = g.range(0, 2);
        final vehicle = v <= 6 ? 'Piyoda' : (v <= 25 ? 'Velosipedchi' : 'Avtomobil');
        if (ask == 0) {
          return g.numberAnswer(
            question: '$vehicle soatiga $v km tezlik bilan $t soat yurdi. U qancha masofani bosib o‘tdi?',
            answer: s,
            input: g.useInput(),
            unit: 'km',
            concept: 'problem:distance',
            hint: 'Masofa = tezlik · vaqt',
            explanation: '$v · $t = $s km',
            meta: {'a': v, 'b': t, 'op': '*'},
          );
        }
        if (ask == 1) {
          return g.numberAnswer(
            question: '$vehicle $s km masofani $t soatda bosib o‘tdi. Uning tezligi soatiga necha km?',
            answer: v,
            input: g.useInput(),
            unit: 'km/soat',
            concept: 'problem:speed',
            hint: 'Tezlik = masofa : vaqt',
            explanation: '$s : $t = $v km/soat',
            meta: {'a': s, 'b': t, 'op': '/'},
          );
        }
        return g.numberAnswer(
          question: '$vehicle soatiga $v km tezlik bilan yuradi. U $s km masofani necha soatda bosib o‘tadi?',
          answer: t,
          input: g.useInput(),
          unit: 'soat',
          concept: 'problem:time',
          hint: 'Vaqt = masofa : tezlik',
          explanation: '$s : $v = $t soat',
          meta: {'a': s, 'b': v, 'op': '/'},
        );
      case 'price':
        final (item, lo, hi) = g.pick(_goods);
        final price = g.range(lo ~/ 500, hi ~/ 500) * 500;
        final n = g.range(2, 9);
        final cost = price * n;
        final ask = g.range(0, 2);
        final unitWord = item.startsWith('kg ') ? '' : ' ta';
        final noun = item.startsWith('kg ') ? item.substring(3) : item;
        final amount = item.startsWith('kg ') ? '$n kg' : '$n ta';
        if (ask == 0) {
          return g.numberAnswer(
            question: '${item.startsWith('kg ') ? '1 kg $noun' : 'Bitta $noun'} ${fmtNum(price)} so‘m turadi. $name $amount $noun oldi. U qancha pul to‘ladi?',
            answer: cost,
            input: g.useInput(),
            unit: 'so‘m',
            concept: 'problem:cost',
            hint: 'Qiymat = narx · miqdor',
            explanation: '${fmtNum(price)} · $n = ${fmtNum(cost)} so‘m',
            meta: {'a': price, 'b': n, 'op': '*'},
          );
        }
        if (ask == 1) {
          return g.numberAnswer(
            question: '$amount $noun ${fmtNum(cost)} so‘m turadi. ${item.startsWith('kg ') ? '1 kg' : 'Bitta'} $noun necha so‘m?',
            answer: price,
            input: g.useInput(),
            unit: 'so‘m',
            concept: 'problem:price',
            hint: 'Narx = qiymat : miqdor',
            explanation: '${fmtNum(cost)} : $n = ${fmtNum(price)} so‘m',
            meta: {'a': cost, 'b': n, 'op': '/'},
          );
        }
        return g.numberAnswer(
          question: '${item.startsWith('kg ') ? '1 kg' : 'Bitta'} $noun ${fmtNum(price)} so‘m turadi. ${fmtNum(cost)} so‘mga necha${item.startsWith('kg ') ? ' kilogramm' : unitWord} $noun olish mumkin?',
          answer: n,
          input: g.useInput(),
          concept: 'problem:quantity',
          hint: 'Miqdor = qiymat : narx',
          explanation: '${fmtNum(cost)} : ${fmtNum(price)} = $n',
          meta: {'a': cost, 'b': price, 'op': '/'},
        );
      case 'work':
        final k = g.range(6, 40), h = g.range(2, 8);
        if (g.chance(0.5)) {
          return g.numberAnswer(
            question: 'Usta bir soatda $k ta detal tayyorlaydi. U $h soatda nechta detal tayyorlaydi?',
            answer: k * h,
            input: g.useInput(),
            concept: 'problem:work',
            hint: 'Ish hajmi = unumdorlik · vaqt',
            explanation: '$k · $h = ${k * h} ta',
            meta: {'a': k, 'b': h, 'op': '*'},
          );
        }
        return g.numberAnswer(
          question: 'Usta $h soatda ${k * h} ta detal tayyorladi. U bir soatda nechta detal tayyorlagan?',
          answer: k,
          input: g.useInput(),
          concept: 'problem:rate',
          hint: 'Unumdorlik = ish hajmi : vaqt',
          explanation: '${k * h} : $h = $k ta',
          meta: {'a': k * h, 'b': h, 'op': '/'},
        );
      case 'rate':
        // Me'yor: bir nechta narsaning narxidan boshqa miqdorning narxi.
        final (item, lo, hi) = g.pick(_goods.where((e) => !e.$1.startsWith('kg ')).toList());
        final price = g.range(lo ~/ 500, hi ~/ 500) * 500;
        final n = g.range(2, 6), m = g.range(2, 9);
        return g.numberAnswer(
          question: '$n ta $item ${fmtNum(price * n)} so‘m turadi. $m ta $item qancha turadi?',
          answer: price * m,
          input: g.useInput(),
          unit: 'so‘m',
          concept: 'problem:unitary',
          hint: 'Avval bittasining narxini toping: ${fmtNum(price * n)} : $n',
          explanation: '${fmtNum(price * n)} : $n = ${fmtNum(price)}; ${fmtNum(price)} · $m = ${fmtNum(price * m)} so‘m',
        );
      default:
        final a = g.range(4, 30), k = g.range(2, 5);
        if (g.chance(0.5)) {
          return g.numberAnswer(
            question: 'Bog‘da $a ta olma daraxti bor. Nok daraxtlari undan $k marta ko‘p. Bog‘da nechta nok daraxti bor?',
            answer: a * k,
            input: g.useInput(),
            concept: 'problem:times_more',
            hint: '“$k marta ko‘p” — ko‘paytirish kerak.',
            explanation: '$a · $k = ${a * k} ta',
            meta: {'a': a, 'b': k, 'op': '*'},
          );
        }
        return g.numberAnswer(
          question: '$name ${a * k} ta marka yig‘di, akasi esa undan $k marta kam. Akasi nechta marka yig‘gan?',
          answer: a,
          input: g.useInput(),
          concept: 'problem:times_less',
          hint: '“$k marta kam” — bo‘lish kerak.',
          explanation: '${a * k} : $k = $a ta',
          meta: {'a': a * k, 'b': k, 'op': '/'},
        );
    }
  }

  // ------------------------------------------------------------ Kasrlar
  static String _frac(int a, int b) => '$a/$b';

  static List<String> _fracForms(int a, int b) {
    final d = gcd(a, b);
    final forms = <String>{_frac(a, b), _frac(a ~/ d, b ~/ d)};
    if (b ~/ d == 1) forms.add('${a ~/ d}');
    return forms.toList();
  }

  static Exercise fractionPart(GenContext g) {
    final dens = g.pl('dens').isEmpty ? const ['2', '3', '4', '5', '6', '8', '10'] : g.pl('dens');
    final b = int.parse(g.pick(dens));
    final a = g.range(1, b - 1);
    final k = g.range(2, g.p('max', 12));
    final whole = b * k;
    if (g.pb('inverse') && g.chance(0.5)) {
      return g.numberAnswer(
        question: 'Sonning $a/$b qismi ${a * k} ga teng. Shu sonni toping.',
        answer: whole,
        input: g.useInput(),
        concept: 'fraction:whole',
        hint: 'Avval bir qismini toping: ${a * k} : $a, keyin $b ga ko‘paytiring.',
        explanation: '${a * k} : $a · $b = $whole',
      );
    }
    return g.numberAnswer(
      question: '$whole ning $a/$b qismini toping.',
      answer: a * k,
      input: g.useInput(),
      concept: 'fraction:part',
      hint: 'Sonni maxrajga bo‘lib, suratga ko‘paytiring: $whole : $b · $a',
      explanation: '$whole : $b = $k; $k · $a = ${a * k}',
    );
  }

  static Exercise fractionOps(GenContext g) {
    final modes = g.pl('modes').isEmpty ? const ['compare', 'add', 'sub'] : g.pl('modes');
    final mode = g.pick(modes);
    final maxDen = g.p('maxDen', 12);
    final n = g.range(3, maxDen);
    switch (mode) {
      case 'compare':
        final a = g.range(1, n - 1);
        var c = g.range(1, n - 1);
        if (g.chance(0.15)) c = a;
        final answer = a > c ? '>' : (a < c ? '<' : '=');
        return g.textChoice(
          question: 'Taqqoslang: $a/$n ○ $c/$n',
          answer: answer,
          wrong: const ['>', '<', '='],
          options: 3,
          concept: 'fraction:compare',
          hint: 'Maxrajlari teng kasrlardan surati kattasi katta.',
          explanation: '$a/$n $answer $c/$n',
          meta: {'a': a, 'b': c, 'op': 'cmp', 'answer': answer},
        );
      case 'sub':
        final a = g.range(2, n), c = g.range(1, a - 1);
        return g.textAnswer(
          question: '$a/$n − $c/$n = ?',
          answer: _frac(a - c, n),
          accept: _fracForms(a - c, n),
          keys: 'fraction',
          concept: 'fraction:sub',
          hint: 'Maxrajlari teng kasrlarni ayirishda suratlar ayiriladi, maxraj o‘zgarmaydi.',
          explanation: '$a/$n − $c/$n = ${a - c}/$n',
        );
      case 'mul_nat':
        final a = g.range(1, n - 1), k = g.range(2, 9);
        return g.textAnswer(
          question: '$a/$n · $k = ?',
          answer: _fracForms(a * k, n).last,
          accept: _fracForms(a * k, n),
          keys: 'fraction',
          concept: 'fraction:mul_nat',
          hint: 'Kasrni natural songa ko‘paytirishda surat shu songa ko‘paytiriladi, maxraj o‘zgarmaydi.',
          explanation: '$a/$n · $k = ${a * k}/$n',
        );
      case 'mul':
        final a = g.range(1, n - 1);
        final m = g.range(2, maxDen);
        final c = g.range(1, m - 1);
        return g.textAnswer(
          question: '$a/$n · $c/$m = ?',
          answer: _fracForms(a * c, n * m).last,
          accept: _fracForms(a * c, n * m),
          keys: 'fraction',
          concept: 'fraction:mul',
          hint: 'Suratni suratga, maxrajni maxrajga ko‘paytiring, keyin iloji bo‘lsa qisqartiring.',
          explanation: '$a/$n · $c/$m = ${a * c}/${n * m}${gcd(a * c, n * m) > 1 ? ' = ${_fracForms(a * c, n * m).last}' : ''}',
        );
      default:
        final a = g.range(1, n - 2), c = g.range(1, n - 1 - a);
        return g.textAnswer(
          question: '$a/$n + $c/$n = ?',
          answer: _frac(a + c, n),
          accept: _fracForms(a + c, n),
          keys: 'fraction',
          concept: 'fraction:add',
          hint: 'Maxrajlari teng kasrlarni qo‘shishda suratlar qo‘shiladi, maxraj o‘zgarmaydi.',
          explanation: '$a/$n + $c/$n = ${a + c}/$n',
        );
    }
  }

  static Exercise fractionDecimal(GenContext g) {
    const dens = [2, 4, 5, 10, 20, 25, 50, 100];
    final b = g.pick(dens);
    final a = g.range(1, b - 1);
    final value = a / b;
    final dec = fmtDec(value);
    final modes = g.pl('modes').isEmpty ? const ['to_decimal', 'to_fraction', 'division'] : g.pl('modes');
    final mode = g.pick(modes);
    switch (mode) {
      case 'to_fraction':
        final hundredths = (value * 100).round();
        final forms = {..._fracForms(a, b), ..._fracForms(hundredths, 100)}.toList();
        return g.textAnswer(
          question: '$dec ni oddiy kasr ko‘rinishida yozing',
          answer: _fracForms(a, b).last,
          accept: forms,
          keys: 'fraction',
          concept: 'decimal:to_fraction',
          hint: 'Verguldan keyingi raqamlar soniga qarab maxraj 10, 100, … bo‘ladi, keyin qisqartiring.',
          explanation: '$dec = ${_fracForms(a, b).last}',
        );
      case 'division':
        final p = g.range(1, 20), q = g.range(2, 20);
        return g.textAnswer(
          question: '$p : $q bo‘linmani kasr ko‘rinishida yozing',
          answer: _frac(p, q),
          accept: _fracForms(p, q),
          keys: 'fraction',
          concept: 'fraction:division',
          hint: 'Bo‘linuvchi — kasrning surati, bo‘luvchi — maxraji: a : b = a/b',
          explanation: '$p : $q = $p/$q',
        );
      default:
        return g.textAnswer(
          question: '$a/$b ni o‘nli kasr ko‘rinishida yozing',
          answer: dec,
          accept: [dec, dec.replaceFirst('0,', ',')],
          keys: 'decimal',
          concept: 'fraction:to_decimal',
          hint: 'Maxrajni 10, 100 yoki 1000 ga keltiring yoki suratni maxrajga bo‘ling.',
          explanation: '$a/$b = $dec',
        );
    }
  }

  static String _mixed(int whole, int num, int den) => num == 0 ? '$whole' : (whole == 0 ? '$num/$den' : '$whole $num/$den');

  static Exercise mixedNumbers(GenContext g) {
    final den = g.range(3, g.p('maxDen', 9));
    final w1 = g.range(1, 6), w2 = g.range(1, 5);
    final n1 = g.range(1, den - 1), n2 = g.range(1, den - 1);
    final total1 = w1 * den + n1, total2 = w2 * den + n2;
    final add = !g.pl('ops').contains('sub') || (g.pl('ops').contains('add') && g.chance(0.5));
    int r;
    String q;
    if (add) {
      r = total1 + total2;
      q = '${_mixed(w1, n1, den)} + ${_mixed(w2, n2, den)} = ?';
    } else {
      final big = total1 >= total2 ? (w1, n1) : (w2, n2);
      final small = total1 >= total2 ? (w2, n2) : (w1, n1);
      final tb = big.$1 * den + big.$2, ts = small.$1 * den + small.$2;
      if (tb == ts) return mixedNumbers(g);
      r = tb - ts;
      q = '${_mixed(big.$1, big.$2, den)} − ${_mixed(small.$1, small.$2, den)} = ?';
    }
    final answer = _mixed(r ~/ den, r % den, den);
    final wrong = <String>{
      _mixed(r ~/ den + 1, r % den, den),
      if (r ~/ den > 0) _mixed(r ~/ den - 1, r % den, den),
      _mixed(r ~/ den, (r % den + 1) % den, den),
      '${r ~/ den} ${r % den}/${den * 2}',
      '$r/$den',
    }.where((w) => w != answer && w.trim().isNotEmpty).toList();
    return g.textChoice(
      question: q,
      answer: answer,
      wrong: wrong,
      concept: add ? 'mixed:add' : 'mixed:sub',
      hint: 'Butun qismlarni alohida, kasr qismlarni alohida hisoblang. Kasr qism maxrajdan oshsa — 1 butun hosil bo‘ladi.',
      explanation: '${q.replaceAll(' = ?', '')} = $answer',
    );
  }

  // ------------------------------------------------------------ O'nli kasrlar
  /// O'nli kasr butun son (mantissa) va vergul o'rni bilan: (345, 2) → 3,45.
  static String _dec(int m, int scale) {
    if (scale <= 0) return fmtNum(m * _pow10(-scale));
    final s = m.toString().padLeft(scale + 1, '0');
    final whole = s.substring(0, s.length - scale);
    final frac = s.substring(s.length - scale).replaceAll(RegExp(r'0+$'), '');
    return frac.isEmpty ? whole : '$whole,$frac';
  }

  static Exercise decimals(GenContext g) {
    final modes = g.pl('modes').isEmpty ? const ['mul10', 'div10', 'compare'] : g.pl('modes');
    final mode = g.pick(modes);
    final scale = g.range(1, 2);
    var m = g.range(11, 9999);
    if (m % 10 == 0) m += 1;
    final x = _dec(m, scale);
    switch (mode) {
      case 'compare':
        var m2 = m + g.range(-9, 9) * (g.chance(0.5) ? 1 : 10);
        if (m2 <= 0) m2 = m + 3;
        final s2 = g.range(1, 3);
        final v1 = m / _pow10(scale), v2 = m2 / _pow10(s2);
        final answer = v1 > v2 ? '>' : (v1 < v2 ? '<' : '=');
        return g.textChoice(
          question: 'Taqqoslang: $x ○ ${_dec(m2, s2)}',
          answer: answer,
          wrong: const ['>', '<', '='],
          options: 3,
          concept: 'decimal:compare',
          hint: 'Avval butun qismlarni, keyin verguldan keyingi raqamlarni xonama-xona solishtiring.',
          explanation: '$x $answer ${_dec(m2, s2)}',
        );
      case 'div10':
        final k = g.range(1, 3);
        final result = _dec(m, scale + k);
        return g.textAnswer(
          question: '$x : ${fmtNum(_pow10(k))} = ?',
          answer: result,
          accept: [result, if (result.startsWith('0,')) result.substring(1)],
          keys: 'decimal',
          concept: 'decimal:div10',
          hint: '10, 100, 1000 ga bo‘lishda vergul chapga 1, 2, 3 xona suriladi.',
          explanation: '$x : ${fmtNum(_pow10(k))} = $result',
        );
      default:
        final k = g.range(1, 3);
        final result = _dec(m, scale - k);
        return g.textAnswer(
          question: '$x · ${fmtNum(_pow10(k))} = ?',
          answer: result.replaceAll(' ', ''),
          accept: [result],
          keys: 'decimal',
          concept: 'decimal:mul10',
          hint: '10, 100, 1000 ga ko‘paytirishda vergul o‘ngga 1, 2, 3 xona suriladi.',
          explanation: '$x · ${fmtNum(_pow10(k))} = $result',
        );
    }
  }

  // ------------------------------------------------------------ Nisbat
  static Exercise ratio(GenContext g) {
    final modes = g.pl('modes').isEmpty ? const ['simplify', 'share', 'find'] : g.pl('modes');
    final mode = g.pick(modes);
    final p = g.range(1, 7);
    var q = g.range(1, 9);
    if (q == p) q = p + 1;
    final k = g.range(2, 8);
    switch (mode) {
      case 'share':
        final total = (p + q) * k;
        final askFirst = g.chance(0.5);
        return g.numberAnswer(
          question: 'Ikki son yig‘indisi $total ga, ularning nisbati esa $p : $q ga teng. ${askFirst ? 'Birinchi' : 'Ikkinchi'} sonni toping.',
          answer: (askFirst ? p : q) * k,
          input: g.useInput(),
          concept: 'ratio:share',
          hint: 'Jami ${p + q} ta teng bo‘lak: bir bo‘lak = $total : ${p + q}',
          explanation: '$total : ${p + q} = $k; $k · ${askFirst ? p : q} = ${(askFirst ? p : q) * k}',
        );
      case 'find':
        final a = p * k;
        return g.numberAnswer(
          question: 'Qizil va ko‘k qalamlar soni nisbati $p : $q. Qizil qalamlar $a ta. Ko‘k qalamlar nechta?',
          answer: q * k,
          input: g.useInput(),
          concept: 'ratio:find',
          hint: 'Bir bo‘lak = $a : $p. Ko‘k qalamlar $q bo‘lak.',
          explanation: '$a : $p = $k; $k · $q = ${q * k} ta',
        );
      default:
        final d = gcd(p, q);
        final answer = '${p ~/ d} : ${q ~/ d}';
        final boys = p * k, girls = q * k;
        return g.textChoice(
          question: 'Sinfda $boys o‘g‘il bola va $girls qiz bola bor. O‘g‘il bolalar sonining qizlar soniga nisbatini eng sodda ko‘rinishda toping.',
          answer: answer,
          wrong: ['${q ~/ d} : ${p ~/ d}', '$boys : $girls', '${p ~/ d} : ${(p + q) ~/ d}', '${p ~/ d + 1} : ${q ~/ d}'],
          concept: 'ratio:simplify',
          hint: 'Ikkala sonni ularning eng katta umumiy bo‘luvchisiga bo‘ling.',
          explanation: '$boys : $girls = $answer',
        );
    }
  }

  // ------------------------------------------------------------ Foiz
  static Exercise percent(GenContext g) {
    final modes = g.pl('modes').isEmpty ? const ['of', 'discount', 'fraction', 'decimal'] : g.pl('modes');
    final mode = g.pick(modes);
    switch (mode) {
      case 'discount':
        final price = g.range(4, 40) * 5000;
        final p = g.pick(const [10, 20, 25, 30, 50]);
        final cut = price * p ~/ 100;
        return g.numberAnswer(
          question: 'Kurtka ${fmtNum(price)} so‘m turadi. Do‘kon $p% chegirma berdi. Kurtka endi necha so‘m turadi?',
          answer: price - cut,
          input: g.useInput(),
          unit: 'so‘m',
          concept: 'percent:discount',
          hint: 'Avval chegirmani toping: ${fmtNum(price)} ning $p% i, keyin narxdan ayiring.',
          explanation: '${fmtNum(price)} · $p : 100 = ${fmtNum(cut)}; ${fmtNum(price)} − ${fmtNum(cut)} = ${fmtNum(price - cut)} so‘m',
        );
      case 'fraction':
        const pairs = [(1, 2), (1, 4), (3, 4), (1, 5), (2, 5), (3, 5), (4, 5), (1, 10), (3, 10), (7, 10), (1, 20), (1, 25), (9, 20)];
        final (a, b) = g.pick(pairs);
        return g.numberAnswer(
          question: '$a/$b kasrni foizda ifodalang',
          answer: a * 100 ~/ b,
          input: g.useInput(),
          unit: '%',
          concept: 'percent:fraction',
          hint: 'Maxrajni 100 ga keltiring: 1% = 1/100',
          explanation: '$a/$b = ${a * 100 ~/ b}/100 = ${a * 100 ~/ b}%',
        );
      case 'decimal':
        final p = g.range(1, 99);
        final dec = fmtDec(p / 100);
        return g.numberAnswer(
          question: '$dec sonini foizda ifodalang',
          answer: p,
          input: g.useInput(),
          unit: '%',
          concept: 'percent:decimal',
          hint: 'O‘nli kasrni 100 ga ko‘paytiring.',
          explanation: '$dec = $p%',
        );
      default:
        final p = g.pick(const [10, 20, 25, 50, 5, 15, 40, 75]);
        final unit = 100 ~/ gcd(p, 100);
        final n = unit * g.range(1, 20);
        return g.numberAnswer(
          question: '${fmtNum(n)} ning $p% ini toping',
          answer: n * p ~/ 100,
          input: g.useInput(),
          concept: 'percent:of',
          hint: 'Sonni 100 ga bo‘lib, $p ga ko‘paytiring.',
          explanation: '${fmtNum(n)} : 100 · $p = ${fmtNum(n * p ~/ 100)}',
        );
    }
  }

  // ------------------------------------------------------------ O'rtacha qiymat
  static Exercise average(GenContext g) {
    final count = g.range(3, 5);
    final mean = g.range(5, g.p('max', 60));
    final values = <int>[];
    var sum = 0;
    for (var i = 0; i < count - 1; i++) {
      final v = mean + g.range(-4, 4);
      values.add(v);
      sum += v;
    }
    final last = mean * count - sum;
    if (last <= 0) return average(g);
    values.add(last);
    values.shuffle(g.rng);
    final story = g.chance(0.5);
    final name = g.pick(names);
    return g.numberAnswer(
      question: story
          ? '$name $count kun kitob o‘qidi: ${values.join(', ')} bet. U kuniga o‘rtacha necha bet o‘qigan?'
          : '${values.join(', ')} sonlarining o‘rtacha qiymatini toping',
      answer: mean,
      input: g.useInput(),
      concept: 'average',
      hint: 'Barcha sonlarni qo‘shing va ular soniga ($count ga) bo‘ling.',
      explanation: '(${values.join(' + ')}) : $count = ${mean * count} : $count = $mean',
    );
  }

  // ------------------------------------------------------------ Uchburchak yuzi
  static Exercise triangleArea(GenContext g) {
    final max = g.p('max', 16);
    var b = g.range(2, max), h = g.range(2, max);
    if ((b * h).isOdd) b += 1;
    if (g.pb('composite') && g.chance(0.5)) {
      final w = g.range(2, max);
      final rect = b * w, tri = b * h ~/ 2;
      return g.numberAnswer(
        question: 'Shakl tomonlari $b sm va $w sm bo‘lgan to‘g‘ri to‘rtburchak va uning ustiga qo‘yilgan uchburchakdan iborat. '
            'Uchburchakning asosi $b sm, balandligi $h sm. Butun shaklning yuzi necha sm²?',
        answer: rect + tri,
        input: g.useInput(),
        unit: 'sm²',
        concept: 'geom:composite',
        hint: 'Shaklni bo‘laklarga ajrating: to‘g‘ri to‘rtburchak yuzi + uchburchak yuzi.',
        explanation: '$b · $w + $b · $h : 2 = $rect + $tri = ${rect + tri} sm²',
      );
    }
    return g.numberAnswer(
      question: 'Uchburchakning asosi $b sm, shu asosga tushirilgan balandligi $h sm. Uchburchakning yuzi necha sm²?',
      answer: b * h ~/ 2,
      input: g.useInput(),
      unit: 'sm²',
      concept: 'geom:triangle',
      hint: 'Uchburchak yuzi: S = asos · balandlik : 2',
      explanation: 'S = $b · $h : 2 = ${b * h ~/ 2} sm²',
    );
  }

  // ------------------------------------------------------------ Burchaklar
  static Exercise angles(GenContext g) {
    final modes = g.pl('modes').isEmpty ? const ['straight', 'vertical', 'triangle', 'right'] : g.pl('modes');
    final mode = g.pick(modes);
    switch (mode) {
      case 'vertical':
        final a = g.range(20, 160);
        return g.numberAnswer(
          question: 'Ikki to‘g‘ri chiziq kesishganda hosil bo‘lgan burchaklardan biri $a°. Unga vertikal burchak necha gradus?',
          answer: a,
          input: g.useInput(),
          unit: '°',
          concept: 'angles:vertical',
          hint: 'Vertikal burchaklar teng.',
          explanation: 'Vertikal burchaklar teng: $a°',
        );
      case 'triangle':
        final a = g.range(20, 100), b = g.range(20, 150 - a);
        return g.numberAnswer(
          question: 'Uchburchakning ikki burchagi $a° va $b°. Uchinchi burchagi necha gradus?',
          answer: 180 - a - b,
          input: g.useInput(),
          unit: '°',
          concept: 'angles:triangle',
          hint: 'Uchburchak burchaklarining yig‘indisi 180°.',
          explanation: '180° − $a° − $b° = ${180 - a - b}°',
        );
      case 'right':
        final a = g.range(10, 80);
        return g.numberAnswer(
          question: 'To‘g‘ri burchak ichidan nur o‘tkazildi. Hosil bo‘lgan burchaklardan biri $a°. Ikkinchisi necha gradus?',
          answer: 90 - a,
          input: g.useInput(),
          unit: '°',
          concept: 'angles:right',
          hint: 'To‘g‘ri burchak 90°.',
          explanation: '90° − $a° = ${90 - a}°',
        );
      default:
        final a = g.range(15, 165);
        return g.numberAnswer(
          question: 'To‘g‘ri chiziqdagi ikki qo‘shni burchakdan biri $a°. Ikkinchisi necha gradus?',
          answer: 180 - a,
          input: g.useInput(),
          unit: '°',
          concept: 'angles:straight',
          hint: 'To‘g‘ri chiziqdagi (yoyiq) burchak 180°.',
          explanation: '180° − $a° = ${180 - a}°',
        );
    }
  }

  // ------------------------------------------------------------ Tenglamalar
  static Exercise equation(GenContext g) {
    final max = g.p('max', 100);
    final forms = g.pl('forms').isEmpty ? const ['x+a', 'x-a', 'a-x', 'x*a', 'x/a', 'a/x'] : g.pl('forms');
    final form = g.pick(forms);
    final x = g.range(2, max);
    String eq;
    String hint;
    switch (form) {
      case 'x-a':
        final a = g.range(1, max);
        eq = 'x − $a = ${x - a < 0 ? 0 : x - a}';
        if (x - a < 0) return equation(g);
        hint = 'Noma’lum kamayuvchini topish uchun ayirmaga ayiriluvchini qo‘shing.';
      case 'a-x':
        final a = x + g.range(1, max);
        eq = '$a − x = ${a - x}';
        hint = 'Noma’lum ayiriluvchini topish uchun kamayuvchidan ayirmani ayiring.';
      case 'x*a':
        final a = g.range(2, 9);
        eq = 'x · $a = ${x * a}';
        hint = 'Noma’lum ko‘paytuvchini topish uchun ko‘paytmani ma’lum ko‘paytuvchiga bo‘ling.';
      case 'x/a':
        final a = g.range(2, 9);
        final xx = x * a;
        return g.numberAnswer(
          question: 'Tenglamani yeching: x : $a = $x. x = ?',
          answer: xx,
          input: g.useInput(),
          concept: 'equation:x/a',
          hint: 'Noma’lum bo‘linuvchini topish uchun bo‘linmani bo‘luvchiga ko‘paytiring.',
          explanation: 'x = $x · $a = $xx',
        );
      case 'a/x':
        final a = g.range(2, 9);
        return g.numberAnswer(
          question: 'Tenglamani yeching: ${x * a} : x = $a. x = ?',
          answer: x,
          input: g.useInput(),
          concept: 'equation:a/x',
          hint: 'Noma’lum bo‘luvchini topish uchun bo‘linuvchini bo‘linmaga bo‘ling.',
          explanation: 'x = ${x * a} : $a = $x',
        );
      default:
        final a = g.range(1, max);
        eq = 'x + $a = ${x + a}';
        hint = 'Noma’lum qo‘shiluvchini topish uchun yig‘indidan ma’lum qo‘shiluvchini ayiring.';
    }
    return g.numberAnswer(
      question: 'Tenglamani yeching: $eq. x = ?',
      answer: x,
      input: g.useInput(),
      concept: 'equation:$form',
      hint: hint,
      explanation: '$eq → x = $x',
    );
  }

  // ------------------------------------------------------------ Rim raqamlari
  static String toRoman(int n) {
    const values = [100, 90, 50, 40, 10, 9, 5, 4, 1];
    const symbols = ['C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
    final b = StringBuffer();
    var v = n;
    for (var i = 0; i < values.length; i++) {
      while (v >= values[i]) {
        b.write(symbols[i]);
        v -= values[i];
      }
    }
    return b.toString();
  }

  static Exercise roman(GenContext g) {
    final n = g.range(1, g.p('max', 39));
    final r = toRoman(n);
    if (g.chance(0.5)) {
      return g.numberAnswer(
        question: 'Rim raqamlarida yozilgan sonni arab raqamlari bilan yozing: $r',
        answer: n,
        input: g.useInput(),
        concept: 'roman:read',
        hint: 'I = 1, V = 5, X = 10, L = 50. Kichik raqam kattasidan oldin kelsa, ayiriladi (IV = 4).',
        explanation: '$r = $n',
      );
    }
    final wrong = <String>{
      toRoman(n + 1),
      if (n > 1) toRoman(n - 1),
      toRoman(n + 5),
      if (n > 5) toRoman(n - 5),
    }.where((w) => w != r).toList();
    return g.textChoice(
      question: '$n soni Rim raqamlarida qanday yoziladi?',
      answer: r,
      wrong: wrong,
      concept: 'roman:write',
      hint: 'I = 1, V = 5, X = 10, L = 50.',
      explanation: '$n = $r',
    );
  }

  // ------------------------------------------------------------ Vaqt
  static String _clock(int minutes) {
    final m = minutes % (24 * 60);
    return '${m ~/ 60}:${(m % 60).toString().padLeft(2, '0')}';
  }

  static Exercise timeCalc(GenContext g) {
    final start = g.range(7 * 12, 18 * 12) * 5;
    final dur = g.range(3, 30) * 5;
    if (g.chance(0.5)) {
      final end = _clock(start + dur);
      return g.textChoice(
        question: 'Dars ${_clock(start)} da boshlanib, $dur minut davom etdi. Dars soat nechada tugadi?',
        answer: end,
        wrong: [_clock(start + dur + 10), _clock(start + dur - 10), _clock(start + dur + 60), _clock(start + dur - 5)],
        concept: 'time:end',
        hint: 'Boshlanish vaqtiga davomiylikni qo‘shing: 60 minut = 1 soat.',
        explanation: '${_clock(start)} + $dur min = $end',
      );
    }
    return g.numberAnswer(
      question: 'Multfilm ${_clock(start)} da boshlanib, ${_clock(start + dur)} da tugadi. U necha minut davom etdi?',
      answer: dur,
      input: g.useInput(),
      unit: 'min',
      concept: 'time:duration',
      hint: 'Tugash vaqtidan boshlanish vaqtini ayiring: 1 soat = 60 minut.',
      explanation: '${_clock(start + dur)} − ${_clock(start)} = $dur minut',
    );
  }

  // ------------------------------------------------------------ To'plamlar
  static String _set(Iterable<int> s) => '{${(s.toList()..sort()).join(', ')}}';

  static Exercise sets(GenContext g) {
    final a = <int>{};
    final b = <int>{};
    while (a.length < 4) {
      a.add(g.range(1, 15));
    }
    final common = g.sample(a.toList(), g.range(1, 2));
    b.addAll(common);
    while (b.length < 4) {
      final v = g.range(1, 15);
      if (!a.contains(v)) b.add(v);
    }
    final mode = g.range(0, 2);
    if (mode == 0) {
      final answer = _set(a.intersection(b));
      return g.textChoice(
        question: 'A = ${_set(a)}, B = ${_set(b)}. A va B to‘plamlarning umumiy elementlari qaysilar?',
        answer: answer,
        wrong: [_set(a.union(b)), _set(a.difference(b)), _set(b.difference(a)), _set(a)],
        concept: 'sets:intersection',
        hint: 'Umumiy elementlar — ikkala to‘plamda ham bor sonlar.',
        explanation: 'A ∩ B = $answer',
      );
    }
    if (mode == 1) {
      final union = a.union(b);
      return g.numberAnswer(
        question: 'A = ${_set(a)}, B = ${_set(b)}. A va B to‘plamlarning birlashmasida nechta element bor?',
        answer: union.length,
        input: g.useInput(),
        concept: 'sets:union',
        hint: 'Ikkala to‘plam elementlarini bir marta sanang (takrorlarini bir marta).',
        explanation: 'A ∪ B = ${_set(union)} — ${union.length} ta',
      );
    }
    final inA = g.chance(0.5);
    final v = inA ? g.pick(a.toList()) : g.pick([for (var i = 1; i <= 15; i++) if (!a.contains(i)) i]);
    return g.textChoice(
      question: '$v soni A = ${_set(a)} to‘plamga tegishlimi?',
      answer: inA ? 'Ha, tegishli' : 'Yo‘q, tegishli emas',
      wrong: [inA ? 'Yo‘q, tegishli emas' : 'Ha, tegishli'],
      options: 2,
      concept: 'sets:member',
      hint: 'To‘plam elementlari qavs ichida sanab o‘tilgan.',
      explanation: inA ? '$v ∈ A' : '$v ∉ A',
    );
  }
}
