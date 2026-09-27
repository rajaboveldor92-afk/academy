import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/tr.dart';
import '../../models/subject.dart';
import '../../theme/app_colors.dart';
import '../lesson/topics_screen.dart';
import '../profiles/profiles_controller.dart';

/// Fan ekrani: shu fan va yosh uchun o'quv dasturi — mavzular ro'yxati.
/// Barcha fanlarning ikkala yosh uchun dasturi bor (testlarda tekshiriladi); kontent fayli
/// o'qilmasa (masalan, buzilgan o'rnatish) — tushunarli xabar va orqaga tugmasi.
class SubjectScreen extends ConsumerWidget {
  const SubjectScreen({super.key, required this.subject});

  final Subject subject;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final profile = ref.watch(activeProfileProvider);
    final suffix = profile?.ageGroup.suffix ?? '6';
    final curriculum = ref.watch(curriculumForProvider((subject.id, suffix)));
    return LangScope(
      lang: profile?.language ?? 'uz',
      child: curriculum.when(
        loading: () => const Scaffold(body: Center(child: CircularProgressIndicator())),
        error: (e, _) => _Unavailable(subject: subject),
        data: (c) => c == null ? _Unavailable(subject: subject) : TopicsScreen(subject: subject, curriculum: c),
      ),
    );
  }
}

class _Unavailable extends StatelessWidget {
  const _Unavailable({required this.subject});

  final Subject subject;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(subject.titleIn(Tr.of(context).lang)), backgroundColor: subject.color.withAlpha(40)),
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
                Text(Tr.of(context).openFailed, style: Theme.of(context).textTheme.headlineMedium),
                const SizedBox(height: 8),
                Text(
                  Tr.of(context).subjectLoadFailed(subject.titleIn(Tr.of(context).lang)),
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.titleMedium,
                ),
                const SizedBox(height: 32),
                FilledButton.icon(
                  onPressed: () => Navigator.of(context).pop(),
                  icon: const Icon(Icons.home_rounded),
                  label: Text(Tr.of(context).back),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
