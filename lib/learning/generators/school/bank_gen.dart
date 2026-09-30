import '../../content/instructions.dart';
import '../../../models/speech_part.dart';
import '../../models/exercise.dart';
import '../../models/visual.dart';
import '../generator_base.dart';
import 'school_base.dart';
import 'school_practice.dart';

/// Savollar banki: maktab fanlari (ona tili, o'qish, ingliz/rus tili, tabiiy fan, tarix, informatika).
///
/// Savollar `assets/data/school/bank_<fan>_g<N>.json` faylida, mavzu id bo'yicha guruhlanadi.
/// Element maydonlari (manba: `tool/content/school/schoolkit.py`):
/// * `t` — turi: `choice` (tanlash), `tf` (to'g'ri / noto'g'ri), `order` (so'zlardan gap), `match` (juftlash);
/// * `q` — savol (ekranda); `a` — to'g'ri javob; `w` — noto'g'ri javoblar;
/// * `d` — qiyinlik 1–3 (N-daraja — `d ≤ N` savollar); `x` — izoh; `h` — maslahat;
/// * `e` — emoji rasm; `text` — o'qiladigan matn (parcha, gap);
/// * `say` + `lang` — ovozda aytiladigan chet tilidagi matn (tinglab tushunish);
/// * `parts`, `extra`, `sep` — `order` uchun; `pairs` — `match` uchun.
///
/// Eski format (`question`, `answer`, `wrong`, `explanation`) ham qo'llab-quvvatlanadi.
///
/// Daraja parametrlari: `options` — variantlar soni (standart: 1-daraja 3, keyin 4), `pairs` — juftlar soni.
class BankGen {
  BankGen._();

  static const String trueText = 'To‘g‘ri';
  static const String falseText = 'Noto‘g‘ri';

  /// Darajaga mos savollar: `d ≤ level`; juda kam bo'lsa — mavzuning barcha savollari.
  static List<Map<String, dynamic>> poolFor(List<Map<String, dynamic>> all, int level) {
    final pool = [for (final i in all) if (((i['d'] as num?) ?? 1) <= level) i];
    return pool.length >= 4 ? pool : all;
  }

  static Exercise bank(GenContext g) {
    final all = g.content.banks[g.topic.id] ?? const <Map<String, dynamic>>[];
    if (all.isEmpty) throw StateError('${g.topic.id}: savollar banki bo‘sh');
    final item = g.pick(poolFor(all, g.level));
    if (item.containsKey('question')) return SchoolPractice.bankItem(g, item);
    return switch (item['t']?.toString() ?? 'choice') {
      'tf' => _trueFalse(g, item),
      'order' => _order(g, item),
      'match' => _match(g, item),
      _ => _choice(g, item),
    };
  }

  static String? _s(Map<String, dynamic> item, String key) {
    final v = item[key];
    if (v == null) return null;
    final s = v.toString().trim();
    return s.isEmpty ? null : s;
  }

  static List<String> _list(Map<String, dynamic> item, String key) =>
      [for (final v in (item[key] as List? ?? const [])) v.toString()];

  /// Ko'rsatma: ekranda o'zbekcha savol; ovozda — chet tilidagi matn (`say`) yoki savolning o'zi.
  static RenderedInstruction _say(GenContext g, Map<String, dynamic> item, String question) {
    final say = _s(item, 'say');
    final lang = _s(item, 'lang') ?? 'uz';
    if (say != null && lang != 'uz') {
      final foreign = InstructionBank.speechFor(say, lang);
      // 1–2-sinf: bola hali o'qiy olmaydi — avval o'zbekcha ko'rsatma, keyin chet tilidagi so'z aytiladi
      // (ko'rsatmada chet tilidagi so'z qo'shtirnoqda bo'lsa, faqat chet tilidagi ovoz).
      final grade = int.tryParse(g.topic.ageSuffix.replaceFirst('g', '')) ?? 0;
      final parts = grade >= 1 && grade <= 2 && !question.contains('“')
          ? [SpeechPart(schoolSpeech(question), 'uz'), SpeechPart(foreign, lang)]
          : const <SpeechPart>[];
      return RenderedInstruction(Localized.same(question), foreign, lang: lang, key: 'school', parts: parts);
    }
    return g.ask(say ?? question);
  }

