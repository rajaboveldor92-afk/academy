import 'dart:math' as math;

import '../../models/speech_part.dart';
import 'visual.dart';

/// Uch tildagi matn.
class Localized {
  const Localized({required this.uz, required this.en, required this.ru});

  const Localized.same(String text)
      : uz = text,
        en = text,
        ru = text;

  final String uz;
  final String en;
  final String ru;

  String of(String lang) => switch (lang) {
        'en' => en,
        'ru' => ru,
        _ => uz,
      };

  bool get isComplete => uz.trim().isNotEmpty && en.trim().isNotEmpty && ru.trim().isNotEmpty;

  Map<String, String> toJson() => {'uz': uz, 'en': en, 'ru': ru};

  static Localized fromJson(Object? json) {
    if (json is Map) {
      return Localized(
        uz: (json['uz'] ?? '').toString(),
        en: (json['en'] ?? '').toString(),
        ru: (json['ru'] ?? '').toString(),
      );
    }
    return Localized.same(json?.toString() ?? '');
  }
}

/// Mashq turi — qaysi o'yin mexanikasi ishlatiladi.
enum ExerciseKind {
  /// Virtual battery–switch–lamp loop (Technology).
  circuit,

  /// Variantlardan birini tanlash (yoki [Exercise.dragToTarget] bo'lsa sudrab qo'yish).
  choice,

  /// Chap va o'ng ustunlardagi juftlarni moslashtirish.
  match,

  /// Narsalarni savatlarga ajratish (guruhlash).
  sort,

  /// Avval rasmni eslab qolish, keyin savol.
  memory,

  /// Labirint: qahramonni uyga olib borish.
  maze,

  /// 4×4 (yoki 3×3) mini-sudoku.
  sudoku,

  /// Strelkalar bilan dastur tuzish (kodlash).
  coding,

  /// Bo'laklardan (harf, bo'g'in, so'z) to'g'ri tartibda yig'ish.
  assemble,

  /// Barmoq bilan chiziq/harf ustidan yurib yozish.
  trace,

  /// Shaxmat doskasi: katakni bosish, figurani yurish (sudrab yoki bosib), mini-o'yin.
  chess,

  /// Juft kartalar (xotira): yopiq kartalardan bir xil rasmlarni topish.
  cards,

  /// Rasm ichidan kerakli narsalarni bosib topish (diqqat, farqni top, pufaklar).
  spot,

  /// Rasmli puzzle: bo'laklarni sudrab joyiga qo'yish.
  jigsaw,

  /// "Ota-ona bilan bajaramiz": ekrandan tashqari faoliyat kartasi.
  activity,

  /// Javobni klaviaturada yozish (maktab: son, kasr, o'nli kasr).
  input,
}

/// Javob varianti: rasm (visual) va/yoki matn.
class ExerciseOption {
  const ExerciseOption({this.visual, this.text, this.speech});

  final ExerciseVisual? visual;
  final String? text;

  /// Variant bosilganda (kichik yoshda) aytiladigan matn.
  final String? speech;

  String describe() => '${text ?? ''}|${visual?.describe() ?? ''}';
}

class MatchPair {
  const MatchPair(this.left, this.right);

  final ExerciseOption left;
  final ExerciseOption right;
}

/// Guruhlash topshirig'i.
class SortTask {
  const SortTask({required this.bins, required this.items, required this.itemBins});

  /// Savatlar (masalan: 🔴 qizil / 🔵 ko'k).
  final List<ExerciseOption> bins;
  final List<ExerciseOption> items;

  /// Har bir narsa qaysi savatga tegishli (indeks).
  final List<int> itemBins;
}

/// Ideal low-voltage series circuit: both wires and switch must be closed.
class CircuitTask {
  const CircuitTask({required this.targetLit, this.wireA = false, this.wireB = false, this.switchClosed = false});
  final bool targetLit;
  final bool wireA;
  final bool wireB;
  final bool switchClosed;
  static bool lampLit(bool wireA, bool wireB, bool switchClosed) => wireA && wireB && switchClosed;
  bool get initiallyLit => lampLit(wireA, wireB, switchClosed);
  String describe() => 'circuit:$targetLit:$wireA:$wireB:$switchClosed';
}

