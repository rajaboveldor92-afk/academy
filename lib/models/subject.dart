import 'package:flutter/painting.dart';

import 'child_profile.dart';

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
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
  ),
  logic(
    id: 'logic',
    title: 'Mantiq',
    emoji: '🧩',
    spokenName: 'Mantiq',
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
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
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
    schoolSuffix: '6',
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
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
  ),
  russian(
    id: 'russian',
    title: 'Русский',
    emoji: '🇷🇺',
    spokenName: 'Русский язык',
    color: Color(0xFF3AA0D8),
    phase: 3,
    speechLang: 'ru',
    grades: [2, 3, 4, 5, 6, 7, 8],
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
  ),

  // ------------------------------------------------------------ Maktab fanlari (1–8-sinf)
  onatili(
    id: 'onatili',
    title: 'Ona tili',
    emoji: '📝',
    spokenName: 'Ona tili',
    color: Color(0xFF1FB57A),
    phase: 6,
    preschool: false,
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
  ),
  reading(
    id: 'reading',
    title: 'O‘qish',
    emoji: '📖',
    spokenName: 'O‘qish',
    color: Color(0xFFAB47BC),
    phase: 6,
    preschool: false,
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
  ),
  science(
    id: 'science',
    title: 'Tabiiy fan',
    emoji: '🌿',
    spokenName: 'Tabiiy fan',
    color: Color(0xFF43A047),
    phase: 6,
    preschool: false,
    grades: [1, 2, 3, 4, 5, 6],
  ),
  history(
    id: 'history',
    title: 'Tarix',
    emoji: '🏛️',
    spokenName: 'Tarix',
    color: Color(0xFF8D6E63),
    phase: 6,
    preschool: false,
    grades: [],
  ),
  technology(
    id: 'technology',
    title: 'Texnologiya',
    emoji: '🛠️',
    spokenName: 'Texnologiya',
    color: Color(0xFF8D6E63),
    phase: 6,
    preschool: false,
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
  ),
  informatics(
    id: 'informatics',
    title: 'Informatika',
    emoji: '💻',
    spokenName: 'Informatika',
    color: Color(0xFF546E7A),
    phase: 6,
    preschool: false,
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
  ),
  geography(
    id: 'geography',
    title: 'Geografiya',
    emoji: '🌍',
    spokenName: 'Geografiya',
    color: Color(0xFF26A69A),
    phase: 6,
    preschool: false,
    grades: [7, 8],
  ),
  biology(
    id: 'biology',
    title: 'Biologiya',
    emoji: '🧬',
    spokenName: 'Biologiya',
    color: Color(0xFF66BB6A),
    phase: 6,
    preschool: false,
    grades: [7, 8],
  ),
  physics(
    id: 'physics',
    title: 'Fizika',
    emoji: '⚛️',
    spokenName: 'Fizika',
    color: Color(0xFF5C6BC0),
    phase: 6,
    preschool: false,
    grades: [7, 8],
  ),
  chemistry(
    id: 'chemistry',
    title: 'Kimyo',
    emoji: '⚗️',
    spokenName: 'Kimyo',
    color: Color(0xFFEF6C00),
    phase: 6,
    preschool: false,
    grades: [7, 8],
  ),
  mental(
    id: 'mental',
    title: 'Mental arifmetika',
    emoji: '🧮',
    spokenName: 'Mental arifmetika',
    color: Color(0xFFFF7043),
    phase: 6,
    preschool: false,
    grades: [1, 2, 3, 4, 5, 6, 7, 8],
  );

  const Subject({
    required this.id,
    required this.title,
    required this.emoji,
    required this.spokenName,
    required this.color,
    required this.phase,
    this.speechLang = 'uz',
    this.preschool = true,
    this.grades = const [],
    this.schoolSuffix,
  });

  /// Maktabgacha yoshdagi bolalar (4 / 6 yosh dasturi) uchun.
  final bool preschool;

  /// Qaysi sinflarda o'qitiladi (maktab o'quvchisi uchun).
  final List<int> grades;

  /// Maktab o'quvchisi uchun alohida sinf dasturi o'rniga ishlatiladigan dastur (shaxmat — `6`).
  final String? schoolSuffix;

  /// Bola uchun ko'rinadimi (maktabgacha yoki sinfiga mos).
  bool isFor(ChildProfile p) => p.isSchool ? grades.contains(p.grade) : preschool;

  /// Bolaga mos dastur qo'shimchasi: `4`, `6` (maktabgacha) yoki `g3` (3-sinf).
  String suffixFor(ChildProfile p) {
    if (!p.isSchool) {
      if (this == Subject.math || this == Subject.logic) return p.age.clamp(3, 8).toString();
      return p.ageGroup.suffix;
    }
    return schoolSuffix ?? 'g${p.grade}';
  }

  /// Bolaga mos fanlar (ota-ona o'chirganlari ham kiradi — [ChildProfile.isSubjectEnabled] bilan filtrlanadi).
  static List<Subject> forProfile(ChildProfile p) => [for (final s in values) if (s.isFor(p)) s];

  /// Sinfga qarab nom: 5-sinfdan "O‘qish" → "Adabiyot".
  String titleForGrade(String lang, int grade) {
    if (this == Subject.reading && grade >= 5) {
      return switch (lang) { 'ru' => 'Литература', 'en' => 'Literature', _ => 'Adabiyot' };
    }
    return titleIn(lang);
  }

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
    'onatili': ('Native language', 'Родной язык'),
    'reading': ('Reading', 'Чтение'),
    'science': ('Science', 'Естествознание'),
    'history': ('History', 'История'),
    'technology': ('Technology', 'Технология'),
    'informatics': ('Computer science', 'Информатика'),
    'geography': ('Geography', 'География'),
    'biology': ('Biology', 'Биология'),
    'physics': ('Physics', 'Физика'),
    'chemistry': ('Chemistry', 'Химия'),
    'mental': ('Mental arithmetic', 'Ментальная арифметика'),
  };

  static Subject? fromId(String id) {
    for (final s in Subject.values) {
      if (s.id == id) return s;
    }
    return null;
  }
}
