# "🏠 Ota-ona bilan bajaramiz" (Montessori uslubidagi ekrandan tashqari faoliyatlar) va
# "🤝 Muloqot" (hislar, sehrli so'zlar, yaxshi do'st, xavfsizlik) ma'lumotlari.
# `python3 tool/content/family_social_src.py` -> assets/data/montessori.json, social.json
#
# Barcha matnlar original. Metodik asos: kundalik hayot mashqlari, sezgi materiallari,
# "boshqaruvni bolaga ber" tamoyili (Montessori), ijtimoiy-emotsional ta'lim (SEL).
import json, os

DATA = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data")

def A(id, age, area, emoji, title, minutes, materials, steps, benefit):
    return {"id": id, "age": age, "area": area, "emoji": emoji, "title": title, "minutes": minutes,
            "materials": materials, "steps": steps, "benefit": benefit}

ACTIVITIES = [
 # ---------------------------------------------------------------- 4 yosh: kundalik hayot
 A("pour_water", 4, "life", "💧", "Suv quyamiz", 10, ["2 ta kichik plastik stakan", "suv", "sochiq"],
   ["Bitta stakanni yarmigacha suv bilan to‘ldiring.", "Suvni qanday sekin quyishni bir marta ko‘rsating.",
    "Bola suvni bir stakandan ikkinchisiga to‘kmasdan quysin.", "To‘kilgan tomchilarni birga sochiq bilan arting."],
   "Qo‘l harakatining aniqligi, diqqat va “o‘zim qila olaman” degan ishonch."),
 A("spoon_transfer", 4, "life", "🥄", "Qoshiqda tashiymiz", 10, ["2 ta kosa", "qoshiq", "katta loviya yoki yong‘oq"],
   ["Loviyalarni bitta kosaga soling.", "Qoshiq bilan bittadan olib, ikkinchi kosaga o‘tkazishni ko‘rsating.",
    "Bola hammasini o‘tkazsin, keyin orqaga qaytarsin.", "Oxirida loviyalarni birga sanang."],
   "Mayda motorika va chapdan o‘ngga ishlash odati (yozishga tayyorgarlik). Kichik narsalarni og‘izga solmasligini kuzating."),
 A("buttons", 4, "life", "👕", "Tugma qadaymiz", 10, ["katta tugmali kofta yoki ko‘ylak"],
   ["Koftani stolga yoyib qo‘ying.", "Bitta tugmani sekin qadab, keyin yechib ko‘rsating.",
    "Bola pastdagi tugmadan boshlab o‘zi qadasin.", "Hammasi qadalgach, birga maqtang va kiyib ko‘rsin."],
   "Barmoqlar kuchi, sabr va kiyinishda mustaqillik."),
 A("socks_pairs", 4, "life", "🧦", "Paypoqlarni juftlaymiz", 10, ["5–6 juft har xil paypoq", "savat"],
   ["Paypoqlarni aralashtirib savatga soling.", "Bitta paypoqni olib, juftini qidirishni ko‘rsating.",
    "Bola hamma juftlarni topsin va yonma-yon qo‘ysin.", "Juftlarni o‘rab, javonga birga joylang."],
   "Rang va naqshni solishtirish (diqqat) hamda uy ishlariga qatnashish."),
 A("water_plant", 4, "life", "🌱", "Gulni sug‘oramiz", 5, ["kichik suv idishi", "uydagi gul"],
   ["Gul tuprog‘ini barmoq bilan ushlab ko‘ring: quruqmi?", "Idishga ozgina suv to‘ldiring.",
    "Bola suvni gul tagiga sekin quysin.", "Har kuni bitta vaqtda gulni birga kuzating."],
   "Mas’uliyat, tirik tabiatga g‘amxo‘rlik va kun tartibi."),
 A("set_table", 4, "life", "🍽️", "Dasturxonga yordam", 10, ["plastik likopchalar", "qoshiqlar", "salfetkalar"],
   ["Oila a’zolari nechta ekanini birga sanang.", "Har bir kishi uchun bitta likopcha qo‘yishni ko‘rsating.",
    "Bola likopcha yoniga qoshiq va salfetka qo‘ysin.", "Ovqatdan keyin likopchalarni birga yig‘ing."],
   "Sanash (birga-bir moslik), tartib va oilaga foydali bo‘lish quvonchi."),
 # ---------------------------------------------------------------- 4 yosh: sezgi
 A("color_sort", 4, "senses", "🎨", "Ranglarni saralaymiz", 10, ["rangli qalamlar yoki koptoklar", "3 ta kosa"],
   ["Har bir kosaga bitta rangni belgilang (qizil, sariq, ko‘k).", "Bitta narsani olib, rangini aytib, kosaga soling.",
    "Bola qolganlarini rang bo‘yicha saralasin.", "Ranglarni birga uch tilda ayting."],
   "Ranglarni ajratish, saralash (mantiq) va so‘z boyligi."),
 A("big_small", 4, "senses", "📦", "Kattadan kichikka", 10, ["o‘lchami har xil 4–5 ta quti yoki idish"],
   ["Qutilarni aralash qo‘ying.", "Eng kattasini topib, birinchi qo‘yishni ko‘rsating.",
    "Bola qolganlarini kattadan kichikka tersin.", "Keyin kichikdan kattaga qayta tering."],
   "O‘lchamni taqqoslash — matematik tafakkurning boshlanishi."),
 A("mystery_bag", 4, "senses", "👜", "Sirli xalta", 10, ["mato xalta", "tanish narsalar: qoshiq, to‘p, kubik, qalam"],
   ["Narsalarni bola ko‘rmasdan xaltaga soling.", "Bola qo‘lini xaltaga solib, bitta narsani ushlab ko‘rsin.",
    "Ko‘rmasdan nima ekanini topib aytsin.", "Chiqarib, to‘g‘ri topganini birga tekshiring."],
   "Sezgi (teginish), tasavvur va narsalarni ta’riflash nutqi."),
 A("sound_jars", 4, "senses", "🔔", "Tovushli idishlar", 10, ["4 ta yopiq idish", "guruch", "tugmalar"],
   ["Ikki idishga guruch, ikkitasiga tugma soling va yoping.", "Idishlarni silkitib, tovushini tinglang.",
    "Bola bir xil tovushli idishlarni juftlasin.", "Ochib, ichini ko‘rib tekshiring."],
   "Eshitish diqqati va tovushlarni farqlash — o‘qishga tayyorgarlik."),
 A("smell_game", 4, "senses", "🍋", "Hidini top", 5, ["limon", "olma", "yalpiz yoki dolchin"],
   ["Mevalarni bola bilan hidlab ko‘ring.", "Bola ko‘zini yumsin.", "Birini hidlatib, nima ekanini topsin.",
    "Hidlarni so‘z bilan ta’riflang: nordon, shirin, yoqimli."],
   "Sezgi a’zolari bilan tanishish va so‘z boyligi."),
 # ---------------------------------------------------------------- 4 yosh: matematika, til, tabiat, harakat
 A("count_spoons", 4, "math", "🔢", "Sanaymiz: 1 dan 5 gacha", 10, ["5 ta qoshiq", "1–5 raqamli kartochkalar"],
   ["Kartochkalarni tartib bilan qo‘ying.", "“1” yoniga bitta qoshiq qo‘yishni ko‘rsating.",
    "Bola har bir raqam yoniga shuncha qoshiq qo‘ysin.", "Barmoq bilan ko‘rsatib, birga sanang."],
   "Son va miqdorni bog‘lash — maktab matematikasi asosi."),
 A("home_words", 4, "language", "🏠", "Uyimizdagi narsalar", 10, ["uydagi narsalar"],
   ["Xonada yurib, narsani ko‘rsating va nomini ayting.", "Bola nomini takrorlasin.",
    "Endi siz nomini ayting — bola o‘sha narsani topsin.", "Bir nechta narsani ruscha va inglizcha ham ayting."],
   "So‘z boyligi va eshitib tushunish."),
 A("story_book", 4, "language", "📖", "Rasmga qarab ertak", 15, ["rasmli kitob"],
   ["Kitobning rasmlarini birga ko‘ring.", "“Bu yerda kim bor? Nima qilyapti?” deb so‘rang.",
    "Bola o‘z so‘zlari bilan aytib bersin.", "Oxirida eng yoqqan rasmni tanlasin."],
   "Nutq, tasavvur va kitobga mehr."),
 A("leaf_walk", 4, "nature", "🍂", "Barglarni yig‘amiz", 20, ["sayr", "kichik savat"],
   ["Hovli yoki bog‘da sayr qiling.", "Har xil barglarni yig‘ing.", "Uyda ularni kattaligi va rangi bo‘yicha tering.",
    "Eng katta va eng kichik bargni birga toping."],
   "Tabiatni kuzatish, taqqoslash va toza havoda harakat."),
 A("weather", 4, "nature", "☀️", "Bugun havo qanday?", 5, ["deraza"],
   ["Ertalab derazadan birga qarang.", "Quyosh bormi, bulutmi, yomg‘irmi — bola aytsin.",
    "Havoga mos kiyimni birga tanlang.", "Kechqurun havo o‘zgardimi — yana qarang."],
   "Kuzatuvchanlik va sabab-oqibat (havo → kiyim)."),
 A("clap_rhythm", 4, "movement", "👏", "Qarsak ritmi", 5, ["hech narsa kerak emas"],
   ["Oddiy ritm chaling: qarsak-qarsak-pauza.", "Bola takrorlasin.", "Ritmni asta murakkablashtiring.",
    "Endi bola ritm chalsin — siz takrorlang."],
   "Eshitish xotirasi, diqqat va navbat bilan harakat qilish."),
 A("balance_line", 4, "movement", "🚶", "Chiziq ustida yuramiz", 10, ["polga yopishtiriladigan lenta"],
   ["Polga 2–3 metrlik lenta yopishtiring.", "Chiziq ustida sekin yurishni ko‘rsating.",
    "Bola qo‘llarini yonga yoyib yursin.", "Keyin qo‘lida qoshiqda to‘p bilan yurib ko‘rsin."],
   "Muvozanat, tana nazorati va diqqat."),
 A("playdough", 4, "art", "✋", "Plastilindan shakllar", 15, ["plastilin yoki uyda tayyorlangan xamir"],
   ["Xamirdan shar yasashni ko‘rsating.", "Bola kaftlari orasida shar va uzun “ilon” yasasin.",
    "Shardan quyosh, ilondan uning nurlarini yasang.", "Yasalgan shaklni birga nomlang."],
   "Barmoq va kaft muskullari — qalam ushlashga tayyorgarlik."),
 A("helper_clean", 4, "life", "🧸", "O‘yinchoqlarni joyiga qo‘yamiz", 10, ["o‘yinchoqlar", "qutilar"],
   ["O‘yin tugagach, qutilarni ochib qo‘ying.", "Kubiklar — bir qutiga, mashinalar — boshqasiga.",
    "Bola o‘yinchoqlarni turi bo‘yicha joylasin.", "Tartibli xonani birga ko‘rib, maqtang."],
   "Tartib, saralash va mas’uliyat."),
 # ---------------------------------------------------------------- 6 yosh: kundalik hayot
 A("sandwich", 6, "life", "🥪", "Buterbrod tayyorlaymiz", 15, ["non", "sariyog‘ yoki pishloq", "o‘tmas plastik pichoq", "taxtacha"],
   ["Qo‘llarni birga yuving.", "Nonga sariyog‘ surtishni ko‘rsating.", "Bola o‘zi surtsin va pishloq qo‘ysin.",
    "Buterbrodni ikki bo‘lakka bo‘lib, birini oila a’zosiga taklif qilsin."],
   "Mustaqillik, ketma-ketlikni rejalash va “yarim” tushunchasi."),
 A("shoe_laces", 6, "life", "👟", "Bog‘ich bog‘lashni o‘rganamiz", 15, ["bog‘ichli oyoq kiyim yoki karton"],
   ["Oyoq kiyimni stolga qo‘ying.", "Birinchi tugunni sekin ko‘rsating.", "“Quloqchalar” yasab, ularni bog‘lashni ko‘rsating.",
    "Bola bir necha marta mashq qilsin — shoshilmang."],
   "Barmoqlar koordinatsiyasi va sabr."),
 A("tidy_room", 6, "life", "🧹", "Xonani tartibga keltiramiz", 15, ["rangli stikerlar yoki kartochkalar"],
   ["Xonada 3 ta vazifa belgilang: kitoblar, o‘yinchoqlar, kiyimlar.", "Bola qaysi biridan boshlashni tanlasin.",
    "Har bir vazifa tugagach, kartochkani belgilasin.", "Oxirida tartibli xonani suratga emas, xotiraga olib, birga quvonishing."],
   "Rejalash, vazifani oxiriga yetkazish va mustaqillik."),
 A("bean_sprout", 6, "nature", "🌱", "Loviya o‘stiramiz", 10, ["shaffof stakan", "paxta yoki salfetka", "2–3 ta loviya", "suv"],
   ["Stakanga namlangan paxta soling.", "Loviyalarni stakan devoriga yaqin qo‘ying.", "Har kuni bir oz suv qo‘shing.",
    "Bir hafta davomida o‘sishini kuzating va rasmini chizing."],
   "Kuzatish, sabr va tirik tabiat qanday o‘sishini tushunish."),
 # ---------------------------------------------------------------- 6 yosh: fan va sezgi
 A("sink_float", 6, "science", "🛁", "Suzadimi yoki cho‘kadimi?", 15, ["katta idishda suv", "qoshiq", "po‘kak", "tanga", "yog‘och kubik", "olma"],
   ["Har bir narsani suvga solishdan oldin bola taxmin qilsin: suzadimi?", "Narsani sekin suvga qo‘ying.",
    "Natijani ikki guruhga ajrating: suzadi / cho‘kadi.", "Qaysi taxminlar to‘g‘ri chiqdi — birga sanang."],
   "Taxmin qilish, tajriba va natijani tekshirish — ilmiy fikrlash."),
 A("magnet", 6, "science", "🧲", "Magnit nimani tortadi?", 15, ["magnit", "qisqich", "qog‘oz", "qalam", "kalit", "plastik o‘yinchoq"],
   ["Narsalarni stolga tering.", "Bola taxmin qilsin: magnit tortadimi?", "Magnitni har biriga yaqinlashtiring.",
    "“Tortadi” va “tortmaydi” guruhlarini tuzing."],
   "Tajriba orqali o‘rganish va saralash."),
 A("shadow_play", 6, "science", "🔦", "Soya o‘yini", 15, ["fonar", "devor", "qo‘llar yoki o‘yinchoqlar"],
   ["Xonani biroz qorong‘ilating.", "Fonar bilan devorga qo‘l soyasini tushiring.",
    "Qo‘lni yaqinlashtirib-uzoqlashtiring: soya qanday o‘zgaradi?", "Bola qo‘llari bilan quyon yoki qush soyasini yasasin."],
   "Yorug‘lik va soya haqida ilk tushuncha, ijodkorlik."),
 A("ice_melt", 6, "science", "❄️", "Muz qayerda tez eriydi?", 20, ["3 ta muz bo‘lagi", "3 ta likopcha"],
   ["Muzlarni likopchalarga qo‘ying.", "Birini quyoshga, birini soyaga, birini xonaga qo‘ying.",
    "Bola taxmin qilsin: qaysi biri tez eriydi?", "15 daqiqadan keyin birga tekshiring."],
   "Taqqoslash, vaqt va harorat haqida tushuncha."),
 # ---------------------------------------------------------------- 6 yosh: matematika
 A("shop_game", 6, "math", "🛒", "Do‘kon o‘yini", 20, ["o‘yinchoq yoki mevalar", "narx yozilgan kartochkalar (1–10)", "o‘yin tangalari"],
   ["Narsalarga 1 dan 10 gacha narx qo‘ying.", "Bola sotuvchi, siz xaridor bo‘ling.", "Tangalarni sanab to‘lang.",
    "Keyin rollarni almashtiring — bola sanab to‘lasin."],
   "10 gacha qo‘shish, sanash va muloqot odobi."),
 A("measure_steps", 6, "math", "📏", "Qadamlab o‘lchaymiz", 10, ["xona"],
   ["Xonaning uzunligini qadamlab o‘lchang.", "Bola o‘z qadamlari bilan o‘lchasin.", "Kimniki ko‘proq qadam chiqdi — nega?",
    "Stol va gilamni ham o‘lchab, taqqoslang."],
   "O‘lchash tushunchasi va taqqoslash."),
 A("daily_clock", 6, "math", "🕰️", "Kun tartibimiz", 15, ["qog‘oz", "rangli qalamlar"],
   ["Kun davomidagi 4–5 ishni birga eslang: uyg‘onish, nonushta, o‘yin, uyqu.", "Har birini rasm qilib chizing.",
    "Rasmlarni tartib bilan tering.", "Soatda uyg‘onish va uxlash vaqtini ko‘rsating."],
   "Vaqt, ketma-ketlik va kun tartibi."),
 A("shape_hunt", 6, "math", "🔺", "Uydagi shakllar ovi", 15, ["uydagi narsalar"],
   ["Doira, kvadrat, uchburchak, to‘rtburchak shakllarini eslang.", "Uyda shu shakldagi narsalarni qidiring.",
    "Har bir shakl uchun kamida 2 ta narsa toping.", "Qaysi shakl ko‘p uchradi — sanang."],
   "Geometrik shakllarni hayotda ko‘rish."),
 # ---------------------------------------------------------------- 6 yosh: til
 A("letter_hunt", 6, "language", "🔤", "Harf ovi", 10, ["uydagi narsalar"],
   ["Bir harfni tanlang, masalan “M”.", "Uyda shu harf bilan boshlanadigan narsalarni qidiring.",
    "Har bir topilgan narsa nomini bo‘g‘inlab ayting.", "Ertaga boshqa harf bilan o‘ynang."],
   "Tovush-harf bog‘lanishi va bo‘g‘inlab o‘qishga tayyorgarlik."),
 A("picture_story", 6, "language", "📚", "Rasmlardan hikoya", 15, ["3–4 ta rasm yoki jurnal qirqimlari"],
   ["Rasmlarni aralash qo‘ying.", "Bola ularni hikoya tartibida tersin.", "Hikoyani boshidan oxirigacha aytib bersin.",
    "Hikoyaga nom qo‘ying."],
   "Izchil nutq, ketma-ketlik va tasavvur."),
 A("letter_to_grandma", 6, "language", "✉️", "Buvijonga rasmli xat", 20, ["qog‘oz", "rangli qalamlar", "konvert"],
   ["Buvi yoki bobo uchun rasm chizing.", "Bola bitta so‘z yoki ismini yozishga harakat qilsin.",
    "Xatni konvertga solib, birga olib boring yoki berib yuboring.", "Buvining javobini birga tinglang."],
   "Yozishga qiziqish, oilaviy mehr va muloqot."),
 A("three_langs", 6, "language", "🌍", "Uch tilda o‘yin", 10, ["uydagi narsalar"],
   ["Narsani ko‘rsating: bola uni o‘zbekcha aytsin.", "Keyin ruscha va inglizcha ayting — bola takrorlasin.",
    "Endi siz inglizcha ayting — bola narsani topsin.", "Har kuni 3 ta yangi so‘z."],
   "Uch tilda so‘z boyligi va eshitib tushunish."),
 # ---------------------------------------------------------------- 6 yosh: ijod, harakat, oila
 A("paper_boat", 6, "art", "⛵", "Qog‘ozdan qayiq", 15, ["A4 qog‘oz", "suv to‘ldirilgan tog‘ora"],
   ["Qog‘ozni buklashni bosqichma-bosqich ko‘rsating.", "Bola har bir bosqichni takrorlasin.",
    "Qayiqni suvga qo‘yib, suzishini kuzating.", "Qayiqqa ism qo‘ying."],
   "Ko‘rsatma bo‘yicha ishlash, mayda motorika va sabr."),
 A("home_orchestra", 6, "art", "🥁", "Uy orkestri", 15, ["qopqoqli idishlar", "qoshiqlar", "guruch solingan shisha"],
   ["Uydagi narsalardan “cholg‘u” yasang.", "Tanish qo‘shiq uchun ritm chaling.", "Tez va sekin, baland va past chalib ko‘ring.",
    "Oila uchun kichik konsert bering."],
   "Ritm hissi, eshitish va o‘ziga ishonch."),
 A("morning_exercise", 6, "movement", "🤸", "Ertalabki mashq", 10, ["qulay kiyim"],
   ["Birga 10 marta sakrang.", "Qo‘llarni yuqoriga cho‘zib, 5 gacha sanang.", "Bir oyoqda 5 soniya turing.",
    "Oxirida chuqur nafas olib, bir-biringizni maqtang."],
   "Sog‘lom odat, muvozanat va sanash."),
 A("family_help", 6, "life", "🤝", "Oilaga yordam", 15, ["kundalik uy ishlari"],
   ["Bugun bola oilaga qanday yordam berishini birga tanlang.", "Masalan: non olib kelish, gul sug‘orish, dasturxon yig‘ish.",
    "Ishni tugatgach, oila a’zolari rahmat aytsin.", "Kechqurun “bugun kimga yordam berdim?” deb eslang."],
   "G‘amxo‘rlik, mas’uliyat va oilaviy qadriyatlar."),
 A("safety_talk", 6, "life", "🏡", "Xavfsizlik qoidalari", 10, ["hech narsa kerak emas"],
   ["Adashib qolsa nima qilishni gaplashing: joyida turish va kattalardan yordam so‘rash.",
    "Ota-onasining ismini to‘liq aytishni mashq qiling.", "Begona odam bilan hech qayoqqa ketmaslikni tushuntiring.",
    "Savol-javob o‘yini qilib, qoidalarni takrorlang."],
   "Xavfsizlik ko‘nikmalari va o‘ziga ishonch."),
]

