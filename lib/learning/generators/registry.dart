import 'generator_base.dart';
import 'attention_gen.dart';
import 'chess_gen.dart';
import 'foreign_language.dart';
import 'logic_junior.dart';
import 'logic_senior.dart';
import 'math_junior.dart';
import 'math_senior.dart';
import 'memory_gen.dart';
import 'puzzle_gen.dart';
import 'social_gen.dart';
import 'trilingual.dart';
import 'uzbek_junior.dart';
import 'uzbek_senior.dart';
import 'writing.dart';
import 'school/school_registry.dart';

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
    for (final e in ForeignLanguage.generators.entries) 'english4.${e.key}': e.value,
    for (final e in ForeignLanguage.generators.entries) 'english6.${e.key}': e.value,
    for (final e in ForeignLanguage.generators.entries) 'russian4.${e.key}': e.value,
    for (final e in ForeignLanguage.generators.entries) 'russian6.${e.key}': e.value,
    for (final e in Trilingual.generators.entries) 'trilingual4.${e.key}': e.value,
    for (final e in Trilingual.generators.entries) 'trilingual6.${e.key}': e.value,
    for (final e in ChessGenerators.generators.entries) 'chess4.${e.key}': e.value,
    for (final e in ChessGenerators.generators.entries) 'chess6.${e.key}': e.value,
    for (final e in MemoryGames.generators.entries) 'memory4.${e.key}': e.value,
    for (final e in MemoryGames.generators.entries) 'memory6.${e.key}': e.value,
    for (final e in AttentionGames.generators.entries) 'attention4.${e.key}': e.value,
    for (final e in AttentionGames.generators.entries) 'attention6.${e.key}': e.value,
    for (final e in AttentionGames.generators.entries) 'motor4.${e.key}': e.value,
    for (final e in AttentionGames.generators.entries) 'motor6.${e.key}': e.value,
    for (final e in PuzzleGames.generators.entries) 'puzzle4.${e.key}': e.value,
    for (final e in PuzzleGames.generators.entries) 'puzzle6.${e.key}': e.value,
    for (final e in SocialGames.generators.entries) 'social4.${e.key}': e.value,
    for (final e in SocialGames.generators.entries) 'social6.${e.key}': e.value,
    for (final e in SocialGames.generators.entries) 'family4.${e.key}': e.value,
    for (final e in SocialGames.generators.entries) 'family6.${e.key}': e.value,
    ...SchoolGenerators.all,
  };

  /// Maktab dasturi (`g3`, `g5` ...) — `school.<fan>.<nom>`, keyin umumiy `school.<nom>`.
  static ExerciseGenerator? find(String subject, String ageSuffix, String name) {
    if (ageSuffix.startsWith('g')) return _all['school.$subject.$name'] ?? _all['school.$name'];
    return _all['$subject$ageSuffix.$name'];
  }

  static Iterable<String> get names => _all.keys;
}
