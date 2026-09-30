import 'package:flutter/material.dart';

/// Abakus (soroban). Har bir ustun raqami = yuqori munchoq (to'singa tushgan bo'lsa — 5) +
/// to'singa ko'tarilgan pastki munchoqlar (har biri 1).
///
/// [onChanged] berilsa, munchoqni bosib son qo'yiladi (yuqori munchoq — 5 ni qo'shadi/olib tashlaydi;
/// pastki munchoq — o'sha munchoqqacha hammasi ko'tariladi yoki tushiriladi).
class AbacusView extends StatelessWidget {
  const AbacusView({super.key, required this.digits, this.onChanged});

  final List<int> digits;
  final ValueChanged<List<int>>? onChanged;

  static const Color frame = Color(0xFF8D6E63);
  static const Color rodColor = Color(0xFFBCAAA4);
  static const Color beadOn = Color(0xFFFF8A3D);
  static const Color beadOff = Color(0xFFEFE3DC);
  static const Color board = Color(0xFFFFF8E1);

  /// Eni / bo'yi nisbati (ustunlar soniga qarab).
  static double aspectFor(int rods) => (rods * 0.36 + 0.14).clamp(0.5, 3.2).toDouble();

  static int valueOf(List<int> digits) => digits.fold(0, (v, d) => v * 10 + d);

  void _tapUpper(int rod) {
    final d = digits[rod];
    _set(rod, d >= 5 ? d - 5 : d + 5);
  }

  void _tapLower(int rod, int bead) {
    final d = digits[rod];
    final lower = d % 5;
    _set(rod, (d >= 5 ? 5 : 0) + (bead < lower ? bead : bead + 1));
  }

  void _set(int rod, int digit) {
    final next = List<int>.from(digits);
    next[rod] = digit;
    onChanged?.call(next);
  }

  @override
  Widget build(BuildContext context) {
    final rods = digits.length;
    return AspectRatio(
      aspectRatio: aspectFor(rods),
      child: LayoutBuilder(builder: (context, outer) {
        final border = (outer.maxHeight * 0.045).clamp(3.0, 14.0).toDouble();
        return Container(
          decoration: BoxDecoration(
            color: board,
            borderRadius: BorderRadius.circular(border * 1.6),
            border: Border.all(color: frame, width: border),
          ),
          padding: EdgeInsets.symmetric(horizontal: border * 0.4, vertical: border * 0.3),
          child: LayoutBuilder(builder: (context, c) {
            final w = c.maxWidth, h = c.maxHeight;
            final rodW = w / rods;
            final bh = h * 0.13;
            final bw = (rodW * 0.86).clamp(0.0, bh * 2.3).toDouble();
            final beamTop = h * 0.30;
            final beamH = h * 0.045;
            final children = <Widget>[];
            for (var r = 0; r < rods; r++) {
              final cx = r * rodW + rodW / 2;
              children.add(Positioned(
                left: cx - 1.5,
                top: 0,
                bottom: 0,
                width: 3,
                child: const ColoredBox(color: rodColor),
              ));
            }
            children.add(Positioned(
              left: 0,
              right: 0,
              top: beamTop,
              height: beamH,
              child: const ColoredBox(color: frame),
            ));
            for (var r = 0; r < rods; r++) {
              // Birlar, minglar ... ustunida to'sinda nuqta (sonni o'qishga yordam beradi).
              if ((rods - 1 - r) % 3 == 0) {
                final cx = r * rodW + rodW / 2;
                children.add(Positioned(
                  left: cx - beamH * 0.3,
                  top: beamTop + beamH * 0.2,
                  width: beamH * 0.6,
                  height: beamH * 0.6,
                  child: const DecoratedBox(decoration: BoxDecoration(color: Colors.white, shape: BoxShape.circle)),
                ));
              }
            }
            for (var r = 0; r < rods; r++) {
              final d = digits[r].clamp(0, 9);
              final left = r * rodW + (rodW - bw) / 2;
              final upperOn = d >= 5;
              children.add(_bead(
                key: ValueKey('bead_${r}_u'),
                left: left,
                top: upperOn ? beamTop - bh : 0,
                width: bw,
                height: bh,
                active: upperOn,
                onTap: onChanged == null ? null : () => _tapUpper(r),
              ));
              for (var i = 0; i < 4; i++) {
                final on = i < d % 5;
                children.add(_bead(
                  key: ValueKey('bead_${r}_$i'),
                  left: left,
                  top: on ? beamTop + beamH + i * bh : h - (4 - i) * bh,
                  width: bw,
                  height: bh,
                  active: on,
                  onTap: onChanged == null ? null : () => _tapLower(r, i),
                ));
              }
            }
            return Stack(clipBehavior: Clip.none, children: children);
          }),
        );
      }),
    );
  }

  Widget _bead({
    required Key key,
    required double left,
    required double top,
    required double width,
    required double height,
    required bool active,
    VoidCallback? onTap,
  }) {
    final color = active ? beadOn : beadOff;
    final bead = Padding(
      padding: EdgeInsets.symmetric(vertical: height * 0.04),
      child: DecoratedBox(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.all(Radius.elliptical(width / 2, height / 2)),
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Color.lerp(color, Colors.white, 0.35)!, color, Color.lerp(color, Colors.black, 0.18)!],
          ),
          border: Border.all(color: Color.lerp(color, Colors.black, 0.3)!, width: 1.2),
        ),
      ),
    );
    return AnimatedPositioned(
      key: key,
      duration: const Duration(milliseconds: 160),
      curve: Curves.easeOut,
      left: left,
      top: top,
      width: width,
      height: height,
      child: onTap == null ? bead : GestureDetector(behavior: HitTestBehavior.opaque, onTap: onTap, child: bead),
    );
  }
}
