import 'package:flutter/painting.dart';

/// Mashq ekranidagi rasm qismi. Barcha rasmlar kod bilan chiziladi
/// (emoji, geometrik shakllar, soat) — tashqi rasm fayllari va mualliflik
/// huquqi muammosi yo'q, APK hajmi kichik qoladi.
abstract class ExerciseVisual {
  const ExerciseVisual();

  /// Takrorlanmaslik va testlar uchun matnli tavsif.
  String describe();
}

/// Sahnadagi element turi.
enum SceneKind { emoji, shape, text, bar, coin }

/// Emoji yoki shaklning yarmini ko'rsatish (puzzle mashqlari uchun).
enum HalfClip { none, left, right }

/// Sahnadagi bitta element. Koordinatalar sahna o'lchamiga nisbatan (0..1),
/// [x], [y] — element markazi; [size] — sahna balandligiga nisbatan.
class SceneItem {
  const SceneItem({
    required this.kind,
    required this.value,
    this.x = 0.5,
    this.y = 0.5,
    this.size = 0.3,
    this.color,
    this.rotation = 0,
    this.flipX = false,
    this.silhouette = false,
    this.crossed = false,
    this.clip = HalfClip.none,
    this.opacity = 1,
    this.length = 0,
  });

  final SceneKind kind;

  /// Emoji, matn, shakl nomi (`circle`, `triangle`, ...) yoki tanga qiymati.
  final String value;
  final double x;
  final double y;
  final double size;
  final Color? color;

  /// Burilish (to'liq aylanish ulushlarida: 0.25 = 90°).
  final double rotation;
  final bool flipX;

  /// Qora soya ko'rinishi ("Soyasini top").
  final bool silhouette;

  /// Ustidan chizilgan (ayirish mashqlari: "olib ketildi").
  final bool crossed;
  final HalfClip clip;
  final double opacity;

  /// Chiziq/lenta uzunligi (sahna kengligiga nisbatan) — [SceneKind.bar] uchun.
  final double length;

  SceneItem copyWith({
    double? x,
    double? y,
    double? size,
    Color? color,
    double? rotation,
    bool? flipX,
    bool? silhouette,
    bool? crossed,
    HalfClip? clip,
    double? opacity,
  }) {
    return SceneItem(
      kind: kind,
      value: value,
      x: x ?? this.x,
      y: y ?? this.y,
      size: size ?? this.size,
      color: color ?? this.color,
      rotation: rotation ?? this.rotation,
      flipX: flipX ?? this.flipX,
      silhouette: silhouette ?? this.silhouette,
      crossed: crossed ?? this.crossed,
      clip: clip ?? this.clip,
      opacity: opacity ?? this.opacity,
      length: length,
    );
  }

  String describe() {
    final b = StringBuffer('${kind.name}:$value');
    if (color != null) b.write('#${color!.toARGB32Compat()}');
    if (size != 0.3) b.write('@${size.toStringAsFixed(2)}');
    if (rotation != 0) b.write('r${rotation.toStringAsFixed(2)}');
    if (flipX) b.write('F');
    if (silhouette) b.write('S');
    if (crossed) b.write('X');
    if (clip != HalfClip.none) b.write('C${clip.name}');
    if (length != 0) b.write('L${length.toStringAsFixed(2)}');
    b.write('(${x.toStringAsFixed(2)},${y.toStringAsFixed(2)})');
    return b.toString();
  }
}

extension ColorCompat on Color {
  /// Rangni butun son ko'rinishida (Flutter versiyalaridan qat'i nazar).
  int toARGB32Compat() {
    int c(double v) => (v * 255.0).round() & 0xff;
    return (c(a) << 24) | (c(r) << 16) | (c(g) << 8) | c(b);
  }
}

/// Erkin joylashtirilgan elementlar sahnasi.
class SceneVisual extends ExerciseVisual {
  const SceneVisual(this.items, {this.aspect = 2.0});

  final List<SceneItem> items;

  /// Kenglik / balandlik nisbati.
  final double aspect;

  @override
  String describe() => 'scene[${items.map((e) => e.describe()).join(';')}]';
}

/// Katta matn: son, misol, ketma-ketlik ("2, 4, 6, ?").
class TextVisual extends ExerciseVisual {
  const TextVisual(this.text, {this.scale = 1});

  final String text;
  final double scale;

  @override
  String describe() => 'text[$text]';
}

/// Analog soat.
class ClockVisual extends ExerciseVisual {
  const ClockVisual(this.hour, this.minute);

  final int hour;
  final int minute;

  @override
  String describe() => 'clock[$hour:$minute]';
}

/// Katakli jadval (2×2 / 3×3 matritsa, kodlash maydoni, koordinatali sahna).
/// `null` katak — "?" (yetishmayotgan element).
class GridVisual extends ExerciseVisual {
  const GridVisual({
    required this.rows,
    required this.cols,
    required this.cells,
    this.showQuestionMark = true,
  });

  final int rows;
  final int cols;

  /// Uzunligi rows*cols. Har bir katak — kichik sahna: elementlar katak
  /// ichidagi nisbiy koordinatalarda (0..1).
  final List<List<SceneItem>?> cells;
  final bool showQuestionMark;

  @override
  String describe() => 'grid${rows}x$cols[${cells.map((c) => c == null ? '?' : c.map((e) => e.describe()).join('+')).join(';')}]';
}
