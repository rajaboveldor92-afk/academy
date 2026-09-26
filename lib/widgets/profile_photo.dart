import 'dart:io';

import 'package:flutter/material.dart';

import '../models/child_profile.dart';
import '../theme/profile_themes.dart';

/// Bolaning katta yumaloq rasmi — mavzu rangidagi qalin ramka bilan.
///
/// Rasm bo'lmasa yoki fayl topilmasa, avatar emoji ko'rsatiladi.
/// Burchakdagi mavzu belgisi (🚀, ☀️) 4 yoshli bola uchun qo'shimcha "belgi" bo'ladi.
class ProfilePhoto extends StatelessWidget {
  const ProfilePhoto({
    super.key,
    required this.profile,
    required this.size,
    this.showBadge = true,
    this.glow = false,
  });

  final ChildProfile profile;
  final double size;
  final bool showBadge;

  /// Tanlanganda yumshoq yorug'lik.
  final bool glow;

  @override
  Widget build(BuildContext context) {
    final theme = ProfileThemes.of(profile.colorIndex);
    final ring = size * 0.055;
    final badgeSize = size * 0.3;

    return SizedBox(
      width: size,
      height: size,
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          AnimatedContainer(
            duration: const Duration(milliseconds: 250),
            width: size,
            height: size,
            padding: EdgeInsets.all(ring),
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [theme.primary, theme.gradient.last],
              ),
              boxShadow: [
                BoxShadow(
                  color: theme.primary.withAlpha(glow ? 150 : 60),
                  blurRadius: glow ? size * 0.28 : size * 0.1,
                  spreadRadius: glow ? size * 0.04 : 0,
                ),
              ],
            ),
            child: Container(
              padding: EdgeInsets.all(ring * 0.6),
              decoration: const BoxDecoration(shape: BoxShape.circle, color: Colors.white),
              child: ClipOval(child: _content(theme)),
            ),
          ),
          if (showBadge)
            Positioned(
              right: -size * 0.02,
              bottom: size * 0.02,
              child: Container(
                width: badgeSize,
                height: badgeSize,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  color: Colors.white,
                  shape: BoxShape.circle,
                  border: Border.all(color: theme.primary, width: ring * 0.6),
                ),
                child: Text(theme.emoji, style: TextStyle(fontSize: badgeSize * 0.52)),
              ),
            ),
        ],
      ),
    );
  }

  Widget _content(ProfileTheme theme) {
    final path = profile.photoPath;
    final emoji = Container(
      color: theme.light,
      alignment: Alignment.center,
      child: Text(profile.avatar, style: TextStyle(fontSize: size * 0.45)),
    );
    if (path == null || path.isEmpty) return emoji;
    final file = File(path);
    if (!file.existsSync()) return emoji;
    // Rasm faqat kerakli o'lchamda dekodlanadi — xotira tejaladi.
    final cache = (size * 2.5).round();
    return Image.file(
      file,
      fit: BoxFit.cover,
      width: size,
      height: size,
      cacheWidth: cache,
      gaplessPlayback: true,
      errorBuilder: (_, __, ___) => emoji,
    );
  }
}
