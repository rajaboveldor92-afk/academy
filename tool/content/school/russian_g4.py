"""Rus tili (o‘zbek maktablari uchun), 4-sinf: assets/data/school/russian_g4.json + bank_russian_g4.json.

Mavzular O‘zbekiston maktab dasturi ("Rus tili", 4-sinf, ≈A1+) yo‘nalishida — 3 va 5-sinf oralig‘idagi bosqich:
sifat va otning moslashuvi, sonlar 100 gacha, Который час?, hafta kunlari va oylar, o‘tgan zamon (читал / читала),
xushmuomala iboralar, uy va kvartira, в / на + -е (Где?), Где? va Куда?, shahar va transport, kasblar, do‘kon,
qisqa matnlar. Hamma matn va savollar o‘zimizniki (o‘qish matnlari ham darslikdan ko‘chirilmagan).
Lug‘at mavzulari (rasmga qarab gap, sonlar, shahar va transport, taomlar) — umumiy `foreign_language.dart`
generatorlari, grammatika, iboralar va o‘qish — savollar banki.
Qayta yaratish: python3 tool/content/school/russian_g4.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("russian", 4, L("Rus tili", "Russian", "Русский язык"))

C1 = "1-chorak. Sifatlar, sonlar va vaqt"
C2 = "2-chorak. Kunlar, oylar va o‘tgan zamon"
C3 = "3-chorak. Uyim va shahrim"
C4 = "4-chorak. Kasblar, do‘kon va matnlar"


# ------------------------------------------------------------ yordamchilar
def RQ(q, a, w, say, d=1, x=None, e=None, h=None):
    """Savolda ruscha matn bor: ovozda `say` rus tilida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=say, lang="ru")


def LISTEN(a, w, say, d=1, x=None):
    """Tinglab tushunish: ruscha gap eshitiladi, o‘zbekcha tarjimasi tanlanadi."""
    return Q("Tinglang va tarjimasini tanlang", a, w, d=d, x=x or f"{say} — {a}", say=say, lang="ru")


