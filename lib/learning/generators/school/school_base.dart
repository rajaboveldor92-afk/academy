import '../../content/instructions.dart';
import '../../content/uz_numbers.dart';
import '../../models/exercise.dart';
import '../../models/visual.dart';
import '../generator_base.dart';

/// Maktab mashqlari uchun yordamchilar: savol matni o'zbekcha (ekranda o'qiladi),
/// ovoz — faqat 🔊 bosilganda (raqamlar so'z bilan).
extension SchoolGen on GenContext {
  /// Savol: ekranda shu matn, ovozda — raqamlar, kasrlar, belgilar va birliklar so'z bilan.
  RenderedInstruction ask(String text, {String lang = 'uz'}) => RenderedInstruction(
        Localized.same(text),
        lang == 'uz' ? schoolSpeech(text) : InstructionBank.speechFor(text, lang),
        lang: lang,
        key: 'school',
      );

  /// Matnli variantlar: [answer] — to'g'ri, [wrong] — chalg'ituvchilar (takrorlar olib tashlanadi).
  Exercise textChoice({
    required String question,
    required String answer,
    required List<String> wrong,
    required String concept,
    int options = 4,
    String? hint,
    String? explanation,
    ExerciseVisual? visual,
    Map<String, Object> meta = const {},
    String lang = 'uz',
  }) {
    final distractors = <String>[];
    for (final w in wrong) {
      if (w != answer && !distractors.contains(w)) distractors.add(w);
    }
    final picked = sample(distractors, options - 1 < distractors.length ? options - 1 : distractors.length);
    return choice(
      say: ask(question, lang: lang),
      options: [Opt.text(answer), for (final w in picked) Opt.text(w)],
      concept: concept,
      visual: visual,
      hint: hint,
      explanation: explanation,
      meta: meta,
    );
  }

  /// Sonli javob: [input] bo'lsa — klaviaturada yoziladi, aks holda yaqin sonlardan tanlanadi.
  Exercise numberAnswer({
    required String question,
    required int answer,
    required String concept,
    bool input = true,
    String unit = '',
    String? hint,
    String? explanation,
    ExerciseVisual? visual,
    Map<String, Object> meta = const {},
    int spread = 0,
  }) {
    final fullMeta = {...meta, 'answer': answer};
    if (input) {
      return custom(
        say: ask(question),
        kind: ExerciseKind.input,
        concept: concept,
        visual: visual,
        input: InputTask(answer: '$answer', keys: answer < 0 ? 'signed' : 'digits', unit: unit),
        hint: hint,
        explanation: explanation,
        meta: fullMeta,
      );
    }
    final d = spread > 0 ? spread : (answer.abs() < 20 ? 3 : (answer.abs() < 200 ? 10 : answer.abs() ~/ 10));
    final values = numberChoices(answer, count: 4, min: answer < 0 ? answer - d * 3 : 0, max: answer + d * 3, spread: d);
    return choice(
      say: ask(question),
      options: [for (final v in values) Opt.text('$v')],
      concept: concept,
      visual: visual,
      hint: hint,
      explanation: explanation,
      meta: fullMeta,
    );
  }

  /// Matnli javobni yozish (kasr `3/4`, o'nli kasr `2,5`): [accept] — teng kuchli yozuvlar.
  Exercise textAnswer({
    required String question,
    required String answer,
    required String concept,
    List<String> accept = const [],
    String keys = 'digits',
    String unit = '',
    String? hint,
    String? explanation,
    ExerciseVisual? visual,
    Map<String, Object> meta = const {},
  }) {
    return custom(
      say: ask(question),
      kind: ExerciseKind.input,
      concept: concept,
      visual: visual,
      input: InputTask(answer: answer, accept: accept, keys: keys, unit: unit),
      hint: hint,
      explanation: explanation,
      meta: meta,
    );
  }

  /// Darajadagi `mode` parametri: `input`, `choice` yoki aralash (standart).
  bool useInput() {
    final mode = ps('mode', 'mixed');
    if (mode == 'input') return true;
    if (mode == 'choice') return false;
    return chance(0.5);
  }
}

