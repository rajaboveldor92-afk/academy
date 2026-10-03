import 'dart:math';

import 'package:academy/database/seed_data.dart';
import 'package:academy/features/parent/child_report.dart';
import 'package:academy/learning/content/content_repository.dart';
import 'package:academy/learning/content/technology_tracks.dart';
import 'package:academy/learning/engine/daily_planner.dart';
import 'package:academy/learning/engine/lesson_builder.dart';
import 'package:academy/learning/engine/mastery.dart';
import 'package:academy/learning/engine/rewards.dart';
import 'package:academy/learning/engine/spaced_repetition.dart';
import 'package:academy/models/child_profile.dart';
import 'package:academy/models/child_progress.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late ContentRepository content;
  setUpAll(() async => content = await ContentRepository.load());

  test('profile recommendation, override and legacy persistence', () {
    final p = ChildProfile.create(id: 'x', name: 'Child', age: 9, avatar: '🦁', grade: 3);
    expect(p.effectiveTechnologyTrack, 'both');
    expect(p.copyWith(gender: 'girl').effectiveTechnologyTrack, 'service');
    expect(p.copyWith(gender: 'boy').effectiveTechnologyTrack, 'technical');
    final override = p.copyWith(gender: 'girl', technologyTrack: 'technical');
    expect(override.effectiveTechnologyTrack, 'technical');
    expect(ChildProfile.fromMap(override.toMap()), override);
    expect(ChildProfile.fromMap({'id': 'old', 'gender': 'invalid', 'technologyTrack': 'invalid'}).effectiveTechnologyTrack, 'both');
  });

  test('v3 migration preserves progress and parent override; repeated launch is stable', () async {
    final t = TestDb.memory();
    addTearDown(t.dispose);
    final original = SeedData.jasmina(DateTime(2026)).copyWith(gender: 'unspecified', technologyTrack: 'technical', greeting: 'Salom!');
    await t.db.saveProfile(original);
    await t.db.saveProgress(ChildProgress.empty(original.id).addStars(57));
    await t.db.saveSettings(t.db.getSettings().copyWith(seeded: true, dataVersion: 3));
    await SeedData.ensureSeeded(t.db);
    final migrated = t.db.getProfile(original.id)!;
    expect(migrated.gender, 'girl');
    expect(migrated.technologyTrack, 'technical');
    expect(migrated.greeting, 'Salom!');
    expect(t.db.getProgress(original.id).stars, 57);
    await SeedData.ensureSeeded(t.db);
    expect(t.db.getProfile(original.id), migrated);
  });

  for (final grade in [3, 5]) {
    for (final track in ['service', 'technical']) {
      test('g$grade $track: common topics, isolated tests and workshops', () {
        final p = ChildProfile.create(id: 'x', name: 'Child', age: grade + 6, avatar: '🦁', grade: grade, technologyTrack: track);
        final raw = content.curriculum('technology', 'g$grade')!;
        final filtered = TechnologyTracks.forProfile(raw, p);
        final ids = filtered.topics.map((t) => t.id).toSet();
        expect(ids, contains('technology_g$grade.${grade == 3 ? 'safety' : 'design'}'));
        expect(filtered.topics.any((t) => t.tags.contains('track:$track')), isTrue);
        expect(filtered.topics.any((t) => t.tags.contains('track:${track == 'service' ? 'technical' : 'service'}')), isFalse);
        expect(TechnologyTracks.forProfile(raw, p.copyWith(technologyTrack: 'both')).topics.length, raw.topics.length);
        for (final topic in filtered.topics.where((t) => t.isTest)) {
          for (final lv in topic.levels) {
            expect(ids, containsAll(lv['topics'] as List));
          }
          final lesson = LessonBuilder.build(content: content, topic: topic, level: 3, count: 10, age: p.age, rng: Random(13));
          expect(lesson.length, 10);
          expect(lesson.every(ExerciseValidator.isPlayable), isTrue);
        }
        var progress = ChildProgress.empty(p.id);
        for (final topic in filtered.topics) {
          progress = progress.withSkill(topic.id, SkillStat(level: topic.maxLevel, ema: 100, lessons: 3));
        }
        expect(Rewards.cup(progress, content, 'technology', 'g$grade', technologyTrack: track), CupTier.gold);
        expect(Rewards.cup(progress, content, 'technology', 'g$grade'), isNot(CupTier.gold));
      });
    }
  }

  test('parent report hides other-track topics and review counts without deleting saved work', () {
    final day = DateTime(2026, 10, 3);
    final profile = SeedData.akramjon(day).copyWith(technologyTrack: 'service');
    final shared = ReviewItem(topicId: 'technology_g5.design', concept: 'shared', stage: 0, due: day);
    final hidden = ReviewItem(topicId: 'technology_g5.mechanisms', concept: 'hidden', stage: 0, due: day);
    final nextWeek = ReviewItem(topicId: 'technology_g5.prototype', concept: 'week', stage: 1, due: day.add(const Duration(days: 3)));
    final progress = ChildProgress.empty(profile.id).withReviews({shared.key: shared, hidden.key: hidden, nextWeek.key: nextWeek});
    final report = ChildReport.build(profile: profile, progress: progress, content: content, now: day);
    expect(report.reviewsDue, 1);
    expect(report.reviewsWeek, 0);
    expect(report.reviewsTotal, 1);
    expect(report.subjects.where((s) => s.subject.id == 'technology').single.topics.every(
      (t) => TechnologyTracks.includes(t.topic, 'service')), isTrue);
    expect(progress.reviews.length, 3);
    final both = ChildReport.build(profile: profile.copyWith(technologyTrack: 'both'), progress: progress, content: content, now: day);
    expect(both.reviewsDue, 2);
    expect(both.reviewsWeek, 1);
    expect(both.reviewsTotal, 3);
  });

  test('daily lessons exclude hidden-track fresh tasks and due reviews', () {
    final day = DateTime(2026, 10, 3);
    final topic = content.topic('technology_g5.mechanisms')!;
    final ex = LessonBuilder.build(content: content, topic: topic, level: 1, count: 1, age: 11, rng: Random(1)).single;
    final queue = SpacedRepetition.record(const {}, topicId: topic.id, concept: ex.conceptKey, firstTry: false, now: day);
    for (final track in ['service', 'technical']) {
      var sawTechnology = false;
      for (var d = 1; d <= 20; d++) {
        final plan = DailyPlanner.build(content: content, age: 11, grade: 5, technologyTrack: track,
          progress: ChildProgress.empty('x').withReviews(queue), isEnabled: (_) => true,
          now: day.add(Duration(days: d)), rng: Random(d));
        expect(plan.length, 10);
        for (final p in plan) {
          expect(TechnologyTracks.includes(p.topic, track), isTrue);
          if (p.topic.subject == 'technology') sawTechnology = true;
        }
        if (track == 'service') expect(plan.any((p) => p.topic.id == topic.id), isFalse);
      }
      expect(sawTechnology, isTrue);
    }
  });
}
