import 'package:flutter/widgets.dart';

/// Ilova tillari: o'zbek (asosiy), rus, ingliz.
///
/// Umumiy ekranlar (profil tanlash, ota-ona bo'limi) — [AppSettings.appLanguage];
/// bola ekranlari va mashqlar — har bir bolaning [ChildProfile.language].
/// Til [LangScope] orqali pastdagi vidjetlarga uzatiladi: `final t = Tr.of(context);`.
class Tr {
  const Tr(this.lang);

  final String lang;

  static const List<String> languages = ['uz', 'ru', 'en'];

  static Tr of(BuildContext context) =>
      Tr(context.dependOnInheritedWidgetOfExactType<LangScope>()?.lang ?? 'uz');

  /// Bitta matnning uch tildagi varianti.
  String p(String uz, String en, String ru) => switch (lang) {
        'ru' => ru,
        'en' => en,
        _ => uz,
      };

  /// Ruscha ko'plik: 1 год, 2 года, 5 лет.
  static String ruPlural(int n, String one, String few, String many) {
    final m10 = n % 10, m100 = n % 100;
    if (m10 == 1 && m100 != 11) return one;
    if (m10 >= 2 && m10 <= 4 && (m100 < 12 || m100 > 14)) return few;
    return many;
  }

  String langName(String code) => switch (code) {
        'ru' => 'Русский',
        'en' => 'English',
        _ => 'O‘zbekcha',
      };

  // ------------------------------------------------------------ Umumiy
  String get back => p('Orqaga', 'Back', 'Назад');
  String get save => p('Saqlash', 'Save', 'Сохранить');
  String get cancel => p('Bekor', 'Cancel', 'Отмена');
  String get delete => p('O‘chirish', 'Delete', 'Удалить');
  String get listen => p('Tinglash', 'Listen', 'Послушать');
  String get parent => p('Ota-ona', 'Parents', 'Родители');
  String get profileNotFound => p('Profil topilmadi', 'Profile not found', 'Профиль не найден');
  String years(int n) => p('$n yosh', n == 1 ? '1 year old' : '$n years old', '$n ${ruPlural(n, 'год', 'года', 'лет')}');
  String minutesShort(int n) => p('$n daq', '$n min', '$n мин');
  String minutes(int n) => p('$n daqiqa', '$n min', '$n мин');
  String days(int n) => p('$n kun', n == 1 ? '1 day' : '$n days', '$n ${ruPlural(n, 'день', 'дня', 'дней')}');
  String get unlimited => p('Cheklanmagan', 'Unlimited', 'Без ограничений');
  String get unlimitedLower => p('cheklanmagan', 'unlimited', 'без ограничений');

  // ------------------------------------------------------------ Profil tanlash
  String get whoPlays => p('Kim o‘ynaydi?', 'Who is playing?', 'Кто играет?');
  String get newProfileParent => p('Yangi profil (ota-ona)', 'New profile (parents)', 'Новый профиль (родители)');
  String get noProfiles => p('Hali profil yo‘q.\nOta-ona pastdagi tugma orqali profil yaratadi.',
      'No profiles yet.\nA parent can create one with the button below.',
      'Профилей пока нет.\nРодитель может создать профиль кнопкой внизу.');

