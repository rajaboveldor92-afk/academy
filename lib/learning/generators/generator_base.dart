import 'dart:math';

import 'package:flutter/painting.dart';

import '../content/content_repository.dart';
import '../content/instructions.dart';
import '../content/lexicon.dart';
import '../content/uzbek_data.dart';
import '../models/exercise.dart';
import '../models/topic.dart';
import '../models/visual.dart';

/// Generator funksiyasi: kontekstdan bitta mashq yaratadi.
typedef ExerciseGenerator = Exercise Function(GenContext ctx);

/// Generatorga beriladigan hamma narsa: tasodif manbai, kontent, mavzu, daraja.
class GenContext {
  GenContext({
    required this.rng,
    required this.content,
    required this.topic,
    required this.level,
    this.age = 6,
    this.lang = 'uz',
  }) : params = topic.paramsFor(level);

  final Random rng;
  final ContentRepository content;
  final Topic topic;
  final int level;
  final int age;

  /// Bolaning tili (`uz`, `ru`, `en`): maslahat, izoh va variant matnlari shu tilda.
  final String lang;
  final Map<String, dynamic> params;

  /// Ko'rsatma tili: O'zbek tili va Yozish darslari o'zbekcha (so'zlar o'zbekcha),
  /// qolgan fanlar — bolaning tilida. Chet tili darslari [sayIn] bilan o'z tilida.
  String get instructionLang => const {'uzbek', 'writing'}.contains(topic.subject) ? 'uz' : lang;

  /// Matnning bolaning tilidagi varianti.
  String tr(String uz, String en, String ru) => switch (lang) {
        'ru' => ru,
        'en' => en,
        _ => uz,
      };

  /// Pul birligi.
  String get sum => tr('so‘m', 'sum', 'сум');

  Lexicon get lex => content.lexicon;

  UzbekData get uz => content.uzbek;

  bool get junior => age <= 5;

  int p(String key, int fallback) {
    final v = params[key];
    return v is num ? v.toInt() : fallback;
  }

  String ps(String key, String fallback) => params[key]?.toString() ?? fallback;

  bool pb(String key, [bool fallback = false]) {
    final v = params[key];
    return v is bool ? v : fallback;
  }

  List<String> pl(String key) {
    final v = params[key];
    return v is List ? v.map((e) => e.toString()).toList() : const [];
  }

  // ------------------------------------------------------------ tasodif

  int range(int min, int max) => min + rng.nextInt(max - min + 1);

  T pick<T>(List<T> list) => list[rng.nextInt(list.length)];

  List<T> sample<T>(List<T> list, int n) {
    final copy = List<T>.from(list)..shuffle(rng);
    return copy.take(n).toList();
  }

  bool chance(double p) => rng.nextDouble() < p;

  /// Bo'laklarni aralashtiradi: boshidagi bo'laklar to'g'ri javob tartibida qolib ketmasin
  /// (aks holda "yig'ish" mashqi o'z-o'zidan yechilgan bo'lib ko'rinadi).
  List<String> mixTiles(List<String> tiles, List<String> answer) {
    final copy = List<String>.from(tiles);
    bool trivial(List<String> l) {
      if (l.length < answer.length) return false;
      for (var i = 0; i < answer.length; i++) {
        if (l[i] != answer[i]) return false;
      }
      return true;
    }

    var attempts = 0;
    do {
      copy.shuffle(rng);
    } while (trivial(copy) && ++attempts < 12);
    // Juda kam ehtimolli holat: aralashtirish baribir to'g'ri tartibni bersa — bittaga suramiz.
    if (trivial(copy) && copy.length > 1) copy.add(copy.removeAt(0));
    return copy;
  }

  // ------------------------------------------------------------ kontent

  RenderedInstruction say(String key, [Map<String, Object> params = const {}]) =>
      content.instructions.render(key, params, instructionLang);

  /// Chet tili darsi: ko'rsatma [lang] tilida aytiladi va ekranda shu tilda ko'rsatiladi.
  RenderedInstruction sayIn(String lang, String key, [Map<String, Object> params = const {}]) =>
      content.instructions.render(key, params, lang);

