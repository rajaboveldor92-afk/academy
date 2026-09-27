import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:academy/database/seed_data.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/services/mother_voice.dart';
import 'package:flutter_test/flutter_test.dart';

/// Onaning ovozi: har bir yozilgan ibora ilovada bor va to'g'ri joyda aytiladi.
void main() {
  late ContentRepository content;

  setUpAll(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    content = await ContentRepository.load();
  });

  List<String> keys(List<dynamic> parts) => [for (final p in parts) '${p.clip ?? '${p.lang}:${p.text}'}'];

  test('har bir ibora uchun fayl bor va ortiqcha fayl yo‘q', () {
    final dir = Directory('assets/audio/uz/ona');
    final files = {for (final f in dir.listSync().whereType<File>()) f.uri.pathSegments.last.replaceAll('.ogg', '')};
    expect(files, MotherVoice.clips.keys.toSet());
    for (final k in [...MotherVoice.praise, ...MotherVoice.encourage, ...MotherVoice.numbers]) {
      expect(MotherVoice.clips.containsKey(k), isTrue, reason: k);
    }
  });

  test('yozuvning barcha iboralari ro‘yxatda (faqat bo‘lim sarlavhasi aytilmaydi)', () {
    final catalog = jsonDecode(File('tool/audio/mother_voice_clips.json').readAsStringSync()) as Map<String, dynamic>;
    final clips = (catalog['clips'] as List).cast<List<dynamic>>();
    final recorded = {for (final c in clips) c[0] as String: c[3] as String};
    expect(recorded.keys.toSet().difference(MotherVoice.clips.keys.toSet()), {'ragbat_va_yakun'});
    for (final e in MotherVoice.clips.entries) {
      expect(recorded[e.key], e.value, reason: e.key);
    }
    // Vaqt oraliqlari ketma-ket va ustma-ust tushmaydi.
    for (var i = 1; i < clips.length; i++) {
      expect((clips[i][1] as num) >= (clips[i - 1][2] as num), isTrue, reason: '${clips[i][0]}');
    }
  });

  test('salom: birinchi kirishda to‘liq, keyin qisqa; o‘z salomi yoki boshqa ism bo‘lsa — yo‘q', () {
    final a = SeedData.azamjon(DateTime(2026));
    final m = SeedData.muhammadjon(DateTime(2026));
    expect(keys(MotherVoice.greeting(a, first: true)!), ['salom_azamjon', 'oynaymiz_organamiz', 'qaysi_oyinni_tanlaymiz']);
    expect(keys(MotherVoice.greeting(m, first: false)!), ['salom', 'muhammadjon', 'keling_birga_oynaymiz']);
    expect(MotherVoice.greeting(a.copyWith(greeting: 'Bugun ham zo‘r kun!'), first: true), isNull);
    expect(MotherVoice.greeting(a.copyWith(name: 'Azam'), first: true), isNull);
    expect(MotherVoice.nameClip(m), 'muhammadjon');
    expect(MotherVoice.subjectClip('logic'), 'mantiq');
    expect(MotherVoice.subjectClip('math'), isNull);
  });

  Exercise first(String topicId, bool Function(Exercise e) test, {int level = 1, int age = 4, int tries = 400}) {
    final topic = content.topic(topicId)!;
    for (var seed = 0; seed < tries; seed++) {
      final list = LessonBuilder.build(content: content, topic: topic, level: level, count: 1, age: age, rng: Random(seed));
      if (list.isNotEmpty && test(list.first)) return list.first;
    }
    fail('$topicId: mos mashq topilmadi');
  }

  test('ko‘rsatmalar mazmuni mos yozuv bilan aytiladi', () {
    final more = first('math4.more_less', (e) => e.instructionKey == 'where_more', level: 2);
    expect(MotherVoice.instructionClip(more), 'qaysi_biri_kop');
    final less = first('math4.more_less', (e) => e.instructionKey == 'where_less', level: 2);
    expect(MotherVoice.instructionClip(less), 'qaysi_biri_kam');
    final bigShape = first('math4.big_small', (e) => e.instructionKey == 'find_big_shape');
    expect(MotherVoice.instructionClip(bigShape), 'eng_katta_shakl');
    final smallShape = first('math4.big_small', (e) => e.instructionKey == 'find_small_shape', level: 2);
    expect(MotherVoice.instructionClip(smallShape), 'eng_kichik_shakl');
    final oddShape = first('logic4.odd', (e) => e.instructionKey == 'odd_shape');
    expect(MotherVoice.instructionClip(oddShape), 'qaysi_shakl_farq_qiladi');
    final shadow = first('logic4.shadow', (e) => e.instructionKey == 'find_shadow');
    expect(MotherVoice.instructionClip(shadow), 'mos_soyasini_top');
    final smaller = first('math6.hundred', (e) => e.instructionKey == 'which_smaller', level: 3, age: 6);
    expect(MotherVoice.instructionClip(smaller), 'qaysi_son_kichik');
    expect(smaller.meta['answer'], min(smaller.meta['a'] as int, smaller.meta['b'] as int));
    final bigger = first('math6.hundred', (e) => e.instructionKey == 'which_bigger', level: 3, age: 6);
    expect(MotherVoice.instructionClip(bigger), 'qaysi_son_katta');
    // Mos yozuv bo'lmasa — mashqning o'z nutqi.
    final count = first('math4.count_1_3', (e) => e.instruction.uz != 'Nechta olma bor?');
    expect(MotherVoice.instructionClip(count), isNull);
    expect(keys(MotherVoice.instruction(count)), ['uz:${count.speech}']);
  });

  test('generatsiya qilingan barcha mashqlarda tanlangan ibora mavjud', () {
    for (final topic in content.allTopics) {
      for (var level = 1; level <= topic.maxLevel; level++) {
        final list = LessonBuilder.build(
          content: content, topic: topic, level: level, count: 6, age: topic.ageSuffix == '4' ? 4 : 6, rng: Random(level),
        );
        for (final e in list) {
          final clip = MotherVoice.instructionClip(e);
          if (clip != null) expect(MotherVoice.clips.containsKey(clip), isTrue, reason: '${topic.id}: $clip');
          for (final p in [...MotherVoice.afterMistake(e, 1, level), ...MotherVoice.afterMistake(e, 2, level)]) {
            if (p.clip != null) expect(MotherVoice.clips.containsKey(p.clip), isTrue, reason: '${topic.id}: ${p.clip}');
          }
        }
      }
    }
  });

  test('xatodan keyin: sanashda "Sanab ko‘r", qo‘shishda "Qo‘shib hisobla", tinglashda qayta eshittirish', () {
    final count = first('math4.count_1_3', (e) => e.instructionKey == 'count_how_many');
    expect(keys(MotherVoice.afterMistake(count, 1, 0)), ['sanab_kor']);
    expect(keys(MotherVoice.afterMistake(count, 2, 0)), ['mos_raqamni_tanla']);
    final add = first('math4.add_5', (e) => e.meta['op'] == '+');
    expect(keys(MotherVoice.afterMistake(add, 1, 0)), ['yana_urinib_kor']);
    expect(keys(MotherVoice.afterMistake(add, 1, 1)), ['shoshilma']);
    expect(keys(MotherVoice.afterMistake(add, 2, 0)), ['qoshib_hisobla']);
    final listen = first('english4.animals', (e) => true);
    final replay = keys(MotherVoice.afterMistake(listen, 2, 0));
    expect(replay.first, 'yana_eshit');
    expect(replay.last, 'en:${listen.speech}');
    expect(MotherVoice.isListening(listen), isTrue);
    expect(MotherVoice.isListening(count), isFalse);
  });

  test('birga sanash: 1–5 gacha, kattaroq sonda sanalmaydi', () {
    final three = first('math4.count_1_5', (e) => e.instructionKey == 'count_how_many' && e.meta['answer'] == 3);
    expect(keys(MotherVoice.countAloud(three)), ['bir', 'ikki', 'uch']);
    final big = first('math4.count_1_10', (e) => e.instructionKey == 'count_how_many' && (e.meta['answer'] as int) > 5);
    expect(MotherVoice.countAloud(big), isEmpty);
    final notCount = first('math4.more_less', (e) => true);
    expect(MotherVoice.countAloud(notCount), isEmpty);
  });

  test('"Ikki olmaga yana bitta olma qo‘shsak" — aynan shu misolda', () {
    final e = first('math4.add_5', (e) => e.meta['a'] == 2 && e.meta['b'] == 1 && e.meta['item'] == 'apple', tries: 20000);
    expect(MotherVoice.instructionClip(e), 'ikki_olmaga_bitta_olma');
  });
}