/// Maktab savolini o'zbekcha ovoz uchun tayyorlaydi (ekrandagi matn o'zgarmaydi):
/// "12 345" → bitta son, "3/4" → "to‘rtdan uch", "2 3/4" → "ikki butun to‘rtdan uch",
/// "2,05" → "ikki butun yuzdan besh", "8:05 da" → "soat sakkizdan besh minut o‘tganda",
/// "·" → "ko‘paytiruv", " : " → "bo‘luv", "sm²" → "kvadrat santimetr", "%" → "foiz", "°" → "gradus".
String schoolSpeech(String text) {
  var s = text;
  // Dasturlash (Python): "17 // 5" → butun bo'luv, "17 % 5" → qoldiqli bo'luv.
  s = s.replaceAll(' // ', ' butun bo‘luv ').replaceAll(RegExp(r'(?<=[\w)]) % (?=[\w(])'), ' qoldiqli bo‘luv ');
  // Xonalarga ajratilgan son bitta son bo'lib o'qiladi.
  s = s.replaceAll(RegExp(r'(?<=\d) (?=\d{3}(?!\d))'), '');
  // Soat: "8:00 da" → "soat sakkizda", "8:05 da" → "soat sakkizdan besh minut o‘tganda".
  s = s.replaceAllMapped(RegExp(r'(\d{1,2}):(\d{2})( da(?![\p{L}‘’]))?', unicode: true), (m) {
    final h = int.parse(m[1]!), min = int.parse(m[2]!);
    if (min == 0) return 'soat $h${m[3] != null ? ' da' : ''}';
    return 'soat $h dan $min minut o‘tganda';
  });
  // Tartib son: "3-sinf" → "uchinchi sinf", "2-katakda" → "ikkinchi katakda".
  s = s.replaceAllMapped(RegExp(r'(?<![\d,/])(\d+)-(?=\p{L})', unicode: true), (m) => '${UzNumbers.ordinal(int.parse(m[1]!))} ');
  // "Ctrl+C" → "Ctrl va C", "he / she" → "he yoki she".
  s = s.replaceAllMapped(RegExp(r'(?<=\p{L})\+(?=\p{L})', unicode: true), (_) => ' va ').replaceAll(' / ', ' yoki ');
  // Aralash son va oddiy kasr.
  s = s.replaceAllMapped(RegExp(r'(\d+) (\d+)/(\d+)'), (m) => '${m[1]} butun ${m[3]} dan ${m[2]}');
  s = s.replaceAllMapped(RegExp(r'(\d+)/(\d+)'), (m) => '${m[2]} dan ${m[1]}');
  // O'nli kasr: verguldan keyingi raqamlar soniga qarab "o‘ndan", "yuzdan", "mingdan".
  s = s.replaceAllMapped(RegExp(r'(\d+),(\d+)'), (m) {
    final frac = m[2]!;
    final place = switch (frac.length) {
      1 => 'o‘ndan',
      2 => 'yuzdan',
      3 => 'mingdan',
      4 => 'o‘n mingdan',
      5 => 'yuz mingdan',
      _ => 'milliondan',
    };
    return '${m[1]} butun $place ${int.parse(frac)}';
  });
  // O'lchov birliklari to'liq nomi bilan.
  s = s.replaceAllMapped(_unitPattern, (m) => _unitWords[m[1]]!);
  // "25% ini" → "yigirma besh foizini".
  s = s.replaceAllMapped(RegExp(r'% (i|ini|iga|idan)(?![\p{L}‘’])', unicode: true), (m) => ' foiz${m[1]}');
  s = s
      .replaceAll('·', ' ko‘paytiruv ')
      .replaceAll('×', ' ko‘paytiruv ')
      .replaceAll(' : ', ' bo‘luv ')
      .replaceAll('○', ' va ')
      .replaceAll('≈', ' taxminan ')
      .replaceAll('%', ' foiz ')
      .replaceAll('°', ' gradus ')
      .replaceAll('(', ' qavs ochiladi, ')
      .replaceAll(')', ' qavs yopiladi, ')
      .replaceAll(RegExp('[{}]'), ' ');
  return InstructionBank.toSpeech(s);
}

const Map<String, String> _unitWords = {
  'km/soat': 'kilometr soatiga',
  'km²': 'kvadrat kilometr',
  'm²': 'kvadrat metr',
  'dm²': 'kvadrat detsimetr',
  'sm²': 'kvadrat santimetr',
  'mm²': 'kvadrat millimetr',
  'm³': 'kub metr',
  'dm³': 'kub detsimetr',
  'sm³': 'kub santimetr',
  'km': 'kilometr',
  'dm': 'detsimetr',
  'sm': 'santimetr',
  'mm': 'millimetr',
  'kg': 'kilogramm',
  'ml': 'millilitr',
  'min': 'minut',
  'm': 'metr',
  'g': 'gramm',
  't': 'tonna',
  'l': 'litr',
};

final RegExp _unitPattern = RegExp(
  '(?<![\\p{L}‘’ʻ])(${_unitWords.keys.join('|')})(?![\\p{L}‘’ʻ²³/])',
  unicode: true,
);

/// Sonni xonalarga ajratib yozish: 1234567 → "1 234 567".
String fmtNum(int n) {
  final neg = n < 0;
  final digits = n.abs().toString();
  final b = StringBuffer();
  for (var i = 0; i < digits.length; i++) {
    if (i > 0 && (digits.length - i) % 3 == 0) b.write(' ');
    b.write(digits[i]);
  }
  return neg ? '−$b' : b.toString();
}

/// O'nli kasr: 2.5 → "2,5" (ortiqcha nollarsiz).
String fmtDec(num v, {int maxDigits = 4}) {
  var s = v.toStringAsFixed(maxDigits);
  if (s.contains('.')) {
    s = s.replaceAll(RegExp(r'0+$'), '');
    if (s.endsWith('.')) s = s.substring(0, s.length - 1);
  }
  return s.replaceAll('.', ',');
}

int gcd(int a, int b) {
  a = a.abs();
  b = b.abs();
  while (b != 0) {
    final t = b;
    b = a % b;
    a = t;
  }
  return a;
}
