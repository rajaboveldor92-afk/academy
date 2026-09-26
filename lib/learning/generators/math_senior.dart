import 'package:flutter/painting.dart';

import '../content/uz_numbers.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';
import 'math_junior.dart';

/// Azamjon (6 yosh) matematikasi: KO'R → TUSHUN → TANLA → HISOBLA → YECH → IZOHNI KO'R.
/// 1-sinf dasturidan oshmaydi: 20 ichida hisob, 100 gacha sonlar, soat va pul.
class MathSenior {
  MathSenior._();

  static final Map<String, ExerciseGenerator> generators = {
    'count_objects': MathJunior.countObjects,
    'ten_frame': tenFrame,
    'neighbors': neighbors,
    'compare_numbers': compareNumbers,
    'arith': arith,
    'missing_number': missingNumber,
    'sequence': sequence,
    'even_odd': evenOdd,
    'skip_count': skipCount,
    'hundred': hundred,
    'word_problem': wordProblem,
    'shapes6': shapes6,
    'spatial': spatial,
    'clock': clock,
    'money': money,
  };

  static const Color _dot = Color(0xFFE53935);
  static const Color _empty = Color(0xFFE0E0E0);

  /// O'nlik ramka(lar): har biri 2×5 katak.
  static SceneVisual tenFrames(int n, {int frames = 2}) {
    final items = <SceneItem>[];
    const cell = 0.085;
    for (var f = 0; f < frames; f++) {
      final baseX = frames == 1 ? 0.28 : 0.06 + f * 0.5;
      for (var i = 0; i < 10; i++) {
        final r = i ~/ 5, c = i % 5;
        final filled = f * 10 + i < n;
        items.add(SceneItem(
          kind: SceneKind.shape,
          value: filled ? 'circle' : 'square',
          color: filled ? _dot : _empty,
          x: baseX + c * cell + cell / 2,
          y: 0.32 + r * 0.36,
          size: filled ? 0.3 : 0.32,
        ));
      }
    }
    return SceneVisual(items, aspect: 2.4);
  }

  // ------------------------------------------------------------ M2 0–20 (o'nlik ramka)
  static Exercise tenFrame(GenContext g) {
    final min = g.p('min', 11), max = g.p('max', 15);
    final n = g.range(min, max);
    return g.choice(
      say: g.say('count_dots'),
      visual: tenFrames(n, frames: n > 10 ? 2 : 1),
      options: [for (final v in g.numberChoices(n, min: 0, max: 20, spread: 2)) Opt.number(v)],
      concept: 'number:$n',
      meta: {'answer': n, 'dots': n},
      hint: 'To‘la ramkada 10 ta. Keyin qolganini qo‘sh.',
      explanation: n > 10 ? '10 + ${n - 10} = $n' : '$n',
    );
  }

  // ------------------------------------------------------------ M3 Oldingi va keyingi
  static Exercise neighbors(GenContext g) {
    final max = g.p('max', 10);
    final asks = g.pl('ask').isEmpty ? ['after', 'before'] : g.pl('ask');
    final ask = g.pick(asks);
    int n;
    int answer;
    switch (ask) {
      case 'before':
        n = g.range(1, max);
        answer = n - 1;
      case 'between':
        n = g.range(0, max - 2);
        answer = n + 1;
      default:
        n = g.range(0, max - 1);
        answer = n + 1;
    }
    final text = switch (ask) {
      'before' => '? , $n',
      'between' => '$n , ? , ${n + 2}',
      _ => '$n , ?',
    };
    return g.choice(
      say: ask == 'between' ? g.say('number_between', {'a': n, 'b': n + 2}) : g.say('number_$ask', {'n': n}),
      visual: TextVisual(text),
      options: [for (final v in g.numberChoices(answer, min: 0, max: max + 1, spread: 2)) Opt.number(v)],
      concept: 'number:$answer',
      meta: {'n': n, 'ask': ask, 'answer': answer},
      explanation: ask == 'before' ? '$answer + 1 = $n' : '$n + 1 = ${n + 1}',
    );
  }

