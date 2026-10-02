# Azamjon & Muhammadjon Academy

4–7 yoshli bolalarni maktabga tayyorlash uchun **offline** ta'limiy o'yin platformasi (Android, Flutter).
Reklama, chat, login, internet yo'q — barcha ma'lumot faqat qurilmada saqlanadi.

> Arxitektura, ma'lumotlar modeli va navigatsiya sxemasi: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)

## Holat (kontent bosqichlari)

| Bosqich | Tarkib | Holat |
|---|---|---|
| Ilova asosi | Profillar (rasm, to‘liq ism, mavzu), lokal baza, vaqt limiti, ota-ona PIN va panel | ✅ |
| CONTENT 1 | Muhammadjon (4): Matematika M1–M15, Mantiq L1–L15 | ✅ |
| CONTENT 2 | Azamjon (6): Matematika M1–M20, Mantiq L1–L15 | ✅ |
| CONTENT 3 | O‘zbek tili (4 yosh: 18 mavzu, 6 yosh: U1–U14), ✏️ Yozishni o‘rganaman (chiziq, nuqta, harf, raqam, so‘z) | ✅ |
| CONTENT 4–5 | English (4 yosh: 17 mavzu, 6 yosh: E1–E21), Русский (4 yosh: 17, 6 yosh: R1–R15), 🍎 3 tilda (300+ tushuncha) | ✅ |
| CONTENT 6 | ♟ Shaxmat: 4 yosh 12 qadam (doska, figuralar 3 tilda, yurishlar), 6 yosh 20 qadam (koordinatalar, olish, shax, mat, AI bilan mini-o‘yinlar) | ✅ |
| CONTENT 7 | 🧠 Xotira (juft kartalar, ketma-ketlik, nima o‘zgardi…), 🎯 Diqqat (rasmdan topish, farqni top, labirint), 🧩 Puzzle (4–25 bo‘lak), ✋ Motorika, 🤝 Muloqot (hislar, sehrli so‘zlar, xavfsizlik), 🏠 Ota-ona bilan (41 ta Montessori faoliyati) | ✅ |
| CONTENT 8 | ▶ Bugungi darsim (fanlar aralash kunlik dars), takrorlash (shu dars → ertaga → 3 kun → 7 kun), 🌳 bog‘, 🎁 sovg‘a qutisi va kolleksiya, 🏅 24 medal, 🏆 fan kuboklari | ✅ |
| CONTENT 9 | 📊 Ota-ona uchun batafsil hisobot: vaqt va faol kunlar, aniqlik, har fan bo‘yicha egallash %, har mavzu holati (daraja, foiz, oxirgi mashq), takrorlash navbati, kuchli tomonlar va e’tibor kerak bo‘lgan mavzular, tavsiyalar | ✅ |
| CONTENT 10 | Yakuniy QA va release | ✅ |
| Maktab rejimi | 1–8-sinf: profilda sinf, Jasmina (3-sinf) va Akramjon (5-sinf); qoida → mashq → nazorat ishi (5 ballik baho), javobni klaviaturada yozish. 3 va 5-sinf: matematika, ona tili, o‘qish/adabiyot, ingliz, rus, tabiiy fan, informatika, tarix ✅ (4 chorak); mantiq — qo‘shimcha mashqlar; boshqa sinflar — navbatda | 🟡 |
| Ilova tillari | O‘zbekcha, Русский, English — har bir bolaga alohida (interfeys + mashqlar), ota-ona bo‘limi uchun umumiy til | ✅ |

## O‘quv dvigateli

```
assets/data/lexicon.json        uch tilli lug‘at (ID orqali bog‘langan uz/en/ru, emoji, kategoriya, teglar)
assets/data/instructions.json   ko‘rsatmalar banki (uz/en/ru, {o‘rinbosar}, {so‘z:ga} qo‘shimchasi)
assets/data/logic_data.json     analogiya, juftlar, yashash joylari, figuralar (original)
assets/data/uzbek.json          alifbo (29 harf), 564 so‘z bo‘g‘inlari bilan (4 yosh: 438), gap/hikoya bo‘laklari
assets/data/glyphs.json         yozish yo‘nalishlari: harflar, raqamlar, yozuvdan oldingi chiziqlar, nuqtali shakllar
assets/data/montessori.json     "Ota-ona bilan bajaramiz": ekrandan tashqari faoliyatlar (materiallar, qadamlar, foydasi)
assets/data/social.json         hislar, vaziyatlar, sehrli so‘zlar, yaxshi do‘st va xavfsizlik tanlovlari
assets/data/languages.json      ingliz/rus alifbolari, harakatlar, sifatlar (ruscha jins shakllari), iboralar,
                                ruscha so‘z jinsi, inglizcha ko‘plik, ruscha ochiq bo‘g‘inli so‘zlar
assets/data/<fan>_<4|6>.json    o‘quv dasturi: mavzu → 3 daraja → generator parametrlari
lib/learning/generators/        parametrik generatorlar (math, logic, uzbek — junior/senior, writing)
lib/learning/chess/             shaxmat qoidalari (n×n doska, shax, mat), masala tekshiruvi, juda oson/oson AI
lib/learning/engine/            LessonBuilder (takrorlanmaslik), AdaptiveRule (≥85 ↑, 60–84 =, <60 ↓), mastery,
                                DailyPlanner (kunlik dars), SpacedRepetition (takrorlash navbati), Rewards (yutuqlar)
lib/learning/ui/                mashq turlari: tanlash, sudrash, juftlash, guruhlash, xotira, labirint, sudoku, kodlash,
                                bo‘laklardan yig‘ish (harf→so‘z, bo‘g‘in→so‘z, so‘z→gap), barmoq bilan yozish
```

