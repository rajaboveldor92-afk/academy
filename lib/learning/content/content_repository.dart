import 'dart:convert';

import 'package:flutter/services.dart';

import '../../core/utils/map_utils.dart';
import '../models/topic.dart';
import 'instructions.dart';
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
  });

  /// Dastur fayllari: `<fan>_<4|6>.json`.
  static const List<String> curriculumFiles = [
    'math_4',
    'logic_4',
    'math_6',
    'logic_6',
    'uzbek_4',
    'uzbek_6',
    'writing_4',
    'writing_6',
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
      curricula[name] = Curriculum.fromJson(await json(name));
    }
    return ContentRepository(
      lexicon: Lexicon.fromJson(await json('lexicon')),
      instructions: InstructionBank.fromJson(await json('instructions')),
      logicData: await json('logic_data'),
      curricula: curricula,
      uzbek: UzbekData.fromJson(await json('uzbek')),
      glyphs: GlyphBank.fromJson(await json('glyphs')),
    );
  }
}