# ---------------------------------------------------------------- Muloqot
EMOTIONS = [
 {"id": "happy", "emoji": "😀", "uz": "xursand", "en": "happy", "ru": "радостный"},
 {"id": "sad", "emoji": "😢", "uz": "xafa", "en": "sad", "ru": "грустный"},
 {"id": "angry", "emoji": "😠", "uz": "jahli chiqqan", "en": "angry", "ru": "сердитый"},
 {"id": "scared", "emoji": "😨", "uz": "qo‘rqqan", "en": "scared", "ru": "испуганный"},
 {"id": "surprised", "emoji": "😲", "uz": "hayron", "en": "surprised", "ru": "удивлённый"},
 {"id": "tired", "emoji": "😩", "uz": "charchagan", "en": "tired", "ru": "уставший"},
 {"id": "calm", "emoji": "😌", "uz": "xotirjam", "en": "calm", "ru": "спокойный"},
 {"id": "shy", "emoji": "😳", "uz": "uyalgan", "en": "shy", "ru": "смущённый"},
]

def S(id, scene, text, emotion, age=4):
    return {"id": id, "scene": scene, "text": text, "emotion": emotion, "age": age}

SITUATIONS = [
 S("gift", ["🎁", "🙂"], "Do‘sting senga sovg‘a berdi. Qanday his qilasan?", "happy"),
 S("broken_toy", ["🧸", "💔"], "Sevimli o‘yinchog‘ing sinib qoldi. Qanday his qilasan?", "sad"),
 S("thunder", ["⛈️", "🌃"], "Kechasi qattiq momaqaldiroq bo‘ldi. Qanday his qilasan?", "scared"),
 S("magic", ["🎩", "🐰"], "Sehrgar qalpoqdan quyon chiqardi. Qanday his qilasan?", "surprised"),
 S("birthday", ["🎂", "🎈"], "Bugun tug‘ilgan kuning! Qanday his qilasan?", "happy"),
 S("long_run", ["🏃", "💦"], "Uzoq yugurding, oyoqlaring toliqdi. Qanday his qilasan?", "tired"),
 S("friend_left", ["👋", "🚗"], "Do‘sting boshqa shaharga ko‘chib ketdi. Qanday his qilasan?", "sad"),
 S("toy_taken", ["🚂", "✋"], "Kimdir o‘yinchog‘ingni so‘ramasdan oldi. Qanday his qilasan?", "angry", 6),
 S("new_group", ["🏫", "👥"], "Yangi guruhga keldingi, hech kimni tanimaysan. Qanday his qilasan?", "shy", 6),
 S("bedtime_story", ["📖", "🛏️"], "Onang ertak o‘qib berdi, yotishga tayyorsan. Qanday his qilasan?", "calm", 6),
 S("big_dog", ["🐕", "❗"], "Katta it baland ovozda vovulladi. Qanday his qilasan?", "scared", 6),
 S("surprise_box", ["📦", "❓"], "Qutini ochding, ichidan kutilmagan narsa chiqdi. Qanday his qilasan?", "surprised", 6),
]

