import 'package:flutter/material.dart';

import '../../l10n/tr.dart';
import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import '../models/visual.dart';
import 'option_card.dart';
import 'visual_view.dart';

/// Rasm ichidan topish: kerakli narsalarni bosish. Topilgani yashil halqa bilan belgilanadi,
/// noto'g'ri narsa yumshoq chayqaladi. "Farqni top"da yuqorida namuna rasm turadi.
class SpotExerciseView extends StatefulWidget {
  const SpotExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<SpotExerciseView> createState() => _SpotExerciseViewState();
}

class _SpotExerciseViewState extends State<SpotExerciseView> {
  final Set<int> _found = {};
  int? _wrong;
  int _mistakes = 0;
  int _shake = 0;
  bool _solved = false;

  SpotTask get task => widget.exercise.spot!;

  void _tap(int i) {
    if (_solved || _found.contains(i)) return;
    if (task.targets.contains(i)) {
      setState(() {
        _found.add(i);
        _wrong = null;
      });
      if (_found.length == task.targets.length) {
        setState(() => _solved = true);
        widget.callbacks.onSolved(_mistakes);
      }
    } else {
      setState(() {
        _mistakes++;
        _shake++;
        _wrong = i;
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  /// 2 ta xatodan keyin — topilmagan narsalardan biri sariq halqa bilan.
  int? get _hint {
    if (_solved || _mistakes < 2) return null;
    for (final t in task.targets) {
      if (!_found.contains(t)) return t;
    }
    return null;
  }

  @override
  Widget build(BuildContext context) {
    final ref = task.reference;
    final remaining = task.targets.length - _found.length;
    return Column(
      children: [
        if (ref != null) ...[
          Expanded(
            child: Center(
              child: _frame(
                label: Tr.of(context).sample,
                child: IgnorePointer(child: SceneView(scene: SceneVisual(ref, aspect: task.aspect))),
              ),
            ),
          ),
          const SizedBox(height: 8),
        ],
        Expanded(
          flex: ref != null ? 1 : 3,
          child: Center(child: _frame(child: _interactive())),
        ),
        if (task.targets.length > 1)
          Padding(
            padding: const EdgeInsets.only(top: 8),
            child: Text(
              _solved ? '✅' : '🔎 × $remaining',
              key: const ValueKey('spot_remaining'),
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900, color: AppColors.text),
            ),
          ),
      ],
    );
  }

  Widget _frame({required Widget child, String? label}) {
    return Container(
      padding: const EdgeInsets.all(6),
      decoration: BoxDecoration(
        color: const Color(0xFFFFFDF7),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: const Color(0xFFEADFC8), width: 2),
      ),
      child: label == null
          ? child
          : Stack(
              children: [
                child,
                Positioned(
                  left: 6,
                  top: 2,
                  child: Text(label, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w800, color: AppColors.textSoft)),
                ),
              ],
            ),
    );
  }

  Widget _interactive() {
    final hint = _hint;
    return AspectRatio(
      aspectRatio: task.aspect,
      child: LayoutBuilder(builder: (context, c) {
        final w = c.maxWidth, h = c.maxHeight;
        return Stack(
          clipBehavior: Clip.none,
          children: [
            for (var i = 0; i < task.items.length; i++) _item(i, w, h, hint == i),
          ],
        );
      }),
    );
  }

  Widget _item(int i, double w, double h, bool hinted) {
    final item = task.items[i];
    // Kichik narsalarni ham bosish oson bo'lsin: bosish maydoni kamida 44 px.
    final s = item.size * h;
    final touch = s < 44 ? 44.0 : s;
    final found = _found.contains(i);
    Widget view = SizedBox(width: s, height: s, child: SceneItemView(item: item, extent: s));
    if (_wrong == i) view = Shake(trigger: _shake, child: view);
    return Positioned(
      left: item.x * w - touch / 2,
      top: item.y * h - touch / 2,
      width: touch,
      height: touch,
      child: GestureDetector(
        key: ValueKey('spot_$i'),
        behavior: HitTestBehavior.opaque,
        onTap: () => _tap(i),
        child: Stack(
          alignment: Alignment.center,
          children: [
            view,
            if (found || hinted)
              IgnorePointer(
                child: Container(
                  width: touch * 0.95,
                  height: touch * 0.95,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    border: Border.all(color: found ? AppColors.success : AppColors.star, width: 4),
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
