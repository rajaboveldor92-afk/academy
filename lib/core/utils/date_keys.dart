/// Kunlik statistika uchun sana kalitlari (`yyyy-MM-dd`, lokal vaqt).
class DateKeys {
  DateKeys._();

  static String dayKey(DateTime date) {
    final y = date.year.toString().padLeft(4, '0');
    final m = date.month.toString().padLeft(2, '0');
    final d = date.day.toString().padLeft(2, '0');
    return '$y-$m-$d';
  }

  static DateTime dateOnly(DateTime date) => DateTime(date.year, date.month, date.day);

  /// Ikki sana orasidagi kalendar kunlar farqi (soat mintaqasi o'zgarishlariga chidamli).
  static int daysBetween(DateTime from, DateTime to) {
    final a = DateTime.utc(from.year, from.month, from.day);
    final b = DateTime.utc(to.year, to.month, to.day);
    return b.difference(a).inDays;
  }

  /// Bugun bilan tugaydigan oxirgi [days] kunning kalitlari (eskidan yangiga).
  static List<String> lastDays(DateTime today, {int days = 7}) {
    final base = DateTime(today.year, today.month, today.day);
    return [
      for (var i = days - 1; i >= 0; i--) dayKey(DateTime(base.year, base.month, base.day - i)),
    ];
  }
}
