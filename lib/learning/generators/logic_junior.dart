import 'package:flutter/painting.dart';

import '../content/lexicon.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';
import 'math_junior.dart';
import 'puzzles.dart';

/// Muhammadjon (4 yosh) mantiqi — asosan rasmli, sudrab va bosib o'ynaladi.
class LogicJunior {
  LogicJunior._();

  static final Map<String, ExerciseGenerator> generators = {
    'same_find': sameFind,
    'odd_one': oddOne,
    'shadow': shadow,
    'pairs_match': pairsMatch,
    'sort_color': sortColor,
    'sort_shape': sortShape,
    'sort_size': sortSize,
    'missing_item': missingItem,
    'next_picture': nextPicture,
    'habitat_match': habitatMatch,
    'maze': maze,
    'analogy': analogy,
    'direction': direction,
    'shelves': shelves,
    'half_puzzle': halfPuzzle,
  };

  static const _mainCategories = [
    'fruit', 'vegetable', 'animal', 'vehicle', 'clothes', 'toy', 'food', 'nature', 'sea', 'bird',
  ];

  /// "Uzoq" kategoriyalar juftligi (kichik yosh uchun farqi yaqqol).
  static const _farPairs = [
    ['fruit', 'vehicle'], ['animal', 'clothes'], ['toy', 'fruit'], ['vehicle', 'animal'],
    ['clothes', 'food'], ['sea', 'vehicle'], ['nature', 'toy'], ['bird', 'clothes'],
  ];

  /// "Yaqin" kategoriyalar juftligi (3-daraja).
  static const _nearPairs = [
    ['fruit', 'vegetable'], ['animal', 'bird'], ['sea', 'animal'], ['toy', 'clothes'], ['food', 'fruit'],
  ];

  static List<String> _categoryPair(GenContext g) {
    final near = g.pb('near');
    final pair = List<String>.from(g.pick(near ? _nearPairs : _farPairs));
    if (g.chance(0.5)) return pair.reversed.toList();
    return pair;
  }

  // ------------------------------------------------------------ 1 Bir xilini top
  static Exercise sameFind(GenContext g) {
    final optCount = g.p('options', 3);
    final sameCat = g.pb('sameCategory');
    final cat = g.pick(_mainCategories);
    final pool = g.category(cat);
    final target = g.pick(pool);
    final others = sameCat
        ? g.sample(pool.where((e) => e.id != target.id).toList(), optCount - 1)
        : [
            for (final c in g.sample(_mainCategories.where((c) => c != cat).toList(), optCount - 1))
              g.pick(g.category(c)),
          ];
    final options = [Opt.emoji(target.emoji), for (final o in others) Opt.emoji(o.emoji)];
    // 3-daraja: chalg'ituvchi sifatida aynan shu rasmning ko'zgudagi aksi.
    if (g.pb('mirror') && options.length > 2) {
      options[options.length - 1] = Opt.emoji(target.emoji, flip: true);
    }
    return g.choice(
      say: g.say('find_same'),
      visual: SceneVisual([Layouts.emoji(target.emoji, size: 0.8)], aspect: 1.6),
      options: options,
      concept: 'same:${target.id}',
      drag: g.pb('drag'),
      meta: {'answer': target.id},
    );
  }

  // ------------------------------------------------------------ 2 Ortig'ini top
  static Exercise oddOne(GenContext g) {
    final count = g.p('items', 3);
    // Ba'zan shakllar bilan: hammasi har xil rangda, bittasining shakli boshqacha.
    if (g.chance(g.p('shapePct', 0) / 100)) {
      final pair = g.sample(const ['circle', 'square', 'triangle', 'star', 'heart'], 2);
      final colors = g.sample(
        g.lex.colors.where((c) => const {'red', 'blue', 'green', 'yellow', 'orange', 'purple'}.contains(c.id)).toList(),
        count,
      );
      return g.choice(
        say: g.say('odd_shape'),
        options: [
          Opt.shape(pair[1], colors.first.color),
          for (final c in colors.skip(1)) Opt.shape(pair[0], c.color),
        ],
        concept: 'odd_shape:${pair[1]}',
        meta: {'answer': pair[1]},
      );
    }
    final cats = _categoryPair(g);
    final main = g.sample(g.category(cats[0]), count - 1);
    final odd = g.pick(g.category(cats[1]));
    final catName = _categoryName(cats[0]);
    return g.choice(
      say: g.say('odd_one_out'),
      options: [Opt.emoji(odd.emoji), for (final m in main) Opt.emoji(m.emoji)],
      concept: 'category:${cats[0]}',
      meta: {'answer': odd.id},
      explanation: '${odd.uz} — boshqa guruhdan. Qolganlari — $catName.',
    );
  }

