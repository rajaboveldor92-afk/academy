import 'dart:math';

/// Shaxmat qoidalari (bolalar mashqlari uchun): n×n doska, figuralar yurishi, olish,
/// shax, mat, piyodaning vazirga aylanishi. Rokirovka va "o'tib olish" yo'q — mashqlarda
/// kerak emas. Toza Dart: testlarda ham ishlaydi.
///
/// Katak raqami: `qator * size + ustun`, 0-qator — yuqorida (oqlar pastdan yuqoriga yuradi).
/// Figura kodi: rang (`w`/`b`) + tur (`K` shoh, `Q` vazir, `R` rux, `B` fil, `N` ot, `P` piyoda).
class ChessMove {
  const ChessMove(this.from, this.to, {required this.piece, this.captured, this.promotion = false});

  final int from;
  final int to;
  final String piece;
  final String? captured;
  final bool promotion;

  bool get isCapture => captured != null;

  @override
  bool operator ==(Object other) => other is ChessMove && other.from == from && other.to == to;

  @override
  int get hashCode => from * 1000 + to;

  @override
  String toString() => '$piece:$from-$to${captured != null ? 'x$captured' : ''}${promotion ? '=Q' : ''}';
}

class ChessPosition {
  ChessPosition(this.size, Map<int, String> pieces) : board = Map.of(pieces);

  final int size;
  final Map<int, String> board;

  int row(int sq) => sq ~/ size;
  int col(int sq) => sq % size;
  bool inside(int r, int c) => r >= 0 && r < size && c >= 0 && c < size;
  String? at(int sq) => board[sq];

  /// Katak rangi: yuqori chap burchak (a8) — oq.
  bool isLight(int sq) => (row(sq) + col(sq)).isEven;

  /// Katak nomi: `e4` (ustun harfi + qator raqami, pastdan sanaladi).
  String name(int sq) => '${'abcdefgh'[col(sq)]}${size - row(sq)}';

  int? square(String name) {
    if (name.length < 2) return null;
    final c = 'abcdefgh'.indexOf(name[0]);
    final r = size - int.parse(name.substring(1));
    return inside(r, c) ? r * size + c : null;
  }

  ChessPosition copy() => ChessPosition(size, board);

  /// Takrorlanmaslik kaliti.
  String describe() {
    final keys = board.keys.toList()..sort();
    return '$size:${keys.map((k) => '$k${board[k]}').join(',')}';
  }
}

class ChessRules {
  ChessRules._();

