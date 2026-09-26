import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../database/local_database.dart';
import '../services/audio_service.dart';

/// Ochilgan ma'lumotlar bazasi. `main.dart` da (yoki testda) override qilinadi.
final databaseProvider = Provider<LocalDatabase>((ref) {
  throw UnimplementedError('databaseProvider ProviderScope ichida override qilinishi kerak');
});

/// Audio servis. Testlarda `SilentAudioService` bilan almashtiriladi.
final audioServiceProvider = Provider<AudioService>((ref) {
  final service = DeviceAudioService();
  ref.onDispose(service.dispose);
  return service;
});

/// Joriy vaqt manbai — testlarda vaqtni boshqarish uchun override qilinadi.
final clockProvider = Provider<DateTime Function()>((ref) => DateTime.now);
