import 'package:flutter/painting.dart';

/// Bosh sahifadagi yo'nalishlar. `id` JSON fayllar, statistika va
/// sozlamalarda kalit sifatida ishlatiladi — o'zgartirmang.
enum Subject {
  math(
    id: 'math',
    title: 'Matematika',
    emoji: '🔢',
    spokenName: 'Matematika',
    color: Color(0xFF4F8EF7),
    phase: 2,
  ),
  logic(
    id: 'logic',
    title: 'Mantiq',
    emoji: '🧩',
    spokenName: 'Mantiq',
    color: Color(0xFF9B6BFF),
    phase: 2,
  ),
  chess(
    id: 'chess',
    title: 'Shaxmat',
    emoji: '♟️',
    spokenName: 'Shaxmat',
    color: Color(0xFF5B6475),
    phase: 4,
  ),
  uzbek(
    id: 'uzbek',
    title: "O‘zbek tili",
    emoji: '🇺🇿',
    spokenName: "O‘zbek tili",
    color: Color(0xFF1FB57A),
    phase: 3,
  ),
  writing(
    id: 'writing',
    title: 'Yozish',
    emoji: '✏️',
    spokenName: 'Yozishni o‘rganaman',
    color: Color(0xFF7E57C2),
    phase: 3,
  ),
  english(
    id: 'english',
    title: 'English',
    emoji: '🇬🇧',
    spokenName: 'English',
    color: Color(0xFFE8505B),
    phase: 3,
    speechLang: 'en',
  ),
  russian(
    id: 'russian',
    title: 'Русский',
    emoji: '🇷🇺',
    spokenName: 'Русский язык',
    color: Color(0xFF3AA0D8),
    phase: 3,
    speechLang: 'ru',
  ),
  trilingual(
    id: 'trilingual',
    title: '3 tilda',
    emoji: '🍎',
    spokenName: "Uch tilda o‘rganamiz",
    color: Color(0xFFFF8A3D),
    phase: 3,
  ),
  memory(
    id: 'memory',
    title: 'Xotira',
    emoji: '🧠',
    spokenName: 'Xotira',
    color: Color(0xFFEC6AA8),
    phase: 5,
  ),
  attention(
    id: 'attention',
    title: 'Diqqat',
    emoji: '🎯',
    spokenName: 'Diqqat',
    color: Color(0xFFF2A516),
    phase: 5,
  ),
  puzzle(
    id: 'puzzle',
    title: 'Puzzle',
    emoji: '🧩',
    spokenName: 'Pazl',
    color: Color(0xFF2BB5A6),
    phase: 5,
  ),
  motor(
    id: 'motor',
    title: 'Motorika',
    emoji: '✋',
    spokenName: 'Barmoqlar mashqi',
    color: Color(0xFF8D6E63),
    phase: 5,
  ),
  social(
    id: 'social',
    title: 'Muloqot',
    emoji: '🤝',
    spokenName: 'Muloqot va do‘stlik',
    color: Color(0xFFE57373),
    phase: 5,
  ),
  family(
    id: 'family',
    title: 'Ota-ona bilan',
    emoji: '🏠',
    spokenName: 'Ota-ona bilan bajaramiz',
    color: Color(0xFF26A69A),
    phase: 5,
  );

  const Subject({
    required this.id,
    required this.title,
    required this.emoji,
    required this.spokenName,
    required this.color,
    required this.phase,
    this.speechLang = 'uz',
  });

  final String id;
  final String title;
  final String emoji;

  /// Karta bosilganda aytiladigan nom.
  final String spokenName;
  final Color color;

  /// Qaysi ishlab chiqish bosqichida to'liq ishga tushadi.
  final int phase;

  /// [spokenName] qaysi tilda aytiladi: `uz`, `en`, `ru`.
  final String speechLang;

  /// Fan nomi tanlangan tilda (o'zbekcha — [title]).
  String titleIn(String lang) {
    if (lang == 'uz') return title;
    final t = _titles[id]!;
    return lang == 'ru' ? t.$2 : t.$1;
  }

  /// Karta bosilganda aytiladigan nom va uning tili ([speechLang] chet tili fanlari uchun).
  (String text, String lang) spokenIn(String lang) {
    if (speechLang != 'uz') return (spokenName, speechLang);
    if (lang == 'uz') return (spokenName, 'uz');
    return (titleIn(lang), lang);
  }

  /// (inglizcha, ruscha) nomlar.
  static const Map<String, (String, String)> _titles = {
    'math': ('Maths', 'Математика'),
    'logic': ('Logic', 'Логика'),
    'chess': ('Chess', 'Шахматы'),
    'uzbek': ('Uzbek', 'Узбекский'),
    'writing': ('Writing', 'Письмо'),
    'english': ('English', 'Английский'),
    'russian': ('Russian', 'Русский'),
    'trilingual': ('3 languages', 'На 3 языках'),
    'memory': ('Memory', 'Память'),
    'attention': ('Attention', 'Внимание'),
    'puzzle': ('Puzzle', 'Пазлы'),
    'motor': ('Fine motor', 'Моторика'),
    'social': ('Friendship', 'Общение'),
    'family': ('With parents', 'С родителями'),
  };

  static Subject? fromId(String id) {
    for (final s in Subject.values) {
      if (s.id == id) return s;
    }
    return null;
  }
}
