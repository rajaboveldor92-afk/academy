import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../models/child_profile.dart';
import '../../router/app_router.dart';
import '../../services/audio_service.dart';
import '../../theme/app_colors.dart';
import '../../theme/profile_themes.dart';
import '../../widgets/pressable_scale.dart';
import '../../widgets/profile_photo.dart';
import '../../widgets/star_burst.dart';
import '../session/session_controller.dart';
import 'profiles_controller.dart';
import '../../l10n/tr.dart';

/// "Kim o'ynaydi?" — profil tanlash ekrani.
///
/// Har bir bola uchun katta, o'z mavzusidagi karta: markazda katta yumaloq
/// rasm, ostida to'liq ism va yosh. 4 yoshli bola o'qimasdan ham rasmi va
/// kartaning rangi/belgisi orqali o'z profilini topadi.
class ProfileSelectScreen extends ConsumerStatefulWidget {
  const ProfileSelectScreen({super.key});

  /// Tanlash animatsiyasi davomiyligi (keyin bosh sahifa ochiladi).
  static const Duration selectDelay = Duration(milliseconds: 700);

  @override
  ConsumerState<ProfileSelectScreen> createState() => _ProfileSelectScreenState();
}

class _ProfileSelectScreenState extends ConsumerState<ProfileSelectScreen> {
  String? _selectedId;

  Future<void> _openProfile(ChildProfile profile) async {
    if (_selectedId != null) return;
    setState(() => _selectedId = profile.id);
    ref.read(audioServiceProvider).playEffect(SoundEffect.star);
    try {
      ref.read(activeChildIdProvider.notifier).select(profile.id);
      await Future.wait([
        ref.read(sessionProvider.notifier).start(profile.id),
        Future<void>.delayed(ProfileSelectScreen.selectDelay),
      ]);
      if (!mounted) return;
      final limitReached = ref.read(sessionProvider).limitReached;
      final navigation =
          Navigator.of(context).pushNamed(limitReached ? AppRoutes.timeUp : AppRoutes.home);
      // Keyingi ekran ochilgach tanlov holatini tozalaymiz.
      Future<void>.delayed(const Duration(milliseconds: 400), () {
        if (mounted) setState(() => _selectedId = null);
      });
      await navigation;
      // Bosh sahifadan qaytildi — sessiyani yopamiz.
      if (!mounted) return;
      await ref.read(sessionProvider.notifier).stop();
      ref.read(activeChildIdProvider.notifier).clear();
    } finally {
      if (mounted && _selectedId != null) setState(() => _selectedId = null);
    }
  }

