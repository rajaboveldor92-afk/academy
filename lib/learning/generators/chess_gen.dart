import '../../models/speech_part.dart';
import '../chess/chess_goals.dart';
import '../chess/chess_rules.dart';
import '../content/instructions.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';

/// ♟ Shaxmat: doska → figuralar (3 tilda) → yurishlar → olish, shax, mat → AI bilan o'yin.
///
/// 4 yosh: kichik doska (5×5), figurani tanish, yulduzchaga yurish.
/// 6 yosh: 8×8 doska, koordinatalar, shax/mat masalalari, juda oson va oson raqib.
/// Masalalar tasodifiy yaratiladi va qoidalar dvigateli bilan tekshiriladi (kamida bitta yechim bor).
class ChessGenerators {
  ChessGenerators._();

  static final Map<String, ExerciseGenerator> generators = {
    'board_tap': boardTap,
    'piece_tap': pieceTap,
    'piece_name': pieceName,
    'move_star': moveStar,
    'collect': collect,
    'puzzle': puzzle,
    'play': play,
  };

  /// Oq figuralar — ichi bo'sh belgilar, qora — to'la belgilar.
  static const Map<String, String> whiteGlyph = {'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙'};
  static const Map<String, String> blackGlyph = {'K': '♚', 'Q': '♛', 'R': '♜', 'B': '♝', 'N': '♞', 'P': '♟︎'};

  static String glyph(String piece) => (piece[0] == 'w' ? whiteGlyph : blackGlyph)[piece[1]]!;

  static const Map<String, Localized> names = {
    'K': Localized(uz: 'Shoh', en: 'King', ru: 'Король'),
    'Q': Localized(uz: 'Vazir', en: 'Queen', ru: 'Ферзь'),
    'R': Localized(uz: 'Rux', en: 'Rook', ru: 'Ладья'),
    'B': Localized(uz: 'Fil', en: 'Bishop', ru: 'Слон'),
    'N': Localized(uz: 'Ot', en: 'Knight', ru: 'Конь'),
    'P': Localized(uz: 'Piyoda', en: 'Pawn', ru: 'Пешка'),
  };

  static const Map<String, String> moveHints = {
    'K': 'Shoh har tomonga faqat bitta katak yuradi.',
    'Q': 'Vazir to‘g‘ri va qiyshiq chiziqlar bo‘ylab istalgancha yuradi.',
    'R': 'Rux to‘g‘ri chiziq bo‘ylab yuradi: oldinga, orqaga, chapga, o‘ngga.',
    'B': 'Fil faqat qiyshiq (diagonal) chiziq bo‘ylab yuradi.',
    'N': 'Ot «G» harfi kabi yuradi: ikki katak to‘g‘ri va bir katak yonga.',
    'P': 'Piyoda oldinga bir katak yuradi, qiyshiq tomonga esa oladi.',
  };

  static const Map<String, Localized> gameNames = {
    'pawn_war': Localized(uz: 'Piyodalar jangi', en: 'Pawn battle', ru: 'Битва пешек'),
    'queen_vs_pawns': Localized(uz: 'Vazir piyodalarga qarshi', en: 'Queen against pawns', ru: 'Ферзь против пешек'),
    'rook_vs_pawns': Localized(uz: 'Ikki rux piyodalarga qarshi', en: 'Two rooks against pawns', ru: 'Две ладьи против пешек'),
  };

  static int _bounded(int v, int lo, int hi) => v < lo ? lo : (v > hi ? hi : v);

  static List<String> _types(GenContext g) => g.pl('types').isEmpty ? ['R', 'B', 'Q', 'K', 'N', 'P'] : g.pl('types');

  static int _randSquare(GenContext g, int size, Map<int, String> used, {bool pawn = false}) {
    while (true) {
      final sq = g.rng.nextInt(size * size);
      final r = sq ~/ size;
      if (used.containsKey(sq)) continue;
      if (pawn && (r == 0 || r == size - 1)) continue;
      return sq;
    }
  }

  static Map<int, String> _place(GenContext g, int size, List<String> pieces, [Map<int, String> base = const {}]) {
    final b = Map<int, String>.of(base);
    for (final p in pieces) {
      b[_randSquare(g, size, b, pawn: p[1] == 'P')] = p;
    }
    return b;
  }

