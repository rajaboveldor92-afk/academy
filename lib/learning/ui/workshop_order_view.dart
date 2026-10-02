import 'package:flutter/material.dart';

import '../models/exercise.dart';
import 'option_card.dart';

/// Process cards use a vertical layout so full steps fit on a phone screen.
class WorkshopOrderExerciseView extends StatefulWidget {
  const WorkshopOrderExerciseView({
    super.key,
    required this.exercise,
    required this.callbacks,
  });
  final Exercise exercise;
  final ExerciseCallbacks callbacks;
  @override
  State<WorkshopOrderExerciseView> createState() =>
      _WorkshopOrderExerciseViewState();
}

class _WorkshopOrderExerciseViewState extends State<WorkshopOrderExerciseView> {
  final List<int> _placed = [];
  int _mistakes = 0;
  int? _wrong;
  AssembleTask get task => widget.exercise.assemble!;
  void _tap(int i) {
    if (_placed.contains(i) || _placed.length == task.answer.length) return;
    if (task.tiles[i] == task.answer[_placed.length]) {
      setState(() {
        _placed.add(i);
        _wrong = null;
      });
      if (_placed.length == task.answer.length)
        widget.callbacks.onSolved(_mistakes);
    } else {
      setState(() {
        _mistakes++;
        _wrong = i;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  @override
  Widget build(BuildContext context) => SingleChildScrollView(
    child: Column(
      children: [
        for (var step = 0; step < task.answer.length; step++)
          ListTile(
            dense: true,
            leading: CircleAvatar(radius: 16, child: Text('${step + 1}')),
            title: Text(
              step < _placed.length ? task.tiles[_placed[step]] : '…',
              style: const TextStyle(fontSize: 17),
            ),
            trailing: step < _placed.length
                ? const Icon(Icons.check_circle, color: Colors.green)
                : null,
          ),
        const Divider(),
        for (var i = 0; i < task.tiles.length; i++)
          if (!_placed.contains(i))
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 4),
              child: SizedBox(
                width: double.infinity,
                child: OutlinedButton(
                  key: ValueKey('workshop_step_$i'),
                  style: OutlinedButton.styleFrom(
                    backgroundColor: _wrong == i ? Colors.orange.shade50 : null,
                    side:
                        _placed.length < task.answer.length &&
                            _mistakes >= 2 &&
                            task.tiles[i] == task.answer[_placed.length]
                        ? const BorderSide(color: Colors.amber, width: 3)
                        : null,
                  ),
                  onPressed: () => _tap(i),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(vertical: 10),
                    child: Text(
                      task.tiles[i],
                      style: const TextStyle(fontSize: 17),
                      textAlign: TextAlign.center,
                    ),
                  ),
                ),
              ),
            ),
      ],
    ),
  );
}
