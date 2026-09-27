import '../core/constants/app_constants.dart';
import '../core/utils/age_group.dart';
import '../core/utils/map_utils.dart';

/// Bola profili. Qurilmada saqlanadi, hech qayerga yuborilmaydi.
///
/// * [name] — qisqa ism: salomlashuv va bosh sahifada ("Azamjon, xush kelibsiz!").
/// * [fullName] — to'liq ism: faqat profil tanlash kartasida ("Odilbekov Azamjon Eldorovich").
/// * [photoPath] — bolaning rasmi; ilovaning shaxsiy papkasida, faqat qurilmada.
/// * [colorIndex] — profil mavzusi (`ProfileThemes`) indeksi.
class ChildProfile {
  const ChildProfile({
    required this.id,
    required this.name,
    required this.age,
    required this.avatar,
    required this.colorIndex,
    required this.dailyLimitMinutes,
    required this.createdAt,
    this.fullName = '',
    this.photoPath,
    this.greeting = '',
    this.disabledSubjects = const <String>[],
    this.difficultyBias = 0,
    this.language = 'uz',
  });

  /// Ilova tillari: o'zbek, rus, ingliz.
  static const List<String> languages = ['uz', 'ru', 'en'];

  /// Yangi profil uchun yoshga mos standart qiymatlar bilan konstruktor.
  factory ChildProfile.create({
    required String id,
    required String name,
    required int age,
    required String avatar,
    int colorIndex = 0,
    String fullName = '',
    String? photoPath,
    String greeting = '',
    String language = 'uz',
    DateTime? now,
  }) {
    final group = AgeGroup.fromAge(age);
    return ChildProfile(
      id: id,
      name: name.trim(),
      fullName: fullName.trim(),
      age: age,
      avatar: avatar,
      photoPath: photoPath,
      greeting: greeting.trim(),
      colorIndex: colorIndex,
      language: languages.contains(language) ? language : 'uz',
      dailyLimitMinutes:
          group.isJunior ? AppConstants.defaultLimitYoung : AppConstants.defaultLimitOlder,
      createdAt: now ?? DateTime.now(),
    );
  }

  static const String defaultGreetingJunior = 'O‘ynab-o‘rganishga tayyormisiz?';
  static const String defaultGreetingSenior = 'Bugun birga o‘rganamiz!';

  final String id;

  /// Qisqa ism (murojaat uchun).
  final String name;

  /// To'liq ism (profil kartasi uchun). Bo'sh bo'lsa [name] ko'rsatiladi.
  final String fullName;
  final int age;

  /// Rasm bo'lmaganda ko'rsatiladigan emoji.
  final String avatar;

  /// Lokal rasm fayli yo'li (ilova hujjatlar papkasida).
  final String? photoPath;

  /// Salomlashuvdan keyingi ikkinchi qator. Bo'sh bo'lsa yoshga mos standart.
  final String greeting;

  /// Profil mavzusi indeksi.
  final int colorIndex;

  /// Kunlik o'yin limiti (daqiqa). 0 — cheklanmagan.
  final int dailyLimitMinutes;

  /// Ota-ona vaqtincha yopgan fanlar (`Subject.id`).
  final List<String> disabledSubjects;

  /// Ota-ona sozlaydigan qiyinlik: -1 osonroq, 0 odatiy, 1 qiyinroq.
  final int difficultyBias;

  /// Bola ekranlari va mashqlar tili: `uz`, `ru` yoki `en` (ota-ona tanlaydi).
  final String language;
  final DateTime createdAt;

  AgeGroup get ageGroup => AgeGroup.fromAge(age);

  bool isSubjectEnabled(String subjectId) => !disabledSubjects.contains(subjectId);

  bool get hasPhoto => photoPath != null && photoPath!.isNotEmpty;

  /// Kartada ko'rsatiladigan ism.
  String get displayFullName => fullName.isNotEmpty ? fullName : name;

  /// "Azamjon, xush kelibsiz!" (bolaning tilida).
  String get welcomeTitle => switch (language) {
        'ru' => '$name, добро пожаловать!',
        'en' => 'Welcome, $name!',
        _ => '$name, xush kelibsiz!',
      };