* Savollar dinamik yaratiladi: har bir mavzu × daraja uchun o‘nlab–yuzlab original variant.
* Ovoz: ko‘rsatma o‘zbekcha, sonlar so‘z bilan aytiladi (TTS raqamni boshqa tilda o‘qimasligi uchun).
* Chet tili darslarida ko‘rsatma o‘sha tilda aytiladi (en-US / ru-RU ovozi) va ekranda o‘sha tilda
  ko‘rsatiladi; ostida o‘zbekcha umumiy yordamchi matn (javobni oshkor qilmaydi).
  "3 tilda" o‘yinlarida har bir so‘z o‘z tilida ketma-ket aytiladi: 🔊 Olma → 🔊 Яблоко → 🔊 Apple.
* Bola ekranida foiz yo‘q — faqat yulduzlar; foizlar (mastery) faqat ota-ona panelida.

### ▶ Bugungi darsim va takrorlash

* **Kunlik dars** (bosh sahifadagi katta tugma): 4 yosh — 6 ta mashq (5–10 daqiqa), 6 yosh — 10 ta
  (10–20 daqiqa). Har kuni boshqa fandan boshlanadi; har fandan bola hozir o‘rganayotgan mavzu
  (hali egallanmagan, oldingi mavzulari boshlangan, eng uzoq mashq qilinmagani) olinadi.
  Ota-ona o‘chirgan fanlar kirmaydi; uzoq faoliyatlar (AI bilan partiya, puzzle, ekrandan tashqari ish) kirmaydi.
* **Takrorlash (spaced repetition)**: xato qilingan tushuncha shu darsning o‘zida 2–3 mashqdan keyin boshqa
  ko‘rinishda qayta so‘raladi (darsda ko‘pi bilan 2 marta), so‘ng ertaga → 3 kundan keyin → 7 kundan keyin
  kunlik darsga qo‘shiladi (darsning uchdan biridan oshmaydi). Takrorlashda xato — yana ertadan boshlanadi.
* **Yutuqlar** (faqat bolaning o‘zi bilan, boshqa bola bilan solishtirilmaydi; real pul va tasodifiy
  “loot box” yo‘q): ⭐ yulduzlar, 🔥 ketma-ket kunlar, 🌳 har 2 darsda yangi niholcha o‘sadigan bog‘,
  🎁 har 30 yulduzga sovg‘a qutisi (36 ta kolleksiya doim bir xil tartibda ochiladi), 🏅 24 ta medal
  (qanday olinishi yozilgan), 🏆 har fan bo‘yicha bronza/kumush/oltin kubok (mavzularni egallashga qarab).
* Yozishni baholash (`TraceScorer`): qamrov, har bir chiziq, uzluksizlik (tartib), yo‘ldan chiqish va
  ortiqcha uzunlik — yumshoq, lekin tartibsiz bo‘yashni o‘tkazmaydi. 2 xatodan keyin namoyish, 4 xatodan keyin yakun.
* Tahrirlash manbalari: `tool/content/*.py` → `python3 tool/content/<fayl>.py` JSON’ni qayta yaratadi.

### Kontentni avtomatik tekshirish

`flutter test test/content` har bir mavzu va daraja uchun 120 tadan mashq yaratib tekshiradi:
dublikat ID, bo‘sh savol/variant, to‘g‘ri javob variantlar ichida va yagona, matematik to‘g‘rilik
(qo‘shish, ayirish, taqqoslash, ketma-ketlik, pul, soat), yoshga moslik (4 yosh ≤ 10, 6 yosh ≤ 100),
Android 9 da ko‘rinmaydigan emoji, uch til tarjimalarining to‘liqligi va o‘rinbosarlar mosligi,
sudoku/labirint/kodlash yechimi borligi, har darajada ≥ 15 xil savol va umumiy hajm (29-band).
O‘zbek tili: bo‘g‘inlar so‘zni tashkil etishi, har bo‘g‘inda bitta unli, lug‘at bog‘lanishlari, so‘z hajmi
(4 yosh ≥ 250, 6 yosh ≥ 500). Yozish: har bir harf/raqam uchun chiziq borligi, namuna o‘tishi,
tartibsiz chizish va tushib qolgan chiziq o‘tmasligi.

