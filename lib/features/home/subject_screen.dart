import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../models/subject.dart';
import '../../theme/app_colors.dart';
import '../lesson/topics_screen.dart';
import '../profiles/profiles_controller.dart';

/// Fan ekrani: shu fan va yosh uchun o'quv dasturi bo'lsa — mavzular ro'yxati;
/// hali kiritilmagan fanlar uchun (keyingi kontent bosqichlari) qisqa xabar.
class SubjectScreen extends ConsumerWidget {
  const SubjectScreen({super.key, required this.subject});

  final Subject subject;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profile = ref.watch(activeProfileProvider);
    final suffix = profile?.ageGroup.suffix ?? '6';
    final curriculum = ref.watch(curriculumForProvider((subject.id, suffix)));
    return curriculum.when(
      loading: () => const Scaffold(body: Center(child: CircularProgressIndicator())),
      error: (e, _) => _Pending(subject: subject, age: profile?.age),
      data: (c) => c == null ? _Pending(subject: subject, age: profile?.age) : TopicsScreen(subject: subject, curriculum: c),
    );
  }
}

class _Pending extends StatelessWidget {
  const _Pending({required this.subject, this.age});

  final Subject subject;
  final int? age;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(subject.title), backgroundColor: subject.color.withAlpha(40)),
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
                Text('Tez orada!', style: Theme.of(context).textTheme.headlineMedium),
                const SizedBox(height: 8),
                Text(
                  "${subject.title} mashg‘ulotlari tayyorlanmoqda${age == null ? '' : ' — $age yosh uchun'}.",
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