  static String _categoryName(String cat) => switch (cat) {
        'fruit' => 'mevalar',
        'vegetable' => 'sabzavotlar',
        'animal' => 'hayvonlar',
        'bird' => 'qushlar',
        'vehicle' => 'transport',
        'clothes' => 'kiyimlar',
        'toy' => 'o‘yinchoqlar',
        'food' => 'taomlar',
        'nature' => 'tabiat',
        'sea' => 'suv jonivorlari',
        'insect' => 'hasharotlar',
        'school' => 'maktab buyumlari',
        'home' => 'uy buyumlari',
        'body' => 'tana a’zolari',
        'family' => 'oila',
        'profession' => 'kasblar',
        _ => cat,
      };

  static String categoryName(String cat) => _categoryName(cat);

  // ------------------------------------------------------------ 3 Soyasini top
  static Exercise shadow(GenContext g) {
    final optCount = g.p('options', 3);
    final cat = g.pick(_mainCategories);
    final sameCat = g.pb('sameCategory');
    final pool = g.category(cat);
    final target = g.pick(pool);
    final others = sameCat
        ? g.sample(pool.where((e) => e.id != target.id).toList(), optCount - 1)
        : [
            for (final c in g.sample(_mainCategories.where((c) => c != cat).toList(), optCount - 1))
              g.pick(g.category(c)),
          ];
    return g.choice(
      say: g.say('find_shadow', {'item': target}),
      visual: SceneVisual([Layouts.emoji(target.emoji, size: 0.8)], aspect: 1.6),
      options: [
        Opt.emoji(target.emoji, silhouette: true),
        for (final o in others) Opt.emoji(o.emoji, silhouette: true),
      ],
      concept: 'shadow:${target.id}',
      drag: g.pb('drag'),
      meta: {'answer': target.id},
    );
  }

  // ------------------------------------------------------------ 4 Juftini top
  static Exercise pairsMatch(GenContext g) {
    final count = g.p('pairs', 2);
    final all = (g.content.logicData['pairs'] as List).map((e) => (e as List).cast<String>()).toList();
    final chosen = <List<String>>[];
    final used = <String>{};
    for (final p in all..shuffle(g.rng)) {
      if (chosen.length >= count) break;
      if (used.contains(p[0]) || used.contains(p[1])) continue;
      used
        ..add(p[0])
        ..add(p[1]);
      chosen.add(p);
    }
    return g.custom(
      say: g.say('match_pairs'),
      kind: ExerciseKind.match,
      concept: 'pairs:${chosen.map((p) => p[0]).join(",")}',
      pairs: [
        for (final p in chosen)
          MatchPair(Opt.emoji(g.lex.byId(p[0]).emoji), Opt.emoji(g.lex.byId(p[1]).emoji)),
      ],
      meta: {'pairs': chosen.map((p) => p.join('=')).join(',')},
    );
  }

  // ------------------------------------------------------------ 5 Rangiga qarab guruhla
  static Exercise sortColor(GenContext g) {
    final binsCount = g.p('bins', 2);
    final itemsCount = g.p('items', 4);
    final useObjects = g.pb('objects');
    final colorsPool = g.lex.colors.where((c) => !{'white', 'black', 'brown', 'pink'}.contains(c.id)).toList();
    final colors = g.sample(colorsPool, binsCount);
    final items = <ExerciseOption>[];
    final itemBins = <int>[];
    final shapes = ['circle', 'square', 'triangle', 'star', 'heart'];
    for (var i = 0; i < itemsCount; i++) {
      final bin = i % binsCount;
      itemBins.add(bin);
      if (useObjects) {
        final objs = g.lex.entries.where((e) => e.color == colors[bin].id && e.ageMin <= g.age).toList();
        items.add(Opt.emoji(g.pick(objs).emoji));
      } else {
        items.add(Opt.shape(g.pick(shapes), colors[bin].color));
      }
    }
    _shuffleTogether(g, items, itemBins);
    return g.custom(
      say: g.say('sort_by_color'),
      kind: ExerciseKind.sort,
      concept: 'sort:color',
      sort: SortTask(
        bins: [for (final c in colors) Opt.shape('circle', c.color, size: 0.55)],
        items: items,
        itemBins: itemBins,
      ),
    );
  }

  static bool _objectsAvailable(GenContext g, String color) =>
      g.lex.entries.any((e) => e.color == color && e.ageMin <= g.age);

