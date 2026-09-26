import 'dart:math';

import '../models/exercise.dart';

/// Labirint, sudoku va kodlash topshiriqlarini yaratuvchi algoritmlar.
/// Hammasi yechimi borligi kafolatlangan holda yaratiladi.
class PuzzleFactory {
  PuzzleFactory._();

  static const _dirs = [MazeTask.top, MazeTask.right, MazeTask.bottom, MazeTask.left];

  static int _opposite(int d) => switch (d) {
        MazeTask.top => MazeTask.bottom,
        MazeTask.bottom => MazeTask.top,
        MazeTask.left => MazeTask.right,
        _ => MazeTask.left,
      };

  /// "Rekursiv orqaga qaytish" algoritmi bilan mukammal labirint
  /// (har ikki katak orasida aynan bitta yo'l). [extraOpenings] — qo'shimcha
  /// ochiq devorlar (kichik yosh uchun osonroq, bir nechta yo'l).
  static MazeTask maze({
    required Random rng,
    required int rows,
    required int cols,
    required String hero,
    required String target,
    int extraOpenings = 0,
  }) {
    final n = rows * cols;
    final walls = List<int>.filled(n, 15);
    final visited = List<bool>.filled(n, false);
    final stack = <int>[0];
    visited[0] = true;
    int? neighborOf(int cell, int d) {
      final r = cell ~/ cols, c = cell % cols;
      switch (d) {
        case MazeTask.top:
          return r > 0 ? cell - cols : null;
        case MazeTask.bottom:
          return r < rows - 1 ? cell + cols : null;
        case MazeTask.left:
          return c > 0 ? cell - 1 : null;
        case MazeTask.right:
          return c < cols - 1 ? cell + 1 : null;
      }
      return null;
    }

    while (stack.isNotEmpty) {
      final cell = stack.last;
      final options = <int>[
        for (final d in _dirs)
          if (neighborOf(cell, d) != null && !visited[neighborOf(cell, d)!]) d,
      ];
      if (options.isEmpty) {
        stack.removeLast();
        continue;
      }
      final d = options[rng.nextInt(options.length)];
      final next = neighborOf(cell, d)!;
      walls[cell] &= ~d;
      walls[next] &= ~_opposite(d);
      visited[next] = true;
      stack.add(next);
    }
    for (var i = 0; i < extraOpenings; i++) {
      final cell = rng.nextInt(n);
      final d = _dirs[rng.nextInt(4)];
      final next = neighborOf(cell, d);
      if (next == null) continue;
      walls[cell] &= ~d;
      walls[next] &= ~_opposite(d);
    }
    // Start — chap yuqori burchak, maqsad — o'ng pastki (yoki tasodifiy chekka).
    const start = 0;
    final goal = n - 1;
    return MazeTask(
      rows: rows,
      cols: cols,
      walls: walls,
      start: start,
      goal: goal,
      hero: hero,
      target: target,
    );
  }

  /// Lotin kvadrati asosida sudoku. size=4 da 2×2 bloklar ham to'g'ri bo'ladi.
  static SudokuTask sudoku({
    required Random rng,
    required int size,
    required int blanks,
    required List<String> symbols,
  }) {
    List<int> base;
    if (size == 4) {
      // 2×2 bloklarga mos asosiy yechim.
      base = [0, 1, 2, 3, 2, 3, 0, 1, 1, 0, 3, 2, 3, 2, 1, 0];
    } else {
      base = [for (var r = 0; r < size; r++) for (var c = 0; c < size; c++) (r + c) % size];
    }
    // Belgilarni almashtirish.
    final perm = List<int>.generate(size, (i) => i)..shuffle(rng);
    var grid = [for (final v in base) perm[v]];
    // Qatorlarni blok ichida va bloklarni almashtirish (4×4 uchun), yoki oddiy almashtirish.
    if (size == 4) {
      List<int> swapRows(List<int> g, int a, int b) {
        final res = List<int>.from(g);
        for (var c = 0; c < 4; c++) {
          res[a * 4 + c] = g[b * 4 + c];
          res[b * 4 + c] = g[a * 4 + c];
        }
        return res;
      }

      List<int> swapCols(List<int> g, int a, int b) {
        final res = List<int>.from(g);
        for (var r = 0; r < 4; r++) {
          res[r * 4 + a] = g[r * 4 + b];
          res[r * 4 + b] = g[r * 4 + a];
        }
        return res;
      }

      if (rng.nextBool()) grid = swapRows(grid, 0, 1);
      if (rng.nextBool()) grid = swapRows(grid, 2, 3);
      if (rng.nextBool()) grid = swapCols(grid, 0, 1);
      if (rng.nextBool()) grid = swapCols(grid, 2, 3);
      if (rng.nextBool()) {
        grid = swapRows(swapRows(grid, 0, 2), 1, 3);
      }
    } else {
      final rowPerm = List<int>.generate(size, (i) => i)..shuffle(rng);
      grid = [for (final r in rowPerm) for (var c = 0; c < size; c++) grid[r * size + c]];
    }
    final givens = List<bool>.filled(size * size, true);
    final cells = List<int>.generate(size * size, (i) => i)..shuffle(rng);
    for (final c in cells.take(blanks)) {
      givens[c] = false;
    }
    return SudokuTask(size: size, solution: grid, givens: givens, symbols: symbols.take(size).toList());
  }

