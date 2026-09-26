/// O'zbekcha sonlar — ovozli ko'rsatmalar uchun (TTS raqamni boshqa tilda
/// o'qib yubormasligi uchun sonlar so'z bilan yoziladi).
class UzNumbers {
  UzNumbers._();

  static const List<String> _ones = [
    'nol', 'bir', 'ikki', 'uch', 'to‘rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to‘qqiz',
  ];
  static const List<String> _tens = [
    '', 'o‘n', 'yigirma', 'o‘ttiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to‘qson',
  ];

  /// 0..1000 oralig'idagi son so'z bilan: 37 → "o‘ttiz yetti".
  static String word(int n) {
    if (n < 0) return 'minus ${word(-n)}';
    if (n < 10) return _ones[n];
    if (n < 100) {
      final t = _tens[n ~/ 10];
      final o = n % 10;
      return o == 0 ? t : '$t ${_ones[o]}';
    }
    if (n < 1000) {
      final h = n ~/ 100;
      final rest = n % 100;
      final head = h == 1 ? 'yuz' : '${_ones[h]} yuz';
      return rest == 0 ? head : '$head ${word(rest)}';
    }
    if (n == 1000) return 'ming';
    return n.toString();
  }

  /// Tartib son: 3 → "uchinchi".
  static String ordinal(int n) {
    final w = word(n);
    // Unli bilan tugasa "-nchi", undosh bilan tugasa "-inchi".
    final last = w.substring(w.length - 1);
    return const {'a', 'e', 'i', 'o', 'u'}.contains(last) ? '${w}nchi' : '${w}inchi';
  }

  /// Matndagi barcha raqamlarni so'zga aylantiradi (ovoz uchun).
  static String spellDigits(String text) =>
      text.replaceAllMapped(RegExp(r'\d+'), (m) => word(int.parse(m.group(0)!)));
}
