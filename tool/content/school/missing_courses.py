"""Original supplemental courses for the 22 previously missing declared combinations.

Not a reproduction of, or a completeness claim about, an official textbook.
Run: python3 tool/content/school/missing_courses.py
"""
from schoolkit import Course, L, Q, TF, MATCH

DATA = {}


def add(subject, grade, units):
    DATA[(subject, grade)] = units


def unit(title, text, note=''):
    pairs = [line.split('|') for line in text.strip().splitlines()]
    assert len(pairs) == 8, title
    assert len({p[0] for p in pairs}) == len({p[1] for p in pairs}) == 8, title
    return title, pairs, note


add('informatics', 1, [
 unit('Qurilmalar va ularning vazifasi', '''Kompyuter|Ma’lumot bilan ishlaydigan qurilma
Monitor|Rasm va yozuvni ko‘rsatadigan ekran
Klaviatura|Harf va raqam kiritish vositasi
Sichqoncha|Ekrandagi ko‘rsatkichni boshqarish vositasi
Printer|Ma’lumotni qog‘ozga chiqarish vositasi
Karnay|Ovozni eshittirish vositasi
Mikrofon|Ovozni kiritish vositasi
Kamera|Tasvirni kiritish vositasi''', 'Misol: rasmni ekranda ko‘rish uchun monitor, qog‘ozga chiqarish uchun printer kerak.'),
 unit('Axborot va sezgi', '''Ko‘rish|Rang va shakl haqida ma’lumot olish
Eshitish|Ovoz haqida ma’lumot olish
Hid bilish|Hid haqida ma’lumot olish
Ta’m bilish|Ta’m haqida ma’lumot olish
Teginish|Sirtning silliq yoki g‘adir-budurligini bilish
Rasm|Tasvir orqali berilgan axborot
Yozuv|Harflar orqali berilgan axborot
Yo‘l belgisi|Rasm bilan yo‘lda ko‘rsatma berish''', 'Misol: qo‘ng‘iroqni eshitamiz, qizil chiroqni ko‘ramiz. Axborot turini aniqlab mashq qilamiz.'),
 unit('Tartib va oddiy algoritm', '''Algoritm|Vazifani bajarish qadamlari
Boshlash|Birinchi qadamga o‘tish
Ketma-ketlik|Qadamlarni belgilangan tartibda bajarish
Oldinga|Ko‘rsatkich qaragan tomonga yurish
Orqaga|Ko‘rsatkich qaragan tomonga teskari yurish
O‘ngga|O‘ng tomon yo‘nalishi
Chapga|Chap tomon yo‘nalishi
Tugatish|Vazifa bajarilgach to‘xtash''', 'Misol: qo‘l yuvish rejasida avval suvni ochamiz, keyin qo‘lni yuvamiz, oxirida quritamiz. Qadamlarning joyini almashtirish natijani o‘zgartiradi.'),
 unit('Qurilmadan ehtiyotkor foydalanish', '''To‘g‘ri o‘tirish|Belni suyab ekranga qulay qarash
Tanaffus|Ekrandan uzoqlashib dam olish
Quruq qo‘l|Qurilmaga namlik olib kelmaslik
Ichimlikni chetga qo‘yish|Suyuqlikni qurilmadan uzoq saqlash
Kattadan yordam|Notanish tugma yoki holatni so‘rash
Rozilik so‘rash|Birovning rasmini ishlatishdan oldin so‘rash
Shaxsiy ma’lumot|Ism va manzil kabi o‘zimiz haqidagi ma’lumot
Notanish havola|Kattaga ko‘rsatish kerak bo‘lgan noma’lum yo‘l''', 'Misol: ekran tushunarsiz xabar ko‘rsatsa, tugmalarni tasodifan bosmay, kattadan yordam so‘raymiz.'),
])
add('informatics', 2, [
 unit('Fayl va papkalar', '''Fayl|Saqlangan ma’lumot birligi
Papka|Fayllarni guruhlash joyi
Fayl nomi|Saqlangan ishni ajratadigan yozuv
Saqlash|Ishni keyin ochish uchun yozib qo‘yish
Ochish|Saqlangan ishni ko‘rish
Nusxa|Asl faylning ikkinchi ko‘rinishi
O‘chirish|Keraksiz faylni olib tashlash
Qidirish|Nom bo‘yicha kerakli faylni topish''', 'Misol: “Rasmlar” papkasida “Bahor” nomli fayl saqlansa, uni keyin nomi bilan topamiz.'),
 unit('Matn va rasm bilan ishlash', '''Bo‘sh joy tugmasi|So‘zlar orasida bo‘shliq qoldirish
Enter|Yangi satrga o‘tish
Backspace|Kursordan oldingi belgini o‘chirish
Kursor|Matn kiritiladigan joyni ko‘rsatish
Qalam vositasi|Erkin chiziq chizish
Rang tanlash|Chiziq yoki shakl rangini belgilash
Shakl vositasi|Doira yoki to‘rtburchak chizish
Bekor qilish|Oxirgi amalni ortga qaytarish''', 'Misol: “Men kitob o‘qiyman” jumlasida so‘zlar orasida bo‘sh joy bo‘ladi. Xato harfni Backspace bilan tuzatish mumkin.'),
 unit('Shart va takrorlash', '''Shart|Rost yoki yolg‘onligi tekshiriladigan fikr
Rost|Shart bajarilgan holat
Yolg‘on|Shart bajarilmagan holat
Takrorlash|Bir amalni yana bajarish
Hisoblagich|Bajarilgan takrorlar sonini sanash
Buyruq|Bajarilishi kerak bo‘lgan ko‘rsatma
Natija|Buyruqlar bajarilgach hosil bo‘lgan holat
Xatoni topish|Noto‘g‘ri qadamni aniqlash''', 'Misol: “Oldinda yo‘l bo‘lsa, yur” — shartli ko‘rsatma. “Uch marta yur” — takrorlash. Robotni belgilangan manzilga olib borishni rejalaymiz.'),
 unit('Raqamli odob va xavfsizlik', '''Parol|Hisobga kirishni himoya qiladigan maxfiy yozuv
Muallif|Rasm yoki matnni yaratgan kishi
Manba|Axborot olingan joy
Hurmatli xabar|Boshqani ranjitmay yozilgan muloqot
Shaxsiy manzil|Hamma bilan tarqatilmaydigan yashash joyi
Ruxsat|Birovning ishini ishlatishga rozilik
Ishonchli katta|Shubhali xabarni ko‘rsatadigan yordamchi
Tekshirish|Axborotni boshqa manba bilan solishtirish''', 'Misol: internetdagi rasmdan foydalanishdan oldin ruxsat va muallifni tekshiramiz. Parolni boshqalarga aytmaymiz.'),
])
add('informatics', 7, [
 unit('Axborotni kodlash va birliklar', '''Bit|Ikkita qiymatdan birini ifodalovchi birlik
Bayt|Sakkiz bitdan tashkil topgan birlik
Ikkilik sanoq|Nol va bir raqamlariga asoslangan tizim
Kodlash|Axborotni kelishilgan belgilar bilan ifodalash
Dekodlash|Kodlangan axborotni qayta talqin qilish
Piksel|Raqamli tasvirning kichik elementi
Unicode|Matn belgilarini raqamlar bilan ifodalash standarti
Siqish|Ma’lumotni kamroq joyda saqlash usuli''', 'Misol: 101₂ = 1×4 + 0×2 + 1×1 = 5. Matn, rasm va tovush kompyuterda kodlangan ma’lumot sifatida saqlanadi.'),
 unit('Elektron jadval va formulalar', '''Katak|Satr va ustun kesishgan joy
Satr|Jadvalning gorizontal qatori
Ustun|Jadvalning vertikal qatori
A1|A ustun va birinchi satr manzili
Formula|Hisoblashni ko‘rsatadigan ifoda
SUM|Sonlarni yig‘ish funksiyasi
Nisbiy manzil|Ko‘chirilganda joyiga qarab o‘zgaradigan havola
Mutlaq manzil|Ko‘chirilganda dollar belgisi bilan mahkamlangan havola''', 'Misol: =SUM(A1:A3) uch katakdagi sonlarni qo‘shadi. =A1*2 ko‘chirilganda A1 o‘zgarishi mumkin; =$A$1*2 da manzil mahkamlangan.'),
 unit('Algoritm, shart va sikl', '''O‘zgaruvchi|Qiymatni nom bilan saqlash joyi
Tayinlash|O‘zgaruvchiga qiymat berish
Taqqoslash|Ikki qiymat orasidagi munosabatni tekshirish
Tarmoqlanish|Shartga qarab yo‘l tanlash
Sikl|Buyruqlarni takrorlash tuzilmasi
Kiritish|Dasturga boshlang‘ich ma’lumot berish
Chiqarish|Dastur natijasini ko‘rsatish
Test holati|Dastur uchun ma’lum kirish va kutilgan natija''', 'Misol: agar ball 60 yoki undan katta bo‘lsa “O‘tdi”, aks holda “Takrorla” chiqadi. Chegaradagi 59 va 60 qiymatlarini alohida sinaymiz.'),
 unit('Tarmoq va manbani tekshirish', '''Internet|O‘zaro bog‘langan tarmoqlar majmui
Brauzer|Veb sahifalarni ko‘rish dasturi
URL|Internet resursi manzili
HTTPS|Ulanishda ma’lumotni shifrlashni qo‘llaydigan protokol
Fishing|Aldov bilan maxfiy ma’lumot olishga urinish
Zaxira nusxa|Yo‘qolgan faylni tiklash uchun alohida nusxa
Ikki bosqichli tasdiq|Kirishda paroldan tashqari qo‘shimcha tekshiruv
Dalil|Da’voni asoslaydigan tekshiriladigan ma’lumot''', 'Misol: HTTPS belgisi saytning barcha da’volari to‘g‘ri ekanini kafolatlamaydi. Muallif, sana va mustaqil manbalarni ham solishtiramiz.'),
])
add('informatics', 8, [
 unit('Dasturlashdagi ma’lumot turlari', '''Butun son|Kasrsiz son turi
Haqiqiy son|Kasrli sonlarni ifodalash turi
Satr|Belgilar ketma-ketligi turi
Mantiqiy qiymat|Rost yoki yolg‘on turi
Ro‘yxat|Bir nechta elementni tartib bilan saqlash
Indeks|Elementning ketma-ketlikdagi o‘rnini belgilash
Turga o‘tkazish|Qiymatni boshqa turda ifodalash
Ifoda|Qiymat hosil qiladigan amal yoki birikma''', 'Misol: Python tilida "12" — satr, 12 — butun son; int("12") butun son beradi. Ro‘yxat indekslari noldan boshlanadi.'),
 unit('Funksiya va dastur sinovi', '''Funksiya|Nomlangan qayta ishlatiladigan kod bo‘lagi
Parametr|Funksiya ta’rifidagi kirish nomi
Argument|Funksiya chaqirilganda berilgan qiymat
Qaytarish|Funksiya natijasini chaqiruvchiga berish
Mahalliy o‘zgaruvchi|Funksiya ichidagi o‘zgaruvchi
Sintaksis xatosi|Til qoidasi buzilgan yozuv
Mantiqiy xato|Ishlaydigan kodning noto‘g‘ri natija berishi
Chegaraviy test|Eng kichik yoki o‘tish chegarasidagi holat sinovi''', 'Misol: ikki son yig‘indisini qaytaradigan funksiya uchun (2,3), (0,0), (-2,2) holatlarini tekshiramiz. Natijalar mos ravishda 5, 0, 0 bo‘ladi.'),
 unit('Ma’lumotlar bazasi va qidiruv', '''Jadval|Satrlar va ustunlardagi ma’lumotlar to‘plami
Yozuv|Bitta obyekt haqidagi satr
Maydon|Bir xossa uchun ustun
Birlamchi kalit|Har yozuvni noyob ajratadigan qiymat
So‘rov|Kerakli yozuvlarni olish ko‘rsatmasi
Filtr|Shartga mos yozuvlarni ajratish
Saralash|Yozuvlarni belgilangan tartibga keltirish
Bog‘lanish|Jadvallar orasidagi mos kalitlar munosabati''', 'Misol: kitob jadvalida ID birlamchi kalit, nom va muallif maydon bo‘ladi. Muallif bo‘yicha filtr qidiruvni qisqartiradi; nom bo‘yicha saralash tartibni o‘zgartiradi.'),
 unit('Veb tuzilma va raqamli loyiha', '''HTML|Sahifa tuzilishini belgilash tili
CSS|Sahifa ko‘rinishini belgilash tili
Sarlavha|Sahifadagi bo‘lim nomi
Havola|Boshqa resursga o‘tish elementi
Muqobil matn|Rasm mazmunini matn bilan tushuntirish
Talab|Loyiha bajarishi kerak bo‘lgan shart
Versiya|Ishning ma’lum o‘zgarishlar holati
Foydalanuvchi sinovi|Odam vazifani bajara olishini kuzatish''', 'Misol: kutubxona sahifasida kitob nomlari, qidiruv va tushunarli havolalar bo‘lishi kerak. Rasmga muqobil matn yozamiz va telefonda o‘qilishini sinaymiz.'),
])
add('geography', 7, [
 unit('Xarita va geografik koordinatalar', '''Ekvator|Yerning shimoliy va janubiy yarimsharlarini ajratadigan chiziq
Parallel|Ekvatorga parallel aylana
Meridian|Qutblarni tutashtiradigan yarim aylana
Geografik kenglik|Ekvatordan shimol yoki janubdagi burchak masofasi
Geografik uzunlik|Boshlang‘ich meridiandan sharq yoki g‘arbdagi burchak masofasi
Masshtab|Xaritadagi va joydagi masofalar nisbati
Legenda|Xarita shartli belgilarining izohi
Mutlaq balandlik|Dengiz sathiga nisbatan balandlik''', 'Misol: 1:100000 masshtabda xaritadagi 1 cm joydagi 1 km ga mos. Kenglik N/S, uzunlik E/W bilan belgilanadi.'),
 unit('Yer qobiqlari va relyef', '''Litosfera|Yerning qattiq tashqi qobig‘i
Gidrosfera|Yer suvlarining majmui
Atmosfera|Yerni o‘ragan gaz qobig‘i
Biosfera|Hayot mavjud bo‘lgan sohalar majmui
Tektonik plita|Litosferaning harakatlanadigan yirik bo‘lagi
Tog‘|Atrofga nisbatan baland ko‘tarilgan relyef
Tekislik|Nisbatan kam balandlik farqli keng yer yuzasi
Eroziya|Suv yoki shamolning jinslarni yemirishi''', 'Misol: daryo vodiysi suvning uzoq davom etgan yemirish faoliyati bilan shakllanishi mumkin. Relyef va qobiq tushunchalarini ajratamiz.'),
 unit('Yevrosiyo tabiati', '''Yevrosiyo|Yevropa va Osiyoni birlashtirgan materik
Himolay|Yevrosiyodagi eng baland tog‘ tizimi
Baykal|Dunyodagi eng chuqur ko‘l
Kaspiy|Yuzasi bo‘yicha eng katta ko‘l
Tayga|Ignabargli o‘rmonlar tabiiy zonasi
Dasht|O‘tlar ustun bo‘lgan tabiiy zona
Musson|Fasllarga qarab yo‘nalishini o‘zgartiruvchi shamol
Kontinental iqlim|Okean ta’siri kam va fasliy farqi katta iqlim''', 'Misol: dengizdan uzoqlashish kontinental xususiyatni kuchaytirishi mumkin. Har joyning iqlimiga kenglik va relyef ham ta’sir qiladi.'),
 unit('Tabiiy resurs va muhit', '''Qayta tiklanuvchi resurs|Tabiiy jarayonda qayta hosil bo‘ladigan manba
Qayta tiklanmaydigan resurs|Inson vaqt o‘lchovida juda sekin hosil bo‘ladigan manba
Suv aylanishi|Suvning bug‘lanish, yog‘in va oqim orqali almashishi
Qo‘riqxona|Tabiiy majmua muhofaza qilinadigan hudud
Cho‘llanish|Qurg‘oqchil yerlarda tuproq va o‘simlik qoplamining buzilishi
Ifloslanish|Muhitga zararli moddalar kirishi
Barqaror foydalanish|Resursni kelajak ehtiyojlarini hisobga olib ishlatish
Monitoring|Muhit holatini muntazam kuzatish''', 'Misol: suv qayta aylansa ham toza ichimlik suvi cheklangan. Resursni tejash va holatini kuzatish bir-birini to‘ldiradi.'),
])
add('geography', 8, [
 unit('O‘zbekistonning joylashuvi va relyefi', '''O‘zbekiston|Markaziy Osiyoda joylashgan davlat
Toshkent|O‘zbekiston poytaxti
Qizilqum|Mamlakatdagi yirik cho‘l
Farg‘ona vodiysi|Sharqda tog‘lar orasidagi keng vodiy
Tyan-Shan|Sharq va shimoli-sharqqa tutash tog‘ tizimi
Hisor tizmasi|Janubdagi baland tog‘ tizmalaridan biri
Amudaryo|Orol havzasining yirik daryosi
Sirdaryo|Farg‘ona vodiysi va tekisliklar orqali oqadigan yirik daryo''', 'Misol: xaritada cho‘l, vodiy va tog‘larni ajratamiz. Amudaryo va Sirdaryo Orol dengizi havzasiga tegishli.'),
 unit('Iqlim, suv va tuproq', '''Keskin kontinental iqlim|Yoz va qish harorati farqi katta iqlim
Sug‘orish|Ekin maydoniga sun’iy suv yetkazish
Kanal|Suvni yo‘naltirish uchun qurilgan o‘zan
Suv ombori|Suvni yig‘ib tartibga soluvchi havza
Sho‘rlanish|Tuproqda eruvchan tuzlar to‘planishi
Bo‘z tuproq|Quruq subtropik tog‘oldi hududlariga xos tuproq
Drenaj|Ortiqcha yerosti suvini chiqarish tizimi
Suvni tejovchi usul|Ekin suv sarfini kamaytiradigan sug‘orish yo‘li''', 'Misol: ortiqcha sug‘orish va yomon drenaj sho‘rlanish xavfini oshiradi. Tuproq va suvdan foydalanish birgalikda rejalashtiriladi.'),
 unit('Aholi va xo‘jalik joylashuvi', '''Aholi zichligi|Hudud birligiga to‘g‘ri keladigan aholi soni
Urbanizatsiya|Shaharlar va shahar aholi ulushining o‘sishi
Migratsiya|Aholining yashash joyini o‘zgartirishi
Mehnat resursi|Mehnat qilish imkoniyatiga ega aholi
Sanoat|Xomashyoni qayta ishlash va mahsulot yaratish sohasi
Qishloq xo‘jaligi|Dehqonchilik va chorvachilik sohasi
Xizmat ko‘rsatish|Aholi ehtiyojiga xizmat taqdim etish sohasi
Transport tuguni|Bir necha transport yo‘li tutashgan joy''', 'Misol: aholi zichligi = aholi soni / maydon. 100000 kishi 500 km² hududda yashasa, zichlik 200 kishi/km² bo‘ladi.'),
 unit('Hududiy iqtisodiyot va ekologiya', '''Xomashyo omili|Korxonani material manbasiga yaqin joylashtirish sababi
Energiya omili|Ko‘p quvvat kerak bo‘lgan ishlab chiqarish omili
Iste’molchi omili|Mahsulot xaridoriga yaqin bo‘lish sababi
Logistika|Yuk oqimini rejalash va tashkil etish
Ixtisoslashuv|Hududning ayrim mahsulot yoki xizmatga yo‘nalishi
Kooperatsiya|Korxonalarning ishlab chiqarishda hamkorligi
Qayta ishlash|Chiqindidan yangi material olish
Ekologik baholash|Loyihaning muhitga ta’sirini oldindan tahlil qilish''', 'Misol: tez buziladigan mahsulot ishlab chiqaruvchiga iste’molchiga yaqinlik kerak bo‘lishi mumkin. Joy tanlashda transport va ekologik ta’sir ham hisobga olinadi.'),
])
add('biology', 7, [
 unit('Hayvonlar tuzilishi va tasnifi', '''Hujayra|Tirik organizmning asosiy tuzilish birligi
To‘qima|O‘xshash vazifali hujayralar guruhi
Organ|Bir nechta to‘qimadan tuzilgan a’zo
Organlar tizimi|Birgalikda vazifa bajaradigan organlar majmui
Umurtqasiz|Umurtqa pog‘onasi bo‘lmagan hayvon
Umurtqali|Umurtqa pog‘onasi bor hayvon
Tur|Tabiiy sharoitda o‘zaro ko‘payib nasl bera oladigan organizmlar guruhi
Moslanish|Muhitda yashashga yordam beradigan belgi''', 'Misol: baliq jabra bilan suvda nafas oladi; qush patlari parvoz va issiqlik saqlashga yordam beradi. Belgi va muhitni bog‘laymiz.'),
 unit('Umurtqasiz hayvonlar', '''Bo‘shliqichlilar|Tanasida ichak bo‘shlig‘i va paypaslagichlari bo‘lgan guruh
Yassi chuvalchanglar|Tanasi yassilashgan chuvalchanglar guruhi
Halqali chuvalchanglar|Tanasi ketma-ket halqalardan tuzilgan guruh
Molluskalar|Yumshoq tanali hayvonlar guruhi
Bo‘g‘imoyoqlilar|Bo‘g‘imlangan oyoq va tashqi skeletli guruh
Hasharotlar|Voyaga yetganda olti oyoqli bo‘g‘imoyoqlilar
O‘rgimchaksimonlar|Odatda sakkiz oyoqli bo‘g‘imoyoqlilar
Qisqichbaqasimonlar|Ko‘pchiligi suvda yashaydigan jabra nafasli guruh''', 'Misol: chumoli hasharot, o‘rgimchak o‘rgimchaksimon. Oyoqlar soni va tana qismlari tasniflashga yordam beradi.'),
 unit('Umurtqali guruhlar', '''Baliqlar|Jabra bilan nafas oladigan suv umurtqalilari
Amfibiyalar|Suv va quruqlik bilan bog‘liq hayot kechiradigan guruh
Sudralib yuruvchilar|Odatda quruq tangachali terili umurtqalilar
Qushlar|Pat bilan qoplangan umurtqalilar
Sutemizuvchilar|Bolalarini sut bilan boqadigan umurtqalilar
Jabra|Suvdagi kislorodni olish organi
O‘pka|Havodan gaz almashish organi
Issiqqonlilik|Tana haroratini nisbatan barqaror saqlash''', 'Misol: kit suvda yashasa ham sutemizuvchi va o‘pka bilan nafas oladi. Yashash joyining o‘zi guruhni aniqlash uchun yetarli emas.'),
 unit('Hayvonlar va ekotizim', '''O‘txo‘r|Asosan o‘simlik bilan oziqlanadigan hayvon
Yirtqich|Boshqa hayvonni ovlab oziqlanadigan hayvon
Hammaxo‘r|O‘simlik va hayvon ozuqasini yeydigan hayvon
Oziq zanjiri|Ozuqa orqali energiya o‘tish ketma-ketligi
Changlatuvchi|Gul changini tashishga yordam beruvchi hayvon
Populyatsiya|Bir hududdagi bir tur vakillari
Yashash muhiti|Organizm hayot kechiradigan sharoitlar majmui
Biologik xilma-xillik|Tirik organizmlar va ularning farqlari boyligi''', 'Misol: o‘t → chigirtka → qurbaqa → ilon zanjirida energiya ozuqa bo‘ylab o‘tadi. Bitta bo‘g‘in kamayishi boshqalariga ta’sir qilishi mumkin.'),
])
add('biology', 8, [
 unit('Odam organizmi va tayanch-harakat', '''Skelet|Tana tayanchi bo‘lgan suyaklar majmui
Bo‘g‘im|Suyaklar tutashadigan harakatli joy
Mushak|Qisqarib harakat hosil qiladigan to‘qima
Pay|Mushakni suyakka bog‘laydigan tuzilma
Boylam|Bo‘g‘imda suyaklarni bog‘laydigan tuzilma
Bosh suyagi|Miyani himoya qiladigan suyaklar majmui
Umurtqa pog‘onasi|Orqa miyani himoya qiladigan tayanch
Qovurg‘a qafasi|Ko‘krak organlarini himoya qiladigan suyak tuzilma''', 'Misol: tirsak bukilganda ayrim mushaklar qisqaradi, qarama-qarshi mushaklar bo‘shashadi. Suyak, mushak va bo‘g‘im birgalikda ishlaydi.'),
 unit('Qon aylanish va nafas olish', '''Yurak|Qonni tomirlarga haydaydigan mushak organ
Arteriya|Qonni yurakdan olib ketadigan tomir
Vena|Qonni yurakka olib keladigan tomir
Kapillyar|Modda almashish sodir bo‘ladigan juda ingichka tomir
Eritrotsit|Gemoglobin orqali kislorod tashuvchi qon hujayrasi
Leykotsit|Organizm himoyasida qatnashuvchi qon hujayrasi
Alveola|O‘pkada gaz almashadigan mayda pufakcha
Diafragma|Nafas harakatida qatnashadigan ko‘krak-qorin to‘sig‘i''', 'Misol: arteriya va vena qondagi kislorod miqdori bilan emas, oqimning yurakka nisbatan yo‘nalishi bilan farqlanadi.'),
 unit('Ovqat hazm qilish va ajratish', '''Og‘iz|Ovqat chaynash va so‘lak bilan aralashish joyi
Qizilo‘ngach|Ovqatni oshqozonga o‘tkazadigan nay
Oshqozon|Ovqatni aralashtirib hazm qilishda qatnashadigan organ
Ingichka ichak|Ozuqa moddalari asosiy so‘riladigan joy
Jigar|O‘t suyuqligini ishlab chiqaradigan organ
Oshqozonosti bezi|Hazm fermentlarini ishlab chiqaradigan bez
Buyrak|Qonni filtrlab siydik hosil qiladigan organ
Siydik pufagi|Siydikni vaqtincha yig‘adigan organ''', 'Misol: ovqat og‘iz → qizilo‘ngach → oshqozon → ichak yo‘lidan o‘tadi. Buyrak ovqat yo‘lining qismi emas, ajratish tizimi organidir.'),
 unit('Boshqaruv, sezgi va irsiyat', '''Neyron|Nerv axborotini uzatadigan hujayra
Bosh miya|Organizm boshqaruvida markaziy organ
Orqa miya|Miya bilan tana o‘rtasida axborot o‘tkazuvchi markaz
Refleks|Ta’sirga nerv tizimi orqali javob
Retseptor|Ta’sirni qabul qiladigan sezuvchi tuzilma
Gormon|Bezlardan ajraladigan kimyoviy boshqaruv moddasi
DNK|Irsiy axborot saqlanadigan molekula
Gen|DNKning irsiy axborotli qismi''', 'Misol: yorug‘lik ko‘z retseptorlariga ta’sir qiladi, nerv yo‘llari axborotni miyaga uzatadi. Nerv va gormonal boshqaruv bir-birini to‘ldiradi.'),
])
add('physics', 7, [
 unit('O‘lchash va mexanik harakat', '''Yo‘l|Jism bosib o‘tgan masofa
Vaqt|Harakat davom etish oralig‘i
O‘rtacha tezlik|Umumiy yo‘lning umumiy vaqtga nisbati
Ko‘chish|Boshlang‘ich joydan oxirgi joyga yo‘nalgan kesma
Sanoq jismi|Harakatni solishtirish uchun tanlangan jism
Metr|Uzunlikning SI birligi
Sekund|Vaqtning SI birligi
Kilogramm|Massaning SI birligi''', 'Misol: jism 120 m yo‘lni 20 s da bosib o‘tsa, o‘rtacha tezlik v=s/t=6 m/s. Boshlagan joyiga qaytsa ko‘chish nol bo‘lishi mumkin, yo‘l esa nol emas.'),
 unit('Kuch va bosim', '''Kuch|Jismlar o‘zaro ta’sirini ifodalovchi kattalik
Nyuton|Kuchning SI birligi
Og‘irlik kuchi|Yerning jismni tortish kuchi
Ishqalanish|Sirtlar nisbiy harakatiga qarshilik qiluvchi kuch
Elastiklik kuchi|Deformatsiyaga qarshi tiklovchi kuch
Bosim|Sirtga tik kuchning yuzaga nisbati
Paskal|Bosimning SI birligi
Dinamometr|Kuchni o‘lchash asbobi''', 'Misol: 20 N kuch 0.5 m² yuzaga tik ta’sir etsa, p=F/S=40 Pa. Kuch bir xil bo‘lsa, kichik yuzada bosim kattaroq bo‘ladi.'),
 unit('Ish, energiya va oddiy mexanizm', '''Mexanik ish|Kuch va uning yo‘nalishidagi ko‘chish ko‘paytmasi
Joul|Ish va energiyaning SI birligi
Quvvat|Bajarilgan ishning vaqtga nisbati
Vatt|Quvvatning SI birligi
Kinetik energiya|Harakat bilan bog‘liq energiya
Potensial energiya|Holat yoki joylashuv bilan bog‘liq energiya
Richag|Tayanch atrofida aylanadigan qattiq jism
Foydali ish koeffitsiyenti|Foydali ishning sarflangan ishga nisbati''', 'Misol: yo‘nalishdosh 10 N kuch jismni 3 m siljitsa A=30 J. Bu ish 5 s da bajarilsa P=6 W. Oddiy mexanizm energiya yaratmaydi.'),
 unit('Issiqlik va modda holati', '''Harorat|Jismning issiqlik holatini ifodalovchi kattalik
Termometr|Haroratni o‘lchash asbobi
Issiqlik o‘tkazuvchanlik|Zarralar orqali issiqlik uzatilishi
Konveksiya|Suyuqlik yoki gaz oqimi bilan issiqlik tashilishi
Nurlanish|Elektromagnit to‘lqin orqali energiya uzatilishi
Erish|Qattiq holatdan suyuq holatga o‘tish
Bug‘lanish|Suyuqlik sirtidan gaz holatiga o‘tish
Kondensatsiya|Gaz holatdan suyuq holatga o‘tish''', 'Misol: metall qoshiq issiqlikni o‘tkazadi, suv oqimlari konveksiya qiladi, Quyosh energiyasi nurlanish orqali yetib keladi.'),
])
add('physics', 8, [
 unit('Elektr zaryad va tok', '''Elektr zaryad|Elektr o‘zaro ta’sirni belgilovchi kattalik
Kulon|Zaryadning SI birligi
Elektr toki|Zaryadlarning tartibli harakati
Amper|Tok kuchining SI birligi
Kuchlanish|Birlik zaryadga to‘g‘ri keladigan elektr ish
Volt|Kuchlanishning SI birligi
Qarshilik|O‘tkazgichning tokka qarshilik ko‘rsatish kattaligi
Om|Elektr qarshilikning SI birligi''', 'Misol: tok uchun yopiq yo‘l va energiya manbai kerak. Tajribalar ilovada virtual bajariladi; maishiy elektr tarmog‘i bilan tajriba qilinmaydi.'),
 unit('Om qonuni va zanjirlar', '''Om qonuni|Tok kuchi kuchlanishning qarshilikka nisbatiga teng
Ketma-ket ulanish|Elementlar bir yo‘lda navbat bilan ulanishi
Parallel ulanish|Elementlar umumiy ikki tugun orasida ulanishi
Ampermetr|Tokni o‘lchash uchun ketma-ket ulanadigan asbob
Voltmetr|Kuchlanishni o‘lchash uchun parallel ulanadigan asbob
Yopiq zanjir|Tok o‘tishi uchun uzluksiz yo‘l
Ochiq zanjir|Tok yo‘li uzilgan holat
Qisqa tutashuv|Juda kichik qarshilikli ortiqcha tok yo‘li''', 'Misol: U=12 V, R=4 Ω bo‘lsa I=U/R=3 A. Ketma-ket ulanishda tok bir xil, parallel shoxlarda kuchlanish bir xil bo‘ladi.'),
 unit('Elektr energiya va magnit maydon', '''Elektr quvvat|Kuchlanish va tok kuchi ko‘paytmasi
Elektr ish|Quvvat va vaqt ko‘paytmasi
Kilovatt-soat|Energiya hisobida ishlatiladigan birlik
Magnit maydon|Magnit va tok ta’siri namoyon bo‘ladigan soha
Elektromagnit|Tokli g‘altak bilan hosil qilingan magnit
Kompas|Magnit maydon yo‘nalishini ko‘rsatadigan asbob
Elektr dvigatel|Elektr energiyasini mexanik harakatga aylantiruvchi qurilma
Generator|Mexanik energiyani elektr energiyasiga aylantiruvchi qurilma''', 'Misol: 100 W qurilma 2 soat ishlasa 0.2 kWh energiya sarflaydi. P=UI; A=Pt. Hisobdagi vaqt birligini quvvat birligiga moslaymiz.'),
 unit('Yorug‘lik va optik hodisalar', '''Qaytish|Yorug‘likning sirtdan orqaga tarqalishi
Sinish|Muhit chegarasida yorug‘lik yo‘nalishining o‘zgarishi
Normal|Sirtga tik o‘tkazilgan yordamchi chiziq
Tushish burchagi|Tushayotgan nur bilan normal orasidagi burchak
Qaytish burchagi|Qaytgan nur bilan normal orasidagi burchak
Yig‘uvchi linza|Parallel nurlarni fokusga yaqinlashtiradigan linza
Sochuvchi linza|Parallel nurlarni tarqatadigan linza
Spektr|Yorug‘likning ranglar bo‘yicha tarkibi''', 'Misol: qaytishda tushish va qaytish burchaklari teng; ular sirtga emas, normalga nisbatan o‘lchanadi. Linza nurlar yo‘lini o‘zgartiradi.'),
])
add('chemistry', 7, [
 unit('Modda va aralashmalar', '''Modda|Jismlarni tashkil etadigan material
Sof modda|Tarkibi muayyan bitta modda
Aralashma|Bir necha moddaning birgalikdagi to‘plami
Bir jinsli aralashma|Tarkibi ko‘zga bir xil ko‘rinadigan aralashma
Turli jinsli aralashma|Qismlari ajralib ko‘rinadigan aralashma
Filtrlash|Erimaydigan qattiq zarrachani suyuqlikdan ajratish
Bug‘latish|Erituvchini bug‘ga aylantirib ajratish
Distillash|Bug‘lanish va kondensatsiya orqali ajratish''', 'Misol: qumli suvni filtrlash mumkin; erigan tuzni oddiy filtr ushlab qolmaydi. Ajratish usulini modda xossasiga qarab tanlaymiz.'),
 unit('Atom, element va formula', '''Atom|Kimyoviy element xossalarini saqlovchi kichik zarra
Kimyoviy element|Yadrodagi proton soni bir xil atomlar turi
Molekula|Bog‘langan atomlardan tashkil topgan zarra
Kimyoviy belgi|Elementning qisqa harfli yozuvi
Formula|Modda tarkibini belgilar va indekslar bilan ko‘rsatish
Indeks|Formulada atomlar sonini ko‘rsatadigan pastki raqam
Oddiy modda|Bitta element atomlaridan tashkil topgan modda
Murakkab modda|Bir nechta element atomlaridan tashkil topgan modda''', 'Misol: H₂O da ikki vodorod va bir kislorod atomi bor; O₂ oddiy modda, H₂O murakkab modda. Formula modda tarkibini bildiradi.'),
 unit('Kimyoviy hodisa va tenglama', '''Fizik hodisa|Yangi modda hosil bo‘lmaydigan o‘zgarish
Kimyoviy hodisa|Yangi modda hosil bo‘ladigan o‘zgarish
Reagent|Reaksiyaga kirishadigan modda
Mahsulot|Reaksiya natijasida hosil bo‘ladigan modda
Koeffitsiyent|Tenglamada zarrachalar nisbatini ko‘rsatadigan old raqam
Massa saqlanishi|Yopiq tizimda reaksiya oldi va keyingi massa tengligi
Tenglashtirish|Har element atom sonini ikki tomonda teng qilish
Reaksiya belgisi|Gaz yoki cho‘kma kabi kimyoviy o‘zgarish dalili''', 'Misol: 2H₂ + O₂ → 2H₂O tenglamasida har tomonda to‘rt vodorod va ikki kislorod atomi bor. Tenglashtirishda indeks emas, koeffitsiyent o‘zgartiriladi.'),
 unit('Kislorod, vodorod va suv', '''Kislorod|Yonishni qo‘llab-quvvatlovchi O₂ gaz
Vodorod|Eng yengil elementning H₂ oddiy moddasi
Suv|H₂O formulali murakkab modda
Oksid|Ikki elementdan biri kislorod bo‘lgan birikma
Erituvchi|Boshqa modda eriydigan muhit
Erigan modda|Erituvchida tarqalgan modda
Eritma|Erituvchi va erigan moddaning bir jinsli aralashmasi
Massa ulushi|Komponent massasining jami massaga nisbati''', 'Misol: 10 g tuz va 90 g suv eritmasi 100 g bo‘ladi; tuz massa ulushi 10%. Gazlarni yoqish tajribasi bu kursda virtual tushuntiriladi.'),
])
add('chemistry', 8, [
 unit('Atom tuzilishi va davriy jadval', '''Proton|Yadrodagi musbat zaryadli zarra
Neytron|Yadrodagi elektr neytral zarra
Elektron|Manfiy zaryadli zarra
Atom raqami|Yadrodagi protonlar soni
Massa soni|Proton va neytronlar soni yig‘indisi
Izotop|Proton soni bir xil, neytron soni turlicha atom
Davr|Davriy jadvalning gorizontal qatori
Guruh|Davriy jadvalning vertikal ustuni''', 'Misol: atom raqami 6 bo‘lgan uglerodda 6 proton bor. Massa soni 12 bo‘lsa 6 neytron; neytral atomda 6 elektron bo‘ladi.'),
 unit('Kimyoviy bog‘lanish va ion', '''Kation|Musbat zaryadli ion
Anion|Manfiy zaryadli ion
Ion bog‘lanish|Qarama-qarshi zaryadli ionlarning tortishuvi
Kovalent bog‘lanish|Umumiy elektron jufti orqali bog‘lanish
Qutbsiz bog‘lanish|Umumiy elektronlar teng taqsimlanadigan bog‘lanish
Qutbli bog‘lanish|Umumiy elektronlar noteng taqsimlanadigan bog‘lanish
Elektrmanfiylik|Atomning bog‘ elektronlarini tortish qobiliyati
Kristall panjara|Zarralarning qattiq moddadagi tartibli joylashuvi''', 'Misol: Na⁺ kation, Cl⁻ anion; NaCl da ion tortishuvi mavjud. H₂ da bir xil atomlar elektron juftini teng bo‘lishadi.'),
 unit('Anorganik moddalar sinflari', '''Asosli oksid|Asosga mos keladigan metall oksidi
Kislotali oksid|Kislotaga mos keladigan oksid
Asos|Metall kationi va gidroksid guruhli birikma
Ishqor|Suvda eriydigan asos
Kislota|Eritmada vodorod ionini bera oladigan modda
Tuz|Kation va kislota qoldig‘i anionidan tuzilgan birikma
Neytrallanish|Kislota va asosdan tuz hamda suv hosil bo‘lishi
Indikator|Muhitga qarab rangini o‘zgartiradigan modda''', 'Misol: NaOH — asos va ishqor; HCl + NaOH → NaCl + H₂O neytrallanish. CO₂ kislotali oksid. Kimyoviy modda bilan mustaqil amaliy tajriba qilinmaydi.'),
 unit('Mol va miqdoriy hisob', '''Mol|Modda miqdorining SI birligi
Molyar massa|Bir mol moddaning massasi
Modda miqdori|Zarralar miqdorini mol bilan ifodalash
Avogadro doimiysi|Bir moldagi zarralar sonini ifodalovchi doimiy
Stexiometrik nisbat|Tenglama koeffitsiyentlari bildiradigan mol nisbati
Cheklovchi reagent|Avval tugab reaksiya miqdorini belgilaydigan modda
Konsentratsiya|Eritmada modda miqdorining ifodasi
Molyar konsentratsiya|Erigan modda molining eritma litriga nisbati''', 'Misol: M(H₂O)≈18 g/mol; 36 g suv n=m/M=2 mol. 1 mol modda 2 L eritmada bo‘lsa c=0.5 mol/L. Mol nisbatini massa nisbati bilan aralashtirmaymiz.'),
])
add('english', 7, [
 unit('Past simple va o‘tgan voqealar', '''I visited my aunt yesterday.|Men kecha xolamnikiga bordim.
She watched a film last night.|U kecha kechqurun film ko‘rdi.
We went to the museum.|Biz muzeyga bordik.
He did not play football.|U futbol o‘ynamadi.
Did you finish your homework?|Uy vazifangni tugatdingmi?
They bought a new book.|Ular yangi kitob sotib oldilar.
I was at home on Sunday.|Men yakshanba kuni uyda edim.
We were tired after the trip.|Biz sayohatdan keyin charchagan edik.''', 'Past simple tugagan o‘tgan ishni bildiradi. To‘g‘ri fe’lga -ed qo‘shiladi, noto‘g‘ri fe’lning alohida shakli bor. Did bilan asosiy fe’l boshlang‘ich shaklda: Did you go?'),
 unit('Reja va kelajak', '''I am going to learn chess.|Men shaxmat o‘rganmoqchiman.
She is going to visit Bukhara.|U Buxoroga bormoqchi.
We are meeting our teacher tomorrow.|Biz ertaga o‘qituvchimiz bilan uchrashyapmiz.
I will help you.|Men senga yordam beraman.
It will rain tomorrow.|Ertaga yomg‘ir yog‘adi.
They are not going to buy a car.|Ular mashina sotib olmoqchi emas.
Are you going to read this book?|Bu kitobni o‘qimoqchimisan?
We will not forget this day.|Biz bu kunni unutmaymiz.''', 'Going to niyat yoki mavjud dalilga asoslangan taxminni ifodalaydi. Present continuous kelishilgan rejaga mos. Will qaror, va’da yoki taxminda ishlatiladi; bitta shakl faqat bitta ma’noga qamalgan emas.'),
 unit('Taqqoslash va tavsif', '''This bag is lighter than that bag.|Bu sumka anavi sumkadan yengilroq.
A train is faster than a bicycle.|Poyezd velosipeddan tezroq.
This is the tallest tree here.|Bu shu yerdagi eng baland daraxt.
My room is smaller than yours.|Mening xonam senikidan kichikroq.
This task is more difficult.|Bu topshiriq qiyinroq.
This is the most interesting story.|Bu eng qiziqarli hikoya.
Today is better than yesterday.|Bugun kechagidan yaxshiroq.
This road is worse than that one.|Bu yo‘l anavi yo‘ldan yomonroq.''', 'Qisqa sifatlarda -er/-est, ko‘p uzun sifatlarda more/most ishlatiladi. Good → better → best; bad → worse → worst. Than ikki narsani solishtirishda keladi.'),
 unit('Majburiyat, maslahat va imkoniyat', '''You must wear a seat belt.|Xavfsizlik kamarini taqishing shart.
You must not touch that wire.|Anavi simga tegishing mumkin emas.
You should check your answer.|Javobingni tekshirishing kerak.
You should not waste water.|Suvni isrof qilmasliging kerak.
I can solve this puzzle.|Men bu boshqotirmani yecha olaman.
May I open the window?|Derazani ochsam maylimi?
We have to arrive on time.|Biz vaqtida yetib borishimiz zarur.
You do not have to bring a pen.|Ruchka olib kelishing shart emas.''', 'Must majburiyat, must not taqiq, do not have to esa majburiyat yo‘qligini bildiradi. Modal fe’ldan keyin asosiy fe’l odatda boshlang‘ich shaklda keladi.'),
])
add('english', 8, [
 unit('Present perfect va tajriba', '''I have visited Samarkand.|Men Samarqandga borib ko‘rganman.
She has just finished her work.|U ishini hozirgina tugatdi.
We have lived here for two years.|Biz bu yerda ikki yildan beri yashaymiz.
He has lived here since Monday.|U dushanbadan beri bu yerda yashaydi.
Have you ever seen a whale?|Hech kitni ko‘rganmisan?
They have not arrived yet.|Ular hali yetib kelishmadi.
I have already read this book.|Men bu kitobni allaqachon o‘qiganman.
She has never flown on a plane.|U hech qachon samolyotda uchmagan.''', 'Present perfect: have/has + past participle. For davomiylik, since boshlanish vaqtini bildiradi. Aniq tugagan o‘tgan vaqt bilan odatda past simple ishlatiladi: I visited it last year.'),
 unit('Shartli gaplar', '''If you heat ice, it melts.|Muzni qizdirsangiz, u eriydi.
If it rains, we will stay inside.|Yomg‘ir yog‘sa, ichkarida qolamiz.
If I study, I will pass the test.|O‘qisam, testdan o‘taman.
If she calls, I will answer.|U qo‘ng‘iroq qilsa, javob beraman.
If I had wings, I would fly.|Qanotlarim bo‘lsa edi, uchardim.
If I were you, I would ask for help.|O‘rningda bo‘lsam, yordam so‘rardim.
If we had more time, we would read.|Vaqtimiz ko‘proq bo‘lsa edi, o‘qirdik.
If he practised, he would improve.|U mashq qilsa edi, yaxshilanardi.''', 'Zero conditional umumiy hodisa: if + present, present. First conditional mumkin kelajak: if + present, will. Second conditional faraz: if + past, would. Farazdagi past har doim o‘tgan vaqt degani emas.'),
 unit('Majhul nisbat va jarayon', '''Paper is made from wood.|Qog‘oz yog‘ochdan tayyorlanadi.
The room is cleaned every day.|Xona har kuni tozalanadi.
English is spoken in many countries.|Ingliz tilida ko‘plab mamlakatlarda gaplashiladi.
The letter was sent yesterday.|Xat kecha yuborildi.
The bridge was built last year.|Ko‘prik o‘tgan yili qurildi.
These books were written in Uzbek.|Bu kitoblar o‘zbek tilida yozilgan.
The door was opened by the teacher.|Eshik o‘qituvchi tomonidan ochildi.
The results will be announced tomorrow.|Natijalar ertaga e’lon qilinadi.''', 'Passive: be + past participle. Present: is/are made; past: was/were made; future: will be made. Diqqat bajaruvchidan harakat ta’sir qilgan narsaga ko‘chadi.'),
 unit('Bog‘lovchilar va dalilli fikr', '''I stayed home because I was ill.|Kasal bo‘lganim uchun uyda qoldim.
Although it was cold, we walked.|Sovuq bo‘lsa ham sayr qildik.
I was tired, so I rested.|Charchagan edim, shuning uchun dam oldim.
I like reading, but he likes drawing.|Men o‘qishni yoqtiraman, lekin u rasm chizishni yoqtiradi.
First, collect the information.|Avval ma’lumotni to‘plang.
Then compare the sources.|Keyin manbalarni solishtiring.
For example, buses carry many people.|Masalan, avtobuslar ko‘p odam tashiydi.
In conclusion, we should save water.|Xulosa qilib, suvni tejashimiz kerak.''', 'Because sababni, so natijani, although qarama-qarshi holatni bog‘laydi. Fikr bayonida dalil va misol qo‘shamiz; manbasiz taxminni fakt deb atamaymiz.'),
])
add('russian', 2, [
 unit('Salomlashish va maktab', '''Здравствуйте!|Assalomu alaykum!
Доброе утро!|Xayrli tong!
До свидания!|Xayr!
Спасибо!|Rahmat!
Пожалуйста!|Marhamat!
учитель|o‘qituvchi
ученик|o‘quvchi
школа|maktab''', 'Salomlashishda vaziyatga mos so‘zni tanlaymiz. Misol: Доброе утро, учитель! Ruscha so‘z va o‘zbekcha ma’nosini juftlaymiz.'),
 unit('Oila va uy', '''мама|ona
папа|ota
брат|aka yoki uka
сестра|opa yoki singil
бабушка|buvi
дедушка|bobo
дом|uy
комната|xona''', 'Misol: Это моя мама. Это мой папа. Моя/мой shakli rus tilidagi ot jinsiga mos keladi.'),
 unit('Ranglar va sonlar', '''красный|qizil
синий|ko‘k
зелёный|yashil
жёлтый|sariq
один|bir
два|ikki
три|uch
четыре|to‘rt''', 'Misol: красный карандаш — qizil qalam; два карандаша — ikki qalam. Rang va sonni buyum nomiga bog‘laymiz.'),
 unit('Oddiy harakatlar va gap', '''Я читаю.|Men o‘qiyman.
Я пишу.|Men yozaman.
Я рисую.|Men rasm chizaman.
Я играю.|Men o‘ynayman.
Я иду в школу.|Men maktabga ketyapman.
Я люблю книги.|Men kitoblarni yaxshi ko‘raman.
Это мой стол.|Bu mening stolim.
Это моя книга.|Bu mening kitobim.''', 'Я — men. Gap oxirida nuqta qo‘yiladi. Misol: Я читаю книгу. Harakatni bildirgan fe’l va gap ma’nosini ajratamiz.'),
])
add('russian', 7, [
 unit('Ot, jins va kelishik', '''Именительный падеж|Кто? Что? so‘roqlariga javob bo‘lgan kelishik
Родительный падеж|Кого? Чего? so‘roqlariga javob bo‘lgan kelishik
Дательный падеж|Кому? Чему? so‘roqlariga javob bo‘lgan kelishik
Винительный падеж|Кого? Что? so‘roqlariga javob bo‘lgan kelishik
Творительный падеж|Кем? Чем? so‘roqlariga javob bo‘lgan kelishik
Предложный падеж|О ком? О чём? so‘roqlariga javob bo‘lgan kelishik
Мужской род|он olmoshi bilan mos keladigan ot jinsi
Женский род|она olmoshi bilan mos keladigan ot jinsi''', 'Misol: книга → нет книги → дать книге → читать книгу → с книгой → о книге. So‘roq bilan birga gapdagi vazifani ham hisobga olamiz; bir xil so‘roq turli kelishikda uchrashi mumkin.'),
 unit('Sifat va moslashuv', '''новый дом|yangi uy
новая книга|yangi kitob
новое окно|yangi deraza
новые друзья|yangi do‘stlar
высокая гора|baland tog‘
синее море|ko‘k dengiz
интересный рассказ|qiziqarli hikoya
зимние дни|qish kunlari''', 'Sifat otning jinsi, soni va kelishigiga moslashadi. Misol: новый дом, новая книга, новое окно, новые дома. Faqat o‘zbekcha tarjimaga qarab qo‘shimcha tanlamaymiz.'),
 unit('Fe’l zamonlari va turi', '''Я читал вчера.|Men kecha o‘qidim.
Я читаю сейчас.|Men hozir o‘qiyapman.
Я буду читать завтра.|Men ertaga o‘qiyman.
Я прочитал книгу.|Men kitobni o‘qib tugatdim.
Она писала письмо.|U xat yozayotgan edi.
Она написала письмо.|U xatni yozib tugatdi.
Мы идём в школу.|Biz maktabga boryapmiz.
Они пришли домой.|Ular uyga yetib kelishdi.''', 'Несовершенный вид jarayon yoki takrorni, совершенный вид yakunlangan natijani ifodalashi mumkin. Misol: читать — прочитать. Zamon va fe’l turini birga tekshiramiz.'),
 unit('Oddiy gap va tinish belgisi', '''Подлежащее|Gap kim yoki nima haqida ekanini bildirgan bosh bo‘lak
Сказуемое|Eganing harakati yoki holatini bildirgan bosh bo‘lak
Дополнение|Harakat bilan bog‘liq predmetni bildirgan ikkinchi bo‘lak
Определение|Predmet belgisini bildirgan ikkinchi bo‘lak
Обстоятельство|Joy, vaqt yoki usulni bildirgan ikkinchi bo‘lak
Обращение|Murojaat qilingan kishini bildirgan so‘z
Однородные члены|Bir xil so‘roqqa javob bo‘lgan teng bo‘laklar
Вопросительное предложение|Savol bildirilgan gap''', 'Misol: Мальчик читает интересную книгу вечером. Мальчик — ega, читает — kesim. Мама, послушай! gapida murojaat vergul bilan ajratiladi.'),
])
add('russian', 8, [
 unit('Qo‘shma gap va bog‘lanish', '''Сложное предложение|Ikki yoki undan ortiq grammatik asosli gap
Сочинительная связь|Teng qismlarni bog‘lash munosabati
Подчинительная связь|Bir qismni boshqasiga tobelantirish munosabati
Главная часть|Ergash qismga nisbatan bosh gap qismi
Придаточная часть|Bosh qismni izohlab keladigan ergash qism
Союз потому что|Sababni bog‘laydigan birikma
Союз если|Shartni bog‘laydigan so‘z
Союз хотя|To‘siqsizlikni bog‘laydigan so‘z''', 'Misol: Я остался дома, потому что шёл дождь. Ikki asos: я остался va дождь шёл. Sabab ergash qism bilan ifodalangan.'),
 unit('Sifatdosh va ravishdosh', '''Причастие|Harakat orqali predmet belgisini bildirgan shakl
Деепричастие|Asosiy harakatga qo‘shimcha harakatni bildirgan shakl
читающий ученик|o‘qiyotgan o‘quvchi
прочитанная книга|o‘qib chiqilgan kitob
улыбаясь|jilmayib
закончив работу|ishni tugatib
Действительное причастие|Harakatni o‘zi bajaradigan predmet belgisi
Страдательное причастие|Harakat ta’sirini olgan predmet belgisi''', 'Misol: Закончив работу, ученик отдохнул. Ikkala harakatni bir o‘quvchi bajaryapti. Деепричастный оборот odatda vergul bilan ajratiladi.'),
 unit('Ko‘chirma gap va muloqot', '''Прямая речь|Birovning so‘zini o‘zgartirmay berish
Косвенная речь|Birovning fikrini muallif gapi tarkibida berish
Слова автора|Kim gapirganini tushuntiruvchi qism
Диалог|Ikki yoki undan ortiq kishining suhbati
Реплика|Suhbatdagi bir kishining navbatdagi gapi
Кавычки|Ko‘chirma so‘zni chegaralovchi belgilar
Двоеточие|Muallif gapidan keyingi ko‘chirma gap oldi belgisi
Тире|Dialogdagi replika boshini ko‘rsatadigan belgi''', 'Misol: Учитель сказал: «Читайте внимательно». Bilvosita: Учитель сказал, чтобы мы читали внимательно. So‘z shakli va tinish belgisi tuzilishga qarab o‘zgaradi.'),
 unit('Matn, uslub va dalil', '''Тема|Matn nima haqida ekanligi
Основная мысль|Muallif yetkazmoqchi bo‘lgan asosiy fikr
Тезис|Isbotlanishi kerak bo‘lgan fikr
Аргумент|Fikrni asoslaydigan dalil
Пример|Dalilni ko‘rsatadigan aniq holat
Вывод|Tahlildan kelib chiqqan yakuniy fikr
Научный стиль|Aniqlik va atamalarga tayangan bayon
Художественный стиль|Obraz va tasvirga tayangan bayon''', 'Misol: “Чтение полезно” — tezis. O‘qish lug‘atni kengaytirishi haqidagi dalil va aniq misol bilan fikrni asoslaymiz. Mavzu bilan asosiy fikrni farqlaymiz.'),
])
add('onatili', 7, [
 unit('Mustaqil so‘z turkumlari', '''Ot|Shaxs yoki narsa nomini bildirgan so‘z turkumi
Sifat|Narsaning belgisini bildirgan so‘z turkumi
Son|Miqdor yoki tartibni bildirgan so‘z turkumi
Olmosh|Ot, sifat yoki son o‘rnida keladigan so‘z turkumi
Fe’l|Harakat yoki holatni bildirgan so‘z turkumi
Ravish|Harakatning belgisini bildirgan so‘z turkumi
Egalik qo‘shimchasi|Narsaning kimga qarashliligini bildirgan qo‘shimcha
Kelishik qo‘shimchasi|Otning boshqa so‘zga munosabatini bildirgan qo‘shimcha''', 'Misol: “Mening ikki yaxshi do‘stim tez keldi”. Do‘st — ot, ikki — son, yaxshi — sifat, tez — ravish, keldi — fe’l. So‘zning gapdagi ma’nosiga qaraymiz.'),
 unit('Fe’l shakllari', '''Bo‘lishli fe’l|Harakat bajarilishini bildirgan shakl
Bo‘lishsiz fe’l|Harakat inkorini bildirgan shakl
O‘tgan zamon|Nutqdan oldingi harakat vaqti
Hozirgi zamon|Nutq paytidagi harakat vaqti
Kelasi zamon|Nutqdan keyingi harakat vaqti
Sifatdosh|Fe’lning sifatga xos vazifada keladigan shakli
Ravishdosh|Fe’lning qo‘shimcha harakatni bildirgan shakli
Harakat nomi|Harakatni nom sifatida bildirgan shakl''', 'Misol: o‘qidi, o‘qiyapti, o‘qiydi — zamon; o‘qimadi — inkor. O‘qigan bola — sifatdosh, kulib gapirdi — ravishdosh, o‘qish foydali — harakat nomi.'),
 unit('Yordamchi so‘zlar', '''Ko‘makchi|So‘zlar orasidagi tobe munosabatni ifodalovchi yordamchi
Bog‘lovchi|So‘z yoki gaplarni bog‘laydigan yordamchi
Yuklama|So‘z yoki gapga qo‘shimcha ma’no beradigan yordamchi
Va|Teng qismlarni biriktiruvchi bog‘lovchi
Ammo|Qarama-qarshi fikrni bog‘lovchi
Chunki|Sabab munosabatini bildiruvchi bog‘lovchi
Uchun|Maqsad yoki sabab munosabatidagi ko‘makchi
Faqat|Cheklash ma’nosidagi yuklama''', 'Misol: “Men va sen”, “keldim, ammo topmadim”, “bilim olish uchun”. Yordamchi so‘zning ma’nosi va bog‘lagan qismlarini tekshiramiz.'),
 unit('So‘z ma’nosi va nutq aniqligi', '''Sinonim|Ma’nosi yaqin so‘z
Antonim|Ma’nosi qarama-qarshi so‘z
Omonim|Shakli bir xil, ma’nosi boshqa so‘z
Ko‘chma ma’no|So‘zning o‘xshashlik yoki bog‘lanish asosidagi ma’nosi
Atama|Bir sohaga oid aniq tushuncha nomi
Ibora|Yaxlit ko‘chma ma’noli turg‘un birikma
Uslub|Nutqning vaziyatga mos ifoda usuli
Tahrir|Matn xatolarini tuzatish va aniqlashtirish''', 'Misol: katta — ulkan sinonim; katta — kichik antonim. “Oltin kuz” ko‘chma tasvir. Matnni tahrirda ortiqcha takror va noaniq so‘zni almashtiramiz.'),
])
add('onatili', 8, [
 unit('So‘z birikmasi va gap', '''So‘z birikmasi|Tobe-hokim munosabatdagi mustaqil so‘zlar birligi
Hokim so‘z|Birikmada tobe so‘z bog‘langan asosiy so‘z
Tobe so‘z|Hokim so‘zni aniqlab yoki izohlab kelgan so‘z
Moslashuv|Qaratqich va egalik orqali bog‘lanish
Boshqaruv|Hokim so‘z talabiga ko‘ra kelishik yoki ko‘makchi bilan bog‘lanish
Bitishuv|Qo‘shimchasiz ma’no va tartib bilan bog‘lanish
Gap|Tugallangan fikrni bildirgan sintaktik birlik
Grammatik asos|Gapning ega va kesimdan yoki kesimdan iborat markazi''', 'Misol: “bolaning kitobi” — moslashuv; “kitobni o‘qimoq” — boshqaruv; “yaxshi kitob” — bitishuv. “Bola o‘qidi” tugallangan fikrli gapdir.'),
 unit('Gap bo‘laklari', '''Ega|Kesim bildirgan harakat yoki holat egasi
Kesim|Ega haqidagi hukmni bildirgan bosh bo‘lak
To‘ldiruvchi|Harakat bilan bog‘liq obyektni bildirgan bo‘lak
Aniqlovchi|Narsa belgisi yoki qarashliligini bildirgan bo‘lak
Hol|Harakatning joy, vaqt yoki usulini bildirgan bo‘lak
Sifatlovchi aniqlovchi|Narsaning qandayligini bildirgan aniqlovchi
Qaratqich aniqlovchi|Narsaning kimga yoki nimaga qarashliligini bildirgan aniqlovchi
Payt holi|Harakat vaqtini bildirgan hol''', 'Misol: “Ziyrak bola ertalab kitobni o‘qidi”. Bola — ega, o‘qidi — kesim, ziyrak — aniqlovchi, ertalab — hol, kitobni — to‘ldiruvchi.'),
 unit('Sodda gapning tuzilishi', '''Yig‘iq gap|Faqat bosh bo‘laklardan tuzilgan gap
Yoyiq gap|Ikkinchi darajali bo‘laklari ham bor gap
Darak gap|Xabar bildirgan gap
So‘roq gap|Savol bildirgan gap
Buyruq gap|Undash yoki buyurishni bildirgan gap
His-hayajon gap|Kuchli hissiyot bilan aytilgan gap
Uyushiq bo‘lak|Bir so‘roqqa javob berib bir vazifada kelgan teng bo‘lak
Umumlashtiruvchi so‘z|Uyushiq bo‘laklarni umumiy nom bilan bildirgan so‘z''', 'Misol: “Bahor keldi” yig‘iq; “Bugun yurtimizga bahor keldi” yoyiq. “Olma, nok va uzum pishdi” gapida meva nomlari uyushiq ega.'),
 unit('Kirish, undalma va tahrir', '''Undalma|Nutq qaratilgan shaxs yoki narsaning nomi
Kirish so‘z|So‘zlovchining fikrga munosabatini bildirgan birlik
Ajratilgan bo‘lak|Ma’nosi ta’kidlanib alohida ohang bilan berilgan bo‘lak
Ko‘chirma gap|Birovning aynan keltirilgan so‘zi
Muallif gapi|Ko‘chirma so‘z egasini yoki vaziyatini tushuntirgan qism
Vergul|Ajratish yoki sanashda ishlatiladigan tinish belgisi
Ikki nuqta|Izoh yoki ko‘chirma oldidan ishlatiladigan belgi
Mantiqiy izchillik|Fikrlar bir-biriga tushunarli bog‘lanishi''', 'Misol: “Aziz do‘stim, tingla” — undalma; “Menimcha, bu yechim to‘g‘ri” — kirish. Tahrirda gap bo‘laklarini topamiz, tinish belgilarini tuzilishga mos tekshiramiz.'),
])
READING = {}


