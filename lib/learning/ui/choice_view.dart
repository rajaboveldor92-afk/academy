import 'dart:async';

import 'package:flutter/material.dart';

import '../../l10n/tr.dart';
import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'option_card.dart';
import 'visual_view.dart';

/// Tanlash mashqi (+ sudrab qo'yish va xotira rejimlari).
///
/// * Noto'g'ri variant xiralashadi va o'chadi — bola boshqasini sinaydi.
/// * 2 ta xatodan keyin to'g'ri javob sariq ramka bilan yumshoq ko'rsatiladi.
/// * [ExerciseKind.memory]: avval rasm [Exercise.previewSeconds] soniya ko'rsatiladi.
class ChoiceExerciseView extends StatefulWidget {
  const ChoiceExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<ChoiceExerciseView> createState() => _ChoiceExerciseViewState();
}

class _ChoiceExerciseViewState extends State<ChoiceExerciseView> {
  final Set<int> _wrong = {};
  int _mistakes = 0;
  int _shake = 0;
  bool _solved = false;
  bool _previewing = false;
  int _previewLeft = 0;
  Timer? _timer;

  Exercise get e => widget.exercise;

  @override
  void initState() {
    super.initState();
    if (e.kind == ExerciseKind.memory && e.previewVisual != null) {
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

  void _answer(int index) {
    if (_solved || _previewing || _wrong.contains(index)) return;
    if (index == e.correctIndex) {
      setState(() => _solved = true);
      widget.callbacks.onSolved(_mistakes);
    } else {
      setState(() {
        _wrong.add(index);
        _mistakes++;
        _shake++;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  OptionState _stateOf(int i) {
    if (_solved && i == e.correctIndex) return OptionState.correct;
    if (_wrong.contains(i)) return OptionState.wrong;
    if (!_solved && _mistakes >= 2 && i == e.correctIndex) return OptionState.hinted;
    return OptionState.idle;
  }

  @override
  Widget build(BuildContext context) {
    if (_previewing) return _preview();
    final visual = e.visual;
    final textOnly = e.options.every((o) => o.visual == null);
    final longText = textOnly && e.options.any((o) => (o.text ?? '').length > 7);

    return LayoutBuilder(builder: (context, c) {
      final options = _options(c.maxWidth, longText);
      return Column(
        children: [
          if (visual != null)
            Expanded(
              flex: 5,
              child: Center(
                child: VisualView(
                  visual: visual,
                  onSpeak: () => widget.callbacks.onSpeak?.call(e.speech),
                ),
              ),
            ),
          if (e.dragToTarget) ...[
            const SizedBox(height: 8),
            _dropTarget(),
          ],
          const SizedBox(height: 12),
          if (longText) options else Expanded(flex: visual == null ? 6 : 4, child: options),
        ],
      );
    });
  }

  Widget _preview() {
    return Column(
      children: [
        Text(Tr.of(context).lookAndRemember,
            textAlign: TextAlign.center,
            style: Theme.of(context).textTheme.titleLarge?.copyWith(color: AppColors.primary)),
        const SizedBox(height: 8),
        Expanded(child: Center(child: VisualView(visual: e.previewVisual!))),
        Padding(
          padding: const EdgeInsets.all(16),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(8),
            child: LinearProgressIndicator(
              value: e.previewSeconds == 0 ? 0 : _previewLeft / e.previewSeconds,
              minHeight: 10,
              color: AppColors.star,
              backgroundColor: const Color(0xFFFFF3D6),
            ),
          ),
        ),
      ],
    );
  }

  Widget _dropTarget() {
    return DragTarget<int>(
      onAcceptWithDetails: (d) => _answer(d.data),
      builder: (context, candidates, rejected) {
        final hovering = candidates.isNotEmpty;
        final solvedOption = _solved ? e.options[e.correctIndex] : null;
        return AnimatedContainer(
          duration: const Duration(milliseconds: 150),
          width: 120,
          height: 110,
          decoration: BoxDecoration(
            color: hovering ? const Color(0xFFFFF3D6) : Colors.white,
            borderRadius: BorderRadius.circular(24),
            border: Border.all(
              color: _solved ? AppColors.success : AppColors.gentle,
              width: 3,
            ),
          ),
          child: solvedOption != null
              ? OptionCard(option: solvedOption, state: OptionState.correct, compact: true)
              : const Center(
                  child: Text('?', style: TextStyle(fontSize: 48, fontWeight: FontWeight.w900, color: AppColors.gentle)),
                ),
        );
      },
    );
  }

  Widget _options(double width, bool longText) {
    final n = e.options.length;
    if (longText) {
      return Column(
        children: [
          for (var i = 0; i < n; i++)
            Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Shake(
                trigger: _wrong.contains(i) ? _shake : 0,
                child: SizedBox(
                  height: 64,
                  width: double.infinity,
                  child: OptionCard(option: e.options[i], state: _stateOf(i), onTap: () => _answer(i)),
                ),
              ),
            ),
        ],
      );
    }
    final cols = n <= 3 ? n : (width > 560 ? n : 2);
    final rows = (n / cols).ceil();
    return Column(
      children: [
        for (var r = 0; r < rows; r++)
          Expanded(
            child: Row(
              children: [
                for (var c = 0; c < cols; c++)
                  if (r * cols + c < n)
                    Expanded(child: Padding(padding: const EdgeInsets.all(6), child: _optionCell(r * cols + c)))
                  else
                    const Expanded(child: SizedBox.shrink()),
              ],
            ),
          ),
      ],
    );
  }

  Widget _optionCell(int i) {
    final card = Shake(
      trigger: _wrong.contains(i) ? _shake : 0,
      child: OptionCard(option: e.options[i], state: _stateOf(i), onTap: () => _answer(i)),
    );
    if (!e.dragToTarget || _solved || _wrong.contains(i)) return card;
    return LayoutBuilder(
      builder: (context, c) => Draggable<int>(
        data: i,
        feedback: Material(
          color: Colors.transparent,
          child: SizedBox(
            width: c.maxWidth,
            height: c.maxHeight,
            child: OptionCard(option: e.options[i], state: OptionState.selected),
          ),
        ),
        childWhenDragging: Opacity(opacity: 0.3, child: card),
        child: card,
      ),
    );
  }
}

/// Test va tekshiruv uchun: variant matni bo'lsa uni, aks holda rasm tavsifini qaytaradi.
String describeOption(ExerciseOption o) => o.text ?? (o.visual is SceneVisual ? 'scene' : 'visual');