/// Labirint: [walls] — har bir katak uchun devorlar bitmaskasi
/// (1 = yuqori, 2 = o'ng, 4 = past, 8 = chap).
class MazeTask {
  const MazeTask({
    required this.rows,
    required this.cols,
    required this.walls,
    required this.start,
    required this.goal,
    required this.hero,
    required this.target,
  });

  static const int top = 1, right = 2, bottom = 4, left = 8;

  final int rows;
  final int cols;
  final List<int> walls;
  final int start;
  final int goal;
  final String hero;
  final String target;

  bool canMove(int cell, int dir) => walls[cell] & dir == 0;

  /// Yo'nalish bo'yicha qo'shni katak (chegara yoki devor bo'lsa `null`).
  int? neighbor(int cell, int dir) {
    if (!canMove(cell, dir)) return null;
    final r = cell ~/ cols, c = cell % cols;
    switch (dir) {
      case top:
        return r > 0 ? cell - cols : null;
      case bottom:
        return r < rows - 1 ? cell + cols : null;
      case left:
        return c > 0 ? cell - 1 : null;
      case right:
        return c < cols - 1 ? cell + 1 : null;
    }
    return null;
  }

  /// Eng qisqa yo'l uzunligi (BFS) — yechim borligini tekshirish uchun.
  int? shortestPath() {
    final dist = List<int>.filled(rows * cols, -1);
    final queue = <int>[start];
    dist[start] = 0;
    for (var i = 0; i < queue.length; i++) {
      final cell = queue[i];
      if (cell == goal) return dist[cell];
      for (final d in const [top, right, bottom, left]) {
        final n = neighbor(cell, d);
        if (n != null && dist[n] < 0) {
          dist[n] = dist[cell] + 1;
          queue.add(n);
        }
      }
    }
    return null;
  }

  String describe() => 'maze${rows}x$cols:$start>$goal:${walls.join(",")}';
}

/// Mini-sudoku. [solution] uzunligi size*size; [givens] — oldindan berilgan kataklar.
class SudokuTask {
  const SudokuTask({
    required this.size,
    required this.solution,
    required this.givens,
    required this.symbols,
  });

  final int size;

  /// Har katak uchun belgi indeksi (0..size-1).
  final List<int> solution;
  final List<bool> givens;

  /// Belgilar: raqamlar, emoji yoki rang nomlari (`color:red`).
  final List<String> symbols;

  int get blanks => givens.where((g) => !g).length;

  String describe() =>
      'sudoku$size:${[for (var i = 0; i < solution.length; i++) givens[i] ? solution[i] : '_'].join()}:${symbols.join()}';
}

/// Kodlash: robotni strelkalar bilan maqsadga olib borish.
class CodingTask {
  const CodingTask({
    required this.rows,
    required this.cols,
    required this.start,
    required this.goal,
    required this.blocked,
    required this.hero,
    required this.target,
    required this.maxSteps,
  });

  final int rows;
  final int cols;
  final int start;
  final int goal;
  final Set<int> blocked;
  final String hero;
  final String target;
  final int maxSteps;

  /// Dasturni bajaradi: 'U','D','L','R'. Maqsadga yetsa `true`.
  bool run(List<String> program) {
    var cell = start;
    for (final step in program) {
      final r = cell ~/ cols, c = cell % cols;
      int? next;
      switch (step) {
        case 'U':
          next = r > 0 ? cell - cols : null;
        case 'D':
          next = r < rows - 1 ? cell + cols : null;
        case 'L':
          next = c > 0 ? cell - 1 : null;
        case 'R':
          next = c < cols - 1 ? cell + 1 : null;
      }
      if (next == null || blocked.contains(next)) return false;
      cell = next;
    }
    return cell == goal;
  }

