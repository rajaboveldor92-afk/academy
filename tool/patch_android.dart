// Android platforma fayllarini ilovaga moslab sozlaydi.
// flutter create dan keyin: dart run tool/patch_android.dart
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
  manifest = manifest.replaceFirst(RegExp(r'android:label="[^"]*"'), 'android:label="$appLabel"');

  if (!manifest.contains('android.intent.action.TTS_SERVICE')) {
    if (manifest.contains('<queries>')) {
      manifest = manifest.replaceFirst('<queries>', '<queries>\n$ttsQuery');
    } else {
      manifest = manifest.replaceFirst('</manifest>', '    <queries>\n$ttsQuery\n    </queries>\n</manifest>');
    }
  }

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

  for (final path in ['android/app/build.gradle.kts', 'android/app/build.gradle']) {
    final gradle = File(path);
    if (!gradle.existsSync()) continue;
    var text = gradle.readAsStringSync();
    final match = RegExp(r'minSdk\s*=?\s*(\d+)').firstMatch(text);
    if (match != null && int.parse(match.group(1)!) < 21) {
      text = text.replaceFirst(match.group(0)!, 'minSdk = 21');
    }
    if (path.endsWith('.kts')) {
      text = _patchSigningKts(text);
      text = _patchFlavorsKts(text);
    }
    gradle.writeAsStringSync(text);
  }
}

const String _propsKts = '''
// Academy: android/key.properties bo'lsa — barqaror release imzosi.
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

const String _flavorsKts = '''
    buildFeatures {
        resValues = true
    }

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

String _patchSigningKts(String text) {
  if (text.contains('academyKeyProps')) return text;
  final android = RegExp(r'^android\s*\{', multiLine: true).firstMatch(text);
  if (android == null) return text;
  text = text.replaceRange(android.end, android.end, '\n$_signingKts');
  text = text.replaceRange(android.start, android.start, _propsKts);
  if (!text.contains('import java.util.Properties')) {
    text = 'import java.util.Properties\n\n$text';
  }
  const debugLine = 'signingConfig = signingConfigs.getByName("debug")';
  if (text.contains(debugLine)) {
    text = text.replaceFirst(
      debugLine,
      'signingConfig = signingConfigs.findByName("academy") ?: signingConfigs.getByName("debug")',
    );
  }
  return text;
}

String _patchFlavorsKts(String text) {
  if (text.contains('flavorDimensions += "edition"')) return text;
  final android = RegExp(r'^android\s*\{', multiLine: true).firstMatch(text);
  if (android == null) return text;
  text = text.replaceRange(android.end, android.end, '\n$_flavorsKts');
  print('build.gradle.kts: kids va school flavorlari qo‘shildi.');
  return text;
}
