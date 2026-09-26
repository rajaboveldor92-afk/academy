import 'package:flutter/material.dart';

/// Emoji avatar doirasi.
class AvatarBubble extends StatelessWidget {
  const AvatarBubble({
    super.key,
    required this.avatar,
    required this.color,
    this.size = 72,
    this.selected = false,
  });

  final String avatar;
  final Color color;
  final double size;
  final bool selected;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: size,
      height: size,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        color: color.withAlpha(45),
        shape: BoxShape.circle,
        border: Border.all(color: selected ? color : Colors.transparent, width: 4),
      ),
      child: Text(
        avatar,
        style: TextStyle(fontSize: size * 0.52, height: 1.1),
        textAlign: TextAlign.center,
      ),
    );
  }
}
