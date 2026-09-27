import 'package:flutter/painting.dart';

import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';

/// 🧩 Rasmli puzzle. Rasmlar kod bilan chiziladi (osmon, yer va emoji'lar) — har safar
/// narsalar joylashuvi biroz boshqacha, shuning uchun bir xil puzzle kam takrorlanadi.
class PuzzleGames {
  PuzzleGames._();

  static final Map<String, ExerciseGenerator> generators = {
    'jigsaw': jigsaw,
  };

  /// Mavzu: fon ranglari, yer chizig'i va narsalar (emoji, x oralig'i, y oralig'i, o'lcham).
  static const Map<String, _Theme> themes = {
    'farm': _Theme(Color(0xFF8FD3FF), Color(0xFF7CC96B), 0.6, [
      _It('☀️', 0.75, 0.92, 0.08, 0.2, 0.2), _It('🏠', 0.1, 0.4, 0.45, 0.6, 0.34), _It('🌳', 0.55, 0.9, 0.42, 0.55, 0.3),
      _It('🐄', 0.1, 0.5, 0.72, 0.85, 0.24), _It('🐔', 0.55, 0.9, 0.75, 0.9, 0.18), _It('🌻', 0.3, 0.7, 0.85, 0.95, 0.14),
    ]),
    'sea': _Theme(Color(0xFF81D4FA), Color(0xFF1E88E5), 0.42, [
      _It('☀️', 0.08, 0.3, 0.08, 0.2, 0.2), _It('⛵', 0.5, 0.85, 0.3, 0.38, 0.24), _It('🐳', 0.1, 0.5, 0.58, 0.7, 0.3),
      _It('🐟', 0.55, 0.9, 0.62, 0.75, 0.16), _It('🐠', 0.2, 0.6, 0.82, 0.92, 0.16), _It('🦀', 0.65, 0.95, 0.86, 0.95, 0.14),
    ]),
    'space': _Theme(Color(0xFF1A237E), Color(0xFF311B92), 1.0, [
      _It('🚀', 0.15, 0.45, 0.45, 0.75, 0.3), _It('🌙', 0.65, 0.9, 0.1, 0.25, 0.24), _It('🌍', 0.55, 0.85, 0.6, 0.85, 0.3),
      _It('⭐', 0.05, 0.3, 0.05, 0.25, 0.1), _It('⭐', 0.35, 0.6, 0.12, 0.3, 0.08), _It('🛸', 0.1, 0.4, 0.82, 0.95, 0.16),
    ]),
    'city': _Theme(Color(0xFFB3E5FC), Color(0xFF9E9E9E), 0.62, [
      _It('🏢', 0.05, 0.3, 0.38, 0.5, 0.36), _It('🏫', 0.4, 0.7, 0.42, 0.52, 0.3), _It('🌳', 0.75, 0.95, 0.46, 0.56, 0.24),
      _It('🚌', 0.1, 0.45, 0.78, 0.88, 0.22), _It('🚗', 0.55, 0.9, 0.8, 0.92, 0.18), _It('☁️', 0.55, 0.9, 0.08, 0.2, 0.18),
    ]),
    'forest': _Theme(Color(0xFFB2EBF2), Color(0xFF558B2F), 0.58, [
      _It('🌲', 0.05, 0.3, 0.38, 0.5, 0.36), _It('🌲', 0.7, 0.95, 0.36, 0.48, 0.34), _It('🦊', 0.3, 0.6, 0.7, 0.82, 0.22),
      _It('🐻', 0.6, 0.9, 0.7, 0.85, 0.26), _It('🍄', 0.05, 0.3, 0.85, 0.95, 0.14), _It('🦉', 0.4, 0.6, 0.12, 0.28, 0.18),
    ]),
    'winter': _Theme(Color(0xFFCFE8FF), Color(0xFFF5F9FF), 0.6, [
      _It('⛄', 0.1, 0.4, 0.6, 0.75, 0.34), _It('🌲', 0.6, 0.9, 0.42, 0.55, 0.32), _It('❄️', 0.05, 0.35, 0.08, 0.25, 0.12),
      _It('❄️', 0.5, 0.8, 0.1, 0.25, 0.1), _It('🛷', 0.55, 0.9, 0.82, 0.93, 0.18), _It('🐧', 0.4, 0.6, 0.85, 0.95, 0.14),
    ]),
    'garden': _Theme(Color(0xFFE1F5FE), Color(0xFF8BC34A), 0.55, [
      _It('🌷', 0.05, 0.3, 0.7, 0.85, 0.2), _It('🌹', 0.35, 0.6, 0.72, 0.88, 0.2), _It('🌻', 0.65, 0.95, 0.65, 0.8, 0.26),
      _It('🦋', 0.1, 0.45, 0.2, 0.4, 0.18), _It('🐝', 0.55, 0.85, 0.25, 0.45, 0.14), _It('🌞', 0.72, 0.95, 0.05, 0.18, 0.18),
    ]),
    'jungle': _Theme(Color(0xFFC8E6C9), Color(0xFF2E7D32), 0.6, [
      _It('🌴', 0.02, 0.25, 0.35, 0.5, 0.4), _It('🐒', 0.3, 0.55, 0.2, 0.38, 0.2), _It('🦁', 0.35, 0.7, 0.66, 0.8, 0.3),
      _It('🐘', 0.68, 0.95, 0.6, 0.78, 0.3), _It('🦜', 0.65, 0.9, 0.12, 0.28, 0.16), _It('🐍', 0.05, 0.35, 0.85, 0.95, 0.14),
    ]),
    'party': _Theme(Color(0xFFFCE4EC), Color(0xFFCE93D8), 0.66, [
      _It('🎈', 0.05, 0.3, 0.1, 0.35, 0.22), _It('🎈', 0.7, 0.95, 0.12, 0.35, 0.2), _It('🎂', 0.35, 0.65, 0.5, 0.65, 0.32),
      _It('🎁', 0.05, 0.3, 0.78, 0.9, 0.2), _It('🎉', 0.7, 0.95, 0.78, 0.9, 0.2), _It('🧸', 0.4, 0.6, 0.82, 0.95, 0.16),
    ]),
  };

