import 'package:academy/core/providers.dart';
import 'package:academy/database/seed_data.dart';
import 'package:academy/features/home/greeting_banner.dart';
import 'package:academy/features/profiles/profile_select_screen.dart';
import 'package:academy/router/app_router.dart';
import 'package:academy/services/audio_service.dart';
import 'package:academy/theme/app_theme.dart';
import 'package:academy/widgets/profile_photo.dart';
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
    expect(find.text('Kim o‘ynaydi?'), findsOneWidget);
    expect(find.text('Odilbekov Azamjon Eldorovich'), findsOneWidget);
    expect(find.text('6 yosh'), findsOneWidget);
    expect(find.text('Odilbekov Muhammadjon Eldorovich'), findsOneWidget);
    expect(find.text('4 yosh'), findsOneWidget);
    // Rasm bo'lmaganda avatar va mavzu belgilari ko'rinadi.
    expect(find.text('🦁'), findsOneWidget);
    expect(find.text('🐻'), findsOneWidget);
    expect(find.byKey(const Key('new_profile_button')), findsOneWidget);
  });

  testWidgets("Ota-ona bo'limi faqat to'g'ri PIN bilan ochiladi", (tester) async {
    await pumpApp(tester);
    await tester.tap(find.byKey(const Key('parent_button')));
    await tester.pumpAndSettle();
    expect(find.text('PIN kodni kiriting'), findsOneWidget);

    await enterPin(tester, '1111');
    expect(find.text('PIN noto‘g‘ri'), findsOneWidget);
    expect(find.text('Bolalar'), findsNothing);

    await enterPin(tester, '1234');
    // Ota-ona bo'limining yuqori qismi (ro'yxat pastki qismi ekrandan tashqarida bo'lishi mumkin).
    expect(find.text('Bolalar'), findsOneWidget);
    expect(find.text('Odilbekov Azamjon Eldorovich'), findsOneWidget);
  });

  testWidgets("Yangi profil faqat PIN orqali ochiladi", (tester) async {
    await pumpApp(tester);
    await tester.tap(find.byKey(const Key('new_profile_button')));
    await tester.pumpAndSettle();
    expect(find.text('PIN kodni kiriting'), findsOneWidget);
    await enterPin(tester, '1234');
    expect(find.byKey(const Key('full_name_field')), findsOneWidget);
    // Qisqa ism maydoni pastroqda — ro'yxatni aylantirib ko'ramiz.
    await tester.drag(find.byType(ListView), const Offset(0, -300));
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('name_field')), findsOneWidget);
    expect(find.byKey(const Key('age_4')), findsOneWidget);
  });

  testWidgets('Salomlashuv faqat qisqa ism bilan', (tester) async {
    final azamjon = SeedData.azamjon(DateTime(2026));
    final muhammadjon = SeedData.muhammadjon(DateTime(2026));
    for (final p in [azamjon, muhammadjon]) {
      await tester.pumpWidget(MaterialApp(home: Scaffold(body: GreetingBanner(profile: p))));
      await tester.pumpAndSettle();
      expect(find.text(p.welcomeTitle), findsOneWidget);
      expect(find.textContaining('Odilbekov'), findsNothing);
    }
    expect(azamjon.welcomeTitle, 'Azamjon, xush kelibsiz!');
    expect(azamjon.welcomeSubtitle, 'Bugun birga o‘rganamiz!');
    expect(muhammadjon.welcomeTitle, 'Muhammadjon, xush kelibsiz!');
    expect(muhammadjon.welcomeSubtitle, 'O‘ynab-o‘rganishga tayyormisiz?');
  });

  testWidgets("Rasm fayli yo'q bo'lsa avatar ko'rsatiladi", (tester) async {
    final p = SeedData.azamjon(DateTime(2026)).copyWith(photoPath: '/yoq/rasm.jpg');
    await tester.pumpWidget(
      MaterialApp(home: Scaffold(body: Center(child: ProfilePhoto(profile: p, size: 160)))),
    );
    expect(find.text('🦁'), findsOneWidget);
    expect(find.text('🚀'), findsOneWidget);
  });
}
