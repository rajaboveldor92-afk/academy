import 'dart:convert';

/// Onaning klonlangan ovozi: `assets/audio/uz/klon/<kalit>.m4a`.
///
/// Onaning yozib olingan iboralari (`uz/ona`) asosida OmniVoice modeli bilan ilovadagi eng ko'p
/// ishlatiladigan o'zbekcha gaplar oldindan tayyorlangan (`tool/voice/`). Model ilovaga kirmaydi —
/// faqat tayyor audio fayllar. Fayl nomi — gap matnining FNV-1a (64 bit) xeshi:
/// Python tomonida ham aynan shu qoida (`tool/voice/voice_keys.py`).
class ClonedVoice {
  ClonedVoice._();

  static const String folder = 'uz/klon';

  static final RegExp _apostrophes = RegExp("[’ʻʼ'`]");
  static final RegExp _spaces = RegExp(r'\s+');

  /// Xesh uchun matn: bo'shliqlar bittaga, apostrof belgilari bir xil (‘).
  static String normalize(String text) => text.trim().replaceAll(_apostrophes, '‘').replaceAll(_spaces, ' ');

  /// FNV-1a 64 bit, 16 ta hex belgi. (Boshlang'ich qiymat 0xcbf29ce484222325 — ishorali 64 bitda.)
  static String keyFor(String text) {
    var h = -0x340d631b7bdddcdb;
    const prime = 0x100000001b3;
    for (final b in utf8.encode(normalize(text))) {
      h ^= b;
      h *= prime;
    }
    final high = (h >> 32) & 0xFFFFFFFF;
    final low = h & 0xFFFFFFFF;
    return high.toRadixString(16).padLeft(8, '0') + low.toRadixString(16).padLeft(8, '0');
  }
}
