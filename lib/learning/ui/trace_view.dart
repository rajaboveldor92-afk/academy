import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../theme/app_colors.dart';
import '../models/exercise.dart';
import 'option_card.dart';

/// Barmoq bilan yozish: chiziq, shakl, harf, raqam, so'z yoki raqamlangan nuqtalar.
///
/// * Yashil nuqta — boshlanish joyi, strelka — yo'nalish (bir nechta chiziq bo'lsa raqamlangan).
/// * Har bir chiziq tugaganda avtomatik tekshiriladi ([TraceScorer]) — yumshoq, lekin
///   tartibsiz chizish o'tmaydi.
/// * Yo'ldan butunlay chiqib ketgan chiziq o'chadi (xato hisoblanadi, lekin urishmaydi).
/// * 2 ta xatodan keyin qanday yozish ko'rsatiladi (animatsiya); 👀 tugmasi ham bor.
/// * 4 ta xatodan keyin mashq yumshoq yakunlanadi — bola qiynalib qolmasin.
class TraceExerciseView extends StatefulWidget {
  const TraceExerciseView({super.key, required this.exercise, required this.callbacks});

  final Exercise exercise;
  final ExerciseCallbacks callbacks;

  /// Maydon chetidagi bo'sh joy (ichki balandlikka nisbatan).
  static const double insetRatio = 0.08;

  /// Shuncha xatodan keyin mashq yakunlanadi.
  static const int maxMistakes = 4;

  @override
  State<TraceExerciseView> createState() => _TraceExerciseViewState();
}

class _TraceExerciseViewState extends State<TraceExerciseView> with SingleTickerProviderStateMixin {
  final List<List<Point2>> _strokes = [];
  List<Point2>? _current;
  int? _pointer;
  int _mistakes = 0;
  int _shake = 0;
  bool _solved = false;
  Rect _inner = Rect.zero;

  /// Namoyish: chiziq chiziladi, oxirida biroz to'xtab turadi va o'chadi (taymersiz).
  late final AnimationController _demo = AnimationController(vsync: this);
  double _demoDrawShare = 1;

  TraceTask get task => widget.exercise.trace!;

  int get _strokeLimit => task.dots ? task.strokes.first.length + 2 : task.strokes.length * 2 + 2;

  @override
  void initState() {
    super.initState();
    final seconds = (TraceScorer.length(task.strokes, task.aspect) / 1.4).clamp(1.2, 4.0).toDouble();
    const hold = 0.5;
    _demoDrawShare = seconds / (seconds + hold);
    _demo.duration = Duration(milliseconds: ((seconds + hold) * 1000).round());
    _demo.addStatusListener((s) {
      if (s == AnimationStatus.completed) _demo.reset();
    });
  }

  @override
  void dispose() {
    _demo.dispose();
    super.dispose();
  }

  Point2 _toNorm(Offset local) => Point2(
        ((local.dx - _inner.left) / _inner.width).clamp(-0.25, 1.25).toDouble(),
        ((local.dy - _inner.top) / _inner.height).clamp(-0.25, 1.25).toDouble(),
      );

  void _down(PointerDownEvent e) {
    if (_solved || _pointer != null) return;
    if (_demo.isAnimating) _demo.reset();
    _pointer = e.pointer;
    setState(() => _current = [_toNorm(e.localPosition)]);
  }

  void _move(PointerMoveEvent e) {
    if (e.pointer != _pointer || _current == null) return;
    final p = _toNorm(e.localPosition);
    final last = _current!.last;
    // Juda yaqin nuqtalarni yozmaymiz (ortiqcha hisob-kitob bo'lmasin).
    if ((p.x - last.x).abs() * task.aspect + (p.y - last.y).abs() < 0.006) return;
    setState(() => _current!.add(p));
  }

  void _up(PointerEvent e) {
    if (e.pointer != _pointer) return;
    _pointer = null;
    final stroke = _current;
    setState(() => _current = null);
    if (stroke == null || _solved) return;
    if (stroke.length < 2 || TraceScorer.length([stroke], task.aspect) < 0.03) return; // tasodifiy tegish
    setState(() => _strokes.add(stroke));
    _check(stroke);
  }

