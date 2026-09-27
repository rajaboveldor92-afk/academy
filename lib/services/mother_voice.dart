import '../learning/models/exercise.dart';
import '../models/child_profile.dart';
import '../models/speech_part.dart';

/// Onaning yozib olingan ovozi: `assets/audio/uz/ona/<kalit>.ogg`.
///
/// Iboralar `tool/audio/cut_mother_voice.py` bilan asl yozuvdan kesilgan
/// (vaqtlari: `tool/audio/mother_voice_clips.json`). Qaysi ibora qayerda aytilishi shu yerda
/// belgilanadi: salomlashuv, ko'rsatmalar, maslahatlar, maqtov, sanash, dars yakuni, dam olish.
/// Yozuv topilmasa matn qurilma ovozida (TTS) aytiladi.
class MotherVoice {
  MotherVoice._();

  static const String folder = 'uz/ona';

  /// Kalit → yozuvdagi matn (TTS zaxirasi va hujjat uchun).
  static const Map<String, String> clips = {
    'salom': 'Salom!',
    'azamjon': 'Azamjon',
    'muhammadjon': 'Muhammadjon',
    'keling_birga_oynaymiz': 'Keling, birga o‘ynaymiz.',
    'salom_azamjon': 'Salom, Azamjon, xush kelibsan!',
    'salom_muhammadjon': 'Salom, Muhammadjon, xush kelibsan!',
    'oynaymiz_organamiz': 'Keling, birga o‘ynaymiz va o‘rganamiz.',
    'qaysi_oyinni_tanlaymiz': 'Qaysi o‘yinni tanlaymiz?',
    'diqqat_bilan_tingla': 'Diqqat bilan tingla.',
    'yaxshilab_qara': 'Yaxshilab qara.',
    'togri_javobni_tanla': 'To‘g‘ri javobni tanla.',
    'yana_eshit': 'Yana bir marta eshit.',
    'davom_etamiz': 'Davom etamiz.',
    // Matematika
    'nechta_olma_bor': 'Nechta olma bor?',
    'sanab_kor': 'Sanab ko‘r.',
    'narsalarni_sanab_kor': 'Rasmdagi narsalarni sanab ko‘r.',
    'nechta_ekanini_top': 'Nechta ekanini top.',
    'mos_raqamni_tanla': 'Mos raqamni tanla.',
    'bir': 'Bir',
    'ikki': 'Ikki',
    'uch': 'Uch',
    'tort': 'To‘rt',
    'besh': 'Besh',
    'qizil_doirani_tanla': 'Qizil doirani tanla.',
    'qaysi_biri_kop': 'Qaysi biri ko‘p?',
    'qaysi_biri_kam': 'Qaysi biri kam?',
    'qaysilari_teng': 'Qaysilari teng?',
    'qaysi_son_katta': 'Qaysi son katta?',
    'qaysi_son_kichik': 'Qaysi son kichik?',
    'keyin_qaysi_son': 'Keyin qaysi son keladi?',
    'yetishmayotgan_son': 'Yetishmayotgan sonni top.',
    'qoshib_hisobla': 'Qo‘shib hisobla.',
    'ayirib_hisobla': 'Ayirib hisobla.',
    'ikki_olmaga_bitta_olma': 'Ikki olmaga yana bitta olma qo‘shsak, nechta bo‘ladi?',
    'eng_katta_shakl': 'Eng katta shaklni tanla.',
    'eng_kichik_shakl': 'Eng kichik shaklni tanla.',
    // Mantiq va xotira
    'mantiq': 'Mantiq',
    'bir_xil_rasmlar': 'Bir xil rasmlarni top.',
    'juftini_top': 'Har bir rasmning juftini top.',
    'qaysi_rasm_farq_qiladi': 'Qaysi rasm boshqalardan farq qiladi?',
    'qaysi_shakl_farq_qiladi': 'Qaysi shakl boshqalardan farq qiladi?',
    'keyin_nima_keladi': 'Keyin nima kelishini top.',
    'yetishmayotgan_shakl': 'Yetishmayotgan shaklni top.',
    'rasmlarni_eslab_qol': 'Rasmlarni eslab qol.',
    'eslab_qolgan_rasmni_top': 'Endi eslab qolgan rasmingni top.',
    'mos_soyasini_top': 'Mos soyasini top.',
    'togri_yolni_top': 'To‘g‘ri yo‘lni top.',
    // Rag'bat va yakun
    'barakalla': 'Barakalla!',
    'togri_topding': 'To‘g‘ri topding!',
    'barakalla_togri_topding': 'Barakalla, to‘g‘ri topding!',
    'ajoyib': 'Ajoyib!',
    'juda_yaxshi': 'Juda yaxshi!',
    'yana_urinib_kor': 'Yana bir marta urinib ko‘r.',
    'yana_urinib_koramiz': 'Yana bir marta urinib ko‘ramiz.',
    'shoshilma': 'Shoshilma.',
    'yaxshilab_oylab_kor': 'Yaxshilab o‘ylab ko‘r.',
    'bugun_yaxshi_harakat': 'Bugun juda yaxshi harakat qilding.',
    'dam_olamiz': 'Endi biroz dam olamiz.',
  };

