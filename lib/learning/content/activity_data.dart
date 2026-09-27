import '../../core/utils/map_utils.dart';
import '../models/exercise.dart';

/// Faoliyat matnlari bitta tilda.
class ActivityText {
  const ActivityText({required this.title, required this.materials, required this.steps, required this.benefit});

  final String title;
  final List<String> materials;
  final List<String> steps;
  final String benefit;

  factory ActivityText.fromJson(Map<String, dynamic> e) => ActivityText(
        title: e['title'].toString(),
        materials: MapUtils.asStringList(e['materials']),
        steps: MapUtils.asStringList(e['steps']),
        benefit: e['benefit'].toString(),
      );
}

/// "Ota-ona bilan bajaramiz" faoliyati (`assets/data/montessori.json`), uch tilda.
class FamilyActivity {
  const FamilyActivity({
    required this.id,
    required this.age,
    required this.area,
    required this.emoji,
    required this.minutes,
    required this.texts,
  });

  final String id;
  final int age;

  /// `life`, `senses`, `math`, `language`, `nature`, `science`, `movement`, `art`.
  final String area;
  final String emoji;
  final int minutes;

  /// Til → matnlar (`uz` doim bor).
  final Map<String, ActivityText> texts;

  ActivityText textIn(String lang) => texts[lang] ?? texts['uz']!;

  String get title => texts['uz']!.title;

  Localized get titleL => Localized(uz: textIn('uz').title, en: textIn('en').title, ru: textIn('ru').title);

  ActivityTask taskIn(String lang) {
    final t = textIn(lang);
    return ActivityTask(
      id: id,
      emoji: emoji,
      title: t.title,
      materials: t.materials,
      steps: t.steps,
      benefit: t.benefit,
      minutes: minutes,
    );
  }

  ActivityTask get task => taskIn('uz');
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
  final Localized text;
  final String emotion;
  final int age;
}

/// Vaziyat → sehrli so'z.
class PoliteCase {
  const PoliteCase({required this.id, required this.scene, required this.text, required this.word});

  final String id;
  final List<String> scene;
  final Localized text;
  final Localized word;
}

/// Tanlov matnlari bitta tilda: [good] — mehribon/xavfsiz yo'l, [others] — boshqa yo'llar.
class SocialChoiceText {
  const SocialChoiceText({required this.text, required this.good, required this.others, required this.why});

  final String text;
  final String good;
  final List<String> others;
  final String why;
}

/// Tanlov: har bir variant — emoji + matn (tilga qarab).
class SocialChoice {
  const SocialChoice({
    required this.id,
    required this.scene,
    required this.goodEmoji,
    required this.otherEmojis,
    required this.texts,
    required this.age,
    required this.kind,
  });

  final String id;
  final List<String> scene;
  final String goodEmoji;
  final List<String> otherEmojis;

  /// Til → matnlar (`uz` doim bor).
  final Map<String, SocialChoiceText> texts;
  final int age;

  /// `kind` (yaxshi do'st) yoki `safety` (xavfsizlik).
  final String kind;

  SocialChoiceText textIn(String lang) => texts[lang] ?? texts['uz']!;
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
  final List<Localized> politeWords;
  final List<SocialChoice> choices;

  Emotion emotion(String id) => emotions.firstWhere((e) => e.id == id);

  static Localized _loc(Map<String, dynamic> e, String uzKey, String enKey, String ruKey) {
    final uz = e[uzKey].toString();
    return Localized(uz: uz, en: (e[enKey] ?? uz).toString(), ru: (e[ruKey] ?? uz).toString());
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
            minutes: MapUtils.asInt(e['minutes'], 10),
            texts: {
              'uz': ActivityText.fromJson(e),
              for (final lang in const ['en', 'ru'])
                if (e[lang] is Map) lang: ActivityText.fromJson(MapUtils.asStringMap(e[lang])),
            },
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
            text: _loc(e, 'text', 'en', 'ru'),
            emotion: e['emotion'].toString(),
            age: MapUtils.asInt(e['age'], 4),
          ),
      ],
      polite: [
        for (final e in (social['polite'] as List).map(MapUtils.asStringMap))
          PoliteCase(
            id: e['id'].toString(),
            scene: MapUtils.asStringList(e['scene']),
            text: _loc(e, 'text', 'textEn', 'textRu'),
            word: _loc(e, 'word', 'wordEn', 'wordRu'),
          ),
      ],
      politeWords: social['politeWordsI18n'] is List
          ? [for (final w in (social['politeWordsI18n'] as List).map(MapUtils.asStringMap)) Localized.fromJson(w)]
          : [for (final w in MapUtils.asStringList(social['politeWords'])) Localized.same(w)],
      choices: [
        for (final e in (social['choices'] as List).map(MapUtils.asStringMap))
          SocialChoice(
            id: e['id'].toString(),
            scene: MapUtils.asStringList(e['scene']),
            goodEmoji: MapUtils.asStringList(e['good'])[0],
            otherEmojis: [for (final o in (e['others'] as List)) MapUtils.asStringList(o)[0]],
            texts: {
              'uz': SocialChoiceText(
                text: e['text'].toString(),
                good: MapUtils.asStringList(e['good'])[1],
                others: [for (final o in (e['others'] as List)) MapUtils.asStringList(o)[1]],
                why: e['why'].toString(),
              ),
              for (final lang in const ['en', 'ru'])
                if (e[lang] is Map)
                  lang: SocialChoiceText(
                    text: MapUtils.asStringMap(e[lang])['text'].toString(),
                    good: MapUtils.asStringMap(e[lang])['good'].toString(),
                    others: MapUtils.asStringList(MapUtils.asStringMap(e[lang])['others']),
                    why: MapUtils.asStringMap(e[lang])['why'].toString(),
                  ),
            },
            age: MapUtils.asInt(e['age'], 4),
            kind: (e['kind'] ?? 'kind').toString(),
          ),
      ],
    );
  }
}
