import '../../content/instructions.dart';
import '../../models/exercise.dart';
import '../../models/visual.dart';
import '../generator_base.dart';

/// Maktab mashqlari uchun yordamchilar: savol matni o'zbekcha (ekranda o'qiladi),
/// ovoz — faqat 🔊 bosilganda (raqamlar so'z bilan).
extension SchoolGen on GenContext {
  /// Savol: ekranda shu matn, ovozda — raqamlar so'z bilan.
  RenderedInstruction ask(String text, {String lang = 'uz'}) => RenderedInstruction(
        Localized.same(text),
        InstructionBank.speechFor(text, lang),
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
