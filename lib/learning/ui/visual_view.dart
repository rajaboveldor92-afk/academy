import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../l10n/tr.dart';
import '../../theme/app_colors.dart';
import '../models/visual.dart';

/// Har qanday [ExerciseVisual] ni chizadi.
class VisualView extends StatelessWidget {
  const VisualView({super.key, required this.visual, this.onSpeak, this.maxHeight});

  final ExerciseVisual visual;

  /// `TextVisual('🔊')` — "tinglab top" mashqlarida katta karnay tugmasi.
  final VoidCallback? onSpeak;
  final double? maxHeight;

  @override
  Widget build(BuildContext context) {
    final v = visual;
    Widget child;
    if (v is SceneVisual) {
      child = SceneView(scene: v);
    } else if (v is TextVisual) {
      if (v.text == '🔊') {
        child = Center(
          child: IconButton.filledTonal(
            iconSize: 72,
            onPressed: onSpeak,
            icon: const Icon(Icons.volume_up_rounded),
          ),
        );
      } else {
        child = Center(
          child: FittedBox(
            fit: BoxFit.scaleDown,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 12),
              child: Text(
                v.text,
                style: TextStyle(
                  fontSize: 56 * v.scale,
                  fontWeight: FontWeight.w900,
                  color: AppColors.text,
                  letterSpacing: 1,
                ),
              ),
            ),
          ),
        );
      }
    } else if (v is ReadingVisual) {
      child = ReadingView(reading: v);
    } else if (v is PictureVisual) {
      child = PictureView(picture: v);
    } else if (v is ClockVisual) {
      child = AspectRatio(aspectRatio: 1, child: CustomPaint(painter: ClockPainter(v.hour, v.minute)));
    } else if (v is GridVisual) {
      child = ExerciseGridView(grid: v);
    } else {
      child = const SizedBox.shrink();
    }
    if (maxHeight != null) {
      return ConstrainedBox(constraints: BoxConstraints(maxHeight: maxHeight!), child: child);
    }
    return child;
  }
}

/// O'qish matni: bitta so'z (juda yirik) yoki gap/hikoya (bir necha qator) + savol.
/// Matn bola o'zi o'qishi uchun — ovozda aytilmaydi (faqat ko'rsatma aytiladi).
class ReadingView extends StatelessWidget {
  const ReadingView({super.key, required this.reading});

  final ReadingVisual reading;

  @override
  Widget build(BuildContext context) {
    final r = reading;
    final emoji = r.emoji;
    final question = r.question;
    return LayoutBuilder(builder: (context, c) {
      final width = c.hasBoundedWidth ? c.maxWidth : 360.0;
      final Widget content;
      if (r.big) {
        content = Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            if (emoji != null) ...[
              Text(emoji, style: const TextStyle(fontSize: 64, height: 1)),
              const SizedBox(width: 18),
            ],
            Text(
              r.text,
              style: const TextStyle(
                fontSize: 64,
                fontWeight: FontWeight.w900,
                color: AppColors.text,
                letterSpacing: 2,
                height: 1.1,
              ),
            ),
          ],
        );
      } else {
        content = Container(
          width: width,
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
          decoration: BoxDecoration(
            color: const Color(0xFFFFFDF7),
            borderRadius: BorderRadius.circular(24),
            border: Border.all(color: const Color(0xFFEADFC8), width: 2),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              if (emoji != null) Text(emoji, style: const TextStyle(fontSize: 44, height: 1.2)),
              Text(
                r.text,
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 28, fontWeight: FontWeight.w700, color: AppColors.text, height: 1.45),
              ),
              if (question != null) ...[
                const SizedBox(height: 12),
                Container(height: 2, width: width * 0.4, color: const Color(0xFFEADFC8)),
                const SizedBox(height: 12),
                Text(
                  question,
                  textAlign: TextAlign.center,
                  style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w900, color: AppColors.primary, height: 1.3),
                ),
              ],
            ],
          ),
        );
      }
      if (!c.hasBoundedHeight) return Center(child: content);
      return FittedBox(fit: BoxFit.scaleDown, child: content);
    });
  }
}

