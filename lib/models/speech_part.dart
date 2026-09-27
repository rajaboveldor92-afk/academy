/// Ketma-ket aytiladigan nutq bo'lagi: masalan, "Apple" (inglizcha) + "qaysi rasm?" (o'zbekcha).
/// [lang] — `uz`, `en` yoki `ru`.
///
/// [clip] berilgan bo'lsa — yozib olingan ovoz (`assets/audio/uz/ona/<clip>.ogg`) ijro etiladi;
/// fayl topilmasa [text] qurilma ovozida (TTS) aytiladi.
class SpeechPart {
  const SpeechPart(this.text, this.lang, {this.clip});

  final String text;
  final String lang;
  final String? clip;

  @override
  String toString() => clip != null ? 'clip:$clip' : '$lang:$text';
}
