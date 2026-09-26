import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:hive_ce_flutter/hive_flutter.dart';

import 'app.dart';
import 'core/providers.dart';
import 'database/local_database.dart';
import 'database/seed_data.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Asosiy rejim — portrait. Shaxmat/puzzle ekranlari keyinroq o'zlari landscape'ni yoqadi.
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);

  await Hive.initFlutter('academy');
  final db = await LocalDatabase.open();
  await SeedData.ensureSeeded(db);

  runApp(
    ProviderScope(
      overrides: [databaseProvider.overrideWithValue(db)],
      child: const AcademyApp(),
    ),
  );
}
