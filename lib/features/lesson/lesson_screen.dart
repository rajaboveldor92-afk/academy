import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../l10n/tr.dart';
import '../../learning/content/content_provider.dart';
import '../../learning/content/number_words.dart';
import '../../learning/engine/daily_planner.dart';
import '../../learning/engine/lesson_builder.dart';
import '../../learning/engine/mastery.dart';
import '../../learning/engine/rewards.dart';
import '../../learning/engine/spaced_repetition.dart';
import '../../learning/models/exercise.dart';
import '../../learning/models/topic.dart';
import '../../learning/ui/activity_view.dart';
import '../../learning/ui/assemble_view.dart';
import '../../learning/ui/cards_view.dart';
import '../../learning/ui/input_view.dart';
import '../../learning/ui/chess_view.dart';
import '../../learning/ui/choice_view.dart';
import '../../learning/ui/coding_view.dart';
import '../../learning/ui/match_view.dart';
import '../../learning/ui/maze_view.dart';
import '../../learning/ui/jigsaw_view.dart';
import '../../learning/ui/option_card.dart';
import '../../learning/ui/sort_view.dart';
import '../../learning/ui/spot_view.dart';
import '../../learning/ui/sudoku_view.dart';
import '../../learning/ui/trace_view.dart';
import '../../models/child_profile.dart';
import '../../models/subject.dart';
import '../../services/audio_service.dart';
import '../../services/mother_voice.dart';
import '../../theme/app_colors.dart';
import '../../theme/profile_themes.dart';
import '../../widgets/star_burst.dart';
import '../profiles/profiles_controller.dart';
import '../session/progress_controller.dart';

/// Dars: bitta mavzu bo'yicha (4 yoshda 6 ta, 6 yoshda 8–10 ta mashq) yoki
/// "▶ BUGUNGI DARSim" — fanlar aralash kunlik dars ([LessonScreen.daily]).
///
/// Xato qilingan mashq shu darsning o'zida biroz keyin boshqa ko'rinishda qayta so'raladi
/// va takrorlash navbatiga (ertaga, 3 kun, 7 kun) qo'shiladi.
class LessonScreen extends ConsumerStatefulWidget {
  const LessonScreen({super.key, required String this.topicId, this.random}) : daily = false;

  const LessonScreen.daily({super.key, this.random})
      : topicId = null,
        daily = true;

  final String? topicId;
  final bool daily;

  /// Testlarda barqaror natija uchun.
  final Random? random;

  @override
  ConsumerState<LessonScreen> createState() => _LessonScreenState();
}

enum _Phase { loading, theory, playing, feedback, finished, error }

class _LessonScreenState extends ConsumerState<LessonScreen> {
  _Phase _phase = _Phase.loading;
  Topic? _topic;
  int _level = 1;
  List<PlannedExercise> _items = const [];
  final List<ExerciseResult> _results = [];
  int _retries = 0;

  /// Maktab mavzusi qoidasi shu darsda ko'rsatildimi (qayta o'ynashda takrorlanmaydi).
  bool _theoryShown = false;
  List<MedalDef> _newMedals = const [];
  int _index = 0;
  int _stars = 0;

  /// Onaning ovozidagi maqtov va dalda navbati (bir xil ibora ketma-ket takrorlanmasin).
  int _praiseTurn = 0;
  int _mistakeTurn = 0;
  String? _praiseText;
  String? _banner;
  bool _bannerHint = false;
  bool _lastCorrect = false;
  int _lastMistakes = 0;
  ({SkillStat stat, LevelDecision decision})? _outcome;
  Timer? _advanceTimer;

  ChildProfile? get _profile => ref.read(activeProfileProvider);
  bool get _junior => _profile?.ageGroup.isJunior ?? true;

  /// Bolaning tili: ekran matnlari, maqtov va dalda shu tilda.
  String get _lang => _profile?.language ?? 'uz';

