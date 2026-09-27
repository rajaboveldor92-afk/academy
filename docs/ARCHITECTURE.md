# Azamjon & Muhammadjon Academy — Arxitektura

## 1. Umumiy tuzilma

Qatlamli (layered) + feature-first tuzilma:

```
UI (features/*, learning/ui, widgets)
   │  ref.watch / ref.read
   ▼
State (Riverpod Notifier'lar: profiles, activeChild, progress, settings, session; contentProvider)
   │
   ▼
O'quv dvigateli (learning/): ContentRepository → GeneratorRegistry → LessonBuilder / DailyPlanner
                              AdaptiveRule + SkillStat (mastery), SpacedRepetition, Rewards
Servislar: AudioService (asset → offline TTS), TimeLimitService, ParentPinService, ProfilePhotoService
   │
   ▼
Database (LocalDatabase — Hive CE, JSON-map ko‘rinishida saqlash)
```

Asosiy tamoyillar:
- **To‘liq offline**: tarmoq so‘rovi yo‘q, release manifestida INTERNET ruxsati ham yo‘q
  (`tool/patch_android.dart` buni ta’minlaydi). Bola rasmi faqat ilova papkasida saqlanadi.
- **Kontent JSON’da** (`assets/data/*.json`), savollar esa parametrik generatorlar orqali
  dinamik yaratiladi: har bir mavzu × daraja uchun o‘nlab–minglab original variant.
- **Yosh → dastur** avtomatik: `age <= 5` → `*_4.json`, `age >= 6` → `*_6.json`.
- **Bola ekranida foiz yo‘q** — faqat yulduzlar va yutuqlar; foizlar faqat ota-ona panelida.
- **Audio**: avval `assets/audio/<lang>/<key>.mp3`; fayl bo‘lmasa, qurilmaning offline TTS ovozi
  (uz → tr zaxira; en-US, ru-RU). Chet tili ko‘rsatmalari o‘z tilida, "3 tilda" — ketma-ket.

## 2. Papkalar

```
lib/
  main.dart, app.dart           bootstrap (Hive, seed, ProviderScope), MaterialApp
  core/                         constants, utils (age_group, date_keys, map_utils), providers (db, audio, soat)
  models/                       child_profile, child_progress, app_settings, subject, speech_part
  database/                     local_database (Hive CE, backup JSON), seed_data (2 farzand profili)
  services/                     audio_service, time_limit_service, parent_pin_service, profile_photo_service
  features/
    splash/  profiles/          profil tanlash, muharrir (rasm, to‘liq ism, mavzu, salom)
    home/                       bosh sahifa (▶ BUGUNGI DARSim, fanlar), fan ekrani, 🏆 Yutuqlarim, vaqt tugadi
    lesson/                     mavzular ro‘yxati, dars ekrani (mavzu darsi va kunlik dars)
    session/                    progress va sessiya (vaqt limiti) controller'lari
    parent/                     PIN, ota-ona paneli, batafsil hisobot (ChildReport), bola sozlamalari
  learning/
    content/                    ContentRepository, lug‘at (lexicon), ko‘rsatmalar banki, til ma’lumotlari
    models/                     Exercise (+ vazifa turlari), Topic, Curriculum, Visual
    generators/                 fanlar bo‘yicha parametrik generatorlar, GeneratorRegistry
    engine/                     LessonBuilder, AdaptiveRule/SkillStat, DailyPlanner, SpacedRepetition, Rewards
    chess/                      n×n doska qoidalari, masala tekshiruvi, oson AI
    ui/                         mashq ko‘rinishlari (14 tur)
  widgets/, theme/, router/
assets/data/                    kontent (JSON), assets/audio/{uz,en,ru,rewards}/, assets/icon/
tool/content/*.py               kontent manbalari → JSON generatsiyasi
test/                           unit, kontent, controller, widget testlar
.github/workflows/build-apk.yml analyze → test → release APK → "latest-build" release
```

## 3. Ma’lumotlar modeli

