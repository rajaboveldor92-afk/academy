"""Ingliz tili, 4-sinf: assets/data/school/english_g4.json + bank_english_g4.json.

Mavzular O‘zbekiston davlat dasturi (4-sinf, ≈A1) yo‘nalishida — 3-sinf va 5-sinf oralig‘idagi bosqich:
vaqt va kun tartibi, kunlar va oylar, ob-havo, taomlar (I like / I don't like), sport va sevimli mashg‘ulotlar,
uy va xonalar (there is / are, 's), shahar va yo‘l so‘rash, kasblar, yovvoyi hayvonlar, Present Continuous,
was / were, qisqa o‘qish matnlari. Hamma matn va savollar o‘zimizniki (darslikdan ko‘chirilmagan).
Imlo — britancha (colour, favourite, flat, cooker). Lug‘at mavzulari (harflab yozish, tabiat, uydagi narsalar) —
umumiy `foreign_language.dart` generatorlari; qolgani — savollar banki.
Qayta yaratish: python3 tool/content/school/english_g4.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("english", 4, L("Ingliz tili", "English", "Английский язык"))

C1 = "1-chorak. Mening kunim va taqvim"
C2 = "2-chorak. Ob-havo, taomlar va sevimli mashg‘ulotlar"
C3 = "3-chorak. Uyim, shahrim va kasblar"
C4 = "4-chorak. Hayvonlar, hozir va kecha"


# ------------------------------------------------------------ yordamchilar
def GAP(sentence, a, w, d=1, x=None, note=None, e=None, h=None):
    """Bo‘sh joyli inglizcha gap: ekranda ko‘rsatma + gap, ovozda — faqat gap (ingliz tilida)."""
    q = f"Bo‘sh joyni to‘ldiring: {sentence}" + (f" ({note})" if note else "")
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=sentence, lang="en")


def LISTEN(say, a, w, d=1, x=None, q="Tinglang va tarjimasini tanlang"):
    """Tinglab tushunish: inglizcha gap eshitiladi, javob tanlanadi."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", say=say, lang="en")


