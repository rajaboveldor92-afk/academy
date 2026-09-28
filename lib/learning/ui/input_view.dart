import 'dart:async';
import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../l10n/tr.dart';
import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';
import 'visual_view.dart';

/// Javobni yozish mashqi (maktab): ekrandagi klaviatura bilan son, kasr yoki o'nli kasr.
///
/// * Noto'g'ri javobda maydon silkinadi va tozalanadi — bola qayta yozadi.
/// * 3 ta xatodan keyin to'g'ri javob ko'rsatiladi va mashq yakunlanadi (keyinroq qayta so'raladi).
class InputExerciseView extends StatefulWidget {
  const InputExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  static const int maxMistakes = 3;
  static const int maxLength = 12;

  @override
  State<InputExerciseView> createState() => _InputExerciseViewState();
}

class _InputExerciseViewState extends State<InputExerciseView> {
  String _value = '';
  int _mistakes = 0;
  int _shake = 0;
  bool _solved = false;
  bool _revealed = false;
  Timer? _timer;

  InputTask get task => widget.exercise.input!;

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  List<String> get _extraKeys => switch (task.keys) {
        'fraction' => const ['/'],
        'decimal' => const [','],
        'signed' => const ['−'],
        'fraction_decimal' => const ['/', ','],
        _ => const [],
      };

  void _type(String key) {
    if (_solved) return;
    setState(() {
      if (key == '⌫') {
        if (_value.isNotEmpty) _value = _value.substring(0, _value.length - 1);
      } else if (_value.length < InputExerciseView.maxLength) {
        _value += key;
      }
    });
  }

  void _check() {
    if (_solved || _value.isEmpty) return;
    if (task.isCorrect(_value)) {
      setState(() => _solved = true);
      widget.callbacks.onSolved(_mistakes);
      return;
    }
    setState(() {
      _mistakes++;
      _shake++;
      _value = '';
    });
    widget.callbacks.onMistake(_mistakes);
    if (_mistakes >= InputExerciseView.maxMistakes) {
      setState(() {
        _revealed = true;
        _solved = true;
        _value = task.answer;
      });
      _timer = Timer(const Duration(milliseconds: 1800), () {
        if (mounted) widget.callbacks.onSolved(_mistakes);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final t = Tr.of(context);
    final visual = widget.exercise.visual;
    final color = _revealed ? AppColors.gentle : (_solved ? AppColors.success : AppColors.primary);
    return Column(
      children: [
        if (visual != null)
          Expanded(
            flex: 4,
            child: Center(child: VisualView(visual: visual)),
          ),
        const SizedBox(height: 8),
        TweenAnimationBuilder<double>(
          key: ValueKey(_shake),
          tween: Tween(begin: 1, end: 0),
          duration: const Duration(milliseconds: 400),
          builder: (context, v, child) => Transform.translate(
            offset: Offset(10 * v * math.sin(v * 24), 0),
            child: child,
          ),
          child: Container(
            key: const ValueKey('input_field'),
            width: double.infinity,
            padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: color, width: 3),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Flexible(
                  child: Text(
                    _value.isEmpty ? '?' : _value,
                    key: const ValueKey('input_value'),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 36,
                      fontWeight: FontWeight.w900,
                      color: _value.isEmpty ? AppColors.textSoft : AppColors.text,
                    ),
                  ),
                ),
                if (task.unit.isNotEmpty) ...[
                  const SizedBox(width: 8),
                  Text(task.unit, style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w700, color: AppColors.textSoft)),
                ],
              ],
            ),
          ),
        ),
        if (_revealed)
          Padding(
            padding: const EdgeInsets.only(top: 6),
            child: Text(
              t.correctAnswerIs(task.answer),
              key: const ValueKey('input_revealed'),
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800, color: AppColors.textSoft),
            ),
          ),
        const SizedBox(height: 10),
        Expanded(flex: visual == null ? 6 : 5, child: _keypad()),
        const SizedBox(height: 8),
        SizedBox(
          width: double.infinity,
          height: 56,
          child: FilledButton.icon(
            key: const ValueKey('input_check'),
            onPressed: _solved || _value.isEmpty ? null : _check,
            icon: const Icon(Icons.check_rounded, size: 28),
            label: Text(t.check, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
          ),
        ),
      ],
    );
  }

  Widget _keypad() {
    final extra = _extraKeys;
    final rows = [
      ['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', '9'],
      [extra.isNotEmpty ? extra.first : '', '0', '⌫'],
      if (extra.length > 1) [for (final k in extra.skip(1)) k],
    ];
    return LayoutBuilder(builder: (context, c) {
      final h = ((c.maxHeight - 8 * rows.length) / rows.length).clamp(36.0, 72.0).toDouble();
      // Joy kam bo'lsa klaviatura kichrayadi (toshib ketmaydi).
      return FittedBox(
        fit: BoxFit.scaleDown,
        child: SizedBox(
          width: c.maxWidth,
          child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          for (final row in rows)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Row(
                children: [
                  for (final k in row)
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 4),
                        child: SizedBox(
                          height: h,
                          child: k.isEmpty
                              ? const SizedBox.shrink()
                              : OutlinedButton(
                                  key: ValueKey('key_$k'),
                                  onPressed: _solved ? null : () => _type(k),
                                  style: OutlinedButton.styleFrom(
                                    padding: EdgeInsets.zero,
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                                  ),
                                  child: Text(k, style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w900)),
                                ),
                        ),
                      ),
                    ),
                ],
              ),
            ),
        ],
          ),
        ),
      );
    });
  }
}