  void _check(List<Point2> latest) {
    final report = TraceScorer.evaluate(task, _strokes);
    if (report.passed(task)) {
      _solve();
      return;
    }
    if (TraceScorer.strokeOffPath(task, latest) > 0.5) {
      // Bu chiziq yo'ldan uzoqda — faqat uni o'chiramiz.
      setState(() => _strokes.removeLast());
      _mistake();
      return;
    }
    if (task.leftToRight && !TraceScorer.leftToRightOk([latest])) {
      setState(() => _strokes.removeLast());
      _mistake();
      return;
    }
    final allDrawn = report.coverage >= task.minCoverage && report.minStrokeCoverage >= TraceScorer.minStrokeCoverage;
    if (allDrawn || report.lengthRatio > TraceScorer.maxLengthRatio || _strokes.length > _strokeLimit) {
      // Hammasi chizildi, lekin tartibsiz (yoki bo'yab tashlandi) — qaytadan.
      setState(() => _strokes.clear());
      _mistake();
    }
  }

  void _mistake() {
    setState(() {
      _mistakes++;
      _shake++;
    });
    widget.callbacks.onMistake(_mistakes);
    if (_mistakes >= TraceExerciseView.maxMistakes) {
      _solve();
    } else if (_mistakes == 2) {
      _showDemo();
    }
  }

  void _solve() {
    if (_solved) return;
    _demo.reset();
    setState(() => _solved = true);
    widget.callbacks.onSolved(_mistakes);
  }

  void _showDemo() {
    if (_solved) return;
    _demo.forward(from: 0);
  }

  void _clear() {
    if (_solved) return;
    setState(() {
      _strokes.clear();
      _current = null;
    });
  }

  @override
  Widget build(BuildContext context) {
    final label = task.label;
    return LayoutBuilder(builder: (context, c) {
      final labelH = label != null ? 52.0 : 0.0;
      const buttonsH = 64.0;
      final maxW = c.maxWidth.isFinite ? c.maxWidth : 400.0;
      final maxH = (c.maxHeight.isFinite ? c.maxHeight : 520.0) - labelH - buttonsH;
      const k = TraceExerciseView.insetRatio;
      final innerH = math.max(48.0, math.min(maxH / (1 + 2 * k), maxW / (task.aspect + 2 * k)));
      final pad = innerH * k;
      final innerW = innerH * task.aspect;
      _inner = Rect.fromLTWH(pad, pad, innerW, innerH);
      final size = Size(innerW + 2 * pad, innerH + 2 * pad);

      return Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Shake(
            trigger: _shake,
            child: Listener(
              key: const ValueKey('trace_area'),
              behavior: HitTestBehavior.opaque,
              onPointerDown: _down,
              onPointerMove: _move,
              onPointerUp: _up,
              onPointerCancel: _up,
              child: AnimatedBuilder(
                animation: _demo,
                builder: (context, _) => CustomPaint(
                  size: size,
                  painter: TracePainter(
                    task: task,
                    inner: _inner,
                    strokes: _strokes,
                    current: _current,
                    solved: _solved,
                    demo: _demo.isAnimating || _demo.value > 0 ? math.min(1.0, _demo.value / _demoDrawShare) : null,
                  ),
                ),
              ),
            ),
          ),
          if (label != null)
            SizedBox(
              height: labelH,
              child: Center(
                child: FittedBox(
                  fit: BoxFit.scaleDown,
                  child: Text(
                    label,
                    style: TextStyle(
                      fontSize: 34,
                      fontWeight: FontWeight.w900,
                      color: _solved ? AppColors.success : AppColors.textSoft,
                      letterSpacing: 4,
                    ),
                  ),
                ),
              ),
            ),
          SizedBox(
            height: buttonsH,
            // Tor ekranlarda ham sig'ishi uchun kichraytiriladi.
            child: FittedBox(
              fit: BoxFit.scaleDown,
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  _RoundButton(
                    key: const ValueKey('trace_clear'),
                    icon: Icons.cleaning_services_rounded,
                    label: 'Tozalash',
                    onTap: _solved ? null : _clear,
                  ),
                  const SizedBox(width: 20),
                  _RoundButton(
                    key: const ValueKey('trace_demo'),
                    icon: Icons.visibility_rounded,
                    label: 'Ko‘rsat',
                    onTap: _solved ? null : _showDemo,
                  ),
                ],
              ),
            ),
          ),
        ],
      );
    });
  }
}

class _RoundButton extends StatelessWidget {
  const _RoundButton({super.key, required this.icon, required this.label, required this.onTap});

