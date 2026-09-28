import 'dart:math' as math;

import '../../models/exercise.dart';
import '../generator_base.dart';
import '../registry.dart';
import 'math_school.dart';

/// Maktab fanlari generatorlari: kalit `school.<fan>.<nom>` yoki umumiy `school.<nom>`.
class SchoolGenerators {
  SchoolGenerators._();

  static Map<String, ExerciseGenerator> get all => {
        for (final e in MathSchool.generators.entries) 'school.math.${e.key}': e.value,
        'school.test': test,
      };

  /// Nazorat ishi: darajadagi `topics` ro'yxatidan tasodifiy mavzu tanlanib, o'sha mavzuning
  /// generatori bilan savol tuziladi (daraja — `level` parametri, mavzu darajalaridan oshmaydi).
  static Exercise test(GenContext g) {
    final ids = g.pl('topics');
    final topic = g.content.topic(g.pick(ids));
    if (topic == null) throw StateError('Nazorat ishi mavzusi topilmadi: $ids');
    final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator);
    if (gen == null || topic.isTest) throw StateError('Generator topilmadi: ${topic.id}');
    final level = math.min(g.p('level', 2), topic.maxLevel);
    return gen(GenContext(rng: g.rng, content: g.content, topic: topic, level: level, age: g.age, lang: g.lang));
  }
}
