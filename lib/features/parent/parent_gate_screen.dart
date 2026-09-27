import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/tr.dart';
import '../../widgets/pin_pad.dart';
import 'settings_controller.dart';

/// PIN bilan himoyalangan kirish. To'g'ri PINdan keyin [nextRoute] ochiladi.
class ParentGateScreen extends ConsumerStatefulWidget {
  const ParentGateScreen({super.key, required this.nextRoute});

  final String nextRoute;

  @override
  ConsumerState<ParentGateScreen> createState() => _ParentGateScreenState();
}

class _ParentGateScreenState extends ConsumerState<ParentGateScreen> {
  /// Xato matni (tilga qarab build'da hosil qilinadi).
  String Function(Tr t)? _error;
  Timer? _lockTimer;

  @override
  void initState() {
    super.initState();
    if (ref.read(parentPinServiceProvider).isLocked) _startLockCountdown();
  }

  @override
  void dispose() {
    _lockTimer?.cancel();
    super.dispose();
  }

  void _startLockCountdown() {
    _lockTimer?.cancel();
    _lockTimer = Timer.periodic(const Duration(seconds: 1), (t) {
      if (!mounted) return;
      final service = ref.read(parentPinServiceProvider);
      if (!service.isLocked) {
        t.cancel();
        setState(() => _error = null);
      } else {
        final seconds = service.lockRemaining.inSeconds + 1;
        setState(() => _error = (tr) => tr.waitSeconds(seconds));
      }
    });
  }

  void _onPin(String pin) {
    final service = ref.read(parentPinServiceProvider);
    final stored = ref.read(settingsProvider).parentPin;
    if (service.verify(pin, stored)) {
      Navigator.of(context).pushReplacementNamed(widget.nextRoute);
      return;
    }
    if (service.isLocked) {
      final seconds = service.lockRemaining.inSeconds + 1;
      setState(() => _error = (tr) => tr.waitSeconds(seconds));
      _startLockCountdown();
    } else {
      setState(() => _error = (t) => t.wrongPin);
    }
  }

  @override
  Widget build(BuildContext context) {
    final locked = ref.read(parentPinServiceProvider).isLocked;
    final t = Tr.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(t.parent)),
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                const Text('🔒', style: TextStyle(fontSize: 56)),
                const SizedBox(height: 8),
                Text(t.enterPin, style: Theme.of(context).textTheme.titleLarge),
                const SizedBox(height: 16),
                PinPad(onCompleted: _onPin, enabled: !locked, errorText: _error?.call(t)),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
