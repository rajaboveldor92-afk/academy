import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../models/child_profile.dart';
import '../../models/subject.dart';
import '../../router/app_router.dart';
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
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final profile = ref.read(activeProfileProvider);
      if (profile != null) {
        // Yumshoq ovozli salomlashuv: faqat qisqa ism bilan.
        ref
            .read(audioServiceProvider)
            .speak('${profile.welcomeTitle} ${profile.welcomeSubtitle}');
      }
    });
  }

  void _onLimitReached() {
    final navigator = Navigator.of(context);
    navigator.popUntil((route) => route.settings.name == AppRoutes.home || route.isFirst);
    navigator.pushReplacementNamed(AppRoutes.timeUp);
  }

  void _openSubject(Subject subject) {
    ref.read(audioServiceProvider).playWord(
          subject.spokenName,
          lang: subject.speechLang,
          key: 'subject_${subject.id}',
        );
    Navigator.of(context).pushNamed(AppRoutes.subject, arguments: subject);
  }

  void _openAchievements() {
    ref.read(audioServiceProvider).speak('Yutuqlarim');
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

    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            _Header(
              profile: profile,
              stars: progress.stars,
              streak: progress.streak,
            ),
            GreetingBanner(profile: profile),
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
                      title: 'Yutuqlarim',
                      color: AppColors.star,
                      compactLabel: profile.ageGroup.isJunior,
                      onTap: _openAchievements,
                    );
                  }
                  final s = subjects[i];
                  return SubjectTile(
                    key: Key('tile_${s.id}'),
                    emoji: s.emoji,
                    title: s.title,
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
            tooltip: 'Profillar',
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
            message: "Ota-ona: bosib turing",
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