  static ExerciseVisual? _visual(Map<String, dynamic> item) {
    final text = _s(item, 'text');
    final emoji = _s(item, 'e');
    if (text != null) return ReadingVisual(text, emoji: emoji);
    if (emoji != null) return Opt.emoji(emoji).visual;
    return null;
  }

  static int _options(GenContext g) => g.p('options', g.level <= 1 ? 3 : 4);

  static String _concept(GenContext g, Map<String, dynamic> item) => 'bank:${g.topic.id}:${item['id']}';

  static Exercise _choice(GenContext g, Map<String, dynamic> item) {
    final question = _s(item, 'q')!;
    final answer = _s(item, 'a')!;
    final wrong = <String>[];
    for (final w in _list(item, 'w')) {
      if (w.trim().isNotEmpty && w != answer && !wrong.contains(w)) wrong.add(w);
    }
    final picked = g.sample(wrong, wrong.length < _options(g) - 1 ? wrong.length : _options(g) - 1);
    return g.choice(
      say: _say(g, item, question),
      options: [Opt.text(answer), for (final w in picked) Opt.text(w)],
      concept: _concept(g, item),
      visual: _visual(item),
      hint: _s(item, 'h'),
      explanation: _s(item, 'x') ?? answer,
      meta: {'answer': answer, 'bankId': '${item['id']}'},
    );
  }

  static Exercise _trueFalse(GenContext g, Map<String, dynamic> item) {
    final statement = _s(item, 'q')!;
    final correct = item['a'] == true;
    final text = _s(item, 'text');
    final emoji = _s(item, 'e');
    final say = text == null && _s(item, 'say') == null
        ? RenderedInstruction(const Localized.same('Bu fikr to‘g‘rimi?'), schoolSpeech('$statement Bu fikr to‘g‘rimi?'), key: 'school')
        : _say(g, item, text == null ? 'Bu fikr to‘g‘rimi?' : statement);
    return g.choice(
      say: say,
      options: [Opt.text(correct ? trueText : falseText), Opt.text(correct ? falseText : trueText)],
      concept: _concept(g, item),
      visual: text != null ? ReadingVisual(text, emoji: emoji) : ReadingVisual(statement, emoji: emoji),
      hint: _s(item, 'h'),
      explanation: _s(item, 'x') ?? (correct ? '$trueText.' : '$falseText.'),
      meta: {'answer': correct ? trueText : falseText, 'bankId': '${item['id']}'},
    );
  }

  static Exercise _order(GenContext g, Map<String, dynamic> item) {
    final parts = _list(item, 'parts');
    final extra = _list(item, 'extra');
    final sep = item['sep']?.toString() ?? ' ';
    final joined = parts.join(sep);
    return g.custom(
      say: _say(g, item, _s(item, 'q') ?? 'So‘zlardan gap tuzing'),
      kind: ExerciseKind.assemble,
      concept: _concept(g, item),
      visual: _visual(item),
      assemble: AssembleTask(answer: parts, tiles: g.mixTiles([...parts, ...extra], parts), separator: sep),
      hint: _s(item, 'h'),
      explanation: _s(item, 'x') ?? joined,
      meta: {'answer': joined, 'bankId': '${item['id']}'},
    );
  }

  static Exercise _match(GenContext g, Map<String, dynamic> item) {
    final pairs = [
      for (final p in (item['pairs'] as List? ?? const []))
        if (p is List && p.length == 2) (p[0].toString(), p[1].toString()),
    ];
    final n = g.p('pairs', g.level <= 1 ? 3 : (g.level == 2 ? 4 : 5));
    final chosen = g.sample(pairs, n < pairs.length ? n : pairs.length);
    return g.custom(
      say: _say(g, item, _s(item, 'q') ?? 'Juftini toping'),
      kind: ExerciseKind.match,
      concept: _concept(g, item),
      pairs: [for (final (a, b) in chosen) MatchPair(Opt.text(a), Opt.text(b))],
      hint: _s(item, 'h'),
      explanation: _s(item, 'x') ?? chosen.map((p) => '${p.$1} — ${p.$2}').join('; '),
      meta: {'pairs': chosen.map((p) => '${p.$1}=${p.$2}').join(','), 'bankId': '${item['id']}'},
    );
  }
}
