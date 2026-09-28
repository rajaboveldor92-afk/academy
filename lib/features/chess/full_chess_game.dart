import 'dart:math';
import 'package:chess/chess.dart' as rules;

/// Full games keep move history, not just FEN, so repetition survives a restart.
class FullChessGame {
  FullChessGame({this.mode = 'computer', this.difficulty = 0, this.help = true});
  rules.Chess board = rules.Chess();
  String mode;
  int difficulty;
  bool help;
  final List<String> history = [];
  bool get whiteTurn => board.turn == rules.Color.WHITE;
  bool get finished => board.game_over;
  bool get computerTurn => mode == 'computer' && !whiteTurn && !finished;
  List<Map<String, dynamic>> get moves => board.generate_moves().map((m) => fullMove(board, m)).toList();

  bool play(Map<String, dynamic> move) {
    if (finished) return false;
    final legal = moves.where((m) => m['from'] == move['from'] && m['to'] == move['to'] &&
        m['promotion'] == move['promotion']).toList();
    if (legal.isEmpty || !board.move(legal.first)) return false;
    history.add(legal.first['san'] as String);
    return true;
  }

  void undo() {
    if (history.isEmpty) return;
    board.undo(); history.removeLast();
    if (mode == 'computer' && !whiteTurn && history.isNotEmpty) {
      board.undo(); history.removeLast();
    }
  }

  Map<String, dynamic> toMap() => {'mode': mode, 'difficulty': difficulty, 'help': help, 'moves': List.of(history)};
  factory FullChessGame.restore(Map<String, dynamic> data) {
    final g = FullChessGame(mode: data['mode'] == 'local' ? 'local' : 'computer',
        difficulty: (data['difficulty'] is int ? data['difficulty'] as int : 0).clamp(0, 2),
        help: data['help'] != false);
    for (final san in data['moves'] as List? ?? const []) {
      if (san is! String || !g.board.move(san)) throw const FormatException('Invalid chess save');
      g.history.add(san);
    }
    return g;
  }
}

/// Runs in a background isolate; no network or native engine required.
Map<String, dynamic>? chooseFullChessMove(Map<String, dynamic> request) {
  final g = FullChessGame.restore(Map<String, dynamic>.from(request['game'] as Map));
  if (g.finished) return null;
  final board = g.board;
  final root = board.generate_moves();
  final rng = Random(request['seed'] as int?);
  root.shuffle(rng);
  final depth = request['depth'] as int? ?? 2;
  if (depth == 0) return fullMove(board, root.first);
  final clock = Stopwatch()..start();
  var nodes = 0;
  const values = {'p': 100, 'n': 320, 'b': 330, 'r': 500, 'q': 900, 'k': 0};
  int evaluate() {
    var score = 0;
    for (var sq = 0; sq < 128; sq++) {
      if ((sq & 0x88) != 0) continue;
      final p = board.board[sq];
      if (p == null) continue;
      final center = (7 - ((sq & 7) * 2 - 7).abs()) + (7 - ((sq >> 4) * 2 - 7).abs());
      final v = values[p.type.name]! + (p.type.name == 'k' ? 0 : center * 2);
      score += p.color == board.turn ? v : -v;
    }
    return score;
  }
  int search(int left, int alpha, int beta, int ply) {
    nodes++;
    if (board.in_draw) return 0;
    final legal = board.generate_moves();
    if (legal.isEmpty) return board.in_check ? -100000 + ply : 0;
    if (left == 0 || nodes > 30000 || clock.elapsedMilliseconds > 1800) return evaluate();
    legal.sort((a, b) => (b.captured == null ? 0 : 1).compareTo(a.captured == null ? 0 : 1));
    for (final m in legal) {
      board.make_move(m);
      final value = -search(left - 1, -beta, -alpha, ply + 1);
      board.undo_move();
      if (value >= beta) return beta;
      if (value > alpha) alpha = value;
    }
    return alpha;
  }
  var best = root.first;
  // Iterative deepening retains a complete previous search if the time budget expires.
  for (var d = 1; d <= depth; d++) {
    var score = -1000000;
    var candidate = best;
    var complete = true;
    for (final m in root) {
      board.make_move(m);
      final value = -search(d - 1, -1000000, -score, 1);
      board.undo_move();
      if (clock.elapsedMilliseconds > 1800 || nodes > 30000) { complete = false; break; }
      if (value > score) { score = value; candidate = m; }
    }
    if (complete) best = candidate;
    if (!complete) break;
  }
  return fullMove(board, best);
}

Map<String, dynamic> fullMove(rules.Chess board, rules.Move move) => {
  'from': move.fromAlgebraic, 'to': move.toAlgebraic,
  'promotion': move.promotion?.name, 'san': board.move_to_san(move),
};
