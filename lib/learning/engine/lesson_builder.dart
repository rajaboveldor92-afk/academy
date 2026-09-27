import 'dart:math';

import '../content/content_repository.dart';
import '../chess/chess_goals.dart';
import '../generators/generator_base.dart';
import '../generators/registry.dart';
import '../models/exercise.dart';
import '../models/topic.dart';

/// Dars (mashqlar to'plami) yaratuvchi.
///
/// * Bir darsda bir xil savol takrorlanmaydi.
/// * Bolaning oxirgi ko'rgan savollari ([avoid]) iloji boricha chetlab o'tiladi.
/// * Generator ba'zan yaroqsiz mashq bersa (masalan, chalg'ituvchi yetmasa),
///   u tashlab yuboriladi — bola hech qachon buzilgan savol ko'rmaydi.
class LessonBuilder {
  LessonBuilder._();

  static int signatureHash(Exercise e) => e.signature.hashCode & 0x7fffffff;

  static List<Exercise> build({
    required ContentRepository content,
    required Topic topic,
    required int level,
    required int count,
    required int age,
    Random? rng,
    Set<int> avoid = const {},
  }) {
    final generator = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator);
    if (generator == null) {
      throw StateError('Generator topilmadi: ${topic.subject}${topic.ageSuffix}.${topic.generator}');
    }
    final random = rng ?? Random();
    final result = <Exercise>[];
    final seen = <int>{};
    final fallback = <Exercise>[];
    for (var attempt = 0; attempt < count * 25 && result.length < count; attempt++) {
      Exercise ex;
      try {
        ex = generator(GenContext(rng: random, content: content, topic: topic, level: level, age: age));
      } catch (_) {
        continue;
      }
      if (!ExerciseValidator.isPlayable(ex)) continue;
      final h = signatureHash(ex);
      if (!seen.add(h)) continue;
      if (avoid.contains(h)) {
        fallback.add(ex);
        continue;
      }
      result.add(ex);
    }
    // Yangi savollar yetmasa — avval ko'rilganlaridan to'ldiramiz.
    for (final ex in fallback) {
      if (result.length >= count) break;
      result.add(ex);
    }
    return result;
  }

  /// Mavzudan bitta yangi mashq. [concept] berilsa — shu tushunchaga oid, lekin boshqa
  /// ko'rinishda (takrorlash uchun); [avoid] dagi imzolar iloji boricha chetlab o'tiladi.
  static Exercise? similar({
    required ContentRepository content,
    required Topic topic,
    required int level,
    required int age,
    Random? rng,
    String? concept,
    Set<int> avoid = const {},
  }) {
    final generator = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator);
    if (generator == null) return null;
    final random = rng ?? Random();
    Exercise? fallback;
    var conceptMatched = false;
    for (var i = 0; i < 30; i++) {
      Exercise ex;
      try {
        ex = generator(GenContext(rng: random, content: content, topic: topic, level: level, age: age));
      } catch (_) {
        continue;
      }
      if (!ExerciseValidator.isPlayable(ex)) continue;
      final fresh = !avoid.contains(signatureHash(ex));
      final matches = concept == null || ex.conceptKey == concept;
      if (matches && fresh) return ex;
      if (matches && !conceptMatched) {
        fallback = ex;
        conceptMatched = true;
      } else if (fallback == null || (!conceptMatched && fresh)) {
        fallback = ex;
      }
    }
    return fallback;
  }
}

/// Mashq o'ynaladigan holatdami (tuzilma bo'yicha minimal tekshiruv).
/// To'liq kontent tekshiruvi testlarda (`test/content/`).
class ExerciseValidator {
  ExerciseValidator._();

  static bool isPlayable(Exercise e) {
    if (e.instruction.uz.trim().isEmpty || e.speech.trim().isEmpty) return false;
    switch (e.kind) {
      case ExerciseKind.choice:
      case ExerciseKind.memory:
        if (e.options.length < 2) return false;
        if (e.correctIndex < 0 || e.correctIndex >= e.options.length) return false;
        final descs = e.options.map((o) => o.describe()).toSet();
        return descs.length == e.options.length;
      case ExerciseKind.match:
        if (e.pairs.length < 2) return false;
        final lefts = e.pairs.map((p) => p.left.describe()).toSet();
        final rights = e.pairs.map((p) => p.right.describe()).toSet();
        return lefts.length == e.pairs.length && rights.length == e.pairs.length;
      case ExerciseKind.sort:
        final s = e.sort;
        return s != null &&
            s.bins.length >= 2 &&
            s.items.length == s.itemBins.length &&
            s.items.isNotEmpty &&
            s.itemBins.every((b) => b >= 0 && b < s.bins.length);
      case ExerciseKind.maze:
        return e.maze?.shortestPath() != null;
      case ExerciseKind.sudoku:
        return e.sudoku != null && e.sudoku!.blanks > 0;
      case ExerciseKind.coding:
        return e.coding != null;
      case ExerciseKind.assemble:
        final a = e.assemble;
        if (a == null || a.answer.length < 2) return false;
        final pool = List<String>.from(a.tiles);
        for (final part in a.answer) {
          if (!pool.remove(part)) return false;
        }
        return true;
      case ExerciseKind.trace:
        final t = e.trace;
        return t != null && t.strokes.isNotEmpty && t.strokes.every((s) => s.length >= 2);
      case ExerciseKind.chess:
        final c = e.chess;
        return c != null && ChessGoals.isPlayable(c);
      case ExerciseKind.cards:
        final c = e.cards;
        if (c == null || c.faces.length < 4 || c.faces.length.isOdd) return false;
        final counts = <String, int>{};
        for (final f in c.faces) {
          counts[f] = (counts[f] ?? 0) + 1;
        }
        return counts.values.every((n) => n == 2);
      case ExerciseKind.spot:
        final s = e.spot;
        return s != null && s.targets.isNotEmpty && s.targets.every((t) => t >= 0 && t < s.items.length);
      case ExerciseKind.jigsaw:
        final j = e.jigsaw;
        return j != null && j.pieces >= 2 && j.picture.items.isNotEmpty;
      case ExerciseKind.activity:
        final a = e.activity;
        return a != null && a.steps.isNotEmpty && a.title.trim().isNotEmpty;
    }
  }
}
