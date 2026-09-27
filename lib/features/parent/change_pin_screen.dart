import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

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
  String? _error;

  static const _titles = ['Hozirgi PIN', 'Yangi PIN', 'Yangi PINni takrorlang'];

  Future<void> _onPin(String pin) async {
    switch (_step) {
      case 0:
        if (pin != ref.read(settingsProvider).parentPin) {
          setState(() => _error = "PIN noto‘g‘ri");
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
              .showSnackBar(const SnackBar(content: Text("PIN o‘zgartirildi")));
          Navigator.of(context).pop();
        } else {
          setState(() {
            _step = 1;
            _error = result == PinChangeResult.mismatch
                ? 'PINlar mos kelmadi, qaytadan kiriting'
                : "PIN 4 ta raqam bo‘lishi kerak";
          });
        }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("PINni o‘zgartirish")),
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                Text(_titles[_step], style: Theme.of(context).textTheme.titleLarge),
                const SizedBox(height: 16),
                PinPad(key: ValueKey(_step), onCompleted: _onPin, errorText: _error),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