  String describe() => 'code${rows}x$cols:$start>$goal:${(blocked.toList()..sort()).join(",")}';
}

/// Bo'laklardan yig'ish: [answer] — to'g'ri tartibdagi bo'laklar,
/// [tiles] — ekranda aralash ko'rsatiladigan bo'laklar (chalg'ituvchilar bo'lishi mumkin).
class AssembleTask {
  const AssembleTask({required this.answer, required this.tiles, this.separator = ''});

  final List<String> answer;
  final List<String> tiles;

  /// Yig'ilgan natijani ko'rsatishda bo'laklar orasidagi belgi ('' — so'z, ' ' — gap).
  final String separator;

  String get result => answer.join(separator);

  String describe() => 'asm:${answer.join("|")}:${(List<String>.from(tiles)..sort()).join("|")}';
}

/// Juft kartalar: [faces] — kartalar tartibi (har bir rasm ikki marta).
class CardsTask {
  const CardsTask({required this.faces, required this.cols});

  final List<String> faces;
  final int cols;

  int get pairs => faces.length ~/ 2;

  String describe() => 'cards$cols:${(List<String>.from(faces)..sort()).join()}';
}

/// Rasm ichidan topish: [items] — sahnadagi narsalar, [targets] — bosilishi kerak bo'lganlar.
/// [reference] bo'lsa — "farqni top": yuqorida namunaviy rasm, pastdagisida bitta narsa boshqacha.
class SpotTask {
  const SpotTask({required this.items, required this.targets, this.aspect = 1.4, this.reference});

  final List<SceneItem> items;
  final Set<int> targets;
  final double aspect;
  final List<SceneItem>? reference;

  String describe() {
    final t = targets.toList()..sort();
    final ref = reference == null ? '' : '|ref:${reference!.map((e) => e.describe()).join(';')}';
    return 'spot:${items.map((e) => e.describe()).join(';')}>${t.join(',')}$ref';
  }
}

/// Rasmli puzzle: [picture] [rows]×[cols] bo'lakka bo'linadi.
class JigsawTask {
  const JigsawTask({required this.picture, required this.rows, required this.cols});

  final PictureVisual picture;
  final int rows;
  final int cols;

  int get pieces => rows * cols;

  String describe() => 'jigsaw${rows}x$cols:${picture.describe()}';
}

/// Ekrandan tashqari faoliyat (Montessori uslubida, ota-ona bilan).
class ActivityTask {
  const ActivityTask({
    required this.id,
    required this.emoji,
    required this.title,
    required this.materials,
    required this.steps,
    required this.benefit,
    this.minutes = 10,
  });

  final String id;
  final String emoji;
  final String title;
  final List<String> materials;
  final List<String> steps;

  /// Bola nimani o'rganadi (ota-ona uchun).
  final String benefit;
  final int minutes;

  String describe() => 'activity:$id';
}

/// Javobni yozish: ekrandagi klaviatura bilan son, kasr (`3/4`) yoki o'nli kasr (`2,5`).
class InputTask {
  const InputTask({
    required this.answer,
    this.accept = const [],
    this.keys = 'digits',
    this.unit = '',
    this.flash = const [],
    this.flashMs = 1500,
    this.rods = 0,
  });

  /// To'g'ri javob (ekranda ko'rsatiladigan ko'rinishi).
  final String answer;

  /// Qabul qilinadigan boshqa yozuvlar (masalan `0,5` va `,5`).
  final List<String> accept;

  /// Klaviatura: `digits`, `fraction` (+ `/`), `decimal` (+ `,`), `signed` (+ `−`);
  /// `abacus` — klaviatura o'rniga abakus (soroban): bola munchoqlarni surib sonni qo'yadi.
  final String keys;

  /// Flesh-anzan: sonlar ekranda birin-ketin ko'rsatiladi (`7`, `+5`, `−3`), keyin javob yoziladi.
  final List<String> flash;

