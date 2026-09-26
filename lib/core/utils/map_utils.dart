/// Hive'dan o'qilgan `Map<dynamic, dynamic>` qiymatlarini xavfsiz
/// Dart turlariga aylantirish yordamchilari.
class MapUtils {
  MapUtils._();

  static Map<String, dynamic> asStringMap(Object? value) {
    if (value is Map) {
      return value.map((key, v) => MapEntry(key.toString(), v));
    }
    return <String, dynamic>{};
  }

  static Map<String, int> asIntMap(Object? value) {
    final result = <String, int>{};
    if (value is Map) {
      value.forEach((key, v) {
        if (v is num) result[key.toString()] = v.toInt();
      });
    }
    return result;
  }

  static List<String> asStringList(Object? value) {
    if (value is List) {
      return value.map((e) => e.toString()).toList();
    }
    return <String>[];
  }

  static int asInt(Object? value, [int fallback = 0]) {
    if (value is num) return value.toInt();
    if (value is String) return int.tryParse(value) ?? fallback;
    return fallback;
  }

  static bool asBool(Object? value, [bool fallback = false]) {
    if (value is bool) return value;
    return fallback;
  }

  static DateTime? asDate(Object? value) {
    if (value is String) return DateTime.tryParse(value);
    if (value is int) return DateTime.fromMillisecondsSinceEpoch(value);
    return null;
  }
}
