import 'package:flutter/painting.dart';

import '../content/lexicon.dart';
import '../content/uzbek_data.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';
import 'uzbek_junior.dart';

/// O'zbek tili — Azamjon (6 yosh): harf → tovush → bo'g'in → so'z → gap → matn.
/// Savod o'rgatishda lug'at bilan ishlash tamoyili: har bir yangi so'z rasm va
/// kontekst bilan beriladi, keyin o'qish va yozishda takrorlanadi.
class UzbekSenior {
  UzbekSenior._();

  static final Map<String, ExerciseGenerator> generators = {
    'letter_find': UzbekJunior.letterFind,
    'first_sound': UzbekJunior.firstSound,
    'case_match': caseMatch,
    'syllables': syllables,
    'word_read': wordRead,
    'picture_word': pictureWord,
    'fill_letter': fillLetter,
    'build_sentence': buildSentence,
    'read_sentence': readSentence,
    'missing_word': missingWord,
    'story': story,
    'picture_sentence': pictureSentence,
  };

  static List<UzWord> _picWords(GenContext g, {int minLetters = 1, int maxLetters = 20, int minSyl = 1, int maxSyl = 9}) {
    return g.uz.picturable(g.age).where((w) {
      final n = w.letters.length;
      final s = w.syllables.length;
      return n >= minLetters && n <= maxLetters && s >= minSyl && s <= maxSyl;
    }).toList();
  }

  static String _emoji(GenContext g, UzWord w) => g.lex.byId(w.lexId!).emoji;

  static String _cap(String s) => s.isEmpty ? s : s[0].toUpperCase() + s.substring(1);

  // ------------------------------------------------------------ U3 Bosh va kichik harf
  static Exercise caseMatch(GenContext g) {
    final count = g.p('pairs', 3);
    final letterSet = g.ps('set', 'all');
    final pool = g.uz.alphabet.where((l) => switch (letterSet) {
          'vowels' => l.vowel,
          'single' => l.lower.length == 1 || l.lower == 'o‘' || l.lower == 'g‘',
          _ => true,
        }).toList();
    final chosen = g.sample(pool, count);
    return g.custom(
      say: g.say('uz_match_case'),
      kind: ExerciseKind.match,
      concept: 'case:${chosen.map((l) => l.lower).join(",")}',
      pairs: [for (final l in chosen) MatchPair(Opt.text(l.upper), Opt.text(l.lower))],
      meta: {'pairs': chosen.map((l) => '${l.upper}=${l.lower}').join(',')},
    );
  }