  /// Har bir son ekranda necha millisekund turadi.
  final int flashMs;

  /// Abakus ustunlari soni (`keys == 'abacus'`).
  final int rods;

  bool get isAbacus => keys == 'abacus';

  /// Javob yonidagi birlik (`sm`, `kg`, `so‘m`) — faqat ko'rsatish uchun.
  final String unit;

  static String normalize(String s) =>
      s.replaceAll(' ', '').replaceAll('.', ',').replaceAll('−', '-').replaceAll(RegExp(r'^\+'), '');

  bool isCorrect(String value) {
    final v = normalize(value);
    if (v.isEmpty) return false;
    if (v == normalize(answer)) return true;
    return accept.any((a) => normalize(a) == v);
  }

  String describe() => 'input:$answer${flash.isEmpty ? '' : ':flash:${flash.join(',')}@$flashMs'}${isAbacus ? ':abacus$rods' : ''}';
}

/// Shaxmat topshirig'i. Katak raqami: `qator * size + ustun` (0-qator — yuqorida).
///
/// [goal]:
/// * `tap_light`, `tap_dark`, `tap_star`, `tap_square` ([target]), `tap_piece` ([pieceType]);
/// * `move_star`, `collect` (hamma yulduzchalar), `capture` ([target]), `safe_capture`,
///   `check`, `escape`, `defend` ([target] — hujumdagi figura), `mate`;
/// * `play` — [game] bo'yicha AI ([ai]: `very_easy` / `easy`) bilan mini-o'yin.
class ChessTask {
  const ChessTask({
    required this.size,
    required this.goal,
    this.pieces = const {},
    this.stars = const {},
    this.target,
    this.pieceType,
    this.coords = false,
    this.game,
    this.ai,
    this.highlight = const {},
  });

  final int size;
  final String goal;
  final Map<int, String> pieces;
  final Set<int> stars;
  final int? target;
  final String? pieceType;

  /// Doska chetida a–h va 1–8 belgilari.
  final bool coords;
  final String? game;
  final String? ai;

  /// Qo'shimcha belgilangan kataklar (masalan, hujum qilayotgan figura).
  final Set<int> highlight;

  bool get isTap => goal.startsWith('tap_');

  String describe() {
    final keys = pieces.keys.toList()..sort();
    final st = stars.toList()..sort();
    return 'chess$size:$goal:${keys.map((k) => '$k${pieces[k]}').join(',')}:${st.join(',')}:${target ?? ''}:${pieceType ?? ''}:${game ?? ''}:${ai ?? ''}';
  }
}

/// Yozish mashqi. [strokes] — yo'naltiruvchi chiziqlar (0..1 koordinatalar),
/// [dots] bo'lsa — faqat raqamlangan nuqtalar ko'rsatiladi (nuqtalarni birlashtirish).
class TraceTask {
  const TraceTask({
    required this.id,
    required this.strokes,
    this.dots = false,
    this.label,
    this.aspect = 1,
    this.tolerance = 0.09,
    this.minCoverage = 0.85,
    this.leftToRight = false,
  });

  final String id;
  final List<List<Point2>> strokes;
  final bool dots;

  /// Chiziq ostida ko'rsatiladigan yozuv (masalan, harf yoki so'z).
  final String? label;

  /// Kenglik / balandlik (so'zlar uchun kengroq maydon).
  final double aspect;

  /// Qanchalik yaqin yurish kerak (maydon balandligiga nisbatan) — yumshoq baholash.
  final double tolerance;

  /// Nazorat nuqtalarining qancha qismi bosib o'tilishi kerak.
  final double minCoverage;

  /// Har bir chiziq chapdan o'ngga yozilishi kerak ("chapdan o'ngga yozish" mashqi).
  final bool leftToRight;

  String describe() => 'trace:$id';
}

/// Oddiy 2D nuqta (Flutter'ga bog'lanmagan, testlarda ham ishlaydi).
class Point2 {
  const Point2(this.x, this.y);