def HEAR(q, a, w, say, d=1, x=None):
    """Tinglab son yoki vaqtni tanlash."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", say=say, lang="ru")


def SENT(ru, tr, d=1, full=None):
    """Ruscha gap tuzish (tinish belgisiz). `full` — izohda ko‘rsatiladigan tinish belgili gap."""
    end = "?" if tr.endswith("?") else "."
    return ORDER("So‘zlardan gap tuzing", ru, d=d, x=f"{full or ru + end} — {tr}", lang="ru")


def RTF(q, a, say, d=1, x=None):
    return TF(q, a, d=d, x=x, say=say, lang="ru")


def READ(text, emoji, questions):
    """O‘qish matni: bir matnga bir nechta savol (Q yoki TF) — `text` maydoni to‘ldiriladi."""
    return [{**it, "text": text, "e": emoji} for it in questions]


def vocab_levels(theme):
    return [
        {"themes": [theme], "modes": ["listen", "read"], "options": 3},
        {"themes": [theme], "modes": ["read", "picture_word"], "options": 3, "sameTheme": True},
        {"themes": [theme], "modes": ["picture_word", "listen", "read"], "options": 4, "sameTheme": True},
    ]


# ============================================================ 1-chorak
T.topic("adjectives", "🌈", L("Sifat: Какой? Какая? Какое? Какие?", "Adjectives: agreement",
                              "Прилагательные: согласование"),
        chapter=C1,
        theory="Sifat narsaning belgisini bildiradi va savolga javob beradi: Какой? Какая? Какое? Какие?\n"
               "• он — какой? новый дом, белый кот, большой стол\n"
               "• она — какая? новая школа, белая кошка, большая сумка\n"
               "• оно — какое? новое платье, белое молоко, большое окно\n"
               "• они — какие? новые книги, белые облака\n"
               "Sifat oxiri otning rodiga qarab o‘zgaradi: -ый / -ой → -ая → -ое → -ые.",
        items=[
            RQ("Mos sifatni tanlang: … кот", "белый", ["белая", "белое", "белые"], say="... кот",
               x="Кот — он: белый кот."),
            RQ("Mos sifatni tanlang: … кошка", "белая", ["белый", "белое", "белые"], say="... кошка",
               x="Кошка — она: белая кошка."),
            RQ("Mos sifatni tanlang: … молоко", "белое", ["белый", "белая", "белые"], say="... молоко",
               x="Молоко — оно: белое молоко."),
            RQ("Mos sifatni tanlang: … сумка", "новая", ["новый", "новое", "новые"], say="... сумка",
               x="Сумка — она: новая сумка."),
            RQ("Mos sifatni tanlang: … стол", "большой", ["большая", "большое", "большие"], say="... стол",
               x="Стол — он: большой стол."),
            RQ("Mos so‘roq so‘zni tanlang: … дом? — Высокий.", "Какой", ["Какая", "Какое", "Какие"],
               say="... дом? Высокий.", x="Дом — он: какой дом?"),
            RQ("Mos so‘roq so‘zni tanlang: … груша? — Сладкая.", "Какая", ["Какой", "Какое", "Какие"],
               say="... груша? Сладкая.", x="Груша — она: какая груша?"),
            Q("“Yangi” ruschasi qanday?", "новый", ["старый", "большой", "белый"], x="Yangi — новый; eski — старый."),
            Q("“Kichkina” ruschasi qanday?", "маленький", ["большой", "длинный", "новый"], x="Kichkina — маленький."),
            RQ("“Вкусный” o‘zbekchasi qanday?", "mazali", ["shirin", "issiq", "katta"], say="вкусный",
               x="Вкусный — mazali: вкусный суп."),
            LISTEN("Bu yangi uy.", ["Bu eski uy.", "Bu katta uy.", "Bu yangi maktab."], say="Это новый дом."),
            RTF("“Белая молоко” — to‘g‘ri birikma.", False, say="белая молоко", x="Молоко — оно: белое молоко."),
            MATCH("Sifat va tarjimasini juftlang",
                  [("сладкий", "shirin"), ("кислый", "nordon"), ("тёплый", "iliq"), ("мягкий", "yumshoq"),
                   ("чистый", "toza"), ("грязный", "iflos"), ("громкий", "baland (ovoz)")]),
            RQ("Mos sifatni tanlang: … облака", "белые", ["белый", "белая", "белое"], say="... облака", d=2,
               x="Облака — ko‘plik: белые облака."),
            RQ("Mos sifatni tanlang: … платье", "новое", ["новый", "новая", "новые"], say="... платье", d=2,
               x="Платье — оно: новое платье."),
            RQ("Mos sifatni tanlang: … карандаши", "новые", ["новый", "новая", "новое"], say="... карандаши", d=2,
               x="Карандаши — ko‘plik: новые карандаши."),
            RQ("Mos sifatni tanlang: … окно", "большое", ["большой", "большая", "большие"], say="... окно", d=2,
               x="Окно — оно: большое окно."),
            RQ("Mos so‘roq so‘zni tanlang: … солнце? — Яркое.", "Какое", ["Какой", "Какая", "Какие"],
               say="... солнце? Яркое.", d=2, x="Солнце — оно: какое солнце?"),
            RQ("Mos so‘roq so‘zni tanlang: … цветы? — Красивые.", "Какие", ["Какой", "Какая", "Какое"],
               say="... цветы? Красивые.", d=2, x="Цветы — ko‘plik: какие цветы?"),
            RQ("Qaysi sifat “окно” so‘ziga mos keladi?", "открытое", ["открытый", "открытая", "открытые"],
               say="окно", d=2, x="Окно — оно: открытое окно."),
            LISTEN("Mening mushugim kulrang.", ["Mening itim kulrang.", "Mening mushugim oq.", "Uning mushugi kulrang."],
                   say="Моя кошка серая.", d=2),
            RTF("“Высокое дерево” — to‘g‘ri birikma.", True, say="высокое дерево", d=2,
                x="Дерево — оно: высокое дерево."),
            Q("Qaysi birikma to‘g‘ri?", "вкусный суп", ["вкусная суп", "вкусное суп", "вкусные суп"], d=2,
              x="Суп — он: вкусный суп."),
            SENT("Это мой новый велосипед", "Bu mening yangi velosipedim.", d=2),
            SENT("Сегодня тёплый день", "Bugun iliq kun.", d=2),
            Q("Qaysi birikma to‘g‘ri?", "жёлтые листья", ["жёлтый листья", "жёлтая листья", "жёлтое листья"], d=3,
              x="Листья — ko‘plik: жёлтые листья."),
        ])

T.topic("sentences", "🖼️", L("Rasm va gap: rang va harakat", "Sentences: colours and actions",
                            "Предложения: цвет и действие"),
        chapter=C1, gen="sentence", prereq=["adjectives"],
        theory="Rus tilida hozirgi zamonda “-dir” (bo‘lmoq) so‘zi aytilmaydi: Мяч красный. — Koptok qizil.\n"
               "• Sifat otga moslashadi: Шар синий. Машина синяя. Яблоко зелёное.\n"
               "• Kim nima qilyapti? Кошка спит. Рыба плывёт. Птица летит.\n"
               "Gapni o‘qing yoki tinglang, rasmga qarang va mosini tanlang yoki so‘zlardan gap tuzing.",
        levels=[
            {"types": ["this", "color"], "modes": ["read", "listen"]},
            {"types": ["color", "action"], "modes": ["read", "picture", "listen"]},
            {"types": ["color", "action"], "modes": ["picture", "build", "listen"]},
        ])

T.topic("numbers", "💯", L("Sonlar 100 gacha", "Numbers to 100", "Числа до 100"),
        chapter=C1, gen="numbers",
        theory="O‘nliklar: двадцать (20), тридцать (30), сорок (40), пятьдесят (50),\n"
               "шестьдесят (60), семьдесят (70), восемьдесят (80), девяносто (90), сто (100).\n"
               "Murakkab son: o‘nlik + birlik — 34 = тридцать четыре, 58 = пятьдесят восемь.\n"
               "• 50, 60, 70, 80 — so‘z o‘rtasida ь yoziladi: пятьдесят, семьдесят.\n"
               "Tinglang va sonni toping: восемьдесят два — 82.",
        levels=[
            {"min": 10, "max": 40, "modes": ["listen_digit"], "options": 3},
            {"min": 20, "max": 100, "modes": ["listen_digit", "match"], "pairs": 4, "options": 4},
            {"min": 1, "max": 100, "modes": ["listen_digit", "match"], "pairs": 5, "options": 4},
        ])

T.topic("time", "🕒", L("Который час?", "What time is it?", "Который час?"),
        chapter=C1,
        theory="Soatni so‘rash: Который час? yoki Сколько времени? — Soat necha?\n"
               "• 1:00 — час;  2:00, 3:00, 4:00 — два, три, четыре часа;  5:00 … 12:00 — пять … двенадцать часов.\n"
               "• Qachon? — в + vaqt: в восемь часов, в два часа.\n"
               "• Kun qismi: семь часов утра (ertalab), два часа дня (kunduzi), шесть часов вечера (kechqurun).\n"
               "Yarim soat: 7:30 — семь тридцать.",
        items=[
            RQ("Soat 4:00. Который час?", "Четыре часа.", ["Четыре часов.", "Четырнадцать часов.", "Четыре час."],
               say="Который час?", e="🕓", x="2, 3, 4 dan keyin — часа: четыре часа."),
            RQ("Soat 9:00. Который час?", "Девять часов.", ["Девять часа.", "Девятнадцать часов.", "Десять часов."],
               say="Который час?", e="🕘", x="5 dan 12 gacha — часов: девять часов."),
            RQ("Soat 6:00. Который час?", "Шесть часов.", ["Шесть часа.", "Шестнадцать часов.", "Шесть час."],
               say="Который час?", e="🕕", x="Шесть часов — soat olti."),
            RQ("Mos so‘zni tanlang: Папа приходит домой в шесть …", "часов", ["час", "часа"],
               say="Папа приходит домой в шесть ...", x="6 dan keyin — часов."),
            RQ("Mos so‘zni tanlang: Урок кончается в два …", "часа", ["час", "часов"],
               say="Урок кончается в два ...", x="2 dan keyin — часа."),
            HEAR("Tinglang va vaqtni tanlang", "7:00", ["17:00", "8:00", "7:30"], say="Семь часов."),
            HEAR("Tinglang va vaqtni tanlang", "4:00", ["14:00", "5:00", "4:30"], say="Четыре часа."),
            Q("“Soat necha?” ruschasi qanday?", "Который час?", ["Сколько тебе лет?", "Какой сегодня день?", "Где часы?"],
              x="Soat necha? — Который час? (yoki Сколько времени?)"),
            RQ("“Сколько времени?” o‘zbekchasi qanday?", "Soat necha?", ["Qancha pul?", "Necha yoshdasan?", "Qachon?"],
               say="Сколько времени?", x="Сколько времени? — Soat necha?"),
            LISTEN("Hozir soat uch.", ["Hozir soat to‘rt.", "Soat uchda kel.", "Hozir soat o‘n uch."],
                   say="Сейчас три часа."),
            RTF("“Шесть часа” — to‘g‘ri.", False, say="шесть часа", x="5 dan 12 gacha — часов: шесть часов."),
            RTF("“Четыре часа” — to‘g‘ri.", True, say="четыре часа", x="2, 3, 4 dan keyin — часа."),
            SENT("Который час", "Soat necha?"),
            RQ("Soat 2:00. Который час?", "Два часа.", ["Два часов.", "Двенадцать часов.", "Два час."],
               say="Который час?", e="🕑", d=2, x="2 dan keyin — часа: два часа."),
            RQ("Soat 11:00. Который час?", "Одиннадцать часов.", ["Одиннадцать часа.", "Один час.", "Двенадцать часов."],
               say="Который час?", e="🕚", d=2, x="11 dan keyin — часов."),
            RQ("Mos sonni tanlang: Мы обедаем в … часа.", "три", ["пять", "семь", "девять"],
               say="Мы обедаем в ... часа.", d=2, x="часа — faqat 2, 3, 4 dan keyin: в три часа."),
            RQ("Mos sonni tanlang: Я ложусь спать в … часов.", "десять", ["два", "три", "четыре"],
               say="Я ложусь спать в ... часов.", d=2, x="часов — 5 va undan katta sonlar bilan: в десять часов."),
            HEAR("Tinglang va vaqtni tanlang", "10:30", ["10:00", "11:30", "3:10"], say="Десять тридцать.", d=2),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("семь часов утра", "ertalab soat 7"), ("два часа дня", "kunduzi soat 2"),
                   ("шесть часов вечера", "kechqurun soat 6"), ("полдень", "tush payti (12:00)"),
                   ("полночь", "yarim tun"), ("минута", "daqiqa")], d=2),
            LISTEN("Kino soat 5 da boshlanadi.", ["Kino soat 5 da tugaydi.", "Kino soat 6 da boshlanadi.",
                                                 "Dars soat 5 da boshlanadi."], say="Фильм начинается в пять часов.", d=2),
            RTF("“Час” — soat 1:00 degani.", True, say="Сейчас час.", d=2,
                x="1:00 — (Сейчас) час; «один» deyilmaydi."),
            RQ("Mos predlogni tanlang: Мы идём в кино … пять часов.", "в", ["на", "с", "у"],
               say="Мы идём в кино ... пять часов.", d=2, x="Qachon? — в пять часов."),
            SENT("Сейчас два часа дня", "Hozir kunduzi soat ikki.", d=2),
            Q("Bir kecha-kunduzda necha soat bor?", "двадцать четыре", ["двенадцать", "шестьдесят", "сорок"], d=2,
              x="Kecha-kunduzda 24 soat: двадцать четыре часа."),
            SENT("Мы ужинаем в семь часов вечера", "Biz kechqurun soat yettida kechki ovqat yeymiz.", d=3),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["adjectives", "sentences", "numbers", "time"], chapter=C1)

# ============================================================ 2-chorak
T.topic("calendar", "📅", L("Hafta kunlari va oylar", "Days and months", "Дни недели и месяцы"),
        chapter=C2,
        theory="Hafta kunlari: понедельник, вторник, среда, четверг, пятница, суббота, воскресенье.\n"
               "Oylar: январь, февраль, март, апрель, май, июнь, июль, август, сентябрь, октябрь, ноябрь, декабрь.\n"
               "• Kun va oy nomlari kichik harf bilan yoziladi.\n"
               "• Qachon? — kun: в понедельник, в среду, в пятницу;  oy: в январе, в мае, в сентябре.\n"
               "Какой сегодня день? — Сегодня четверг. Какой сейчас месяц? — Сейчас октябрь.",
        items=[
            Q("“Yanvar” ruschasi qanday?", "январь", ["июнь", "июль", "февраль"], x="Yanvar — январь."),
            RQ("“Март” — yilning nechanchi oyi?", "3-oy", ["1-oy", "5-oy", "8-oy"], say="март",
               x="Январь (1), февраль (2), март (3)."),
            RQ("Qaysi oy “июнь” dan keyin keladi?", "июль", ["май", "август", "сентябрь"], say="июнь",
               x="Июнь, июль, август — yoz oylari."),
            RQ("Qatorni to‘ldiring: январь, февраль, …", "март", ["май", "апрель", "декабрь"],
               say="январь, февраль, ...", x="Январь, февраль, март."),
            RQ("Qatorni to‘ldiring: четверг, …, суббота", "пятница", ["среда", "воскресенье", "понедельник"],
               say="четверг, ..., суббота", x="Payshanba, juma, shanba: четверг, пятница, суббота."),
            Q("Yil qaysi oy bilan boshlanadi?", "январь", ["декабрь", "март", "сентябрь"], x="Yil январь bilan boshlanadi."),
            Q("Yil qaysi oy bilan tugaydi?", "декабрь", ["ноябрь", "январь", "октябрь"], x="Yil декабрь bilan tugaydi."),
            Q("O‘zbekistonda o‘quv yili qaysi oyda boshlanadi?", "сентябрь", ["август", "январь", "июнь"],
              x="O‘quv yili sentabrda boshlanadi — в сентябре."),
            Q("Yil nechta oydan iborat?", "двенадцать", ["десять", "семь", "двадцать"],
              x="Yilda 12 oy: двенадцать месяцев."),
            MATCH("Oy va tarjimasini juftlang",
                  [("январь", "yanvar"), ("март", "mart"), ("май", "may"), ("июль", "iyul"), ("сентябрь", "sentabr"),
                   ("ноябрь", "noyabr")]),
            LISTEN("Bugun seshanba.", ["Ertaga seshanba.", "Bugun chorshanba.", "Bugun payshanba."],
                   say="Сегодня вторник."),
            RTF("Rus tilida oy nomlari kichik harf bilan yoziladi: май, июнь.", True, say="май, июнь",
                x="To‘g‘ri: oy va kun nomlari kichik harf bilan yoziladi."),
            RTF("“В январе” — “yanvarda” degani.", True, say="в январе", x="Qachon? — в январе (yanvarda)."),
            SENT("Сегодня пятница", "Bugun juma."),
            RQ("Qatorni to‘ldiring: сентябрь, …, ноябрь", "октябрь", ["август", "декабрь", "март"],
               say="сентябрь, ..., ноябрь", d=2, x="Сентябрь, октябрь, ноябрь — kuz oylari."),
            RQ("Mos shaklni tanlang: Мой день рождения в …", "мае", ["май", "мая", "маю"],
               say="Мой день рождения в ...", d=2, x="Qachon? — в мае (в + -е)."),
            RQ("Mos shaklni tanlang: Летом, в …, очень жарко.", "июле", ["июль", "июля", "июлем"],
               say="Летом, в ..., очень жарко.", d=2, x="Qachon? — в июле."),
            RQ("Mos shaklni tanlang: Я хожу в бассейн в …", "среду", ["среда", "среде", "средой"],
               say="Я хожу в бассейн в ...", d=2, x="Qachon? — в среду (-а → -у)."),
            LISTEN("Mening tug‘ilgan kunim aprelda.", ["Mening tug‘ilgan kunim avgustda.", "Uning tug‘ilgan kuni aprelda.",
                                                      "Aprelda havo iliq."], say="Мой день рождения в апреле.", d=2),
            LISTEN("Shanba kuni biz parkka boramiz.", ["Yakshanba kuni biz parkka boramiz.",
                                                      "Shanba kuni biz muzeyga boramiz.", "Juma kuni biz parkka boramiz."],
                   say="В субботу мы идём в парк.", d=2),
            RTF("Dekabrdan keyin fevral keladi.", False, say="декабрь, февраль", d=2,
                x="Dekabrdan keyin yangi yil — январь keladi."),
            SENT("В сентябре дети идут в школу", "Sentabrda bolalar maktabga boradi.", d=2),
            SENT("Какой сейчас месяц", "Hozir qaysi oy?", d=2),
            RQ("Mos shaklni tanlang: В … мы отдыхаем.", "воскресенье", ["воскресенья", "воскресеньем", "воскресенью"],
               say="В ... мы отдыхаем.", d=3, x="Воскресенье — оно, в bilan o‘zgarmaydi: в воскресенье."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "четверг", ["читверг", "четверк", "чутверг"], d=3,
              x="To‘g‘ri yozilishi: четверг."),
        ])

T.topic("past", "⏪", L("O‘tgan zamon: он читал, она читала", "Past tense: он читал, она читала",
                       "Прошедшее время: он читал, она читала"),
        chapter=C2,
        theory="O‘tgan zamonda fe’l -ть o‘rniga -л oladi: читать → читал.\n"
               "• он (o‘g‘il bola, erkak) — -л: Али читал.\n"
               "• она (qiz bola, ayol) — -ла: Лола читала.\n"
               "• они (ko‘plik) — -ли: Дети читали.  (оно — -ло: Солнце светило.)\n"
               "Kalit so‘zlar: вчера (kecha), утром, вечером, летом.  Вчера я рисовал (o‘g‘il bola) / рисовала (qiz bola).",
        items=[
            RQ("Mos fe’lni tanlang: Вчера Бобур … в футбол.", "играл", ["играла", "играли", "играло"],
               say="Вчера Бобур ... в футбол.", x="Бобур — он: играл."),
            RQ("Mos fe’lni tanlang: Вчера Нигора … кошку.", "рисовала", ["рисовал", "рисовали", "рисовало"],
               say="Вчера Нигора ... кошку.", x="Нигора — она: рисовала."),
            RQ("Mos fe’lni tanlang: Вчера дети … мультфильм.", "смотрели", ["смотрел", "смотрела", "смотрело"],
               say="Вчера дети ... мультфильм.", x="Дети — ko‘plik: смотрели."),
            RQ("“Спать” fe’lining o‘tgan zamon shakli (она)?", "спала", ["спал", "спит", "спали"], say="спать",
               x="Она — спала."),
            RQ("“Гулять” fe’lining o‘tgan zamon shakli (они)?", "гуляли", ["гулял", "гуляют", "гуляла"], say="гулять",
               x="Они — гуляли."),
            RQ("“Рисовать” fe’lining o‘tgan zamon shakli (он)?", "рисовал", ["рисовала", "рисует", "рисовали"],
               say="рисовать", x="Он — рисовал."),
            LISTEN("Kecha men parkda sayr qildim.", ["Bugun men parkda sayr qilyapman.", "Kecha men bog‘da ishladim.",
                                                    "Kecha biz parkda sayr qildik."], say="Вчера я гулял в парке."),
            RTF("“Лола играл” — to‘g‘ri.", False, say="Лола играл", x="Лола — qiz bola: Лола играла."),
            RTF("“Мы смотрели” — to‘g‘ri.", True, say="мы смотрели", x="Мы — ko‘plik: смотрели."),
            RTF("“Вчера” — “ertaga” degani.", False, say="вчера", x="Вчера — kecha; ertaga — завтра."),
            SENT("Вечером папа смотрел футбол", "Kechqurun otam futbol tomosha qildi."),
            RQ("Mos fe’lni tanlang: Бабушка … песню.", "пела", ["пел", "пели", "пело"], say="Бабушка ... песню.", d=2,
               x="Бабушка — она: пела."),
            RQ("Mos fe’lni tanlang: Вчера папа … машину.", "мыл", ["мыла", "мыли", "моет"],
               say="Вчера папа ... машину.", d=2, x="Папа — он, вчера — o‘tgan zamon: мыл."),
            RQ("Mos fe’lni tanlang: Утром мы … зарядку.", "делали", ["делал", "делала", "делает"],
               say="Утром мы ... зарядку.", d=2, x="Мы — ko‘plik: делали."),
            RQ("Азиз aytadi: Вчера я … письмо.", "писал", ["писала", "писали", "писало"], say="Вчера я ... письмо.", d=2,
               x="Aziz — o‘g‘il bola: я писал."),
            RQ("Мадина aytadi: Летом я … в деревне.", "отдыхала", ["отдыхал", "отдыхали", "отдыхало"],
               say="Летом я ... в деревне.", d=2, x="Madina — qiz bola: я отдыхала."),
            Q("Qaysi fe’l qiz bola haqida (o‘tgan zamon)?", "играла", ["играл", "играли", "играет"], d=2,
              x="Она — -ла: играла."),
            MATCH("Hozirgi va o‘tgan zamonni juftlang",
                  [("рисует", "рисовал"), ("гуляет", "гулял"), ("поёт", "пел"), ("спит", "спал"), ("делает", "делал"),
                   ("пьёт", "пил")], d=2),
            LISTEN("Onam kechqurun kitob o‘qidi.", ["Onam ertalab kitob o‘qidi.", "Otam kechqurun kitob o‘qidi.",
                                                   "Onam kechqurun gazeta o‘qidi."], say="Вечером мама читала книгу.", d=2),
            LISTEN("O‘g‘il bolalar futbol o‘ynashdi.", ["O‘g‘il bolalar futbol o‘ynayapti.", "Qizlar futbol o‘ynashdi.",
                                                       "O‘g‘il bolalar shaxmat o‘ynashdi."],
                   say="Мальчики играли в футбол.", d=2),
            Q("Qaysi gap to‘g‘ri?", "Мама готовила плов.", ["Мама готовил плов.", "Мама готовили плов.",
                                                          "Мама готовило плов."], d=2, x="Мама — она: готовила."),
            Q("Qaysi gap to‘g‘ri?", "Кошка спала на диване.", ["Кошка спал на диване.", "Кошка спали на диване.",
                                                             "Кошка спало на диване."], d=2, x="Кошка — она: спала."),
            RQ("Mos so‘zni tanlang: … мы были в театре.", "Вчера", ["Завтра", "Сейчас", "Через час"],
               say="... мы были в театре.", d=2, x="Были — o‘tgan zamon, shuning uchun вчера."),
            SENT("Сестра рисовала цветы", "Opam gullar chizdi.", d=2),
            RQ("Mos fe’lni tanlang: Утром … дождь.", "шёл", ["шла", "шли", "шло"], say="Утром ... дождь.", d=3,
               x="Дождь — он: дождь шёл (идти → шёл — istisno shakl)."),
            SENT("Летом дети отдыхали на озере", "Yozda bolalar ko‘lda dam olishdi.", d=3),
        ])

T.topic("polite", "🙏", L("Xushmuomala iboralar", "Polite phrases", "Вежливые фразы"),
        chapter=C2,
        theory="Iltimos qilish: Скажите, пожалуйста, где библиотека?  Дайте, пожалуйста, ручку.\n"
               "Ruxsat so‘rash: Можно войти? (Kirsam maylimi?) Можно взять книгу?\n"
               "Rahmat va javob: Спасибо большое! — Не за что! / Пожалуйста!\n"
               "Kechirim: Извините, пожалуйста. Простите, я опоздал.\n"
               "Tilaklar: Приятного аппетита! Счастливого пути! С днём рождения! Будь здоров!",
        items=[
            RQ("“Можно войти?” o‘zbekchasi qanday?", "Kirsam maylimi?", ["Chiqsam maylimi?", "Kiring!", "Qayerga kiray?"],
               say="Можно войти?", x="Можно войти? — Kirsam maylimi?"),
            RQ("“Не за что!” qachon aytiladi?", "rahmatga javoban", ["salomlashganda", "kechirim so‘raganda",
                                                                    "ovqatdan oldin"], say="Не за что!",
               x="Не за что! — Arzimaydi! (rahmatga javob)"),
            Q("Ovqatlanayotgan odamga nima deymiz?", "Приятного аппетита!", ["Счастливого пути!", "Спокойной ночи!",
                                                                           "С днём рождения!"],
              x="Приятного аппетита! — Yoqimli ishtaha!"),
            Q("Safarga ketayotgan odamga nima deymiz?", "Счастливого пути!", ["Приятного аппетита!", "Будь здоров!",
                                                                            "Добро пожаловать!"],
              x="Счастливого пути! — Oq yo‘l!"),
            Q("Do‘stingiz aksirdi. Nima deysiz?", "Будь здоров!", ["Не за что!", "Приятного аппетита!", "Счастливого пути!"],
              x="Aksirganda: Будь здоров! (Sog‘ bo‘l!)"),
            Q("Tug‘ilgan kun egasiga nima deymiz?", "С днём рождения!", ["С Новым годом!", "Спокойной ночи!", "Извините!"],
              x="С днём рождения! — Tug‘ilgan kuning bilan!"),
            Q("Yangi yil bayramida nima deymiz?", "С Новым годом!", ["С днём рождения!", "Приятного аппетита!", "Будь здоров!"],
              x="С Новым годом! — Yangi yil bilan!"),
            MATCH("Ibora va tarjimasini juftlang",
                  [("Спасибо большое!", "Katta rahmat!"), ("Не за что!", "Arzimaydi!"), ("Будь здоров!", "Sog‘ bo‘l!"),
                   ("Добро пожаловать!", "Xush kelibsiz!"), ("Счастливого пути!", "Oq yo‘l!"),
                   ("Приятного аппетита!", "Yoqimli ishtaha!"), ("Можно?", "Mumkinmi?")]),
            LISTEN("Iltimos, menga ruchka bering.", ["Iltimos, menga kitob bering.", "Rahmat, ruchka kerak emas.",
                                                    "Ruchkangni olsam maylimi?"], say="Дайте мне, пожалуйста, ручку."),
            RTF("“Приятного аппетита!” — ovqat oldidan aytiladi.", True, say="Приятного аппетита!",
                x="To‘g‘ri: ovqatlanayotganlarga aytiladi."),
            RTF("“Счастливого пути!” — uxlashdan oldin aytiladi.", False, say="Счастливого пути!",
                x="Счастливого пути! — safarga ketayotganga aytiladi; uxlashdan oldin — Спокойной ночи!"),
            SENT("Можно взять эту книгу", "Bu kitobni olsam maylimi?"),
            Q("Mehmonni kutib olganda nima deymiz?", "Добро пожаловать!", ["До свидания!", "Будь здоров!", "Не за что!"],
              d=2, x="Добро пожаловать! — Xush kelibsiz!"),
            Q("Darsga kechikdingiz. O‘qituvchiga nima deysiz?", "Извините, можно войти?",
              ["Привет, я здесь!", "Спасибо, до свидания!", "Приятного аппетита!"], d=2,
              x="Kechirim so‘rab, ruxsat olamiz: Извините, можно войти?"),
            RQ("Mos so‘zni tanlang: …, пожалуйста, где остановка?", "Скажите", ["Спасибо", "Пока", "Здравствуй"],
               say="..., пожалуйста, где остановка?", d=2, x="Скажите, пожалуйста… — Ayting-chi, iltimos…"),
            RQ("Mos so‘zni tanlang: Спасибо …!", "большое", ["большой", "большая", "большие"], say="Спасибо ...!", d=2,
               x="Спасибо большое! — Katta rahmat!"),
            RQ("Mos so‘zni tanlang: … взять твою ручку?", "Можно", ["Спасибо", "Пожалуйста", "Привет"],
               say="... взять твою ручку?", d=2, x="Ruxsat so‘rash: Можно взять…?"),
            LISTEN("Kechirasiz, men kechikdim.", ["Kechirasiz, men ketdim.", "Rahmat, men keldim.",
                                                 "Kechirasiz, siz kechikdingiz."], say="Извините, я опоздал.", d=2),
            RTF("“Здравствуйте” — faqat do‘stlarga aytiladi.", False, say="Здравствуйте", d=2,
                x="Здравствуйте — kattalarga va notanishlarga hurmat bilan aytiladi; do‘stga — Привет."),
            Q("Kattalarga murojaat qilganda qaysi olmosh ishlatiladi?", "вы", ["ты", "он", "они"], d=2,
              x="Kattalarga hurmat bilan «вы» deymiz: Вы можете мне помочь?"),
            RQ("Suhbatni to‘ldiring: — Спасибо за подарок! — …", "Пожалуйста!", ["Будь здоров!", "Счастливого пути!",
                                                                                "Спокойной ночи!"],
               say="Спасибо за подарок!", d=2, x="Rahmatga javob: Пожалуйста! yoki Не за что!"),
            SENT("Спасибо за помощь", "Yordamingiz uchun rahmat.", d=2),
            SENT("Скажите пожалуйста где метро", "Ayting-chi, iltimos, metro qayerda?", d=2,
                 full="Скажите, пожалуйста, где метро?"),
            LISTEN("Menga yordam bera olasizmi?", ["Sizga yordam beraymi?", "Menga yordam kerak emas.",
                                                  "U menga yordam berdi."], say="Вы можете мне помочь?", d=3),
            Q("Qaysi ibora do‘stona (norasmiy)?", "Привет!", ["Здравствуйте!", "Добрый день!", "Добро пожаловать!"], d=3,
              x="Привет! — do‘stlar orasida; qolganlari rasmiyroq."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["calendar", "past", "polite", "time"],
       chapter=C2)

# ============================================================ 3-chorak
T.topic("home", "🏠", L("Mening uyim va kvartiram", "My house and flat", "Мой дом и квартира"),
        chapter=C3,
        theory="Uy va kvartira: дом (uy), квартира (kvartira), комната (xona), кухня (oshxona), спальня (yotoqxona),\n"
               "гостиная (mehmonxona), ванная (hammom), балкон, этаж (qavat), лестница (zina).\n"
               "Mebel: стол, стул, диван, кровать (karavot), шкаф, полка (javon), ковёр (gilam), лампа.\n"
               "У нас есть … — Bizda … bor: У нас есть балкон.\n"
               "Я живу на третьем этаже. — Men uchinchi qavatda yashayman.",
        items=[
            Q("“Oshxona” ruschasi qanday?", "кухня", ["спальня", "ванная", "балкон"], x="Oshxona — кухня."),
            Q("“Xona” ruschasi qanday?", "комната", ["квартира", "кухня", "этаж"], x="Xona — комната."),
            Q("“Gilam” ruschasi qanday?", "ковёр", ["шкаф", "стол", "диван"], x="Gilam — ковёр."),
            RQ("“Спальня” o‘zbekchasi qanday?", "yotoqxona", ["oshxona", "hammom", "dahliz"], say="спальня",
               x="Спальня — yotoqxona (спать — uxlamoq)."),
            RQ("“Этаж” o‘zbekchasi qanday?", "qavat", ["xona", "eshik", "tom"], say="этаж", x="Этаж — qavat."),
            Q("Qayerda ovqat tayyorlaymiz?", "на кухне", ["в спальне", "в ванной", "на балконе"], x="Oshxonada — на кухне."),
            Q("Qayerda uxlaymiz?", "в спальне", ["на кухне", "в ванной", "в прихожей"], x="Yotoqxonada — в спальне."),
            MATCH("So‘z va tarjimasini juftlang",
                  [("кухня", "oshxona"), ("спальня", "yotoqxona"), ("ванная", "hammom"), ("гостиная", "mehmonxona"),
                   ("окно", "deraza"), ("дверь", "eshik"), ("стена", "devor")]),
            LISTEN("Bizning kvartiramiz katta.", ["Bizning uyimiz kichik.", "Bizning kvartiramiz kichik.",
                                                 "Ularning kvartirasi katta."], say="Наша квартира большая."),
            RQ("Mos so‘zni tanlang: У нас есть … балкон.", "большой", ["большая", "большое", "большие"],
               say="У нас есть ... балкон.", x="Балкон — он: большой балкон."),
            RTF("“Гостиная” — mehmonxona (mehmon kutadigan xona).", True, say="гостиная",
                x="To‘g‘ri: гостиная — mehmonxona."),
            RTF("“Кровать” oshxonada turadi.", False, say="кровать", x="Кровать — karavot, u yotoqxonada turadi."),
            Q("Qaysi so‘z ortiqcha?", "автобус", ["кухня", "спальня", "балкон"], x="Автобус — transport; qolganlari uy qismlari."),
            SENT("У нас есть кухня и две комнаты", "Bizda oshxona va ikkita xona bor."),
            RQ("“Лестница” o‘zbekchasi qanday?", "zina", ["deraza", "eshik", "devor"], say="лестница", d=2,
               x="Лестница — zina."),
            Q("Qayerda cho‘milamiz?", "в ванной", ["в гостиной", "на кухне", "в спальне"], d=2,
              x="Hammomda — в ванной."),
            MATCH("Mebel va narsalar: juftlang",
                  [("кровать", "karavot"), ("полка", "javon"), ("ковёр", "gilam"), ("зеркало", "ko‘zgu"),
                   ("холодильник", "muzlatkich"), ("часы", "soat")], d=2),
            LISTEN("Mening xonamda katta deraza bor.", ["Mening xonamda katta shkaf bor.", "Oshxonada katta deraza bor.",
                                                       "Mening xonamda deraza yo‘q."],
                   say="В моей комнате есть большое окно.", d=2),
            RQ("Mos so‘zni tanlang: Наша кухня очень …", "светлая", ["светлый", "светлое", "светлые"],
               say="Наша кухня очень ...", d=2, x="Кухня — она: светлая."),
            Q("Qaysi narsa oshxonada turadi?", "холодильник", ["кровать", "ванна", "шкаф для одежды"], d=2,
              x="Холодильник — muzlatkich, u oshxonada turadi."),
            RQ("“Где ты живёшь?” savoliga mos javob", "Я живу в доме номер пять.",
               ["Мне десять лет.", "Меня зовут Анвар.", "Сегодня среда."], say="Где ты живёшь?", d=2,
               x="Где? — qayerda? Javob: в доме номер пять."),
            SENT("Моя комната светлая и уютная", "Mening xonam yorug‘ va shinam.", d=2),
            RQ("Mos so‘zni tanlang: В квартире три …", "комнаты", ["комната", "комнат", "комнату"],
               say="В квартире три ...", d=3, x="2, 3, 4 dan keyin: три комнаты."),
            LISTEN("Biz beshinchi qavatda yashaymiz.", ["Biz uchinchi qavatda yashaymiz.", "Ular beshinchi qavatda yashaydi.",
                                                       "Biz besh xonali uyda yashaymiz."],
                   say="Мы живём на пятом этаже.", d=3),
            SENT("На стене висит картина", "Devorda rasm osilib turibdi.", d=3),
        ])

T.topic("prepositional", "📍", L("Qayerda? в / на + -е", "Where? Prepositional case", "Где? Предложный падеж"),
        chapter=C3, prereq=["home"],
        theory="Где? (Qayerda?) savoliga javob — в yoki на + otning -е shakli:\n"
               "• в — ichida: в комнате, в коробке, в городе, в Самарканде.\n"
               "• на — ustida yoki ochiq joyda: на столе, на окне, на улице, на балконе, на кухне.\n"
               "• -ь bilan tugagan она rodidagi so‘zlar -и oladi: в тетради, на площади.\n"
               "• Yodlang: в саду, в лесу, в шкафу, на полу (-у oladi).",
        items=[
            RQ("Mos shaklni tanlang: Книга лежит на …", "столе", ["стол", "стола", "столу"], say="Книга лежит на ...",
               x="Где? — на столе."),
            RQ("Mos shaklni tanlang: Мама на …", "кухне", ["кухня", "кухню", "кухней"], say="Мама на ...",
               x="Где? — на кухне."),
            RQ("Mos shaklni tanlang: Мы живём в …", "городе", ["город", "города", "городу"], say="Мы живём в ...",
               x="Где? — в городе."),
            RQ("Mos shaklni tanlang: Игрушки в …", "коробке", ["коробка", "коробку", "коробкой"], say="Игрушки в ...",
               x="Где? — в коробке."),
            RQ("Mos shaklni tanlang: Дети играют на …", "улице", ["улица", "улицу", "улицей"], say="Дети играют на ...",
               x="Где? — на улице."),
            RQ("Mos predlogni tanlang: Бабушка живёт … Самарканде.", "в", ["на", "под"],
               say="Бабушка живёт ... Самарканде.", x="Shaharda — в: в Самарканде."),
            LISTEN("Soat devorda.", ["Soat stolda.", "Rasm devorda.", "Soat derazada."], say="Часы на стене."),
            RTF("“На кухне” — “oshxonada” degani.", True, say="на кухне", x="To‘g‘ri: на кухне — oshxonada."),
            SENT("Ручка лежит в пенале", "Ruchka penalda yotibdi."),
            Q("Qaysi gap to‘g‘ri?", "Мы живём в Ташкенте.", ["Мы живём в Ташкент.", "Мы живём на Ташкенте.",
                                                           "Мы живём в Ташкенту."], x="Где? — в Ташкенте."),
            Q("Qaysi gap to‘g‘ri?", "Картина висит на стене.", ["Картина висит на стена.", "Картина висит в стене.",
                                                              "Картина висит на стену."], x="Devorda — на стене."),
            RQ("Mos shaklni tanlang: Цветы стоят на …", "окне", ["окно", "окна", "окну"], say="Цветы стоят на ...", d=2,
               x="Где? — на окне."),
            RQ("Mos shaklni tanlang: Молоко в …", "холодильнике", ["холодильник", "холодильника", "холодильнику"],
               say="Молоко в ...", d=2, x="Где? — в холодильнике."),
            RQ("Mos predlogni tanlang: Лампа висит … потолке.", "на", ["в", "под"], say="Лампа висит ... потолке.", d=2,
               x="Shiftda (ustida) — на потолке."),
            RQ("Mos predlogni tanlang: Летом мы загораем … пляже.", "на", ["в", "под"],
               say="Летом мы загораем ... пляже.", d=2, x="Plyajda — на пляже."),
            RQ("— Где папа? — Папа … (balkonda).", "на балконе", ["на балкон", "в балконе", "балкон"],
               say="Где папа? Папа ...", d=2, x="Где? — на балконе."),
            LISTEN("Kitoblar shkafda.", ["Kitoblar stolda.", "Kitoblar sumkada.", "Daftarlar shkafda."],
                   say="Книги в шкафу.", d=2),
            LISTEN("Bolalar hovlida o‘ynayapti.", ["Bolalar sinfda o‘ynayapti.", "Bolalar hovliga chiqdi.",
                                                  "Qizlar hovlida o‘tiribdi."], say="Дети играют во дворе.", d=2),
            MATCH("Birikma va tarjimasini juftlang",
                  [("на столе", "stolda"), ("в коробке", "qutida"), ("на улице", "ko‘chada"), ("в лесу", "o‘rmonda"),
                   ("в саду", "bog‘da"), ("на полу", "polda"), ("на кухне", "oshxonada")], d=2),
            SENT("Бабушка работает в саду", "Buvim bog‘da ishlayapti.", d=2),
            RQ("Mos shaklni tanlang: Я пишу в …", "тетради", ["тетрадь", "тетраде", "тетрадью"], say="Я пишу в ...", d=3,
               x="-ь bilan tugagan она rodidagi so‘z -и oladi: в тетради."),
            RQ("Mos shaklni tanlang: Яблоки растут в …", "саду", ["саде", "сад", "сада"], say="Яблоки растут в ...", d=3,
               x="Istisno: в саду."),
            RQ("Mos shaklni tanlang: Медведь живёт в …", "лесу", ["лесе", "лес", "леса"], say="Медведь живёт в ...", d=3,
               x="Istisno: в лесу."),
            RQ("Mos shaklni tanlang: Кошка спит на …", "полу", ["пол", "пола", "полом"], say="Кошка спит на ...", d=3,
               x="Istisno: на полу (polda)."),
            RTF("“В лесе” — to‘g‘ri shakl.", False, say="в лесе", d=3, x="Istisno: в лесу."),
            SENT("Кошка спит на полу", "Mushuk polda uxlayapti.", d=3),
        ])

T.topic("where_to", "🚶", L("Где? va Куда?", "Where? and Where to?", "Где? и Куда?"),
        chapter=C3, prereq=["prepositional"],
        theory="Где? — qayerda? (joy): Я в школе. Мама на рынке. Папа дома.\n"
               "Куда? — qayerga? (yo‘nalish): Я иду в школу. Мама идёт на рынок. Папа идёт домой.\n"
               "• Куда? — в / на + so‘z (-а → -у): в школу, на почту; он rodidagi so‘z o‘zgarmaydi: в парк, на стадион.\n"
               "• дома — uyda (Где?),  домой — uyga (Куда?)\n"
               "• здесь / тут — shu yerda, там — u yerda (Где?);  сюда — bu yerga, туда — u yerga (Куда?).",
        items=[
            RQ("Mos so‘roq so‘zni tanlang: … ты идёшь? — В бассейн.", "Куда", ["Где", "Когда", "Кто"],
               say="... ты идёшь? В бассейн.", x="В бассейн — qayerga? Куда?"),
            RQ("Mos so‘roq so‘zni tanlang: … мама? — На рынке.", "Где", ["Куда", "Когда", "Чья"],
               say="... мама? На рынке.", x="На рынке — qayerda? Где?"),
            RQ("Mos so‘zni tanlang: Уроки кончились. Я иду …", "домой", ["дома", "дом", "домом"],
               say="Уроки кончились. Я иду ...", x="Qayerga? — домой (uyga)."),
            RQ("Mos so‘zni tanlang: Бабушка сейчас …", "дома", ["домой", "дому", "домом"],
               say="Бабушка сейчас ...", x="Qayerda? — дома (uyda)."),
            RQ("Mos shaklni tanlang: Мы идём в …", "зоопарк", ["зоопарке", "зоопарка", "зоопарку"],
               say="Мы идём в ...", x="Куда? — в зоопарк (он rodi, o‘zgarmaydi)."),
            RQ("Mos shaklni tanlang: Сестра идёт на …", "почту", ["почта", "почте", "почтой"],
               say="Сестра идёт на ...", x="Куда? — на почту (-а → -у)."),
            MATCH("So‘z va tarjimasini juftlang",
                  [("дома", "uyda"), ("домой", "uyga"), ("здесь", "shu yerda"), ("сюда", "bu yerga"), ("там", "u yerda"),
                   ("туда", "u yerga")]),
            LISTEN("Men uyga ketyapman.", ["Men uydaman.", "Men maktabga ketyapman.", "U uyga ketyapti."],
                   say="Я иду домой."),
            RTF("“Домой” — “Где?” savoliga javob.", False, say="домой",
                x="Домой — qayerga? (Куда?). Где? savoliga — дома."),
            RTF("“На почту” — “Куда?” savoliga javob.", True, say="на почту", x="На почту — qayerga? Куда?"),
            SENT("Куда ты идёшь", "Qayerga ketyapsan?"),
            SENT("Мы идём на стадион", "Biz stadionga ketyapmiz."),
            RQ("Mos so‘roq so‘zni tanlang: … едет папа? — На вокзал.", "Куда", ["Где", "Кто", "Что"],
               say="... едет папа? На вокзал.", d=2, x="На вокзал — qayerga? Куда?"),
            RQ("Mos so‘roq so‘zni tanlang: … работает врач? — В больнице.", "Где", ["Куда", "Кого", "Чей"],
               say="... работает врач? В больнице.", d=2, x="В больнице — qayerda? Где?"),
            RQ("Mos shaklni tanlang: Сестра работает на …", "почте", ["почта", "почту", "почтой"],
               say="Сестра работает на ...", d=2, x="Где? — на почте."),
            RQ("Mos shaklni tanlang: Вечером мы были в …", "цирке", ["цирк", "цирка", "цирку"],
               say="Вечером мы были в ...", d=2, x="Где? — в цирке."),
            RQ("Mos shaklni tanlang: Мама идёт в …", "аптеку", ["аптека", "аптеке", "аптекой"],
               say="Мама идёт в ...", d=2, x="Куда? — в аптеку."),
            RQ("“Куда ты идёшь?” savoliga mos javob", "На стадион.", ["На стадионе.", "Стадион.", "Дома."],
               say="Куда ты идёшь?", d=2, x="Куда? — на стадион."),
            RQ("“Где ты был вчера?” savoliga mos javob", "В бассейне.", ["В бассейн.", "Бассейн.", "Домой."],
               say="Где ты был вчера?", d=2, x="Где? — в бассейне."),
            LISTEN("Otam vokzalda.", ["Otam vokzalga ketyapti.", "Onam vokzalda.", "Otam bekatda."],
                   say="Папа на вокзале.", d=2),
            SENT("После школы я иду домой", "Maktabdan keyin men uyga boraman.", d=2),
            RQ("Mos so‘zni tanlang: Иди …! (bu yerga)", "сюда", ["здесь", "тут", "там"], say="Иди ...!", d=3,
               x="Qayerga? — сюда (bu yerga)."),
            RQ("Mos so‘zni tanlang: Мой брат … (u yerda).", "там", ["туда", "сюда", "куда"], say="Мой брат ...", d=3,
               x="Qayerda? — там (u yerda)."),
            LISTEN("Ertaga biz hayvonot bog‘iga boramiz.", ["Kecha biz hayvonot bog‘ida edik.", "Ertaga biz sirkka boramiz.",
                                                           "Ertaga ular hayvonot bog‘iga boradi."],
                   say="Завтра мы пойдём в зоопарк.", d=3),
            Q("Qaysi gap to‘g‘ri?", "Брат идёт на рынок.", ["Брат идёт на рынке.", "Брат идёт в рынок.",
                                                          "Брат идёт на рынку."], d=3, x="Куда? — на рынок."),
        ])

T.topic("city", "🚌", L("Shahar va transport", "Town and transport", "Город и транспорт"),
        chapter=C3, gen="vocab", prereq=["where_to"],
        theory="Transport: автобус, трамвай, метро, такси, поезд, самолёт, велосипед, машина.\n"
               "Nimada? — на + -е: на автобусе, на поезде, на велосипеде; метро va такси o‘zgarmaydi: на метро, на такси.\n"
               "Shahar: улица (ko‘cha), площадь (maydon), мост (ko‘prik), больница, магазин, стадион, светофор.\n"
               "Kasb va joy: водитель водит автобус, врач работает в больнице.",
        levels=vocab_levels("transport_city"))

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["home", "prepositional", "where_to", "city"],
       chapter=C3)

# ============================================================ 4-chorak
T.topic("professions", "👷", L("Kasblar", "Professions", "Профессии"),
        chapter=C4,
        theory="Kasblar: врач (shifokor), учитель (o‘qituvchi), повар (oshpaz), водитель (haydovchi), продавец (sotuvchi),\n"
               "строитель (quruvchi), фермер, лётчик (uchuvchi), художник (rassom), почтальон (pochtachi).\n"
               "Ba’zi kasblarning ayollar shakli bor: учитель — учительница, певец — певица.\n"
               "Kim nima qiladi? Повар готовит еду. Строитель строит дом. Врач лечит людей.\n"
               "Кто твоя мама по профессии? — Моя мама — учительница. Она работает в школе.",
        items=[
            Q("“Oshpaz” ruschasi qanday?", "повар", ["врач", "водитель", "строитель"], x="Oshpaz — повар."),
            Q("“Haydovchi” ruschasi qanday?", "водитель", ["продавец", "лётчик", "повар"], x="Haydovchi — водитель."),
            RQ("“Строитель” o‘zbekchasi qanday?", "quruvchi", ["sotuvchi", "haydovchi", "rassom"], say="строитель",
               x="Строитель — quruvchi (строить — qurmoq)."),
            RQ("“Продавец” o‘zbekchasi qanday?", "sotuvchi", ["oshpaz", "quruvchi", "shifokor"], say="продавец",
               x="Продавец — sotuvchi (продавать — sotmoq)."),
            Q("Kim odamlarni davolaydi?", "врач", ["повар", "строитель", "продавец"], x="Врач лечит людей."),
            Q("Kim samolyotni boshqaradi?", "лётчик", ["водитель", "почтальон", "фермер"], x="Лётчик — uchuvchi."),
            Q("Kim rasm chizadi?", "художник", ["учитель", "повар", "врач"], x="Художник — rassom."),
            RQ("Mos fe’lni tanlang: Повар … обед.", "готовит", ["лечит", "строит", "водит"], say="Повар ... обед.",
               x="Повар готовит обед — oshpaz tushlik tayyorlaydi."),
            RQ("Mos fe’lni tanlang: Строитель … дом.", "строит", ["лечит", "готовит", "продаёт"],
               say="Строитель ... дом.", x="Строитель строит дом."),
            LISTEN("Bobom — fermer.", ["Bobom — quruvchi.", "Otam — fermer.", "Bobom fermada yashaydi."],
                   say="Мой дедушка — фермер."),
            RTF("“Лётчик” — samolyot uchuvchisi.", True, say="лётчик", x="To‘g‘ri: лётчик — uchuvchi."),
            RTF("“Повар” maktabda dars beradi.", False, say="повар", x="Повар ovqat pishiradi; dars beradi — учитель."),
            Q("Qaysi so‘z kasb emas?", "больница", ["врач", "повар", "фермер"], x="Больница — kasalxona (joy)."),
            SENT("Моя мама работает в школе", "Onam maktabda ishlaydi."),
            RQ("“Почтальон” o‘zbekchasi qanday?", "pochtachi (xat tashuvchi)", ["politsiyachi", "haydovchi", "fermer"],
               say="почтальон", d=2, x="Почтальон — xat va gazeta tashuvchi."),
            RQ("Mos fe’lni tanlang: Врач … детей.", "лечит", ["строит", "продаёт", "водит"], say="Врач ... детей.", d=2,
               x="Врач лечит — shifokor davolaydi."),
            RQ("Mos fe’lni tanlang: Продавец … фрукты.", "продаёт", ["лечит", "строит", "учит"],
               say="Продавец ... фрукты.", d=2, x="Продавец продаёт — sotuvchi sotadi."),
            RQ("Ayollar shaklini tanlang: учитель → …", "учительница", ["учителка", "учителья", "учителина"],
               say="учитель", d=2, x="Учитель — учительница (o‘qituvchi ayol)."),
            MATCH("Kasb va ish joyini juftlang",
                  [("врач", "больница"), ("учитель", "школа"), ("повар", "кухня"), ("продавец", "магазин"),
                   ("лётчик", "самолёт"), ("фермер", "ферма"), ("почтальон", "почта")], d=2),
            LISTEN("Opam — sotuvchi. U do‘konda ishlaydi.", ["Opam — oshpaz. U oshxonada ishlaydi.",
                                                            "Akam — sotuvchi. U bozorda ishlaydi.", "Opam do‘konga bordi."],
                   say="Моя сестра — продавец. Она работает в магазине.", d=2),
            RQ("“Кто твой папа по профессии?” savoliga mos javob", "Мой папа — водитель.",
               ["Мой папа дома.", "Моему папе сорок лет.", "Это папина машина."],
               say="Кто твой папа по профессии?", d=2, x="Kasb so‘ralgan: Мой папа — водитель."),
            SENT("Строитель строит новый дом", "Quruvchi yangi uy quryapti.", d=2),
            RQ("Topishmoq: Он водит автобус. Кто это?", "водитель", ["лётчик", "повар", "почтальон"],
               say="Он водит автобус. Кто это?", d=2, x="Avtobusni haydovchi boshqaradi — водитель."),
            RQ("Ayollar shaklini tanlang: певец → …", "певица", ["певка", "певеца", "певецка"], say="певец", d=3,
               x="Певец — певица (qo‘shiqchi ayol)."),
            RQ("Topishmoq: Она лечит животных. Кто это?", "ветеринар", ["учительница", "продавец", "художница"],
               say="Она лечит животных. Кто это?", d=3, x="Hayvonlarni veterinar davolaydi."),
            SENT("Мой брат хочет быть врачом", "Akam shifokor bo‘lishni xohlaydi.", d=3),
        ])

T.topic("shop", "🛒", L("Do‘konda", "At the shop", "В магазине"),
        chapter=C4, prereq=["professions"],
        theory="Mahsulotlar: хлеб, молоко, масло (sariyog‘), сахар (shakar), соль (tuz), яйца (tuxum), рыба (baliq),\n"
               "курица (tovuq), мёд (asal), фрукты (mevalar), овощи (sabzavotlar).\n"
               "Do‘konda so‘rash: У вас есть свежий хлеб? — Да, есть. / Нет, к сожалению, нет.\n"
               "Сколько стоит масло? — Двадцать тысяч сумов.  Дорого — qimmat, дёшево — arzon.\n"
               "Xushmuomala bo‘ling: Дайте, пожалуйста… — Вот, пожалуйста. Спасибо! До свидания!",
        items=[
            Q("“Shakar” ruschasi qanday?", "сахар", ["соль", "масло", "мёд"], x="Shakar — сахар."),
            Q("“Tuz” ruschasi qanday?", "соль", ["сахар", "сок", "суп"], x="Tuz — соль."),
            Q("“Asal” ruschasi qanday?", "мёд", ["мясо", "масло", "молоко"], x="Asal — мёд."),
            RQ("“Рыба” o‘zbekchasi qanday?", "baliq", ["tovuq", "go‘sht", "non"], say="рыба", x="Рыба — baliq."),
            RQ("“Дорого” o‘zbekchasi qanday?", "qimmat", ["arzon", "mazali", "yangi"], say="дорого", x="Дорого — qimmat."),
            Q("Qaysi mahsulot shirin?", "мёд", ["соль", "рыба", "хлеб"], x="Мёд — asal, u shirin."),
            MATCH("Mahsulot va tarjimasini juftlang",
                  [("сахар", "shakar"), ("соль", "tuz"), ("мёд", "asal"), ("рыба", "baliq"), ("курица", "tovuq"),
                   ("яйца", "tuxumlar"), ("фрукты", "mevalar")]),
            LISTEN("Bu juda qimmat.", ["Bu juda arzon.", "Bu juda mazali.", "Bu juda katta."], say="Это очень дорого."),
            RTF("“Соль” — shirin.", False, say="соль", x="Соль — tuz, u sho‘r; shirin — сахар."),
            RTF("“Касса” — pul to‘lanadigan joy.", True, say="касса", x="To‘g‘ri: kassada pul to‘laymiz."),
            Q("Qaysi so‘z ortiqcha?", "тетрадь", ["сахар", "соль", "мёд"], x="Тетрадь — daftar; qolganlari mahsulotlar."),
            RQ("Mos so‘zni tanlang: Мама хочет … рыбу.", "купить", ["продать", "читать", "играть"],
               say="Мама хочет ... рыбу.", x="Купить — sotib olmoq."),
            RQ("“Дёшево” o‘zbekchasi qanday?", "arzon", ["qimmat", "shirin", "issiq"], say="дёшево", d=2,
               x="Дёшево — arzon; дорого — qimmat."),
            RQ("“Масло” o‘zbekchasi qanday?", "sariyog‘ (yog‘)", ["sut", "go‘sht", "tuxum"], say="масло", d=2,
               x="Масло — sariyog‘ yoki o‘simlik yog‘i."),
            RQ("“У вас есть молоко?” o‘zbekchasi qanday?", "Sizda sut bormi?",
               ["Sut qancha turadi?", "Menga sut bering.", "Sut qayerda?"], say="У вас есть молоко?", d=2,
               x="У вас есть…? — Sizda … bormi?"),
            RQ("Mos so‘zni tanlang: — … стоит сахар? — Десять тысяч сумов.", "Сколько", ["Где", "Кто", "Какой"],
               say="... стоит сахар? Десять тысяч сумов.", d=2, x="Narx so‘raladi: Сколько стоит?"),
            Q("Sutdan nima tayyorlanadi?", "сыр", ["хлеб", "мёд", "рыба"], d=2, x="Сыр (pishloq) sutdan tayyorlanadi."),
            Q("Pul qayerda to‘lanadi?", "в кассе", ["в холодильнике", "на полке", "в корзине"], d=2,
              x="Kassada — в кассе."),
            LISTEN("Sizda yangi non bormi?", ["Yangi non qancha turadi?", "Menga yangi non bering.", "Sizda yangi sut bormi?"],
                   say="У вас есть свежий хлеб?", d=2),
            LISTEN("Men shakar va tuz sotib oldim.", ["Men shakar va choy sotib oldim.", "Men tuz sotib olmadim.",
                                                     "Onam shakar va tuz sotib oldi."], say="Я купил сахар и соль.", d=2),
            RQ("— Дайте, пожалуйста, рыбу. — …", "Вот, пожалуйста.", ["Будь здоров!", "Спокойной ночи!", "Меня зовут Олег."],
               say="Дайте, пожалуйста, рыбу.", d=2, x="Sotuvchi beradi: Вот, пожалуйста."),
            SENT("У вас есть свежая рыба", "Sizda yangi baliq bormi?", d=2),
            SENT("Сколько стоит этот торт", "Bu tort qancha turadi?", d=2),
            RQ("Mos so‘zni tanlang: Хлеб стоит пять тысяч …", "сумов", ["сум", "сума", "сумы"],
               say="Хлеб стоит пять тысяч ...", d=3, x="5 dan keyin: пять тысяч сумов."),
            RQ("Mos so‘zni tanlang: Я … молоко и хлеб.", "купил", ["лечил", "строил", "учил"],
               say="Я ... молоко и хлеб.", d=3, x="Купил — sotib oldim (купить → купил)."),
        ])

T.topic("food", "🍰", L("Taomlar", "Food", "Еда"),
        chapter=C4, gen="vocab", prereq=["shop"],
        theory="Taomlar: хлеб, сыр, яйцо, молоко, мёд, суп, рис, торт, пирог, блины, салат, чай, мороженое.\n"
               "Rodni eslang: мой суп, моя пицца, моё мороженое.\n"
               "Я люблю … — Men … ni yaxshi ko‘raman: Я люблю блины. Я не люблю рис.\n"
               "Что ты ешь на завтрак? — На завтрак я ем яйцо и хлеб.",
        levels=vocab_levels("food"))

TEXT_FLAT = ("Меня зовут Камила. Мне десять лет. Я живу в Намангане. Наша квартира на третьем этаже. "
             "В квартире три комнаты, кухня и балкон. Моя комната маленькая, но светлая. На окне стоят цветы.")
TEXT_PLOV = ("Вчера была суббота. Утром Жасур и папа ходили на рынок. Там они купили мясо, морковь и лук. "
             "Днём мама готовила плов. Вечером к нам пришли бабушка и дедушка. Плов был очень вкусный!")
TEXT_CITY = ("Это наш город. Он большой и зелёный. В центре есть парк и площадь. Около парка — школа и "
             "библиотека. Я езжу в школу на автобусе. Мой друг Саид живёт рядом со школой, он ходит в школу пешком.")
TEXT_DOCTOR = ("Мой дедушка — врач. Он работает в больнице. Каждый день он встаёт в шесть часов. Дедушка очень "
               "добрый. Он лечит детей и взрослых. Я тоже хочу быть врачом.")
TEXT_LESSON = ("Сегодня понедельник. Первый урок — русский язык. Он начинается в восемь часов. Учительница "
               "читает рассказ, а дети слушают. Потом они пишут в тетрадях.")

T.topic("reading", "📖", L("Qisqa matnlar", "Short texts", "Короткие тексты"),
        chapter=C4,
        theory="Matnni o‘qishdan oldin savolni o‘qing — nimani qidirish kerakligini bilasiz.\n"
               "• Кто? — kim;  Где? — qayerda;  Когда? — qachon;  Что делал? — nima qildi.\n"
               "• Notanish so‘z bo‘lsa, gapdagi boshqa so‘zlarga qarab ma’nosini taxmin qiling.\n"
               "Javobni matndan toping: Где живёт Камила? — В Намангане.",
        items=[
            *READ(TEXT_FLAT, "🏠", [
                Q("Kamila necha yoshda?", "10", ["9", "11", "3"], x="Мне десять лет — 10 yosh."),
                Q("Kamila qayerda yashaydi?", "в Намангане", ["в Ташкенте", "в Бухаре", "в Самарканде"],
                  x="Я живу в Намангане."),
                Q("Kvartira nechanchi qavatda?", "3-qavatda", ["1-qavatda", "5-qavatda", "10-qavatda"], d=2,
                  x="Наша квартира на третьем этаже."),
                TF("Kamilaning xonasi katta va qorong‘i.", False, d=2, x="Моя комната маленькая, но светлая."),
                Q("Derazada nima turibdi?", "цветы", ["книги", "часы", "игрушки"], d=2, x="На окне стоят цветы."),
            ]),
            *READ(TEXT_PLOV, "🍲", [
                Q("Jasur kim bilan bozorga bordi?", "с папой", ["с мамой", "с бабушкой", "с другом"],
                  x="Утром Жасур и папа ходили на рынок."),
                Q("Ular bozordan nima sotib olishdi?", "мясо, морковь и лук", ["хлеб, молоко и сыр",
                                                                             "рыбу и рис", "яблоки и мёд"], d=2,
                  x="Там они купили мясо, морковь и лук."),
                Q("Palovni kim tayyorladi?", "мама", ["папа", "бабушка", "Жасур"], x="Днём мама готовила плов."),
                TF("Kechqurun buvi va bobo kelishdi.", True, x="Вечером к нам пришли бабушка и дедушка."),
                TF("Palov mazasiz edi.", False, d=2, x="Плов был очень вкусный!"),
            ]),
            *READ(TEXT_CITY, "🏙️", [
                Q("Shahar qanday?", "большой и зелёный", ["маленький и старый", "новый и серый", "тихий и жёлтый"],
                  x="Он большой и зелёный."),
                Q("Muallif maktabga nimada boradi?", "на автобусе", ["на метро", "на велосипеде", "пешком"], d=2,
                  x="Я езжу в школу на автобусе."),
                Q("Said maktabga qanday boradi?", "пешком", ["на автобусе", "на такси", "на машине"], d=2,
                  x="Он ходит в школу пешком — piyoda."),
                TF("Parkning yonida maktab va kutubxona bor.", True, d=2, x="Около парка — школа и библиотека."),
            ]),
            *READ(TEXT_DOCTOR, "🏥", [
                Q("Bobosi qayerda ishlaydi?", "в больнице", ["в школе", "в магазине", "на почте"],
                  x="Он работает в больнице."),
                Q("Bobosi soat nechada turadi?", "6 da", ["7 da", "8 da", "5 da"], x="Он встаёт в шесть часов."),
                TF("Muallif ham shifokor bo‘lishni xohlaydi.", True, d=2, x="Я тоже хочу быть врачом."),
                Q("Bobosi kimlarni davolaydi?", "детей и взрослых", ["только детей", "животных", "только бабушек"], d=3,
                  x="Он лечит детей и взрослых — bolalar va kattalarni."),
            ]),
            *READ(TEXT_LESSON, "📚", [
                Q("Bugun qaysi kun?", "понедельник", ["вторник", "суббота", "пятница"], x="Сегодня понедельник."),
                Q("Birinchi dars qaysi fan?", "русский язык", ["математика", "английский язык", "музыка"],
                  x="Первый урок — русский язык."),
                Q("Dars soat nechada boshlanadi?", "8 da", ["9 da", "7 da", "10 da"], d=2,
                  x="Он начинается в восемь часов."),
                TF("O‘qituvchi hikoya o‘qiydi, bolalar tinglaydi.", True, d=2,
                   x="Учительница читает рассказ, а дети слушают."),
                Q("Keyin bolalar nima qiladi?", "пишут в тетрадях", ["играют в футбол", "поют песни", "рисуют на доске"],
                  d=3, x="Потом они пишут в тетрадях."),
            ]),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["professions", "shop", "food", "reading"],
       chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["adjectives", "time", "calendar", "past", "polite", "home", "prepositional", "where_to", "professions", "shop",
        "reading"], chapter=C4, level=3)

T.write()
