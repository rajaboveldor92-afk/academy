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

  /// 0..999 999 (o'zbekcha — milliardgacha).
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
    if (n < 1000) {
      final r = n % 100;
      return '${_enOnes[n ~/ 100]} hundred${r == 0 ? '' : ' and ${_en(r)}'}';
    }
    if (n < 1000000) {
      final r = n % 1000;
      return '${_en(n ~/ 1000)} thousand${r == 0 ? '' : r < 100 ? ' and ${_en(r)}' : ' ${_en(r)}'}';
    }
    return '$n';
  }

  static const List<String> _ruHundreds = [
    '', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот',
  ];

  static String _ru(int n) {
    if (n < 0) return 'минус ${_ru(-n)}';
    if (n < 20) return _ruOnes[n];
    if (n < 100) {
      final o = n % 10;
      return o == 0 ? _ruTens[n ~/ 10] : '${_ruTens[n ~/ 10]} ${_ruOnes[o]}';
    }
    if (n < 1000) {
      final r = n % 100;
      return r == 0 ? _ruHundreds[n ~/ 100] : '${_ruHundreds[n ~/ 100]} ${_ru(r)}';
    }
    if (n < 1000000) {
      final k = n ~/ 1000, r = n % 1000;
      // "тысяча" — ayol jinsi: одна тысяча, две тысячи, пять тысяч.
      final words = _ru(k).replaceAll(RegExp(r'один$'), 'одна').replaceAll(RegExp(r'два$'), 'две');
      final form = (k % 100 >= 11 && k % 100 <= 14)
          ? 'тысяч'
          : switch (k % 10) {
              1 => 'тысяча',
              2 || 3 || 4 => 'тысячи',
              _ => 'тысяч',
            };
      return '$words $form${r == 0 ? '' : ' ${_ru(r)}'}';
    }
    return '$n';
  }

  /// Matndagi barcha sonlarni so'zga aylantiradi.
  static String spellDigits(String text, String lang) {
    if (lang == 'uz') return UzNumbers.spellDigits(text);
    return text.replaceAllMapped(RegExp(r'\d+'), (m) => word(int.parse(m.group(0)!), lang));
  }
}