  final double x;
  final double y;

  double distanceTo(Point2 o) {
    final dx = x - o.x, dy = y - o.y;
    return math.sqrt(dx * dx + dy * dy);
  }
}

/// Yozuvni baholash natijasi.
class TraceReport {
  const TraceReport({
    required this.coverage,
    required this.minStrokeCoverage,
    required this.offPath,
    required this.continuity,
    required this.lengthRatio,
    required this.directionOk,
  });

  static const empty = TraceReport(
    coverage: 0,
    minStrokeCoverage: 0,
    offPath: 0,
    continuity: 0,
    lengthRatio: 0,
    directionOk: true,
  );

  /// Nazorat nuqtalarining bosib o'tilgan ulushi (0..1).
  final double coverage;

  /// Eng kam qamralgan chiziqning qamrovi (bitta chiziq tushib qolmasin).
  final double minStrokeCoverage;

  /// Yo'ldan uzoqda chizilgan nuqtalar ulushi (0..1).
  final double offPath;

  /// Chiziq bo'ylab ketma-ket, uzilishsiz yurish ulushi (tartibsiz chizishni ajratadi).
  final double continuity;

  /// Chizilgan uzunlik / namunaviy uzunlik (qalin bo'yab tashlashni ajratadi).
  final double lengthRatio;

  /// "Chapdan o'ngga" talabi bajarildimi.
  final bool directionOk;

  bool passed(TraceTask t) =>
      directionOk &&
      coverage >= t.minCoverage &&
      minStrokeCoverage >= TraceScorer.minStrokeCoverage &&
      continuity >= TraceScorer.minContinuity &&
      offPath <= TraceScorer.maxOffPath &&
      lengthRatio <= TraceScorer.maxLengthRatio;

  @override
  String toString() => 'TraceReport(cov ${coverage.toStringAsFixed(2)}, stroke ${minStrokeCoverage.toStringAsFixed(2)}, '
      'off ${offPath.toStringAsFixed(2)}, cont ${continuity.toStringAsFixed(2)}, len ${lengthRatio.toStringAsFixed(2)}, dir $directionOk)';
}

/// Yozuvni baholash (yumshoq, lekin tartibsiz chizishni o'tkazmaydi):
/// * qamrov — yo'naltiruvchi chiziq bo'ylab nazorat nuqtalari bosib o'tilganmi;
/// * har bir chiziq — hech bir chiziq tushib qolmaganmi;
/// * uzluksizlik — nuqtalar ketma-ket (bir yo'nalishda) o'tilganmi;
/// * yo'ldan chiqish va ortiqcha uzunlik — bo'yab tashlash emasmi.
///
/// Masofalar maydon BALANDLIGI birligida o'lchanadi: x koordinata [TraceTask.aspect]
/// ga ko'paytiriladi, shuning uchun keng maydonda (so'zlar) ham baholash adolatli.
class TraceScorer {
  TraceScorer._();

  static const double maxOffPath = 0.25;
  static const double minStrokeCoverage = 0.7;
  static const double minContinuity = 0.8;
  static const double maxLengthRatio = 1.7;

  static Point2 _scaled(Point2 p, double aspect) => Point2(p.x * aspect, p.y);

  /// Siniq chiziqni ~[spacing] oraliqdagi nuqtalarga aylantiradi (masshtablangan).
  static List<Point2> densify(List<Point2> stroke, double aspect, double spacing) {
    if (stroke.isEmpty) return const [];
    final pts = [for (final p in stroke) _scaled(p, aspect)];
    final result = <Point2>[pts.first];
    for (var i = 1; i < pts.length; i++) {
      final a = pts[i - 1], b = pts[i];
      final n = (a.distanceTo(b) / spacing).ceil();
      for (var k = 1; k <= n; k++) {
        final t = k / n;
        result.add(Point2(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t));
      }
    }
    return result;
  }

