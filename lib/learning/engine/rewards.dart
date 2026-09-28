import '../../models/child_progress.dart';
import '../content/content_repository.dart';
import '../models/exercise.dart';

/// Medal: nima uchun beriladi va qanday qo'lga kiritiladi.
class MedalDef {
  const MedalDef(this.id, this.emoji, this.title, this.hint, this.earned);

  final String id;
  final String emoji;
  final Localized title;

  /// Bola/ota-ona uchun: medalni qanday olish mumkin.
  final Localized hint;
  final bool Function(ChildProgress p) earned;
}

/// Kolleksiya elementi (sovg'a qutisidan chiqadi).
class Collectible {
  const Collectible(this.emoji, this.name);

  final String emoji;
  final Localized name;
}

/// Fan kubogi darajasi.
enum CupTier { none, bronze, silver, gold }

Localized _l(String uz, String en, String ru) => Localized(uz: uz, en: en, ru: ru);

/// O'yinlashtirish: yulduzlar, medallar, kuboklar, sovg'a qutisi, o'suvchi bog'.
///
/// Muhim tamoyillar: real pul yo'q, tasodifiy "loot box" yo'q (sovg'alar doim bir xil
/// tartibda ochiladi), bolalar bir-biri bilan solishtirilmaydi — faqat o'z yutug'i.
class Rewards {
  Rewards._();

  static int _correct(ChildProgress p, String subject) => p.scoreOf(subject).correct;