  List<LexiconEntry> countables() => lex.countables(maxAge: age);

  List<LexiconEntry> category(String cat) => lex.category(cat, maxAge: age);

  // ------------------------------------------------------------ yig'uvchilar

  /// Variantlarni aralashtirib, tanlash mashqini yaratadi.
  /// [options] ning birinchisi — to'g'ri javob.
  Exercise choice({
    required RenderedInstruction say,
    required List<ExerciseOption> options,
    required String concept,
    ExerciseVisual? visual,
    bool drag = false,
    String? hint,
    String? explanation,
    Map<String, Object> meta = const {},
    ExerciseKind kind = ExerciseKind.choice,
    ExerciseVisual? preview,
    int previewSeconds = 0,
  }) {
    final correct = options.first;
    final shuffled = List<ExerciseOption>.from(options)..shuffle(rng);
    return Exercise(
      topicId: topic.id,
      subject: topic.subject,
      level: level,
      kind: kind,
      instruction: say.text,
      speech: say.speech,
      conceptKey: concept,
      visual: visual,
      options: shuffled,
      correctIndex: shuffled.indexOf(correct),
      dragToTarget: drag,
      hint: hint,
      explanation: explanation,
      previewVisual: preview,
      previewSeconds: previewSeconds,
      meta: meta,
      speechLang: say.lang,
      speechParts: say.parts,
      instructionKey: say.key,
    );
  }

  Exercise custom({
    required RenderedInstruction say,
    required ExerciseKind kind,
    required String concept,
    ExerciseVisual? visual,
    List<MatchPair> pairs = const [],
    SortTask? sort,
    CircuitTask? circuit,
    MazeTask? maze,
    SudokuTask? sudoku,
    CodingTask? coding,
    AssembleTask? assemble,
    TraceTask? trace,
    ChessTask? chess,
    CardsTask? cards,
    SpotTask? spot,
    JigsawTask? jigsaw,
    ActivityTask? activity,
    InputTask? input,
    ExerciseVisual? preview,
    int previewSeconds = 0,
    String? hint,
    String? explanation,
    Map<String, Object> meta = const {},
    int rewardStars = 1,
  }) {
    return Exercise(
      topicId: topic.id,
      subject: topic.subject,
      level: level,
      kind: kind,
      instruction: say.text,
      speech: say.speech,
      conceptKey: concept,
      visual: visual,
      pairs: pairs,
      sort: sort,
      circuit: circuit,
      maze: maze,
      sudoku: sudoku,
      coding: coding,
      assemble: assemble,
      trace: trace,
      chess: chess,
      cards: cards,
      spot: spot,
      jigsaw: jigsaw,
      activity: activity,
      input: input,
      previewVisual: preview,
      previewSeconds: previewSeconds,
      hint: hint,
      explanation: explanation,
      meta: meta,
      rewardStars: rewardStars,
      speechLang: say.lang,
      speechParts: say.parts,
      instructionKey: say.key,
    );
  }

  /// To'g'ri son + yaqin chalg'ituvchi sonlar (hammasi [min]..[max] ichida, takrorlanmas).
  List<int> numberChoices(int correct, {int count = 3, int min = 0, int max = 20, int spread = 3}) {
    final result = <int>[correct];
    var guard = 0;
    while (result.length < count && guard++ < 200) {
      final d = range(-spread, spread);
      final v = correct + d;
      if (d != 0 && v >= min && v <= max && !result.contains(v)) result.add(v);
    }
    var v = min;
    while (result.length < count && v <= max) {
      if (!result.contains(v)) result.add(v);
      v++;
    }
    return result;
  }
}

/// Sahna joylashtirish yordamchilari.
class Layouts {
  Layouts._();