  /// Ota-ona yozgan salom yoki yoshga mos standart (bolaning tilida).
  String get welcomeSubtitle {
    if (hasCustomGreeting) return greeting;
    final junior = ageGroup.isJunior;
    return switch (language) {
      'ru' => junior ? 'Готов играть и учиться?' : 'Сегодня учимся вместе!',
      'en' => junior ? 'Ready to play and learn?' : 'Let’s learn together today!',
      _ => junior ? defaultGreetingJunior : defaultGreetingSenior,
    };
  }

  /// Ota-ona o'z salomini yozganmi (standart matnlardan farqli).
  bool get hasCustomGreeting =>
      greeting.isNotEmpty && greeting != defaultGreetingJunior && greeting != defaultGreetingSenior;

  ChildProfile copyWith({
    String? name,
    String? fullName,
    int? age,
    String? avatar,
    String? photoPath,
    bool clearPhoto = false,
    String? greeting,
    int? colorIndex,
    int? dailyLimitMinutes,
    List<String>? disabledSubjects,
    int? difficultyBias,
    String? language,
  }) {
    return ChildProfile(
      id: id,
      name: name ?? this.name,
      fullName: fullName ?? this.fullName,
      age: age ?? this.age,
      avatar: avatar ?? this.avatar,
      photoPath: clearPhoto ? null : (photoPath ?? this.photoPath),
      greeting: greeting ?? this.greeting,
      colorIndex: colorIndex ?? this.colorIndex,
      dailyLimitMinutes: dailyLimitMinutes ?? this.dailyLimitMinutes,
      disabledSubjects: disabledSubjects ?? this.disabledSubjects,
      difficultyBias: difficultyBias ?? this.difficultyBias,
      language: language ?? this.language,
      createdAt: createdAt,
    );
  }

  Map<String, dynamic> toMap() => {
        'id': id,
        'name': name,
        'fullName': fullName,
        'age': age,
        'avatar': avatar,
        'photoPath': photoPath,
        'greeting': greeting,
        'colorIndex': colorIndex,
        'dailyLimitMinutes': dailyLimitMinutes,
        'disabledSubjects': List<String>.from(disabledSubjects),
        'difficultyBias': difficultyBias,
        'language': language,
        'createdAt': createdAt.toIso8601String(),
      };

  factory ChildProfile.fromMap(Map<String, dynamic> map) {
    final age = MapUtils.asInt(map['age'], 6);
    final photo = map['photoPath']?.toString();
    return ChildProfile(
      id: map['id'].toString(),
      name: (map['name'] ?? '').toString(),
      fullName: (map['fullName'] ?? '').toString(),
      age: age,
      avatar: (map['avatar'] ?? '👦').toString(),
      photoPath: (photo == null || photo.isEmpty) ? null : photo,
      greeting: (map['greeting'] ?? '').toString(),
      colorIndex: MapUtils.asInt(map['colorIndex']),
      dailyLimitMinutes: MapUtils.asInt(
        map['dailyLimitMinutes'],
        AgeGroup.fromAge(age).isJunior
            ? AppConstants.defaultLimitYoung
            : AppConstants.defaultLimitOlder,
      ),
      disabledSubjects: MapUtils.asStringList(map['disabledSubjects']),
      difficultyBias: _clampBias(MapUtils.asInt(map['difficultyBias'])),
      language: languages.contains(map['language']) ? map['language'].toString() : 'uz',
      createdAt: MapUtils.asDate(map['createdAt']) ?? DateTime.fromMillisecondsSinceEpoch(0),
    );
  }

  static int _clampBias(int value) {
    if (value < -1) return -1;
    if (value > 1) return 1;
    return value;
  }

  @override
  bool operator ==(Object other) =>
      other is ChildProfile &&
      other.id == id &&
      other.name == name &&
      other.fullName == fullName &&
      other.age == age &&
      other.avatar == avatar &&
      other.photoPath == photoPath &&
      other.greeting == greeting &&
      other.colorIndex == colorIndex &&
      other.dailyLimitMinutes == dailyLimitMinutes &&
      other.difficultyBias == difficultyBias &&
      other.language == language &&
      other.disabledSubjects.join(',') == disabledSubjects.join(',');

  @override
  int get hashCode =>
      Object.hash(id, name, fullName, age, avatar, photoPath, greeting, colorIndex, dailyLimitMinutes);
}
