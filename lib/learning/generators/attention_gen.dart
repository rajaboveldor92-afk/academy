import 'package:flutter/painting.dart';

import '../content/instructions.dart';
import '../content/lexicon.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';
import 'logic_junior.dart';
import 'writing.dart';

/// 🎯 Diqqat va ✋ motorika: rasm ichidan topish, hammasini topish, ranglar, farqni top,
/// diqqat bilan sanash, egizagini top, labirint; pufaklarni yorish, soyaga sudrash, chiziq bo'ylab yurish.
/// Vaqt bosimi yo'q — bola o'z sur'atida ishlaydi.
class AttentionGames {
  AttentionGames._();

  static final Map<String, ExerciseGenerator> generators = {
    'find': find,
    'find_all': findAll,
    'find_color': findColor,
    'difference': difference,
    'count': countInScene,
    'twin': LogicJunior.sameFind,
    'maze': LogicJunior.maze,
    'bubbles': bubbles,
    'drag_shadow': LogicJunior.shadow,
    'trace': WritingGenerators.trace,
  };

  static const double aspect = 1.4;

  /// [n] ta joy: katakchalar bo'yicha, biroz tartibsiz, ustma-ust tushmaydi.
  static List<(double, double, double)> _spots(GenContext g, int n, {double fill = 0.7}) {
    var cols = 1;
    while (cols * (cols / aspect).ceil() < n) {
      cols++;
    }
    final rows = (n / cols).ceil() < (cols / aspect).ceil() ? (cols / aspect).ceil() : (n / cols).ceil();
    final cells = g.sample([for (var i = 0; i < cols * rows; i++) i], n);
    final cw = 1 / cols, ch = 1 / rows;
    final size = (cw * aspect < ch ? cw * aspect : ch) * fill;
    return [
      for (final c in cells)
        (
          (c % cols + 0.5 + (g.rng.nextDouble() - 0.5) * 0.25) * cw,
          (c ~/ cols + 0.5 + (g.rng.nextDouble() - 0.5) * 0.25) * ch,
          size,
        ),
    ];
  }

  static List<LexiconEntry> _pool(GenContext g) {
    final seen = <String>{};
    return [for (final e in g.countables()) if (seen.add(e.emoji)) e];
  }

  static Exercise _spot(GenContext g, RenderedInstruction say, List<SceneItem> items, Set<int> targets, String concept,
      {List<SceneItem>? reference, String? hint, Map<String, Object> meta = const {}}) {
    return g.custom(
      say: say,
      kind: ExerciseKind.spot,
      concept: concept,
      spot: SpotTask(items: items, targets: targets, aspect: aspect, reference: reference),
      hint: hint,
      meta: meta,
    );
  }

  // ------------------------------------------------------------ Bitta narsani top
  static Exercise find(GenContext g) {
    final n = g.p('items', 6);
    final pool = _pool(g);
    final target = g.pick(pool);
    final others = g.sample(pool.where((e) => e.id != target.id).toList(), n - 1);
    final spots = _spots(g, n);
    final emojis = [target, ...others];
    final items = [for (var i = 0; i < n; i++) Layouts.emoji(emojis[i].emoji, x: spots[i].$1, y: spots[i].$2, size: spots[i].$3)];
    return _spot(g, g.say('at_find', {'item': target}), items, {0}, 'attention:find:${target.id}',
        meta: {'answer': target.id});
  }

  // ------------------------------------------------------------ Hammasini top
  static Exercise findAll(GenContext g) {
    final n = g.p('items', 8);
    final k = g.p('targets', 3);
    final pool = _pool(g);
    final target = g.pick(pool);
    // Katta darajada chalg'ituvchilar shu kategoriyadan (o'xshash) bo'ladi.
    final similar = g.pb('similar');
    final distractorPool = pool.where((e) => e.id != target.id && (!similar || e.category == target.category)).toList();
    final kinds = g.sample(distractorPool.length >= 2 ? distractorPool : pool.where((e) => e.id != target.id).toList(), 3);
    final spots = _spots(g, n);
    final sizeScale = g.p('sizePct', 100) / 100;
    final items = <SceneItem>[
      for (var i = 0; i < n; i++)
        Layouts.emoji(
          i < k ? target.emoji : kinds[i % kinds.length].emoji,
          x: spots[i].$1,
          y: spots[i].$2,
          size: spots[i].$3 * sizeScale,
        ),
    ];
    return _spot(g, g.say('at_find_all', {'item': target}), items, {for (var i = 0; i < k; i++) i},
        'attention:find_all:${target.id}',
        hint: 'Rasmni chapdan o‘ngga, qatorma-qator ko‘zdan kechir.', meta: {'answer': k});
  }

