import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../l10n/tr.dart';
import '../../services/audio_service.dart';
import '../../theme/app_colors.dart';

/// «Ovozni tekshirish»: telefonda o'zbek, rus va ingliz tili ovozi bormi — har birini sinab eshitish.
///
/// Ruscha va inglizcha so'zlarni telefonning TTS dasturi o'qiydi; ovoz yo'q bo'lsa so'zlar jim qoladi.
/// Ota-ona shu yerda sababni ko'radi va qanday yoqishni o'qiydi.
class VoiceCheckDialog extends ConsumerStatefulWidget {
  const VoiceCheckDialog({super.key, required this.t});

  /// Ota-ona bo'limi tili (dialog ekran ustida ochiladi).
  final Tr t;

  static Future<void> show(BuildContext context) {
    final t = Tr.of(context);
    return showDialog<void>(context: context, builder: (_) => VoiceCheckDialog(t: t));
  }

  @override
  ConsumerState<VoiceCheckDialog> createState() => _VoiceCheckDialogState();
}

class _VoiceCheckDialogState extends ConsumerState<VoiceCheckDialog> {
  final Map<String, TtsVoice?> _voices = {};
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _check();
  }

  Future<void> _check() async {
    setState(() => _loading = true);
    final audio = ref.read(audioServiceProvider);
    final result = <String, TtsVoice?>{};
    for (final lang in Tr.languages) {
      result[lang] = await audio.ttsVoice(lang);
    }
    if (!mounted) return;
    setState(() {
      _voices
        ..clear()
        ..addAll(result);
      _loading = false;
    });
  }

  String _status(TtsVoice? v) {
    final t = widget.t;
    if (v == null) return t.voiceMissing;
    return v.installed ? '${t.voiceReady} (${v.locale})' : '${t.voiceNotDownloaded} (${v.locale})';
  }

  @override
  Widget build(BuildContext context) {
    final t = widget.t;
    final missing = _voices.entries.any((e) => e.key != 'uz' && (e.value == null || !e.value!.installed));
    return AlertDialog(
      key: const Key('voice_check_dialog'),
      title: Text(t.voiceCheck),
      content: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(t.voiceCheckHint, style: const TextStyle(color: AppColors.textSoft)),
            const SizedBox(height: 12),
            if (_loading)
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 16),
                child: Row(children: [
                  const SizedBox(width: 22, height: 22, child: CircularProgressIndicator(strokeWidth: 3)),
                  const SizedBox(width: 12),
                  Text(t.voiceChecking),
                ]),
              )
            else
              for (final lang in Tr.languages)
                Padding(
                  padding: const EdgeInsets.only(bottom: 10),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(t.langName(lang), style: const TextStyle(fontWeight: FontWeight.w800)),
                            if (lang == 'uz') ...[
                              Text(t.voiceMother, style: const TextStyle(fontSize: 13)),
                              Text(t.voiceRest(_status(_voices[lang])), style: const TextStyle(fontSize: 13)),
                            ] else
                              Text(_status(_voices[lang]), key: Key('voice_status_$lang'), style: const TextStyle(fontSize: 13)),
                          ],
                        ),
                      ),
                      IconButton(
                        key: Key('voice_test_$lang'),
                        tooltip: t.listen,
                        icon: const Icon(Icons.volume_up_rounded, color: AppColors.primary),
                        onPressed: () => ref.read(audioServiceProvider).speak(t.voiceSample(lang), lang: lang),
                      ),
                    ],
                  ),
                ),
            if (!_loading && missing) ...[
              const SizedBox(height: 4),
              Text(t.voiceHowTo, key: const Key('voice_how_to'), style: const TextStyle(fontSize: 13)),
            ],
          ],
        ),
      ),
      actions: [
        TextButton(onPressed: _loading ? null : _check, child: Text(t.checkAgain)),
        TextButton(onPressed: () => Navigator.of(context).pop(), child: Text(t.close)),
      ],
    );
  }
}