## Maktab rejimi (1–8-sinf)

* Profilda **sinf** tanlanadi (Ota-ona → profil tahriri → «Sinf»). Sinf tanlangan bola uchun fanlar va mavzular
  shu sinf dasturidan olinadi, kichiklar esa yoshiga qarab (4 / 6 yosh dasturi) o‘ynaydi. Bir ilovada 4 bola:
  Azamjon (6 yosh), Muhammadjon (4 yosh), Jasmina (3-sinf), Akramjon (5-sinf).
* Fanlar (O‘zbekiston tayanch o‘quv rejasi bo‘yicha): Matematika, Ona tili, O‘qish / Adabiyot, Ingliz tili,
  Rus tili (2-sinfdan), Tabiiy fan (1–6), Texnologiya (3 va 5), Informatika, Geografiya, Biologiya, Fizika, Kimyo (7–8).
  Dasturi tayyor bo‘lgan fanlargina bosh sahifada ko‘rinadi.
* Dars formati: **qisqa qoida va misollar** (📘, dars davomida ham ochiladi) → **mashqlar** (tanlash yoki javobni
  ekrandagi klaviaturada yozish: son, kasr `3/4`, o‘nli kasr `0,75`) → har chorak oxirida **nazorat ishi**
  (10 ta aralash savol, 5 ballik baho: ≥90% — 5, ≥70% — 4, ≥50% — 3).
* Maktab o‘quvchisiga ko‘rsatma avtomatik o‘qib berilmaydi (o‘zi o‘qiydi, 🔊 bosilsa aytiladi); chet tili darslari bundan mustasno.
* Kontent: `tool/content/school/*.py` → `assets/data/school/<fan>_g<sinf>.json`; generatorlar `lib/learning/generators/school/`.
  Mavzular darslik tartibiga moslangan, tushuntirish va savollar o‘zimizniki (darslik matnlari ko‘chirilmagan).
* Tekshiruv: `test/content/school_content_test.dart` — har bir mashq javobi mustaqil hisoblab tekshiriladi.
* **3 va 5-sinf to‘liq fanlari (1.5.0):** Ona tili, O‘qish/Adabiyot, Ingliz tili, Rus tili, Tabiiy fan, Informatika, Tarix (5-sinf) — har biri 4 chorak,
  14–16 mavzu, har chorakda nazorat ishi va yillik takrorlash; jami ~3 940 ta savol.
  Ona tili savollari so‘z ro‘yxatlaridan (`uzlang.py`) dastur bilan tuziladi, sinonim/antonim chalg‘ituvchilari qo‘lda tanlangan. Manba —
  `tool/content/school/<fan>_g<sinf>.py` (`schoolkit.py`: `Q` tanlash, `TF` to‘g‘ri/noto‘g‘ri, `ORDER` so‘zlardan gap,
  `MATCH` juftlash; `d` — qiyinlik 1–3). Qayta yaratish: `python3 tool/content/school/english_g3.py` va hokazo —
  skript savollar sonini, takrorni, javob noto‘g‘rilar ichida emasligini va o‘/g‘ belgisini tekshiradi.
  Chet tilidagi gaplar (`say`) ingliz/rus ovozida aytiladi; ovozda raqam, kasr, soat, tartib son (“3-sinf” → “uchinchi sinf”)
  va o‘lchov birliklari so‘z bilan o‘qiladi.
* **4 va 6-sinf (1.6.0):** Ingliz tili, Rus tili, Tabiiy fan, Informatika — har biri 4 chorak (~2 580 ta savol).
* **Mental arifmetika, 1–8-sinf (1.6.0):** 🧮 alohida fan. Ekranda chiziladigan **abakus (soroban)**: son o‘qish,
  munchoqlarni bosib son qo‘yish (klaviatura o‘rniga abakus), kichik do‘stlar (+4 = +5 − 1), katta do‘stlar (+7 = +10 − 3),
  aralash formula (+6 = +1 − 5 + 10), zanjirli hisob, **flesh-anzan** (sonlar ekranda birin-ketin tez ko‘rinadi, tezlik
  sinfga qarab 2 soniyadan 0,7 soniyagacha) va tez hisoblash usullari (×5, ×9, ×11, ×25, ×99, ×125, 5 bilan tugaydigan
  son kvadrati, 100 ga yaqin sonlar, foizlar, darajalar, ildiz, Gauss usuli, bo‘linish belgilari). Har sinfda 8 mavzu,
  4 ta nazorat ishi va yillik takrorlash. Dastur: `tool/content/school/mental_curricula.py`, generatorlar —
  `lib/learning/generators/school/mental_gen.dart`, tekshiruv — `test/content/mental_test.dart`.