  static SpeechPart part(String key) => SpeechPart(clips[key]!, 'uz', clip: key);

  static List<SpeechPart> parts(List<String> keys) => [for (final k in keys) part(k)];

  /// To'g'ri javobdan keyin (navbat bilan almashadi).
  static const List<String> praise = ['barakalla', 'togri_topding', 'ajoyib', 'juda_yaxshi', 'barakalla_togri_topding'];

  /// Birinchi xatodan keyin (navbat bilan almashadi).
  static const List<String> encourage = ['yana_urinib_kor', 'shoshilma', 'yaxshilab_oylab_kor', 'yana_urinib_koramiz'];

  static const List<String> numbers = ['bir', 'ikki', 'uch', 'tort', 'besh'];

  // ------------------------------------------------------------ Bola ismi va salom

  /// Ota-ona ismni o'zgartirmagan bo'lsa — yozib olingan ism.
  static String? nameClip(ChildProfile p) {
    if (p.id == 'azamjon' && p.name == 'Azamjon') return 'azamjon';
    if (p.id == 'muhammadjon' && p.name == 'Muhammadjon') return 'muhammadjon';
    return null;
  }

  /// Bosh sahifadagi salom. Ota-ona o'z salomini yozgan bo'lsa yoki ism yozilmagan bo'lsa — `null`
  /// (unda profil matni qurilma ovozida aytiladi). [first] — ilova ochilgandan keyingi birinchi kirish.
  static List<SpeechPart>? greeting(ChildProfile p, {required bool first}) {
    final name = nameClip(p);
    final customGreeting = p.greeting.isNotEmpty &&
        p.greeting != ChildProfile.defaultGreetingJunior &&
        p.greeting != ChildProfile.defaultGreetingSenior;
    if (name == null || customGreeting) return null;
    return first
        ? parts(['salom_$name', 'oynaymiz_organamiz', 'qaysi_oyinni_tanlaymiz'])
        : parts(['salom', name, 'keling_birga_oynaymiz']);
  }

  /// Fan ochilganda aytiladigan nom.
  static String? subjectClip(String subjectId) => subjectId == 'logic' ? 'mantiq' : null;

  // ------------------------------------------------------------ Mashqlar

  static bool _numericOptions(Exercise e) =>
      e.options.isNotEmpty && e.options.every((o) => o.visual == null && int.tryParse(o.text ?? '') != null);

