import 'dart:math' as math;

import '../../models/exercise.dart';
import '../../models/visual.dart';
import '../generator_base.dart';
import 'school_base.dart';

/// Maktab mantiqi (1–8-sinf): murakkab ketma-ketliklar, rostgo'y va yolg'onchilar, sehrli kvadrat,
/// rasmli tenglamalar, "kim nima?" jadvali, o'ylangan son, kombinatorika, yosh masalalari,
/// kalendar va vaqt, Dirixle prinsipi.
class LogicSchool {
  LogicSchool._();

  static Map<String, ExerciseGenerator> get generators => {
        'seq': seq,
        'knights': knights,
        'magic': magic,
        'emoji_eq': emojiEq,
        'table_logic': tableLogic,
        'number_think': numberThink,
        'combin': combin,
        'ages': ages,
        'calendar': calendar,
        'pigeonhole': pigeonhole,
      };

  static const String minus = '−';

  static const List<String> names = [
    'Ali', 'Vali', 'Zarina', 'Malika', 'Bobur', 'Sardor', 'Nodira', 'Jasur', 'Laylo', 'Temur', 'Dilnoza', 'Aziz',
  ];

  static int _fact(int n) => n <= 1 ? 1 : n * _fact(n - 1);

  static int choose(int n, int k) => _fact(n) ~/ (_fact(k) * _fact(n - k));

  // ------------------------------------------------------------ ketma-ketliklar

