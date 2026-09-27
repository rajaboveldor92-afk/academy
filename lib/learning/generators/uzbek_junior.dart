import 'package:flutter/painting.dart';

import '../content/lexicon.dart';
import '../content/uzbek_data.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';
import 'math_junior.dart';

/// O'zbek tili — Muhammadjon (4 yosh): eshitish, so'z boyligi, tovush, harfni tanish.
/// Har bir so'z: RASM + AUDIO + SO'Z. Bola o'qishi shart emas — hammasi ovozda aytiladi.
class UzbekJunior {
  UzbekJunior._();

  static final Map<String, ExerciseGenerator> generators = {
    'word_listen': wordListen,
    'colors': MathJunior.colors,
    'number_words': MathJunior.countObjects,
    'first_sound': firstSound,
    'letter_find': letterFind,
    'letter_picture': letterPicture,
  };

  /// Mavzu → lug'at kategoriyalari.
  static const Map<String, List<String>> themeCategories = {
    'family': ['family'],
    'home': ['home'],
    'kindergarten': ['school', 'toy'],
    'animals': ['animal', 'insect'],
    'birds': ['bird'],
    'fruits': ['fruit'],
    'vegetables': ['vegetable'],
    'body': ['body'],
    'clothes': ['clothes'],
    'transport': ['vehicle'],
    'toys': ['toy'],
    'nature': ['nature'],
    'professions': ['profession'],
    'food': ['food'],
    'places': ['place'],
  };

  /// "Qaysi biri {x} emas?" uchun mavzu nomi (birlik).
  static const Map<String, Localized> themeNoun = {
    'family': Localized(uz: 'oila a’zosi', en: 'a family member', ru: 'член семьи'),
    'home': Localized(uz: 'uy buyumi', en: 'a thing at home', ru: 'предмет дома'),
    'kindergarten': Localized(uz: 'bog‘cha buyumi', en: 'a kindergarten thing', ru: 'предмет из садика'),
    'animals': Localized(uz: 'hayvon', en: 'an animal', ru: 'животное'),
    'birds': Localized(uz: 'qush', en: 'a bird', ru: 'птица'),
    'fruits': Localized(uz: 'meva', en: 'a fruit', ru: 'фрукт'),
    'vegetables': Localized(uz: 'sabzavot', en: 'a vegetable', ru: 'овощ'),
    'body': Localized(uz: 'tana a’zosi', en: 'a body part', ru: 'часть тела'),
    'clothes': Localized(uz: 'kiyim', en: 'clothing', ru: 'одежда'),
    'transport': Localized(uz: 'transport', en: 'transport', ru: 'транспорт'),
    'toys': Localized(uz: 'o‘yinchoq', en: 'a toy', ru: 'игрушка'),
    'nature': Localized(uz: 'tabiat', en: 'nature', ru: 'природа'),
    'professions': Localized(uz: 'kasb egasi', en: 'a job', ru: 'профессия'),
    'food': Localized(uz: 'taom', en: 'food', ru: 'еда'),
    'places': Localized(uz: 'joy', en: 'a place', ru: 'место'),
  };

  static List<LexiconEntry> themeEntries(GenContext g, String theme) {
    final cats = themeCategories[theme] ?? const [];
    return [
      for (final c in cats) ...g.category(c),
    ].where((e) => !e.uz.contains(' ') || theme == 'professions').toList();
  }

  static List<LexiconEntry> otherThemeEntries(GenContext g, String theme) {
    final cats = themeCategories[theme] ?? const [];
    return g.lex.entries
        .where((e) => e.ageMin <= g.age && !cats.contains(e.category) && themeCategories.values.any((l) => l.contains(e.category)))
        .toList();
  }

  // ------------------------------------------------------------ Mavzuli so'zlar
  /// Rejimlar: `listen` (so'zni eshitib rasmni top), `odd` (mavzuga kirmaydiganini top).
  static Exercise wordListen(GenContext g) {
    final theme = g.ps('theme', 'fruits');
    final mode = g.pick(g.pl('modes').isEmpty ? ['listen'] : g.pl('modes'));
    final optCount = g.p('options', 3);
    final pool = themeEntries(g, theme);
    final others = otherThemeEntries(g, theme);
    if (mode == 'odd') {
      final main = g.sample(pool, optCount - 1);
      final odd = g.pick(others);
      return g.choice(
        say: g.say('uz_not_in_theme', {'theme': themeNoun[theme]!}),
        options: [Opt.emoji(odd.emoji), for (final m in main) Opt.emoji(m.emoji)],
        concept: 'word:${odd.id}',
        meta: {'answer': odd.id, 'theme': theme},
        explanation: g.tr('${odd.uz} — ${themeNoun[theme]!.uz} emas.', '${odd.uz} is not ${themeNoun[theme]!.en}.', '${odd.uz} — это не ${themeNoun[theme]!.ru}.'),
      );
    }
    final target = g.pick(pool);
    final distractors = g.pb('sameTheme')
        ? g.sample(pool.where((e) => e.id != target.id).toList(), optCount - 1)
        : g.sample(others, optCount - 1);
    return g.choice(
      say: g.say('uz_find_word', {'item': target}),
      options: [Opt.emoji(target.emoji), for (final d in distractors) Opt.emoji(d.emoji)],
      concept: 'word:${target.id}',
      drag: g.pb('drag'),
      meta: {'answer': target.id, 'theme': theme},
      explanation: target.uz,
    );
  }

