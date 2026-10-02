import 'package:flutter/material.dart';

import '../models/exercise.dart';
import 'option_card.dart';

/// Live ideal series loop; editing never earns a star until the task is checked.
class CircuitExerciseView extends StatefulWidget {
  const CircuitExerciseView({
    super.key,
    required this.exercise,
    required this.callbacks,
  });
  final Exercise exercise;
  final ExerciseCallbacks callbacks;
  @override
  State<CircuitExerciseView> createState() => _CircuitExerciseViewState();
}

class _CircuitExerciseViewState extends State<CircuitExerciseView> {
  late bool _a, _b, _closed;
  bool _solved = false;
  int _mistakes = 0;
  String? _message;
  CircuitTask get task => widget.exercise.circuit!;
  bool get lit => CircuitTask.lampLit(_a, _b, _closed);
  String tr(String uz, String en, String ru) =>
      switch (widget.exercise.speechLang) {
        'en' => en,
        'ru' => ru,
        _ => uz,
      };

  @override
  void initState() {
    super.initState();
    _a = task.wireA;
    _b = task.wireB;
    _closed = task.switchClosed;
  }

  void _check() {
    if (_solved) return;
    if (_a && _b && lit == task.targetLit) {
      setState(() => _solved = true);
      widget.callbacks.onSolved(_mistakes);
    } else {
      setState(() {
        _mistakes++;
        _message = !_a || !_b
            ? tr(
                'Ikkala simni ulang, so‘ng kalit holatini tekshiring.',
                'Connect both wires, then check the switch.',
                'Подключите оба провода, затем проверьте выключатель.',
              )
            : tr(
                'Kalit holatini topshiriqqa mos o‘zgartiring.',
                'Change the switch to meet the task.',
                'Измените положение выключателя по заданию.',
              );
      });
      widget.callbacks.onMistake(_mistakes);
    }
  }

  @override
  Widget build(BuildContext context) => SingleChildScrollView(
    padding: const EdgeInsets.all(8),
    child: Column(
      children: [
        Text(
          tr(
            'Virtual tajriba · 3 V batareya',
            'Virtual experiment · 3 V battery',
            'Виртуальный опыт · батарея 3 В',
          ),
          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
        ),
        SizedBox(
          height: 190,
          child: LayoutBuilder(
            builder: (context, size) => Stack(
              children: [
                Positioned.fill(
                  child: CustomPaint(
                    painter: _CircuitPainter(
                      a: _a,
                      b: _b,
                      closed: _closed,
                      lit: lit,
                    ),
                  ),
                ),
                Positioned(
                  left: 0,
                  top: 85,
                  width: size.maxWidth * .28,
                  child: Text(
                    '🔋\n3 V',
                    textAlign: TextAlign.center,
                    style: const TextStyle(fontSize: 25),
                  ),
                ),
                Positioned(
                  left: size.maxWidth * .72,
                  top: 72,
                  width: size.maxWidth * .28,
                  child: Semantics(
                    label: lit ? 'lamp_on' : 'lamp_off',
                    child: AnimatedContainer(
                      key: ValueKey(lit ? 'lamp_on' : 'lamp_off'),
                      duration: const Duration(milliseconds: 250),
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: lit
                            ? Colors.yellow.shade200
                            : Colors.grey.shade200,
                        boxShadow: lit
                            ? [
                                const BoxShadow(
                                  color: Colors.amber,
                                  blurRadius: 20,
                                ),
                              ]
                            : [],
                      ),
                      child: Text(
                        lit ? '💡' : '⚪',
                        textAlign: TextAlign.center,
                        style: const TextStyle(fontSize: 36),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
        Text(
          lit
              ? tr('Lampochka yonmoqda', 'Lamp is on', 'Лампа горит')
              : tr('Lampochka o‘chiq', 'Lamp is off', 'Лампа выключена'),
          style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 19),
        ),
        SwitchListTile(
          key: const Key('circuit_wire_a'),
          title: Text(
            tr(
              'Batareya → kalit simi',
              'Battery → switch wire',
              'Провод: батарея → выключатель',
            ),
          ),
          value: _a,
          onChanged: _solved
              ? null
              : (v) => setState(() {
                  _a = v;
                  _message = null;
                }),
        ),
        SwitchListTile(
          key: const Key('circuit_wire_b'),
          title: Text(
            tr(
              'Lampochka → batareya simi',
              'Lamp → battery wire',
              'Провод: лампа → батарея',
            ),
          ),
          value: _b,
          onChanged: _solved
              ? null
              : (v) => setState(() {
                  _b = v;
                  _message = null;
                }),
        ),
        SwitchListTile(
          key: const Key('circuit_switch'),
          title: Text(
            tr('Kalitni yopish', 'Close the switch', 'Замкнуть выключатель'),
          ),
          value: _closed,
          onChanged: _solved
              ? null
              : (v) => setState(() {
                  _closed = v;
                  _message = null;
                }),
        ),
        if (_message != null)
          Text(
            _message!,
            key: const Key('circuit_hint'),
            textAlign: TextAlign.center,
          ),
        FilledButton(
          key: const Key('circuit_check'),
          onPressed: _solved ? null : _check,
          child: Text(tr('Tekshirish', 'Check', 'Проверить')),
        ),
      ],
    ),
  );
}

class _CircuitPainter extends CustomPainter {
  const _CircuitPainter({
    required this.a,
    required this.b,
    required this.closed,
    required this.lit,
  });
  final bool a, b, closed, lit;
  @override
  void paint(Canvas canvas, Size size) {
    final p = Paint()
      ..strokeWidth = 4
      ..style = PaintingStyle.stroke;
    Offset pt(double x, double y) => Offset(size.width * x, size.height * y);
    void line(double x, double y, double u, double v, bool connected) {
      p.color = connected
          ? (lit ? Colors.amber.shade800 : Colors.blue.shade700)
          : Colors.grey.shade400;
      if (connected) {
        canvas.drawLine(pt(x, y), pt(u, v), p);
      } else {
        canvas.drawLine(pt(x, y), Offset.lerp(pt(x, y), pt(u, v), .4)!, p);
        canvas.drawLine(Offset.lerp(pt(x, y), pt(u, v), .6)!, pt(u, v), p);
      }
    }

    line(.14, .5, .14, .2, true);
    line(.14, .2, .44, .2, a);
    line(.44, .2, .56, closed ? .2 : .08, true);
    line(.56, .2, .86, .2, true);
    line(.86, .2, .86, .5, true);
    line(.86, .65, .86, .85, true);
    line(.86, .85, .14, .85, b);
    line(.14, .85, .14, .68, true);
  }

  @override
  bool shouldRepaint(_CircuitPainter old) =>
      a != old.a || b != old.b || closed != old.closed || lit != old.lit;
}