  /// Onaning yozib olingan ovozi faqat o'zbek tilidagi profilda ishlatiladi.
  bool get _uzChild => _lang == 'uz';
  Tr get _t => Tr(_lang);
  late final AudioService _audio;
  Exercise get _current => _items[_index].exercise;
  PlannedExercise get _item => _items[_index];

  @override
  void initState() {
    super.initState();
    _audio = ref.read(audioServiceProvider);
    _start();
  }

  @override
  void dispose() {
    _advanceTimer?.cancel();
    _audio.stop();
    super.dispose();
  }

  Future<void> _start() async {
    try {
      final content = await ref.read(contentProvider.future);
      final profile = _profile;
      if (profile == null) throw StateError('Profil tanlanmagan');
      final progress = ref.read(progressProvider.notifier).of(profile.id);
      Topic? topic;
      var level = 1;
      List<PlannedExercise> items;
      if (widget.daily) {
        items = DailyPlanner.build(
          content: content,
          age: profile.age,
          progress: progress,
          isEnabled: profile.isSubjectEnabled,
          now: ref.read(clockProvider)(),
          rng: widget.random,
          difficultyBias: profile.difficultyBias,
          lang: profile.language,
          grade: profile.grade,
        );
      } else {
        topic = content.topic(widget.topicId!);
        if (topic == null) throw StateError('Mavzu topilmadi');
        final stat = progress.skillOf(topic.id);
        level = (stat.level + profile.difficultyBias).clamp(1, topic.maxLevel).toInt();
        final curriculum = content.curriculum(topic.subject, topic.ageSuffix);
        final size = topic.lessonSize ?? curriculum?.lessonSize ?? (_junior ? 6 : 10);
        final exercises = LessonBuilder.build(
          content: content,
          topic: topic,
          level: level,
          count: size,
          age: profile.age,
          rng: widget.random,
          avoid: progress.recentOf(topic.id).toSet(),
          lang: profile.language,
        );
        items = [for (final e in exercises) PlannedExercise(topic: topic, level: level, exercise: e)];
      }
      if (!mounted) return;
      final theoryTopic = topic;
      final showTheory = !_theoryShown && theoryTopic != null && theoryTopic.theoryIn(profile.language) != null;
      setState(() {
        _topic = topic;
        _level = level;
        _items = items;
        _results.clear();
        _retries = 0;
        _newMedals = const [];
        _index = 0;
        _stars = 0;
        _outcome = null;
        _phase = items.isEmpty ? _Phase.error : (showTheory ? _Phase.theory : _Phase.playing);
      });
      _speakCurrent();
    } catch (e) {
      debugPrint('Dars yuklanmadi: $e');
      if (mounted) setState(() => _phase = _Phase.error);
    }
  }

  /// Maktab o'quvchisi o'zi o'qiydi: ko'rsatma avtomatik aytilmaydi (🔊 bosilsa aytiladi),
  /// chet tili darslari bundan mustasno (talaffuz eshitilishi kerak).
  bool get _autoSpeak {
    final profile = _profile;
    if (profile == null || !profile.isSchool) return true;
    return MotherVoice.listeningSubjects.contains(_current.subject);
  }

  void _startPractice() {
    setState(() {
      _theoryShown = true;
      _phase = _Phase.playing;
    });
    _speakCurrent();
  }

  void _speakCurrent() {
    if (_phase != _Phase.playing || _items.isEmpty) return;
    if (!_autoSpeak) return;
    final ex = _current;
    // Xotira mashqida ko'rsatma rasm yashiringanda aytiladi; avval — "Yaxshilab qara. Rasmlarni eslab qol."
    if (ex.kind == ExerciseKind.memory || (ex.kind == ExerciseKind.assemble && ex.previewVisual != null)) {
      if (_uzChild) {
        _audio.speakParts(MotherVoice.memorize());
      } else {
        _audio.speak(_t.lookAndRemember, lang: _lang);
      }
      return;
    }
    _speakExercise(ex, intro: _index == 0);
  }

