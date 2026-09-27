import '../../core/utils/date_keys.dart';
import '../../core/utils/map_utils.dart';

/// Takrorlash navbati (spaced repetition) — bitta tushuncha bo'yicha.
///
/// Bola xato qilgan tushuncha qayta so'raladi:
/// * shu darsning o‘zida (boshqa ko‘rinishda) — [SpacedRepetition.maxRetriesPerLesson] tagacha;
/// * ertasi kuni (0-bosqich), keyin 3 kundan so'ng (1), keyin 7 kundan so'ng (2);
/// * 7 kunlik takrorlashda ham to'g'ri topsa — tushuncha o'rganilgan hisoblanadi.
///
/// Takrorlashda xato qilsa — yana ertasi kundan boshlanadi.
class ReviewItem {
  const ReviewItem({required this.topicId, required this.concept, required this.stage, required this.due});

  final String topicId;
  final String concept;

  /// 0 — ertaga, 1 — 3 kundan keyin, 2 — 7 kundan keyin.
  final int stage;
  final DateTime due;

  String get key => SpacedRepetition.keyOf(topicId, concept);

  bool isDue(DateTime now) => DateKeys.daysBetween(due, now) >= 0;

  Map<String, dynamic> toMap() => {'topicId': topicId, 'concept': concept, 'stage': stage, 'due': due.toIso8601String()};

  factory ReviewItem.fromMap(Map<String, dynamic> m) => ReviewItem(
        topicId: m['topicId'].toString(),
        concept: m['concept'].toString(),
        stage: MapUtils.asInt(m['stage']),
        due: MapUtils.asDate(m['due']) ?? DateTime.now(),
      );
}

class SpacedRepetition {
  SpacedRepetition._();

  /// Bosqichdan keyingi takrorlashgacha kunlar: xatodan so'ng 1, keyin 3, keyin 7.
  static const List<int> intervals = [1, 3, 7];

  /// Bir darsda shuncha xato qilingan mashq shu darsning o'zida qayta so'raladi.
  static const int maxRetriesPerLesson = 2;

  /// Navbat hajmi cheklangan (eng eskilari o'chadi).
  static const int maxItems = 200;

  static String keyOf(String topicId, String concept) => '$topicId|$concept';

  static DateTime _day(DateTime now, int plusDays) => DateTime(now.year, now.month, now.day + plusDays);

  /// Javobni hisobga olib navbatni yangilaydi (o'zgarmas nusxa qaytaradi).
  static Map<String, ReviewItem> record(
    Map<String, ReviewItem> queue, {
    required String topicId,
    required String concept,
    required bool firstTry,
    required DateTime now,
  }) {
    final key = keyOf(topicId, concept);
    final existing = queue[key];
    final updated = Map<String, ReviewItem>.from(queue);
    if (!firstTry) {
      // Xato: ertasi kundan qaytadan.
      updated[key] = ReviewItem(topicId: topicId, concept: concept, stage: 0, due: _day(now, intervals[0]));
    } else if (existing != null && existing.isDue(now)) {
      final next = existing.stage + 1;
      if (next >= intervals.length) {
        updated.remove(key); // o'rganildi
      } else {
        updated[key] = ReviewItem(topicId: topicId, concept: concept, stage: next, due: _day(now, intervals[next]));
      }
    }
    if (updated.length > maxItems) {
      final sorted = updated.values.toList()..sort((a, b) => a.due.compareTo(b.due));
      for (final r in sorted.take(updated.length - maxItems)) {
        updated.remove(r.key);
      }
    }
    return updated;
  }

  /// Bugun takrorlanishi kerak bo'lganlar (eng eskisi birinchi).
  static List<ReviewItem> due(Map<String, ReviewItem> queue, DateTime now) =>
      queue.values.where((r) => r.isDue(now)).toList()..sort((a, b) => a.due.compareTo(b.due));
}
