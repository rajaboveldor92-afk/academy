import 'dart:async';
import 'dart:math';

import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:flutter_tts/flutter_tts.dart';

import '../models/app_settings.dart';
import '../models/speech_part.dart';
import 'cloned_voice.dart';
import 'mother_voice.dart';

export '../models/speech_part.dart';

/// Qisqa effekt ovozlari. Fayllar `assets/audio/rewards/<name>.ogg` (`tool/audio/make_sounds.py`).
enum SoundEffect { tap, correct, tryAgain, star, medal }

/// Til kodlari: `uz`, `en`, `ru`.
typedef LangCode = String;

/// Barcha audio shu servis orqali o'tadi.
///
/// Ishlash tartibi (`playWord` / `speak`):
/// 1. `assets/audio/<lang>/<key>.(mp3|ogg|m4a|wav)` fayli bo'lsa — o'sha ijro etiladi.
/// 2. O'zbekcha gap onaning yozib olingan iborasiga ([MotherVoice]) yoki klonlangan ovozdagi
///    tayyor faylga ([ClonedVoice]) mos kelsa — o'sha.
/// 3. Aks holda qurilmaning **offline** TTS ovozi matnni aytadi.
///
/// Shuning uchun keyinchalik haqiqiy ovoz yozuvlarini qo'shish uchun kodni
/// o'zgartirish shart emas — faylni to'g'ri nom bilan papkaga qo'yish kifoya.
abstract class AudioService {
  void applySettings(AppSettings settings);

  /// So'z yoki iborani aytadi. [key] — `assets/audio/<lang>/` ichidagi fayl nomi.
  Future<void> playWord(String text, {LangCode lang = 'uz', String? key});

  /// Faqat TTS orqali aytish.
  Future<void> speak(String text, {LangCode lang = 'uz'});

  /// Bir necha bo'lakni ketma-ket aytadi: har biri o'z tilidagi ovozda yoki yozib olingan
  /// ovozda ([SpeechPart.clip] — onaning ovozi). Yangi `speak`/`speakParts` chaqirilsa, oldingisi to'xtaydi.
  Future<void> speakParts(List<SpeechPart> parts);

  Future<void> playEffect(SoundEffect effect);

  /// To'g'ri javobdan keyingi maqtov ("Barakalla!", "Great job!" ...).
  Future<void> praise({LangCode lang = 'uz'});

  /// Noto'g'ri javobdan keyingi yumshoq dalda.
  Future<void> encourage({LangCode lang = 'uz'});

  Future<void> stop();

  /// Ilova oldingi plandami. Fonga o'tganda nutq to'xtaydi, fon musiqasi pauza qilinadi.
  Future<void> setForeground(bool foreground);

  /// Telefonning ovoz dasturidagi (TTS) shu til ovozi. `null` — ovoz yo'q
  /// (ota-ona «Ovozni tekshirish» oynasida ko'radi). Har chaqiruvda qayta tekshiriladi.
  Future<TtsVoice?> ttsVoice(LangCode lang);

  Future<void> dispose();
}

/// Telefon ovozi: [locale] (`ru-RU`), [installed] — ovoz ma'lumotlari telefonga yuklangan
/// (internetsiz ishlaydi). `false` bo'lsa, ovoz jim qolishi mumkin.
class TtsVoice {
  const TtsVoice(this.locale, {this.installed = true});

  final String locale;
  final bool installed;
}

/// Iboralar ro'yxati (spetsifikatsiyaning 21-bandi).
class FeedbackPhrases {
  FeedbackPhrases._();

  static const Map<String, List<String>> praise = {
    'uz': ['Barakalla!', 'Ajoyib!', "Zo‘r!", 'Juda yaxshi!', 'Qoyil!'],
    'en': ['Great job!', 'Excellent!', 'Well done!', 'Super!'],
    'ru': ['Молодец!', 'Отлично!', 'Умница!', 'Здорово!'],
  };

  static const Map<String, List<String>> encourage = {
    'uz': ["Yana urinib ko‘ramiz.", 'Deyarli topding!', "Boshqa variantni sinab ko‘r."],
    'en': ["Let's try again.", 'Almost!', 'Try another one.'],
    'ru': ['Попробуем ещё раз.', 'Почти!', 'Попробуй другой вариант.'],
  };

  static String randomPraise(LangCode lang, [Random? random]) =>
      _pick(praise[lang] ?? praise['uz']!, random);

  static String randomEncourage(LangCode lang, [Random? random]) =>
      _pick(encourage[lang] ?? encourage['uz']!, random);

  static String _pick(List<String> list, Random? random) =>
      list[(random ?? Random()).nextInt(list.length)];
}

/// Real qurilmadagi implementatsiya (audioplayers + flutter_tts).
class DeviceAudioService implements AudioService {
  DeviceAudioService({AssetBundle? bundle}) : _bundle = bundle ?? rootBundle;