  /// Ko'rsatmani aytadi: onaning yozib olingan ovozida (mazmuni mos ibora bo'lsa) yoki
  /// mashqning o'z tilida. Tinglash darsi boshida — "Diqqat bilan tingla."
  void _speakExercise(Exercise ex, {bool intro = false}) {
    final parts = [
      if (intro && MotherVoice.isListening(ex))
        _uzChild ? MotherVoice.part('diqqat_bilan_tingla') : SpeechPart(_t.listenCarefully, _lang),
      ...MotherVoice.instruction(ex),
    ];
    if (parts.length == 1 && parts.first.clip == null) {
      _audio.speak(parts.first.text, lang: parts.first.lang);
    } else {
      _audio.speakParts(parts);
    }
  }

  void _onMistake(int mistakes) {
    final ex = _current;
    // O'zbek tilidagi profilda, o'zbekcha mashqlarda — onaning ovozida dalda va mashqqa mos maslahat.
    // Tinglash mashqida ikkinchi xatoda — "Yana bir marta eshit" + ko'rsatma.
    // Qolgan hollarda dalda: chet tili darsida — o'sha tilda, boshqa darslarda — bolaning tilida.
    final foreign = MotherVoice.listeningSubjects.contains(ex.subject);
    final encourageLang = foreign ? ex.speechLang : _lang;
    List<SpeechPart>? say;
    if (_uzChild && ex.speechLang == 'uz') {
      say = MotherVoice.afterMistake(ex, mistakes, _mistakeTurn++);
    } else if (mistakes >= 2 && MotherVoice.isListening(ex)) {
      say = [
        _uzChild ? MotherVoice.part('yana_eshit') : SpeechPart(_t.listenAgain, _lang),
        ...MotherVoice.instruction(ex),
      ];
    }
    if (say == null) {
      _audio.encourage(lang: encourageLang);
    } else {
      _audio.playEffect(SoundEffect.tryAgain);
      _audio.speakParts(say);
    }
    setState(() {
      _bannerHint = mistakes >= 2 && ex.hint != null;
      _banner = _bannerHint ? ex.hint : (say?.first.text ?? FeedbackPhrases.randomEncourage(encourageLang));
    });
  }

  Future<void> _onSolved(int mistakes) async {
    final ex = _current;
    final item = _item;
    final profile = _profile;
    final firstTry = mistakes == 0;
    _results.add(ExerciseResult(
      topicId: item.topic.id,
      concept: ex.conceptKey,
      firstTry: firstTry,
      signature: LessonBuilder.signatureHash(ex),
      retry: item.retry,
    ));
    if (!firstTry && !item.retry) _scheduleRetry(item);
    final earned = firstTry ? ex.rewardStars : 0;
    // Kichik yoshda sanash mashqidan keyin birga sanaydi: "Bir, ikki, uch" (o'zbekchada — onaning ovozida).
    final countTo = _junior ? MotherVoice.countTarget(ex) : null;
    final foreign = MotherVoice.listeningSubjects.contains(ex.subject);
    String? praiseText;
    var spokenCount = 0;
    if (_uzChild && ex.speechLang == 'uz') {
      final count = _junior ? MotherVoice.countAloud(ex) : const <SpeechPart>[];
      spokenCount = count.length;
      final key = firstTry ? MotherVoice.praise[_praiseTurn++ % MotherVoice.praise.length] : 'togri_topding';
      praiseText = MotherVoice.clips[key];
      _audio.playEffect(SoundEffect.correct);
      _audio.speakParts([...count, MotherVoice.part(key)]);
    } else if (foreign && ex.speechLang != _lang) {
      // Chet tili darsida maqtov o'sha tilda.
      _audio.praise(lang: ex.speechLang);
    } else {
      final phrases = FeedbackPhrases.praise[_lang] ?? FeedbackPhrases.praise['uz']!;
      praiseText = firstTry ? phrases[_praiseTurn++ % phrases.length] : _t.gotIt;
      spokenCount = countTo ?? 0;
      _audio.playEffect(SoundEffect.correct);
      _audio.speakParts([
        for (var i = 1; i <= spokenCount; i++) SpeechPart(NumberWords.word(i, _lang), _lang),
        SpeechPart(praiseText, _lang),
      ]);
    }
    setState(() {
      _phase = _Phase.feedback;
      _lastCorrect = firstTry;
      _lastMistakes = mistakes;
      _praiseText = praiseText;
      _banner = null;
      _stars += earned;
    });
    if (profile != null) {
      await ref.read(progressProvider.notifier).recordAnswer(
            childId: profile.id,
            subjectId: ex.subject,
            isCorrect: firstTry,
            rewardStars: earned,
          );
    }
    // Kichik yoshda avtomatik o'tish; 6 yoshda izohni ko'rib, o'zi o'tadi.
    if (_junior || ex.explanation == null) {
      _advanceTimer = Timer(Duration(milliseconds: 1500 + spokenCount * 550), _next);
    }
  }

