import '../core/constants/app_constants.dart';

/// PIN o'zgartirish natijasi.
enum PinChangeResult { success, wrongOldPin, invalidFormat, mismatch }

/// Ota-ona PIN kodini tekshirish va ketma-ket xato urinishlarda
/// vaqtincha bloklash mantig'i.
class ParentPinService {
  ParentPinService({DateTime Function()? clock}) : _clock = clock ?? DateTime.now;

  final DateTime Function() _clock;
  int _failedAttempts = 0;
  DateTime? _lockedUntil;

  int get failedAttempts => _failedAttempts;

  /// PIN faqat 4 ta raqamdan iborat bo'lishi kerak.
  static bool isValidFormat(String pin) =>
      pin.length == AppConstants.pinLength && RegExp(r'^\d+$').hasMatch(pin);

  bool get isLocked {
    final until = _lockedUntil;
    if (until == null) return false;
    if (_clock().isAfter(until)) {
      _lockedUntil = null;
      _failedAttempts = 0;
      return false;
    }
    return true;
  }

  Duration get lockRemaining {
    final until = _lockedUntil;
    if (until == null) return Duration.zero;
    final left = until.difference(_clock());
    return left.isNegative ? Duration.zero : left;
  }

  /// Kiritilgan [input] saqlangan [storedPin] bilan mos kelsa `true`.
  bool verify(String input, String storedPin) {
    if (isLocked) return false;
    if (input == storedPin) {
      _failedAttempts = 0;
      return true;
    }
    _failedAttempts++;
    if (_failedAttempts >= AppConstants.maxPinAttempts) {
      _lockedUntil = _clock().add(AppConstants.pinLockDuration);
    }
    return false;
  }

  /// Yangi PINni tekshiradi. Saqlash chaqiruvchi tomonidan bajariladi.
  static PinChangeResult validateChange({
    required String storedPin,
    required String oldPin,
    required String newPin,
    required String confirmPin,
  }) {
    if (oldPin != storedPin) return PinChangeResult.wrongOldPin;
    if (!isValidFormat(newPin)) return PinChangeResult.invalidFormat;
    if (newPin != confirmPin) return PinChangeResult.mismatch;
    return PinChangeResult.success;
  }
}
