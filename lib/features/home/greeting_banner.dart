import 'package:flutter/material.dart';

import '../../models/child_profile.dart';
import '../../theme/app_colors.dart';
import '../../theme/profile_themes.dart';

/// Bosh sahifadagi samimiy salomlashuv:
///
///   Azamjon, xush kelibsiz!
///   Bugun birga o'rganamiz!
///
/// Faqat qisqa ism ishlatiladi. Yumshoq paydo bo'ladi (fade + slide).
class GreetingBanner extends StatelessWidget {
  const GreetingBanner({super.key, required this.profile});

  final ChildProfile profile;

  @override
  Widget build(BuildContext context) {
    final theme = ProfileThemes.of(profile.colorIndex);
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: 0, end: 1),
      duration: const Duration(milliseconds: 600),
      curve: Curves.easeOutCubic,
      builder: (context, t, child) => Opacity(
        opacity: t,
        child: Transform.translate(offset: Offset(0, 16 * (1 - t)), child: child),
      ),
      child: Container(
        key: const Key('greeting_banner'),
        width: double.infinity,
        margin: const EdgeInsets.fromLTRB(16, 0, 16, 8),
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(28),
          gradient: LinearGradient(colors: theme.gradient),
        ),
        child: Row(
          children: [
            Text(theme.emoji, style: const TextStyle(fontSize: 38)),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    profile.welcomeTitle,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.w900,
                      color: AppColors.text,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    profile.welcomeSubtitle,
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w700,
                      color: AppColors.text.withAlpha(190),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
