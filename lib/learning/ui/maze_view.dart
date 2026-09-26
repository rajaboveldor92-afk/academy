import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Labirint: qahramonni strelkalar, surish (swipe) yoki qo'shni katakni bosib yurgizish.
class MazeExerciseView extends StatefulWidget {
  const MazeExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  @override
  State<MazeExerciseView> createState() => _MazeExerciseViewState();
}

class _MazeExerciseViewState extends State<MazeExerciseView> {
  late int _pos = maze.start;
  late final List<int> _trail = [maze.start];
  bool _done = false;
  int _bumps = 0;
  int _shake = 0;

  MazeTask get maze => widget.exercise.maze!;

  void _move(int dir) {
    if (_done) return;
    final next = maze.neighbor(_pos, dir);
    if (next == null) {
      setState(() {
        _bumps++;
        _shake++;
      });
      return;
    }
    setState(() {
      _pos = next;
      if (_trail.length > 1 && _trail[_trail.length - 2] == next) {
        _trail.removeLast(); // orqaga qaytdi
      } else {
        _trail.add(next);
      }
    });
    if (_pos == maze.goal) {
      _done = true;
      // Devorga urilish xato hisoblanmaydi — labirintda sinab ko'rish tabiiy.
      widget.callbacks.onSolved(0);
    }
  }

  void _tapCell(int cell) {
    final r = _pos ~/ maze.cols, c = _pos % maze.cols;
    final tr = cell ~/ maze.cols, tc = cell % maze.cols;
    if (tr == r && tc == c + 1) _move(MazeTask.right);
    if (tr == r && tc == c - 1) _move(MazeTask.left);
    if (tc == c && tr == r + 1) _move(MazeTask.bottom);
    if (tc == c && tr == r - 1) _move(MazeTask.top);
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: Center(
            child: AspectRatio(
              aspectRatio: maze.cols / maze.rows,
              child: Shake(
                trigger: _shake,
                child: GestureDetector(
                  onPanEnd: (d) {
                    final v = d.velocity.pixelsPerSecond;
                    if (v.distance < 150) return;
                    if (v.dx.abs() > v.dy.abs()) {
                      _move(v.dx > 0 ? MazeTask.right : MazeTask.left);
                    } else {
                      _move(v.dy > 0 ? MazeTask.bottom : MazeTask.top);
                    }
                  },
                  child: LayoutBuilder(builder: (context, c) {
                    final cw = c.maxWidth / maze.cols, ch = c.maxHeight / maze.rows;
                    return Stack(
                      children: [
                        Positioned.fill(child: CustomPaint(painter: _MazePainter(maze, _trail))),
                        for (var i = 0; i < maze.rows * maze.cols; i++)
                          Positioned(
                            left: (i % maze.cols) * cw,
                            top: (i ~/ maze.cols) * ch,
                            width: cw,
                            height: ch,
                            child: GestureDetector(
                              behavior: HitTestBehavior.opaque,
                              onTap: () => _tapCell(i),
                              child: Center(
                                child: i == _pos
                                    ? Text(maze.hero, style: TextStyle(fontSize: ch * 0.62))
                                    : (i == maze.goal ? Text(maze.target, style: TextStyle(fontSize: ch * 0.62)) : null),
                              ),
                            ),
                          ),
                      ],
                    );
                  }),
                ),
              ),
            ),
          ),
        ),
        const SizedBox(height: 10),
        _ArrowPad(onMove: _move),
      ],
    );
  }
}

class _MazePainter extends CustomPainter {
  _MazePainter(this.maze, this.trail);

  final MazeTask maze;
  final List<int> trail;

  @override
  void paint(Canvas canvas, Size size) {
    final cw = size.width / maze.cols, ch = size.height / maze.rows;
    final bg = Paint()..color = const Color(0xFFFFFBF2);
    canvas.drawRRect(RRect.fromRectAndRadius(Offset.zero & size, const Radius.circular(12)), bg);
    final trailPaint = Paint()..color = const Color(0xFFDFF3E8);
    for (final cell in trail) {
      final r = cell ~/ maze.cols, c = cell % maze.cols;
      canvas.drawRect(Rect.fromLTWH(c * cw + 2, r * ch + 2, cw - 4, ch - 4), trailPaint);
    }
    final goalR = maze.goal ~/ maze.cols, goalC = maze.goal % maze.cols;
    canvas.drawRect(Rect.fromLTWH(goalC * cw + 2, goalR * ch + 2, cw - 4, ch - 4), Paint()..color = const Color(0xFFFFF0C2));
    final wall = Paint()
      ..color = AppColors.primary
      ..strokeWidth = (cw < ch ? cw : ch) * 0.1
      ..strokeCap = StrokeCap.round;
    for (var i = 0; i < maze.rows * maze.cols; i++) {
      final r = i ~/ maze.cols, c = i % maze.cols;
      final x = c * cw, y = r * ch;
      final w = maze.walls[i];
      if (w & MazeTask.top != 0) canvas.drawLine(Offset(x, y), Offset(x + cw, y), wall);
      if (w & MazeTask.left != 0) canvas.drawLine(Offset(x, y), Offset(x, y + ch), wall);
      if (r == maze.rows - 1 && w & MazeTask.bottom != 0) canvas.drawLine(Offset(x, y + ch), Offset(x + cw, y + ch), wall);
      if (c == maze.cols - 1 && w & MazeTask.right != 0) canvas.drawLine(Offset(x + cw, y), Offset(x + cw, y + ch), wall);
    }
  }

  @override
  bool shouldRepaint(_MazePainter old) => true;
}

class _ArrowPad extends StatelessWidget {
  const _ArrowPad({required this.onMove});

  final void Function(int dir) onMove;

  Widget _btn(IconData icon, int dir, String key) => Padding(
        padding: const EdgeInsets.all(4),
        child: SizedBox(
          width: 66,
          height: 58,
          child: FilledButton.tonal(
            key: Key('arrow_$key'),
            style: FilledButton.styleFrom(padding: EdgeInsets.zero, minimumSize: const Size(60, 54)),
            onPressed: () => onMove(dir),
            child: Icon(icon, size: 34),
          ),
        ),
      );

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        _btn(Icons.arrow_back_rounded, MazeTask.left, 'left'),
        Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            _btn(Icons.arrow_upward_rounded, MazeTask.top, 'up'),
            _btn(Icons.arrow_downward_rounded, MazeTask.bottom, 'down'),
          ],
        ),
        _btn(Icons.arrow_forward_rounded, MazeTask.right, 'right'),
      ],
    );
  }
}
