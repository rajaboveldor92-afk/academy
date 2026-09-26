import '../../core/utils/map_utils.dart';
import '../models/exercise.dart';

/// Alifbodagi harf.
class UzLetter {
  const UzLetter({required this.upper, required this.lower, required this.vowel, required this.lexId, required this.word});

  final String upper;
  final String lower;
  final bool vowel;

  /// Shu harf bilan boshlanadigan rasmli so'z (lug'at id).
  final String lexId;
  final String word;
}

/// So'z bazasidagi so'z (bo'g'inlarga ajratilgan).
class UzWord {
  const UzWord({required this.word, required this.syllables, required this.theme, required this.age, this.lexId});

  final String word;
  final List<String> syllables;
  final String theme;
  final int age;
  final String? lexId;

  bool get hasPicture => lexId != null;

  List<String> get letters => UzbekData.letters(word);
}

/// Gap shablonlari uchun harakat ("uchyapti", "suzyapti" ...).
class UzAction {
  const UzAction({required this.id, required this.text, required this.tag, required this.categories});

  final String id;
  final Localized text;

  /// Mos jonivor tegi (bo'sh — hamma uchun).
  final String tag;
  final List<String> categories;
}

class UzPlace {
  const UzPlace({required this.id, required this.text, required this.emoji});

  final String id;
  final Localized text;
  final String emoji;
}

/// O'zbek tili ma'lumotlari (`assets/data/uzbek.json`).
class UzbekData {
  UzbekData({
    required this.alphabet,
    required this.words,
    required this.actions,
    required this.places,
    required this.names,
    required this.themes,
  });

  static const Set<String> vowels = {'a', 'e', 'i', 'o', 'u', 'o‘'};

  final List<UzLetter> alphabet;
  final List<UzWord> words;
  final List<UzAction> actions;
  final List<UzPlace> places;
  final List<String> names;
  final Map<String, String> themes;

  List<UzWord> forAge(int age) => words.where((w) => w.age <= age).toList();

  List<UzWord> picturable(int age) => words.where((w) => w.age <= age && w.hasPicture).toList();

  UzLetter letter(String lower) => alphabet.firstWhere((l) => l.lower == lower);

  /// So'zni o'zbek harflariga ajratadi: "qo‘ng‘iroq" → q, o‘, n, g‘, i, r, o, q.
  static List<String> letters(String word) {
    final w = word.toLowerCase();
    final out = <String>[];
    var i = 0;
    while (i < w.length) {
      final ch = w[i];
      if (ch == 'ʼ' && out.isNotEmpty) {
        out[out.length - 1] = '${out.last}ʼ';
        i++;
        continue;
      }
      if (i + 2 < w.length && w.substring(i, i + 3) == 'ng‘') {
        out.add('n');
        i++;
        continue;
      }
      if (i + 1 < w.length) {
        final two = w.substring(i, i + 2);
        if (two == 'o‘' || two == 'g‘' || two == 'sh' || two == 'ch' || two == 'ng') {
          out.add(two);
          i += 2;
          continue;
        }
      }
      out.add(ch);
      i++;
    }
    return out;
  }

  static bool isVowel(String letter) => vowels.contains(letter.replaceAll('ʼ', ''));

  /// Harfning bosh ko'rinishi: "sh" → "Sh", "o‘" → "O‘".
  static String capital(String letter) => letter.isEmpty ? letter : letter[0].toUpperCase() + letter.substring(1);