* **Mantiq, 1–8-sinf (1.6.0):** har sinfda 4 chorak, 8–11 mavzu. 1–2-sinf: naqsh, ortiqchasini topish, guruhlash,
  o‘xshatish, labirint, sudoku, matritsa, aylantirish, rasmli tenglamalar, hafta kunlari. 3–8-sinf: o‘ylangan son,
  “kim nima?” jadvali, sehrli kvadrat, rostgo‘y va yolg‘onchilar, Dirixle prinsipi, kombinatorika, yosh masalalari,
  murakkab qonuniyatlar (Fibonachchi, kvadratlar, tub sonlar), 7–8-sinfda mulohaza, inkor va mantiqiy amallar
  (VA, YOKI, EMAS), ehtimollik. Har bir jumboq generator bilan tuziladi va javobi yagonaligi tekshiriladi
  (`lib/learning/generators/school/logic_school.dart`, `test/content/logic_school_test.dart`); dastur —
  `tool/content/school/logic_curricula.py` (3 va 5-sinfdagi eski mavzu kalitlari saqlangan).
* **Matematika, 1–8-sinf (1.6.0):** 1, 2, 4-sinf — mavjud generatorlar bilan (10/20/100 ichida hisob, o‘nliklar,
  ko‘paytirish jadvali, ko‘p xonali sonlar, kasrlar, perimetr, masalalar). 6–8-sinf uchun yangi generatorlar
  (`lib/learning/generators/school/math_upper.dart`): butun sonlar, EKUB/EKUK, o‘nli kasrlar, proporsiya, koordinatalar,
  aylana (π ≈ 3,14), darajalar, algebraik ifodalar, chiziqli tenglama va funksiya, sistemalar, qisqa ko‘paytirish
  formulalari, kvadrat ildiz, kvadrat tenglama va Viyet teoremasi, tengsizliklar, Pifagor teoremasi, yuzalar,
  ko‘pburchak burchaklari, statistika. Dastur — `tool/content/school/math_grades.py`, tekshiruv —
  `test/content/math_upper_test.dart` (har bir javob mustaqil hisoblanadi). Ovozda manfiy son (“−7” → “minus yetti”),
  daraja (“x²”, “2⁵”), ildiz va tengsizlik belgilari so‘z bilan o‘qiladi.

## Texnologiya: interaktiv ustaxonalar

Texnologiya interaktiv ustaxonalari: har biri mavzuga mos saralash, juftlash va ish qadamlarini tartiblashni beradi.
5-sinf mexanizmlar mavzusida virtual batareya–kalit–lampochka zanjiri mavjud; sim/kalit holati lampochkani darhol o‘zgartiradi.
3- va 5-sinfda jami 8 ustaxona, 128 original mashq va 5 zanjir topshirig‘i mavjud.
Kontentni qayta yaratish: `python3 tool/content/school/technology.py`.
Joriy sinf–fan qamrovi va hali yetishmayotgan fayllar: [qamrov auditi](docs/school-content-audit.md).
Bu qo‘shimcha mashqlar barcha sinflarning to‘liq rasmiy yillik o‘quv dasturi sifatida belgilangan emas.

## Ilova tillari

Ilova uch tilda ishlaydi: **O‘zbekcha**, **Русский**, **English**.

* **Har bir bolaga alohida til** — Ota-ona → bola sozlamalari → «Ilova tili (bola ekranlari va mashqlar)»
  (yoki profil tahririda). Bola tanlagach bosh sahifa, fanlar, mavzular, dars, yutuqlar va «vaqt tugadi» ekrani,
  mashq ko‘rsatmalari, maslahatlar, izohlar, variantlar, maqtov va dalda shu tilda bo‘ladi (ovoz ham).
* **Umumiy til** (profil tanlash ekrani va ota-ona bo‘limi, hisobot bilan) — Ota-ona → Sozlamalar.
* Qaysi darslar o‘z tilida qoladi: **O‘zbek tili** va **✏️ Yozish** — o‘zbekcha (so‘z va harflar o‘zbekcha),
  ko‘rsatma ostida bolaning tilidagi tarjimasi ko‘rinadi; **English**, **Русский** va **3 tilda** — o‘rganilayotgan tilda.
