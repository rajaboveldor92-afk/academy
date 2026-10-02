import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'visual_view.dart';

/// Javob kartasi holati.
enum OptionState { idle, selected, correct, wrong, hinted, done }

/// Mashq vidjetlari uchun umumiy chaqiruvlar.
class ExerciseCallbacks {
  const ExerciseCallbacks({required this.onMistake, required this.onSolved, this.onSpeak, this.onAchievement});

  /// Noto'g'ri urinish (yumshoq fikr-mulohaza uchun). Argument — jami xatolar soni.
  final void Function(int mistakes) onMistake;

  /// Mashq tugadi. Argument — jami xatolar soni (0 bo'lsa birinchi urinishda to'g'ri).
  final void Function(int mistakes) onSolved;

  /// Matnni ovozda aytish.
  final void Function(String text)? onSpeak;

  /// Maxsus yutuq (medallar uchun): `chess_win`, `puzzle_big` ...
  final void Function(String id)? onAchievement;
}

/// Variant kartasi: rasm yoki matn.
class OptionCard extends StatelessWidget {
  const OptionCard({
    super.key,
    required this.option,
    this.state = OptionState.idle,
    this.onTap,
    this.compact = false,
    this.wrapText = false,
  });

  final ExerciseOption option;
  final OptionState state;
  final VoidCallback? onTap;
  final bool compact;
  final bool wrapText;

  Color get _border => switch (state) {
        OptionState.correct || OptionState.done => AppColors.success,
        OptionState.wrong => AppColors.gentle,
        OptionState.selected => AppColors.primary,
        OptionState.hinted => AppColors.star,
        OptionState.idle => const Color(0xFFE3E6F0),
      };

  Color get _fill => switch (state) {
        OptionState.correct || OptionState.done => const Color(0xFFE6F8EE),
        OptionState.wrong => const Color(0xFFFFF1E3),
        OptionState.selected => const Color(0xFFE8EEFF),
        OptionState.hinted => const Color(0xFFFFF8E1),
        OptionState.idle => Colors.white,
      };

  @override
  Widget build(BuildContext context) {
    final visual = option.visual;
    final text = option.text;
    Widget content;
    if (visual != null) {
      content = Padding(
        padding: EdgeInsets.all(compact ? 4 : 8),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Expanded(child: Center(child: VisualView(visual: visual))),
            if (text != null)
              FittedBox(
                fit: BoxFit.scaleDown,
                child: Text(
                  text,
                  maxLines: 1,
                  textAlign: TextAlign.center,
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800),
                ),
              ),
          ],
        ),
      );
    } else if (wrapText) {
      content = Center(child: Padding(padding: const EdgeInsets.all(8),
        child: Text(text ?? '', textAlign: TextAlign.center,
          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700))));
    } else {
      content = Center(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
          child: FittedBox(
            fit: BoxFit.scaleDown,
            child: Text(
              text ?? '',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: (text ?? '').length <= 3 ? 44 : 24,
                fontWeight: FontWeight.w900,
                color: AppColors.text,
              ),
            ),
          ),
        ),
      );
    }
    return AnimatedOpacity(
      duration: const Duration(milliseconds: 200),
      opacity: state == OptionState.wrong ? 0.55 : 1,
      child: Material(
        color: _fill,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(24),
          side: BorderSide(color: _border, width: state == OptionState.idle ? 2 : 4),
        ),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onTap,
          child: Stack(
            children: [
              Positioned.fill(child: content),
              if (state == OptionState.correct || state == OptionState.done)
                const Positioned(
                  right: 6,
                  top: 4,
                  child: Icon(Icons.check_circle_rounded, color: AppColors.success, size: 26),
                ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Yengil "chayqalish" animatsiyasi (noto'g'ri javobda, qo'rqitmasdan).
class Shake extends StatefulWidget {
  const Shake({super.key, required this.trigger, required this.child});

  /// Qiymat o'zgarganda chayqaladi.
  final int trigger;
  final Widget child;

  @override
  State<Shake> createState() => _ShakeState();
}

class _ShakeState extends State<Shake> with SingleTickerProviderStateMixin {
  late final AnimationController _c = AnimationController(vsync: this, duration: const Duration(milliseconds: 350));

  @override
  void didUpdateWidget(Shake oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.trigger != widget.trigger) _c.forward(from: 0);
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _c,
      builder: (context, child) {
        final t = _c.value;
        final dx = math.sin(t * math.pi * 6) * 8 * (1 - t);
        return Transform.translate(offset: Offset(dx, 0), child: child);
      },
      child: widget.child,
    );
  }
}