  /// Xato qilingan tushuncha 2–3 mashqdan keyin boshqa ko'rinishda qayta so'raladi.
  void _scheduleRetry(PlannedExercise item) {
    if (_retries >= SpacedRepetition.maxRetriesPerLesson) return;
    const long = {ExerciseKind.activity, ExerciseKind.jigsaw, ExerciseKind.cards};
    if (long.contains(item.exercise.kind) || item.exercise.chess?.goal == 'play') return;
    final content = ref.read(contentProvider).valueOrNull;
    final profile = _profile;
    if (content == null || profile == null) return;
    final retry = LessonBuilder.similar(
      content: content,
      topic: item.topic,
      level: item.level,
      age: profile.age,
      rng: widget.random,
      concept: item.exercise.conceptKey,
      avoid: {for (final i in _items) LessonBuilder.signatureHash(i.exercise)},
      lang: profile.language,
    );
    if (retry == null) return;
    _retries++;
    final at = min(_index + 3, _items.length);
    setState(() {
      _items = [
        ..._items.sublist(0, at),
        PlannedExercise(topic: item.topic, level: item.level, exercise: retry, retry: true),
        ..._items.sublist(at),
      ];
    });
  }

  void _onAchievement(String id) {
    final profile = _profile;
    if (profile != null) ref.read(progressProvider.notifier).addCounter(profile.id, id);
  }

  Future<void> _next() async {
    _advanceTimer?.cancel();
    if (!mounted) return;
    if (_index + 1 < _items.length) {
      setState(() {
        _index++;
        _phase = _Phase.playing;
        _banner = null;
      });
      _speakCurrent();
      return;
    }
    await _finish();
  }

