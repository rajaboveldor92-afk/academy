import '../../models/child_progress.dart';
import '../content/content_repository.dart';

/// Medal: nima uchun beriladi va qanday qo'lga kiritiladi.
class MedalDef {
  const MedalDef(this.id, this.emoji, this.title, this.hint, this.earned);

  final String id;
  final String emoji;
  final String title;

  /// Bola/ota-ona uchun: medalni qanday olish mumkin.
  final String hint;
  final bool Function(ChildProgress p) earned;
}

/// Kolleksiya elementi (sovg'a qutisidan chiqadi).
class Collectible {
  const Collectible(this.emoji, this.name);

  final String emoji;
  final String name;
}

/// Fan kubogi darajasi.
enum CupTier { none, bronze, silver, gold }

/// O'yinlashtirish: yulduzlar, medallar, kuboklar, sovg'a qutisi, o'suvchi bog'.
///
/// Muhim tamoyillar: real pul yo'q, tasodifiy "loot box" yo'q (sovg'alar doim bir xil
/// tartibda ochiladi), bolalar bir-biri bilan solishtirilmaydi — faqat o'z yutug'i.
class Rewards {
  Rewards._();

  static int _correct(ChildProgress p, String subject) => p.scoreOf(subject).correct;

  static final List<MedalDef> medals = [
    MedalDef('first_lesson', '🎈', 'Birinchi dars', 'Birinchi darsni tugat', (p) => p.completedLessons >= 1),
    MedalDef('lessons_10', '🥉', '10 ta dars', '10 ta darsni tugat', (p) => p.completedLessons >= 10),
    MedalDef('lessons_50', '🥈', '50 ta dars', '50 ta darsni tugat', (p) => p.completedLessons >= 50),
    MedalDef('lessons_100', '🥇', '100 ta dars', '100 ta darsni tugat', (p) => p.completedLessons >= 100),
    MedalDef('stars_100', '⭐', '100 yulduz', '100 ta yulduz to‘pla', (p) => p.stars >= 100),
    MedalDef('stars_500', '🌟', '500 yulduz', '500 ta yulduz to‘pla', (p) => p.stars >= 500),
    MedalDef('stars_1000', '💫', '1000 yulduz', '1000 ta yulduz to‘pla', (p) => p.stars >= 1000),
    MedalDef('streak_3', '🔥', '3 kun ketma-ket', '3 kun ketma-ket o‘yna', (p) => p.streak >= 3),
    MedalDef('streak_7', '📅', 'Bir hafta', '7 kun ketma-ket o‘yna', (p) => p.streak >= 7),
    MedalDef('streak_30', '🗓️', 'Bir oy', '30 kun ketma-ket o‘yna', (p) => p.streak >= 30),
    MedalDef('daily_1', '▶️', 'Bugungi dars', '“Bugungi darsim”ni bajar', (p) => p.dailyLessons >= 1),
    MedalDef('daily_10', '🎯', '10 ta bugungi dars', '“Bugungi darsim”ni 10 marta bajar', (p) => p.dailyLessons >= 10),
    MedalDef('perfect', '💯', 'Xatosiz dars', 'Bir darsni birorta xatosiz tugat', (p) => p.counter('perfect_lesson') >= 1),
    MedalDef('math', '🔢', 'Matematik', 'Matematikada 100 ta to‘g‘ri javob', (p) => _correct(p, 'math') >= 100),
    MedalDef('reader', '📖', 'O‘quvchi', 'O‘zbek tilida 100 ta to‘g‘ri javob', (p) => _correct(p, 'uzbek') >= 100),
    MedalDef('writer', '✏️', 'Yozuvchi', '30 ta harf yoki shakl yoz', (p) => _correct(p, 'writing') >= 30),
    MedalDef('logic', '🧩', 'Mantiqchi', 'Mantiqda 100 ta to‘g‘ri javob', (p) => _correct(p, 'logic') >= 100),
    MedalDef('polyglot', '🌍', 'Uch til', 'Ingliz, rus va “3 tilda”da 20 tadan to‘g‘ri javob',
        (p) => _correct(p, 'english') >= 20 && _correct(p, 'russian') >= 20 && _correct(p, 'trilingual') >= 20),
    MedalDef('memory', '🧠', 'Xotira chempioni', 'Xotira o‘yinlarida 50 ta to‘g‘ri javob', (p) => _correct(p, 'memory') >= 50),
    MedalDef('attention', '🔎', 'Ziyrak', 'Diqqat o‘yinlarida 50 ta to‘g‘ri javob', (p) => _correct(p, 'attention') >= 50),
    MedalDef('chess_win', '♟️', 'Shaxmat g‘olibi', 'AI raqibni yeng', (p) => p.counter('chess_win') >= 1),
    MedalDef('puzzle_master', '🖼️', 'Puzzle ustasi', '25 bo‘lakli puzzleni yoki 3 marta 9 bo‘lakli puzzleni yig‘',
        (p) => p.counter('puzzle_25') >= 1 || p.counter('puzzle_9') >= 3),
    MedalDef('helper', '🏠', 'Oila yordamchisi', 'Ota-ona bilan 5 ta faoliyatni bajar', (p) => _correct(p, 'family') >= 5),
    MedalDef('friend', '🤝', 'Yaxshi do‘st', 'Muloqot o‘yinlarida 30 ta to‘g‘ri javob', (p) => _correct(p, 'social') >= 30),
  ];

