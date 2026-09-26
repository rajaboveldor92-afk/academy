#!/usr/bin/env bash
# Android platform fayllarini o'rnatilgan Flutter versiyasiga mos ravishda
# generatsiya qiladi va ilovaga moslab sozlaydi.
#
#   bash tool/setup_android.sh
#
# Nima uchun generatsiya? Gradle/AGP/Kotlin versiyalari Flutter versiyasi bilan
# qat'iy bog'liq. Ularni qo'lda yozib qo'yish eski yoki yangi Flutter'da build
# xatosiga olib keladi. `flutter create` mavjud fayllarni (lib/, test/, pubspec)
# o'zgartirmaydi — faqat yetishmayotgan platforma fayllarini qo'shadi.
set -euo pipefail
cd "$(dirname "$0")/.."

if [ ! -f android/app/build.gradle.kts ] && [ ! -f android/app/build.gradle ]; then
  echo ">> Android platforma fayllari generatsiya qilinmoqda..."
  flutter create --platforms=android --org uz.academy --project-name academy .
fi

flutter pub get

echo ">> Ilova ikonkasi generatsiya qilinmoqda..."
dart run flutter_launcher_icons

echo ">> AndroidManifest va Gradle sozlanmoqda..."
dart run tool/patch_android.dart

echo ">> Tayyor. Endi: flutter build apk --release"
