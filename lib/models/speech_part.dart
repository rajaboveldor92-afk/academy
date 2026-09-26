/// Ketma-ket aytiladigan nutq bo'lagi: masalan, "Apple" (inglizcha) + "qaysi rasm?" (o'zbekcha).
/// [lang] — `uz`, `en` yoki `ru`.
class SpeechPart {
  const SpeechPart(this.text, this.lang);

  final String text;
  final String lang;

  @override
  String toString() => '$lang:$text';
}
