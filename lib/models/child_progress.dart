import '../core/utils/date_keys.dart';
import '../core/utils/map_utils.dart';
import '../learning/engine/mastery.dart';
import '../learning/engine/spaced_repetition.dart';

/// Bitta fan bo'yicha to'plangan natija.
class SubjectScore {
  const SubjectScore({this.correct = 0, this.total = 0});

  final int correct;
  final int total;

  double get ratio => total == 0 ? 0 : correct / total;

  SubjectScore add({required bool isCorrect}) =>
      SubjectScore(correct: correct + (isCorrect ? 1 : 0), total: total + 1);

  Map<String, dynamic> toMap() => {'correct': correct, 'total': total};

  factory SubjectScore.fromMap(Map<String, dynamic> map) => SubjectScore(
        correct: MapUtils.asInt(map['correct']),
        total: MapUtils.asInt(map['total']),
      );
}

/// Bolaning umumiy statistikasi (spetsifikatsiyaning 30-bandi).
///
/// Model o'zgarmas (immutable): har bir amal yangi nusxa qaytaradi.
class ChildProgress {
  const ChildProgress({
    required this.childId,
    this.completedLessons = 0,
    this.correctAnswers = 0,
    this.wrongAnswers = 0,
    this.stars = 0,
    this.medals = const <String>[],
    this.currentLevels = const <String, int>{},
    this.subjectScores = const <String, SubjectScore>{},
    this.dailySeconds = const <String, int>{},
    this.dailyCorrect = const <String, int>{},
    this.lastPlayed,
    this.streak = 0,
    this.skills = const <String, SkillStat>{},
    this.recent = const <String, List<int>>{},
    this.reviews = const <String, ReviewItem>{},
    this.dailyLessons = 0,
    this.lastDailyLesson,
    this.giftsOpened = 0,
    this.counters = const <String, int>{},
  });

  factory ChildProgress.empty(String childId) => ChildProgress(childId: childId);

  final String childId;
  final int completedLessons;
  final int correctAnswers;
  final int wrongAnswers;
  final int stars;
  final List<String> medals;

  /// Fan → joriy daraja (1 dan boshlanadi).
  final Map<String, int> currentLevels;
  final Map<String, SubjectScore> subjectScores;

  /// `yyyy-MM-dd` → shu kuni o'ynalgan soniyalar.
  final Map<String, int> dailySeconds;

  /// `yyyy-MM-dd` → shu kuni berilgan to'g'ri javoblar.
  final Map<String, int> dailyCorrect;
  final DateTime? lastPlayed;

  /// Ketma-ket o'ynagan kunlar soni.
  final int streak;

  /// Mavzu (ko'nikma) bo'yicha daraja va egallash holati: `topicId → SkillStat`.
  final Map<String, SkillStat> skills;

  /// Oxirgi ko'rilgan savollar imzolari (takrorlanmaslik uchun): `topicId → hash[]`.
  final Map<String, List<int>> recent;

  /// Takrorlash navbati (spaced repetition): `topicId|concept → ReviewItem`.
  final Map<String, ReviewItem> reviews;

  /// "Bugungi darsim" necha marta bajarilgan va oxirgi marta qachon.
  final int dailyLessons;
  final DateTime? lastDailyLesson;

  /// Ochilgan sovg'a qutilari soni (kolleksiya shu tartibda to'ladi).
  final int giftsOpened;

  /// Yutuqlar uchun hisoblagichlar: `chess_win`, `puzzle_25`, `perfect_lesson` ...
  final Map<String, int> counters;

  static const int recentLimit = 60;

  int counter(String id) => counters[id] ?? 0;

  bool dailyDoneOn(DateTime day) => lastDailyLesson != null && DateKeys.daysBetween(lastDailyLesson!, day) == 0;

  ChildProgress withReviews(Map<String, ReviewItem> value) => _copy(reviews: value);

  ChildProgress addCounter(String id, [int by = 1]) {
    final updated = Map<String, int>.from(counters);
    updated[id] = (updated[id] ?? 0) + by;
    return _copy(counters: updated);
  }

  ChildProgress completeDaily(DateTime now) => _copy(dailyLessons: dailyLessons + 1, lastDailyLesson: now);

  ChildProgress openGift() => _copy(giftsOpened: giftsOpened + 1);

  SkillStat skillOf(String topicId) => skills[topicId] ?? const SkillStat();

  List<int> recentOf(String topicId) => recent[topicId] ?? const [];