  static Exercise _chess(GenContext g, RenderedInstruction say, ChessTask task, String concept,
      {String? hint, String? explanation, Map<String, Object> meta = const {}, int rewardStars = 1}) {
    return g.custom(
      say: say,
      kind: ExerciseKind.chess,
      concept: concept,
      chess: task,
      hint: hint,
      explanation: explanation,
      meta: meta,
      rewardStars: rewardStars,
    );
  }

  // ------------------------------------------------------------ Doska
  /// Rejimlar: `light`, `dark`, `star`, `square` (koordinata bo'yicha).
  static Exercise boardTap(GenContext g) {
    final size = g.p('size', 5);
    final mode = g.pick(g.pl('modes').isEmpty ? ['light', 'dark'] : g.pl('modes'));
    final coords = g.pb('coords');
    switch (mode) {
      case 'star':
        final star = g.rng.nextInt(size * size);
        return _chess(g, g.say('ch_tap_star'), ChessTask(size: size, goal: 'tap_star', stars: {star}, coords: coords),
            'chess:board', meta: {'answer': star});
      case 'square':
        final sq = g.rng.nextInt(size * size);
        final name = ChessPosition(size, const {}).name(sq);
        return _chess(g, g.say('ch_tap_square', {'sq': name}), ChessTask(size: size, goal: 'tap_square', target: sq, coords: true),
            'chess:coords', meta: {'answer': name},
            hint: 'Avval harfni (pastda), keyin raqamni (chapda) top.', explanation: '$name: ${name[0]} ustun, ${name.substring(1)}-qator');
      default:
        final light = mode == 'light';
        // Doskada 1–2 ta figura ham turadi (katak rangi figuraga bog'liq emasligini ko'rsatish uchun).
        final pieces = g.chance(0.5) ? _place(g, size, [g.pick(['wR', 'wN', 'bB', 'bQ'])]) : <int, String>{};
        return _chess(g, g.say(light ? 'ch_tap_light' : 'ch_tap_dark'),
            ChessTask(size: size, goal: light ? 'tap_light' : 'tap_dark', pieces: pieces, coords: coords), 'chess:board',
            meta: {'answer': mode});
    }
  }

  // ------------------------------------------------------------ Figurani top (doskada)
  static Exercise pieceTap(GenContext g) {
    final size = g.p('size', 5);
    final types = _types(g);
    final count = g.p('count', 3);
    final chosen = g.sample(types, _bounded(count, 2, types.length));
    final target = chosen.first;
    final pieces = _place(g, size, [for (final t in chosen) '${g.chance(0.7) ? 'w' : 'b'}$t']);
    return _chess(
      g,
      g.say('ch_tap_piece', {'piece': names[target]!}),
      ChessTask(size: size, goal: 'tap_piece', pieces: pieces, pieceType: target, coords: g.pb('coords')),
      'chess:piece:$target',
      meta: {'answer': target},
      explanation: '${whiteGlyph[target]} ${names[target]!.uz} · ${names[target]!.ru} · ${names[target]!.en}',
    );
  }

