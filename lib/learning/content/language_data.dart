import '../../core/utils/map_utils.dart';
import '../models/exercise.dart';

/// Chet tili alifbosidagi harf (`assets/data/languages.json`).
class LangLetter {
  const LangLetter({required this.upper, required this.lower, required this.vowel, this.lexId, this.initial = true});

  final String upper;
  final String lower;
  final bool vowel;

  /// Rasmli misol (lug'at id); ba'zi harflarda yo'q (rus tilida Ъ, Щ, Э).
  final String? lexId;

  /// Misol so'z shu harf bilan boshlanadimi (X — box, Ы — сыр kabi hollarda yo'q).
  final bool initial;
}

/// Harakat: 🏃 run / running / бегать / бежит.
class LangAction {
  const LangAction({
    required this.id,
    required this.emoji,
    required this.uz,
    required this.uzNow,
    required this.en,
    required this.enIng,
    required this.ru,
    required this.ruNow,
    required this.ageMin,
  });

  final String id;
  final String emoji;
  final String uz;
  final String uzNow;
  final String en;
  final String enIng;
  final String ru;
  final String ruNow;
  final int ageMin;

  /// Lug'at shakli (uch tilda o'rganish uchun): yugurmoq / run / бегать.
  Localized get word => Localized(uz: uz, en: en, ru: ru);

  /// "Hozir nima qilyapti" shakli: yuguryapti / running / бежит.
  Localized get now => Localized(uz: uzNow, en: enIng, ru: ruNow);
}

/// Hayvon harakati gapda: "The bird is flying." / "Птица летит."
class AnimalAction {
  const AnimalAction({
    required this.id,
    required this.en,
    required this.ru,
    required this.context,
    required this.categories,
    required this.tag,
  });

  final String id;
  final String en;
  final String ru;

  /// Harakatni ko'rsatuvchi qo'shimcha rasm (☁️, 🌊, 💤 ...).
  final String context;
  final List<String> categories;

  /// Mos jonivor tegi (bo'sh — hamma uchun).
  final String tag;
}

/// Sifat (qarama-qarshi jufti bilan). Rus tilida jinsga qarab shakllari bor.
class Adjective {
  const Adjective({
    required this.id,
    required this.pair,
    required this.uz,
    required this.en,
    required this.ruForms,
    required this.visual,
  });

  final String id;
  final String pair;
  final String uz;
  final String en;

  /// `m`, `f`, `n`, `pl` → shakl.
  final Map<String, String> ruForms;

  /// `size`, `length` yoki `emoji:<e>`.
  final String visual;

  String? get emoji => visual.startsWith('emoji:') ? visual.substring(6) : null;

  String ru([String gender = 'm']) => ruForms[gender] ?? ruForms['m']!;

  Localized word([String gender = 'm']) => Localized(uz: uz, en: en, ru: ru(gender));
}

/// Kundalik ibora: "Thank you!" / "Спасибо!" / "Rahmat!" va unga mos sahna.
class Phrase {
  const Phrase({required this.id, required this.scene, required this.text, required this.ageMin});

  final String id;
  final List<String> scene;
  final Localized text;
  final int ageMin;
}

/// Ingliz va rus tili modullari ma'lumotlari.
class LanguageData {
  LanguageData({
    required this.alphabets,
    required this.actions,
    required this.animalActions,
    required this.adjectives,
    required this.colorForms,
    required this.phrases,
    required this.ruGender,
    required this.enPlural,
    required this.ruSyllables,
  });

  final Map<String, List<LangLetter>> alphabets;
  final List<LangAction> actions;
  final List<AnimalAction> animalActions;
  final List<Adjective> adjectives;
  final Map<String, Map<String, String>> colorForms;
  final List<Phrase> phrases;

  /// Rus tilida so'z jinsi (faqat bir so'zli otlar): `m`, `f`, `n`, `pl`.
  final Map<String, String> ruGender;

  /// Inglizcha ko'plik (faqat sanaladigan otlar).
  final Map<String, String> enPlural;

  /// Rus tilida bir ma'noli bo'g'inga ajraladigan so'zlar (ма-ши-на).
  final Map<String, List<String>> ruSyllables;

  static const Set<String> ruVowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'};
  static const Set<String> enVowels = {'a', 'e', 'i', 'o', 'u'};

  List<LangLetter> alphabet(String lang) => alphabets[lang] ?? const [];

  Adjective adjective(String id) => adjectives.firstWhere((a) => a.id == id);

  /// Rang nomi rus tilida kerakli jinsda: "красная" (машина), "красное" (яблоко).
  String colorRu(String colorId, String gender) => colorForms[colorId]?[gender] ?? colorForms[colorId]?['m'] ?? colorId;

  factory LanguageData.fromJson(Map<String, dynamic> j) {
    List<LangLetter> letters(Object? v) => [
          for (final e in (v as List).map(MapUtils.asStringMap))
            LangLetter(
              upper: e['upper'].toString(),
              lower: e['lower'].toString(),
              vowel: MapUtils.asBool(e['vowel']),
              lexId: e['lexId']?.toString(),
              initial: MapUtils.asBool(e['initial'], true),
            ),
        ];
    Map<String, String> strMap(Object? v) => MapUtils.asStringMap(v).map((k, x) => MapEntry(k, x.toString()));
    return LanguageData(
      alphabets: {
        'en': letters(MapUtils.asStringMap(j['en'])['alphabet']),
        'ru': letters(MapUtils.asStringMap(j['ru'])['alphabet']),
      },
      actions: [
        for (final e in (j['actions'] as List).map(MapUtils.asStringMap))
          LangAction(
            id: e['id'].toString(),
            emoji: e['emoji'].toString(),
            uz: e['uz'].toString(),
            uzNow: e['uzNow'].toString(),
            en: e['en'].toString(),
            enIng: e['enIng'].toString(),
            ru: e['ru'].toString(),
            ruNow: e['ruNow'].toString(),
            ageMin: MapUtils.asInt(e['ageMin'], 4),
          ),
      ],
      animalActions: [
        for (final e in (j['animalActions'] as List).map(MapUtils.asStringMap))
          AnimalAction(
            id: e['id'].toString(),
            en: e['en'].toString(),
            ru: e['ru'].toString(),
            context: e['context'].toString(),
            categories: MapUtils.asStringList(e['cats']),
            tag: (e['tag'] ?? '').toString(),
          ),
      ],
      adjectives: [
        for (final e in (j['adjectives'] as List).map(MapUtils.asStringMap))
          Adjective(
            id: e['id'].toString(),
            pair: e['pair'].toString(),
            uz: e['uz'].toString(),
            en: e['en'].toString(),
            ruForms: strMap(e['ru']),
            visual: e['visual'].toString(),
          ),
      ],
      colorForms: MapUtils.asStringMap(j['colorForms']).map((k, v) => MapEntry(k, strMap(v))),
      phrases: [
        for (final e in (j['phrases'] as List).map(MapUtils.asStringMap))
          Phrase(
            id: e['id'].toString(),
            scene: MapUtils.asStringList(e['scene']),
            text: Localized.fromJson(e),
            ageMin: MapUtils.asInt(e['ageMin'], 4),
          ),
      ],
      ruGender: strMap(j['ruGender']),
      enPlural: strMap(j['enPlural']),
      ruSyllables: MapUtils.asStringMap(j['ruSyllables']).map((k, v) => MapEntry(k, MapUtils.asStringList(v))),
    );
  }
}