  // ------------------------------------------------------------ Profil muharriri
  String get editProfile => p('Profilni tahrirlash', 'Edit profile', 'Редактировать профиль');
  String get newProfile => p('Yangi profil', 'New profile', 'Новый профиль');
  String get namePlaceholder => p('Ism', 'Name', 'Имя');
  String photoOpenFailed(Object e) => p('Rasmni ochib bo‘lmadi: $e', 'Could not open the photo: $e', 'Не удалось открыть фото: $e');
  String get pickGallery => p('Galereyadan tanlash', 'Choose from gallery', 'Выбрать из галереи');
  String get takePhoto => p('Kamerada suratga olish', 'Take a photo', 'Сфотографировать');
  String get removePhoto => p('Rasmni olib tashlash (avatar ko‘rsatiladi)', 'Remove photo (avatar will be shown)', 'Убрать фото (будет аватар)');
  String get addPhoto => p('Rasm qo‘shish', 'Add photo', 'Добавить фото');
  String get changePhoto => p('Rasmni almashtirish', 'Change photo', 'Заменить фото');
  String get photoLocalOnly => p('🔒 Rasm faqat shu telefonda saqlanadi va hech qayerga yuborilmaydi.',
      '🔒 The photo is stored only on this phone and is never sent anywhere.',
      '🔒 Фото хранится только на этом телефоне и никуда не отправляется.');
  String get fullNameLabel => p('To‘liq ism (kartada)', 'Full name (on the card)', 'Полное имя (на карточке)');
  String get fullNameHint => p('Masalan: Odilbekov Azamjon Eldorovich', 'For example: Odilbekov Azamjon Eldorovich', 'Например: Одилбеков Азамжон Элдорович');
  String get shortNameLabel => p('Qisqa ism (murojaat uchun)', 'Short name (how we address the child)', 'Короткое имя (для обращения)');
  String get shortNameHint => p('Masalan: Azamjon', 'For example: Azamjon', 'Например: Азамжон');
  String get age => p('Yosh', 'Age', 'Возраст');
  String get themeLabel => p('Profil mavzusi va ramkasi', 'Profile theme and frame', 'Тема и рамка профиля');
  String get avatarLabel => p('Avatar (rasm bo‘lmasa ko‘rinadi)', 'Avatar (shown when there is no photo)', 'Аватар (если нет фото)');
  String get greetingLabel => p('Salomlashuv (ikkinchi qator)', 'Greeting (second line)', 'Приветствие (вторая строка)');
  String childSees(String text) => p('Bola ko‘radi: "$text"', 'The child sees: "$text"', 'Ребёнок увидит: «$text»');
  String get appLanguageForChild => p('Ilova tili (bola uchun)', 'App language (for the child)', 'Язык приложения (для ребёнка)');
  String get nameRequired => p('Qisqa ismni kiriting', 'Enter a short name', 'Введите короткое имя');
  String get nameTooLong => p('Ism juda uzun', 'The name is too long', 'Имя слишком длинное');
  String get fullNameTooLong => p('To‘liq ism juda uzun', 'The full name is too long', 'Полное имя слишком длинное');
  String get ageRange => p('Yosh 3 dan 16 gacha bo‘lishi kerak', 'Age must be from 3 to 16', 'Возраст должен быть от 3 до 16');
  String get gradeLabel => p('Sinf', 'Grade', 'Класс');
  String get preschool => p('Maktabgacha', 'Preschool', 'Дошкольник');
  String gradeName(int g) => g <= 0 ? preschool : p('$g-sinf', 'Grade $g', '$g класс');
  String get gradeHint => p('Maktab o‘quvchisi uchun sinfni tanlang — fanlar va mavzular shu sinf dasturiga mos bo‘ladi.',
      'For a school pupil choose the grade — subjects and topics follow that grade’s curriculum.',
      'Для школьника выберите класс — предметы и темы будут по программе этого класса.');
  String themeName(String id) => switch (id) {
        'ocean' => p('Dengiz', 'Sea', 'Море'),
        'sunny' => p('Quyosh', 'Sun', 'Солнце'),
        'forest' => p('O‘rmon', 'Forest', 'Лес'),
        'berry' => p('Rezavor', 'Berry', 'Ягода'),
        'space' => p('Koinot', 'Space', 'Космос'),
        'candy' => p('Shirinlik', 'Candy', 'Сладости'),
        _ => id,
      };

  // ------------------------------------------------------------ Bosh sahifa
  String get profiles => p('Profillar', 'Profiles', 'Профили');
  String get parentHold => p('Ota-ona: bosib turing', 'Parents: press and hold', 'Родители: нажмите и удерживайте');
  String get achievements => p('Yutuqlarim', 'My achievements', 'Мои достижения');
  String get dailyLesson => p('BUGUNGI DARSim', 'TODAY’S LESSON', 'УРОК ДНЯ');
  String get dailyLessonSpoken => p('Bugungi darsim', 'Today’s lesson', 'Урок дня');
  String get dailyDone => p('Bugun bajarding! Yana bir marta?', 'Done for today! One more time?', 'Сегодня выполнено! Ещё раз?');
  String dailyJunior(int n) => p('$n ta qiziqarli mashq', '$n fun exercises', '$n интересных заданий');
  String dailySenior(int n) => p('$n ta mashq · 10–20 daqiqa', '$n exercises · 10–20 min', '$n заданий · 10–20 мин');