/// Rangli fonli rasm (osmon + yer + emoji'lar) — puzzle rasmi.
class PictureView extends StatelessWidget {
  const PictureView({super.key, required this.picture});

  final PictureVisual picture;

  @override
  Widget build(BuildContext context) {
    final p = picture;
    return AspectRatio(
      aspectRatio: p.aspect,
      child: ClipRect(
        child: Stack(
          fit: StackFit.expand,
          children: [
            DecoratedBox(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [p.top, Color.lerp(p.top, Colors.white, 0.45)!, p.ground, Color.lerp(p.ground, Colors.black, 0.12)!],
                  stops: [0, p.horizon, p.horizon, 1],
                ),
              ),
            ),
            SceneView(scene: SceneVisual(p.items, aspect: p.aspect)),
          ],
        ),
      ),
    );
  }
}

/// Erkin sahna: elementlar nisbiy koordinatalarda.
class SceneView extends StatelessWidget {
  const SceneView({super.key, required this.scene});

  final SceneVisual scene;

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: scene.aspect,
      child: LayoutBuilder(
        builder: (context, c) {
          final w = c.maxWidth, h = c.maxHeight;
          return Stack(
            clipBehavior: Clip.none,
            children: [
              for (final item in scene.items) _positioned(item, w, h),
            ],
          );
        },
      ),
    );
  }

  Widget _positioned(SceneItem item, double w, double h) {
    if (item.kind == SceneKind.bar) {
      final bw = item.length * w, bh = math.max(4.0, item.size * h);
      return Positioned(
        left: item.x * w - bw / 2,
        top: item.y * h - bh / 2,
        width: bw,
        height: bh,
        child: DecoratedBox(
          decoration: BoxDecoration(
            color: item.color ?? AppColors.primary,
            borderRadius: BorderRadius.circular(bh / 2),
          ),
        ),
      );
    }
    final s = item.size * h;
    return Positioned(
      left: item.x * w - s / 2,
      top: item.y * h - s / 2,
      width: s,
      height: s,
      child: SceneItemView(item: item, extent: s),
    );
  }
}

/// Bitta sahna elementi (kvadrat [extent] ichida).
class SceneItemView extends StatelessWidget {
  const SceneItemView({super.key, required this.item, required this.extent});

  final SceneItem item;
  final double extent;

  @override
  Widget build(BuildContext context) {
    Widget child;
    switch (item.kind) {
      case SceneKind.emoji:
        child = Center(
          child: Text(
            item.value,
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: extent * 0.8, height: 1.0),
          ),
        );
        if (item.silhouette) {
          child = ColorFiltered(
            colorFilter: const ColorFilter.mode(Color(0xFF2A2D43), BlendMode.srcIn),
            child: child,
          );
        }
      case SceneKind.shape:
        child = CustomPaint(
          size: Size.square(extent),
          painter: ShapePainter(item.value, item.color ?? AppColors.primary, silhouette: item.silhouette),
        );
      case SceneKind.text:
        child = Center(
          child: FittedBox(
            fit: BoxFit.scaleDown,
            child: Text(
              item.value,
              style: TextStyle(
                fontSize: extent * 0.8,
                height: 1.0,
                fontWeight: FontWeight.w900,
                color: item.color ?? AppColors.text,
              ),
            ),
          ),
        );
      case SceneKind.coin:
        child = _Coin(value: item.value, color: item.color ?? const Color(0xFFFFD54F), extent: extent);
      case SceneKind.bar:
        child = const SizedBox.shrink();
    }
    if (item.flipX) {
      child = Transform(alignment: Alignment.center, transform: Matrix4.diagonal3Values(-1, 1, 1), child: child);
    }
    if (item.rotation != 0) {
      child = Transform.rotate(angle: item.rotation * 2 * math.pi, child: child);
    }
    if (item.clip != HalfClip.none) {
      child = ClipRect(clipper: _HalfClipper(item.clip), child: child);
    }
    if (item.crossed) {
      child = Stack(
        fit: StackFit.expand,
        children: [
          Opacity(opacity: 0.45, child: child),
          CustomPaint(painter: _CrossPainter()),
        ],
      );
    }
    if (item.opacity < 1) child = Opacity(opacity: item.opacity, child: child);
    return child;
  }
}