  // ------------------------------------------------------------ Birinchi tovush
  /// "Qaysi rasm «M» tovushi bilan boshlanadi?" — `position: last` bo'lsa oxirgi tovush.
  static Exercise firstSound(GenContext g) {
    final optCount = g.p('options', 3);
    final last = g.ps('position', 'first') == 'last';
    final allowed = g.pl('letters');
    final words = g.uz.picturable(g.age).where((w) => w.letters.length >= 2).toList();
    String key(UzWord w) => last ? w.letters.last : w.letters.first;
    final byLetter = <String, List<UzWord>>{};
    for (final w in words) {
      byLetter.putIfAbsent(key(w), () => []).add(w);
    }
    final letters = byLetter.keys.where((l) => (allowed.isEmpty || allowed.contains(l)) && byLetter[l]!.isNotEmpty).toList();
    final letter = g.pick(letters);
    final target = g.pick(byLetter[letter]!);
    // Chalg'ituvchilar: boshqa harf bilan boshlanadigan (tugaydigan) so'zlar; "o"/"o‘" kabi o'xshashlar ham.
    final wrongPool = words.where((w) => key(w) != letter).toList();
    final wrong = g.sample(wrongPool, optCount - 1);
    final shown = UzbekData.capital(letter);
    return g.choice(
      say: g.say(last ? 'uz_last_sound' : 'uz_first_sound', {'l': shown}),
      visual: TextVisual(last ? '…$letter' : '$shown…', scale: 1.1),
      options: [
        Opt.emoji(g.lex.byId(target.lexId!).emoji),
        for (final w in wrong) Opt.emoji(g.lex.byId(w.lexId!).emoji),
      ],
      concept: 'sound:$letter',
      meta: {'answer': target.word, 'letter': letter, 'position': last ? 'last' : 'first'},
      explanation: last
          ? g.tr('${target.word} — oxiri «$letter»', '${target.word} ends with «$letter»', '${target.word} — заканчивается на «$letter»')
          : g.tr('${target.word} — «$shown» bilan boshlanadi', '${target.word} starts with «$shown»', '${target.word} — начинается с «$shown»'),
    );
  }

  // ------------------------------------------------------------ Harfni tanish
  /// Rejimlar: `upper` (bosh harflar), `lower`, `mixed` (bosh harf aytiladi, kichigini top).
  static Exercise letterFind(GenContext g) {
    final letterSet = g.ps('set', 'vowels');
    final optCount = g.p('options', 3);
    final mode = g.pick(g.pl('modes').isEmpty ? ['upper'] : g.pl('modes'));
    final alphabet = g.uz.alphabet;
    const digraphs = {'o‘', 'g‘', 'sh', 'ch', 'ng'};
    // O'xshash harflar — chalg'ituvchi sifatida (o / o‘, s / sh ...).
    const similar = {
      'o‘': ['o', 'u'], 'g‘': ['g', 'q'], 'sh': ['s', 'ch'], 'ch': ['sh', 'j'], 'ng': ['n', 'g'],
      'o': ['o‘', 'u'], 'u': ['o', 'o‘'], 'e': ['i', 'a'], 'b': ['d', 'p'], 'd': ['b', 'p'],
      'p': ['b', 'd'], 'q': ['k', 'g‘'], 'k': ['q', 'x'], 'x': ['h', 'k'], 'h': ['x', 'n'],
    };
    final pool = switch (letterSet) {
      'vowels' => alphabet.where((l) => l.vowel).toList(),
      'consonants' => alphabet.where((l) => !l.vowel && !digraphs.contains(l.lower)).toList(),
      'digraphs' => alphabet.where((l) => digraphs.contains(l.lower)).toList(),
      _ => alphabet,
    };
    final target = g.pick(pool);
    final wrong = <UzLetter>[];
    if (g.pb('similar')) {
      for (final s in similar[target.lower] ?? const <String>[]) {
        if (wrong.length < optCount - 1) wrong.add(g.uz.letter(s));
      }
    }
    for (final l in g.sample(alphabet, alphabet.length)) {
      if (wrong.length >= optCount - 1) break;
      if (l.lower != target.lower && !wrong.contains(l)) wrong.add(l);
    }
    String shownOf(UzLetter l) => mode == 'upper' ? l.upper : l.lower;
    return g.choice(
      say: g.say(mode == 'mixed' ? 'uz_find_small_letter' : 'uz_find_letter', {'l': target.upper}),
      visual: mode == 'mixed' ? TextVisual(target.upper, scale: 1.4) : null,
      options: [Opt.text(shownOf(target)), for (final w in wrong) Opt.text(shownOf(w))],
      concept: 'letter:${target.lower}',
      meta: {'answer': target.lower},
      explanation: '${target.upper} ${target.lower} — ${target.word}',
    );
  }

  // ------------------------------------------------------------ Harf va rasm
  static Exercise letterPicture(GenContext g) {
    final count = g.p('pairs', 2);
    final letterSet = g.ps('set', 'all');
    final allowed = g.pl('letters');
    // "Ng" so'z boshida kelmaydi — rasm bilan juftlashda ishlatilmaydi.
    final pool = g.uz.alphabet
        .where((l) => l.lower != 'ng')
        .where((l) => allowed.isNotEmpty ? allowed.contains(l.lower) : (letterSet != 'vowels' || l.vowel))
        .toList();
    final chosen = g.sample(pool, count);
    return g.custom(
      say: g.say('uz_match_letter_picture'),
      kind: ExerciseKind.match,
      concept: 'letters:${chosen.map((l) => l.lower).join(",")}',
      pairs: [
        for (final l in chosen)
          MatchPair(
            ExerciseOption(text: l.upper, speech: l.upper),
            Opt.emoji(g.lex.byId(l.lexId).emoji),
          ),
      ],
      meta: {'pairs': chosen.map((l) => '${l.upper}=${l.word}').join(',')},
    );
  }

  /// Kichik test yordamchisi: rangli so'z uchun.
  static Color colorOf(GenContext g, String id) => g.lex.color(id).color;
}
