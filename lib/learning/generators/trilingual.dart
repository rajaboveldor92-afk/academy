import '../../models/speech_part.dart';
import '../content/instructions.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'foreign_language.dart';
import 'generator_base.dart';

/// 🍎 3 tilda o'rganamiz: bitta tushuncha — o'zbekcha, ruscha, inglizcha (umumiy lug'at ID).
///
/// Har bir so'z o'z tilida aytiladi ("Apple" — ingliz ovozida), savol esa o'zbekcha
/// ("qaysi rasm?"). Ekranda o'zbekcha ko'rsatma.
class Trilingual {
  Trilingual._();

  static final Map<String, ExerciseGenerator> generators = {
    'listen': listen,
    'what_is': whatIs,
    'which_lang': whichLang,
    'match': match,
  };

  static const Map<String, String> flags = {'uz': '🇺🇿', 'ru': '🇷🇺', 'en': '🇬🇧'};

  static const Map<String, Localized> langNames = {
    'uz': Localized(uz: 'o‘zbekcha', en: 'Uzbek', ru: 'узбекское'),
    'ru': Localized(uz: 'ruscha', en: 'Russian', ru: 'русское'),
    'en': Localized(uz: 'inglizcha', en: 'English', ru: 'английское'),
  };

  /// Uch tildagi so'zlari bir-biridan farq qiladigan lug'at elementlari (robot/robot kabilar emas).
  static List<VocabItem> items(GenContext g, List<String> themes) {
    final seen = <String>{};
    final out = <VocabItem>[];
    for (final theme in themes) {
      for (final e in g.lex.entries) {
        final cats = ForeignLanguage.themeCategories[theme] ?? const <String>[];
        if (e.ageMin > g.age || !cats.contains(e.category)) continue;
        final w = e.word;
        if (w.uz.toLowerCase() == w.en.toLowerCase()) continue;
        if (!seen.add(e.id)) continue;
        out.add(VocabItem(id: e.id, kind: 'lex', word: w, emoji: e.emoji));
      }
    }
    return out;
  }

  static List<String> _themes(GenContext g) => g.pl('themes').isEmpty ? ['fruits'] : g.pl('themes');

  /// Har bir tildagi so'zlari takrorlanmaydigan [n] ta element.
  static List<VocabItem> _distinct(GenContext g, List<VocabItem> pool, VocabItem target, int n) {
    final words = {for (final l in ['uz', 'en', 'ru']) l: <String>{target.word.of(l).toLowerCase()}};
    final pics = <String>{target.option.describe()};
    final out = <VocabItem>[];
    for (final x in g.sample(pool, pool.length)) {
      if (out.length >= n) break;
      final ok = ['uz', 'en', 'ru'].every((l) => !words[l]!.contains(x.word.of(l).toLowerCase()));
      if (ok && pics.add(x.option.describe())) {
        for (final l in ['uz', 'en', 'ru']) {
          words[l]!.add(x.word.of(l).toLowerCase());
        }
        out.add(x);
      }
    }
    return out;
  }

  static RenderedInstruction _withParts(RenderedInstruction base, List<SpeechPart> parts) =>
      RenderedInstruction(base.text, parts.map((p) => p.text).join(' '), parts: parts);

  // ------------------------------------------------------------ Eshit → rasm
  /// Rejimlar: `en`, `ru` (bitta til), `all3` (uch tilda ketma-ket).
  static Exercise listen(GenContext g) {
    final pool = items(g, _themes(g));
    final mode = g.pick(g.pl('modes').isEmpty ? ['all3'] : g.pl('modes'));
    final target = g.pick(pool);
    final others = _distinct(g, pool, target, g.p('options', 3) - 1);
    final wd = target.word;
    final RenderedInstruction say;
    if (mode == 'all3') {
      final shown = '${flags['uz']} ${wd.uz} · ${flags['ru']} ${wd.ru} · ${flags['en']} ${wd.en}';
      say = _withParts(g.say('tri_listen3', {'w': Localized.same(shown)}), [
        SpeechPart(wd.uz, 'uz'),
        SpeechPart(wd.ru, 'ru'),
        SpeechPart(wd.en, 'en'),
        const SpeechPart('Qaysi rasm?', 'uz'),
      ]);
    } else {
      final word = wd.of(mode);
      say = _withParts(g.say('tri_which_picture', {'w': Localized.same('${flags[mode]} $word')}), [
        SpeechPart(word, mode),
        const SpeechPart('qaysi rasm?', 'uz'),
      ]);
    }
    return g.choice(
      say: say,
      visual: const TextVisual('🔊', scale: 0.8),
      options: [target.option, for (final o in others) o.option],
      concept: 'tri:${target.id}',
      meta: {'answer': target.id, 'mode': mode},
      explanation: '${wd.uz} · ${wd.ru} · ${wd.en}',
    );
  }

