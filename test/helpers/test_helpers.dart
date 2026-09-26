import 'dart:io';

import 'package:academy/core/providers.dart';
import 'package:academy/database/local_database.dart';
import 'package:academy/services/audio_service.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:hive_ce/hive.dart';

/// Har bir test uchun alohida vaqtinchalik papkadagi Hive bazasi.
class TestDb {
  TestDb._(this.db, this._dir);

  final LocalDatabase db;
  final Directory _dir;

  static Future<TestDb> open() async {
    final dir = await Directory.systemTemp.createTemp('academy_test_');
    Hive.init(dir.path);
    final db = await LocalDatabase.open();
    return TestDb._(db, dir);
  }

  Future<void> dispose() async {
    await Hive.close();
    if (_dir.existsSync()) await _dir.delete(recursive: true);
  }
}

/// Testda boshqariladigan soat.
class FakeClock {
  FakeClock(this.now);

  DateTime now;

  DateTime call() => now;

  void advance(Duration d) => now = now.add(d);
}

ProviderContainer makeContainer(LocalDatabase db, {FakeClock? clock}) {
  return ProviderContainer(
    overrides: [
      databaseProvider.overrideWithValue(db),
      audioServiceProvider.overrideWithValue(SilentAudioService()),
      if (clock != null) clockProvider.overrideWithValue(clock.call),
    ],
  );
}
