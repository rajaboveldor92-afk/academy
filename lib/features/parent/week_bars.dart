import 'package:flutter/material.dart';

/// Oddiy 7 kunlik ustunli diagramma (qo'shimcha kutubxonasiz).
class WeekBars extends StatelessWidget {
  const WeekBars({super.key, required this.values, required this.days, required this.color});

  final List<int> values;
  final List<String> days;
  final Color color;

  @override
  Widget build(BuildContext context) {
    final maxValue = values.fold<int>(0, (m, v) => v > m ? v : m);
    return SizedBox(
      height: 90,
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          for (var i = 0; i < values.length; i++)
            Expanded(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 3),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Text('${values[i]}', style: const TextStyle(fontSize: 12)),
                    const SizedBox(height: 2),
                    Container(
                      height: maxValue == 0 ? 3 : 3 + 48 * values[i] / maxValue,
                      decoration: BoxDecoration(
                        color: i == values.length - 1 ? color : color.withAlpha(110),
                        borderRadius: BorderRadius.circular(6),
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(days[i].substring(8), style: const TextStyle(fontSize: 11)),
                  ],
                ),
              ),
            ),
        ],
      ),
    );
  }
}
