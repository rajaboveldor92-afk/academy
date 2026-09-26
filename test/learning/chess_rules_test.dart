import 'dart:math';

import 'package:academy/learning/chess/chess_goals.dart';
import 'package:academy/learning/chess/chess_rules.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:flutter_test/flutter_test.dart';

/// Shaxmat qoidalari, masalalar va AI.
void main() {
  // 8×8: katak = qator*8 + ustun; 0-qator — 8-gorizontal (a8..h8).
  ChessPosition pos(Map<String, String> pieces, {int size = 8}) {
    final p = ChessPosition(size, const {});
    return ChessPosition(size, {for (final e in pieces.entries) p.square(e.key)!: e.value});
  }

  int movesOf(ChessPosition p, String sq) => ChessRules.movesFrom(p, p.square(sq)!).length;

  test('katak nomlari va rangi', () {
    final p = ChessPosition(8, const {});
    expect(p.name(0), 'a8');
    expect(p.name(63), 'h1');
    expect(p.square('e4'), 4 * 8 + 4);
    expect(p.isLight(p.square('a8')!), isTrue);
    expect(p.isLight(p.square('a1')!), isFalse); // a1 — qora katak
    expect(p.isLight(p.square('h1')!), isTrue);
  });

  test('figuralar yurishi bo‘sh doskada', () {
    expect(movesOf(pos({'a1': 'wN'}), 'a1'), 2);
    expect(movesOf(pos({'d4': 'wN'}), 'd4'), 8);
    expect(movesOf(pos({'d4': 'wR'}), 'd4'), 14);
    expect(movesOf(pos({'d4': 'wB'}), 'd4'), 13);
    expect(movesOf(pos({'d4': 'wQ'}), 'd4'), 27);
    expect(movesOf(pos({'d4': 'wK'}), 'd4'), 8);
    expect(movesOf(pos({'e2': 'wP'}), 'e2'), 2); // birinchi yurishda ikki katak
    expect(movesOf(pos({'e3': 'wP'}), 'e3'), 1);
    expect(movesOf(pos({'e2': 'wP', 'e3': 'bP'}), 'e2'), 0); // oldi to'silgan
    expect(movesOf(pos({'e4': 'wP', 'd5': 'bN', 'f5': 'wB'}), 'e4'), 2); // oldinga + d5 ni olish
    // Kichik doskada piyoda faqat bir katak yuradi.
    expect(ChessRules.movesFrom(ChessPosition(5, {3 * 5 + 2: 'wP'}), 3 * 5 + 2).length, 1);
  });

  test('to‘siq va o‘z figurasi', () {
    // Rux d4, o'z piyodasi d6 va raqib oti f4 da.
    final p = pos({'d4': 'wR', 'd6': 'wP', 'f4': 'bN'});
    final targets = ChessRules.movesFrom(p, p.square('d4')!).map((m) => p.name(m.to)).toSet();
    expect(targets.contains('d5'), isTrue);
    expect(targets.contains('d6'), isFalse);
    expect(targets.contains('d7'), isFalse);
    expect(targets.contains('f4'), isTrue); // olish
    expect(targets.contains('g4'), isFalse);
  });

  test('shax, mat va noqonuniy yurishlar', () {
    // Shoh hujum qilingan katakka yura olmaydi.
    final p = pos({'e1': 'wK', 'd8': 'bR', 'h8': 'bK'});
    final kingTargets = ChessRules.movesFrom(p, p.square('e1')!).map((m) => p.name(m.to)).toSet();
    expect(kingTargets.contains('d1'), isFalse);
    expect(kingTargets.contains('d2'), isFalse);
    expect(kingTargets.contains('f2'), isTrue);
    // Orqa qatorda mat: Ra8#.
    final back = pos({'g8': 'bK', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP', 'a1': 'wR', 'g1': 'wK'});
    final mate = ChessRules.find(back, back.square('a1')!, back.square('a8')!)!;
    final after = ChessRules.apply(back, mate);
    expect(ChessRules.inCheck(after, 'b'), isTrue);
    expect(ChessRules.isMate(after, 'b'), isTrue);
    // Shax, lekin mat emas.
    final notMate = pos({'g8': 'bK', 'a1': 'wR', 'g1': 'wK'});
    final ra8 = ChessRules.apply(notMate, ChessRules.find(notMate, notMate.square('a1')!, notMate.square('a8')!)!);
    expect(ChessRules.inCheck(ra8, 'b'), isTrue);
    expect(ChessRules.isMate(ra8, 'b'), isFalse);
    // Bog'langan figura shohni ochib qo'ya olmaydi.
    final pinned = pos({'e1': 'wK', 'e2': 'wB', 'e8': 'bR', 'a8': 'bK'});
    expect(ChessRules.movesFrom(pinned, pinned.square('e2')!), isEmpty);
  });

  test('piyoda oxirgi qatorda vazirga aylanadi', () {
    final p = pos({'a7': 'wP', 'h1': 'bK', 'c1': 'wK'});
    final m = ChessRules.find(p, p.square('a7')!, p.square('a8')!)!;
    expect(m.promotion, isTrue);
    expect(ChessRules.apply(p, m).at(p.square('a8')!), 'wQ');
    expect(ChessMiniGame.winner(ChessRules.apply(p, m), m, 'b'), 'w');
  });

  test('AI: qonuniy yurish qiladi, "oson" daraja bepul vazirni oladi', () {
    final rng = Random(3);
    final start = ChessMiniGame.start('pawn_war');
    for (var i = 0; i < 20; i++) {
      final m = ChessAi.choose(start, 'b', i.isEven ? 'very_easy' : 'easy', rng)!;
      expect(ChessRules.legalMoves(start, 'b').contains(m), isTrue);
    }
    final free = pos({'d5': 'wQ', 'e6': 'bP', 'h8': 'bK', 'a1': 'wK'});
    final m = ChessAi.choose(free, 'b', 'easy', Random(1))!;
    expect(free.name(m.to), 'd5');
  });

  test('mini-o‘yin: AI bilan to‘liq partiya tugaydi', () {
    for (final game in ['pawn_war', 'queen_vs_pawns', 'rook_vs_pawns']) {
      final rng = Random(game.length);
      var p = ChessMiniGame.start(game);
      String? winner;
      var turn = 'w';
      for (var ply = 0; ply < 300 && winner == null; ply++) {
        final m = ChessAi.choose(p, turn, 'easy', rng);
        if (m == null) {
          winner = ChessRules.opponent(turn);
          break;
        }
        p = ChessRules.apply(p, m);
        turn = ChessRules.opponent(turn);
        winner = ChessMiniGame.winner(p, m, turn);
      }
      expect(winner, isNotNull, reason: game);
    }
  });

  group('masalalar (generatorlar bilan)', () {
    late ContentRepository content;
    setUpAll(() async {
      TestWidgetsFlutterBinding.ensureInitialized();
      content = await ContentRepository.load();
    });

    test('har bir masalada yechim bor va noto‘g‘ri yurish ham bor', () {
      for (final t in content.curriculum('chess', '6')!.topics.where((t) => t.generator == 'puzzle')) {
        final gen = GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator)!;
        for (var level = 1; level <= t.maxLevel; level++) {
          for (var i = 0; i < 25; i++) {
            final e = gen(GenContext(rng: Random(i * 31 + level), content: content, topic: t, level: level, age: 6));
            final task = e.chess!;
            final start = ChessGoals.initial(task);
            final all = ChessRules.legalMoves(start, 'w');
            final good = ChessGoals.solutions(task);
            expect(good, isNotEmpty, reason: '${t.id} ${task.describe()}');
            if (task.goal != 'escape') {
              expect(all.length, greaterThan(good.length), reason: '${t.id}: hamma yurish to‘g‘ri — masala emas');
            }
            if (task.goal == 'mate') {
              for (final m in good) {
                expect(ChessRules.isMate(ChessRules.apply(start, m), 'b'), isTrue);
              }
            }
            if (task.goal == 'safe_capture') {
              expect(good.length, 1, reason: task.describe());
            }
          }
        }
      }
    });

    test('4 yosh: kichik doska, yulduzchaga bir yurishda yetib boriladi', () {
      for (final t in content.curriculum('chess', '4')!.topics.where((t) => t.generator == 'move_star')) {
        final gen = GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator)!;
        for (var level = 1; level <= t.maxLevel; level++) {
          for (var i = 0; i < 25; i++) {
            final e = gen(GenContext(rng: Random(i + level * 7), content: content, topic: t, level: level, age: 4));
            final task = e.chess!;
            expect(task.size, lessThanOrEqualTo(6));
            expect(ChessGoals.solutions(task), isNotEmpty, reason: task.describe());
            expect(e.kind, ExerciseKind.chess);
          }
        }
      }
    });
  });
}
