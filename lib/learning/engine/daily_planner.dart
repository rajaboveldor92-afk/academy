import 'dart:math';

import '../../models/child_progress.dart';
import '../content/content_repository.dart';
import '../content/technology_tracks.dart';
import '../models/exercise.dart';
import '../models/topic.dart';
import 'lesson_builder.dart';
import 'spaced_repetition.dart';

/// Rejadagi mashq: qaysi mavzudan, qaysi darajada, takrorlashmi.
class PlannedExercise {
  const PlannedExercise({
    required this.topic,
    required this.level,
    required this.exercise,
    this.review = false,
    this.retry = false,
  });

  final Topic topic;
  final int level;
  final Exercise exercise;

  /// Takrorlash navbatidan (spaced repetition) olingan.
  final bool review;

  /// Shu darsda xato qilingan tushuncha — biroz keyin boshqa ko'rinishda qayta so'raladi.
  final bool retry;
}

/// "▶ BUGUNGI DARSim" — kunlik aralash dars.
///
/// * Avval takrorlash vaqti kelgan tushunchalar (boshqa ko'rinishda qayta yaratiladi).
/// * Keyin fanlar navbat bilan: har bir fandan bola hozir o'rganayotgan mavzu
///   (hali egallanmagan, oldingi mavzulari boshlangan), eng uzoq mashq qilinmagani.
/// * Uzoq faoliyatlar (AI bilan o'yin, puzzle, ekrandan tashqari ish) kunlik darsga kirmaydi.
/// * 4 yosh: 6 ta mashq (5–10 daqiqa), 6 yosh: 10 ta mashq (10–20 daqiqa).
class DailyPlanner {
  DailyPlanner._();

  static const Set<String> skipGenerators = {'activity', 'play', 'jigsaw', 'test'};

  static const List<String> juniorOrder = [
    'math', 'uzbek', 'logic', 'english', 'memory', 'writing', 'russian', 'attention', 'trilingual', 'motor', 'social', 'chess',
  ];
  static const List<String> seniorOrder = [
    'math', 'uzbek', 'writing', 'logic', 'english', 'russian', 'chess', 'math', 'memory', 'attention', 'trilingual', 'social',
  ];

  /// Maktab o'quvchilari: fanlar navbati (matematika va ona tili ko'proq).
  static const List<String> schoolOrder = [
    'math', 'logic', 'onatili', 'english', 'mental', 'reading', 'russian', 'science', 'math', 'informatics', 'technology',
    'onatili', 'geography', 'biology', 'physics', 'chemistry',
  ];

  static int sizeFor(int age, {int grade = 0}) => grade > 0 ? 10 : (age <= 5 ? 6 : 10);

