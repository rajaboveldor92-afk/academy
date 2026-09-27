import '../core/constants/app_constants.dart';
import '../core/utils/map_utils.dart';

/// Butun ilova (barcha bolalar) uchun umumiy sozlamalar.
class AppSettings {
  const AppSettings({
    this.parentPin = AppConstants.defaultParentPin,
    this.soundEnabled = true,
    this.voiceEnabled = true,
    this.musicEnabled = false,
    this.seeded = false,
    this.dataVersion = 1,
    this.appLanguage = 'uz',
  });

  /// Ota-ona bo'limi PIN kodi (4 raqam). Faqat qurilmada saqlanadi.
  final String parentPin;

  /// Effekt ovozlari (yulduz, to'g'ri javob).
  final bool soundEnabled;

  /// So'z va nomlarni ovozda aytish.
  final bool voiceEnabled;

  /// Fon musiqasi.
  final bool musicEnabled;

  /// Standart profillar (Azamjon, Muhammadjon) bir marta yaratilganmi.
  final bool seeded;

  /// Saqlangan ma'lumotlar sxemasi versiyasi (migratsiyalar uchun).
  final int dataVersion;

  /// Umumiy ekranlar (profil tanlash, ota-ona bo'limi) tili: `uz`, `ru`, `en`.
  /// Bola ekranlari tili har bir bola profilida alohida.
  final String appLanguage;

  AppSettings copyWith({
    String? parentPin,
    bool? soundEnabled,
    bool? voiceEnabled,
    bool? musicEnabled,
    bool? seeded,
    int? dataVersion,
    String? appLanguage,
  }) {
    return AppSettings(
      parentPin: parentPin ?? this.parentPin,
      soundEnabled: soundEnabled ?? this.soundEnabled,
      voiceEnabled: voiceEnabled ?? this.voiceEnabled,
      musicEnabled: musicEnabled ?? this.musicEnabled,
      seeded: seeded ?? this.seeded,
      dataVersion: dataVersion ?? this.dataVersion,
      appLanguage: appLanguage ?? this.appLanguage,
    );
  }

  Map<String, dynamic> toMap() => {
        'parentPin': parentPin,
        'soundEnabled': soundEnabled,
        'voiceEnabled': voiceEnabled,
        'musicEnabled': musicEnabled,
        'seeded': seeded,
        'dataVersion': dataVersion,
        'appLanguage': appLanguage,
      };

  factory AppSettings.fromMap(Map<String, dynamic> map) {
    final pin = (map['parentPin'] ?? '').toString();
    return AppSettings(
      parentPin: pin.length == AppConstants.pinLength ? pin : AppConstants.defaultParentPin,
      soundEnabled: MapUtils.asBool(map['soundEnabled'], true),
      voiceEnabled: MapUtils.asBool(map['voiceEnabled'], true),
      musicEnabled: MapUtils.asBool(map['musicEnabled'], false),
      seeded: MapUtils.asBool(map['seeded'], false),
      dataVersion: MapUtils.asInt(map['dataVersion'], 1),
      appLanguage: const ['uz', 'ru', 'en'].contains(map['appLanguage']) ? map['appLanguage'].toString() : 'uz',
    );
  }
}
