import 'dart:math' as math;

import '../content/instructions.dart';
import '../content/language_data.dart';
import '../content/lexicon.dart';
import '../content/number_words.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';

/// Lug'at elementi: rasm (emoji yoki sahna) + uch tildagi so'z.
class VocabItem {
  const VocabItem({required this.id, required this.kind, required this.word, this.emoji, this.scene = const []});

  final String id;

  /// `lex` (lug'at), `action`, `adj`, `phrase`.
  final String kind;
  final Localized word;
  final String? emoji;
  final List<String> scene;

  ExerciseVisual get visual => scene.isEmpty
      ? SceneVisual([Layouts.emoji(emoji!, size: 0.8)], aspect: 1.6)
      : SceneVisual(Layouts.row([for (final e in scene) Layouts.emoji(e, size: 0.6)]), aspect: 1.6);

  ExerciseOption get option => scene.isEmpty
      ? Opt.emoji(emoji!)
      : Opt.scene(Layouts.row([for (final e in scene) Layouts.emoji(e, size: 0.55)], left: 0.1, right: 0.9), aspect: 1.3);
}

/// 🇬🇧 English va 🇷🇺 Русский: bitta generatorlar to'plami, til — mavzuning fanidan.
///
/// * 4 yosh: eshitish → rasm tanlash, qayta eshitish (🔊), harf va rasm.
/// * 6 yosh: harf, "qaysi harf bilan boshlanadi", so'z o'qish/yozish, rang va son
///   so'zlari, harakatlar, qarama-qarshi so'zlar, oddiy gap, tinglab tushunish, iboralar.
///
/// Ko'rsatma va ovoz — o'rganilayotgan tilda; ekranda o'zbekcha umumiy yordamchi
/// matn ham bor (javobni oshkor qilmaydi).
class ForeignLanguage {
  ForeignLanguage._();

  static final Map<String, ExerciseGenerator> generators = {
    'vocab': vocab,
    'colors': colors,
    'numbers': numbers,
    'letters': letters,
    'case_match': caseMatch,
    'first_letter': firstLetter,
    'vowels': vowels,
    'alphabet_listen': alphabetListen,
    'spell': spell,
    'syllables': syllables,
    'opposites': opposites,
    'sentence': sentence,
  };

  static String langOf(GenContext g) => g.topic.subject == 'russian' ? 'ru' : 'en';

  /// Mavzu → lug'at kategoriyalari. Maxsus mavzular: `actions`, `opposites`, `phrases`.
  static const Map<String, List<String>> themeCategories = {
    'animals': ['animal', 'bird', 'insect', 'sea'],
    'fruits': ['fruit'],
    'vegetables': ['vegetable'],
    'fruits_veg': ['fruit', 'vegetable'],
    'food': ['food'],
    'food_all': ['food', 'fruit', 'vegetable'],
    'family': ['family', 'fairy'],
    'body': ['body'],
    'family_body': ['family', 'fairy', 'body'],
    'toys': ['toy'],
    'school': ['school'],
    'toys_school': ['toy', 'school'],
    'transport': ['vehicle'],
    'home': ['home'],
    'clothes': ['clothes'],
    'clothes_home': ['clothes', 'home'],
    'nature': ['nature', 'holiday'],
    'jobs_places': ['profession', 'place'],
    'transport_city': ['vehicle', 'profession', 'place'],
    'animals_nature': ['animal', 'bird', 'insect', 'sea', 'nature', 'holiday'],
  };

  static const Set<String> specialThemes = {'actions', 'opposites', 'phrases'};

  /// Mavzuga kiruvchi lug'at elementlari (yoshga mos).
  static List<VocabItem> items(GenContext g, String theme) {
    final lang = langOf(g);
    final data = g.content.languages;
    switch (theme) {
      case 'actions':
        return [
          for (final a in data.actions)
            if (a.ageMin <= g.age) VocabItem(id: a.id, kind: 'action', word: a.now, emoji: a.emoji),
        ];
      case 'opposites':
        return [
          for (final a in data.adjectives)
            if (a.emoji != null) VocabItem(id: a.id, kind: 'adj', word: a.word(), emoji: a.emoji),
        ];
      case 'phrases':
        return [
          for (final p in data.phrases)
            if (p.ageMin <= g.age) VocabItem(id: p.id, kind: 'phrase', word: p.text, scene: p.scene),
        ];
    }
    final cats = themeCategories[theme] ?? const <String>[];
    final seen = <String>{};
    return [
      for (final e in g.lex.entries)
        if (e.ageMin <= g.age && cats.contains(e.category) && seen.add(e.word.of(lang).toLowerCase()))
          VocabItem(id: e.id, kind: 'lex', word: e.word, emoji: e.emoji),
    ];
  }