  static List<PlannedExercise> build({
    required ContentRepository content,
    required int age,
    required ChildProgress progress,
    required bool Function(String subjectId) isEnabled,
    required DateTime now,
    Random? rng,
    int difficultyBias = 0,
    String lang = 'uz',
    int grade = 0,
    String technologyTrack = 'both',
  }) {
    final random = rng ?? Random();
    // Maktab o'quvchisi — sinf dasturi (`g3`), shaxmat — 6 yosh dasturi.
    String suffixOf(String subject) => grade > 0 ? (subject == 'chess' ? '6' : 'g$grade') : ((subject == 'math' || subject == 'logic') ? age.clamp(3, 8).toString() : (age <= 5 ? '4' : '6'));
    final total = sizeFor(age, grade: grade);
    final plan = <PlannedExercise>[];
    final usedTopics = <String>{};

    int levelOf(Topic t) => (progress.skillOf(t.id).level + difficultyBias).clamp(1, t.maxLevel).toInt();

    // 1) Takrorlash.
    final reviews = <PlannedExercise>[];
    for (final r in SpacedRepetition.due(progress.reviews, now)) {
      if (reviews.length >= total ~/ 3) break;
      final t = content.topic(r.topicId);
      if (t == null || !TechnologyTracks.includes(t, technologyTrack) || t.ageSuffix != suffixOf(t.subject) || !isEnabled(t.subject) || skipGenerators.contains(t.generator)) {
        continue;
      }
      if (usedTopics.contains(t.id)) continue;
      final ex = LessonBuilder.similar(
        content: content,
        topic: t,
        level: levelOf(t),
        age: age,
        rng: random,
        lang: lang,
        concept: r.concept,
        avoid: progress.recentOf(t.id).toSet(),
      );
      if (ex == null) continue;
      usedTopics.add(t.id);
      reviews.add(PlannedExercise(topic: t, level: levelOf(t), exercise: ex, review: true));
    }

    // 2) Fanlar navbati (har kuni boshqa fandan boshlanadi).
    final order = grade > 0 ? schoolOrder : (age <= 5 ? juniorOrder : seniorOrder);
    final offset = now.difference(DateTime(2024)).inDays % order.length;
    final fresh = <PlannedExercise>[];
    var guard = 0;
    for (var i = 0; fresh.length + reviews.length < total && guard < order.length * 3; i++, guard++) {
      final subject = order[(offset + i) % order.length];
      if (!isEnabled(subject)) continue;
      final c = content.curriculum(subject, suffixOf(subject));
      if (c == null) continue;
      final t = nextTopic(c.topics.where((t) => TechnologyTracks.includes(t, technologyTrack)).toList(), progress, random, exclude: usedTopics);
      if (t == null) continue;
      final ex = LessonBuilder.similar(
        content: content,
        topic: t,
        level: levelOf(t),
        age: age,
        rng: random,
        lang: lang,
        avoid: progress.recentOf(t.id).toSet(),
      );
      if (ex == null) continue;
      usedTopics.add(t.id);
      fresh.add(PlannedExercise(topic: t, level: levelOf(t), exercise: ex));
    }

    // 3) Aralashtirish: birinchisi — yangi (qiziqarli boshlanish), takrorlashlar orasiga tarqaladi.
    if (fresh.isNotEmpty) plan.add(fresh.removeAt(0));
    final gap = reviews.isEmpty ? 0 : (fresh.length / (reviews.length + 1)).ceil().clamp(1, 99).toInt();
    while (fresh.isNotEmpty || reviews.isNotEmpty) {
      for (var k = 0; k < gap && fresh.isNotEmpty; k++) {
        plan.add(fresh.removeAt(0));
      }
      if (reviews.isNotEmpty) plan.add(reviews.removeAt(0));
      if (gap == 0) {
        plan.addAll(fresh);
        fresh.clear();
      }
    }
    return plan;
  }

  /// Bola hozir o'rganayotgan mavzu: hali egallanmagan, oldingi mavzulari boshlangan,
  /// shular ichida eng uzoq mashq qilinmagani. Hammasi egallangan bo'lsa — tasodifiy takrorlash.
  static Topic? nextTopic(List<Topic> topics, ChildProgress progress, Random rng, {Set<String> exclude = const {}}) {
    final usable = topics.where((t) => !skipGenerators.contains(t.generator) && !exclude.contains(t.id)).toList();
    if (usable.isEmpty) return null;
    bool mastered(Topic t) => progress.skillOf(t.id).mastery(t.maxLevel) >= 85;
    bool ready(Topic t) => t.prerequisites.every((p) => progress.skillOf(p).started);
    final frontier = usable.where((t) => !mastered(t) && ready(t)).take(3).toList();
    if (frontier.isEmpty) return usable[rng.nextInt(usable.length)];
    frontier.sort((a, b) {
      final la = progress.skillOf(a.id).lastPracticed, lb = progress.skillOf(b.id).lastPracticed;
      if (la == null && lb == null) return 0;
      if (la == null) return -1;
      if (lb == null) return 1;
      return la.compareTo(lb);
    });
    return frontier.first;
  }
}
