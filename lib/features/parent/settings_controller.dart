import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/providers.dart';
import '../../models/app_settings.dart';
import '../../services/parent_pin_service.dart';

/// Umumiy ilova sozlamalari.
class SettingsNotifier extends Notifier<AppSettings> {
  @override
  AppSettings build() {
    final settings = ref.read(databaseProvider).getSettings();
    ref.read(audioServiceProvider).applySettings(settings);
    return settings;
  }

  Future<void> _save(AppSettings settings) async {
    await ref.read(databaseProvider).saveSettings(settings);
    ref.read(audioServiceProvider).applySettings(settings);
    state = settings;
  }

  Future<void> setSound(bool value) => _save(state.copyWith(soundEnabled: value));

  Future<void> setVoice(bool value) => _save(state.copyWith(voiceEnabled: value));

  Future<void> setMusic(bool value) => _save(state.copyWith(musicEnabled: value));

  Future<void> setAppLanguage(String lang) => _save(state.copyWith(appLanguage: lang));

  /// PINni almashtiradi. Faqat [PinChangeResult.success] da saqlanadi.
  Future<PinChangeResult> changePin({
    required String oldPin,
    required String newPin,
    required String confirmPin,
  }) async {
    final result = ParentPinService.validateChange(
      storedPin: state.parentPin,
      oldPin: oldPin,
      newPin: newPin,
      confirmPin: confirmPin,
    );
    if (result == PinChangeResult.success) {
      await _save(state.copyWith(parentPin: newPin));
    }
    return result;
  }

  void reload() {
    final settings = ref.read(databaseProvider).getSettings();
    ref.read(audioServiceProvider).applySettings(settings);
    state = settings;
  }
}

final settingsProvider = NotifierProvider<SettingsNotifier, AppSettings>(SettingsNotifier.new);

/// PIN urinishlari hisoblagichi ilova ishlab turgan davomida saqlanadi.
final parentPinServiceProvider = Provider<ParentPinService>(
  (ref) => ParentPinService(clock: ref.read(clockProvider)),
);
