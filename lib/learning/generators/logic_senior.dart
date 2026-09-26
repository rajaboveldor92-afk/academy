import 'package:flutter/painting.dart';

import '../content/lexicon.dart';
import '../content/uz_numbers.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';
import 'logic_junior.dart';
import 'math_junior.dart';
import 'math_senior.dart';
import 'puzzles.dart';

/// Azamjon (6 yosh) mantiqi: ketma-ketlik, tasniflash, analogiya, matritsa,
/// labirint, aylantirish, kodlash, tangram, sudoku, mantiqiy masalalar.
class LogicSenior {
  LogicSenior._();

  static final Map<String, ExerciseGenerator> generators = {
    'picture_sequence': pictureSequence,
    'number_sequence': MathSenior.sequence,
    'classify': classify,
    'odd_attribute': oddAttribute,
    'analogy6': LogicJunior.analogy,
    'pattern6': pattern6,
    'matrix': matrix,
    'maze6': LogicJunior.maze,
    'rotation': rotation,
    'grid_position': MathSenior.spatial,
    'coding': coding,
    'tangram': tangram,
    'sudoku': sudoku,
    'logic_problem': logicProblem,
  };

  static List<ColorEntry> _colors(GenContext g) =>
      g.lex.colors.where((c) => !{'white', 'black', 'brown', 'pink'}.contains(c.id)).toList();

  static const _shapeIds = ['circle', 'square', 'triangle', 'star', 'heart', 'rhombus'];

  // ------------------------------------------------------------ 1 Rasmli ketma-ketlik
  static Exercise pictureSequence(GenContext g) {
    if (g.pb('growth') && g.chance(0.5)) return LogicJunior.nextPicture(g);
    return MathJunior.pattern(g);
  }

  // ------------------------------------------------------------ 3 Tasniflash
  static const _classGroups = [
    ['fruit', 'vegetable'],
    ['animal', 'bird'],
    ['vehicle', 'toy'],
    ['clothes', 'food'],
    ['sea', 'insect'],
    ['school', 'home'],
    ['fruit', 'vegetable', 'food'],
    ['animal', 'bird', 'sea'],
    ['vehicle', 'clothes', 'toy'],
  ];

  static const _binIcons = {
    'fruit': '🍎', 'vegetable': '🥕', 'animal': '🐾', 'bird': '🐦', 'vehicle': '🚦', 'toy': '🧸',
    'clothes': '👕', 'food': '🍽️', 'sea': '🌊', 'insect': '🐞', 'school': '🏫', 'home': '🏠',
  };

  static Exercise classify(GenContext g) {
    final binsCount = g.p('bins', 2);
    final itemsCount = g.p('items', 6);
    final groups = _classGroups.where((gr) => gr.length == binsCount).toList();
    final cats = g.pick(groups);
    final items = <ExerciseOption>[];
    final bins = <int>[];
    final perCat = <int, List<LexiconEntry>>{
      for (var i = 0; i < cats.length; i++) i: g.sample(g.category(cats[i]), itemsCount),
    };
    for (var i = 0; i < itemsCount; i++) {
      final b = i % cats.length;
      bins.add(b);
      items.add(Opt.emoji(perCat[b]![i ~/ cats.length].emoji));
    }
    final idx = List<int>.generate(items.length, (i) => i)..shuffle(g.rng);
    return g.custom(
      say: g.say('classify'),
      kind: ExerciseKind.sort,
      concept: 'classify:${cats.join("+")}',
      sort: SortTask(
        bins: [
          for (final c in cats)
            ExerciseOption(
              text: LogicJunior.categoryName(c),
              speech: LogicJunior.categoryName(c),
              visual: SceneVisual([Layouts.emoji(_binIcons[c] ?? '📦', size: 0.7)], aspect: 1),
            ),
        ],
        items: [for (final i in idx) items[i]],
        itemBins: [for (final i in idx) bins[i]],
      ),
    );
  }

