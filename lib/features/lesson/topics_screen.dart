import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../learning/content/content_provider.dart';
import '../../learning/engine/mastery.dart';
import '../../learning/models/topic.dart';
import '../../models/child_profile.dart';
import '../../models/child_progress.dart';
import '../../models/subject.dart';
import '../../l10n/tr.dart';
import '../../router/app_router.dart';
import '../../services/mother_voice.dart';
import '../../theme/app_colors.dart';
import '../../widgets/pressable_scale.dart';
import '../profiles/profiles_controller.dart';
import '../session/progress_controller.dart';

/// Fan ichidagi mavzular: "▶ Davom etamiz" + mavzu kartalari (yulduzchalar bilan).
/// Foizlar bola ekranida ko'rsatilmaydi — faqat ota-ona panelida.
class TopicsScreen extends ConsumerWidget {
  const TopicsScreen({super.key, required this.subject, required this.curriculum});

  final Subject subject;
  final Curriculum curriculum;

  /// Tavsiya etilgan mavzu: tartib bo'yicha birinchi hali to'liq egallanmagani.
  static Topic recommended(Curriculum c, ChildProgress p) {
    for (final t in c.topics) {
      final s = p.skillOf(t.id);
      final mastered = s.level >= t.maxLevel && s.lastAccuracy >= AdaptiveRule.upThreshold;
      if (!mastered) return t;
    }
    // Hammasi egallangan — eng uzoq mashq qilinmaganini takrorlaymiz.
    final sorted = [...c.topics]
      ..sort((a, b) {
        final da = p.skillOf(a.id).lastPracticed ?? DateTime(2000);
        final db = p.skillOf(b.id).lastPracticed ?? DateTime(2000);
        return da.compareTo(db);
      });
    return sorted.first;
  }

  /// Kartadagi yulduzlar: egallangan darajalar soni (0..3).
  static int starsFor(Topic t, SkillStat s) {
    if (!s.started) return 0;
    final cleared = s.level - 1 + (s.lastAccuracy >= AdaptiveRule.upThreshold && s.level >= t.maxLevel ? 1 : 0);
    return cleared.clamp(0, t.maxLevel).toInt();
  }

  void _open(BuildContext context, WidgetRef ref, Topic t, {bool resume = false}) {
    final audio = ref.read(audioServiceProvider);
    // "Davom etamiz" kartasi — onaning ovozida; boshqa mavzu — uning nomi.
    final lang = ref.read(activeProfileProvider)?.language ?? 'uz';
    if (resume && lang == 'uz') {
      audio.speakParts([MotherVoice.part('davom_etamiz')]);
    } else {
      audio.speak(resume ? Tr(lang).continueLesson : t.title.of(lang), lang: lang);
    }
    Navigator.of(context).pushNamed(AppRoutes.lesson, arguments: t.id);
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profile = ref.watch(activeProfileProvider);
    if (profile == null) return const Scaffold();
    final progress = ref.watch(childProgressProvider(profile.id));
    final rec = recommended(curriculum, progress);
    final width = MediaQuery.sizeOf(context).width;
    final columns = width >= 900 ? 4 : (width >= 600 ? 3 : 2);
    final lang = profile.language;

    return LangScope(
      lang: lang,
      child: Scaffold(
      appBar: AppBar(
        title: Text('${subject.emoji}  ${curriculum.title.of(lang)}'),
        backgroundColor: subject.color.withAlpha(40),
      ),
      body: SafeArea(
        child: CustomScrollView(
          slivers: [
            SliverToBoxAdapter(child: _continueCard(context, ref, rec, profile)),
            SliverPadding(
              padding: const EdgeInsets.fromLTRB(12, 4, 12, 24),
              sliver: SliverGrid(
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: columns,
                  mainAxisSpacing: 12,
                  crossAxisSpacing: 12,
                  childAspectRatio: 0.95,
                ),
                delegate: SliverChildBuilderDelegate(
                  (context, i) {
                    final t = curriculum.topics[i];
                    return _TopicCard(
                      topic: t,
                      stars: starsFor(t, progress.skillOf(t.id)),
                      color: subject.color,
                      highlighted: t.id == rec.id,
                      showCode: !profile.ageGroup.isJunior,
                      onTap: () => _open(context, ref, t),
                    );
                  },
                  childCount: curriculum.topics.length,
                ),
              ),
            ),
          ],
        ),
      ),
      ),
    );
  }

  Widget _continueCard(BuildContext context, WidgetRef ref, Topic rec, ChildProfile profile) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(12, 12, 12, 8),
      child: PressableScale(
        onTap: () => _open(context, ref, rec, resume: true),
        child: Container(
          key: const Key('continue_topic'),
          padding: const EdgeInsets.all(18),
          decoration: BoxDecoration(
            color: subject.color,
            borderRadius: BorderRadius.circular(28),
            boxShadow: [BoxShadow(color: subject.color.withAlpha(80), blurRadius: 16, offset: const Offset(0, 8))],
          ),
          child: Row(
            children: [
              const Icon(Icons.play_circle_fill_rounded, color: Colors.white, size: 56),
              const SizedBox(width: 14),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(Tr(profile.language).continueLesson,
                        style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.w900)),
                    Text(
                      '${rec.emoji}  ${rec.title.of(profile.language)}',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.w700),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _TopicCard extends StatelessWidget {
  const _TopicCard({
    required this.topic,
    required this.stars,
    required this.color,
    required this.highlighted,
    required this.showCode,
    required this.onTap,
  });

  final Topic topic;
  final int stars;
  final Color color;
  final bool highlighted;
  final bool showCode;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return PressableScale(
      onTap: onTap,
      semanticLabel: topic.title.of(Tr.of(context).lang),
      child: Container(
        key: Key('topic_${topic.id}'),
        padding: const EdgeInsets.all(10),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(24),
          border: Border.all(color: highlighted ? color : color.withAlpha(60), width: highlighted ? 4 : 2),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (showCode)
              Align(
                alignment: Alignment.topLeft,
                child: Text(topic.code, style: TextStyle(color: color, fontWeight: FontWeight.w900)),
              ),
            Expanded(
              child: FittedBox(
                child: Text(topic.emoji, style: const TextStyle(fontSize: 48)),
              ),
            ),
            Text(
              topic.title.of(Tr.of(context).lang),
              textAlign: TextAlign.center,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: AppColors.text, height: 1.1),
            ),
            const SizedBox(height: 4),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                for (var i = 0; i < topic.maxLevel; i++)
                  Icon(
                    i < stars ? Icons.star_rounded : Icons.star_outline_rounded,
                    color: i < stars ? AppColors.star : const Color(0xFFD0D4E0),
                    size: 22,
                  ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

/// Fan ekrani: dasturi bor fanlar uchun mavzular, qolganlari uchun keyingi bosqich xabari.
final curriculumForProvider = FutureProvider.family<Curriculum?, (String, String)>((ref, key) async {
  final content = await ref.watch(contentProvider.future);
  return content.curriculum(key.$1, key.$2);
});