  // ------------------------------------------------------------ Fan va mavzular
  String get continueLesson => p('Davom etamiz', 'Let’s continue', 'Продолжаем');
  String get openFailed => p('Ochib bo‘lmadi', 'Could not open', 'Не удалось открыть');
  String subjectLoadFailed(String subject) => p('$subject mashg‘ulotlarini o‘qib bo‘lmadi. Ilovani yopib, qayta oching.',
      'Could not load $subject lessons. Close the app and open it again.',
      'Не удалось загрузить занятия «$subject». Закройте и снова откройте приложение.');

  // ------------------------------------------------------------ Dars
  String get lessonLoadFailed => p('Mashqlarni ochib bo‘lmadi.', 'Could not open the exercises.', 'Не удалось открыть задания.');
  String get review => p('takrorlash', 'review', 'повторение');
  String get oneMoreTime => p('Yana bir marta', 'One more time', 'Ещё раз');
  String get firstTryNext => p('Keyingisini birinchi urinishda topamiz!', 'Let’s get the next one on the first try!', 'Следующее угадаем с первой попытки!');
  String get gotIt => p('To‘g‘ri topding!', 'You got it!', 'Правильно!');
  String get next => p('Keyingisi', 'Next', 'Дальше');
  String starsToday(int n) => p('Bugungi yulduzlar: $n ⭐', 'Stars today: $n ⭐', 'Звёзды сегодня: $n ⭐');
  String get gardenWatered => p('🌱 Bog‘ingga suv quydik — gullaring o‘smoqda!', '🌱 We watered your garden — your flowers are growing!', '🌱 Мы полили твой сад — цветы растут!');
  String firstTry(int a, int b) => p('Birinchi urinishda: $a / $b', 'On the first try: $a / $b', 'С первой попытки: $a / $b');
  String levelOf(int a, int b) => p('Daraja: $a / $b', 'Level: $a / $b', 'Уровень: $a / $b');
  String newMedal(String title) => p('Yangi medal: $title', 'New medal: $title', 'Новая медаль: $title');
  String get giftWaiting => p('🎁 Sovg‘a qutisi seni kutyapti! «Yutuqlarim»ga kir.', '🎁 A gift box is waiting for you! Open “My achievements”.', '🎁 Тебя ждёт подарок! Зайди в «Мои достижения».');
  String get playAgain => p('Yana o‘ynaymiz', 'Play again', 'Играем ещё');
  String get home => p('Bosh sahifa', 'Home', 'Главная');
  String get topics => p('Mavzular', 'Topics', 'Темы');
  String get dailyFinished => p('Barakalla! Bugun juda yaxshi harakat qilding!', 'Well done! You worked really hard today!', 'Молодец! Сегодня ты очень старался!');
  String get levelUp => p('Barakalla! Yangi daraja ochildi!', 'Well done! A new level is open!', 'Молодец! Открыт новый уровень!');
  String get levelUpSpoken => p('Yangi daraja ochildi!', 'A new level is open!', 'Открыт новый уровень!');
  String get levelStay => p('Juda yaxshi! Yana mashq qilamiz.', 'Very good! Let’s practise more.', 'Очень хорошо! Потренируемся ещё.');
  String get levelDown => p('Yaxshi harakat! Keyingi safar osonroq mashqlardan boshlaymiz.',
      'Good try! Next time we’ll start with easier exercises.', 'Хорошая попытка! В следующий раз начнём с заданий полегче.');
  String get lookAndRemember => p('Yaxshilab qara va eslab qol!', 'Look carefully and remember!', 'Посмотри внимательно и запомни!');
  String get listenCarefully => p('Diqqat bilan tingla.', 'Listen carefully.', 'Слушай внимательно.');
  String get listenAgain => p('Yana bir marta eshit.', 'Listen once more.', 'Послушай ещё раз.');

