import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';

import '../../l10n/tr.dart';
import '../../theme/app_colors.dart';
import '../chess/chess_goals.dart';
import '../chess/chess_rules.dart';
import '../generators/chess_gen.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Shaxmat doskasi: katakni bosish, figurani sudrab yoki bosib yurish, AI bilan mini-o'yin.
///
/// * Figura tanlanganda boradigan kataklar nuqta bilan ko'rsatiladi.
/// * Noto'g'ri (qoidaga zid) yurishda figura eski joyida qoladi va yumshoq chayqaladi.
/// * Qonuniy, lekin topshiriqqa mos bo'lmagan yurish ham qaytariladi (xato sifatida).
/// * 2 ta xatodan keyin to'g'ri yurish sariq rangda ko'rsatiladi.
class ChessExerciseView extends StatefulWidget {
  const ChessExerciseView({super.key, required this.exercise, required this.callbacks, this.random});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  /// AI uchun tasodif manbai (testlarda aniq natija uchun).
  final Random? random;

  /// AI javobidan oldingi pauza.
  static const Duration aiDelay = Duration(milliseconds: 600);

  /// O'yinda shuncha mag'lubiyatdan keyin mashq yakunlanadi (bola charchab qolmasin).
  static const int maxLosses = 2;

  @override
  State<ChessExerciseView> createState() => _ChessExerciseViewState();
}

class _ChessExerciseViewState extends State<ChessExerciseView> {
  late ChessPosition _pos;
  late Set<int> _stars;
  late final Random _rng = widget.random ?? Random();
  int? _selected;
  List<ChessMove> _targets = const [];
  int _mistakes = 0;
  int _shake = 0;
  bool _solved = false;
  int? _wrongSq;
  int? _goodSq;
  ChessMove? _lastMove;
  bool _aiThinking = false;
  int _losses = 0;
  /// Holat matni (tilga qarab build'da hosil qilinadi).
  String Function(Tr t)? _status;
  Timer? _timer;

  ChessTask get task => widget.exercise.chess!;

  bool get _play => task.goal == 'play';