  static const List<String> _extensions = ['mp3', 'ogg', 'm4a', 'wav'];

  /// TTS til zaxirasi: o'zbek ovozi bo'lmasa turkcha ovoz lotin yozuvini
  /// ancha to'g'ri o'qiydi.
  static const Map<LangCode, List<String>> _ttsLocales = {
    'uz': ['uz-UZ', 'uz', 'tr-TR', 'en-US'],
    'en': ['en-US', 'en-GB', 'en'],
    'ru': ['ru-RU', 'ru'],
  };

  /// Fon musiqasi ovozi past (nutq va effektlar aniq eshitilsin).
  static const double musicVolume = 0.22;
  static const double effectVolume = 0.7;

  /// Effekt va musiqa audio fokusni olmaydi: bir-birini va TTS ni to'xtatib qo'ymaydi.
  static final AudioContext _mixContext = AudioContext(
    android: const AudioContextAndroid(
      audioFocus: AndroidAudioFocus.none,
      usageType: AndroidUsageType.game,
      contentType: AndroidContentType.music,
    ),
  );

  final AssetBundle _bundle;
  final AudioPlayer _voicePlayer = AudioPlayer();
  final AudioPlayer _effectPlayer = AudioPlayer();
  final AudioPlayer _musicPlayer = AudioPlayer();
  bool _playersReady = false;
  FlutterTts? _tts;
  Set<String>? _assets;
  final Map<LangCode, String> _resolvedLocale = {};
  final Map<LangCode, bool> _localeInstalled = {};

  /// Ovozi topilmagan til qachon tekshirilgani: ota-ona ovozni o'rnatib qaytsa, qayta tekshiriladi.
  final Map<LangCode, DateTime> _missingSince = {};
  String? _currentLocale;

  bool _soundEnabled = true;
  bool _voiceEnabled = true;
  bool _musicEnabled = false;
  bool _foreground = true;
  bool _musicOn = false;

  @override
  void applySettings(AppSettings settings) {
    _soundEnabled = settings.soundEnabled;
    _voiceEnabled = settings.voiceEnabled;
    _musicEnabled = settings.musicEnabled;
    _syncMusic();
  }

  Future<void> _preparePlayers() async {
    if (_playersReady) return;
    _playersReady = true;
    try {
      await _effectPlayer.setAudioContext(_mixContext);
      await _effectPlayer.setVolume(effectVolume);
      await _musicPlayer.setAudioContext(_mixContext);
      await _musicPlayer.setReleaseMode(ReleaseMode.loop);
      await _musicPlayer.setVolume(musicVolume);
    } catch (e) {
      debugPrint('AudioService: pleyer sozlanmadi: $e');
    }
  }

  /// Fon musiqasi: sozlamada yoqilgan va ilova oldingi planda bo'lsa — aylanib chaladi.
  Future<void> _syncMusic() async {
    final want = _musicEnabled && _foreground;
    if (want == _musicOn) return;
    _musicOn = want;
    try {
      await _preparePlayers();
      if (want) {
        if (_musicPlayer.state == PlayerState.paused) {
          await _musicPlayer.resume();
        } else {
          final path = await _findAsset('music', 'theme');
          if (path != null && _musicOn) await _musicPlayer.play(AssetSource(path));
        }
      } else {
        await _musicPlayer.pause();
      }
    } catch (e) {
      debugPrint('AudioService: musiqa xatosi: $e');
    }
  }

  @override
  Future<void> setForeground(bool foreground) async {
    if (_foreground == foreground) return;
    _foreground = foreground;
    if (!foreground) await stop();
    await _syncMusic();
  }

  Future<Set<String>> _assetSet() async {
    final cached = _assets;
    if (cached != null) return cached;
    try {
      final manifest = await AssetManifest.loadFromAssetBundle(_bundle);
      _assets = manifest.listAssets().toSet();
    } catch (e) {
      debugPrint('AudioService: asset manifest o\'qilmadi: $e');
      _assets = <String>{};
    }
    return _assets!;
  }

  /// `uz/olma` → `audio/uz/olma.mp3` (AssetSource `assets/` prefiksini o'zi qo'shadi).
  Future<String?> _findAsset(String folder, String key) async {
    final assets = await _assetSet();
    for (final ext in _extensions) {
      final path = 'assets/audio/$folder/$key.$ext';
      if (assets.contains(path)) return path.substring('assets/'.length);
    }
    return null;
  }

  Future<bool> _playAsset(AudioPlayer player, String folder, String key) async {
    final path = await _findAsset(folder, key);
    if (path == null) return false;
    try {
      await player.stop();
      await player.play(AssetSource(path));
      return true;
    } catch (e) {
      debugPrint('AudioService: $path ijro etilmadi: $e');
      return false;
    }
  }

