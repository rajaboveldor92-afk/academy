import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../models/subject.dart';
import '../../theme/app_colors.dart';
import '../profiles/profiles_controller.dart';

/// Fan ekrani. Har bir fan o'z ishlab chiqish bosqichida (phase) to'liq
/// o'yinlar bilan almashtiriladi; hozircha bola uchun tushunarli
/// "tez orada" ekranini ko'rsatadi.
class SubjectScreen extends ConsumerWidget {
  const SubjectScreen({super.key, required this.subject});

  final Subject subject;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profile = ref.watch(activeProfileProvider);
    return Scaffold(
      appBar: AppBar(
        title: Text(subject.title),
        backgroundColor: subject.color.withAlpha(40),
      ),
      backgroundColor: AppColors.background,
      body: SafeArea(
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(subject.emoji, style: const TextStyle(fontSize: 110)),
                const SizedBox(height: 16),
                Text(
                  'Tez orada!',
                  style: Theme.of(context).textTheme.headlineMedium,
                ),
                const SizedBox(height: 8),
                Text(
                  "${subject.title} o'yinlari tayyorlanmoqda"
                  "${profile == null ? '' : ' — ${profile.age} yosh uchun'}.",
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.titleMedium,
                ),
                const SizedBox(height: 32),
                FilledButton.icon(
                  onPressed: () => Navigator.of(context).pop(),
                  icon: const Icon(Icons.home_rounded),
                  label: const Text('Orqaga'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