  // ------------------------------------------------------------ 6 Shakliga qarab guruhla
  static Exercise sortShape(GenContext g) {
    final binsCount = g.p('bins', 2);
    final itemsCount = g.p('items', 4);
    final shapes = g.sample(['circle', 'square', 'triangle', 'star', 'heart'], binsCount);
    final colorsPool = g.lex.colors.where((c) => !{'white', 'black'}.contains(c.id)).toList();
    final items = <ExerciseOption>[];
    final itemBins = <int>[];
    for (var i = 0; i < itemsCount; i++) {
      final bin = i % binsCount;
      itemBins.add(bin);
      final size = g.pb('varySize') ? 0.45 + g.rng.nextDouble() * 0.35 : 0.7;
      items.add(Opt.shape(shapes[bin], g.pick(colorsPool).color, size: size));
    }
    _shuffleTogether(g, items, itemBins);
    return g.custom(
      say: g.say('sort_by_shape'),
      kind: ExerciseKind.sort,
      concept: 'sort:shape',
      sort: SortTask(
        bins: [for (final s in shapes) Opt.shape(s, const Color(0xFF9E9E9E), size: 0.55)],
        items: items,
        itemBins: itemBins,
      ),
    );
  }

  // ------------------------------------------------------------ 7 Katta-kichikni ajrat
  static Exercise sortSize(GenContext g) {
    final itemsCount = g.p('items', 4);
    final sameItem = g.pb('sameItem', true);
    final pool = g.countables();
    final base = g.pick(pool);
    final items = <ExerciseOption>[];
    final itemBins = <int>[];
    for (var i = 0; i < itemsCount; i++) {
      final big = i.isEven;
      itemBins.add(big ? 0 : 1);
      final e = sameItem ? base : g.pick(pool);
      items.add(Opt.emoji(e.emoji, size: big ? 0.9 : 0.42));
    }
    _shuffleTogether(g, items, itemBins);
    return g.custom(
      say: g.say('sort_by_size'),
      kind: ExerciseKind.sort,
      concept: 'sort:size',
      sort: SortTask(
        bins: [Opt.text('Katta', speech: 'katta'), Opt.text('Kichik', speech: 'kichik')],
        items: items,
        itemBins: itemBins,
      ),
    );
  }

  static void _shuffleTogether(GenContext g, List<ExerciseOption> items, List<int> bins) {
    final idx = List<int>.generate(items.length, (i) => i)..shuffle(g.rng);
    final i2 = [for (final i in idx) items[i]];
    final b2 = [for (final i in idx) bins[i]];
    items
      ..clear()
      ..addAll(i2);
    bins
      ..clear()
      ..addAll(b2);
  }

  // ------------------------------------------------------------ 8 Qaysi biri yo'qoldi?
  static Exercise missingItem(GenContext g) {
    final count = g.p('items', 3);
    final seconds = g.p('seconds', 4);
    final items = g.sample(g.countables(), count);
    final missing = g.rng.nextInt(count);
    final preview = SceneVisual(Layouts.row([for (final e in items) Layouts.emoji(e.emoji, size: 0.55)]),
        aspect: count * 0.8);
    final after = SceneVisual(
      Layouts.row([
        for (var i = 0; i < count; i++)
          i == missing ? Layouts.text('?', size: 0.5, color: const Color(0xFFFF9F43)) : Layouts.emoji(items[i].emoji, size: 0.55),
      ]),
      aspect: count * 0.8,
    );
    final extra = g.sample(g.countables().where((e) => !items.contains(e)).toList(), 2);
    return g.choice(
      say: g.say('what_missing'),
      kind: ExerciseKind.memory,
      preview: preview,
      previewSeconds: seconds,
      visual: after,
      options: [Opt.emoji(items[missing].emoji), for (final e in extra) Opt.emoji(e.emoji)],
      concept: 'memory:${items[missing].id}',
      meta: {'answer': items[missing].id},
    );
  }

  // ------------------------------------------------------------ 9 Navbatdagi rasm
  static Exercise nextPicture(GenContext g) {
    if (g.pb('growth')) {
      final seqs = (g.content.logicData['sequences'] as List).map((e) => (e as List).cast<String>()).toList();
      final seq = g.pick(seqs);
      final entries = seq.map(g.lex.byId).toList();
      final shownCount = entries.length - 1;
      final answer = entries.last;
      final distract = g.sample(
        g.countables().where((e) => !seq.contains(e.id)).toList(),
        2,
      );
      final wrongFromSeq = entries.length > 2 ? entries.first : null;
      return g.choice(
        say: g.say('what_next'),
        visual: SceneVisual(
          Layouts.row([
            for (var i = 0; i < shownCount; i++) Layouts.emoji(entries[i].emoji, size: 0.55),
            Layouts.text('?', size: 0.55, color: const Color(0xFFFF9F43)),
          ]),
          aspect: entries.length * 0.85,
        ),
        options: [
          Opt.emoji(answer.emoji),
          if (wrongFromSeq != null) Opt.emoji(wrongFromSeq.emoji) else Opt.emoji(distract[1].emoji),
          Opt.emoji(distract[0].emoji),
        ],
        concept: 'sequence:${seq.join(">")}',
        drag: g.pb('drag'),
        meta: {'answer': answer.id},
        explanation: seq.map((id) => g.lex.byId(id).uz).join(' → '),
      );
    }
    return MathJunior.pattern(g);
  }