  // ------------------------------------------------------------ Figura nomi (3 tilda)
  /// Rejimlar: `name` (belgi → nom), `find` (nom → belgi), `three_lang` (uch tilda eshit → nom).
  static Exercise pieceName(GenContext g) {
    final types = _types(g);
    final mode = g.pick(g.pl('modes').isEmpty ? ['find'] : g.pl('modes'));
    final optCount = g.p('options', 3);
    final chosen = g.sample(types, _bounded(optCount, 2, types.length));
    final target = chosen.first;
    final n = names[target]!;
    final explanation = '${whiteGlyph[target]} O‘zbekcha: ${n.uz} · Русский: ${n.ru} · English: ${n.en}';
    switch (mode) {
      case 'name':
        return g.choice(
          say: g.say('ch_piece_name'),
          visual: TextVisual(whiteGlyph[target]!, scale: 1.6),
          options: [for (final t in chosen) Opt.text(names[t]!.uz)],
          concept: 'chess:piece:$target',
          meta: {'answer': target},
          explanation: explanation,
        );
      case 'three_lang':
        final base = g.say('ch_three_lang');
        final parts = [SpeechPart(n.uz, 'uz'), SpeechPart(n.ru, 'ru'), SpeechPart(n.en, 'en'), const SpeechPart('Qaysi figura?', 'uz')];
        return g.choice(
          say: RenderedInstruction(base.text, parts.map((p) => p.text).join(' '), parts: parts, key: base.key),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final t in chosen) Opt.text(whiteGlyph[t]!)],
          concept: 'chess:piece:$target',
          meta: {'answer': target},
          explanation: explanation,
        );
      default:
        return g.choice(
          say: g.say('ch_find_piece', {'piece': n}),
          options: [for (final t in chosen) Opt.text(whiteGlyph[t]!)],
          concept: 'chess:piece:$target',
          meta: {'answer': target},
          explanation: explanation,
        );
    }
  }

  // ------------------------------------------------------------ Yulduzchaga yur
  static Exercise moveStar(GenContext g) {
    final size = g.p('size', 5);
    final type = g.pick(_types(g));
    // To'siq figuralar (katta darajada): yo'lni to'sadi, o'ylab yurish kerak.
    final blockers = g.p('blockers', 0);
    for (var attempt = 0; attempt < 200; attempt++) {
      var pieces = _place(g, size, ['w$type']);
      if (blockers > 0) pieces = _place(g, size, List.filled(blockers, 'wP'), pieces);
      final pos = ChessPosition(size, pieces);
      final from = pieces.entries.firstWhere((e) => e.value == 'w$type').key;
      final moves = ChessRules.movesFrom(pos, from);
      if (moves.length < (type == 'P' ? 1 : 2)) continue;
      final star = g.pick(moves).to;
      if (pieces.containsKey(star)) continue;
      // Piyoda oxirgi qatorga chiqib vazirga aylanmasin (kichiklar uchun chalkash).
      if (type == 'P' && star ~/ size == 0) continue;
      final task = ChessTask(size: size, goal: 'move_star', pieces: pieces, stars: {star}, coords: g.pb('coords'));
      return _chess(g, g.say('ch_move_star', {'piece': names[type]!}), task, 'chess:move:$type',
          hint: moveHints[type], explanation: moveHints[type], meta: {'answer': star, 'piece': type});
    }
    throw StateError('move_star');
  }

  // ------------------------------------------------------------ Hamma yulduzchalarni yig'
  static Exercise collect(GenContext g) {
    final size = g.p('size', 8);
    final type = g.pick(_types(g).where((t) => t != 'P').toList());
    final count = g.p('stars', 3);
    final pieces = _place(g, size, ['w$type']);
    final from = pieces.keys.first;
    final pos = ChessPosition(size, pieces);
    final stars = <int>{};
    var guard = 0;
    while (stars.length < count && guard++ < 500) {
      final sq = g.rng.nextInt(size * size);
      if (sq == from || stars.contains(sq)) continue;
      // Fil faqat o'z rangidagi kataklarga boradi.
      if (type == 'B' && pos.isLight(sq) != pos.isLight(from)) continue;
      stars.add(sq);
    }
    return _chess(g, g.say('ch_collect', {'piece': names[type]!}),
        ChessTask(size: size, goal: 'collect', pieces: pieces, stars: stars, coords: g.pb('coords')), 'chess:collect:$type',
        hint: moveHints[type], meta: {'piece': type, 'stars': stars.length});
  }

  // ------------------------------------------------------------ Masalalar
  /// `goal`: `capture`, `safe_capture`, `check`, `escape`, `defend`, `mate`.
  static Exercise puzzle(GenContext g) {
    final goals = g.pl('goals').isEmpty ? ['capture'] : g.pl('goals');
    final goal = g.pick(goals);
    final size = g.p('size', 8);
    for (var attempt = 0; attempt < 800; attempt++) {
      final task = _tryPuzzle(g, goal, size);
      if (task == null) continue;
      if (!ChessGoals.isPlayable(task)) continue;
      final (key, hint, explanation) = switch (goal) {
        'capture' => ('ch_capture', 'Qaysi oq figura qora figuraga yeta oladi?', 'Olish — raqib figurasi turgan katakka yurish.'),
        'safe_capture' => ('ch_safe_capture', 'Olgandan keyin figurangni raqib ola olmasligi kerak.', 'Himoyalanmagan figurani olsang, o‘z figurang xavfsiz qoladi.'),
        'check' => ('ch_check', 'Shohga to‘g‘ridan-to‘g‘ri hujum qiladigan yurishni top.', 'Shax — shohga hujum.'),
        'escape' => ('ch_escape', 'Shohni hujum qilinmagan katakka o‘tkaz yoki hujumchini ol.', 'Shaxdan qutulish: qochish, to‘sish yoki hujumchini olish.'),
        'defend' => ('ch_defend', 'Figurani hujum yetmaydigan katakka o‘tkaz.', 'Hujumdagi figurani xavfsiz joyga olib qochdik.'),
        _ => ('ch_mate', 'Shohga shax ber — qochadigan joyi qolmasin.', 'Mat — shohga shax va qochadigan joy yo‘q.'),
      };
      return _chess(g, g.say(key), task, 'chess:$goal', hint: hint, explanation: explanation, meta: {'goal': goal});
    }
    throw StateError('puzzle $goal');
  }

  static ChessTask? _tryPuzzle(GenContext g, String goal, int size) {
    final coords = g.pb('coords');
    switch (goal) {
      case 'capture':
        // Bitta oq figura va bitta qora figura (shohlarsiz) — to'g'ridan-to'g'ri olish.
        final type = g.pick(_types(g).where((t) => t != 'K').toList());
        final victim = g.pick(const ['bP', 'bN', 'bB', 'bR']);
        final extra = g.p('extraBlack', 0);
        final pieces = _place(g, size, ['w$type', victim, ...List.filled(extra, 'bP')]);
        final pos = ChessPosition(size, pieces);
        final legal = ChessRules.legalMoves(pos, 'w');
        final caps = legal.where((m) => m.isCapture).toList();
        // Bitta olish va kamida ikkita boshqa yurish — tanlash kerak bo'lsin.
        if (caps.length != 1 || legal.length - caps.length < 2) return null;
        return ChessTask(size: size, goal: 'capture', pieces: pieces, target: caps.first.to, coords: coords);
      case 'safe_capture':
        final hero = g.pick(const ['wQ', 'wR', 'wB', 'wN']);
        final blacks = g.sample(const ['bN', 'bB', 'bR', 'bP', 'bP'], 3);
        final pieces = _place(g, size, ['wK', 'bK', hero, ...blacks]);
        final pos = ChessPosition(size, pieces);
        if (!ChessRules.isSane(pos) || ChessRules.inCheck(pos, 'w')) return null;
        final caps = ChessRules.legalMoves(pos, 'w').where((m) => m.isCapture && m.captured![1] != 'K').toList();
        final safe = caps.where((m) => !ChessRules.isAttacked(ChessRules.apply(pos, m), m.to, 'b')).toList();
        if (safe.length != 1 || safe.length == caps.length) return null;
        return ChessTask(size: size, goal: 'safe_capture', pieces: pieces, coords: coords);
      case 'check':
        final extra = g.pick(const [['wQ'], ['wR'], ['wB', 'wN'], ['wR', 'wB'], ['wN', 'wR']]);
        final pieces = _place(g, size, ['wK', 'bK', ...extra]);
        final pos = ChessPosition(size, pieces);
        if (!ChessRules.isSane(pos) || ChessRules.inCheck(pos, 'w')) return null;
        final moves = ChessRules.legalMoves(pos, 'w');
        final good = moves.where((m) => ChessRules.inCheck(ChessRules.apply(pos, m), 'b')).length;
        if (good == 0 || good > 6 || moves.length - good < 2) return null;
        return ChessTask(size: size, goal: 'check', pieces: pieces, coords: coords);
      case 'escape':
        final attacker = g.pick(const ['bR', 'bB', 'bQ', 'bN']);
        final helpers = g.pick(const [<String>[], ['wR'], ['wN']]);
        final pieces = _place(g, size, ['wK', 'bK', attacker, ...helpers]);
        final pos = ChessPosition(size, pieces);
        if (!ChessRules.isSane(pos) || !ChessRules.inCheck(pos, 'w')) return null;
        final legal = ChessRules.legalMoves(pos, 'w');
        if (legal.isEmpty) return null;
        final k = ChessRules.kingSquare(pos, 'w')!;
        // Shohning ba'zi yurishlari noqonuniy bo'lsin — o'ylash kerak.
        final illegal = ChessRules.pseudoMoves(pos, 'w').where((m) => m.from == k && !legal.contains(m));
        if (illegal.isEmpty) return null;
        final attackerSq = pieces.entries.firstWhere((e) => e.value == attacker).key;
        return ChessTask(size: size, goal: 'escape', pieces: pieces, coords: coords, highlight: {attackerSq, k});
      case 'defend':
        final hero = g.pick(const ['wQ', 'wR', 'wB', 'wN']);
        final enemy = g.pick(const ['bR', 'bB', 'bN', 'bQ', 'bP']);
        final pieces = _place(g, size, ['wK', 'bK', hero, enemy]);
        final pos = ChessPosition(size, pieces);
        if (!ChessRules.isSane(pos) || ChessRules.inCheck(pos, 'w')) return null;
        final hs = pieces.entries.firstWhere((e) => e.value == hero).key;
        if (!ChessRules.isAttacked(pos, hs, 'b')) return null;
        // Figura himoyalanmagan bo'lsin (aks holda qutqarish shart emas).
        final probe = ChessPosition(size, {...pieces, hs: 'bP'});
        if (ChessRules.isAttacked(probe, hs, 'w')) return null;
        final moves = ChessRules.legalMoves(pos, 'w').where((m) => m.from == hs).toList();
        final good = moves.where((m) => !ChessRules.isAttacked(ChessRules.apply(pos, m), m.to, 'b')).length;
        if (good == 0 || good == moves.length) return null;
        final es = pieces.entries.firstWhere((e) => e.value == enemy).key;
        return ChessTask(size: size, goal: 'defend', pieces: pieces, target: hs, coords: coords, highlight: {hs, es});
      default: // mate
        final kind = g.pick(g.pl('mates').isEmpty ? const ['RR', 'QK', 'RK'] : g.pl('mates'));
        final bk = g.rng.nextInt(size); // qora shoh chetki qatorda
        final base = <int, String>{bk: 'bK'};
        final extra = switch (kind) { 'RR' => ['wR', 'wR'], 'QK' => ['wQ'], _ => ['wR'] };
        final pieces = _place(g, size, ['wK', ...extra], base);
        final pos = ChessPosition(size, pieces);
        if (!ChessRules.isSane(pos) || ChessRules.inCheck(pos, 'w')) return null;
        final mates = ChessRules.legalMoves(pos, 'w').where((m) => ChessRules.isMate(ChessRules.apply(pos, m), 'b')).length;
        if (mates == 0) return null;
        return ChessTask(size: size, goal: 'mate', pieces: pieces, coords: coords);
    }
  }

  // ------------------------------------------------------------ AI bilan o'yin
  static Exercise play(GenContext g) {
    final game = g.pick(g.pl('games').isEmpty ? ['pawn_war'] : g.pl('games'));
    final ai = g.ps('ai', 'very_easy');
    final rules = switch (game) {
      'queen_vs_pawns' => 'Hamma piyodalarni ol — birortasi ham oxirgi qatorga yetmasin.',
      'rook_vs_pawns' => 'Ikki rux bilan hamma piyodalarni ol.',
      _ => 'Piyodangni oxirgi qatorga birinchi bo‘lib olib bor yoki raqib piyodalarini ol.',
    };
    return _chess(
      g,
      g.say('ch_play', {'game': gameNames[game]!}),
      ChessTask(size: 8, goal: 'play', game: game, ai: ai, coords: g.pb('coords')),
      'chess:play:$game',
      hint: rules,
      explanation: rules,
      meta: {'game': game, 'ai': ai},
      // O'yin uzoqroq — ko'proq yulduz.
      rewardStars: 3,
    );
  }
}
