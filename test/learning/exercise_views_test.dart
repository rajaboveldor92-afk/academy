import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/puzzles.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/chess/chess_rules.dart';
import 'package:academy/learning/models/visual.dart';
import 'package:academy/learning/ui/activity_view.dart';
import 'package:academy/learning/ui/assemble_view.dart';
import 'package:academy/learning/ui/cards_view.dart';
import 'package:academy/learning/ui/chess_view.dart';
import 'package:academy/learning/ui/choice_view.dart';
import 'package:academy/learning/ui/coding_view.dart';
import 'package:academy/learning/ui/jigsaw_view.dart';
import 'package:academy/learning/ui/match_view.dart';
import 'package:academy/learning/ui/maze_view.dart';
import 'package:academy/learning/ui/option_card.dart';
import 'package:academy/learning/ui/sort_view.dart';
import 'package:academy/learning/ui/spot_view.dart';
import 'package:academy/learning/ui/sudoku_view.dart';
import 'package:academy/learning/ui/trace_view.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

/// Har bir mashq turini haqiqiy generatsiya qilingan kontent bilan o'ynab ko'ramiz.
void main() {
  late ContentRepository content;

  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    content = await ContentRepository.load();
  });

  Exercise make(String topicId, int level, {int seed = 3}) {
    final t = content.topic(topicId)!;
    final gen = GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator)!;
    return gen(GenContext(rng: Random(seed), content: content, topic: t, level: level, age: t.ageSuffix == '4' ? 4 : 6));
  }

  Future<void> host(WidgetTester tester, Widget child) async {
    tester.view.physicalSize = const Size(1080, 2000);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(MaterialApp(home: Scaffold(body: Padding(padding: const EdgeInsets.all(8), child: child))));
    await tester.pump();
  }

  testWidgets('tanlash: noto‘g‘ri javob xato sifatida, to‘g‘ri javob yechim sifatida', (tester) async {
    final e = make('math4.count_1_5', 1);
    final mistakes = <int>[];
    int? solved;
    await host(
      tester,
      ChoiceExerciseView(
        exercise: e,
        callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m),
      ),
    );
    final cards = find.byType(OptionCard);
    expect(cards, findsNWidgets(e.options.length));
    final wrong = [for (var i = 0; i < e.options.length; i++) if (i != e.correctIndex) i].first;
    await tester.tap(cards.at(wrong));
    await tester.pump(const Duration(milliseconds: 400));
    expect(mistakes, [1]);
    expect(solved, isNull);
    await tester.tap(cards.at(e.correctIndex));
    await tester.pump(const Duration(milliseconds: 400));
    expect(solved, 1);
  });

  testWidgets('sudrab qo‘yish: to‘g‘ri variantni ? ga sudrash', (tester) async {
    final e = make('math4.add_5', 3);
    expect(e.dragToTarget, isTrue);
    int? solved;
    await host(
      tester,
      ChoiceExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    final from = tester.getCenter(find.byType(OptionCard).at(e.correctIndex));
    final to = tester.getCenter(find.text('?'));
    final gesture = await tester.startGesture(from);
    await tester.pump(const Duration(milliseconds: 50));
    await gesture.moveTo(to, timeStamp: const Duration(milliseconds: 300));
    await tester.pump();
    await gesture.up();
    await tester.pump(const Duration(milliseconds: 300));
    expect(solved, 0);
  });

  testWidgets('xotira: avval rasm, keyin savol', (tester) async {
    final e = make('logic4.missing', 1);
    int? solved;
    await host(
      tester,
      ChoiceExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    expect(find.text('Yaxshilab qara va eslab qol!'), findsOneWidget);
    await tester.pump(Duration(seconds: e.previewSeconds + 1));
    await tester.pump();
    await tester.tap(find.byType(OptionCard).at(e.correctIndex));
    await tester.pump(const Duration(milliseconds: 300));
    expect(solved, 0);
  });

  testWidgets('juftlash: barcha juftlar topiladi', (tester) async {
    final e = make('logic4.pairs', 2);
    int? solved;
    await host(
      tester,
      MatchExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    final cards = find.byType(OptionCard);
    final n = e.pairs.length;
    expect(cards, findsNWidgets(n * 2));
    // Chap ustun — 0..n-1; o'ng ustun ekranda aralash, shuning uchun mos kartani mazmuni bo'yicha topamiz.
    for (var i = 0; i < n; i++) {
      await tester.tap(cards.at(i));
      await tester.pump();
      final rightWidgets = [for (var j = n; j < 2 * n; j++) tester.widget<OptionCard>(cards.at(j))];
      final target = rightWidgets.indexWhere((w) => w.option.describe() == e.pairs[i].right.describe());
      await tester.tap(cards.at(n + target));
      await tester.pump(const Duration(milliseconds: 300));
    }
    expect(solved, 0);
  });

  testWidgets('guruhlash: har bir narsa o‘z savatiga', (tester) async {
    final e = make('logic4.sort_color', 1);
    final task = e.sort!;
    int? solved;
    await host(
      tester,
      SortExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    for (var k = 0; k < task.items.length; k++) {
      // Birinchi qolgan narsa (tartib saqlanadi).
      final itemCard = find.byType(OptionCard).first;
      final widget = tester.widget<OptionCard>(itemCard);
      final idx = [for (var i = 0; i < task.items.length; i++) i]
          .firstWhere((i) => identical(task.items[i], widget.option));
      await tester.tap(itemCard);
      await tester.pump();
      final bins = find.byIcon(Icons.shopping_basket_rounded);
      await tester.tap(bins.at(task.itemBins[idx]));
      await tester.pump(const Duration(milliseconds: 300));
    }
    expect(solved, 0);
  });

  testWidgets('labirint: eng qisqa yo‘l bilan maqsadga', (tester) async {
    final e = make('logic4.maze', 1);
    final maze = e.maze!;
    int? solved;
    await host(
      tester,
      MazeExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    // BFS bilan yo'nalishlar.
    final prev = <int, (int, int)>{};
    final queue = [maze.start];
    final seen = {maze.start};
    for (var i = 0; i < queue.length; i++) {
      for (final d in const [MazeTask.top, MazeTask.right, MazeTask.bottom, MazeTask.left]) {
        final n = maze.neighbor(queue[i], d);
        if (n != null && seen.add(n)) {
          prev[n] = (queue[i], d);
          queue.add(n);
        }
      }
    }
    final dirs = <int>[];
    var cur = maze.goal;
    while (cur != maze.start) {
      final (p, d) = prev[cur]!;
      dirs.add(d);
      cur = p;
    }
    const keys = {MazeTask.top: 'up', MazeTask.bottom: 'down', MazeTask.left: 'left', MazeTask.right: 'right'};
    for (final d in dirs.reversed) {
      await tester.tap(find.byKey(Key('arrow_${keys[d]}')));
      await tester.pump();
    }
    expect(solved, 0);
  });

  testWidgets('sudoku: bo‘sh kataklarni to‘ldirish', (tester) async {
    final e = make('logic6.sudoku', 1);
    final task = e.sudoku!;
    int? solved;
    await host(
      tester,
      SudokuExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    // Ko'rinish avtomatik birinchi bo'sh katakni tanlaydi va keyingisiga o'tadi.
    for (var i = 0; i < task.solution.length; i++) {
      if (task.givens[i]) continue;
      await tester.tap(find.byKey(Key('sudoku_symbol_${task.solution[i]}')));
      await tester.pump();
    }
    expect(solved, 0);
  });

  testWidgets('kodlash: to‘g‘ri dastur robotni maqsadga olib boradi', (tester) async {
    final e = make('logic6.coding', 3);
    expect(e.kind, ExerciseKind.coding);
    final solution = PuzzleFactory.solveCoding(e.coding!)!;
    int? solved;
    await host(
      tester,
      CodingExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    for (final s in solution) {
      await tester.tap(find.byKey(Key('code_$s')));
      await tester.pump();
    }
    await tester.tap(find.byKey(const Key('code_run')));
    for (var i = 0; i <= solution.length + 1; i++) {
      await tester.pump(const Duration(milliseconds: 500));
    }
    expect(solved, 0);
  });

  /// Bo'laklarni to'g'ri tartibda bosish: har safar navbatdagi kerakli bo'lakning birinchi
  /// ishlatilmagan nusxasi.
  Future<void> tapAnswer(WidgetTester tester, AssembleTask task) async {
    final used = <int>{};
    for (final part in task.answer) {
      final i = [for (var k = 0; k < task.tiles.length; k++) k].firstWhere((k) => !used.contains(k) && task.tiles[k] == part);
      used.add(i);
      await tester.tap(find.byKey(ValueKey('tile_$i')));
      await tester.pump(const Duration(milliseconds: 250));
    }
  }

  testWidgets('yig‘ish: so‘zlardan gap, noto‘g‘ri bo‘lak xato hisoblanadi', (tester) async {
    final e = make('uzbek6.build_sentence', 2);
    expect(e.kind, ExerciseKind.assemble);
    final task = e.assemble!;
    final mistakes = <int>[];
    final spoken = <String>[];
    int? solved;
    await host(
      tester,
      AssembleExerciseView(
        exercise: e,
        callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m, onSpeak: spoken.add),
      ),
    );
    // Birinchi katakka mos kelmaydigan bo'lak — xato, katakka tushmaydi.
    final wrong = [for (var k = 0; k < task.tiles.length; k++) k].firstWhere((k) => task.tiles[k] != task.answer.first);
    await tester.tap(find.byKey(ValueKey('tile_$wrong')));
    await tester.pump(const Duration(milliseconds: 400));
    expect(mistakes, [1]);
    expect(solved, isNull);
    await tapAnswer(tester, task);
    expect(solved, 1);
    expect(spoken.last, task.result);
  });

  testWidgets('yig‘ish: harflardan so‘z (ortiqcha harflar bilan)', (tester) async {
    final e = make('uzbek6.short_words', 3);
    expect(e.kind, ExerciseKind.assemble);
    int? solved;
    await host(
      tester,
      AssembleExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
    );
    await tapAnswer(tester, e.assemble!);
    expect(solved, 0);
  });

  group('yozish (trace)', () {
    /// Normallashtirilgan nuqtani ekran koordinatasiga o'giradi.
    Offset toScreen(WidgetTester tester, TraceTask t, Point2 p) {
      final rect = tester.getRect(find.byKey(const ValueKey('trace_area')));
      const k = TraceExerciseView.insetRatio;
      final innerH = rect.height / (1 + 2 * k);
      final pad = innerH * k;
      final innerW = rect.width - 2 * pad;
      return rect.topLeft + Offset(pad + p.x * innerW, pad + p.y * innerH);
    }

    Future<void> draw(WidgetTester tester, TraceTask t, List<Point2> stroke) async {
      final g = await tester.startGesture(toScreen(tester, t, stroke.first));
      for (final p in stroke.skip(1)) {
        await g.moveTo(toScreen(tester, t, p));
      }
      await g.up();
      await tester.pump();
    }

    Exercise traceExercise(TraceTask task) => Exercise(
          topicId: 'test.trace',
          subject: 'writing',
          level: 1,
          kind: ExerciseKind.trace,
          instruction: const Localized(uz: 'Chiziqni yoz', en: 'Trace the line', ru: 'Обведи линию'),
          speech: 'Chiziqni yoz',
          conceptKey: 'trace:test',
          trace: task,
        );

    testWidgets('harfni namuna bo‘yicha yozish — yechiladi', (tester) async {
      final e = make('writing6.letters', 1);
      final task = e.trace!;
      int? solved;
      await host(
        tester,
        TraceExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
      );
      for (final s in task.strokes) {
        await draw(tester, task, s);
      }
      expect(solved, 0, reason: task.id);
    });

    testWidgets('nuqtalarni birlashtirish — yechiladi', (tester) async {
      final e = make('writing4.dots', 1);
      final task = e.trace!;
      expect(task.dots, isTrue);
      int? solved;
      await host(
        tester,
        TraceExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)),
      );
      await draw(tester, task, task.strokes.first);
      expect(solved, 0);
    });

    testWidgets('yo‘ldan chiqqan chiziq o‘chadi va xato hisoblanadi; keyin to‘g‘ri yozish', (tester) async {
      const task = TraceTask(
        id: 'v',
        strokes: [
          [Point2(0.5, 0.1), Point2(0.5, 0.5), Point2(0.5, 0.9)],
        ],
        tolerance: 0.1,
      );
      final mistakes = <int>[];
      int? solved;
      await host(
        tester,
        TraceExerciseView(
          exercise: traceExercise(task),
          callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m),
        ),
      );
      await draw(tester, task, const [Point2(0.05, 0.1), Point2(0.05, 0.5), Point2(0.05, 0.9)]);
      await tester.pump(const Duration(milliseconds: 400));
      expect(mistakes, [1]);
      expect(solved, isNull);
      await draw(tester, task, task.strokes.first);
      expect(solved, 1);
    });

    testWidgets('ko‘p xatodan keyin mashq yumshoq yakunlanadi', (tester) async {
      const task = TraceTask(
        id: 'v',
        strokes: [
          [Point2(0.5, 0.1), Point2(0.5, 0.9)],
        ],
        tolerance: 0.1,
      );
      final mistakes = <int>[];
      int? solved;
      await host(
        tester,
        TraceExerciseView(
          exercise: traceExercise(task),
          callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m),
        ),
      );
      for (var i = 0; i < TraceExerciseView.maxMistakes; i++) {
        await draw(tester, task, const [Point2(0.95, 0.1), Point2(0.95, 0.9)]);
        await tester.pump(const Duration(milliseconds: 400));
      }
      expect(mistakes.length, TraceExerciseView.maxMistakes);
      expect(solved, TraceExerciseView.maxMistakes);
      // Namoyish animatsiyasi to'xtaydi.
      await tester.pump(const Duration(seconds: 5));
    });

    testWidgets('tozalash va ko‘rsatish tugmalari ishlaydi', (tester) async {
      final e = make('writing4.letters', 1);
      await host(
        tester,
        TraceExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (_) {})),
      );
      await tester.tap(find.byKey(const ValueKey('trace_demo')));
      await tester.pump(const Duration(milliseconds: 500));
      await tester.tap(find.byKey(const ValueKey('trace_clear')));
      await tester.pump(const Duration(seconds: 5));
      expect(tester.takeException(), isNull);
    });
  });

  group('shaxmat', () {
    Exercise chessExercise(ChessTask task) => Exercise(
          topicId: 'test.chess',
          subject: 'chess',
          level: 1,
          kind: ExerciseKind.chess,
          instruction: const Localized(uz: 'Shaxmat', en: 'Chess', ru: 'Шахматы'),
          speech: 'Shaxmat',
          conceptKey: 'chess:test',
          chess: task,
        );

    Future<void> tapSquare(WidgetTester tester, int sq) async {
      await tester.tap(find.byKey(ValueKey('sq_$sq')));
      await tester.pump(const Duration(milliseconds: 400));
    }

    testWidgets('oq katakni bosish: qora katak — xato, oq katak — yechim', (tester) async {
      const task = ChessTask(size: 4, goal: 'tap_light');
      final mistakes = <int>[];
      int? solved;
      await host(tester, ChessExerciseView(exercise: chessExercise(task), callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m)));
      await tapSquare(tester, 1); // (0,1) — qora
      expect(mistakes, [1]);
      await tapSquare(tester, 0); // (0,0) — oq
      expect(solved, 1);
    });

    testWidgets('ruxni bosib yulduzchaga yurish; qoidaga zid yurish qaytariladi', (tester) async {
      // 5×5: rux (4,0) da, yulduzcha (0,0) da.
      const task = ChessTask(size: 5, goal: 'move_star', pieces: {20: 'wR'}, stars: {0});
      final mistakes = <int>[];
      int? solved;
      await host(tester, ChessExerciseView(exercise: chessExercise(task), callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m)));
      await tapSquare(tester, 20);
      await tapSquare(tester, 6); // (1,1) — rux qiyshiq yurmaydi
      expect(mistakes, [1]);
      expect(solved, isNull);
      await tapSquare(tester, 20);
      await tapSquare(tester, 10); // (2,0) — qonuniy, lekin yulduzcha emas
      expect(mistakes, [1, 2]);
      await tapSquare(tester, 20); // rux joyida qolgan
      await tapSquare(tester, 0);
      expect(solved, 2);
    });

    testWidgets('otni sudrab yulduzchaga olib borish', (tester) async {
      // 5×5: ot (4,1) da, yulduzcha (2,2) da.
      const task = ChessTask(size: 5, goal: 'move_star', pieces: {21: 'wN'}, stars: {12});
      int? solved;
      await host(tester, ChessExerciseView(exercise: chessExercise(task), callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)));
      final from = tester.getCenter(find.byKey(const ValueKey('sq_21')));
      final to = tester.getCenter(find.byKey(const ValueKey('sq_12')));
      final gesture = await tester.startGesture(from);
      await tester.pump(const Duration(milliseconds: 50));
      await gesture.moveTo(from + const Offset(0, -20));
      await tester.pump();
      await gesture.moveTo(to);
      await tester.pump();
      await gesture.up();
      await tester.pump(const Duration(milliseconds: 300));
      expect(solved, 0);
    });

    testWidgets('bir yurishda mat', (tester) async {
      final p = ChessPosition(8, const {});
      final pieces = {
        p.square('g8')!: 'bK', p.square('f7')!: 'bP', p.square('g7')!: 'bP', p.square('h7')!: 'bP',
        p.square('a1')!: 'wR', p.square('g1')!: 'wK',
      };
      final task = ChessTask(size: 8, goal: 'mate', pieces: pieces, coords: true);
      int? solved;
      await host(tester, ChessExerciseView(exercise: chessExercise(task), callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)));
      await tapSquare(tester, p.square('a1')!);
      await tapSquare(tester, p.square('a8')!);
      expect(solved, 0);
    });

    testWidgets('AI bilan o‘yin: yurishdan keyin raqib javob beradi', (tester) async {
      const task = ChessTask(size: 8, goal: 'play', game: 'pawn_war', ai: 'very_easy');
      await host(tester, ChessExerciseView(exercise: chessExercise(task), callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (_) {}), random: Random(1)));
      // e2 → e4
      await tapSquare(tester, 6 * 8 + 4);
      await tapSquare(tester, 4 * 8 + 4);
      expect(find.text('Raqib o‘ylayapti…'), findsOneWidget);
      await tester.pump(ChessExerciseView.aiDelay + const Duration(milliseconds: 50));
      await tester.pump();
      expect(find.text('Sening navbating — oq figuralar'), findsOneWidget);
      await tester.pumpWidget(const SizedBox.shrink());
    });
  });

  group('xotira, diqqat, puzzle, ota-ona bilan', () {
    testWidgets('juft kartalar: har xil kartalar yopiladi, juftlar ochiq qoladi', (tester) async {
      final e = make('memory4.cards', 1);
      final faces = e.cards!.faces;
      int? solved;
      await host(tester, CardsExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)));
      // Avval ikkita har xil kartani ochamiz.
      final a = 0;
      final b = [for (var i = 1; i < faces.length; i++) i].firstWhere((i) => faces[i] != faces[a]);
      await tester.tap(find.byKey(const ValueKey('card_0')));
      await tester.pump(const Duration(milliseconds: 300));
      await tester.tap(find.byKey(ValueKey('card_$b')));
      await tester.pump(CardsExerciseView.flipBack + const Duration(milliseconds: 300));
      // Endi hamma juftlarni topamiz.
      final done = <int>{};
      for (var i = 0; i < faces.length; i++) {
        if (done.contains(i)) continue;
        final j = [for (var k = 0; k < faces.length; k++) k].firstWhere((k) => k != i && faces[k] == faces[i]);
        await tester.tap(find.byKey(ValueKey('card_$i')));
        await tester.pump(const Duration(milliseconds: 300));
        await tester.tap(find.byKey(ValueKey('card_$j')));
        await tester.pump(const Duration(milliseconds: 300));
        done.addAll([i, j]);
      }
      expect(solved, 0); // bitta adashish — tabiiy, hisoblanmaydi
    });

    testWidgets('rasm ichidan hammasini topish: noto‘g‘ri narsa — xato', (tester) async {
      final e = make('attention4.find_all', 2);
      final task = e.spot!;
      final mistakes = <int>[];
      int? solved;
      await host(tester, SpotExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m)));
      final wrong = [for (var i = 0; i < task.items.length; i++) i].firstWhere((i) => !task.targets.contains(i));
      await tester.tap(find.byKey(ValueKey('spot_$wrong')));
      await tester.pump(const Duration(milliseconds: 400));
      expect(mistakes, [1]);
      for (final t in task.targets) {
        await tester.tap(find.byKey(ValueKey('spot_$t')));
        await tester.pump(const Duration(milliseconds: 100));
      }
      expect(solved, 1);
    });

    testWidgets('farqni top: namuna rasm va o‘zgargan narsa', (tester) async {
      final e = make('attention6.difference', 1);
      int? solved;
      await host(tester, SpotExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)));
      expect(find.text('Namuna'), findsOneWidget);
      await tester.tap(find.byKey(ValueKey('spot_${e.spot!.targets.first}')));
      await tester.pump(const Duration(milliseconds: 100));
      expect(solved, 0);
    });

    testWidgets('puzzle: bo‘lakni bosib, keyin joyini bosib yig‘ish', (tester) async {
      final e = make('puzzle4.p4', 1);
      final n = e.jigsaw!.pieces;
      final mistakes = <int>[];
      int? solved;
      await host(tester, JigsawExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m)));
      // Noto'g'ri joy: 0-bo'lakni 1-katakka.
      await tester.tap(find.byKey(const ValueKey('piece_0')));
      await tester.pump();
      await tester.tap(find.byKey(const ValueKey('slot_1')));
      await tester.pump(const Duration(milliseconds: 400));
      expect(mistakes, [1]);
      for (var i = 0; i < n; i++) {
        await tester.tap(find.byKey(ValueKey('piece_$i')));
        await tester.pump();
        await tester.tap(find.byKey(ValueKey('slot_$i')));
        await tester.pump(const Duration(milliseconds: 200));
      }
      expect(solved, 1);
    });

    testWidgets('puzzle: bo‘lakni sudrab joyiga qo‘yish', (tester) async {
      final e = make('puzzle6.p9', 1);
      await host(tester, JigsawExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (_) {})));
      final from = tester.getCenter(find.byKey(const ValueKey('piece_4')));
      final to = tester.getCenter(find.byKey(const ValueKey('slot_4')));
      final gesture = await tester.startGesture(from);
      await tester.pump(const Duration(milliseconds: 50));
      await gesture.moveTo(from + const Offset(0, -30));
      await tester.pump();
      await gesture.moveTo(to);
      await tester.pump();
      await gesture.up();
      await tester.pump(const Duration(milliseconds: 300));
      // Joylangan bo'lak tokchadan yo'qoladi.
      expect(find.byKey(const ValueKey('piece_4')), findsNothing);
    });

    testWidgets('ketma-ketlikni eslab qolish: avval ko‘rsatiladi, keyin yig‘iladi', (tester) async {
      final e = make('memory4.sequence', 2);
      expect(e.previewVisual, isA<SceneVisual>());
      int? solved;
      await host(tester, AssembleExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)));
      expect(find.text('Yaxshilab qara va eslab qol!'), findsOneWidget);
      expect(find.byKey(const ValueKey('tile_0')), findsNothing);
      await tester.pump(Duration(seconds: e.previewSeconds + 1));
      await tester.pump();
      await tapAnswer(tester, e.assemble!);
      expect(solved, 0);
    });

    testWidgets('ota-ona bilan faoliyat: "Bajardik!"', (tester) async {
      final e = make('family6.science', 1);
      int? solved;
      await host(tester, ActivityExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (m) => solved = m)));
      expect(find.text(e.activity!.title), findsOneWidget);
      await tester.tap(find.byKey(const ValueKey('activity_done')));
      await tester.pump();
      expect(solved, 0);
    });
  });

  testWidgets('barcha mashq turlari xatosiz chiziladi', (tester) async {
    for (final t in content.allTopics) {
      for (var level = 1; level <= t.maxLevel; level++) {
        final e = make(t.id, level, seed: level + 11);
        final cb = ExerciseCallbacks(onMistake: (_) {}, onSolved: (_) {});
        final Widget view = switch (e.kind) {
          ExerciseKind.match => MatchExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.sort => SortExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.maze => MazeExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.sudoku => SudokuExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.coding => CodingExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.assemble => AssembleExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.trace => TraceExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.chess => ChessExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.cards => CardsExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.spot => SpotExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.jigsaw => JigsawExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.activity => ActivityExerciseView(exercise: e, callbacks: cb),
          ExerciseKind.choice || ExerciseKind.memory => ChoiceExerciseView(exercise: e, callbacks: cb),
        };
        await host(tester, KeyedSubtree(key: ValueKey('${t.id}-$level'), child: view));
        expect(tester.takeException(), isNull, reason: '${t.id} L$level');
      }
    }
    // Xotira mashqlarining taymerlari tugashi uchun.
    await tester.pumpWidget(const SizedBox.shrink());
    await tester.pump(const Duration(seconds: 10));
  });
}