  final IconData icon;
  final String label;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return OutlinedButton.icon(
      onPressed: onTap,
      style: OutlinedButton.styleFrom(
        minimumSize: const Size(120, 52),
        shape: const StadiumBorder(),
        side: const BorderSide(color: Color(0xFFD1C4E9), width: 2),
        foregroundColor: const Color(0xFF5E35B1),
        backgroundColor: Colors.white,
      ),
      icon: Icon(icon, size: 26),
      label: Text(label, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
    );
  }
}

/// Yozish maydonini chizadi: daftar chiziqlari, yo'naltiruvchi yo'lak, boshlanish
/// nuqtalari va strelkalar, raqamlangan nuqtalar, bola chizgan chiziqlar va namoyish.
class TracePainter extends CustomPainter {
  TracePainter({
    required this.task,
    required this.inner,
    required this.strokes,
    required this.current,
    required this.solved,
    this.demo,
  });

  final TraceTask task;
  final Rect inner;
  final List<List<Point2>> strokes;
  final List<Point2>? current;
  final bool solved;

  /// Namoyish jarayoni (0..1) yoki `null`.
  final double? demo;

  static const _lane = Color(0xFFEDE7F6);
  static const _guide = Color(0xFFB39DDB);
  static const _start = Color(0xFF2DBE72);
  static const _dot = Color(0xFF7E57C2);

  Offset _map(Point2 p) => Offset(inner.left + p.x * inner.width, inner.top + p.y * inner.height);

  Path _path(List<Point2> pts) {
    final path = Path();
    if (pts.isEmpty) return path;
    final first = _map(pts.first);
    path.moveTo(first.dx, first.dy);
    for (final p in pts.skip(1)) {
      final o = _map(p);
      path.lineTo(o.dx, o.dy);
    }
    return path;
  }

  @override
  void paint(Canvas canvas, Size size) {
    final h = inner.height;
    final bg = RRect.fromRectAndRadius(Offset.zero & size, const Radius.circular(24));
    canvas.drawRRect(bg, Paint()..color = Colors.white);
    canvas.drawRRect(
      bg,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2
        ..color = const Color(0xFFE3DDF2),
    );

    if (task.label != null) _copybookLines(canvas);

    if (task.dots) {
      _dots(canvas, h);
    } else {
      _guideStrokes(canvas, h);
    }

    final demo = this.demo;
    if (demo != null && !solved) _demoPath(canvas, h, demo);

    final ink = Paint()
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round
      ..strokeWidth = math.max(6.0, h * 0.045)
      ..color = solved ? AppColors.success : AppColors.primary;
    for (final s in strokes) {
      canvas.drawPath(_path(s), ink);
    }
    final cur = current;
    if (cur != null) {
      if (cur.length == 1) {
        canvas.drawCircle(_map(cur.first), ink.strokeWidth / 2, Paint()..color = ink.color);
      } else {
        canvas.drawPath(_path(cur), ink);
      }
    }
  }

  /// Daftar chiziqlari: yuqori, o'rta (uzuq) va asosiy chiziq.
  void _copybookLines(Canvas canvas) {
    final p = Paint()
      ..color = const Color(0xFFD6E4FF)
      ..strokeWidth = 2;
    for (final y in const [0.1, 0.9]) {
      final yy = inner.top + y * inner.height;
      canvas.drawLine(Offset(inner.left - 6, yy), Offset(inner.right + 6, yy), p);
    }
    final mid = inner.top + 0.5 * inner.height;
    for (var x = inner.left; x < inner.right; x += 14) {
      canvas.drawLine(Offset(x, mid), Offset(math.min(x + 7, inner.right), mid), p);
    }
  }

  void _guideStrokes(Canvas canvas, double h) {
    final lane = Paint()
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round
      ..strokeWidth = 2 * task.tolerance * h
      ..color = solved ? const Color(0xFFE6F8EE) : _lane;
    for (final s in task.strokes) {
      canvas.drawPath(_path(s), lane);
    }
    final dash = Paint()
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round
      ..strokeWidth = math.max(2.5, h * 0.012)
      ..color = _guide;
    for (final s in task.strokes) {
      _dashed(canvas, _path(s), dash, h * 0.035, h * 0.03);
    }
    if (solved) return;
    final numbered = task.strokes.length > 1;
    for (var i = task.strokes.length - 1; i >= 0; i--) {
      final s = task.strokes[i];
      if (s.length < 2) continue;
      _arrow(canvas, s, h);
      final r = math.max(11.0, h * 0.045);
      final o = _map(s.first);
      canvas.drawCircle(o, r, Paint()..color = _start);
      if (numbered) _label(canvas, '${i + 1}', o, r * 1.2, Colors.white);
    }
  }

