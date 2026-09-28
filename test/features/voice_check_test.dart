import 'package:academy/core/providers.dart';
import 'package:academy/features/parent/voice_check_dialog.dart';
import 'package:academy/l10n/tr.dart';
import 'package:academy/services/audio_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

/// «Ovozni tekshirish»: telefonda qaysi til ovozi yo'qligi va qanday yoqish ko'rsatiladi.
void main() {
  testWidgets('rus ovozi yo‘q bo‘lsa — ogohlantirish va ko‘rsatma, sinab eshitish ishlaydi', (tester) async {
    final audio = SilentAudioService()..missingVoices.add('ru');
    await tester.pumpWidget(ProviderScope(
      overrides: [audioServiceProvider.overrideWithValue(audio)],
      child: MaterialApp(
        home: Builder(
          builder: (context) => Scaffold(
            body: TextButton(onPressed: () => VoiceCheckDialog.show(context), child: const Text('open')),
          ),
        ),
      ),
    ));
    await tester.tap(find.text('open'));
    await tester.pumpAndSettle();
    const t = Tr('uz');
    expect(find.byKey(const Key('voice_check_dialog')), findsOneWidget);
    expect(find.text(t.voiceMissing), findsOneWidget);
    expect(find.text('${t.voiceReady} (en-TEST)'), findsOneWidget);
    expect(find.text(t.voiceMother), findsOneWidget);
    expect(find.byKey(const Key('voice_how_to')), findsOneWidget);

    await tester.ensureVisible(find.byKey(const Key('voice_test_en')));
    await tester.pumpAndSettle();
    await tester.tap(find.byKey(const Key('voice_test_en')));
    await tester.pump();
    expect(audio.log, contains('speak:en:${t.voiceSample('en')}'));

    // Ovoz o'rnatildi — qayta tekshirish ogohlantirishni olib tashlaydi.
    audio.missingVoices.clear();
    await tester.tap(find.text(t.checkAgain));
    await tester.pumpAndSettle();
    expect(find.text(t.voiceMissing), findsNothing);
    expect(find.byKey(const Key('voice_how_to')), findsNothing);
  });
}
