import 'dart:async';

import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';
import 'visual_view.dart';

/// Bo'laklardan yig'ish: harflardan so'z, bo'g'inlardan so'z, so'zlardan gap.
///
/// * Bola bo'lakni bosadi — to'g'ri bo'lsa navbatdagi katakka tushadi.
/// * Noto'g'ri bo'lak joyida chayqaladi (qo'rqitmasdan), katakka tushmaydi.
/// * 2 ta xatodan keyin navbatdagi to'g'ri bo'lak sariq ramka bilan ko'rsatiladi.
/// * Yig'ib bo'lingach natija ovozda aytiladi.
class AssembleExerciseView extends StatefulWidget {
  const AssembleExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<AssembleExerciseView> createState() => _AssembleExerciseViewState();
}

class _AssembleExerciseViewState extends State<AssembleExerciseView> {
  /// Kataklarga joylangan bo'laklar (tiles indekslari) tartib bilan.
  final List<int> _placed = [];
  int? _wrongTile;
  int _mistakes = 0;
  int _shake = 0;
  bool _solved = false;

  /// Xotira rejimi: avval ketma-ketlik ko'rsatiladi, keyin yashiriladi.
  bool _previewing = false;
  int _previewLeft = 0;
  Timer? _timer;

  AssembleTask get task => widget.exercise.assemble!;

