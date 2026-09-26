import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../core/utils/date_keys.dart';
import '../../models/child_profile.dart';
import '../../models/child_progress.dart';
import '../../models/subject.dart';
import '../../router/app_router.dart';
import '../../theme/app_colors.dart';
import '../../widgets/avatar_bubble.dart';
import '../session/progress_controller.dart';
import '../profiles/profiles_controller.dart';
import 'settings_controller.dart';

/// Ota-ona bo'limi: bolalar statistikasi va umumiy sozlamalar.
class ParentHomeScreen extends ConsumerWidget {
  const ParentHomeScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profiles = ref.watch(profilesProvider);
    final settings = ref.watch(settingsProvider);
    final now = ref.read(clockProvider)();
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: const Text('Ota-ona')),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            Text('Bolalar', style: textTheme.titleLarge),
            const SizedBox(height: 8),
            for (final p in profiles)
              _ChildSummaryCard(
                profile: p,
                progress: ref.watch(childProgressProvider(p.id)),
                now: now,
                onTap: () => Navigator.of(context)
                    .pushNamed(AppRoutes.childSettings, arguments: p.id),
              ),
            const SizedBox(height: 8),
            OutlinedButton.icon(
              onPressed: () => Navigator.of(context).pushNamed(AppRoutes.profileEditor),
              icon: const Icon(Icons.person_add_alt_1_rounded),
              label: const Text("Bola qo'shish"),
            ),
            const SizedBox(height: 24),
            Text('Sozlamalar', style: textTheme.titleLarge),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: [
                  SwitchListTile(
                    title: const Text('Ovoz effektlari'),
                    value: settings.soundEnabled,
                    onChanged: (v) => ref.read(settingsProvider.notifier).setSound(v),
                  ),
                  SwitchListTile(
                    title: const Text("So'zlarni ovozda aytish"),
                    value: settings.voiceEnabled,
                    onChanged: (v) => ref.read(settingsProvider.notifier).setVoice(v),
                  ),
                  SwitchListTile(
                    title: const Text('Fon musiqasi'),
                    value: settings.musicEnabled,
                    onChanged: (v) => ref.read(settingsProvider.notifier).setMusic(v),
                  ),
                  ListTile(
                    leading: const Icon(Icons.password_rounded),
                    title: const Text("PIN kodni o'zgartirish"),
                    trailing: const Icon(Icons.chevron_right_rounded),
                    onTap: () => Navigator.of(context).pushNamed(AppRoutes.changePin),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),
            Text(
              "Barcha ma'lumotlar faqat shu qurilmada saqlanadi. Reklama, chat va internet yo'q.",
              style: textTheme.bodyMedium?.copyWith(color: AppColors.textSoft),
            ),
          ],
        ),
      ),
    );
  }
}

class _ChildSummaryCard extends StatelessWidget {
  const _ChildSummaryCard({
    required this.profile,
    required this.progress,
    required this.now,
    required this.onTap,
  });

  final ChildProfile profile;
  final ChildProgress progress;
  final DateTime now;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final color = AppColors.profileColor(profile.colorIndex);
    final textTheme = Theme.of(context).textTheme;
    final scores = progress.subjectScores.entries.where((e) => e.value.total > 0).toList();
    final limit = profile.dailyLimitMinutes == 0 ? 'cheklanmagan' : '${profile.dailyLimitMinutes} daq';

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: InkWell(
        borderRadius: BorderRadius.circular(12),
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  AvatarBubble(avatar: profile.avatar, color: color, size: 52),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(profile.name, style: textTheme.titleLarge),
                        Text('${profile.age} yosh · limit: $limit',
                            style: textTheme.bodyMedium?.copyWith(color: AppColors.textSoft)),
                      ],
                    ),
                  ),
                  const Icon(Icons.settings_rounded, color: AppColors.textSoft),
                ],
              ),
              const SizedBox(height: 12),
              Wrap(
                spacing: 16,
                runSpacing: 4,
                children: [
                  Text('Bugun: ${progress.minutesOn(now)} daqiqa', style: textTheme.titleMedium),
                  Text('⭐ ${progress.stars}', style: textTheme.titleMedium),
                  Text('🔥 ${progress.streak} kun', style: textTheme.titleMedium),
                ],
              ),
              if (scores.isNotEmpty) ...[
                const SizedBox(height: 8),
                for (final e in scores)
                  Text(
                    '${Subject.fromId(e.key)?.title ?? e.key}: ${e.value.correct}/${e.value.total}',
                    style: textTheme.bodyLarge,
                  ),
              ],
              const SizedBox(height: 12),
              Text('Haftalik (daqiqa)', style: textTheme.bodyMedium),
              const SizedBox(height: 6),
              _WeekBars(values: progress.weeklyMinutes(now), days: DateKeys.lastDays(now), color: color),
            ],
          ),
        ),
      ),
    );
  }
}

/// Oddiy 7 kunlik ustunli diagramma (qo'shimcha kutubxonasiz).
class _WeekBars extends StatelessWidget {
  const _WeekBars({required this.values, required this.days, required this.color});

  final List<int> values;
  final List<String> days;
  final Color color;

  @override
  Widget build(BuildContext context) {
    final maxValue = values.fold<int>(0, (m, v) => v > m ? v : m);
    return SizedBox(
      height: 90,
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          for (var i = 0; i < values.length; i++)
            Expanded(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 3),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Text('${values[i]}', style: const TextStyle(fontSize: 12)),
                    const SizedBox(height: 2),
                    Container(
                      height: maxValue == 0 ? 3 : 3 + 48 * values[i] / maxValue,
                      decoration: BoxDecoration(
                        color: i == values.length - 1 ? color : color.withAlpha(110),
                        borderRadius: BorderRadius.circular(6),
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(days[i].substring(8), style: const TextStyle(fontSize: 11)),
                  ],
                ),
              ),
            ),
        ],
      ),
    );
  }
}
