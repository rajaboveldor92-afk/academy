import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Belgini chizish: `color:red` — rangli doira, aks holda matn/emoji.
Widget sudokuSymbol(String symbol, double size) {
  if (symbol.startsWith('color:')) {
    const colors = {
      'red': Color(0xFFE53935),
      'yellow': Color(0xFFFDD835),
      'green': Color(0xFF43A047),
      'blue': Color(0xFF1E88E5),
      'orange': Color(0xFFFB8C00),
      'purple': Color(0xFF8E24AA),
      'pink': Color(0xFFEC407A),
      'brown': Color(0xFF795548),
    };
    return Container(
      width: size * 0.62,
      height: size * 0.62,
      decoration: BoxDecoration(color: colors[symbol.substring(6)] ?? Colors.grey, shape: BoxShape.circle),
    );
  }
  return Text(symbol, style: TextStyle(fontSize: size * 0.55, fontWeight: FontWeight.w900, height: 1));
}

/// Mini-sudoku: bo'sh katakni tanlab, pastdagi belgini bosish.
class SudokuExerciseView extends StatefulWidget {
  const SudokuExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<SudokuExerciseView> createState() => _SudokuExerciseViewState();
}

class _SudokuExerciseViewState extends State<SudokuExerciseView> {
  late final List<int?> _values = [
    for (var i = 0; i < task.solution.length; i++) task.givens[i] ? task.solution[i] : null,
  ];
  int? _selected;
  int? _wrongCell;
  int _mistakes = 0;
  int _shake = 0;
  bool _done = false;

  SudokuTask get task => widget.exercise.sudoku!;

  @override
  void initState() {
    super.initState();
    _selected = _values.indexWhere((v) => v == null);
  }

  void _put(int symbol) {
    final cell = _selected;
    if (cell == null || _done || _values[cell] != null) return;
    if (task.solution[cell] == symbol) {
      setState(() {
        _values[cell] = symbol;
        _wrongCell = null;
        final next = _values.indexWhere((v) => v == null);
        _selected = next < 0 ? null : next;
      });
      if (_values.every((v) => v != null)) {
        _done = true;
        widget.callbacks.onSolved(_mistakes);
      }
    } else {
      setState(() {
        _mistakes++;
        _shake++;
        _wrongCell = cell;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  @override
  Widget build(BuildContext context) {
    final s = task.size;
    return Column(
      children: [
        Expanded(
          child: Center(
            child: AspectRatio(
              aspectRatio: 1,
              child: LayoutBuilder(builder: (context, c) {
                final cell = c.maxWidth / s;
                return Container(
                  decoration: BoxDecoration(
                    border: Border.all(color: AppColors.text, width: 3),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Column(
                    children: [
                      for (var r = 0; r < s; r++)
                        Expanded(
                          child: Row(
                            children: [
                              for (var col = 0; col < s; col++) Expanded(child: _cell(r * s + col, cell, r, col)),
                            ],
                          ),
                        ),
                    ],
                  ),
                );
              }),
            ),
          ),
        ),
        const SizedBox(height: 12),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            for (var i = 0; i < task.symbols.length; i++)
              Padding(
                padding: const EdgeInsets.all(5),
                child: SizedBox(
                  width: 70,
                  height: 70,
                  child: Material(
                    color: Colors.white,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(18),
                      side: const BorderSide(color: Color(0xFFE3E6F0), width: 2),
                    ),
                    child: InkWell(
                      key: Key('sudoku_symbol_$i'),
                      borderRadius: BorderRadius.circular(18),
                      onTap: () => _put(i),
                      child: Center(child: sudokuSymbol(task.symbols[i], 70)),
                    ),
                  ),
                ),
              ),
          ],
        ),
      ],
    );
  }

  Widget _cell(int i, double size, int r, int c) {
    final v = _values[i];
    final given = task.givens[i];
    final selected = _selected == i;
    final s = task.size;
    final thickRight = s == 4 && c == 1;
    final thickBottom = s == 4 && r == 1;
    return GestureDetector(
      onTap: v == null ? () => setState(() => _selected = i) : null,
      child: Shake(
        trigger: _wrongCell == i ? _shake : 0,
        child: Container(
          decoration: BoxDecoration(
            color: selected
                ? const Color(0xFFE8EEFF)
                : (_wrongCell == i ? const Color(0xFFFFF1E3) : (given ? const Color(0xFFF3F4F8) : Colors.white)),
            border: Border(
              right: BorderSide(color: AppColors.text.withAlpha(thickRight ? 255 : 60), width: thickRight ? 3 : 1),
              bottom: BorderSide(color: AppColors.text.withAlpha(thickBottom ? 255 : 60), width: thickBottom ? 3 : 1),
            ),
          ),
          alignment: Alignment.center,
          child: v == null
              ? (selected ? Icon(Icons.touch_app_rounded, color: AppColors.primary.withAlpha(120), size: size * 0.4) : null)
              : sudokuSymbol(task.symbols[v], size),
        ),
      ),
    );
  }
}
