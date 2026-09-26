# Azamjon & Muhammadjon Academy — Arxitektura

## 1. Project architecture

Qatlamli (layered) + feature-first tuzilma:

```
UI (features/*/screens, widgets)
   │  ref.watch / ref.read
   ▼
State (Riverpod Notifier'lar: profiles, activeChild, progress, settings, session)
   │
   ▼
Services (AudioService, TimeLimitService, ParentPinService, ContentRepository*, MathGenerator*)
   │
   ▼
Database (LocalDatabase — Hive CE, JSON-map ko‘rinishida saqlash)
```
`*` — Phase 2 da qo‘shiladi.

Asosiy tamoyillar:
- **Offline-first**: hech qanday tarmoq so‘rovi yo‘q. Release manifestida INTERNET ruxsati ham yo‘q.
- **Kontent JSON’da** (`assets/data/*.json`), kodda emas.
- **Yosh → kontent guruhi** avtomatik: `age <= 5` → `_4` fayllar, `age >= 6` → `_6` fayllar.
- **Audio**: avval `assets/audio/<lang>/<key>.mp3` qidiriladi; fayl bo‘lmasa, qurilmaning offline TTS ovozi ishlatiladi (uz → tr → en zaxira tartibi). Keyinchalik haqiqiy ovoz yozuvlarini shunchaki papkaga qo‘yish kifoya.

## 2. Folder structure

```
lib/
  main.dart                 bootstrap (Hive, seed, ProviderScope)
  app.dart                  MaterialApp
  core/
    constants/              app_constants.dart
    utils/                  age_group.dart, date_keys.dart, map_utils.dart
    providers.dart          umumiy provider'lar (db, audio)
  models/                   child_profile, child_progress, app_settings, subject, question
  database/                 local_database.dart, seed_data.dart
  services/                 audio_service, time_limit_service, parent_pin_service
  features/
    splash/  profiles/  home/  parent/  session/
    math/ logic/ chess/ uzbek/ english/ russian/ memory/ attention/ puzzle/ gamification/  (keyingi phase’lar)
  widgets/                  qayta ishlatiladigan UI: BigButton, PinPad, AvatarBubble, SubjectTile
  theme/                    app_colors.dart, app_theme.dart
  router/                   app_router.dart
assets/
  data/                     *.json kontent
  audio/uz en ru rewards/
  images/
  icon/app_icon.png
test/
tool/                       setup_android.sh, patch_android.py
.github/workflows/build.yml
```

## 3. Data models

| Model | Maydonlar |
|---|---|
| ChildProfile | id, name, age, avatar, colorIndex, dailyLimitMinutes, disabledSubjects, difficultyBias, createdAt |
| ChildProgress | childId, completedLessons, correctAnswers, wrongAnswers, stars, medals, currentLevels{subject→level}, subjectScores{subject→correct/total}, dailySeconds{yyyy-MM-dd→sec}, lastPlayed, streak |
| AppSettings | parentPin, soundEnabled, voiceEnabled, musicEnabled, seeded |
| Question | id, subject, topic, ageMin, ageMax, difficulty, questionType, question, options, correctAnswer, image, audio, explanation, rewardStars |

`weeklyProgress` — `dailySeconds` va kunlik natijalardan hisoblanadi (oxirgi 7 kun).

## 4. Database schema (Hive CE)

Hive tanlandi: sof Dart, code-generation talab qilmaydi, juda tez, kichik hajm, Android 9+ da muammosiz. Isar hozir faol qo‘llab-quvvatlanmaydi; SQLite bu hajmdagi kalit-qiymat ma’lumot uchun ortiqcha.

| Box | Kalit | Qiymat |
|---|---|---|
| `profiles` | profile.id | ChildProfile.toMap() |
| `progress` | profile.id | ChildProgress.toMap() |
| `settings` | `"app"` | AppSettings.toMap() |

Backup (`academy_backup.json`) — uchala box’ning JSON nusxasi; import shu formatni tiklaydi.

## 5. Navigation flow

```
Splash (≈1.2s)
  → Kim o‘ynaydi? (profil tanlash)
       ├─ ➕ Yangi profil → Profil muharriri → qaytish
       ├─ [profil] → (limit tugagan bo‘lsa) Vaqt tugadi ekrani
       │             → Bosh sahifa
       │                  ├─ Fan kartasi → Fan ekrani (Phase 2+)
       │                  ├─ 🏆 Yutuqlarim
       │                  └─ 🔒 (bosib turish) → PIN → Ota-ona bo‘limi
       └─ ⚙ Ota-ona (PIN) → Dashboard / Sozlamalar / Profillar / PIN
```

## 6. Packages

| Package | Nima uchun |
|---|---|
| flutter_riverpod | State management (sabab README’da) |
| hive_ce, hive_ce_flutter | Lokal ma’lumotlar bazasi |
| audioplayers | Asset audio (mp3/ogg) ijrosi |
| flutter_tts | Audio fayli yo‘q so‘zlar uchun offline ovoz |
| flutter_launcher_icons (dev) | Ilova ikonkasini generatsiya qilish |
| flutter_lints (dev) | Kod sifati |
