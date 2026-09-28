import 'package:chess/chess.dart' as rules;
import 'package:academy/features/chess/full_chess_game.dart';
import 'package:academy/database/local_database.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  void san(FullChessGame g, String s) => expect(g.play(g.moves.firstWhere((m) => m['san'] == s)), isTrue);
  test('legal opening, illegal move, save/reload, and paired undo', () {
    final g = FullChessGame();
    expect(g.moves.length, 20);
    expect(g.play({'from':'e2','to':'e5'}), isFalse);
    san(g, 'e4'); san(g, 'e5');
    final restored = FullChessGame.restore(g.toMap());
    expect(restored.board.fen, g.board.fen);
    restored.undo();
    expect(restored.history, isEmpty);
    expect(restored.board.fen, rules.Chess().fen);
  });
  test('castling moves king and rook, and cannot castle through check', () {
    final g = FullChessGame(mode:'local');
    g.board = rules.Chess.fromFEN('r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1');
    san(g, 'O-O');
    expect(g.board.get('g1')?.type.name, 'k');
    expect(g.board.get('f1')?.type.name, 'r');
    g.board = rules.Chess.fromFEN('r3kr1r/8/8/8/8/8/8/R3K2R w KQ - 0 1');
    expect(g.moves.any((m) => m['san'] == 'O-O'), isFalse);
  });
  test('en passant removes captured pawn', () {
    final g = FullChessGame(mode:'local');
    for (final s in ['e4','a6','e5','d5','exd6']) { san(g,s); }
    expect(g.board.get('d5'), isNull);
    expect(g.board.get('d6')?.type.name, 'p');
  });
  test('all four promotion choices work', () {
    for (final p in ['q','r','b','n']) {
      final g = FullChessGame(mode:'local');
      g.board = rules.Chess.fromFEN('7k/P7/8/8/8/8/8/7K w - - 0 1');
      expect(g.moves.where((m) => m['from']=='a7').length, 4);
      expect(g.play({'from':'a7','to':'a8','promotion':p}), isTrue);
      expect(g.board.get('a8')?.type.name, p);
    }
  });
  test('checkmate, stalemate and repetition after restart', () {
    final g = FullChessGame(mode:'local');
    for (final s in ['f3','e5','g4','Qh4#']) { san(g,s); }
    expect(g.board.in_checkmate, isTrue);
    g.board = rules.Chess.fromFEN('7k/5Q2/6K1/8/8/8/8/8 b - - 0 1');
    expect(g.board.in_stalemate, isTrue);
    final r = FullChessGame(mode:'local');
    for (final s in ['Nf3','Nf6','Ng1','Ng8','Nf3','Nf6','Ng1','Ng8']) { san(r,s); }
    expect(FullChessGame.restore(r.toMap()).board.in_threefold_repetition, isTrue);
  });
  test('AI returns legal move for every level and finds mate in one', () {
    final g = FullChessGame();
    for (final d in [0,2,3]) {
      final result = chooseFullChessMove({'game':g.toMap(),'depth':d,'seed':7});
      expect(g.moves.any((m) => m['san']==result?['san']), isTrue);
    }
    for (final s in ['f3','e5','g4']) { san(g,s); }
    final result = chooseFullChessMove({'game':g.toMap(),'depth':2,'seed':7});
    expect(result?['san'], 'Qh4#');
  });
  test('saves stay separate by child and corrupt history is rejected', () async {
    final db = LocalDatabase.memory();
    final g = FullChessGame(); san(g,'e4');
    await db.saveChessGame('azamjon',g.toMap());
    expect(db.getChessGame('muhammadjon'), isNull);
    expect(FullChessGame.restore(db.getChessGame('azamjon')!).history, ['e4']);
    expect(() => FullChessGame.restore({'moves':['invalid']}), throwsFormatException);
  });
}
