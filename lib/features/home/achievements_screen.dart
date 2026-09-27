import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../learning/content/content_provider.dart';
import '../../learning/engine/rewards.dart';
import '../../models/child_profile.dart';
import '../../models/child_progress.dart';
import '../../models/subject.dart';
import '../../theme/app_colors.dart';
import '../../widgets/stat_chip.dart';
import '../profiles/profiles_controller.dart';
import '../session/progress_controller.dart';

/// 🏆 Yutuqlarim — bolaning faqat o'z yutuqlari (boshqa bolalar bilan solishtirilmaydi):
/// o'suvchi bog', sovg'a qutisi va kolleksiya, medallar, fan kuboklari.
class AchievementsScreen extends ConsumerWidget {
  const AchievementsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profile = ref.watch(activeProfileProvider);
    if (profile == null) return const Scaffold();
    final progress = ref.watch(childProgressProvider(profile.id));

    return Scaffold(
      appBar: AppBar(title: const Text('Yutuqlarim')),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
          children: [
            Wrap(
              alignment: WrapAlignment.center,
              spacing: 10,
              runSpacing: 10,
              children: [
                StatChip(icon: '⭐', value: '${progress.stars}'),
                StatChip(icon: '🔥', value: '${progress.streak}', color: AppColors.gentle),
                StatChip(icon: '📚', value: '${progress.completedLessons}', color: AppColors.primary),
                StatChip(icon: '✅', value: '${progress.correctAnswers}', color: AppColors.success),
              ],
            ),
            const SizedBox(height: 16),
            _GardenCard(progress: progress),
            const SizedBox(height: 16),
            _GiftCard(profile: profile, progress: progress),
            const SizedBox(height: 16),
            _MedalsCard(progress: progress),
            const SizedBox(height: 16),
            _CupsCard(profile: profile, progress: progress),
          ],
        ),
      ),
    );
  }
}

class _Section extends StatelessWidget {
  const _Section({required this.title, required this.child, this.color = AppColors.primary, this.trailing});

  final String title;
  final Widget child;
  final Color color;
  final Widget? trailing;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: color.withAlpha(90), width: 3),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              Expanded(
                child: Text(title, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: AppColors.text)),
              ),
              if (trailing != null) trailing!,
            ],
          ),
          const SizedBox(height: 12),
          child,
        ],
      ),
    );
  }
}

// ------------------------------------------------------------------ Bog'
class _GardenCard extends StatelessWidget {
  const _GardenCard({required this.progress});

  final ChildProgress progress;

  @override
  Widget build(BuildContext context) {
    final plants = Rewards.garden(progress);
    final left = Rewards.lessonsPerPlant - progress.completedLessons % Rewards.lessonsPerPlant;
    final full = plants.length >= Rewards.maxPlants;
    return _Section(
      title: '🌳 Mening bog‘im',
      color: AppColors.success,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Container(
            key: const Key('garden'),
            constraints: const BoxConstraints(minHeight: 72),
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: const Color(0xFFE8F5E9),
              borderRadius: BorderRadius.circular(20),
            ),
            child: plants.isEmpty
                ? const Center(child: Opacity(opacity: 0.3, child: Text('🌱 🌱 🌱', style: TextStyle(fontSize: 34))))
                : Wrap(
                    alignment: WrapAlignment.center,
                    spacing: 6,
                    runSpacing: 4,
                    children: [for (final p in plants) Text(p, style: const TextStyle(fontSize: 34))],
                  ),
          ),
          const SizedBox(height: 8),
          Text(
            plants.isEmpty
                ? 'Darsni tugat — bog‘ingga birinchi niholcha ekamiz!'
                : (full ? 'Bog‘ing gullab-yashnayapti! Darslar gullarni o‘stiradi.' : 'Yana $left ta dars — yangi niholcha!'),
            textAlign: TextAlign.center,
            style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700, color: AppColors.textSoft),
          ),
        ],
      ),
    );
  }
}

// ------------------------------------------------------------------ Sovg'a qutisi
class _GiftCard extends ConsumerWidget {
  const _GiftCard({required this.profile, required this.progress});

  final ChildProfile profile;
  final ChildProgress progress;

