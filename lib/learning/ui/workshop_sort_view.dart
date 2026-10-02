import 'package:flutter/material.dart';

import '../models/exercise.dart';
import 'option_card.dart';

/// Full-width text cards keep Technology scenarios legible; tap or drag to a bin.
class WorkshopSortExerciseView extends StatefulWidget {
  const WorkshopSortExerciseView({
    super.key,
    required this.exercise,
    required this.callbacks,
  });
  final Exercise exercise;
  final ExerciseCallbacks callbacks;
  @override
  State<WorkshopSortExerciseView> createState() =>
      _WorkshopSortExerciseViewState();
}

class _WorkshopSortExerciseViewState extends State<WorkshopSortExerciseView> {
  final Set<int> _done = {};
  int? _selected;
  int _mistakes = 0;
  SortTask get task => widget.exercise.sort!;
  void _place(int item, int bin) {
    if (_done.contains(item)) return;
    if (task.itemBins[item] == bin) {
      setState(() {
        _done.add(item);
        _selected = null;
      });
      if (_done.length == task.items.length)
        widget.callbacks.onSolved(_mistakes);
    } else {
      setState(() => _mistakes++);
      widget.callbacks.onMistake(_mistakes);
    }
  }

  @override
  Widget build(BuildContext context) => SingleChildScrollView(
    child: Column(
      children: [
        for (var bin = 0; bin < task.bins.length; bin++)
          DragTarget<int>(
            onAcceptWithDetails: (d) => _place(d.data, bin),
            builder: (ctx, incoming, rejected) => Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: SizedBox(
                width: double.infinity,
                child: FilledButton.tonal(
                  key: ValueKey('workshop_bin_$bin'),
                  onPressed: _selected == null
                      ? null
                      : () => _place(_selected!, bin),
                  child: Padding(
                    padding: const EdgeInsets.all(10),
                    child: Column(
                      children: [
                        Text(
                          task.bins[bin].text!,
                          style: const TextStyle(fontSize: 18),
                        ),
                        for (final i in _done.where(
                          (i) => task.itemBins[i] == bin,
                        ))
                          Text(
                            '✓ ${task.items[i].text}',
                            textAlign: TextAlign.center,
                          ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ),
        for (var i = 0; i < task.items.length; i++)
          if (!_done.contains(i))
            Draggable<int>(
              data: i,
              feedback: Material(
                child: SizedBox(
                  width: 250,
                  child: Padding(
                    padding: const EdgeInsets.all(12),
                    child: Text(
                      task.items[i].text!,
                      style: const TextStyle(fontSize: 18),
                    ),
                  ),
                ),
              ),
              childWhenDragging: const SizedBox(height: 48),
              child: Padding(
                padding: const EdgeInsets.symmetric(vertical: 4),
                child: SizedBox(
                  width: double.infinity,
                  child: OutlinedButton(
                    key: ValueKey('workshop_item_$i'),
                    style: OutlinedButton.styleFrom(
                      backgroundColor: _selected == i
                          ? Colors.blue.shade50
                          : null,
                    ),
                    onPressed: () => setState(() => _selected = i),
                    child: Padding(
                      padding: const EdgeInsets.all(10),
                      child: Text(
                        task.items[i].text!,
                        style: const TextStyle(fontSize: 17),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  ),
                ),
              ),
            ),
      ],
    ),
  );
}