  /// Har bir yo'naltiruvchi chiziq uchun nazorat nuqtalari (masshtablangan).
  /// Nuqtalarni birlashtirishda — nuqtalarning o'zi.
  static List<List<Point2>> strokeCheckpoints(TraceTask t, {double spacing = 0.05}) => [
        for (final s in t.strokes)
          if (t.dots) [for (final p in s) _scaled(p, t.aspect)] else densify(s, t.aspect, spacing),
      ];

  static List<Point2> checkpoints(TraceTask t) => [for (final s in strokeCheckpoints(t)) ...s];

  /// Siniq chiziq uzunligi (masshtablangan).
  static double length(List<List<Point2>> strokes, double aspect) {
    var sum = 0.0;
    for (final s in strokes) {
      for (var i = 1; i < s.length; i++) {
        sum += _scaled(s[i - 1], aspect).distanceTo(_scaled(s[i], aspect));
      }
    }
    return sum;
  }

  static double _tol(TraceTask t) => t.dots ? t.tolerance * 1.3 : t.tolerance;

  /// Yo'ldan chiqish chegarasi.
  static double offRadius(TraceTask t) => math.min(_tol(t) * 1.6, _tol(t) + 0.035);

  static bool _near(Point2 p, List<Point2> pts, double r) {
    final r2 = r * r;
    for (final q in pts) {
      final dx = p.x - q.x, dy = p.y - q.y;
      if (dx * dx + dy * dy <= r2) return true;
    }
    return false;
  }

  /// Bitta chizilgan chiziqning yo'ldan chiqqan qismi (xato chiziqni olib tashlash uchun).
  static double strokeOffPath(TraceTask t, List<Point2> stroke) {
    final pts = densify(stroke, t.aspect, t.tolerance / 2);
    if (pts.isEmpty) return 0;
    final path = [for (final s in t.strokes) ...densify(s, t.aspect, 0.025)];
    final r = offRadius(t);
    return pts.where((p) => !_near(p, path, r)).length / pts.length;
  }

  static TraceReport evaluate(TraceTask t, List<List<Point2>> drawn) {
    final strokes = drawn.where((s) => s.isNotEmpty).toList();
    final pts = [for (final s in strokes) ...densify(s, t.aspect, t.tolerance / 2)];
    if (pts.isEmpty) return TraceReport.empty;
    final tol = _tol(t);
    final perStroke = strokeCheckpoints(t);

    var covered = 0, total = 0;
    var minStroke = 1.0;
    for (final cps in perStroke) {
      if (cps.isEmpty) continue;
      final c = cps.where((p) => _near(p, pts, tol)).length;
      covered += c;
      total += cps.length;
      minStroke = math.min(minStroke, c / cps.length);
    }

    final path = [for (final s in t.strokes) ...densify(s, t.aspect, 0.025)];
    final r = offRadius(t);
    final off = pts.where((p) => !_near(p, path, r)).length / pts.length;

    var good = 0, pairs = 0;
    final reversed = pts.reversed.toList();
    for (final cps in perStroke) {
      if (cps.length < 2) continue;
      final f = _continuity(cps, pts, tol);
      final b = _continuity(cps, reversed, tol);
      final best = f.good >= b.good ? f : b;
      good += best.good;
      pairs += best.pairs;
    }

    final guideLength = length(t.strokes, t.aspect);
    return TraceReport(
      coverage: total == 0 ? 0 : covered / total,
      minStrokeCoverage: minStroke,
      offPath: off,
      continuity: pairs == 0 ? 1 : good / pairs,
      lengthRatio: guideLength == 0 ? 0 : length(strokes, t.aspect) / guideLength,
      directionOk: !t.leftToRight || leftToRightOk(strokes),
    );
  }

