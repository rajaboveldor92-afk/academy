import 'package:flutter/painting.dart';

/// Har bir bola profili uchun alohida vizual uslub (ramka, fon, belgi).
/// `ChildProfile.colorIndex` shu ro'yxatdagi indeksni saqlaydi.
class ProfileTheme {
  const ProfileTheme({
    required this.id,
    required this.name,
    required this.emoji,
    required this.primary,
    required this.light,
    required this.gradient,
  });

  final String id;

  /// Ota-ona sozlamalarida ko'rinadigan nom.
  final String name;

  /// Kartadagi kichik belgi — bola profilini rasmsiz ham tanib oladi.
  final String emoji;

  /// Ramka, tugmalar va urg'u rangi.
  final Color primary;

  /// Karta foni uchun och rang.
  final Color light;

  /// Karta va salomlashuv fonidagi gradient.
  final List<Color> gradient;
}

class ProfileThemes {
  ProfileThemes._();

  static const List<ProfileTheme> all = [
    ProfileTheme(
      id: 'ocean',
      name: 'Dengiz',
      emoji: '🐳',
      primary: Color(0xFF2F80ED),
      light: Color(0xFFE3F0FF),
      gradient: [Color(0xFFBFE0FF), Color(0xFF7FB8FF)],
    ),
    ProfileTheme(
      id: 'sunny',
      name: 'Quyosh',
      emoji: '☀️',
      primary: Color(0xFFF2994A),
      light: Color(0xFFFFF1DC),
      gradient: [Color(0xFFFFE7A3), Color(0xFFFFB86B)],
    ),
    ProfileTheme(
      id: 'forest',
      name: "O‘rmon",
      emoji: '🌿',
      primary: Color(0xFF27AE60),
      light: Color(0xFFE2F7EA),
      gradient: [Color(0xFFC8F2D6), Color(0xFF7ED9A0)],
    ),
    ProfileTheme(
      id: 'berry',
      name: 'Rezavor',
      emoji: '🍓',
      primary: Color(0xFFE0457B),
      light: Color(0xFFFFE4EE),
      gradient: [Color(0xFFFFD1E1), Color(0xFFFF93B8)],
    ),
    ProfileTheme(
      id: 'space',
      name: 'Koinot',
      emoji: '🚀',
      primary: Color(0xFF6C5CE7),
      light: Color(0xFFECE9FF),
      gradient: [Color(0xFFD7D1FF), Color(0xFF9D8CFF)],
    ),
    ProfileTheme(
      id: 'candy',
      name: 'Shirinlik',
      emoji: '🍭',
      primary: Color(0xFF12A8A0),
      light: Color(0xFFDDF7F5),
      gradient: [Color(0xFFBDF1EC), Color(0xFF6FD6CD)],
    ),
  ];

  static ProfileTheme of(int index) => all[index.abs() % all.length];

  static int indexOfId(String id) {
    final i = all.indexWhere((t) => t.id == id);
    return i < 0 ? 0 : i;
  }
}
