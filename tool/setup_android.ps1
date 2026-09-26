# Windows uchun: PowerShell'da loyiha papkasida ishga tushiring:
#   powershell -ExecutionPolicy Bypass -File tool\setup_android.ps1
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
if (-not (Test-Path "android/app/build.gradle.kts") -and -not (Test-Path "android/app/build.gradle")) {
  flutter create --platforms=android --org uz.academy --project-name academy .
}
flutter pub get
dart run flutter_launcher_icons
dart run tool/patch_android.dart
Write-Host "Tayyor. Endi: flutter build apk --release"