  @override
  Widget build(BuildContext context) {
    final profiles = ref.watch(profilesProvider);
    final t = Tr.of(context);

    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(8, 8, 8, 0),
              child: Row(
                children: [
                  IconButton(
                    iconSize: 32,
                    tooltip: t.listen,
                    onPressed: () => ref.read(audioServiceProvider).speak(t.whoPlays, lang: t.lang),
                    icon: const Icon(Icons.volume_up_rounded, color: AppColors.primary),
                  ),
                  Expanded(
                    child: Text(
                      t.whoPlays,
                      textAlign: TextAlign.center,
                      style: Theme.of(context).textTheme.headlineMedium,
                    ),
                  ),
                  IconButton(
                    key: const Key('parent_button'),
                    iconSize: 30,
                    tooltip: t.parent,
                    onPressed: () => Navigator.of(context).pushNamed(AppRoutes.parentGate),
                    icon: const Icon(Icons.lock_rounded, color: AppColors.parent),
                  ),
                ],
              ),
            ),
            Expanded(
              child: profiles.isEmpty
                  ? const _EmptyProfiles()
                  : LayoutBuilder(
                      builder: (context, constraints) {
                        const padding = 16.0;
                        const spacing = 16.0;
                        final width = constraints.maxWidth;
                        final columns = width >= 1000 ? 3 : (width >= 640 ? 2 : 1);
                        final rowsOnScreen = columns == 1
                            ? (profiles.length >= 2 ? 2 : 1)
                            : 1;
                        final available =
                            constraints.maxHeight - padding * 2 - spacing * (rowsOnScreen - 1);
                        final cardHeight = (available / rowsOnScreen).clamp(240.0, 460.0).toDouble();

                        return GridView.builder(
                          padding: const EdgeInsets.all(padding),
                          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                            crossAxisCount: columns,
                            mainAxisSpacing: spacing,
                            crossAxisSpacing: spacing,
                            mainAxisExtent: cardHeight,
                          ),
                          itemCount: profiles.length,
                          itemBuilder: (context, i) {
                            final p = profiles[i];
                            return ProfileCard(
                              profile: p,
                              selected: _selectedId == p.id,
                              dimmed: _selectedId != null && _selectedId != p.id,
                              onTap: () => _openProfile(p),
                            );
                          },
                        );
                      },
                    ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 0, 20, 12),
              child: TextButton.icon(
                key: const Key('new_profile_button'),
                onPressed: () => Navigator.of(context)
                    .pushNamed(AppRoutes.parentGate, arguments: AppRoutes.profileEditor),
                icon: const Icon(Icons.add_circle_outline_rounded),
                label: Text(t.newProfileParent),
                style: TextButton.styleFrom(foregroundColor: AppColors.textSoft),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Bitta bola kartasi.
class ProfileCard extends StatelessWidget {
  const ProfileCard({
    super.key,
    required this.profile,
    required this.onTap,
    this.selected = false,
    this.dimmed = false,
  });

  final ChildProfile profile;
  final VoidCallback onTap;
  final bool selected;
  final bool dimmed;

  @override
  Widget build(BuildContext context) {
    final theme = ProfileThemes.of(profile.colorIndex);

    return AnimatedOpacity(
      duration: const Duration(milliseconds: 250),
      opacity: dimmed ? 0.45 : 1,
      child: AnimatedScale(
        duration: const Duration(milliseconds: 250),
        curve: Curves.easeOutBack,
        scale: selected ? 1.04 : 1,
        child: PressableScale(
          onTap: onTap,
          semanticLabel: '${profile.displayFullName}, ${Tr.of(context).years(profile.age)}',
          child: Container(
            key: Key('profile_${profile.id}'),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(36),
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: theme.gradient,
              ),
              border: Border.all(color: Colors.white, width: 4),
              boxShadow: [
                BoxShadow(
                  color: theme.primary.withAlpha(selected ? 120 : 55),
                  blurRadius: selected ? 28 : 14,
                  offset: const Offset(0, 8),
                ),
              ],
            ),
            child: LayoutBuilder(
              builder: (context, c) {
                final photoSize = (c.maxHeight * 0.5 < c.maxWidth * 0.62
                        ? c.maxHeight * 0.5
                        : c.maxWidth * 0.62)
                    .clamp(110.0, 280.0)
                    .toDouble();
                final nameSize = (c.maxHeight * 0.075).clamp(18.0, 28.0).toDouble();
                return Stack(
                  alignment: Alignment.center,
                  children: [
                    // Fondagi katta mavzu belgisi — kartalarni bir-biridan ajratadi.
                    Positioned(
                      top: 10,
                      left: 16,
                      child: Opacity(
                        opacity: 0.35,
                        child: Text(theme.emoji, style: TextStyle(fontSize: c.maxHeight * 0.14)),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16, 14, 16, 14),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Stack(
                            alignment: Alignment.center,
                            clipBehavior: Clip.none,
                            children: [
                              ProfilePhoto(profile: profile, size: photoSize, glow: selected),
                              if (selected)
                                Positioned(
                                  left: -photoSize * 0.35,
                                  top: -photoSize * 0.35,
                                  child: StarBurst(size: photoSize * 1.7),
                                ),
                            ],
                          ),
                          SizedBox(height: c.maxHeight * 0.04),
                          Text(
                            profile.displayFullName,
                            textAlign: TextAlign.center,
                            maxLines: 2,
                            overflow: TextOverflow.ellipsis,
                            style: TextStyle(
                              fontSize: nameSize,
                              height: 1.15,
                              fontWeight: FontWeight.w900,
                              color: AppColors.text,
                            ),
                          ),
                          const SizedBox(height: 6),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
                            decoration: BoxDecoration(
                              color: Colors.white.withAlpha(200),
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Text(
                              Tr.of(context).years(profile.age),
                              style: TextStyle(
                                fontSize: nameSize * 0.7,
                                fontWeight: FontWeight.w700,
                                color: theme.primary,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                );
              },
            ),
          ),
        ),
      ),
    );
  }
}

class _EmptyProfiles extends StatelessWidget {
  const _EmptyProfiles();

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(32),
        child: Text(
          Tr.of(context).noProfiles,
          textAlign: TextAlign.center,
          style: Theme.of(context).textTheme.titleMedium,
        ),
      ),
    );
  }
}
