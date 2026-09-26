/// Kunlik vaqt limiti hisoblari (sof mantiq — test qilish oson).
class TimeLimitService {
  const TimeLimitService._();

  /// [limitMinutes] == 0 bo'lsa cheklov yo'q.
  static bool isExceeded({required int usedSeconds, required int limitMinutes}) {
    if (limitMinutes <= 0) return false;
    return usedSeconds >= limitMinutes * 60;
  }

  /// Qolgan soniyalar; cheklov yo'q bo'lsa `null`.
  static int? remainingSeconds({required int usedSeconds, required int limitMinutes}) {
    if (limitMinutes <= 0) return null;
    final left = limitMinutes * 60 - usedSeconds;
    return left < 0 ? 0 : left;
  }

  /// Limitga oz qolganda (2 daqiqa) ogohlantirish kerakmi.
  static bool isNearLimit({required int usedSeconds, required int limitMinutes}) {
    final left = remainingSeconds(usedSeconds: usedSeconds, limitMinutes: limitMinutes);
    return left != null && left > 0 && left <= 120;
  }

  /// Ota-ona sozlamalari uchun tanlov qiymatlari (daqiqa). 0 — cheklanmagan.
  static const List<int> presets = [0, 10, 15, 20, 30, 45, 60];
}
