import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../learning/engine/daily_planner.dart';
import '../../learning/engine/rewards.dart';
import '../../l10n/tr.dart';
import '../../models/child_profile.dart';
import '../../models/subject.dart';
import '../../router/app_router.dart';
import '../../services/audio_service.dart';
import '../../services/mother_voice.dart';
import '../../theme/app_colors.dart';
import '../../widgets/profile_photo.dart';
import '../../widgets/stat_chip.dart';
import '../../widgets/subject_tile.dart';
import '../profiles/profiles_controller.dart';
import '../session/progress_controller.dart';
import '../session/session_controller.dart';
import 'greeting_banner.dart';

/// Tanlangan bolaning bosh sahifasi — katta fan kartalari.
class HomeScreen extends ConsumerStatefulWidget {
  const HomeScreen({super.key});

  @override
  ConsumerState<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends ConsumerState<HomeScreen> {
  /// Ilova ochilgandan beri salom berilgan profillar (birinchi kirishda to'liq salom).
  static final Set<String> _greeted = {};

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final profile = ref.read(activeProfileProvider);
      if (profile == null) return;
      final audio = ref.read(audioServiceProvider);
      // Onaning ovozida salom; ota-ona o'z salomini yozgan bo'lsa — o'sha matn (faqat qisqa ism bilan).
      final first = _greeted.add(profile.id);
      final greeting = profile.language == 'uz' ? MotherVoice.greeting(profile, first: first) : null;
      if (greeting != null) {
        audio.speakParts(greeting);
      } else {
        audio.speak('${profile.welcomeTitle} ${profile.welcomeSubtitle}', lang: profile.language);
      }
    });
  }

  void _onLimitReached() {
    final navigator = Navigator.of(context);
    navigator.popUntil((route) => route.settings.name == AppRoutes.home || route.isFirst);
    navigator.pushReplacementNamed(AppRoutes.timeUp);
  }

  String get _lang => ref.read(activeProfileProvider)?.language ?? 'uz';

  void _openSubject(Subject subject) {
    final audio = ref.read(audioServiceProvider);
    audio.playEffect(SoundEffect.tap);
    final clip = _lang == 'uz' ? MotherVoice.subjectClip(subject.id) : null;
    final (name, lang) = subject.spokenIn(_lang);
    if (clip != null) {
      audio.speakParts([MotherVoice.part(clip)]);
    } else if (lang == 'uz') {
      audio.playWord(name, lang: lang, key: 'subject_${subject.id}');
    } else {
      audio.speak(name, lang: lang);
    }
    Navigator.of(context).pushNamed(AppRoutes.subject, arguments: subject);
  }

  void _openDailyLesson() {
    ref.read(audioServiceProvider).playEffect(SoundEffect.tap);
    ref.read(audioServiceProvider).speak(Tr(_lang).dailyLessonSpoken, lang: _lang);
    Navigator.of(context).pushNamed(AppRoutes.dailyLesson);
  }

  void _openAchievements() {
    ref.read(audioServiceProvider).speak(Tr(_lang).achievements, lang: _lang);
    Navigator.of(context).pushNamed(AppRoutes.achievements);
  }

  @override
  Widget build(BuildContext context) {
    ref.listen<SessionState>(sessionProvider, (previous, next) {
      if (next.limitReached && !(previous?.limitReached ?? false)) {
        _onLimitReached();
      }
    });

    final profile = ref.watch(activeProfileProvider);
    if (profile == null) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    final progress = ref.watch(childProgressProvider(profile.id));
    final subjects = Subject.values.where((s) => profile.isSubjectEnabled(s.id)).toList();
    final width = MediaQuery.sizeOf(context).width;
    final columns = width >= 900 ? 4 : (width >= 600 ? 3 : 2);
    final t = Tr(profile.language);

    return LangScope(
      lang: profile.language,
      child: Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            _Header(
              profile: profile,
              stars: progress.stars,
              streak: progress.streak,
            ),
            GreetingBanner(profile: profile),
            _DailyLessonCard(
              done: progress.dailyDoneOn(ref.read(clockProvider)()),
              junior: profile.ageGroup.isJunior,
              exercises: DailyPlanner.sizeFor(profile.age),
              color: AppColors.profileColor(profile.colorIndex),
              onTap: _openDailyLesson,
            ),
            Expanded(
              child: GridView.builder(
                padding: const EdgeInsets.fromLTRB(16, 8, 16, 24),
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: columns,
                  mainAxisSpacing: 16,
                  crossAxisSpacing: 16,
                ),
                itemCount: subjects.length + 1,
                itemBuilder: (context, i) {
                  if (i == subjects.length) {
                    return SubjectTile(
                      key: const Key('tile_achievements'),
                      emoji: '🏆',
                      title: t.achievements,
                      color: AppColors.star,
                      compactLabel: profile.ageGroup.isJunior,
                      // Ochilmagan sovg'a qutisi bo'lsa — belgi.
                      badge: Rewards.giftsAvailable(progress) > 0 ? '🎁' : null,
                      onTap: _openAchievements,
                    );
                  }
                  final s = subjects[i];
                  return SubjectTile(
                    key: Key('tile_${s.id}'),
                    emoji: s.emoji,
                    title: s.titleIn(profile.language),
                    color: s.color,
                    compactLabel: profile.ageGroup.isJunior,
                    badge: progress.currentLevels.containsKey(s.id)
                        ? '${progress.levelOf(s.id)}'
                        : null,
                    onTap: () => _openSubject(s),
                  );
                },
              ),
            ),
          ],
        ),
      ),
      ),
    );
  }
}

