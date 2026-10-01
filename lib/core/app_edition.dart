import '../models/child_profile.dart';

/// Release edition selected with --dart-define=ACADEMY_EDITION=kids|school.
class AppEditionConfig {
  AppEditionConfig._();
  static const String raw = String.fromEnvironment('ACADEMY_EDITION', defaultValue: 'all');
  static bool get isKids => raw == 'kids';
  static bool get isSchool => raw == 'school';
  static String get appName => isKids ? 'Academy Kids' : (isSchool ? 'Academy Maktab' : 'A&M Academy');
  static bool acceptsProfile(ChildProfile p) => isKids ? (!p.isSchool && p.age >= 3 && p.age <= 8) : (isSchool ? p.isSchool : true);
  static int normalizeAge(int age) => isKids ? age.clamp(3, 8) : age;
  static int normalizeGrade(int grade) => isKids ? 0 : (isSchool ? grade.clamp(1, ChildProfile.maxGrade) : grade);
}
