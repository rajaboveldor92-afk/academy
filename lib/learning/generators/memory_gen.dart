import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';
import 'logic_junior.dart';

/// 🧠 Xotira o'yinlari: juft kartalar, "qaysi biri yo'qoldi?", ketma-ketlikni eslab qolish,
/// "nima o'zgardi?", rasmda nima (nechta) bor edi, narsa qayerda edi.
class MemoryGames {
  MemoryGames._();

  static final Map<String, ExerciseGenerator> generators = {
    'cards': cards,
    'missing': LogicJunior.missingItem,
    'recall': recall,
    'changed': changed,
    'was_there': wasThere,
    'how_many': howMany,
    'where': where,
  };

  /// Rangli yuraklar — Android 9 da ham ko'rinadigan rang belgilari.
  static const List<String> colorHearts = ['❤️', '🧡', '💛', '💚', '💙', '💜'];

  static List<String> _emojis(GenContext g) => {for (final e in g.countables()) e.emoji}.toList();

  // ------------------------------------------------------------ Juft kartalar
  static Exercise cards(GenContext g) {
    final pairs = g.p('pairs', 3);
    final faces = g.sample(_emojis(g), pairs);
    final deck = [...faces, ...faces]..shuffle(g.rng);
    final cols = switch (deck.length) { <= 4 => 2, 6 => 3, _ => 4 };
    return g.custom(
      say: g.say('mem_cards'),
      kind: ExerciseKind.cards,
      concept: 'memory:cards:$pairs',
      cards: CardsTask(faces: deck, cols: cols),
      meta: {'pairs': pairs},
      rewardStars: pairs >= 6 ? 2 : 1,
    );
  }

  static SceneVisual _row(List<String> emojis, {double size = 0.55}) =>
      SceneVisual(Layouts.row([for (final e in emojis) Layouts.emoji(e, size: size)]), aspect: emojis.length * 0.85);

  // ------------------------------------------------------------ Ketma-ketlikni eslab qol
  /// `kind`: `emoji` (rasmlar) yoki `color` (rangli yuraklar). Avval ko'rsatiladi, keyin tartib bilan bosiladi.
  static Exercise recall(GenContext g) {
    final n = g.p('items', 3);
    final colors = g.ps('kind', 'emoji') == 'color';
    final seq = g.sample(colors ? colorHearts : _emojis(g), n);
    final extra = g.p('extra', 0);
    final tiles = [...seq];
    if (extra > 0) {
      final pool = (colors ? colorHearts : _emojis(g)).where((e) => !seq.contains(e)).toList();
      tiles.addAll(g.sample(pool, extra));
    }
    return g.custom(
      say: g.say(colors ? 'mem_colors' : 'mem_recall'),
      kind: ExerciseKind.assemble,
      concept: 'memory:sequence:$n',
      assemble: AssembleTask(answer: seq, tiles: g.mixTiles(tiles, seq)),
      preview: _row(seq),
      previewSeconds: g.p('seconds', n + 2),
      meta: {'answer': seq.join()},
      explanation: seq.join(' → '),
    );
  }

  // ------------------------------------------------------------ Nima o'zgardi?
  static Exercise changed(GenContext g) {
    final n = g.p('items', 3);
    final pool = _emojis(g);
    final items = g.sample(pool, n + 1);
    final before = items.take(n).toList();
    final fresh = items.last;
    final idx = g.rng.nextInt(n);
    final after = [for (var i = 0; i < n; i++) i == idx ? fresh : before[i]];
    final others = g.sample([for (var i = 0; i < n; i++) if (i != idx) after[i]], g.p('options', 3) - 1);
    return g.choice(
      say: g.say('mem_changed'),
      kind: ExerciseKind.memory,
      preview: _row(before),
      previewSeconds: g.p('seconds', n + 2),
      visual: _row(after),
      options: [Opt.emoji(fresh), for (final o in others) Opt.emoji(o)],
      concept: 'memory:changed:$n',
      meta: {'answer': fresh},
      explanation: '${before[idx]} → $fresh',
    );
  }

