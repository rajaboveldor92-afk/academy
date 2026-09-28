import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/tr.dart';
import '../../models/child_profile.dart';
import '../../models/subject.dart';
import '../../router/app_router.dart';
import '../../services/time_limit_service.dart';
import '../../widgets/profile_photo.dart';
import '../profiles/profiles_controller.dart';
import '../session/session_controller.dart';

/// Bitta bola uchun ota-ona sozlamalari: limit, qiyinlik, fanlar, profil.
class ChildSettingsScreen extends ConsumerWidget {
  const ChildSettingsScreen({super.key, required this.childId});

  final String childId;

  Future<void> _update(WidgetRef ref, ChildProfile updated) async {
    await ref.read(profilesProvider.notifier).updateProfile(updated);
    ref.read(sessionProvider.notifier).recheckLimit();
  }

  Future<void> _confirmDelete(BuildContext context, WidgetRef ref, ChildProfile profile) async {
    final t = Tr.of(context);
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text(t.deleteProfile),
        content: Text(t.deleteProfileConfirm(profile.name)),
        actions: [
          TextButton(onPressed: () => Navigator.of(ctx).pop(false), child: Text(t.cancel)),
          TextButton(onPressed: () => Navigator.of(ctx).pop(true), child: Text(t.delete)),
        ],
      ),
    );
    if (ok != true) return;
    await ref.read(profilesProvider.notifier).delete(profile.id);
    if (context.mounted) Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    ChildProfile? profile;
    for (final p in ref.watch(profilesProvider)) {
      if (p.id == childId) profile = p;
    }
    final current = profile;
    final t = Tr.of(context);
    if (current == null) {
      return Scaffold(appBar: AppBar(), body: Center(child: Text(t.profileNotFound)));
    }
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: Text(current.name)),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            ListTile(
              leading: ProfilePhoto(profile: current, size: 56, showBadge: false),
              title: Text('${current.displayFullName}, ${t.years(current.age)}'),
              subtitle: Text(t.editProfileHint),
              trailing: const Icon(Icons.edit_rounded),
              onTap: () => Navigator.of(context)
                  .pushNamed(AppRoutes.profileEditor, arguments: current),
            ),
            const Divider(),
            Text(t.childLanguage, style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                for (final code in ChildProfile.languages)
                  ChoiceChip(
                    key: Key('child_lang_$code'),
                    label: Text(t.langName(code)),
                    selected: current.language == code,
                    onSelected: (_) => _update(ref, current.copyWith(language: code)),
                  ),
              ],
            ),
            const SizedBox(height: 6),
            Text(t.childLanguageNote, style: textTheme.bodySmall),
            const SizedBox(height: 20),
            Text(t.dailyLimit, style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                for (final m in TimeLimitService.presets)
                  ChoiceChip(
                    label: Text(m == 0 ? t.unlimited : t.minutesShort(m)),
                    selected: current.dailyLimitMinutes == m,
                    onSelected: (_) => _update(ref, current.copyWith(dailyLimitMinutes: m)),
                  ),
              ],
            ),
            const SizedBox(height: 20),
            Text(t.difficulty, style: textTheme.titleMedium),
            const SizedBox(height: 8),
            SegmentedButton<int>(
              segments: [
                ButtonSegment(value: -1, label: Text(t.easier)),
                ButtonSegment(value: 0, label: Text(t.normal)),
                ButtonSegment(value: 1, label: Text(t.harder)),
              ],
              selected: {current.difficultyBias},
              onSelectionChanged: (s) => _update(ref, current.copyWith(difficultyBias: s.first)),
            ),
            const SizedBox(height: 20),
            Text(t.subjects, style: textTheme.titleMedium),
            for (final s in Subject.forProfile(current))
              SwitchListTile(
                secondary: Text(s.emoji, style: const TextStyle(fontSize: 26)),
                title: Text(s.titleIn(t.lang)),
                value: current.isSubjectEnabled(s.id),
                onChanged: (enabled) {
                  final disabled = List<String>.from(current.disabledSubjects);
                  if (enabled) {
                    disabled.remove(s.id);
                  } else if (!disabled.contains(s.id)) {
                    disabled.add(s.id);
                  }
                  _update(ref, current.copyWith(disabledSubjects: disabled));
                },
              ),
            const SizedBox(height: 24),
            OutlinedButton.icon(
              style: OutlinedButton.styleFrom(foregroundColor: Colors.red.shade400),
              onPressed: () => _confirmDelete(context, ref, current),
              icon: const Icon(Icons.delete_outline_rounded),
              label: Text(t.deleteProfile),
            ),
          ],
        ),
      ),
    );
  }
}