def reading(grade, title, passage, questions):
    READING.setdefault(grade, []).append((title, passage, [r.split('|') for r in questions.strip().splitlines()]))


reading(2, 'Kutubxonadagi tanlov', 'Malika shanba kuni otasi bilan kutubxonaga bordi. U hayvonlar haqidagi kitobni tanladi. Kutubxonachi kitobni ikki haftaga berdi. Malika uyda har kuni bir sahifa o‘qidi. Tushunmagan so‘zini daftariga yozdi. Keyin bu so‘zni otasidan so‘radi. Kitobni toza saqlab, vaqtida qaytardi.', '''Kim kitob tanladi?|Malika
Qaysi kuni kutubxonaga bordi?|Shanba kuni
Kim bilan bordi?|Otasi bilan
Nima haqidagi kitobni oldi?|Hayvonlar haqida
Kitob qancha muddatga berildi?|Ikki haftaga
Har kuni qancha o‘qidi?|Bir sahifa
Tushunmagan so‘zini qayerga yozdi?|Daftariga
Kitobga qanday munosabatda bo‘ldi?|Toza saqlab, vaqtida qaytardi''')
reading(2, 'Urug‘ning o‘sishi', 'Ali bir dona loviya urug‘ini tuproqli idishga ekdi. Idishni deraza yoniga qo‘ydi. Har kuni tuproqni tekshirdi, quruq bo‘lsa ozgina suv quydi. Bir necha kundan keyin yashil nihol chiqdi. Ali nihol rasmini daftariga chizdi. U o‘simlikka qarash uchun sabr kerakligini tushundi.', '''Kim urug‘ ekdi?|Ali
Qanday urug‘ tanlandi?|Loviya
Urug‘ nimaga ekildi?|Tuproqli idishga
Idish qayerga qo‘yildi?|Deraza yoniga
Qachon suv quyildi?|Tuproq quruq bo‘lganda
Nima paydo bo‘ldi?|Yashil nihol
Ali nimani chizdi?|Nihol rasmini
U qanday xulosaga keldi?|O‘simlikka qarashda sabr kerak''')
reading(2, 'Qayta ishlatilgan quti', 'Nodira bo‘sh karton qutini tashlamadi. U qutini tozalab, tashqarisiga rangli qog‘oz yopishtirdi. Ichini ikki bo‘limga ajratdi. Bir bo‘limga qalam, ikkinchisiga o‘chirg‘ich qo‘ydi. Endi buyumlari stol ustida sochilib yotmasdi. Ukasi ham shunday quti yasashni so‘radi.', '''Qutini kim saqlab qoldi?|Nodira
Quti qaysi materialdan edi?|Karton
Bezatishdan oldin nima qildi?|Qutini tozaladi
Tashqariga nima yopishtirdi?|Rangli qog‘oz
Ichini nechta bo‘limga ajratdi?|Ikki bo‘limga
Birinchi bo‘limga nima qo‘ydi?|Qalam
Ikkinchi bo‘limga nima qo‘ydi?|O‘chirg‘ich
Ishning foydasi nima bo‘ldi?|Buyumlar tartibga keldi''')
reading(2, 'Do‘stga yordam', 'Yomg‘irli kuni Diyor maktabga soyabon bilan keldi. Darvoza oldida soyabonsiz turgan Sherzodni ko‘rdi. Diyor uni soyaboni ostiga taklif qildi. Ular yo‘lakdan ehtiyotkor yurib sinfga yetdilar. Sherzod rahmat aytdi. Diyor do‘stiga yordam berganidan xursand bo‘ldi.', '''Havo qanday edi?|Yomg‘irli
Kim soyabon olib keldi?|Diyor
Kim soyabonsiz edi?|Sherzod
Ular qayerda uchrashdi?|Darvoza oldida
Diyor nima taklif qildi?|Soyaboni ostiga kirishni
Ular qanday yurishdi?|Ehtiyotkor
Sherzod nima dedi?|Rahmat
Diyor nima uchun xursand bo‘ldi?|Do‘stiga yordam bergani uchun''')
reading(7, 'Dalil va taxmin', 'Maktab bog‘ida ikki bir xil idishga bir xil urug‘ ekildi. Bir idish yorug‘ deraza yoniga, ikkinchisi kam yorug‘ joyga qo‘yildi. Ikkalasiga bir xil miqdorda suv berildi. O‘quvchilar bo‘yini har uch kunda o‘lchadilar. Ikki haftada yorug‘ joydagi nihol yashil va baquvvat, ikkinchisi esa rangpar va cho‘zilgan bo‘ldi. Dastlab “balandroq nihol sog‘lomroq” degan taxmin aytilgan edi. Natijalar bu taxminni qo‘llamadi. O‘quvchilar faqat bo‘yga qarab sog‘lomlikni baholab bo‘lmasligini yozdilar. Ular xulosani boshqa urug‘lar bilan qayta tekshirishni taklif qildilar.', '''Tajribaning o‘zgartirilgan omili nima?|Yorug‘lik sharoiti
Qaysi shart bir xil saqlandi?|Suv miqdori
O‘lchov qachon qilindi?|Har uch kunda
Yorug‘ joydagi nihol qanday edi?|Yashil va baquvvat
Ikkinchi nihol qanday edi?|Rangpar va cho‘zilgan
Dastlabki taxmin qanday edi?|Balandroq nihol sog‘lomroq
Natija qanday xulosaga olib keldi?|Bo‘yning o‘zi sog‘lomlikni ko‘rsatmaydi
Nima uchun boshqa urug‘ bilan sinash taklif qilindi?|Xulosani qayta tekshirish uchun''')
reading(7, 'Mahalla xaritasi', 'Dilshod mahallaning eski xaritasini topdi. Unda hozirgi ko‘prik yo‘q, daryo bo‘yida esa bozor belgisi bor edi. U xaritani hozirgi joy bilan solishtirdi. Bobosi bozor ilgari daryo yonida bo‘lganini aytdi, lekin aniq yilni eslay olmadi. Dilshod bu xotirani mahalla arxividagi sana yozilgan surat bilan tekshirdi. Suratdagi bozor eski xarita belgisi bilan mos tushdi. U yozuvida bobosining taxmini bilan hujjatdagi sanani alohida ko‘rsatdi. Xarita joyni, surat esa ma’lum vaqtdagi holatni tasdiqladi.', '''Dilshod nimani topdi?|Eski xaritani
Eski xaritada nima yo‘q edi?|Hozirgi ko‘prik
Bozor qayerda ko‘rsatilgan?|Daryo bo‘yida
Bobosi nimani aniq eslay olmadi?|Yilni
Xotira qaysi manba bilan tekshirildi?|Sana yozilgan arxiv surati
Surat nimaga mos tushdi?|Xaritadagi bozor belgisiga
Taxmin va sana qanday berildi?|Alohida ko‘rsatildi
Matnning asosiy fikri nima?|Manbalarni solishtirib xulosa qilish''')
reading(7, 'Ikki yo‘lning narxi', 'Zilola uyidan maktabgacha ikki yo‘lni bilardi. Katta ko‘cha bo‘ylab yo‘l qisqaroq, ammo mashinalar ko‘p edi. Bog‘ yonidagi yo‘l biroz uzunroq bo‘lsa ham, piyodalar yo‘lagi bor edi. Bir kuni u shoshilib qisqa yo‘lni tanlamoqchi bo‘ldi. Do‘sti Madina xavfsiz o‘tish joyigacha baribir aylanib borish kerakligini eslatdi. Ular vaqtni o‘lchab, bog‘ yo‘li amalda faqat ikki daqiqa ko‘proq vaqt olishini bildilar. Keyingi kunlar oldinroq chiqishga kelishdilar. Zilola xaritadagi uzunlik bilan kundalik qulaylik har doim bir xil emasligini anglab yetdi.', '''Qisqa yo‘l qayerdan o‘tardi?|Katta ko‘chadan
Qisqa yo‘ldagi muammo nima edi?|Mashinalar ko‘pligi
Bog‘ yo‘lining afzalligi nima edi?|Piyodalar yo‘lagi borligi
Zilola nega qisqa yo‘lni tanlamoqchi bo‘ldi?|Shoshilgani uchun
Madina nimani eslatdi?|Xavfsiz o‘tish joyigacha aylanishni
Vaqt farqi qancha edi?|Ikki daqiqa
Ular qanday reja tuzdilar?|Oldinroq chiqish
Matndan qanday xulosa chiqadi?|Masofa bilan qulaylik har doim teng emas''')
reading(7, 'Kitob qaydi va xotira', 'Sardor hikoya o‘qigach, qahramon nega safarga chiqqanini do‘stiga aytdi. Do‘sti bunga boshqa sabab ko‘rsatdi. Ular bahslashish o‘rniga matnga qaytdilar. Birinchi bobda qahramon yo‘qolgan daftarni izlash niyatini aytgan edi. Keyingi bobda esa do‘stiga yordam berish uning yo‘lini o‘zgartirgan. Sardor boshlang‘ich maqsad bilan keyingi qarorni aralashtirib yuborganini tan oldi. U daftarga “voqeaga qadar”, “voqeada”, “voqeadan keyin” sarlavhalari bilan qisqa qayd yozdi. Keyingi suhbatda ular har bir fikr uchun matndan dalil keltirdilar.', '''Suhbatdagi kelishmovchilik nima haqida edi?|Safar sababi
Ular bahsni qanday hal qildilar?|Matnga qaytdilar
Boshlang‘ich maqsad nima edi?|Yo‘qolgan daftarni izlash
Keyingi qarorga nima ta’sir qildi?|Do‘stiga yordam berish
Sardor nimani aralashtirdi?|Maqsad va keyingi qarorni
Qayd qanday tuzildi?|Voqea bosqichlari bo‘yicha
Keyingi suhbatda nima keltirildi?|Matndan dalil
Qaydning foydasi nima?|Voqealar va sabablarni ajratish''')
reading(8, 'Raqam ortidagi savol', 'Maktab gazetasi “O‘quvchilarning ko‘pchiligi velosipedni afzal ko‘radi” degan sarlavha yozdi. So‘rov sport to‘garagidagi yigirma o‘quvchidan olingan, ulardan o‘n to‘rttasi velosipedni tanlagan edi. Muharrir Nargiza natija shu guruhga tegishli ekanini aytdi. Boshqa sinflar va uzoqda yashovchilar so‘ralmagan edi. Muallif sarlavhani “So‘ralgan sport to‘garagi a’zolarining ko‘pchiligi velosipedni tanladi” deb tuzatdi. Keyin turli sinflardan ishtirokchilar yig‘ishni rejaladi. Raqam o‘zgarmadi, lekin da’voning chegarasi aniqlandi.', '''So‘rov kimlardan olingan?|Sport to‘garagi a’zolaridan
Nechta ishtirokchi so‘ralgan?|Yigirma
Nechtasi velosipedni tanlagan?|O‘n to‘rt
Dastlabki sarlavhadagi muammo nima?|Guruh natijasi hammaga yoyilgan
Kim chegarani ko‘rsatdi?|Nargiza
Kimlar so‘ralmagan?|Boshqa sinflar va uzoqda yashovchilar
Sarlavha qanday tuzatildi?|So‘ralgan guruh aniq aytildi
Asosiy xulosa nima?|Raqamning qamrovini ham tekshirish kerak''')
reading(8, 'Ustaxona va meros', 'Hunarmand buva nabirasiga eski sandiqning naqshini ko‘rsatdi. Nabira naqshni telefonga suratga olib, yangi qalamdon bezagiga moslashtirmoqchi bo‘ldi. Buva ruxsat berdi, ammo shakl nega takrorlanishini avval tushunishni so‘radi. U naqshda markaz va chetlar muvozanatini ko‘rsatdi. Nabira aynan nusxa ko‘chirmay, shu tamoyilni kichik buyumga qo‘lladi. Taqdimotda naqsh manbasini va o‘z o‘zgarishini aytdi. Buva yangi buyum eski naqshning tarixini eslatib turganidan mamnun bo‘ldi.', '''Naqsh qaysi buyumda edi?|Eski sandiqda
Nabira nimani bezamoqchi edi?|Qalamdonni
Buva avval nimani tushunishni so‘radi?|Takrorlanish sababini
Qaysi tamoyil ko‘rsatildi?|Markaz va chetlar muvozanati
Nabira qanday ishladi?|Tamoyilni yangi buyumga moslashtirdi
Taqdimotda nima aytildi?|Manba va o‘z o‘zgarishi
Buva nega mamnun bo‘ldi?|Naqsh tarixi eslatilgani uchun
Matnning asosiy fikri nima?|Merosni tushunib ijodiy davom ettirish''')
reading(8, 'Bog‘ haqida ikki xat', 'Mahalla bog‘ida yangi yo‘lak qurish taklif qilindi. Birinchi xat muallifi yomg‘irda loy bo‘ladigan yo‘ldan keksalar qiynalayotganini yozdi. Ikkinchi xat muallifi daraxt ildizlari shikastlanishi mumkinligini eslatdi. Yig‘ilishda ikkala xat ham o‘qildi. Mutaxassis ildizlardan uzoqroq yo‘nalish va suvni o‘tkazadigan qoplama taklif etdi. Reja nafaqat yo‘lak uzunligi, balki daraxtlar holati va yurish qulayligi bilan ham baholanadigan bo‘ldi. Mualliflar turli xavfni ko‘rsatgan bo‘lsalar ham, ikkalasi bog‘dan yaxshi foydalanishni istardi.', '''Birinchi xatdagi muammo nima?|Yomg‘irdagi loy yo‘l
Kimlar qiynalayotgani aytildi?|Keksalar
Ikkinchi xatda qanday xavf aytildi?|Ildizlar shikastlanishi
Kim muqobil yechim berdi?|Mutaxassis
Yo‘nalish qanday tanlandi?|Ildizlardan uzoqroq
Qanday qoplama taklif qilindi?|Suvni o‘tkazadigan
Reja nimaga qarab baholanadi?|Daraxt holati va yurish qulayligi ham hisobga olinadi
Ikki xatni nima birlashtiradi?|Bog‘dan yaxshi foydalanish istagi''')
reading(8, 'Tajriba natijasini e’lon qilish', 'O‘quvchilar qog‘oz ko‘prik modelining ikkita shaklini sinadilar. Birinchi model ko‘proq yuk ko‘tardi. Dastlab guruh uni “har doim eng mustahkam” deb atamoqchi bo‘ldi. Hisobotni yozgan Kamol birinchi modelga qalinroq qog‘oz sarflanganini payqadi. U shakl bilan material birga o‘zgarganini yozdi. Guruh ikkala modelni bir xil qog‘oz va bir xil tayanch oralig‘ida qayta sinadi. Natijani jadvalga kiritib, aynan shu sharoitdagi xulosani e’lon qildi. Kamol kamchilikni ochiq yozish hisobotni kuchsizlantirmasdan, tekshirishga yordam berishini tushuntirdi.', '''Nima sinovdan o‘tkazildi?|Ikki qog‘oz ko‘prik shakli
Dastlab qaysi model ko‘proq yuk ko‘tardi?|Birinchi model
Dastlabki da’vo qanday edi?|Har doim eng mustahkam
Kamol qanday farqni payqadi?|Qog‘oz qalinligi farqini
Sinovdagi muammo nima?|Shakl va material birga o‘zgargan
Qayta sinovda nimalar tenglashtirildi?|Qog‘oz va tayanch oralig‘i
Natijalar qayerga kiritildi?|Jadvalga
Kamchilikni yozishning foydasi nima?|Hisobotni tekshirishga yordam beradi''')