  Future<void> _open(BuildContext context, WidgetRef ref) async {
    final gift = await ref.read(progressProvider.notifier).openGift(profile.id);
    if (gift == null || !context.mounted) return;
    ref.read(audioServiceProvider).speak('Voy! ${gift.name}!');
    await showDialog<void>(
      context: context,
      builder: (context) => AlertDialog(
        key: const Key('gift_dialog'),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(28)),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(gift.emoji, style: const TextStyle(fontSize: 96)),
            const SizedBox(height: 8),
            Text(gift.name, style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w900)),
            const SizedBox(height: 4),
            const Text('Kolleksiyangga qo‘shildi!', style: TextStyle(fontSize: 18)),
          ],
        ),
        actionsAlignment: MainAxisAlignment.center,
        actions: [
          FilledButton(
            key: const Key('gift_ok'),
            onPressed: () => Navigator.of(context).pop(),
            child: const Text('Zo‘r!'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final available = Rewards.giftsAvailable(progress);
    final collected = Rewards.collected(progress);
    final toNext = Rewards.starsToNextGift(progress);
    final unique = {for (final c in collected) c.emoji};
    return _Section(
      title: '🎁 Sovg‘a qutisi',
      color: AppColors.star,
      trailing: Text('${unique.length}/${Rewards.collection.length}',
          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: AppColors.textSoft)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          if (available > 0)
            FilledButton.icon(
              key: const Key('open_gift'),
              style: FilledButton.styleFrom(
                backgroundColor: AppColors.secondary,
                padding: const EdgeInsets.symmetric(vertical: 16),
                textStyle: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900),
              ),
              onPressed: () => _open(context, ref),
              icon: const Text('🎁', style: TextStyle(fontSize: 30)),
              label: Text(available > 1 ? 'Ochish ($available)' : 'Ochish'),
            )
          else ...[
            ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: LinearProgressIndicator(
                value: 1 - toNext / Rewards.starsPerGift,
                minHeight: 14,
                color: AppColors.star,
                backgroundColor: const Color(0xFFFFF3D6),
              ),
            ),
            const SizedBox(height: 6),
            Text(
              'Yana $toNext ⭐ to‘pla — sovg‘a qutisi ochiladi!',
              key: const Key('gift_progress'),
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700, color: AppColors.textSoft),
            ),
          ],
          const SizedBox(height: 12),
          const Text('🧸 Kolleksiyam', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w800)),
          const SizedBox(height: 8),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: [
              for (final c in Rewards.collection)
                Tooltip(
                  message: unique.contains(c.emoji) ? c.name : '?',
                  child: Container(
                    width: 46,
                    height: 46,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: unique.contains(c.emoji) ? const Color(0xFFFFF8E1) : const Color(0xFFF1F1F4),
                      borderRadius: BorderRadius.circular(14),
                    ),
                    child: unique.contains(c.emoji)
                        ? Text(c.emoji, style: const TextStyle(fontSize: 28))
                        : const Text('?', style: TextStyle(fontSize: 20, fontWeight: FontWeight.w900, color: Color(0xFFBDBDC7))),
                  ),
                ),
            ],
          ),
        ],
      ),
    );
  }
}

// ------------------------------------------------------------------ Medallar
class _MedalsCard extends StatelessWidget {
  const _MedalsCard({required this.progress});

  final ChildProgress progress;

  @override
  Widget build(BuildContext context) {
    final earned = progress.medals.toSet();
    final count = Rewards.medals.where((m) => earned.contains(m.id)).length;
    return _Section(
      title: '🏅 Medallar',
      color: AppColors.gentle,
      trailing: Text('$count/${Rewards.medals.length}',
          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800, color: AppColors.textSoft)),
      child: LayoutBuilder(builder: (context, c) {
        final perRow = c.maxWidth >= 600 ? 4 : 2;
        final w = (c.maxWidth - 10 * (perRow - 1)) / perRow;
        return Wrap(
          spacing: 10,
          runSpacing: 10,
          children: [
            // Qo'lga kiritilganlar oldinda.
            for (final m in [
              ...Rewards.medals.where((m) => earned.contains(m.id)),
              ...Rewards.medals.where((m) => !earned.contains(m.id)),
            ])
              SizedBox(width: w, child: _MedalTile(medal: m, earned: earned.contains(m.id))),
          ],
        );
      }),
    );
  }
}

class _MedalTile extends StatelessWidget {
  const _MedalTile({required this.medal, required this.earned});

  final MedalDef medal;
  final bool earned;

  @override
  Widget build(BuildContext context) {
    return Container(
      key: ValueKey('medal_${medal.id}'),
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: earned ? const Color(0xFFFFF8E1) : const Color(0xFFF5F5F7),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: earned ? AppColors.star : const Color(0xFFE0E0E6), width: 2),
      ),
      child: Row(
        children: [
          Opacity(
            opacity: earned ? 1 : 0.35,
            child: Text(earned ? medal.emoji : '🔒', style: const TextStyle(fontSize: 30)),
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  medal.title,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w900,
                    color: earned ? AppColors.text : AppColors.textSoft,
                  ),
                ),
                if (!earned)
                  Text(
                    medal.hint,
                    maxLines: 3,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: AppColors.textSoft),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// ------------------------------------------------------------------ Kuboklar
class _CupsCard extends ConsumerWidget {
  const _CupsCard({required this.profile, required this.progress});

  final ChildProfile profile;
  final ChildProgress progress;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final content = ref.watch(contentProvider).valueOrNull;
    return _Section(
      title: '🏆 Fan kuboklari',
      color: AppColors.secondary,
      child: content == null
          ? const Center(child: Padding(padding: EdgeInsets.all(12), child: CircularProgressIndicator()))
          : Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Text(
                  '🥉 bronza → 🥈 kumush → 🏆 oltin: fandagi mavzularni o‘rganganing sari kubok o‘sadi.',
                  style: TextStyle(fontSize: 14, fontWeight: FontWeight.w600, color: AppColors.textSoft),
                ),
                const SizedBox(height: 10),
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: [
                    for (final s in Subject.values)
                      if (profile.isSubjectEnabled(s.id) && content.curriculum(s.id, profile.age <= 5 ? '4' : '6') != null)
                        _CupChip(subject: s, tier: Rewards.cup(progress, content, s.id, profile.age)),
                  ],
                ),
              ],
            ),
    );
  }
}

class _CupChip extends StatelessWidget {
  const _CupChip({required this.subject, required this.tier});

  final Subject subject;
  final CupTier tier;

  @override
  Widget build(BuildContext context) {
    final has = tier != CupTier.none;
    return Container(
      key: ValueKey('cup_${subject.id}'),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      decoration: BoxDecoration(
        color: has ? subject.color.withAlpha(40) : const Color(0xFFF5F5F7),
        borderRadius: BorderRadius.circular(18),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(subject.emoji, style: const TextStyle(fontSize: 22)),
          const SizedBox(width: 6),
          Text(subject.title, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w800)),
          const SizedBox(width: 6),
          Opacity(opacity: has ? 1 : 0.4, child: Text(Rewards.cupEmoji(tier), style: const TextStyle(fontSize: 22))),
        ],
      ),
    );
  }
}
