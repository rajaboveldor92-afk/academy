import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../models/subject.dart';
import '../../learning/content/content_provider.dart';
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
    if (profile == null) return const Scaffold();
    final suffix = subject == Subject.math || subject == Subject.logic
        ? '${profile.age}'
        : profile.ageGroup.suffix;
    final curriculum = ref.watch(curriculumForProvider((subject.id, suffix)));
    return curriculum.when(
      loading: () =>
          const Scaffold(body: Center(child: CircularProgressIndicator())),
      error: (e, stack) {
        debugPrint('Kontent yuklanmadi (${subject.id}/$suffix): $e\n$stack');
        return _ContentError(
            subject: subject,
            onRetry: () {
              ref.invalidate(contentProvider);
              ref.invalidate(curriculumForProvider((subject.id, suffix)));
            });
      },
      data: (c) {
        if (c != null && c.topics.isNotEmpty) {
          return TopicsScreen(subject: subject, curriculum: c);
        }
        if (subject == Subject.math || subject == Subject.logic) {
          return _ContentError(
              subject: subject,
              onRetry: () {
                ref.invalidate(contentProvider);
                ref.invalidate(curriculumForProvider((subject.id, suffix)));
              });
        }
        return _Pending(subject: subject, age: profile.age);
      },
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
      appBar: AppBar(
          title: Text(subject.title),
          backgroundColor: subject.color.withAlpha(40)),
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
                Text('Tez orada!',
                    style: Theme.of(context).textTheme.headlineMedium),
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

/// A broken installed lesson is different from a subject still in development.
class _ContentError extends StatelessWidget {
  const _ContentError({required this.subject, required this.onRetry});
  final Subject subject;
  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: Text(subject.title)),
        body: Center(
            child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            const Icon(Icons.refresh_rounded, size: 64),
            const SizedBox(height: 16),
            const Text('Darslarni yuklab bo‘lmadi.',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            const Text(
                'Qayta urinib ko‘ring. Xato davom etsa, ilovani oxirgi versiyaga yangilang.',
                textAlign: TextAlign.center),
            const SizedBox(height: 20),
            FilledButton.icon(
                key: const Key('retry_content'),
                onPressed: onRetry,
                icon: const Icon(Icons.refresh),
                label: const Text('Qayta urinish')),
          ]),
        )),
      );
}
