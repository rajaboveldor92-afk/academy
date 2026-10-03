import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/school/bank_gen.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/ui/circuit_view.dart';
import 'package:academy/learning/ui/match_view.dart';
import 'package:academy/learning/ui/option_card.dart';
import 'package:academy/learning/ui/workshop_order_view.dart';
import 'package:academy/learning/ui/workshop_sort_view.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;
  setUpAll(() async => content = await ContentRepository.load());
  Exercise item(String topic, String kind, {bool? targetLit}) {
    final t = content.topic(topic)!;
    final source = content.banks[topic]!.firstWhere(
      (i) =>
          i['t'] == kind && (targetLit == null || i['targetLit'] == targetLit),
    );
    return BankGen.fromItem(
      GenContext(
        rng: Random(17),
        content: content,
        topic: t,
        level: 1,
        age: 11,
      ),
      source,
    );
  }

  Future<void> host(WidgetTester tester, Widget child) async {
    tester.view.physicalSize = const Size(360, 640);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: Padding(padding: const EdgeInsets.all(8), child: child),
        ),
      ),
    );
    await tester.pump();
  }

  Future<void> tap(WidgetTester tester, Key key) async {
    final target = find.byKey(key);
    await tester.ensureVisible(target);
    await tester.tap(target);
    await tester.pumpAndSettle();
  }

  test(
    'each of thirteen workshops builds six interactive exercises at every level',
    () {
      final workshops = content.allTopics
          .where((t) => t.subject == 'technology' && t.generator == 'workshop')
          .toList();
      expect(workshops.length, 13);
      for (final t in workshops) {
        for (var level = 1; level <= 3; level++) {
          for (var seed = 0; seed < 10; seed++) {
            final lesson = LessonBuilder.build(
              content: content,
              topic: t,
              level: level,
              count: 6,
              age: 11,
              rng: Random(seed),
            );
            expect(lesson.length, 6, reason: '${t.id}: $level/$seed');
            expect(
              lesson.every(
                (e) =>
                    e.kind != ExerciseKind.choice &&
                    ExerciseValidator.isPlayable(e),
              ),
              isTrue,
            );
            expect(lesson.map((e) => e.signature).toSet().length, 6);
          }
        }
      }
    },
  );
  test('all authored tasks validate, including group assignments and circuit starts', () {
    for (final entry in content.banks.entries.where(
      (e) => e.key.startsWith('technology_'),
    )) {
      final t = content.topic(entry.key)!;
      expect(entry.value.length, greaterThanOrEqualTo(16));
      for (final source in entry.value) {
        for (var level = 1; level <= 3; level++) {
          final e = BankGen.fromItem(
            GenContext(
              rng: Random(12),
              content: content,
              topic: t,
              level: level,
              age: 11,
            ),
            source,
          );
          expect(
            ExerciseValidator.isPlayable(e),
            isTrue,
            reason: '${entry.key}/${source['id']}',
          );
          if (e.sort != null) {
            final expected = {
              for (final row in source['items'] as List) row[0]: row[1],
            };
            for (var i = 0; i < e.sort!.items.length; i++) {
              expect(e.sort!.itemBins[i], expected[e.sort!.items[i].text]);
            }
          }
        }
      }
    }
  });
  test('lamp requires both wires and a closed switch for all eight states', () {
    for (var state = 0; state < 8; state++) {
      expect(
        CircuitTask.lampLit((state & 1) != 0, (state & 2) != 0, (state & 4) != 0),
        state == 7,
      );
    }
  });
  testWidgets(
    'circuit: incomplete loop cannot pass; the bulb responds live; award once',
    (tester) async {
      final e = item('technology_g5.mechanisms', 'circuit', targetLit: true);
      final mistakes = <int>[];
      final solved = <int>[];
      await host(
        tester,
        CircuitExerciseView(
          exercise: e,
          callbacks: ExerciseCallbacks(
            onMistake: mistakes.add,
            onSolved: solved.add,
          ),
        ),
      );
      await tap(tester, const Key('circuit_switch'));
      await tap(tester, const Key('circuit_check'));
      expect(mistakes, [1]);
      expect(solved, isEmpty);
      expect(find.byKey(const ValueKey('lamp_off')), findsOneWidget);
      await tap(tester, const Key('circuit_wire_a'));
      await tap(tester, const Key('circuit_wire_b'));
      expect(find.byKey(const ValueKey('lamp_on')), findsOneWidget);
      await tap(tester, const Key('circuit_check'));
      await tap(tester, const Key('circuit_check'));
      expect(solved, [1]);
      expect(tester.takeException(), isNull);
    },
  );
  testWidgets(
    'switch-off task requires intact wires, not a disconnected circuit',
    (tester) async {
      final e = item('technology_g5.mechanisms', 'circuit', targetLit: false);
      final solved = <int>[];
      await host(
        tester,
        CircuitExerciseView(
          exercise: e,
          callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: solved.add),
        ),
      );
      await tap(tester, const Key('circuit_wire_a'));
      await tap(tester, const Key('circuit_check'));
      expect(solved, isEmpty);
      await tap(tester, const Key('circuit_wire_a'));
      await tap(tester, const Key('circuit_switch'));
      await tap(tester, const Key('circuit_check'));
      expect(solved, [1]);
      expect(tester.takeException(), isNull);
    },
  );
  testWidgets(
    'process cards: wrong step remains unplaced; ordered steps finish',
    (tester) async {
      final e = item('technology_g3.paper', 'order');
      final task = e.assemble!;
      final solved = <int>[];
      await host(
        tester,
        WorkshopOrderExerciseView(
          exercise: e,
          callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: solved.add),
        ),
      );
      final wrong = task.tiles.indexWhere((v) => v != task.answer.first);
      await tap(tester, ValueKey('workshop_step_$wrong'));
      expect(solved, isEmpty);
      for (final step in task.answer) {
        await tap(
          tester,
          ValueKey('workshop_step_${task.tiles.indexOf(step)}'),
        );
      }
      expect(solved, [1]);
      expect(tester.takeException(), isNull);
    },
  );
  testWidgets(
    'material sorting: incorrect bin is a mistake, then all cards solve',
    (tester) async {
      final e = item('technology_g3.reuse', 'sort');
      final task = e.sort!;
      final solved = <int>[];
      await host(
        tester,
        WorkshopSortExerciseView(
          exercise: e,
          callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: solved.add),
        ),
      );
      await tap(tester, const ValueKey('workshop_item_0'));
      await tap(tester, ValueKey('workshop_bin_${1 - task.itemBins[0]}'));
      expect(solved, isEmpty);
      for (var i = 0; i < task.items.length; i++) {
        await tap(tester, ValueKey('workshop_item_$i'));
        await tap(tester, ValueKey('workshop_bin_${task.itemBins[i]}'));
      }
      expect(solved, [1]);
      expect(tester.takeException(), isNull);
    },
  );
  testWidgets('long school grammar pairs wrap and remain tappable on a narrow phone', (tester) async {
    final e = item('english_g8.unit2', 'match');
    final solved = <int>[];
    await host(tester, MatchExerciseView(exercise: e,
      callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: solved.add)));
    expect(tester.widgetList<OptionCard>(find.byType(OptionCard)).every((w) => w.wrapText), isTrue);
    for (final pair in e.pairs) {
      for (final text in [pair.left.text, pair.right.text]) {
        final card = find.byWidgetPredicate((w) => w is OptionCard && w.option.text == text);
        await tester.ensureVisible(card);
        await tester.tap(card);
        await tester.pumpAndSettle();
      }
    }
    expect(solved, [0]);
    expect(tester.takeException(), isNull);
  });
  testWidgets('long Technology match cards fit a narrow phone', (tester) async {
    final e = item('technology_g5.materials', 'match');
    await host(
      tester,
      MatchExerciseView(
        exercise: e,
        callbacks: ExerciseCallbacks(onMistake: (_) {}, onSolved: (_) {}),
      ),
    );
    expect(find.byType(OptionCard), findsNWidgets(e.pairs.length * 2));
    expect(tester.takeException(), isNull);
  });
}