  // ------------------------------------------------------------ Mashq ko'rinishlari
  String get sample => p('Namuna', 'Sample', 'Образец');
  String get clear => p('Tozalash', 'Clear', 'Стереть');
  String get show => p('Ko‘rsat', 'Show me', 'Покажи');
  String get weDidIt => p('Bajardik!', 'We did it!', 'Сделали!');
  String get needed => p('🧺 Kerak bo‘ladi', '🧺 You will need', '🧺 Понадобится');
  String get howWeDoIt => p('👣 Qanday bajaramiz', '👣 How we do it', '👣 Как выполняем');
  String aboutMinutes(int n) => p('⏱ ~$n daqiqa', '⏱ ~$n min', '⏱ ~$n мин');
  String get tapArrows => p('Strelkalarni bos…', 'Tap the arrows…', 'Нажимай стрелки…');
  String get yourTurn => p('Sening navbating — oq figuralar', 'Your turn — white pieces', 'Твой ход — белые фигуры');
  String get opponentThinks => p('Raqib o‘ylayapti…', 'The opponent is thinking…', 'Соперник думает…');
  String get youWon => p('Sen yutding! 🏆', 'You won! 🏆', 'Ты победил! 🏆');
  String get opponentWon => p('Bu safar raqib yutdi. Yana o‘ynaymiz!', 'The opponent won this time. Let’s play again!', 'В этот раз победил соперник. Сыграем ещё!');
  String get sum => p('so‘m', 'sum', 'сум');

  // ------------------------------------------------------------ Yutuqlar
  String get myGarden => p('🌳 Mening bog‘im', '🌳 My garden', '🌳 Мой сад');
  String get gardenEmpty => p('Darsni tugat — bog‘ingga birinchi niholcha ekamiz!', 'Finish a lesson and we’ll plant your first sprout!', 'Закончи урок — и мы посадим первый росток!');
  String get gardenFull => p('Bog‘ing gullab-yashnayapti! Darslar gullarni o‘stiradi.', 'Your garden is blooming! Lessons make the flowers grow.', 'Твой сад цветёт! Уроки помогают цветам расти.');
  String lessonsToSprout(int n) => p('Yana $n ta dars — yangi niholcha!', n == 1 ? '1 more lesson — a new sprout!' : '$n more lessons — a new sprout!',
      'Ещё $n ${ruPlural(n, 'урок', 'урока', 'уроков')} — и новый росток!');
  String get giftBox => p('🎁 Sovg‘a qutisi', '🎁 Gift box', '🎁 Подарок');
  String open(int n) => n > 1 ? p('Ochish ($n)', 'Open ($n)', 'Открыть ($n)') : p('Ochish', 'Open', 'Открыть');
  String starsToGift(int n) => p('Yana $n ⭐ to‘pla — sovg‘a qutisi ochiladi!', 'Collect $n more ⭐ to open a gift box!', 'Собери ещё $n ⭐ — и откроется подарок!');
  String get myCollection => p('🧸 Kolleksiyam', '🧸 My collection', '🧸 Моя коллекция');
  String get addedToCollection => p('Kolleksiyangga qo‘shildi!', 'Added to your collection!', 'Добавлено в коллекцию!');
  String get great => p('Zo‘r!', 'Great!', 'Здорово!');
  String wow(String name) => p('Voy! $name!', 'Wow! $name!', 'Ух ты! $name!');
  String get medals => p('🏅 Medallar', '🏅 Medals', '🏅 Медали');
  String get subjectCups => p('🏆 Fan kuboklari', '🏆 Subject cups', '🏆 Кубки по предметам');
  String get cupsInfo => p('🥉 bronza → 🥈 kumush → 🏆 oltin: fandagi mavzularni o‘rganganing sari kubok o‘sadi.',
      '🥉 bronze → 🥈 silver → 🏆 gold: the cup grows as you learn the topics.',
      '🥉 бронза → 🥈 серебро → 🏆 золото: кубок растёт, когда ты изучаешь темы.');

  // ------------------------------------------------------------ Vaqt tugadi
  String get timeUp => p('Bugun juda yaxshi harakat qilding! Endi biroz dam olamiz. Ertaga davom etamiz.',
      'You worked really hard today! Now let’s rest a little. We’ll continue tomorrow.',
      'Сегодня ты очень старался! Теперь немного отдохнём. Продолжим завтра.');
  String get backToProfiles => p('Profillarga qaytish', 'Back to profiles', 'Назад к профилям');