  /// Sudoku yechimi to'g'rimi (qator, ustun, 2×2 blok).
  static bool isValidSudoku(SudokuTask t) {
    final s = t.size;
    for (var i = 0; i < s; i++) {
      final row = {for (var c = 0; c < s; c++) t.solution[i * s + c]};
      final col = {for (var r = 0; r < s; r++) t.solution[r * s + i]};
      if (row.length != s || col.length != s) return false;
    }
    if (s == 4) {
      for (final br in [0, 2]) {
        for (final bc in [0, 2]) {
          final block = {
            for (var r = br; r < br + 2; r++)
              for (var c = bc; c < bc + 2; c++) t.solution[r * 4 + c],
          };
          if (block.length != 4) return false;
        }
      }
    }
    return true;
  }

  /// Kodlash maydoni: robot va maqsad orasida yo'l bor, to'siqlar bilan.
  static ({CodingTask task, List<String> solution}) coding({
    required Random rng,
    required int rows,
    required int cols,
    required int obstacles,
    required String hero,
    required String target,
    required int minSteps,
    required int maxSteps,
  }) {
    for (var attempt = 0; attempt < 500; attempt++) {
      final n = rows * cols;
      final start = rng.nextInt(n);
      final goal = rng.nextInt(n);
      if (start == goal) continue;
      final blocked = <int>{};
      while (blocked.length < obstacles) {
        final b = rng.nextInt(n);
        if (b != start && b != goal) blocked.add(b);
      }
      final path = _shortest(rows, cols, start, goal, blocked);
      if (path == null || path.length < minSteps || path.length > maxSteps) continue;
      return (
        task: CodingTask(
          rows: rows,
          cols: cols,
          start: start,
          goal: goal,
          blocked: blocked,
          hero: hero,
          target: target,
          maxSteps: maxSteps + 2,
        ),
        solution: path,
      );
    }
    // Zaxira: to'siqsiz oddiy maydon.
    const task = CodingTask(rows: 3, cols: 3, start: 0, goal: 8, blocked: {}, hero: '🤖', target: '⭐', maxSteps: 6);
    return (task: task, solution: const ['R', 'R', 'D', 'D']);
  }

  /// Kodlash topshirig'ining eng qisqa yechimi (testlar va maslahat uchun).
  static List<String>? solveCoding(CodingTask t) =>
      _shortest(t.rows, t.cols, t.start, t.goal, t.blocked);

  /// BFS bilan eng qisqa buyruqlar ketma-ketligi.
  static List<String>? _shortest(int rows, int cols, int start, int goal, Set<int> blocked) {
    final prev = <int, (int, String)>{};
    final queue = <int>[start];
    final seen = {start};
    for (var i = 0; i < queue.length; i++) {
      final cell = queue[i];
      if (cell == goal) break;
      final r = cell ~/ cols, c = cell % cols;
      for (final (next, step) in [
        if (r > 0) (cell - cols, 'U'),
        if (r < rows - 1) (cell + cols, 'D'),
        if (c > 0) (cell - 1, 'L'),
        if (c < cols - 1) (cell + 1, 'R'),
      ]) {
        if (blocked.contains(next) || !seen.add(next)) continue;
        prev[next] = (cell, step);
        queue.add(next);
      }
    }
    if (!seen.contains(goal)) return null;
    final steps = <String>[];
    var cur = goal;
    while (cur != start) {
      final (p, s) = prev[cur]!;
      steps.add(s);
      cur = p;
    }
    return steps.reversed.toList();
  }
}