  /// [count] ta bir xil emoji'ni sahnaga chiroyli tartibda joylaydi.
  /// Hudud: [left]..[right] (kenglik ulushi).
  static List<SceneItem> group(
    String emoji,
    int count, {
    double left = 0.05,
    double right = 0.95,
    double top = 0.1,
    double bottom = 0.9,
    double aspect = 2.0,
    bool crossedFromEnd = false,
    int crossed = 0,
    Color? color,
    SceneKind kind = SceneKind.emoji,
  }) {
    if (count <= 0) return const [];
    final w = (right - left) * aspect;
    final h = bottom - top;
    // Eng katta element o'lchamiga mos ustunlar sonini tanlaymiz.
    var bestCols = 1;
    var bestSize = 0.0;
    for (var cols = 1; cols <= count; cols++) {
      final rows = (count / cols).ceil();
      final size = min(w / cols, h / rows);
      if (size > bestSize) {
        bestSize = size;
        bestCols = cols;
      }
    }
    final cols = bestCols;
    final rows = (count / cols).ceil();
    final cellW = (right - left) / cols;
    final cellH = h / rows;
    final size = min(bestSize * 0.8, 0.42);
    final items = <SceneItem>[];
    for (var i = 0; i < count; i++) {
      final r = i ~/ cols;
      final inRow = r == rows - 1 ? count - r * cols : cols;
      final c = i % cols;
      final rowLeft = left + (cols - inRow) * cellW / 2;
      items.add(SceneItem(
        kind: kind,
        value: emoji,
        x: rowLeft + cellW * (c + 0.5),
        y: top + cellH * (r + 0.5),
        size: size,
        color: color,
        crossed: crossedFromEnd && i >= count - crossed,
      ));
    }
    return items;
  }

  /// Elementlarni bir qatorga teng oraliq bilan joylaydi.
  static List<SceneItem> row(List<SceneItem> items, {double y = 0.5, double left = 0.06, double right = 0.94}) {
    final n = items.length;
    final step = (right - left) / n;
    return [
      for (var i = 0; i < n; i++) items[i].copyWith(x: left + step * (i + 0.5), y: y),
    ];
  }

  static SceneItem emoji(String e, {double size = 0.3, double x = 0.5, double y = 0.5}) =>
      SceneItem(kind: SceneKind.emoji, value: e, size: size, x: x, y: y);

  static SceneItem shape(String s, Color color, {double size = 0.3, double x = 0.5, double y = 0.5, double rotation = 0}) =>
      SceneItem(kind: SceneKind.shape, value: s, color: color, size: size, x: x, y: y, rotation: rotation);

  static SceneItem text(String t, {double size = 0.3, double x = 0.5, double y = 0.5, Color? color}) =>
      SceneItem(kind: SceneKind.text, value: t, size: size, x: x, y: y, color: color);
}

/// Variant yaratish qisqartmalari.
class Opt {
  Opt._();

  static ExerciseOption number(int n) => ExerciseOption(text: '$n');

  static ExerciseOption text(String t, {String? speech}) => ExerciseOption(text: t, speech: speech);

  static ExerciseOption emoji(String e, {bool silhouette = false, bool flip = false, double rotation = 0, HalfClip clip = HalfClip.none, double size = 0.8}) =>
      ExerciseOption(
        visual: SceneVisual([
          SceneItem(kind: SceneKind.emoji, value: e, size: size, silhouette: silhouette, flipX: flip, rotation: rotation, clip: clip),
        ], aspect: 1),
      );

  static ExerciseOption shape(String s, Color c, {double size = 0.75, double rotation = 0}) => ExerciseOption(
        visual: SceneVisual([SceneItem(kind: SceneKind.shape, value: s, color: c, size: size, rotation: rotation)], aspect: 1),
      );

  static ExerciseOption scene(List<SceneItem> items, {double aspect = 1}) =>
      ExerciseOption(visual: SceneVisual(items, aspect: aspect));

  /// [count] ta emoji guruhi (variant sifatida).
  static ExerciseOption group(String e, int count, {double aspect = 1.3}) =>
      ExerciseOption(visual: SceneVisual(Layouts.group(e, count, aspect: aspect), aspect: aspect));
}
