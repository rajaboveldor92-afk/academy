import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'core/app_edition.dart';
import 'core/constants/app_constants.dart';
import 'features/session/session_lifecycle.dart';
import 'l10n/lang_providers.dart';
import 'l10n/tr.dart';
import 'router/app_router.dart';
import 'theme/app_theme.dart';

/// Ilova ildizi.
class AcademyApp extends ConsumerWidget {
  const AcademyApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final lang = ref.watch(appLangProvider);
    return SessionLifecycle(
      child: MaterialApp(
        title: AppEditionConfig.appName,
        debugShowCheckedModeBanner: false,
        theme: AppTheme.light(),
        initialRoute: AppRoutes.splash,
        onGenerateRoute: AppRouter.onGenerateRoute,
        builder: (context, child) {
          // Tizim shrift o'lchami juda katta bo'lsa ham layout buzilmasin.
          final media = MediaQuery.of(context);
          return MediaQuery(
            data: media.copyWith(
              textScaler: media.textScaler.clamp(maxScaleFactor: 1.3),
            ),
            // Umumiy ekranlar tili; bola ekranlari o'z LangScope'ini qo'yadi.
            child: LangScope(lang: lang, child: child ?? const SizedBox.shrink()),
          );
        },
      ),
    );
  }
}
