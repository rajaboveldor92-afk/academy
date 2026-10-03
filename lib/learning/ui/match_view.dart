import 'dart:math';

import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Juftlash: chapdan bittasini, o'ngdan unga mosini bosish.
/// Topilgan juftlar bir xil rangga bo'yaladi va qulflanadi.
class MatchExerciseView extends StatefulWidget {
  const MatchExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<MatchExerciseView> createState() => _MatchExerciseViewState();
}

class _MatchExerciseViewState extends State<MatchExerciseView> {
  static const _pairColors = [
    Color(0xFF4F8EF7), Color(0xFF2DBE72), Color(0xFFEC6AA8), Color(0xFFFF8A3D), Color(0xFF9B6BFF),
  ];

  late final List<int> _rightOrder;
  final Map<int, int> _matched = {}; // chap indeks -> rang indeksi
  int? _selectedLeft;
  int? _selectedRight;
  int? _wrongRight;
  int? _wrongLeft;
  int _mistakes = 0;
  int _shake = 0;

  List<MatchPair> get pairs => widget.exercise.pairs;

  bool get _wrapText => widget.exercise.subject == 'technology' ||
      (widget.exercise.topicId.contains('_g') && pairs.any((p) =>
        (p.left.text ?? '').length > 24 || (p.right.text ?? '').length > 24));

  @override
  void initState() {
    super.initState();
    // O'ng ustun aralashtiriladi (mashq imzosi asosida — qayta chizishda o'zgarmaydi).
    final rng = Random(widget.exercise.signature.hashCode);
    _rightOrder = List<int>.generate(pairs.length, (i) => i)..shuffle(rng);
    var guard = 0;
    while (pairs.length > 1 && guard++ < 10 && [for (var i = 0; i < pairs.length; i++) _rightOrder[i] == i].every((x) => x)) {
      _rightOrder.shuffle(rng);
    }
  }

  void _tapLeft(int i) {
    if (_matched.containsKey(i)) return;
    setState(() {
      _selectedLeft = i;
      _wrongLeft = null;
    });
    if (_selectedRight != null) _check(i, _selectedRight!);
  }

  void _tapRight(int pairIndex) {
    if (_matched.containsKey(pairIndex)) return;
    setState(() {
      _selectedRight = pairIndex;
      _wrongRight = null;
    });
    if (_selectedLeft != null) _check(_selectedLeft!, pairIndex);
  }

  void _check(int left, int right) {
    if (left == right) {
      setState(() {
        _matched[left] = _matched.length % _pairColors.length;
        _selectedLeft = null;
        _selectedRight = null;
      });
      if (_matched.length == pairs.length) widget.callbacks.onSolved(_mistakes);
    } else {
      setState(() {
        _mistakes++;
        _shake++;
        _wrongRight = right;
        _wrongLeft = left;
        _selectedLeft = null;
        _selectedRight = null;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  Widget _cell({
    required ExerciseOption option,
    required bool selected,
    required int? color,
    required bool wrong,
    required VoidCallback onTap,
  }) {
    final card = OptionCard(
      option: option,
      state: color != null ? OptionState.done : (selected ? OptionState.selected : (wrong ? OptionState.wrong : OptionState.idle)),
      onTap: onTap,
      compact: true,
      wrapText: _wrapText,
    );
    return Padding(
      padding: const EdgeInsets.all(5),
      child: Shake(
        trigger: wrong ? _shake : 0,
        child: color == null
            ? card
            : DecoratedBox(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(26),
                  border: Border.all(color: _pairColors[color], width: 5),
                ),
                child: card,
              ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final n = pairs.length;
    final row = Row(
      children: [
        Expanded(
          child: Column(
            children: [
              for (var i = 0; i < n; i++)
                Expanded(
                  child: _cell(
                    option: pairs[i].left,
                    selected: _selectedLeft == i,
                    color: _matched[i],
                    wrong: _wrongLeft == i,
                    onTap: () => _tapLeft(i),
                  ),
                ),
            ],
          ),
        ),
        SizedBox(
          width: 28,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.swap_horiz_rounded, color: AppColors.textSoft.withAlpha(120), size: 28),
            ],
          ),
        ),
        Expanded(
          child: Column(
            children: [
              for (final p in _rightOrder)
                Expanded(
                  child: _cell(
                    option: pairs[p].right,
                    selected: _selectedRight == p,
                    color: _matched[p],
                    wrong: _wrongRight == p,
                    onTap: () => _tapRight(p),
                  ),
                ),
            ],
          ),
        ),
      ],
    );
    if (!_wrapText) return row;
    return LayoutBuilder(builder: (context, constraints) {
      final cellWidth = ((constraints.maxWidth - 28) / 2 - 40).clamp(40.0, double.infinity).toDouble();
      var rowHeight = 130.0;
      for (final pair in pairs) {
        for (final option in [pair.left, pair.right]) {
          final painter = TextPainter(
            text: TextSpan(text: option.text ?? '', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700)),
            textDirection: Directionality.of(context), textScaler: MediaQuery.textScalerOf(context),
          )..layout(maxWidth: cellWidth);
          if (painter.height + 42 > rowHeight) rowHeight = painter.height + 42;
          painter.dispose();
        }
      }
      return SingleChildScrollView(child: SizedBox(height: n * rowHeight, child: row));
    });
  }
}
