import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../models/child_profile.dart';
import '../../router/app_router.dart';
import '../../theme/app_colors.dart';
import '../../widgets/avatar_bubble.dart';
import '../../widgets/pressable_scale.dart';
import '../session/session_controller.dart';
import 'profiles_controller.dart';

/// "Kim o'ynaydi?" — profil tanlash ekrani.
class ProfileSelectScreen extends ConsumerStatefulWidget {
  const ProfileSelectScreen({super.key});

  @override
  ConsumerState<ProfileSelectScreen> createState() => _ProfileSelectScreenState();
}

class _ProfileSelectScreenState extends ConsumerState<ProfileSelectScreen> {
  bool _opening = false;

  Future<void> _openProfile(ChildProfile profile) async {
    if (_opening) return;
    _opening = true;
    try {
      ref.read(activeChildIdProvider.notifier).select(profile.id);
      ref.read(audioServiceProvider).playWord(profile.name);
      await ref.read(sessionProvider.notifier).start(profile.id);
      if (!mounted) return;
      final limitReached = ref.read(sessionProvider).limitReached;
      await Navigator.of(context).pushNamed(limitReached ? AppRoutes.timeUp : AppRoutes.home);
      // Bosh sahifadan qaytildi — sessiyani yopamiz.
      if (!mounted) return;
      await ref.read(sessionProvider.notifier).stop();
      ref.read(activeChildIdProvider.notifier).clear();
    } finally {
      _opening = false;
    }
  }

  @override
  Widget build(BuildContext context) {
    final profiles = ref.watch(profilesProvider);
    final width = MediaQuery.sizeOf(context).width;
    final columns = width >= 900 ? 4 : (width >= 600 ? 3 : 2);

    return Scaffold(
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 12, 8, 0),
              child: Row(
                children: [
                  IconButton(
                    iconSize: 32,
                    tooltip: 'Tinglash',
                    onPressed: () =>
                        ref.read(audioServiceProvider).speak("Kim o'ynaydi?"),
                    icon: const Icon(Icons.volume_up_rounded, color: AppColors.primary),
                  ),
                  Expanded(
                    child: Text(
                      "Kim o'ynaydi?",
                      textAlign: TextAlign.center,
                      style: Theme.of(context).textTheme.displaySmall,
                    ),
                  ),
                  IconButton(
                    key: const Key('parent_button'),
                    iconSize: 30,
                    tooltip: 'Ota-ona',
                    onPressed: () => Navigator.of(context).pushNamed(AppRoutes.parentGate),
                    icon: const Icon(Icons.lock_rounded, color: AppColors.parent),
                  ),
                ],
              ),
            ),
            Expanded(
              child: profiles.isEmpty
                  ? const _EmptyProfiles()
                  : GridView.builder(
                      padding: const EdgeInsets.all(20),
                      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                        crossAxisCount: columns,
                        mainAxisSpacing: 20,
                        crossAxisSpacing: 20,
                        childAspectRatio: 0.82,
                      ),
                      itemCount: profiles.length,
                      itemBuilder: (context, i) => _ProfileCard(
                        profile: profiles[i],
                        onTap: () => _openProfile(profiles[i]),
                      ),
                    ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
              child: SizedBox(
                width: double.infinity,
                child: FilledButton.icon(
                  key: const Key('new_profile_button'),
                  style: FilledButton.styleFrom(backgroundColor: AppColors.success),
                  onPressed: () => Navigator.of(context).pushNamed(AppRoutes.profileEditor),
                  icon: const Icon(Icons.add_rounded, size: 30),
                  label: const Text('Yangi profil'),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _ProfileCard extends StatelessWidget {
  const _ProfileCard({required this.profile, required this.onTap});

  final ChildProfile profile;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final color = AppColors.profileColor(profile.colorIndex);
    return PressableScale(
      onTap: onTap,
      semanticLabel: profile.name,
      child: Container(
        key: Key('profile_${profile.id}'),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(32),
          border: Border.all(color: color, width: 4),
          boxShadow: [
            BoxShadow(color: color.withAlpha(50), blurRadius: 14, offset: const Offset(0, 6)),
          ],
        ),
        padding: const EdgeInsets.all(12),
        child: LayoutBuilder(
          builder: (context, c) {
            final avatarSize = c.maxWidth * 0.55;
            return Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                AvatarBubble(avatar: profile.avatar, color: color, size: avatarSize),
                const SizedBox(height: 10),
                Text(
                  profile.name,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                Text(
                  '${profile.age} yosh',
                  style: Theme.of(context)
                      .textTheme
                      .titleMedium
                      ?.copyWith(color: AppColors.textSoft),
                ),
              ],
            );
          },
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
          "Hali profil yo'q.\nPastdagi tugma orqali yangi profil yarating.",
          textAlign: TextAlign.center,
          style: Theme.of(context).textTheme.titleMedium,
        ),
      ),
    );
  }
}