  // ------------------------------------------------------------ Ota-ona: PIN
  String get enterPin => p('PIN kodni kiriting', 'Enter the PIN', 'Введите PIN-код');
  String get wrongPin => p('PIN noto‘g‘ri', 'Wrong PIN', 'Неверный PIN');
  String waitSeconds(int s) => p('Kuting: $s s', 'Wait: $s s', 'Подождите: $s с');
  String get currentPin => p('Hozirgi PIN', 'Current PIN', 'Текущий PIN');
  String get newPin => p('Yangi PIN', 'New PIN', 'Новый PIN');
  String get repeatPin => p('Yangi PINni takrorlang', 'Repeat the new PIN', 'Повторите новый PIN');
  String get pinChanged => p('PIN o‘zgartirildi', 'PIN changed', 'PIN изменён');
  String get pinsMismatch => p('PINlar mos kelmadi, qaytadan kiriting', 'The PINs do not match, try again', 'PIN-коды не совпадают, введите снова');
  String get pinLength => p('PIN 4 ta raqam bo‘lishi kerak', 'The PIN must be 4 digits', 'PIN должен состоять из 4 цифр');
  String get changePin => p('PINni o‘zgartirish', 'Change PIN', 'Изменить PIN');
  String get changePinCode => p('PIN kodni o‘zgartirish', 'Change PIN code', 'Изменить PIN-код');

  // ------------------------------------------------------------ Ota-ona paneli
  String get children => p('Bolalar', 'Children', 'Дети');
  String get addChild => p('Bola qo‘shish', 'Add a child', 'Добавить ребёнка');
  String get settings => p('Sozlamalar', 'Settings', 'Настройки');
  String get soundEffects => p('Ovoz effektlari', 'Sound effects', 'Звуковые эффекты');
  String get voiceWords => p('So‘zlarni ovozda aytish', 'Read words aloud', 'Озвучивать слова');
  String get music => p('Fon musiqasi', 'Background music', 'Фоновая музыка');
  String get parentLanguage => p('Ota-ona bo‘limi va profil tanlash tili', 'Language of the parent section and profile screen', 'Язык раздела для родителей и выбора профиля');
  String get privacyNote => p('Barcha ma’lumotlar faqat shu qurilmada saqlanadi. Reklama, chat va internet yo‘q.',
      'All data is stored only on this device. No ads, no chat, no internet.',
      'Все данные хранятся только на этом устройстве. Без рекламы, чатов и интернета.');
  String ageAndLimit(int age, String limit) => '${years(age)} · ${p('limit', 'limit', 'лимит')}: $limit';
  String todayMinutes(int n) => p('Bugun: $n daqiqa', 'Today: $n min', 'Сегодня: $n мин');
  String get weeklyMinutes => p('Haftalik (daqiqa)', 'This week (minutes)', 'За неделю (минуты)');
  String get detailedReport => p('Batafsil hisobot', 'Detailed report', 'Подробный отчёт');

  // ------------------------------------------------------------ Maktab darsi
  String get check => p('Tekshirish', 'Check', 'Проверить');
  String correctAnswerIs(String a) => p('To‘g‘ri javob: $a', 'Correct answer: $a', 'Правильный ответ: $a');
  String get theory => p('Qisqacha qoida', 'Quick rule', 'Коротко о главном');
  String get startPractice => p('Mashqni boshlash', 'Start practice', 'Начать упражнения');
  String get showRule => p('Qoidani ko‘rish', 'Show the rule', 'Показать правило');
  String get testTitle => p('Nazorat ishi', 'Test', 'Контрольная работа');
  String markLabel(int mark) => p('Baho: $mark', 'Mark: $mark', 'Оценка: $mark');
  String markName(int mark) => switch (mark) {
        5 => p('A’lo!', 'Excellent!', 'Отлично!'),
        4 => p('Yaxshi!', 'Good!', 'Хорошо!'),
        3 => p('Qoniqarli. Mavzularni takrorlaymiz.', 'Satisfactory. Let’s revise the topics.', 'Удовлетворительно. Повторим темы.'),
        _ => p('Mavzularni qayta o‘rganamiz — keyin yana urinib ko‘ramiz.', 'Let’s study the topics again and retry.', 'Повторим темы и попробуем ещё раз.'),
      };
  String get schoolContentUzOnly => p('Maktab fanlari mashqlari hozircha o‘zbek tilida.', 'School subject exercises are in Uzbek for now.',
      'Упражнения по школьным предметам пока на узбекском языке.');