  static final List<MedalDef> medals = [
    MedalDef('first_lesson', '🎈', _l('Birinchi dars', 'First lesson', 'Первый урок'),
        _l('Birinchi darsni tugat', 'Finish your first lesson', 'Закончи первый урок'), (p) => p.completedLessons >= 1),
    MedalDef('lessons_10', '🥉', _l('10 ta dars', '10 lessons', '10 уроков'),
        _l('10 ta darsni tugat', 'Finish 10 lessons', 'Закончи 10 уроков'), (p) => p.completedLessons >= 10),
    MedalDef('lessons_50', '🥈', _l('50 ta dars', '50 lessons', '50 уроков'),
        _l('50 ta darsni tugat', 'Finish 50 lessons', 'Закончи 50 уроков'), (p) => p.completedLessons >= 50),
    MedalDef('lessons_100', '🥇', _l('100 ta dars', '100 lessons', '100 уроков'),
        _l('100 ta darsni tugat', 'Finish 100 lessons', 'Закончи 100 уроков'), (p) => p.completedLessons >= 100),
    MedalDef('stars_100', '⭐', _l('100 yulduz', '100 stars', '100 звёзд'),
        _l('100 ta yulduz to‘pla', 'Collect 100 stars', 'Собери 100 звёзд'), (p) => p.stars >= 100),
    MedalDef('stars_500', '🌟', _l('500 yulduz', '500 stars', '500 звёзд'),
        _l('500 ta yulduz to‘pla', 'Collect 500 stars', 'Собери 500 звёзд'), (p) => p.stars >= 500),
    MedalDef('stars_1000', '💫', _l('1000 yulduz', '1000 stars', '1000 звёзд'),
        _l('1000 ta yulduz to‘pla', 'Collect 1000 stars', 'Собери 1000 звёзд'), (p) => p.stars >= 1000),
    MedalDef('streak_3', '🔥', _l('3 kun ketma-ket', '3 days in a row', '3 дня подряд'),
        _l('3 kun ketma-ket o‘yna', 'Play 3 days in a row', 'Играй 3 дня подряд'), (p) => p.streak >= 3),
    MedalDef('streak_7', '📅', _l('Bir hafta', 'One week', 'Неделя'),
        _l('7 kun ketma-ket o‘yna', 'Play 7 days in a row', 'Играй 7 дней подряд'), (p) => p.streak >= 7),
    MedalDef('streak_30', '🗓️', _l('Bir oy', 'One month', 'Месяц'),
        _l('30 kun ketma-ket o‘yna', 'Play 30 days in a row', 'Играй 30 дней подряд'), (p) => p.streak >= 30),
    MedalDef('daily_1', '▶️', _l('Bugungi dars', 'Today’s lesson', 'Урок дня'),
        _l('“Bugungi darsim”ni bajar', 'Complete “Today’s lesson”', 'Выполни «Урок дня»'), (p) => p.dailyLessons >= 1),
    MedalDef('daily_10', '🎯', _l('10 ta bugungi dars', '10 daily lessons', '10 уроков дня'),
        _l('“Bugungi darsim”ni 10 marta bajar', 'Complete “Today’s lesson” 10 times', 'Выполни «Урок дня» 10 раз'), (p) => p.dailyLessons >= 10),
    MedalDef('perfect', '💯', _l('Xatosiz dars', 'Perfect lesson', 'Урок без ошибок'),
        _l('Bir darsni birorta xatosiz tugat', 'Finish a lesson without a single mistake', 'Закончи урок без единой ошибки'),
        (p) => p.counter('perfect_lesson') >= 1),
    MedalDef('math', '🔢', _l('Matematik', 'Mathematician', 'Математик'),
        _l('Matematikada 100 ta to‘g‘ri javob', '100 correct answers in Maths', '100 правильных ответов по математике'),
        (p) => _correct(p, 'math') >= 100),
    MedalDef('reader', '📖', _l('O‘quvchi', 'Reader', 'Читатель'),
        _l('O‘zbek tilida 100 ta to‘g‘ri javob', '100 correct answers in Uzbek', '100 правильных ответов по узбекскому'),
        (p) => _correct(p, 'uzbek') >= 100),
    MedalDef('writer', '✏️', _l('Yozuvchi', 'Writer', 'Писатель'),
        _l('30 ta harf yoki shakl yoz', 'Write 30 letters or shapes', 'Напиши 30 букв или фигур'), (p) => _correct(p, 'writing') >= 30),
    MedalDef('logic', '🧩', _l('Mantiqchi', 'Logician', 'Логик'),
        _l('Mantiqda 100 ta to‘g‘ri javob', '100 correct answers in Logic', '100 правильных ответов по логике'),
        (p) => _correct(p, 'logic') >= 100),
    MedalDef('polyglot', '🌍', _l('Uch til', 'Three languages', 'Три языка'),
        _l('Ingliz, rus va “3 tilda”da 20 tadan to‘g‘ri javob', '20 correct answers each in English, Russian and “3 languages”',
            'По 20 правильных ответов в английском, русском и «На 3 языках»'),
        (p) => _correct(p, 'english') >= 20 && _correct(p, 'russian') >= 20 && _correct(p, 'trilingual') >= 20),
    MedalDef('memory', '🧠', _l('Xotira chempioni', 'Memory champion', 'Чемпион памяти'),
        _l('Xotira o‘yinlarida 50 ta to‘g‘ri javob', '50 correct answers in memory games', '50 правильных ответов в играх на память'),
        (p) => _correct(p, 'memory') >= 50),
    MedalDef('attention', '🔎', _l('Ziyrak', 'Sharp eyes', 'Внимательный'),
        _l('Diqqat o‘yinlarida 50 ta to‘g‘ri javob', '50 correct answers in attention games', '50 правильных ответов в играх на внимание'),
        (p) => _correct(p, 'attention') >= 50),
    MedalDef('chess_win', '♟️', _l('Shaxmat g‘olibi', 'Chess winner', 'Победитель в шахматах'),
        _l('AI raqibni yeng', 'Beat the computer', 'Победи компьютер'), (p) => p.counter('chess_win') >= 1),
    MedalDef('puzzle_master', '🖼️', _l('Puzzle ustasi', 'Puzzle master', 'Мастер пазлов'),
        _l('25 bo‘lakli puzzleni yoki 3 marta 9 bo‘lakli puzzleni yig‘', 'Solve a 25-piece puzzle or a 9-piece puzzle 3 times',
            'Собери пазл из 25 частей или 3 раза пазл из 9 частей'),
        (p) => p.counter('puzzle_25') >= 1 || p.counter('puzzle_9') >= 3),
    MedalDef('helper', '🏠', _l('Oila yordamchisi', 'Family helper', 'Помощник семьи'),
        _l('Ota-ona bilan 5 ta faoliyatni bajar', 'Do 5 activities with your parents', 'Выполни 5 занятий с родителями'),
        (p) => _correct(p, 'family') >= 5),
    MedalDef('friend', '🤝', _l('Yaxshi do‘st', 'Good friend', 'Хороший друг'),
        _l('Muloqot o‘yinlarida 30 ta to‘g‘ri javob', '30 correct answers in friendship games', '30 правильных ответов в играх об общении'),
        (p) => _correct(p, 'social') >= 30),
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

  static final List<Collectible> collection = [
    Collectible('🐣', _l('Jo‘jacha', 'Chick', 'Цыплёнок')),
    Collectible('🦄', _l('Yolqin', 'Unicorn', 'Единорог')),
    Collectible('🚀', _l('Raketa', 'Rocket', 'Ракета')),
    Collectible('🐬', _l('Delfin', 'Dolphin', 'Дельфин')),
    Collectible('🌈', _l('Kamalak', 'Rainbow', 'Радуга')),
    Collectible('🦁', _l('Sher', 'Lion', 'Лев')),
    Collectible('🎠', _l('Karusel', 'Carousel', 'Карусель')),
    Collectible('🐢', _l('Toshbaqa', 'Turtle', 'Черепаха')),
    Collectible('⛵', _l('Yelkanli qayiq', 'Sailboat', 'Парусник')),
    Collectible('🦋', _l('Kapalak', 'Butterfly', 'Бабочка')),
    Collectible('🐘', _l('Fil', 'Elephant', 'Слон')),
    Collectible('🎨', _l('Bo‘yoqlar', 'Paints', 'Краски')),
    Collectible('🦉', _l('Boyqush', 'Owl', 'Сова')),
    Collectible('🚂', _l('Poyezd', 'Train', 'Поезд')),
    Collectible('🐙', _l('Sakkizoyoq', 'Octopus', 'Осьминог')),
    Collectible('🌻', _l('Kungaboqar', 'Sunflower', 'Подсолнух')),
    Collectible('🦒', _l('Jirafa', 'Giraffe', 'Жираф')),
    Collectible('🎸', _l('Gitara', 'Guitar', 'Гитара')),
    Collectible('🐧', _l('Pingvin', 'Penguin', 'Пингвин')),
    Collectible('🏰', _l('Qasr', 'Castle', 'Замок')),
    Collectible('🦊', _l('Tulki', 'Fox', 'Лиса')),
    Collectible('🚁', _l('Vertolyot', 'Helicopter', 'Вертолёт')),
    Collectible('🐳', _l('Kit', 'Whale', 'Кит')),
    Collectible('🎻', _l('Skripka', 'Violin', 'Скрипка')),
    Collectible('🦓', _l('Zebra', 'Zebra', 'Зебра')),
    Collectible('🌋', _l('Vulqon', 'Volcano', 'Вулкан')),
    Collectible('🐼', _l('Panda', 'Panda', 'Панда')),
    Collectible('🛸', _l('Uchar likopcha', 'Flying saucer', 'Летающая тарелка')),
    Collectible('🦜', _l('To‘tiqush', 'Parrot', 'Попугай')),
    Collectible('🎡', _l('Charxpalak', 'Ferris wheel', 'Колесо обозрения')),
    Collectible('🐨', _l('Koala', 'Koala', 'Коала')),
    Collectible('🌍', _l('Yer shari', 'Planet Earth', 'Земной шар')),
    Collectible('🦚', _l('Tovus', 'Peacock', 'Павлин')),
    Collectible('🎺', _l('Karnay', 'Trumpet', 'Труба')),
    Collectible('🐅', _l('Yo‘lbars', 'Tiger', 'Тигр')),
    Collectible('👑', _l('Toj', 'Crown', 'Корона')),
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
  /// [suffix] — bolaga mos dastur (`4`, `6`, `g3` ...), qarang `Subject.suffixFor`.
  static CupTier cup(ChildProgress p, ContentRepository content, String subject, String suffix) {
    final c = content.curriculum(subject, suffix);
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
