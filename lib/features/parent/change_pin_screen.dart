import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/tr.dart';
import '../../services/parent_pin_service.dart';
import '../../widgets/pin_pad.dart';
import 'settings_controller.dart';

/// PINni uch bosqichda almashtirish: eski → yangi → tasdiqlash.
class ChangePinScreen extends ConsumerStatefulWidget {
  const ChangePinScreen({super.key});

  @override
  ConsumerState<ChangePinScreen> createState() => _ChangePinScreenState();
}

class _ChangePinScreenState extends ConsumerState<ChangePinScreen> {
  int _step = 0;
  String _old = '';
  String _new = '';
  String Function(Tr t)? _error;

  String _title(Tr t) => switch (_step) {
        0 => t.currentPin,
        1 => t.newPin,
        _ => t.repeatPin,
      };

  Future<void> _onPin(String pin) async {
    switch (_step) {
      case 0:
        if (pin != ref.read(settingsProvider).parentPin) {
          setState(() => _error = (t) => t.wrongPin);
          return;
        }
        setState(() {
          _old = pin;
          _step = 1;
          _error = null;
        });
      case 1:
        setState(() {
          _new = pin;
          _step = 2;
          _error = null;
        });
      default:
        final result = await ref.read(settingsProvider.notifier).changePin(
              oldPin: _old,
              newPin: _new,
              confirmPin: pin,
            );
        if (!mounted) return;
        if (result == PinChangeResult.success) {
          ScaffoldMessenger.of(context)
              .showSnackBar(SnackBar(content: Text(Tr.of(context).pinChanged)));
          Navigator.of(context).pop();
        } else {
          setState(() {
            _step = 1;
            _error = result == PinChangeResult.mismatch ? (Tr t) => t.pinsMismatch : (Tr t) => t.pinLength;
          });
        }
    }
  }

  @override
  Widget build(BuildContext context) {
    final t = Tr.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(t.changePin)),
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                Text(_title(t), style: Theme.of(context).textTheme.titleLarge),
                const SizedBox(height: 16),
                PinPad(key: ValueKey(_step), onCompleted: _onPin, errorText: _error?.call(t)),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
