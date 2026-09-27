import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../learning/engine/mastery.dart';
import '../../learning/engine/rewards.dart';
import '../../learning/engine/spaced_repetition.dart';
import '../../models/child_progress.dart';

/// Darsdagi bitta mashq natijasi (takrorlash navbati va kunlik dars uchun).
class ExerciseResult {
  const ExerciseResult({
    required this.topicId,
    required this.concept,
    required this.firstTry,
    required this.signature,
    this.retry = false,
  });

  final String topicId;
  final String concept;
  final bool firstTry;
  final int signature;

  /// Shu darsning o'zida qayta so'ralgan (xatodan keyin) mashq.
  final bool retry;
}

/// Barcha bolalar statistikasi: `childId → ChildProgress`.
///
/// Har bir o'zgarish darhol lokal bazaga yoziladi, shuning uchun ilova
/// kutilmaganda yopilsa ham progress yo'qolmaydi.
class ProgressNotifier extends Notifier<Map<String, ChildProgress>> {
  @override
  Map<String, ChildProgress> build() => ref.read(databaseProvider).getAllProgress();

  ChildProgress of(String childId) => state[childId] ?? ChildProgress.empty(childId);

  /// [change] funksiyasi eski qiymatdan yangisini yasaydi; natija saqlanadi.
  Future<ChildProgress> update(
    String childId,
    ChildProgress Function(ChildProgress current) change,
  ) async {
    final updated = change(of(childId));
    state = {...state, childId: updated};
    await ref.read(databaseProvider).saveProgress(updated);
    return updated;
  }

  Future<void> registerVisit(String childId) =>
      update(childId, (p) => p.registerVisit(ref.read(clockProvider)()));

  Future<void> addSeconds(String childId, int seconds) =>
      update(childId, (p) => p.addSeconds(ref.read(clockProvider)(), seconds));

  /// Javobni qayd etadi va to'g'ri bo'lsa yulduz beradi.
  Future<ChildProgress> recordAnswer({
    required String childId,
    required String subjectId,
    required bool isCorrect,
    int rewardStars = 1,
  }) {
    return update(
      childId,
      (p) => p.recordAnswer(
        subjectId: subjectId,
        isCorrect: isCorrect,
        now: ref.read(clockProvider)(),
        rewardStars: rewardStars,
      ),
    );
  }

  /// Mavzu bo'yicha dars tugaganda: adaptiv daraja, mastery va takrorlanmaslik tarixi.
  Future<({SkillStat stat, LevelDecision decision})> completeTopicLesson({
    required String childId,
    required String topicId,
    required int maxLevel,
    required int correctFirstTry,
    required int total,
    Iterable<int> signatures = const [],
  }) async {
    late ({SkillStat stat, LevelDecision decision}) outcome;
    await update(childId, (p) {
      outcome = AdaptiveRule.apply(
        p.skillOf(topicId),
        correctFirstTry: correctFirstTry,
        total: total,
        maxLevel: maxLevel,
        now: ref.read(clockProvider)(),
      );
      return p.withSkill(topicId, outcome.stat).addRecent(topicId, signatures).completeLesson();
    });
    return outcome;
  }

  /// Takrorlash navbatini natijalar bo'yicha yangilaydi (xato → ertaga, to'g'ri takrorlash → keyingi bosqich).
  static ChildProgress applyReviews(ChildProgress p, Iterable<ExerciseResult> results, DateTime now) {
    var queue = p.reviews;
    for (final r in results) {
      // Shu darsning o'zidagi qayta so'rash navbatni o'zgartirmaydi: ertangi takrorlash baribir bo'ladi.
      if (r.retry) continue;
      queue = SpacedRepetition.record(queue, topicId: r.topicId, concept: r.concept, firstTry: r.firstTry, now: now);
    }
    return p.withReviews(queue);
  }

  Future<void> recordReviews(String childId, Iterable<ExerciseResult> results) =>
      update(childId, (p) => applyReviews(p, results, ref.read(clockProvider)()));

  /// "Bugungi darsim" tugaganda: har bir mavzu yengil hisobga olinadi (daraja o'zgarmaydi),
  /// takrorlash navbati va yutuqlar yangilanadi.
  Future<ChildProgress> completeDailyLesson(String childId, List<ExerciseResult> results) {
    final now = ref.read(clockProvider)();
    return update(childId, (p) {
      var next = p;
      final byTopic = <String, List<ExerciseResult>>{};
      for (final r in results.where((r) => !r.retry)) {
        byTopic.putIfAbsent(r.topicId, () => []).add(r);
      }
      byTopic.forEach((topicId, list) {
        final correct = list.where((r) => r.firstTry).length;
        next = next
            .withSkill(topicId, next.skillOf(topicId).practiced(correct: correct, total: list.length, now: now))
            .addRecent(topicId, list.map((r) => r.signature));
      });
      next = applyReviews(next, results, now).completeLesson().completeDaily(now);
      if (results.isNotEmpty && results.every((r) => r.firstTry)) next = next.addCounter('perfect_lesson');
      return next;
    });
  }

  Future<void> addCounter(String childId, String id) => update(childId, (p) => p.addCounter(id));

  /// Yangi qo'lga kiritilgan medallarni beradi va ularni qaytaradi (tabriklash uchun).
  Future<List<MedalDef>> awardMedals(String childId) async {
    final fresh = Rewards.newMedals(of(childId));
    if (fresh.isEmpty) return const [];
    await update(childId, (p) {
      var next = p;
      for (final m in fresh) {
        next = next.addMedal(m.id);
      }
      return next;
    });
    return fresh;
  }

  /// Sovg'a qutisini ochadi (yulduzlar yetarli bo'lsa). Kolleksiyaga qo'shilgan narsani qaytaradi.
  Future<Collectible?> openGift(String childId) async {
    final p = of(childId);
    if (Rewards.giftsAvailable(p) <= 0) return null;
    final gift = Rewards.nextGift(p);
    await update(childId, (c) => c.openGift());
    return gift;
  }

  void reload() => state = ref.read(databaseProvider).getAllProgress();
}

final progressProvider =
    NotifierProvider<ProgressNotifier, Map<String, ChildProgress>>(ProgressNotifier.new);

/// Bitta bolaning statistikasi.
final childProgressProvider = Provider.family<ChildProgress, String>((ref, childId) {
  return ref.watch(progressProvider)[childId] ?? ChildProgress.empty(childId);
});
