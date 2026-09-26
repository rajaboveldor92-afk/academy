// Android platforma fayllarini ilovaga moslab sozlaydi.
// `flutter create` dan keyin ishga tushiriladi:
//
//   dart run tool/patch_android.dart
//
// Qiladigan ishlari (qayta ishga tushirish xavfsiz — idempotent):
//  * ilova nomi (android:label) -> "A&M Academy";
//  * offline TTS uchun Android 11+ talab qiladigan <queries> yozuvi;
//  * asosiy manifestda INTERNET va boshqa xavfli ruxsatlar yo'qligini ta'minlash.
// ignore_for_file: avoid_print
import 'dart:io';

const String appLabel = 'A&amp;M Academy';
const String ttsQuery = '''
        <intent>
            <action android:name="android.intent.action.TTS_SERVICE" />
        </intent>''';

void main() {
  final manifestFile = File('android/app/src/main/AndroidManifest.xml');
  if (!manifestFile.existsSync()) {
    stderr.writeln('AndroidManifest.xml topilmadi. Avval tool/setup_android.sh ni ishga tushiring.');
    exit(1);
  }
  var manifest = manifestFile.readAsStringSync();

  // 1. Ilova nomi.
  manifest = manifest.replaceFirst(
    RegExp(r'android:label="[^"]*"'),
    'android:label="$appLabel"',
  );

  // 2. TTS xizmatiga murojaat (Android 11+ package visibility).
  if (!manifest.contains('android.intent.action.TTS_SERVICE')) {
    if (manifest.contains('<queries>')) {
      manifest = manifest.replaceFirst('<queries>', '<queries>\n$ttsQuery');
    } else {
      manifest = manifest.replaceFirst(
        '</manifest>',
        '    <queries>\n$ttsQuery\n    </queries>\n</manifest>',
      );
    }
  }

  // 3. Bolalar ilovasi: tarmoq, joylashuv, kamera, mikrofon ruxsatlari yo'q.
  const forbidden = [
    'android.permission.INTERNET',
    'android.permission.ACCESS_FINE_LOCATION',
    'android.permission.ACCESS_COARSE_LOCATION',
    'android.permission.CAMERA',
    'android.permission.RECORD_AUDIO',
  ];
  for (final permission in forbidden) {
    manifest = manifest.replaceAll(
      RegExp('\\s*<uses-permission[^>]*"${RegExp.escape(permission)}"[^>]*/>'),
      '',
    );
  }

  manifestFile.writeAsStringSync(manifest);
  print('AndroidManifest.xml sozlandi.');

  // 4. minSdk kamida 21 (Android 5.0) — Android 9+ talabini bemalol qoplaydi.
  for (final path in ['android/app/build.gradle.kts', 'android/app/build.gradle']) {
    final gradle = File(path);
    if (!gradle.existsSync()) continue;
    var text = gradle.readAsStringSync();
    final match = RegExp(r'minSdk\s*=?\s*(\d+)').firstMatch(text);
    if (match != null && int.parse(match.group(1)!) < 21) {
      text = text.replaceFirst(match.group(0)!, 'minSdk = 21');
      gradle.writeAsStringSync(text);
      print('$path: minSdk = 21');
    }
  }
}
