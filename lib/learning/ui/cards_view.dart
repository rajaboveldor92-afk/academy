import 'dart:async';

import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Juft kartalar (xotira o'yini). Karta bosilsa ochiladi; ikkita ochiq karta bir xil
/// bo'lsa — ochiq qoladi, aks holda biroz kutib yopiladi. Adashish tabiiy — xato deb
/// aytilmaydi; faqat juda ko'p urinishlar natijada hisobga olinadi.
class CardsExerciseView extends StatefulWidget {
  const CardsExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  /// Ikkita har xil karta ochiq turadigan vaqt.
  static const Duration flipBack = Duration(milliseconds: 900);

  @override
  State<CardsExerciseView> createState() => _CardsExerciseViewState();
}

class _CardsExerciseViewState extends State<CardsExerciseView> {
  final Set<int> _matched = {};
  final List<int> _open = [];
  int _misses = 0;
  bool _solved = false;
  Timer? _timer;

  CardsTask get task => widget.exercise.cards!;

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void _tap(int i) {
    if (_solved || _matched.contains(i) || _open.contains(i) || _open.length >= 2) return;
    setState(() => _open.add(i));
    if (_open.length < 2) return;
    final a = _open[0], b = _open[1];
    if (task.faces[a] == task.faces[b]) {
      setState(() {
        _matched.addAll([a, b]);
        _open.clear();
      });
      if (_matched.length == task.faces.length) {
        setState(() => _solved = true);
        // Har bir juft uchun bitta adashish — tabiiy; undan ortig'i natijada hisobga olinadi.
        final extra = _misses - task.pairs;
        widget.callbacks.onSolved(extra > 0 ? extra : 0);
      }
    } else {
      _misses++;
      _timer = Timer(CardsExerciseView.flipBack, () {
        if (mounted) setState(_open.clear);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final n = task.faces.length;
    final cols = task.cols;
    final rows = (n / cols).ceil();
    return LayoutBuilder(builder: (context, c) {
      final w = c.maxWidth.isFinite ? c.maxWidth : 400.0;
      final h = c.maxHeight.isFinite ? c.maxHeight : 500.0;
      final cell = (w / cols < h / rows ? w / cols : h / rows).clamp(40.0, 160.0).toDouble();
      return Center(
        child: SizedBox(
          width: cell * cols,
          height: cell * rows,
          child: Wrap(
            children: [
              for (var i = 0; i < n; i++)
                SizedBox(
                  width: cell,
                  height: cell,
                  child: Padding(padding: const EdgeInsets.all(5), child: _card(i, cell)),
                ),
            ],
          ),
        ),
      );
    });
  }

  Widget _card(int i, double cell) {
    final open = _open.contains(i) || _matched.contains(i);
    final matched = _matched.contains(i);
    return GestureDetector(
      key: ValueKey('card_$i'),
      onTap: () => _tap(i),
      child: AnimatedSwitcher(
        duration: const Duration(milliseconds: 220),
        transitionBuilder: (child, anim) => ScaleTransition(scale: anim, child: child),
        child: Container(
          key: ValueKey(open),
          decoration: BoxDecoration(
            color: open ? (matched ? const Color(0xFFE6F8EE) : Colors.white) : AppColors.primary,
            borderRadius: BorderRadius.circular(18),
            border: Border.all(color: matched ? AppColors.success : const Color(0xFFE3E6F0), width: matched ? 3 : 2),
            boxShadow: const [BoxShadow(color: Color(0x22000000), blurRadius: 4, offset: Offset(0, 2))],
          ),
          alignment: Alignment.center,
          child: open
              ? Text(task.faces[i], style: TextStyle(fontSize: cell * 0.48, height: 1))
              : Text('?', style: TextStyle(fontSize: cell * 0.4, fontWeight: FontWeight.w900, color: Colors.white)),
        ),
      ),
    );
  }
}