  // ------------------------------------------------------------ "Яблоко nima?"
  /// Ruscha yoki inglizcha so'z → o'zbekcha so'z (6 yosh) yoki rasm (`pictures: true`).
  static Exercise whatIs(GenContext g) {
    final pool = items(g, _themes(g));
    final langs = g.pl('langs').isEmpty ? ['ru', 'en'] : g.pl('langs');
    final lang = g.pick(langs);
    final target = g.pick(pool);
    final others = _distinct(g, pool, target, g.p('options', 3) - 1);
    final word = target.word.of(lang);
    final say = _withParts(g.say('tri_what_is', {'w': Localized.same('${flags[lang]} $word')}), [
      SpeechPart(word, lang),
      const SpeechPart('nima?', 'uz'),
    ]);
    final pictures = g.pb('pictures');
    return g.choice(
      say: say,
      visual: pictures ? const TextVisual('🔊', scale: 0.8) : null,
      options: pictures
          ? [target.option, for (final o in others) o.option]
          : [Opt.text(target.word.uz), for (final o in others) Opt.text(o.word.uz)],
      concept: 'tri:${target.id}',
      meta: {'answer': target.id, 'lang': lang},
      explanation: '$word — ${target.word.uz} ${target.emoji}',
    );
  }

  // ------------------------------------------------------------ Qaysi so'z inglizcha?
  static Exercise whichLang(GenContext g) {
    final pool = items(g, _themes(g)).where((x) {
      final w = x.word;
      return w.uz.toLowerCase() != w.ru.toLowerCase() && w.en.toLowerCase() != w.ru.toLowerCase();
    }).toList();
    final target = g.pick(pool);
    final langs = g.pl('langs').isEmpty ? ['en', 'ru', 'uz'] : g.pl('langs');
    final lang = g.pick(langs);
    final order = [lang, ...['uz', 'ru', 'en'].where((l) => l != lang)];
    return g.choice(
      say: g.say('tri_which_lang', {'lang': langNames[lang]!}),
      visual: target.visual,
      options: [for (final l in order) Opt.text(target.word.of(l))],
      concept: 'tri_lang:$lang',
      meta: {'answer': target.word.of(lang), 'lang': lang},
      explanation: '${flags['uz']} ${target.word.uz} · ${flags['ru']} ${target.word.ru} · ${flags['en']} ${target.word.en}',
    );
  }

  // ------------------------------------------------------------ Juftlash
  static Exercise match(GenContext g) {
    final pool = items(g, _themes(g));
    final langs = g.pl('langs').isEmpty ? ['en', 'ru'] : g.pl('langs');
    final lang = g.pick(langs);
    final count = g.p('pairs', 3);
    final first = g.pick(pool);
    final chosen = [first, ..._distinct(g, pool, first, count - 1)];
    final pairLabel = Localized(
      uz: '${langNames['uz']!.uz} — ${langNames[lang]!.uz}',
      en: '${langNames['uz']!.en} — ${langNames[lang]!.en}',
      ru: 'узбекские — ${lang == 'ru' ? 'русские' : 'английские'}',
    );
    return g.custom(
      say: g.say('tri_match', {'lang': pairLabel}),
      kind: ExerciseKind.match,
      concept: 'tri_match:$lang:${chosen.map((c) => c.id).join(",")}',
      pairs: [for (final c in chosen) MatchPair(Opt.text(c.word.uz), Opt.text(c.word.of(lang)))],
      meta: {'pairs': chosen.map((c) => '${c.word.uz}=${c.word.of(lang)}').join(',')},
    );
  }
}
