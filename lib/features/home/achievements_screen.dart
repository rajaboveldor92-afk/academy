import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../theme/app_colors.dart';
import '../profiles/profiles_controller.dart';
import '../session/progress_controller.dart';

/// 🏆 Yutuqlarim — yulduzlar, ketma-ket kunlar va medallar.
class AchievementsScreen extends ConsumerWidget {
  const AchievementsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profile = ref.watch(activeProfileProvider);
    if (profile == null) return const Scaffold();
    final progress = ref.watch(childProgressProvider(profile.id));
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: const Text('Yutuqlarim')),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(20),
          children: [
            _BigStat(emoji: '⭐', value: progress.stars, label: 'Yulduzlar', color: AppColors.star),
            const SizedBox(height: 16),
            _BigStat(
              emoji: '🔥',
              value: progress.streak,
              label: 'Ketma-ket kunlar',
              color: AppColors.gentle,
            ),
            const SizedBox(height: 16),
            _BigStat(
              emoji: '✅',
              value: progress.correctAnswers,
              label: "To'g'ri javoblar",
              color: AppColors.success,
            ),
            const SizedBox(height: 24),
            Text('🏅 Medallar', style: textTheme.titleLarge),
            const SizedBox(height: 12),
            if (progress.medals.isEmpty)
              Text(
                "Birinchi medal uchun o'ynashda davom et!",
                style: textTheme.titleMedium?.copyWith(color: AppColors.textSoft),
              )
            else
              Wrap(
                spacing: 12,
                runSpacing: 12,
                children: [
                  for (final m in progress.medals) Chip(label: Text('🏅 $m')),
                ],
              ),
          ],
        ),
      ),
    );
  }
}

class _BigStat extends StatelessWidget {
  const _BigStat({
    required this.emoji,
    required this.value,
    required this.label,
    required this.color,
  });

  final String emoji;
  final int value;
  final String label;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: color.withAlpha(40),
        borderRadius: BorderRadius.circular(28),
      ),
      child: Row(
        children: [
          Text(emoji, style: const TextStyle(fontSize: 48)),
          const SizedBox(width: 20),
          Expanded(child: Text(label, style: Theme.of(context).textTheme.titleLarge)),
          Text('$value', style: Theme.of(context).textTheme.displaySmall),
        ],
      ),
    );
  }
}