  @override
  void initState() {
    super.initState();
    _reset();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void _reset() {
    _pos = ChessGoals.initial(task);
    _stars = Set.of(task.stars);
    _selected = null;
    _targets = const [];
    _lastMove = null;
    _aiThinking = false;
    _status = _play ? (Tr t) => t.yourTurn : null;
  }

  // ------------------------------------------------------------ Hodisalar
  void _onTap(int sq) {
    if (_solved || _aiThinking) return;
    if (task.isTap) {
      if (ChessGoals.tapCorrect(task, sq)) {
        setState(() {
          _goodSq = sq;
          _solved = true;
        });
        widget.callbacks.onSolved(_mistakes);
      } else {
        _mistake(sq);
      }
      return;
    }
    final piece = _pos.at(sq);
    final sel = _selected;
    if (sel != null && _targets.any((m) => m.to == sq)) {
      _tryMove(sel, sq);
      return;
    }
    if (piece != null && piece[0] == 'w') {
      _select(sq);
      return;
    }
    if (sel != null) {
      // Figura bu katakka bora olmaydi — joyida qoladi.
      _mistake(sq);
      setState(() {
        _selected = null;
        _targets = const [];
      });
    }
  }

  void _select(int sq) {
    setState(() {
      _selected = sq;
      _targets = ChessRules.movesFrom(_pos, sq);
      _wrongSq = null;
    });
    final p = _pos.at(sq);
    if (p != null) widget.callbacks.onSpeak?.call(ChessGenerators.names[p[1]]!.uz);
  }

  void _onDrop(int from, int to) {
    if (_solved || _aiThinking || from == to) return;
    final m = ChessRules.find(_pos, from, to);
    if (m == null) {
      // Qoidaga zid — figura eski joyiga qaytadi.
      _mistake(to);
      setState(() {
        _selected = null;
        _targets = const [];
      });
      return;
    }
    _tryMove(from, to);
  }

  void _tryMove(int from, int to) {
    final m = ChessRules.find(_pos, from, to);
    if (m == null) {
      _mistake(to);
      return;
    }
    if (_play) {
      _playMove(m);
      return;
    }
    final correct = ChessGoals.moveCorrect(task, _pos, m);
    if (task.goal == 'collect') {
      setState(() {
        _pos = ChessRules.apply(_pos, m);
        _lastMove = m;
        _stars.remove(m.to);
        _selected = null;
        _targets = const [];
      });
      if (_stars.isEmpty) {
        setState(() {
          _solved = true;
          _goodSq = m.to;
        });
        widget.callbacks.onSolved(_mistakes);
      }
      return;
    }
    if (correct) {
      setState(() {
        _pos = ChessRules.apply(_pos, m);
        _lastMove = m;
        _goodSq = m.to;
        _selected = null;
        _targets = const [];
        _solved = true;
      });
      widget.callbacks.onSolved(_mistakes);
    } else {
      // Qonuniy, lekin topshiriqqa mos emas — qaytariladi.
      setState(() {
        _selected = null;
        _targets = const [];
      });
      _mistake(to);
    }
  }

  void _mistake(int sq) {
    setState(() {
      _mistakes++;
      _shake++;
      _wrongSq = sq;
    });
    widget.callbacks.onMistake(_mistakes);
  }

  // ------------------------------------------------------------ Mini-o'yin
  void _playMove(ChessMove m) {
    setState(() {
      _pos = ChessRules.apply(_pos, m);
      _lastMove = m;
      _selected = null;
      _targets = const [];
      _wrongSq = null;
    });
    final w = ChessMiniGame.winner(_pos, m, 'b');
    if (w != null) {
      _finish(w);
      return;
    }
    setState(() {
      _aiThinking = true;
      _status = (t) => t.opponentThinks;
    });
    _timer = Timer(ChessExerciseView.aiDelay, _aiMove);
  }

  void _aiMove() {
    if (!mounted) return;
    final m = ChessAi.choose(_pos, 'b', task.ai ?? 'very_easy', _rng);
    if (m == null) {
      _finish('w');
      return;
    }
    setState(() {
      _pos = ChessRules.apply(_pos, m);
      _lastMove = m;
      _aiThinking = false;
      _status = (t) => t.yourTurn;
    });
    final w = ChessMiniGame.winner(_pos, m, 'w');
    if (w != null) _finish(w);
  }

  void _finish(String winner) {
    if (winner == 'w') {
      setState(() {
        _status = (t) => t.youWon;
        _aiThinking = false;
        _solved = true;
      });
      widget.callbacks.onAchievement?.call('chess_win');
      widget.callbacks.onSolved(_mistakes);
      return;
    }
    _losses++;
    setState(() {
      _mistakes++;
      _shake++;
      _aiThinking = true;
      _status = (t) => t.opponentWon;
    });
    widget.callbacks.onMistake(_mistakes);
    if (_losses >= ChessExerciseView.maxLosses) {
      setState(() {
        _solved = true;
        _aiThinking = false;
      });
      widget.callbacks.onSolved(_mistakes);
      return;
    }
    _timer = Timer(const Duration(milliseconds: 1400), () {
      if (!mounted) return;
      setState(_reset);
    });
  }

  // ------------------------------------------------------------ Yordam
  Set<int> get _hintSquares {
    if (_solved || _mistakes < 2 || _play) return const {};
    if (task.isTap) {
      final t = ChessGoals.tapTargets(task);
      return t.length <= 3 ? t.toSet() : const {};
    }
    if (task.goal == 'collect') return const {};
    final sol = ChessGoals.solutions(task);
    if (sol.isEmpty) return const {};
    return {sol.first.from, sol.first.to};
  }

  // ------------------------------------------------------------ Chizish
  @override
  Widget build(BuildContext context) {
    final hints = _hintSquares;
    return LayoutBuilder(builder: (context, c) {
      final statusH = _status != null || task.goal == 'collect' ? 40.0 : 0.0;
      final labels = task.coords ? 22.0 : 0.0;
      final maxW = c.maxWidth.isFinite ? c.maxWidth : 400.0;
      final maxH = (c.maxHeight.isFinite ? c.maxHeight : 520.0) - statusH;
      final boardSide = max(120.0, min(maxW - labels, maxH - labels));
      final cell = boardSide / task.size;
      return Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Shake(
            trigger: _shake,
            child: SizedBox(
              width: boardSide + labels,
              height: boardSide + labels,
              child: Stack(
                children: [
                  Positioned(
                    left: labels,
                    top: 0,
                    child: Container(
                      key: const ValueKey('chess_board'),
                      width: boardSide,
                      height: boardSide,
                      decoration: BoxDecoration(
                        border: Border.all(color: const Color(0xFF6D4C41), width: 2),
                      ),
                      child: Column(
                        children: [
                          for (var r = 0; r < task.size; r++)
                            Row(
                              children: [
                                for (var col = 0; col < task.size; col++) _square(r * task.size + col, cell - 4 / task.size, hints),
                              ],
                            ),
                        ],
                      ),
                    ),
                  ),
                  if (task.coords) ..._coordLabels(boardSide, cell, labels),
                ],
              ),
            ),
          ),
          if (statusH > 0)
            SizedBox(
              height: statusH,
              child: Center(
                child: Text(
                  task.goal == 'collect' && !_solved ? '⭐ × ${_stars.length}' : (_status?.call(Tr.of(context)) ?? ''),
                  key: const ValueKey('chess_status'),
                  style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800, color: AppColors.text),
                ),
              ),
            ),
        ],
      );
    });
  }

  List<Widget> _coordLabels(double side, double cell, double labels) {
    const style = TextStyle(fontSize: 12, fontWeight: FontWeight.w800, color: AppColors.textSoft);
    return [
      for (var i = 0; i < task.size; i++) ...[
        Positioned(
          left: 0,
          top: i * cell,
          width: labels,
          height: cell,
          child: Center(child: Text('${task.size - i}', style: style)),
        ),
        Positioned(
          left: labels + i * cell,
          top: side,
          width: cell,
          height: labels,
          child: Center(child: Text('abcdefgh'[i], style: style)),
        ),
      ],
    ];
  }

  Widget _square(int sq, double cell, Set<int> hints) {
    final light = _pos.isLight(sq);
    var color = light ? const Color(0xFFF0D9B5) : const Color(0xFFB58863);
    final last = _lastMove;
    if (last != null && (last.from == sq || last.to == sq)) color = Color.lerp(color, const Color(0xFFCDE67A), 0.55)!;
    if (task.highlight.contains(sq) && !_solved) color = Color.lerp(color, const Color(0xFFFF8A65), 0.45)!;
    if (_selected == sq) color = Color.lerp(color, const Color(0xFFFFEB3B), 0.6)!;
    if (_goodSq == sq) color = Color.lerp(color, AppColors.success, 0.55)!;
    if (_wrongSq == sq && !_solved) color = Color.lerp(color, AppColors.gentle, 0.45)!;
    final isTarget = _targets.any((m) => m.to == sq);
    final piece = _pos.at(sq);

    Widget content = Stack(
      alignment: Alignment.center,
      children: [
        if (_stars.contains(sq)) Text('⭐', style: TextStyle(fontSize: cell * 0.55)),
        if (piece != null) _pieceWidget(piece, cell),
        if (isTarget)
          Container(
            width: cell * (piece != null ? 0.9 : 0.28),
            height: cell * (piece != null ? 0.9 : 0.28),
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: piece != null ? null : const Color(0x55000000),
              border: piece != null ? Border.all(color: const Color(0x88000000), width: 3) : null,
            ),
          ),
        if (hints.contains(sq))
          Container(
            decoration: BoxDecoration(border: Border.all(color: AppColors.star, width: 4)),
          ),
      ],
    );

    if (piece != null && piece[0] == 'w' && !task.isTap && !_solved && !_aiThinking) {
      content = Draggable<int>(
        data: sq,
        feedback: Material(color: Colors.transparent, child: SizedBox(width: cell, height: cell, child: Center(child: _pieceWidget(piece, cell * 1.15)))),
        childWhenDragging: Opacity(opacity: 0.35, child: content),
        onDragStarted: () => _select(sq),
        child: content,
      );
    }

    return DragTarget<int>(
      onWillAcceptWithDetails: (_) => !task.isTap,
      onAcceptWithDetails: (d) => _onDrop(d.data, sq),
      builder: (context, candidates, _) => GestureDetector(
        key: ValueKey('sq_$sq'),
        behavior: HitTestBehavior.opaque,
        onTap: () => _onTap(sq),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 150),
          width: cell,
          height: cell,
          color: candidates.isNotEmpty ? Color.lerp(color, Colors.white, 0.35) : color,
          child: content,
        ),
      ),
    );
  }

  Widget _pieceWidget(String piece, double cell) {
    final size = cell * 0.78;
    if (piece[0] == 'w') {
      // Oq figura: oq to'ldirilgan belgi ustiga qora kontur.
      return Stack(
        alignment: Alignment.center,
        children: [
          Text(ChessGenerators.blackGlyph[piece[1]]!, style: TextStyle(fontSize: size, color: Colors.white, height: 1)),
          Text(ChessGenerators.whiteGlyph[piece[1]]!, style: TextStyle(fontSize: size, color: const Color(0xFF212121), height: 1)),
        ],
      );
    }
    return Text(ChessGenerators.blackGlyph[piece[1]]!, style: TextStyle(fontSize: size, color: const Color(0xFF1B1B1B), height: 1));
  }
}
