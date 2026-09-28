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

  /// Maktab mashqlaridagi butun son so'z bilan: 37 → "o‘ttiz yetti".
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
    for (final scale in [(1000000000, 'milliard'), (1000000, 'million'), (1000, 'ming')]) {
      if (n < scale.$1) continue;
      final count = n ~/ scale.$1;
      final rest = n % scale.$1;
      final head = scale.$1 == 1000 && count == 1 ? 'ming' : '${word(count)} ${scale.$2}';
      return rest == 0 ? head : '$head ${word(rest)}';
    }
    throw StateError('Unreachable number: $n');
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
