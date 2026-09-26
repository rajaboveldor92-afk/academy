import '../core/constants/app_constants.dart';
import '../core/utils/age_group.dart';
import '../core/utils/map_utils.dart';

/// Bola profili. Qurilmada saqlanadi, hech qayerga yuborilmaydi.
class ChildProfile {
  const ChildProfile({
    required this.id,
    required this.name,
    required this.age,
    required this.avatar,
    required this.colorIndex,
    required this.dailyLimitMinutes,
    required this.createdAt,
    this.disabledSubjects = const <String>[],
    this.difficultyBias = 0,
  });

  /// Yangi profil uchun yoshga mos standart qiymatlar bilan konstruktor.
  factory ChildProfile.create({
    required String id,
    required String name,
    required int age,
    required String avatar,
    int colorIndex = 0,
    DateTime? now,
  }) {
    final group = AgeGroup.fromAge(age);
    return ChildProfile(
      id: id,
      name: name.trim(),
      age: age,
      avatar: avatar,
      colorIndex: colorIndex,
      dailyLimitMinutes:
          group.isJunior ? AppConstants.defaultLimitYoung : AppConstants.defaultLimitOlder,
      createdAt: now ?? DateTime.now(),
    );
  }

  final String id;
  final String name;
  final int age;
  final String avatar;
  final int colorIndex;

  /// Kunlik o'yin limiti (daqiqa). 0 — cheklanmagan.
  final int dailyLimitMinutes;

  /// Ota-ona vaqtincha yopgan fanlar (`Subject.id`).
  final List<String> disabledSubjects;

  /// Ota-ona sozlaydigan qiyinlik: -1 osonroq, 0 odatiy, 1 qiyinroq.
  final int difficultyBias;
  final DateTime createdAt;

  AgeGroup get ageGroup => AgeGroup.fromAge(age);

  bool isSubjectEnabled(String subjectId) => !disabledSubjects.contains(subjectId);

  ChildProfile copyWith({
    String? name,
    int? age,
    String? avatar,
    int? colorIndex,
    int? dailyLimitMinutes,
    List<String>? disabledSubjects,
    int? difficultyBias,
  }) {
    return ChildProfile(
      id: id,
      name: name ?? this.name,
      age: age ?? this.age,
      avatar: avatar ?? this.avatar,
      colorIndex: colorIndex ?? this.colorIndex,
      dailyLimitMinutes: dailyLimitMinutes ?? this.dailyLimitMinutes,
      disabledSubjects: disabledSubjects ?? this.disabledSubjects,
      difficultyBias: difficultyBias ?? this.difficultyBias,
      createdAt: createdAt,
    );
  }

  Map<String, dynamic> toMap() => {
        'id': id,
        'name': name,
        'age': age,
        'avatar': avatar,
        'colorIndex': colorIndex,
        'dailyLimitMinutes': dailyLimitMinutes,
        'disabledSubjects': List<String>.from(disabledSubjects),
        'difficultyBias': difficultyBias,
        'createdAt': createdAt.toIso8601String(),
      };

  factory ChildProfile.fromMap(Map<String, dynamic> map) {
    final age = MapUtils.asInt(map['age'], 6);
    return ChildProfile(
      id: map['id'].toString(),
      name: (map['name'] ?? '').toString(),
      age: age,
      avatar: (map['avatar'] ?? '👦').toString(),
      colorIndex: MapUtils.asInt(map['colorIndex']),
      dailyLimitMinutes: MapUtils.asInt(
        map['dailyLimitMinutes'],
        AgeGroup.fromAge(age).isJunior
            ? AppConstants.defaultLimitYoung
            : AppConstants.defaultLimitOlder,
      ),
      disabledSubjects: MapUtils.asStringList(map['disabledSubjects']),
      difficultyBias: _clampBias(MapUtils.asInt(map['difficultyBias'])),
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
      other.age == age &&
      other.avatar == avatar &&
      other.colorIndex == colorIndex &&
      other.dailyLimitMinutes == dailyLimitMinutes &&
      other.difficultyBias == difficultyBias &&
      other.disabledSubjects.join(',') == disabledSubjects.join(',');

  @override
  int get hashCode => Object.hash(id, name, age, avatar, colorIndex, dailyLimitMinutes);
}