  Future<void> _finish() async {
    final profile = _profile;
    if (profile == null) return;
    final notifier = ref.read(progressProvider.notifier);
    final original = _results.where((r) => !r.retry).toList();
    ({SkillStat stat, LevelDecision decision})? outcome;
    final topic = _topic;
    if (widget.daily) {
      await notifier.completeDailyLesson(profile.id, _results);
    } else if (topic != null) {
      outcome = await notifier.completeTopicLesson(
        childId: profile.id,
        topicId: topic.id,
        maxLevel: topic.maxLevel,
        correctFirstTry: original.where((r) => r.firstTry).length,
        total: original.length,
        signatures: original.map((r) => r.signature),
      );
      await notifier.recordReviews(profile.id, _results);
      if (_results.isNotEmpty && _results.every((r) => r.firstTry)) await notifier.addCounter(profile.id, 'perfect_lesson');
    }
    final medals = await notifier.awardMedals(profile.id);
    if (!mounted) return;
    setState(() {
      _outcome = outcome;
      _newMedals = medals;
      _phase = _Phase.finished;
    });
    _audio.playEffect(medals.isEmpty ? SoundEffect.star : SoundEffect.medal);
    // O'zbek tilidagi profilda — onaning ovozida maqtov (ism bilan), qolgani qurilma ovozida.
    final name = MotherVoice.nameClip(profile);
    final decision = outcome?.decision;
    final medalLine = medals.isEmpty ? null : '${_t.newMedal(medals.first.title.of(_lang))}!';
    final mark = _testMark;
    if (mark != null) {
      // Nazorat ishi: 5 ballik baho.
      _audio.speakParts([
        SpeechPart('${_t.markLabel(mark)}. ${_t.markName(mark)}', _lang),
        if (medalLine != null) SpeechPart(medalLine, _lang),
      ]);
      return;
    }
    if (!_uzChild) {
      _audio.speakParts([
        SpeechPart(widget.daily ? _t.dailyFinished : _finishMessage(decision ?? LevelDecision.stay), _lang),
        if (medalLine != null) SpeechPart(medalLine, _lang),
      ]);
      return;
    }
    final say = <SpeechPart>[
      if (widget.daily) ...[
        MotherVoice.part('barakalla'),
        if (name != null) MotherVoice.part(name),
        MotherVoice.part('bugun_yaxshi_harakat'),
      ] else if (decision == LevelDecision.up) ...[
        MotherVoice.part('barakalla'),
        if (name != null) MotherVoice.part(name),
        SpeechPart(_t.levelUpSpoken, 'uz'),
      ] else if (decision == LevelDecision.stay) ...[
        MotherVoice.part('juda_yaxshi'),
        const SpeechPart('Yana mashq qilamiz.', 'uz'),
      ] else
        SpeechPart(_finishMessage(LevelDecision.down), 'uz'),
      if (medalLine != null) SpeechPart(medalLine, 'uz'),
    ];
    _audio.speakParts(say);
  }

  /// Nazorat ishi bahosi (5 ballik): birinchi urinishdagi to'g'ri javoblar ulushi bo'yicha.
  int? get _testMark {
    final topic = _topic;
    if (topic == null || !topic.isTest || widget.daily) return null;
    final original = _results.where((r) => !r.retry).toList();
    if (original.isEmpty) return null;
    final ratio = original.where((r) => r.firstTry).length / original.length;
    return ratio >= 0.9 ? 5 : (ratio >= 0.7 ? 4 : (ratio >= 0.5 ? 3 : 2));
  }

  String _finishMessage(LevelDecision d) => switch (d) {
        LevelDecision.up => _t.levelUp,
        LevelDecision.stay => _t.levelStay,
        LevelDecision.down => _t.levelDown,
      };

  @override
  Widget build(BuildContext context) {
    final profile = ref.watch(activeProfileProvider);
    final theme = ProfileThemes.of(profile?.colorIndex ?? 0);
    // Mashq vidjetlari (Tr.of) bolaning tilini shu yerdan oladi.
    return LangScope(
      lang: profile?.language ?? 'uz',
      child: Scaffold(
        backgroundColor: theme.light,
        body: SafeArea(
          child: switch (_phase) {
            _Phase.loading => const Center(child: CircularProgressIndicator()),
            _Phase.error => _error(),
            _Phase.theory => _theoryView(theme),
            _Phase.finished => _result(theme),
            _ => _playing(theme),
          },
        ),
      ),
    );
  }

