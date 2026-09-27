import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// "🏠 Ota-ona bilan bajaramiz": ekrandan tashqari faoliyat kartasi.
/// Ota-ona bola bilan birga bajaradi va "Bajardik!" tugmasini bosadi — to'g'ri/noto'g'ri yo'q.
class ActivityExerciseView extends StatefulWidget {
  const ActivityExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<ActivityExerciseView> createState() => _ActivityExerciseViewState();
}

class _ActivityExerciseViewState extends State<ActivityExerciseView> {
  bool _done = false;

  ActivityTask get task => widget.exercise.activity!;

  void _finish() {
    if (_done) return;
    setState(() => _done = true);
    widget.callbacks.onSolved(0);
  }

  @override
  Widget build(BuildContext context) {
    final t = task;
    return Column(
      children: [
        Expanded(
          child: SingleChildScrollView(
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                color: const Color(0xFFFFFDF7),
                borderRadius: BorderRadius.circular(24),
                border: Border.all(color: const Color(0xFFEADFC8), width: 2),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Text(t.emoji, style: const TextStyle(fontSize: 54)),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(t.title, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: AppColors.text)),
                            const SizedBox(height: 4),
                            Text('⏱ ~${t.minutes} daqiqa', style: const TextStyle(fontSize: 14, color: AppColors.textSoft, fontWeight: FontWeight.w700)),
                          ],
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 14),
                  _heading('🧺 Kerak bo‘ladi'),
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: [
                      for (final m in t.materials)
                        Chip(
                          label: Text(m, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w700)),
                          backgroundColor: Colors.white,
                          side: const BorderSide(color: Color(0xFFE3E6F0)),
                        ),
                    ],
                  ),
                  const SizedBox(height: 14),
                  _heading('👣 Qanday bajaramiz'),
                  for (var i = 0; i < t.steps.length; i++)
                    Padding(
                      padding: const EdgeInsets.only(bottom: 8),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          CircleAvatar(
                            radius: 14,
                            backgroundColor: AppColors.primary,
                            child: Text('${i + 1}', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900)),
                          ),
                          const SizedBox(width: 10),
                          Expanded(child: Text(t.steps[i], style: const TextStyle(fontSize: 17, height: 1.35, color: AppColors.text))),
                        ],
                      ),
                    ),
                  const SizedBox(height: 8),
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(color: const Color(0xFFEFF4FF), borderRadius: BorderRadius.circular(16)),
                    child: Text('💡 ${t.benefit}', style: const TextStyle(fontSize: 15, height: 1.35, color: AppColors.text)),
                  ),
                ],
              ),
            ),
          ),
        ),
        const SizedBox(height: 12),
        SizedBox(
          width: double.infinity,
          height: 60,
          child: FilledButton.icon(
            key: const ValueKey('activity_done'),
            onPressed: _done ? null : _finish,
            style: FilledButton.styleFrom(
              backgroundColor: AppColors.success,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
            ),
            icon: const Icon(Icons.check_circle_rounded, size: 28),
            label: const Text('Bajardik!', style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
          ),
        ),
      ],
    );
  }

  Widget _heading(String text) => Padding(
        padding: const EdgeInsets.only(bottom: 8),
        child: Text(text, style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w900, color: AppColors.primary)),
      );
}