* **Onaning ovozi** faqat o‘zbek tilidagi profilda eshitiladi; rus/ingliz profilida gaplar qurilma ovozida (TTS).
* Kod: `lib/l10n/tr.dart` (`Tr` — barcha ekran matnlari, `LangScope` — tilni pastdagi vidjetlarga uzatadi),
  `lib/l10n/lang_providers.dart`; generatorlar `GenContext.lang` / `g.tr(uz, en, ru)` bilan ishlaydi,
  ko‘rsatmalar `InstructionBank` (uch tilda). Ota-ona bilan faoliyatlar va muloqot vaziyatlari tarjimalari:
  `tool/content/family_social_i18n.py` → `python3 tool/content/family_social_src.py`.

## Talablar

- **Flutter 3.27 yoki yangiroq** (stable kanal; tavsiya — eng so'nggi stable). Dart ≥ 3.5.
- Android SDK + Java 17 (Android Studio bilan birga keladi).
- Qurilma: Android 9 va undan yuqori (texnik minimal — Android 5.0 / API 21).

## Package'lar

| Package | Maqsad |
|---|---|
| `flutter_riverpod` | State management |
| `hive_ce`, `hive_ce_flutter` | Lokal ma'lumotlar bazasi |
| `audioplayers` | `assets/audio` dagi ovoz fayllari |
| `flutter_tts` | Ovoz fayli bo'lmagan so'zlar uchun qurilmaning offline ovozi |
| `image_picker`, `path_provider` | Bola rasmi (faqat ilova papkasida saqlanadi, hech qayerga yuborilmaydi) |
| `flutter_launcher_icons` (dev) | Ilova ikonkasi |
| `flutter_lints` (dev) | Kod sifati |

### Nima uchun Riverpod?
- `BuildContext`ga bog'liq emas — servislar (vaqt limiti, progress) ekranlardan tashqarida ham ishlaydi.
- `ProviderContainer` + `overrides` bilan testlash juda oson: baza, audio va hatto **soat** almashtiriladi (vaqt limiti testlari shu tufayli aniq).
- Bloc'ga nisbatan kamroq boilerplate, bu hajmdagi loyiha uchun o'qish va kengaytirish osonroq.
- Kod generatsiyasiz `Notifier` API ishlatilgan.

### Nima uchun Hive CE?
Sof Dart, adapter/code-gen talab qilmaydi (yozuvlar JSON-mos `Map` sifatida saqlanadi), juda tez va kichik. Isar hozir faol qo'llab-quvvatlanmaydi, SQLite esa bu kalit-qiymat ma'lumotlari uchun ortiqcha. Backup (`academy_backup.json`) shu sababli oddiy JSON.

## Loyiha tuzilmasi

```
lib/
  main.dart, app.dart
  core/        constants, utils (age_group, date_keys, map_utils), providers
  models/      child_profile, child_progress, app_settings, subject, speech_part
  database/    local_database (Hive CE), seed_data
  services/    audio_service, time_limit_service, parent_pin_service, profile_photo_service
  features/    splash, profiles, home, lesson, session, parent
  learning/    content, models, generators, engine, chess, ui  (o‘quv dvigateli)
  widgets/     qayta ishlatiladigan UI
  theme/, router/
assets/        data/ (JSON), audio/{uz,en,ru,rewards}/, images/, icon/
test/          unit, kontent, controller va widget testlar
tool/          setup_android.sh / .ps1, patch_android.dart, content/*.py (kontent manbalari)
.github/workflows/build-apk.yml
```

Batafsil: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Birinchi sozlash (bir marta)

Android platforma fayllari (Gradle, AGP, Kotlin versiyalari) **o'rnatilgan Flutter versiyangizga mos** ravishda generatsiya qilinadi — qo'lda yozilgan Gradle fayllar boshqa Flutter versiyasida buziladi.

```bash
# Linux / macOS
bash tool/setup_android.sh
# Windows (PowerShell)
powershell -ExecutionPolicy Bypass -File tool\setup_android.ps1
```

Skript: `flutter create --platforms=android` (mavjud kodga tegmaydi) → `flutter pub get` → ikonka generatsiyasi → `tool/patch_android.dart` (ilova nomi "A&M Academy", TTS uchun `<queries>`, INTERNET/joylashuv/kamera/mikrofon ruxsatlari yo'qligini ta'minlash).

## Ishga tushirish

```bash
flutter analyze
flutter test
flutter run                 # debug, ulangan telefon/emulyatorda
flutter build apk --debug   # debug APK
flutter build apk --release # release APK
```

Natija: `build/app/outputs/flutter-apk/app-release.apk`

### Imzo (yangilanishda progress saqlanishi uchun)

Android yangi versiyani eskisining ustiga faqat **bir xil imzo** bo‘lsa o‘rnatadi; imzo o‘zgarsa ilovani
o‘chirib qayta o‘rnatish kerak bo‘ladi va bolalar natijalari yo‘qoladi. Shuning uchun:

* GitHub Actions har buildni bir xil kalit bilan imzolaydi: `tool/signing/family-release.jks`
  (oilaviy, qo‘lda o‘rnatiladigan build uchun; parol workflow faylida).
* Shaxsiy kalitga o‘tish (masalan, Google Play uchun — tavsiya etiladi): kalit yarating va repozitoriy
  **Settings → Secrets and variables → Actions** ga qo‘shing: `ANDROID_KEYSTORE_BASE64` (`base64 -w0 kalit.jks`),
  `ANDROID_KEYSTORE_PASSWORD`, `ANDROID_KEY_ALIAS`, `ANDROID_KEY_PASSWORD`. Shundan so‘ng workflow o‘sha kalitni
  ishlatadi (kalit almashgan birinchi yangilanishda ilovani bir marta qayta o‘rnatish kerak bo‘ladi).
* Kompyuterda: `android/key.properties` (`storeFile`, `storePassword`, `keyAlias`, `keyPassword`) bo‘lsa release shu
  kalit bilan imzolanadi, bo‘lmasa Flutter’ning debug kaliti ishlatiladi.

## Kompyutersiz: GitHub Actions orqali APK olish

1. github.com da yangi (private bo'lishi mumkin) repozitoriy yarating va shu papkani yuklang.
2. **Actions** bo'limida "Build APK" workflow avtomatik ishga tushadi (yoki "Run workflow").
3. Tugagach, APK **Releases → latest-build** sahifasida paydo bo‘ladi (telefondan to‘g‘ridan-to‘g‘ri yuklab olish mumkin):
   `academy-arm64-v8a.apk` (zamonaviy telefonlar, eng kichik hajm), `academy-armeabi-v7a.apk` (eski 32-bit telefonlar),
   `academy-app-release.apk` (universal). Shuningdek **Artifacts** → `app-release-apk`.

Workflow har safar `analyze`, testlar va release build'ni bajaradi — xato bo'lsa qizil bo'lib ko'rinadi va loglar bilan Issue ochiladi.

## APKni telefonga o'rnatish

1. `app-release.apk` ni telefonga o'tkazing (USB, Telegram "Saqlangan xabarlar", Google Drive).
2. Telefonda faylni oching. "Noma'lum manbalardan o'rnatish" so'ralsa — shu ilova (Fayllar/Telegram) uchun ruxsat bering.
3. **O'rnatish** → ilova "A&M Academy" nomi bilan paydo bo'ladi.
4. Birinchi ochilishda Azamjon (6) va Muhammadjon (4) profillari tayyor turadi. Ota-ona PIN: **1234** — darhol almashtiring (🔒 → Sozlamalar → PIN).

Ovoz: so'zlar telefonning **offline TTS** ovozi bilan aytiladi. Sifatli ovoz uchun: Sozlamalar → Tizim → Til → Matndan nutqqa → "Google nutq xizmati" → rus/ingliz (va mavjud bo'lsa o'zbek) ovoz paketlarini yuklab qo'ying. O'zbek ovozi bo'lmasa, turkcha ovoz ishlatiladi (lotin yozuvini yaxshi o'qiydi).

## Yangi bola profili

- Ilovada: "Kim o'ynaydi?" → **➕ Yangi profil** → ism, yosh, avatar, rang.
- Ota-ona bo'limida: 🔒 → PIN → **Bola qo'shish**. Bola kartasidagi **Batafsil hisobot** — fanlar va mavzular bo‘yicha foizlar, takrorlash navbati, tavsiyalar; **Sozlamalar** — limit, qiyinlik, fanlar va profilni o'chirish.
- Kontent **yoshga** bog'liq: 3–5 yosh → `*_4.json`, 6–8 yosh → `*_6.json`. Yosh o'zgartirilsa, kontent avtomatik almashadi.

## JSON strukturasi (mavzu va savollar qo‘shish)

Savollar qo‘lda bittalab yozilmaydi: har bir fan va yosh uchun **o‘quv dasturi**
(`assets/data/<fan>_<4|6>.json`) mavzularni va ularning 3 darajasini tasvirlaydi, savollarni esa
parametrik generatorlar yaratadi (`lib/learning/generators/`).

```json
{
  "subject": "math", "ageGroup": "4", "ageMin": 3, "ageMax": 5, "lessonSize": 6,
  "title": {"uz": "Matematika", "en": "Maths", "ru": "Математика"},
  "model": "KO‘R → ESHIT → BOS → SUR → MOSLASHTIR → MAQTOV OL",
  "topics": [
    {
      "id": "math4.count_1_5", "code": "M3", "emoji": "✋",
      "title": {"uz": "1 dan 5 gacha", "en": "Numbers 1–5", "ru": "Числа 1–5"},
      "generator": "count_objects", "skill": "counting",
      "prerequisites": ["math4.count_1_3"],
      "levels": [
        {"min": 1, "max": 4, "modes": ["count"]},
        {"min": 1, "max": 5, "modes": ["count", "group"]},
        {"min": 1, "max": 5, "modes": ["drag", "group", "numeral"], "options": 4}
      ]
    }
  ]
}
```

| Maydon | Izoh |
|---|---|
| `subject`, `ageGroup` | Fan (`math`, `logic`, `uzbek`, `writing`, `english`, `russian`, `trilingual`, `chess`, `memory`, `attention`, `puzzle`, `motor`, `social`, `family`) va guruh (`4` — 3–5 yosh, `6` — 6–8 yosh) |
| `lessonSize` | Bir darsdagi mashqlar soni (mavzuda `lessonSize` bilan alohida belgilanishi mumkin) |
| `id`, `code` | Global noyob id (`<fan><guruh>.<nom>`) va dasturdagi tartib (M3, L7) |
| `generator` | `GeneratorRegistry` dagi generator nomi |
| `prerequisites` | Oldin boshlangan bo‘lishi kerak bo‘lgan mavzular (kunlik dars shu tartibda ochadi) |
| `levels` | 3 daraja parametrlari (son chegarasi, variantlar soni, so‘zlar mavzusi va h.k.) |

So‘zlar va rasmlar uch tilli lug‘atdan (`lexicon.json`: id → uz/en/ru, emoji, kategoriya), ko‘rsatmalar
esa ko‘rsatmalar bankidan (`instructions.json`) olinadi.

Yangi mavzu qo‘shish:
1. `tool/content/curriculum_src.py` da tegishli dasturga `T(...)` qatorini qo‘shing (mavjud generator va parametrlar bilan).
2. `python3 tool/content/curriculum_src.py` — JSON fayllar qayta yaratiladi.
3. `flutter test test/content` — har bir daraja uchun 120 ta mashq yaratilib tekshiriladi
   (to‘g‘ri javob yagona, matematik to‘g‘rilik, yoshga moslik, takrorlanmaslik, to‘liq dars tuziladi).
4. `flutter build apk --release`.

## Audio

- **Onaning ovozi** (`assets/audio/uz/ona/*.ogg`, 58 ibora): asl yozuv (2:16) iboralarga bo‘lingan —
  `python3 tool/audio/cut_mother_voice.py Academy_ona_ovozi.mp3` (vaqtlar: `tool/audio/mother_voice_clips.json`).
  Qayerda eshitiladi (`lib/services/mother_voice.dart`):
  - bosh sahifa: "Salom, Azamjon/Muhammadjon, xush kelibsan! Keling, birga o‘ynaymiz va o‘rganamiz. Qaysi o‘yinni
    tanlaymiz?" (qayta kirishda qisqa: "Salom! Azamjon. Keling, birga o‘ynaymiz."); Mantiq fani nomi; "Davom etamiz";
  - ko‘rsatmalar (mazmuni mos bo‘lsa): ko‘p/kam, katta/kichik son, keyingi son, yetishmayotgan son, eng katta/kichik
    shakl, farq qiladigan rasm/shakl, bir xil rasmlar, juftini top, soyasini top, to‘g‘ri yo‘l, keyin nima keladi,
    yetishmayotgan shakl, "Nechta olma bor?", "Qizil doirani tanla", xotira mashqida "Yaxshilab qara. Rasmlarni eslab qol";
  - tinglash darsi boshida "Diqqat bilan tingla"; xatodan keyin dalda va maslahat ("Sanab ko‘r", "Qo‘shib hisobla",
    "Shoshilma", "Yana bir marta eshit" + ko‘rsatma qayta); to‘g‘ri javobda maqtov; kichik yoshda birga sanash
    ("Bir, ikki, uch"); dars yakuni ism bilan ("Barakalla, Azamjon! Bugun juda yaxshi harakat qilding"); vaqt tugaganda
    "Endi biroz dam olamiz".
  Yozuv bo‘lmagan gaplar qurilma ovozida (TTS) aytiladi. Ssenariydagi "Rag‘bat va yakun" bo‘lim sarlavhasi bolaga aytilmaydi.
- **Onaning klonlangan ovozi** (`assets/audio/uz/klon/*.m4a`, ~3000 gap): onaning yozuvidan ikki ibora
  referens qilib olinib, [OmniVoice](https://github.com/k2-fsa/OmniVoice) (zero-shot, o‘zbek tilini qo‘llaydi) modeli
  bilan ilovadagi eng ko‘p ishlatiladigan o‘zbekcha gaplar oldindan tayyorlangan — mashq ko‘rsatmalari, fan va mavzu
  nomlari, medal va sovg‘alar (bola eshitadigan o‘zbekcha gaplarning ~97%). Model ilovaga kirmaydi, faqat tayyor fayllar.
  Fayl nomi — gap matnining xeshi (`lib/services/cloned_voice.dart` ↔ `tool/voice/voice_keys.py`); `AudioService`
  o‘zbekcha gapni avval onaning haqiqiy iborasidan, keyin klonlangan fayllardan qidiradi, topilmasa — TTS.
  Qayta tayyorlash: `tool/voice/` (gaplarni yig‘ish → tanlash → GitHub Actions’da 20 ta parallel bo‘lakda generatsiya,
  `voice-lab` tarmog‘iga push) va `python3 tool/voice/collect.py <zip papka> lines.json`.
- **Ovoz effektlari** (`assets/audio/rewards/{tap,correct,tryAgain,star,medal}.ogg`) va **fon musiqasi**
  (`assets/audio/music/theme.ogg`, 22 soniyalik uzluksiz kuy) — originali, `python3 tool/audio/make_sounds.py`
  bilan sintez qilingan (tashqi namuna yo‘q). Fon musiqasi sukut bo‘yicha o‘chiq; ota-ona panelida yoqiladi,
  past ovozda chaladi va ilova fonga o‘tganda pauza qilinadi. Effekt va musiqa audio fokusni olmaydi — nutqni to‘xtatmaydi.
- **So‘zlar va ko‘rsatmalar**: fayl `assets/audio/<uz|en|ru>/<kalit>.mp3` (yoki `.ogg`, `.m4a`, `.wav`) bo‘lsa — u ijro
  etiladi, bo‘lmasa qurilmaning offline TTS ovozi. Kalit — so‘zning kichik harfli ko‘rinishi, bo‘shliq o‘rniga `_`:
  "Olma" → `assets/audio/uz/olma.mp3`, "Яблоко" → `assets/audio/ru/яблоко.mp3`. Kod o‘zgartirish shart emas.
  Tavsiya: mono, 64 kbps, 1–2 soniya (APK hajmi uchun).

## Testlar

`flutter test` quyidagilarni tekshiradi:
- **Kontent** (`test/content`): barcha fan × yosh × mavzu × daraja uchun mashqlar generatsiyasi,
  to‘g‘rilik, yagona javob, yoshga moslik, emoji, uch til tarjimalari, dars to‘liq tuzilishi, hajm;
  rus va ingliz tilidagi profil uchun ham barcha mavzular (ko‘rsatma bolaning tilida, maslahat va variantlarda
  o‘zbekcha so‘z qolmagan, ovozda raqam yo‘q).
- **Dvigatel** (`test/learning`): adaptiv qoida, mastery, takrorlash navbati, kunlik reja, yutuqlar,
  shaxmat qoidalari, yozishni baholash, barcha mashq ko‘rinishlari (bosish, sudrash, chizish).
- **Controller va model**: profil yaratish/tanlash/o‘chirish, progress saqlash va qayta yuklash
  (eski formatdagi yozuvlar ham), streak, kunlik vaqt limiti (soxta soat bilan), ota-ona PIN, backup.
- **Widget**: profil ekrani, PIN himoyasi, fan → mavzu → dars oqimi, kunlik dars, qayta so‘rash,
  yutuqlar ekrani, ota-ona hisoboti; ruscha/inglizcha profil (bosh sahifa, dars, dalda va maqtov tili),
  bola tili va umumiy ilova tilini tanlash.

## Xavfsizlik

- Release manifestida hech qanday ruxsat yo'q (INTERNET ham) — ilova jismonan tarmoqqa chiqa olmaydi.
- Ota-ona bo'limi PIN bilan; bosh sahifada qulf belgisini **bosib turish** kerak. 5 ta xato urinishdan keyin 30 soniya blok.
- Tashqi havolalar, reklama, chat, ijtimoiy tarmoq yo'q.

### Maktab fanlari: qo‘shimcha mashqlar (1.4.0)

Jasmina (3-sinf) va Akramjon (5-sinf) uchun mantiq, ingliz tili, rus tili,
ona tili, o‘qish/adabiyot, tabiiy fan va informatika; 5-sinf uchun tarix
mashqlari mavjud. Matematika va to‘liq shaxmat avvalgi tartibda ishlaydi.
Yangi kontent: 15 dastur, 75 mavzu (takrorlash darslari bilan), 454 yozilgan
savol hamda tasodifiy mantiq va matnni tushunish mashqlari.
Bu qo‘shimcha mashqlar to‘plami; rasmiy yillik darslikni to‘liq qamrash da’vosi yo‘q.
Qoidalar va izohlar o‘zbekcha; chet tilidagi savollar tegishli tilda aytiladi.

Kontent manbasi: `tool/content/school_subjects_src.py` (mantiq; qolgan fanlar 1.5.0 da
`tool/content/school/` dagi batafsil dasturlarga ko‘chirildi); qayta yaratish:
`python3 tool/content/school_subjects_src.py`.
APK tekshiruvi maktab dasturlari va savollar banklari ham yig‘ilganini tekshiradi.
