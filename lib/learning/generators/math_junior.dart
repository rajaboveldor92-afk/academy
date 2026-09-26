import 'package:flutter/painting.dart';

import '../content/lexicon.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';

/// Muhammadjon (4 yosh) matematikasi: KO'R → ESHIT → BOS → SUR → MOSLASHTIR.
/// Hamma savol rasmli, ko'rsatma ovozda aytiladi, bir ekranda bitta vazifa.
class MathJunior {
  MathJunior._();

  static final Map<String, ExerciseGenerator> generators = {
    'one_many': oneMany,
    'count_objects': countObjects,
    'number_match': numberMatch,
    'size_compare': sizeCompare,
    'more_less': moreLess,
    'long_short': longShort,
    'high_low': highLow,
    'left_right': leftRight,
    'colors': colors,
    'shapes': shapes,
    'pattern': pattern,
    'add_pictures': addPictures,
    'sub_pictures': subPictures,
  };

  static const double _groupAspect = 1.3;

  // ------------------------------------------------------------ M1 Bir va ko'p
  static Exercise oneMany(GenContext g) {
    final item = g.pick(g.countables());
    final manyMin = g.p('manyMin', 4), manyMax = g.p('manyMax', 6);
    final withEmpty = g.pb('withEmpty');
    final many = g.range(manyMin, manyMax);
    final asks = withEmpty ? ['one', 'many', 'none'] : ['one', 'many'];
    final ask = g.pick(asks);
    ExerciseOption groupOpt(int n) => n == 0
        ? Opt.scene([Layouts.shape('circle', const Color(0xFFE0E0E0), size: 0.7)])
        : Opt.group(item.emoji, n, aspect: _groupAspect);
    final counts = <String, int>{'one': 1, 'many': many, if (withEmpty) 'none': 0};
    final correct = counts[ask]!;
    final others = counts.values.where((v) => v != correct).toList();
    return g.choice(
      say: g.say('one_many_$ask', {'item': item}),
      options: [groupOpt(correct), for (final o in others) groupOpt(o)],
      concept: 'quantity:$ask',
      meta: {'answer': correct},
      hint: ask == 'many' ? 'Qaysi savatda narsalar ko‘proq?' : null,
    );
  }