  // ------------------------------------------------------------ M4 Katta, kichik, teng
  static Exercise compareNumbers(GenContext g) {
    final max = g.p('max', 10);
    final withExpr = g.pb('expressions');
    int a, b;
    String left;
    if (withExpr) {
      final x = g.range(1, max - 2), y = g.range(1, max - x);
      a = x + y;
      left = '$x + $y';
      b = g.chance(0.34) ? a : g.range(1, max);
    } else {
      a = g.range(0, max);
      b = g.chance(0.25) ? a : g.range(0, max);
      left = '$a';
    }
    final sign = a > b ? '>' : (a < b ? '<' : '=');
    return g.choice(
      say: g.say('compare_sign'),
      visual: TextVisual('$left  ☐  $b'),
      options: [Opt.text(sign), for (final s in ['>', '<', '='].where((s) => s != sign)) Opt.text(s)],
      concept: 'compare:$sign',
      meta: {'a': a, 'b': b, 'op': 'cmp', 'answer': sign},
      hint: 'Qush tumshug‘i katta songa ochiladi: 5 > 3.',
      explanation: '$left $sign $b',
    );
  }

  // ------------------------------------------------------------ M5–M8 Qo'shish / ayirish
  /// Rejimlar: `pictures` (rasmli), `plain`, `tens` (10 + n), `nocarry`, `carry`,
  /// `maketen` (7 + ? = 10).
  static Exercise arith(GenContext g) {
    final op = g.ps('op', '+');
    final max = g.p('max', 10);
    final mode = g.pick(g.pl('modes').isEmpty ? ['plain'] : g.pl('modes'));
    int a, b;
    var result = 0;
    var tries = 0;
    do {
      switch (mode) {
        case 'tens':
          if (op == '+') {
            a = 10;
            b = g.range(1, max - 10);
          } else {
            a = g.range(11, max);
            b = a - 10;
          }
        case 'nocarry':
          if (op == '+') {
            a = g.range(11, max - 2 < 11 ? 11 : max - 2);
            b = g.range(1, 9 - (a % 10));
          } else {
            a = g.range(12, 19);
            b = g.range(1, a % 10);
          }
        case 'carry':
          if (op == '+') {
            a = g.range(5, 9);
            b = g.range(11 - a, 9);
          } else {
            a = g.range(11, 18);
            b = g.range((a % 10) + 1, 9);
          }
        case 'maketen':
          a = g.range(1, 9);
          b = 10 - a;
        default:
          if (op == '+') {
            a = g.range(0, max);
            b = g.range(0, max - a);
          } else {
            a = g.range(1, max);
            b = g.range(0, a);
          }
      }
      result = op == '+' ? a + b : a - b;
      tries++;
    } while ((result < 0 || result > max || (mode == 'pictures' && (a == 0 || b == 0))) && tries < 50);

    if (mode == 'maketen') {
      return g.choice(
        say: g.say('make_ten'),
        visual: TextVisual('$a + ? = 10'),
        options: [for (final v in g.numberChoices(b, min: 0, max: 10, spread: 2)) Opt.number(v)],
        concept: 'bond10:$a',
        meta: {'a': a, 'b': b, 'op': '+', 'answer': b, 'total': 10},
        hint: 'Barmoqlaringda $a ni ko‘rsat. 10 gacha nechta yetmaydi?',
        explanation: '$a + $b = 10',
      );
    }

    final sign = op == '+' ? '+' : '−';
    ExerciseVisual visual;
    if (mode == 'pictures') {
      final item = g.pick(g.countables());
      visual = op == '+'
          ? SceneVisual([
              ...Layouts.group(item.emoji, a, left: 0.02, right: 0.42, aspect: 2.4),
              Layouts.text('+', x: 0.5, size: 0.4, color: const Color(0xFF4F7CF7)),
              ...Layouts.group(item.emoji, b, left: 0.58, right: 0.98, aspect: 2.4),
            ], aspect: 2.4)
          : SceneVisual(Layouts.group(item.emoji, a, aspect: 2, crossedFromEnd: true, crossed: b), aspect: 2);
    } else {
      visual = TextVisual('$a $sign $b = ?');
    }
    final hint = switch (mode) {
      'carry' when op == '+' => 'Avval 10 gacha to‘ldir: $a + ${10 - a} = 10, keyin qolganini qo‘sh.',
      'carry' => 'Avval 10 gacha ayir: $a − ${a - 10} = 10, keyin qolganini ayir.',
      _ => op == '+' ? 'Kattaroq sondan boshlab sanab qo‘sh.' : 'Orqaga sanab ayir.',
    };
    return g.choice(
      say: g.say(op == '+' ? 'solve_add' : 'solve_sub', {'a': a, 'b': b}),
      visual: visual,
      options: [for (final v in g.numberChoices(result, min: 0, max: max, spread: 3)) Opt.number(v)],
      concept: op == '+' ? 'add:$a+$b' : 'sub:$a-$b',
      meta: {'a': a, 'b': b, 'op': op, 'answer': result},
      hint: hint,
      explanation: '$a $sign $b = $result',
    );
  }

