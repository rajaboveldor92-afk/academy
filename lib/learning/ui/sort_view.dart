import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Guruhlash: narsani bosib (yoki sudrab) kerakli savatga joylash.
class SortExerciseView extends StatefulWidget {
  const SortExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<SortExerciseView> createState() => _SortExerciseViewState();
}

class _SortExerciseViewState extends State<SortExerciseView> {
  final Set<int> _placed = {};
  int? _selected;
  int? _wrongItem;
  int _mistakes = 0;
  int _shake = 0;

  SortTask get task => widget.exercise.sort!;

  void _place(int item, int bin) {
    if (_placed.contains(item)) return;
    if (task.itemBins[item] == bin) {
      setState(() {
        _placed.add(item);
        _selected = null;
        _wrongItem = null;
      });
      if (_placed.length == task.items.length) widget.callbacks.onSolved(_mistakes);
    } else {
      setState(() {
        _mistakes++;
        _shake++;
        _wrongItem = item;
        _selected = null;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  void _tapBin(int bin) {
    final s = _selected;
    if (s == null) {
      final label = task.bins[bin].speech;
      if (label != null) widget.callbacks.onSpeak?.call(label);
      return;
    }
    _place(s, bin);
  }

  @override
  Widget build(BuildContext context) {
    final remaining = [for (var i = 0; i < task.items.length; i++) if (!_placed.contains(i)) i];
    return LayoutBuilder(builder: (context, c) {
      final itemSize = (c.maxWidth / 4.4).clamp(64.0, 120.0).toDouble();
      return Column(
        children: [
          Expanded(
            flex: 4,
            child: Center(
              child: SingleChildScrollView(
                child: Wrap(
                  alignment: WrapAlignment.center,
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (final i in remaining)
                      SizedBox(width: itemSize, height: itemSize, child: _item(i, itemSize)),
                  ],
                ),
              ),
            ),
          ),
          const SizedBox(height: 8),
          Expanded(
            flex: 5,
            child: Row(
              children: [
                for (var b = 0; b < task.bins.length; b++) Expanded(child: _bin(b)),
              ],
            ),
          ),
        ],
      );
    });
  }

  Widget _item(int i, double size) {
    final card = Shake(
      trigger: _wrongItem == i ? _shake : 0,
      child: OptionCard(
        option: task.items[i],
        state: _selected == i ? OptionState.selected : (_wrongItem == i ? OptionState.wrong : OptionState.idle),
        onTap: () => setState(() {
          _selected = _selected == i ? null : i;
          _wrongItem = null;
        }),
        compact: true,
      ),
    );
    return Draggable<int>(
      data: i,
      feedback: Material(
        color: Colors.transparent,
        child: SizedBox(width: size, height: size, child: OptionCard(option: task.items[i], state: OptionState.selected)),
      ),
      childWhenDragging: Opacity(opacity: 0.3, child: card),
      child: card,
    );
  }

  Widget _bin(int b) {
    final placedHere = [for (final i in _placed) if (task.itemBins[i] == b) i];
    return DragTarget<int>(
      onAcceptWithDetails: (d) => _place(d.data, b),
      builder: (context, candidates, _) {
        final hover = candidates.isNotEmpty || _selected != null;
        return GestureDetector(
          onTap: () => _tapBin(b),
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 150),
            margin: const EdgeInsets.all(6),
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: hover ? const Color(0xFFEFF4FF) : const Color(0xFFF7F3EC),
              borderRadius: BorderRadius.circular(26),
              border: Border.all(color: hover ? AppColors.primary : const Color(0xFFD7CCC8), width: 3),
            ),
            child: Column(
              children: [
                SizedBox(height: 64, child: IgnorePointer(child: OptionCard(option: task.bins[b], compact: true))),
                const SizedBox(height: 6),
                Expanded(
                  child: Wrap(
                    alignment: WrapAlignment.center,
                    spacing: 4,
                    runSpacing: 4,
                    children: [
                      for (final i in placedHere)
                        SizedBox(
                          width: 44,
                          height: 44,
                          child: IgnorePointer(child: OptionCard(option: task.items[i], state: OptionState.done, compact: true)),
                        ),
                    ],
                  ),
                ),
                const Icon(Icons.shopping_basket_rounded, color: Color(0xFFBCAAA4), size: 30),
              ],
            ),
          ),
        );
      },
    );
  }
}
