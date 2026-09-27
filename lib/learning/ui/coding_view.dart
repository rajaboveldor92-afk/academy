import 'dart:async';

import 'package:flutter/material.dart';

import '../../l10n/tr.dart';
import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Kodlash: strelkalardan dastur tuzib, robotni ▶ bilan yurgizish.
class CodingExerciseView extends StatefulWidget {
  const CodingExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<CodingExerciseView> createState() => _CodingExerciseViewState();
}

class _CodingExerciseViewState extends State<CodingExerciseView> {
  static const _arrows = {'U': '⬆️', 'D': '⬇️', 'L': '⬅️', 'R': '➡️'};

  final List<String> _program = [];
  late int _robot = task.start;
  bool _running = false;
  bool _done = false;
  int _mistakes = 0;
  int _shake = 0;
  Timer? _timer;

  CodingTask get task => widget.exercise.coding!;

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void _add(String step) {
    if (_running || _done || _program.length >= task.maxSteps) return;
    setState(() => _program.add(step));
  }

  void _run() {
    if (_running || _done || _program.isEmpty) return;
    setState(() {
      _running = true;
      _robot = task.start;
    });
    var i = 0;
    _timer = Timer.periodic(const Duration(milliseconds: 450), (t) {
      if (!mounted) return t.cancel();
      if (i >= _program.length) {
        t.cancel();
        _finish(_robot == task.goal);
        return;
      }
      final next = _step(_robot, _program[i]);
      if (next == null) {
        t.cancel();
        _finish(false);
        return;
      }
      setState(() => _robot = next);
      i++;
    });
  }

  int? _step(int cell, String s) {
    final r = cell ~/ task.cols, c = cell % task.cols;
    int? next;
    switch (s) {
      case 'U':
        next = r > 0 ? cell - task.cols : null;
      case 'D':
        next = r < task.rows - 1 ? cell + task.cols : null;
      case 'L':
        next = c > 0 ? cell - 1 : null;
      case 'R':
        next = c < task.cols - 1 ? cell + 1 : null;
    }
    if (next == null || task.blocked.contains(next)) return null;
    return next;
  }

  void _finish(bool success) {
    setState(() => _running = false);
    if (success) {
      _done = true;
      widget.callbacks.onSolved(_mistakes);
    } else {
      setState(() {
        _mistakes++;
        _shake++;
        _robot = task.start;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: Center(
            child: AspectRatio(
              aspectRatio: task.cols / task.rows,
              child: Shake(
                trigger: _shake,
                child: Container(
                  padding: const EdgeInsets.all(4),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: AppColors.primary.withAlpha(70), width: 2),
                  ),
                  child: Column(
                    children: [
                      for (var r = 0; r < task.rows; r++)
                        Expanded(
                          child: Row(
                            children: [
                              for (var c = 0; c < task.cols; c++) Expanded(child: _cell(r * task.cols + c)),
                            ],
                          ),
                        ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
        const SizedBox(height: 10),
        // Dastur qatori.
        Container(
          height: 58,
          padding: const EdgeInsets.symmetric(horizontal: 10),
          decoration: BoxDecoration(
            color: const Color(0xFFF1F4FF),
            borderRadius: BorderRadius.circular(18),
          ),
          child: Row(
            children: [
              Expanded(
                child: SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Text(
                    _program.isEmpty ? Tr.of(context).tapArrows : _program.map((s) => _arrows[s]).join(' '),
                    style: TextStyle(fontSize: _program.isEmpty ? 18 : 28, color: AppColors.textSoft),
                  ),
                ),
              ),
              IconButton(
                key: const Key('code_undo'),
                onPressed: _running || _program.isEmpty ? null : () => setState(_program.removeLast),
                icon: const Icon(Icons.backspace_rounded),
              ),
            ],
          ),
        ),
        const SizedBox(height: 8),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            for (final s in const ['L', 'U', 'D', 'R'])
              Padding(
                padding: const EdgeInsets.all(4),
                child: SizedBox(
                  width: 60,
                  height: 56,
                  child: FilledButton.tonal(
                    key: Key('code_$s'),
                    style: FilledButton.styleFrom(padding: EdgeInsets.zero, minimumSize: const Size(56, 52)),
                    onPressed: () => _add(s),
                    child: Text(_arrows[s]!, style: const TextStyle(fontSize: 26)),
                  ),
                ),
              ),
            const SizedBox(width: 8),
            SizedBox(
              width: 70,
              height: 56,
              child: FilledButton(
                key: const Key('code_run'),
                style: FilledButton.styleFrom(
                  padding: EdgeInsets.zero,
                  minimumSize: const Size(64, 52),
                  backgroundColor: AppColors.success,
                ),
                onPressed: _running || _program.isEmpty ? null : _run,
                child: const Icon(Icons.play_arrow_rounded, size: 34),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _cell(int i) {
    String? emoji;
    if (i == _robot) {
      emoji = task.hero;
    } else if (i == task.goal) {
      emoji = task.target;
    } else if (task.blocked.contains(i)) {
      emoji = '🧱';
    }
    return Container(
      margin: const EdgeInsets.all(2),
      decoration: BoxDecoration(
        color: i == task.goal ? const Color(0xFFFFF3D6) : const Color(0xFFF7F8FC),
        borderRadius: BorderRadius.circular(10),
      ),
      alignment: Alignment.center,
      child: emoji == null
          ? null
          : LayoutBuilder(builder: (context, c) => Text(emoji!, style: TextStyle(fontSize: c.maxHeight * 0.6))),
    );
  }
}