  ChildProgress withSkill(String topicId, SkillStat stat) {
    final updated = Map<String, SkillStat>.from(skills);
    updated[topicId] = stat;
    return _copy(skills: updated);
  }

  ChildProgress addRecent(String topicId, Iterable<int> hashes) {
    final list = [...recentOf(topicId), ...hashes];
    final trimmed = list.length > recentLimit ? list.sublist(list.length - recentLimit) : list;
    final updated = Map<String, List<int>>.from(recent);
    updated[topicId] = trimmed;
    return _copy(recent: updated);
  }

  int levelOf(String subjectId) => currentLevels[subjectId] ?? 1;

  SubjectScore scoreOf(String subjectId) => subjectScores[subjectId] ?? const SubjectScore();

  int secondsOn(DateTime day) => dailySeconds[DateKeys.dayKey(day)] ?? 0;

  int minutesOn(DateTime day) => secondsOn(day) ~/ 60;

  /// Oxirgi 7 kunlik daqiqalar (eskidan yangiga) — haftalik progress.
  List<int> weeklyMinutes(DateTime today) =>
      DateKeys.lastDays(today).map((k) => (dailySeconds[k] ?? 0) ~/ 60).toList();

  List<int> weeklyCorrect(DateTime today) =>
      DateKeys.lastDays(today).map((k) => dailyCorrect[k] ?? 0).toList();

  /// Bola o'ynashni boshlaganda chaqiriladi: ketma-ket kunlar (streak)ni yangilaydi.
  ChildProgress registerVisit(DateTime now) {
    final last = lastPlayed;
    int newStreak;
    if (last == null) {
      newStreak = 1;
    } else {
      final diff = DateKeys.daysBetween(last, now);
      if (diff <= 0) {
        newStreak = streak == 0 ? 1 : streak;
      } else if (diff == 1) {
        newStreak = streak + 1;
      } else {
        newStreak = 1;
      }
    }
    return _copy(lastPlayed: now, streak: newStreak);
  }

  ChildProgress addSeconds(DateTime now, int seconds) {
    if (seconds <= 0) return this;
    final key = DateKeys.dayKey(now);
    final updated = Map<String, int>.from(dailySeconds);
    updated[key] = (updated[key] ?? 0) + seconds;
    _pruneOldDays(updated, now);
    return _copy(dailySeconds: updated, lastPlayed: now);
  }

  /// Bitta javobni qayd etadi. [rewardStars] — to'g'ri javob uchun beriladigan yulduzlar.
  ChildProgress recordAnswer({
    required String subjectId,
    required bool isCorrect,
    required DateTime now,
    int rewardStars = 0,
  }) {
    final scores = Map<String, SubjectScore>.from(subjectScores);
    scores[subjectId] = scoreOf(subjectId).add(isCorrect: isCorrect);
    final daily = Map<String, int>.from(dailyCorrect);
    if (isCorrect) {
      final key = DateKeys.dayKey(now);
      daily[key] = (daily[key] ?? 0) + 1;
      _pruneOldDays(daily, now);
    }
    return _copy(
      correctAnswers: correctAnswers + (isCorrect ? 1 : 0),
      wrongAnswers: wrongAnswers + (isCorrect ? 0 : 1),
      stars: stars + (isCorrect && rewardStars > 0 ? rewardStars : 0),
      subjectScores: scores,
      dailyCorrect: daily,
      lastPlayed: now,
    );
  }

  ChildProgress addStars(int amount) => _copy(stars: (stars + amount) < 0 ? 0 : stars + amount);

  ChildProgress completeLesson() => _copy(completedLessons: completedLessons + 1);

  ChildProgress setLevel(String subjectId, int level) {
    final levels = Map<String, int>.from(currentLevels);
    levels[subjectId] = level < 1 ? 1 : level;
    return _copy(currentLevels: levels);
  }

  ChildProgress addMedal(String medalId) {
    if (medals.contains(medalId)) return this;
    return _copy(medals: [...medals, medalId]);
  }

  /// 60 kundan eski kunlik yozuvlarni o'chiradi — ma'lumotlar bazasi o'smasligi uchun.
  static void _pruneOldDays(Map<String, int> map, DateTime now) {
    if (map.length <= 60) return;
    final keep = DateKeys.lastDays(now, days: 60).toSet();
    map.removeWhere((key, _) => !keep.contains(key));
  }