  /// Ko'rsatma uchun yozib olingan ibora (mazmuni bir xil bo'lsa); bo'lmasa `null`.
  static String? instructionClip(Exercise e) {
    if (e.speechLang != 'uz' || e.speechParts.isNotEmpty) return null;
    final text = e.instruction.uz;
    if (text == 'Nechta olma bor?') return 'nechta_olma_bor';
    if (text == 'Qizil doirani top') return 'qizil_doirani_tanla';
    final m = e.meta;
    switch (e.instructionKey) {
      case 'where_more':
        return 'qaysi_biri_kop';
      case 'where_less':
        return 'qaysi_biri_kam';
      case 'which_bigger':
        return 'qaysi_son_katta';
      case 'which_smaller':
        return 'qaysi_son_kichik';
      case 'continue_sequence':
      case 'missing_number':
        return 'yetishmayotgan_son';
      case 'what_next':
        return _numericOptions(e) ? 'keyin_qaysi_son' : 'keyin_nima_keladi';
      case 'count_dots':
        return 'nechta_ekanini_top';
      case 'add_pictures':
        return (m['a'] == 2 && m['b'] == 1 && m['item'] == 'apple') ? 'ikki_olmaga_bitta_olma' : null;
      case 'find_big_shape':
        return 'eng_katta_shakl';
      case 'find_small_shape':
        return 'eng_kichik_shakl';
      case 'find_same':
      case 'mem_cards':
        return 'bir_xil_rasmlar';
      case 'match_pairs':
        return 'juftini_top';
      case 'odd_one_out':
        return 'qaysi_rasm_farq_qiladi';
      case 'odd_shape':
        return 'qaysi_shakl_farq_qiladi';
      case 'tangram_missing':
        return 'yetishmayotgan_shakl';
      case 'find_shadow':
      case 'mo_drag_shadow':
        return 'mos_soyasini_top';
      case 'maze_go':
        return 'togri_yolni_top';
      case 'mem_was_there':
        return 'eslab_qolgan_rasmni_top';
    }
    return null;
  }

  /// Ko'rsatmani aytish: yozib olingan ibora bo'lsa — o'sha, aks holda mashqning o'z nutqi.
  static List<SpeechPart> instruction(Exercise e) {
    if (e.speechParts.isNotEmpty) return e.speechParts;
    final clip = instructionClip(e);
    return [SpeechPart(clip != null ? clips[clip]! : e.speech, e.speechLang, clip: clip)];
  }

  /// Tinglab bajariladigan mashq (chet tili, "eshit va top", 3 tilda).
  static bool isListening(Exercise e) =>
      e.speechLang != 'uz' ||
      e.instructionKey.startsWith('lg_') ||
      e.instructionKey.startsWith('tri_') ||
      e.speechParts.isNotEmpty;

  /// Xotira mashqida rasm ko'rsatilayotganda.
  static List<SpeechPart> memorize() => parts(['yaxshilab_qara', 'rasmlarni_eslab_qol']);

  static bool _counting(Exercise e) => const {'count_how_many', 'count_dots', 'find_group_n'}.contains(e.instructionKey);

  /// Xatodan keyingi so'z. [mistakes] — shu mashqdagi xatolar soni, [turn] — darsdagi navbat raqami.
  /// Ikkinchi xatoda — mashq turiga mos maslahat (tinglashda ko'rsatma qayta aytiladi).
  static List<SpeechPart> afterMistake(Exercise e, int mistakes, int turn) {
    if (mistakes >= 2) {
      final m = e.meta;
      if (isListening(e)) return [part('yana_eshit'), ...instruction(e)];
      if (_counting(e)) return [part(_numericOptions(e) ? 'mos_raqamni_tanla' : 'narsalarni_sanab_kor')];
      if (m['op'] == '+') return [part('qoshib_hisobla')];
      if (m['op'] == '-') return [part('ayirib_hisobla')];
      if (m['op'] == 'cmp') return [part(m['answer'] == '=' ? 'qaysilari_teng' : 'yaxshilab_oylab_kor')];
      if (e.kind == ExerciseKind.spot) return [part('yaxshilab_qara')];
      if (e.kind == ExerciseKind.choice) return [part('togri_javobni_tanla')];
    }
    if (_counting(e)) return [part('sanab_kor')];
    return [part(encourage[turn % encourage.length])];
  }

  /// Kichik yoshda sanash mashqidan keyin birga sanaymiz: "Bir, ikki, uch".
  static List<SpeechPart> countAloud(Exercise e) {
    final n = e.meta['answer'];
    if (!_counting(e) || n is! int || n < 1 || n > numbers.length) return const [];
    return parts(numbers.take(n).toList());
  }
}