  static MedalDef? medal(String id) {
    for (final m in medals) {
      if (m.id == id) return m;
    }
    return null;
  }

  /// Hali berilmagan, lekin endi qo'lga kiritilgan medallar.
  static List<MedalDef> newMedals(ChildProgress p) =>
      [for (final m in medals) if (!p.medals.contains(m.id) && m.earned(p)) m];

  // ------------------------------------------------------------ Sovg'a qutisi
  /// Har shuncha yulduz uchun bitta sovg'a qutisi.
  static const int starsPerGift = 30;

  static const List<Collectible> collection = [
    Collectible('🐣', 'Jo‘jacha'), Collectible('🦄', 'Yolqin'), Collectible('🚀', 'Raketa'), Collectible('🐬', 'Delfin'),
    Collectible('🌈', 'Kamalak'), Collectible('🦁', 'Sher'), Collectible('🎠', 'Karusel'), Collectible('🐢', 'Toshbaqa'),
    Collectible('⛵', 'Yelkanli qayiq'), Collectible('🦋', 'Kapalak'), Collectible('🐘', 'Fil'), Collectible('🎨', 'Bo‘yoqlar'),
    Collectible('🦉', 'Boyqush'), Collectible('🚂', 'Poyezd'), Collectible('🐙', 'Sakkizoyoq'), Collectible('🌻', 'Kungaboqar'),
    Collectible('🦒', 'Jirafa'), Collectible('🎸', 'Gitara'), Collectible('🐧', 'Pingvin'), Collectible('🏰', 'Qasr'),
    Collectible('🦊', 'Tulki'), Collectible('🚁', 'Vertolyot'), Collectible('🐳', 'Kit'), Collectible('🎻', 'Skripka'),
    Collectible('🦓', 'Zebra'), Collectible('🌋', 'Vulqon'), Collectible('🐼', 'Panda'), Collectible('🛸', 'Uchar likopcha'),
    Collectible('🦜', 'To‘tiqush'), Collectible('🎡', 'Charxpalak'), Collectible('🐨', 'Koala'), Collectible('🌍', 'Yer shari'),
    Collectible('🦚', 'Tovus'), Collectible('🎺', 'Karnay'), Collectible('🐅', 'Yo‘lbars'), Collectible('👑', 'Toj'),
  ];

  static int giftsEarned(ChildProgress p) => p.stars ~/ starsPerGift;

  static int giftsAvailable(ChildProgress p) {
    final n = giftsEarned(p) - p.giftsOpened;
    return n < 0 ? 0 : n;
  }

  /// Keyingi sovg'agacha qolgan yulduzlar.
  static int starsToNextGift(ChildProgress p) => starsPerGift - p.stars % starsPerGift;

  /// Ochiladigan navbatdagi sovg'a (tartib doim bir xil).
  static Collectible nextGift(ChildProgress p) => collection[p.giftsOpened % collection.length];

  static List<Collectible> collected(ChildProgress p) =>
      [for (var i = 0; i < p.giftsOpened; i++) collection[i % collection.length]];

  // ------------------------------------------------------------ O'suvchi bog'
  static const List<String> _plantTypes = ['🌷', '🌻', '🌳', '🌹', '🌼', '🍎', '🌸', '🌲'];

  /// Har 2 ta dars — yangi o'simlik; o'simlik darslar bilan o'sadi: 🌱 → 🌿 → gul/daraxt.
  static const int lessonsPerPlant = 2;
  static const int maxPlants = 24;

  static List<String> garden(ChildProgress p) {
    final n = p.completedLessons ~/ lessonsPerPlant;
    final count = n > maxPlants ? maxPlants : n;
    return [for (var i = 0; i < count; i++) _plant(p.completedLessons, i)];
  }

  static String _plant(int lessons, int i) {
    final growth = lessons - (i + 1) * lessonsPerPlant;
    if (growth < 2) return '🌱';
    if (growth < 5) return '🌿';
    return _plantTypes[i % _plantTypes.length];
  }

  // ------------------------------------------------------------ Kuboklar
  /// Fan bo'yicha kubok: bolaning yoshiga mos dasturdagi mavzular o'rtacha egallanishi.
  static CupTier cup(ChildProgress p, ContentRepository content, String subject, int age) {
    final c = content.curriculum(subject, age <= 5 ? '4' : '6');
    if (c == null || c.topics.isEmpty) return CupTier.none;
    var sum = 0;
    for (final t in c.topics) {
      sum += p.skillOf(t.id).mastery(t.maxLevel);
    }
    final avg = sum / c.topics.length;
    if (avg >= 85) return CupTier.gold;
    if (avg >= 55) return CupTier.silver;
    if (avg >= 25) return CupTier.bronze;
    return CupTier.none;
  }

  static String cupEmoji(CupTier t) => switch (t) {
        CupTier.gold => '🏆',
        CupTier.silver => '🥈',
        CupTier.bronze => '🥉',
        CupTier.none => '▫️',
      };
}