  // ------------------------------------------------------------ Ovozni tekshirish
  String get voiceCheck => p('Ovozni tekshirish', 'Voice check', 'Проверка голоса');
  String get voiceCheckHint => p(
      'O‘zbekcha gaplarning ko‘pini onaning ovozi aytadi. Ruscha va inglizcha so‘zlarni telefonning ovoz dasturi (TTS) o‘qiydi — '
          'shu tilning ovozi telefonda bo‘lmasa, so‘zlar jim qoladi.',
      'Most Uzbek phrases are spoken in the mother’s voice. Russian and English words are read by the phone’s text-to-speech (TTS) — '
          'if the phone has no voice for that language, the words stay silent.',
      'Большинство узбекских фраз звучат голосом мамы. Русские и английские слова читает синтезатор речи телефона (TTS) — '
          'если на телефоне нет голоса для этого языка, слова не звучат.');
  String get voiceChecking => p('Tekshirilmoqda…', 'Checking…', 'Проверяем…');
  String get voiceReady => p('Telefon ovozi bor ✅', 'Phone voice installed ✅', 'Голос телефона есть ✅');
  String get voiceNotDownloaded => p('Ovoz bor, lekin yuklab olinmagan ⚠️', 'Voice found but not downloaded ⚠️', 'Голос есть, но не загружен ⚠️');
  String get voiceMissing => p('Telefon ovozi yo‘q ❌ — so‘zlar jim qoladi', 'No phone voice ❌ — words will be silent', 'Нет голоса телефона ❌ — слова не звучат');
  String get voiceMother => p('Onaning ovozi: bor (3000+ gap) ✅', 'Mother’s voice: included (3000+ phrases) ✅', 'Голос мамы: есть (3000+ фраз) ✅');
  String voiceRest(String status) => p('Qolgan gaplar — $status', 'Other phrases — $status', 'Остальные фразы — $status');
  String get voiceHowTo => p(
      'Qanday yoqiladi: Sozlamalar → Umumiy boshqaruv → Matnni nutqqa aylantirish → «Afzal dvigatel» yonidagi ⚙️ → '
          '«Ovoz ma’lumotlarini o‘rnatish» → tilni yuklab oling. Samsung dvigatelida til bo‘lmasa, «Afzal dvigatel»ni Google’ga '
          'almashtiring. So‘ng bu yerda «Qayta tekshirish»ni bosing.',
      'How to fix: Settings → General management → Text-to-speech → ⚙️ next to “Preferred engine” → “Install voice data” → '
          'download the language. If the Samsung engine lacks it, switch the preferred engine to Google. Then tap “Check again” here.',
      'Как включить: Настройки → Общие настройки → Преобразование текста в речь → ⚙️ рядом с «Предпочитаемый модуль» → '
          '«Установка голосовых данных» → загрузите язык. Если в модуле Samsung языка нет, выберите модуль Google. '
          'Затем нажмите здесь «Проверить снова».');
  String get checkAgain => p('Qayta tekshirish', 'Check again', 'Проверить снова');
  String get close => p('Yopish', 'Close', 'Закрыть');
  String voiceSample(String lang) => switch (lang) {
        'ru' => 'Привет! Давай учиться вместе.',
        'en' => 'Hello! Let’s learn together.',
        _ => 'Bugun juda yaxshi harakat qilding.',
      };

  // ------------------------------------------------------------ Bola sozlamalari
  String get deleteProfile => p('Profilni o‘chirish', 'Delete profile', 'Удалить профиль');
  String deleteProfileConfirm(String name) => p('$name profili va uning barcha natijalari o‘chiriladi. Davom etasizmi?',
      'The profile of $name and all results will be deleted. Continue?',
      'Профиль «$name» и все его результаты будут удалены. Продолжить?');
  String get editProfileHint => p('Rasm, ism, yosh, mavzu va salomni tahrirlash', 'Edit photo, name, age, theme and greeting', 'Изменить фото, имя, возраст, тему и приветствие');
  String get dailyLimit => p('Kunlik vaqt limiti', 'Daily time limit', 'Дневной лимит времени');
  String get difficulty => p('Qiyinlik darajasi', 'Difficulty', 'Сложность');
  String get easier => p('Osonroq', 'Easier', 'Легче');
  String get normal => p('Odatiy', 'Normal', 'Обычно');
  String get harder => p('Qiyinroq', 'Harder', 'Сложнее');
  String get subjects => p('Fanlar', 'Subjects', 'Предметы');
  String get childLanguage => p('Ilova tili (bola ekranlari va mashqlar)', 'App language (child screens and exercises)', 'Язык приложения (экраны ребёнка и задания)');
  String get childLanguageNote => p(
      'O‘zbek tili va Yozish darslari o‘zbekcha, English va Русский darslari o‘z tilida qoladi. Onaning ovozi o‘zbek tilida eshitiladi.',
      'Uzbek and Writing lessons stay in Uzbek; English and Russian lessons stay in their own language. The mother’s voice is heard in Uzbek mode.',
      'Уроки узбекского языка и письма остаются на узбекском, уроки English и русского — на своём языке. Голос мамы звучит в узбекском режиме.');