  Widget _error() {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text('🙈', style: TextStyle(fontSize: 72)),
            const SizedBox(height: 12),
            Text(_t.lessonLoadFailed, style: const TextStyle(fontSize: 20)),
            const SizedBox(height: 20),
            FilledButton(onPressed: () => Navigator.of(context).maybePop(), child: Text(_t.back)),
          ],
        ),
      ),
    );
  }

  /// Maktab mavzusi: mashqdan oldin qisqa qoida va misollar.
  Widget _theoryView(ProfileTheme theme) {
    final topic = _topic!;
    final text = topic.theoryIn(_lang) ?? '';
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              IconButton(
                key: const Key('lesson_close'),
                iconSize: 30,
                onPressed: () => Navigator.of(context).maybePop(),
                icon: const Icon(Icons.close_rounded),
              ),
              Expanded(
                child: Text(
                  '${topic.emoji} ${topic.title.of(_lang)}',
                  style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: AppColors.text),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          Expanded(
            child: Container(
              key: const Key('lesson_theory_card'),
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(24),
                border: Border.all(color: theme.primary.withAlpha(90), width: 2),
              ),
              child: SingleChildScrollView(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('📘 ${_t.theory}', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w900, color: theme.primary)),
                    const SizedBox(height: 10),
                    Text(text, style: const TextStyle(fontSize: 19, height: 1.4, color: AppColors.text)),
                  ],
                ),
              ),
            ),
          ),
          const SizedBox(height: 12),
          SizedBox(
            height: 58,
            child: FilledButton.icon(
              key: const Key('theory_start'),
              onPressed: _startPractice,
              icon: const Icon(Icons.play_arrow_rounded, size: 30),
              label: Text(_t.startPractice, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
            ),
          ),
        ],
      ),
    );
  }

  void _showTheoryDialog() {
    final topic = _topic;
    final text = topic?.theoryIn(_lang);
    if (topic == null || text == null) return;
    final t = _t;
    showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      showDragHandle: true,
      builder: (ctx) => SafeArea(
        child: ConstrainedBox(
          constraints: BoxConstraints(maxHeight: MediaQuery.sizeOf(ctx).height * 0.8),
          child: SingleChildScrollView(
            padding: const EdgeInsets.fromLTRB(20, 0, 20, 24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('📘 ${t.theory}', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
                const SizedBox(height: 10),
                Text(text, style: const TextStyle(fontSize: 18, height: 1.4)),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _topBar(ProfileTheme theme) {
    final total = _items.length;
    final done = _index + (_phase == _Phase.feedback ? 1 : 0);
    final hasTheory = !widget.daily && _topic?.theoryIn(_lang) != null;
    return Padding(
      padding: const EdgeInsets.fromLTRB(4, 4, 12, 0),
      child: Row(
        children: [
          IconButton(
            key: const Key('lesson_close'),
            iconSize: 30,
            onPressed: () => Navigator.of(context).maybePop(),
            icon: const Icon(Icons.close_rounded),
          ),
          Expanded(
            child: ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: LinearProgressIndicator(
                value: total == 0 ? 0 : done / total,
                minHeight: 14,
                color: theme.primary,
                backgroundColor: Colors.white,
              ),
            ),
          ),
          if (hasTheory)
            IconButton(
              key: const Key('lesson_theory'),
              tooltip: _t.showRule,
              onPressed: _showTheoryDialog,
              icon: const Text('📘', style: TextStyle(fontSize: 24)),
            )
          else
            const SizedBox(width: 12),
          Text('⭐ $_stars', style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
        ],
      ),
    );
  }

  Widget _playing(ProfileTheme theme) {
    final ex = _current;
    final callbacks = ExerciseCallbacks(
      onMistake: _onMistake,
      onSolved: _onSolved,
      onSpeak: (t) => t == ex.speech ? _speakExercise(ex) : _audio.speak(t, lang: ex.speechLang),
      onAchievement: _onAchievement,
    );
    final key = ValueKey('ex_$_index');
    final Widget body = switch (ex.kind) {
      ExerciseKind.match => MatchExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.sort => SortExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.maze => MazeExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.sudoku => SudokuExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.coding => CodingExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.assemble => AssembleExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.trace => TraceExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.chess => ChessExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.cards => CardsExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.spot => SpotExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.jigsaw => JigsawExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.activity => ActivityExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.input => InputExerciseView(key: key, exercise: ex, callbacks: callbacks),
      ExerciseKind.choice || ExerciseKind.memory => ChoiceExerciseView(key: key, exercise: ex, callbacks: callbacks),
    };
    return Stack(
      children: [
        Column(
          children: [
            _topBar(theme),
            _instruction(ex, theme),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(12, 4, 12, 12),
                child: AbsorbPointer(absorbing: _phase == _Phase.feedback, child: body),
              ),
            ),
            if (_banner != null) _bannerView(),
          ],
        ),
        if (_phase == _Phase.feedback) _feedbackOverlay(ex, theme),
      ],
    );
  }

  Widget _instruction(Exercise ex, ProfileTheme theme) {
    final item = _item;
    final subject = Subject.fromId(item.topic.subject);
    final label = widget.daily && subject != null
        ? '${subject.emoji} ${subject.titleIn(_lang)}${item.review || item.retry ? ' · 🔁 ${_t.review}' : ''}'
        : (item.retry ? '🔁 ${_t.oneMoreTime}' : null);
    final row = _instructionRow(ex, theme);
    if (label == null) return row;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(16, 6, 16, 0),
          child: Text(label, key: const Key('lesson_subject'), style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w800, color: AppColors.textSoft)),
        ),
        row,
      ],
    );
  }

  Widget _instructionRow(Exercise ex, ProfileTheme theme) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(12, 10, 12, 6),
      child: Row(
        children: [
          IconButton.filled(
            key: const Key('lesson_speak'),
            iconSize: 30,
            style: IconButton.styleFrom(backgroundColor: theme.primary),
            onPressed: () => _speakExercise(ex),
            icon: const Icon(Icons.volume_up_rounded),
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  ex.prompt,
                  key: const Key('lesson_instruction'),
                  style: TextStyle(
                    fontSize: _junior ? 22 : 20,
                    fontWeight: FontWeight.w800,
                    color: AppColors.text,
                    height: 1.2,
                  ),
                ),
                // Ko'rsatma boshqa tilda bo'lsa (chet tili yoki o'zbek tili darsi) — bolaning tilidagi tarjimasi.
                if (ex.speechLang != _lang)
                  Text(
                    ex.instruction.of(_lang),
                    key: const Key('lesson_instruction_uz'),
                    style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w600, color: AppColors.textSoft),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _bannerView() {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.fromLTRB(12, 0, 12, 12),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: _bannerHint ? const Color(0xFFFFF8E1) : const Color(0xFFFFF1E3),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        children: [
          Text(_bannerHint ? '💡' : '🤗', style: const TextStyle(fontSize: 26)),
          const SizedBox(width: 10),
          Expanded(
            child: Text(_banner!, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w700)),
          ),
        ],
      ),
    );
  }

  Widget _feedbackOverlay(Exercise ex, ProfileTheme theme) {
    final phrases = FeedbackPhrases.praise[ex.speechLang] ?? FeedbackPhrases.praise['uz']!;
    final praise = _praiseText ??
        (_lastCorrect ? phrases[_index % phrases.length] : (ex.speechLang == _lang ? _t.gotIt : phrases.last));
    final showExplanation = !_junior && ex.explanation != null;
    return Positioned.fill(
      child: IgnorePointer(
        ignoring: !showExplanation,
        child: Container(
          color: Colors.white.withAlpha(140),
          alignment: Alignment.center,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              if (_lastCorrect)
                const SizedBox(width: 180, height: 180, child: StarBurst(size: 180))
              else
                const Text('👍', style: TextStyle(fontSize: 80)),
              Text(praise, style: TextStyle(fontSize: 34, fontWeight: FontWeight.w900, color: theme.primary)),
              if (_lastCorrect && ex.rewardStars > 0)
                Text('+${ex.rewardStars} ⭐', style: const TextStyle(fontSize: 26, fontWeight: FontWeight.w800)),
              if (!_lastCorrect && _lastMistakes > 0)
                Text(_t.firstTryNext, textAlign: TextAlign.center, style: const TextStyle(fontSize: 18)),
              if (showExplanation) ...[
                const SizedBox(height: 16),
                Container(
                  margin: const EdgeInsets.symmetric(horizontal: 24),
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(color: theme.primary.withAlpha(80), width: 2),
                  ),
                  child: Text(
                    ex.explanation!,
                    key: const Key('lesson_explanation'),
                    textAlign: TextAlign.center,
                    style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w800),
                  ),
                ),
                const SizedBox(height: 16),
                FilledButton.icon(
                  key: const Key('lesson_next'),
                  onPressed: _next,
                  icon: const Icon(Icons.arrow_forward_rounded),
                  label: Text(_t.next),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }

  Widget _result(ProfileTheme theme) {
    final outcome = _outcome;
    final decision = outcome?.decision ?? LevelDecision.stay;
    final total = _results.length;
    final firstTry = _results.where((r) => r.firstTry).length;
    final starsRow = total == 0 ? 1 : (firstTry * 3 / total).ceil().clamp(1, 3).toInt();
    final profile = _profile;
    final progress = profile == null ? null : ref.read(progressProvider.notifier).of(profile.id);
    final gifts = progress == null ? 0 : Rewards.giftsAvailable(progress);
    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            Text('⭐' * starsRow, style: const TextStyle(fontSize: 64)),
            if (_testMark != null)
              Text(
                _t.markLabel(_testMark!),
                key: const Key('test_mark'),
                style: TextStyle(fontSize: 40, fontWeight: FontWeight.w900, color: theme.primary),
              ),
            const SizedBox(height: 12),
            Text(
              widget.daily ? _t.dailyFinished : (_testMark != null ? _t.markName(_testMark!) : _finishMessage(decision)),
              key: const Key('lesson_result'),
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 28, fontWeight: FontWeight.w900, color: theme.primary),
            ),
            const SizedBox(height: 12),
            Text(_t.starsToday(_stars), style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w700)),
            if (widget.daily)
              Padding(
                padding: const EdgeInsets.only(top: 6),
                child: Text(_t.gardenWatered, textAlign: TextAlign.center, style: const TextStyle(fontSize: 18)),
              ),
            if (!_junior) ...[
              const SizedBox(height: 8),
              Text(_t.firstTry(firstTry, total), style: const TextStyle(fontSize: 20)),
              if (_topic != null)
                Text(_t.levelOf(outcome?.stat.level ?? _level, _topic!.maxLevel), style: const TextStyle(fontSize: 20)),
            ],
            for (final m in _newMedals)
              Container(
                key: ValueKey('new_medal_${m.id}'),
                margin: const EdgeInsets.only(top: 14),
                padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
                decoration: BoxDecoration(color: const Color(0xFFFFF8E1), borderRadius: BorderRadius.circular(20), border: Border.all(color: AppColors.star, width: 2)),
                child: Text('${m.emoji} ${_t.newMedal(m.title.of(_lang))}', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
              ),
            if (gifts > 0)
              Padding(
                padding: const EdgeInsets.only(top: 14),
                child: Text(_t.giftWaiting, textAlign: TextAlign.center, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w800)),
              ),
            const SizedBox(height: 28),
            if (!widget.daily) ...[
              FilledButton.icon(
                key: const Key('lesson_again'),
                onPressed: () {
                  setState(() => _phase = _Phase.loading);
                  _start();
                },
                icon: const Icon(Icons.replay_rounded),
                label: Text(_t.playAgain),
              ),
              const SizedBox(height: 12),
            ],
            OutlinedButton.icon(
              key: const Key('lesson_done'),
              onPressed: () => Navigator.of(context).maybePop(),
              icon: Icon(widget.daily ? Icons.home_rounded : Icons.grid_view_rounded),
              label: Text(widget.daily ? _t.home : _t.topics),
            ),
          ],
        ),
      ),
    );
  }
}