class _HalfClipper extends CustomClipper<Rect> {
  _HalfClipper(this.clip);

  final HalfClip clip;

  @override
  Rect getClip(Size size) => clip == HalfClip.left
      ? Rect.fromLTWH(0, 0, size.width / 2, size.height)
      : Rect.fromLTWH(size.width / 2, 0, size.width / 2, size.height);

  @override
  bool shouldReclip(_HalfClipper oldClipper) => oldClipper.clip != clip;
}

class _CrossPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()
      ..color = const Color(0xFFE53935)
      ..strokeWidth = size.width * 0.08
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(Offset(size.width * 0.15, size.height * 0.15), Offset(size.width * 0.85, size.height * 0.85), p);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

class _Coin extends StatelessWidget {
  const _Coin({required this.value, required this.color, required this.extent});

  final String value;
  final Color color;
  final double extent;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: color,
        shape: BoxShape.circle,
        border: Border.all(color: Colors.brown.withAlpha(120), width: extent * 0.05),
        boxShadow: const [BoxShadow(color: Color(0x33000000), blurRadius: 3, offset: Offset(0, 2))],
      ),
      alignment: Alignment.center,
      child: FittedBox(
        fit: BoxFit.scaleDown,
        child: Padding(
          padding: EdgeInsets.all(extent * 0.12),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(value, style: TextStyle(fontSize: extent * 0.4, fontWeight: FontWeight.w900, height: 1)),
              Text(Tr.of(context).sum, style: TextStyle(fontSize: extent * 0.16, fontWeight: FontWeight.w700, height: 1)),
            ],
          ),
        ),
      ),
    );
  }
}

/// Geometrik shakllar.
class ShapePainter extends CustomPainter {
  ShapePainter(this.shape, this.color, {this.silhouette = false});

  final String shape;
  final Color color;
  final bool silhouette;

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()..color = silhouette ? const Color(0xFF2A2D43) : color;
    final border = Paint()
      ..color = Colors.black.withAlpha(35)
      ..style = PaintingStyle.stroke
      ..strokeWidth = size.width * 0.03;
    final w = size.width, h = size.height;
    final path = shapePath(shape, w, h);
    canvas.drawPath(path, paint);
    canvas.drawPath(path, border);
  }

  static Path shapePath(String shape, double w, double h) {
    final p = Path();
    final m = w * 0.08;
    switch (shape) {
      case 'circle':
        p.addOval(Rect.fromLTWH(m, m, w - 2 * m, h - 2 * m));
      case 'oval':
        p.addOval(Rect.fromLTWH(m, h * 0.22, w - 2 * m, h * 0.56));
      case 'square':
        p.addRRect(RRect.fromRectAndRadius(Rect.fromLTWH(m, m, w - 2 * m, h - 2 * m), Radius.circular(w * 0.06)));
      case 'rectangle':
        p.addRRect(RRect.fromRectAndRadius(Rect.fromLTWH(m, h * 0.25, w - 2 * m, h * 0.5), Radius.circular(w * 0.05)));
      case 'triangle':
        p
          ..moveTo(w / 2, m)
          ..lineTo(w - m, h - m)
          ..lineTo(m, h - m)
          ..close();
      case 'rhombus':
        p
          ..moveTo(w / 2, m)
          ..lineTo(w - m, h / 2)
          ..lineTo(w / 2, h - m)
          ..lineTo(m, h / 2)
          ..close();
      case 'star':
        final cx = w / 2, cy = h / 2 + h * 0.03, ro = w / 2 - m, ri = ro * 0.45;
        for (var i = 0; i < 10; i++) {
          final r = i.isEven ? ro : ri;
          final a = -math.pi / 2 + i * math.pi / 5;
          final pt = Offset(cx + r * math.cos(a), cy + r * math.sin(a));
          if (i == 0) {
            p.moveTo(pt.dx, pt.dy);
          } else {
            p.lineTo(pt.dx, pt.dy);
          }
        }
        p.close();
      case 'heart':
        p
          ..moveTo(w / 2, h * 0.85)
          ..cubicTo(w * 0.05, h * 0.55, w * 0.1, h * 0.12, w / 2, h * 0.3)
          ..cubicTo(w * 0.9, h * 0.12, w * 0.95, h * 0.55, w / 2, h * 0.85)
          ..close();
      default:
        p.addOval(Rect.fromLTWH(m, m, w - 2 * m, h - 2 * m));
    }
    return p;
  }

  @override
  bool shouldRepaint(ShapePainter old) => old.shape != shape || old.color != color || old.silhouette != silhouette;
}

