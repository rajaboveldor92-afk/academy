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
    this.maze,
    this.sudoku,
    this.coding,
    this.previewVisual,
    this.previewSeconds = 0,
    this.hint,
    this.explanation,
    this.rewardStars = 1,
    this.meta = const {},
  });

  final String topicId;
  final String subject;
  final int level;
  final ExerciseKind kind;

  /// Ko'rsatma (uz/en/ru). Ekranda o'zbekcha ko'rsatiladi.
  final Localized instruction;

  /// Ovozda aytiladigan o'zbekcha matn (sonlar so'z bilan).
  final String speech;

  /// Takrorlash (spaced repetition) uchun tushuncha: `number:7`, `shape:circle`.
  final String conceptKey;

  final ExerciseVisual? visual;
  final List<ExerciseOption> options;
  final int correctIndex;

  /// Kichik yoshda: to'g'ri javobni "?" katakchasiga sudrab qo'yish.
  final bool dragToTarget;
  final List<MatchPair> pairs;
  final SortTask? sort;
  final MazeTask? maze;
  final SudokuTask? sudoku;
  final CodingTask? coding;

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
    final b = StringBuffer('$topicId|${kind.name}|${instruction.uz}|${visual?.describe() ?? ''}');
    for (final o in options) {
      b.write('|${o.describe()}');
    }
    for (final p in pairs) {
      b.write('|${p.left.describe()}=${p.right.describe()}');
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