  // ------------------------------------------------------------ U4 Bo'g'in
  /// Rejimlar: `count` (nechta bo'g'in), `missing` (tushib qolgan bo'g'in), `build` (bo'g'inlardan yig'ish).
  static Exercise syllables(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['count'] : g.pl('modes'));
    final minSyl = g.p('minSyl', 1), maxSyl = g.p('maxSyl', 3);
    final words = _picWords(g, minSyl: mode == 'count' ? minSyl : 2, maxSyl: maxSyl);
    final w = g.pick(words);
    final pic = SceneVisual([Layouts.emoji(_emoji(g, w), size: 0.8)], aspect: 1.6);
    switch (mode) {
      case 'missing':
        final idx = g.rng.nextInt(w.syllables.length);
        final shown = [for (var i = 0; i < w.syllables.length; i++) i == idx ? '?' : w.syllables[i]].join(' - ');
        final correct = w.syllables[idx];
        final others = <String>{};
        for (final o in g.sample(words, words.length)) {
          for (final s in o.syllables) {
            if (s != correct && others.length < 2 && !_formsWord(g, w, idx, s)) others.add(s);
          }
          if (others.length >= 2) break;
        }
        return g.choice(
          say: g.say('uz_missing_syllable'),
          visual: ReadingVisual(shown, emoji: _emoji(g, w), big: true),
          options: [Opt.text(correct), for (final o in others) Opt.text(o)],
          concept: 'syllable:${w.word}',
          meta: {'answer': correct, 'word': w.word},
          explanation: w.syllables.join(' - '),
        );
      case 'build':
        final tiles = [...w.syllables];
        final extra = g.p('extra', 0);
        if (extra > 0) {
          final pool = [for (final o in words) ...o.syllables].where((s) => !w.syllables.contains(s)).toList();
          tiles.addAll(g.sample(pool, extra));
        }
        return g.custom(
          say: g.say('uz_build_syllables'),
          kind: ExerciseKind.assemble,
          visual: pic,
          concept: 'syllable:${w.word}',
          assemble: AssembleTask(answer: w.syllables, tiles: g.mixTiles(tiles, w.syllables)),
          meta: {'answer': w.word},
          explanation: '${w.syllables.join(' - ')} → ${w.word}',
        );
      default:
        final n = w.syllables.length;
        final opts = <int>{n, if (n > 1) n - 1, n + 1, n + 2}.take(3).toList();
        return g.choice(
          say: g.say('uz_count_syllables'),
          visual: ReadingVisual(w.word, emoji: _emoji(g, w), big: true),
          options: [for (final v in opts) Opt.number(v)],
          concept: 'syllable_count:$n',
          meta: {'answer': n, 'word': w.word},
          hint: 'Qarsak chalib ayt: har bir qarsak — bitta bo‘g‘in.',
          explanation: '${w.syllables.join(' - ')} — $n ta bo‘g‘in',
        );
    }
  }

  /// Bo'g'inni almashtirganda boshqa haqiqiy so'z chiqib qolmasin (ikkita to'g'ri javob bo'lmasligi uchun).
  static bool _formsWord(GenContext g, UzWord w, int idx, String replacement) {
    final candidate = [for (var i = 0; i < w.syllables.length; i++) i == idx ? replacement : w.syllables[i]].join();
    return g.uz.words.any((x) => x.word == candidate);
  }

  // ------------------------------------------------------------ U5–U6 So'z o'qish / yig'ish
  static Exercise wordRead(GenContext g) {
    final minL = g.p('minLetters', 2), maxL = g.p('maxLetters', 3);
    final mode = g.pick(g.pl('modes').isEmpty ? ['read'] : g.pl('modes'));
    final words = _picWords(g, minLetters: minL, maxLetters: maxL);
    final w = g.pick(words);
    if (mode == 'build') {
      final letters = w.letters;
      final tiles = [...letters];
      final extra = g.p('extra', 0);
      if (extra > 0) {
        final pool = g.uz.alphabet.map((l) => l.lower).where((l) => !letters.contains(l)).toList();
        tiles.addAll(g.sample(pool, extra));
      }
      return g.custom(
        say: g.say('uz_build_word'),
        kind: ExerciseKind.assemble,
        visual: SceneVisual([Layouts.emoji(_emoji(g, w), size: 0.8)], aspect: 1.6),
        concept: 'spell:${w.word}',
        assemble: AssembleTask(answer: letters, tiles: g.mixTiles(tiles, letters)),
        meta: {'answer': w.word},
        explanation: w.word,
      );
    }
    final others = g.sample(_picWords(g).where((x) => x.lexId != w.lexId).toList(), g.p('options', 3) - 1);
    return g.choice(
      say: g.say('uz_read_word'),
      visual: ReadingVisual(w.word, big: true),
      options: [Opt.emoji(_emoji(g, w)), for (final o in others) Opt.emoji(_emoji(g, o))],
      concept: 'read:${w.word}',
      meta: {'answer': w.word},
    );
  }

  // ------------------------------------------------------------ U7 Rasmga mos so'z
  static Exercise pictureWord(GenContext g) {
    final similarity = g.ps('similar', 'none');
    final words = _picWords(g, minLetters: 2, maxLetters: g.p('maxLetters', 6));
    final w = g.pick(words);
    List<UzWord> pool;
    switch (similarity) {
      case 'first':
        pool = words.where((x) => x.word != w.word && x.letters.first == w.letters.first).toList();
      case 'theme':
        pool = words.where((x) => x.word != w.word && x.theme == w.theme).toList();
      default:
        pool = words.where((x) => x.word != w.word).toList();
    }
    if (pool.length < 2) pool = words.where((x) => x.word != w.word).toList();
    final others = g.sample(pool, g.p('options', 3) - 1);
    return g.choice(
      say: g.say('uz_picture_word'),
      visual: SceneVisual([Layouts.emoji(_emoji(g, w), size: 0.8)], aspect: 1.6),
      options: [Opt.text(w.word), for (final o in others) Opt.text(o.word)],
      concept: 'read:${w.word}',
      meta: {'answer': w.word},
    );
  }

  // ------------------------------------------------------------ U8 So'zni to'ldir
  static Exercise fillLetter(GenContext g) {
    final which = g.ps('which', 'vowel');
    final words = _picWords(g, minLetters: 3, maxLetters: g.p('maxLetters', 5));
    for (var attempt = 0; attempt < 30; attempt++) {
      final w = g.pick(words);
      final letters = w.letters;
      final candidates = [
        for (var i = 0; i < letters.length; i++)
          if (which == 'any' || (which == 'vowel') == UzbekData.isVowel(letters[i])) i,
      ];
      if (candidates.isEmpty) continue;
      final idx = g.pick(candidates);
      final correct = letters[idx];
      final pool = g.uz.alphabet
          .map((l) => l.lower)
          .where((l) => l != correct && (which == 'any' || (which == 'vowel') == UzbekData.isVowel(l)))
          .where((l) {
        final alt = [for (var i = 0; i < letters.length; i++) i == idx ? l : letters[i]].join();
        return !g.uz.words.any((x) => x.word == alt);
      }).toList();
      if (pool.length < 2) continue;
      final wrong = g.sample(pool, g.p('options', 3) - 1);
      final shown = [for (var i = 0; i < letters.length; i++) i == idx ? '_' : letters[i]].join();
      return g.choice(
        say: g.say('uz_fill_letter'),
        visual: ReadingVisual(shown, emoji: _emoji(g, w), big: true),
        options: [Opt.text(correct), for (final l in wrong) Opt.text(l)],
        concept: 'spell:${w.word}',
        meta: {'answer': correct, 'word': w.word},
        explanation: w.word,
      );
    }
    return pictureWord(g);
  }

  // ------------------------------------------------------------ Gaplar
  /// Tasodifiy gap: so'zlar ro'yxati, mos rasm (sahna) va gap turi.
  static ({List<String> words, List<SceneItem> scene, String type, String key}) sentence(GenContext g, List<String> types) {
    final type = g.pick(types);
    switch (type) {
      case 'action':
        final action = g.pick(g.uz.actions);
        final subjects = g.lex.entries
            .where((e) =>
                e.ageMin <= g.age &&
                !e.uz.contains(' ') &&
                action.categories.contains(e.category) &&
                (action.tag.isEmpty || e.has(action.tag)))
            .toList();
        final s = g.pick(subjects);
        final ctx = _actionContext[action.id] ?? '⭐';
        return (
          words: [_cap(s.uz), ...action.text.uz.split(' ')],
          scene: [Layouts.emoji(s.emoji, x: 0.35, size: 0.6), Layouts.emoji(ctx, x: 0.72, size: 0.42)],
          type: type,
          key: '${s.id}:${action.id}',
        );
      case 'color':
        final items = g.lex.entries
            .where((e) => e.ageMin <= g.age && !e.uz.contains(' ') && e.color != null && !g.lex.color(e.color!).name.uz.contains(' ') && const {'fruit', 'vegetable', 'toy', 'clothes', 'vehicle'}.contains(e.category))
            .toList();
        final it = g.pick(items);
        return (
          words: [_cap(it.uz), g.lex.color(it.color!).name.uz],
          scene: [Layouts.emoji(it.emoji, size: 0.75)],
          type: type,
          key: '${it.id}:${it.color}',
        );
      case 'count':
        final name = g.pick(g.uz.names);
        final it = g.pick(g.lex.entries.where((e) => e.ageMin <= g.age && !e.uz.contains(' ') && const {'fruit', 'toy', 'food'}.contains(e.category)).toList());
        final n = g.range(2, 5);
        return (
          words: ['${name}da', '$n', 'ta', it.uz, 'bor'],
          scene: Layouts.group(it.emoji, n, aspect: 1.6),
          type: type,
          key: '${it.id}:$n',
        );
      default:
        final it = g.pick(g.lex.entries.where((e) => e.ageMin <= g.age && !e.uz.contains(' ') && const {'fruit', 'animal', 'toy', 'vehicle', 'bird'}.contains(e.category)).toList());
        return (
          words: ['Bu', it.uz],
          scene: [Layouts.emoji(it.emoji, size: 0.75)],
          type: 'this',
          key: it.id,
        );
    }
  }

  static const Map<String, String> _actionContext = {
    'flies': '☁️',
    'swims': '🌊',
    'runs': '💨',
    'sleeps': '💤',
    'eats': '🍽️',
  };

  // ------------------------------------------------------------ U9 So'zlardan gap tuz
  static Exercise buildSentence(GenContext g) {
    final s = sentence(g, g.pl('types').isEmpty ? ['this', 'color'] : g.pl('types'));
    return g.custom(
      say: g.say('uz_build_sentence'),
      kind: ExerciseKind.assemble,
      visual: SceneVisual(s.scene, aspect: 1.6),
      concept: 'sentence:${s.type}',
      assemble: AssembleTask(answer: s.words, tiles: g.mixTiles(s.words, s.words), separator: ' '),
      meta: {'answer': '${s.words.join(' ')}.'},
      explanation: '${s.words.join(' ')}.',
    );
  }

  // ------------------------------------------------------------ U10 Gapni o'qi
  static Exercise readSentence(GenContext g) {
    final types = g.pl('types').isEmpty ? ['action'] : g.pl('types');
    final s = sentence(g, types);
    final wrong = <List<SceneItem>>[];
    final keys = <String>{s.key};
    var guard = 0;
    while (wrong.length < 2 && guard++ < 50) {
      final o = sentence(g, [s.type]);
      if (keys.add(o.key) && !_sameMeaning(s, o)) wrong.add(o.scene);
    }
    return g.choice(
      say: g.say('uz_read_sentence'),
      visual: ReadingVisual('${s.words.join(' ')}.'),
      options: [Opt.scene(s.scene, aspect: 1.6), for (final w in wrong) Opt.scene(w, aspect: 1.6)],
      concept: 'sentence:${s.type}',
      meta: {'answer': s.key},
    );
  }

  /// Ikki gap bitta rasmga mos kelib qolmasin (masalan, bir xil narsa, bir xil rang).
  static bool _sameMeaning(({List<String> words, List<SceneItem> scene, String type, String key}) a,
      ({List<String> words, List<SceneItem> scene, String type, String key}) b) {
    final ea = a.scene.map((e) => e.value).toSet();
    final eb = b.scene.map((e) => e.value).toSet();
    return ea.intersection(eb).isNotEmpty && a.type != 'count';
  }

  // ------------------------------------------------------------ U11 Yetishmayotgan so'z
  static Exercise missingWord(GenContext g) {
    final ctx = g.pick(_contexts);
    final right = g.lex.entries.where((e) => e.ageMin <= g.age && !e.uz.contains(' ') && ctx.fits(e)).toList();
    final wrongPool = g.lex.entries.where((e) => e.ageMin <= g.age && !e.uz.contains(' ') && ctx.wrong(e)).toList();
    final answer = g.pick(right);
    final wrong = g.sample(wrongPool, g.p('options', 3) - 1);
    final name = g.pick(g.uz.names);
    final text = ctx.template.replaceAll('{name}', name).replaceAll('{x}', '___');
    return g.choice(
      say: g.say('uz_missing_word'),
      visual: ReadingVisual(text),
      options: [Opt.text(answer.uz), for (final w in wrong) Opt.text(w.uz)],
      concept: 'context:${ctx.id}',
      meta: {'answer': answer.uz},
      explanation: ctx.template.replaceAll('{name}', name).replaceAll('{x}', answer.uz),
    );
  }

  static final List<_Context> _contexts = [
    _Context('sky', 'Osmonda {x} uchyapti.', (e) => e.has('flies') && e.category != 'toy' && e.id != 'ladybug',
        (e) => !e.has('flies') && const {'fruit', 'vegetable', 'food', 'clothes', 'home'}.contains(e.category)),
    _Context('sea', 'Dengizda {x} suzyapti.',
        (e) => e.category == 'sea' || const {'boat', 'ship', 'speedboat', 'penguin', 'turtle'}.contains(e.id),
        (e) => !e.has('swims') && const {'fruit', 'clothes', 'home', 'school'}.contains(e.category)),
    _Context('basket', 'Savatda bitta {x} bor.', (e) => const {'fruit', 'vegetable'}.contains(e.category),
        (e) => const {'vehicle', 'profession', 'place'}.contains(e.category)),
    _Context('wear', '{name} yangi {x} kiydi.',
        (e) => e.category == 'clothes' && !e.has('pair') && !const {'glasses', 'sunglasses', 'ring', 'purse', 'handbag', 'ribbon'}.contains(e.id),
        (e) => const {'fruit', 'vehicle', 'animal', 'food'}.contains(e.category)),
    _Context('eat', '{name} mazali {x} yedi.',
        (e) => const {'fruit', 'food'}.contains(e.category) && !e.has('drink') && !const {'salt', 'bone', 'lemon', 'coconut', 'rice', 'soup'}.contains(e.id),
        (e) => const {'clothes', 'vehicle', 'school', 'home'}.contains(e.category)),
    _Context('play', '{name} {x} bilan o‘ynadi.',
        (e) => e.category == 'toy' && !const {'trophy', 'medal', 'gift', 'circus', 'ferris_wheel', 'carousel', 'soccer_goal'}.contains(e.id),
        (e) => const {'food', 'fruit', 'vegetable', 'nature'}.contains(e.category)),
    _Context('night', 'Tunda osmonda {x} ko‘rinadi.', (e) => e.id == 'moon' || e.id == 'star',
        (e) => const {'fruit', 'clothes', 'vehicle', 'animal'}.contains(e.category)),
    // O'zbek bog'ida o'sadigan mevalar va gullar (tropik mevalarsiz).
    _Context('garden', 'Bog‘da {x} o‘sadi.',
        (e) => const {'apple', 'cherry', 'peach', 'pear', 'grapes', 'strawberry', 'melon', 'watermelon', 'flower', 'tulip', 'rose', 'sunflower', 'tree', 'seedling', 'blossom'}.contains(e.id),
        (e) => const {'vehicle', 'clothes', 'school', 'home'}.contains(e.category)),
  ];

  // ------------------------------------------------------------ U12–U13 Hikoya
  /// Rejimlar: `picture` (hikoyaga mos rasm), `question` (matn bo'yicha savol).
  static Exercise story(GenContext g) {
    final mode = g.pick(g.pl('modes').isEmpty ? ['picture'] : g.pl('modes'));
    final long = g.pb('long');
    final name = g.pick(g.uz.names);
    final place = g.pick(g.uz.places);
    final items = g.lex.entries
        .where((e) => e.ageMin <= g.age && !e.uz.contains(' ') && e.color != null && !g.lex.color(e.color!).name.uz.contains(' ') && const {'fruit', 'toy', 'animal', 'bird'}.contains(e.category))
        .toList();
    final item = g.pick(items);
    final n = g.range(2, 6);
    final color = g.lex.color(item.color!);
    final sentences = [
      '$name ${place.text.uz} bordi.',
      'U yerda $n ta ${item.uz} ko‘rdi.',
      if (long) '${_cap(item.uz)}lar ${color.name.uz} edi.',
    ];
    final text = sentences.join(' ');
    if (mode == 'question') {
      final qTypes = ['where', 'count', 'who', if (long) 'color'];
      final q = g.pick(qTypes);
      switch (q) {
        case 'count':
          return g.choice(
            say: g.say('uz_story_question'),
            visual: ReadingVisual(text, question: '$name nechta ${item.uz} ko‘rdi?'),
            options: [for (final v in g.numberChoices(n, min: 1, max: 9, spread: 2)) Opt.number(v)],
            concept: 'story:count',
            meta: {'answer': n},
          );
        case 'who':
          final others = g.sample(g.uz.names.where((x) => x != name).toList(), 2);
          return g.choice(
            say: g.say('uz_story_question'),
            visual: ReadingVisual(text, question: 'Kim ${place.text.uz} bordi?'),
            options: [Opt.text(name), for (final o in others) Opt.text(o)],
            concept: 'story:who',
            meta: {'answer': name},
          );
        case 'color':
          final others = g.sample(
            g.lex.colors.where((c) => c.id != color.id && !c.name.uz.contains(' ')).toList(),
            2,
          );
          return g.choice(
            say: g.say('uz_story_question'),
            visual: ReadingVisual(text, question: '${_cap(item.uz)}lar qanday rangda edi?'),
            options: [Opt.text(color.name.uz), for (final c in others) Opt.text(c.name.uz)],
            concept: 'story:color',
            meta: {'answer': color.id},
          );
        default:
          final others = g.sample(g.uz.places.where((p) => p.id != place.id).toList(), 2);
          return g.choice(
            say: g.say('uz_story_question'),
            visual: ReadingVisual(text, question: '$name qayerga bordi?'),
            options: [Opt.text(_cap(place.text.uz)), for (final p in others) Opt.text(_cap(p.text.uz))],
            concept: 'story:where',
            meta: {'answer': place.id},
          );
      }
    }
    // Rasm: to'g'ri narsa va son; chalg'ituvchilar — boshqa son yoki boshqa narsa.
    final otherItem = g.pick(items.where((e) => e.id != item.id).toList());
    final otherN = n == 2 ? n + 2 : n - 1;
    return g.choice(
      say: g.say('uz_story_picture'),
      visual: ReadingVisual(text),
      options: [
        Opt.group(item.emoji, n),
        Opt.group(item.emoji, otherN),
        Opt.group(otherItem.emoji, n),
      ],
      concept: 'story:picture',
      meta: {'answer': '${item.id}x$n'},
    );
  }

  // ------------------------------------------------------------ U14 Rasm asosida gap
  static Exercise pictureSentence(GenContext g) {
    final types = g.pl('types').isEmpty ? ['action', 'color'] : g.pl('types');
    final s = sentence(g, types);
    final wrong = <String>[];
    final keys = <String>{s.key};
    var guard = 0;
    while (wrong.length < 2 && guard++ < 60) {
      final o = sentence(g, [s.type]);
      final text = '${o.words.join(' ')}.';
      if (keys.add(o.key) && !_sameMeaning(s, o) && !wrong.contains(text)) wrong.add(text);
    }
    return g.choice(
      say: g.say('uz_picture_sentence'),
      visual: SceneVisual(s.scene, aspect: 1.6),
      options: [Opt.text('${s.words.join(' ')}.'), for (final w in wrong) Opt.text(w)],
      concept: 'sentence:${s.type}',
      meta: {'answer': s.key},
    );
  }

  /// Test yordamchisi.
  static Color colorOf(GenContext g, LexiconEntry e) => g.lex.color(e.color!).color;
}

class _Context {
  _Context(this.id, this.template, this.fits, this.wrong);

  final String id;
  final String template;
  final bool Function(LexiconEntry e) fits;
  final bool Function(LexiconEntry e) wrong;
}
