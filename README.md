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
| CONTENT 9–10 | To‘liq ota-ona paneli, QA, release | ⏳ |

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
  core/        constants, utils (age_group, date_keys), providers
  models/      child_profile, child_progress, app_settings, subject, question
  database/    local_database (Hive), seed_data
  services/    audio_service, time_limit_service, parent_pin_service
  features/    splash, profiles, home, parent, session (+ keyingi fanlar)
  widgets/     qayta ishlatiladigan UI
  theme/, router/
assets/        data/ (JSON), audio/{uz,en,ru,rewards}/, images/, icon/
test/          unit, controller va widget testlar
tool/          setup_android.sh / .ps1, patch_android.dart
.github/workflows/build-apk.yml
```

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

Release APK hozircha Flutter'ning standart debug kaliti bilan imzolanadi — telefonga o'rnatish uchun yetarli. Google Play'ga chiqarish kerak bo'lsa, o'z kalitingizni yarating (`keytool`) va `android/key.properties` orqali ulang.

## Kompyutersiz: GitHub Actions orqali APK olish

1. github.com da yangi (private bo'lishi mumkin) repozitoriy yarating va shu papkani yuklang.
2. **Actions** bo'limida "Build APK" workflow avtomatik ishga tushadi (yoki "Run workflow").
3. Tugagach, ishga tushirish sahifasining pastidagi **Artifacts** → `app-release-apk` ni yuklab oling (zip ichida `app-release.apk`).

Workflow har safar `analyze`, testlar va release build'ni bajaradi — xato bo'lsa qizil bo'lib ko'rinadi.

## APKni telefonga o'rnatish

1. `app-release.apk` ni telefonga o'tkazing (USB, Telegram "Saqlangan xabarlar", Google Drive).
2. Telefonda faylni oching. "Noma'lum manbalardan o'rnatish" so'ralsa — shu ilova (Fayllar/Telegram) uchun ruxsat bering.
3. **O'rnatish** → ilova "A&M Academy" nomi bilan paydo bo'ladi.
4. Birinchi ochilishda Azamjon (6) va Muhammadjon (4) profillari tayyor turadi. Ota-ona PIN: **1234** — darhol almashtiring (🔒 → Sozlamalar → PIN).

Ovoz: so'zlar telefonning **offline TTS** ovozi bilan aytiladi. Sifatli ovoz uchun: Sozlamalar → Tizim → Til → Matndan nutqqa → "Google nutq xizmati" → rus/ingliz (va mavjud bo'lsa o'zbek) ovoz paketlarini yuklab qo'ying. O'zbek ovozi bo'lmasa, turkcha ovoz ishlatiladi (lotin yozuvini yaxshi o'qiydi).

## Yangi bola profili

- Ilovada: "Kim o'ynaydi?" → **➕ Yangi profil** → ism, yosh, avatar, rang.
- Ota-ona bo'limida: 🔒 → PIN → **Bola qo'shish**. Bola kartasini bosib limit, qiyinlik, fanlar va profilni o'chirishni boshqarasiz.
- Kontent **yoshga** bog'liq: 3–5 yosh → `*_4.json`, 6–8 yosh → `*_6.json`. Yosh o'zgartirilsa, kontent avtomatik almashadi.

## JSON strukturasi (yangi savol qo'shish)

Kontent: `assets/data/<fan>_<4|6>.json` — `Question` obyektlari massivi.

```json
[
  {
    "id": "math4_count_001",
    "subject": "math",
    "topic": "counting",
    "ageMin": 3,
    "ageMax": 5,
    "difficulty": 1,
    "questionType": "choice",
    "question": "Nechta olma bor?",
    "image": "🍎🍎🍎",
    "options": ["2", "3", "4"],
    "correctAnswer": "3",
    "audio": "uz/q_nechta_olma",
    "explanation": "Sanaymiz: bir, ikki, uch.",
    "rewardStars": 1
  }
]
```

| Maydon | Izoh |
|---|---|
| `id` | Takrorlanmas identifikator |
| `subject` | `math`, `logic`, `chess`, `uzbek`, `english`, `russian`, `memory`, `attention` |
| `difficulty` | 1 (oson) … 5 |
| `questionType` | `choice`, `imageChoice`, `listenChoice`, `trueFalse` |
| `image` | Emoji matni yoki `assets/images/...` yo'li |
| `correctAnswer` | `options` ichida bo'lishi **shart** (aks holda savol o'tkazib yuboriladi) |
| `audio` | `assets/audio/` ichidagi kalit, kengaytmasiz (ixtiyoriy) |

Yangi savol qo'shish: tegishli faylga obyekt qo'shing → `flutter build apk --release`.

## Yangi audio qo'shish

Fayl: `assets/audio/<uz|en|ru>/<kalit>.mp3` (yoki `.ogg`, `.m4a`, `.wav`).
Kalit — so'zning kichik harfli ko'rinishi, bo'shliq o'rniga `_`: "Olma" → `assets/audio/uz/olma.mp3`, "Яблоко" → `assets/audio/ru/яблоко.mp3`.
Effektlar: `assets/audio/rewards/{tap,correct,tryAgain,star,medal}.mp3`.

Fayl mavjud bo'lsa u ijro etiladi, bo'lmasa TTS ishlaydi — kod o'zgartirish shart emas. Tavsiya: mono, 64 kbps, 1–2 soniya (APK hajmi uchun).

## Testlar

`flutter test` quyidagilarni tekshiradi: profil yaratish/tanlash/o'chirish, yosh → kontent guruhi, progress saqlash va qayta yuklash, yulduz berish, streak, kunlik vaqt limiti (soxta soat bilan), pauza, ota-ona PIN (blok, almashtirish), backup eksport/import, widget: profil ekrani va PIN himoyasi.

## Xavfsizlik

- Release manifestida hech qanday ruxsat yo'q (INTERNET ham) — ilova jismonan tarmoqqa chiqa olmaydi.
- Ota-ona bo'limi PIN bilan; bosh sahifada qulf belgisini **bosib turish** kerak. 5 ta xato urinishdan keyin 30 soniya blok.
- Tashqi havolalar, reklama, chat, ijtimoiy tarmoq yo'q.
