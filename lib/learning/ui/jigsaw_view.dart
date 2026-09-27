import 'dart:math';

import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';
import 'visual_view.dart';

/// Rasmli puzzle: pastdagi aralash bo'laklarni sudrab (yoki bosib, keyin katakni bosib)
/// rasmdagi joyiga qo'yish. Noto'g'ri joyga qo'yilgan bo'lak qaytib keladi.
class JigsawExerciseView extends StatefulWidget {
  const JigsawExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<JigsawExerciseView> createState() => _JigsawExerciseViewState();
}

class _JigsawExerciseViewState extends State<JigsawExerciseView> {
  final Set<int> _placed = {};
  late final List<int> _trayOrder;
  int? _selected;
  int? _wrongPiece;
  int _mistakes = 0;
  int _shake = 0;
  bool _solved = false;

  JigsawTask get task => widget.exercise.jigsaw!;

  @override
  void initState() {
    super.initState();
    // Bo'laklar tartibi mashq kalitidan (takrorlanganda bir xil, lekin aralash).
    final order = [for (var i = 0; i < task.pieces; i++) i];
    order.shuffle(Random(task.describe().hashCode));
    if (task.pieces > 1 && _sorted(order)) order.add(order.removeAt(0));
    _trayOrder = order;
  }

  static bool _sorted(List<int> l) {
    for (var i = 0; i < l.length; i++) {
      if (l[i] != i) return false;
    }
    return true;
  }

  void _place(int piece, int slot) {
    if (_solved || _placed.contains(piece)) return;
    if (piece == slot) {
      setState(() {
        _placed.add(piece);
        _selected = null;
        _wrongPiece = null;
      });
      if (_placed.length == task.pieces) {
        setState(() => _solved = true);
        widget.callbacks.onSolved(_mistakes);
      }
    } else {
      setState(() {
        _mistakes++;
        _shake++;
        _wrongPiece = piece;
        _selected = null;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(builder: (context, c) {
      final w = c.maxWidth.isFinite ? c.maxWidth : 400.0;
      final h = c.maxHeight.isFinite ? c.maxHeight : 600.0;
      final aspect = task.picture.aspect;
      // Rasm maydoni ~ 58% balandlik, qolgani — bo'laklar.
      var boardW = w;
      var boardH = boardW / aspect;
      if (boardH > h * 0.58) {
        boardH = h * 0.58;
        boardW = boardH * aspect;
      }
      final pw = boardW / task.cols, ph = boardH / task.rows;
      return Column(
        children: [
          SizedBox(
            width: boardW,
            height: boardH,
            child: Stack(
              children: [
                // Xira namuna — bola qayerga qo'yishni ko'rsin.
                Positioned.fill(child: Opacity(opacity: 0.18, child: PictureView(picture: task.picture))),
                for (var r = 0; r < task.rows; r++)
                  for (var col = 0; col < task.cols; col++) _slot(r * task.cols + col, pw, ph, boardW, boardH),
              ],
            ),
          ),
          const SizedBox(height: 10),
          Expanded(
            child: SingleChildScrollView(
              child: Wrap(
                alignment: WrapAlignment.center,
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final p in _trayOrder)
                    if (!_placed.contains(p)) _trayPiece(p, _trayScale(pw, ph, w), boardW, boardH),
                ],
              ),
            ),
          ),
        ],
      );
    });
  }

  /// Bo'laklar tokchada biroz kichikroq (ko'p bo'lakli puzzle ham sig'sin).
  double _trayScale(double pw, double ph, double w) {
    final perRow = task.pieces <= 6 ? task.pieces : (task.pieces <= 12 ? 6 : 7);
    final maxW = (w - 8 * perRow) / perRow;
    return min(1.0, maxW / pw);
  }

  Widget _slot(int i, double pw, double ph, double boardW, double boardH) {
    final r = i ~/ task.cols, c = i % task.cols;
    final placed = _placed.contains(i);
    return Positioned(
      left: c * pw,
      top: r * ph,
      width: pw,
      height: ph,
      child: DragTarget<int>(
        onAcceptWithDetails: (d) => _place(d.data, i),
        builder: (context, candidates, _) => GestureDetector(
          key: ValueKey('slot_$i'),
          behavior: HitTestBehavior.opaque,
          onTap: () {
            final s = _selected;
            if (s != null) _place(s, i);
          },
          child: Container(
            decoration: BoxDecoration(
              border: Border.all(
                color: candidates.isNotEmpty ? AppColors.primary : const Color(0x55000000),
                width: candidates.isNotEmpty ? 3 : 1,
              ),
            ),
            child: placed ? _pieceImage(i, pw, ph, boardW, boardH) : null,
          ),
        ),
      ),
    );
  }

  Widget _trayPiece(int i, double scale, double boardW, double boardH) {
    final pw = boardW / task.cols, ph = boardH / task.rows;
    final image = _pieceImage(i, pw, ph, boardW, boardH);
    final selected = _selected == i;
    Widget piece = Container(
      decoration: BoxDecoration(
        border: Border.all(color: selected ? AppColors.primary : Colors.white, width: selected ? 3 : 2),
        boxShadow: const [BoxShadow(color: Color(0x33000000), blurRadius: 4, offset: Offset(0, 2))],
      ),
      child: image,
    );
    piece = SizedBox(width: pw * scale, height: ph * scale, child: FittedBox(child: SizedBox(width: pw, height: ph, child: piece)));
    if (_wrongPiece == i) piece = Shake(trigger: _shake, child: piece);
    return Draggable<int>(
      data: i,
      feedback: Material(color: Colors.transparent, child: Opacity(opacity: 0.9, child: SizedBox(width: pw, height: ph, child: image))),
      childWhenDragging: Opacity(opacity: 0.3, child: piece),
      child: GestureDetector(
        key: ValueKey('piece_$i'),
        onTap: () => setState(() {
          _selected = _selected == i ? null : i;
          _wrongPiece = null;
        }),
        child: piece,
      ),
    );
  }

  /// Rasmning (r, c) bo'lagi: to'liq rasm siljitilib, faqat kerakli qismi ko'rsatiladi.
  Widget _pieceImage(int i, double pw, double ph, double boardW, double boardH) {
    final r = i ~/ task.cols, c = i % task.cols;
    return ClipRect(
      child: OverflowBox(
        alignment: Alignment.topLeft,
        minWidth: boardW,
        maxWidth: boardW,
        minHeight: boardH,
        maxHeight: boardH,
        child: Transform.translate(
          offset: Offset(-c * pw, -r * ph),
          child: SizedBox(width: boardW, height: boardH, child: PictureView(picture: task.picture)),
        ),
      ),
    );
  }
}