  static const List<(int, int)> _knight = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)];
  static const List<(int, int)> _king = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
  static const List<(int, int)> _rook = [(-1, 0), (1, 0), (0, -1), (0, 1)];
  static const List<(int, int)> _bishop = [(-1, -1), (-1, 1), (1, -1), (1, 1)];

  /// Figura qiymati (AI va tekshiruvlar uchun).
  static const Map<String, int> value = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 100};

  static String opponent(String color) => color == 'w' ? 'b' : 'w';

  /// [sq] dagi figura hujum qiladigan kataklar (piyoda — faqat qiyshiq kataklar).
  static List<int> attacks(ChessPosition pos, int sq) {
    final p = pos.board[sq];
    if (p == null) return const [];
    final color = p[0], type = p[1];
    final r = pos.row(sq), c = pos.col(sq), n = pos.size;
    final out = <int>[];
    if (type == 'P') {
      final dr = color == 'w' ? -1 : 1;
      for (final dc in const [-1, 1]) {
        if (pos.inside(r + dr, c + dc)) out.add((r + dr) * n + c + dc);
      }
      return out;
    }
    if (type == 'N' || type == 'K') {
      for (final (dr, dc) in type == 'N' ? _knight : _king) {
        if (pos.inside(r + dr, c + dc)) out.add((r + dr) * n + c + dc);
      }
      return out;
    }
    final dirs = type == 'R' ? _rook : (type == 'B' ? _bishop : [..._rook, ..._bishop]);
    for (final (dr, dc) in dirs) {
      var rr = r + dr, cc = c + dc;
      while (pos.inside(rr, cc)) {
        final t = rr * n + cc;
        out.add(t);
        if (pos.board.containsKey(t)) break;
        rr += dr;
        cc += dc;
      }
    }
    return out;
  }

  static bool _promotes(ChessPosition pos, String piece, int to) =>
      piece[1] == 'P' && ((piece[0] == 'w' && pos.row(to) == 0) || (piece[0] == 'b' && pos.row(to) == pos.size - 1));

  /// Shoh xavfsizligini hisobga olmagan yurishlar.
  static List<ChessMove> pseudoMoves(ChessPosition pos, String color) {
    final n = pos.size;
    final moves = <ChessMove>[];
    for (final e in pos.board.entries.toList()) {
      final sq = e.key, p = e.value;
      if (p[0] != color) continue;
      if (p[1] == 'P') {
        final r = pos.row(sq), c = pos.col(sq);
        final dr = color == 'w' ? -1 : 1;
        if (pos.inside(r + dr, c)) {
          final one = (r + dr) * n + c;
          if (!pos.board.containsKey(one)) {
            moves.add(ChessMove(sq, one, piece: p, promotion: _promotes(pos, p, one)));
            // Standart doskada birinchi yurishda ikki katak.
            final start = color == 'w' ? n - 2 : 1;
            final two = (r + 2 * dr) * n + c;
            if (n == 8 && r == start && !pos.board.containsKey(two)) moves.add(ChessMove(sq, two, piece: p));
          }
        }
        for (final dc in const [-1, 1]) {
          if (!pos.inside(r + dr, c + dc)) continue;
          final t = (r + dr) * n + c + dc;
          final target = pos.board[t];
          if (target != null && target[0] != color) {
            moves.add(ChessMove(sq, t, piece: p, captured: target, promotion: _promotes(pos, p, t)));
          }
        }
        continue;
      }
      for (final t in attacks(pos, sq)) {
        final target = pos.board[t];
        if (target != null && target[0] == color) continue;
        moves.add(ChessMove(sq, t, piece: p, captured: target));
      }
    }
    return moves;
  }

  static bool isAttacked(ChessPosition pos, int sq, String byColor) {
    for (final e in pos.board.entries) {
      if (e.value[0] == byColor && attacks(pos, e.key).contains(sq)) return true;
    }
    return false;
  }

  static int? kingSquare(ChessPosition pos, String color) {
    for (final e in pos.board.entries) {
      if (e.value == '${color}K') return e.key;
    }
    return null;
  }

  static bool inCheck(ChessPosition pos, String color) {
    final k = kingSquare(pos, color);
    return k != null && isAttacked(pos, k, opponent(color));
  }

  static ChessPosition apply(ChessPosition pos, ChessMove m) {
    final next = pos.copy();
    final p = next.board.remove(m.from)!;
    next.board[m.to] = m.promotion ? '${p[0]}Q' : p;
    return next;
  }

  /// Qonuniy yurishlar: o'z shohini xavf ostida qoldirmaydi (shoh bo'lmasa — hammasi).
  static List<ChessMove> legalMoves(ChessPosition pos, String color) =>
      pseudoMoves(pos, color).where((m) => !inCheck(apply(pos, m), color)).toList();

  static List<ChessMove> movesFrom(ChessPosition pos, int sq) {
    final p = pos.board[sq];
    if (p == null) return const [];
    return legalMoves(pos, p[0]).where((m) => m.from == sq).toList();
  }

  static ChessMove? find(ChessPosition pos, int from, int to) {
    for (final m in movesFrom(pos, from)) {
      if (m.to == to) return m;
    }
    return null;
  }

  static bool isMate(ChessPosition pos, String color) => inCheck(pos, color) && legalMoves(pos, color).isEmpty;

  /// Pozitsiya mashq uchun to'g'rimi: shohlar yonma-yon emas, navbati bo'lmagan tomon shaxda emas,
  /// piyodalar chetki qatorlarda emas.
  static bool isSane(ChessPosition pos, {String toMove = 'w'}) {
    final wk = kingSquare(pos, 'w'), bk = kingSquare(pos, 'b');
    if (wk != null && bk != null) {
      final dr = (pos.row(wk) - pos.row(bk)).abs(), dc = (pos.col(wk) - pos.col(bk)).abs();
      if (max(dr, dc) <= 1) return false;
    }
    if (inCheck(pos, opponent(toMove))) return false;
    for (final e in pos.board.entries) {
      if (e.value[1] == 'P' && (pos.row(e.key) == 0 || pos.row(e.key) == pos.size - 1)) return false;
    }
    return true;
  }
}

