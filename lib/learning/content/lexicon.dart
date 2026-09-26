import 'dart:math';

import 'package:flutter/painting.dart';

import '../../core/utils/map_utils.dart';
import '../models/exercise.dart';

/// Lug'atdagi bitta tushuncha (uch tilda, bitta ID bilan bog'langan).
class LexiconEntry {
  const LexiconEntry({
    required this.id,
    required this.emoji,
    required this.word,
    required this.category,
    required this.tags,
    required this.ageMin,
    this.color,
  });

  final String id;
  final String emoji;
  final Localized word;
  final String category;
  final Set<String> tags;
  final int ageMin;

  /// Asosiy rang (`red`, `yellow` ...), ranglar mashqlari uchun.
  final String? color;

  String get uz => word.uz;

  bool has(String tag) => tags.contains(tag);

  factory LexiconEntry.fromJson(Map<String, dynamic> j) => LexiconEntry(
        id: j['id'].toString(),
        emoji: j['emoji'].toString(),
        word: Localized.fromJson(j),
        category: j['category'].toString(),
        tags: MapUtils.asStringList(j['tags']).toSet(),
        ageMin: MapUtils.asInt(j['ageMin'], 4),
        color: j['color']?.toString(),
      );
}

class ColorEntry {
  const ColorEntry({required this.id, required this.color, required this.name});

  final String id;
  final Color color;
  final Localized name;
}

class ShapeEntry {
  const ShapeEntry({required this.id, required this.name, required this.corners});

  final String id;
  final Localized name;

  /// Burchaklar soni (doira/oval uchun 0).
  final int corners;
}

/// Uch tilli lug'at (`assets/data/lexicon.json`).
class Lexicon {
  Lexicon({required List<LexiconEntry> entries, required this.colors, required this.shapes})
      : entries = entries.where((e) => e.ageMin < 99).toList() {
    for (final e in this.entries) {
      _byId[e.id] = e;
      _byCategory.putIfAbsent(e.category, () => []).add(e);
    }
  }

  final List<LexiconEntry> entries;
  final List<ColorEntry> colors;
  final List<ShapeEntry> shapes;
  final Map<String, LexiconEntry> _byId = {};
  final Map<String, List<LexiconEntry>> _byCategory = {};

  LexiconEntry byId(String id) {
    final e = _byId[id];
    if (e == null) throw ArgumentError('Lug\'atda yo\'q: $id');
    return e;
  }

  bool contains(String id) => _byId.containsKey(id);

  List<String> get categories => _byCategory.keys.toList();

  /// Kategoriya bo'yicha (yoshga mos) elementlar.
  List<LexiconEntry> category(String cat, {int maxAge = 8}) =>
      (_byCategory[cat] ?? const []).where((e) => e.ageMin <= maxAge).toList();

  List<LexiconEntry> where(bool Function(LexiconEntry e) test) => entries.where(test).toList();

  ColorEntry color(String id) => colors.firstWhere((c) => c.id == id);

  ShapeEntry shape(String id) => shapes.firstWhere((s) => s.id == id);

  /// Sanash mashqlari uchun oddiy, tanish narsalar.
  List<LexiconEntry> countables({int maxAge = 8}) => entries
      .where((e) =>
          e.ageMin <= maxAge &&
          const {'fruit', 'vegetable', 'animal', 'bird', 'toy', 'insect', 'sea', 'food'}.contains(e.category))
      .toList();

  LexiconEntry pick(Random rng, List<LexiconEntry> from) => from[rng.nextInt(from.length)];

  factory Lexicon.fromJson(Map<String, dynamic> json) {
    Color parseHex(String hex) => Color(int.parse('FF${hex.replaceAll('#', '')}', radix: 16));
    return Lexicon(
      entries: (json['entries'] as List)
          .map((e) => LexiconEntry.fromJson(MapUtils.asStringMap(e)))
          .toList(),
      colors: (json['colors'] as List).map((e) {
        final m = MapUtils.asStringMap(e);
        return ColorEntry(id: m['id'].toString(), color: parseHex(m['hex'].toString()), name: Localized.fromJson(m));
      }).toList(),
      shapes: (json['shapes'] as List).map((e) {
        final m = MapUtils.asStringMap(e);
        return ShapeEntry(
          id: m['id'].toString(),
          name: Localized.fromJson(m),
          corners: MapUtils.asInt(m['corners']),
        );
      }).toList(),
    );
  }
}