  // ------------------------------------------------------------ 10 Hayvonni uyiga olib bor
  static Exercise habitatMatch(GenContext g) {
    final count = g.p('pairs', 2);
    final all = (g.content.logicData['habitats'] as List).map((e) => (e as List).cast<String>()).toList()
      ..shuffle(g.rng);
    final chosen = <List<String>>[];
    final usedHomes = <String>{};
    for (final p in all) {
      if (chosen.length >= count) break;
      if (usedHomes.add(p[1])) chosen.add(p);
    }
    return g.custom(
      say: g.say('animal_home'),
      kind: ExerciseKind.match,
      concept: 'habitat:${chosen.map((p) => p[0]).join(",")}',
      pairs: [
        for (final p in chosen)
          MatchPair(Opt.emoji(g.lex.byId(p[0]).emoji), Opt.emoji(g.lex.byId(p[1]).emoji)),
      ],
      meta: {'pairs': chosen.map((p) => p.join('=')).join(',')},
    );
  }

  // ------------------------------------------------------------ 11 Labirint
  static Exercise maze(GenContext g) {
    final rows = g.p('rows', 3), cols = g.p('cols', 3);
    final goals = (g.content.logicData['maze_goals'] as List).map((e) => (e as List).cast<String>()).toList();
    final goal = g.pick(goals);
    final hero = g.lex.byId(goal[0]), target = g.lex.byId(goal[1]);
    final task = PuzzleFactory.maze(
      rng: g.rng,
      rows: rows,
      cols: cols,
      hero: hero.emoji,
      target: target.emoji,
      extraOpenings: g.p('extraOpenings', 0),
    );
    return g.custom(
      say: g.say('maze_go', {'hero': hero, 'target': target}),
      kind: ExerciseKind.maze,
      concept: 'maze:${rows}x$cols',
      maze: task,
      meta: {'shortest': task.shortestPath() ?? -1},
    );
  }

  // ------------------------------------------------------------ 12 Analogiya 2×2
  static Exercise analogy(GenContext g) {
    final allowed = g.pl('relations');
    final rels = (g.content.logicData['relations'] as Map).entries
        .where((e) => allowed.isEmpty || allowed.contains(e.key))
        .toList();
    final rel = g.pick(rels);
    final pairs = ((rel.value as Map)['pairs'] as List).map((e) => (e as List).cast<String>()).toList();
    var two = g.sample(pairs, 2);
    var guard = 0;
    while (two[0][1] == two[1][1] && guard++ < 20) {
      two = g.sample(pairs, 2);
    }
    final a = g.lex.byId(two[0][0]), b = g.lex.byId(two[0][1]);
    final c = g.lex.byId(two[1][0]), d = g.lex.byId(two[1][1]);
    final used = {a.id, b.id, c.id, d.id};
    // Chalg'ituvchilar: boshqa juftlarning "B" qismi + tasodifiy narsa.
    final otherBs = pairs.map((p) => p[1]).where((id) => !used.contains(id)).toSet().toList()..shuffle(g.rng);
    final wrong = <LexiconEntry>[
      for (final id in otherBs.take(g.p('options', 3) - 2)) g.lex.byId(id),
      g.pick(g.countables().where((e) => !used.contains(e.id) && !otherBs.contains(e.id)).toList()),
    ];
    SceneItem cell(LexiconEntry e) => Layouts.emoji(e.emoji, size: 0.7);
    return g.choice(
      say: g.say('analogy'),
      visual: GridVisual(rows: 2, cols: 2, cells: [[cell(a)], [cell(b)], [cell(c)], null]),
      options: [Opt.emoji(d.emoji), for (final w in wrong) Opt.emoji(w.emoji)],
      concept: 'analogy:${rel.key}',
      drag: g.pb('drag'),
      meta: {'answer': d.id, 'relation': rel.key},
      explanation: '${a.uz} → ${b.uz}, ${c.uz} → ${d.uz}',
    );
  }