  // ------------------------------------------------------------ Rasmda nima bor edi?
  static Exercise wasThere(GenContext g) {
    final n = g.p('items', 3);
    final pool = _emojis(g);
    final shown = g.sample(pool, n);
    final absent = g.sample(pool.where((e) => !shown.contains(e)).toList(), g.p('options', 3) - 1);
    final answer = g.pick(shown);
    return g.choice(
      say: g.say('mem_was_there'),
      kind: ExerciseKind.memory,
      preview: SceneVisual(_scatter(g, shown), aspect: 1.6),
      previewSeconds: g.p('seconds', n + 2),
      options: [Opt.emoji(answer), for (final a in absent) Opt.emoji(a)],
      concept: 'memory:was_there:$n',
      meta: {'answer': answer},
    );
  }

  /// Narsalarni sahnaga tartibsiz (lekin ustma-ust tushmasdan) joylash.
  static List<SceneItem> _scatter(GenContext g, List<String> emojis, {double aspect = 1.6}) {
    final n = emojis.length;
    final cols = n <= 3 ? n : (n <= 6 ? 3 : 4);
    final rows = (n / cols).ceil();
    final cells = g.sample([for (var i = 0; i < cols * rows; i++) i], n);
    final cw = 1 / cols, ch = 1 / rows;
    final size = (cw * aspect < ch ? cw * aspect : ch) * 0.62;
    return [
      for (var i = 0; i < n; i++)
        Layouts.emoji(
          emojis[i],
          size: size,
          x: (cells[i] % cols + 0.5 + (g.rng.nextDouble() - 0.5) * 0.3) * cw,
          y: (cells[i] ~/ cols + 0.5 + (g.rng.nextDouble() - 0.5) * 0.3) * ch,
        ),
    ];
  }

  // ------------------------------------------------------------ Nechta bor edi?
  static Exercise howMany(GenContext g) {
    final max = g.p('max', 4);
    final k = g.range(1, max);
    final item = g.pick(g.countables());
    final distractors = g.p('distractors', 0);
    final others = g.sample(_emojis(g).where((e) => e != item.emoji).toList(), distractors);
    final shown = [...List.filled(k, item.emoji), ...others]..shuffle(g.rng);
    return g.choice(
      say: g.say('mem_how_many', {'item': item}),
      kind: ExerciseKind.memory,
      preview: SceneVisual(_scatter(g, shown), aspect: 1.6),
      previewSeconds: g.p('seconds', 4),
      options: [for (final v in g.numberChoices(k, min: 1, max: max + 1, spread: 2)) Opt.number(v)],
      concept: 'memory:count:$k',
      meta: {'answer': k},
    );
  }

  // ------------------------------------------------------------ Qayerda edi?
  static Exercise where(GenContext g) {
    final size = g.p('grid', 2);
    final cellsN = size * size;
    final count = g.p('items', 2).clamp(1, cellsN).toInt();
    final emojis = g.sample(_emojis(g), count);
    final places = g.sample([for (var i = 0; i < cellsN; i++) i], count);
    final targetIdx = g.rng.nextInt(count);
    final target = emojis[targetIdx];
    final preview = GridVisual(
      rows: size,
      cols: size,
      cells: [
        for (var c = 0; c < cellsN; c++)
          places.contains(c) ? [Layouts.emoji(emojis[places.indexOf(c)], size: 0.7)] : <SceneItem>[],
      ],
      showQuestionMark: false,
    );
    GridVisual marker(int cell) => GridVisual(
          rows: size,
          cols: size,
          cells: [
            for (var c = 0; c < cellsN; c++) c == cell ? [Layouts.emoji('⭐', size: 0.7)] : <SceneItem>[],
          ],
          showQuestionMark: false,
        );
    final correct = places[targetIdx];
    final wrong = g.sample([for (var c = 0; c < cellsN; c++) if (c != correct) c], (g.p('options', 3) - 1).clamp(1, cellsN - 1).toInt());
    final label = Opt.emoji(target);
    return g.choice(
      say: g.say('mem_where', {'item': g.lex.entries.firstWhere((e) => e.emoji == target)}),
      kind: ExerciseKind.memory,
      preview: preview,
      previewSeconds: g.p('seconds', 4),
      visual: label.visual,
      options: [ExerciseOption(visual: marker(correct)), for (final c in wrong) ExerciseOption(visual: marker(c))],
      concept: 'memory:where:$size',
      meta: {'answer': correct},
    );
  }
}