  // ------------------------------------------------------------ Hisobot
  String reportTitle(String name) => p('Hisobot: $name', 'Report: $name', 'Отчёт: $name');
  String get contentLoadFailed => p('Dastur ma’lumotlarini o‘qib bo‘lmadi.', 'Could not read the curriculum data.', 'Не удалось прочитать данные программы.');
  String get bySubject => p('Fanlar bo‘yicha', 'By subject', 'По предметам');
  String get masteryInfo => p('Foiz — yoshga mos dasturdagi barcha mavzular bo‘yicha o‘rtacha egallash. Mavzu 85% dan oshsa — egallangan hisoblanadi.',
      'The percentage is the average mastery of all topics in the age-appropriate curriculum. A topic above 85% counts as mastered.',
      'Процент — среднее освоение всех тем программы для этого возраста. Тема выше 85% считается освоенной.');
  String get localCalc => p('Barcha hisob-kitoblar faqat shu qurilmada bajariladi. Ma’lumotlar hech qayerga yuborilmaydi.',
      'All calculations happen only on this device. No data is sent anywhere.',
      'Все расчёты выполняются только на этом устройстве. Данные никуда не отправляются.');
  String get mToday => p('bugun, daq', 'today, min', 'сегодня, мин');
  String get mWeek => p('hafta, daq', 'week, min', 'неделя, мин');
  String get mActiveDays => p('faol kunlar', 'active days', 'активные дни');
  String get mStreak => p('ketma-ket kun', 'day streak', 'дней подряд');
  String get mLessons => p('dars', 'lessons', 'уроков');
  String get mDaily => p('bugungi dars', 'daily lessons', 'уроков дня');
  String get mAccuracy => p('1-urinishda to‘g‘ri', 'right on 1st try', 'верно с 1-й попытки');
  String get mStars => p('yulduz', 'stars', 'звёзд');
  String get mMedals => p('medal', 'medals', 'медалей');
  String get last7Minutes => p('Oxirgi 7 kun (daqiqa)', 'Last 7 days (minutes)', 'Последние 7 дней (минуты)');
  String get last7Correct => p('Oxirgi 7 kun (to‘g‘ri javoblar)', 'Last 7 days (correct answers)', 'Последние 7 дней (правильные ответы)');
  String get tips => p('Tavsiyalar', 'Recommendations', 'Рекомендации');
  String get reviewQueue => p('🔁 Takrorlash navbati', '🔁 Review queue', '🔁 Очередь повторения');
  String get mDueToday => p('bugun', 'today', 'сегодня');
  String get mNext7 => p('keyingi 7 kun', 'next 7 days', 'следующие 7 дней');
  String get mQueued => p('jami navbatda', 'total queued', 'всего в очереди');
  String get reviewInfo => p('Xato qilingan tushuncha ertaga, keyin 3 va 7 kundan so‘ng boshqa ko‘rinishda qayta so‘raladi. 7 kunlik takrorlashda ham to‘g‘ri topsa — navbatdan chiqadi.',
      'A concept answered wrongly is asked again in a different form tomorrow, then after 3 and 7 days. If it is right at the 7-day review, it leaves the queue.',
      'Понятие, в котором была ошибка, спрашивается снова в другом виде завтра, затем через 3 и 7 дней. Если на 7-дневном повторении ответ верный — оно уходит из очереди.');
  String get strengthsTitle => p('Kuchli tomonlar va e’tibor kerak', 'Strengths and what needs attention', 'Сильные стороны и что требует внимания');
  String get mastered => p('💪 Egallangan', '💪 Mastered', '💪 Освоено');
  String get noMastered => p('Hali egallangan mavzu yo‘q — darslar davom etmoqda.', 'No mastered topics yet — lessons are in progress.', 'Освоенных тем пока нет — уроки продолжаются.');
  String get needsAttention => p('🤝 E’tibor kerak (oxirgi natija 60% dan past)', '🤝 Needs attention (last result below 60%)', '🤝 Требует внимания (последний результат ниже 60%)');
  String get noStruggles => p('Qiynalayotgan mavzu yo‘q.', 'No topics with difficulties.', 'Трудных тем нет.');
  String subjectLine(int mastery, int mastered, int total, int started, int? acc) => p(
        '$mastery% · mavzular: $mastered/$total egallangan, $started boshlangan${acc == null ? '' : ' · aniqlik $acc%'}',
        '$mastery% · topics: $mastered/$total mastered, $started started${acc == null ? '' : ' · accuracy $acc%'}',
        '$mastery% · темы: $mastered/$total освоено, $started начато${acc == null ? '' : ' · точность $acc%'}',
      );
  String now(String topic) => p('Hozir: $topic', 'Now: $topic', 'Сейчас: $topic');
  String get stNotStarted => p('boshlanmagan', 'not started', 'не начата');
  String get stLearning => p('o‘rganmoqda', 'learning', 'изучает');
  String get stNeedsHelp => p('qiynalmoqda', 'needs help', 'трудности');
  String get stMastered => p('egallangan', 'mastered', 'освоена');
  String levelShort(int a, int b) => p('daraja $a/$b', 'level $a/$b', 'уровень $a/$b');
  String lessonsCount(int n) => p('$n dars', n == 1 ? '1 lesson' : '$n lessons', '$n ${ruPlural(n, 'урок', 'урока', 'уроков')}');
  String tipDaily(String name, bool junior) => p('▶ Bugungi dars hali bajarilmagan — $name uchun ${junior ? '5–10' : '10–20'} daqiqa yetarli.',
      '▶ Today’s lesson is not done yet — ${junior ? '5–10' : '10–20'} minutes are enough for $name.',
      '▶ Урок дня ещё не выполнен — для $name достаточно ${junior ? '5–10' : '10–20'} минут.');
  String tipReviews(int n) => p('🔁 Bugun $n ta tushunchani takrorlash vaqti keldi — «Bugungi darsim» ularni o‘zi qo‘shadi.',
      '🔁 Today $n concepts are due for review — “Today’s lesson” adds them automatically.',
      '🔁 Сегодня пора повторить понятий: $n — «Урок дня» добавит их сам.');
  String tipHelp(String topic, String subject) => p(
      '🤝 «$topic» ($subject) mavzusida qiynalmoqda — birga 1–2 dars qiling; dastur osonroq darajadan davom etadi va 2-xatodan keyin maslahat beradi.',
      '🤝 Having trouble with “$topic” ($subject) — do 1–2 lessons together; the program continues at an easier level and gives a hint after the 2nd mistake.',
      '🤝 Трудности с темой «$topic» ($subject) — позанимайтесь вместе 1–2 урока; программа продолжит с более лёгкого уровня и подскажет после 2-й ошибки.');
  String tipUntouched(String list) => p('🧭 Hali boshlanmagan fanlar: $list.', '🧭 Subjects not started yet: $list.', '🧭 Ещё не начатые предметы: $list.');
  String get tipFamily => p('🏠 «Ota-ona bilan» bo‘limidan bitta ekransiz faoliyatni birga bajaring — materiallar uyda bor narsalar.',
      '🏠 Do one screen-free activity from “With parents” together — the materials are things you have at home.',
      '🏠 Выполните вместе одно занятие без экрана из раздела «С родителями» — материалы есть дома.');
  String tipWeek(int n) => p('📅 Bu hafta $n kun o‘ynadi. Har kuni qisqa dars uzoq, kamdan-kam darsdan samaraliroq.',
      '📅 Played on $n days this week. A short lesson every day works better than long, rare ones.',
      '📅 На этой неделе занятия были $n ${ruPlural(n, 'день', 'дня', 'дней')}. Короткий урок каждый день полезнее длинных и редких.');
  String tipAllGood(String name) => p('🌟 Hammasi joyida: $name muntazam o‘rganmoqda. Yutuqlarini birga ko‘rib, maqtab qo‘ying!',
      '🌟 All good: $name is learning regularly. Look at the achievements together and praise!',
      '🌟 Всё хорошо: $name занимается регулярно. Посмотрите достижения вместе и похвалите!');
}

/// Pastdagi vidjetlar uchun til ([Tr.of]).
class LangScope extends InheritedWidget {
  const LangScope({super.key, required this.lang, required super.child});

  final String lang;

  @override
  bool updateShouldNotify(LangScope oldWidget) => oldWidget.lang != lang;
}