  ChildProgress _copy({
    int? completedLessons,
    int? correctAnswers,
    int? wrongAnswers,
    int? stars,
    List<String>? medals,
    Map<String, int>? currentLevels,
    Map<String, SubjectScore>? subjectScores,
    Map<String, int>? dailySeconds,
    Map<String, int>? dailyCorrect,
    DateTime? lastPlayed,
    int? streak,
    Map<String, SkillStat>? skills,
    Map<String, List<int>>? recent,
    Map<String, ReviewItem>? reviews,
    int? dailyLessons,
    DateTime? lastDailyLesson,
    int? giftsOpened,
    Map<String, int>? counters,
  }) {
    return ChildProgress(
      childId: childId,
      completedLessons: completedLessons ?? this.completedLessons,
      correctAnswers: correctAnswers ?? this.correctAnswers,
      wrongAnswers: wrongAnswers ?? this.wrongAnswers,
      stars: stars ?? this.stars,
      medals: medals ?? this.medals,
      currentLevels: currentLevels ?? this.currentLevels,
      subjectScores: subjectScores ?? this.subjectScores,
      dailySeconds: dailySeconds ?? this.dailySeconds,
      dailyCorrect: dailyCorrect ?? this.dailyCorrect,
      lastPlayed: lastPlayed ?? this.lastPlayed,
      streak: streak ?? this.streak,
      skills: skills ?? this.skills,
      recent: recent ?? this.recent,
      reviews: reviews ?? this.reviews,
      dailyLessons: dailyLessons ?? this.dailyLessons,
      lastDailyLesson: lastDailyLesson ?? this.lastDailyLesson,
      giftsOpened: giftsOpened ?? this.giftsOpened,
      counters: counters ?? this.counters,
    );
  }

  Map<String, dynamic> toMap() => {
        'childId': childId,
        'completedLessons': completedLessons,
        'correctAnswers': correctAnswers,
        'wrongAnswers': wrongAnswers,
        'stars': stars,
        'medals': List<String>.from(medals),
        'currentLevels': Map<String, int>.from(currentLevels),
        'subjectScores': subjectScores.map((k, v) => MapEntry(k, v.toMap())),
        'dailySeconds': Map<String, int>.from(dailySeconds),
        'dailyCorrect': Map<String, int>.from(dailyCorrect),
        'lastPlayed': lastPlayed?.toIso8601String(),
        'streak': streak,
        'skills': skills.map((k, v) => MapEntry(k, v.toMap())),
        'recent': recent.map((k, v) => MapEntry(k, List<int>.from(v))),
        'reviews': reviews.map((k, v) => MapEntry(k, v.toMap())),
        'dailyLessons': dailyLessons,
        'lastDailyLesson': lastDailyLesson?.toIso8601String(),
        'giftsOpened': giftsOpened,
        'counters': Map<String, int>.from(counters),
      };

  factory ChildProgress.fromMap(Map<String, dynamic> map) {
    final rawScores = MapUtils.asStringMap(map['subjectScores']);
    return ChildProgress(
      childId: map['childId'].toString(),
      completedLessons: MapUtils.asInt(map['completedLessons']),
      correctAnswers: MapUtils.asInt(map['correctAnswers']),
      wrongAnswers: MapUtils.asInt(map['wrongAnswers']),
      stars: MapUtils.asInt(map['stars']),
      medals: MapUtils.asStringList(map['medals']),
      currentLevels: MapUtils.asIntMap(map['currentLevels']),
      subjectScores: rawScores.map(
        (k, v) => MapEntry(k, SubjectScore.fromMap(MapUtils.asStringMap(v))),
      ),
      dailySeconds: MapUtils.asIntMap(map['dailySeconds']),
      dailyCorrect: MapUtils.asIntMap(map['dailyCorrect']),
      lastPlayed: MapUtils.asDate(map['lastPlayed']),
      streak: MapUtils.asInt(map['streak']),
      skills: MapUtils.asStringMap(map['skills']).map(
        (k, v) => MapEntry(k, SkillStat.fromMap(MapUtils.asStringMap(v))),
      ),
      recent: MapUtils.asStringMap(map['recent']).map(
        (k, v) => MapEntry(k, (v is List ? v : const []).whereType<num>().map((e) => e.toInt()).toList()),
      ),
      reviews: MapUtils.asStringMap(map['reviews']).map(
        (k, v) => MapEntry(k, ReviewItem.fromMap(MapUtils.asStringMap(v))),
      ),
      dailyLessons: MapUtils.asInt(map['dailyLessons']),
      lastDailyLesson: MapUtils.asDate(map['lastDailyLesson']),
      giftsOpened: MapUtils.asInt(map['giftsOpened']),
      counters: MapUtils.asIntMap(map['counters']),
    );
  }
}