  FlutterTts _ttsInstance() {
    final existing = _tts;
    if (existing != null) return existing;
    final tts = FlutterTts();
    _tts = tts;
    return tts;
  }

  Future<String?> _localeFor(LangCode lang, {bool fresh = false}) async {
    final cached = _resolvedLocale[lang];
    if (cached != null) return cached;
    final missing = _missingSince[lang];
    if (!fresh && missing != null && DateTime.now().difference(missing) < const Duration(seconds: 20)) return null;
    final tts = _ttsInstance();
    // Avval ovoz ma'lumotlari telefonga yuklangan variant; bunday bo'lmasa — birinchi mavjud variant
    // (ba'zi dvigatellar "yuklanganmi" savoliga javob bermaydi).
    String? installed, available;
    for (final locale in _ttsLocales[lang] ?? const <String>['en-US']) {
      try {
        final ok = await tts.isLanguageAvailable(locale);
        if (ok != true && ok != 1) continue;
        available ??= locale;
        if (defaultTargetPlatform != TargetPlatform.android) {
          installed = locale;
          break;
        }
        final local = await tts.isLanguageInstalled(locale);
        if (local == true || local == 1) {
          installed = locale;
          break;
        }
      } catch (_) {
        // Plagin mavjud bo'lmasa (masalan, testda) — keyingisini sinaymiz.
      }
    }
    final found = installed ?? available;
    _localeInstalled[lang] = installed != null;
    if (found == null) {
      _missingSince[lang] = DateTime.now();
    } else {
      _resolvedLocale[lang] = found;
      _missingSince.remove(lang);
    }
    return found;
  }

  @override
  Future<TtsVoice?> ttsVoice(LangCode lang) async {
    _resolvedLocale.remove(lang);
    final locale = await _localeFor(lang, fresh: true);
    if (locale == null) return null;
    return TtsVoice(locale, installed: _localeInstalled[lang] ?? true);
  }

  /// Fayl nomi uchun xavfsiz kalit: `Olma` → `olma`, `Яблоко` → `яблоко`.
  static String keyFor(String text) =>
      text.trim().toLowerCase().replaceAll(RegExp(r"[\s'’`ʻ]+"), '_').replaceAll(RegExp(r'[!?.,]'), '');

  @override
  Future<void> playWord(String text, {LangCode lang = 'uz', String? key}) async {
    if (!_voiceEnabled) return;
    final fileKey = key ?? keyFor(text);
    if (await _playAsset(_voicePlayer, lang, fileKey)) return;
    await speak(text, lang: lang);
  }

  /// Har yangi nutq so'rovi raqamni oshiradi — eski ketma-ketlik to'xtaydi.
  int _speechToken = 0;

  Future<bool> _prepare(LangCode lang) async {
    final locale = await _localeFor(lang);
    if (locale == null) return false;
    final tts = _ttsInstance();
    if (_currentLocale != locale) {
      await tts.setLanguage(locale);
      await tts.setSpeechRate(0.42);
      await tts.setPitch(1.1);
      _currentLocale = locale;
    }
    return true;
  }

  /// Yozib olingan ibora tugashini kutish (yangi nutq so'ralsa darhol bo'shatiladi).
  Completer<void>? _clipWait;

  void _interrupt() {
    _speechToken++;
    final wait = _clipWait;
    _clipWait = null;
    if (wait != null && !wait.isCompleted) wait.complete();
  }

  /// Onaning ovozidagi iborani oxirigacha ijro etadi. Fayl bo'lmasa `false`.
  Future<bool> _playClip(String key, int token) => _playClipAt(MotherVoice.folder, key, token);

  /// O'zbekcha gap uchun tayyor yozuv: onaning haqiqiy iborasi yoki klonlangan ovozdagi fayl.
  Future<(String, String)?> _recordedFor(String text) async {
    final mother = MotherVoice.clipForText(text);
    if (mother != null && await _findAsset(MotherVoice.folder, mother) != null) return (MotherVoice.folder, mother);
    final key = ClonedVoice.keyFor(text);
    if (await _findAsset(ClonedVoice.folder, key) != null) return (ClonedVoice.folder, key);
    return null;
  }

  /// [folder] dagi yozuvni oxirigacha ijro etadi. Fayl bo'lmasa `false`.
  Future<bool> _playClipAt(String folder, String key, int token) async {
    final path = await _findAsset(folder, key);
    if (path == null) return false;
    if (token != _speechToken) return true;
    final wait = Completer<void>();
    _clipWait = wait;
    final sub = _voicePlayer.onPlayerComplete.listen((_) {
      if (!wait.isCompleted) wait.complete();
    });
    try {
      await _voicePlayer.stop();
      if (token != _speechToken) return true;
      await _voicePlayer.play(AssetSource(path));
      await wait.future.timeout(const Duration(seconds: 30), onTimeout: () {});
    } catch (e) {
      debugPrint('AudioService: $path ijro etilmadi: $e');
    } finally {
      await sub.cancel();
      if (identical(_clipWait, wait)) _clipWait = null;
    }
    return true;
  }