  @override
  void initState() {
    super.initState();
    final e = widget.exercise;
    if (e.previewVisual != null && e.previewSeconds > 0) {
      _previewing = true;
      _previewLeft = e.previewSeconds;
      _timer = Timer.periodic(const Duration(seconds: 1), (t) {
        if (!mounted) return;
        setState(() => _previewLeft--);
        if (_previewLeft <= 0) {
          t.cancel();
          setState(() => _previewing = false);
          widget.callbacks.onSpeak?.call(e.speech);
        }
      });
    }
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  bool get _sentence => task.separator.isNotEmpty;

  /// Barcha bo'laklar bitta-ikkita belgidan iborat (harflar).
  bool get _letters => task.tiles.every((t) => t.length <= 2);

  String? get _expected => _placed.length < task.answer.length ? task.answer[_placed.length] : null;

  void _tap(int i) {
    if (_solved || _placed.contains(i)) return;
    final expected = _expected;
    if (expected == null) return;
    if (task.tiles[i] == expected) {
      setState(() {
        _placed.add(i);
        _wrongTile = null;
      });
      if (_placed.length == task.answer.length) {
        setState(() => _solved = true);
        widget.callbacks.onSpeak?.call(task.result);
        widget.callbacks.onSolved(_mistakes);
      }
    } else {
      setState(() {
        _mistakes++;
        _shake++;
        _wrongTile = i;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  /// 2 ta xatodan keyin — navbatdagi to'g'ri bo'lak.
  int? get _hintTile {
    final expected = _expected;
    if (_solved || _mistakes < 2 || expected == null) return null;
    for (var i = 0; i < task.tiles.length; i++) {
      if (!_placed.contains(i) && task.tiles[i] == expected) return i;
    }
    return null;
  }

  @override
  Widget build(BuildContext context) {
    if (_previewing) {
      return Column(
        children: [
          const Text('Yaxshilab qara va eslab qol!', style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: AppColors.primary)),
          const SizedBox(height: 8),
          Expanded(child: Center(child: VisualView(visual: widget.exercise.previewVisual!))),
          Text('$_previewLeft', key: const ValueKey('preview_left'), style: const TextStyle(fontSize: 40, fontWeight: FontWeight.w900, color: AppColors.textSoft)),
        ],
      );
    }
    final visual = widget.exercise.visual;
    return Column(
      children: [
        if (visual != null)
          Expanded(
            flex: 4,
            child: Center(child: VisualView(visual: visual)),
          ),
        const SizedBox(height: 8),
        _slots(),
        const SizedBox(height: 18),
        Expanded(flex: 3, child: Center(child: SingleChildScrollView(child: _tiles()))),
      ],
    );
  }

  double get _fontSize => _letters ? 34 : (_sentence ? 24 : 28);

  Widget _slots() {
    final n = task.answer.length;
    return Wrap(
      alignment: WrapAlignment.center,
      crossAxisAlignment: WrapCrossAlignment.end,
      spacing: _sentence ? 10 : 6,
      runSpacing: 10,
      children: [
        for (var s = 0; s < n; s++) _slot(s),
        if (_sentence)
          Padding(
            padding: const EdgeInsets.only(bottom: 6),
            child: Text('.', style: TextStyle(fontSize: _fontSize, fontWeight: FontWeight.w900)),
          ),
      ],
    );
  }

  Widget _slot(int s) {
    final filled = s < _placed.length;
    final text = filled ? task.tiles[_placed[s]] : '';
    final active = !_solved && s == _placed.length;
    final minWidth = _letters ? 52.0 : (_sentence ? 64.0 : 72.0);
    return AnimatedContainer(
      key: ValueKey('slot_$s'),
      duration: const Duration(milliseconds: 200),
      constraints: BoxConstraints(minWidth: minWidth, minHeight: 64),
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      decoration: BoxDecoration(
        color: _solved
            ? const Color(0xFFE6F8EE)
            : (filled ? Colors.white : (active ? const Color(0xFFEFF4FF) : const Color(0xFFF4F1EA))),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: _solved ? AppColors.success : (active ? AppColors.primary : const Color(0xFFD9D2C3)),
          width: active ? 3 : 2,
        ),
      ),
      child: Center(
        widthFactor: 1,
        child: Text(
          text,
          style: TextStyle(
            fontSize: _fontSize,
            fontWeight: FontWeight.w900,
            color: _solved ? AppColors.success : AppColors.text,
          ),
        ),
      ),
    );
  }

  Widget _tiles() {
    final hint = _hintTile;
    return Wrap(
      alignment: WrapAlignment.center,
      spacing: 10,
      runSpacing: 10,
      children: [
        for (var i = 0; i < task.tiles.length; i++)
          Shake(
            trigger: _wrongTile == i ? _shake : 0,
            child: _Tile(
              key: ValueKey('tile_$i'),
              text: task.tiles[i],
              used: _placed.contains(i),
              wrong: _wrongTile == i,
              hinted: hint == i,
              fontSize: _fontSize,
              minWidth: _letters ? 60 : 76,
              onTap: () => _tap(i),
            ),
          ),
      ],
    );
  }
}

class _Tile extends StatelessWidget {
  const _Tile({
    super.key,
    required this.text,
    required this.used,
    required this.wrong,
    required this.hinted,
    required this.fontSize,
    required this.minWidth,
    required this.onTap,
  });

  final String text;
  final bool used;
  final bool wrong;
  final bool hinted;
  final double fontSize;
  final double minWidth;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final border = hinted ? AppColors.star : (wrong ? AppColors.gentle : const Color(0xFFE3E6F0));
    final fill = hinted ? const Color(0xFFFFF8E1) : (wrong ? const Color(0xFFFFF1E3) : Colors.white);
    return AnimatedOpacity(
      duration: const Duration(milliseconds: 200),
      opacity: used ? 0.22 : 1,
      child: Material(
        color: fill,
        elevation: used ? 0 : 3,
        shadowColor: const Color(0x33000000),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(18),
          side: BorderSide(color: border, width: hinted || wrong ? 3 : 2),
        ),
        child: InkWell(
          borderRadius: BorderRadius.circular(18),
          onTap: used ? null : onTap,
          child: ConstrainedBox(
            constraints: BoxConstraints(minWidth: minWidth, minHeight: 68),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              child: Center(
                widthFactor: 1,
                child: Text(
                  text,
                  style: TextStyle(fontSize: fontSize, fontWeight: FontWeight.w900, color: AppColors.text),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