class _Header extends StatelessWidget {
  const _Header({required this.profile, required this.stars, required this.streak});

  final ChildProfile profile;
  final int stars;
  final int streak;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(8, 8, 12, 8),
      child: Row(
        children: [
          IconButton(
            key: const Key('home_back'),
            iconSize: 32,
            tooltip: Tr.of(context).profiles,
            onPressed: () => Navigator.of(context).maybePop(),
            icon: const Icon(Icons.arrow_back_rounded),
          ),
          ProfilePhoto(profile: profile, size: 52, showBadge: false),
          const SizedBox(width: 10),
          Expanded(
            child: Text(
              profile.name,
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
              style: Theme.of(context).textTheme.headlineSmall,
            ),
          ),
          StatChip(icon: '⭐', value: '$stars'),
          const SizedBox(width: 8),
          StatChip(icon: '🔥', value: '$streak', color: AppColors.gentle),
          const SizedBox(width: 4),
          // Ota-ona bo'limi: bosib turish + PIN (bola tasodifan kira olmaydi).
          Tooltip(
            message: Tr.of(context).parentHold,
            child: GestureDetector(
              key: const Key('home_parent_lock'),
              onLongPress: () => Navigator.of(context).pushNamed(AppRoutes.parentGate),
              child: const Padding(
                padding: EdgeInsets.all(8),
                child: Icon(Icons.lock_outline_rounded, color: AppColors.textSoft, size: 26),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// "▶ BUGUNGI DARSim" — har kuni fanlar aralash qisqa dars (takrorlash bilan).
class _DailyLessonCard extends StatelessWidget {
  const _DailyLessonCard({
    required this.done,
    required this.junior,
    required this.exercises,
    required this.color,
    required this.onTap,
  });

  final bool done;
  final bool junior;
  final int exercises;
  final Color color;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final t = Tr.of(context);
    final subtitle = done ? t.dailyDone : (junior ? t.dailyJunior(exercises) : t.dailySenior(exercises));
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 4, 16, 8),
      child: Material(
        color: done ? Colors.white : color,
        borderRadius: BorderRadius.circular(28),
        elevation: done ? 0 : 4,
        shadowColor: color.withAlpha(90),
        child: InkWell(
          key: const Key('daily_lesson_button'),
          borderRadius: BorderRadius.circular(28),
          onTap: onTap,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(28),
              border: done ? Border.all(color: color.withAlpha(120), width: 3) : null,
            ),
            child: Row(
              children: [
                Text(done ? '✅' : '▶️', style: const TextStyle(fontSize: 40)),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        t.dailyLesson,
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.w900,
                          color: done ? AppColors.text : Colors.white,
                        ),
                      ),
                      Text(
                        subtitle,
                        key: const Key('daily_lesson_subtitle'),
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w700,
                          color: done ? AppColors.textSoft : Colors.white.withAlpha(230),
                        ),
                      ),
                    ],
                  ),
                ),
                Icon(Icons.play_circle_fill_rounded, size: 44, color: done ? color : Colors.white),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
