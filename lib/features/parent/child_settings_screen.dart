import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../models/child_profile.dart';
import '../../models/subject.dart';
import '../../router/app_router.dart';
import '../../services/time_limit_service.dart';
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
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text("Profilni o'chirish"),
        content: Text("${profile.name} profili va uning barcha natijalari o'chiriladi. Davom etasizmi?"),
        actions: [
          TextButton(onPressed: () => Navigator.of(ctx).pop(false), child: const Text('Bekor')),
          TextButton(onPressed: () => Navigator.of(ctx).pop(true), child: const Text("O'chirish")),
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
    if (current == null) {
      return Scaffold(appBar: AppBar(), body: const Center(child: Text('Profil topilmadi')));
    }
    final textTheme = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: Text(current.name)),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            ListTile(
              leading: Text(current.avatar, style: const TextStyle(fontSize: 36)),
              title: Text('${current.name}, ${current.age} yosh'),
              subtitle: const Text('Ism, yosh va avatarni tahrirlash'),
              trailing: const Icon(Icons.edit_rounded),
              onTap: () => Navigator.of(context)
                  .pushNamed(AppRoutes.profileEditor, arguments: current),
            ),
            const Divider(),
            Text('Kunlik vaqt limiti', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                for (final m in TimeLimitService.presets)
                  ChoiceChip(
                    label: Text(m == 0 ? 'Cheklanmagan' : '$m daq'),
                    selected: current.dailyLimitMinutes == m,
                    onSelected: (_) => _update(ref, current.copyWith(dailyLimitMinutes: m)),
                  ),
              ],
            ),
            const SizedBox(height: 20),
            Text('Qiyinlik darajasi', style: textTheme.titleMedium),
            const SizedBox(height: 8),
            SegmentedButton<int>(
              segments: const [
                ButtonSegment(value: -1, label: Text('Osonroq')),
                ButtonSegment(value: 0, label: Text('Odatiy')),
                ButtonSegment(value: 1, label: Text('Qiyinroq')),
              ],
              selected: {current.difficultyBias},
              onSelectionChanged: (s) => _update(ref, current.copyWith(difficultyBias: s.first)),
            ),
            const SizedBox(height: 20),
            Text('Fanlar', style: textTheme.titleMedium),
            for (final s in Subject.values)
              SwitchListTile(
                secondary: Text(s.emoji, style: const TextStyle(fontSize: 26)),
                title: Text(s.title),
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
              label: const Text("Profilni o'chirish"),
            ),
          ],
        ),
      ),
    );
  }
}
