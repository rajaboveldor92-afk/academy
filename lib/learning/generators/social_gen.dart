import '../content/instructions.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'generator_base.dart';

/// 🤝 Muloqot (hislar, sehrli so'zlar, yaxshi do'st, xavfsizlik) va 🏠 ota-ona bilan faoliyatlar.
///
/// Muloqot mashqlari hukm qilmaydi: noto'g'ri tanlovda "xato" deyilmaydi, yumshoq dalda
/// beriladi, to'g'ri javobdan keyin nima uchun shunday qilish yaxshi ekani tushuntiriladi.
class SocialGames {
  SocialGames._();

  static final Map<String, ExerciseGenerator> generators = {
    'emotion_find': emotionFind,
    'emotion_name': emotionName,
    'situation': situation,
    'polite': polite,
    'polite_when': politeWhen,
    'choice': choice,
    'activity': activity,
  };

  static SceneVisual _scene(List<String> emojis) =>
      SceneVisual(Layouts.row([for (final e in emojis) Layouts.emoji(e, size: 0.6)], left: 0.15, right: 0.85), aspect: 1.8);

  static ExerciseOption _sceneOption(List<String> emojis) =>
      Opt.scene(Layouts.row([for (final e in emojis) Layouts.emoji(e, size: 0.55)], left: 0.1, right: 0.9), aspect: 1.3);

  // ------------------------------------------------------------ Hislar
  static Exercise emotionFind(GenContext g) {
    final data = g.content.activities;
    final allowed = g.pl('emotions');
    final pool = data.emotions.where((e) => allowed.isEmpty || allowed.contains(e.id)).toList();
    final chosen = g.sample(pool, g.p('options', 3));
    final target = chosen.first;
    return g.choice(
      say: g.say('so_emotion_find', {'emotion': target.name}),
      options: [for (final e in chosen) Opt.emoji(e.emoji)],
      concept: 'emotion:${target.id}',
      meta: {'answer': target.id},
      explanation: '${target.emoji} — ${target.name.of(g.lang)}',
    );
  }

  static Exercise emotionName(GenContext g) {
    final data = g.content.activities;
    final chosen = g.sample(data.emotions, g.p('options', 3));
    final target = chosen.first;
    return g.choice(
      say: g.say('so_emotion_name'),
      visual: SceneVisual([Layouts.emoji(target.emoji, size: 0.8)], aspect: 1.6),
      options: [for (final e in chosen) Opt.text(e.name.of(g.lang))],
      concept: 'emotion:${target.id}',
      meta: {'answer': target.id},
    );
  }

  static Exercise situation(GenContext g) {
    final data = g.content.activities;
    final cases = data.situations.where((s) => s.age <= g.age).toList();
    final s = g.pick(cases);
    final target = data.emotion(s.emotion);
    final others = g.sample(data.emotions.where((e) => e.id != target.id).toList(), g.p('options', 3) - 1);
    return g.choice(
      say: g.say('so_situation', {'text': s.text}),
      visual: _scene(s.scene),
      options: [Opt.emoji(target.emoji), for (final o in others) Opt.emoji(o.emoji)],
      concept: 'situation:${s.id}',
      meta: {'answer': target.id},
      explanation: g.tr('Bunday paytda odatda ${target.name.uz} bo‘lamiz ${target.emoji}. His-tuyg‘ularni aytish — yaxshi odat.',
          'At such times we usually feel ${target.name.en} ${target.emoji}. Talking about feelings is a good habit.',
          'В такие моменты мы обычно чувствуем себя так: ${target.name.ru} ${target.emoji}. Говорить о чувствах — хорошая привычка.'),
    );
  }

