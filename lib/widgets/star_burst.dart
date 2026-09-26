import 'dart:math' as math;

import 'package:flutter/material.dart';

/// Qisqa "quvonch" animatsiyasi: markazdan yulduzchalar sochilib, so'nib ketadi.
/// Bitta AnimationController va bir nechta Transform — eski telefonlarda ham yengil.
class StarBurst extends StatefulWidget {
  const StarBurst({
    super.key,
    required this.size,
    this.count = 10,
    this.duration = const Duration(milliseconds: 750),
    this.colors = const [Color(0xFFFFC83D), Color(0xFFFF8A3D), Color(0xFFFFE27A)],
  });

  final double size;
  final int count;
  final Duration duration;
  final List<Color> colors;

  @override
  State<StarBurst> createState() => _StarBurstState();
}

class _StarBurstState extends State<StarBurst> with SingleTickerProviderStateMixin {
  late final AnimationController _c = AnimationController(vsync: this, duration: widget.duration)
    ..forward();

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final half = widget.size / 2;
    return IgnorePointer(
      child: SizedBox(
        width: widget.size,
        height: widget.size,
        child: AnimatedBuilder(
          animation: _c,
          builder: (context, _) {
            final t = Curves.easeOutCubic.transform(_c.value);
            final fade = 1 - Curves.easeIn.transform(_c.value);
            return Stack(
              children: [
                for (var i = 0; i < widget.count; i++)
                  () {
                    final angle = (2 * math.pi / widget.count) * i - math.pi / 2;
                    final radius = half * (0.25 + 0.7 * t) * (i.isEven ? 1.0 : 0.8);
                    final starSize = half * (i.isEven ? 0.2 : 0.14) * (0.6 + 0.4 * (1 - t));
                    return Positioned(
                      left: half + math.cos(angle) * radius - starSize / 2,
                      top: half + math.sin(angle) * radius - starSize / 2,
                      child: Opacity(
                        opacity: fade.clamp(0.0, 1.0).toDouble(),
                        child: Transform.rotate(
                          angle: t * math.pi,
                          child: Icon(
                            Icons.star_rounded,
                            size: starSize,
                            color: widget.colors[i % widget.colors.length],
                          ),
                        ),
                      ),
                    );
                  }(),
              ],
            );
          },
        ),
      ),
    );
  }
}