  static const List<int> _primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61];

  /// Qonuniyat bo'yicha ketma-ketlik va uning izohi.
  static (List<int>, String) sequenceOf(GenContext g, String kind) {
    switch (kind) {
      case 'arith_down':
        final d = g.range(2, 9), a = g.range(5 * d + 5, 5 * d + 60);
        return ([for (var i = 0; i < 6; i++) a - d * i], 'Har bir son oldingisidan $d ta kam.');
      case 'geom':
        final q = g.range(2, 3), a = g.range(1, q == 2 ? 6 : 4);
        return ([for (var i = 0; i < 5; i++) a * math.pow(q, i).toInt()], 'Har bir son oldingisidan $q marta katta.');
      case 'alt':
        final up = g.range(3, 9), down = g.range(1, up - 1), a = g.range(1, 20);
        final list = [a];
        for (var i = 1; i < 7; i++) {
          list.add(list.last + (i.isOdd ? up : -down));
        }
        return (list, 'Navbat bilan: +$up, $minus$down, +$up, $minus$down …');
      case 'alt_op':
        final k = g.range(1, 5), a = g.range(1, 4);
        final list = [a];
        for (var i = 1; i < 6; i++) {
          list.add(i.isOdd ? list.last * 2 : list.last + k);
        }
        return (list, 'Navbat bilan: × 2, + $k, × 2, + $k …');
      case 'diff':
        final a = g.range(1, 15), d0 = g.range(1, 3);
        final list = [a];
        for (var i = 0; i < 5; i++) {
          list.add(list.last + d0 + i);
        }
        return (list, 'Farqlar har safar 1 ga ortadi: +$d0, +${d0 + 1}, +${d0 + 2} …');
      case 'squares':
        final s = g.range(1, 8);
        return ([for (var n = s; n < s + 5; n++) n * n], 'Ketma-ket sonlarning kvadratlari: $s × $s, ${s + 1} × ${s + 1} …');
      case 'fib':
        final a = g.range(1, 5), b = g.range(a, a + 4);
        final list = [a, b];
        while (list.length < 7) {
          list.add(list[list.length - 1] + list[list.length - 2]);
        }
        return (list, 'Har bir son oldingi ikki sonning yig‘indisiga teng.');
      case 'two':
        final a = g.range(1, 10), d1 = g.range(2, 5), b = g.range(30, 50), d2 = g.range(2, 5);
        return ([for (var i = 0; i < 8; i++) i.isEven ? a + d1 * (i ~/ 2) : b - d2 * (i ~/ 2)],
            'Ikki qator aralashgan: toq o‘rinlarda +$d1, juft o‘rinlarda $minus$d2.');
      case 'cubes':
        final s = g.range(1, 5);
        return ([for (var n = s; n < s + 4; n++) n * n * n], 'Ketma-ket sonlarning kublari: $s × $s × $s …');
      case 'tri':
        final s = g.range(1, 5);
        return ([for (var n = s; n < s + 6; n++) n * (n + 1) ~/ 2], 'Farqlar har safar 1 ga ortadi (uchburchak sonlar).');
      case 'primes':
        final s = g.range(0, 10);
        return (_primes.sublist(s, s + 6), 'Tub sonlar: faqat 1 ga va o‘ziga bo‘linadi.');
      case 'mult_inc':
        final a = g.range(1, 3);
        final list = [a];
        for (var i = 2; i <= 5; i++) {
          list.add(list.last * i);
        }
        return (list, 'Navbat bilan × 2, × 3, × 4, × 5.');
      default:
        final d = g.range(2, 9), a = g.range(1, 30);
        return ([for (var i = 0; i < 6; i++) a + d * i], 'Har bir son oldingisidan $d ta ko‘p.');
    }
  }

  static Exercise seq(GenContext g) {
    final kinds = g.pl('kinds');
    final kind = g.pick(kinds.isEmpty ? const ['arith'] : kinds);
    final (list, rule) = sequenceOf(g, kind);
    final index = g.pb('inside') && g.chance(0.5) ? g.range(1, list.length - 2) : list.length - 1;
    final shown = [for (var i = 0; i < list.length; i++) i == index ? '?' : '${list[i]}'].join(', ');
    return g.numberAnswer(
      question: 'Qonuniyatni toping: $shown',
      answer: list[index],
      concept: 'logic:seq:$kind:${list.join(',')}:$index',
      input: g.useInput(),
      visual: TextVisual(shown, scale: 0.7),
      hint: 'Qo‘shni sonlar orasidagi farq yoki nisbatga qarang.',
      explanation: '$rule ? = ${list[index]}',
      meta: {'seq': list, 'index': index, 'kind': kind},
    );
  }

  // ------------------------------------------------------------ rostgo'y va yolg'onchilar

  static String _whoLabel(List<String> people, List<bool> knights) {
    final yes = [for (var i = 0; i < people.length; i++) if (knights[i]) people[i]];
    if (yes.isEmpty) return 'Hech biri';
    if (yes.length == people.length) return people.length == 2 ? 'Ikkalasi ham' : 'Uchalasi ham';
    if (yes.length == 1) return 'Faqat ${yes.first}';
    return '${yes[0]} va ${yes[1]}';
  }

  /// Rostgo'y har doim rost, yolg'onchi har doim yolg'on gapiradi: [statements] ga mos barcha taqsimotlar.
  static List<List<bool>> solveKnights(int n, List<(int, bool Function(List<bool>))> statements) {
    final out = <List<bool>>[];
    for (var mask = 0; mask < (1 << n); mask++) {
      final k = [for (var i = 0; i < n; i++) mask & (1 << i) != 0];
      if (statements.every((s) => s.$2(k) == k[s.$1])) out.add(k);
    }
    return out;
  }

  static Exercise knights(GenContext g) {
    final n = g.p('people', 2);
    for (var attempt = 0; attempt < 300; attempt++) {
      final people = g.sample(names, n);
      final lines = <String>[];
      final statements = <(int, bool Function(List<bool>))>[];
      for (var s = 0; s < n; s++) {
        final o = (s + 1 + g.rng.nextInt(n - 1)) % n;
        final t = [for (var i = 0; i < n; i++) if (i != s && i != o) i];
        final options = <(String, bool Function(List<bool>))>[
          ('${people[o]} — yolg‘onchi.', (k) => !k[o]),
          ('${people[o]} — rostgo‘y.', (k) => k[o]),
          (n == 2 ? 'Ikkalamiz ham yolg‘onchimiz.' : 'Men ham, ${people[o]} ham yolg‘onchimiz.', (k) => !k[s] && !k[o]),
          (n == 2 ? 'Ikkalamiz ham rostgo‘ymiz.' : 'Men ham, ${people[o]} ham rostgo‘ymiz.', (k) => k[s] && k[o]),
          ('${people[o]} ham xuddi menday.', (k) => k[s] == k[o]),
          ('Oramizda kamida bitta yolg‘onchi bor.', (k) => k.any((x) => !x)),
          ('Oramizda aynan bitta rostgo‘y bor.', (k) => k.where((x) => x).length == 1),
          if (t.isNotEmpty) ('${people[o]} va ${people[t.first]} — bir xil.', (k) => k[o] == k[t.first]),
          if (n == 3) ('Hammamiz yolg‘onchimiz.', (k) => k.every((x) => !x)),
        ];
        final pick = g.pick(options);
        lines.add('${people[s]}: «${pick.$1}»');
        statements.add((s, pick.$2));
      }
      final solutions = solveKnights(n, statements);
      if (solutions.length != 1) continue;
      final truth = solutions.first;
      final answer = _whoLabel(people, truth);
      final wrong = <String>{};
      for (var mask = 0; mask < (1 << n); mask++) {
        final label = _whoLabel(people, [for (var i = 0; i < n; i++) mask & (1 << i) != 0]);
        if (label != answer) wrong.add(label);
      }
      return g.textChoice(
        question: 'Rostgo‘y har doim rost, yolg‘onchi har doim yolg‘on gapiradi. Kim rostgo‘y?',
        answer: answer,
        wrong: g.sample(wrong.toList(), math.min(3, wrong.length)),
        concept: 'logic:knights:${lines.join('|')}',
        visual: ReadingVisual(lines.join('\n')),
        hint: 'Birinchi odamni rostgo‘y deb faraz qiling va qolganlarini tekshiring. Qarama-qarshilik chiqsa — u yolg‘onchi.',
        explanation: [for (var i = 0; i < n; i++) '${people[i]} — ${truth[i] ? 'rostgo‘y' : 'yolg‘onchi'}'].join(', '),
        meta: {'truth': truth.map((x) => x ? 1 : 0).join(), 'people': people.join(','), 'solutions': solutions.length},
      );
    }
    throw StateError('knights: jumboq topilmadi');
  }

  // ------------------------------------------------------------ sehrli kvadrat

  static const List<int> _loShu = [2, 7, 6, 9, 5, 1, 4, 3, 8];

  static List<int> _transform(List<int> sq, int sym) {
    int at(int r, int c) => sq[r * 3 + c];
    return [
      for (var r = 0; r < 3; r++)
        for (var c = 0; c < 3; c++)
          switch (sym) {
            1 => at(c, 2 - r),
            2 => at(2 - r, 2 - c),
            3 => at(2 - c, r),
            4 => at(r, 2 - c),
            5 => at(2 - r, c),
            6 => at(c, r),
            7 => at(2 - c, 2 - r),
            _ => at(r, c),
          },
    ];
  }

  static bool isMagic(List<int> sq) {
    final s = sq[0] + sq[1] + sq[2];
    final lines = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6],
    ];
    return lines.every((l) => sq[l[0]] + sq[l[1]] + sq[l[2]] == s);
  }

  static Exercise magic(GenContext g) {
    final a = g.range(1, g.p('scale', 1));
    final b = g.range(0, g.p('shift', 10));
    final sq = [for (final v in _transform(_loShu, g.range(0, 7))) a * v + b];
    final sum = 15 * a + 3 * b;
    final blanks = g.p('blanks', 1);
    final missing = g.range(0, 8);
    final hidden = {missing};
    if (blanks > 1) {
      // Ikkinchi bo'sh katak — o'sha qatorda (ustun orqali topiladi).
      final row = missing ~/ 3;
      hidden.add(row * 3 + g.pick<int>([for (var c = 0; c < 3; c++) if (row * 3 + c != missing) c]));
    }
    final showSum = g.pb('sum');
    return g.numberAnswer(
      question: showSum
          ? 'Sehrli kvadratda har bir qator, ustun va diagonal yig‘indisi $sum ga teng. ? o‘rniga qaysi son turadi?'
          : 'Sehrli kvadratda har bir qator, ustun va diagonal yig‘indisi bir xil. ? o‘rniga qaysi son turadi?',
      answer: sq[missing],
      concept: 'logic:magic:${sq.join(',')}:$missing:${hidden.join(',')}',
      input: g.useInput(),
      visual: GridVisual(rows: 3, cols: 3, cells: [
        for (var i = 0; i < 9; i++)
          i == missing ? null : (hidden.contains(i) ? const <SceneItem>[] : [Layouts.text('${sq[i]}', size: 0.5)]),
      ]),
      hint: showSum ? '? turgan qator yoki ustundagi ikki sonni $sum dan ayiring.' : 'Avval to‘liq qator yig‘indisini toping.',
      explanation: 'Yig‘indi $sum: ? = ${sq[missing]}',
      meta: {'square': sq, 'missing': missing, 'sum': sum},
    );
  }

  // ------------------------------------------------------------ rasmli tenglamalar

  static const List<String> _eqEmoji = ['🍎', '🍌', '🍒', '🍇', '🍓', '🍋', '⭐', '⚽', '🎈', '🌸'];

  static Exercise emojiEq(GenContext g) {
    final level = g.p('depth', 1);
    final e = g.sample(_eqEmoji, 3);
    final v1 = g.range(2, 9), v2 = g.range(1, 12), v3 = g.range(v2 + 1, v2 + 10);
    final lines = <String>[];
    final int answer;
    if (level <= 1) {
      lines.add('${e[0]} + ${e[0]} = ${2 * v1}');
      lines.add('${e[0]} + ${e[1]} = ${v1 + v2}');
      if (g.chance(0.5)) {
        lines.add('${e[1]} = ?');
        answer = v2;
      } else {
        lines.add('${e[1]} + ${e[1]} = ?');
        answer = 2 * v2;
      }
    } else if (level == 2) {
      lines.add('${e[0]} + ${e[0]} + ${e[0]} = ${3 * v1}');
      lines.add('${e[0]} + ${e[1]} = ${v1 + v2}');
      lines.add('${e[2]} $minus ${e[1]} = ${v3 - v2}');
      lines.add('${e[0]} + ${e[1]} + ${e[2]} = ?');
      answer = v1 + v2 + v3;
    } else {
      lines.add('${e[0]} + ${e[0]} = ${2 * v1}');
      lines.add('${e[0]} × ${e[1]} = ${v1 * v2}');
      lines.add('${e[2]} $minus ${e[1]} = ${v3 - v2}');
      lines.add('${e[2]} + ${e[1]} × ${e[0]} = ?');
      answer = v3 + v2 * v1;
    }
    return g.numberAnswer(
      question: 'Bir xil rasm — bir xil son. Oxirgi qatorda ? o‘rniga qaysi son turadi?',
      answer: answer,
      concept: 'logic:emoji_eq:${lines.join('|')}',
      input: g.useInput(),
      visual: ReadingVisual(lines.join('\n')),
      hint: 'Avval bitta rasm qatnashgan qatordan boshlang.',
      explanation: '${e[0]} = $v1, ${e[1]} = $v2${level >= 2 ? ', ${e[2]} = $v3' : ''} → $answer',
      meta: {'lines': lines, 'values': '${e[0]}=$v1,${e[1]}=$v2,${e[2]}=$v3'},
    );
  }

  // ------------------------------------------------------------ "kim nima?" jadvali

  static const Map<String, List<(String, String)>> _tableItems = {
    'pets': [('mushuk', 'mushugi'), ('it', 'iti'), ('quyon', 'quyoni'), ('to‘tiqush', 'to‘tiqushi'), ('baliq', 'balig‘i')],
    'sports': [('futbol', 'futbolga'), ('shaxmat', 'shaxmatga'), ('suzish', 'suzishga'), ('kurash', 'kurashga'), ('tennis', 'tennisga')],
    'colors': [('qizil', 'qizil'), ('ko‘k', 'ko‘k'), ('yashil', 'yashil'), ('sariq', 'sariq'), ('oq', 'oq')],
  };

  static String _clue(String cat, String person, (String, String) item, bool positive) => switch (cat) {
        'pets' => '${person}ning ${item.$2} ${positive ? 'bor' : 'yo‘q'}.',
        'sports' => '$person ${item.$2} ${positive ? 'qatnashadi' : 'qatnashmaydi'}.',
        _ => '${person}ning ko‘ylagi ${item.$2}${positive ? '' : ' emas'}.',
      };

  static String _tableQuestion(String cat, (String, String) item) => switch (cat) {
        'pets' => 'Kimning ${item.$2} bor?',
        'sports' => 'Kim ${item.$2} qatnashadi?',
        _ => 'Kimning ko‘ylagi ${item.$2}?',
      };

  static String _tableIntro(String cat, List<(String, String)> items) {
    final list = andList([for (final i in items) i.$1]);
    return switch (cat) {
      'pets' => 'Har birida bittadan uy hayvoni bor: $list.',
      'sports' => 'Har biri bitta to‘garakka qatnashadi: $list.',
      _ => 'Har birining ko‘ylagi har xil rangda: $list.',
    };
  }

  /// "a, b va c".
  static String andList(List<String> items) =>
      items.length <= 1 ? items.join() : '${items.sublist(0, items.length - 1).join(', ')} va ${items.last}';

  static List<List<int>> _perms(int n) {
    if (n == 1) {
      return [
        [0],
      ];
    }
    final out = <List<int>>[];
    for (final p in _perms(n - 1)) {
      for (var i = 0; i <= p.length; i++) {
        out.add([...p.sublist(0, i), n - 1, ...p.sublist(i)]);
      }
    }
    return out;
  }

  /// Ko'rsatmalarga ([clues]: odam, narsa, bor/yo'q) mos keladigan taqsimotlar.
  static List<List<int>> solveTable(int n, List<(int, int, bool)> clues) =>
      _perms(n).where((p) => clues.every((c) => (p[c.$1] == c.$2) == c.$3)).toList();

  static Exercise tableLogic(GenContext g) {
    final n = g.p('people', 3);
    final cat = g.pick(g.pl('cats').isEmpty ? _tableItems.keys.toList() : g.pl('cats'));
    final people = g.sample(names, n);
    final items = g.sample(_tableItems[cat]!, n);
    final perm = List<int>.generate(n, (i) => i)..shuffle(g.rng);
    final candidates = <(int, int, bool)>[
      for (var p = 0; p < n; p++)
        for (var i = 0; i < n; i++)
          if (perm[p] != i) (p, i, false),
    ]..shuffle(g.rng);
    if (g.pb('positive') && g.chance(0.5)) candidates.insert(0, (g.range(0, n - 1), -1, true));
    final clues = <(int, int, bool)>[];
    for (final c in candidates) {
      final clue = c.$2 < 0 ? (c.$1, perm[c.$1], true) : c;
      clues.add(clue);
      if (solveTable(n, clues).length == 1) break;
    }
    // Ortiqcha ko'rsatmalarni olib tashlaymiz (javob yagona qolsa).
    for (var i = clues.length - 1; i >= 0; i--) {
      final without = [...clues]..removeAt(i);
      if (solveTable(n, without).length == 1) clues.removeAt(i);
    }
    final stated = {for (final c in clues) if (c.$3) c.$2};
    final askable = [for (var i = 0; i < n; i++) if (!stated.contains(i)) i];
    final item = g.pick(askable.isEmpty ? List<int>.generate(n, (i) => i) : askable);
    final owner = perm.indexOf(item);
    final lines = [for (final c in clues) '• ${_clue(cat, people[c.$1], items[c.$2], c.$3)}'];
    return g.textChoice(
      question: '${andList(people)} — do‘stlar. ${_tableIntro(cat, items)} ${_tableQuestion(cat, items[item])}',
      answer: people[owner],
      wrong: [for (var p = 0; p < n; p++) if (p != owner) people[p]],
      concept: 'logic:table:$cat:${people.join(',')}:${perm.join(',')}:$item',
      options: n,
      visual: ReadingVisual(lines.join('\n')),
      hint: 'Jadval chizing: qatorlar — odamlar, ustunlar — ${cat == 'colors' ? 'ranglar' : 'narsalar'}. “Yo‘q” kataklarni belgilang.',
      explanation: [for (var p = 0; p < n; p++) '${people[p]} — ${items[perm[p]].$1}'].join(', '),
      meta: {
        'answer': people[owner],
        'perm': perm.join(','),
        'clues': [for (final c in clues) '${c.$1}:${c.$2}:${c.$3 ? 1 : 0}'].join(';'),
        'item': item,
      },
    );
  }

  // ------------------------------------------------------------ o'ylangan son

  static Exercise numberThink(GenContext g) {
    final count = g.p('ops', 2);
    for (var attempt = 0; attempt < 200; attempt++) {
      final x = g.range(2, g.p('max', 20));
      var v = x;
      final ops = <String>[];
      final phrases = <String>[];
      var ok = true;
      for (var i = 0; i < count; i++) {
        final op = g.pick(const ['+', '-', '*', '/']);
        final k = op == '*' || op == '/' ? g.range(2, 5) : g.range(2, 15);
        final first = i == 0;
        switch (op) {
          case '+':
            v += k;
            phrases.add(first ? 'unga $k ni qo‘shdim' : 'natijaga $k ni qo‘shdim');
          case '-':
            if (v - k < 1) {
              ok = false;
              break;
            }
            v -= k;
            phrases.add(first ? 'undan $k ni ayirdim' : 'natijadan $k ni ayirdim');
          case '*':
            v *= k;
            phrases.add(first ? 'uni $k ga ko‘paytirdim' : 'natijani $k ga ko‘paytirdim');
          case '/':
            if (v % k != 0) {
              ok = false;
              break;
            }
            v ~/= k;
            phrases.add(first ? 'uni $k ga bo‘ldim' : 'natijani $k ga bo‘ldim');
        }
        if (!ok) break;
        ops.add('$op$k');
      }
      if (!ok || v > 500) continue;
      final text = 'Men bir son o‘yladim, ${phrases.join(', keyin ')} va $v hosil bo‘ldi. Qaysi sonni o‘yladim?';
      final back = [for (final o in ops.reversed) _inverse(o)].join(', ');
      return g.numberAnswer(
        question: text,
        answer: x,
        concept: 'logic:think:${ops.join()}:$v',
        input: g.useInput(),
        hint: 'Oxiridan boshlang va teskari amallarni bajaring: qo‘shish ↔ ayirish, ko‘paytirish ↔ bo‘lish.',
        explanation: '$v dan boshlab: $back → $x',
        meta: {'ops': ops.join(','), 'result': v},
      );
    }
    throw StateError('number_think');
  }

  static String _inverse(String op) {
    final k = op.substring(1);
    return switch (op[0]) {
      '+' => '$minus $k',
      '-' => '+ $k',
      '*' => ': $k',
      _ => '× $k',
    };
  }

  // ------------------------------------------------------------ kombinatorika

  static Exercise combin(GenContext g) {
    final kinds = g.pl('kinds');
    final kind = g.pick(kinds.isEmpty ? const ['outfit', 'handshake'] : kinds);
    final who = g.pick(names);
    switch (kind) {
      case 'chance':
        return _chance(g);
      case 'outfit':
        final a = g.range(2, 5), b = g.range(2, 5);
        final three = g.pb('three') && g.chance(0.5);
        final c = three ? g.range(2, 3) : 1;
        return _num(g, kind,
            three
                ? '${who}ning $a ta ko‘ylagi, $b ta shimi va $c ta do‘ppisi bor. U necha xil usulda kiyinishi mumkin?'
                : '${who}ning $a ta ko‘ylagi va $b ta shimi bor. U necha xil usulda kiyinishi mumkin?',
            a * b * c,
            'Har bir ko‘ylakni har bir shim bilan kiyish mumkin — ko‘paytiring.',
            three ? '$a × $b × $c = ${a * b * c}' : '$a × $b = ${a * b}',
            {'a': a, 'b': b, 'c': c});
      case 'handshake':
        final n = g.range(3, 12);
        return _num(g, kind,
            'Uchrashuvga $n kishi keldi. Har biri qolganlarning har biri bilan bir martadan qo‘l berib ko‘rishdi. Jami nechta qo‘l berishish bo‘ldi?',
            n * (n - 1) ~/ 2,
            'Har kim ${n - 1} kishi bilan ko‘rishadi, lekin har bir ko‘rishish ikki marta sanalmasin.',
            '$n × ${n - 1} : 2 = ${n * (n - 1) ~/ 2}',
            {'n': n});
      case 'tournament':
        final n = g.range(4, 10);
        final twice = g.pb('twice') && g.chance(0.5);
        return _num(g, kind,
            'Turnirda $n ta jamoa qatnashdi. Har bir jamoa qolganlarining har biri bilan ${twice ? 'ikki martadan — uyda va mehmonda —' : 'bir martadan'} o‘ynadi. Jami nechta o‘yin bo‘ldi?',
            twice ? n * (n - 1) : n * (n - 1) ~/ 2,
            'Har bir jamoa ${n - 1} ta raqib bilan o‘ynaydi.',
            twice ? '$n × ${n - 1} = ${n * (n - 1)}' : '$n × ${n - 1} : 2 = ${n * (n - 1) ~/ 2}',
            {'n': n, 'twice': twice ? 1 : 0});
      case 'digits':
        final k = g.range(3, 5);
        final digits = g.sample(const [1, 2, 3, 4, 5, 6, 7, 8, 9], k)..sort();
        final repeat = g.pb('repeat') && g.chance(0.5);
        return _num(g, kind,
            '${digits.join(', ')} raqamlaridan foydalanib, raqamlari ${repeat ? 'takrorlanishi mumkin bo‘lgan' : 'takrorlanmaydigan'} nechta ikki xonali son yozish mumkin?',
            repeat ? k * k : k * (k - 1),
            'O‘nliklar xonasiga $k xil raqam, birliklar xonasiga — ${repeat ? k : k - 1} xil.',
            repeat ? '$k × $k = ${k * k}' : '$k × ${k - 1} = ${k * (k - 1)}',
            {'k': k, 'repeat': repeat ? 1 : 0});
      case 'queue':
        final k = g.range(3, 5);
        return _num(g, kind, '$k nafar do‘st bir qatorga necha xil usulda turishi mumkin?', _fact(k),
            'Birinchi o‘ringa $k kishidan biri, ikkinchisiga qolgan ${k - 1} kishidan biri …',
            '${[for (var i = k; i >= 1; i--) i].join(' × ')} = ${_fact(k)}', {'k': k});
      case 'routes':
        final a = g.range(2, 4), b = g.range(2, 5);
        final direct = g.pb('direct') && g.chance(0.5);
        final c = direct ? g.range(1, 3) : 0;
        return _num(g, kind,
            'A qishloqdan B qishloqqa $a ta, B dan C ga $b ta yo‘l bor.${direct ? ' Bundan tashqari, A dan C ga to‘g‘ridan-to‘g‘ri $c ta yo‘l bor.' : ''} A dan C ga necha xil yo‘l bilan borish mumkin?',
            a * b + c,
            'B orqali: har bir birinchi yo‘lni har bir ikkinchi yo‘l bilan juftlang.',
            direct ? '$a × $b + $c = ${a * b + c}' : '$a × $b = ${a * b}',
            {'a': a, 'b': b, 'c': c});
      case 'choose2':
        final n = g.range(4, 10);
        return _num(g, kind, 'Sinfdagi $n o‘quvchidan navbatchilik uchun 2 kishini necha xil usulda tanlash mumkin?',
            n * (n - 1) ~/ 2, 'Juftlikda tartib muhim emas: $n × ${n - 1} ni 2 ga bo‘ling.', '$n × ${n - 1} : 2 = ${n * (n - 1) ~/ 2}', {'n': n});
      case 'paths':
        final w = g.range(2, 4), h = g.range(1, 3);
        return _num(g, kind,
            'Chumoli eni $w, bo‘yi $h katakli to‘rning pastki chap burchagidan yuqori o‘ng burchagiga faqat o‘ngga va yuqoriga yurib boradi. Nechta turli yo‘l bor?',
            choose(w + h, h),
            'Har bir tugunga kelish yo‘llari = chapdagi + pastdagi tugun yo‘llari.',
            'Yo‘llar soni = ${choose(w + h, h)}', {'w': w, 'h': h});
      default:
        throw StateError('combin: $kind');
    }
  }

  static Exercise _num(GenContext g, String kind, String q, int answer, String hint, String expl, Map<String, Object> params) =>
      g.numberAnswer(
        question: q,
        answer: answer,
        concept: 'logic:$kind:$q',
        input: g.useInput(),
        hint: hint,
        explanation: expl,
        meta: {...params, 'kind': kind},
      );

  /// Ehtimollik: javob — qisqartirilgan kasr.
  static Exercise _chance(GenContext g) {
    final type = g.range(0, 3);
    final int fav, total;
    final String q;
    switch (type) {
      case 0:
        fav = 3;
        total = 6;
        q = 'O‘yin kubigi tashlandi. Juft son tushish ehtimoli qancha?';
      case 1:
        final k = g.range(1, 4);
        fav = 6 - k;
        total = 6;
        q = 'O‘yin kubigi tashlandi. $k dan katta son tushish ehtimoli qancha?';
      case 2:
        final r = g.range(1, 6), b = g.range(1, 6);
        fav = r;
        total = r + b;
        q = 'Xaltada $r ta qizil va $b ta ko‘k shar bor. Qarab turmay bitta shar olindi. Uning qizil bo‘lish ehtimoli qancha?';
      default:
        final n = g.range(5, 10), k = g.range(1, n - 1);
        fav = k;
        total = n;
        q = '$n ta chiptadan $k tasi yutuqli. Bitta chipta olindi. Uning yutuqli bo‘lish ehtimoli qancha?';
    }
    final d = gcd(fav, total);
    final answer = '${fav ~/ d}/${total ~/ d}';
    return g.textAnswer(
      question: q,
      answer: answer,
      accept: ['$fav/$total'],
      keys: 'fraction',
      concept: 'logic:chance:$q',
      hint: 'Ehtimollik = qulay holatlar soni : barcha holatlar soni.',
      explanation: '$fav/$total = $answer',
      meta: {'fav': fav, 'total': total, 'kind': 'chance'},
    );
  }

  // ------------------------------------------------------------ yosh masalalari

  static Exercise ages(GenContext g) {
    final kinds = g.pl('kinds');
    final kind = g.pick(kinds.isEmpty ? const ['simple', 'later'] : kinds);
    final who = g.pick(names);
    switch (kind) {
      case 'simple':
        final a = g.range(3, 9), back = g.range(2, 5), fwd = g.range(2, 6);
        return _num(g, kind, '$who $back yil oldin $a yoshda edi. $fwd yildan keyin u necha yoshda bo‘ladi?', a + back + fwd,
            'Avval hozirgi yoshini toping.', 'Hozir ${a + back} yosh; ${a + back} + $fwd = ${a + back + fwd}',
            {'a': a, 'back': back, 'fwd': fwd});
      case 'later':
        final small = g.range(3, 10), diff = g.range(2, 8), target = g.range(small + 3, 25);
        return _num(g, kind,
            '$who $small yoshda, akasi ${small + diff} yoshda. $who $target yoshga to‘lganda akasi necha yoshda bo‘ladi?',
            target + diff, 'Yoshlar farqi hech qachon o‘zgarmaydi.', 'Farq $diff yosh: $target + $diff = ${target + diff}',
            {'small': small, 'diff': diff, 'target': target});
      case 'sum_diff':
        final y = g.range(3, 15), d = g.range(2, 10);
        final askOld = g.chance(0.5);
        return _num(g, kind,
            'Aka va ukaning yoshlari yig‘indisi ${2 * y + d} ga teng. Aka ukadan $d yosh katta. ${askOld ? 'Aka' : 'Uka'} necha yoshda?',
            askOld ? y + d : y, 'Yig‘indidan farqni ayirib, 2 ga bo‘ling — ukaning yoshi chiqadi.',
            '(${2 * y + d} $minus $d) : 2 = $y; aka ${y + d} yoshda', {'y': y, 'd': d, 'old': askOld ? 1 : 0});
      case 'times_future':
        for (;;) {
          final b = g.range(2, 12), x = g.range(1, 12), k = g.range(2, 4);
          final a = k * (b + x) - x;
          if (a - b < 20 || a - b > 40) continue;
          return _num(g, kind, 'Ota $a yoshda, o‘g‘li $b yoshda. Necha yildan keyin ota o‘g‘lidan $k marta katta bo‘ladi?', x,
              'Farq ${a - b} yosh o‘zgarmaydi: o‘shanda o‘g‘li ${a - b} : ${k - 1} yoshda bo‘ladi.',
              'O‘g‘li ${(a - b) ~/ (k - 1)} yoshda bo‘ladi: ${(a - b) ~/ (k - 1)} $minus $b = $x yil', {'a': a, 'b': b, 'k': k});
        }
      case 'times_past':
        for (;;) {
          final b = g.range(8, 16), x = g.range(1, b - 2), k = g.range(3, 6);
          final a = k * (b - x) + x;
          if (a - b < 20 || a - b > 40) continue;
          return _num(g, kind, 'Ota $a yoshda, o‘g‘li $b yoshda. Necha yil oldin ota o‘g‘lidan $k marta katta edi?', x,
              'Farq ${a - b} yosh o‘zgarmaydi: o‘shanda o‘g‘li ${a - b} : ${k - 1} yoshda bo‘lgan.',
              'O‘g‘li ${(a - b) ~/ (k - 1)} yoshda edi: $b $minus ${(a - b) ~/ (k - 1)} = $x yil', {'a': a, 'b': b, 'k': k});
        }
      default:
        throw StateError('ages: $kind');
    }
  }

  // ------------------------------------------------------------ kalendar va vaqt

  static const List<String> weekdays = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba'];

  static String hm(int minutes) => '${minutes ~/ 60}:${(minutes % 60).toString().padLeft(2, '0')}';

  static Exercise calendar(GenContext g) {
    final kinds = g.pl('kinds');
    final kind = g.pick(kinds.isEmpty ? const ['weekday', 'time_add'] : kinds);
    switch (kind) {
      case 'weekday':
      case 'weekday_back':
        final d = g.range(0, 6), n = g.range(2, g.p('days', 30));
        final back = kind == 'weekday_back';
        final r = ((d + (back ? -n : n)) % 7 + 7) % 7;
        return g.textChoice(
          question: 'Bugun ${weekdays[d]}. $n kun${back ? ' oldin' : 'dan keyin'} qaysi kun ${back ? 'edi' : 'bo‘ladi'}?',
          answer: weekdays[r],
          wrong: [for (var i = 0; i < 7; i++) if (i != r) weekdays[i]],
          concept: 'logic:weekday:$d:$n:$back',
          hint: 'Har 7 kunda hafta kuni takrorlanadi: $n ni 7 ga bo‘lib, qoldiqqa qarang.',
          explanation: '$n = ${n ~/ 7} × 7 + ${n % 7}: ${n % 7} kun ${back ? 'orqaga' : 'oldinga'} → ${weekdays[r]}',
          meta: {'answer': weekdays[r], 'd': d, 'n': back ? -n : n, 'kind': kind},
        );
      case 'yesterday':
        final d = g.range(0, 6);
        final r = (d + 3) % 7;
        return g.textChoice(
          question: 'Kechadan oldingi kun ${weekdays[d]} edi. Ertaga qaysi kun bo‘ladi?',
          answer: weekdays[r],
          wrong: [for (var i = 0; i < 7; i++) if (i != r) weekdays[i]],
          concept: 'logic:yesterday:$d',
          hint: 'Kechadan oldingi kun → kecha → bugun → ertaga.',
          explanation: '${weekdays[d]} → ${weekdays[(d + 1) % 7]} → ${weekdays[(d + 2) % 7]} (bugun) → ${weekdays[r]}',
          meta: {'answer': weekdays[r], 'd': d, 'n': 3, 'kind': kind},
        );
      case 'time_add':
        final start = g.range(7 * 12, 17 * 12) * 5, dur = g.range(3, 30) * 5;
        final end = start + dur;
        final wrong = [end + 60, end - 10, end + 10, end - 60, end + 5].map(hm).toList();
        return g.textChoice(
          question: 'Dars ${hm(start)} da boshlanib, $dur minut davom etdi. Dars soat nechada tugadi?',
          answer: hm(end),
          wrong: wrong,
          concept: 'logic:time:$start:$dur',
          hint: 'Avval yaxlit soatgacha qancha qolganini toping.',
          explanation: '${hm(start)} + $dur minut = ${hm(end)}',
          meta: {'answer': hm(end), 'start': start, 'dur': dur, 'kind': kind},
        );
      case 'duration':
        final start = g.range(8 * 12, 19 * 12) * 5, dur = g.range(5, 40) * 5;
        return _num(g, kind, 'Film ${hm(start)} da boshlanib, ${hm(start + dur)} da tugadi. Film necha minut davom etdi?', dur,
            '1 soat = 60 minut. Yaxlit soatgacha va undan keyingi minutlarni qo‘shing.', '${hm(start + dur)} $minus ${hm(start)} = $dur minut',
            {'start': start, 'end': start + dur});
      default:
        throw StateError('calendar: $kind');
    }
  }

  // ------------------------------------------------------------ Dirixle prinsipi

  static const List<String> _colorWords = ['qizil', 'ko‘k', 'yashil', 'sariq'];

  static Exercise pigeonhole(GenContext g) {
    final kinds = g.pl('kinds');
    final kind = g.pick(kinds.isEmpty ? const ['pair_any', 'one_color'] : kinds);
    final thing = g.pick(const ['paypoq', 'qalam', 'shar', 'koptok']);
    switch (kind) {
      case 'months':
        final variant = g.range(0, 3);
        final (q, answer, expl) = switch (variant) {
          0 => ('Kamida nechta o‘quvchi bo‘lsa, ulardan ikkitasi albatta bir oyda tug‘ilgan bo‘ladi?', 13, '12 oy: 12 + 1 = 13'),
          1 => ('Kamida nechta o‘quvchi bo‘lsa, ulardan ikkitasi albatta haftaning bir kunida tug‘ilgan bo‘ladi?', 8, '7 kun: 7 + 1 = 8'),
          2 => ('Kamida nechta o‘quvchi bo‘lsa, ulardan uchtasi albatta bir oyda tug‘ilgan bo‘ladi?', 25, '12 × 2 + 1 = 25'),
          _ => ('Kamida nechta o‘quvchi bo‘lsa, ulardan uchtasi albatta haftaning bir kunida tug‘ilgan bo‘ladi?', 15, '7 × 2 + 1 = 15'),
        };
        return _num(g, kind, q, answer, 'Eng yomon holatni tasavvur qiling: hamma “qutilar” teng to‘lgan.', expl, {'variant': variant});
      default:
        final k = kind == 'two_color' || kind == 'one_color' ? 2 : g.range(2, 4);
        final counts = [for (var i = 0; i < k; i++) g.range(3, 9)];
        final colors = _colorWords.take(k).toList();
        final list = [for (var i = 0; i < k; i++) '${counts[i]} ta ${colors[i]}'].join(k == 2 ? ' va ' : ', ');
        final total = counts.fold(0, (s, v) => s + v);
        final (goal, answer, expl) = switch (kind) {
          'one_color' => (
              'albatta kamida bitta ${colors[0]} $thing bo‘lishi uchun',
              total - counts[0] + 1,
              'Eng yomon holat: avval hamma ${colors[1]}lari (${counts[1]} ta) chiqadi, keyingisi albatta ${colors[0]}: ${counts[1]} + 1 = ${total - counts[0] + 1}',
            ),
          'two_color' => (
              'albatta ikkala rangdagi $thing ham bo‘lishi uchun',
              math.max(counts[0], counts[1]) + 1,
              'Eng yomon holat: avval ko‘pi (${math.max(counts[0], counts[1])} ta) bir xil rangda chiqadi: ${math.max(counts[0], counts[1])} + 1',
            ),
          'three_same' => (
              'albatta uchta bir xil rangli $thing bo‘lishi uchun',
              2 * k + 1,
              'Eng yomon holat: har rangdan 2 tadan ($k × 2 = ${2 * k}), keyingisi uchinchi bo‘ladi: ${2 * k + 1}',
            ),
          _ => (
              'albatta ikkita bir xil rangli $thing bo‘lishi uchun',
              k + 1,
              'Eng yomon holat: har rangdan bittadan ($k ta), keyingisi albatta takrorlanadi: $k + 1 = ${k + 1}',
            ),
        };
        return _num(g, kind, 'Qutida $list $thing bor. Qarab turmay kamida nechta $thing olish kerak, $goal?', answer,
            'Eng omadsiz holatni tasavvur qiling.', expl, {'counts': counts.join(','), 'k': k});
    }
  }
}