def P(id, scene, text, word):
    return {"id": id, "scene": scene, "text": text, "word": word}

POLITE = [
 P("thanks_help", ["🎁", "🙂"], "Kimdir senga yordam berdi yoki sovg‘a qildi.", "Rahmat!"),
 P("thanks_food", ["🍲", "👵"], "Buving mazali ovqat pishirib berdi.", "Rahmat!"),
 P("please_cookie", ["🍪", "🤲"], "Sen pechenye so‘ramoqchisan.", "Iltimos"),
 P("please_pencil", ["✏️", "🤲"], "Do‘stingdan qalam so‘ramoqchisan.", "Iltimos"),
 P("sorry_bump", ["😔", "💥"], "Tasodifan do‘stingni turtib yubording.", "Kechirasiz!"),
 P("sorry_late", ["⏰", "😔"], "Mashg‘ulotga kechikib kelding.", "Kechirasiz!"),
 P("hello_morning", ["🏫", "🙂"], "Ertalab bog‘chaga kelding.", "Salom!"),
 P("bye_home", ["🚪", "👋"], "Mehmondan uyga ketyapsan.", "Xayr!"),
]
POLITE_WORDS = ["Rahmat!", "Iltimos", "Kechirasiz!", "Salom!", "Xayr!"]

def K(id, scene, text, good, others, why, age=4, kind="kind"):
    return {"id": id, "scene": scene, "text": text, "good": good, "others": others, "why": why, "age": age, "kind": kind}

