import 'uz_numbers.dart';

/// Sonlarni so'z bilan yozish (ovoz uchun): o'zbek, ingliz va rus tillarida.
/// TTS raqamni noto'g'ri tilda o'qib yubormasligi uchun ko'rsatmalarda sonlar so'z bilan aytiladi.
class NumberWords {
  NumberWords._();

  static const List<String> _enOnes = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
  ];
  static const List<String> _enTens = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
  ];

  static const List<String> _ruOnes = [
    'ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
    'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
    'семнадцать', 'восемнадцать', 'девятнадцать',
  ];
  static const List<String> _ruTens = [
    '', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто',
  ];

  /// 0..100 (o'zbekcha — 0..1000).
  static String word(int n, String lang) {
    switch (lang) {
      case 'en':
        return _en(n);
      case 'ru':
        return _ru(n);
      default:
        return UzNumbers.word(n);
    }
  }

  static String _en(int n) {
    if (n < 0) return 'minus ${_en(-n)}';
    if (n < 20) return _enOnes[n];
    if (n < 100) {
      final o = n % 10;
      return o == 0 ? _enTens[n ~/ 10] : '${_enTens[n ~/ 10]}-${_enOnes[o]}';
    }
    if (n == 100) return 'one hundred';
    return '$n';
  }

  static String _ru(int n) {
    if (n < 0) return 'минус ${_ru(-n)}';
    if (n < 20) return _ruOnes[n];
    if (n < 100) {
      final o = n % 10;
      return o == 0 ? _ruTens[n ~/ 10] : '${_ruTens[n ~/ 10]} ${_ruOnes[o]}';
    }
    if (n == 100) return 'сто';
    return '$n';
  }

  /// Matndagi barcha sonlarni so'zga aylantiradi.
  static String spellDigits(String text, String lang) {
    if (lang == 'uz') return UzNumbers.spellDigits(text);
    return text.replaceAllMapped(RegExp(r'\d+'), (m) => word(int.parse(m.group(0)!), lang));
  }
}