  // ------------------------------------------------------------ 4 Odd one out (xususiyat)
  static Exercise oddAttribute(GenContext g) {
    final attrs = (g.content.logicData['attributes'] as Map).entries.toList();
    final attr = g.pick(attrs);
    final data = attr.value as Map;
    final pool = (data['pool'] as List).cast<String>();
    final oddPool = (data['odd'] as List).cast<String>();
    final count = g.p('items', 4);
    final main = g.sample(pool, count - 1).map(g.lex.byId).toList();
    final odd = g.lex.byId(g.pick(oddPool));
    final quality = Localized.fromJson(data);
    return g.choice(
      say: g.say('odd_one_out'),
      options: [Opt.emoji(odd.emoji), for (final m in main) Opt.emoji(m.emoji)],
      concept: 'attribute:${attr.key}',
      meta: {'answer': odd.id, 'attribute': attr.key},
      hint: 'Uchtasida bor, bittasida yo‘q narsa nima?',
      explanation: 'Qolganlari ${quality.uz}, ${odd.uz} esa yo‘q.',
    );
  }

  // ------------------------------------------------------------ 6 Pattern (ikki belgili)
  static Exercise pattern6(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['rotate'] : g.pl('modes'));
    if (mode == 'rotate') {
      // Strelka har qadamda 90° buriladi.
      final stepTurn = g.pick([0.25, -0.25, 0.5]);
      final start = g.pick([0.0, 0.25, 0.5, 0.75]);
      const shown = 4;
      final emoji = g.pick(['➡️', '🐟', '🚗', '👉']);
      final seq = [for (var i = 0; i <= shown; i++) (start + stepTurn * i) % 1.0];
      final answer = seq.last;
      final wrong = {(answer + 0.25) % 1.0, (answer + 0.5) % 1.0, (answer + 0.75) % 1.0}.toList()..shuffle(g.rng);
      SceneItem arrow(double r, {double size = 0.55}) =>
          SceneItem(kind: SceneKind.emoji, value: emoji, rotation: r, size: size);
      return g.choice(
        say: g.say('what_next'),
        visual: SceneVisual(
          Layouts.row([
            for (var i = 0; i < shown; i++) arrow(seq[i]),
            Layouts.text('?', size: 0.55, color: const Color(0xFFFF9F43)),
          ]),
          aspect: (shown + 1) * 0.8,
        ),
        options: [
          Opt.scene([arrow(answer, size: 0.75)]),
          for (final w in wrong.take(2)) Opt.scene([arrow(w, size: 0.75)]),
        ],
        concept: 'pattern:rotate',
        meta: {'answer': answer},
        explanation: 'Har safar ${stepTurn.abs() == 0.5 ? "yarim" : "chorak"} marta buriladi.',
      );
    }
    // Rang va shakl birga almashadi: (qizil doira, ko'k uchburchak, ...)
    final colors = g.sample(_colors(g), 2);
    final shapes = g.sample(_shapeIds, 3);
    final pat = g.pick(['AB', 'ABC', 'AABB']);
    final symbols = pat.split('').toSet().toList()..sort();
    final tokens = <String, SceneItem>{
      for (var i = 0; i < symbols.length; i++)
        symbols[i]: Layouts.shape(shapes[i % shapes.length], colors[i % 2].color),
    };
    const shown = 6;
    final seq = [for (var i = 0; i <= shown; i++) pat[i % pat.length]];
    final answer = tokens[seq.last]!;
    // Chalg'ituvchilar: to'g'ri shakl + noto'g'ri rang, noto'g'ri shakl + to'g'ri rang.
    final otherColor = colors.firstWhere((c) => c.color != answer.color);
    final otherShape = shapes.firstWhere((s) => s != answer.value);
    return g.choice(
      say: g.say('what_next'),
      visual: SceneVisual(
        Layouts.row([
          for (var i = 0; i < shown; i++) tokens[seq[i]]!.copyWith(size: 0.5),
          Layouts.text('?', size: 0.5, color: const Color(0xFFFF9F43)),
        ]),
        aspect: (shown + 1) * 0.7,
      ),
      options: [
        Opt.shape(answer.value, answer.color!),
        Opt.shape(answer.value, otherColor.color),
        Opt.shape(otherShape, answer.color!),
      ],
      concept: 'pattern:$pat',
      meta: {'pattern': pat, 'answer': seq.last},
      hint: 'Ham shakliga, ham rangiga qara.',
    );
  }

  // ------------------------------------------------------------ 7–8 Matritsa (2×2, 3×3)
  /// Qatorlar bir xil shakl, ustunlar bir xil rang (yoki son) — yetishmayotganini top.
  static Exercise matrix(GenContext g) {
    final size = g.p('size', 2);
    final rule = g.pick(g.pl('rules').isEmpty ? ['shape_color'] : g.pl('rules'));
    final shapes = g.sample(_shapeIds, size);
    final colors = g.sample(_colors(g), size);
    final missing = g.chance(0.6) ? size * size - 1 : g.rng.nextInt(size * size);

    /// Qoidalar: `shape_color` — qatorda shakl, ustunda rang bir xil;
    /// `count` — qatorda shakl (va rang), ustunda soni bir xil (1..size).
    List<SceneItem> cellItems(int r, int c) {
      if (rule == 'count') {
        final k = c + 1;
        return [
          for (var i = 0; i < k; i++)
            Layouts.shape(shapes[r], colors[r].color, size: k == 1 ? 0.5 : 0.32, x: (i + 0.5) / k, y: 0.5),
        ];
      }
      return [Layouts.shape(shapes[r], colors[c].color, size: 0.62)];
    }

    final cells = <List<SceneItem>?>[
      for (var r = 0; r < size; r++)
        for (var c = 0; c < size; c++) (r * size + c == missing) ? null : cellItems(r, c),
    ];
    final mr = missing ~/ size, mc = missing % size;
    ExerciseOption optFor(int r, int c) => Opt.scene(cellItems(r, c), aspect: 1);

    // Chalg'ituvchilar: qatori yoki ustuni to'g'ri, lekin ikkinchisi xato.
    final wrongRC = <(int, int)>{};
    for (final rc in [((mr + 1) % size, mc), (mr, (mc + 1) % size), ((mr + 1) % size, (mc + 1) % size)]) {
      if (rc != (mr, mc)) wrongRC.add(rc);
    }
    final options = [optFor(mr, mc), for (final rc in wrongRC.take(size == 2 ? 2 : 3)) optFor(rc.$1, rc.$2)];
    return g.choice(
      say: g.say('matrix_missing'),
      visual: GridVisual(rows: size, cols: size, cells: cells),
      options: options,
      concept: 'matrix:$size:$rule',
      drag: g.pb('drag'),
      meta: {'row': mr, 'col': mc, 'rule': rule},
      hint: 'Har bir qatorga qara: nima bir xil? Har bir ustunga qara: nima bir xil?',
    );
  }

  // ------------------------------------------------------------ 10 Fazoviy aylantirish
  static Exercise rotation(GenContext g) {
    // Assimetrik emoji'lar — ko'zgudagi aksini burilgandan ajratish mumkin.
    const asym = ['🦒', '🐿️', '👢', '🦘', '🐌', '🛴', '🐊', '🦜', '🚚', '🐓', '🦕', '🐘'];
    final emoji = g.pick(asym);
    final optCount = g.p('options', 3);
    final turn = g.pick([0.25, 0.5, 0.75]);
    final mirrors = <ExerciseOption>[
      Opt.emoji(emoji, flip: true, rotation: turn),
      Opt.emoji(emoji, flip: true, rotation: (turn + 0.5) % 1.0),
      Opt.emoji(emoji, flip: true, rotation: (turn + 0.25) % 1.0),
    ]..shuffle(g.rng);
    return g.choice(
      say: g.say('same_rotated'),
      visual: SceneVisual([Layouts.emoji(emoji, size: 0.75)], aspect: 1.6),
      options: [
        Opt.emoji(emoji, rotation: turn),
        ...mirrors.take(optCount - 1),
      ],
      concept: 'rotation',
      meta: {'turn': turn},
      hint: 'Rasmni xayolan bur. Ko‘zgudagi aksi bo‘lsa — to‘g‘ri kelmaydi.',
    );
  }

  // ------------------------------------------------------------ 12 Kodlash
  static const _arrow = {'U': '⬆️', 'D': '⬇️', 'L': '⬅️', 'R': '➡️'};

  static String programText(List<String> p) => p.map((s) => _arrow[s]).join(' ');

  static Exercise coding(GenContext g) {
    final rows = g.p('rows', 3), cols = g.p('cols', 3);
    final build = g.pb('build');
    final generated = PuzzleFactory.coding(
      rng: g.rng,
      rows: rows,
      cols: cols,
      obstacles: g.p('obstacles', 0),
      hero: '🤖',
      target: g.pick(['⭐', '🔋', '🍎', '🎁']),
      minSteps: g.p('minSteps', 2),
      maxSteps: g.p('maxSteps', 4),
    );
    final task = generated.task;
    final solution = generated.solution;
    if (build) {
      return g.custom(
        say: g.say('code_build'),
        kind: ExerciseKind.coding,
        concept: 'coding:${solution.length}',
        coding: task,
        meta: {'solutionLength': solution.length},
        hint: 'Birinchi qadam: ${_arrow[solution.first]}',
      );
    }
    // Tanlash: to'g'ri dastur + 2 ta noto'g'ri (bitta qadami o'zgargan).
    final wrong = <String>{};
    var guard = 0;
    while (wrong.length < 2 && guard++ < 100) {
      final p = List<String>.from(solution);
      final i = g.rng.nextInt(p.length);
      p[i] = g.pick(['U', 'D', 'L', 'R'].where((d) => d != p[i]).toList());
      if (g.chance(0.3) && p.length > 1) p.removeLast();
      if (!task.run(p)) wrong.add(p.join());
    }
    final cells = <List<SceneItem>?>[
      for (var i = 0; i < rows * cols; i++)
        i == task.start
            ? [Layouts.emoji(task.hero, size: 0.7)]
            : i == task.goal
                ? [Layouts.emoji(task.target, size: 0.7)]
                : task.blocked.contains(i)
                    ? [Layouts.emoji('🧱', size: 0.7)]
                    : <SceneItem>[],
    ];
    return g.choice(
      say: g.say('code_choose'),
      visual: GridVisual(rows: rows, cols: cols, cells: cells, showQuestionMark: false),
      options: [
        Opt.text(programText(solution)),
        for (final w in wrong) Opt.text(programText(w.split(''))),
      ],
      concept: 'coding:${solution.length}',
      meta: {'program': solution.join()},
      hint: 'Robot turgan joydan barmog‘ing bilan yur.',
    );
  }

  // ------------------------------------------------------------ 13 Tangram
  static List<SceneItem> figureItems(GenContext g, Map fig, {int? skip}) {
    final parts = (fig['parts'] as List).cast<Map>();
    return [
      for (var i = 0; i < parts.length; i++)
        if (i != skip)
          SceneItem(
            kind: SceneKind.shape,
            value: parts[i]['s'].toString(),
            color: g.lex.color(parts[i]['c'].toString()).color,
            x: (parts[i]['x'] as num).toDouble(),
            y: (parts[i]['y'] as num).toDouble(),
            size: (parts[i]['size'] as num).toDouble(),
            rotation: ((parts[i]['r'] ?? 0) as num).toDouble(),
          ),
    ];
  }

  static Exercise tangram(GenContext g) {
    final figures = (g.content.logicData['figures'] as List).cast<Map>();
    final fig = g.pick(figures);
    final parts = (fig['parts'] as List).cast<Map>();
    final mode = g.pick(g.pl('modes').isEmpty ? ['parts'] : g.pl('modes'));
    final name = fig['uz'].toString();
    final partShapes = parts.map((p) => p['s'].toString()).toSet();

    if (mode == 'count') {
      final shapeId = g.pick(partShapes.toList());
      final count = parts.where((p) => p['s'] == shapeId).length;
      final shape = g.lex.shape(shapeId);
      return g.choice(
        say: g.say('count_shapes_in_figure', {'shape': shape}),
        visual: SceneVisual(figureItems(g, fig), aspect: 1.2),
        options: [for (final v in {count, count + 1, count == 1 ? 2 + 1 : count - 1}) Opt.number(v)],
        concept: 'tangram:count',
        meta: {'answer': count, 'figure': fig['id'].toString()},
        explanation: '$name: $count ta ${shape.name.uz}',
      );
    }
    if (mode == 'missing') {
      final skip = g.rng.nextInt(parts.length);
      final missingPart = parts[skip];
      final correct = Opt.shape(missingPart['s'].toString(), g.lex.color(missingPart['c'].toString()).color,
          rotation: ((missingPart['r'] ?? 0) as num).toDouble());
      final wrongShapes = g.sample(_shapeIds.where((s) => s != missingPart['s']).toList(), 2);
      return g.choice(
        say: g.say('tangram_missing', {'name': name}),
        visual: SceneVisual(figureItems(g, fig, skip: skip), aspect: 1.2),
        options: [
          correct,
          for (final w in wrongShapes) Opt.shape(w, g.lex.color(missingPart['c'].toString()).color),
        ],
        concept: 'tangram:missing',
        meta: {'answer': missingPart['s'].toString(), 'figure': fig['id'].toString()},
      );
    }
    // Qaysi shakllardan tuzilgan?
    final correctSet = partShapes.toList()..sort();
    ExerciseOption setOption(List<String> ids) => Opt.scene([
          for (var i = 0; i < ids.length; i++)
            Layouts.shape(ids[i], const Color(0xFF4F7CF7), size: 0.5, x: (i + 0.5) / ids.length, y: 0.5),
        ], aspect: 0.9 * ids.length);
    final wrongSets = <String>{};
    final wrongOptions = <ExerciseOption>[];
    var guard = 0;
    while (wrongOptions.length < 2 && guard++ < 50) {
      final alt = List<String>.from(correctSet);
      alt[g.rng.nextInt(alt.length)] = g.pick(_shapeIds.where((s) => !correctSet.contains(s)).toList());
      alt.sort();
      if (alt.toSet().length == alt.length && wrongSets.add(alt.join())) wrongOptions.add(setOption(alt));
    }
    return g.choice(
      say: g.say('tangram_parts', {'name': name}),
      visual: SceneVisual(figureItems(g, fig), aspect: 1.2),
      options: [setOption(correctSet), ...wrongOptions],
      concept: 'tangram:parts',
      meta: {'answer': correctSet.join(','), 'figure': fig['id'].toString()},
    );
  }

  // ------------------------------------------------------------ 14 Mini-sudoku
  static Exercise sudoku(GenContext g) {
    final size = g.p('size', 4);
    final blanks = g.range(g.p('minBlanks', 3), g.p('maxBlanks', 5));
    final symbolsKind = g.pick(g.pl('symbols').isEmpty ? ['emoji'] : g.pl('symbols'));
    final symbols = switch (symbolsKind) {
      'numbers' => ['1', '2', '3', '4'],
      'colors' => [for (final c in g.sample(_colors(g), size)) 'color:${c.id}'],
      _ => [for (final e in g.sample(g.category('fruit'), size)) e.emoji],
    };
    final task = PuzzleFactory.sudoku(rng: g.rng, size: size, blanks: blanks, symbols: symbols);
    return g.custom(
      say: g.say('sudoku'),
      kind: ExerciseKind.sudoku,
      concept: 'sudoku:$size',
      sudoku: task,
      meta: {'blanks': blanks},
      hint: 'Har qatorda va har ustunda har bir belgi bir martadan.',
      rewardStars: blanks >= 6 ? 3 : 2,
    );
  }

  // ------------------------------------------------------------ 15 Sodda mantiqiy masala
  static const _people = ['Ali', 'Nodira', 'Sardor', 'Malika', 'Bobur', 'Zarina'];

  static Exercise logicProblem(GenContext g) {
    final type = g.pick(g.pl('types').isEmpty ? ['taller'] : g.pl('types'));
    if (type == 'where') {
      // "Mushuk qutining ustida emas, ostida ham emas" -> yonida.
      final animal = g.pick(g.category('animal'));
      const places = {
        'on': Localized(uz: 'ustida', en: 'on', ru: 'на ней'),
        'under': Localized(uz: 'ostida', en: 'under', ru: 'под ней'),
        'next': Localized(uz: 'yonida', en: 'next to', ru: 'рядом с ней'),
      };
      final answer = g.pick(places.keys.toList());
      final nots = places.keys.where((k) => k != answer).toList();
      final say = g.say('where_riddle', {'item': animal, 'p1': places[nots[0]]!, 'p2': places[nots[1]]!});
      return g.choice(
        say: say,
        visual: SceneVisual([Layouts.emoji(animal.emoji, x: 0.3, size: 0.5), Layouts.emoji('📦', x: 0.7, size: 0.5)], aspect: 2),
        options: [
          Opt.text('Qutining ${places[answer]!.uz}'),
          for (final n in nots) Opt.text('Qutining ${places[n]!.uz}'),
        ],
        concept: 'riddle:where',
        meta: {'answer': answer},
        explanation: '${places[nots[0]]!.uz} ham emas, ${places[nots[1]]!.uz} ham emas — demak, ${places[answer]!.uz}.',
      );
    }
    if (type == 'order') {
      // Poyga: "Ali Nodiradan oldinda, Nodira Sardordan oldinda. Kim birinchi?"
      final names = g.sample(_people, 3);
      final askFirst = g.chance(0.5);
      return g.choice(
        say: g.say(askFirst ? 'race_first' : 'race_last', {'a': names[0], 'b': names[1], 'c': names[2]}),
        visual: SceneVisual([Layouts.emoji('🏃', x: 0.3, size: 0.5), Layouts.emoji('🏁', x: 0.75, size: 0.5)], aspect: 2),
        options: [Opt.text(askFirst ? names[0] : names[2]), Opt.text(names[1]), Opt.text(askFirst ? names[2] : names[0])],
        concept: 'riddle:order',
        meta: {'order': names.join('>'), 'answer': askFirst ? names[0] : names[2]},
        explanation: '${names[0]} → ${names[1]} → ${names[2]}',
      );
    }
    if (type == 'syllogism') {
      const facts = <(Localized, Localized, Localized, bool)>[
        (
          Localized(uz: 'Hamma qushlarning qanoti bor.', en: 'All birds have wings.', ru: 'У всех птиц есть крылья.'),
          Localized(uz: 'Tovuq — qush.', en: 'A hen is a bird.', ru: 'Курица — птица.'),
          Localized(uz: 'Tovuqning qanoti bormi?', en: 'Does a hen have wings?', ru: 'Есть ли у курицы крылья?'),
          true,
        ),
        (
          Localized(uz: 'Hamma mashinalarning g‘ildiragi bor.', en: 'All cars have wheels.', ru: 'У всех машин есть колёса.'),
          Localized(uz: 'Taksi — mashina.', en: 'A taxi is a car.', ru: 'Такси — машина.'),
          Localized(uz: 'Taksining g‘ildiragi bormi?', en: 'Does a taxi have wheels?', ru: 'Есть ли у такси колёса?'),
          true,
        ),
        (
          Localized(uz: 'Baliqlar suvda yashaydi.', en: 'Fish live in water.', ru: 'Рыбы живут в воде.'),
          Localized(uz: 'Mushuk — baliq emas.', en: 'A cat is not a fish.', ru: 'Кошка — не рыба.'),
          Localized(uz: 'Mushuk suvda yashaydimi?', en: 'Does a cat live in water?', ru: 'Живёт ли кошка в воде?'),
          false,
        ),
        (
          Localized(uz: 'Qishda qor yog‘adi.', en: 'It snows in winter.', ru: 'Зимой идёт снег.'),
          Localized(uz: 'Hozir yoz.', en: 'Now it is summer.', ru: 'Сейчас лето.'),
          Localized(uz: 'Hozir qor yog‘yaptimi?', en: 'Is it snowing now?', ru: 'Идёт ли сейчас снег?'),
          false,
        ),
        (
          Localized(uz: 'Tunda quyosh ko‘rinmaydi.', en: 'You cannot see the sun at night.', ru: 'Ночью солнца не видно.'),
          Localized(uz: 'Hozir tun.', en: 'Now it is night.', ru: 'Сейчас ночь.'),
          Localized(uz: 'Quyosh ko‘rinyaptimi?', en: 'Can you see the sun?', ru: 'Видно ли солнце?'),
          false,
        ),
        (
          Localized(uz: 'Har bir kvadratning 4 ta burchagi bor.', en: 'Every square has 4 corners.', ru: 'У каждого квадрата 4 угла.'),
          Localized(uz: 'Bu shakl — kvadrat.', en: 'This shape is a square.', ru: 'Эта фигура — квадрат.'),
          Localized(uz: 'Unda 4 ta burchak bormi?', en: 'Does it have 4 corners?', ru: 'Есть ли у неё 4 угла?'),
          true,
        ),
        (
          Localized(uz: 'Hamma mevalar yeyiladi.', en: 'All fruits can be eaten.', ru: 'Все фрукты можно есть.'),
          Localized(uz: 'Olma — meva.', en: 'An apple is a fruit.', ru: 'Яблоко — фрукт.'),
          Localized(uz: 'Olmani yesa bo‘ladimi?', en: 'Can you eat an apple?', ru: 'Можно ли съесть яблоко?'),
          true,
        ),
        (
          Localized(uz: 'Uxlayotgan odam gapirmaydi.', en: 'A sleeping person does not talk.', ru: 'Спящий человек не разговаривает.'),
          Localized(uz: 'Bobur uxlayapti.', en: 'Bobur is sleeping.', ru: 'Бобур спит.'),
          Localized(uz: 'Bobur gapiryaptimi?', en: 'Is Bobur talking?', ru: 'Бобур разговаривает?'),
          false,
        ),
        (
          Localized(uz: 'Yomg‘ir yog‘sa, yer ho‘l bo‘ladi.', en: 'When it rains, the ground gets wet.', ru: 'Когда идёт дождь, земля мокрая.'),
          Localized(uz: 'Hozir yomg‘ir yog‘yapti.', en: 'It is raining now.', ru: 'Сейчас идёт дождь.'),
          Localized(uz: 'Yer ho‘lmi?', en: 'Is the ground wet?', ru: 'Земля мокрая?'),
          true,
        ),
      ];
      final f = g.pick(facts);
      final say = g.say('syllogism', {'f1': f.$1, 'f2': f.$2, 'q': f.$3});
      return g.choice(
        say: say,
        options: [Opt.text(f.$4 ? 'Ha' : 'Yo‘q'), Opt.text(f.$4 ? 'Yo‘q' : 'Ha')],
        concept: 'riddle:syllogism',
        meta: {'answer': f.$4 ? 'yes' : 'no'},
      );
    }
    // Bo'y: "Ali Nodiradan baland. Nodira Sardordan baland. Kim eng baland?"
    final names = g.sample(_people, 3);
    final askTallest = g.chance(0.5);
    return g.choice(
      say: g.say(askTallest ? 'tallest' : 'shortest', {'a': names[0], 'b': names[1], 'c': names[2]}),
      visual: SceneVisual([
        Layouts.emoji('👦', x: 0.25, size: 0.75),
        Layouts.emoji('👦', x: 0.5, size: 0.6),
        Layouts.emoji('👦', x: 0.75, size: 0.45),
      ], aspect: 2),
      options: [Opt.text(askTallest ? names[0] : names[2]), Opt.text(names[1]), Opt.text(askTallest ? names[2] : names[0])],
      concept: 'riddle:height',
      meta: {'order': names.join('>'), 'answer': askTallest ? names[0] : names[2]},
      explanation: '${names[0]} > ${names[1]} > ${names[2]}',
    );
  }

  /// Test uchun: kichik yordamchi.
  static String ordinalWord(int n) => UzNumbers.ordinal(n);
}
