import 'package:flutter/material.dart';

import '../features/home/achievements_screen.dart';
import '../features/home/home_screen.dart';
import '../features/home/subject_screen.dart';
import '../features/home/time_up_screen.dart';
import '../features/lesson/lesson_screen.dart';
import '../features/parent/change_pin_screen.dart';
import '../features/parent/child_settings_screen.dart';
import '../features/parent/parent_gate_screen.dart';
import '../features/parent/parent_home_screen.dart';
import '../features/profiles/profile_editor_screen.dart';
import '../features/profiles/profile_select_screen.dart';
import '../features/splash/splash_screen.dart';
import '../models/child_profile.dart';
import '../models/subject.dart';

/// Barcha marshrutlar bitta joyda.
class AppRoutes {
  AppRoutes._();

  static const String splash = '/';
  static const String profiles = '/profiles';
  static const String profileEditor = '/profile-editor';
  static const String home = '/home';
  static const String subject = '/subject';
  static const String lesson = '/lesson';
  static const String dailyLesson = '/lesson/daily';
  static const String achievements = '/achievements';
  static const String timeUp = '/time-up';
  static const String parentGate = '/parent-gate';
  static const String parentHome = '/parent';
  static const String childSettings = '/parent/child';
  static const String changePin = '/parent/pin';
}

class AppRouter {
  AppRouter._();

  static Route<dynamic> onGenerateRoute(RouteSettings settings) {
    final args = settings.arguments;
    Widget page;
    switch (settings.name) {
      case AppRoutes.splash:
        page = const SplashScreen();
      case AppRoutes.profiles:
        page = const ProfileSelectScreen();
      case AppRoutes.profileEditor:
        page = ProfileEditorScreen(initial: args is ChildProfile ? args : null);
      case AppRoutes.home:
        page = const HomeScreen();
      case AppRoutes.subject:
        page = SubjectScreen(subject: args is Subject ? args : Subject.math);
      case AppRoutes.lesson:
        page = LessonScreen(topicId: args is String ? args : '');
      case AppRoutes.dailyLesson:
        page = const LessonScreen.daily();
      case AppRoutes.achievements:
        page = const AchievementsScreen();
      case AppRoutes.timeUp:
        page = const TimeUpScreen();
      case AppRoutes.parentGate:
        page = ParentGateScreen(nextRoute: args is String ? args : AppRoutes.parentHome);
      case AppRoutes.parentHome:
        page = const ParentHomeScreen();
      case AppRoutes.childSettings:
        page = ChildSettingsScreen(childId: args is String ? args : '');
      case AppRoutes.changePin:
        page = const ChangePinScreen();
      default:
        page = const ProfileSelectScreen();
    }
    return MaterialPageRoute<dynamic>(builder: (_) => page, settings: settings);
  }
}
