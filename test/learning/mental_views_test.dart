import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/models/visual.dart';
import 'package:academy/learning/ui/abacus_view.dart';
import 'package:academy/learning/ui/input_view.dart';
import 'package:academy/learning/ui/visual_view.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

/// Mental arifmetika ekranlari: abakusda son qo'yish va flesh-anzan.
void main() {
  late ContentRepository content;

  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    content = await ContentRepository.load();
  });

  Exercise make(String topicId, int level, {int seed = 3}) {
    final t = content.topic(topicId)!;
    final gen = GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator)!;
    return gen(GenContext(rng: Random(seed), content: content, topic: t, level: level, age: 9));
  }

  Future<void> host(WidgetTester tester, Widget child) async {
    tester.view.physicalSize = const Size(1080, 2000);
    tester.view.devicePixelRatio = 2.5;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(MaterialApp(home: Scaffold(body: Padding(padding: const EdgeInsets.all(8), child: child))));
    await tester.pump();
  }

  /// Ustunga raqam qo'yish (bo'sh ustundan): yuqori munchoq + kerakli pastki munchoq.
  Future<void> setDigit(WidgetTester tester, int rod, int digit) async {
    if (digit >= 5) {
      await tester.tap(find.byKey(ValueKey('bead_${rod}_u')));
      await tester.pump(const Duration(milliseconds: 200));
    }
    if (digit % 5 > 0) {
      await tester.tap(find.byKey(ValueKey('bead_${rod}_${digit % 5 - 1}')));
      await tester.pump(const Duration(milliseconds: 200));
    }
  }

  testWidgets('abakus rasmi: son to‘g‘ri chiziladi', (tester) async {
    await host(tester, const Center(child: SizedBox(height: 300, child: VisualView(visual: AbacusVisual(47, rods: 2)))));
    final view = tester.widget<AbacusView>(find.byType(AbacusView));
    expect(view.digits, [4, 7]);
    expect(AbacusView.valueOf(view.digits), 47);
    expect(tester.takeException(), isNull);
  });

  testWidgets('abakusda son qo‘yish: munchoqlarni bosib javob beriladi', (tester) async {
    Exercise? e;
    for (var seed = 1; seed < 50 && e == null; seed++) {
      final x = make('mental_g2.set2', 1, seed: seed);
      if (x.input!.isAbacus && x.input!.answer.length == 2) e = x;
    }
    final task = e!.input!;
    int? solved;
    final mistakes = <int>[];
    await host(tester, InputExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m)));
    expect(find.byType(AbacusView), findsOneWidget);
    // Bo'sh abakusda tekshirib bo'lmaydi.
    expect(tester.widget<FilledButton>(find.byKey(const ValueKey('input_check'))).onPressed, isNull);

    // Avval noto'g'ri son: birlarga 1 (yoki 2).
    final wrongDigit = task.answer.endsWith('1') ? 2 : 1;
    await setDigit(tester, 1, wrongDigit);
    await tester.tap(find.byKey(const ValueKey('input_check')));
    await tester.pump();
    expect(mistakes, [1]);

    await tester.tap(find.byKey(const ValueKey('abacus_clear')));
    await tester.pump(const Duration(milliseconds: 200));
    final digits = AbacusVisual.digitsOf(int.parse(task.answer), 2);
    for (var r = 0; r < 2; r++) {
      await setDigit(tester, r, digits[r]);
    }
    expect(AbacusView.valueOf(tester.widget<AbacusView>(find.byType(AbacusView)).digits), int.parse(task.answer));
    await tester.tap(find.byKey(const ValueKey('input_check')));
    await tester.pump();
    expect(solved, 1);
  });

  testWidgets('flesh-anzan: sonlar ko‘rsatiladi, keyin javob yoziladi', (tester) async {
    final e = make('mental_g1.flash_simple', 1);
    final task = e.input!;
    expect(task.flash, isNotEmpty);
    int? solved;
    final mistakes = <int>[];
    await host(tester, InputExerciseView(exercise: e, callbacks: ExerciseCallbacks(onMistake: mistakes.add, onSolved: (m) => solved = m)));
    // Boshlashdan oldin klaviatura yopiq.
    expect(tester.widget<OutlinedButton>(find.byKey(const ValueKey('key_1'))).onPressed, isNull);
    String shown() => tester.widget<Text>(find.byKey(const ValueKey('flash_number'))).data!;
    await tester.tap(find.byKey(const ValueKey('flash_start')));
    await tester.pump();
    expect(shown(), task.flash.first);
    await tester.pump(Duration(milliseconds: task.flashMs + 300));
    expect(shown(), task.flash[1]);
    await tester.pump(Duration(milliseconds: (task.flashMs + 300) * task.flash.length));
    expect(find.byKey(const ValueKey('flash_replay')), findsNothing);

    Future<void> type(String v) async {
      for (final c in v.split('')) {
        await tester.tap(find.byKey(ValueKey('key_$c')));
        await tester.pump();
      }
      await tester.tap(find.byKey(const ValueKey('input_check')));
      await tester.pump();
    }

    await type(task.answer == '9' ? '8' : '9');
    expect(mistakes, [1]);
    // Xatodan keyin sonlarni yana ko'rish mumkin.
    expect(find.byKey(const ValueKey('flash_replay')), findsOneWidget);
    await type(task.answer);
    expect(solved, 1);
  });
}
