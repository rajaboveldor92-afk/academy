import 'dart:async';
import 'dart:math' as math;
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/providers.dart';
import '../../models/child_profile.dart';
import '../session/session_controller.dart';
import 'full_chess_game.dart';

class FullChessScreen extends ConsumerStatefulWidget {
  const FullChessScreen({super.key, required this.profile});
  final ChildProfile profile;
  @override
  ConsumerState<FullChessScreen> createState() => _FullChessScreenState();
}

class _FullChessScreenState extends ConsumerState<FullChessScreen> with WidgetsBindingObserver {
  late FullChessGame game;
  String? selected;
  Map<String, dynamic>? hint;
  bool busy = false, flipped = false, foreground = true;
  int generation = 0;
  Future<void> writes = Future.value();
  String t(String uz, String ru, String en) => switch (widget.profile.language) { 'ru' => ru, 'en' => en, _ => uz };
  bool get blocked => busy || game.finished || ref.read(sessionProvider).limitReached;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    game = FullChessGame(difficulty: widget.profile.age < 6 ? 0 : 1, help: widget.profile.age <= 6);
    final saved = ref.read(databaseProvider).getChessGame(widget.profile.id);
    if (saved != null) {
      try { game = FullChessGame.restore(saved); }
      catch (_) { WidgetsBinding.instance.addPostFrameCallback((_) { if (mounted) _message(t('Saqlangan o‘yin ochilmadi. Yangi o‘yin boshlandi.', 'Не удалось открыть сохранение. Начата новая игра.', 'Could not load the save. A new game has started.')); }); }
    }
    WidgetsBinding.instance.addPostFrameCallback((_) => _computer());
  }

  @override
  void dispose() { generation++; WidgetsBinding.instance.removeObserver(this); super.dispose(); }
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    foreground = state == AppLifecycleState.resumed;
    if (!foreground) { generation++; busy = false; }
    else { setState(() {}); _computer(); }
  }

  void _message(String text) => ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(text)));
  void _save() {
    final data = game.toMap();
    final db = ref.read(databaseProvider);
    writes = writes.then((_) => db.saveChessGame(widget.profile.id, data)).catchError((Object e) {
      if (mounted) _message(t('O‘yinni saqlab bo‘lmadi.', 'Не удалось сохранить игру.', 'Could not save the game.'));
    });
  }

  Future<void> _computer() async {
    if (!mounted || !foreground || busy || !game.computerTurn || ref.read(sessionProvider).limitReached) return;
    final ticket = ++generation;
    setState(() => busy = true);
    try {
      final move = await compute(chooseFullChessMove, {'game': game.toMap(), 'depth': [0, 2, 3][game.difficulty]});
      if (!mounted || ticket != generation || !foreground || ref.read(sessionProvider).limitReached) return;
      setState(() { if (move != null) game.play(move); busy = false; });
      _save();
    } catch (_) {
      if (!mounted || ticket != generation) return;
      setState(() => busy = false);
      _message(t('Qayta urinish uchun doskani bosing.', 'Нажмите на доску, чтобы повторить.', 'Tap the board to retry.'));
    }
  }

  Future<void> _tap(String square) async {
    if (blocked || !foreground) return;
    if (game.computerTurn) { _computer(); return; }
    final legal = game.moves.where((m) => m['from'] == selected && m['to'] == square).toList();
    if (legal.isNotEmpty) {
      var move = legal.first;
      if (legal.length > 1) {
        final ticket = generation;
        final promotion = await showDialog<String>(context: context, builder: (context) => AlertDialog(
          title: Text(t('Qaysi donaga aylantiramiz?', 'Выберите фигуру', 'Promote to which piece?')),
          content: Wrap(spacing: 8, children: [for (final type in ['q', 'r', 'b', 'n'])
            TextButton(onPressed: () => Navigator.pop(context, type), child: Text(_glyph(type, game.whiteTurn), style: const TextStyle(fontSize: 42)))]),
        ));
        if (!mounted || promotion == null || ticket != generation || !foreground || ref.read(sessionProvider).limitReached) return;
        move = legal.firstWhere((m) => m['promotion'] == promotion);
      }
      setState(() { game.play(move); selected = null; hint = null; });
      _save(); _computer();
    } else {
      final piece = game.board.get(square);
      final own = piece != null && piece.color == game.board.turn;
      setState(() { selected = own && selected != square ? square : null; hint = null; });
    }
  }

  Future<void> _hint() async {
    if (blocked || game.computerTurn) return;
    final ticket = ++generation;
    setState(() => busy = true);
    try {
      final move = await compute(chooseFullChessMove, {'game': game.toMap(), 'depth': 2});
      if (!mounted || ticket != generation || !foreground) return;
      setState(() { hint = move; selected = move?['from'] as String?; busy = false; });
    } catch (_) { if (mounted && ticket == generation) setState(() => busy = false); }
  }

  Future<void> _newGame() async {
    var mode = game.mode;
    var level = game.difficulty;
    var help = game.help;
    final ok = await showDialog<bool>(context: context, builder: (ctx) => StatefulBuilder(builder: (ctx, change) => AlertDialog(
      title: Text(t('Yangi o‘yin', 'Новая игра', 'New game')),
      content: SingleChildScrollView(child: Column(mainAxisSize: MainAxisSize.min, children: [
        Text(t('Joriy o‘yin o‘rniga yangisi saqlanadi.', 'Текущая игра будет заменена.', 'This replaces the saved game.')),
        DropdownButton<String>(isExpanded: true, value: mode, items: [
          DropdownMenuItem(value: 'computer', child: Text(t('Kompyuterga qarshi', 'С компьютером', 'Vs computer'))),
          DropdownMenuItem(value: 'local', child: Text(t('Ikki kishi', 'Два игрока', 'Two players'))),
        ], onChanged: (v) => change(() => mode = v!)),
        if (mode == 'computer') DropdownButton<int>(isExpanded: true, value: level, items: [
          DropdownMenuItem(value: 0, child: Text(t('Oson', 'Легко', 'Easy'))),
          DropdownMenuItem(value: 1, child: Text(t('O‘rta', 'Средне', 'Medium'))),
          DropdownMenuItem(value: 2, child: Text(t('Qiyin', 'Сложно', 'Hard'))),
        ], onChanged: (v) => change(() => level = v!)),
        SwitchListTile(contentPadding: EdgeInsets.zero, title: Text(t('O‘rgatuvchi yordam', 'Подсказки', 'Learning help')), value: help, onChanged: (v) => change(() => help = v)),
      ])),
      actions: [TextButton(onPressed: () => Navigator.pop(ctx, false), child: Text(t('Bekor qilish', 'Отмена', 'Cancel'))),
        FilledButton(onPressed: () => Navigator.pop(ctx, true), child: Text(t('Boshlash', 'Начать', 'Start')))],
    )));
    if (ok != true || !mounted) return;
    generation++;
    setState(() { game = FullChessGame(mode: mode, difficulty: level, help: help); selected = null; hint = null; busy = false; });
    _save();
  }

  String get status {
    if (game.board.in_checkmate) return game.whiteTurn ? t('Mot! Qoralar yutdi.', 'Мат! Чёрные выиграли.', 'Checkmate! Black wins.') : t('Mot! Oqlar yutdi.', 'Мат! Белые выиграли.', 'Checkmate! White wins.');
    if (game.board.in_stalemate) return t('Pat — durang.', 'Пат — ничья.', 'Stalemate — draw.');
    if (game.board.in_draw) return t('Durang.', 'Ничья.', 'Draw.');
    if (busy) return t('O‘ylayapti…', 'Думает…', 'Thinking…');
    final turn = game.whiteTurn ? t('Oqlar yuradi', 'Ход белых', 'White to move') : t('Qoralar yuradi', 'Ход чёрных', 'Black to move');
    return game.board.in_check ? '${t('Shoh!', 'Шах!', 'Check!')} $turn' : turn;
  }

  static String _glyph(String type, bool white) => (white ? const {'k':'♔','q':'♕','r':'♖','b':'♗','n':'♘','p':'♙'} : const {'k':'♚','q':'♛','r':'♜','b':'♝','n':'♞','p':'♟'})[type]!;

  @override
  Widget build(BuildContext context) {
    final limit = ref.watch(sessionProvider).limitReached;
    final targets = selected == null || !game.help ? <String>{} : game.moves.where((m) => m['from'] == selected).map((m) => m['to'] as String).toSet();
    return Scaffold(
      appBar: AppBar(title: Text(t('Shaxmat o‘ynash', 'Игра в шахматы', 'Play chess'))),
      body: SafeArea(child: SingleChildScrollView(child: Center(child: ConstrainedBox(constraints: const BoxConstraints(maxWidth: 580), child: Padding(
        padding: const EdgeInsets.all(12), child: Column(children: [
          Text(game.mode == 'computer' ? t('Siz — oqlar • Kompyuter — qoralar', 'Вы — белые • Компьютер — чёрные', 'You — White • Computer — Black') : t('Ikki kishi • Navbat bilan o‘ynang', 'Два игрока • Играйте по очереди', 'Two players • Take turns')),
          const SizedBox(height: 10),
          Semantics(liveRegion: true, child: Text(limit ? t('Dam olish vaqti', 'Время отдыхать', 'Time for a break') : status, key: const Key('full_chess_status'), style: Theme.of(context).textTheme.titleLarge)),
          const SizedBox(height: 12),
          LayoutBuilder(builder: (ctx, box) {
            final side = math.min(box.maxWidth, 520.0);
            final cell = side / 8;
            return SizedBox(width: side, height: side, child: GridView.builder(
              physics: const NeverScrollableScrollPhysics(), padding: EdgeInsets.zero,
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 8), itemCount: 64,
              itemBuilder: (ctx, index) {
                final i = flipped ? 63-index : index;
                final square = '${'abcdefgh'[i%8]}${8-i~/8}';
                final piece = game.board.get(square);
                final white = piece != null && piece.color.toString().endsWith('WHITE');
                var color = (i~/8+i%8).isEven ? const Color(0xFFF0D9B5) : const Color(0xFFB58863);
                if (selected == square) color = const Color(0xFFF6D55C);
                if (hint?['to'] == square) color = const Color(0xFF80CBC4);
                return Semantics(label: '$square ${piece?.type.name ?? ''}', button: true, child: InkWell(
                  key: Key('full_square_$square'), onTap: limit ? null : () => _tap(square),
                  child: Container(color: color, child: Stack(alignment: Alignment.center, children: [
                    if (piece != null) Text(_glyph(piece.type.name, white), style: TextStyle(fontSize: cell*.78, height: 1, color: Colors.black)),
                    if (targets.contains(square)) Container(width: cell*.25, height: cell*.25, decoration: BoxDecoration(color: Colors.teal.withAlpha(160), shape: BoxShape.circle)),
                    Positioned(left: 2, bottom: 1, child: Text(square, style: TextStyle(fontSize: math.max(8, cell*.16), color: Colors.black54))),
                  ])),
                ));
              },
            ));
          }),
          if (hint != null) Padding(padding: const EdgeInsets.all(8), child: Text('${t('Maslahat', 'Подсказка', 'Hint')}: ${hint!['from']} → ${hint!['to']}')),
          Wrap(alignment: WrapAlignment.center, spacing: 8, children: [
            TextButton.icon(onPressed: game.history.isEmpty || limit ? null : () { generation++; setState(() { game.undo(); busy = false; selected = null; hint = null; }); _save(); }, icon: const Icon(Icons.undo), label: Text(t('Qaytarish', 'Отменить ход', 'Undo'))),
            if (game.help) TextButton.icon(onPressed: blocked || game.computerTurn ? null : _hint, icon: const Icon(Icons.lightbulb_outline), label: Text(t('Maslahat', 'Подсказка', 'Hint'))),
            TextButton.icon(onPressed: () => setState(() => flipped = !flipped), icon: const Icon(Icons.flip_camera_android), label: Text(t('Aylantirish', 'Повернуть', 'Flip'))),
          ]),
          FilledButton.icon(onPressed: limit ? null : _newGame, icon: const Icon(Icons.refresh), label: Text(t('Yangi o‘yin / Rejim', 'Новая игра / Режим', 'New game / Mode'))),
          const SizedBox(height: 12),
          Text(t('Yurishlar avtomatik saqlanadi. Kompyuterga qarshi o‘yinda oqlar bilan o‘ynaysiz.', 'Ходы сохраняются автоматически. С компьютером вы играете белыми.', 'Moves save automatically. You play White against the computer.'), textAlign: TextAlign.center),
          if (game.history.isNotEmpty) ExpansionTile(title: Text(t('Yurishlar', 'Ходы', 'Moves')), children: [Padding(padding: const EdgeInsets.all(8), child: Text([for (var i=0;i<game.history.length;i+=2) '${i~/2+1}. ${game.history[i]} ${i+1<game.history.length ? game.history[i+1] : ''}'].join('   ')))]),
        ]),
      ))))),
    );
  }
}
