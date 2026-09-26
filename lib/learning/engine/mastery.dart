import '../../core/utils/map_utils.dart';

/// Adaptiv qaror: keyingi darsda daraja qanday bo'ladi.
enum LevelDecision { up, stay, down }

/// Bitta ko'nikma (mavzu) bo'yicha holat.
class SkillStat {
  const SkillStat({
    this.level = 1,
    this.ema = 0,
    this.lessons = 0,
    this.attempts = 0,
    this.firstTryCorrect = 0,
    this.lastPracticed,
    this.lastAccuracy = 0,
  });

  /// Joriy daraja (1..maxLevel).
  final int level;

  /// Joriy darajadagi natijalarning silliqlangan o'rtachasi (0..100).
  final double ema;
  final int lessons;
  final int attempts;
  final int firstTryCorrect;
  final DateTime? lastPracticed;

  /// Oxirgi dars natijasi (0..100).
  final double lastAccuracy;

  bool get started => lessons > 0;

  /// Ko'nikmani egallash darajasi 0..100% (faqat ota-ona panelida ko'rsatiladi).
  /// Har bir daraja umumiy shkalaning teng ulushi; joriy darajadagi natija
  /// shu ulushning qanchasi bajarilganini bildiradi.
  int mastery(int maxLevel) {
    if (!started) return 0;
    final share = 100 / maxLevel;
    final value = (level - 1) * share + share * (ema / 100);
    return value.round().clamp(0, 100).toInt();
  }

  Map<String, dynamic> toMap() => {
        'level': level,
        'ema': ema,
        'lessons': lessons,
        'attempts': attempts,
        'firstTryCorrect': firstTryCorrect,
        'lastPracticed': lastPracticed?.toIso8601String(),
        'lastAccuracy': lastAccuracy,
      };

  factory SkillStat.fromMap(Map<String, dynamic> m) => SkillStat(
        level: MapUtils.asInt(m['level'], 1),
        ema: (m['ema'] is num) ? (m['ema'] as num).toDouble() : 0,
        lessons: MapUtils.asInt(m['lessons']),
        attempts: MapUtils.asInt(m['attempts']),
        firstTryCorrect: MapUtils.asInt(m['firstTryCorrect']),
        lastPracticed: MapUtils.asDate(m['lastPracticed']),
        lastAccuracy: (m['lastAccuracy'] is num) ? (m['lastAccuracy'] as num).toDouble() : 0,
      );
}

/// Dars natijasi bo'yicha adaptiv qoida (spetsifikatsiya 25-band):
/// * ≥85% — keyingi murakkablik;
/// * 60–84% — shu darajada yangi variantlar;
/// * <60% — osonroq daraja va ko'rsatma.
class AdaptiveRule {
  AdaptiveRule._();

  static const double upThreshold = 85;
  static const double stayThreshold = 60;

  static LevelDecision decide(double accuracy) {
    if (accuracy >= upThreshold) return LevelDecision.up;
    if (accuracy >= stayThreshold) return LevelDecision.stay;
    return LevelDecision.down;
  }

  static ({SkillStat stat, LevelDecision decision}) apply(
    SkillStat s, {
    required int correctFirstTry,
    required int total,
    required int maxLevel,
    required DateTime now,
  }) {
    final accuracy = total == 0 ? 0.0 : correctFirstTry * 100 / total;
    final decision = decide(accuracy);
    final smoothed = s.started && s.ema > 0 ? s.ema * 0.5 + accuracy * 0.5 : accuracy;
    var level = s.level;
    var ema = smoothed;
    switch (decision) {
      case LevelDecision.up:
        if (level < maxLevel) {
          level++;
          ema = 0; // yangi darajada noldan boshlanadi
        } else {
          ema = smoothed;
        }
      case LevelDecision.down:
        if (level > 1) {
          level--;
          ema = 70; // oldingi daraja allaqachon o'rganilgan deb hisoblanadi
        }
      case LevelDecision.stay:
        break;
    }
    return (
      stat: SkillStat(
        level: level,
        ema: ema,
        lessons: s.lessons + 1,
        attempts: s.attempts + total,
        firstTryCorrect: s.firstTryCorrect + correctFirstTry,
        lastPracticed: now,
        lastAccuracy: accuracy,
      ),
      decision: decision,
    );
  }
}
