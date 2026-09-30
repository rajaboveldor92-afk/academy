"""Ingliz tili, 6-sinf: assets/data/school/english_g6.json + bank_english_g6.json.

Mavzular O‘zbekiston davlat dasturi (6-sinf, ≈A2) yo‘nalishida — 5-sinfdan keyingi bosqich: Past Simple
(to‘g‘ri / noto‘g‘ri fe’llar, did bilan savol va inkor), sayohat, holat ravishlari, will va be going to,
sog‘liq va maslahat (should), have to / mustn't, taqqoslash va as … as, do‘kon (much / many, some / any / no),
texnologiya, Present Perfect (ever / never, just / already), atrof-muhit, uzunroq o‘qish matnlari.
Hamma matn va savollar o‘zimizniki (darslikdan ko‘chirilmagan). Imlo — britancha (travelled, colour, kilometre,
chemist's, rubbish, trainers). Lug‘at mavzulari (harflab yozish, tana a’zolari, qarama-qarshi sifatlar, tabiat) —
umumiy `foreign_language.dart` generatorlari; qolgani — savollar banki.
Qayta yaratish: python3 tool/content/school/english_g6.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("english", 6, L("Ingliz tili", "English", "Английский язык"))

C1 = "1-chorak. O‘tgan zamon va sayohatlar"
C2 = "2-chorak. Kelajak, sog‘liq va maslahatlar"
C3 = "3-chorak. Taqqoslash, xarid va texnologiya"
C4 = "4-chorak. Tajriba, tabiat va o‘qish"


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
    """“take” fe’lining o‘tgan zamon shakli — so‘z ingliz ovozida aytiladi."""
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
        {"themes": themes, "modes": ["read", "picture_word"], "options": 4, "sameTheme": True},
        {"themes": themes, "modes": ["picture_word", "read", "listen"], "options": 4, "sameTheme": True},
    ]


# ============================================================ 1-chorak
T.topic("past_simple", "🕰️", L("Past Simple: savol va inkor bilan", "Past Simple: questions and negatives",
                               "Past Simple: вопросы и отрицания"),
        chapter=C1,
        theory="Past Simple — o‘tgan zamonda tugagan ish: I visited my aunt last week.\n"
               "To‘g‘ri fe’llar -ed oladi: work → worked, live → lived, study → studied, drop → dropped.\n"
               "Noto‘g‘ri fe’llar yodlanadi: take → took, write → wrote, find → found, bring → brought, teach → taught.\n"
               "Inkor: didn't + fe’lning oddiy shakli: We didn't go out.  Savol: Did you enjoy it? — Yes, I did. / No, I didn't.\n"
               "So‘roq so‘zi bilan: Where did you go? What did she buy? When did they arrive?",
        items=[
            FORM("take", "fe’lining o‘tgan zamon shakli", "took", ["taked", "taken", "tooked"],
                 x="Noto‘g‘ri fe’l: take → took."),
            FORM("write", "fe’lining o‘tgan zamon shakli", "wrote", ["writed", "written", "wrought"],
                 x="Noto‘g‘ri fe’l: write → wrote (written — 3-shakl)."),
            FORM("find", "fe’lining o‘tgan zamon shakli", "found", ["finded", "fond", "finds"],
                 x="Noto‘g‘ri fe’l: find → found."),
            GAP("Last year we ... in a small village.", "lived", ["live", "lives", "living"],
                x="last year — o‘tgan zamon: live → lived."),
            GAP("She ... a letter to her pen friend yesterday.", "wrote", ["writes", "write", "writed"],
                x="yesterday — o‘tgan zamon: write → wrote."),
            GAP("I ... my keys under the sofa this morning.", "found", ["find", "finded", "finds"],
                x="find → found."),
            GAP("... you finish your project? — Yes, I did.", "Did", ["Do", "Were", "Have"],
                x="Javob Yes, I did — demak savol Did bilan."),
            LISTEN("We didn't watch the match yesterday.", "Kecha biz o‘yinni ko‘rmadik.",
                   ["Kecha biz o‘yinni ko‘rdik.", "Bugun biz o‘yinni ko‘rmaymiz.", "Kecha ular o‘yinni ko‘rmadi."]),
            TFE("“My grandfather taught maths for thirty years.” — to‘g‘ri gap.", True,
                say="My grandfather taught maths for thirty years.", x="To‘g‘ri: teach → taught."),
            TFE("“Did he found his bag?” — to‘g‘ri gap.", False, say="Did he found his bag?",
                x="Did dan keyin fe’lning oddiy shakli: Did he find his bag?"),
            Q("Qaysi so‘z birikmasi o‘tgan zamonni bildiradi?", "two days ago", ["next week", "tomorrow", "every day"],
              x="two days ago — ikki kun oldin (o‘tgan zamon)."),
            FORM("bring", "fe’lining o‘tgan zamon shakli", "brought", ["bringed", "brang", "bought"], d=2,
                 x="bring → brought; bought — buy fe’lining o‘tgan zamoni."),
            FORM("teach", "fe’lining o‘tgan zamon shakli", "taught", ["teached", "thought", "tought"], d=2,
                 x="teach → taught; thought — think fe’lining o‘tgan zamoni."),
            FORM("study", "fe’lining o‘tgan zamon shakli", "studied", ["studyed", "studed", "studid"], d=2,
                 x="Undosh + y → -ied: studied."),
            FORM("drop", "fe’lining o‘tgan zamon shakli", "dropped", ["droped", "dropt", "drops"], d=2,
                 x="Qisqa fe’lda oxirgi undosh ikkilanadi: dropped."),
            FORM("swim", "fe’lining o‘tgan zamon shakli", "swam", ["swimmed", "swum", "swimed"], d=2,
                 x="swim → swam (swum — 3-shakl)."),
            GAP("They didn't ... the bus.", "catch", ["caught", "catches", "catched"], d=2,
                x="didn't dan keyin fe’lning oddiy shakli: didn't catch."),
            GAP("Where ... you go last summer?", "did", ["do", "were", "was"], d=2,
                x="O‘tgan zamonda so‘roq so‘zi + did: Where did you go?"),
            GAP("What ... Kamila buy at the market yesterday?", "did", ["does", "was", "is"], d=2,
                x="yesterday — o‘tgan zamon: What did Kamila buy?"),
            EN("Inkor shaklini tanlang: He took the train.", "He didn't take the train.",
               ["He didn't took the train.", "He not took the train.", "He doesn't took the train."],
               say="He took the train.", d=2, x="didn't + fe’lning oddiy shakli: didn't take."),
            EN("Savol shaklini tanlang: They arrived at six.", "Did they arrive at six?",
               ["Did they arrived at six?", "Do they arrived at six?", "Arrived they at six?"],
               say="They arrived at six.", d=2, x="Did + ega + fe’lning oddiy shakli."),
            MATCH("Fe’lni o‘tgan zamon shakli bilan juftlang",
                  [("take", "took"), ("write", "wrote"), ("find", "found"), ("bring", "brought"), ("teach", "taught"),
                   ("fly", "flew"), ("swim", "swam")], d=2, lang="en"),
            LISTEN("Did you enjoy the concert?", "Konsert sizga yoqdimi?",
                   ["Konsertga borasizmi?", "Konsert qachon edi?", "Konsertni yoqtirasizmi?"], d=2),
            SENT("We travelled to Bukhara by train", d=2,
                 x="We travelled to Bukhara by train. — Biz Buxoroga poyezdda bordik."),
            FORM("fly", "fe’lining o‘tgan zamon shakli", "flew", ["flied", "flown", "flyed"], d=3,
                 x="fly → flew (flown — 3-shakl)."),
            FORM("think", "fe’lining o‘tgan zamon shakli", "thought", ["thinked", "thank", "taught"], d=3,
                 x="think → thought."),
            GAP("Yesterday I ... my bike to school.", "rode", ["rided", "ridden", "ride"], d=3,
                x="ride → rode (ridden — 3-shakl)."),
            EN("Javobga mos savolni tanlang: I got up at six.", "What time did you get up?",
               ["What time do you got up?", "What time did you got up?", "When you got up?"],
               say="I got up at six.", d=3, x="What time + did + ega + fe’lning oddiy shakli."),
            QSENT("What did you do at the weekend", d=3,
                  x="What did you do at the weekend? — Dam olish kunlari nima qilding?"),
        ])

T.topic("travel", "✈️", L("Sayohat va ta’til", "Travel and holidays", "Путешествия и каникулы"),
        chapter=C1, prereq=["past_simple"],
        theory="Sayohat so‘zlari: holiday (ta’til), trip / journey (safar), suitcase (chamadon), ticket (chipta),\n"
               "passport, luggage (yuk), airport, railway station (vokzal), hotel (mehmonxona), map (xarita), guide (gid).\n"
               "by + transport: by train, by plane, by car, by bus;  piyoda esa — on foot.\n"
               "Iboralar: go on holiday, go sightseeing, pack a suitcase, book a hotel, take photos, miss the train.\n"
               "Misol: Last summer we went to Samarkand by train. We stayed in a hotel and took a lot of photos.",
        items=[
            Q("“chamadon” inglizcha qanday?", "suitcase", ["passport", "ticket", "map"], x="suitcase — chamadon."),
            Q("“chipta” inglizcha qanday?", "ticket", ["hotel", "guide", "suitcase"], x="ticket — chipta."),
            Q("Boshqa davlatga uchish uchun qaysi hujjat kerak?", "a passport", ["a menu", "a diary", "a timetable"],
              x="passport — pasport, chet elga chiqish hujjati."),
            Q("Qayerda samolyotga chiqamiz?", "at the airport", ["at the railway station", "at the bus stop", "at the port"],
              x="airport — aeroport."),
            GAP("We went to Samarkand ... train.", "by", ["on", "with", "in"], x="Transport bilan by: by train."),
            GAP("Don't forget to pack your ...!", "suitcase", ["ticket office", "hotel", "airport"],
                x="pack a suitcase — chamadon yig‘moq."),
            GAP("We stayed in a nice ... near the sea.", "hotel", ["ticket", "passport", "suitcase"],
                x="stay in a hotel — mehmonxonada turmoq."),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("go on holiday", "ta’tilga chiqmoq"), ("pack a suitcase", "chamadon yig‘moq"),
                   ("book a hotel", "mehmonxona band qilmoq"), ("take photos", "suratga olmoq"),
                   ("buy a ticket", "chipta sotib olmoq"), ("miss the train", "poyezddan qolib ketmoq")], lang="en"),
            TFE("“journey” — safar, yo‘l yurish degani.", True, say="journey", x="To‘g‘ri: journey — safar."),
            Q("Qaysi so‘z transport emas?", "suitcase", ["train", "plane", "ship"], x="suitcase — chamadon."),
            SENT("My dad bought the tickets online", x="My dad bought the tickets online. — Dadam chiptalarni internetda sotib oldi."),
            Q("“vokzal (temir yo‘l)” britancha qanday?", "railway station", ["airport", "bus stop", "harbour"], d=2,
              x="Britaniyada temir yo‘l vokzali — railway station."),
            GAP("I walk to school. I go on ...", "foot", ["feet", "walk", "legs"], d=2, x="Piyoda — on foot."),
            GAP("Let's go ... in the old town.", "sightseeing", ["swimming pool", "sight", "tourist"], d=2,
                x="go sightseeing — diqqatga sazovor joylarni ko‘rgani bormoq."),
            GAP("The train ... at 9:15 and arrived at 11:30.", "left", ["leaved", "leave", "lefted"], d=2,
                x="leave → left (jo‘nab ketdi)."),
            MATCH("Shahar va diqqatga sazovor joyni juftlang",
                  [("Samarkand", "the Registan"), ("Bukhara", "the Ark"), ("Khiva", "Itchan Kala"),
                   ("Tashkent", "the TV Tower"), ("Shakhrisabz", "Ak-Saray Palace")], d=2, lang="en"),
            LISTEN("Have a good trip!", "Safaringiz yaxshi o‘tsin!",
                   ["Xush kelibsiz!", "Yaxshi dam oling!", "Tezroq qayting!"], d=2),
            TFE("“by foot” — to‘g‘ri ibora.", False, say="by foot", d=2,
                x="Piyoda — on foot; by esa transport bilan: by bus, by car."),
            EN("“Where did you go on holiday?” savoliga mos javobni tanlang", "We went to the mountains.",
               ["We go to the mountains every day.", "By train.", "Yes, we did."],
               say="Where did you go on holiday?", d=2, x="Where? — qayerga? Javobda joy: to the mountains."),
            EN("“How did you get there?” savoliga mos javobni tanlang", "We went by plane.",
               ["We stayed for a week.", "It was great.", "In July."], say="How did you get there?", d=2,
               x="How? — qanday (nima bilan)? Javob: by plane."),
            SENT("We stayed in a hotel near the beach", d=2,
                 x="We stayed in a hotel near the beach. — Biz sohil yaqinidagi mehmonxonada turdik."),
            LISTEN("We missed the plane because of the traffic.", "Tirbandlik tufayli samolyotga ulgurmadik.",
                   ["Tirbandlik tufayli poyezdga ulgurmadik.", "Samolyotga o‘z vaqtida yetib keldik.",
                    "Tirbandlik tufayli samolyot kechikdi."], d=3),
            LISTEN("How long does the journey take?", "Safar qancha vaqt oladi?",
                   ["Safar qachon boshlanadi?", "Chipta qancha turadi?", "Poyezd qayerdan jo‘naydi?"], d=3),
            Q("Mehmonxonada xona band qilganda nima deymiz?", "I'd like to book a room, please.",
              ["I'd like to book a ticket for a room.", "Give me the room now.", "Where is the room of me?"], d=3,
              x="Xushmuomala so‘rov: I'd like to book a room, please."),
            QSENT("How did you travel to Khiva", d=3, x="How did you travel to Khiva? — Xivaga qanday bording?"),
        ])

T.topic("adverbs", "🐢", L("Holat ravishlari: quickly, well", "Adverbs of manner", "Наречия образа действия"),
        chapter=C1,
        theory="Ravish fe’lni tasvirlaydi — ish QANDAY bajariladi? (How?)\n"
               "Sifat + -ly: quick → quickly, slow → slowly, quiet → quietly, careful → carefully, loud → loudly.\n"
               "-y → -ily: easy → easily, happy → happily;  -le → -ly: gentle → gently.\n"
               "Maxsus: good → well, fast → fast, hard → hard (hardly — “deyarli … emas” degani, boshqa so‘z!).\n"
               "Sifat otni, ravish fe’lni tasvirlaydi: She is a careful driver. — She drives carefully.",
        items=[
            FORM("quick", "sifatidan hosil bo‘lgan ravish", "quickly", ["quickily", "quickely", "quick"],
                 x="quick + -ly = quickly (tez)."),
            FORM("slow", "sifatidan hosil bo‘lgan ravish", "slowly", ["slowily", "slowlly", "slowely"],
                 x="slow + -ly = slowly (sekin)."),
            FORM("good", "sifatidan hosil bo‘lgan ravish", "well", ["goodly", "good", "better"],
                 x="Maxsus shakl: good → well."),
            GAP("The tortoise walks very ...", "slowly", ["slow", "slowing", "slows"],
                x="walks — fe’l; uni ravish tasvirlaydi: slowly."),
            GAP("Please speak ... . The baby is sleeping.", "quietly", ["quiet", "quietness", "loudly"],
                x="Chaqaloq uxlayapti — sekin (quietly) gapiramiz."),
            GAP("Madina sings very ...", "well", ["good", "goodly", "nice"], x="sings — fe’l, shuning uchun well."),
            Q("Qaysi so‘z ravish?", "badly", ["bad", "bed", "badge"], x="badly — yomon (ravish); bad — sifat."),
            Q("“Sekin” (ravish) inglizcha qanday?", "slowly", ["slow", "slower", "slowness"], x="slowly — sekin (ravish)."),
            LISTEN("Please drive carefully.", "Iltimos, ehtiyotkorlik bilan haydang.",
                   ["Iltimos, tezroq haydang.", "U ehtiyotkor haydovchi.", "Iltimos, sekin yuring."]),
            TFE("“He speaks English very good.” — to‘g‘ri gap.", False, say="He speaks English very good.",
                x="Fe’lni ravish tasvirlaydi: He speaks English very well."),
            TFE("“The cat jumped quickly onto the table.” — to‘g‘ri gap.", True,
                say="The cat jumped quickly onto the table.", x="To‘g‘ri: jumped — fe’l, quickly — ravish."),
            FORM("careful", "sifatidan hosil bo‘lgan ravish", "carefully", ["carefuly", "carefulily", "carefullly"], d=2,
                 x="careful + -ly = carefully (ikkita l)."),
            FORM("easy", "sifatidan hosil bo‘lgan ravish", "easily", ["easyly", "easly", "easilly"], d=2,
                 x="-y → -ily: easily."),
            FORM("happy", "sifatidan hosil bo‘lgan ravish", "happily", ["happyly", "happly", "happilly"], d=2,
                 x="-y → -ily: happily."),
            GAP("He answered all the questions ...", "correctly", ["correct", "corrects", "correction"], d=2,
                x="answered — fe’l, shuning uchun ravish: correctly (to‘g‘ri)."),
            GAP("Read the instructions ...", "carefully", ["careful", "care", "carefulness"], d=2,
                x="Read — fe’l: carefully (diqqat bilan)."),
            MATCH("Sifat va ravishni juftlang",
                  [("quick", "quickly"), ("good", "well"), ("easy", "easily"), ("careful", "carefully"),
                   ("loud", "loudly"), ("happy", "happily")], d=2, lang="en"),
            LISTEN("The children played happily in the garden.", "Bolalar bog‘da xursand o‘ynashdi.",
                   ["Bolalar bog‘da jim o‘tirishdi.", "Bolalar bog‘da xursand o‘ynayapti.", "Bolalar bog‘da tez yugurishdi."],
                   d=2),
            SENT("The old man walked slowly to the bus stop", d=2,
                 x="The old man walked slowly to the bus stop. — Qariya avtobus bekatiga sekin yurib bordi."),
            SENT("Please write your name clearly", d=2, x="Please write your name clearly. — Iltimos, ismingizni aniq yozing."),
            FORM("fast", "sifatidan hosil bo‘lgan ravish", "fast", ["fastly", "fastily", "faster"], d=3,
                 x="fast — sifat ham, ravish ham: He runs fast. (fastly degan so‘z yo‘q)"),
            FORM("gentle", "sifatidan hosil bo‘lgan ravish", "gently", ["gentlely", "gentely", "gentlly"], d=3,
                 x="-le → -ly: gently (mayin)."),
            GAP("My brother works very ... . He is always busy.", "hard", ["hardly", "hardy", "harden"], d=3,
                x="work hard — qattiq ishlamoq; hardly — “deyarli … emas”."),
            Q("Qaysi so‘z ravish?", "loudly", ["loud", "lovely", "friendly"], d=3,
              x="loudly — baland ovozda (ravish). lovely va friendly -ly bilan tugasa ham sifat."),
            EN("Ravish bilan qayta yozing: She is a slow reader.", "She reads slowly.",
               ["She reads slow.", "She slowly reader.", "She reads slower."], say="She is a slow reader.", d=3,
               x="slow reader (sifat + ot) → reads slowly (fe’l + ravish)."),
        ])

T.topic("spelling", "✍️", L("So‘zlarni to‘g‘ri yozish", "Spelling", "Правописание"),
        chapter=C1, gen="spell",
        theory="Uzunroq so‘zlarni yozishda qoidalarga e’tibor bering:\n"
               "• Qo‘sh undosh: rabbit, carrot, butterfly, balloon.\n"
               "• Harf birikmalari: ph = f (dolphin), wh (whale), ck (clock), igh (lightning).\n"
               "• Eshitilmaydigan harflar: k (knife), w (write), b (lamb).\n"
               "Rasmga qarang, so‘zni ichingizda bo‘g‘inlab ayting va harflarni tering. Ortiqcha harflar ham bor!",
        levels=[{"minLetters": 4, "maxLetters": 6, "extra": 1},
                {"minLetters": 5, "maxLetters": 7, "extra": 2},
                {"minLetters": 6, "maxLetters": 9, "extra": 2}])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["past_simple", "travel", "adverbs", "spelling"], chapter=C1)

# ============================================================ 2-chorak
T.topic("future", "🔮", L("Kelasi zamon: will va be going to", "Future: will and be going to",
                         "Будущее время: will и be going to"),
        chapter=C2,
        theory="will + fe’l — bashorat, shu zahoti qilingan qaror, va’da: It will rain tomorrow. I'll help you!\n"
               "Qisqa shakl: I'll, she'll; inkor: won't (will not): We won't be late.\n"
               "be going to + fe’l — oldindan rejalashtirilgan ish yoki aniq belgi:\n"
               "I'm going to visit my aunt on Sunday. Look at those clouds! It's going to rain.\n"
               "Savol: Will you come? — Yes, I will.  Are you going to play? — Yes, I am.\n"
               "Kalit so‘zlar: tomorrow, next week, next year, soon, in the future.",
        items=[
            GAP("I think it ... rain tomorrow.", "will", ["is", "does", "was"], x="Bashorat — will: it will rain."),
            GAP("I'm cold. — Wait, I ... close the window.", "will", ["am", "was", "do"],
                x="Shu zahoti qilingan qaror — will: I'll close the window."),
            GAP("We are ... to visit Samarkand next month.", "going", ["go", "goes", "gone"],
                x="Reja: be going to — We are going to visit."),
            GAP("She is going ... a new dress.", "to buy", ["buy", "buying", "to buys"], x="going to + fe’l: going to buy."),
            GAP("They ... going to watch the match tonight.", "are", ["is", "will", "am"], x="they bilan are going to."),
            Q("Qaysi gap kelasi zamonda?", "We will fly to London.",
              ["We flew to London.", "We fly to London every year.", "We are flying now."],
              x="will + fe’l — kelasi zamon."),
            Q("Qaysi so‘z birikmasi kelajakni bildiradi?", "next year", ["last year", "yesterday", "two days ago"],
              x="next year — kelasi yil."),
            LISTEN("I'll call you later.", "Keyinroq senga qo‘ng‘iroq qilaman.",
                   ["Hozir senga qo‘ng‘iroq qilyapman.", "Kecha senga qo‘ng‘iroq qildim.", "Keyinroq menga qo‘ng‘iroq qil."]),
            TFE("“She will goes to the party.” — to‘g‘ri gap.", False, say="She will goes to the party.",
                x="will dan keyin fe’l o‘zgarmaydi: She will go."),
            TFE("“I'm going to read this book next week.” — to‘g‘ri gap.", True,
                say="I'm going to read this book next week.", x="To‘g‘ri: am going to + read."),
            MATCH("To‘liq va qisqa shaklni juftlang",
                  [("I will", "I'll"), ("you will", "you'll"), ("she will", "she'll"), ("we will", "we'll"),
                   ("they will", "they'll"), ("will not", "won't")], lang="en"),
            GAP("I've got a ticket. I ... going to see the concert tonight.", "am", ["will", "is", "do"],
                x="I bilan am going to."),
            GAP("Don't worry, I ... tell anyone.", "won't", ["don't", "am not", "wasn't"], d=2,
                x="Va’da (inkor): I won't tell anyone."),
            GAP("Look at those black clouds! It's going to ...", "rain", ["raining", "rains", "rained"], d=2,
                x="going to + fe’lning oddiy shakli: going to rain."),
            GAP("... you help me with my homework? — Yes, of course.", "Will", ["Are", "Do", "Did"], d=2,
                x="Iltimos yoki taklif: Will you help me?"),
            EN("Inkor shaklini tanlang: He will be at home.", "He won't be at home.",
               ["He willn't be at home.", "He will not is at home.", "He doesn't will be at home."],
               say="He will be at home.", d=2, x="will not = won't: He won't be at home."),
            EN("Savol shaklini tanlang: She is going to learn French.", "Is she going to learn French?",
               ["Does she going to learn French?", "Will she going to learn French?", "She is going learn French?"],
               say="She is going to learn French.", d=2, x="is oldinga chiqadi: Is she going to …?"),
            LISTEN("We're going to paint the kitchen this weekend.", "Shu dam olish kunlari oshxonani bo‘yamoqchimiz.",
                   ["O‘tgan dam olish kunlari oshxonani bo‘yadik.", "Shu dam olish kunlari mehmonxonani bo‘yamoqchimiz.",
                    "Oshxonani bo‘yashni yoqtiramiz."], d=2),
            LISTEN("It won't be easy.", "Bu oson bo‘lmaydi.", ["Bu oson bo‘ladi.", "Bu oson emas edi.", "Bu juda qiyin edi."],
                   d=2),
            EN("“Will it be sunny tomorrow?” savoliga qisqa javob", "Yes, it will.",
               ["Yes, it is.", "Yes, it does.", "Yes, it wills."], say="Will it be sunny tomorrow?", d=2,
               x="Will …? savoliga qisqa javob: Yes, it will. / No, it won't."),
            SENT("I will send you a message tomorrow", d=2, x="I will send you a message tomorrow. — Ertaga senga xabar yuboraman."),
            SENT("My parents are going to buy a new car", d=2,
                 x="My parents are going to buy a new car. — Ota-onam yangi mashina sotib olmoqchi."),
            GAP("Is Nodir going to come? — No, he ...", "isn't", ["doesn't", "aren't", "didn't"], d=3,
                x="Is …going to…? savoliga qisqa javob: No, he isn't."),
            GAP("Next year my sister ... ten.", "will be", ["is being", "was", "has been"], d=3,
                x="Kelasi yil — will be: My sister will be ten."),
            EN("Mos javobni tanlang: “The phone is ringing!”", "I'll answer it.",
               ["I answered it.", "I'm answer it.", "I will answering it."], say="The phone is ringing!", d=3,
               x="Shu zahoti qaror — will: I'll answer it."),
            QSENT("What are you going to do this summer", d=3,
                  x="What are you going to do this summer? — Bu yoz nima qilmoqchisan?"),
        ])

T.topic("health", "🤒", L("Sog‘liq va kasalliklar", "Health and illnesses", "Здоровье и болезни"),
        chapter=C2,
        theory="Nima bo‘ldi? — What's the matter? / What's wrong?\n"
               "I've got a headache (boshim og‘riyapti), a sore throat (tomog‘im), a cold (shamollash), a cough (yo‘tal),\n"
               "a temperature (isitma), toothache (tish og‘rig‘i), stomach ache (qorin og‘rig‘i).\n"
               "My leg hurts. — Oyog‘im og‘riyapti.  I feel ill. — O‘zimni yomon his qilyapman.\n"
               "Maslahat — should: You should see a doctor. You shouldn't eat too many sweets.\n"
               "Dori — medicine; britancha dorixona — the chemist's. Get well soon! — Tezroq tuzalib keting!",
        items=[
            Q("“Boshim og‘riyapti” inglizcha qanday?", "I've got a headache.",
              ["I've got a cold.", "My leg hurts.", "I've got a sore throat."], x="headache — bosh og‘rig‘i."),
            Q("“Tomog‘im og‘riyapti” inglizcha qanday?", "I've got a sore throat.",
              ["I've got a headache.", "My back hurts.", "I've got a cough."], x="sore throat — tomoq og‘rig‘i."),
            MATCH("So‘zni tarjimasi bilan juftlang",
                  [("headache", "bosh og‘rig‘i"), ("toothache", "tish og‘rig‘i"), ("sore throat", "tomoq og‘rig‘i"),
                   ("cough", "yo‘tal"), ("temperature", "isitma"), ("stomach ache", "qorin og‘rig‘i"),
                   ("medicine", "dori")], lang="en"),
            LISTEN("What's the matter?", "Nima bo‘ldi?", ["Soat necha?", "Qayerdansiz?", "Nima qilyapsiz?"]),
            GAP("You've got a cold. You ... stay in bed.", "should", ["shouldn't", "mustn't", "can't"],
                x="Maslahat — should: You should stay in bed."),
            GAP("You ... eat so many sweets. They're bad for your teeth.", "shouldn't", ["should", "must", "have"],
                x="Yomon odatdan qaytarish — shouldn't."),
            GAP("I've got toothache. I'm going to the ...", "dentist", ["vet", "baker", "hairdresser"],
                x="Tish og‘risa — tish shifokoriga (dentist)."),
            GAP("My ... hurts. I can't walk.", "leg", ["ear", "tooth", "throat"], x="Yura olmayman — oyog‘im (leg) og‘riyapti."),
            LISTEN("You should drink a lot of water.", "Ko‘p suv ichishingiz kerak.",
                   ["Ko‘p suv ichmasligingiz kerak.", "Men ko‘p suv ichaman.", "Suv ichish mumkin emas."]),
            LISTEN("My back hurts.", "Belim og‘riyapti.", ["Boshim og‘riyapti.", "Qornim og‘riyapti.", "Qo‘lim og‘riyapti."]),
            TFE("“Get well soon!” — kasal odamga aytiladi.", True, say="Get well soon!",
                x="Get well soon! — Tezroq tuzalib keting!"),
            Q("Qaysi so‘z tana a’zosi?", "shoulder", ["cough", "medicine", "nurse"], x="shoulder — yelka."),
            SENT("You should go to bed early", x="You should go to bed early. — Erta uxlashingiz kerak."),
            Q("Sog‘lom turmush uchun qaysi odat foydali?", "eating fruit and vegetables",
              ["going to bed very late", "eating crisps every day", "never doing sport"],
              x="Meva va sabzavot yeyish — foydali odat."),
            GAP("You can buy medicine at the ...", "chemist's", ["butcher's", "baker's", "newsagent's"], d=2,
                x="Britaniyada dorixona — the chemist's."),
            GAP("She ... a bad cough.", "has got", ["have got", "is", "does"], d=2, x="she bilan has got."),
            GAP("I feel ... . I think I've got a temperature.", "ill", ["well", "fine", "happy"], d=2,
                x="I feel ill — o‘zimni yomon his qilyapman."),
            TFE("“You should to see a doctor.” — to‘g‘ri gap.", False, say="You should to see a doctor.", d=2,
                x="should dan keyin to qo‘yilmaydi: You should see a doctor."),
            LISTEN("I feel much better today, thanks.", "Bugun o‘zimni ancha yaxshi his qilyapman, rahmat.",
                   ["Bugun o‘zimni yomon his qilyapman.", "Kecha o‘zimni yaxshi his qildim.", "Bugun men kasalman, rahmat."],
                   d=2),
            EN("“I've got a headache.” — eng yaxshi maslahatni tanlang", "You should lie down and rest.",
               ["You should play loud music.", "You should run five kilometres.", "You shouldn't sleep tonight."],
               say="I've got a headache.", d=2, x="Bosh og‘riganda yotib dam olish kerak."),
            EN("“How are you feeling today?” savoliga mos javobni tanlang", "Not very well. I've got a cough.",
               ["I'm eleven.", "I feel it on Monday.", "By bus."], say="How are you feeling today?", d=2,
               x="O‘zingizni qanday his qilyapsiz? — Unchalik yaxshi emas, yo‘talyapman."),
            SENT("I have got a terrible cold", d=2, x="I have got a terrible cold. — Qattiq shamollaganman."),
            Q("“Isitmam bor” inglizcha qanday?", "I've got a temperature.",
              ["I've got a thermometer.", "I've got a cold hand.", "It's a hot temperature."], d=3,
              x="Isitma — a temperature: I've got a temperature."),
            GAP("He broke his arm, so he went to ...", "hospital", ["school", "the cinema", "the bakery"], d=3,
                x="Britaniyada: go to hospital (kasalxonaga bormoq)."),
            QSENT("What is wrong with your arm", d=3, x="What is wrong with your arm? — Qo‘lingizga nima bo‘ldi?"),
        ])

T.topic("modals", "🚦", L("should, have to, mustn't", "should, have to, mustn't", "should, have to, mustn't"),
        chapter=C2, prereq=["health"],
        theory="should — maslahat (… qilgan ma’qul): You should wear a coat.  shouldn't — qilmagan ma’qul.\n"
               "have to / has to — majburiyat, qoida: I have to wear a uniform. She has to get up early.\n"
               "don't have to — shart emas: We don't have to go to school on Sunday.\n"
               "mustn't — mumkin emas, taqiq: You mustn't use your phone in the exam.\n"
               "Diqqat: mustn't (taqiq) va don't have to (shart emas) — ma’nosi har xil!  O‘tgan zamon: had to — I had to wait.",
        items=[
            GAP("It's cold outside. You ... wear a hat.", "should", ["shouldn't", "mustn't", "don't have to"],
                x="Maslahat — should."),
            GAP("You ... stay up late before a test.", "shouldn't", ["should", "have to", "has to"],
                x="Imtihon oldidan kech yotmaslik kerak — shouldn't."),
            GAP("My brother ... get up at six for work.", "has to", ["have to", "must to", "should to"],
                x="he bilan has to."),
            GAP("We ... wear a uniform at our school.", "have to", ["has to", "haves to", "having to"],
                x="we bilan have to."),
            GAP("You ... swim here. It's dangerous.", "mustn't", ["must", "have to", "should"],
                x="Xavfli — mumkin emas: mustn't."),
            GAP("You look tired. You ... have a rest.", "should", ["mustn't", "shouldn't", "don't have to"],
                x="Charchagan odamga maslahat — should."),
            EN("“mustn't” nimani bildiradi?", "taqiq (mumkin emas)", ["maslahat", "shart emas", "qobiliyat"], say="mustn't",
              x="mustn't — mumkin emas, taqiqlangan."),
            LISTEN("Students mustn't run in the corridors.", "O‘quvchilarga yo‘laklarda yugurish mumkin emas.",
                   ["O‘quvchilar yo‘laklarda yugurishi kerak.", "O‘quvchilar yo‘laklarda yugurishi shart emas.",
                    "O‘quvchilar yo‘laklarda yugura oladi."]),
            TFE("“He have to go now.” — to‘g‘ri gap.", False, say="He have to go now.",
                x="he bilan has to: He has to go now."),
            TFE("“You shouldn't eat too much sugar.” — to‘g‘ri maslahat.", True,
                say="You shouldn't eat too much sugar.", x="To‘g‘ri: shakarni ko‘p yemaslik kerak."),
            SENT("You should ask your teacher for help", x="You should ask your teacher for help. — O‘qituvchingizdan yordam so‘rashingiz kerak."),
            GAP("It's Saturday! I ... get up early.", "don't have to", ["mustn't", "have to", "has to"], d=2,
                x="Shanba — erta turish shart emas: don't have to."),
            GAP("Visitors ... touch the paintings in the museum.", "mustn't", ["don't have to", "have to", "should"], d=2,
                x="Muzeyda rasmlarga tegish taqiqlangan — mustn't."),
            GAP("... I have to bring my own lunch?", "Do", ["Does", "Am", "Must"], d=2,
                x="I bilan savol: Do I have to …?"),
            EN("“don't have to” nimani bildiradi?", "shart emas", ["mumkin emas", "kerak", "qila olmaydi"], say="don't have to", d=2,
              x="don't have to — shart emas, majbur emas."),
            MATCH("Modal fe’lni ma’nosi bilan juftlang",
                  [("should", "maslahat"), ("mustn't", "taqiq"), ("have to", "majburiyat"),
                   ("don't have to", "shart emas"), ("can", "qobiliyat yoki ruxsat")], d=2, lang="en"),
            LISTEN("You don't have to come with us.", "Biz bilan kelishing shart emas.",
                   ["Biz bilan kelishing mumkin emas.", "Biz bilan kelishing kerak.", "Biz bilan kela olmaysan."], d=2),
            Q("Suzish havzasi qoidasi uchun mos gapni tanlang", "You have to wear a swimming cap.",
              ["You mustn't wear a swimming cap.", "You has to wear a swimming cap.", "You should to wear a swimming cap."],
              d=2, x="Havzada shapka kiyish majburiy: You have to wear a swimming cap."),
            EN("Maslahat bering: “I'm always tired.”", "You should go to bed earlier.",
               ["You should go to bed later.", "You mustn't sleep.", "You have to watch more TV."],
               say="I'm always tired.", d=2, x="Doim charchasangiz — ertaroq yotishingiz kerak."),
            SENT("We don't have to do homework today", d=2, x="We don't have to do homework today. — Bugun uy vazifasi qilishimiz shart emas."),
            GAP("She ... take the bus because her bike was broken.", "had to", ["has to", "have to", "must"], d=3,
                x="O‘tgan zamon (was broken): had to."),
            GAP("Does he have to work tomorrow? — Yes, he ...", "does", ["has", "have", "is"], d=3,
                x="Does …? savoliga qisqa javob: Yes, he does."),
            LISTEN("I had to finish my project last night.", "Kecha kechqurun loyihamni tugatishim kerak edi.",
                   ["Bugun loyihamni tugatishim kerak.", "Kecha loyihamni tugatmadim.",
                    "Loyihamni tugatishim shart emas edi."], d=3),
            Q("Qaysi gap to‘g‘ri?", "She doesn't have to cook tonight.",
              ["She don't have to cook tonight.", "She doesn't has to cook tonight.", "She hasn't to cooking tonight."],
              d=3, x="she bilan inkor: doesn't have to (has emas)."),
            QSENT("Do we have to take a test tomorrow", d=3, x="Do we have to take a test tomorrow? — Ertaga test topshirishimiz shartmi?"),
        ])

T.topic("body", "👀", L("Tana a’zolari", "Parts of the body", "Части тела"),
        chapter=C2, gen="vocab", prereq=["health"],
        theory="Tana a’zolari: head (bosh), eye (ko‘z), ear (quloq), nose (burun), mouth (og‘iz), tongue (til),\n"
               "tooth (tish), hand (qo‘l panjasi), foot (oyoq panjasi), shoulder (yelka), back (bel, orqa).\n"
               "Ichki a’zolar: brain (miya), heart (yurak), muscle (mushak), bone (suyak).\n"
               "Maxsus ko‘plik: tooth → teeth, foot → feet.  We see with our eyes and hear with our ears.",
        levels=vocab_levels(["body"]))

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["future", "health", "modals", "body"], chapter=C2)

# ============================================================ 3-chorak
T.topic("comparatives", "📏", L("Taqqoslash: -er, the most, as … as", "Comparison: -er, the most, as … as",
                               "Сравнение: -er, the most, as … as"),
        chapter=C3,
        theory="Qiyosiy daraja: -er / more + than: A plane is faster than a train. This book is more interesting than that one.\n"
               "Orttirma daraja: the -est / the most: Mount Everest is the highest mountain in the world.\n"
               "Maxsus: good → better → the best; bad → worse → the worst.\n"
               "as … as — xuddi … dek (teng): Anvar is as tall as his father.\n"
               "not as … as — … chalik emas: A bike isn't as fast as a car.",
        items=[
            GAP("My sister is as tall ... my mum.", "as", ["than", "like", "so"], x="as … as — xuddi … dek."),
            GAP("A bicycle isn't as fast ... a car.", "as", ["than", "that", "then"], x="not as … as — … chalik emas."),
            GAP("Today is ... than yesterday.", "warmer", ["warm", "warmest", "more warm"], x="than bilan -er: warmer than."),
            GAP("Mount Everest is the ... mountain in the world.", "highest", ["higher", "most high", "high"],
                x="Eng baland — the highest. Everest — dunyodagi eng baland tog‘."),
            FORM("heavy", "sifatining qiyosiy darajasi", "heavier", ["heavyer", "more heavy", "heavyest"],
                 x="Undosh + y → -ier: heavier."),
            FORM("interesting", "sifatining qiyosiy darajasi", "more interesting",
                 ["interestinger", "most interesting", "interestinger than"], x="Uzun sifat — more: more interesting."),
            Q("Qaysi gap to‘g‘ri? (fakt)", "The Sun is bigger than the Moon.",
              ["The Moon is bigger than the Sun.", "The Moon is as big as the Sun.", "The Earth is bigger than the Sun."],
              x="Quyosh Oydan ham, Yerdan ham ancha katta."),
            TFE("“He is as clever as his sister.” — to‘g‘ri gap.", True, say="He is as clever as his sister.",
                x="To‘g‘ri: as + sifat + as."),
            TFE("“She is more taller than me.” — to‘g‘ri gap.", False, say="She is more taller than me.",
                x="taller — o‘zi qiyosiy daraja, more qo‘shilmaydi: She is taller than me."),
            EN("Ma’nosi mos gapni tanlang: Ali is 150 cm tall. Vali is 150 cm tall.", "Ali is as tall as Vali.",
               ["Ali is taller than Vali.", "Ali isn't as tall as Vali.", "Vali is the tallest."],
               say="Ali is 150 centimetres tall. Vali is 150 centimetres tall.",
               x="Bo‘ylari teng — as tall as."),
            SENT("Winter is colder than autumn", x="Winter is colder than autumn. — Qish kuzdan sovuqroq."),
            GAP("The Pacific is the ... ocean on Earth.", "largest", ["larger", "most large", "large"], d=2,
                x="Tinch okeani — Yerdagi eng katta okean: the largest."),
            GAP("Maths is ... difficult than English for me.", "more", ["most", "much", "as"], d=2,
                x="Uzun sifat: more difficult than."),
            GAP("My handwriting is ... than my brother's.", "worse", ["badder", "worst", "more bad"], d=2,
                x="bad → worse → the worst."),
            GAP("Cheetahs are the ... animals on land.", "fastest", ["faster", "most fast", "fast"], d=2,
                x="Gepard — quruqlikdagi eng tez hayvon: the fastest."),
            FORM("thin", "sifatining qiyosiy darajasi", "thinner", ["thiner", "more thin", "thinnest"], d=2,
                 x="Unli + undosh: undosh ikkilanadi — thinner."),
            FORM("famous", "sifatining orttirma darajasi", "the most famous",
                 ["the famousest", "the more famous", "most famous the"], d=2, x="Uzun sifat: the most famous."),
            FORM("busy", "sifatining orttirma darajasi", "the busiest", ["the busyest", "the most busy", "the busier"], d=2,
                 x="Undosh + y → -iest: the busiest."),
            Q("Qaysi gap to‘g‘ri? (fakt)", "A blue whale is heavier than an elephant.",
              ["An elephant is heavier than a blue whale.", "A mouse is as heavy as an elephant.",
               "A cat is heavier than a horse."], d=2, x="Ko‘k kit — dunyodagi eng og‘ir hayvon."),
            MATCH("Sifatni orttirma darajasi bilan juftlang",
                  [("good", "the best"), ("bad", "the worst"), ("big", "the biggest"), ("happy", "the happiest"),
                   ("beautiful", "the most beautiful"), ("cheap", "the cheapest")], d=2, lang="en"),
            LISTEN("This test was easier than the last one.", "Bu test oldingisidan osonroq edi.",
                   ["Bu test oldingisidan qiyinroq edi.", "Bu test eng oson test edi.", "Bu test oldingisidek oson edi."],
                   d=2),
            SENT("This is the most expensive phone in the shop", d=2,
                 x="This is the most expensive phone in the shop. — Bu do‘kondagi eng qimmat telefon."),
            GAP("This is the ... film I've ever seen.", "best", ["better", "good", "most good"], d=3,
                x="Eng yaxshi — the best."),
            EN("Ma’nosi mos gapni tanlang: A bus is slower than a train.", "A bus isn't as fast as a train.",
               ["A bus is as fast as a train.", "A train isn't as fast as a bus.", "A bus is the fastest."],
               say="A bus is slower than a train.", d=3, x="slower than = not as fast as."),
            LISTEN("My room isn't as big as yours.", "Mening xonam senikichalik katta emas.",
                   ["Mening xonam senikidan kattaroq.", "Mening xonam seniki bilan bir xil katta.",
                    "Sening xonang meniki kabi kichik."], d=3),
            SENT("My bike is not as new as yours", d=3, x="My bike is not as new as yours. — Mening velosipedim senikichalik yangi emas."),
        ])

T.topic("opposites", "↔️", L("Qarama-qarshi sifatlar", "Opposite adjectives", "Противоположные прилагательные"),
        chapter=C3, gen="opposites", prereq=["comparatives"],
        theory="Qarama-qarshi sifatlar: big — small, long — short, hot — cold, fast — slow,\n"
               "old — young, happy — sad, loud — quiet, open — closed.\n"
               "Taqqoslashda ham ishlatamiz: A snail is slower than a rabbit. The Arctic is colder than the desert.\n"
               "not as … as bilan: A mouse isn't as big as a cat. = A mouse is smaller than a cat.",
        levels=[{"modes": ["size", "length", "read"], "options": 3},
                {"modes": ["read", "listen"], "options": 4},
                {"modes": ["read", "listen"], "options": 4}])

T.topic("shopping", "🛍️", L("Do‘konda: pul va miqdor", "Shopping: money and quantity", "Покупки: деньги и количество"),
        chapter=C3, prereq=["comparatives"],
        theory="Do‘konda: How much is it? / How much are they? — It's £5. / They're £3.50 (three pounds fifty).\n"
               "Can I help you? — Yes, I'd like a T-shirt, please. Can I try it on? Here's your change.\n"
               "much — sanalmaydigan otlar bilan (money, water, time), many — sanaladigan (apples, shops):\n"
               "How much money? How many books?  a lot of — ikkalasi bilan: a lot of people, a lot of sugar.\n"
               "some — darak gapda, any — savol va inkorda, no = not any: There's no milk. = There isn't any milk.",
        items=[
            GAP("How ... is this jacket? — It's £40.", "much", ["many", "any", "lot"],
                x="Narx so‘ralganda — How much?"),
            GAP("How ... apples do you need? — Six, please.", "many", ["much", "any", "lot of"],
                x="apples sanaladi — How many?"),
            GAP("I haven't got ... money left.", "any", ["some", "many", "no"], x="Inkor gapda — any."),
            Q("“Qancha turadi?” (bitta narsa) inglizcha qanday?", "How much is it?",
              ["How many is it?", "How much are it?", "What costs it?"], x="Narx: How much is it?"),
            EN("Qaysi so‘z bilan “many” ishlatiladi?", "bananas", ["milk", "sugar", "money"], say="many",
              x="bananas — sanaladi: many bananas."),
            LISTEN("Can I help you?", "Sizga yordam bera olamanmi?",
                   ["Menga yordam bera olasizmi?", "Qancha turadi?", "Kiyib ko‘rsam bo‘ladimi?"]),
            TFE("“How many milk do you want?” — to‘g‘ri gap.", False, say="How many milk do you want?",
                x="milk sanalmaydi: How much milk do you want?"),
            TFE("“There is no juice in the fridge.” = “There isn't any juice in the fridge.”", True,
                say="There is no juice in the fridge. There isn't any juice in the fridge.",
                x="To‘g‘ri: no = not any."),
            EN("Sotuvchi: “That's £7, please.” Siz £10 berdingiz. Qaytimi qancha?", "£3", ["£7", "£17", "£2"],
               say="That's seven pounds, please.", x="10 − 7 = 3 funt qaytim (change)."),
            SENT("I would like a kilo of apples", x="I would like a kilo of apples. — Menga bir kilo olma bering."),
            Q("Qaysi so‘z sanalmaydi?", "money", ["coin", "pound", "shop"],
              x="money — sanalmaydi (How much money?); coins, pounds — sanaladi."),
            GAP("There are ... people in the market today.", "a lot of", ["much", "a lot", "any"], d=2,
                x="Ko‘p odam — a lot of people (much — sanalmaydiganlar bilan)."),
            GAP("There's ... bread. Let's buy some.", "no", ["any", "some", "many"], d=2,
                x="Non yo‘q — There's no bread."),
            GAP("We don't have ... time. Hurry up!", "much", ["many", "a lot", "no"], d=2,
                x="time sanalmaydi, inkorda — much."),
            GAP("Can I try it ...? — Of course. The changing room is over there.", "on", ["in", "at", "up"], d=2,
                x="try on — kiyib ko‘rmoq."),
            Q("£2.50 qanday o‘qiladi?", "two pounds fifty", ["two fifty pounds", "two pound fifty", "twenty-five pounds"],
              d=2, x="£2.50 — two pounds fifty (ikki funt ellik pens)."),
            MATCH("Do‘kon va nima sotishini juftlang",
                  [("baker's", "bread and cakes"), ("butcher's", "meat"), ("chemist's", "medicine"),
                   ("greengrocer's", "fruit and vegetables"), ("newsagent's", "newspapers"), ("bookshop", "books")],
                  d=2, lang="en"),
            LISTEN("I'd like two bottles of water, please.", "Ikki shisha suv bering, iltimos.",
                   ["Ikki stakan suv bering, iltimos.", "Ikki shisha sharbat bering, iltimos.", "Menga suv kerak emas."],
                   d=2),
            EN("“How much are these trainers?” savoliga mos javobni tanlang", "They're £35.",
               ["It's £35.", "There are 35.", "They're 35 trainers."], say="How much are these trainers?", d=2,
               x="trainers — ko‘plik, shuning uchun They're £35."),
            QSENT("How much is this red T-shirt", d=2, x="How much is this red T-shirt? — Bu qizil futbolka qancha turadi?"),
            GAP("Here's your ... . — Thank you.", "change", ["changes", "chance", "charge"], d=3,
                x="change — qaytim (pul)."),
            LISTEN("It's too expensive. Have you got a cheaper one?", "Bu juda qimmat. Arzonrog‘i bormi?",
                   ["Bu juda arzon. Qimmatrog‘i bormi?", "Bu juda qimmat. Kattarog‘i bormi?", "Bu arzon. Men olaman."],
                   d=3),
            Q("Kiyimni sotib olishdan oldin nima so‘raymiz?", "Can I try it on?",
              ["Can I try it in?", "Can I try on it?", "Can I wear it off?"], d=3,
              x="try on + olmosh: try it on (try on it — xato)."),
            SENT("There are not many shops in our village", d=3,
                 x="There are not many shops in our village. — Qishlog‘imizda do‘konlar ko‘p emas."),
        ])

T.topic("technology", "💻", L("Texnologiya va internet", "Technology and the internet", "Технологии и интернет"),
        chapter=C3,
        theory="Qurilmalar: computer, laptop (noutbuk), tablet (planshet), smartphone, screen (ekran), keyboard (klaviatura),\n"
               "mouse (sichqoncha), printer, headphones (quloqchin), charger (quvvatlagich).\n"
               "Harakatlar: switch on / switch off (yoqmoq / o‘chirmoq), type (terish), download (yuklab olish),\n"
               "upload (joylash), save (saqlash), send a message, search the internet.\n"
               "Xavfsizlik: password (parol) — uni hech kimga aytmang! Notanish odamlarga shaxsiy ma’lumot yubormang.",
        items=[
            Q("“Parol” inglizcha qanday?", "password", ["passport", "username", "keyboard"], x="password — parol."),
            Q("“Klaviatura” inglizcha qanday?", "keyboard", ["screen", "mouse", "printer"], x="keyboard — klaviatura."),
            Q("Qaysi qurilma bilan hujjatni qog‘ozga chiqaramiz?", "a printer", ["a speaker", "a keyboard", "a webcam"],
              x="printer — hujjatni qog‘ozga chiqaradi."),
            Q("Faqat o‘zimiz musiqa eshitishimiz uchun nima kerak?", "headphones", ["a printer", "a mouse", "a keyboard"],
              x="headphones — quloqchin."),
            GAP("Please switch ... your phones during the lesson.", "off", ["on", "in", "up"],
                x="Darsda telefon o‘chiriladi: switch off."),
            GAP("My brother sent me a ... on my phone.", "message", ["keyboard", "screen", "password"],
                x="send a message — xabar yubormoq."),
            GAP("You should never tell anyone your ...", "password", ["keyboard", "screen", "laptop"],
                x="Parolni hech kimga aytmaymiz."),
            GAP("She is typing a letter on her ...", "laptop", ["headphones", "charger", "speaker"],
                x="Xatni noutbukda terish mumkin: laptop."),
            MATCH("So‘zni tarjimasi bilan juftlang",
                  [("screen", "ekran"), ("keyboard", "klaviatura"), ("laptop", "noutbuk"), ("headphones", "quloqchin"),
                   ("password", "parol"), ("download", "yuklab olmoq"), ("save", "saqlamoq")], lang="en"),
            LISTEN("Can you send me the photos?", "Menga suratlarni yubora olasanmi?",
                   ["Senga suratlarni yubordim.", "Suratlarni o‘chira olasanmi?", "Menga video yubora olasanmi?"]),
            TF("Parolni do‘stlarga aytish xavfsiz.", False, x="Parol sir saqlanadi — uni hech kimga aytmang."),
            TFE("“switch on” — o‘chirmoq degani.", False, say="switch on",
                x="switch on — yoqmoq; switch off — o‘chirmoq."),
            SENT("I use my tablet to read books", x="I use my tablet to read books. — Kitob o‘qish uchun planshetimdan foydalanaman."),
            Q("“Yuklab olmoq” inglizcha qanday?", "download", ["upload", "delete", "print"], d=2,
              x="download — yuklab olish; upload — joylash."),
            GAP("Don't forget to ... your work before you close the file.", "save", ["delete", "switch", "send off"], d=2,
                x="Faylni yopishdan oldin saqlaymiz: save."),
            GAP("I ... the internet to find information for my project.", "searched", ["looked", "saw", "watched"], d=2,
                x="search the internet — internetdan qidirmoq."),
            TFE("“upload” — internetga (saytga) fayl joylash degani.", True, say="upload", d=2,
                x="To‘g‘ri: upload — joylash; download — yuklab olish."),
            Q("Qaysi so‘z qurilma emas?", "website", ["laptop", "tablet", "smartphone"], d=2,
              x="website — veb-sayt, u qurilma emas."),
            LISTEN("The battery is low. I need to charge my phone.", "Batareya kam. Telefonimni quvvatlashim kerak.",
                   ["Batareya to‘la. Telefonim tayyor.", "Telefonim buzildi.", "Batareya kam. Yangi telefon sotib olaman."],
                   d=2),
            EN("“How often do you use a computer?” savoliga mos javobni tanlang", "Every day, for my homework.",
               ["It's in my room.", "It's a new laptop.", "Yes, I do."], say="How often do you use a computer?", d=2,
               x="How often? — qanchalik tez-tez? Javob: Every day."),
            SENT("Never open emails from strangers", d=2, x="Never open emails from strangers. — Notanishlardan kelgan xatlarni hech qachon ochmang."),
            GAP("I can't hear the video. Can you turn ... the volume?", "up", ["on", "off", "in"], d=3,
                x="turn up the volume — ovozni balandlatmoq."),
            LISTEN("Don't share your personal information online.", "Shaxsiy ma’lumotlaringizni internetda ulashmang.",
                   ["Shaxsiy ma’lumotlaringizni internetda ulashing.", "Internetdan ma’lumot izlang.",
                    "Do‘stlaringizga xat yozing."], d=3),
            Q("Internetda ma’lumot qidirish uchun nimadan foydalanamiz?", "a search engine",
              ["a printer", "a charger", "a speaker"], d=3, x="search engine — qidiruv tizimi."),
            QSENT("Can you help me with this program", d=3, x="Can you help me with this program? — Shu dasturda menga yordam bera olasanmi?"),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["comparatives", "opposites", "shopping", "technology"], chapter=C3)

# ============================================================ 4-chorak
T.topic("present_perfect", "✅", L("Present Perfect: ever, never, just, already", "Present Perfect",
                                  "Present Perfect"),
        chapter=C4, prereq=["past_simple"],
        theory="Present Perfect — have / has + fe’lning 3-shakli (V3): I have visited Bukhara. She has finished her work.\n"
               "To‘g‘ri fe’llarda V3 = -ed: play → played. Noto‘g‘ri: see → seen, be → been, eat → eaten, do → done,\n"
               "write → written, go → gone, take → taken.\n"
               "Tajriba: Have you ever been to Khiva? — Yes, I have. / No, I've never been there.\n"
               "just — hozirgina: I've just had lunch.  already — allaqachon: She has already done her homework.\n"
               "yet — hali (savol va inkorda, gap oxirida): Have you finished yet? I haven't finished yet.",
        items=[
            GAP("I ... visited the Registan three times.", "have", ["has", "am", "did"], x="I bilan have + V3."),
            GAP("She ... just finished her homework.", "has", ["have", "is", "did"], x="she bilan has + V3."),
            GAP("We have ... that film. It's great!", "seen", ["saw", "see", "seeing"], x="have + V3: see → seen."),
            FORM("do", "fe’lining 3-shakli (V3)", "done", ["did", "doed", "does"], x="do → did → done."),
            FORM("see", "fe’lining 3-shakli (V3)", "seen", ["saw", "seed", "sawn"], x="see → saw → seen."),
            TFE("“He has lost his keys.” — to‘g‘ri gap.", True, say="He has lost his keys.",
                x="To‘g‘ri: has + lost (lose → lost → lost)."),
            TFE("“I have saw this cartoon.” — to‘g‘ri gap.", False, say="I have saw this cartoon.",
                x="have + V3: I have seen this cartoon."),
            EN("“just” so‘zi Present Perfect gapida nimani bildiradi?", "hozirgina", ["hech qachon", "hali", "ertaga"], say="I've just arrived.",
              x="just — hozirgina: I've just arrived."),
            SENT("I have already read this book", x="I have already read this book. — Men bu kitobni allaqachon o‘qiganman."),
            GAP("Have you ever ... to the sea?", "been", ["be", "was", "went"], d=2,
                x="Tajriba haqida: Have you ever been to …?"),
            GAP("I have never ... sushi.", "eaten", ["ate", "eat", "eated"], d=2, x="eat → ate → eaten."),
            GAP("They have ... left. You can't see them now.", "already", ["yet", "ever", "never"], d=2,
                x="already — allaqachon."),
            GAP("Has the film started ...?", "yet", ["already", "just", "ever"], d=2,
                x="Savolda gap oxirida — yet (hali … mi?)."),
            GAP("I'm not hungry. I've ... had lunch.", "just", ["yet", "ever", "never"], d=2,
                x="just — hozirgina tushlik qildim."),
            FORM("write", "fe’lining 3-shakli (V3)", "written", ["wrote", "writed", "writen"], d=2,
                 x="write → wrote → written (ikkita t)."),
            FORM("go", "fe’lining 3-shakli (V3)", "gone", ["went", "goed", "goes"], d=2, x="go → went → gone."),
            MATCH("Fe’lni 3-shakli bilan juftlang",
                  [("be", "been"), ("eat", "eaten"), ("do", "done"), ("see", "seen"), ("write", "written"),
                   ("take", "taken"), ("speak", "spoken")], d=2, lang="en"),
            EN("“Have you ever been to Khiva?” savoliga mos javobni tanlang", "No, I haven't.",
               ["No, I didn't.", "No, I wasn't.", "No, I haven't been never."], say="Have you ever been to Khiva?", d=2,
               x="Have …? savoliga qisqa javob: Yes, I have. / No, I haven't."),
            EN("Qisqa javobni tanlang: Has Madina finished her project?", "Yes, she has.",
               ["Yes, she did.", "Yes, she is.", "Yes, she have."], say="Has Madina finished her project?", d=2,
               x="Has …? savoliga: Yes, she has."),
            LISTEN("I have never flown in a plane.", "Men hech qachon samolyotda uchmaganman.",
                   ["Men har doim samolyotda uchaman.", "Men kecha samolyotda uchdim.", "U hech qachon samolyotda uchmagan."],
                   d=2),
            LISTEN("She has already cleaned her room.", "U xonasini allaqachon yig‘ishtirib qo‘ydi.",
                   ["U hali xonasini yig‘ishtirmadi.", "U hozir xonasini yig‘ishtiryapti.",
                    "Men xonamni allaqachon yig‘ishtirdim."], d=2),
            SENT("My parents have never been to London", d=2,
                 x="My parents have never been to London. — Ota-onam hech qachon Londonda bo‘lishmagan."),
            FORM("break", "fe’lining 3-shakli (V3)", "broken", ["broke", "breaked", "brokened"], d=3,
                 x="break → broke → broken."),
            LISTEN("Have you done your homework yet?", "Uy vazifangni bajarib bo‘ldingmi?",
                   ["Uy vazifangni qachon bajarasan?", "Uy vazifasi qiyinmi?", "Uy vazifangni kecha bajardingmi?"], d=3),
            Q("Qaysi gap to‘g‘ri?", "She hasn't called me yet.",
              ["She hasn't called me already.", "She didn't called me yet.", "She hasn't call me yet."], d=3,
              x="Inkorda gap oxirida yet: She hasn't called me yet."),
            QSENT("Have you ever seen a dolphin", d=3, x="Have you ever seen a dolphin? — Hech delfin ko‘rganmisan?"),
        ])

T.topic("environment", "♻️", L("Atrof-muhitni asrash", "The environment", "Окружающая среда"),
        chapter=C4, prereq=["modals"],
        theory="Muammolar: pollution (ifloslanish), rubbish (axlat), plastic, cutting down trees, wasting water (suvni isrof qilish).\n"
               "Yechimlar: recycle (qayta ishlash), reuse (qayta foydalanish), reduce (kamaytirish), plant trees,\n"
               "save water and energy (suv va energiyani tejash).\n"
               "Maslahatlar: We should turn off the lights. We shouldn't drop litter. Take a reusable bag to the shop.\n"
               "Tabiat: forest, river, lake, desert, ocean, air, wildlife (yovvoyi tabiat).",
        items=[
            Q("“axlat” britan inglizchasida qanday?", "rubbish", ["rubber", "robbery", "rabbit"],
              x="Britaniyada axlat — rubbish."),
            Q("“qayta ishlamoq” (chiqindini) inglizcha qanday?", "recycle", ["reply", "repeat", "return"],
              x="recycle — qayta ishlash (qog‘oz, shisha, plastik)."),
            Q("Daraxtlar havoga nima chiqaradi?", "oxygen", ["plastic", "smoke", "rubbish"],
              x="Daraxtlar kislorod (oxygen) chiqaradi."),
            GAP("We should ... off the lights when we leave the room.", "turn", ["make", "do", "put"],
                x="turn off — o‘chirmoq."),
            GAP("Let's ... some trees in the school garden.", "plant", ["cut", "burn", "drop"], x="plant trees — daraxt ekmoq."),
            GAP("Close the tap. Don't ... water.", "waste", ["save", "drink", "recycle"], x="waste water — suvni isrof qilmoq."),
            GAP("You can ... plastic bottles, paper and glass.", "recycle", ["waste", "pollute", "grow"],
                x="Plastik, qog‘oz va shishani qayta ishlash mumkin: recycle."),
            MATCH("So‘zni tarjimasi bilan juftlang",
                  [("pollution", "ifloslanish"), ("rubbish", "axlat"), ("recycle", "qayta ishlamoq"),
                   ("environment", "atrof-muhit"), ("plant", "ekmoq"), ("save", "tejamoq"), ("bin", "axlat qutisi")],
                  lang="en"),
            LISTEN("We should use less plastic.", "Kamroq plastik ishlatishimiz kerak.",
                   ["Ko‘proq plastik ishlatishimiz kerak.", "Biz plastik ishlatmaymiz.", "Plastik juda arzon."]),
            TFE("“We should throw rubbish into the river.” — to‘g‘ri maslahat.", False,
                say="We should throw rubbish into the river.", x="Daryoga axlat tashlash — tabiatga zarar."),
            Q("Qaysi harakat tabiatga foydali?", "planting trees",
              ["cutting down forests", "dropping litter", "wasting electricity"], x="Daraxt ekish — tabiatga foydali."),
            Q("Qaysi gap to‘g‘ri maslahat?", "Take a reusable bag to the shop.",
              ["Buy a new plastic bag every day.", "Leave the TV on all night.", "Throw batteries in the river."],
              x="reusable bag — qayta ishlatiladigan sumka."),
            SENT("We must protect wild animals", x="We must protect wild animals. — Yovvoyi hayvonlarni himoya qilishimiz kerak."),
            Q("“ifloslanish” inglizcha qanday?", "pollution", ["population", "solution", "position"], d=2,
              x="pollution — ifloslanish; population — aholi."),
            GAP("Don't drop ... in the street. Put it in the bin.", "litter", ["leaves", "water", "trees"], d=2,
                x="litter — ko‘chaga tashlangan axlat."),
            GAP("Cars and factories ... the air.", "pollute", ["clean", "recycle", "plant"], d=2,
                x="pollute — ifloslantirmoq."),
            TFE("“reuse” — narsadan yana foydalanish degani.", True, say="reuse", d=2,
                x="To‘g‘ri: reuse — qayta foydalanmoq."),
            TF("Orol dengizi 1960-yillardan beri ancha kichrayib ketgan.", True, d=2,
               x="Orol dengizi suvi kamayib, ancha kichrayib qolgan — bu katta ekologik muammo."),
            LISTEN("The river is very dirty because of the factory.", "Zavod tufayli daryo juda iflos.",
                   ["Zavod tufayli daryo juda toza.", "Daryo tufayli zavod juda iflos.", "Daryo zavod yonida."], d=2),
            SENT("Let's pick up the litter in the park", d=2, x="Let's pick up the litter in the park. — Keling, bog‘dagi axlatni terib olaylik."),
            LISTEN("Walking or cycling is better for the environment than driving.",
                   "Piyoda yoki velosipedda yurish atrof-muhit uchun mashinada yurishdan yaxshiroq.",
                   ["Mashinada yurish atrof-muhit uchun eng yaxshisi.", "Velosiped mashinadan tezroq.",
                    "Piyoda yurish mashinada yurishdan qiyinroq."], d=3),
            Q("Qaysi so‘z “yovvoyi tabiat” degani?", "wildlife", ["wild card", "lifestyle", "lifetime"], d=3,
              x="wildlife — yovvoyi hayvonlar va o‘simliklar dunyosi."),
            GAP("Plastic takes hundreds of years to break ...", "down", ["up", "out", "in"], d=3,
                x="break down — parchalanmoq. Plastik yuzlab yil parchalanmaydi."),
            SENT("Paper and glass can be recycled", d=3, x="Paper and glass can be recycled. — Qog‘oz va shishani qayta ishlash mumkin."),
            QSENT("How can we save energy at home", d=3, x="How can we save energy at home? — Uyda energiyani qanday tejash mumkin?"),
        ])

T.topic("nature", "🌍", L("Tabiat va hayvonot dunyosi", "Nature and wildlife", "Природа и животный мир"),
        chapter=C4, gen="vocab", prereq=["environment"],
        theory="Tabiat: mountain (tog‘), desert (cho‘l), island (orol), volcano (vulqon), forest (o‘rmon), sea (dengiz).\n"
               "Hayvonlar va qushlar: eagle (burgut), owl (boyqush), dolphin (delfin), whale (kit), crocodile (timsoh).\n"
               "Hasharotlar: bee (asalari), butterfly (kapalak), ant (chumoli), spider (o‘rgimchak).\n"
               "Misol: Bees are very important for flowers and fruit trees.",
        levels=vocab_levels(["animals_nature"]))

R1 = ("Last spring, Zarina and her family went to Samarkand for three days. They travelled by high-speed train, "
      "and the journey took about two hours. On the first day, they visited the Registan. Zarina thought the blue "
      "tiles were beautiful. On the second day, they went to a paper workshop and watched how people made paper "
      "from the bark of mulberry trees. Zarina bought a small notebook as a souvenir. She wants to go back one day.")
R2 = ("Sardor wasn't at school on Monday. He had a bad cold, a sore throat and a temperature. His mother took him "
      "to the doctor. The doctor told him to stay in bed, drink a lot of warm drinks and take his medicine. She also "
      "said, 'You shouldn't play outside until you feel better.' Sardor was bored at home, so he read two books. "
      "By Thursday he felt much better and went back to school.")
R3 = ("Next summer, Nodira is going to take part in a science camp in the mountains. She's going to study plants "
      "and insects with other students. The camp will last two weeks. Nodira is a bit nervous because she has never "
      "been away from her family for so long. But her older brother says she'll love it and make a lot of new friends.")
R4 = ("Our school has started a 'Green Week'. Every class has a job. Class 6A is collecting plastic bottles for "
      "recycling. Class 6B is planting trees near the sports ground. The younger pupils are making posters about "
      "saving water and electricity. Our teacher says that small actions can make a big difference. I think she's "
      "right: we have already collected more than five hundred bottles!")
R5 = ("Timur and his grandfather both love technology, but in different ways. Timur uses a smartphone and a laptop "
      "every day. His grandfather prefers his old radio and a paper newspaper. 'The news on my radio is as "
      "interesting as your internet,' he says with a smile. Last month Timur taught his grandfather how to make "
      "video calls. Now Grandad calls his friends in Andijan every Sunday.")

T.topic("reading", "📖", L("O‘qib tushunish", "Reading comprehension", "Чтение и понимание"),
        chapter=C4,
        theory="Uzun matnni o‘qishdan oldin sarlavha yoki birinchi gapga qarang — matn nima haqida?\n"
               "Savolni o‘qing va kalit so‘zni (ism, son, joy, vaqt) matndan qidiring.\n"
               "Javob ba’zan boshqa so‘zlar bilan berilgan bo‘ladi: “felt much better” = “got well”.\n"
               "True / False: fikrning hamma qismi matnga mos kelsagina — To‘g‘ri.",
        items=[
            READ(R1, "How long did Zarina's family stay in Samarkand?", "three days",
                 ["two days", "a week", "two hours"], x="Matnda: went to Samarkand for three days."),
            READ(R1, "How did they travel?", "by high-speed train", ["by plane", "by car", "by bus"],
                 x="Matnda: They travelled by high-speed train."),
            RTF(R1, "They visited the Registan on the first day.", True, x="Matnda: On the first day, they visited the Registan."),
            READ(R2, "Why wasn't Sardor at school?", "He was ill.", ["He was on holiday.", "He was late.", "He was at a camp."],
                 x="Matnda: He had a bad cold, a sore throat and a temperature."),
            READ(R2, "Who took Sardor to the doctor?", "his mother", ["his father", "his teacher", "his brother"],
                 x="Matnda: His mother took him to the doctor."),
            RTF(R2, "Sardor read two books at home.", True, x="Matnda: so he read two books."),
            READ(R3, "Where is the science camp?", "in the mountains", ["by the sea", "in the city", "in the desert"],
                 x="Matnda: a science camp in the mountains."),
            READ(R3, "How long will the camp last?", "two weeks", ["two days", "one month", "one week"],
                 x="Matnda: The camp will last two weeks."),
            READ(R4, "What is Class 6B doing?", "planting trees", ["collecting bottles", "making posters", "saving water"],
                 x="Matnda: Class 6B is planting trees near the sports ground."),
            READ(R5, "What does Timur's grandfather prefer?", "his old radio and a paper newspaper",
                 ["a smartphone and a laptop", "video games", "a new television"],
                 x="Matnda: His grandfather prefers his old radio and a paper newspaper."),
            RTF(R5, "Timur never uses a laptop.", False, x="Matnda: Timur uses a smartphone and a laptop every day."),
            READ(R1, "What did Zarina buy as a souvenir?", "a small notebook", ["a blue tile", "a mulberry tree", "a train ticket"],
                 d=2, x="Matnda: Zarina bought a small notebook as a souvenir."),
            READ(R1, "What is the paper made from?", "the bark of mulberry trees",
                 ["plastic bottles", "old newspapers", "cotton"], d=2,
                 x="Matnda: people made paper from the bark of mulberry trees."),
            RTF(R2, "The doctor said Sardor should play outside.", False, d=2,
                x="Matnda: You shouldn't play outside until you feel better."),
            READ(R2, "When did Sardor go back to school?", "by Thursday", ["on Monday", "on Tuesday", "next week"], d=2,
                 x="Matnda: By Thursday he felt much better and went back to school."),
            READ(R3, "What is Nodira going to study?", "plants and insects", ["stars and planets", "rocks", "birds only"],
                 d=2, x="Matnda: She's going to study plants and insects."),
            READ(R3, "Who thinks Nodira will love the camp?", "her older brother", ["her mother", "her teacher", "Nodira"],
                 d=2, x="Matnda: her older brother says she'll love it."),
            READ(R4, "What are the younger pupils making?", "posters", ["cakes", "bird houses", "bottles"], d=2,
                 x="Matnda: The younger pupils are making posters."),
            RTF(R4, "The school has collected fewer than one hundred bottles.", False, d=2,
                x="Matnda: more than five hundred bottles — 500 dan ortiq."),
            READ(R5, "What did Timur teach his grandfather last month?", "how to make video calls",
                 ["how to read a newspaper", "how to fix a radio", "how to take photos"], d=2,
                 x="Matnda: Timur taught his grandfather how to make video calls."),
            READ(R3, "Why is Nodira nervous?", "She has never been away from her family for so long.",
                 ["She doesn't like insects.", "She can't find the camp.", "Her brother is going too."], d=3,
                 x="Matnda: she has never been away from her family for so long."),
            READ(R4, "What does the teacher think?", "Small actions can make a big difference.",
                 ["Recycling is not important.", "Only adults can help nature.", "Posters are boring."], d=3,
                 x="Matnda: Our teacher says that small actions can make a big difference."),
            RTF(R5, "The grandfather thinks the radio news is as interesting as the internet.", True, d=3,
                x="Matnda: The news on my radio is as interesting as your internet."),
            READ(R5, "When does Grandad call his friends now?", "every Sunday", ["every day", "on Mondays", "never"], d=3,
                 x="Matnda: Now Grandad calls his friends in Andijan every Sunday."),
            RTF(R1, "Zarina never wants to visit Samarkand again.", False, d=3,
                x="Matnda: She wants to go back one day — u yana borishni xohlaydi."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["present_perfect", "environment", "nature", "reading"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["past_simple", "travel", "adverbs", "future", "health", "modals", "comparatives", "shopping", "technology",
        "present_perfect", "environment", "reading"], chapter=C4, level=3)

T.write()
