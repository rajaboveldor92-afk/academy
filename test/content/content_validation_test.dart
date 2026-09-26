import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/content/uzbek_data.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/puzzles.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/models/topic.dart';
import 'package:academy/learning/models/visual.dart';
import 'package:flutter_test/flutter_test.dart';

/// KONTENTNI AVTOMATIK TEKSHIRISH (spetsifikatsiya 31-band).
///
/// Har bir mavzu × daraja uchun ko'p sonli mashq generatsiya qilinadi va
/// quyidagilar tekshiriladi: bo'sh savol/variant, dublikat variantlar,
/// to'g'ri javob variantlar ichida va yagona, matematik to'g'rilik,
/// yoshga moslik (son chegaralari), Android 9 da ko'rinmaydigan emoji,
/// tarjimalar to'liqligi, har darajada kamida 15 ta turli savol.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  /// Android 9 (Emoji 11) da yo'q emoji'lar — kontentda uchramasligi kerak.
  const unsupportedEmoji = [
    '🪜', '🫥', '🪙', '🪶', '🧍', '🧃', '🪑', '🧼', '🪥', '🪁', '🧅', '🧄', '🫐', '🦫', '🪴', '🛝',
  ];

  const samplesPerLevel = 120;

  int ageFor(Topic t) => t.ageSuffix == '4' ? 4 : 6;

  /// Variantlar tartibiga bog'liq bo'lmagan "ma'no" kaliti.
  String semanticKey(Exercise e) {
    final opts = e.options.map((o) => o.describe()).toList()..sort();
    final pairs = e.pairs.map((p) => '${p.left.describe()}=${p.right.describe()}').toList()..sort();
    return [
      e.instruction.uz,
      e.speech,
      e.speechParts.join('+'),
      e.visual?.describe() ?? '',
      opts.join('|'),
      pairs.join('|'),
      e.sort?.items.map((i) => i.describe()).join('|') ?? '',
      e.maze?.describe() ?? '',
      e.sudoku?.describe() ?? '',
      e.coding?.describe() ?? '',
      e.previewVisual?.describe() ?? '',
      e.assemble?.describe() ?? '',
      e.trace?.describe() ?? '',
      e.chess?.describe() ?? '',
    ].join('#');
  }

  Iterable<String> allText(Exercise e) sync* {
    yield e.instruction.uz;
    yield e.instruction.en;
    yield e.instruction.ru;
    yield e.visual?.describe() ?? '';
    yield e.previewVisual?.describe() ?? '';
    for (final o in e.options) {
      yield o.describe();
    }
    for (final p in e.pairs) {
      yield p.left.describe();
      yield p.right.describe();
    }
    final s = e.sort;
    if (s != null) {
      for (final o in [...s.bins, ...s.items]) {
        yield o.describe();
      }
    }
    if (e.maze != null) yield '${e.maze!.hero}${e.maze!.target}';
    if (e.sudoku != null) yield e.sudoku!.symbols.join();
    if (e.coding != null) yield '${e.coding!.hero}${e.coding!.target}';
    if (e.assemble != null) yield e.assemble!.tiles.join(' ');
    if (e.trace?.label != null) yield e.trace!.label!;
  }

  /// Har bir daraja uchun kamida shuncha turli savol. Yozish mashqlarida elementlar
  /// ro'yxati qisqa (masalan, 5 ta harf) — ularning har biri alohida tekshiriladi.
  int minUnique(Topic t, int level) {
    // Shaxmat: AI bilan o'yin — bitta boshlang'ich pozitsiya; figura nomlari — 6 ta figura.
    if (t.subject == 'chess' && t.generator == 'play') return 1;
    if (t.subject == 'chess' && t.generator == 'piece_name') return 6;
    if (t.generator != 'trace') return 15;
    final items = (t.paramsFor(level)['items'] as List).map((e) => '$e').toList();
    if (items.any((i) => i.startsWith('words:'))) return 10;
    return min(3, items.length);
  }

  /// Matematik to'g'rilikni meta ma'lumotlar orqali mustaqil tekshiradi.
  void checkMath(Exercise e) {
    final m = e.meta;
    final a = m['a'], b = m['b'], answer = m['answer'];
    final op = m['op'];
    if (a is int && b is int && answer is int && op == '+' && !m.containsKey('form')) {
      if (m.containsKey('total')) {
        expect(a + answer, m['total'], reason: '${e.topicId}: $a + ? = ${m['total']}');
      } else {
        expect(answer, a + b, reason: '${e.topicId}: $a + $b');
      }
    }
    if (a is int && b is int && answer is int && op == '-' && !m.containsKey('form')) {
      expect(answer, a - b, reason: '${e.topicId}: $a - $b');
      expect(answer, greaterThanOrEqualTo(0));
    }
    if (op == 'cmp') {
      final x = a as int, y = b as int;
      expect(answer, x > y ? '>' : (x < y ? '<' : '='), reason: e.topicId);
    }
    if (m.containsKey('form')) {
      final aa = m['a'] as int, bb = m['b'] as int, cc = m['c'] as int;
      expect(aa + bb, cc);
      final expected = switch (m['form']) {
        '?+b=c' => aa,
        'a-?=b' => bb,
        '?-a=b' => cc,
        _ => bb,
      };
      expect(answer, expected, reason: '${e.topicId} ${m['form']}');
    }
    if (m.containsKey('start') && m.containsKey('step') && m.containsKey('index')) {
      expect(answer, (m['start'] as int) + (m['step'] as int) * (m['index'] as int) - (e.topicId.contains('by_') ? 0 : 0),
          reason: '${e.topicId} sequence');
    }
    if (m.containsKey('groups') && m.containsKey('step')) {
      expect(answer, (m['groups'] as int) * (m['step'] as int));
    }
    if (m.containsKey('count') && e.visual is SceneVisual) {
      final items = (e.visual! as SceneVisual).items.where((i) => i.kind == SceneKind.emoji).length;
      expect(items, m['count'], reason: '${e.topicId}: sahnadagi narsalar soni');
    }
    if (m.containsKey('coins')) {
      final sum = (m['coins'] as String).split('+').map(int.parse).fold<int>(0, (s, v) => s + v);
      expect(sum, answer);
    }
    if (m.containsKey('tens')) {
      expect(answer, (m['tens'] as int) * 10 + (m['ones'] as int));
    }
    if (m.containsKey('hour') && m.containsKey('minute')) {
      expect(m['hour'] as int, inInclusiveRange(1, 12));
      expect(m['minute'], anyOf(0, 30));
    }
  }

  /// To'g'ri variant meta'dagi javobga mos va yagona bo'lishi kerak.
  void checkCorrectOption(Exercise e) {
    final answer = e.meta['answer'];
    if (e.options.isEmpty) return;
    final correct = e.options[e.correctIndex];
    if (answer is int && correct.text != null && int.tryParse(correct.text!) != null) {
      expect(correct.text, '$answer', reason: '${e.topicId}: to‘g‘ri variant');
      final same = e.options.where((o) => o.text == '$answer').length;
      expect(same, 1, reason: '${e.topicId}: bir nechta to‘g‘ri javob');
    }
    if (answer is int && (correct.text ?? '').endsWith('so‘m')) {
      expect(correct.text, '$answer so‘m');
    }
    if (answer is String && e.meta['op'] == 'cmp') {
      expect(correct.text, answer);
    }
    if (e.meta.containsKey('hour') && answer is String) {
      expect(correct.text, answer);
    }
  }

  test('lug‘at: ID noyob, uch tilda to‘liq', () {
    final ids = <String>{};
    for (final e in content.lexicon.entries) {
      expect(ids.add(e.id), isTrue, reason: 'dublikat ${e.id}');
      expect(e.word.isComplete, isTrue, reason: e.id);
      expect(e.emoji.trim(), isNotEmpty, reason: e.id);
      for (final bad in unsupportedEmoji) {
        expect(e.emoji.contains(bad), isFalse, reason: '${e.id}: $bad');
      }
    }
    expect(content.lexicon.entries.length, greaterThanOrEqualTo(200));
    for (final c in content.lexicon.colors) {
      expect(c.name.isComplete, isTrue);
    }
    for (final s in content.lexicon.shapes) {
      expect(s.name.isComplete, isTrue);
    }
  });

  test('ko‘rsatmalar: uch tilda, o‘rinbosarlar mos', () {
    final ph = RegExp(r'\{(\w+)(?::\w+)?\}');
    for (final key in content.instructions.keys) {
      final t = content.instructions.template(key)!;
      for (final lang in ['uz', 'en', 'ru']) {
        expect((t[lang] ?? '').trim(), isNotEmpty, reason: '$key/$lang');
      }
      Set<String> names(String s) => ph.allMatches(s).map((m) => m.group(1)!).toSet();
      if (key.startsWith('lg_')) {
        // Chet tili darsi: o'zbekcha matn — umumiy yordamchi (javobni oshkor qilmaydi).
        expect(names(t['ru']!), names(t['en']!), reason: '$key ru');
        expect(names(t['en']!).containsAll(names(t['uz']!)), isTrue, reason: '$key uz');
      } else {
        expect(names(t['en']!), names(t['uz']!), reason: '$key en');
        expect(names(t['ru']!), names(t['uz']!), reason: '$key ru');
      }
    }
  });

  test('dasturlar: mavzular noyob, generatorlar mavjud, oldingi mavzular to‘g‘ri', () {
    final ids = <String>{};
    for (final t in content.allTopics) {
      expect(ids.add(t.id), isTrue, reason: 'dublikat ${t.id}');
      expect(t.title.isComplete, isTrue, reason: t.id);
      expect(t.maxLevel, 3, reason: '${t.id}: 3 daraja bo‘lishi kerak');
      expect(GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator), isNotNull,
          reason: '${t.id}: generator ${t.generator}');
    }
    for (final t in content.allTopics) {
      for (final p in t.prerequisites) {
        expect(ids.contains(p), isTrue, reason: '${t.id} -> $p');
      }
    }
    expect(content.curriculum('math', '4')!.topics.length, 15);
    expect(content.curriculum('math', '6')!.topics.length, 20);
    expect(content.curriculum('logic', '4')!.topics.length, 15);
    expect(content.curriculum('logic', '6')!.topics.length, 15);
    expect(content.curriculum('uzbek', '4')!.topics.length, greaterThanOrEqualTo(15));
    expect(content.curriculum('uzbek', '6')!.topics.length, 14);
    expect(content.curriculum('writing', '4')!.topics.length, greaterThanOrEqualTo(5));
    expect(content.curriculum('writing', '6')!.topics.length, greaterThanOrEqualTo(6));
    expect(content.curriculum('english', '4')!.topics.length, greaterThanOrEqualTo(15));
    expect(content.curriculum('english', '6')!.topics.length, greaterThanOrEqualTo(20));
    expect(content.curriculum('russian', '4')!.topics.length, greaterThanOrEqualTo(12));
    expect(content.curriculum('russian', '6')!.topics.length, 15);
    expect(content.curriculum('trilingual', '4')!.topics.length, greaterThanOrEqualTo(6));
    expect(content.curriculum('trilingual', '6')!.topics.length, greaterThanOrEqualTo(6));
    // Shaxmat: 4 yosh — 12 qadam, 6 yosh — 20 qadam.
    expect(content.curriculum('chess', '4')!.topics.length, 12);
    expect(content.curriculum('chess', '6')!.topics.length, 20);
  });

  test('o‘zbek tili bazasi: alifbo, bo‘g‘inlar, rasmlar', () {
    final uz = content.uzbek;
    expect(uz.alphabet.length, 29, reason: 'lotin alifbosi: 24 harf + O‘ G‘ Sh Ch Ng');
    for (final l in uz.alphabet) {
      expect(content.lexicon.contains(l.lexId), isTrue, reason: 'harf ${l.upper}: ${l.lexId}');
      // "Ng" so'z boshida kelmaydi — so'z ichida bo'lsa yetarli (tong).
      final letters = UzbekData.letters(l.word);
      expect(l.lower == 'ng' ? letters.contains('ng') : letters.first == l.lower, isTrue, reason: '${l.upper} — ${l.word}');
      expect(l.vowel, UzbekData.isVowel(l.lower), reason: l.upper);
    }
    final seen = <String>{};
    for (final w in uz.words) {
      expect(seen.add(w.word), isTrue, reason: 'dublikat so‘z ${w.word}');
      expect(w.syllables.join(), w.word, reason: 'bo‘g‘inlar: ${w.syllables} ≠ ${w.word}');
      for (final syl in w.syllables) {
        final vowels = UzbekData.letters(syl).where(UzbekData.isVowel).length;
        expect(vowels, 1, reason: '${w.word}: "$syl" bo‘g‘inida bitta unli bo‘lishi kerak');
      }
      if (w.lexId != null) {
        expect(content.lexicon.contains(w.lexId!), isTrue, reason: '${w.word}: ${w.lexId}');
      }
      expect(w.age, anyOf(4, 6), reason: w.word);
    }
    // Spetsifikatsiya: 4 yosh — kamida 250 so'z, 6 yosh — kamida 500 so'z.
    expect(uz.forAge(4).length, greaterThanOrEqualTo(250));
    expect(uz.forAge(6).length, greaterThanOrEqualTo(500));
    expect(uz.picturable(4).length, greaterThanOrEqualTo(200));
    expect(uz.names.length, greaterThanOrEqualTo(8));
    expect(UzbekData.letters('qo‘ng‘iroq'), ['q', 'o‘', 'n', 'g‘', 'i', 'r', 'o', 'q']);
    expect(UzbekData.letters('choynak'), ['ch', 'o', 'y', 'n', 'a', 'k']);
    expect(UzbekData.letters('tong'), ['t', 'o', 'ng']);
  });

  test('yozish: har bir harf, raqam va element uchun chiziqlar bor', () {
    final bank = content.glyphs;
    for (final l in content.uzbek.alphabet) {
      expect(bank.letter(l.upper), isNotNull, reason: 'harf ${l.upper}');
    }
    for (var d = 0; d <= 9; d++) {
      expect(bank.letter('$d'), isNotNull, reason: 'raqam $d');
    }
    for (final topic in content.allTopics.where((t) => t.generator == 'trace')) {
      for (var level = 1; level <= topic.maxLevel; level++) {
        for (final item in (topic.paramsFor(level)['items'] as List).map((e) => '$e')) {
          final parts = item.split(':');
          final id = parts.sublist(1).join(':');
          final ok = switch (parts.first) {
            'pre' => bank.prewriting.containsKey(id),
            'dots' => bank.dots.containsKey(id),
            'glyph' => bank.letter(id) != null,
            'words' => int.tryParse(id) != null,
            _ => false,
          };
          expect(ok, isTrue, reason: '${topic.id} L$level: $item');
        }
      }
    }
  });

  group('yozishni baholash (TraceScorer)', () {
    const tolerances = [0.085, 0.11];
    const scribbles = <String, List<List<Point2>>>{
      'zigzag': [
        [Point2(0, 0), Point2(1, .2), Point2(0, .4), Point2(1, .6), Point2(0, .8), Point2(1, 1)],
      ],
      'zigzag_v': [
        [Point2(0, 0), Point2(.2, 1), Point2(.4, 0), Point2(.6, 1), Point2(.8, 0), Point2(1, 1)],
      ],
      'frame': [
        [Point2(.05, .05), Point2(.95, .05), Point2(.95, .95), Point2(.05, .95), Point2(.05, .05)],
      ],
    };

    Map<String, TraceTask> tasks(double tol) {
      final bank = content.glyphs;
      const wide = {'zigzag', 'zigzag2', 'wave', 'waves2', 'loops', 'steps', 'horizontal'};
      return {
        for (final e in bank.glyphs.entries) 'glyph:${e.key}': TraceTask(id: e.key, strokes: e.value, tolerance: tol),
        for (final e in bank.prewriting.entries)
          'pre:${e.key}': TraceTask(id: e.key, strokes: e.value, tolerance: tol, aspect: wide.contains(e.key) ? 1.6 : 1),
        for (final e in bank.dots.entries) 'dots:${e.key}': TraceTask(id: e.key, strokes: [e.value], dots: true, tolerance: tol),
      };
    }

    test('namuna bo‘yicha aniq yozish o‘tadi', () {
      for (final tol in tolerances) {
        tasks(tol).forEach((name, t) {
          expect(TraceScorer.passed(t, t.strokes), isTrue, reason: '$name ($tol): ${TraceScorer.evaluate(t, t.strokes)}');
        });
      }
    });

    /// Silliq tebranish: chetga og'ish sekin o'zgaradi (qo'l titrashi kabi), maksimal [amt].
    List<Point2> wobble(List<Point2> stroke, double amt, double aspect, Random rng) {
      var ox = 0.0, oy = 0.0;
      final out = <Point2>[];
      for (final p in stroke) {
        ox = (ox + (rng.nextDouble() - 0.5) * amt / 1.5).clamp(-amt, amt).toDouble();
        oy = (oy + (rng.nextDouble() - 0.5) * amt / 1.5).clamp(-amt, amt).toDouble();
        out.add(Point2(p.x + ox / aspect, p.y + oy));
      }
      return out;
    }

    test('yumshoq tebranish bilan yozish ham o‘tadi', () {
      final rng = Random(5);
      for (final tol in tolerances) {
        tasks(tol).forEach((name, t) {
          final drawn = [for (final s in t.strokes) wobble(s, tol * 0.5, t.aspect, rng)];
          expect(TraceScorer.passed(t, drawn), isTrue, reason: '$name ($tol): ${TraceScorer.evaluate(t, drawn)}');
        });
      }
    });

    test('tartibsiz chizish (bo‘yab tashlash) o‘tmaydi', () {
      for (final tol in tolerances) {
        tasks(tol).forEach((name, t) {
          scribbles.forEach((sName, drawn) {
            expect(TraceScorer.passed(t, drawn), isFalse, reason: '$name ($tol) — $sName: ${TraceScorer.evaluate(t, drawn)}');
          });
        });
      }
    });

    test('bitta chiziq tushib qolsa o‘tmaydi', () {
      for (final tol in tolerances) {
        tasks(tol).forEach((name, t) {
          if (t.dots || t.strokes.length < 2) return;
          for (var i = 0; i < t.strokes.length; i++) {
            final drawn = [for (var j = 0; j < t.strokes.length; j++) if (j != i) t.strokes[j]];
            expect(TraceScorer.passed(t, drawn), isFalse, reason: '$name ($tol) — $i-chiziqsiz');
          }
        });
      }
    });

    test('chapdan o‘ngga talabi: teskari yozish o‘tmaydi', () {
      final line = content.glyphs.prewriting['horizontal']!;
      final t = TraceTask(id: 'h', strokes: line, tolerance: 0.1, leftToRight: true, aspect: 1.6);
      expect(TraceScorer.passed(t, line), isTrue);
      final reversed = [for (final s in line) s.reversed.toList()];
      expect(TraceScorer.passed(t, reversed), isFalse);
    });

    test('so‘zlar: namuna o‘tadi, maydon keng', () {
      final bank = content.glyphs;
      for (final word in ['ota', 'ona', 'olma', 'choy', 'o‘q', 'shar']) {
        final strokes = bank.word(word)!;
        final t = TraceTask(id: word, strokes: strokes, tolerance: 0.1, aspect: GlyphBank.wordAspect(word), minCoverage: 0.8);
        expect(TraceScorer.passed(t, strokes), isTrue, reason: word);
        expect(TraceScorer.passed(t, scribbles['zigzag']!), isFalse, reason: word);
        for (final s in strokes) {
          for (final p in s) {
            expect(p.x, inInclusiveRange(-0.01, 1.01), reason: word);
          }
        }
      }
    });
  });

  test('barcha mashqlar: to‘g‘ri, yagona javobli, yoshga mos, xilma-xil', () {
    final report = <String, int>{};
    for (final topic in content.allTopics) {
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      var topicUnique = 0;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 7919 + topic.id.hashCode);
        final unique = <String>{};
        for (var i = 0; i < samplesPerLevel; i++) {
          final ctx = GenContext(rng: rng, content: content, topic: topic, level: level, age: ageFor(topic));
          final Exercise e;
          try {
            e = gen(ctx);
          } catch (err) {
            fail('${topic.id} L$level: generator xatosi: $err');
          }
          final where = '${topic.id} L$level';
          expect(ExerciseValidator.isPlayable(e), isTrue, reason: '$where: o‘ynab bo‘lmaydi');
          expect(e.instruction.isComplete, isTrue, reason: '$where: tarjima');
          expect(e.instruction.uz.contains('{'), isFalse, reason: '$where: ${e.instruction.uz}');
          expect(RegExp(r'\d').hasMatch(e.speech), isFalse, reason: '$where: ovozda raqam: ${e.speech}');
          for (final text in allText(e)) {
            for (final bad in unsupportedEmoji) {
              expect(text.contains(bad), isFalse, reason: '$where: $bad');
            }
          }
          checkMath(e);
          checkCorrectOption(e);
          // Yoshga moslik: 4 yosh — 10 gacha, 6 yosh — 100 gacha.
          final ans = e.meta['answer'];
          if (topic.subject == 'math' && ans is int) {
            expect(ans, inInclusiveRange(0, topic.ageSuffix == '4' ? 10 : 100), reason: where);
          }
          if (e.kind == ExerciseKind.sudoku) {
            expect(PuzzleFactory.isValidSudoku(e.sudoku!), isTrue, reason: where);
          }
          if (e.kind == ExerciseKind.coding) {
            expect(PuzzleFactory.solveCoding(e.coding!), isNotNull, reason: where);
          }
          if (e.kind == ExerciseKind.maze) {
            expect(e.maze!.shortestPath(), isNotNull, reason: where);
          }
          if (e.kind == ExerciseKind.assemble) {
            final a = e.assemble!;
            final pool = List<String>.from(a.tiles);
            for (final part in a.answer) {
              expect(pool.remove(part), isTrue, reason: '$where: "$part" bo‘lagi yo‘q');
            }
            expect(a.answer.every((p) => p.trim().isNotEmpty), isTrue, reason: where);
            if (a.answer.toSet().length > 1 && a.tiles.length >= a.answer.length) {
              expect(a.tiles.take(a.answer.length).toList(), isNot(equals(a.answer)), reason: '$where: bo‘laklar aralashmagan');
            }
          }
          if (e.kind == ExerciseKind.trace) {
            final t = e.trace!;
            // Namunaning o'zi (aniq chizilgan) o'tishi shart.
            expect(TraceScorer.passed(t, t.strokes), isTrue, reason: '$where ${t.id}: ${TraceScorer.evaluate(t, t.strokes)}');
            for (final s in t.strokes) {
              for (final p in s) {
                expect(p.x, inInclusiveRange(-0.02, 1.02), reason: where);
                expect(p.y, inInclusiveRange(-0.02, 1.02), reason: where);
              }
            }
          }
          unique.add(semanticKey(e));
        }
        expect(unique.length, greaterThanOrEqualTo(minUnique(topic, level)),
            reason: '${topic.id} L$level: faqat ${unique.length} ta turli savol');
        topicUnique += unique.length;
      }
      final key = '${topic.subject}_${topic.ageSuffix}';
      report[key] = (report[key] ?? 0) + topicUnique;
    }
    // Spetsifikatsiya 29-band: minimal kontent hajmi.
    expect(report['math_4']!, greaterThanOrEqualTo(250));
    expect(report['logic_4']!, greaterThanOrEqualTo(200));
    expect(report['math_6']!, greaterThanOrEqualTo(500));
    expect(report['logic_6']!, greaterThanOrEqualTo(300));
    expect(report['uzbek_4']!, greaterThanOrEqualTo(250));
    expect(report['uzbek_6']!, greaterThanOrEqualTo(500));
    expect(report['english_4']!, greaterThanOrEqualTo(250));
    expect(report['english_6']!, greaterThanOrEqualTo(500));
    expect(report['russian_4']!, greaterThanOrEqualTo(250));
    expect(report['russian_6']!, greaterThanOrEqualTo(500));
    expect(report['trilingual_4']!, greaterThanOrEqualTo(120));
    expect(report['trilingual_6']!, greaterThanOrEqualTo(200));
    // ignore: avoid_print
    print('Kontent hisoboti (turli savollar soni): $report');
  });

  test('har bir mavzu va daraja uchun to‘liq dars tuziladi', () {
    for (final topic in content.allTopics) {
      final c = content.curriculum(topic.subject, topic.ageSuffix)!;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final lesson = LessonBuilder.build(
          content: content,
          topic: topic,
          level: level,
          count: topic.lessonSize ?? c.lessonSize,
          age: ageFor(topic),
          rng: Random(level),
        );
        expect(lesson.length, topic.lessonSize ?? c.lessonSize, reason: '${topic.id} L$level');
        expect(lesson.map(LessonBuilder.signatureHash).toSet().length, lesson.length,
            reason: '${topic.id} L$level: darsda takror');
      }
    }
  });

  test('takrorlanmaslik: avval ko‘rilgan savollar chetlab o‘tiladi', () {
    final topic = content.topic('math6.add_10')!;
    final first = LessonBuilder.build(content: content, topic: topic, level: 2, count: 10, age: 6, rng: Random(1));
    final seen = first.map(LessonBuilder.signatureHash).toSet();
    final second = LessonBuilder.build(
      content: content, topic: topic, level: 2, count: 10, age: 6, rng: Random(2), avoid: seen,
    );
    final repeats = second.where((e) => seen.contains(LessonBuilder.signatureHash(e))).length;
    expect(repeats, 0);
  });
}