def EN(q, a, w, say, d=1, x=None, e=None, h=None):
    """Savol matnida inglizcha qism bor — u ingliz ovozida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=say, lang="en")


def FORM(word, what, a, w, d=1, x=None):
    """“go” fe’lining he / she bilan shakli — so‘z ingliz ovozida aytiladi."""
    return Q(f"“{word}” {what}", a, w, d=d, x=x or f"{word} → {a}", say=word, lang="en")


def TFE(q, a, say, d=1, x=None):
    return TF(q, a, d=d, x=x, say=say, lang="en")


def SENT(en, d=1, x=None, q="So‘zlardan gap tuzing"):
    """Inglizcha gap tuzish (tinish belgisiz, javob ovozda aytilmaydi)."""
    return ORDER(q, en, d=d, x=x, lang="en")


def QSENT(en, d=1, x=None):
    return SENT(en, d=d, x=x, q="So‘zlardan savol tuzing")


def READ(text, q, a, w, d=1, x=None):
    """O‘qib tushunish: matn ekranda, savol inglizcha (ovozda ham)."""
    return Q(q, a, w, d=d, x=x, text=text, say=q, lang="en")


def RTF(text, statement, a, d=1, x=None):
    return TF(statement, a, d=d, x=x, text=text, say=statement, lang="en")


def vocab_levels(themes):
    return [
        {"themes": themes, "modes": ["listen", "read"], "options": 3},
        {"themes": themes, "modes": ["read", "picture_word"], "options": 3, "sameTheme": True},
        {"themes": themes, "modes": ["picture_word", "read", "listen"], "options": 4, "sameTheme": True},
    ]


# ============================================================ 1-chorak
T.topic("time", "⏰", L("Soat necha? Vaqtni aytish", "What time is it?", "Который час?"),
        chapter=C1,
        theory="Vaqtni so‘rash: What time is it? — Soat necha?  Javob: It's … — Soat …\n"
               "• To‘liq soat — o’clock: 3:00 — It's three o’clock.\n"
               "• Yarim soat — half past: 7:30 — It's half past seven (yettidan yarim soat o‘tdi).\n"
               "• Qachon? — at: I get up at seven o’clock. School starts at eight.\n"
               "Kun qismlari: in the morning (ertalab), in the afternoon (tushdan keyin),\n"
               "in the evening (kechqurun), at night (tunda).",
        items=[
            Q("Soatga mos javobni tanlang: 3:00", "It's three o'clock.",
              ["It's thirteen o'clock.", "It's half past three.", "It's two o'clock."], e="🕒",
              x="3:00 — three o’clock (soat uch)."),
            Q("Soatga mos javobni tanlang: 9:00", "It's nine o'clock.",
              ["It's nineteen o'clock.", "It's half past nine.", "It's five o'clock."], e="🕘",
              x="9:00 — nine o’clock (soat to‘qqiz)."),
            Q("Soatga mos javobni tanlang: 6:30", "It's half past six.",
              ["It's half past seven.", "It's six o'clock.", "It's sixteen o'clock."], e="🕡",
              x="6:30 — half past six (oltidan yarim soat o‘tdi)."),
            Q("Soatga mos javobni tanlang: 11:30", "It's half past eleven.",
              ["It's half past twelve.", "It's eleven o'clock.", "It's half past seven."], e="🕦",
              x="11:30 — half past eleven."),
            LISTEN("It's two o'clock.", "2:00", ["12:00", "2:30", "10:00"], q="Tinglang va vaqtni tanlang",
                   x="two o'clock — 2:00."),
            LISTEN("It's half past five.", "5:30", ["5:00", "6:30", "4:30"], q="Tinglang va vaqtni tanlang",
                   x="half past five — 5:30."),
            LISTEN("It's twelve o'clock.", "12:00", ["2:00", "11:00", "12:30"], q="Tinglang va vaqtni tanlang",
                   x="twelve o'clock — 12:00."),
            LISTEN("What time is it?", "Soat necha?", ["Bugun qaysi kun?", "Necha yoshdasan?", "Qayerdasan?"]),
            MATCH("Kun qismlarini tarjimasi bilan juftlang",
                  [("in the morning", "ertalab"), ("in the afternoon", "tushdan keyin"),
                   ("in the evening", "kechqurun"), ("at night", "tunda"), ("at midnight", "yarim tunda"),
                   ("every day", "har kuni")], lang="en"),
            GAP("I get up ... seven o'clock.", "at", ["in", "on", "to"],
                x="Soat oldidan at qo‘yiladi: at seven o'clock."),
            GAP("I read books ... the evening.", "in", ["at", "on", "to"],
                x="in the evening — kechqurun."),
            GAP("It's half ... four.", "past", ["to", "at", "of"], x="4:30 — half past four."),
            TFE("“half past one” — 1:30 degani.", True, say="half past one", x="To‘g‘ri: half past one — 1:30."),
            TFE("“six o'clock” — 6:30 degani.", False, say="six o'clock",
                x="six o'clock — 6:00; 6:30 esa — half past six."),
            TFE("“at night” — ertalab degani.", False, say="at night", d=2,
                x="at night — tunda, kechasi; ertalab — in the morning."),
            Q("Soatga mos javobni tanlang: 12:30", "It's half past twelve.",
              ["It's half past one.", "It's twelve o'clock.", "It's half past two."], e="🕧", d=2,
              x="12:30 — half past twelve."),
            Q("Dars soat 8:00 da boshlanadi. Mos gapni tanlang", "School starts at eight o'clock.",
              ["School starts in eight o'clock.", "School starts at eighteen o'clock.",
               "School starts on eight o'clock."], d=2, x="Soat oldidan at: at eight o’clock."),
            GAP("We have lunch at one o'clock in the ...", "afternoon", ["morning", "night", "midnight"], d=2,
                x="Soat birdan keyin — in the afternoon (tushdan keyin)."),
            Q("Hozir soat 4:00. Bir soatdan keyin soat necha bo‘ladi?", "five o'clock",
              ["four o'clock", "three o'clock", "half past four"], d=2, x="4:00 + 1 soat = 5:00 — five o’clock."),
            LISTEN("I have breakfast at half past seven.", "Men soat 7:30 da nonushta qilaman.",
                   ["Men soat 7:00 da nonushta qilaman.", "Men soat 7:30 da tushlik qilaman.",
                    "Men soat 6:30 da nonushta qilaman."], d=2),
            SENT("I get up at seven o'clock", d=2, x="I get up at seven o'clock. — Men soat yettida turaman."),
            QSENT("What time is it now", d=2, x="What time is it now? — Hozir soat necha?"),
            Q("Soatga mos javobni tanlang: 10:30", "It's half past ten.",
              ["It's half past eleven.", "It's half to ten.", "It's ten o'clock."], e="🕥", d=3,
              x="10:30 — half past ten (o‘ndan yarim soat o‘tdi)."),
            Q("Qaysi vaqt eng erta?", "six o'clock", ["half past six", "seven o'clock", "half past seven"], d=3,
              x="6:00 — eng erta: 6:00, 6:30, 7:00, 7:30."),
            EN("Hozir half past eight. Yarim soatdan keyin soat necha bo‘ladi?", "nine o'clock",
               ["eight o'clock", "half past nine", "ten o'clock"], say="half past eight", d=3,
               x="8:30 + 30 daqiqa = 9:00 — nine o'clock."),
        ])

T.topic("routine", "🔁", L("Kun tartibi: Present Simple", "Daily routine: Present Simple",
                          "Распорядок дня: Present Simple"),
        chapter=C1, prereq=["time"],
        theory="Present Simple — har kuni takrorlanadigan ishlar: I get up at 7. We go to school.\n"
               "he / she / it bilan fe’lga -s qo‘shiladi: I play → she plays, I read → he reads.\n"
               "-sh, -ch, -o dan keyin -es: wash → washes, watch → watches, go → goes, do → does.\n"
               "have → has: She has breakfast at 7.\n"
               "Kun tartibi: wake up, get dressed, have breakfast, go to school, do homework, go to bed.",
        items=[
            GAP("I ... up at seven.", "get", ["gets", "getting", "am get"], x="I bilan fe’l o‘zgarmaydi: I get up."),
            GAP("My sister ... up at seven.", "gets", ["get", "getting", "is get"],
                x="my sister = she, shuning uchun -s: she gets up."),
            GAP("We ... to school at eight.", "go", ["goes", "going", "gos"], x="we bilan fe’l o‘zgarmaydi: we go."),
            GAP("My mum ... breakfast for us.", "makes", ["make", "making", "maked"],
                x="my mum = she → makes."),
            GAP("They ... their homework after school.", "do", ["does", "dos", "doing"],
                x="they bilan fe’l o‘zgarmaydi: they do."),
            FORM("go", "fe’lining he / she bilan shakli", "goes", ["gos", "go", "goies"],
                 x="-o dan keyin -es: go → goes."),
            FORM("wash", "fe’lining he / she bilan shakli", "washes", ["washs", "wash", "washies"],
                 x="-sh dan keyin -es: wash → washes."),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("wake up", "uyg‘onmoq"), ("get dressed", "kiyinmoq"), ("have a shower", "dush qabul qilmoq"),
                   ("have lunch", "tushlik qilmoq"), ("have dinner", "kechki ovqat yemoq"),
                   ("walk the dog", "itni sayrga olib chiqmoq"), ("wash my face", "yuzimni yuvmoq")], lang="en"),
            LISTEN("She gets dressed and has breakfast.", "U kiyinadi va nonushta qiladi.",
                   ["Men kiyinaman va nonushta qilaman.", "U uyg‘onadi va dush qabul qiladi.",
                    "U kiyinadi va tushlik qiladi."]),
            LISTEN("My brother walks the dog every evening.", "Akam har kuni kechqurun itni sayrga olib chiqadi.",
                   ["Akam har kuni ertalab itni sayrga olib chiqadi.", "Men har kuni kechqurun itni sayrga olib chiqaman.",
                    "Akam har kuni kechqurun mushukni boqadi."]),
            TFE("“He play football after school.” — to‘g‘ri gap.", False, say="He play football after school.",
                x="he bilan fe’lga -s qo‘shiladi: He plays football."),
            TFE("“Our dog sleeps in the garden.” — to‘g‘ri gap.", True, say="Our dog sleeps in the garden.",
                x="To‘g‘ri: our dog = it → sleeps."),
            Q("“har kuni” inglizcha qanday?", "every day", ["today", "yesterday", "now"], x="every day — har kuni."),
            SENT("I have a shower in the morning", x="I have a shower in the morning. — Men ertalab dush qabul qilaman."),
            GAP("He ... his teeth every morning.", "brushes", ["brush", "brushs", "brushing"], d=2,
                x="he bilan; -sh dan keyin -es: brushes."),
            GAP("Anvar ... to school by bus.", "goes", ["go", "gos", "going"], d=2, x="Anvar = he → goes."),
            GAP("Lola ... her homework in the evening.", "does", ["do", "dos", "doing"], d=2,
                x="Lola = she; do → does."),
            GAP("My dad ... the news in the evening.", "watches", ["watch", "watchs", "watching"], d=2,
                x="my dad = he; -ch dan keyin -es: watches."),
            GAP("She ... lunch at one o'clock.", "has", ["have", "haves", "having"], d=2,
                x="she bilan have → has."),
            FORM("do", "fe’lining he / she bilan shakli", "does", ["dos", "do", "dose"], d=2, x="do → does."),
            Q("Qaysi gap to‘g‘ri?", "Madina reads a book every evening.",
              ["Madina read a book every evening.", "Madina reades a book every evening.",
               "Madina reading a book every evening."], d=2, x="Madina = she → reads."),
            SENT("My father goes to work at eight", d=2,
                 x="My father goes to work at eight. — Otam soat sakkizda ishga boradi."),
            GAP("I ... like fish.", "don't", ["doesn't", "not", "am not"], d=3,
                x="I bilan inkor: don't — I don't like fish."),
            GAP("My brother ... like milk.", "doesn't", ["don't", "not", "isn't"], d=3,
                x="he bilan inkor: doesn't — My brother doesn't like milk."),
            GAP("Does Ali get up early? — Yes, he ...", "does", ["do", "is", "gets"], d=3,
                x="Does …? savoliga qisqa javob: Yes, he does."),
            Q("To‘g‘ri tartibni tanlang", "get up — have breakfast — go to school",
              ["go to school — get up — have breakfast", "have breakfast — get up — go to school",
               "go to bed — get up — have breakfast"], d=3,
              x="Avval turamiz, keyin nonushta qilamiz, so‘ng maktabga boramiz."),
        ])

T.topic("calendar", "📅", L("Kunlar, oylar va sanalar", "Days, months and dates", "Дни, месяцы и даты"),
        chapter=C1,
        theory="Hafta kunlari: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n"
               "Oylar: January, February, March, April, May, June, July, August, September, October, November, December.\n"
               "Kun va oy nomlari doim bosh harf bilan yoziladi.\n"
               "Predloglar: on + kun (on Monday), in + oy yoki fasl (in May, in winter).\n"
               "Tartib sonlar: first (1st), second (2nd), third (3rd), fourth (4th), fifth (5th).\n"
               "When is your birthday? — It's in April. It's on the fifth of April.",
        items=[
            Q("Yilning uchinchi oyi qaysi?", "March", ["May", "January", "April"],
              x="January (1), February (2), March (3)."),
            EN("“August” — qaysi oy?", "avgust", ["aprel", "oktyabr", "iyun"], say="August", x="August — avgust."),
            EN("“October” — qaysi oy?", "oktyabr", ["avgust", "dekabr", "sentabr"], say="October",
               x="October — oktyabr."),
            EN("Qaysi oy tushib qolgan? January, ..., March", "February", ["December", "April", "November"],
               say="January, ..., March", x="January, February, March."),
            EN("Qaysi kun tushib qolgan? Tuesday, ..., Thursday", "Wednesday", ["Monday", "Friday", "Sunday"],
               say="Tuesday, ..., Thursday", x="Tuesday, Wednesday, Thursday."),
            GAP("School starts ... September.", "in", ["on", "at", "to"], x="Oy oldidan in: in September."),
            GAP("We have music ... Friday.", "on", ["in", "at", "to"], x="Hafta kuni oldidan on: on Friday."),
            GAP("It's cold ... winter.", "in", ["on", "at", "of"], x="Fasl oldidan in: in winter."),
            MATCH("Oyni tarjimasi bilan juftlang",
                  [("January", "yanvar"), ("March", "mart"), ("June", "iyun"), ("July", "iyul"),
                   ("September", "sentabr"), ("November", "noyabr")], lang="en"),
            Q("Yangi yil qaysi oyda boshlanadi?", "January", ["December", "March", "September"],
              x="Yil 1-yanvarda boshlanadi: January."),
            EN("Qaysi oy yozga kiradi? (O‘zbekistonda)", "July", ["January", "October", "March"], say="July",
               x="Yoz oylari: June, July, August."),
            TFE("“Sunday” — dam olish kuni (weekend).", True, say="Sunday",
                x="To‘g‘ri: weekend — Saturday and Sunday."),
            LISTEN("My birthday is in December.", "Mening tug‘ilgan kunim dekabrda.",
                   ["Mening tug‘ilgan kunim noyabrda.", "Uning tug‘ilgan kuni dekabrda.", "Dekabrda havo issiq."]),
            SENT("We have art on Tuesday", x="We have art on Tuesday. — Seshanba kuni rasm darsimiz bor."),
            Q("Qaysi oyda 28 yoki 29 kun bo‘ladi?", "February", ["January", "March", "December"], d=2,
              x="February — eng qisqa oy: 28 kun, kabisa yilida 29 kun."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "Thursday", ["thursday", "Thirsday", "Thursdey"], d=2,
              x="Thursday — bosh harf bilan, u-r-s-d-a-y."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "January", ["january", "Janury", "Januari"], d=2,
              x="January — oy nomi bosh harf bilan yoziladi."),
            EN("Bugun — Monday. Ikki kundan keyin qaysi kun bo‘ladi?", "Wednesday",
               ["Tuesday", "Thursday", "Sunday"], say="Today is Monday.", d=2,
               x="Monday → Tuesday → Wednesday."),
            EN("Qaysi oy tushib qolgan? October, ..., December", "November", ["September", "January", "August"],
               say="October, ..., December", d=2, x="October, November, December."),
            MATCH("Son va tartib sonni juftlang",
                  [("1st", "first"), ("2nd", "second"), ("3rd", "third"), ("4th", "fourth"), ("5th", "fifth"),
                   ("10th", "tenth")], d=2, lang="en"),
            TFE("“the second” — ikkinchi degani.", True, say="the second", d=2, x="To‘g‘ri: second — ikkinchi (2nd)."),
            LISTEN("On Saturday we visit our granny.", "Shanba kuni buvimiznikiga boramiz.",
                   ["Yakshanba kuni buvimiznikiga boramiz.", "Shanba kuni bobomiznikiga boramiz.",
                    "Juma kuni buvimiz bizga keladi."], d=2),
            EN("“When is your birthday?” savoliga mos javobni tanlang", "It's in April.",
               ["It's Monday today.", "I'm ten.", "It's sunny."], say="When is your birthday?", d=2,
               x="When? — qachon? Javob: It's in April. — Aprelda."),
            SENT("The first month is January", d=2, x="The first month is January. — Birinchi oy — yanvar."),
            QSENT("When is your birthday", d=2, x="When is your birthday? — Tug‘ilgan kuning qachon?"),
            Q("Navro‘z qaysi kuni nishonlanadi?", "on the 21st of March",
              ["on the 1st of January", "on the 1st of June", "on the 21st of May"], d=3,
              x="Navro‘z — 21-mart: the twenty-first of March."),
            Q("Qaysi gap to‘g‘ri?", "We have English on Monday and Thursday.",
              ["We have English in Monday and Thursday.", "We have English on monday and thursday.",
               "We have English at Monday and Thursday."], d=3,
              x="Hafta kuni oldidan on, kun nomlari bosh harf bilan."),
        ])

T.topic("spelling", "✍️", L("So‘zlarni harflab yozish", "Spelling", "Правописание слов"),
        chapter=C1, gen="spell",
        theory="Inglizcha so‘z ko‘pincha eshitilganidek yozilmaydi — uni ko‘rib, yodlab olish kerak.\n"
               "• Qo‘sh harflar: apple, ball, egg, tree, moon.\n"
               "• Ikki harf — bitta tovush: sh (fish), ch (chair), th (three), ee (tree), oo (book).\n"
               "• So‘z oxiridagi e odatda o‘qilmaydi: cake, bike, nose.\n"
               "Rasmga qarang, so‘zni ichingizda ayting va harflarni tartib bilan tering.",
        levels=[{"minLetters": 3, "maxLetters": 4},
                {"minLetters": 4, "maxLetters": 5, "extra": 1},
                {"minLetters": 5, "maxLetters": 6, "extra": 2}])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["time", "routine", "calendar", "spelling"], chapter=C1)

# ============================================================ 2-chorak
T.topic("weather", "🌦️", L("Ob-havo va fasllar", "Weather and seasons", "Погода и времена года"),
        chapter=C2,
        theory="What's the weather like? — Havo qanday?\n"
               "Otdan sifat: sun → sunny (quyoshli), cloud → cloudy (bulutli), rain → rainy (yomg‘irli),\n"
               "wind → windy (shamolli), snow → snowy (qorli), fog → foggy (tumanli).\n"
               "Harorat: hot (issiq), warm (iliq), cool (salqin), cold (sovuq).\n"
               "Fasllar: spring, summer, autumn, winter. In autumn it's cool and rainy.\n"
               "Hozir bo‘layotgan ob-havo: It's raining. It's snowing. Take an umbrella!",
        items=[
            FORM("rain", "so‘zidan ob-havo sifati", "rainy", ["rainny", "raine", "rained"], x="rain → rainy."),
            FORM("cloud", "so‘zidan ob-havo sifati", "cloudy", ["cloudly", "clouddy", "cloudie"], x="cloud → cloudy."),
            FORM("wind", "so‘zidan ob-havo sifati", "windy", ["windly", "winddy", "windie"], x="wind → windy."),
            EN("Rasmga qarang: What's the weather like?", "It's foggy.", ["It's sunny.", "It's hot.", "It's snowy."],
               say="What's the weather like?", e="🌫️", x="Tuman — foggy."),
            EN("Rasmga qarang: What's the weather like?", "It's windy.", ["It's rainy.", "It's snowy.", "It's hot."],
               say="What's the weather like?", e="🌬️", x="Shamol — windy."),
            EN("Rasmga qarang: What's the weather like?", "It's cloudy.", ["It's sunny.", "It's snowy.", "It's foggy."],
               say="What's the weather like?", e="☁️", x="Bulut — cloudy."),
            GAP("It's raining. Take your ...", "umbrella", ["sunglasses", "T-shirt", "kite"],
                x="Yomg‘irda soyabon olamiz: umbrella."),
            GAP("It's cold and snowy. Put on your ...", "coat", ["shorts", "sandals", "sunglasses"],
                x="Qishda issiq palto kiyamiz: coat."),
            Q("“iliq” inglizcha qanday?", "warm", ["cold", "cool", "hot"],
              x="warm — iliq; hot — issiq; cool — salqin; cold — sovuq."),
            MATCH("So‘zni tarjimasi bilan juftlang",
                  [("hot", "issiq"), ("warm", "iliq"), ("cool", "salqin"), ("cold", "sovuq"), ("foggy", "tumanli"),
                   ("stormy", "bo‘ronli")], lang="en"),
            LISTEN("It's raining and it's cold.", "Yomg‘ir yog‘yapti va sovuq.",
                   ["Qor yog‘yapti va sovuq.", "Quyosh charaqlayapti va issiq.", "Yomg‘ir yog‘yapti va iliq."]),
            Q("Qaysi faslda barglar sarg‘ayib to‘kiladi?", "autumn", ["spring", "summer", "winter"],
              x="Kuzda (autumn) barglar sarg‘ayadi va to‘kiladi."),
            Q("Qaysi gap qish haqida?", "It's cold and snowy.",
              ["It's hot and sunny.", "The flowers are opening.", "We swim in the river."],
              x="Qishda sovuq va qor yog‘adi: cold and snowy."),
            SENT("It is windy today", x="It is windy today. — Bugun shamol bor."),
            FORM("sun", "so‘zidan ob-havo sifati", "sunny", ["suny", "sunnie", "sunner"], d=2,
                 x="sun → sunny (n harfi ikkilanadi)."),
            FORM("snow", "so‘zidan ob-havo sifati", "snowy", ["snowly", "snowwy", "snowie"], d=2, x="snow → snowy."),
            GAP("It's hot and sunny. Let's go ...", "swimming", ["skiing", "skating", "sledging"], d=2,
                x="Issiq kunda suzishga boramiz: go swimming."),
            GAP("What's the weather ... today?", "like", ["is", "does", "how"], d=2,
                x="What's the weather like? — Havo qanday?"),
            GAP("It's snowing. The children are making a ...", "snowman", ["sandcastle", "kite", "boat"], d=2,
                x="Qordan odam yasashadi: a snowman."),
            TFE("“In summer we make a snowman.” — O‘zbekiston uchun to‘g‘ri fikr.", False,
                say="In summer we make a snowman.", d=2,
                x="Qordan odam qishda yasaladi: In winter we make a snowman."),
            LISTEN("In spring it's warm and the trees are green.", "Bahorda iliq, daraxtlar yashil.",
                   ["Kuzda salqin, daraxtlar sariq.", "Yozda issiq, daraxtlar yashil.", "Bahorda sovuq, qor yog‘adi."],
                   d=2),
            Q("Qaysi so‘z ortiqcha?", "sandwich", ["sunny", "windy", "cloudy"], d=2,
              x="sandwich — buterbrod; qolganlari ob-havo so‘zlari."),
            SENT("In autumn it is cool and rainy", d=2, x="In autumn it is cool and rainy. — Kuzda salqin va yomg‘irli."),
            EN("“It's freezing!” nimani bildiradi?", "Juda sovuq!", ["Juda issiq!", "Yomg‘ir yog‘yapti!", "Shamol yo‘q!"],
               say="It's freezing!", d=3, x="freezing — muzlatadigan darajada sovuq."),
            QSENT("What is the weather like in winter", d=3, x="What is the weather like in winter? — Qishda havo qanday?"),
        ])

T.topic("nature", "🌈", L("Tabiat so‘zlari", "Nature words", "Природа"),
        chapter=C2, gen="vocab", prereq=["weather"],
        theory="Osmon: sun — quyosh, moon — oy, star — yulduz, cloud — bulut, rainbow — kamalak.\n"
               "Ob-havo: rain — yomg‘ir, snow — qor, wind — shamol, lightning — chaqmoq.\n"
               "Yer: tree — daraxt, flower — gul, grass — o‘t, leaf — barg, mountain — tog‘, sea — dengiz, island — orol.\n"
               "Misol: There is a rainbow in the sky. — Osmonda kamalak bor.",
        levels=vocab_levels(["nature"]))

T.topic("likes", "🍕", L("Taomlar: I like / I don't like", "Food: I like / I don't like", "Еда: I like / I don't like"),
        chapter=C2, prereq=["routine"],
        theory="like — yoqtirmoq: I like apples. — Men olmani yoqtiraman.  love — juda yaxshi ko‘rmoq: I love plov!\n"
               "don't like — yoqtirmayman: I don't like onions.\n"
               "he / she bilan: She likes pizza. He doesn't like fish.\n"
               "Savol: Do you like milk? — Yes, I do. / No, I don't.  Does he like tea? — Yes, he does.\n"
               "Taomlar: bread, rice, soup, meat, fish, cheese, eggs, juice, honey, sweets (konfetlar), biscuits (pechene).",
        items=[
            LISTEN("I like bananas.", "Men bananni yoqtiraman.",
                   ["Men bananni yoqtirmayman.", "U bananni yoqtiradi.", "Men olmani yoqtiraman."]),
            LISTEN("I don't like onions.", "Men piyozni yoqtirmayman.",
                   ["Men piyozni yoqtiraman.", "U piyozni yoqtirmaydi.", "Men sabzini yoqtirmayman."]),
            GAP("I ... like fish. I never eat it.", "don't", ["doesn't", "am not", "not"],
                x="I bilan inkor: I don't like."),
            GAP("My sister ... chocolate.", "likes", ["like", "liking", "is like"], x="my sister = she → likes."),
            GAP("Do you like grapes? — Yes, I ...", "do", ["does", "am", "like"],
                x="Do …? savoliga qisqa javob: Yes, I do."),
            GAP("Do you like milk? — No, I ...", "don't", ["doesn't", "not", "am not"],
                x="Qisqa inkor javob: No, I don't."),
            GAP("... you like pizza?", "Do", ["Does", "Are", "Is"], x="you bilan savol: Do you like …?"),
            Q("“Men sho‘rvani juda yaxshi ko‘raman.” inglizcha qanday?", "I love soup.",
              ["I don't like soup.", "I loves soup.", "I love juice."], x="love — juda yaxshi ko‘rmoq; soup — sho‘rva."),
            MATCH("Taomlarni tarjimasi bilan juftlang",
                  [("bread", "non"), ("rice", "guruch"), ("meat", "go‘sht"), ("fish", "baliq"), ("cheese", "pishloq"),
                   ("juice", "sharbat"), ("honey", "asal")], lang="en"),
            Q("Qaysi so‘z ichimlik?", "juice", ["bread", "cheese", "rice"], x="juice — sharbat, uni ichamiz."),
            TFE("“She like apples.” — to‘g‘ri gap.", False, say="She like apples.",
                x="she bilan -s: She likes apples."),
            TFE("“We don't like cold soup.” — to‘g‘ri gap.", True, say="We don't like cold soup.",
                x="To‘g‘ri: we bilan don't."),
            Q("Qaysi so‘z ortiqcha?", "chair", ["bread", "soup", "cheese"], x="chair — stul; qolganlari taomlar."),
            SENT("I like apples and pears", x="I like apples and pears. — Men olma va noklarni yoqtiraman."),
            GAP("Does your dad like tea? — Yes, he ...", "does", ["do", "is", "likes"], d=2,
                x="Does …? savoliga qisqa javob: Yes, he does."),
            GAP("... she like rice?", "Does", ["Do", "Is", "Are"], d=2, x="she bilan savol: Does she like …?"),
            EN("“Do you like ice cream?” savoliga mos javobni tanlang", "Yes, I do.",
               ["Yes, I like.", "Yes, I am.", "Yes, I does."], say="Do you like ice cream?", d=2,
               x="Qisqa javob: Yes, I do. / No, I don't."),
            EN("“What's your favourite food?” savoliga mos javobni tanlang", "My favourite food is plov.",
               ["I'm fine, thanks.", "It's in May.", "It's sunny."], say="What's your favourite food?", d=2,
               x="favourite food — sevimli taom."),
            Q("“Konfetlar (shirinliklar)” britan inglizchasida qanday?", "sweets", ["sweaters", "sheets", "seats"], d=2,
              x="Britaniyada konfetlar — sweets."),
            LISTEN("Kamola loves strawberries.", "Kamola qulupnayni juda yaxshi ko‘radi.",
                   ["Kamola qulupnayni yoqtirmaydi.", "Kamola olchani juda yaxshi ko‘radi.",
                    "Men qulupnayni juda yaxshi ko‘raman."], d=2),
            SENT("My brother doesn't like milk", d=2, x="My brother doesn't like milk. — Akam sutni yoqtirmaydi."),
            QSENT("Do you like chocolate", d=2, x="Do you like chocolate? — Shokoladni yoqtirasanmi?"),
            GAP("He doesn't ... cheese.", "like", ["likes", "liking", "liked"], d=3,
                x="doesn't dan keyin fe’l -s siz: doesn't like."),
            Q("Qaysi gap to‘g‘ri?", "Timur likes juice, but he doesn't like tea.",
              ["Timur like juice, but he doesn't like tea.", "Timur likes juice, but he don't like tea.",
               "Timur likes juice, but he doesn't likes tea."], d=3,
              x="Timur = he: likes; inkorda doesn't + like."),
        ])

T.topic("hobbies", "⚽", L("Sport va sevimli mashg‘ulotlar", "Sports and hobbies", "Спорт и хобби"),
        chapter=C2, prereq=["likes"],
        theory="Sport: play football / basketball / tennis / chess; go swimming / go skating; ride a bike; do judo.\n"
               "like + -ing — … ni yoqtiraman: I like swimming. She likes drawing. He doesn't like running.\n"
               "can — qila olaman: I can play chess. I can't skate.  Can you swim? — Yes, I can.\n"
               "-ing qo‘shish: draw → drawing, ride → riding (e tushadi), swim → swimming, jog → jogging.\n"
               "What's your hobby? — My hobby is reading.",
        items=[
            GAP("I like ... football.", "playing", ["play", "plays", "played"], x="like + -ing: I like playing football."),
            GAP("She likes ... pictures.", "drawing", ["draw", "draws", "drawed"], x="like + -ing: likes drawing."),
            GAP("I can ... a bike.", "ride", ["riding", "rides", "rode"], x="can dan keyin fe’l o‘zgarmaydi: can ride."),
            GAP("Can you skate? — No, I ...", "can't", ["don't", "am not", "doesn't"],
                x="Can …? savoliga qisqa javob: No, I can't."),
            Q("Qaysi birikma to‘g‘ri?", "go swimming", ["play swimming", "ride swimming", "make swimming"],
              x="go + -ing: go swimming, go skating."),
            Q("Qaysi birikma to‘g‘ri?", "play chess", ["go chess", "ride chess", "do chess"],
              x="O‘yinlar bilan play: play chess, play football."),
            FORM("draw", "fe’lining -ing shakli", "drawing", ["drawwing", "drawng", "draws"], x="draw → drawing."),
            MATCH("Mashg‘ulotni tarjimasi bilan juftlang",
                  [("swimming", "suzish"), ("skating", "konkida uchish"), ("drawing", "rasm chizish"),
                   ("reading", "kitob o‘qish"), ("dancing", "raqsga tushish"), ("singing", "qo‘shiq aytish"),
                   ("cooking", "ovqat pishirish")], lang="en"),
            LISTEN("My hobby is reading.", "Mening sevimli mashg‘ulotim — kitob o‘qish.",
                   ["Mening sevimli mashg‘ulotim — rasm chizish.", "Uning sevimli mashg‘uloti — kitob o‘qish.",
                    "Men kitob o‘qishni yoqtirmayman."]),
            LISTEN("They like playing basketball.", "Ular basketbol o‘ynashni yoqtiradi.",
                   ["Ular futbol o‘ynashni yoqtiradi.", "Biz basketbol o‘ynashni yoqtiramiz.",
                    "Ular basketbol o‘ynay olmaydi."]),
            TFE("“I like swim.” — to‘g‘ri gap.", False, say="I like swim.",
                x="like dan keyin -ing: I like swimming."),
            TFE("“We like dancing.” — to‘g‘ri gap.", True, say="We like dancing.", x="To‘g‘ri: like + dancing."),
            Q("Qaysi sport turi suvda bo‘ladi?", "swimming", ["football", "running", "chess"],
              x="swimming — suzish, suvda bo‘ladi."),
            SENT("I can play the piano", x="I can play the piano. — Men pianino chala olaman."),
            GAP("My brother plays ... . He's got a racket.", "tennis", ["swimming", "judo", "skating"], d=2,
                x="Raketka bilan tennis o‘ynaladi."),
            Q("Qaysi birikma to‘g‘ri?", "ride a horse", ["play a horse", "go a horse", "do a horse"], d=2,
              x="Ot, velosiped minish — ride: ride a horse, ride a bike."),
            FORM("skate", "fe’lining -ing shakli", "skating", ["skateing", "skatting", "skates"], d=2,
                 x="Oxirgi e tushadi: skating."),
            FORM("ride", "fe’lining -ing shakli", "riding", ["rideing", "ridding", "rides"], d=2,
                 x="Oxirgi e tushadi: riding."),
            LISTEN("He can swim, but he can't dive.", "U suza oladi, lekin sho‘ng‘iy olmaydi.",
                   ["U sho‘ng‘iy oladi, lekin suza olmaydi.", "Men suza olaman, lekin sho‘ng‘iy olmayman.",
                    "U suzishni yoqtiradi."], d=2),
            TFE("“She can plays chess.” — to‘g‘ri gap.", False, say="She can plays chess.", d=2,
                x="can dan keyin fe’l o‘zgarmaydi: She can play chess."),
            EN("“What's your hobby?” savoliga mos javobni tanlang", "I like collecting stamps.",
               ["I'm ten.", "It's rainy.", "It's on Monday."], say="What's your hobby?", d=2,
               x="hobby — sevimli mashg‘ulot: I like collecting stamps (marka yig‘ish)."),
            Q("“Men konkida ucha olmayman.” inglizcha qanday?", "I can't skate.",
              ["I can skate.", "I don't can skate.", "I can't skating."], d=2, x="can't + fe’l: I can't skate."),
            Q("Qaysi o‘yin 64 katakli taxtada o‘ynaladi?", "chess", ["tennis", "football", "basketball"], d=2,
              x="Shaxmat (chess) taxtasida 64 ta katak bor."),
            SENT("I like playing chess with my dad", d=2,
                 x="I like playing chess with my dad. — Dadam bilan shaxmat o‘ynashni yoqtiraman."),
            QSENT("Can you ride a horse", d=2, x="Can you ride a horse? — Ot mina olasanmi?"),
            FORM("jog", "fe’lining -ing shakli", "jogging", ["joging", "jogeing", "jogs"], d=3,
                 x="Qisqa fe’lda oxirgi undosh ikkilanadi: jogging."),
            Q("Qaysi gap to‘g‘ri?", "He likes running in the park.",
              ["He likes runing in the park.", "He like running in the park.", "He likes run in the park."], d=3,
              x="he → likes; like + running (n ikkilanadi)."),
            GAP("I'm good ... swimming.", "at", ["in", "on", "for"], d=3,
                x="be good at — … ni yaxshi bajarmoq: I'm good at swimming."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["weather", "nature", "likes", "hobbies"], chapter=C2)

# ============================================================ 3-chorak
T.topic("house", "🏠", L("Mening uyim: there is / there are va 's", "My house: there is / are and 's",
                        "Мой дом: there is / are и 's"),
        chapter=C3,
        theory="Xonalar: kitchen (oshxona), living room (mehmonxona), bedroom (yotoqxona), bathroom (hammom),\n"
               "hall (dahliz), garden (bog‘). Britaniyada kvartira — flat.\n"
               "There is + bitta narsa: There is a sofa in the living room.\n"
               "There are + ko‘p narsa: There are two beds in my bedroom.\n"
               "Savol: Is there a garden? — Yes, there is. / No, there isn't.  Are there any chairs? — Yes, there are.\n"
               "'s — egalik: my sister's room — opamning xonasi, Dad's car — dadamning mashinasi.",
        items=[
            GAP("There ... a big sofa in our living room.", "is", ["are", "am", "be"], x="Bitta divan — There is."),
            GAP("There ... four chairs in the kitchen.", "are", ["is", "am", "be"], x="To‘rtta stul — There are."),
            GAP("There ... a lamp next to my bed.", "is", ["are", "am", "be"], x="Bitta chiroq — There is."),
            GAP("There ... two windows in my bedroom.", "are", ["is", "am", "be"], x="Ikkita deraza — There are."),
            Q("Qayerda ovqat pishiramiz?", "in the kitchen", ["in the bedroom", "in the bathroom", "in the garden"],
              x="kitchen — oshxona."),
            Q("Qayerda uxlaymiz?", "in the bedroom", ["in the kitchen", "in the hall", "in the garage"],
              x="bedroom — yotoqxona."),
            MATCH("Xonalarni tarjimasi bilan juftlang",
                  [("kitchen", "oshxona"), ("bedroom", "yotoqxona"), ("bathroom", "hammom"),
                   ("living room", "mehmonxona"), ("hall", "dahliz"), ("garden", "bog‘"), ("garage", "garaj")],
                  lang="en"),
            LISTEN("There is a fridge in the kitchen.", "Oshxonada muzlatkich bor.",
                   ["Oshxonada muzlatkich yo‘q.", "Yotoqxonada muzlatkich bor.", "Oshxonada ikkita muzlatkich bor."]),
            TFE("“There are a bed in my room.” — to‘g‘ri gap.", False, say="There are a bed in my room.",
                x="Bitta karavot — There is a bed."),
            TFE("“There are three bedrooms in our flat.” — to‘g‘ri gap.", True,
                say="There are three bedrooms in our flat.", x="To‘g‘ri: uchta xona — There are."),
            Q("Qaysi narsa odatda oshxonada bo‘ladi?", "a cooker", ["a bed", "a bath", "a wardrobe"],
              x="cooker — plita (britancha), u oshxonada bo‘ladi."),
            Q("Qaysi gap to‘g‘ri?", "There is a carpet on the floor.",
              ["There are a carpet on the floor.", "There is carpet a on the floor.", "There is a carpets on the floor."],
              x="Bitta gilam: There is a carpet."),
            SENT("There is a big mirror in the hall", x="There is a big mirror in the hall. — Dahlizda katta oyna bor."),
            Q("Qayerda yuvinamiz va cho‘milamiz?", "in the bathroom", ["in the living room", "in the kitchen", "in the garden"],
              d=2, x="bathroom — hammom (vanna xonasi)."),
            LISTEN("This is my brother's bedroom.", "Bu akamning yotoqxonasi.",
                   ["Bu mening yotoqxonam.", "Bu opamning yotoqxonasi.", "Bu akamning oshxonasi."], d=2),
            GAP("Is there a garden? — Yes, there ...", "is", ["are", "has", "does"], d=2,
                x="Is there …? savoliga qisqa javob: Yes, there is."),
            GAP("Are there any pictures on the wall? — No, there ...", "aren't", ["isn't", "don't", "haven't"], d=2,
                x="Are there …? savoliga qisqa javob: No, there aren't."),
            GAP("... there a TV in your room?", "Is", ["Are", "Do", "Has"], d=2, x="Bitta televizor: Is there …?"),
            Q("“Opamning xonasi” inglizcha qanday?", "my sister's room",
              ["my sister room", "my room's sister", "my sisters room's"], d=2, x="Egalik 's bilan: my sister's room."),
            Q("“Dadamning mashinasi” inglizcha qanday?", "my dad's car", ["my dad car", "my car's dad", "car my dad's"],
              d=2, x="Egalik 's bilan: my dad's car."),
            GAP("That is ... cat. It belongs to Sardor.", "Sardor's", ["Sardor", "Sardors", "Sardor is"], d=2,
                x="Sardorning mushugi — Sardor's cat."),
            Q("Qaysi narsa odatda yotoqxonada bo‘ladi?", "a wardrobe", ["a fridge", "a cooker", "a bath"], d=2,
              x="wardrobe — kiyim javoni, u yotoqxonada turadi."),
            SENT("My grandma's kitchen is very clean", d=2,
                 x="My grandma's kitchen is very clean. — Buvimning oshxonasi juda toza."),
            QSENT("Is there a garden near your house", d=3,
                  x="Is there a garden near your house? — Uyingiz yonida bog‘ bormi?"),
            EN("“How many rooms are there in your flat?” savoliga mos javobni tanlang", "There are four rooms.",
               ["There is four rooms.", "It's four o'clock.", "Yes, there are."],
               say="How many rooms are there in your flat?", d=3,
               x="Ko‘p xona — There are four rooms."),
            Q("Britan inglizchasida “kvartira” qanday ataladi?", "flat", ["floor", "hall", "roof"], d=3,
              x="Britaniyada kvartira — flat (Amerikada — apartment)."),
        ])

T.topic("home", "🛋️", L("Uydagi narsalar", "Things at home", "Вещи в доме"),
        chapter=C3, gen="vocab", prereq=["house"],
        theory="Uydagi narsalar: bed — karavot, sofa — divan, door — eshik, clock — devor soati, TV — televizor,\n"
               "cup — chashka, plate — likopcha, spoon — qoshiq, key — kalit, box — quti, shower — dush.\n"
               "Misol: There is a clock on the wall. The keys are on the table.\n"
               "Savol: What's this? — It's a spoon. Where is the key? — It's in the box.",
        levels=vocab_levels(["home"]))

T.topic("town", "🏙️", L("Shahar: joylar va yo‘l so‘rash", "Places in town and directions",
                       "Места в городе и дорога"),
        chapter=C3, prereq=["house"],
        theory="Joylar: park, school, hospital, bank, café, library (kutubxona), post office (pochta),\n"
               "bus stop (avtobus bekati), museum (muzey).\n"
               "next to — yonida, opposite — qarshisida, between — orasida, behind — orqasida, in front of — oldida.\n"
               "The bank is next to the park. The café is between the bank and the library.\n"
               "Yo‘l so‘rash: Excuse me, where is the museum? — Go straight on. Turn left / Turn right.",
        items=[
            Q("“yonida” inglizcha qanday?", "next to", ["opposite", "between", "behind"], x="next to — yonida."),
            Q("“qarshisida” inglizcha qanday?", "opposite", ["next to", "under", "between"],
              x="opposite — qarshisida (ro‘parasida)."),
            Q("“orasida” inglizcha qanday?", "between", ["behind", "opposite", "on"],
              x="between … and … — … va … orasida."),
            MATCH("So‘zni tarjimasi bilan juftlang",
                  [("next to", "yonida"), ("opposite", "qarshisida"), ("between", "orasida"), ("behind", "orqasida"),
                   ("in front of", "oldida"), ("turn left", "chapga buriling"), ("turn right", "o‘ngga buriling")],
                  lang="en"),
            LISTEN("The bank is next to the park.", "Bank parkning yonida.",
                   ["Bank parkning qarshisida.", "Park bankning orqasida.", "Bank parkning ichida."]),
            LISTEN("The café is opposite the school.", "Kafe maktabning qarshisida.",
                   ["Kafe maktabning yonida.", "Kafe maktabning orqasida.", "Maktab kafening ichida."]),
            LISTEN("Go straight on.", "To‘g‘riga yuring.", ["Chapga buriling.", "O‘ngga buriling.", "Orqaga qayting."]),
            GAP("Excuse me, ... is the library?", "where", ["what", "who", "when"],
                x="Joy so‘ralganda — where: Where is the library?"),
            Q("Xat jo‘natish uchun qayerga boramiz?", "to the post office", ["to the museum", "to the park", "to the café"],
              x="post office — pochta."),
            Q("Qayerda avtobus kutamiz?", "at the bus stop", ["at the museum", "in the library", "in the post office"],
              x="bus stop — avtobus bekati."),
            TFE("“opposite” — orqasida degani.", False, say="opposite",
                x="opposite — qarshisida; orqasida — behind."),
            TFE("“Turn right” — o‘ngga buriling degani.", True, say="Turn right", x="To‘g‘ri: right — o‘ng, left — chap."),
            SENT("The museum is opposite the park", x="The museum is opposite the park. — Muzey parkning qarshisida."),
            Q("“orqasida” inglizcha qanday?", "behind", ["in front of", "next to", "between"], d=2,
              x="behind — orqasida; in front of — oldida."),
            LISTEN("Turn left at the bus stop.", "Avtobus bekatida chapga buriling.",
                   ["Avtobus bekatida o‘ngga buriling.", "Avtobus bekatigacha to‘g‘ri yuring.", "Avtobus bekatida kuting."],
                   d=2),
            GAP("The shop is ... the bank and the café.", "between", ["next", "opposite of", "behind of"], d=2,
                x="between … and … — … va … orasida."),
            GAP("The car is in front ... the house.", "of", ["to", "at", "from"], d=2, x="in front of — oldida."),
            GAP("My house is next ... the park.", "to", ["of", "at", "on"], d=2, x="next to — yonida."),
            Q("Ko‘chada: 🏦 🌳 🏪 (bank, park, do‘kon). Park qayerda?", "between the bank and the shop",
              ["opposite the bank", "behind the shop", "in the bank"], d=2,
              x="Park bank va do‘kon orasida: between the bank and the shop."),
            Q("Qayerda eski buyumlar va tarixni ko‘ramiz?", "in a museum", ["in a café", "at a bus stop", "in a bank"],
              d=2, x="museum — muzey."),
            EN("“Excuse me, where is the bank?” savoliga mos javobni tanlang", "It's next to the café.",
               ["It's half past two.", "Yes, it is.", "I like the bank."], say="Excuse me, where is the bank?", d=2,
               x="Where? — qayerda? Javobda joy aytiladi: next to the café."),
            SENT("Go straight on and turn left", d=2, x="Go straight on and turn left. — To‘g‘riga yurib, chapga buriling."),
            QSENT("Where is the post office", d=2, x="Where is the post office? — Pochta qayerda?"),
            Q("Qaysi gap to‘g‘ri?", "The school is behind the hospital.",
              ["The school is behind of the hospital.", "The school is behind to the hospital.",
               "The school behind is the hospital."], d=3,
              x="behind dan keyin of yoki to qo‘yilmaydi: behind the hospital."),
            QSENT("Excuse me where is the nearest café", d=3,
                  x="Excuse me, where is the nearest café? — Kechirasiz, eng yaqin kafe qayerda?"),
        ])

T.topic("jobs", "👷", L("Kasblar", "Jobs", "Профессии"),
        chapter=C3, prereq=["town"],
        theory="Kasblar: doctor (shifokor), nurse (hamshira), teacher (o‘qituvchi), driver (haydovchi), cook (oshpaz),\n"
               "vet (veterinar), farmer (fermer), pilot (uchuvchi), dentist (tish shifokori), shop assistant (sotuvchi).\n"
               "Kasb oldidan a / an: She is a nurse. He is an artist.\n"
               "What does your mum do? — She's a teacher. Where does she work? — She works at a school.\n"
               "-er / -or qo‘shimchasi: teach → teacher, drive → driver, act → actor.",
        items=[
            Q("Kasal hayvonlarni kim davolaydi?", "a vet", ["a pilot", "a driver", "a cook"],
              x="vet — veterinar, hayvonlar shifokori."),
            Q("Kim samolyot boshqaradi?", "a pilot", ["a farmer", "a nurse", "a dentist"], x="pilot — uchuvchi."),
            Q("Kim tishlarimizni davolaydi?", "a dentist", ["a teacher", "a vet", "a builder"],
              x="dentist — tish shifokori."),
            Q("Kim restoranda ovqat pishiradi?", "a cook", ["a doctor", "a pilot", "a farmer"], x="cook — oshpaz."),
            Q("Kim dalada bug‘doy ekadi va sigir boqadi?", "a farmer", ["a dentist", "a pilot", "a shop assistant"],
              x="farmer — fermer."),
            FORM("teach", "fe’lidan kasb nomi", "teacher", ["teachor", "teachist", "teaching"],
                 x="teach + -er = teacher (o‘qituvchi)."),
            GAP("My aunt is ... nurse.", "a", ["an", "is", "at"], x="Undosh bilan boshlangan so‘z oldidan a: a nurse."),
            GAP("A teacher works ... a school.", "at", ["on", "under", "of"], x="works at a school — maktabda ishlaydi."),
            MATCH("Kasb va ish joyini juftlang",
                  [("doctor", "hospital"), ("teacher", "school"), ("pilot", "plane"), ("farmer", "farm"),
                   ("shop assistant", "shop"), ("vet", "animal clinic")], lang="en"),
            TFE("“A pilot flies a plane.” — to‘g‘ri fikr.", True, say="A pilot flies a plane.",
                x="To‘g‘ri: uchuvchi samolyotni boshqaradi."),
            TFE("“A dentist works on a farm.” — to‘g‘ri fikr.", False, say="A dentist works on a farm.",
                x="Tish shifokori klinikada ishlaydi; fermada fermer ishlaydi."),
            Q("Qaysi so‘z kasb emas?", "kitchen", ["nurse", "driver", "vet"], x="kitchen — oshxona; qolganlari kasblar."),
            Q("“Uchuvchi” inglizcha qanday?", "pilot", ["driver", "painter", "police officer"], x="pilot — uchuvchi."),
            SENT("My uncle is a bus driver", x="My uncle is a bus driver. — Amakim avtobus haydovchisi."),
            FORM("drive", "fe’lidan kasb nomi", "driver", ["drivor", "driveer", "driving"], d=2,
                 x="drive + -r = driver (haydovchi)."),
            FORM("sing", "fe’lidan kasb nomi", "singer", ["singor", "singist", "singing"], d=2,
                 x="sing + -er = singer (qo‘shiqchi)."),
            GAP("He is ... artist.", "an", ["a", "is", "at"], d=2, x="Unli bilan boshlangan so‘z oldidan an: an artist."),
            GAP("What ... your father do? — He's a driver.", "does", ["do", "is", "are"], d=2,
                x="your father = he → What does he do?"),
            LISTEN("My mum is a doctor. She works at a hospital.", "Onam shifokor. U kasalxonada ishlaydi.",
                   ["Onam o‘qituvchi. U maktabda ishlaydi.", "Opam shifokor. U kasalxonada ishlaydi.",
                    "Onam hamshira. U dorixonada ishlaydi."], d=2),
            EN("“What do you want to be?” savoliga mos javobni tanlang", "I want to be a vet.",
               ["I'm ten years old.", "I like pizza.", "It's in June."], say="What do you want to be?", d=2,
               x="What do you want to be? — Kim bo‘lishni xohlaysan?"),
            EN("Topishmoq: I work in a shop. I sell things. Who am I?", "a shop assistant",
               ["a farmer", "a pilot", "a nurse"], say="I work in a shop. I sell things. Who am I?", d=2,
               x="Do‘konda ishlaydi, narsa sotadi — sotuvchi (a shop assistant)."),
            EN("Topishmoq: I help doctors. I work in a hospital. Who am I?", "a nurse",
               ["a vet", "a cook", "a driver"], say="I help doctors. I work in a hospital. Who am I?", d=2,
               x="Shifokorlarga yordam beradi — hamshira (a nurse)."),
            SENT("She works in a big hospital", d=2, x="She works in a big hospital. — U katta kasalxonada ishlaydi."),
            Q("“Oshpaz” inglizcha qanday?", "cook", ["cooker", "cooking", "cookie"], d=3,
              x="cook — oshpaz; cooker esa — plita (oshxona jihozi)."),
            FORM("act", "fe’lidan kasb nomi", "actor", ["acter", "actist", "acting"], d=3,
                 x="act + -or = actor (aktyor)."),
            LISTEN("He wants to be a firefighter.", "U o‘t o‘chiruvchi bo‘lishni xohlaydi.",
                   ["U politsiyachi bo‘lishni xohlaydi.", "U o‘t o‘chiruvchi.", "Men o‘t o‘chiruvchi bo‘lishni xohlayman."],
                   d=3),
            QSENT("What does your sister do", d=3, x="What does your sister do? — Opang kim bo‘lib ishlaydi?"),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["house", "home", "town", "jobs"], chapter=C3)

# ============================================================ 4-chorak
T.topic("wild_animals", "🦁", L("Yovvoyi hayvonlar va ularning makoni", "Wild animals and habitats",
                               "Дикие животные и их среда"),
        chapter=C4,
        theory="Hayvonlar turli joylarda yashaydi:\n"
               "• jungle (tropik o‘rmon): monkey, parrot, snake;  • forest (o‘rmon): bear, fox, wolf, owl;\n"
               "• desert (cho‘l): camel, lizard;  • sea / ocean (dengiz, okean): dolphin, whale, shark;\n"
               "• savannah (savanna): lion, giraffe, zebra, elephant;  • Arctic (Arktika): polar bear.\n"
               "Where do camels live? — They live in the desert. A giraffe has got a long neck.",
        items=[
            Q("Tuya qayerda yashaydi?", "in the desert", ["in the ocean", "in the Arctic", "in the jungle"], e="🐪",
              x="Tuya (camel) cho‘lda yashaydi: in the desert."),
            Q("Delfin qayerda yashaydi?", "in the sea", ["in the desert", "in the forest", "on a farm"], e="🐬",
              x="Delfin (dolphin) dengizda yashaydi."),
            Q("Oq ayiq qayerda yashaydi?", "in the Arctic", ["in the desert", "in the jungle", "in the savannah"], e="❄️",
              x="Oq ayiq (polar bear) Arktikada yashaydi."),
            EN("Where do monkeys live?", "in the jungle", ["in the Arctic", "in the desert", "in the ocean"],
               say="Where do monkeys live?", e="🐒", x="Maymunlar tropik o‘rmonda yashaydi: in the jungle."),
            EN("Where do foxes live?", "in the forest", ["in the sea", "in the desert", "in the Arctic"],
               say="Where do foxes live?", e="🦊", x="Tulkilar o‘rmonda yashaydi: in the forest."),
            Q("Kit qayerda yashaydi?", "in the ocean", ["in the desert", "in the forest", "in the jungle"],
              e="🐋", x="Kit okeanda yashaydi."),
            MATCH("Hayvonni makoni bilan juftlang",
                  [("camel", "desert"), ("polar bear", "Arctic"), ("dolphin", "sea"), ("monkey", "jungle"),
                   ("bear", "forest"), ("zebra", "savannah")], lang="en"),
            MATCH("Hayvonlarni tarjimasi bilan juftlang",
                  [("camel", "tuya"), ("giraffe", "jirafa"), ("wolf", "bo‘ri"), ("fox", "tulki"), ("owl", "boyqush"),
                   ("lizard", "kaltakesak"), ("whale", "kit")], lang="en"),
            LISTEN("A giraffe has got a very long neck.", "Jirafaning bo‘yni juda uzun.",
                   ["Jirafaning oyoqlari juda qisqa.", "Filning bo‘yni juda uzun.", "Jirafaning dumi juda uzun."]),
            TFE("“A whale is a very big animal.” — to‘g‘ri fikr.", True, say="A whale is a very big animal.",
                x="To‘g‘ri: kit — juda katta hayvon."),
            GAP("An elephant ... got a long trunk.", "has", ["have", "is", "are"],
                x="An elephant = it → has got. trunk — xartum."),
            GAP("Monkeys ... climb trees very well.", "can", ["can't", "are", "has"],
                x="Maymunlar daraxtga juda yaxshi chiqa oladi: can climb."),
            Q("Qaysi hayvonning terisi qora-oq yo‘l-yo‘l?", "zebra", ["giraffe", "camel", "lion"], x="zebra — zebra."),
            Q("Qaysi hayvon dengizda yashaydi?", "shark", ["camel", "fox", "giraffe"], x="shark — akula, dengizda yashaydi."),
            Q("Qaysi hayvon ortiqcha (u uy hayvoni)?", "cat", ["lion", "tiger", "wolf"],
              x="cat — uy hayvoni; qolganlari yovvoyi hayvonlar."),
            LISTEN("Lions live in Africa.", "Sherlar Afrikada yashaydi.",
                   ["Sherlar Arktikada yashaydi.", "Yo‘lbarslar Afrikada yashaydi.", "Sherlar o‘rmonda uxlaydi."], d=2),
            TFE("“Kangaroos live in Australia.” — to‘g‘ri fikr.", True, say="Kangaroos live in Australia.", d=2,
                x="To‘g‘ri: kenguru Avstraliyada yashaydi."),
            GAP("Snakes ... got legs.", "haven't", ["hasn't", "aren't", "don't"], d=2,
                x="Snakes = they → haven't got: ilonlarning oyog‘i yo‘q."),
            GAP("Owls sleep in the day and hunt at ...", "night", ["noon", "breakfast", "lunch"], d=2,
                x="Ko‘pchilik boyqushlar kunduzi uxlab, tunda ov qiladi: at night."),
            SENT("Polar bears live in the Arctic", d=2, x="Polar bears live in the Arctic. — Oq ayiqlar Arktikada yashaydi."),
            SENT("Dolphins are very clever animals", d=2, x="Dolphins are very clever animals. — Delfinlar juda aqlli hayvonlar."),
            QSENT("Where do lions live", d=2, x="Where do lions live? — Sherlar qayerda yashaydi?"),
            EN("Topishmoq: It's very big and grey. It has got big ears and a trunk.", "an elephant",
               ["a zebra", "a giraffe", "a whale"], say="It's very big and grey. It has got big ears and a trunk.", d=2,
               x="Katta, kulrang, quloqlari katta, xartumi bor — fil (an elephant)."),
            TFE("“Penguins live in the Arctic.” — to‘g‘ri fikr.", False, say="Penguins live in the Arctic.", d=3,
                x="Pingvinlar asosan Janubiy yarimsharda, masalan, Antarktidada yashaydi; Arktikada pingvin yo‘q."),
            EN("Topishmoq: It lives in the forest. It has got red fur and a long tail.", "a fox",
               ["a bear", "a wolf", "a camel"], say="It lives in the forest. It has got red fur and a long tail.", d=3,
               x="O‘rmonda yashaydi, yungi qizg‘ish, dumi uzun — tulki (a fox)."),
        ])

T.topic("present_continuous", "🏃", L("Present Continuous: I am reading", "Present Continuous", "Present Continuous"),
        chapter=C4, prereq=["routine"],
        theory="Present Continuous — ayni paytda bo‘layotgan ish: Look! The baby is sleeping.\n"
               "Tuzilishi: am / is / are + fe’l-ing: I am reading. She is singing. They are playing.\n"
               "-ing qo‘shish: read → reading, make → making (e tushadi), cut → cutting, sit → sitting.\n"
               "Inkor: I'm not sleeping. He isn't eating.  Savol: Is she dancing? — Yes, she is.\n"
               "What are you doing? — I'm drawing a cat.",
        items=[
            GAP("I ... writing a letter to my granny.", "am", ["is", "are", "be"], x="I bilan am: I am writing."),
            GAP("Look! Dad ... washing the car.", "is", ["are", "am", "be"], x="Dad = he → is washing."),
            GAP("The children ... playing in the yard.", "are", ["is", "am", "be"], x="children — ko‘plik: are playing."),
            GAP("My mum is ... a cake.", "making", ["make", "makes", "makeing"], x="make → making (e tushadi)."),
            GAP("The birds are ... in the sky.", "flying", ["fly", "flies", "flys"], x="are + flying."),
            GAP("We are ... to music.", "listening", ["listen", "listens", "listning"], x="are + listening."),
            FORM("make", "fe’lining -ing shakli", "making", ["makeing", "makking", "makes"], x="Oxirgi e tushadi: making."),
            FORM("eat", "fe’lining -ing shakli", "eating", ["eatting", "eatng", "eats"], x="eat + -ing = eating."),
            EN("Rasmga qarang. What is he doing?", "He is swimming.", ["He is running.", "He is sleeping.", "He swimming."],
               say="What is he doing?", e="🏊", x="Rasmda suzayotgan odam: He is swimming."),
            EN("Rasmga qarang. What is he doing?", "He is riding a bike.",
               ["He is riding a horse.", "He is driving a car.", "He is ride a bike."],
               say="What is he doing?", e="🚴", x="Rasmda velosiped haydayotgan odam: He is riding a bike."),
            EN("Rasmga qarang. What is she doing?", "She is dancing.", ["She is singing.", "She is swimming.", "She is dance."],
               say="What is she doing?", e="💃", x="Rasmda raqsga tushayotgan ayol: She is dancing."),
            LISTEN("Grandpa is reading a newspaper.", "Bobom gazeta o‘qiyapti.",
                   ["Bobom gazeta o‘qiydi.", "Buvim gazeta o‘qiyapti.", "Bobom kitob o‘qiyapti."]),
            TFE("“She is drawing a horse.” — to‘g‘ri gap.", True, say="She is drawing a horse.",
                x="To‘g‘ri: is + drawing."),
            TFE("“I is eating an apple.” — to‘g‘ri gap.", False, say="I is eating an apple.",
                x="I bilan am: I am eating an apple."),
            SENT("The cat is drinking milk", x="The cat is drinking milk. — Mushuk sut ichyapti."),
            FORM("cut", "fe’lining -ing shakli", "cutting", ["cuting", "cuteing", "cuts"], d=2,
                 x="Qisqa fe’lda oxirgi undosh ikkilanadi: cutting."),
            FORM("smile", "fe’lining -ing shakli", "smiling", ["smileing", "smilling", "smiles"], d=2,
                 x="Oxirgi e tushadi: smiling."),
            LISTEN("We aren't watching TV.", "Biz televizor ko‘rmayapmiz.",
                   ["Biz televizor ko‘ryapmiz.", "Ular televizor ko‘rmayapti.", "Biz kino ko‘rmayapmiz."], d=2),
            GAP("Is it snowing? — Yes, it ...", "is", ["does", "are", "am"], d=2,
                x="Is …? savoliga qisqa javob: Yes, it is."),
            GAP("Are you sleeping? — No, I'm ...", "not", ["isn't", "don't", "aren't"], d=2,
                x="Qisqa inkor javob: No, I'm not."),
            GAP("What ... Lola doing? — She's cooking.", "is", ["are", "does", "do"], d=2,
                x="Lola = she → What is she doing?"),
            Q("Qaysi gap aynan hozir sodir bo‘layotgan ishni bildiradi?", "Listen! Somebody is singing.",
              ["He sings every morning.", "We sing at school.", "They often sing."], d=2,
              x="Listen! — hozir: is singing (Present Continuous)."),
            SENT("My friends are playing football now", d=2,
                 x="My friends are playing football now. — Do‘stlarim hozir futbol o‘ynayapti."),
            FORM("clap", "fe’lining -ing shakli", "clapping", ["claping", "clapeing", "claps"], d=3,
                 x="Oxirgi undosh ikkilanadi: clapping."),
            Q("Qaysi gap to‘g‘ri?", "The dog is sitting under the table.",
              ["The dog is siting under the table.", "The dog sitting under the table.",
               "The dog are sitting under the table."], d=3, x="is + sitting (t ikkilanadi)."),
            QSENT("What are the children doing", d=3, x="What are the children doing? — Bolalar nima qilyapti?"),
        ])

T.topic("was_were", "🕰️", L("was / were: kecha qayerda edim?", "was / were", "was / were"),
        chapter=C4, prereq=["present_continuous"],
        theory="was / were — to be fe’lining o‘tgan zamoni (edi, edim).\n"
               "I / he / she / it — was: I was at school yesterday. The film was funny.\n"
               "we / you / they — were: We were in the park. They were happy.\n"
               "Inkor: wasn't, weren't: It wasn't cold.  Savol: Were you at home? — Yes, I was. / No, I wasn't.\n"
               "Kalit so‘zlar: yesterday (kecha), last week (o‘tgan hafta), last Sunday, two days ago (ikki kun oldin).",
        items=[
            GAP("I ... at the dentist yesterday.", "was", ["were", "is", "be"], x="I bilan was: I was."),
            GAP("My friends ... at the cinema last Sunday.", "were", ["was", "is", "be"],
                x="my friends = they → were."),
            GAP("The weather ... sunny yesterday.", "was", ["were", "are", "be"], x="the weather = it → was."),
            GAP("Bobur and Aziz ... late for school yesterday.", "were", ["was", "is", "am"],
                x="Ikki kishi — ko‘plik: were."),
            GAP("It ... my birthday last Friday.", "was", ["were", "is", "are"], x="it bilan was."),
            GAP("We ... in Khiva last summer.", "were", ["was", "are", "be"], x="we bilan were."),
            Q("“kecha” inglizcha qanday?", "yesterday", ["tomorrow", "today", "tonight"], x="yesterday — kecha."),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("yesterday", "kecha"), ("last week", "o‘tgan hafta"), ("last year", "o‘tgan yili"),
                   ("two days ago", "ikki kun oldin"), ("last night", "kecha kechasi"), ("today", "bugun")], lang="en"),
            LISTEN("I was ill last week.", "O‘tgan hafta kasal edim.",
                   ["Bugun kasalman.", "O‘tgan hafta u kasal edi.", "O‘tgan hafta charchagan edim."]),
            TFE("“They was at the zoo.” — to‘g‘ri gap.", False, say="They was at the zoo.",
                x="they bilan were: They were at the zoo."),
            TFE("“I was tired after the match.” — to‘g‘ri gap.", True, say="I was tired after the match.",
                x="To‘g‘ri: I bilan was."),
            SENT("We were at the park yesterday", x="We were at the park yesterday. — Kecha biz parkda edik."),
            Q("“o‘tgan hafta” inglizcha qanday?", "last week", ["next week", "this week", "every week"], d=2,
              x="last week — o‘tgan hafta; next week — kelasi hafta."),
            LISTEN("The museum was very interesting.", "Muzey juda qiziqarli edi.",
                   ["Muzey juda katta edi.", "Muzey juda qiziqarli.", "Kino juda qiziqarli edi."], d=2),
            GAP("It ... cold yesterday. It was warm.", "wasn't", ["weren't", "isn't", "aren't"], d=2,
                x="it bilan inkor: wasn't."),
            GAP("We ... at school on Sunday.", "weren't", ["wasn't", "aren't", "didn't"], d=2,
                x="we bilan inkor: weren't."),
            GAP("... you at the party yesterday? — Yes, I was.", "Were", ["Was", "Are", "Did"], d=2,
                x="you bilan savol: Were you …?"),
            EN("O‘tgan zamonga o‘tkazing: She is at school.", "She was at school.",
               ["She were at school.", "She is at school yesterday.", "She be at school."],
               say="She is at school.", d=2, x="is → was: She was at school."),
            EN("O‘tgan zamonga o‘tkazing: They are happy.", "They were happy.",
               ["They was happy.", "They are happy yesterday.", "They be happy."], say="They are happy.", d=2,
               x="are → were: They were happy."),
            SENT("My granny was a teacher", d=2, x="My granny was a teacher. — Buvim o‘qituvchi bo‘lgan."),
            GAP("Was the test easy? — No, it ...", "wasn't", ["weren't", "isn't", "didn't"], d=3,
                x="Was …? savoliga qisqa javob: No, it wasn't."),
            Q("Qaysi gap to‘g‘ri?", "Last week my brother and I were in Tashkent.",
              ["Last week my brother and I was in Tashkent.", "Last week my brother and I are in Tashkent.",
               "Last week my brother and me was in Tashkent."], d=3,
              x="my brother and I = we → were."),
            EN("“Where were you yesterday?” savoliga mos javobni tanlang", "I was at my granny's.",
               ["I am at home.", "I'm ten.", "Yes, I was."], say="Where were you yesterday?", d=3,
               x="Where? — qayerda? O‘tgan zamon: I was at my granny's (buvimnikida edim)."),
            QSENT("Where were you last Saturday", d=3, x="Where were you last Saturday? — O‘tgan shanba qayerda eding?"),
        ])

R1 = ("My name is Diyor. I am ten years old. I get up at seven o'clock. I wash my face and have breakfast "
      "with my family. School starts at eight. My favourite lesson is Maths. After school I play football "
      "with my friends. In the evening I do my homework and read a book. I go to bed at half past nine.")
R2 = ("Malika lives in a flat in Tashkent. There are three rooms in the flat: a living room, a kitchen and "
      "a bedroom. Malika's bedroom is small but nice. There is a bed, a desk and a big wardrobe. There are "
      "a lot of books on the shelf. Her white cat, Paxta, likes sleeping on the bed.")
R3 = ("It is Saturday morning. The weather is cool and windy. Aziz and his dad are in the park. They are "
      "flying a kite. The kite is red and yellow. Aziz's little sister is riding her bike. Their mum is "
      "sitting on a bench and reading a book.")
R4 = ("Our town is small and green. There is a big park in the centre. The library is next to the park, "
      "and the museum is opposite the library. There is a café between the post office and the bank. "
      "I like going to the library on Fridays.")
R5 = ("Camels live in the desert. The desert is very hot in the day, but it can be cold at night. Camels "
      "can walk for a long time without water. They have got long legs and big feet, so they can walk on "
      "the sand. People use camels to carry things.")
R6 = ("Last Sunday was my grandfather's birthday. We were at his house in the village. The weather was warm "
      "and sunny. All my cousins were there. The food was delicious and the cake was very big. "
      "We were very happy.")

T.topic("reading", "📖", L("O‘qib tushunish", "Reading", "Чтение"),
        chapter=C4,
        theory="Avval savolni o‘qing — matndan nimani izlash kerakligini bilasiz.\n"
               "Keyin matnni sekin, diqqat bilan o‘qing va javobni matndan toping.\n"
               "Savol so‘zlari: Who? — kim, Where? — qayerda, When? / What time? — qachon, soat nechada, What? — nima.\n"
               "True / False: fikr matnga mos kelsa — To‘g‘ri, mos kelmasa — Noto‘g‘ri.",
        items=[
            READ(R1, "How old is Diyor?", "ten", ["seven", "eight", "nine"], x="Matnda: I am ten years old."),
            READ(R1, "What time does Diyor get up?", "at seven o'clock",
                 ["at eight o'clock", "at half past nine", "at six o'clock"], x="Matnda: I get up at seven o'clock."),
            READ(R1, "What is Diyor's favourite lesson?", "Maths", ["English", "Art", "Music"],
                 x="Matnda: My favourite lesson is Maths."),
            RTF(R1, "Diyor plays football after school.", True, x="Matnda: After school I play football with my friends."),
            READ(R2, "Where does Malika live?", "in Tashkent", ["in Samarkand", "in Bukhara", "in Fergana"],
                 x="Matnda: Malika lives in a flat in Tashkent."),
            READ(R2, "How many rooms are there in the flat?", "three", ["two", "four", "five"],
                 x="Matnda: There are three rooms in the flat."),
            RTF(R2, "Malika's bedroom is very big.", False, x="Matnda: Malika's bedroom is small but nice."),
            READ(R3, "What is the weather like?", "cool and windy", ["hot and sunny", "cold and snowy", "warm and rainy"],
                 x="Matnda: The weather is cool and windy."),
            READ(R3, "What colour is the kite?", "red and yellow", ["blue and green", "black and white", "pink"],
                 x="Matnda: The kite is red and yellow."),
            READ(R4, "Where is the library?", "next to the park", ["opposite the bank", "behind the café", "in the museum"],
                 x="Matnda: The library is next to the park."),
            RTF(R6, "The weather was cold and rainy.", False, x="Matnda: The weather was warm and sunny."),
            READ(R1, "What does Diyor do in the evening?", "He does his homework and reads a book.",
                 ["He plays football.", "He has breakfast.", "He goes to school."], d=2,
                 x="Matnda: In the evening I do my homework and read a book."),
            RTF(R1, "Diyor goes to bed at nine o'clock.", False, d=2, x="Matnda: at half past nine — soat 9:30 da."),
            READ(R2, "Where does Paxta like sleeping?", "on the bed", ["on the desk", "in the wardrobe", "in the kitchen"],
                 d=2, x="Matnda: Her white cat, Paxta, likes sleeping on the bed."),
            READ(R3, "What is Aziz's sister doing?", "She is riding her bike.",
                 ["She is flying a kite.", "She is reading a book.", "She is sitting on a bench."], d=2,
                 x="Matnda: Aziz's little sister is riding her bike."),
            READ(R3, "Who is reading a book?", "Aziz's mum", ["Aziz", "Aziz's dad", "Aziz's sister"], d=2,
                 x="Matnda: Their mum is sitting on a bench and reading a book."),
            READ(R4, "What is opposite the library?", "the museum", ["the park", "the bank", "the café"], d=2,
                 x="Matnda: the museum is opposite the library."),
            RTF(R4, "The café is between the post office and the bank.", True, d=2,
                x="Matnda: There is a café between the post office and the bank."),
            READ(R5, "Where do camels live?", "in the desert", ["in the forest", "in the sea", "in the mountains"], d=2,
                 x="Matnda: Camels live in the desert."),
            RTF(R5, "The desert can be cold at night.", True, d=2, x="Matnda: but it can be cold at night."),
            READ(R6, "Whose birthday was it?", "the grandfather's", ["the writer's", "a cousin's", "the grandmother's"],
                 d=2, x="Matnda: Last Sunday was my grandfather's birthday."),
            READ(R6, "Where were they?", "in the village", ["in the city", "at school", "in a café"], d=2,
                 x="Matnda: We were at his house in the village."),
            READ(R5, "Why can camels walk on the sand?", "They have got big feet.",
                 ["They have got short legs.", "They can fly.", "They drink a lot of water."], d=3,
                 x="Matnda: They have got long legs and big feet, so they can walk on the sand."),
            RTF(R5, "Camels can't walk without water.", False, d=3,
                x="Matnda: Camels can walk for a long time without water."),
            READ(R4, "When does the writer go to the library?", "on Fridays", ["on Mondays", "every day", "on Sundays"],
                 d=3, x="Matnda: I like going to the library on Fridays."),
            READ(R6, "How was the cake?", "very big", ["very small", "not tasty", "cold"], d=3,
                 x="Matnda: the cake was very big."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["wild_animals", "present_continuous", "was_were", "reading"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["time", "routine", "calendar", "weather", "likes", "hobbies", "house", "town", "jobs", "wild_animals",
        "present_continuous", "was_were", "reading"], chapter=C4, level=3)

T.write()
