// Android platforma fayllarini ilovaga moslab sozlaydi.
// `flutter create` dan keyin ishga tushiriladi:
//
//   dart run tool/patch_android.dart
//
// Qiladigan ishlari (qayta ishga tushirish xavfsiz — idempotent):
//  * ilova nomi (android:label) -> "A&M Academy";
//  * offline TTS uchun Android 11+ talab qiladigan <queries> yozuvi;
//  * asosiy manifestda INTERNET va boshqa xavfli ruxsatlar yo'qligini ta'minlash;
//  * release imzosi: `android/key.properties` bo'lsa — o'sha kalit (har build bir xil imzo,
//    shuning uchun yangi versiya eski ustiga o'rnatiladi va bolalar progressi saqlanadi).
// ignore_for_file: avoid_print
import 'dart:io';

const String appLabel = '@string/app_name';
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
      print('$path: minSdk = 21');
    }
    // 5. Release imzosi.
    if (path.endsWith('.kts')) {
      text = _patchSigningKts(text);
      text = _patchFlavorsKts(text);
    } else if (!text.contains('key.properties')) {
      print('$path: Groovy build fayli — release imzosi uchun key.properties qo‘lda ulanadi (README).');
    }
    gradle.writeAsStringSync(text);
  }
}


const String _flavorsKts = '''
    flavorDimensions += "edition"
    productFlavors {
        create("kids") {
            dimension = "edition"
            applicationIdSuffix = ".kids"
            resValue("string", "app_name", "Academy Kids")
        }
        create("school") {
            dimension = "edition"
            applicationIdSuffix = ".school"
            resValue("string", "app_name", "Academy Maktab")
        }
    }
''';

String _patchFlavorsKts(String text) {
  if (text.contains('flavorDimensions += "edition"')) return text;
  final android = RegExp(r'^android\s*\{\s*\
// A&M Academy: android/key.properties bo'lsa — barqaror release imzosi.
val academyKeyProps = Properties().apply {
    val f = rootProject.file("key.properties")
    if (f.exists()) f.inputStream().use { stream -> load(stream) }
}

''';

const String _signingKts = '''
    signingConfigs {
        if (academyKeyProps.getProperty("storeFile") != null) {
            create("academy") {
                storeFile = file(academyKeyProps.getProperty("storeFile"))
                storePassword = academyKeyProps.getProperty("storePassword")
                keyAlias = academyKeyProps.getProperty("keyAlias")
                keyPassword = academyKeyProps.getProperty("keyPassword")
            }
        }
    }
''';

String _patchSigningKts(String text) {
  if (text.contains('academyKeyProps')) return text;
  final android = RegExp(r'^android\s*\{\s*$', multiLine: true).firstMatch(text);
  if (android == null) {
    print('build.gradle.kts: "android {" bloki topilmadi — imzo sozlanmadi.');
    return text;
  }
  // android { ... } ichida `java` — Gradle kengaytmasi, shuning uchun Properties import qilinadi
  // va kalit fayli blokdan tashqarida o'qiladi.
  text = text.replaceRange(android.end, android.end, '\n$_signingKts');
  text = text.replaceRange(android.start, android.start, _propsKts);
  if (!text.contains('import java.util.Properties')) text = 'import java.util.Properties\n\n$text';
  const debugLine = 'signingConfig = signingConfigs.getByName("debug")';
  if (text.contains(debugLine)) {
    text = text.replaceFirst(
      debugLine,
      'signingConfig = signingConfigs.findByName("academy") ?: signingConfigs.getByName("debug")',
    );
    print('build.gradle.kts: release imzosi key.properties orqali.');
  } else {
    print('build.gradle.kts: release signingConfig qatori topilmadi — imzo sozlanmadi.');
  }
  return text;
}
, multiLine: true).firstMatch(text);
  if (android == null) return text;
  text = text.replaceRange(android.end, android.end, '\n\$_flavorsKts');
  print('build.gradle.kts: kids va school flavorlari qo‘shildi.');
  return text;
}

const String _propsKts = '''
// A&M Academy: android/key.properties bo'lsa — barqaror release imzosi.
val academyKeyProps = Properties().apply {
    val f = rootProject.file("key.properties")
    if (f.exists()) f.inputStream().use { stream -> load(stream) }
}

''';

const String _signingKts = '''
    signingConfigs {
        if (academyKeyProps.getProperty("storeFile") != null) {
            create("academy") {
                storeFile = file(academyKeyProps.getProperty("storeFile"))
                storePassword = academyKeyProps.getProperty("storePassword")
                keyAlias = academyKeyProps.getProperty("keyAlias")
                keyPassword = academyKeyProps.getProperty("keyPassword")
            }
        }
    }
''';

String _patchSigningKts(String text) {
  if (text.contains('academyKeyProps')) return text;
  final android = RegExp(r'^android\s*\{\s*$', multiLine: true).firstMatch(text);
  if (android == null) {
    print('build.gradle.kts: "android {" bloki topilmadi — imzo sozlanmadi.');
    return text;
  }
  // android { ... } ichida `java` — Gradle kengaytmasi, shuning uchun Properties import qilinadi
  // va kalit fayli blokdan tashqarida o'qiladi.
  text = text.replaceRange(android.end, android.end, '\n$_signingKts');
  text = text.replaceRange(android.start, android.start, _propsKts);
  if (!text.contains('import java.util.Properties')) text = 'import java.util.Properties\n\n$text';
  const debugLine = 'signingConfig = signingConfigs.getByName("debug")';
  if (text.contains(debugLine)) {
    text = text.replaceFirst(
      debugLine,
      'signingConfig = signingConfigs.findByName("academy") ?: signingConfigs.getByName("debug")',
    );
    print('build.gradle.kts: release imzosi key.properties orqali.');
  } else {
    print('build.gradle.kts: release signingConfig qatori topilmadi — imzo sozlanmadi.');
  }
  return text;
}
