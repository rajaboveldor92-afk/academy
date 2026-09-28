import 'dart:io';
import 'dart:math';

import 'package:academy/l10n/tr.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/models/subject.dart';
import 'package:academy/services/cloned_voice.dart';
import 'package:academy/services/mother_voice.dart';
import 'package:flutter_test/flutter_test.dart';

/// Klonlangan ovoz fayllari ilovadagi haqiqiy gaplarga mos keladi (kalit — matn xeshi).
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final dir = Directory('assets/audio/uz/klon');
  final files = dir.existsSync()
      ? dir.listSync().whereType<File>().map((f) => f.uri.pathSegments.last).toSet()
      : <String>{};

  bool voiced(String text) => MotherVoice.clipForText(text) != null || files.contains('${ClonedVoice.keyFor(text)}.m4a');

  test('fayllar bor va hajmi me’yorda', () {
    expect(files.length, greaterThan(2500));
    final bytes = dir.listSync().whereType<File>().fold<int>(0, (a, f) => a + f.lengthSync());
    expect(bytes, lessThan(40 * 1024 * 1024));
    expect(files.every((f) => RegExp(r'^[0-9a-f]{16}\.m4a$').hasMatch(f)), isTrue);
  });

  test('ekran gaplari va fan nomlari klonlangan ovozda', () {
    const t = Tr('uz');
    for (final s in [t.dailyLessonSpoken, t.achievements, t.whoPlays, t.levelUpSpoken, t.levelDown, t.lookAndRemember]) {
      expect(voiced(s), isTrue, reason: s);
    }
    for (final s in Subject.values) {
      expect(voiced(s.spokenIn('uz').$1), isTrue, reason: s.id);
    }
  });

  test('mashq ko‘rsatmalarining ko‘pchiligi klonlangan ovozda', () async {
    final content = await ContentRepository.load();
    var total = 0, hit = 0;
    for (final id in ['math4.count_1_3', 'uzbek4.letters', 'attention4.find', 'math6.add_10', 'uzbek6.letters', 'logic4.missing']) {
      final topic = content.topic(id);
      if (topic == null) continue;
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      final rng = Random(7);
      for (var i = 0; i < 40; i++) {
        final e = gen(GenContext(rng: rng, content: content, topic: topic, level: 1, age: topic.ageSuffix == '4' ? 4 : 6));
        if (e.speechLang != 'uz' || e.speechParts.isNotEmpty) continue;
        total++;
        if (voiced(e.speech) || MotherVoice.instructionClip(e) != null) hit++;
      }
    }
    expect(total, greaterThan(100));
    expect(hit / total, greaterThan(0.8), reason: '$hit / $total');
  });
}