TITLES = {
 'informatics':L('Informatika','Computing','Информатика'),
 'geography':L('Geografiya','Geography','География'),
 'biology':L('Biologiya','Biology','Биология'),
 'physics':L('Fizika','Physics','Физика'),
 'chemistry':L('Kimyo','Chemistry','Химия'),
 'english':L('Ingliz tili','English','Английский язык'),
 'russian':L('Rus tili','Russian','Русский язык'),
 'onatili':L('Ona tili','Native language','Родной язык'),
 'reading':L('O‘qish va matn tahlili','Reading and text analysis','Чтение и анализ текста'),
}


def write_course(subject, grade, units, reading_mode=False):
    course = Course(subject, grade, TITLES[subject])
    keys = []
    for n, data in enumerate(units, 1):
        if reading_mode:
            title, passage, pairs = data
            assert len(pairs) == 8 and len({b for _,b in pairs}) == 8, title
            theory = 'Matnni diqqat bilan o‘qing. Javobni matndagi dalil bilan tekshiring; voqea, sabab va xulosani ajrating.\n\n' + passage
            note = ''
        else:
            title, pairs, note = data
            passage = None
            theory = 'Qoida va tushunchalar: ' + '; '.join(f'{a} — {b}' for a,b in pairs) + '.\n\n' + note + '\nMashqda tushunchani ta’rif yoki misol bilan bog‘lang va javob izohini o‘qing.'
        items = []
        for i, (left,right) in enumerate(pairs):
            wrong = [b for j,(_,b) in enumerate(pairs) if j != i][:3]
            explanation = f'Matnda berilgan javob: {right}.' if reading_mode else f'{left} — {right}. {note}'
            items.append(Q(left if reading_mode else f'«{left}» uchun mos ma’noni tanlang.',right,wrong,x=explanation,h=explanation,text=passage))
            if reading_mode:
                true = i % 2 == 0
                proposed = right if true else pairs[(i+1)%8][1]
                items.append(TF(f'Matnga ko‘ra «{left}» savolining javobi «{proposed}».',true,d=2,x=explanation,h=explanation,text=passage))
            else:
                items.append(Q(f'«{right}» qaysi tushuncha yoki iboraga mos?',left,[a for j,(a,_) in enumerate(pairs) if j != i][:3],d=2,x=explanation,h=explanation))
        if not reading_mode:
            for label, subset in [('Asosiy tushunchalar',pairs[:4]),('Mavzuni mustahkamlash',pairs[4:])]:
                items.append(MATCH(f'{title}: {label.lower()}ni moslang.',subset,x='; '.join(f'{a} — {b}' for a,b in subset),h=note))
        key = f'unit{n}'
        keys.append(key)
        chapter = f'{n}-chorak. {title}'
        course.topic(key,'📖' if reading_mode else '💡',L(title,title,title),chapter=chapter,theory=theory,items=items)
        course.test(f'test{n}',L(f'{n}-nazorat ishi',f'Test {n}',f'Контрольная работа {n}'),[key],chapter=chapter,size=8)
    course.test('final',L('Yakuniy takrorlash','Final review','Итоговое повторение'),keys,chapter='Yakuniy takrorlash',size=12)
    course.write()


def build():
    for (subject,grade), units in DATA.items():
        write_course(subject,grade,units)
    for grade,units in READING.items():
        write_course('reading',grade,units,True)
    assert len(DATA)+len(READING) == 22


if __name__ == '__main__':
    build()