  /// Ketma-ket qamralgan nazorat nuqtalari juftlaridan nechtasi chizilgan chiziq
  /// bo'ylab to'g'ridan-to'g'ri (orqaga qaytmasdan, aylanib o'tmasdan) bog'langan.
  static ({int good, int pairs}) _continuity(List<Point2> cps, List<Point2> pts, double tol) {
    final cum = List<double>.filled(pts.length, 0);
    for (var k = 1; k < pts.length; k++) {
      cum[k] = cum[k - 1] + pts[k - 1].distanceTo(pts[k]);
    }
    final tol2 = tol * tol;
    int? prev;
    var good = 0, pairs = 0;
    var along = 0.0;
    for (var i = 0; i < cps.length; i++) {
      final c = cps[i];
      if (i > 0) along += cps[i - 1].distanceTo(c);
      final near = <int>[];
      for (var k = 0; k < pts.length; k++) {
        final dx = pts[k].x - c.x, dy = pts[k].y - c.y;
        if (dx * dx + dy * dy <= tol2) near.add(k);
      }
      if (near.isEmpty) continue;
      if (prev == null) {
        prev = near.first;
        along = 0;
        continue;
      }
      pairs++;
      final bound = along * 1.6 + 2 * tol;
      final from = prev;
      final next = near.where((k) => k >= from && cum[k] - cum[from] <= bound).firstOrNull;
      if (next != null) {
        good++;
        prev = next;
      } else {
        prev = near.first;
      }
      along = 0;
    }
    return (good: good, pairs: pairs);
  }

  /// "Chapdan o'ngga" talabi: har bir chiziq chapdan boshlanib o'ngda tugaydi.
  static bool leftToRightOk(List<List<Point2>> drawn) =>
      drawn.every((st) => st.length < 2 || st.last.x - st.first.x > -0.05);

  static bool passed(TraceTask t, List<List<Point2>> drawn) => evaluate(t, drawn).passed(t);
}

/// Bitta mashq (runtime obyekt). Generatorlar yaratadi, pleyer ko'rsatadi.
class Exercise {
  const Exercise({
    required this.topicId,
    required this.subject,
    required this.level,
    required this.kind,
    required this.instruction,
    required this.speech,
    required this.conceptKey,
    this.visual,
    this.options = const [],
    this.correctIndex = 0,
    this.dragToTarget = false,
    this.pairs = const [],
    this.sort,
    this.circuit,
    this.maze,
    this.sudoku,
    this.coding,
    this.assemble,
    this.trace,
    this.chess,
    this.cards,
    this.spot,
    this.jigsaw,
    this.activity,
    this.input,
    this.previewVisual,
    this.previewSeconds = 0,
    this.hint,
    this.explanation,
    this.rewardStars = 1,
    this.meta = const {},
    this.speechLang = 'uz',
    this.speechParts = const [],
    this.instructionKey = '',
  });

  final String topicId;
  final String subject;
  final int level;
  final ExerciseKind kind;

  /// Ko'rsatma (uz/en/ru). Ekranda o'zbekcha ko'rsatiladi.
  final Localized instruction;

  /// Ovozda aytiladigan matn (sonlar so'z bilan), [speechLang] tilida.
  final String speech;

  /// Ovoz va ekrandagi asosiy ko'rsatma tili: `uz`; chet tili darslarida `en` / `ru`.
  final String speechLang;

  /// Bir necha tildagi nutq (3 tilda o'rganamiz): bo'sh bo'lmasa [speech] o'rniga aytiladi.
  final List<SpeechPart> speechParts;

  /// Ko'rsatmalar bankidagi kalit (`where_more`, `count_how_many` ...). Yozib olingan
  /// ovozni tanlash uchun; mashq kaliti ([signature]) ga kirmaydi.
  final String instructionKey;

  /// Ekranda ko'rsatiladigan asosiy ko'rsatma.
  String get prompt => instruction.of(speechLang);

  /// Takrorlash (spaced repetition) uchun tushuncha: `number:7`, `shape:circle`.
  final String conceptKey;

  final ExerciseVisual? visual;
  final List<ExerciseOption> options;
  final int correctIndex;

