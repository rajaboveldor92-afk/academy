import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/content/number_words.dart';
import 'package:academy/learning/generators/foreign_language.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/generators/trilingual.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/learning/models/topic.dart';
import 'package:flutter_test/flutter_test.dart';

/// Ingliz, rus va "3 tilda" modullari: ma'lumotlar, grammatika, lug'at hajmi.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  int ageOf(Topic t) => t.ageSuffix == '4' ? 4 : 6;

  GenContext ctx(Topic t, int level, [int seed = 1]) =>
      GenContext(rng: Random(seed), content: content, topic: t, level: level, age: ageOf(t));

  test('alifbolar: 26 inglizcha va 33 ruscha harf, misollar mos', () {
    final en = content.languages.alphabet('en');
    final ru = content.languages.alphabet('ru');
    expect(en.length, 26);
    expect(ru.length, 33);
    expect(en.map((l) => l.upper).join(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ');
    expect(ru.map((l) => l.upper).join(), 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ');
    expect(en.where((l) => l.vowel).map((l) => l.lower).join(), 'aeiou');
    expect(ru.where((l) => l.vowel).map((l) => l.lower).join(), 'аеёиоуыэюя');
    for (final l in en) {
      expect(l.lower, l.upper.toLowerCase());
      expect(content.lexicon.contains(l.lexId!), isTrue, reason: l.upper);
      final word = content.lexicon.byId(l.lexId!).word.en.toLowerCase();
      expect(word.contains(l.lower), isTrue, reason: '${l.upper}: $word');
      if (l.initial) expect(word.startsWith(l.lower), isTrue, reason: '${l.upper}: $word');
    }
    for (final l in ru) {
      if (l.lexId == null) continue;
      final word = content.lexicon.byId(l.lexId!).word.ru;
      expect(word.contains(l.lower), isTrue, reason: '${l.upper}: $word');
      if (l.initial) expect(word.startsWith(l.lower), isTrue, reason: '${l.upper}: $word');
    }
  });

  test('rus tili: so‘z jinsi, rang va sifat shakllari, bo‘g‘inlar', () {
    final data = content.languages;
    for (final e in data.ruGender.entries) {
      final word = content.lexicon.byId(e.key).word.ru;
      final last = word[word.length - 1];
      switch (e.value) {
        case 'f':
          expect('аяь'.contains(last), isTrue, reason: '$word — f');
        case 'n':
          expect('оеёи'.contains(last), isTrue, reason: '$word — n');
        case 'pl':
          expect('ыиа'.contains(last), isTrue, reason: '$word — pl');
        case 'm':
          expect('аоеёиыэюя'.contains(last) && !const {'папа', 'дедушка', 'мишка'}.contains(word), isFalse,
              reason: '$word — m');
        default:
          fail('$word: noma’lum jins ${e.value}');
      }
    }
    // Sifat shakllari: -ый/-ий/-ой, -ая/-яя, -ое/-ее, -ые/-ие.
    void checkForms(Map<String, String> f, String what) {
      expect(RegExp(r'(ый|ий|ой)$').hasMatch(f['m']!), isTrue, reason: '$what m ${f['m']}');
      expect(RegExp(r'(ая|яя)$').hasMatch(f['f']!), isTrue, reason: '$what f ${f['f']}');
      expect(RegExp(r'(ое|ее)$').hasMatch(f['n']!), isTrue, reason: '$what n ${f['n']}');
      expect(RegExp(r'(ые|ие)$').hasMatch(f['pl']!), isTrue, reason: '$what pl ${f['pl']}');
    }

    expect(data.colorForms.keys.toSet(), content.lexicon.colors.map((c) => c.id).toSet());
    data.colorForms.forEach((id, f) {
      checkForms(f, id);
      expect(f['m'], content.lexicon.color(id).name.ru, reason: id);
    });
    for (final a in data.adjectives.where((a) => a.id != 'up' && a.id != 'down')) {
      checkForms(a.ruForms, a.id);
      expect(data.adjectives.any((b) => b.id == a.pair && b.pair == a.id), isTrue, reason: a.id);
    }
    expect(data.ruSyllables.length, greaterThanOrEqualTo(60));
    data.ruSyllables.forEach((id, sy) {
      final word = content.lexicon.byId(id).word.ru;
      expect(sy.join(), word, reason: id);
      for (final s in sy) {
        expect(s.split('').where((ch) => 'аеёиоуыэюя'.contains(ch)).length, 1, reason: '$word: $s');
      }
    });
  });

  test('ingliz tili: ko‘plik shakllari va artikllar', () {
    const irregular = {'mice', 'sheep', 'fish', 'children', 'teeth', 'feet', 'deer', 'geese', 'oxen', 'men', 'women', 'people', 'dice'};
    content.languages.enPlural.forEach((id, p) {
      final word = content.lexicon.byId(id).word.en;
      expect(p.endsWith('s') || irregular.contains(p), isTrue, reason: '$word → $p');
      expect(p.contains(' '), isFalse, reason: word);
    });
    expect(content.languages.enPlural['mouse'], 'mice');
    expect(content.languages.enPlural['strawberry'], 'strawberries');
    expect(content.languages.enPlural['fox'], 'foxes');
    expect(ForeignLanguage.article('apple'), 'an');
    expect(ForeignLanguage.article('umbrella'), 'an');
    expect(ForeignLanguage.article('unicorn'), 'a');
    expect(ForeignLanguage.article('cat'), 'a');
    expect(NumberWords.word(7, 'en'), 'seven');
    expect(NumberWords.word(21, 'en'), 'twenty-one');
    expect(NumberWords.word(14, 'ru'), 'четырнадцать');
    expect(NumberWords.word(20, 'ru'), 'двадцать');
    expect(NumberWords.spellDigits('Find 3', 'en'), 'Find three');
  });

  test('harakatlar, sifatlar, iboralar: uch tilda to‘liq', () {
    final data = content.languages;
    final lexEmoji = content.lexicon.entries.map((e) => e.emoji).toSet();
    final emojis = <String>{};
    for (final a in data.actions) {
      expect(a.word.isComplete && a.now.isComplete, isTrue, reason: a.id);
      expect(a.enIng.contains('ing'), isTrue, reason: a.id);
      expect(emojis.add(a.emoji), isTrue, reason: 'takroriy emoji ${a.id}');
      expect(lexEmoji.contains(a.emoji), isFalse, reason: 'lug‘atdagi emoji ${a.id}');
    }
    expect(data.actions.where((a) => a.ageMin <= 4).length, greaterThanOrEqualTo(10));
    for (final p in data.phrases) {
      expect(p.text.isComplete, isTrue, reason: p.id);
      expect(p.scene, isNotEmpty);
    }
    expect(data.phrases.map((p) => p.scene.join()).toSet().length, data.phrases.length);
    for (final a in data.animalActions) {
      expect(a.en.startsWith('is '), isTrue, reason: a.id);
    }
  });

  /// Dasturdagi mavzular orqali bola o'rganadigan so'zlar (shu tilda).
  Set<String> vocabulary(String subject, String age, String lang) {
    final words = <String>{};
    for (final t in content.curriculum(subject, age)!.topics) {
      for (var level = 1; level <= t.maxLevel; level++) {
        final g = ctx(t, level);
        final p = t.paramsFor(level);
        switch (t.generator) {
          case 'vocab':
            for (final theme in (p['themes'] as List)) {
              for (final it in ForeignLanguage.items(g, '$theme')) {
                words.add(it.word.of(lang).toLowerCase());
              }
            }
          case 'colors':
            for (final id in (p['colors'] as List)) {
              words.add(content.lexicon.color('$id').name.of(lang));
            }
          case 'numbers':
            for (var n = (p['min'] as num).toInt(); n <= (p['max'] as num).toInt(); n++) {
              words.add(NumberWords.word(n, lang));
            }
          case 'opposites':
            for (final a in content.languages.adjectives) {
              words.add(a.word().of(lang));
            }
          case 'alphabet_listen':
            for (final l in content.languages.alphabet(lang)) {
              if (l.initial && l.lexId != null) words.add(content.lexicon.byId(l.lexId!).word.of(lang).toLowerCase());
            }
        }
      }
    }
    return words;
  }

  test('lug‘at hajmi: 4 yosh ≥ 200, 6 yosh ≥ 400 so‘z (ingliz va rus)', () {
    final en4 = vocabulary('english', '4', 'en').length;
    final en6 = vocabulary('english', '6', 'en').length;
    final ru4 = vocabulary('russian', '4', 'ru').length;
    final ru6 = vocabulary('russian', '6', 'ru').length;
    // ignore: avoid_print
    print('Lug‘at: EN 4 yosh $en4, 6 yosh $en6; RU 4 yosh $ru4, 6 yosh $ru6');
    expect(en4, greaterThanOrEqualTo(200));
    expect(ru4, greaterThanOrEqualTo(200));
    expect(en6, greaterThanOrEqualTo(400));
    expect(ru6, greaterThanOrEqualTo(400));
  });

  test('3 tilda: 6 yoshda ≥ 300 tushuncha, har biri uch tilda', () {
    final ids = <String>{};
    for (final t in content.curriculum('trilingual', '6')!.topics) {
      for (var level = 1; level <= t.maxLevel; level++) {
        final themes = (t.paramsFor(level)['themes'] as List).map((e) => '$e').toList();
        for (final it in Trilingual.items(ctx(t, level), themes)) {
          expect(it.word.isComplete, isTrue, reason: it.id);
          ids.add(it.id);
        }
      }
    }
    // ignore: avoid_print
    print('3 tilda: ${ids.length} tushuncha');
    expect(ids.length, greaterThanOrEqualTo(300));
  });

  test('chet tili mashqlari o‘sha tilda aytiladi; o‘zbekcha yordamchi javobni oshkor qilmaydi', () {
    for (final subject in ['english', 'russian']) {
      final lang = subject == 'english' ? 'en' : 'ru';
      for (final age in ['4', '6']) {
        for (final t in content.curriculum(subject, age)!.topics) {
          final gen = GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator)!;
          for (var level = 1; level <= t.maxLevel; level++) {
            for (var i = 0; i < 30; i++) {
              final e = gen(ctx(t, level, i + level * 101));
              final where = '${t.id} L$level';
              expect(e.speechLang, lang, reason: where);
              expect(e.prompt, e.instruction.of(lang), reason: where);
              final word = e.meta['word'];
              if (word is String) {
                final helper = ' ${e.instruction.uz.toLowerCase().replaceAll(RegExp(r'[?.!,:«»]'), ' ')} ';
                expect(helper.contains(' ${word.toLowerCase()} '), isFalse, reason: '$where: "$word" o‘zbekcha matnda');
              }
              if (lang == 'ru') {
                // Ruscha nutqda lotin harflari bo'lmasin (TTS noto'g'ri o'qiydi).
                expect(RegExp('[a-zA-Z]').hasMatch(e.speech), isFalse, reason: '$where: ${e.speech}');
              }
            }
          }
        }
      }
    }
  });

  test('3 tilda: har bir so‘z o‘z tilida aytiladi', () {
    for (final age in ['4', '6']) {
      for (final t in content.curriculum('trilingual', age)!.topics) {
        final gen = GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator)!;
        for (var level = 1; level <= t.maxLevel; level++) {
          for (var i = 0; i < 20; i++) {
            final e = gen(ctx(t, level, i));
            if (t.generator == 'listen' || t.generator == 'what_is') {
              expect(e.speechParts, isNotEmpty, reason: t.id);
              for (final p in e.speechParts) {
                if (p.lang == 'ru') expect(RegExp('[a-zA-Z]').hasMatch(p.text), isFalse, reason: '${t.id}: $p');
                if (p.lang == 'en') expect(RegExp('[а-яА-ЯёЁ]').hasMatch(p.text), isFalse, reason: '${t.id}: $p');
              }
              expect(e.speechParts.last.lang, 'uz', reason: t.id);
            }
          }
        }
      }
    }
  });

  test('ruscha gaplar: sifat ot jinsiga mos (Мяч красный, Машина красная)', () {
    final t = content.topic('russian6.sentences')!;
    final data = content.languages;
    for (var i = 0; i < 200; i++) {
      final g = ctx(t, 3, i);
      final s = ForeignLanguage.makeSentence(g, 'ru', ['color']);
      final noun = s.words[0].toLowerCase();
      final entry = content.lexicon.entries.firstWhere((e) => e.word.ru == noun);
      final gender = data.ruGender[entry.id]!;
      expect(s.words[1], data.colorRu(entry.color!, gender), reason: s.words.join(' '));
    }
    final en = content.topic('english6.sentences')!;
    for (var i = 0; i < 100; i++) {
      final s = ForeignLanguage.makeSentence(ctx(en, 3, i), 'en', ['this']);
      expect(s.words.take(2).join(' '), 'It is');
      expect(s.words[2], ForeignLanguage.article(s.words[3]), reason: s.words.join(' '));
    }
  });

  test('tinglash mashqlarida bir xil variantlar, lekin boshqa so‘z — boshqa savol', () {
    final t = content.topic('english4.animals')!;
    final gen = GeneratorRegistry.find(t.subject, t.ageSuffix, t.generator)!;
    final a = gen(ctx(t, 2, 1));
    expect(a.signature.contains(a.speech), isTrue);
    expect(a.kind, ExerciseKind.choice);
  });
}