| Model | Maydonlar |
|---|---|
| ChildProfile | id, name (qisqa ism), fullName, age, avatar, photoPath (lokal), greeting, colorIndex, dailyLimitMinutes, disabledSubjects, difficultyBias (−1/0/+1), createdAt |
| ChildProgress | childId, completedLessons, correctAnswers, wrongAnswers, stars, medals, subjectScores{fan→correct/total}, dailySeconds{kun→soniya}, dailyCorrect{kun→son}, lastPlayed, streak, skills{mavzu→SkillStat}, recent{mavzu→imzolar}, reviews{mavzu\|tushuncha→ReviewItem}, dailyLessons, lastDailyLesson, giftsOpened, counters{chess_win, puzzle_25, perfect_lesson…} |
| SkillStat | level (1..3), ema (joriy darajadagi silliqlangan natija), lessons, attempts, firstTryCorrect, lastPracticed, lastAccuracy → mastery 0..100% |
| ReviewItem | topicId, concept, stage (0 → ertaga, 1 → 3 kun, 2 → 7 kun), due |
| AppSettings | parentPin, soundEnabled, voiceEnabled, musicEnabled, seeded, dataVersion |
| Topic / Curriculum | `assets/data/<fan>_<4\|6>.json`: mavzu → generator → 3 daraja parametrlari (README: JSON strukturasi) |
| Exercise | kind (choice, match, sort, memory, maze, sudoku, coding, assemble, trace, chess, cards, spot, jigsaw, activity), ko‘rsatma (uz/en/ru), ovoz, variantlar/vazifa, conceptKey, hint, explanation, rewardStars |

Ma’lumotlar eski formatdan xatosiz o‘qiladi: yangi maydonlar yo‘q bo‘lsa — standart qiymat.

## 4. Baza (Hive CE)

Hive: sof Dart, code-generation talab qilmaydi, tez, kichik hajm, Android 9+ da muammosiz.

| Box | Kalit | Qiymat |
|---|---|---|
| `profiles` | profile.id | ChildProfile.toMap() |
| `progress` | profile.id | ChildProgress.toMap() |
| `settings` | `"app"` | AppSettings.toMap() |

Har bir o‘zgarish darhol yoziladi (ilova kutilmaganda yopilsa ham progress yo‘qolmaydi).
Yozuvlar hajmi cheklangan: kunlik statistika 60 kun, takrorlanmaslik tarixi mavzuga 60 imzo,
takrorlash navbati 200 tushuncha.

## 5. O‘quv dvigateli

1. **LessonBuilder** — mavzu darsi: generatordan mashqlar, darsda takror yo‘q, bola yaqinda ko‘rgan
   savollar chetlab o‘tiladi, yaroqsiz mashq (`ExerciseValidator`) tashlanadi.
2. **AdaptiveRule** — dars natijasi: ≥85% → keyingi daraja, 60–84% → shu daraja, <60% → osonroq
   daraja; 2-xatodan keyin maslahat.
3. **DailyPlanner** — "▶ BUGUNGI DARSim": takrorlash vaqti kelgan tushunchalar (≤ darsning 1/3)
   + fanlar navbati (har kuni boshqa fandan), har fandan hozir o‘rganilayotgan mavzu.
4. **SpacedRepetition** — xato → shu darsda boshqa ko‘rinishda qayta so‘rash → ertaga → 3 kun → 7 kun.
5. **Rewards** — medallar (shartlari bilan), sovg‘a qutisi (har 30 ⭐, doim bir xil tartib — tasodif yo‘q),
   o‘suvchi bog‘, fan kuboklari. Bolalar bir-biri bilan solishtirilmaydi.

## 6. Navigatsiya

```
Splash
  → Kim o‘ynaydi? (profil tanlash)
       ├─ ➕ Yangi profil (PIN) → Profil muharriri
       ├─ [profil] → (limit tugagan bo‘lsa) Vaqt tugadi
       │             → Bosh sahifa
       │                  ├─ ▶ BUGUNGI DARSim → Dars (aralash)
       │                  ├─ Fan kartasi → Mavzular → Dars → Natija
       │                  ├─ 🏆 Yutuqlarim (bog‘, sovg‘a qutisi, medallar, kuboklar)
       │                  └─ 🔒 (bosib turish) → PIN → Ota-ona bo‘limi
       └─ ⚙ Ota-ona (PIN) → Bolalar → Batafsil hisobot / Sozlamalar; umumiy sozlamalar; PIN
```

## 7. Package'lar

| Package | Nima uchun |
|---|---|
| flutter_riverpod | State management (sabab README’da) |
| hive_ce, hive_ce_flutter | Lokal ma’lumotlar bazasi |
| audioplayers | Asset audio (mp3/ogg) ijrosi |
| flutter_tts | Audio fayli yo‘q so‘zlar uchun offline ovoz |
| image_picker, path_provider | Bola rasmini tanlash va faqat ilova papkasida saqlash |
| flutter_launcher_icons (dev) | Ilova ikonkasini generatsiya qilish |
| flutter_lints (dev) | Kod sifati |
