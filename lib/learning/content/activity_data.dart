import '../../core/utils/map_utils.dart';
import '../models/exercise.dart';

/// "Ota-ona bilan bajaramiz" faoliyati (`assets/data/montessori.json`).
class FamilyActivity {
  const FamilyActivity({
    required this.id,
    required this.age,
    required this.area,
    required this.emoji,
    required this.title,
    required this.minutes,
    required this.materials,
    required this.steps,
    required this.benefit,
  });

  final String id;
  final int age;

  /// `life`, `senses`, `math`, `language`, `nature`, `science`, `movement`, `art`.
  final String area;
  final String emoji;
  final String title;
  final int minutes;
  final List<String> materials;
  final List<String> steps;
  final String benefit;

  ActivityTask get task => ActivityTask(
        id: id,
        emoji: emoji,
        title: title,
        materials: materials,
        steps: steps,
        benefit: benefit,
        minutes: minutes,
      );
}

/// His-tuyg'u.
class Emotion {
  const Emotion({required this.id, required this.emoji, required this.name});

  final String id;
  final String emoji;
  final Localized name;
}

/// Vaziyat → his-tuyg'u.
class Situation {
  const Situation({required this.id, required this.scene, required this.text, required this.emotion, required this.age});

  final String id;
  final List<String> scene;
  final String text;
  final String emotion;
  final int age;
}

/// Vaziyat → sehrli so'z.
class PoliteCase {
  const PoliteCase({required this.id, required this.scene, required this.text, required this.word});

  final String id;
  final List<String> scene;
  final String text;
  final String word;
}

/// Tanlov: [good] — mehribon/xavfsiz yo'l, [others] — boshqa yo'llar. Har biri: (emoji, matn).
class SocialChoice {
  const SocialChoice({
    required this.id,
    required this.scene,
    required this.text,
    required this.good,
    required this.others,
    required this.why,
    required this.age,
    required this.kind,
  });

  final String id;
  final List<String> scene;
  final String text;
  final (String, String) good;
  final List<(String, String)> others;
  final String why;
  final int age;

  /// `kind` (yaxshi do'st) yoki `safety` (xavfsizlik).
  final String kind;
}

class ActivityData {
  ActivityData({
    required this.activities,
    required this.emotions,
    required this.situations,
    required this.polite,
    required this.politeWords,
    required this.choices,
  });

  final List<FamilyActivity> activities;
  final List<Emotion> emotions;
  final List<Situation> situations;
  final List<PoliteCase> polite;
  final List<String> politeWords;
  final List<SocialChoice> choices;

  Emotion emotion(String id) => emotions.firstWhere((e) => e.id == id);

  static (String, String) _pair(Object? v) {
    final l = MapUtils.asStringList(v);
    return (l[0], l[1]);
  }

  factory ActivityData.fromJson(Map<String, dynamic> montessori, Map<String, dynamic> social) {
    return ActivityData(
      activities: [
        for (final e in (montessori['activities'] as List).map(MapUtils.asStringMap))
          FamilyActivity(
            id: e['id'].toString(),
            age: MapUtils.asInt(e['age'], 4),
            area: e['area'].toString(),
            emoji: e['emoji'].toString(),
            title: e['title'].toString(),
            minutes: MapUtils.asInt(e['minutes'], 10),
            materials: MapUtils.asStringList(e['materials']),
            steps: MapUtils.asStringList(e['steps']),
            benefit: e['benefit'].toString(),
          ),
      ],
      emotions: [
        for (final e in (social['emotions'] as List).map(MapUtils.asStringMap))
          Emotion(id: e['id'].toString(), emoji: e['emoji'].toString(), name: Localized.fromJson(e)),
      ],
      situations: [
        for (final e in (social['situations'] as List).map(MapUtils.asStringMap))
          Situation(
            id: e['id'].toString(),
            scene: MapUtils.asStringList(e['scene']),
            text: e['text'].toString(),
            emotion: e['emotion'].toString(),
            age: MapUtils.asInt(e['age'], 4),
          ),
      ],
      polite: [
        for (final e in (social['polite'] as List).map(MapUtils.asStringMap))
          PoliteCase(
            id: e['id'].toString(),
            scene: MapUtils.asStringList(e['scene']),
            text: e['text'].toString(),
            word: e['word'].toString(),
          ),
      ],
      politeWords: MapUtils.asStringList(social['politeWords']),
      choices: [
        for (final e in (social['choices'] as List).map(MapUtils.asStringMap))
          SocialChoice(
            id: e['id'].toString(),
            scene: MapUtils.asStringList(e['scene']),
            text: e['text'].toString(),
            good: _pair(e['good']),
            others: [for (final o in (e['others'] as List)) _pair(o)],
            why: e['why'].toString(),
            age: MapUtils.asInt(e['age'], 4),
            kind: (e['kind'] ?? 'kind').toString(),
          ),
      ],
    );
  }
}