/// Analog soat.
class ClockPainter extends CustomPainter {
  ClockPainter(this.hour, this.minute);

  final int hour;
  final int minute;

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2);
    final r = size.shortestSide / 2 * 0.92;
    canvas.drawCircle(c, r, Paint()..color = Colors.white);
    canvas.drawCircle(
      c,
      r,
      Paint()
        ..color = AppColors.primary
        ..style = PaintingStyle.stroke
        ..strokeWidth = r * 0.07,
    );
    for (var i = 1; i <= 12; i++) {
      final a = -math.pi / 2 + i * math.pi / 6;
      final tp = TextPainter(
        text: TextSpan(
          text: '$i',
          style: TextStyle(fontSize: r * 0.2, fontWeight: FontWeight.w800, color: AppColors.text),
        ),
        textDirection: TextDirection.ltr,
      )..layout();
      final pos = Offset(c.dx + math.cos(a) * r * 0.78, c.dy + math.sin(a) * r * 0.78);
      tp.paint(canvas, pos - Offset(tp.width / 2, tp.height / 2));
    }
    void hand(double turns, double length, double width, Color color) {
      final a = -math.pi / 2 + turns * 2 * math.pi;
      canvas.drawLine(
        c,
        Offset(c.dx + math.cos(a) * length, c.dy + math.sin(a) * length),
        Paint()
          ..color = color
          ..strokeWidth = width
          ..strokeCap = StrokeCap.round,
      );
    }

    hand(((hour % 12) + minute / 60) / 12, r * 0.48, r * 0.1, AppColors.text);
    hand(minute / 60, r * 0.72, r * 0.06, const Color(0xFFE53935));
    canvas.drawCircle(c, r * 0.06, Paint()..color = AppColors.text);
  }

  @override
  bool shouldRepaint(ClockPainter old) => old.hour != hour || old.minute != minute;
}

/// Katakli jadval (matritsa, kodlash maydoni).
class ExerciseGridView extends StatelessWidget {
  const ExerciseGridView({super.key, required this.grid});

  final GridVisual grid;

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: grid.cols / grid.rows,
      child: Container(
        padding: const EdgeInsets.all(4),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(18),
          border: Border.all(color: AppColors.primary.withAlpha(60), width: 2),
        ),
        child: Column(
          children: [
            for (var r = 0; r < grid.rows; r++)
              Expanded(
                child: Row(
                  children: [
                    for (var c = 0; c < grid.cols; c++)
                      Expanded(child: _cell(grid.cells[r * grid.cols + c])),
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }

  Widget _cell(List<SceneItem>? items) {
    return Container(
      margin: const EdgeInsets.all(3),
      decoration: BoxDecoration(
        color: items == null ? const Color(0xFFFFF3E0) : const Color(0xFFF7F8FC),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: items == null ? AppColors.gentle : const Color(0xFFE3E6F0),
          width: items == null ? 2.5 : 1,
        ),
      ),
      child: items == null
          ? (grid.showQuestionMark
              ? const Center(
                  child: FittedBox(
                    child: Text('?', style: TextStyle(fontSize: 40, fontWeight: FontWeight.w900, color: AppColors.gentle)),
                  ),
                )
              : const SizedBox.shrink())
          : LayoutBuilder(
              builder: (context, c) => SceneView(
                scene: SceneVisual(items, aspect: c.maxWidth / (c.maxHeight == 0 ? 1 : c.maxHeight)),
              ),
            ),
    );
  }
}