  // ------------------------------------------------------------ M9 Yetishmayotgan son
  static Exercise missingNumber(GenContext g) {
    final max = g.p('max', 10);
    final forms = g.pl('forms').isEmpty ? ['a+?=c'] : g.pl('forms');
    final form = g.pick(forms);
    final c = g.range(2, max);
    final a = g.range(0, c);
    final b = c - a;
    late String text;
    late int answer;
    switch (form) {
      case '?+b=c':
        text = '? + $b = $c';
        answer = a;
      case 'a-?=b':
        text = '$c − ? = $a';
        answer = b;
      case '?-a=b':
        text = '? − $a = $b';
        answer = c;
      default:
        text = '$a + ? = $c';
        answer = b;
    }
    return g.choice(
      say: g.say('missing_number'),
      visual: TextVisual(text),
      options: [for (final v in g.numberChoices(answer, min: 0, max: max, spread: 3)) Opt.number(v)],
      concept: 'missing:$form',
      meta: {'form': form, 'a': a, 'b': b, 'c': c, 'answer': answer},
      hint: 'Javobni ? o‘rniga qo‘yib tekshir.',
      explanation: text.replaceFirst('?', '$answer'),
    );
  }

  // ------------------------------------------------------------ M10 Sonli ketma-ketlik
  static Exercise sequence(GenContext g) {
    final steps = g.pl('steps').isEmpty ? ['1'] : g.pl('steps');
    final step = int.parse(g.pick(steps));
    final max = g.p('max', 20);
    final len = g.p('length', 4);
    final missingPos = g.pb('missingInside') && g.chance(0.5) ? g.range(1, len - 1) : len;
    int start;
    if (step > 0) {
      final hi = max - step * len;
      start = g.range(0, hi < 0 ? 0 : hi);
    } else {
      start = g.range(-step * len, max);
    }
    final seq = [for (var i = 0; i <= len; i++) start + step * i];
    final answer = seq[missingPos];
    final shown = [for (var i = 0; i <= len; i++) i == missingPos ? '?' : '${seq[i]}'];
    return g.choice(
      say: g.say('continue_sequence'),
      visual: TextVisual(shown.join(', ')),
      options: [for (final v in g.numberChoices(answer, min: 0, max: max + 10, spread: 3)) Opt.number(v)],
      concept: 'sequence:$step',
      meta: {'start': start, 'step': step, 'index': missingPos, 'answer': answer},
      hint: step > 0 ? 'Har safar nechtaga oshyapti?' : 'Har safar nechtaga kamayyapti?',
      explanation: step > 0 ? 'Har safar +$step' : 'Har safar −${-step}',
    );
  }