  /// Boshqa mavzulardagi lug'at elementlari (chalg'ituvchi sifatida — 1-daraja osonroq).
  static List<VocabItem> otherItems(GenContext g, String theme) {
    final lang = langOf(g);
    final cats = themeCategories[theme] ?? const <String>[];
    final all = themeCategories.values.expand((c) => c).toSet();
    final seen = <String>{};
    return [
      for (final e in g.lex.entries)
        if (e.ageMin <= g.age && !cats.contains(e.category) && all.contains(e.category) && seen.add(e.word.of(lang).toLowerCase()))
          VocabItem(id: e.id, kind: 'lex', word: e.word, emoji: e.emoji),
    ];
  }

  /// [pool] dan [n] ta element: so'zi (shu tilda) va rasmi nishondagidan farq qiladi.
  static List<VocabItem> distinctSample(GenContext g, List<VocabItem> pool, VocabItem target, int n, String lang) {
    final words = <String>{target.word.of(lang).toLowerCase()};
    final pics = <String>{target.option.describe()};
    final out = <VocabItem>[];
    for (final x in g.sample(pool, pool.length)) {
      if (out.length >= n) break;
      if (words.add(x.word.of(lang).toLowerCase()) && pics.add(x.option.describe())) out.add(x);
    }
    return out;
  }

  /// Tinglash mashqi: ekranda umumiy ko'rsatma ("Listen and find"), ovozda — so'z bilan.
  static RenderedInstruction listenSay(GenContext g, String lang, String speechKey, Map<String, Object> params) {
    final shown = g.sayIn(lang, 'lg_listen');
    final spoken = g.sayIn(lang, speechKey, params);
    return RenderedInstruction(shown.text, spoken.speech, lang: lang, key: shown.key);
  }

  static Localized w(String text) => Localized.same(text);

  static String _explain(VocabItem it, String lang) => '${it.word.of(lang)} — ${it.word.uz}';