  /// Boshlanish nuqtasidan biroz keyin yo'nalish strelkasi.
  void _arrow(Canvas canvas, List<Point2> s, double h) {
    final pts = [for (final p in s) _map(p)];
    final want = h * 0.16;
    var acc = 0.0;
    var at = pts.last, dir = pts.last - pts.first;
    for (var i = 1; i < pts.length; i++) {
      final seg = (pts[i] - pts[i - 1]).distance;
      if (acc + seg >= want && seg > 0) {
        final t = (want - acc) / seg;
        at = pts[i - 1] + (pts[i] - pts[i - 1]) * t;
        dir = pts[i] - pts[i - 1];
        break;
      }
      acc += seg;
    }
    if (dir.distance == 0) return;
    final u = dir / dir.distance;
    final n = Offset(-u.dy, u.dx);
    final len = math.max(10.0, h * 0.05);
    final tip = at + u * len * 0.6;
    final path = Path()
      ..moveTo(tip.dx, tip.dy)
      ..lineTo((at - u * len * 0.5 + n * len * 0.55).dx, (at - u * len * 0.5 + n * len * 0.55).dy)
      ..lineTo((at - u * len * 0.5 - n * len * 0.55).dx, (at - u * len * 0.5 - n * len * 0.55).dy)
      ..close();
    canvas.drawPath(path, Paint()..color = _start);
  }

  void _dots(Canvas canvas, double h) {
    final pts = task.strokes.first;
    final closed = pts.length > 2 && pts.first.distanceTo(pts.last) < 1e-6;
    final shown = closed ? pts.sublist(0, pts.length - 1) : pts;
    if (solved) {
      final line = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = math.max(4.0, h * 0.02)
        ..strokeJoin = StrokeJoin.round
        ..color = const Color(0xFFB9F0D2);
      canvas.drawPath(_path(pts), line);
    }
    final r = math.max(7.0, h * 0.028);
    final center = _map(Point2(
      shown.map((p) => p.x).reduce((a, b) => a + b) / shown.length,
      shown.map((p) => p.y).reduce((a, b) => a + b) / shown.length,
    ));
    for (var i = 0; i < shown.length; i++) {
      final o = _map(shown[i]);
      final first = i == 0;
      canvas.drawCircle(o, first ? r * 1.35 : r, Paint()..color = first && !solved ? _start : _dot);
      // Raqam nuqtadan tashqariga (shakl markazidan uzoqroqqa) yoziladi.
      var away = o - center;
      away = away.distance == 0 ? const Offset(0, -1) : away / away.distance;
      _label(canvas, '${i + 1}', o + away * r * 2.6, r * 2.1, AppColors.text);
    }
  }

  void _demoPath(Canvas canvas, double h, double t) {
    final metrics = [
      for (final s in task.strokes) ..._path(s).computeMetrics(),
    ];
    final sum = metrics.fold<double>(0, (a, m) => a + m.length);
    if (sum == 0) return;
    var remaining = sum * t;
    final p = Paint()
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round
      ..strokeWidth = math.max(6.0, h * 0.04)
      ..color = AppColors.star;
    Offset? head;
    for (final m in metrics) {
      if (remaining <= 0) break;
      final len = math.min(remaining, m.length);
      canvas.drawPath(m.extractPath(0, len), p);
      head = m.getTangentForOffset(len)?.position;
      remaining -= m.length;
    }
    if (head != null) {
      canvas.drawCircle(head, math.max(10.0, h * 0.045), Paint()..color = const Color(0xCCFF9F43));
    }
  }

  void _dashed(Canvas canvas, Path path, Paint paint, double on, double off) {
    for (final m in path.computeMetrics()) {
      var d = 0.0;
      while (d < m.length) {
        canvas.drawPath(m.extractPath(d, math.min(d + on, m.length)), paint);
        d += on + off;
      }
    }
  }

  void _label(Canvas canvas, String text, Offset center, double fontSize, Color color) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(fontSize: fontSize, fontWeight: FontWeight.w900, color: color)),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(TracePainter old) => true;
}
