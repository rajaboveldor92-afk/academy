import 'dart:math';

import 'package:academy/l10n/tr.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/daily_planner.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/engine/rewards.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/models/app_settings.dart';
import 'package:academy/models/child_profile.dart';
import 'package:academy/models/child_progress.dart';
import 'package:academy/models/subject.dart';
import 'package:flutter_test/flutter_test.dart';

/// ILOVA TILLARI: rus va ingliz tilidagi profil uchun mashqlar.
///
/// * Ko'rsatma uch tilda to'liq, ovozda raqam yo'q (TTS sonni boshqa tilda o'qimasin).
/// * Matematika, mantiq, xotira, diqqat, shaxmat, muloqot, ota-ona bilan — ko'rsatma bolaning tilida.
/// * O'zbek tili va Yozish — o'zbekcha; English, Русский, 3 tilda — o'rganilayotgan tilda.
/// * Maslahat, izoh, variant va faoliyat matnlarida o'zbekcha so'z qolmagan (o‘/g‘ yo'q).
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;

  setUpAll(() async {
    content = await ContentRepository.load();
  });

  const uzbekSubjects = {'uzbek', 'writing'};
  const foreignSubjects = {'english', 'russian', 'trilingual'};
  final uzbekLetters = RegExp('[oOgG]‘');
  final digits = RegExp(r'\d');

  Iterable<String> childTexts(Exercise e) sync* {
    if (e.hint != null) yield e.hint!;
    if (e.explanation != null) yield e.explanation!;
    for (final o in e.options) {
      if (o.text != null) yield o.text!;
    }
    for (final p in e.pairs) {
      if (p.left.text != null) yield p.left.text!;
      if (p.right.text != null) yield p.right.text!;
    }
    final a = e.activity;
    if (a != null) {
      yield a.title;
      yield* a.materials;
      yield* a.steps;
      yield a.benefit;
    }
  }

  for (final lang in const ['ru', 'en']) {
    test('$lang: barcha mavzular — ko‘rsatma va maslahatlar bolaning tilida', () {
      var total = 0;
      // Maktab fanlari mashqlari hozircha o'zbekcha.
      for (final topic in content.allTopics.where((t) => !t.isSchool)) {
        final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
        final age = topic.ageSuffix == '4' ? 4 : 6;
        for (var level = 1; level <= topic.maxLevel; level++) {
          final rng = Random(level * 7919 + topic.id.hashCode + lang.hashCode);
          var playable = 0;
          for (var i = 0; i < 25; i++) {
            final where = '$lang ${topic.id} L$level';
            final Exercise e;
            try {
              e = gen(GenContext(rng: rng, content: content, topic: topic, level: level, age: age, lang: lang));
            } catch (err) {
              fail('$where: generator xatosi: $err');
            }
            if (ExerciseValidator.isPlayable(e)) playable++;
            expect(e.instruction.isComplete, isTrue, reason: '$where: tarjima');
            expect(e.instruction.of(lang).contains('{'), isFalse, reason: '$where: ${e.instruction.of(lang)}');
            expect(e.speech.trim(), isNotEmpty, reason: where);
            expect(digits.hasMatch(e.speech), isFalse, reason: '$where: ovozda raqam: ${e.speech}');
            if (uzbekSubjects.contains(topic.subject)) {
              expect(e.speechLang, 'uz', reason: '$where: o‘zbek tili darsi o‘zbekcha');
            } else if (!foreignSubjects.contains(topic.subject)) {
              if (e.speechParts.isEmpty) expect(e.speechLang, lang, reason: '$where: ${e.speech}');
              for (final text in childTexts(e)) {
                expect(uzbekLetters.hasMatch(text), isFalse, reason: '$where: o‘zbekcha matn: $text');
              }
            }
            total++;
          }
          expect(playable, greaterThan(0), reason: '$lang ${topic.id} L$level: o‘ynab bo‘ladigan mashq yo‘q');
        }
      }
      expect(total, greaterThan(1000));
    });

    test('$lang: har bir mavzu va daraja uchun to‘liq dars tuziladi', () {
      for (final topic in content.allTopics.where((t) => !t.isSchool)) {
        final c = content.curriculum(topic.subject, topic.ageSuffix)!;
        final size = topic.lessonSize ?? c.lessonSize;
        for (var level = 1; level <= topic.maxLevel; level++) {
          final lesson = LessonBuilder.build(
            content: content,
            topic: topic,
            level: level,
            count: size,
            age: topic.ageSuffix == '4' ? 4 : 6,
            rng: Random(level),
            lang: lang,
          );
          expect(lesson.length, size, reason: '$lang ${topic.id} L$level');
        }
      }
    });

    test('$lang: kunlik dars bolaning tilida', () {
      for (final age in const [4, 6]) {
        final plan = DailyPlanner.build(
          content: content,
          age: age,
          progress: ChildProgress.empty('x'),
          isEnabled: (_) => true,
          now: DateTime(2026, 9, 27),
          rng: Random(3),
          lang: lang,
        );
        expect(plan.length, DailyPlanner.sizeFor(age));
        for (final item in plan) {
          final e = item.exercise;
          if (uzbekSubjects.contains(e.subject) || foreignSubjects.contains(e.subject) || e.speechParts.isNotEmpty) continue;
          expect(e.speechLang, lang, reason: '${item.topic.id}: ${e.speech}');
        }
      }
    });
  }

  test('faoliyat va muloqot matnlari uch tilda', () {
    final data = content.activities;
    for (final a in data.activities) {
      for (final lang in const ['en', 'ru']) {
        expect(a.texts.containsKey(lang), isTrue, reason: '${a.id}: $lang');
        final t = a.textIn(lang);
        expect(t.title.trim(), isNotEmpty, reason: a.id);
        expect(t.steps.length, a.textIn('uz').steps.length, reason: '${a.id}: $lang qadamlar');
        expect(t.materials.length, a.textIn('uz').materials.length, reason: '${a.id}: $lang materiallar');
        expect(t.benefit.trim(), isNotEmpty, reason: a.id);
      }
    }
    for (final c in data.choices) {
      for (final lang in const ['en', 'ru']) {
        expect(c.texts.containsKey(lang), isTrue, reason: '${c.id}: $lang');
        expect(c.textIn(lang).others.length, c.otherEmojis.length, reason: '${c.id}: $lang');
      }
    }
    for (final s in data.situations) {
      expect(s.text.isComplete, isTrue, reason: s.id);
      expect(s.text.ru == s.text.uz || s.text.en == s.text.uz, isFalse, reason: '${s.id}: tarjima yo‘q');
    }
    for (final p in data.polite) {
      expect(p.text.en == p.text.uz || p.text.ru == p.text.uz, isFalse, reason: '${p.id}: tarjima yo‘q');
      expect(p.word.isComplete, isTrue, reason: p.id);
    }
    expect(data.politeWords.every((w) => w.isComplete), isTrue);
  });

  test('fanlar, medallar va kolleksiya nomlari uch tilda', () {
    for (final s in Subject.values) {
      for (final lang in const ['uz', 'en', 'ru']) {
        expect(s.titleIn(lang).trim(), isNotEmpty, reason: '${s.id} $lang');
        final (name, speechLang) = s.spokenIn(lang);
        expect(name.trim(), isNotEmpty, reason: '${s.id} $lang');
        expect(Tr.languages.contains(speechLang), isTrue);
      }
    }
    for (final m in Rewards.medals) {
      expect(m.title.isComplete && m.hint.isComplete, isTrue, reason: m.id);
    }
    for (final c in Rewards.collection) {
      expect(c.name.isComplete, isTrue, reason: c.emoji);
    }
  });

  test('profil va sozlamalarda til saqlanadi', () {
    final p = ChildProfile.create(id: 'k', name: 'Kamola', age: 5, avatar: '🦄', language: 'ru');
    expect(ChildProfile.fromMap(p.toMap()).language, 'ru');
    expect(ChildProfile.fromMap({...p.toMap(), 'language': 'de'}).language, 'uz');
    expect(ChildProfile.fromMap({...p.toMap()}..remove('language')).language, 'uz');
    expect(p.copyWith(language: 'en').welcomeTitle, 'Welcome, Kamola!');
    expect(p.welcomeTitle, 'Kamola, добро пожаловать!');
    // Standart o'zbekcha salom bolaning tiliga moslanadi; ota-ona yozgan salom o'zgarmaydi.
    expect(p.copyWith(greeting: ChildProfile.defaultGreetingJunior).welcomeSubtitle, 'Готов играть и учиться?');
    expect(p.copyWith(greeting: 'Salom, qizim!').welcomeSubtitle, 'Salom, qizim!');

    const s = AppSettings(appLanguage: 'en');
    expect(AppSettings.fromMap(s.toMap()).appLanguage, 'en');
    expect(AppSettings.fromMap({...s.toMap(), 'appLanguage': 'xx'}).appLanguage, 'uz');
  });

  test('Tr: uch tilda farqli matnlar va ruscha ko‘plik', () {
    const uz = Tr('uz'), en = Tr('en'), ru = Tr('ru');
    expect(uz.whoPlays, 'Kim o‘ynaydi?');
    expect(en.whoPlays, 'Who is playing?');
    expect(ru.whoPlays, 'Кто играет?');
    expect(ru.years(1), '1 год');
    expect(ru.years(4), '4 года');
    expect(ru.years(6), '6 лет');
    expect(en.years(6), '6 years old');
    expect(uz.years(6), '6 yosh');
    expect(ru.levelUp, isNot(uz.levelUp));
  });
}