  // ------------------------------------------------------------ Lug'at
  /// Rejimlar: `listen` (eshit → rasm), `read` (o'qi → rasm), `picture_word` (rasm → so'z).
  static Exercise vocab(GenContext g) {
    final lang = langOf(g);
    final themes = g.pl('themes').isEmpty ? ['animals'] : g.pl('themes');
    final theme = g.pick(themes);
    final mode = g.pick(g.pl('modes').isEmpty ? ['listen'] : g.pl('modes'));
    final optCount = g.p('options', 3);
    final pool = items(g, theme);
    final target = g.pick(pool);
    final same = g.pb('sameTheme') || specialThemes.contains(theme);
    final others = distinctSample(g, same ? pool : otherItems(g, theme), target, optCount - 1, lang);
    final word = target.word.of(lang);
    final meta = <String, Object>{'answer': target.id, 'word': word, 'theme': theme};
    switch (mode) {
      case 'read':
        return g.choice(
          say: g.sayIn(lang, 'lg_read'),
          visual: ReadingVisual(word, big: word.length <= 12),
          options: [target.option, for (final o in others) o.option],
          concept: 'vocab:$lang:${target.id}',
          meta: meta,
          explanation: _explain(target, lang),
        );
      case 'picture_word':
        final key = switch (target.kind) {
          'action' => 'lg_what_action',
          'adj' => 'lg_what_adj',
          'phrase' => 'lg_what_phrase',
          _ => 'lg_what',
        };
        return g.choice(
          say: g.sayIn(lang, key),
          visual: target.visual,
          options: [Opt.text(word), for (final o in others) Opt.text(o.word.of(lang))],
          concept: 'vocab:$lang:${target.id}',
          meta: meta,
          explanation: _explain(target, lang),
        );
      default:
        final key = switch (target.kind) {
          'action' => 'lg_find_action',
          'adj' => 'lg_find_word',
          'phrase' => 'lg_find_phrase',
          _ => 'lg_find',
        };
        return g.choice(
          say: listenSay(g, lang, key, {'w': w(word)}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [target.option, for (final o in others) o.option],
          concept: 'vocab:$lang:${target.id}',
          meta: meta,
          hint: _explain(target, lang),
          explanation: _explain(target, lang),
        );
    }
  }

  // ------------------------------------------------------------ Ranglar
  /// Rejimlar: `listen`, `read`, `picture_word`, `object` ("Find something red").
  static Exercise colors(GenContext g) {
    final lang = langOf(g);
    final data = g.content.languages;
    final ids = g.pl('colors').isEmpty ? ['red', 'yellow', 'blue'] : g.pl('colors');
    final pool = ids.map(g.lex.color).toList();
    final optCount = g.p('options', 3);
    final mode = g.pick(g.pl('modes').isEmpty ? ['listen'] : g.pl('modes'));
    const shapes = ['circle', 'square', 'heart', 'star'];
    final chosen = g.sample(pool, math.min(optCount, pool.length));
    final target = chosen.first;
    final name = target.name.of(lang);
    final shape = g.pick(shapes);
    final meta = <String, Object>{'answer': target.id};
    final explanation = '$name — ${target.name.uz}';
    switch (mode) {
      case 'object':
        final withColor = g.lex.entries
            .where((e) => e.ageMin <= g.age && e.color != null && ids.contains(e.color))
            .toList();
        final colorTarget = g.pick(pool.where((c) => withColor.any((e) => e.color == c.id)).toList());
        final correct = g.pick(withColor.where((e) => e.color == colorTarget.id).toList());
        final used = <String>{colorTarget.id};
        final wrong = <LexiconEntry>[];
        for (final e in g.sample(withColor, withColor.length)) {
          if (wrong.length >= optCount - 1) break;
          if (used.add(e.color!)) wrong.add(e);
        }
        final objName = colorTarget.name.of(lang);
        final shown = lang == 'ru' ? data.colorRu(colorTarget.id, 'n') : objName;
        return g.choice(
          say: listenSay(g, lang, 'lg_find_color_object', {'w': w(shown)}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [Opt.emoji(correct.emoji), for (final e in wrong) Opt.emoji(e.emoji)],
          concept: 'color:$lang:${colorTarget.id}',
          meta: {'answer': colorTarget.id},
          explanation: '$shown — ${colorTarget.name.uz}',
        );
      case 'read':
        return g.choice(
          say: g.sayIn(lang, 'lg_read_color'),
          visual: ReadingVisual(name, big: true),
          options: [for (final c in chosen) Opt.shape(shape, c.color)],
          concept: 'color:$lang:${target.id}',
          meta: meta,
          explanation: explanation,
        );
      case 'picture_word':
        return g.choice(
          say: g.sayIn(lang, 'lg_what_color'),
          visual: SceneVisual([Layouts.shape(shape, target.color, size: 0.7)], aspect: 1.6),
          options: [for (final c in chosen) Opt.text(c.name.of(lang))],
          concept: 'color:$lang:${target.id}',
          meta: meta,
          explanation: explanation,
        );
      default:
        return g.choice(
          say: listenSay(g, lang, 'lg_find_color', {'w': w(name)}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final c in chosen) Opt.shape(shape, c.color)],
          concept: 'color:$lang:${target.id}',
          meta: meta,
          hint: explanation,
          explanation: explanation,
        );
    }
  }

  // ------------------------------------------------------------ Sonlar
  /// Rejimlar: `listen_group`, `listen_digit`, `read_word`, `match`.
  static Exercise numbers(GenContext g) {
    final lang = langOf(g);
    final min = g.p('min', 1), max = g.p('max', 5);
    final optCount = g.p('options', 3);
    final mode = g.pick(g.pl('modes').isEmpty ? ['listen_digit'] : g.pl('modes'));
    if (mode == 'match') {
      final count = g.p('pairs', 3);
      final nums = g.sample([for (var i = min; i <= max; i++) i], count);
      return g.custom(
        say: g.sayIn(lang, 'lg_match_numbers'),
        kind: ExerciseKind.match,
        concept: 'numbers:$lang:${nums.join(",")}',
        pairs: [for (final n in nums) MatchPair(Opt.number(n), Opt.text(NumberWords.word(n, lang)))],
        meta: {'pairs': nums.map((n) => '$n=${NumberWords.word(n, lang)}').join(',')},
      );
    }
    final n = g.range(min, max);
    final word = NumberWords.word(n, lang);
    final nums = g.numberChoices(n, count: optCount, min: math.max(1, min), max: math.max(max, 5), spread: 2);
    final explanation = '$n — $word';
    switch (mode) {
      case 'listen_group':
        final item = g.pick(g.countables());
        return g.choice(
          say: listenSay(g, lang, 'lg_find_group', {'w': w(word)}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final v in nums) Opt.group(item.emoji, v)],
          concept: 'number:$lang:$n',
          meta: {'answer': n},
          explanation: explanation,
        );
      case 'read_word':
        final item = g.pick(g.countables());
        return g.choice(
          say: g.sayIn(lang, 'lg_how_many'),
          visual: SceneVisual(Layouts.group(item.emoji, n, aspect: 2), aspect: 2),
          options: [for (final v in nums) Opt.text(NumberWords.word(v, lang))],
          concept: 'number:$lang:$n',
          meta: {'answer': word, 'count': n},
          explanation: explanation,
        );
      default:
        return g.choice(
          say: listenSay(g, lang, 'lg_find_number', {'w': w(word)}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final v in nums) Opt.number(v)],
          concept: 'number:$lang:$n',
          meta: {'answer': n},
          hint: explanation,
          explanation: explanation,
        );
    }
  }

  // ------------------------------------------------------------ Harflar
  static List<LangLetter> _letterPool(GenContext g, String lang, String set) {
    final all = g.content.languages.alphabet(lang);
    return switch (set) {
      'vowels' => all.where((l) => l.vowel).toList(),
      'consonants' => all.where((l) => !l.vowel && !_signs.contains(l.lower)).toList(),
      'common' => all.where((l) => !_signs.contains(l.lower)).toList(),
      _ => all,
    };
  }

  /// Rus tilidagi belgilar (tovush bildirmaydi).
  static const Set<String> _signs = {'ъ', 'ь'};

  /// Rejimlar: `upper`, `lower`, `mixed` (bosh harf ko'rsatiladi — kichigini top).
  static Exercise letters(GenContext g) {
    final lang = langOf(g);
    final optCount = g.p('options', 3);
    final mode = g.pick(g.pl('modes').isEmpty ? ['upper'] : g.pl('modes'));
    final pool = _letterPool(g, lang, g.ps('set', 'all'));
    final alphabet = g.content.languages.alphabet(lang);
    final target = g.pick(pool);
    final wrong = <LangLetter>[];
    // O'xshash harflar chalg'ituvchi sifatida (b/d, p/q, Ш/Щ, Е/Ё ...).
    for (final s in (_similar[target.lower] ?? const <String>[])) {
      final l = alphabet.where((x) => x.lower == s);
      if (g.pb('similar') && l.isNotEmpty && wrong.length < optCount - 1) wrong.add(l.first);
    }
    for (final l in g.sample(alphabet, alphabet.length)) {
      if (wrong.length >= optCount - 1) break;
      if (l.lower != target.lower && !wrong.contains(l)) wrong.add(l);
    }
    String shown(LangLetter l) => mode == 'upper' ? l.upper : l.lower;
    return g.choice(
      say: g.sayIn(lang, mode == 'mixed' ? 'lg_find_small_letter' : 'lg_find_letter', {'l': target.upper}),
      visual: mode == 'mixed' ? TextVisual(target.upper, scale: 1.4) : null,
      options: [Opt.text(shown(target)), for (final l in wrong) Opt.text(shown(l))],
      concept: 'letter:$lang:${target.lower}',
      meta: {'answer': target.lower},
      explanation: _letterExplain(g, target, lang),
    );
  }

  static const Map<String, List<String>> _similar = {
    'b': ['d', 'p'], 'd': ['b', 'q'], 'p': ['q', 'b'], 'q': ['p', 'g'], 'm': ['n', 'w'], 'n': ['m', 'h'],
    'u': ['v', 'n'], 'v': ['u', 'w'], 'i': ['l', 'j'], 'l': ['i', 't'],
    'ш': ['щ', 'и'], 'щ': ['ш', 'ц'], 'е': ['ё', 'э'], 'ё': ['е', 'о'], 'и': ['й', 'н'], 'й': ['и', 'ц'],
    'б': ['в', 'д'], 'в': ['б', 'з'], 'п': ['н', 'л'], 'ь': ['ъ', 'ы'], 'ъ': ['ь', 'ы'], 'ы': ['ь', 'и'],
  };

  static String _letterExplain(GenContext g, LangLetter l, String lang) {
    final id = l.lexId;
    if (id == null || !g.lex.contains(id)) return '${l.upper} ${l.lower}';
    final e = g.lex.byId(id);
    return '${l.upper} ${l.lower} — ${e.word.of(lang)} ${e.emoji}';
  }

  static Exercise caseMatch(GenContext g) {
    final lang = langOf(g);
    final pool = _letterPool(g, lang, g.ps('set', 'common'))
        // Bosh va kichik shakli bir xil ko'rinadigan harflar (o/O, с/С) ham o'rgatiladi, lekin
        // juftlashda ular 2 tadan ko'p bo'lmasin — aks holda mashq juda oson.
        .toList();
    final chosen = g.sample(pool, g.p('pairs', 3));
    return g.custom(
      say: g.sayIn(lang, 'lg_match_case'),
      kind: ExerciseKind.match,
      concept: 'case:$lang:${chosen.map((l) => l.lower).join(",")}',
      pairs: [for (final l in chosen) MatchPair(Opt.text(l.upper), Opt.text(l.lower))],
      meta: {'pairs': chosen.map((l) => '${l.upper}=${l.lower}').join(',')},
    );
  }

  /// Birinchi harfi tovushiga mos keladigan so'zlar (ingliz tilida kn-, wr-, ph-, ce- kabilar chiqarib tashlanadi).
  static bool goodInitial(String word, String lang) {
    if (word.contains(' ') || word.contains('-')) return false;
    final w = word.toLowerCase();
    if (lang == 'en') {
      if (!RegExp(r'^[a-z]+$').hasMatch(w)) return false;
      if (RegExp(r'^(kn|wr|ph|ch|sh|th|wh|gn|ps)').hasMatch(w)) return false;
      if (RegExp(r'^[cg][eiy]').hasMatch(w)) return false;
      return true;
    }
    return RegExp(r'^[а-яё]+$').hasMatch(w) && !const {'ъ', 'ь', 'ы'}.contains(w[0]);
  }

  static Exercise firstLetter(GenContext g) {
    final lang = langOf(g);
    final optCount = g.p('options', 3);
    final entries = g.lex.entries.where((e) => e.ageMin <= g.age && goodInitial(e.word.of(lang), lang)).toList();
    final byLetter = <String, List<LexiconEntry>>{};
    for (final e in entries) {
      byLetter.putIfAbsent(e.word.of(lang)[0].toLowerCase(), () => []).add(e);
    }
    final allowed = g.pl('letters');
    final letters = byLetter.keys.where((l) => allowed.isEmpty || allowed.contains(l)).toList();
    final letter = g.pick(letters);
    final target = g.pick(byLetter[letter]!);
    final wrongPool = entries.where((e) => e.word.of(lang)[0].toLowerCase() != letter).toList();
    final wrong = <LexiconEntry>[];
    final firsts = <String>{letter};
    for (final e in g.sample(wrongPool, wrongPool.length)) {
      if (wrong.length >= optCount - 1) break;
      // Chalg'ituvchilar ham har xil harf bilan boshlansin.
      if (firsts.add(e.word.of(lang)[0].toLowerCase())) wrong.add(e);
    }
    final upper = letter.toUpperCase();
    return g.choice(
      say: g.sayIn(lang, 'lg_first_letter', {'l': upper}),
      visual: TextVisual('$upper $letter', scale: 1.1),
      options: [Opt.emoji(target.emoji), for (final e in wrong) Opt.emoji(e.emoji)],
      concept: 'sound:$lang:$letter',
      meta: {'answer': target.id, 'letter': letter},
      explanation: '${target.word.of(lang)} — $upper',
    );
  }

  /// "Unli harfni top" / "Undosh harfni top".
  static Exercise vowels(GenContext g) {
    final lang = langOf(g);
    final optCount = g.p('options', 3);
    final find = g.pick(g.pl('modes').isEmpty ? ['vowel'] : g.pl('modes'));
    final vowels = _letterPool(g, lang, 'vowels');
    final consonants = _letterPool(g, lang, 'consonants');
    final wantVowel = find == 'vowel';
    final target = g.pick(wantVowel ? vowels : consonants);
    final wrong = g.sample(wantVowel ? consonants : vowels, optCount - 1);
    return g.choice(
      say: g.sayIn(lang, wantVowel ? 'lg_find_vowel' : 'lg_find_consonant'),
      options: [Opt.text(target.upper), for (final l in wrong) Opt.text(l.upper)],
      concept: 'vowel:$lang:${target.lower}',
      meta: {'answer': target.lower},
      explanation: wantVowel ? '${target.upper} — unli' : '${target.upper} — undosh',
    );
  }

  /// 4 yosh: "A is for apple. Find the apple." — harf nomi va so'z bilan tanishish.
  static Exercise alphabetListen(GenContext g) {
    final lang = langOf(g);
    final optCount = g.p('options', 3);
    final letters = g.content.languages
        .alphabet(lang)
        .where((l) => l.initial && l.lexId != null && g.lex.contains(l.lexId!))
        .where((l) => g.pl('letters').isEmpty || g.pl('letters').contains(l.lower))
        .toList();
    final letter = g.pick(letters);
    final target = g.lex.byId(letter.lexId!);
    final word = target.word.of(lang);
    final pool = g.lex.entries
        .where((e) => e.ageMin <= g.age && e.id != target.id && e.word.of(lang).toLowerCase()[0] != letter.lower)
        .map((e) => VocabItem(id: e.id, kind: 'lex', word: e.word, emoji: e.emoji))
        .toList();
    final t = VocabItem(id: target.id, kind: 'lex', word: target.word, emoji: target.emoji);
    final others = distinctSample(g, pool, t, optCount - 1, lang);
    return g.choice(
      say: listenSay(g, lang, 'lg_alphabet', {'l': letter.upper, 'w': w(word)}),
      visual: TextVisual('${letter.upper} ${letter.lower}', scale: 1.2),
      options: [t.option, for (final o in others) o.option],
      concept: 'letter:$lang:${letter.lower}',
      meta: {'answer': target.id, 'letter': letter.lower},
      explanation: '${letter.upper} — $word',
    );
  }

  // ------------------------------------------------------------ So'z yozish (harflardan)
  static bool spellable(String word, String lang) =>
      lang == 'en' ? RegExp(r'^[a-z]+$').hasMatch(word) : RegExp(r'^[а-яё]+$').hasMatch(word);

  static Exercise spell(GenContext g) {
    final lang = langOf(g);
    final minL = g.p('minLetters', 3), maxL = g.p('maxLetters', 4);
    final entries = g.lex.entries.where((e) {
      final wd = e.word.of(lang);
      return e.ageMin <= g.age && spellable(wd, lang) && wd.length >= minL && wd.length <= maxL;
    }).toList();
    final target = g.pick(entries);
    final word = target.word.of(lang);
    final letters = word.split('');
    final tiles = [...letters];
    final extra = g.p('extra', 0);
    if (extra > 0) {
      final pool = g.content.languages
          .alphabet(lang)
          .map((l) => l.lower)
          .where((l) => !letters.contains(l) && !_signs.contains(l))
          .toList();
      tiles.addAll(g.sample(pool, extra));
    }
    return g.custom(
      say: g.sayIn(lang, 'lg_spell', {'w': w(word)}),
      kind: ExerciseKind.assemble,
      visual: SceneVisual([Layouts.emoji(target.emoji, size: 0.8)], aspect: 1.6),
      concept: 'spell:$lang:${target.id}',
      assemble: AssembleTask(answer: letters, tiles: g.mixTiles(tiles, letters)),
      meta: {'answer': word},
      explanation: '$word — ${target.uz}',
    );
  }

  // ------------------------------------------------------------ Bo'g'inlar (rus tili)
  /// Rejimlar: `count` (unli harflar soni = bo'g'inlar), `build`, `missing`.
  static Exercise syllables(GenContext g) {
    final lang = langOf(g);
    final data = g.content.languages;
    final mode = g.pick(g.pl('modes').isEmpty ? ['count'] : g.pl('modes'));
    final maxSyl = g.p('maxSyl', 3);
    bool isVowel(String ch) => (lang == 'ru' ? LanguageData.ruVowels : LanguageData.enVowels).contains(ch);
    if (mode == 'count') {
      final entries = g.lex.entries.where((e) {
        final wd = e.word.of(lang);
        final n = wd.split('').where(isVowel).length;
        return e.ageMin <= g.age && spellable(wd, lang) && n >= 1 && n <= maxSyl;
      }).toList();
      final target = g.pick(entries);
      final word = target.word.of(lang);
      final n = word.split('').where(isVowel).length;
      final opts = <int>{n, if (n > 1) n - 1, n + 1, n + 2}.take(3).toList();
      final sy = data.ruSyllables[target.id];
      return g.choice(
        say: g.sayIn(lang, 'lg_count_syllables'),
        visual: ReadingVisual(word, emoji: target.emoji, big: true),
        options: [for (final v in opts) Opt.number(v)],
        concept: 'syllable_count:$lang:$n',
        meta: {'answer': n, 'word': word},
        hint: 'Nechta unli harf bo‘lsa, shuncha bo‘g‘in.',
        explanation: sy != null ? '${sy.join(' - ')} — $n' : '$word — $n',
      );
    }
    final candidates = data.ruSyllables.entries
        .where((e) => g.lex.contains(e.key) && g.lex.byId(e.key).ageMin <= g.age && e.value.length >= 2 && e.value.length <= maxSyl)
        .toList();
    final pick = g.pick(candidates);
    final target = g.lex.byId(pick.key);
    final sy = pick.value;
    if (mode == 'build') {
      final tiles = [...sy];
      final extra = g.p('extra', 0);
      if (extra > 0) {
        final pool = [for (final c in candidates) ...c.value].where((s) => !sy.contains(s)).toSet().toList();
        tiles.addAll(g.sample(pool, extra));
      }
      return g.custom(
        say: g.sayIn(lang, 'lg_build_syllables'),
        kind: ExerciseKind.assemble,
        visual: SceneVisual([Layouts.emoji(target.emoji, size: 0.8)], aspect: 1.6),
        concept: 'syllable:$lang:${target.id}',
        assemble: AssembleTask(answer: sy, tiles: g.mixTiles(tiles, sy)),
        meta: {'answer': sy.join()},
        explanation: '${sy.join(' - ')} → ${sy.join()}',
      );
    }
    final idx = g.rng.nextInt(sy.length);
    final correct = sy[idx];
    final realWords = {for (final e in g.lex.entries) e.word.of(lang)};
    final others = <String>{};
    for (final c in g.sample(candidates, candidates.length)) {
      for (final s in c.value) {
        final alt = [for (var i = 0; i < sy.length; i++) i == idx ? s : sy[i]].join();
        if (s != correct && others.length < 2 && !realWords.contains(alt)) others.add(s);
      }
      if (others.length >= 2) break;
    }
    final shown = [for (var i = 0; i < sy.length; i++) i == idx ? '?' : sy[i]].join(' - ');
    return g.choice(
      say: g.sayIn(lang, 'lg_missing_syllable'),
      visual: ReadingVisual(shown, emoji: target.emoji, big: true),
      options: [Opt.text(correct), for (final o in others) Opt.text(o)],
      concept: 'syllable:$lang:${target.id}',
      meta: {'answer': correct, 'word': sy.join()},
      explanation: sy.join(' - '),
    );
  }

  // ------------------------------------------------------------ Qarama-qarshi so'zlar
  /// Rejimlar: `size` (katta/kichik narsa), `length` (uzun/qisqa chiziq), `listen` (eshit → rasm),
  /// `read` (o'qi → rasm).
  static Exercise opposites(GenContext g) {
    final lang = langOf(g);
    final data = g.content.languages;
    final mode = g.pick(g.pl('modes').isEmpty ? ['size'] : g.pl('modes'));
    switch (mode) {
      case 'size':
        final big = g.chance(0.5);
        final adj = data.adjective(big ? 'big' : 'small');
        final nouns = g.countables().where((e) => !e.word.of(lang).contains(' ') && (lang != 'ru' || data.ruGender[e.id] != null && data.ruGender[e.id] != 'pl')).toList();
        final item = g.pick(nouns);
        final gender = lang == 'ru' ? data.ruGender[item.id]! : 'm';
        const sizes = [0.35, 0.58, 0.85];
        final correct = big ? sizes.last : sizes.first;
        final ordered = [correct, ...sizes.where((s) => s != correct)];
        return g.choice(
          say: listenSay(g, lang, 'lg_find_big', {'a': w(adj.word(gender).of(lang)), 'w': w(item.word.of(lang))}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final s in ordered) Opt.emoji(item.emoji, size: s)],
          concept: 'adj:$lang:${adj.id}',
          meta: {'answer': adj.id, 'item': item.id},
          explanation: '${adj.word(gender).of(lang)} — ${adj.uz}',
        );
      case 'length':
        final long = g.chance(0.5);
        final adj = data.adjective(long ? 'long' : 'short');
        const lengths = [0.25, 0.5, 0.85];
        final correct = long ? lengths.last : lengths.first;
        final ordered = [correct, ...lengths.where((s) => s != correct)];
        final color = g.lex.color(g.pick(const ['red', 'blue', 'green', 'orange', 'purple'])).color;
        return g.choice(
          say: listenSay(g, lang, 'lg_find_line', {'a': w(adj.word('f').of(lang))}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [
            for (final l in ordered)
              Opt.scene([SceneItem(kind: SceneKind.bar, value: 'bar', length: l, size: 0.16, color: color)], aspect: 1.6),
          ],
          concept: 'adj:$lang:${adj.id}',
          meta: {'answer': adj.id},
          explanation: '${adj.word('f').of(lang)} — ${adj.uz}',
        );
      default:
        final pool = items(g, 'opposites');
        final target = g.pick(pool);
        final pairItem = pool.firstWhere((x) => x.id == data.adjective(target.id).pair);
        final rest = distinctSample(g, pool.where((x) => x.id != pairItem.id).toList(), target, g.p('options', 3) - 2, lang);
        final opts = [target, pairItem, ...rest];
        final word = target.word.of(lang);
        if (mode == 'read') {
          return g.choice(
            say: g.sayIn(lang, 'lg_read'),
            visual: ReadingVisual(word, big: true),
            options: [for (final o in opts) o.option],
            concept: 'adj:$lang:${target.id}',
            meta: {'answer': target.id},
            explanation: _explain(target, lang),
          );
        }
        return g.choice(
          say: listenSay(g, lang, 'lg_find_word', {'w': w(word)}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [for (final o in opts) o.option],
          concept: 'adj:$lang:${target.id}',
          meta: {'answer': target.id},
          hint: _explain(target, lang),
          explanation: _explain(target, lang),
        );
    }
  }

  // ------------------------------------------------------------ Gaplar
  static String _cap(String s) => s.isEmpty ? s : s[0].toUpperCase() + s.substring(1);

  /// Inglizcha artikl: a / an (unicorn — "a", chunki "yu" deb o'qiladi).
  static String article(String noun) {
    const yu = {'unicorn', 'uniform', 'ukulele', 'university'};
    return RegExp(r'^[aeiou]').hasMatch(noun) && !yu.contains(noun) ? 'an' : 'a';
  }

  static const _countCats = {'fruit', 'toy', 'animal', 'bird', 'insect', 'sea', 'vehicle'};

  /// Tasodifiy oddiy gap: so'zlar, mos rasm (sahna), turi va ma'no kaliti.
  static ({List<String> words, List<SceneItem> scene, String type, String key}) makeSentence(
      GenContext g, String lang, List<String> types) {
    final data = g.content.languages;
    var type = g.pick(types);
    if (lang == 'ru' && type == 'count') type = 'this';
    final ambiguous = ambiguousWords(g, lang);
    bool single(LexiconEntry e) =>
        e.ageMin <= g.age &&
        !e.word.of(lang).contains(' ') &&
        !e.word.of(lang).contains('-') &&
        !ambiguous.contains(e.word.of(lang));
    switch (type) {
      case 'color':
        final items = g.lex.entries
            .where((e) => single(e) && e.color != null && const {'fruit', 'vegetable', 'toy', 'clothes', 'vehicle', 'animal'}.contains(e.category))
            .where((e) => lang != 'ru' || data.ruGender[e.id] != null)
            .toList();
        final it = g.pick(items);
        final noun = it.word.of(lang);
        final words = lang == 'en'
            ? ['The', noun, 'is', g.lex.color(it.color!).name.en]
            : [_cap(noun), data.colorRu(it.color!, data.ruGender[it.id]!)];
        return (words: words, scene: [Layouts.emoji(it.emoji, size: 0.75)], type: type, key: '${it.id}:${it.color}');
      case 'count':
        final items = g.lex.entries.where((e) => single(e) && _countCats.contains(e.category) && data.enPlural[e.id] != null).toList();
        final it = g.pick(items);
        final n = g.range(2, 5);
        return (
          words: ['I', 'see', NumberWords.word(n, 'en'), data.enPlural[it.id]!],
          scene: Layouts.group(it.emoji, n, aspect: 1.6),
          type: type,
          key: '${it.id}:$n',
        );
      case 'action':
        final action = g.pick(data.animalActions);
        final subjects = g.lex.entries
            .where((e) =>
                single(e) &&
                action.categories.contains(e.category) &&
                (action.tag.isEmpty || e.has(action.tag)) &&
                (lang == 'en' ? data.enPlural[e.id] != null : (data.ruGender[e.id] != null && data.ruGender[e.id] != 'pl')))
            .toList();
        final s = g.pick(subjects);
        final noun = s.word.of(lang);
        final words = lang == 'en' ? ['The', noun, ...action.en.split(' ')] : [_cap(noun), action.ru];
        return (
          words: words,
          scene: [Layouts.emoji(s.emoji, x: 0.35, size: 0.6), Layouts.emoji(action.context, x: 0.72, size: 0.42)],
          type: type,
          key: '${s.id}:${action.id}',
        );
      default:
        final items = g.lex.entries
            .where((e) => single(e) && const {'fruit', 'animal', 'toy', 'vehicle', 'bird', 'school', 'clothes'}.contains(e.category))
            .where((e) => lang != 'en' || data.enPlural[e.id] != null)
            .toList();
        final it = g.pick(items);
        final noun = it.word.of(lang);
        final words = lang == 'en' ? ['It', 'is', article(noun), noun] : ['Это', noun];
        return (words: words, scene: [Layouts.emoji(it.emoji, size: 0.75)], type: 'this', key: it.id);
    }
  }

  /// Lug'atda bir necha rasmga to'g'ri keladigan so'zlar (ru: замок — qasr va qulf).
  static Set<String> ambiguousWords(GenContext g, String lang) {
    final seen = <String>{}, dup = <String>{};
    for (final e in g.lex.entries) {
      if (!seen.add(e.word.of(lang))) dup.add(e.word.of(lang));
    }
    return dup;
  }

  static bool _overlap(List<SceneItem> a, List<SceneItem> b) {
    final ea = a.map((e) => e.value).toSet();
    final eb = b.map((e) => e.value).toSet();
    return ea.intersection(eb).isNotEmpty;
  }

  /// Rejimlar: `read` (gapni o'qi → rasm), `picture` (rasm → gap), `listen` (eshit → rasm), `build` (so'zlardan gap).
  static Exercise sentence(GenContext g) {
    final lang = langOf(g);
    final types = g.pl('types').isEmpty ? ['this'] : g.pl('types');
    final mode = g.pick(g.pl('modes').isEmpty ? ['read'] : g.pl('modes'));
    final s = makeSentence(g, lang, types);
    final text = '${s.words.join(' ')}.';
    if (mode == 'build') {
      return g.custom(
        say: g.sayIn(lang, 'lg_build_sentence'),
        kind: ExerciseKind.assemble,
        visual: SceneVisual(s.scene, aspect: 1.6),
        concept: 'sentence:$lang:${s.type}',
        assemble: AssembleTask(answer: s.words, tiles: g.mixTiles(s.words, s.words), separator: ' '),
        meta: {'answer': text},
        explanation: text,
      );
    }
    // Chalg'ituvchilar: xuddi shu turdagi boshqa gaplar (boshqa narsa, son yoki harakat).
    final wrong = <({List<String> words, List<SceneItem> scene, String type, String key})>[];
    final keys = <String>{s.key};
    var guard = 0;
    final texts = <String>{text};
    while (wrong.length < 2 && guard++ < 80) {
      final o = makeSentence(g, lang, [s.type]);
      if (!keys.add(o.key) || !texts.add('${o.words.join(' ')}.')) continue;
      // Bir xil narsa (lekin boshqa son) — faqat sanash gaplarida farqlanadi.
      if (s.type != 'count' && _overlap(o.scene, s.scene)) continue;
      if (s.type == 'count' && _overlap(o.scene, s.scene) && o.scene.length == s.scene.length) continue;
      wrong.add(o);
    }
    switch (mode) {
      case 'picture':
        return g.choice(
          say: g.sayIn(lang, 'lg_picture_sentence'),
          visual: SceneVisual(s.scene, aspect: 1.6),
          options: [Opt.text(text), for (final o in wrong) Opt.text('${o.words.join(' ')}.')],
          concept: 'sentence:$lang:${s.type}',
          meta: {'answer': s.key},
        );
      case 'listen':
        return g.choice(
          say: listenSay(g, lang, 'lg_listen_sentence', {'w': w(text)}),
          visual: const TextVisual('🔊', scale: 0.8),
          options: [Opt.scene(s.scene, aspect: 1.6), for (final o in wrong) Opt.scene(o.scene, aspect: 1.6)],
          concept: 'sentence:$lang:${s.type}',
          meta: {'answer': s.key},
          explanation: text,
        );
      default:
        return g.choice(
          say: g.sayIn(lang, 'lg_read_sentence'),
          visual: ReadingVisual(text),
          options: [Opt.scene(s.scene, aspect: 1.6), for (final o in wrong) Opt.scene(o.scene, aspect: 1.6)],
          concept: 'sentence:$lang:${s.type}',
          meta: {'answer': s.key},
        );
    }
  }
}
