import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../core/utils/date_keys.dart';
import '../../l10n/tr.dart';
import '../../models/child_profile.dart';
import '../../models/child_progress.dart';
import '../../models/subject.dart';
import '../../router/app_router.dart';
import '../../theme/app_colors.dart';
import '../../widgets/profile_photo.dart';
import '../session/progress_controller.dart';
import '../profiles/profiles_controller.dart';
import 'settings_controller.dart';
import 'voice_check_dialog.dart';
import 'week_bars.dart';

/// Ota-ona bo'limi: bolalar statistikasi va umumiy sozlamalar.
class ParentHomeScreen extends ConsumerWidget {
  const ParentHomeScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profiles = ref.watch(profilesProvider);
    final settings = ref.watch(settingsProvider);
    final now = ref.read(clockProvider)();
    final textTheme = Theme.of(context).textTheme;
    final t = Tr.of(context);

    return Scaffold(
      appBar: AppBar(title: Text(t.parent)),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            Text(t.children, style: textTheme.titleLarge),
            const SizedBox(height: 8),
            for (final p in profiles)
              _ChildSummaryCard(
                profile: p,
                progress: ref.watch(childProgressProvider(p.id)),
                now: now,
                onTap: () => Navigator.of(context)
                    .pushNamed(AppRoutes.childSettings, arguments: p.id),
                onReport: () => Navigator.of(context)
                    .pushNamed(AppRoutes.childReport, arguments: p.id),
              ),
            const SizedBox(height: 8),
            OutlinedButton.icon(
              onPressed: () => Navigator.of(context).pushNamed(AppRoutes.profileEditor),
              icon: const Icon(Icons.person_add_alt_1_rounded),
              label: Text(t.addChild),
            ),
            const SizedBox(height: 24),
            Text(t.settings, style: textTheme.titleLarge),
            const SizedBox(height: 8),
            Card(
              child: Column(
                children: [
                  Padding(
                    padding: const EdgeInsets.fromLTRB(16, 12, 16, 4),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            const Icon(Icons.translate_rounded, color: AppColors.textSoft),
                            const SizedBox(width: 12),
                            Expanded(child: Text(t.parentLanguage, style: textTheme.titleMedium)),
                          ],
                        ),
                        const SizedBox(height: 8),
                        Wrap(
                          spacing: 8,
                          children: [
                            for (final code in Tr.languages)
                              ChoiceChip(
                                key: Key('app_lang_$code'),
                                label: Text(t.langName(code)),
                                selected: settings.appLanguage == code,
                                onSelected: (_) => ref.read(settingsProvider.notifier).setAppLanguage(code),
                              ),
                          ],
                        ),
                      ],
                    ),
                  ),
                  SwitchListTile(
                    title: Text(t.soundEffects),
                    value: settings.soundEnabled,
                    onChanged: (v) => ref.read(settingsProvider.notifier).setSound(v),
                  ),
                  SwitchListTile(
                    title: Text(t.voiceWords),
                    value: settings.voiceEnabled,
                    onChanged: (v) => ref.read(settingsProvider.notifier).setVoice(v),
                  ),
                  SwitchListTile(
                    title: Text(t.music),
                    value: settings.musicEnabled,
                    onChanged: (v) => ref.read(settingsProvider.notifier).setMusic(v),
                  ),
                  ListTile(
                    key: const Key('voice_check_button'),
                    leading: const Icon(Icons.record_voice_over_rounded),
                    title: Text(t.voiceCheck),
                    trailing: const Icon(Icons.chevron_right_rounded),
                    onTap: () => VoiceCheckDialog.show(context),
                  ),
                  ListTile(
                    leading: const Icon(Icons.password_rounded),
                    title: Text(t.changePinCode),
                    trailing: const Icon(Icons.chevron_right_rounded),
                    onTap: () => Navigator.of(context).pushNamed(AppRoutes.changePin),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),
            Text(
              t.privacyNote,
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
    required this.onReport,
  });

  final ChildProfile profile;
  final ChildProgress progress;
  final DateTime now;
  final VoidCallback onTap;
  final VoidCallback onReport;

  @override
  Widget build(BuildContext context) {
    final color = AppColors.profileColor(profile.colorIndex);
    final textTheme = Theme.of(context).textTheme;
    final scores = progress.subjectScores.entries.where((e) => e.value.total > 0).toList();
    final t = Tr.of(context);
    final limit = profile.dailyLimitMinutes == 0 ? t.unlimitedLower : t.minutesShort(profile.dailyLimitMinutes);

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
                  ProfilePhoto(profile: profile, size: 56, showBadge: false),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(profile.displayFullName, style: textTheme.titleLarge),
                        Text(t.ageAndLimit(profile.age, limit),
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
                  Text(t.todayMinutes(progress.minutesOn(now)), style: textTheme.titleMedium),
                  Text('⭐ ${progress.stars}', style: textTheme.titleMedium),
                  Text('🔥 ${t.days(progress.streak)}', style: textTheme.titleMedium),
                ],
              ),
              if (scores.isNotEmpty) ...[
                const SizedBox(height: 8),
                for (final e in scores)
                  _SubjectLine(
                    title: Subject.fromId(e.key)?.titleIn(t.lang) ?? e.key,
                    correct: e.value.correct,
                    total: e.value.total,
                    mastery: subjectMastery(progress, e.key),
                    color: Subject.fromId(e.key)?.color ?? color,
                  ),
              ],
              const SizedBox(height: 12),
              Text(t.weeklyMinutes, style: textTheme.bodyMedium),
              const SizedBox(height: 6),
              WeekBars(values: progress.weeklyMinutes(now), days: DateKeys.lastDays(now), color: color),
              const SizedBox(height: 12),
              Row(
                children: [
                  Expanded(
                    child: FilledButton.icon(
                      key: Key('report_button_${profile.id}'),
                      onPressed: onReport,
                      icon: const Icon(Icons.insights_rounded),
                      label: Text(t.detailedReport),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Expanded(
                    child: OutlinedButton.icon(
                      onPressed: onTap,
                      icon: const Icon(Icons.tune_rounded),
                      label: Text(t.settings),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Fan bo'yicha o'rtacha egallash darajasi (boshlangan mavzular bo'yicha), 0..100.
/// Faqat ota-ona panelida ko'rsatiladi.
int? subjectMastery(ChildProgress p, String subjectId) {
  final values = [
    for (final e in p.skills.entries)
      if (e.key.startsWith(subjectId) && e.value.started) e.value.mastery(3),
  ];
  if (values.isEmpty) return null;
  return (values.reduce((a, b) => a + b) / values.length).round();
}

class _SubjectLine extends StatelessWidget {
  const _SubjectLine({
    required this.title,
    required this.correct,
    required this.total,
    required this.mastery,
    required this.color,
  });

  final String title;
  final int correct;
  final int total;
  final int? mastery;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 3),
      child: Row(
        children: [
          SizedBox(width: 110, child: Text(title, style: const TextStyle(fontWeight: FontWeight.w700))),
          Expanded(
            child: ClipRRect(
              borderRadius: BorderRadius.circular(6),
              child: LinearProgressIndicator(
                value: (mastery ?? 0) / 100,
                minHeight: 10,
                color: color,
                backgroundColor: color.withAlpha(40),
              ),
            ),
          ),
          const SizedBox(width: 8),
          SizedBox(
            width: 92,
            child: Text(
              mastery == null ? '$correct/$total' : '$mastery% · $correct/$total',
              textAlign: TextAlign.right,
              style: const TextStyle(fontSize: 13),
            ),
          ),
        ],
      ),
    );
  }
}
