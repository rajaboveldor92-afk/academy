import 'dart:convert';

import 'package:flutter/services.dart';

import '../../core/utils/map_utils.dart';
import '../models/topic.dart';
import 'activity_data.dart';
import 'instructions.dart';
import 'language_data.dart';
import 'lexicon.dart';
import 'uzbek_data.dart';

/// Barcha o'quv kontenti: lug'at, ko'rsatmalar, mantiqiy bog'lanishlar va
/// fanlar bo'yicha dasturlar. Bir marta yuklanadi (lazy) va xotirada turadi.
class ContentRepository {
  ContentRepository({
    required this.lexicon,
    required this.instructions,
    required this.logicData,
    required this.curricula,
    required this.uzbek,
    required this.glyphs,
    required this.languages,
    required this.activities,
    this.banks = const {},
  });

  /// Maktab fanlari savollar banki: mavzu id → savollar (`assets/data/school/bank_*.json`).
  final Map<String, List<Map<String, dynamic>>> banks;

  /// Savollar banki fayllari.
  static const List<String> bankFiles = [];

  /// Dastur fayllari: `<fan>_<4|6>.json`.
  static const List<String> curriculumFiles = [
    'math_3', 'logic_3',
    'math_5', 'logic_5',
    'math_7', 'logic_7',
    'math_8', 'logic_8',
    'math_4',
    'logic_4',
    'math_6',
    'logic_6',
    'uzbek_4',
    'uzbek_6',
    'writing_4',
    'writing_6',
    'english_4',
    'english_6',
    'russian_4',
    'russian_6',
    'trilingual_4',
    'trilingual_6',
    'chess_4',
    'chess_6',
    'memory_4',
    'memory_6',
    'attention_4',
    'attention_6',
    'puzzle_4',
    'puzzle_6',
    'motor_4',
    'motor_6',
    'family_4',
    'family_6',
    'social_4',
    'social_6',
    // Maktab dasturlari (1–8-sinf): `assets/data/school/<fan>_g<sinf>.json`.
    ...schoolFiles,
  ];

  /// Maktab fanlari dasturlari.
  static const List<String> schoolFiles = [
    'school/math_g3',
    'school/math_g5',
  ];

  final Lexicon lexicon;
  final InstructionBank instructions;

  /// Mantiq o'yinlari uchun qo'lda tuzilgan bog'lanishlar (analogiya, juftlar ...).
  final Map<String, dynamic> logicData;

  /// Kalit: `math_4`, `logic_6` ...
  final Map<String, Curriculum> curricula;

  /// O'zbek tili: alifbo, so'z bazasi, gap resurslari.
  final UzbekData uzbek;

  /// Yozish mashqlari chiziqlari.
  final GlyphBank glyphs;

  /// Ingliz va rus tili: alifbolar, harakatlar, sifatlar, iboralar, grammatik ma'lumot.
  final LanguageData languages;

  /// Ota-ona bilan faoliyatlar va muloqot (hislar, sehrli so'zlar, yaxshi do'st, xavfsizlik).
  final ActivityData activities;

  Curriculum? curriculum(String subject, String ageSuffix) => curricula['${subject}_$ageSuffix'];

  Topic? topic(String topicId) {
    for (final c in curricula.values) {
      final t = c.topic(topicId);
      if (t != null) return t;
    }
    return null;
  }

  Iterable<Topic> get allTopics => curricula.values.expand((c) => c.topics);

  static Future<ContentRepository> load([AssetBundle? bundle]) async {
    final b = bundle ?? rootBundle;
    Future<Map<String, dynamic>> json(String name) async =>
        MapUtils.asStringMap(jsonDecode(await b.loadString('assets/data/$name.json')));

    final curricula = <String, Curriculum>{};
    for (final name in curriculumFiles) {
      final c = Curriculum.fromJson(await json(name));
      curricula['${c.subject}_${c.ageSuffix}'] = c;
    }
    final banks = <String, List<Map<String, dynamic>>>{};
    for (final name in bankFiles) {
      final data = await json(name);
      for (final item in (data['items'] as List? ?? const []).map(MapUtils.asStringMap)) {
        banks.putIfAbsent(item['topic'].toString(), () => []).add(item);
      }
    }
    return ContentRepository(
      lexicon: Lexicon.fromJson(await json('lexicon')),
      instructions: InstructionBank.fromJson(await json('instructions')),
      logicData: await json('logic_data'),
      curricula: curricula,
      uzbek: UzbekData.fromJson(await json('uzbek')),
      glyphs: GlyphBank.fromJson(await json('glyphs')),
      languages: LanguageData.fromJson(await json('languages')),
      activities: ActivityData.fromJson(await json('montessori'), await json('social')),
      banks: banks,
    );
  }
}
