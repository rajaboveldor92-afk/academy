import '../../core/utils/map_utils.dart';
import '../models/exercise.dart';
import 'lexicon.dart';
import 'uz_numbers.dart';

/// Tayyor ko'rsatma: ekrandagi matn (3 tilda) va ovozli o'zbekcha matn.
class RenderedInstruction {
  const RenderedInstruction(this.text, this.speech);

  final Localized text;
  final String speech;
}

/// Ko'rsatmalar banki (`assets/data/instructions.json`).
///
/// Shablon: `"Nechta {item} bor?"`. Parametrlar:
/// * `int` — ekranda raqam, ovozda so'z ("7" → "yetti");
/// * [LexiconEntry], [ColorEntry], [ShapeEntry], [Localized] — har tilda o'z so'zi;
/// * `String` — o'zgarishsiz.
class InstructionBank {
  InstructionBank(this._templates);

  final Map<String, Map<String, String>> _templates;

  Iterable<String> get keys => _templates.keys;

  Map<String, String>? template(String key) => _templates[key];

  bool has(String key) => _templates.containsKey(key);

  RenderedInstruction render(String key, [Map<String, Object> params = const {}]) {
    final t = _templates[key];
    if (t == null) throw ArgumentError('Ko\'rsatma topilmadi: $key');
    String fill(String lang, String template, {bool speech = false}) {
      final filled = template.replaceAllMapped(RegExp(r'\{(\w+)(?::(\w+))?\}'), (m) {
        final v = params[m.group(1)!];
        if (v == null) throw ArgumentError('Parametr yo\'q: ${m.group(1)} ($key)');
        final word = _value(v, lang, speech: speech);
        final suffix = m.group(2);
        return (suffix != null && lang == 'uz') ? uzSuffix(word, suffix) : word;
      });
      return capitalize(filled);
    }

    final text = Localized(
      uz: fill('uz', t['uz']!),
      en: fill('en', t['en']!),
      ru: fill('ru', t['ru']!),
    );
    final speechTemplate = t['speech'] ?? t['uz']!;
    return RenderedInstruction(text, toSpeech(fill('uz', speechTemplate, speech: true)));
  }

  static String _value(Object v, String lang, {bool speech = false}) {
    if (v is int) return speech ? UzNumbers.word(v) : '$v';
    if (v is LexiconEntry) return v.word.of(lang);
    if (v is ColorEntry) return v.name.of(lang);
    if (v is ShapeEntry) return v.name.of(lang);
    if (v is Localized) return v.of(lang);
    return v.toString();
  }

  /// O'zbekcha qo'shimcha: jo'nalish kelishigi `-ga` (k → ka, q → qa, g → ga).
  static String uzSuffix(String word, String suffix) {
    if (suffix != 'ga' || word.isEmpty) return '$word$suffix';
    final last = word[word.length - 1];
    if (last == 'k') return '${word}ka';
    if (last == 'q') return '${word}qa';
    return '${word}ga';
  }

  /// Gap bosh harf bilan boshlansin (emoji yoki raqam bo'lsa o'zgarmaydi).
  static String capitalize(String s) {
    if (s.isEmpty) return s;
    return s[0].toUpperCase() + s.substring(1);
  }

  /// Matnni ovoz uchun tayyorlaydi: raqamlar va belgilar so'z bilan.
  static String toSpeech(String text) {
    var s = text
        .replaceAll('+', ' qo‘shuv ')
        .replaceAll('−', ' ayiruv ')
        .replaceAll(' - ', ' ayiruv ')
        .replaceAll('=', ' teng ')
        .replaceAll('>', ' katta ')
        .replaceAll('<', ' kichik ')
        .replaceAll('?', '?');
    s = UzNumbers.spellDigits(s);
    return s.replaceAll(RegExp(r'\s+'), ' ').trim();
  }

  factory InstructionBank.fromJson(Map<String, dynamic> json) {
    final map = <String, Map<String, String>>{};
    MapUtils.asStringMap(json['instructions']).forEach((k, v) {
      final m = MapUtils.asStringMap(v);
      map[k] = m.map((lang, text) => MapEntry(lang, text.toString()));
    });
    return InstructionBank(map);
  }
}
