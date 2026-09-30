import 'dart:async';
import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../l10n/tr.dart';
import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'abacus_view.dart';
import 'option_card.dart';
import 'visual_view.dart';

/// Javobni yozish mashqi (maktab): ekrandagi klaviatura bilan son, kasr yoki o'nli kasr.
///
/// * Noto'g'ri javobda maydon silkinadi va tozalanadi — bola qayta yozadi.
/// * 3 ta xatodan keyin to'g'ri javob ko'rsatiladi va mashq yakunlanadi (keyinroq qayta so'raladi).
/// * Flesh-anzan ([InputTask.flash]): "Boshlash" bosilgach sonlar birin-ketin ko'rsatiladi,
///   so'ng klaviatura ochiladi; xatodan keyin sonlarni yana bir bor ko'rish mumkin.
/// * Abakus ([InputTask.isAbacus]): klaviatura o'rniga soroban — javob munchoqlar bilan qo'yiladi.
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

  // Flesh-anzan: -1 — boshlanmagan; 0..n-1 — ko'rsatilayotgan son; n — tugadi.
  int _flashIndex = -1;
  bool _flashVisible = false;
  Timer? _flashTimer;

  late List<int> _beads = List.filled(task.rods < 1 ? 1 : task.rods, 0);

  InputTask get task => widget.exercise.input!;

  bool get _flashDone => task.flash.isEmpty || _flashIndex >= task.flash.length;

  @override
  void dispose() {
    _timer?.cancel();
    _flashTimer?.cancel();
    super.dispose();
  }

  void _startFlash() {
    _flashTimer?.cancel();
    setState(() {
      _flashIndex = 0;
      _flashVisible = true;
    });
    _scheduleFlash();
  }

  void _scheduleFlash() {
    _flashTimer = Timer(Duration(milliseconds: task.flashMs), () {
      if (!mounted) return;
      setState(() => _flashVisible = false);
      // Qisqa bo'shliq: ketma-ket bir xil sonlar ham ajralib ko'rinadi.
      _flashTimer = Timer(const Duration(milliseconds: 250), () {
        if (!mounted) return;
        setState(() {
          _flashIndex++;
          _flashVisible = _flashIndex < task.flash.length;
        });
        if (_flashIndex < task.flash.length) _scheduleFlash();
      });
    });
  }

  void _setBeads(List<int> digits) {
    if (_solved) return;
    setState(() {
      _beads = digits;
      _value = '${AbacusView.valueOf(digits)}';
    });
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
    if (_solved || _value.isEmpty || !_flashDone) return;
    if (task.isCorrect(_value)) {
      setState(() => _solved = true);
      widget.callbacks.onSolved(_mistakes);
      return;
    }
    setState(() {
      _mistakes++;
      _shake++;
      // Abakusda munchoqlar joyida qoladi — bola xatosini tuzatadi.
      if (!task.isAbacus) _value = '';
    });
    widget.callbacks.onMistake(_mistakes);
    if (_mistakes >= InputExerciseView.maxMistakes) {
      setState(() {
        _revealed = true;
        _solved = true;
        _value = task.answer;
        if (task.isAbacus) _beads = AbacusVisual.digitsOf(int.parse(task.answer), _beads.length);
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
    if (task.isAbacus) return _abacusLayout(t, visual, color);
    return Column(
      children: [
        if (task.flash.isNotEmpty)
          Expanded(flex: 4, child: _flashPanel(t))
        else if (visual != null)
          Expanded(
            flex: 4,
            child: Center(child: VisualView(visual: visual)),
          ),
        const SizedBox(height: 8),
        _shaking(
          Container(
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
        Expanded(flex: visual == null && task.flash.isEmpty ? 6 : 5, child: _keypad()),
        const SizedBox(height: 8),
        _checkButton(t),
      ],
    );
  }

  Widget _checkButton(Tr t) {
    final empty = _value.isEmpty || (task.isAbacus && _value == '0');
    return SizedBox(
      width: double.infinity,
      height: 56,
      child: FilledButton.icon(
        key: const ValueKey('input_check'),
        onPressed: _solved || empty || !_flashDone ? null : _check,
        icon: const Icon(Icons.check_rounded, size: 28),
        label: Text(t.check, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
      ),
    );
  }

  Widget _shaking(Widget child) => TweenAnimationBuilder<double>(
        key: ValueKey(_shake),
        tween: Tween(begin: 1, end: 0),
        duration: const Duration(milliseconds: 400),
        builder: (context, v, child) => Transform.translate(
          offset: Offset(10 * v * math.sin(v * 24), 0),
          child: child,
        ),
        child: child,
      );

  /// Abakus rejimi: savol (rasm) tepada, pastda bola munchoqlarni suradigan soroban.
  Widget _abacusLayout(Tr t, ExerciseVisual? visual, Color color) {
    return Column(
      children: [
        if (visual != null) Expanded(flex: 3, child: Center(child: VisualView(visual: visual))),
        const SizedBox(height: 8),
        Expanded(
          flex: 6,
          child: _shaking(Container(
            key: const ValueKey('input_abacus'),
            padding: const EdgeInsets.all(6),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(24),
              border: Border.all(color: color, width: 3),
            ),
            child: Center(child: AbacusView(digits: _beads, onChanged: _solved ? null : _setBeads)),
          )),
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
        Align(
          alignment: Alignment.centerRight,
          child: TextButton.icon(
            key: const ValueKey('abacus_clear'),
            onPressed: _solved ? null : () => _setBeads(List.filled(_beads.length, 0)),
            icon: const Icon(Icons.refresh_rounded),
            label: Text(t.clear),
          ),
        ),
        _checkButton(t),
      ],
    );
  }

  /// Flesh-anzan: sonlar birin-ketin katta shriftda ko'rsatiladi.
  Widget _flashPanel(Tr t) {
    if (_flashIndex < 0) {
      return Center(
        child: FilledButton.icon(
          key: const ValueKey('flash_start'),
          onPressed: _startFlash,
          style: FilledButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 16)),
          icon: const Icon(Icons.play_arrow_rounded, size: 40),
          label: Text(t.flashStart, style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w900)),
        ),
      );
    }
    if (!_flashDone) {
      return Center(
        child: FittedBox(
          fit: BoxFit.scaleDown,
          child: Text(
            _flashVisible ? task.flash[_flashIndex] : ' ',
            key: const ValueKey('flash_number'),
            style: const TextStyle(fontSize: 120, fontWeight: FontWeight.w900, color: AppColors.primary),
          ),
        ),
      );
    }
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Text('= ?', style: TextStyle(fontSize: 56, fontWeight: FontWeight.w900, color: AppColors.textSoft)),
          if (!_solved && _mistakes > 0)
            TextButton.icon(
              key: const ValueKey('flash_replay'),
              onPressed: _startFlash,
              icon: const Icon(Icons.replay_rounded),
              label: Text(t.flashReplay, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800)),
            ),
        ],
      ),
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
                                  onPressed: _solved || !_flashDone ? null : () => _type(k),
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
