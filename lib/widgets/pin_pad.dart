import 'package:flutter/material.dart';

import '../core/constants/app_constants.dart';
import '../theme/app_colors.dart';

/// Raqamli PIN klaviaturasi. [length] ta raqam kiritilgach [onCompleted] chaqiriladi
/// va maydon tozalanadi.
class PinPad extends StatefulWidget {
  const PinPad({
    super.key,
    required this.onCompleted,
    this.length = AppConstants.pinLength,
    this.enabled = true,
    this.errorText,
  });

  final ValueChanged<String> onCompleted;
  final int length;
  final bool enabled;
  final String? errorText;

  @override
  State<PinPad> createState() => _PinPadState();
}

class _PinPadState extends State<PinPad> {
  String _value = '';

  void _press(String digit) {
    if (!widget.enabled || _value.length >= widget.length) return;
    setState(() => _value += digit);
    if (_value.length == widget.length) {
      final entered = _value;
      Future<void>.delayed(const Duration(milliseconds: 120), () {
        if (!mounted) return;
        setState(() => _value = '');
        widget.onCompleted(entered);
      });
    }
  }

  void _backspace() {
    if (_value.isEmpty) return;
    setState(() => _value = _value.substring(0, _value.length - 1));
  }

  Widget _key(String label, {VoidCallback? onTap, Key? key}) {
    return Padding(
      padding: const EdgeInsets.all(6),
      child: Material(
        color: Colors.white,
        shape: const CircleBorder(),
        child: InkWell(
          key: key,
          customBorder: const CircleBorder(),
          onTap: widget.enabled ? onTap : null,
          child: SizedBox(
            width: 72,
            height: 72,
            child: Center(
              child: Text(
                label,
                style: const TextStyle(fontSize: 28, fontWeight: FontWeight.w700),
              ),
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final rows = [
      ['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', '9'],
    ];
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            for (var i = 0; i < widget.length; i++)
              Container(
                margin: const EdgeInsets.all(8),
                width: 20,
                height: 20,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: i < _value.length ? AppColors.primary : Colors.transparent,
                  border: Border.all(color: AppColors.primary, width: 2),
                ),
              ),
          ],
        ),
        SizedBox(
          height: 32,
          child: Center(
            child: Text(
              widget.errorText ?? '',
              style: const TextStyle(color: AppColors.gentle, fontWeight: FontWeight.w600),
            ),
          ),
        ),
        for (final row in rows)
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              for (final d in row) _key(d, key: Key('pin_$d'), onTap: () => _press(d)),
            ],
          ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const SizedBox(width: 84, height: 84),
            _key('0', key: const Key('pin_0'), onTap: () => _press('0')),
            _key('⌫', key: const Key('pin_back'), onTap: _backspace),
          ],
        ),
      ],
    );
  }
}
