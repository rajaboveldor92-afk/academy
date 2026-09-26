import 'package:flutter/material.dart';

import 'profile_themes.dart';

/// Ilova ranglari — yorqin, ammo ko'zni charchatmaydigan palitra.
class AppColors {
  AppColors._();

  static const Color primary = Color(0xFF4F7CF7);
  static const Color secondary = Color(0xFFFFB627);
  static const Color background = Color(0xFFFFF8EC);
  static const Color surface = Colors.white;
  static const Color text = Color(0xFF2A2D43);
  static const Color textSoft = Color(0xFF6B6F86);
  static const Color success = Color(0xFF2DBE72);
  static const Color gentle = Color(0xFFFF9F43); // xato o'rniga yumshoq rang
  static const Color star = Color(0xFFFFC83D);
  static const Color parent = Color(0xFF5B6475);

  /// Profil mavzusining asosiy rangi (`ChildProfile.colorIndex` → [ProfileThemes]).
  static Color profileColor(int index) => ProfileThemes.of(index).primary;
}
