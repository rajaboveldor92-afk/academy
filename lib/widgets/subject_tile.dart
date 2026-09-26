import 'package:flutter/material.dart';

import '../theme/app_colors.dart';
import 'pressable_scale.dart';

/// Bosh sahifadagi katta fan kartasi: katta emoji-ikonka + qisqa nom.
/// 4 yoshli bola o'qiy olmasa ham ikonka orqali yo'l topadi.
class SubjectTile extends StatelessWidget {
  const SubjectTile({
    super.key,
    required this.emoji,
    required this.title,
    required this.color,
    required this.onTap,
    this.badge,
    this.compactLabel = false,
  });

  final String emoji;
  final String title;
  final Color color;
  final VoidCallback onTap;

  /// Burchakdagi kichik belgi (masalan daraja: "2").
  final String? badge;

  /// Kichik yoshdagilar uchun matn kichikroq, ikonka kattaroq.
  final bool compactLabel;

  @override
  Widget build(BuildContext context) {
    return PressableScale(
      onTap: onTap,
      semanticLabel: title,
      child: LayoutBuilder(
        builder: (context, constraints) {
          final size = constraints.biggest.shortestSide;
          return Container(
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(28),
              border: Border.all(color: color.withAlpha(90), width: 3),
              boxShadow: [
                BoxShadow(
                  color: color.withAlpha(40),
                  blurRadius: 12,
                  offset: const Offset(0, 6),
                ),
              ],
            ),
            child: Stack(
              children: [
                Positioned.fill(
                  child: Padding(
                    padding: const EdgeInsets.all(10),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(
                          width: size * 0.5,
                          height: size * 0.5,
                          alignment: Alignment.center,
                          decoration: BoxDecoration(
                            color: color.withAlpha(38),
                            shape: BoxShape.circle,
                          ),
                          child: Text(
                            emoji,
                            style: TextStyle(fontSize: size * (compactLabel ? 0.3 : 0.26)),
                          ),
                        ),
                        SizedBox(height: size * 0.06),
                        Text(
                          title,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontSize: (size * 0.12).clamp(14.0, 24.0).toDouble(),
                            fontWeight: FontWeight.w800,
                            color: AppColors.text,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                if (badge != null)
                  Positioned(
                    top: 10,
                    right: 10,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                      decoration: BoxDecoration(
                        color: color,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Text(
                        badge!,
                        style: const TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.w800,
                          fontSize: 14,
                        ),
                      ),
                    ),
                  ),
              ],
            ),
          );
        },
      ),
    );
  }
}