  /// Kichik yoshda: to'g'ri javobni "?" katakchasiga sudrab qo'yish.
  final bool dragToTarget;
  final List<MatchPair> pairs;
  final SortTask? sort;
  final CircuitTask? circuit;
  final MazeTask? maze;
  final SudokuTask? sudoku;
  final CodingTask? coding;
  final AssembleTask? assemble;
  final TraceTask? trace;
  final ChessTask? chess;
  final CardsTask? cards;
  final SpotTask? spot;
  final JigsawTask? jigsaw;
  final ActivityTask? activity;
  final InputTask? input;

  /// [ExerciseKind.memory]: avval ko'rsatiladigan rasm va vaqti.
  final ExerciseVisual? previewVisual;
  final int previewSeconds;

  /// Qiynalganda beriladigan yordam.
  final String? hint;

  /// To'g'ri javobdan keyingi qisqa izoh (6 yosh: "IZOHNI KO'R").
  final String? explanation;
  final int rewardStars;

  /// Avtomatik tekshirish uchun ma'lumot (masalan: a, b, op, answer).
  final Map<String, Object> meta;

  ExerciseOption? get correctOption =>
      options.isEmpty ? null : options[correctIndex];

  /// Mazmun bo'yicha kalit — bir xil savollarni aniqlash uchun.
  String get signature {
    // Ovoz ham kalitga kiradi: tinglash mashqlarida ekrandagi matn bir xil, so'z esa har xil.
    final b = StringBuffer('$topicId|${kind.name}|${instruction.uz}|$speech|${speechParts.join('+')}|${visual?.describe() ?? ''}');
    // Variantlar tartibi kalitga kirmaydi: bir xil savol aralashtirilgan holda takrorlanmasin.
    for (final o in options.map((o) => o.describe()).toList()..sort()) {
      b.write('|$o');
    }
    for (final p in pairs.map((p) => '${p.left.describe()}=${p.right.describe()}').toList()..sort()) {
      b.write('|$p');
    }
    final s = sort;
    if (s != null) {
      for (var i = 0; i < s.items.length; i++) {
        b.write('|${s.items[i].describe()}>${s.itemBins[i]}');
      }
    }
    if (maze != null) b.write('|${maze!.describe()}');
    if (sudoku != null) b.write('|${sudoku!.describe()}');
    if (coding != null) b.write('|${coding!.describe()}');
    if (circuit != null) b.write('|${circuit!.describe()}');
    if (assemble != null) b.write('|${assemble!.describe()}');
    if (trace != null) b.write('|${trace!.describe()}');
    if (chess != null) b.write('|${chess!.describe()}');
    if (cards != null) b.write('|${cards!.describe()}');
    if (spot != null) b.write('|${spot!.describe()}');
    if (jigsaw != null) b.write('|${jigsaw!.describe()}');
    if (activity != null) b.write('|${activity!.describe()}');
    if (input != null) b.write('|${input!.describe()}');
    if (previewVisual != null) b.write('|pre:${previewVisual!.describe()}');
    return b.toString();
  }

  /// Kontent bazasi formatidagi yozuv (eksport va tekshiruv uchun).
  Map<String, Object?> toContentJson({required String skill, required int ageMin, required int ageMax}) => {
        'id': '$topicId-L$level-${signature.hashCode.toUnsigned(32).toRadixString(16)}',
        'subject': subject,
        'skill': skill,
        'topic': topicId,
        'ageMin': ageMin,
        'ageMax': ageMax,
        'level': level,
        'difficulty': level,
        'instructionUz': instruction.uz,
        'instructionEn': instruction.en,
        'instructionRu': instruction.ru,
        'question': visual?.describe(),
        'options': options.map((o) => o.describe()).toList(),
        'correctAnswer': correctOption?.describe(),
        'hint': hint,
        'explanation': explanation,
        'rewardStars': rewardStars,
        'tags': [kind.name, conceptKey],
      };
}