  // ------------------------------------------------------------ M2–M4 Sanash
  /// Rejimlar: `count` (sanab raqamni tanlash), `group` (aytilgan songa mos
  /// guruhni tanlash), `drag` (sanab, raqamni ? ga sudrash), `numeral`
  /// (aytilgan raqamni tanish).
  static Exercise countObjects(GenContext g) {
    final min = g.p('min', 1), max = g.p('max', 3);
    final modes = g.pl('modes').isEmpty ? ['count'] : g.pl('modes');
    final mode = g.pick(modes);
    final n = g.range(min, max);
    final item = g.pick(g.countables());
    final optCount = g.p('options', 3);
    final nums = g.numberChoices(n, count: optCount, min: min == 0 ? 0 : 1, max: max < 5 ? 5 : max, spread: 2);

    switch (mode) {
      case 'group':
        return g.choice(
          say: g.say('find_group_n', {'n': n, 'item': item}),
          options: [for (final v in nums) Opt.group(item.emoji, v, aspect: _groupAspect)],
          concept: 'number:$n',
          meta: {'answer': n},
        );
      case 'numeral':
        return g.choice(
          say: g.say('find_numeral', {'n': n}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final v in nums) Opt.number(v)],
          concept: 'number:$n',
          meta: {'answer': n},
        );
      default:
        return g.choice(
          say: g.say('count_how_many', {'item': item}),
          visual: SceneVisual(Layouts.group(item.emoji, n, aspect: 2), aspect: 2),
          options: [for (final v in nums) Opt.number(v)],
          concept: 'number:$n',
          drag: mode == 'drag',
          meta: {'answer': n, 'count': n},
          hint: 'Barmog‘ing bilan bittadan sana.',
        );
    }
  }

  // ------------------------------------------------------------ M5 Son va miqdor
  static Exercise numberMatch(GenContext g) {
    final pairsCount = g.p('pairs', 2);
    final max = g.p('max', 3);
    final numbers = g.sample([for (var i = 1; i <= max; i++) i], pairsCount);
    final items = g.sample(g.countables(), pairsCount);
    return g.custom(
      say: g.say('match_number_group'),
      kind: ExerciseKind.match,
      concept: 'number_match:${numbers.join(",")}',
      pairs: [
        for (var i = 0; i < pairsCount; i++)
          MatchPair(Opt.number(numbers[i]), Opt.group(items[i].emoji, numbers[i], aspect: _groupAspect)),
      ],
      meta: {'numbers': numbers.join(',')},
    );
  }

  // ------------------------------------------------------------ M6 Katta–kichik
  static Exercise sizeCompare(GenContext g) {
    final count = g.p('items', 2);
    final asks = g.pl('ask').isEmpty ? ['big'] : g.pl('ask');
    final ask = g.pick(asks);
    final item = g.pick(g.countables());
    // O'lchamlar: farq darajaga qarab kamayadi.
    final gap = g.p('gapPct', 45) / 100;
    final sizes = <double>[0.9];
    while (sizes.length < count) {
      sizes.add(sizes.last - gap / (count - 1) * (count == 2 ? 1 : 1.1));
    }
    final correctSize = ask == 'big' ? sizes.first : sizes.last;
    final ordered = [correctSize, ...sizes.where((s) => s != correctSize)];
    return g.choice(
      say: g.say(ask == 'big' ? 'find_big' : 'find_small', {'item': item}),
      options: [for (final s in ordered) Opt.emoji(item.emoji, size: s)],
      concept: 'size:$ask',
      meta: {'answer': ask},
    );
  }

  // ------------------------------------------------------------ M7 Ko'p–kam
  static Exercise moreLess(GenContext g) {
    final maxN = g.p('max', 6);
    final minDiff = g.p('minDiff', 3);
    final ask = g.pick(g.pl('ask').isEmpty ? ['more'] : g.pl('ask'));
    final groups = g.p('groups', 2);
    final item = g.pick(g.countables());
    final values = <int>[];
    var guard = 0;
    while (values.length < groups && guard++ < 500) {
      final v = g.range(1, maxN);
      if (values.every((x) => (x - v).abs() >= minDiff)) values.add(v);
    }
    while (values.length < groups) {
      values.add(values.last + minDiff);
    }
    values.sort();
    final correct = ask == 'more' ? values.last : values.first;
    return g.choice(
      say: g.say(ask == 'more' ? 'where_more' : 'where_less', {'item': item}),
      options: [
        Opt.group(item.emoji, correct, aspect: _groupAspect),
        for (final v in values.where((v) => v != correct)) Opt.group(item.emoji, v, aspect: _groupAspect),
      ],
      concept: 'compare_quantity:$ask',
      meta: {'answer': correct, 'values': values.join(',')},
    );
  }

  // ------------------------------------------------------------ M8 Uzun–qisqa
  static Exercise longShort(GenContext g) {
    final count = g.p('items', 2);
    final ask = g.pick(g.pl('ask').isEmpty ? ['long'] : g.pl('ask'));
    final palette = g.sample(g.lex.colors.where((c) => !{'white', 'black', 'brown'}.contains(c.id)).toList(), count);
    final gap = g.p('gapPct', 40) / 100;
    final longest = 0.82 + g.rng.nextDouble() * 0.12;
    final lengths = <double>[longest];
    while (lengths.length < count) {
      lengths.add(lengths.last - gap / (count == 2 ? 1 : 1.6));
    }
    final correctIdx = ask == 'long' ? 0 : count - 1;
    ExerciseOption bar(int i) => ExerciseOption(
          visual: SceneVisual([
            SceneItem(
              kind: SceneKind.bar,
              value: 'bar',
              color: palette[i].color,
              x: 0.04 + lengths[i] / 2,
              y: 0.5,
              size: 0.4,
              length: lengths[i],
            ),
          ], aspect: 3.5),
        );
    return g.choice(
      say: g.say(ask == 'long' ? 'find_long' : 'find_short'),
      options: [bar(correctIdx), for (var i = 0; i < count; i++) if (i != correctIdx) bar(i)],
      concept: 'length:$ask',
      meta: {'answer': ask},
    );
  }

  // ------------------------------------------------------------ M9 Yuqori–past
  static Exercise highLow(GenContext g) {
    final count = g.p('items', 2);
    final ask = g.pick(g.pl('ask').isEmpty ? ['high'] : g.pl('ask'));
    final items = g.sample(g.countables(), count);
    // Narvon: har bir narsa boshqa balandlikda, ustunlar bo'yicha.
    final ys = count == 2 ? [0.18, 0.82] : [0.15, 0.5, 0.85];
    final order = List<int>.generate(count, (i) => i)..shuffle(g.rng);
    final scene = <SceneItem>[
      const SceneItem(kind: SceneKind.bar, value: 'ground', color: Color(0xFF8D6E63), x: 0.5, y: 0.97, size: 0.05, length: 0.96),
      for (var i = 0; i < count; i++)
        Layouts.emoji(items[i].emoji, size: 0.26, x: (i + 0.5) / count, y: ys[order[i]]),
    ];
    final highestIdx = order.indexOf(0);
    final lowestIdx = order.indexOf(count - 1);
    final correct = ask == 'high' ? highestIdx : lowestIdx;
    return g.choice(
      say: g.say(ask == 'high' ? 'which_high' : 'which_low'),
      visual: SceneVisual(scene, aspect: 1.6),
      options: [
        Opt.emoji(items[correct].emoji),
        for (var i = 0; i < count; i++)
          if (i != correct) Opt.emoji(items[i].emoji),
      ],
      concept: 'position:$ask',
      meta: {'answer': items[correct].id},
    );
  }

  // ------------------------------------------------------------ M10 Chap–o'ng
  static Exercise leftRight(GenContext g) {
    final count = g.p('items', 2);
    final ask = g.pick(g.pl('ask').isEmpty ? ['left'] : g.pl('ask'));
    final items = g.sample(g.countables(), count);
    final scene = Layouts.row([for (final e in items) Layouts.emoji(e.emoji, size: 0.5)]);
    final idx = switch (ask) { 'left' => 0, 'right' => count - 1, _ => count ~/ 2 };
    return g.choice(
      say: g.say('which_$ask'),
      visual: SceneVisual(scene, aspect: count * 0.9),
      options: [
        Opt.emoji(items[idx].emoji),
        for (var i = 0; i < count; i++)
          if (i != idx) Opt.emoji(items[i].emoji),
      ],
      concept: 'position:$ask',
      meta: {'answer': items[idx].id},
      hint: ask == 'left' ? 'Chap qo‘lingni ko‘tar — o‘sha tomon chap.' : null,
    );
  }

  // ------------------------------------------------------------ M11 Ranglar
  static Exercise colors(GenContext g) {
    final pool = g.pl('colors').map(g.lex.color).toList();
    final optCount = g.p('options', 3);
    if (g.pb('objects')) {
      // "Qizil narsani top" — rangli narsalar orasidan.
      final withColor = g.lex.entries
          .where((e) => e.ageMin <= g.age && e.color != null && pool.any((c) => c.id == e.color))
          .toList();
      final target = g.pick(pool.where((c) => withColor.any((e) => e.color == c.id)).toList());
      final correct = g.pick(withColor.where((e) => e.color == target.id).toList());
      final wrong = g.sample(withColor.where((e) => e.color != target.id).toList(), optCount - 1);
      final usedColors = <String>{target.id};
      final distinctWrong = <LexiconEntry>[];
      for (final w in wrong) {
        if (usedColors.add(w.color!)) distinctWrong.add(w);
      }
      for (final w in withColor..shuffle(g.rng)) {
        if (distinctWrong.length >= optCount - 1) break;
        if (usedColors.add(w.color!)) distinctWrong.add(w);
      }
      return g.choice(
        say: g.say('find_color_object', {'color': target}),
        options: [Opt.emoji(correct.emoji), for (final w in distinctWrong) Opt.emoji(w.emoji)],
        concept: 'color:${target.id}',
        meta: {'answer': target.id},
      );
    }
    final chosen = g.sample(pool, optCount);
    final target = chosen.first;
    const shapes = ['circle', 'square', 'heart', 'star', 'triangle'];
    // Bir xil shakl (1-daraja soddaroq) yoki har xil shakllar — ikkalasida ham faqat rang muhim.
    final same = g.chance(0.5) ? g.pick(shapes) : null;
    return g.choice(
      say: g.say('find_color', {'color': target}),
      options: [for (final c in chosen) Opt.shape(same ?? g.pick(shapes), c.color)],
      concept: 'color:${target.id}',
      meta: {'answer': target.id},
    );
  }

  // ------------------------------------------------------------ M12 Shakllar
  static Exercise shapes(GenContext g) {
    final pool = g.pl('shapes').map(g.lex.shape).toList();
    final optCount = g.p('options', 3);
    final colorsPool = g.lex.colors.where((c) => !{'white', 'black', 'brown'}.contains(c.id)).toList();
    if (g.pb('withColor')) {
      // "Qizil uchburchakni top": chalg'ituvchilar rangi yoki shakli bir xil.
      final shape = g.pick(pool);
      final color = g.pick(colorsPool);
      final otherShape = g.pick(pool.where((s) => s.id != shape.id).toList());
      final otherColor = g.pick(colorsPool.where((c) => c.id != color.id).toList());
      final options = <ExerciseOption>[
        Opt.shape(shape.id, color.color),
        Opt.shape(otherShape.id, color.color),
        Opt.shape(shape.id, otherColor.color),
      ];
      if (optCount > 3) options.add(Opt.shape(otherShape.id, otherColor.color));
      return g.choice(
        say: g.say('find_color_shape', {'color': color, 'shape': shape}),
        options: options,
        concept: 'shape:${shape.id}',
        meta: {'answer': '${color.id}_${shape.id}'},
      );
    }
    final chosen = g.sample(pool, optCount);
    final sameColor = g.pb('sameColor', true);
    final base = g.pick(colorsPool);
    return g.choice(
      say: g.say('find_shape', {'shape': chosen.first}),
      options: [
        for (final s in chosen) Opt.shape(s.id, sameColor ? base.color : g.pick(colorsPool).color),
      ],
      concept: 'shape:${chosen.first.id}',
      meta: {'answer': chosen.first.id},
    );
  }

  // ------------------------------------------------------------ M13 Ketma-ketlik
  /// `pattern`: "AB", "AAB", "ABC", "ABB", "AABB". Elementlar: emoji,
  /// rangli shakl yoki rang.
  static Exercise pattern(GenContext g) {
    final patterns = g.pl('patterns').isEmpty ? ['AB'] : g.pl('patterns');
    final pat = g.pick(patterns);
    final kinds = g.pl('kinds').isEmpty ? ['emoji'] : g.pl('kinds');
    final kind = g.pick(kinds);
    final symbols = pat.split('').toSet().toList()..sort();
    final shown = g.p('shown', 5);

    List<SceneItem> tokens;
    List<ExerciseOption> Function(SceneItem correct, List<SceneItem> others) optionsOf;
    final colorsPool = g.lex.colors.where((c) => !{'white', 'brown', 'black'}.contains(c.id)).toList();
    switch (kind) {
      case 'shape':
        final shapesPool = g.sample(g.lex.shapes.where((s) => s.id != 'oval').toList(), symbols.length + 1);
        final color = g.pick(colorsPool);
        tokens = [for (final s in shapesPool) Layouts.shape(s.id, color.color)];
      case 'color':
        final cs = g.sample(colorsPool, symbols.length + 1);
        final shape = g.pick(['circle', 'square', 'star', 'heart']);
        tokens = [for (final c in cs) Layouts.shape(shape, c.color)];
      default:
        final es = g.sample(g.countables(), symbols.length + 1);
        tokens = [for (final e in es) Layouts.emoji(e.emoji)];
    }
    optionsOf = (correct, others) => [
          Opt.scene([correct.copyWith(x: 0.5, y: 0.5, size: 0.75)]),
          for (final o in others) Opt.scene([o.copyWith(x: 0.5, y: 0.5, size: 0.75)]),
        ];
    final map = {for (var i = 0; i < symbols.length; i++) symbols[i]: tokens[i]};
    final extra = tokens.last; // chalg'ituvchi (naqshda yo'q)
    final seq = [for (var i = 0; i <= shown; i++) pat[i % pat.length]];
    final answerSymbol = seq.last;
    final visibleItems = [
      for (var i = 0; i < shown; i++) map[seq[i]]!.copyWith(size: 0.55),
      Layouts.text('?', size: 0.55, color: const Color(0xFFFF9F43)),
    ];
    final correctToken = map[answerSymbol]!;
    final wrong = <SceneItem>[
      for (final s in symbols)
        if (s != answerSymbol) map[s]!,
      extra,
    ].take(2).toList();
    return g.choice(
      say: g.say('what_next'),
      visual: SceneVisual(Layouts.row(visibleItems), aspect: (shown + 1) * 0.75),
      options: optionsOf(correctToken, wrong),
      concept: 'pattern:$pat',
      meta: {'pattern': pat, 'answer': answerSymbol},
      drag: g.pb('drag'),
      hint: 'Boshidan takrorlab ayt: ${seq.take(pat.length).join("-")}...',
    );
  }

  // ------------------------------------------------------------ M14 Rasmli qo'shish
  static Exercise addPictures(GenContext g) {
    final max = g.p('max', 3);
    final a = g.range(1, max - 1);
    final b = g.range(1, max - a);
    final item = g.pick(g.countables());
    final sum = a + b;
    final scene = <SceneItem>[
      ...Layouts.group(item.emoji, a, left: 0.02, right: 0.42, aspect: 2.4),
      Layouts.text('+', x: 0.5, size: 0.4, color: const Color(0xFF4F7CF7)),
      ...Layouts.group(item.emoji, b, left: 0.58, right: 0.98, aspect: 2.4),
    ];
    return g.choice(
      say: g.say('add_pictures', {'item': item}),
      visual: SceneVisual(scene, aspect: 2.4),
      options: [for (final v in g.numberChoices(sum, min: 1, max: max + 1, spread: 2)) Opt.number(v)],
      concept: 'add:$a+$b',
      meta: {'a': a, 'b': b, 'op': '+', 'answer': sum},
      drag: g.pb('drag'),
      hint: 'Hammasini birga sana.',
      explanation: '$a + $b = $sum',
    );
  }

  // ------------------------------------------------------------ M15 Rasmli ayirish
  static Exercise subPictures(GenContext g) {
    final max = g.p('max', 3);
    final a = g.range(2, max);
    final b = g.range(1, a - 1);
    final item = g.pick(g.countables());
    final rest = a - b;
    return g.choice(
      say: g.say('sub_pictures', {'n': b, 'item': item}),
      visual: SceneVisual(Layouts.group(item.emoji, a, aspect: 2, crossedFromEnd: true, crossed: b), aspect: 2),
      options: [for (final v in g.numberChoices(rest, min: 0, max: max, spread: 2)) Opt.number(v)],
      concept: 'sub:$a-$b',
      meta: {'a': a, 'b': b, 'op': '-', 'answer': rest},
      drag: g.pb('drag'),
      hint: 'Chizilganlarini sanama — qolganlarini sana.',
      explanation: '$a − $b = $rest',
    );
  }
}
