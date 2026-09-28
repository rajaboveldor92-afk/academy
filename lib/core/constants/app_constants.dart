/// Ilova bo'ylab ishlatiladigan o'zgarmas qiymatlar.
class AppConstants {
  AppConstants._();

  static const String appName = 'Azamjon & Muhammadjon Academy';
  static const String appShortName = 'A&M Academy';

  /// Birinchi ishga tushirishdagi ota-ona PIN kodi.
  static const String defaultParentPin = '1234';
  static const int pinLength = 4;

  /// Ketma-ket noto'g'ri PIN kiritilganda vaqtincha bloklash.
  static const int maxPinAttempts = 5;
  static const Duration pinLockDuration = Duration(seconds: 30);

  /// Profil yoshi chegaralari.
  static const int minAge = 3;
  static const int maxAge = 16;

  /// Standart kunlik vaqt limitlari (daqiqa). 0 = cheklanmagan.
  static const int defaultLimitYoung = 15;
  static const int defaultLimitOlder = 20;

  /// Maktab o'quvchilari uchun (daqiqa).
  static const int defaultLimitSchool = 40;

  /// Foydalanish vaqti shu intervalda hisoblanadi.
  static const Duration usageTick = Duration(seconds: 15);

  static const Duration splashDuration = Duration(milliseconds: 1200);

  static const int maxNameLength = 20;
  static const int maxFullNameLength = 60;

  /// Profil uchun tanlanadigan avatarlar (emoji — APK hajmini oshirmaydi).
  static const List<String> avatars = [
    '👦', '👧', '🧒', '🦁', '🐯', '🐻', '🐼', '🦊',
    '🐰', '🐸', '🦄', '🐧', '🚀', '⚽', '🦖', '🐙',
  ];
}
