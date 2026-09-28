import 'dart:async';
import 'dart:typed_data';

import 'package:academy/models/app_settings.dart';
import 'package:academy/services/audio_service.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_tts/flutter_tts.dart';

class _Bundle extends CachingAssetBundle {
  @override
  Future<ByteData> load(String key) async => const StandardMessageCodec().encodeMessage({
    'assets/audio/uz/ona/barakalla.ogg': [ {'asset': 'assets/audio/uz/ona/barakalla.ogg'} ],
  })!;
}

class _Player implements AudioPlayer {
  int plays = 0;
  @override
  Stream<void> get onPlayerComplete => const Stream<void>.empty();
  @override
  dynamic noSuchMethod(Invocation invocation) {
    if (invocation.memberName == #play) {
      plays++;
      return Future<void>.error(StateError('broken recording'));
    }
    return Future<void>.value();
  }
}

class _Tts implements FlutterTts {
  final List<String> checked = [];
  final List<String> spoken = [];
  bool available = true;
  Completer<bool>? pending;
  final queried = Completer<void>();
  @override
  dynamic noSuchMethod(Invocation invocation) {
    if (invocation.memberName == #isLanguageAvailable) {
      checked.add(invocation.positionalArguments.first as String);
      if (!queried.isCompleted) queried.complete();
      return pending?.future ?? Future<dynamic>.value(available);
    }
    if (invocation.memberName == #isLanguageInstalled) return Future<dynamic>.value(true);
    if (invocation.memberName == #speak) spoken.add(invocation.positionalArguments.first as String);
    return Future<dynamic>.value(1);
  }
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  late _Tts tts;
  late _Player player;
  late DeviceAudioService audio;
  setUp(() {
    tts = _Tts();
    player = _Player();
    audio = DeviceAudioService(bundle: _Bundle(), tts: tts, voicePlayer: player);
  });

  test('missing Uzbek voice never selects Turkish or English', () async {
    tts.available = false;
    expect(await audio.ttsVoice('uz'), isNull);
    expect(tts.checked, ['uz-UZ', 'uz']);
    tts.available = true;
    expect((await audio.ttsVoice('uz'))!.locale, 'uz-UZ');
  });

  test('broken recorded phrase falls back to Uzbek TTS', () async {
    await audio.speak('Barakalla!');
    expect(player.plays, 1);
    expect(tts.spoken, ['Barakalla!']);
  });

  test('stop during delayed voice lookup prevents stale speech', () async {
    tts.pending = Completer<bool>();
    final speaking = audio.speak('Hello', lang: 'en');
    await tts.queried.future;
    await audio.stop();
    tts.pending!.complete(true);
    await speaking;
    expect(tts.spoken, isEmpty);
  });

  test('background and disabled voice block every speech entry point', () async {
    await audio.setForeground(false);
    await audio.speak('Hello', lang: 'en');
    await audio.playWord('Hello', lang: 'en');
    await audio.speakParts([const SpeechPart('Hello', 'en')]);
    await audio.setForeground(true);
    audio.applySettings(const AppSettings(voiceEnabled: false));
    await audio.speak('Hello', lang: 'en');
    expect(tts.spoken, isEmpty);
    expect(player.plays, 0);
  });
}
