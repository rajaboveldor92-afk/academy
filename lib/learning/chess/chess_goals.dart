import '../models/exercise.dart';
import 'chess_rules.dart';

/// Shaxmat topshirig'ini tekshirish: qaysi bosish yoki yurish to'g'ri.
/// Bola doimo oq figuralar bilan o'ynaydi.
class ChessGoals {
  ChessGoals._();

  static ChessPosition initial(ChessTask t) =>
      t.goal == 'play' ? ChessMiniGame.start(t.game ?? 'pawn_war') : ChessPosition(t.size, t.pieces);

  static bool tapCorrect(ChessTask t, int sq) {
    final pos = ChessPosition(t.size, t.pieces);
    switch (t.goal) {
      case 'tap_light':
        return pos.isLight(sq);
      case 'tap_dark':
        return !pos.isLight(sq);
      case 'tap_star':
        return t.stars.contains(sq);
      case 'tap_square':
        return sq == t.target;
      case 'tap_piece':
        final p = t.pieces[sq];
        return p != null && p[1] == t.pieceType;
      default:
        return false;
    }
  }

  /// To'g'ri bosiladigan kataklar (tekshiruv va yordam uchun).
  static List<int> tapTargets(ChessTask t) => [
        for (var sq = 0; sq < t.size * t.size; sq++)
          if (tapCorrect(t, sq)) sq,
      ];

  /// Qonuniy [m] yurish topshiriq bo'yicha to'g'rimi.
  static bool moveCorrect(ChessTask t, ChessPosition before, ChessMove m) {
    final after = ChessRules.apply(before, m);
    switch (t.goal) {
      case 'move_star':
        return t.stars.contains(m.to);
      case 'collect':
      case 'escape':
        return true;
      case 'capture':
        return m.isCapture && (t.target == null || m.to == t.target);
      case 'safe_capture':
        return m.isCapture && !ChessRules.isAttacked(after, m.to, 'b');
      case 'check':
        return ChessRules.inCheck(after, 'b');
      case 'defend':
        final target = t.target!;
        final sq = m.from == target ? m.to : target;
        return !ChessRules.isAttacked(after, sq, 'b');
      case 'mate':
        return ChessRules.isMate(after, 'b');
      default:
        return false;
    }
  }

  /// Birinchi yurishdagi barcha to'g'ri yechimlar.
  static List<ChessMove> solutions(ChessTask t) {
    if (t.isTap || t.goal == 'play') return const [];
    final pos = initial(t);
    return ChessRules.legalMoves(pos, 'w').where((m) => moveCorrect(t, pos, m)).toList();
  }

  /// Topshiriq yechiladigan va ma'noli ekanini tekshiradi.
  static bool isPlayable(ChessTask t) {
    if (t.size < 3 || t.size > 8) return false;
    if (t.isTap) return tapTargets(t).isNotEmpty;
    if (t.goal == 'play') return t.game != null && ChessRules.legalMoves(initial(t), 'w').isNotEmpty;
    final pos = initial(t);
    if (!ChessRules.isSane(pos)) return false;
    if (t.goal == 'collect') {
      return t.stars.isNotEmpty && ChessRules.legalMoves(pos, 'w').isNotEmpty;
    }
    return solutions(t).isNotEmpty;
  }
}
