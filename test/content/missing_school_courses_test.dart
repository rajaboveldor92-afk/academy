import 'dart:math';

import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/models/child_profile.dart';
import 'package:academy/models/subject.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;
  setUpAll(() async => content = await ContentRepository.load());

  test('all declared grades have usable content; no subject disappears through a missing file', () {
    for (var grade = 1; grade <= 8; grade++) {
      final profile = ChildProfile.create(id: 'g$grade', name: 'Child', age: grade + 6, avatar: '🦁', grade: grade);
      for (final subject in Subject.forProfile(profile)) {
        final c = content.curriculum(subject.id, subject.suffixFor(profile));
        expect(c, isNotNull, reason: '${subject.id}/g$grade');
        expect(c!.topics, isNotEmpty);
      }
    }
  });

  test('22 new courses: each lesson and each test builds at all three levels', () {
    const missing = {
      'english': [7,8], 'russian': [2,7,8], 'onatili': [7,8],
      'reading': [2,7,8], 'informatics': [1,2,7,8],
      'geography': [7,8], 'biology': [7,8], 'physics': [7,8], 'chemistry': [7,8],
    };
    for (final entry in missing.entries) {
      for (final grade in entry.value) {
        final c = content.curriculum(entry.key, 'g$grade')!;
        expect(c.topics.where((t) => !t.isTest).length, 4);
        expect(c.topics.where((t) => t.isTest).length, 5);
        for (final t in c.topics) {
          for (var level = 1; level <= 3; level++) {
            final lesson = LessonBuilder.build(content: content, topic: t, level: level,
              count: 8, age: grade + 6, rng: Random(level * 73));
            expect(lesson.length, 8, reason: '${t.id}/$level');
            expect(lesson.every(ExerciseValidator.isPlayable), isTrue, reason: t.id);
          }
        }
      }
    }
    final g7 = content.curriculum('english', 'g7')!.topics.first;
    final g8 = content.curriculum('english', 'g8')!.topics.first;
    expect(g7.theoryIn('uz'), isNot(g8.theoryIn('uz')));
  });
}