  /// Bitta katta rasm (4 yosh, oson): markazda yirik hayvon + 1–2 kichik narsa.
  static const List<String> bigHeroes = ['🦁', '🐶', '🐱', '🐸', '🐼', '🐯', '🐵', '🐰', '🦄', '🐻'];

  static PictureVisual picture(GenContext g, String style) {
    if (style == 'big') {
      final hero = g.pick(bigHeroes);
      final bg = g.pick(const [Color(0xFFFFF3C4), Color(0xFFD7F5E0), Color(0xFFDDEBFF), Color(0xFFFFE0EC)]);
      return PictureVisual(
        id: 'big$hero',
        top: bg,
        ground: Color.lerp(bg, const Color(0xFF7CC96B), 0.5)!,
        horizon: 0.8,
        items: [
          Layouts.emoji(hero, size: 0.7, x: 0.45 + g.rng.nextDouble() * 0.1, y: 0.5),
          Layouts.emoji(g.pick(const ['☀️', '⭐', '🌈', '☁️']), size: 0.2, x: 0.84, y: 0.14),
          Layouts.emoji(g.pick(const ['🌷', '🍎', '🎈', '🦋']), size: 0.18, x: 0.14, y: 0.86),
        ],
      );
    }
    final key = g.pick(themes.keys.toList());
    final t = themes[key]!;
    double between(double a, double b) => a + g.rng.nextDouble() * (b - a);
    return PictureVisual(
      id: key,
      top: t.top,
      ground: t.ground,
      horizon: t.horizon,
      items: [
        for (final it in t.items) Layouts.emoji(it.emoji, size: it.size, x: between(it.x0, it.x1), y: between(it.y0, it.y1)),
      ],
    );
  }

  static Exercise jigsaw(GenContext g) {
    final rows = g.p('rows', 2), cols = g.p('cols', 2);
    final style = g.pick(g.pl('styles').isEmpty ? ['scene'] : g.pl('styles'));
    final pic = picture(g, style);
    return g.custom(
      say: g.say('pz_jigsaw'),
      kind: ExerciseKind.jigsaw,
      concept: 'puzzle:${rows * cols}',
      jigsaw: JigsawTask(picture: pic, rows: rows, cols: cols),
      meta: {'pieces': rows * cols, 'picture': pic.id},
      rewardStars: rows * cols >= 12 ? 3 : (rows * cols >= 6 ? 2 : 1),
    );
  }
}

class _Theme {
  const _Theme(this.top, this.ground, this.horizon, this.items);

  final Color top;
  final Color ground;
  final double horizon;
  final List<_It> items;
}

class _It {
  const _It(this.emoji, this.x0, this.x1, this.y0, this.y1, this.size);

  final String emoji;
  final double x0, x1, y0, y1, size;
}