/// Juda oson va oson raqib (6 yosh uchun). Kuchli dvigatel ataylab ishlatilmaydi.
class ChessAi {
  ChessAi._();

  static ChessMove? choose(ChessPosition pos, String color, String level, Random rng) {
    final moves = ChessRules.legalMoves(pos, color);
    if (moves.isEmpty) return null;
    if (level == 'very_easy') {
      // Asosan tasodifiy; faqat ba'zan olish yoki vazirga aylanishni tanlaydi.
      final good = moves.where((m) => m.promotion || m.isCapture).toList();
      if (good.isNotEmpty && rng.nextDouble() < 0.35) return good[rng.nextInt(good.length)];
      return moves[rng.nextInt(moves.length)];
    }
    ChessMove? best;
    var bestScore = -1e9;
    for (final m in moves) {
      final score = _score(pos, m, color) + rng.nextDouble() * 0.6;
      if (score > bestScore) {
        bestScore = score;
        best = m;
      }
    }
    return best;
  }

  static double _score(ChessPosition pos, ChessMove m, String color) {
    final after = ChessRules.apply(pos, m);
    var s = 0.0;
    if (m.captured != null) s += ChessRules.value[m.captured![1]]!;
    if (m.promotion) s += 8;
    final moved = after.board[m.to]!;
    // Himoyasiz qolgan figura — yo'qotish.
    if (ChessRules.isAttacked(after, m.to, ChessRules.opponent(color)) && !ChessRules.isAttacked(after, m.to, color)) {
      s -= ChessRules.value[moved[1]]! * 0.9;
    }
    if (moved[1] == 'P') {
      final progress = color == 'w' ? pos.size - 1 - pos.row(m.to) : pos.row(m.to);
      s += progress * 0.15;
    }
    if (ChessRules.inCheck(after, ChessRules.opponent(color))) s += 0.3;
    return s;
  }
}

/// Kichik o'yinlar qoidasi.
class ChessMiniGame {
  ChessMiniGame._();

  /// Boshlang'ich pozitsiya.
  static ChessPosition start(String game) {
    const n = 8;
    final b = <int, String>{};
    switch (game) {
      case 'queen_vs_pawns':
        for (var c = 0; c < 5; c++) {
          b[1 * n + c] = 'bP';
        }
        b[7 * n + 3] = 'wQ';
      case 'rook_vs_pawns':
        for (var c = 0; c < 4; c++) {
          b[1 * n + c] = 'bP';
        }
        b[7 * n + 0] = 'wR';
        b[7 * n + 7] = 'wR';
      default: // pawn_war
        for (var c = 0; c < n; c++) {
          b[6 * n + c] = 'wP';
          b[1 * n + c] = 'bP';
        }
    }
    return ChessPosition(n, b);
  }

  /// G'olib (`w`/`b`) yoki o'yin davom etadi (`null`). [last] — oxirgi yurish, [toMove] — endi kimning navbati.
  static String? winner(ChessPosition pos, ChessMove? last, String toMove) {
    if (last != null && last.promotion) return last.piece[0];
    final whites = pos.board.values.where((p) => p[0] == 'w').length;
    final blacks = pos.board.values.where((p) => p[0] == 'b').length;
    if (blacks == 0) return 'w';
    if (whites == 0) return 'b';
    // Yurish qolmasa — yutqazadi (bolalar uchun sodda qoida).
    if (ChessRules.legalMoves(pos, toMove).isEmpty) return ChessRules.opponent(toMove);
    return null;
  }
}
