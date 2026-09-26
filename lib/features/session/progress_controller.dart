import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../learning/engine/mastery.dart';
import '../../models/child_progress.dart';

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

  void reload() => state = ref.read(databaseProvider).getAllProgress();
}

final progressProvider =
    NotifierProvider<ProgressNotifier, Map<String, ChildProgress>>(ProgressNotifier.new);

/// Bitta bolaning statistikasi.
final childProgressProvider = Provider.family<ChildProgress, String>((ref, childId) {
  return ref.watch(progressProvider)[childId] ?? ChildProgress.empty(childId);
});