  // ------------------------------------------------------------ Bir xil rangdagilarni top
  static Exercise findColor(GenContext g) {
    final n = g.p('items', 8);
    final k = g.p('targets', 3);
    final colors = g.lex.colors.where((c) => !{'white', 'brown', 'black'}.contains(c.id)).toList();
    final picked = g.sample(colors, 3);
    final target = picked.first;
    const shapes = ['circle', 'square', 'triangle', 'star', 'heart'];
    final spots = _spots(g, n);
    final items = <SceneItem>[
      for (var i = 0; i < n; i++)
        Layouts.shape(
          g.pick(shapes),
          i < k ? target.color : picked[1 + i % 2].color,
          x: spots[i].$1,
          y: spots[i].$2,
          size: spots[i].$3,
        ),
    ];
    final ru = g.content.languages.colorRu(target.id, 'n');
    return _spot(
      g,
      g.say('at_find_color', {'color': Localized(uz: target.name.uz, en: target.name.en, ru: ru)}),
      items,
      {for (var i = 0; i < k; i++) i},
      'attention:color:${target.id}',
      meta: {'answer': target.id},
    );
  }

  // ------------------------------------------------------------ Farqni top
  static Exercise difference(GenContext g) {
    final n = g.p('items', 4);
    final pool = _pool(g);
    final chosen = g.sample(pool, n + 1);
    final spots = _spots(g, n, fill: 0.62);
    final reference = [for (var i = 0; i < n; i++) Layouts.emoji(chosen[i].emoji, x: spots[i].$1, y: spots[i].$2, size: spots[i].$3)];
    final idx = g.rng.nextInt(n);
    final changed = [
      for (var i = 0; i < n; i++) i == idx ? reference[i].copyWith() : reference[i],
    ];
    changed[idx] = Layouts.emoji(chosen.last.emoji, x: spots[idx].$1, y: spots[idx].$2, size: spots[idx].$3);
    return _spot(g, g.say('at_difference'), changed, {idx}, 'attention:difference:$n',
        reference: reference, hint: 'Ikkala rasmni narsama-narsa solishtir.', meta: {'answer': chosen.last.id});
  }

  // ------------------------------------------------------------ Diqqat bilan sana
  static Exercise countInScene(GenContext g) {
    final max = g.p('max', 5);
    final n = g.p('items', 8);
    final k = g.range(1, max < n ? max : n - 1);
    final pool = _pool(g);
    final target = g.pick(pool);
    final kinds = g.sample(pool.where((e) => e.id != target.id && e.category == target.category).toList(), 2);
    final fillers = kinds.length < 2 ? g.sample(pool.where((e) => e.id != target.id).toList(), 2) : kinds;
    final spots = _spots(g, n);
    final items = [
      for (var i = 0; i < n; i++) Layouts.emoji(i < k ? target.emoji : fillers[i % 2].emoji, x: spots[i].$1, y: spots[i].$2, size: spots[i].$3),
    ];
    return g.choice(
      say: g.say('at_count', {'item': target}),
      visual: SceneVisual(items, aspect: aspect),
      options: [for (final v in g.numberChoices(k, min: 1, max: n, spread: 2)) Opt.number(v)],
      concept: 'attention:count:$k',
      meta: {'answer': k, 'target': target.id},
      hint: 'Topganingni barmog‘ing bilan bittadan sana.',
    );
  }

  // ------------------------------------------------------------ Pufaklar (motorika)
  static Exercise bubbles(GenContext g) {
    final n = g.p('items', 5);
    final sizeScale = g.p('sizePct', 100) / 100;
    final spots = _spots(g, n, fill: 0.75);
    const palette = [Color(0xFF81D4FA), Color(0xFFA5D6A7), Color(0xFFFFCC80), Color(0xFFF48FB1), Color(0xFFCE93D8)];
    final items = [
      for (var i = 0; i < n; i++)
        SceneItem(
          kind: SceneKind.shape,
          value: 'circle',
          color: palette[g.rng.nextInt(palette.length)],
          x: spots[i].$1,
          y: spots[i].$2,
          size: spots[i].$3 * sizeScale * (0.8 + g.rng.nextDouble() * 0.3),
          opacity: 0.85,
        ),
    ];
    return _spot(g, g.say('mo_bubbles'), items, {for (var i = 0; i < n; i++) i}, 'motor:bubbles:$n',
        meta: {'answer': n});
  }
}