# good/others: [emoji, matn]
CHOICES = [
 K("friend_fell", ["🧒", "🤕"], "Do‘sting yiqilib tushdi. Nima qilasan?", ["🤝", "Yordam beraman"],
   [["😂", "Kulaman"], ["⚽", "O‘ynashda davom etaman"]], "Yiqilgan do‘stga yordam berish — haqiqiy do‘stlik."),
 K("share_toy", ["🧸", "🧒"], "Do‘sting sening o‘yinchog‘ingni so‘radi. Nima qilasan?", ["🔁", "Navbat bilan o‘ynaymiz"],
   [["🙅", "Hech kimga bermayman"], ["😠", "Jahlim chiqadi"]], "Navbat bilan o‘ynasak, hammaga qiziq bo‘ladi."),
 K("new_kid", ["🧒", "👋"], "Guruhga yangi bola keldi, u yolg‘iz turibdi. Nima qilasan?", ["🤗", "O‘yinga taklif qilaman"],
   [["🙈", "Qaramayman"], ["🏃", "Qochib ketaman"]], "Yangi bolani o‘yinga chaqirsang, u tezda do‘st topadi."),
 K("mom_tired", ["👩", "😩"], "Onang charchab keldi. Nima qilasan?", ["🧹", "Uy ishida yordam beraman"],
   [["📺", "Multfilm ko‘raman"], ["😭", "Yig‘lab o‘yinchoq so‘rayman"]], "Oilaga yordam berish — mehr belgisi."),
 K("friend_sad", ["🧒", "😢"], "Do‘sting xafa bo‘lib o‘tiribdi. Nima qilasan?", ["🤗", "Yoniga borib yupataman"],
   [["😂", "Ustidan kulaman"], ["🙈", "E’tibor bermayman"]], "Xafa odamga iliq so‘z juda kerak."),
 K("wait_turn", ["🎠", "🧒"], "Karuselga navbat bor. Nima qilasan?", ["⏳", "Navbatimni kutaman"],
   [["💨", "Oldinga o‘tib olaman"], ["😠", "Itarib o‘taman"]], "Navbat kutish — hammaga adolatli.", 6),
 K("one_apple", ["🍎", "👧"], "Bitta olma bor, sen va singling ikkalangiz yemoqchisizlar. Nima qilasan?", ["🔪", "Teng bo‘lishamiz"],
   [["🙅", "Hammasini o‘zim yeyman"], ["😭", "Yig‘layman"]], "Bo‘lishsak, ikkalamiz ham xursand bo‘lamiz.", 6),
 K("mistake", ["🥛", "💦"], "Tasodifan sutni to‘kib yubording. Nima qilasan?", ["🧽", "Kechirim so‘rab, artib qo‘yaman"],
   [["🙈", "Yashirinaman"], ["👉", "Boshqani ayblayman"]], "Xato qilish mumkin — muhimi, uni tuzatish.", 6),
 K("baby_crying", ["👶", "😭"], "Kichik ukang yig‘layapti. Nima qilasan?", ["🧸", "O‘yinchoq berib, ovutaman"],
   [["😠", "Baqiraman"], ["🎧", "Quloqlarimni yopaman"]], "Kichiklarga g‘amxo‘rlik qilish — katta bo‘lish belgisi.", 6),
 K("praise_friend", ["🎨", "🧒"], "Do‘sting chiroyli rasm chizdi. Nima deysan?", ["👏", "Juda chiroyli ekan!"],
   [["😒", "Meniki yaxshiroq"], ["🤐", "Hech narsa demayman"]], "Maqtov do‘stingni ruhlantiradi.", 6),
 # xavfsizlik
 K("stranger_candy", ["🍬", "🧔"], "Begona odam shirinlik berib, “yur” dedi. Nima qilasan?", ["🙅", "Bormayman, ota-onamga aytaman"],
   [["🚶", "U bilan boraman"], ["🍬", "Shirinlikni olaman"]], "Begona odam bilan hech qayoqqa bormaymiz.", 4, "safety"),
 K("street", ["🚦", "🚗"], "Ko‘chani kesib o‘tish kerak. Nima qilasan?", ["✅", "Kattalar bilan, yashil chiroqda o‘taman"],
   [["🏃", "Yugurib o‘taman"], ["🔴", "Qizil chiroqda o‘taman"]], "Ko‘chadan faqat kattalar bilan va yashil chiroqda o‘tamiz.", 4, "safety"),
 K("hot_pot", ["☕", "🔥"], "Stolda juda issiq choy turibdi. Nima qilasan?", ["✋", "Tegmayman"],
   [["👆", "Ushlab ko‘raman"], ["🧒", "Yaqiniga chiqaman"]], "Issiq narsalar kuydirishi mumkin — faqat kattalar ushlaydi.", 4, "safety"),
 K("medicine", ["💊", "🧒"], "Stolda dori turibdi. Nima qilasan?", ["👩", "Faqat kattalar beradi"],
   [["🍬", "Konfet deb yeyman"], ["🤲", "O‘ynayman"]], "Dorini faqat kattalar beradi.", 6, "safety"),
 K("lost", ["🏬", "😟"], "Do‘konda onangni yo‘qotib qo‘yding. Nima qilasan?", ["🙋", "Joyimda turib, sotuvchidan yordam so‘rayman"],
   [["🚪", "Ko‘chaga chiqib ketaman"], ["😭", "Yugurib ketaman"]], "Joyida turib, xodimdan yordam so‘rash — eng to‘g‘ri yo‘l.", 6, "safety"),
 K("socket", ["🔌", "🧒"], "Devordagi rozetkani ko‘rding. Nima qilasan?", ["✋", "Tegmayman"],
   [["✏️", "Ichiga narsa tiqaman"], ["👆", "Barmog‘imni tiqaman"]], "Tok xavfli — rozetkaga tegmaymiz.", 6, "safety"),
 K("seat_belt", ["🚗", "🧒"], "Mashinaga o‘tirding. Nima qilasan?", ["🔒", "Kamar taqaman"],
   [["🤸", "O‘rindiqda sakrayman"], ["🤪", "Derazadan boshimni chiqaraman"]], "Mashinada doim kamar taqamiz.", 6, "safety"),
]

out_m = {"schemaVersion": 1, "note": "Ota-ona bilan bajariladigan original faoliyatlar (Montessori uslubida).", "activities": ACTIVITIES}
out_s = {"schemaVersion": 1, "note": "Muloqot va ijtimoiy-emotsional ko‘nikmalar (original vaziyatlar).",
         "emotions": EMOTIONS, "situations": SITUATIONS, "polite": POLITE, "politeWords": POLITE_WORDS, "choices": CHOICES}

ids = [a["id"] for a in ACTIVITIES]
assert len(ids) == len(set(ids))
assert all(len(a["steps"]) >= 3 and a["materials"] for a in ACTIVITIES)
emo = {e["id"] for e in EMOTIONS}
assert all(s["emotion"] in emo for s in SITUATIONS)
assert all(p["word"] in POLITE_WORDS for p in POLITE)
json.dump(out_m, open(os.path.join(DATA, "montessori.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(out_s, open(os.path.join(DATA, "social.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(ACTIVITIES), "activities (4y:", sum(a["age"] == 4 for a in ACTIVITIES), ", 6y:", sum(a["age"] == 6 for a in ACTIVITIES), "),",
      len(SITUATIONS), "situations,", len(POLITE), "polite,", len(CHOICES), "choices")