  // ------------------------------------------------------------ Sehrli so'zlar
  static Exercise polite(GenContext g) {
    final data = g.content.activities;
    final c = g.pick(data.polite);
    final others = g.sample(data.politeWords.where((w) => w.uz != c.word.uz).toList(), g.p('options', 3) - 1);
    final word = c.word.of(g.lang);
    return g.choice(
      say: g.say('so_polite', {'text': c.text}),
      visual: _scene(c.scene),
      options: [Opt.text(word), for (final o in others) Opt.text(o.of(g.lang))],
      concept: 'polite:${c.word.uz}',
      meta: {'answer': c.word.uz},
      explanation: g.tr('«$word» — sehrli so‘z. U odamlarni xursand qiladi.', '“$word” is a magic word. It makes people happy.',
          '«$word» — волшебное слово. Оно радует людей.'),
    );
  }

  static Exercise politeWhen(GenContext g) {
    final data = g.content.activities;
    final c = g.pick(data.polite);
    final others = <List<String>>[];
    final usedWords = <String>{c.word.uz};
    for (final o in g.sample(data.polite, data.polite.length)) {
      if (others.length >= g.p('options', 3) - 1) break;
      if (usedWords.add(o.word.uz)) others.add(o.scene);
    }
    return g.choice(
      say: g.say('so_polite_when', {'word': c.word}),
      visual: const TextVisual('🔊', scale: 0.8),
      options: [_sceneOption(c.scene), for (final o in others) _sceneOption(o)],
      concept: 'polite:${c.word.uz}',
      meta: {'answer': c.id},
      explanation: c.text.of(g.lang),
    );
  }

  // ------------------------------------------------------------ Yaxshi do'st va xavfsizlik
  /// `kinds`: `kind`, `safety`. 4 yoshda variantlar faqat rasm, 6 yoshda rasm + so'z.
  static Exercise choice(GenContext g) {
    final data = g.content.activities;
    final kinds = g.pl('kinds').isEmpty ? ['kind'] : g.pl('kinds');
    final cases = data.choices.where((c) => c.age <= g.age && kinds.contains(c.kind)).toList();
    final c = g.pick(cases);
    final withText = !g.junior || g.pb('text');
    final t = c.textIn(g.instructionLang);
    // 6 yoshda: "🤝 Yordam beraman" — butun qatorli katta tugma (uzun matn ham o'qiladi).
    ExerciseOption opt(String emoji, String text) => withText ? Opt.text('$emoji $text') : Opt.emoji(emoji);
    final lang = g.instructionLang;
    final speech = g.junior
        // Kichiklar o'qimaydi — variantlar ovozda ham aytiladi.
        ? '${t.text} ${t.good}? ${t.others.join('? ')}?'
        : null;
    final say = g.say('so_choice', {
      'text': Localized(uz: c.textIn('uz').text, en: c.textIn('en').text, ru: c.textIn('ru').text),
    });
    return g.choice(
      say: speech == null
          ? say
          : RenderedInstruction(say.text, InstructionBank.speechFor(speech, lang), lang: say.lang, key: say.key),
      visual: _scene(c.scene),
      options: [
        opt(c.goodEmoji, t.good),
        for (var i = 0; i < c.otherEmojis.length; i++) opt(c.otherEmojis[i], t.others[i]),
      ],
      concept: '${c.kind}:${c.id}',
      meta: {'answer': c.textIn('uz').good, 'case': c.id},
      hint: t.why,
      explanation: t.why,
    );
  }

  // ------------------------------------------------------------ Ota-ona bilan
  static Exercise activity(GenContext g) {
    final data = g.content.activities;
    final areas = g.pl('areas');
    final pool = data.activities.where((a) => a.age == (g.junior ? 4 : 6) && (areas.isEmpty || areas.contains(a.area))).toList();
    final a = g.pick(pool);
    return g.custom(
      say: g.say('fa_activity', {'title': a.titleL}),
      kind: ExerciseKind.activity,
      concept: 'activity:${a.id}',
      activity: a.taskIn(g.lang),
      meta: {'area': a.area},
      rewardStars: 3,
    );
  }
}