  factory UzbekData.fromJson(Map<String, dynamic> j) {
    return UzbekData(
      alphabet: [
        for (final e in (j['alphabet'] as List).map(MapUtils.asStringMap))
          UzLetter(
            upper: e['upper'].toString(),
            lower: e['lower'].toString(),
            vowel: MapUtils.asBool(e['vowel']),
            lexId: e['lexId'].toString(),
            word: e['word'].toString(),
          ),
      ],
      words: [
        for (final e in (j['words'] as List).map(MapUtils.asStringMap))
          UzWord(
            word: e['w'].toString(),
            syllables: MapUtils.asStringList(e['syl']),
            theme: e['theme'].toString(),
            age: MapUtils.asInt(e['age'], 4),
            lexId: e['lexId']?.toString(),
          ),
      ],
      actions: [
        for (final e in (j['actions'] as List).map(MapUtils.asStringMap))
          UzAction(
            id: e['id'].toString(),
            text: Localized.fromJson(e),
            tag: (e['tag'] ?? '').toString(),
            categories: MapUtils.asStringList(e['cats']),
          ),
      ],
      places: [
        for (final e in (j['places'] as List).map(MapUtils.asStringMap))
          UzPlace(id: e['id'].toString(), text: Localized.fromJson(e), emoji: e['emoji'].toString()),
      ],
      names: MapUtils.asStringList(j['names']),
      themes: MapUtils.asStringMap(j['themes']).map((k, v) => MapEntry(k, v.toString())),
    );
  }
}

/// Yozish mashqlari uchun chiziqlar (`assets/data/glyphs.json`).
class GlyphBank {
  GlyphBank({required this.glyphs, required this.prewriting, required this.dots});

  final Map<String, List<List<Point2>>> glyphs;
  final Map<String, List<List<Point2>>> prewriting;
  final Map<String, List<Point2>> dots;

  static List<List<Point2>> _strokes(Object? v) => [
        for (final s in (v as List))
          [for (final p in (s as List)) Point2(((p as List)[0] as num).toDouble(), (p[1] as num).toDouble())],
      ];

  factory GlyphBank.fromJson(Map<String, dynamic> j) => GlyphBank(
        glyphs: MapUtils.asStringMap(j['glyphs']).map((k, v) => MapEntry(k, _strokes(v))),
        prewriting: MapUtils.asStringMap(j['prewriting']).map((k, v) => MapEntry(k, _strokes(v))),
        dots: MapUtils.asStringMap(j['dots']).map(
          (k, v) => MapEntry(k, [for (final p in (v as List)) Point2(((p as List)[0] as num).toDouble(), (p[1] as num).toDouble())]),
        ),
      );

  /// Harf (o'zbek harfi) chiziqlari: "O‘" = O + tutuq belgisi, "SH" = S + H.
  List<List<Point2>>? letter(String upper) {
    final u = upper.toUpperCase();
    if (glyphs.containsKey(u)) return glyphs[u];
    if (u == 'O‘' || u == 'G‘') {
      final base = glyphs[u[0]];
      if (base == null) return null;
      return [
        ...squeeze(base, 0, 0.84),
        const [Point2(0.95, 0.04), Point2(0.9, 0.2)],
      ];
    }
    if (u.length == 2 && glyphs.containsKey(u[0]) && glyphs.containsKey(u[1])) {
      return [...squeeze(glyphs[u[0]]!, 0, 0.5), ...squeeze(glyphs[u[1]]!, 0.5, 1)];
    }
    return null;
  }

  /// Chiziqlarni [x0]..[x1] gorizontal oralig'iga siqadi.
  static List<List<Point2>> squeeze(List<List<Point2>> strokes, double x0, double x1) => [
        for (final s in strokes) [for (final p in s) Point2(x0 + p.x * (x1 - x0), p.y)],
      ];

  /// Harfning nisbiy kengligi: "SH", "CH", "NG" ikki belgidan iborat — kengroq.
  static double unitWidth(String upper) => upper.length == 2 && upper[1] != '‘' ? 1.6 : 1.0;

  /// So'z yozish maydonining kenglik/balandlik nisbati.
  static double wordAspect(String text, {double perLetter = 0.72}) =>
      UzbekData.letters(text).fold<double>(0, (s, l) => s + unitWidth(l.toUpperCase())) * perLetter;

  /// So'z (bosh harflar bilan) — harflar yonma-yon: chapdan o'ngga yozish.
  List<List<Point2>>? word(String text) {
    final units = UzbekData.letters(text).map((l) => l.toUpperCase()).toList();
    final total = units.fold<double>(0, (s, u) => s + unitWidth(u));
    final result = <List<Point2>>[];
    var x = 0.0;
    for (final u in units) {
      final g = letter(u);
      if (g == null) return null;
      final w = unitWidth(u) / total;
      result.addAll(squeeze(g, x, x + w));
      x += w;
    }
    return result;
  }
}
