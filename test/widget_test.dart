import 'package:academy/core/providers.dart';
import 'package:academy/database/seed_data.dart';
import 'package:academy/features/profiles/profile_select_screen.dart';
import 'package:academy/router/app_router.dart';
import 'package:academy/services/audio_service.dart';
import 'package:academy/theme/app_theme.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import 'helpers/test_helpers.dart';

void main() {
  TestDb? t;

  tearDown(() async {
    await t?.dispose();
    t = null;
  });

  Future<void> pumpApp(WidgetTester tester) async {
    await tester.runAsync(() async {
      t = await TestDb.open();
      await SeedData.ensureSeeded(t!.db);
    });
    await tester.pumpWidget(
      ProviderScope(
        overrides: [
          databaseProvider.overrideWithValue(t!.db),
          audioServiceProvider.overrideWithValue(SilentAudioService()),
        ],
        child: MaterialApp(
          theme: AppTheme.light(),
          home: const ProfileSelectScreen(),
          onGenerateRoute: AppRouter.onGenerateRoute,
        ),
      ),
    );
    await tester.pumpAndSettle();
  }

  Future<void> enterPin(WidgetTester tester, String pin) async {
    for (final d in pin.split('')) {
      await tester.tap(find.byKey(Key('pin_$d')));
      await tester.pump();
    }
    await tester.pump(const Duration(milliseconds: 200));
    await tester.pumpAndSettle();
  }

  testWidgets("Kim o'ynaydi? ekrani ikki farzandni ko'rsatadi", (tester) async {
    await pumpApp(tester);
    expect(find.text("Kim o'ynaydi?"), findsOneWidget);
    expect(find.text('Azamjon'), findsOneWidget);
    expect(find.text('6 yosh'), findsOneWidget);
    expect(find.text('Muhammadjon'), findsOneWidget);
    expect(find.text('4 yosh'), findsOneWidget);
    expect(find.text('Yangi profil'), findsOneWidget);
  });

  testWidgets("Ota-ona bo'limi faqat to'g'ri PIN bilan ochiladi", (tester) async {
    await pumpApp(tester);
    await tester.tap(find.byKey(const Key('parent_button')));
    await tester.pumpAndSettle();
    expect(find.text('PIN kodni kiriting'), findsOneWidget);

    await enterPin(tester, '1111');
    expect(find.text("PIN noto'g'ri"), findsOneWidget);
    expect(find.text('Sozlamalar'), findsNothing);

    await enterPin(tester, '1234');
    expect(find.text('Sozlamalar'), findsOneWidget);
    expect(find.text('Azamjon'), findsOneWidget);
  });

  testWidgets("Yangi profil ekrani ochiladi", (tester) async {
    await pumpApp(tester);
    await tester.tap(find.byKey(const Key('new_profile_button')));
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('name_field')), findsOneWidget);
    expect(find.byKey(const Key('age_4')), findsOneWidget);
  });
}
