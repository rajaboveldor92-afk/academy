import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:academy/l10n/tr.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/generators/generator_base.dart';
import 'package:academy/learning/generators/registry.dart';
import 'package:academy/learning/models/exercise.dart';
import 'package:academy/models/subject.dart';
import 'package:academy/services/mother_voice.dart';
import 'package:flutter_test/flutter_test.dart';

/// Ilovadagi barcha o'zbekcha nutq matnlarini yig'adi (onaning klonlangan ovozi uchun).
///
/// `flutter test tool/voice/dump_speech_test.dart` → `tool/voice/out/speech_uz.json`:
/// har bir matn va u qancha marta uchragani (ko'p uchraydiganlari birinchi).
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('o‘zbekcha nutq matnlari', () async {
    final content = await ContentRepository.load();
    final counts = <String, int>{};
    final source = <String, String>{};
    void add(String text, String where, [int weight = 1]) {
      final t = text.trim();
      if (t.isEmpty) return;
      counts[t] = (counts[t] ?? 0) + weight;
      source.putIfAbsent(t, () => where);
    }

    final samples = int.tryParse(Platform.environment['SPEECH_SAMPLES'] ?? '') ?? 300;
    for (final topic in content.allTopics) {
      final gen = GeneratorRegistry.find(topic.subject, topic.ageSuffix, topic.generator)!;
      final age = topic.ageSuffix == '4' ? 4 : 6;
      for (var level = 1; level <= topic.maxLevel; level++) {
        final rng = Random(level * 7919 + topic.id.hashCode);
        for (var i = 0; i < samples; i++) {
          final Exercise e;
          try {
            e = gen(GenContext(rng: rng, content: content, topic: topic, level: level, age: age));
          } catch (_) {
            continue;
          }
          final where = '${topic.id}:${e.instructionKey}';
          if (e.speechParts.isNotEmpty) {
            for (final p in e.speechParts) {
              if (p.lang == 'uz' && p.clip == null) add(p.text, where);
            }
          } else if (e.speechLang == 'uz' && MotherVoice.instructionClip(e) == null) {
            add(e.speech, where);
          }
          if (e.speechLang == 'uz') {
            for (final o in e.options) {
              if (o.speech != null) add(o.speech!, '$where:option');
            }
            final a = e.assemble;
            if (a != null) add(a.result, '$where:assemble');
          }
        }
      }
    }

    // Ekranlar va maqtov: Tr (o'zbekcha), fan va mavzu nomlari, medal va sovg'a nomlari.
    const t = Tr('uz');
    for (final s in [
      t.whoPlays, t.dailyLessonSpoken, t.achievements, t.continueLesson, t.timeUp, t.levelUpSpoken,
      t.lookAndRemember, t.listenCarefully, t.listenAgain, 'Yana mashq qilamiz.', t.levelDown,
    ]) {
      add(s, 'ui', 50);
    }
    for (final s in Subject.values) {
      add(s.spokenIn('uz').$1, 'subject', 50);
    }
    for (final topic in content.allTopics) {
      add(topic.title.uz, 'topic_title', 5);
    }

    final sorted = counts.entries.toList()..sort((a, b) => b.value.compareTo(a.value));
    final out = Directory('tool/voice/out')..createSync(recursive: true);
    File('${out.path}/speech_uz.json').writeAsStringSync(const JsonEncoder.withIndent(' ').convert({
      'samples_per_level': samples,
      'distinct': sorted.length,
      'items': [for (final e in sorted) {'text': e.key, 'n': e.value, 'src': source[e.key]}],
    }));
    // ignore: avoid_print
    print('Distinct o‘zbekcha matnlar: ${sorted.length}');
  }, timeout: const Timeout(Duration(minutes: 30)));
}
