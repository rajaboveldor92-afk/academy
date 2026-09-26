import 'generator_base.dart';
import 'logic_junior.dart';
import 'logic_senior.dart';
import 'math_junior.dart';
import 'math_senior.dart';
import 'uzbek_junior.dart';
import 'uzbek_senior.dart';
import 'writing.dart';

/// Barcha generatorlar ro'yxati. Kalit — dastur JSON'idagi `generator` qiymati,
/// fan prefiksi bilan: `math4.count_objects`, `logic6.coding`.
class GeneratorRegistry {
  GeneratorRegistry._();

  static final Map<String, ExerciseGenerator> _all = {
    for (final e in MathJunior.generators.entries) 'math4.${e.key}': e.value,
    for (final e in LogicJunior.generators.entries) 'logic4.${e.key}': e.value,
    for (final e in MathSenior.generators.entries) 'math6.${e.key}': e.value,
    for (final e in LogicSenior.generators.entries) 'logic6.${e.key}': e.value,
    for (final e in UzbekJunior.generators.entries) 'uzbek4.${e.key}': e.value,
    for (final e in UzbekSenior.generators.entries) 'uzbek6.${e.key}': e.value,
    for (final e in WritingGenerators.generators.entries) 'writing4.${e.key}': e.value,
    for (final e in WritingGenerators.generators.entries) 'writing6.${e.key}': e.value,
  };

  static ExerciseGenerator? find(String subject, String ageSuffix, String name) =>
      _all['$subject$ageSuffix.$name'];

  static Iterable<String> get names => _all.keys;
}
