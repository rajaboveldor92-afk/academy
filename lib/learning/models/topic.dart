import '../../core/utils/map_utils.dart';
import 'exercise.dart';

/// O'quv dasturidagi bitta mavzu (ko'nikma), masalan "M3. 1–5".
/// `assets/data/<fan>_<3..8>.json` fayllaridan o'qiladi.
class Topic {
  const Topic({
    required this.id,
    required this.code,
    required this.subject,
    required this.emoji,
    required this.title,
    required this.generator,
    required this.levels,
    required this.ageMin,
    required this.ageMax,
    this.ageSuffix = '6',
    this.skill = '',
    this.prerequisites = const [],
    this.tags = const [],
    this.lessonSize,
  });

  /// Global noyob id: `math4.count_1_5`.
  final String id;

  /// Dasturdagi tartib raqami: `M3`, `L7`.
  final String code;
  final String subject;
  final String emoji;
  final Localized title;

  /// Generator nomi (`GeneratorRegistry` dagi kalit).
  final String generator;

  /// Har bir daraja uchun generator parametrlari (1-daraja = levels[0]).
  final List<Map<String, dynamic>> levels;
  final int ageMin;
  final int ageMax;

  /// Dastur guruhi: `3` dan `8` gacha.
  final String ageSuffix;

  /// Ota-ona panelidagi ko'nikma nomi (masalan `addition`).
  final String skill;
  final List<String> prerequisites;
  final List<String> tags;

  /// Mavzuga xos dars hajmi (masalan, AI bilan o'yinda — 1 ta partiya). `null` — dastur bo'yicha.
  final int? lessonSize;

  int get maxLevel => levels.length;

  Map<String, dynamic> paramsFor(int level) {
    final l = level < 1 ? 1 : (level > maxLevel ? maxLevel : level);
    return levels[l - 1];
  }

  factory Topic.fromJson(
    Map<String, dynamic> json, {
    required String subject,
    required int ageMin,
    required int ageMax,
    required String ageSuffix,
  }) {
    return Topic(
      id: json['id'].toString(),
      code: (json['code'] ?? '').toString(),
      subject: subject,
      emoji: (json['emoji'] ?? '⭐').toString(),
      title: Localized.fromJson(json['title']),
      generator: json['generator'].toString(),
      levels: (json['levels'] as List? ?? const [])
          .map((e) => MapUtils.asStringMap(e))
          .toList(),
      ageMin: MapUtils.asInt(json['ageMin'], ageMin),
      ageMax: MapUtils.asInt(json['ageMax'], ageMax),
      ageSuffix: ageSuffix,
      skill: (json['skill'] ?? json['generator']).toString(),
      prerequisites: MapUtils.asStringList(json['prerequisites']),
      tags: MapUtils.asStringList(json['tags']),
      lessonSize: json['lessonSize'] is num ? (json['lessonSize'] as num).toInt() : null,
    );
  }
}

/// Bitta fan + yosh guruhi uchun dastur (masalan `math_4.json`).
class Curriculum {
  const Curriculum({
    required this.subject,
    required this.ageSuffix,
    required this.title,
    required this.model,
    required this.topics,
    required this.lessonSize,
  });

  final String subject;

  /// `3` dan `8` gacha.
  final String ageSuffix;
  final Localized title;

  /// Pedagogik model ("KO'R → ESHIT → BOS ...").
  final String model;
  final List<Topic> topics;

  /// Bir darsdagi mashqlar soni.
  final int lessonSize;

  Topic? topic(String id) {
    for (final t in topics) {
      if (t.id == id) return t;
    }
    return null;
  }

  factory Curriculum.fromJson(Map<String, dynamic> json) {
    final subject = json['subject'].toString();
    final suffix = json['ageGroup'].toString();
    final ageMin = MapUtils.asInt(json['ageMin'], suffix == '4' ? 3 : 6);
    final ageMax = MapUtils.asInt(json['ageMax'], suffix == '4' ? 5 : 8);
    return Curriculum(
      subject: subject,
      ageSuffix: suffix,
      title: Localized.fromJson(json['title']),
      model: (json['model'] ?? '').toString(),
      lessonSize: MapUtils.asInt(json['lessonSize'], suffix == '4' ? 6 : 10),
      topics: (json['topics'] as List? ?? const [])
          .map((e) => Topic.fromJson(
                MapUtils.asStringMap(e),
                subject: subject,
                ageMin: ageMin,
                ageMax: ageMax,
                ageSuffix: suffix,
              ))
          .toList(),
    );
  }
}