  @override
  Future<void> speak(String text, {LangCode lang = 'uz'}) async {
    if (!_voiceEnabled || text.trim().isEmpty) return;
    _interrupt();
    final token = _speechToken;
    try {
      if (lang == 'uz') {
        final recorded = await _recordedFor(text);
        if (token != _speechToken) return;
        if (recorded != null) {
          await _tts?.stop();
          await _playClipAt(recorded.$1, recorded.$2, token);
          return;
        }
      }
      await _voicePlayer.stop();
      if (!await _prepare(lang)) return;
      final tts = _ttsInstance();
      await tts.awaitSpeakCompletion(false);
      await tts.stop();
      await tts.speak(text);
    } catch (e) {
      debugPrint('AudioService: TTS xatosi: $e');
    }
  }

  @override
  Future<void> speakParts(List<SpeechPart> parts) async {
    if (!_voiceEnabled || parts.isEmpty) return;
    _interrupt();
    final token = _speechToken;
    try {
      await _voicePlayer.stop();
      final tts = _ttsInstance();
      await tts.stop();
      await tts.awaitSpeakCompletion(true);
      for (final part in parts) {
        if (token != _speechToken) return;
        final clip = part.clip;
        if (clip != null && await _playClip(clip, token)) continue;
        if (token != _speechToken) return;
        if (clip == null && part.lang == 'uz') {
          final recorded = await _recordedFor(part.text);
          if (token != _speechToken) return;
          if (recorded != null && await _playClipAt(recorded.$1, recorded.$2, token)) continue;
          if (token != _speechToken) return;
        }
        if (part.text.trim().isEmpty || !await _prepare(part.lang)) continue;
        if (token != _speechToken) return;
        await tts.speak(part.text);
      }
    } catch (e) {
      debugPrint('AudioService: TTS xatosi: $e');
    } finally {
      if (token == _speechToken) {
        try {
          await _tts?.awaitSpeakCompletion(false);
        } catch (_) {}
      }
    }
  }

  @override
  Future<void> playEffect(SoundEffect effect) async {
    if (!_soundEnabled) return;
    await _preparePlayers();
    await _playAsset(_effectPlayer, 'rewards', effect.name);
  }

  @override
  Future<void> praise({LangCode lang = 'uz'}) async {
    await playEffect(SoundEffect.correct);
    await speak(FeedbackPhrases.randomPraise(lang), lang: lang);
  }

  @override
  Future<void> encourage({LangCode lang = 'uz'}) async {
    await playEffect(SoundEffect.tryAgain);
    await speak(FeedbackPhrases.randomEncourage(lang), lang: lang);
  }

  @override
  Future<void> stop() async {
    _interrupt();
    try {
      await _voicePlayer.stop();
      await _tts?.stop();
    } catch (_) {}
  }

  @override
  Future<void> dispose() async {
    try {
      await _voicePlayer.dispose();
      await _effectPlayer.dispose();
      await _musicPlayer.dispose();
      await _tts?.stop();
    } catch (_) {}
  }
}

/// Testlar va ovozsiz rejim uchun: hech narsa ijro etmaydi, faqat qayd qiladi.
class SilentAudioService implements AudioService {
  final List<String> log = [];

  @override
  void applySettings(AppSettings settings) {}

  @override
  Future<void> playWord(String text, {LangCode lang = 'uz', String? key}) async =>
      log.add('word:$lang:$text');

  @override
  Future<void> speak(String text, {LangCode lang = 'uz'}) async => log.add('speak:$lang:$text');

  @override
  Future<void> speakParts(List<SpeechPart> parts) async => log.add('parts:${parts.join('|')}');

  @override
  Future<void> playEffect(SoundEffect effect) async => log.add('effect:${effect.name}');

  @override
  Future<void> setForeground(bool foreground) async => log.add('foreground:$foreground');

  /// Testlarda: [missingVoices] dagi tillar uchun ovoz yo'q.
  final Set<LangCode> missingVoices = {};

  @override
  Future<TtsVoice?> ttsVoice(LangCode lang) async => missingVoices.contains(lang) ? null : TtsVoice('$lang-TEST');

  @override
  Future<void> praise({LangCode lang = 'uz'}) async => log.add('praise:$lang');

  @override
  Future<void> encourage({LangCode lang = 'uz'}) async => log.add('encourage:$lang');

  @override
  Future<void> stop() async {}

  @override
  Future<void> dispose() async {}
}
