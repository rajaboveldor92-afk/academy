import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../l10n/lang_providers.dart';
import '../../l10n/tr.dart';
import '../../services/mother_voice.dart';
import '../../theme/app_colors.dart';

/// Kunlik limit tugaganda ko'rsatiladigan mehribon xabar.
class TimeUpScreen extends ConsumerStatefulWidget {
  const TimeUpScreen({super.key});


  @override
  ConsumerState<TimeUpScreen> createState() => _TimeUpScreenState();
}

class _TimeUpScreenState extends ConsumerState<TimeUpScreen> {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final lang = ref.read(childLangProvider);
      final audio = ref.read(audioServiceProvider);
      // O'zbekchada onaning ovozida: "Bugun juda yaxshi harakat qilding. Endi biroz dam olamiz."
      if (lang == 'uz') {
        audio.speakParts(MotherVoice.parts(['bugun_yaxshi_harakat', 'dam_olamiz']));
      } else {
        audio.speak(Tr(lang).timeUp, lang: lang);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final t = Tr(ref.watch(childLangProvider));
    return LangScope(
      lang: t.lang,
      child: Scaffold(
      backgroundColor: AppColors.secondary.withAlpha(60),
      body: SafeArea(
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(28),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Text('🌙⭐', style: TextStyle(fontSize: 96)),
                const SizedBox(height: 24),
                Text(
                  t.timeUp,
                  key: const Key('time_up_message'),
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.headlineMedium,
                ),
                const SizedBox(height: 40),
                FilledButton.icon(
                  onPressed: () => Navigator.of(context).maybePop(),
                  icon: const Icon(Icons.people_alt_rounded),
                  label: Text(t.backToProfiles),
                ),
              ],
            ),
          ),
        ),
      ),
      ),
    );
  }
}
