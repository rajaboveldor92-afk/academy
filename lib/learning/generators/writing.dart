import 'dart:math' as math;

import '../content/uzbek_data.dart';
import '../models/exercise.dart';
import 'generator_base.dart';

/// ✏️ Yozishni o'rganaman: yozuvdan oldingi chiziqlar, nuqtalarni birlashtirish,
/// harf, raqam va qisqa so'zlarni barmoq bilan yozish. Aniqlik yumshoq baholanadi.
class WritingGenerators {
  WritingGenerators._();

  static final Map<String, ExerciseGenerator> generators = {
    'trace': trace,
  };

  /// `items` — elementlar ro'yxati:
  /// * `pre:<id>` — chiziq/shakl (`vertical`, `circle`, `zigzag` ...);
  /// * `dots:<id>` — raqamlangan nuqtalar (`star`, `house` ...);
  /// * `glyph:<X>` — harf yoki raqam (`A`, `O‘`, `SH`, `7`);
  /// * `words:<n>` — n harfli tasodifiy so'z (bosh harflar bilan).
  static Exercise trace(GenContext g) {
    final items = g.pl('items');
    final spec = g.pick(items);
    final junior = g.junior;
    final tolerance = math.min(0.12, (junior ? 0.11 : 0.085) * (g.p('tolerancePct', 100) / 100));
    final leftToRight = g.pb('leftToRight');
    // 4 yoshda qo'l harakati hali shakllanmoqda — qamrov talabi yumshoqroq.
    final coverage = junior ? 0.8 : 0.85;
    final parts = spec.split(':');
    final kind = parts[0], id = parts.sublist(1).join(':');
    final bank = g.content.glyphs;

    switch (kind) {
      case 'dots':
        final dots = bank.dots[id]!;
        return g.custom(
          say: g.say('wr_dots'),
          kind: ExerciseKind.trace,
          concept: 'trace:dots:$id',
          trace: TraceTask(id: spec, strokes: [dots], dots: true, tolerance: tolerance, minCoverage: 0.85),
          meta: {'item': spec},
        );
      case 'glyph':
        final strokes = bank.letter(id)!;
        final isDigit = RegExp(r'^\d$').hasMatch(id);
        return g.custom(
          say: isDigit ? g.say('wr_digit', {'n': int.parse(id)}) : g.say('wr_letter', {'l': _display(id)}),
          kind: ExerciseKind.trace,
          concept: 'trace:$id',
          trace: TraceTask(
            id: spec,
            strokes: strokes,
            label: _display(id),
            tolerance: tolerance,
            minCoverage: coverage,
            aspect: GlyphBank.unitWidth(id) > 1 ? 1.5 : 1.0,
          ),
          meta: {'item': spec},
          hint: 'Yashil nuqtadan boshla va strelka bo‘yicha yur.',
        );
      case 'words':
        final n = int.parse(id);
        final pool = g.uz.forAge(g.age).where((w) {
          final letters = w.letters;
          return letters.length == n && letters.every((l) => bank.letter(l.toUpperCase()) != null);
        }).toList();
        final w = g.pick(pool);
        final text = w.word.toUpperCase();
        return g.custom(
          say: g.say('wr_word', {'w': text}),
          kind: ExerciseKind.trace,
          concept: 'trace:word:${w.word}',
          trace: TraceTask(
            id: 'word:${w.word}',
            strokes: bank.word(w.word)!,
            label: text,
            aspect: GlyphBank.wordAspect(w.word),
            // Maydon pastroq bo'lgani uchun (balandlik birligida) chegarani biroz kengaytiramiz.
            tolerance: tolerance * 1.2,
            minCoverage: 0.8,
          ),
          meta: {'item': 'word:${w.word}'},
          hint: 'Harflarni chapdan o‘ngga, birma-bir yoz.',
        );
      default:
        final strokes = bank.prewriting[id]!;
        return g.custom(
          say: g.say(leftToRight ? 'wr_left_right' : (_shapes.contains(id) ? 'wr_trace_shape' : 'wr_trace_line')),
          kind: ExerciseKind.trace,
          concept: 'trace:pre:$id',
          trace: TraceTask(
            id: spec,
            strokes: strokes,
            tolerance: tolerance,
            minCoverage: coverage,
            leftToRight: leftToRight,
            aspect: _wide.contains(id) ? 1.6 : 1.0,
          ),
          meta: {'item': spec},
        );
    }
  }

  static const _shapes = {'circle', 'square', 'triangle', 'spiral'};
  static const _wide = {'zigzag', 'zigzag2', 'wave', 'waves2', 'loops', 'steps', 'horizontal'};

  /// "SH" → "Sh" (o'zbek yozuvidagi ko'rinishi).
  static String _display(String id) => id.length == 2 && id[1] != '‘' ? id[0] + id[1].toLowerCase() : id;
}
