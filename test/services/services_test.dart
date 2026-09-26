import 'package:academy/services/parent_pin_service.dart';
import 'package:academy/services/time_limit_service.dart';
import 'package:flutter_test/flutter_test.dart';

import '../helpers/test_helpers.dart';

void main() {
  group('TimeLimitService', () {
    test('limit 0 — cheklanmagan', () {
      expect(TimeLimitService.isExceeded(usedSeconds: 99999, limitMinutes: 0), isFalse);
      expect(TimeLimitService.remainingSeconds(usedSeconds: 10, limitMinutes: 0), isNull);
    });

    test('20 daqiqalik limit', () {
      expect(TimeLimitService.isExceeded(usedSeconds: 1199, limitMinutes: 20), isFalse);
      expect(TimeLimitService.isExceeded(usedSeconds: 1200, limitMinutes: 20), isTrue);
      expect(TimeLimitService.remainingSeconds(usedSeconds: 1100, limitMinutes: 20), 100);
      expect(TimeLimitService.remainingSeconds(usedSeconds: 1500, limitMinutes: 20), 0);
      expect(TimeLimitService.isNearLimit(usedSeconds: 1100, limitMinutes: 20), isTrue);
      expect(TimeLimitService.isNearLimit(usedSeconds: 600, limitMinutes: 20), isFalse);
    });
  });

  group('ParentPinService', () {
    test('standart PIN 1234 qabul qilinadi, boshqasi yo\'q', () {
      final s = ParentPinService();
      expect(s.verify('0000', '1234'), isFalse);
      expect(s.failedAttempts, 1);
      expect(s.verify('1234', '1234'), isTrue);
      expect(s.failedAttempts, 0);
    });

    test('5 marta xato — 30 soniya blok', () {
      final clock = FakeClock(DateTime(2026, 9, 26, 12));
      final s = ParentPinService(clock: clock.call);
      for (var i = 0; i < 5; i++) {
        s.verify('9999', '1234');
      }
      expect(s.isLocked, isTrue);
      expect(s.verify('1234', '1234'), isFalse, reason: 'blok vaqtida to\'g\'ri PIN ham o\'tmaydi');
      clock.advance(const Duration(seconds: 31));
      expect(s.isLocked, isFalse);
      expect(s.verify('1234', '1234'), isTrue);
    });

    test('PIN almashtirish tekshiruvi', () {
      expect(
        ParentPinService.validateChange(
            storedPin: '1234', oldPin: '1111', newPin: '5678', confirmPin: '5678'),
        PinChangeResult.wrongOldPin,
      );
      expect(
        ParentPinService.validateChange(
            storedPin: '1234', oldPin: '1234', newPin: '12a4', confirmPin: '12a4'),
        PinChangeResult.invalidFormat,
      );
      expect(
        ParentPinService.validateChange(
            storedPin: '1234', oldPin: '1234', newPin: '5678', confirmPin: '5679'),
        PinChangeResult.mismatch,
      );
      expect(
        ParentPinService.validateChange(
            storedPin: '1234', oldPin: '1234', newPin: '5678', confirmPin: '5678'),
        PinChangeResult.success,
      );
    });
  });
}
