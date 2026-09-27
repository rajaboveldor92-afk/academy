import 'dart:math';

import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:flutter_tts/flutter_tts.dart';

import '../models/app_settings.dart';
import '../models/speech_part.dart';

export '../models/speech_part.dart';

/// Qisqa effekt ovozlari. Fayllar `assets/audio/rewards/<name>.ogg` (`tool/audio/make_sounds.py`).
enum SoundEffect { tap, correct, tryAgain, star, medal }

/// Til kodlari: `uz`, `en`, `ru`.
typedef LangCode = String;

/// Barcha audio shu servis orqali o'tadi.
///
/// Ishlash tartibi (`playWord` / `speak`):
/// 1. `assets/audio/<lang>/<key>.(mp3|ogg|m4a|wav)` fayli bo'lsa — o'sha ijro etiladi.
/// 2. Aks holda qurilmaning **offline** TTS ovozi matnni aytadi.
///
/// Shuning uchun keyinchalik haqiqiy ovoz yozuvlarini qo'shish uchun kodni
/// o'zgartirish shart emas — faylni to'g'ri nom bilan papkaga qo'yish kifoya.
abstract class AudioService {
  void applySettings(AppSettings settings);

  /// So'z yoki iborani aytadi. [key] — `assets/audio/<lang>/` ichidagi fayl nomi.
  Future<void> playWord(String text, {LangCode lang = 'uz', String? key});

  /// Faqat TTS orqali aytish.
  Future<void> speak(String text, {LangCode lang = 'uz'});

  /// Bir necha tildagi bo'laklarni ketma-ket aytadi (har biri o'z ovozida).
  /// Yangi `speak`/`speakParts` chaqirilsa, oldingisi to'xtaydi.
  Future<void> speakParts(List<SpeechPart> parts);

  Future<void> playEffect(SoundEffect effect);

  /// To'g'ri javobdan keyingi maqtov ("Barakalla!", "Great job!" ...).
  Future<void> praise({LangCode lang = 'uz'});

  /// Noto'g'ri javobdan keyingi yumshoq dalda.
  Future<void> encourage({LangCode lang = 'uz'});

  Future<void> stop();

  /// Ilova oldingi plandami. Fonga o'tganda nutq to'xtaydi, fon musiqasi pauza qilinadi.
  Future<void> setForeground(bool foreground);

  Future<void> dispose();
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
    'uz': ['uz-UZ', 'tr-TR', 'en-US'],
    'en': ['en-US', 'en-GB'],
    'ru': ['ru-RU'],
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
  final Map<LangCode, String?> _resolvedLocale = {};
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

  Future<String?> _localeFor(LangCode lang) async {
    if (_resolvedLocale.containsKey(lang)) return _resolvedLocale[lang];
    final tts = _ttsInstance();
    String? found;
    for (final locale in _ttsLocales[lang] ?? const <String>['en-US']) {
      try {
        final available = await tts.isLanguageAvailable(locale);
        if (available == true || available == 1) {
          found = locale;
          break;
        }
      } catch (_) {
        // Plagin mavjud bo'lmasa (masalan, testda) — keyingisini sinaymiz.
      }
    }
    _resolvedLocale[lang] = found;
    return found;
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

  @override
  Future<void> speak(String text, {LangCode lang = 'uz'}) async {
    if (!_voiceEnabled || text.trim().isEmpty) return;
    _speechToken++;
    try {
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
    final token = ++_speechToken;
    try {
      final tts = _ttsInstance();
      await tts.stop();
      await tts.awaitSpeakCompletion(true);
      for (final part in parts) {
        if (token != _speechToken) return;
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

  @override
  Future<void> praise({LangCode lang = 'uz'}) async => log.add('praise:$lang');

  @override
  Future<void> encourage({LangCode lang = 'uz'}) async => log.add('encourage:$lang');

  @override
  Future<void> stop() async {}

  @override
  Future<void> dispose() async {}
}