  // ------------------------------------------------------------ 13 Chap / o'ng
  static Exercise direction(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['arrows'] : g.pl('modes'));
    if (mode == 'row') {
      // "Chapdan birinchi" / "O'ngdan birinchi".
      final count = g.p('items', 3);
      final items = g.sample(g.countables(), count);
      final fromLeft = g.chance(0.5);
      final idx = fromLeft ? 0 : count - 1;
      return g.choice(
        say: g.say(fromLeft ? 'first_from_left' : 'first_from_right'),
        visual: SceneVisual(Layouts.row([for (final e in items) Layouts.emoji(e.emoji, size: 0.5)]), aspect: count * 0.9),
        options: [Opt.emoji(items[idx].emoji), for (var i = 0; i < count; i++) if (i != idx) Opt.emoji(items[i].emoji)],
        concept: 'direction:${fromLeft ? "left" : "right"}',
        meta: {'answer': items[idx].id},
      );
    }
    final dirs = mode == 'arrows4' ? ['right', 'left', 'up', 'down'] : ['right', 'left', 'up'];
    final ask = g.pick(dirs.take(2).toList());
    const arrows = {'right': '➡️', 'left': '⬅️', 'up': '⬆️', 'down': '⬇️'};
    const hands = {'right': '👉', 'left': '👈', 'up': '👆', 'down': '👇'};
    final useHands = g.pb('hands') && g.chance(0.5);
    final glyphs = useHands ? hands : arrows;
    return g.choice(
      say: g.say(ask == 'right' ? 'points_right' : 'points_left'),
      options: [Opt.emoji(glyphs[ask]!), for (final d in dirs.where((d) => d != ask)) Opt.emoji(glyphs[d]!)],
      concept: 'direction:$ask',
      meta: {'answer': ask},
    );
  }

  // ------------------------------------------------------------ 14 Yuqori / past (javonlar)
  static Exercise shelves(GenContext g) {
    final levels = g.p('shelves', 2);
    final asks = g.pl('ask').isEmpty ? ['top', 'bottom'] : g.pl('ask');
    final ask = g.pick(asks);
    final items = g.sample(g.category('toy') + g.category('fruit'), levels);
    final scene = <SceneItem>[];
    for (var i = 0; i < levels; i++) {
      final y = (i + 1) / (levels + 0.3);
      scene.add(SceneItem(kind: SceneKind.bar, value: 'shelf', color: const Color(0xFFA1887F), x: 0.5, y: y, size: 0.05, length: 0.9));
      final itemSize = 0.55 / levels + 0.05;
      scene.add(Layouts.emoji(items[i].emoji, size: itemSize, x: 0.3 + 0.4 * g.rng.nextDouble(), y: y - itemSize / 2 - 0.02));
    }
    final idx = switch (ask) { 'top' => 0, 'bottom' => levels - 1, _ => levels ~/ 2 };
    return g.choice(
      say: g.say('shelf_$ask'),
      visual: SceneVisual(scene, aspect: 1.2),
      options: [Opt.emoji(items[idx].emoji), for (var i = 0; i < levels; i++) if (i != idx) Opt.emoji(items[i].emoji)],
      concept: 'position:$ask',
      meta: {'answer': items[idx].id},
    );
  }

  // ------------------------------------------------------------ 15 Oddiy puzzle
  static Exercise halfPuzzle(GenContext g) {
    final optCount = g.p('options', 3);
    final cat = g.pick(_mainCategories);
    final pool = g.category(cat);
    final target = g.pick(pool);
    final others = g.pb('sameCategory')
        ? g.sample(pool.where((e) => e.id != target.id).toList(), optCount - 1)
        : [
            for (final c in g.sample(_mainCategories.where((c) => c != cat).toList(), optCount - 1))
              g.pick(g.category(c)),
          ];
    return g.choice(
      say: g.say('complete_picture'),
      visual: SceneVisual([
        SceneItem(kind: SceneKind.emoji, value: target.emoji, size: 0.8, x: 0.5, y: 0.5, clip: HalfClip.left),
        Layouts.text('?', size: 0.5, x: 0.72, color: const Color(0xFFFF9F43)),
      ], aspect: 1.6),
      options: [
        Opt.emoji(target.emoji, clip: HalfClip.right),
        for (final o in others) Opt.emoji(o.emoji, clip: HalfClip.right),
      ],
      concept: 'puzzle:${target.id}',
      drag: g.pb('drag'),
      meta: {'answer': target.id},
    );
  }

  /// Rang uchun obyekt yetarliligini tekshirish (test uchun).
  static bool colorHasObjects(GenContext g, String color) => _objectsAvailable(g, color);
}