  // ------------------------------------------------------------ M11 Juft / toq
  static Exercise evenOdd(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['pairs'] : g.pl('modes'));
    final max = g.p('max', 10);
    if (mode == 'pairs') {
      final n = g.range(2, 10);
      final item = g.pick(g.countables());
      final even = n.isEven;
      return g.choice(
        say: g.say('can_pair', {'item': item}),
        visual: SceneVisual(Layouts.group(item.emoji, n, aspect: 2.2), aspect: 2.2),
        options: [
          Opt.text(even ? 'Ha, hammasi juft' : 'Yo‘q, bittasi ortadi'),
          Opt.text(even ? 'Yo‘q, bittasi ortadi' : 'Ha, hammasi juft'),
        ],
        concept: 'parity:${even ? "even" : "odd"}',
        meta: {'n': n, 'answer': even ? 'even' : 'odd'},
        hint: 'Ikkitadan birlashtirib ko‘r.',
        explanation: even ? '$n — juft son.' : '$n — toq son, bittasi ortib qoladi.',
      );
    }
    final wantEven = mode == 'even';
    final pool = [for (var i = 1; i <= max; i++) i];
    final correct = g.pick(pool.where((v) => v.isEven == wantEven).toList());
    final wrong = g.sample(pool.where((v) => v.isEven != wantEven).toList(), 2);
    return g.choice(
      say: g.say(wantEven ? 'find_even' : 'find_odd'),
      options: [Opt.number(correct), for (final w in wrong) Opt.number(w)],
      concept: 'parity:${wantEven ? "even" : "odd"}',
      meta: {'answer': correct, 'parity': wantEven ? 'even' : 'odd'},
      hint: 'Juft sonlar: 2, 4, 6, 8, 10 …',
      explanation: wantEven ? '$correct — juft.' : '$correct — toq.',
    );
  }

  // ------------------------------------------------------------ M12–M14 2, 5, 10 tadan sanash
  static Exercise skipCount(GenContext g) {
    final step = g.p('step', 2);
    final mode = g.pick(g.pl('modes').isEmpty ? ['groups'] : g.pl('modes'));
    final maxGroups = g.p('maxGroups', 5);

    // Chalg'ituvchilar: bir qadam kam/ko'p va yaqin sonlar.
    List<int> choices(int answer) {
      final result = <int>[answer];
      final pool = <int>{answer + step, answer - step, answer + 1, answer - 1, answer + 2}
        ..removeWhere((v) => v <= 0 || v == answer);
      result.addAll(g.sample(pool.toList(), 2));
      return result;
    }

    if (mode == 'sequence') {
      const len = 4;
      final hi = maxGroups - len - 1;
      final startK = g.range(0, hi < 0 ? 0 : hi);
      final seq = [for (var i = 1; i <= len + 1; i++) (startK + i) * step];
      final answer = seq.last;
      return g.choice(
        say: g.say('count_by', {'n': step}),
        visual: TextVisual('${seq.take(len).join(', ')}, ?'),
        options: [for (final v in choices(answer)) Opt.number(v)],
        concept: 'skip:$step',
        meta: {'start': seq.first, 'step': step, 'index': len, 'answer': answer},
        explanation: '${seq.take(len).join(' → ')} → $answer',
      );
    }
    final groups = g.range(2, maxGroups > 6 ? 6 : maxGroups);
    final answer = groups * step;
    ExerciseVisual visual;
    if (step == 10) {
      visual = SceneVisual([
        for (var i = 0; i < groups; i++)
          ...tenFrames(10, frames: 1).items.map((it) => it.copyWith(
                x: (i % 3) * 0.33 + (it.x - 0.28) * 0.6 + 0.04,
                y: (i ~/ 3) * 0.5 + it.y * 0.42 + 0.04,
                size: it.size * 0.45,
              )),
      ], aspect: 2.4);
    } else {
      // Har bir guruh — alohida "tovoqcha": 2 tadan juftliklar yoki 5 tadan qatorlar.
      final item = step == 2
          ? g.pick(['🧦', '🧤', '👟', '👞', '👢', '🍒', '👀'])
          : g.pick(g.countables()).emoji;
      final cols = groups <= 3 ? groups : 3;
      final rows = (groups / cols).ceil();
      final items = <SceneItem>[];
      for (var i = 0; i < groups; i++) {
        final c = i % cols, r = i ~/ cols;
        final left = c / cols + 0.02, right = (c + 1) / cols - 0.02;
        final top = r / rows + 0.04, bottom = (r + 1) / rows - 0.04;
        items.add(SceneItem(
          kind: SceneKind.bar,
          value: 'plate',
          color: const Color(0xFFFFF3D6),
          x: (left + right) / 2,
          y: (top + bottom) / 2,
          size: (bottom - top),
          length: right - left,
        ));
        items.addAll(Layouts.group(item, step, left: left + 0.02, right: right - 0.02, top: top, bottom: bottom, aspect: 2.4));
      }
      visual = SceneVisual(items, aspect: 2.4);
    }
    return g.choice(
      say: g.say(step == 2 ? 'count_pairs' : (step == 5 ? 'count_fingers' : 'count_tens')),
      visual: visual,
      options: [for (final v in choices(answer)) Opt.number(v)],
      concept: 'skip:$step',
      meta: {'groups': groups, 'step': step, 'answer': answer},
      hint: '$step tadan sana: ${[for (var i = 1; i <= 3; i++) i * step].join(', ')} …',
      explanation: '${[for (var i = 1; i <= groups; i++) i * step].join(', ')} — hammasi $answer',
    );
  }

  // ------------------------------------------------------------ M15 0–100
  static Exercise hundred(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['read'] : g.pl('modes'));
    switch (mode) {
      case 'tens_ones':
        final t = g.range(1, 9), o = g.range(0, 9);
        final n = t * 10 + o;
        final swapped = o * 10 + t;
        final opts = <int>{n, if (swapped != n && swapped > 0) swapped, n + 10 <= 99 ? n + 10 : n - 10, n + 1 <= 99 ? n + 1 : n - 1};
        return g.choice(
          say: g.say('tens_and_ones', {'t': t, 'o': o}),
          visual: SceneVisual([
            ...Layouts.group('🔟', t, left: 0.02, right: 0.55, aspect: 2.4),
            if (o > 0) ...Layouts.group('1️⃣', o, left: 0.6, right: 0.98, aspect: 2.4),
          ], aspect: 2.4),
          options: [for (final v in opts.take(3)) Opt.number(v)],
          concept: 'place_value:$n',
          meta: {'tens': t, 'ones': o, 'answer': n},
          explanation: '$t o‘nlik va $o birlik = $n',
        );
      case 'compare':
        final a = g.range(10, 99);
        var b = g.range(10, 99);
        while (b == a) {
          b = g.range(10, 99);
        }
        final bigger = a > b ? a : b;
        return g.choice(
          say: g.say('which_bigger'),
          options: [Opt.number(bigger), Opt.number(a > b ? b : a)],
          concept: 'compare100',
          meta: {'a': a, 'b': b, 'answer': bigger},
          hint: 'Avval o‘nliklarni solishtir.',
          explanation: '${a > b ? a : b} > ${a > b ? b : a}',
        );
      default:
        final t = g.range(1, 9), o = g.range(1, 9);
        final n = t * 10 + o;
        final swapped = o * 10 + t;
        final opts = <int>{n, if (swapped != n) swapped, t * 10 + ((o + 2) % 10)};
        while (opts.length < 3) {
          opts.add(g.range(10, 99));
        }
        return g.choice(
          say: g.say('find_numeral', {'n': n}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final v in opts) Opt.number(v)],
          concept: 'number:$n',
          meta: {'answer': n},
          explanation: '$n — ${UzNumbers.word(n)}',
        );
    }
  }

  // ------------------------------------------------------------ M16 Matnli masalalar
  static const _names = ['Ali', 'Nodira', 'Sardor', 'Malika', 'Bobur', 'Zarina', 'Jasur', 'Laylo'];

  static Exercise wordProblem(GenContext g) {
    final max = g.p('max', 10);
    final types = g.pl('types').isEmpty ? ['add'] : g.pl('types');
    final type = g.pick(types);
    final item = g.pick(g.lex.entries
        .where((e) => const {'fruit', 'toy', 'food'}.contains(e.category) && e.ageMin <= 6)
        .toList());
    final names = g.sample(_names, 2);
    late int a, b, answer;
    late String key;
    switch (type) {
      case 'sub':
        a = g.range(3, max);
        b = g.range(1, a - 1);
        answer = a - b;
        key = 'problem_sub';
      case 'compare':
        a = g.range(3, max);
        b = g.range(1, a - 1);
        answer = a - b;
        key = 'problem_compare';
      default:
        a = g.range(1, max - 1);
        b = g.range(1, max - a);
        answer = a + b;
        key = 'problem_add';
    }
    final say = g.say(key, {'name': names[0], 'name2': names[1], 'a': a, 'b': b, 'item': item});
    final visual = SceneVisual([
      ...Layouts.group(item.emoji, a, left: 0.02, right: 0.46, aspect: 2.4),
      if (type == 'compare') ...Layouts.group(item.emoji, b, left: 0.54, right: 0.98, aspect: 2.4),
    ], aspect: 2.4);
    final sign = type == 'add' ? '+' : '−';
    return g.choice(
      say: say,
      visual: visual,
      options: [for (final v in g.numberChoices(answer, min: 0, max: max, spread: 3)) Opt.number(v)],
      concept: 'word:$type',
      meta: {'a': a, 'b': b, 'op': type == 'add' ? '+' : '-', 'answer': answer},
      hint: type == 'add' ? 'Ko‘paydimi? Unda qo‘shamiz.' : 'Kamaydimi yoki farqmi? Unda ayiramiz.',
      explanation: '$a $sign $b = $answer',
    );
  }

  // ------------------------------------------------------------ M17 Shakllar
  static const _objectShapes = {
    'ball': 'circle',
    'clock': 'circle',
    'cookie': 'circle',
    'egg': 'oval',
    'dice': 'square',
    'tv': 'rectangle',
    'books': 'rectangle',
    'notebook': 'rectangle',
    'star': 'star',
    'pizza': 'triangle',
  };

  static Exercise shapes6(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['name'] : g.pl('modes'));
    final colorsPool = g.lex.colors.where((c) => !{'white', 'black'}.contains(c.id)).toList();
    switch (mode) {
      case 'corners':
        final shape = g.pick(g.lex.shapes.where((s) => {'triangle', 'square', 'rectangle', 'rhombus', 'circle'}.contains(s.id)).toList());
        final answer = shape.corners;
        return g.choice(
          say: g.say('how_many_corners', {'shape': shape}),
          visual: SceneVisual([Layouts.shape(shape.id, g.pick(colorsPool).color, size: 0.8)], aspect: 1.6),
          options: [
            for (final v in answer == 0 ? {0, 1, 2} : {answer, answer - 1, answer + 1}) Opt.number(v),
          ],
          concept: 'shape:${shape.id}',
          meta: {'answer': answer},
          explanation: '${shape.name.uz}: $answer ta burchak',
        );
      case 'objects':
        final entry = g.pick(_objectShapes.entries.toList());
        final obj = g.lex.byId(entry.key);
        final shape = g.lex.shape(entry.value);
        final wrong = g.sample(g.lex.shapes.where((s) => s.id != shape.id && s.id != 'heart').toList(), 2);
        return g.choice(
          say: g.say('object_shape', {'item': obj}),
          visual: SceneVisual([Layouts.emoji(obj.emoji, size: 0.8)], aspect: 1.6),
          options: [
            Opt.shape(shape.id, const Color(0xFF4F7CF7)),
            for (final w in wrong) Opt.shape(w.id, const Color(0xFF4F7CF7)),
          ],
          concept: 'shape:${shape.id}',
          meta: {'answer': shape.id},
          explanation: '${obj.uz} — ${shape.name.uz} shaklida.',
        );
      default:
        final chosen = g.sample(g.lex.shapes.toList(), g.p('options', 4));
        return g.choice(
          say: g.say('find_shape', {'shape': chosen.first}),
          options: [for (final s in chosen) Opt.shape(s.id, g.pick(colorsPool).color)],
          concept: 'shape:${chosen.first.id}',
          meta: {'answer': chosen.first.id},
        );
    }
  }

  // ------------------------------------------------------------ M18 Fazoviy tushunchalar
  static const _relations = ['on', 'under', 'in', 'next'];

  static Exercise spatial(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['box'] : g.pl('modes'));
    if (mode == 'ordinal') {
      final count = g.p('items', 5);
      final items = g.sample(g.countables(), count);
      final k = g.range(1, count);
      final fromLeft = g.chance(0.6);
      final idx = fromLeft ? k - 1 : count - k;
      return g.choice(
        say: g.say(fromLeft ? 'nth_from_left' : 'nth_from_right', {
          'k': Localized(uz: UzNumbers.ordinal(k), en: '$k', ru: '$k'),
        }),
        visual: SceneVisual(Layouts.row([for (final e in items) Layouts.emoji(e.emoji, size: 0.5)]), aspect: count * 0.8),
        options: [
          Opt.emoji(items[idx].emoji),
          for (final i in g.sample([for (var i = 0; i < count; i++) if (i != idx) i], 2)) Opt.emoji(items[i].emoji),
        ],
        concept: 'ordinal:$k',
        meta: {'answer': items[idx].id},
      );
    }
    if (mode == 'grid') {
      final cells = g.sample(g.countables(), 9);
      final center = g.range(0, 8);
      final r = center ~/ 3, c = center % 3;
      final dirs = <String, int>{
        if (c > 0) 'left': center - 1,
        if (c < 2) 'right': center + 1,
        if (r > 0) 'above': center - 3,
        if (r < 2) 'below': center + 3,
      };
      final dir = g.pick(dirs.keys.toList());
      final answer = cells[dirs[dir]!];
      final wrong = g.sample([for (var i = 0; i < 9; i++) if (i != dirs[dir] && i != center) cells[i]], 2);
      return g.choice(
        say: g.say('grid_$dir', {'item': cells[center]}),
        visual: GridVisual(rows: 3, cols: 3, cells: [for (final e in cells) [Layouts.emoji(e.emoji, size: 0.7)]], showQuestionMark: false),
        options: [Opt.emoji(answer.emoji), for (final w in wrong) Opt.emoji(w.emoji)],
        concept: 'spatial:$dir',
        meta: {'answer': answer.id},
      );
    }
    // Quti atrofida: ustida / ostida / ichida / yonida.
    final rel = g.pick(_relations);
    final animal = g.pick(g.category('animal'));
    const box = '📦';
    final pos = switch (rel) {
      'on' => (0.5, 0.2, 1.0),
      'under' => (0.5, 0.86, 1.0),
      'in' => (0.5, 0.55, 0.6),
      _ => (0.82, 0.58, 1.0),
    };
    final scene = <SceneItem>[
      SceneItem(kind: SceneKind.emoji, value: box, x: 0.5, y: 0.56, size: 0.52),
      SceneItem(kind: SceneKind.emoji, value: animal.emoji, x: pos.$1, y: pos.$2, size: 0.3, opacity: pos.$3),
    ];
    final labels = {
      'on': 'Qutining ustida',
      'under': 'Qutining ostida',
      'in': 'Qutining ichida',
      'next': 'Qutining yonida',
    };
    return g.choice(
      say: g.say('where_is', {'item': animal}),
      visual: SceneVisual(scene, aspect: 1.5),
      options: [
        Opt.text(labels[rel]!, speech: labels[rel]),
        for (final o in g.sample(_relations.where((x) => x != rel).toList(), 2)) Opt.text(labels[o]!, speech: labels[o]),
      ],
      concept: 'spatial:$rel',
      meta: {'answer': rel},
    );
  }

  // ------------------------------------------------------------ M19 Soat
  static Exercise clock(GenContext g) {
    final half = g.pb('half');
    final reverse = g.pb('reverse');
    final hour = g.range(1, 12);
    final minute = half && g.chance(0.6) ? 30 : 0;
    String fmt(int h, int m) => '$h:${m.toString().padLeft(2, '0')}';
    final wrongs = <(int, int)>{};
    while (wrongs.length < 2) {
      final h = ((hour + g.range(1, 5) * (g.chance(0.5) ? 1 : -1) - 1) % 12) + 1;
      final m = half ? g.pick([0, 30]) : 0;
      if (h != hour || m != minute) wrongs.add((h, m));
    }
    if (reverse) {
      return g.choice(
        say: g.say('find_clock', {'time': fmt(hour, minute)}),
        visual: TextVisual(fmt(hour, minute)),
        options: [
          ExerciseOption(visual: ClockVisual(hour, minute)),
          for (final w in wrongs) ExerciseOption(visual: ClockVisual(w.$1, w.$2)),
        ],
        concept: 'clock:$hour:$minute',
        meta: {'hour': hour, 'minute': minute},
      );
    }
    return g.choice(
      say: g.say('what_time'),
      visual: ClockVisual(hour, minute),
      options: [Opt.text(fmt(hour, minute)), for (final w in wrongs) Opt.text(fmt(w.$1, w.$2))],
      concept: 'clock:$hour:$minute',
      meta: {'hour': hour, 'minute': minute, 'answer': fmt(hour, minute)},
      hint: minute == 30 ? 'Uzun strelka pastda — yarim soat.' : 'Uzun strelka tepada — soat to‘liq.',
      explanation: minute == 30 ? 'Soat $hour yarim' : 'Soat $hour',
    );
  }

  // ------------------------------------------------------------ M20 Pul
  static const _coinColors = {
    1: Color(0xFFB0BEC5),
    2: Color(0xFFBCAAA4),
    5: Color(0xFFFFD54F),
    10: Color(0xFFFFB74D),
  };

  static List<SceneItem> _coins(List<int> values, {double left = 0.04, double right = 0.96}) {
    final n = values.length;
    final step = (right - left) / n;
    return [
      for (var i = 0; i < n; i++)
        SceneItem(
          kind: SceneKind.coin,
          value: '${values[i]}',
          color: _coinColors[values[i]],
          x: left + step * (i + 0.5),
          y: 0.5,
          size: (step * 2.4).clamp(0.2, 0.55).toDouble(),
        ),
    ];
  }

  static Exercise money(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['count'] : g.pl('modes'));
    final max = g.p('max', 10);
    if (mode == 'enough') {
      final price = g.range(3, max);
      final item = g.pick(g.lex.entries.where((e) => const {'toy', 'food', 'fruit'}.contains(e.category) && e.ageMin <= 6).toList());
      List<int> purse(int total) {
        final res = <int>[];
        var left = total;
        for (final c in const [10, 5, 2, 1]) {
          while (left >= c) {
            res.add(c);
            left -= c;
          }
        }
        return res;
      }

      final enoughAmount = price + g.range(0, 2);
      final low = g.sample([for (var v = 1; v < price; v++) v], 2);
      return g.choice(
        say: g.say('enough_money', {'item': item, 'n': price}),
        visual: SceneVisual([
          Layouts.emoji(item.emoji, x: 0.35, size: 0.6),
          Layouts.text('$price so‘m', x: 0.72, size: 0.26),
        ], aspect: 2.2),
        options: [
          Opt.scene(_coins(purse(enoughAmount)), aspect: 2.8),
          for (final v in low) Opt.scene(_coins(purse(v)), aspect: 2.8),
        ],
        concept: 'money:enough',
        meta: {'price': price, 'answer': enoughAmount, 'others': low.join(',')},
        hint: 'Har bir hamyondagi tangalarni qo‘shib chiq.',
      );
    }
    final List<int> coins;
    if (mode == 'count') {
      final v = g.pick([1, 2]);
      final k = g.range(2, max ~/ v);
      coins = List<int>.filled(k, v);
    } else {
      coins = [];
      var total = 0;
      final target = g.range(4, max);
      for (final c in [10, 5, 2, 1]) {
        while (total + c <= target && coins.length < 6 && (c != 10 || target >= 10)) {
          if (c == 10 && g.chance(0.5)) break;
          coins.add(c);
          total += c;
        }
      }
      coins.shuffle(g.rng);
    }
    final total = coins.fold<int>(0, (s, v) => s + v);
    return g.choice(
      say: g.say('how_much_money'),
      visual: SceneVisual(_coins(coins), aspect: 2.6),
      options: [for (final v in g.numberChoices(total, min: 1, max: max + 5, spread: 3)) Opt.text('$v so‘m')],
      concept: 'money:$total',
      meta: {'coins': coins.join('+'), 'answer': total},
      hint: 'Kattasidan boshlab qo‘sh.',
      explanation: '${coins.join(' + ')} = $total so‘m',
    );
  }
}
