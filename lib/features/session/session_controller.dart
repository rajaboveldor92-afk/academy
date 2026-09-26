import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../core/constants/app_constants.dart';
import '../../core/providers.dart';
import '../../models/child_profile.dart';
import '../../services/time_limit_service.dart';
import '../profiles/profiles_controller.dart';
import 'progress_controller.dart';

/// Joriy o'yin sessiyasi holati.
@immutable
class SessionState {
  const SessionState({this.childId, this.running = false, this.limitReached = false});

  final String? childId;
  final bool running;

  /// Bugungi limit tugadi — "Ertaga davom etamiz" ekrani ko'rsatiladi.
  final bool limitReached;

  SessionState copyWith({bool? running, bool? limitReached}) => SessionState(
        childId: childId,
        running: running ?? this.running,
        limitReached: limitReached ?? this.limitReached,
      );
}

/// Bolaning kunlik o'yin vaqtini hisoblaydi va limitni nazorat qiladi.
///
/// Vaqt "devor soati" bo'yicha o'lchanadi va bitta qadamda
/// [maxStepSeconds] dan ko'p qo'shilmaydi — ilova fonda qolib ketsa ham
/// vaqt noto'g'ri yig'ilmaydi. Ilova fonga o'tganda [pause] chaqiriladi.
class SessionNotifier extends Notifier<SessionState> {
  static const int maxStepSeconds = 60;

  Timer? _timer;
  DateTime? _lastTick;

  @override
  SessionState build() {
    ref.onDispose(() => _timer?.cancel());
    return const SessionState();
  }

  DateTime _now() => ref.read(clockProvider)();

  ChildProfile? _profile(String childId) {
    for (final p in ref.read(profilesProvider)) {
      if (p.id == childId) return p;
    }
    return null;
  }

  /// Bola uchun bugungi limit tugaganmi (sessiya boshlamasdan tekshirish).
  bool isLimitReachedFor(String childId) {
    final profile = _profile(childId);
    if (profile == null) return false;
    final used = ref.read(progressProvider.notifier).of(childId).secondsOn(_now());
    return TimeLimitService.isExceeded(
      usedSeconds: used,
      limitMinutes: profile.dailyLimitMinutes,
    );
  }

  /// Bugun qolgan soniyalar (cheklov bo'lmasa `null`).
  int? remainingSecondsFor(String childId) {
    final profile = _profile(childId);
    if (profile == null) return null;
    final used = ref.read(progressProvider.notifier).of(childId).secondsOn(_now());
    return TimeLimitService.remainingSeconds(
      usedSeconds: used,
      limitMinutes: profile.dailyLimitMinutes,
    );
  }

  Future<void> start(String childId) async {
    await stop();
    await ref.read(progressProvider.notifier).registerVisit(childId);
    final reached = isLimitReachedFor(childId);
    state = SessionState(childId: childId, running: !reached, limitReached: reached);
    if (!reached) _startTimer();
  }

  void _startTimer() {
    _timer?.cancel();
    _lastTick = _now();
    _timer = Timer.periodic(AppConstants.usageTick, (_) => flush());
  }

  /// O'tgan vaqtni progressga yozadi va limitni tekshiradi.
  Future<void> flush() async {
    final childId = state.childId;
    final last = _lastTick;
    if (childId == null || last == null || !state.running) return;
    final now = _now();
    var elapsed = now.difference(last).inSeconds;
    if (elapsed <= 0) return;
    if (elapsed > maxStepSeconds) elapsed = maxStepSeconds;
    _lastTick = now;
    await ref.read(progressProvider.notifier).addSeconds(childId, elapsed);
    if (isLimitReachedFor(childId)) {
      _timer?.cancel();
      _timer = null;
      state = state.copyWith(running: false, limitReached: true);
    }
  }

  /// Ilova fonga o'tganda.
  Future<void> pause() async {
    if (!state.running) return;
    await flush();
    _timer?.cancel();
    _timer = null;
    _lastTick = null;
    if (!state.limitReached) state = state.copyWith(running: false);
  }

  /// Ilova qayta ochilganda.
  void resume() {
    final childId = state.childId;
    if (childId == null || state.running) return;
    if (isLimitReachedFor(childId)) {
      state = state.copyWith(limitReached: true);
      return;
    }
    state = state.copyWith(running: true, limitReached: false);
    _startTimer();
  }

  /// Ota-ona limitni o'zgartirganda qayta tekshirish.
  void recheckLimit() {
    final childId = state.childId;
    if (childId == null) return;
    final reached = isLimitReachedFor(childId);
    if (reached == state.limitReached) return;
    if (reached) {
      _timer?.cancel();
      _timer = null;
      state = state.copyWith(running: false, limitReached: true);
    } else {
      state = state.copyWith(running: true, limitReached: false);
      _startTimer();
    }
  }

  Future<void> stop() async {
    await flush();
    _timer?.cancel();
    _timer = null;
    _lastTick = null;
    state = const SessionState();
  }
}

final sessionProvider = NotifierProvider<SessionNotifier, SessionState>(SessionNotifier.new);
