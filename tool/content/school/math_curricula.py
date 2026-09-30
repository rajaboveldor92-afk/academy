"""Maktab matematikasi dasturlari: assets/data/school/math_g3.json, math_g5.json.

Mavzular O'zbekiston maktab dasturi (3-sinf: Novda Edutainment darsligi tartibi, 5-sinf: "AHA" darsligi)
bo'yicha tuzilgan; tushuntirish matnlari — o'zimizniki (darslikdan ko'chirilmagan).
Qayta yaratish: python3 tool/content/school/math_curricula.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def L(uz, en, ru):
    return {"uz": uz, "en": en, "ru": ru}


def lv(*levels):
    return list(levels)


def topic(grade, key, code, emoji, title, gen, levels, theory, chapter, prereq=None):
    return {
        "id": f"math_g{grade}.{key}",
        "code": code,
        "emoji": emoji,
        "title": title,
        "generator": gen,
        "skill": gen,
        "chapter": chapter,
        "prerequisites": prereq or [],
        "levels": levels,
        "theory": {"uz": theory} if theory else None,
    }


def test(grade, key, code, title, topics, chapter, level=2):
    return {
        "id": f"math_g{grade}.{key}",
        "code": code,
        "emoji": "📝",
        "title": title,
        "generator": "test",
        "skill": "test",
        "chapter": chapter,
        "prerequisites": [],
        "lessonSize": 10,
        # Nazorat ishi ham 3 darajali: bola natijasiga qarab savollar qiyinlashadi (1 → 3).
        "levels": [{"topics": [f"math_g{grade}.{t}" for t in topics], "level": min(3, l + level - 2)} for l in (1, 2, 3)],
    }


# ============================================================ 3-sinf
C1 = "1-chorak. Takrorlash va ko‘p xonali sonlar"
C2 = "2-chorak. Ko‘paytirish va bo‘lish"
C3 = "3-chorak. Kattaliklar va geometriya"
C4 = "4-chorak. Masalalar, kasrlar, to‘plamlar"

g3 = [
    topic(3, "table", "1", "✖️", L("Ko‘paytirish jadvali", "Times tables", "Таблица умножения"), "mul_table",
          lv({"min": 2, "max": 5, "division": False, "mode": "choice"}, {"min": 2, "max": 9, "division": True, "mode": "mixed"},
             {"min": 2, "max": 9, "division": True, "mode": "input"}),
          "Ko‘paytirish — bir xil sonlarni qo‘shishning qisqa yozuvi: 4 · 3 = 4 + 4 + 4 = 12.\n"
          "Bo‘lish — ko‘paytirishga teskari amal: 12 : 3 = 4, chunki 4 · 3 = 12.\n"
          "• Istalgan son · 1 = shu son;  istalgan son · 0 = 0.\n"
          "• Ko‘paytuvchilar o‘rnini almashtirsa ham natija o‘zgarmaydi: 6 · 7 = 7 · 6 = 42.", C1),
    topic(3, "review_100", "2", "➕", L("100 ichida qo‘shish va ayirish", "Adding and subtracting within 100", "Сложение и вычитание в пределах 100"), "add_sub",
          lv({"min": 10, "max": 50, "mode": "choice"}, {"min": 10, "max": 99, "mode": "mixed"}, {"min": 10, "max": 99, "mode": "input"}),
          "Ikki xonali sonlarni qo‘shishda o‘nliklar o‘nliklarga, birliklar birliklarga qo‘shiladi:\n"
          "47 + 25 = (40 + 20) + (7 + 5) = 60 + 12 = 72.\n"
          "Ayirishda birliklar yetmasa, bitta o‘nlikni birliklarga aylantiramiz: 63 − 28 = 35.", C1),
    topic(3, "three_digit", "3", "💯", L("Uch xonali sonlar", "Three-digit numbers", "Трёхзначные числа"), "place_value",
          lv({"min": 100, "max": 999, "modes": ["place", "expanded"], "mode": "choice"},
             {"min": 100, "max": 999, "modes": ["place", "expanded", "write"], "mode": "mixed"},
             {"min": 100, "max": 999, "modes": ["write", "expanded", "count"], "mode": "input"}),
          "Uch xonali son uchta xonadan iborat: yuzlar, o‘nlar va birlar.\n"
          "507 = 5 yuzlik + 0 o‘nlik + 7 birlik = 500 + 7.\n"
          "Son yozilganda bo‘sh xonaga 0 qo‘yiladi: “to‘rt yuz sakkiz” — 408.", C1, ["math_g3.review_100"]),
    topic(3, "multi_digit", "4", "🔢", L("Ko‘p xonali sonlar", "Multi-digit numbers", "Многозначные числа"), "place_value",
          lv({"min": 1000, "max": 9999, "modes": ["place", "expanded"], "mode": "choice"},
             {"min": 1000, "max": 99999, "modes": ["place", "expanded", "write", "count"], "mode": "mixed"},
             {"min": 10000, "max": 999999, "modes": ["write", "expanded", "count"], "mode": "input"}),
          "Ko‘p xonali sonlar o‘ngdan chapga uchta xonadan sinflarga bo‘linadi: birlar sinfi va minglar sinfi.\n"
          "45 302 — qirq besh ming uch yuz ikki.\n"
          "Xonalar: birlar, o‘nlar, yuzlar, minglar, o‘n minglar, yuz minglar.\n"
          "Pozitsion sanoq: bitta raqam turgan joyiga qarab turli qiymat oladi — 3 045 da 3 minglarni, 345 da yuzlarni bildiradi.", C1, ["math_g3.three_digit"]),
    topic(3, "compare", "5", "⚖️", L("Sonlarni taqqoslash", "Comparing numbers", "Сравнение чисел"), "compare",
          lv({"min": 100, "max": 999, "mode": "choice"}, {"min": 1000, "max": 9999, "mode": "choice"}, {"min": 10000, "max": 999999, "mode": "choice"}),
          "Ikki sonni taqqoslash:\n"
          "1) Xonalari ko‘p bo‘lgan son katta: 1 205 > 987.\n"
          "2) Xonalar soni teng bo‘lsa, chapdan boshlab raqamlarni solishtiramiz: 4 563 < 4 571 (o‘nlar: 6 < 7).\n"
          "Belgilar: > katta, < kichik, = teng.", C1, ["math_g3.multi_digit"]),
    topic(3, "round", "6", "🎯", L("Sonlarni yaxlitlash", "Rounding numbers", "Округление чисел"), "round",
          lv({"max": 999, "places": ["10"], "mode": "choice"}, {"max": 9999, "places": ["10", "100"], "mode": "mixed"},
             {"max": 99999, "places": ["10", "100", "1000"], "mode": "input"}),
          "Sonni yaxlitlashda keyingi xonadagi raqamga qaraymiz:\n"
          "• 0, 1, 2, 3, 4 bo‘lsa — pastga: 342 ≈ 340.\n"
          "• 5, 6, 7, 8, 9 bo‘lsa — yuqoriga: 347 ≈ 350.\n"
          "Yuzlargacha: 2 651 ≈ 2 700.", C1, ["math_g3.compare"]),
    topic(3, "add", "7", "➕", L("Ko‘p xonali sonlarni qo‘shish", "Adding multi-digit numbers", "Сложение многозначных чисел"), "add_sub",
          lv({"min": 100, "max": 999, "ops": ["+"], "mode": "choice"}, {"min": 1000, "max": 9999, "ops": ["+"], "mode": "mixed"},
             {"min": 1000, "max": 99999, "ops": ["+"], "mode": "input"}),
          "Ustun usulida qo‘shish: sonlarni xonama-xona ustma-ust yozamiz va birlardan boshlaymiz.\n"
          "  2 468\n+ 1 357\n  3 825\n"
          "Xonadagi yig‘indi 10 dan oshsa, 1 ni keyingi xonaga o‘tkazamiz (8 + 7 = 15: 5 yoziladi, 1 o‘tadi).", C1, ["math_g3.multi_digit"]),
    topic(3, "sub", "8", "➖", L("Ko‘p xonali sonlarni ayirish", "Subtracting multi-digit numbers", "Вычитание многозначных чисел"), "add_sub",
          lv({"min": 100, "max": 999, "ops": ["-"], "mode": "choice"}, {"min": 1000, "max": 9999, "ops": ["-"], "mode": "mixed"},
             {"min": 1000, "max": 99999, "ops": ["-"], "mode": "input"}),
          "Ustun usulida ayirish: birlardan boshlaymiz.\n"
          "  5 302\n− 1 745\n  3 557\n"
          "Raqam yetmasa, chapdagi xonadan 1 ta birlik “olamiz” (u 10 ga aylanadi).\n"
          "Tekshirish: ayirma + ayiriluvchi = kamayuvchi (3 557 + 1 745 = 5 302).", C1, ["math_g3.add"]),
    test(3, "test1", "N1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
         ["table", "review_100", "three_digit", "multi_digit", "compare", "round", "add", "sub"], C1),

    topic(3, "pow10", "9", "🔟", L("10, 100, 1000 ga ko‘paytirish va bo‘lish", "Multiplying and dividing by 10, 100, 1000", "Умножение и деление на 10, 100, 1000"), "mul_div",
          lv({"aMin": 2, "aMax": 50, "modes": ["pow10"], "mode": "choice"}, {"aMin": 2, "aMax": 99, "modes": ["pow10"], "mode": "mixed"},
             {"aMin": 12, "aMax": 999, "modes": ["pow10"], "mode": "input"}),
          "10 ga ko‘paytirishda son oxiriga bitta 0 yoziladi: 37 · 10 = 370.\n"
          "100 ga — ikkita 0: 37 · 100 = 3 700;  1000 ga — uchta 0: 37 · 1000 = 37 000.\n"
          "Oxiri nollar bilan tugagan sonni 10, 100, 1000 ga bo‘lishda shuncha 0 olib tashlanadi: 4 500 : 100 = 45.", C2, ["math_g3.table"]),
    topic(3, "mul", "10", "✖️", L("Bir xonali songa ko‘paytirish", "Multiplying by a one-digit number", "Умножение на однозначное число"), "mul_div",
          lv({"aMin": 11, "aMax": 49, "bMin": 2, "bMax": 5, "modes": ["mul"], "mode": "choice"},
             {"aMin": 12, "aMax": 99, "bMin": 2, "bMax": 9, "modes": ["mul"], "mode": "mixed"},
             {"aMin": 101, "aMax": 999, "bMin": 2, "bMax": 9, "modes": ["mul"], "mode": "input"}),
          "Taqsimot xossasi: (a + b) · c = a · c + b · c.\n"
          "34 · 6 = 30 · 6 + 4 · 6 = 180 + 24 = 204.\n"
          "Ustun usulida birlardan boshlaymiz: 4 · 6 = 24 → 4 yoziladi, 2 o‘nlik keyingi xonaga qo‘shiladi.", C2, ["math_g3.table"]),
    topic(3, "div", "11", "➗", L("Bir xonali songa bo‘lish", "Dividing by a one-digit number", "Деление на однозначное число"), "mul_div",
          lv({"aMin": 20, "aMax": 99, "bMin": 2, "bMax": 5, "modes": ["div"], "mode": "choice"},
             {"aMin": 20, "aMax": 999, "bMin": 2, "bMax": 9, "modes": ["div"], "mode": "mixed"},
             {"aMin": 100, "aMax": 9999, "bMin": 2, "bMax": 9, "modes": ["div"], "mode": "input"}),
          "Yig‘indini songa bo‘lish: (60 + 12) : 6 = 60 : 6 + 12 : 6 = 10 + 2 = 12.\n"
          "Burchak usuli: chapdan boshlab bo‘lamiz. 852 : 4 → 8 : 4 = 2, 5 : 4 = 1 (qoldiq 1), 12 : 4 = 3 → 213.\n"
          "Tekshirish: bo‘linma · bo‘luvchi = bo‘linuvchi (213 · 4 = 852).", C2, ["math_g3.mul"]),
    topic(3, "remainder", "12", "🍬", L("Qoldiqli bo‘lish", "Division with remainder", "Деление с остатком"), "mul_div",
          lv({"aMin": 10, "aMax": 50, "bMin": 2, "bMax": 5, "modes": ["remainder"], "mode": "choice"},
             {"aMin": 10, "aMax": 99, "bMin": 2, "bMax": 9, "modes": ["remainder"], "mode": "mixed"},
             {"aMin": 100, "aMax": 999, "bMin": 2, "bMax": 9, "modes": ["remainder"], "mode": "input"}),
          "Har doim ham son qoldiqsiz bo‘linmaydi: 17 ta konfetni 5 bolaga teng bo‘lsak, har biriga 3 tadan tegadi va 2 ta qoladi.\n"
          "17 : 5 = 3 (qoldiq 2), chunki 3 · 5 + 2 = 17.\n"
          "Qoidasi: qoldiq har doim bo‘luvchidan kichik bo‘ladi.", C2, ["math_g3.div"]),
    topic(3, "order", "13", "🧮", L("Amallar tartibi", "Order of operations", "Порядок действий"), "order_ops",
          lv({"max": 10, "parens": False, "mode": "choice"}, {"max": 20, "parens": True, "mode": "mixed"}, {"max": 30, "parens": True, "mode": "input"}),
          "Ifodada amallar quyidagi tartibda bajariladi:\n"
          "1) qavs ichidagi amallar;\n2) ko‘paytirish va bo‘lish (chapdan o‘ngga);\n3) qo‘shish va ayirish (chapdan o‘ngga).\n"
          "Misol: 20 + 4 · 5 = 20 + 20 = 40;  (20 + 4) · 5 = 24 · 5 = 120.", C2, ["math_g3.mul"]),
    topic(3, "equation", "14", "❓", L("Tenglamalar", "Equations", "Уравнения"), "equation",
          lv({"max": 50, "forms": ["x+a", "x-a"], "mode": "choice"}, {"max": 100, "forms": ["x+a", "x-a", "a-x", "x*a"], "mode": "mixed"},
             {"max": 500, "mode": "input"}),
          "Tenglama — noma’lum son (x) qatnashgan tenglik. Uni yechish — x ni topish.\n"
          "• x + 35 = 80 → x = 80 − 35 = 45 (noma’lum qo‘shiluvchi).\n"
          "• x − 12 = 30 → x = 30 + 12 = 42 (noma’lum kamayuvchi).\n"
          "• x · 6 = 54 → x = 54 : 6 = 9 (noma’lum ko‘paytuvchi).\n"
          "Tekshirish: topilgan sonni tenglamaga qo‘yib ko‘ring.", C2, ["math_g3.order"]),
    test(3, "test2", "N2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["pow10", "mul", "div", "remainder", "order", "equation"], C2),

    topic(3, "mass", "15", "⚖️", L("Massa birliklari", "Units of mass", "Единицы массы"), "units",
          lv({"kinds": ["mass"], "modes": ["simple"], "max": 9, "mode": "choice"}, {"kinds": ["mass"], "modes": ["simple", "reverse"], "max": 9, "mode": "mixed"},
             {"kinds": ["mass"], "modes": ["simple", "compound", "reverse"], "max": 20, "mode": "input"}),
          "1 kg = 1 000 g\n1 sentner = 100 kg\n1 t (tonna) = 1 000 kg = 10 sentner\n"
          "Katta birlikdan kichigiga o‘tishda ko‘paytiramiz: 3 kg = 3 000 g.\n"
          "Kichik birlikdan kattasiga o‘tishda bo‘lamiz: 5 000 kg = 5 t.", C3),
    topic(3, "length", "16", "📏", L("Uzunlik birliklari", "Units of length", "Единицы длины"), "units",
          lv({"kinds": ["length"], "modes": ["simple"], "max": 9, "mode": "choice"}, {"kinds": ["length"], "modes": ["simple", "reverse"], "max": 9, "mode": "mixed"},
             {"kinds": ["length"], "modes": ["simple", "compound", "reverse"], "max": 20, "mode": "input"}),
          "1 sm = 10 mm\n1 dm = 10 sm\n1 m = 10 dm = 100 sm = 1 000 mm\n1 km = 1 000 m\n"
          "Misol: 3 m 45 sm = 300 sm + 45 sm = 345 sm.", C3),
    topic(3, "area_units", "17", "⬛", L("Yuza birliklari: ar va gektar", "Units of area: are and hectare", "Единицы площади: ар и гектар"), "units",
          lv({"kinds": ["area"], "modes": ["simple"], "max": 9, "mode": "choice"}, {"kinds": ["area"], "modes": ["simple", "reverse"], "max": 9, "mode": "mixed"},
             {"kinds": ["area"], "modes": ["simple", "compound", "reverse"], "max": 20, "mode": "input"}),
          "Yuza kvadrat birliklarda o‘lchanadi: 1 sm² — tomoni 1 sm bo‘lgan kvadrat yuzi.\n"
          "1 dm² = 100 sm²,  1 m² = 100 dm²\n1 ar (sotix) = 100 m²,  1 ga (gektar) = 100 ar = 10 000 m²\n"
          "Yer maydonlari ar va gektarda o‘lchanadi.", C3, ["math_g3.length"]),
    topic(3, "time_units", "18", "⏰", L("Vaqt birliklari", "Units of time", "Единицы времени"), "units",
          lv({"kinds": ["time"], "modes": ["simple"], "max": 5, "mode": "choice"}, {"kinds": ["time"], "modes": ["simple", "reverse"], "max": 9, "mode": "mixed"},
             {"kinds": ["time"], "modes": ["simple", "compound", "reverse"], "max": 12, "mode": "input"}),
          "1 minut = 60 sekund\n1 soat = 60 minut\n1 sutka = 24 soat\n1 hafta = 7 kun\n1 yil = 12 oy\n"
          "Misol: 2 soat 15 minut = 120 + 15 = 135 minut.", C3),
    topic(3, "clock", "19", "🕰️", L("Vaqtni hisoblash", "Calculating time", "Вычисление времени"), "time_calc",
          lv({"mode": "choice"}, {"mode": "mixed"}, {"mode": "input"}),
          "Tugash vaqti = boshlanish vaqti + davomiylik.\n"
          "Dars 8:30 da boshlanib 45 minut davom etsa: 8:30 + 30 min = 9:00, yana 15 min → 9:15.\n"
          "Davomiylik = tugash vaqti − boshlanish vaqti: 14:20 dan 16:05 gacha → 1 soat 45 minut = 105 minut.", C3, ["math_g3.time_units"]),
    topic(3, "perimeter", "20", "⬛", L("Perimetr va yuza", "Perimeter and area", "Периметр и площадь"), "perimeter_area",
          lv({"max": 9, "modes": ["perimeter", "square"], "mode": "choice"}, {"max": 12, "modes": ["perimeter", "area", "square"], "mode": "mixed"},
             {"max": 20, "modes": ["perimeter", "area", "square", "inverse"], "mode": "input"}),
          "Perimetr (P) — shakl barcha tomonlari uzunliklarining yig‘indisi.\n"
          "To‘g‘ri to‘rtburchak: P = (a + b) · 2;  kvadrat: P = a · 4.\n"
          "Yuza (S) — shakl egallagan joy, kvadrat birliklarda o‘lchanadi.\n"
          "To‘g‘ri to‘rtburchak: S = a · b;  kvadrat: S = a · a.\n"
          "Misol: 6 sm va 4 sm → P = 20 sm, S = 24 sm².", C3),
    topic(3, "volume", "21", "📦", L("Kub va parallelepiped. Hajm", "Cube and cuboid. Volume", "Куб и параллелепипед. Объём"), "volume",
          lv({"max": 5, "modes": ["cube", "edges"], "mode": "choice"}, {"max": 6, "modes": ["cuboid", "cube", "edges"], "mode": "mixed"},
             {"max": 9, "modes": ["cuboid", "cube", "edges", "liters"], "mode": "input"}),
          "Kubning 6 ta yog‘i (hammasi kvadrat) va 12 ta teng qirrasi bor.\n"
          "To‘g‘ri burchakli parallelepipedning (kuboidning) yog‘lari — to‘g‘ri to‘rtburchaklar.\n"
          "Hajm — jism egallagan joy, kub birliklarda: V = uzunlik · en · balandlik.\n"
          "Kub: V = a · a · a. 1 dm³ = 1 litr.", C3, ["math_g3.perimeter"]),
    test(3, "test3", "N3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["mass", "length", "area_units", "time_units", "clock", "perimeter", "volume"], C3),

    topic(3, "motion", "22", "🚲", L("Harakat: tezlik, vaqt, masofa", "Motion: speed, time, distance", "Движение: скорость, время, расстояние"), "word_problem",
          lv({"kinds": ["speed"], "mode": "choice"}, {"kinds": ["speed"], "mode": "mixed"}, {"kinds": ["speed"], "mode": "input"}),
          "Masofa = tezlik · vaqt   (s = v · t)\nTezlik = masofa : vaqt   (v = s : t)\nVaqt = masofa : tezlik   (t = s : v)\n"
          "Misol: velosipedchi soatiga 12 km tezlik bilan 3 soat yursa, 12 · 3 = 36 km yo‘l bosadi.", C4),
    topic(3, "price", "23", "🛒", L("Narx, miqdor, qiymat", "Price, quantity, cost", "Цена, количество, стоимость"), "word_problem",
          lv({"kinds": ["price"], "mode": "choice"}, {"kinds": ["price"], "mode": "mixed"}, {"kinds": ["price", "rate"], "mode": "input"}),
          "Qiymat = narx · miqdor\nNarx = qiymat : miqdor\nMiqdor = qiymat : narx\n"
          "Misol: bitta daftar 3 000 so‘m bo‘lsa, 4 ta daftar 12 000 so‘m turadi.", C4),
    topic(3, "work", "24", "🛠️", L("Unumdorlik. Marta ko‘p, marta kam", "Work rate. Times more, times less", "Производительность. Во сколько раз"), "word_problem",
          lv({"kinds": ["work", "times"], "mode": "choice"}, {"kinds": ["work", "times"], "mode": "mixed"}, {"kinds": ["work", "times"], "mode": "input"}),
          "Ish hajmi = unumdorlik (1 soatdagi ish) · vaqt.\n"
          "“3 marta ko‘p” — 3 ga ko‘paytiramiz; “3 marta kam” — 3 ga bo‘lamiz.\n"
          "“5 ta ko‘p” — qo‘shamiz; “5 ta kam” — ayiramiz. Masalani o‘qiganda shu so‘zlarga e’tibor bering!", C4),
    topic(3, "problems", "25", "📚", L("Qo‘shish va ayirishga doir masalalar", "Addition and subtraction problems", "Задачи на сложение и вычитание"), "word_problem",
          lv({"kinds": ["sum", "diff"], "max": 200, "mode": "choice"}, {"kinds": ["sum", "diff"], "max": 1000, "mode": "mixed"},
             {"kinds": ["sum", "diff"], "max": 10000, "mode": "input"}),
          "Masalani yechish tartibi:\n1) Diqqat bilan o‘qing: nima ma’lum, nimani topish kerak?\n"
          "2) Amalni tanlang: “hammasi”, “jami” — qo‘shish; “qoldi”, “qanchaga ko‘p/kam” — ayirish.\n3) Hisoblang va javobni tekshiring.", C4),
    topic(3, "fraction_part", "26", "🍕", L("Ulush va kasrlar", "Parts and fractions", "Доли и дроби"), "fraction_part",
          lv({"dens": ["2", "3", "4", "5"], "max": 6, "mode": "choice"}, {"dens": ["2", "3", "4", "5", "6", "8", "10"], "max": 10, "mode": "mixed"},
             {"dens": ["2", "3", "4", "5", "6", "8", "10"], "max": 12, "mode": "input"}),
          "Butunni teng bo‘laklarga bo‘lsak, har bir bo‘lak — ulush. 1/4 — to‘rtdan bir ulush.\n"
          "Kasr: 3/4 — surati 3 (nechta ulush olindi), maxraji 4 (butun nechta teng bo‘lakka bo‘lindi).\n"
          "Sonning qismini topish: 20 ning 3/4 qismi = 20 : 4 · 3 = 15.", C4, ["math_g3.div"]),
    topic(3, "fraction_ops", "27", "🥧", L("Maxrajlari teng kasrlar", "Fractions with equal denominators", "Дроби с одинаковыми знаменателями"), "fraction_ops",
          lv({"modes": ["compare"], "maxDen": 8, "mode": "choice"}, {"modes": ["compare", "add"], "maxDen": 10, "mode": "mixed"},
             {"modes": ["compare", "add", "sub"], "maxDen": 12, "mode": "input"}),
          "Maxrajlari teng kasrlardan surati kattasi katta: 5/8 > 3/8.\n"
          "Qo‘shish va ayirishda suratlar qo‘shiladi (ayiriladi), maxraj o‘zgarmaydi:\n2/7 + 3/7 = 5/7;  6/9 − 2/9 = 4/9.\n"
          "Javobni kasr ko‘rinishida yozish uchun “/” tugmasidan foydalaning.", C4, ["math_g3.fraction_part"]),
    topic(3, "roman", "28", "🏛️", L("Rim raqamlari", "Roman numerals", "Римские цифры"), "roman",
          lv({"max": 12, "mode": "choice"}, {"max": 20, "mode": "mixed"}, {"max": 39, "mode": "input"}),
          "Rim raqamlari: I = 1, V = 5, X = 10, L = 50, C = 100.\n"
          "Kichik raqam kattasidan keyin kelsa — qo‘shiladi: VI = 6, XII = 12.\n"
          "Kichik raqam kattasidan oldin kelsa — ayiriladi: IV = 4, IX = 9, XL = 40.\n"
          "Bir raqam ketma-ket uch martadan ko‘p yozilmaydi: 30 = XXX, 40 = XL.", C4),
    topic(3, "sets", "29", "🔵", L("To‘plamlar", "Sets", "Множества"), "sets",
          lv({"mode": "choice"}, {"mode": "mixed"}, {"mode": "mixed"}),
          "To‘plam — narsalar (elementlar) majmuasi. A = {1, 3, 5} — elementlari 1, 3 va 5.\n"
          "• 3 ∈ A — 3 soni A to‘plamga tegishli; 4 ∉ A — tegishli emas.\n"
          "• Umumiy qismi (kesishma) — ikkala to‘plamda bor elementlar.\n"
          "• Birlashma — ikkala to‘plamning barcha elementlari (takrorlanmasdan).\n"
          "Eyler–Venn diagrammasida to‘plamlar doiralar bilan tasvirlanadi.", C4),
    test(3, "test4", "N4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["motion", "price", "work", "problems", "fraction_part", "fraction_ops", "roman", "sets"], C4),
    test(3, "final", "Y", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
         ["add", "sub", "mul", "div", "remainder", "order", "equation", "length", "mass", "perimeter", "motion", "price", "fraction_part"], C4, level=3),
]

# ============================================================ 5-sinf
D1 = "1-chorak. Natural sonlar va kasrlar"
D2 = "2-chorak. Geometriya, hajm va nisbat"
D3 = "3-chorak. O‘nli kasrlar, me’yor va foiz"
D4 = "4-chorak. O‘rtacha qiymat, burchaklar, tenglamalar"

g5 = [
    topic(5, "millions", "1", "🔢", L("10 milliongacha bo‘lgan sonlar", "Numbers up to 10 million", "Числа до 10 миллионов"), "place_value",
          lv({"min": 10000, "max": 999999, "modes": ["place", "expanded"], "mode": "choice"},
             {"min": 100000, "max": 9999999, "modes": ["place", "expanded", "write", "count"], "mode": "mixed"},
             {"min": 1000000, "max": 9999999, "modes": ["write", "expanded", "count"], "mode": "input"}),
          "Sonlar sinflarga bo‘linadi: birlar sinfi, minglar sinfi, millionlar sinfi (har birida uchtadan xona).\n"
          "4 305 020 — to‘rt million uch yuz besh ming yigirma.\n"
          "1 million = 1 000 ming = 1 000 000.", D1),
    topic(5, "compare", "2", "⚖️", L("Katta sonlarni taqqoslash va yaxlitlash", "Comparing and rounding large numbers", "Сравнение и округление больших чисел"), "compare",
          lv({"min": 10000, "max": 999999, "mode": "choice"}, {"min": 100000, "max": 9999999, "mode": "choice"}, {"min": 1000000, "max": 9999999, "mode": "choice"}),
          "Taqqoslashda avval xonalar sonini, keyin chapdan boshlab raqamlarni solishtiramiz.\n"
          "2 504 318 < 2 540 318 (yuz minglar teng, o‘n minglar: 0 < 4).\n"
          "Yaxlitlash: keyingi xona raqami 5 va undan katta bo‘lsa — yuqoriga.", D1, ["math_g5.millions"]),
    topic(5, "round", "3", "🎯", L("Sonlarni yaxlitlash", "Rounding", "Округление"), "round",
          lv({"max": 99999, "places": ["10", "100"], "mode": "choice"}, {"max": 999999, "places": ["100", "1000"], "mode": "mixed"},
             {"max": 9999999, "places": ["1000"], "mode": "input"}),
          "Sonni biror xonagacha yaxlitlaganda o‘ng tomondagi xonalar 0 ga aylanadi.\n"
          "Keyingi raqam 0–4 → pastga, 5–9 → yuqoriga: 38 462 ≈ 38 000 (minglargacha), 38 562 ≈ 39 000.", D1, ["math_g5.compare"]),
    topic(5, "pow10", "4", "🔟", L("10, 100, 1000 ga ko‘paytirish va bo‘lish", "Multiplying and dividing by 10, 100, 1000", "Умножение и деление на 10, 100, 1000"), "mul_div",
          lv({"aMin": 12, "aMax": 999, "modes": ["pow10"], "mode": "choice"}, {"aMin": 100, "aMax": 9999, "modes": ["pow10"], "mode": "mixed"},
             {"aMin": 100, "aMax": 99999, "modes": ["pow10"], "mode": "input"}),
          "10, 100, 1000 ga ko‘paytirishda son oxiriga 1, 2, 3 ta nol yoziladi: 4 507 · 100 = 450 700.\n"
          "O‘nliklarga ko‘paytirish: 23 · 40 = 23 · 4 · 10 = 920.\n"
          "Bo‘lishda oxiridagi nollar olib tashlanadi: 36 000 : 1 000 = 36.", D1),
    topic(5, "order", "5", "🧮", L("Amallar tartibi", "Order of operations", "Порядок действий"), "order_ops",
          lv({"max": 20, "parens": True, "mode": "choice"}, {"max": 50, "parens": True, "mode": "mixed"}, {"max": 99, "parens": True, "mode": "input"}),
          "Qavssiz ifodada: avval ko‘paytirish va bo‘lish, keyin qo‘shish va ayirish (chapdan o‘ngga).\n"
          "Qavsli ifodada avval qavs ichidagi amallar bajariladi.\n"
          "120 − 60 : 4 · 2 = 120 − 30 = 90;  (120 − 60) : 4 · 2 = 30.", D1),
    topic(5, "mul", "6", "✖️", L("Ko‘p xonali sonlarni ko‘paytirish", "Multiplying multi-digit numbers", "Умножение многозначных чисел"), "mul_div",
          lv({"aMin": 100, "aMax": 999, "bMin": 2, "bMax": 9, "modes": ["mul"], "mode": "choice"},
             {"aMin": 100, "aMax": 9999, "bMin": 11, "bMax": 99, "modes": ["mul"], "mode": "mixed"},
             {"aMin": 100, "aMax": 9999, "bMin": 11, "bMax": 99, "modes": ["mul"], "mode": "input"}),
          "Ikki xonali songa ko‘paytirish: 347 · 26 = 347 · 20 + 347 · 6 = 6 940 + 2 082 = 9 022.\n"
          "Ustun usulida har bir xonaga alohida ko‘paytirib, natijalarni qo‘shamiz.", D1, ["math_g5.pow10"]),
    topic(5, "div", "7", "➗", L("Ko‘p xonali sonlarni bo‘lish", "Dividing multi-digit numbers", "Деление многозначных чисел"), "mul_div",
          lv({"aMin": 100, "aMax": 9999, "bMin": 2, "bMax": 9, "modes": ["div"], "mode": "choice"},
             {"aMin": 1000, "aMax": 99999, "bMin": 11, "bMax": 99, "modes": ["div"], "mode": "mixed"},
             {"aMin": 1000, "aMax": 99999, "bMin": 11, "bMax": 99, "modes": ["div", "remainder"], "mode": "input"}),
          "Burchak usulida bo‘lish: bo‘linuvchining chap qismidan bo‘luvchidan katta bo‘lgan birinchi to‘liqsiz bo‘linuvchini ajratamiz,\n"
          "keyin har bir qadamda bo‘linmaning navbatdagi raqamini topamiz.\n"
          "Tekshirish: bo‘linma · bo‘luvchi (+ qoldiq) = bo‘linuvchi.", D1, ["math_g5.mul"]),
    topic(5, "problems", "8", "📚", L("Matnli masalalar", "Word problems", "Текстовые задачи"), "word_problem",
          lv({"kinds": ["sum", "diff", "times"], "max": 1000, "mode": "choice"}, {"kinds": ["sum", "diff", "times", "price"], "max": 10000, "mode": "mixed"},
             {"kinds": ["sum", "diff", "times", "price", "work"], "max": 100000, "mode": "input"}),
          "Masalani yechishda: shartni qisqa yozing, qaysi kattalik noma’lumligini aniqlang,\n"
          "amallarni tanlang va har bir qadamni tushuntiring. Javobni masala shartiga qo‘yib tekshiring.", D1),
    topic(5, "div_fraction", "9", "➗", L("Bo‘lishni kasr ko‘rinishida yozish", "Division as a fraction", "Деление в виде дроби"), "fraction_decimal",
          lv({"modes": ["division"], "mode": "input"}, {"modes": ["division"], "mode": "input"}, {"modes": ["division", "to_fraction"], "mode": "input"}),
          "Ikki sonning bo‘linmasini kasr ko‘rinishida yozish mumkin: a : b = a/b.\n"
          "3 : 4 = 3/4;  7 : 9 = 7/9.  Kasr chizig‘i — bo‘lish belgisi.\n"
          "Surat maxrajdan katta bo‘lsa — noto‘g‘ri kasr: 9/4 = 2 1/4 (aralash son).", D1),
    topic(5, "to_decimal", "10", "🔄", L("Oddiy kasrni o‘nli kasrga aylantirish", "Fractions to decimals", "Перевод обыкновенной дроби в десятичную"), "fraction_decimal",
          lv({"modes": ["to_decimal"], "mode": "input"}, {"modes": ["to_decimal", "to_fraction"], "mode": "input"}, {"modes": ["to_decimal", "to_fraction"], "mode": "input"}),
          "Maxrajni 10, 100 yoki 1000 ga keltiramiz: 3/4 = 75/100 = 0,75;  2/5 = 4/10 = 0,4.\n"
          "O‘nli kasrni oddiy kasrga: 0,6 = 6/10 = 3/5;  0,25 = 25/100 = 1/4.\n"
          "Vergul uchun “,” tugmasini bosing.", D1, ["math_g5.div_fraction"]),
    topic(5, "mixed", "11", "🥧", L("Aralash sonlarni qo‘shish va ayirish", "Adding and subtracting mixed numbers", "Сложение и вычитание смешанных чисел"), "mixed_numbers",
          lv({"ops": ["add"], "maxDen": 6, "mode": "choice"}, {"ops": ["add", "sub"], "maxDen": 8, "mode": "choice"}, {"ops": ["add", "sub"], "maxDen": 10, "mode": "choice"}),
          "Aralash son — butun va kasr qismdan iborat: 2 3/5.\n"
          "Qo‘shishda butunlar alohida, kasr qismlar alohida qo‘shiladi: 2 1/5 + 1 3/5 = 3 4/5.\n"
          "Kasr qism 1 dan oshsa, butunga o‘tkaziladi: 1 4/5 + 2 3/5 = 3 7/5 = 4 2/5.\n"
          "Ayirishda kasr qism yetmasa, bitta butunni kasrga aylantiramiz: 4 1/5 − 1 3/5 = 3 6/5 − 1 3/5 = 2 3/5.", D1),
    topic(5, "frac_mul", "12", "✖️", L("Kasrlarni ko‘paytirish", "Multiplying fractions", "Умножение дробей"), "fraction_ops",
          lv({"modes": ["mul_nat"], "maxDen": 9, "mode": "input"}, {"modes": ["mul_nat", "mul"], "maxDen": 9, "mode": "input"}, {"modes": ["mul"], "maxDen": 12, "mode": "input"}),
          "Kasrni natural songa ko‘paytirish: surat songa ko‘paytiriladi, maxraj o‘zgarmaydi: 2/9 · 4 = 8/9.\n"
          "Kasrni kasrga ko‘paytirish: surat suratga, maxraj maxrajga: 2/3 · 3/4 = 6/12 = 1/2.\n"
          "Javobni qisqartirib yoki qisqartirmasdan yozishingiz mumkin.", D1),
    topic(5, "frac_part", "13", "🍰", L("Sonning qismini topish", "Finding a fraction of a number", "Нахождение части числа"), "fraction_part",
          lv({"max": 10, "mode": "choice"}, {"max": 15, "inverse": True, "mode": "mixed"}, {"max": 20, "inverse": True, "mode": "input"}),
          "Sonning a/b qismini topish: sonni b ga bo‘lib, a ga ko‘paytiramiz: 36 ning 2/3 qismi = 36 : 3 · 2 = 24.\n"
          "Qismiga ko‘ra sonni topish: sonning 3/5 qismi 30 bo‘lsa, butun son = 30 : 3 · 5 = 50.\n"
          "Qolgan qismning qismi: avval qolgan qismni, keyin uning qismini topamiz.", D1),
    test(5, "test1", "N1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
         ["millions", "compare", "pow10", "order", "mul", "div", "problems", "div_fraction", "to_decimal", "mixed", "frac_mul", "frac_part"], D1),

    topic(5, "triangle", "14", "🔺", L("Uchburchak va murakkab shakllar yuzi", "Area of triangles and composite shapes", "Площадь треугольника и составных фигур"), "triangle_area",
          lv({"max": 10, "mode": "choice"}, {"max": 14, "composite": True, "mode": "mixed"}, {"max": 20, "composite": True, "mode": "input"}),
          "Uchburchak yuzi: S = asos · balandlik : 2 (to‘g‘ri to‘rtburchak yuzining yarmi).\n"
          "Balandlik — uchidan asosga tik tushirilgan kesma.\n"
          "Murakkab shakl yuzini topish uchun uni to‘g‘ri to‘rtburchak va uchburchaklarga bo‘lamiz va yuzalarni qo‘shamiz.", D2),
    topic(5, "volume", "15", "📦", L("Kub va kuboid hajmi", "Volume of cubes and cuboids", "Объём куба и прямоугольного параллелепипеда"), "volume",
          lv({"max": 6, "modes": ["cube", "cuboid"], "mode": "choice"}, {"max": 10, "modes": ["cube", "cuboid", "liters"], "mode": "mixed"},
             {"max": 15, "modes": ["cube", "cuboid", "liters"], "mode": "input"}),
          "Hajm birliklari: sm³, dm³, m³. Kuboid hajmi: V = uzunlik · en · balandlik.\n"
          "Kub hajmi: V = a · a · a.  1 dm³ = 1 l, 1 m³ = 1 000 dm³ = 1 000 l.\n"
          "Misol: 4 dm × 3 dm × 5 dm idishga 60 l suv sig‘adi.", D2),
    topic(5, "volume_units", "16", "🥛", L("Hajm birliklari", "Units of volume", "Единицы объёма"), "units",
          lv({"kinds": ["volume"], "modes": ["simple"], "max": 9, "mode": "choice"}, {"kinds": ["volume"], "modes": ["simple", "reverse"], "max": 9, "mode": "mixed"},
             {"kinds": ["volume"], "modes": ["simple", "compound", "reverse"], "max": 20, "mode": "input"}),
          "1 l = 1 000 ml\n1 dm³ = 1 000 sm³ = 1 l\n1 m³ = 1 000 dm³\n"
          "Suyuqlik hajmi litr va millilitrda o‘lchanadi: 2 l 350 ml = 2 350 ml.", D2, ["math_g5.volume"]),
    topic(5, "ratio", "17", "⚖️", L("Nisbat", "Ratio", "Отношение"), "ratio",
          lv({"modes": ["simplify"], "mode": "choice"}, {"modes": ["simplify", "find"], "mode": "mixed"}, {"modes": ["simplify", "find", "share"], "mode": "input"}),
          "Nisbat ikki miqdorni solishtiradi: 6 o‘g‘il va 9 qiz — 6 : 9 = 2 : 3.\n"
          "Teng kuchli nisbatlar: ikkala hadni bir songa ko‘paytirsak yoki bo‘lsak, nisbat o‘zgarmaydi (2 : 3 = 4 : 6).\n"
          "Jami miqdorni nisbatda bo‘lish: 40 ni 3 : 5 nisbatda → 8 bo‘lak, bir bo‘lak 5 → 15 va 25.", D2),
    test(5, "test2", "N2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["triangle", "volume", "volume_units", "ratio"], D2),

    topic(5, "decimals", "18", "🔟", L("O‘nli kasrlar", "Decimals", "Десятичные дроби"), "decimals",
          lv({"modes": ["compare"], "mode": "choice"}, {"modes": ["compare", "mul10", "div10"], "mode": "input"}, {"modes": ["mul10", "div10"], "mode": "input"}),
          "O‘nli kasr: 3,45 — 3 butun 45 yuzdan. Verguldan keyin: o‘ndan birlar, yuzdan birlar, mingdan birlar.\n"
          "10, 100, 1000 ga ko‘paytirishda vergul o‘ngga 1, 2, 3 xona suriladi: 3,45 · 100 = 345.\n"
          "Bo‘lishda vergul chapga suriladi: 27,3 : 100 = 0,273.\n"
          "Taqqoslash: 0,7 > 0,65, chunki 0,70 > 0,65.", D3),
    topic(5, "units", "19", "📐", L("O‘lchov birliklarini almashtirish", "Converting units", "Перевод единиц измерения"), "units",
          lv({"kinds": ["length", "mass"], "modes": ["simple", "reverse"], "max": 20, "mode": "choice"},
             {"kinds": ["length", "mass", "area", "time"], "modes": ["simple", "compound", "reverse"], "max": 50, "mode": "mixed"},
             {"kinds": ["length", "mass", "area", "time", "volume"], "modes": ["simple", "compound", "reverse"], "max": 99, "mode": "input"}),
          "Katta birlikdan kichigiga — ko‘paytiramiz, kichikdan kattasiga — bo‘lamiz.\n"
          "km → m: · 1 000;  m → sm: · 100;  kg → g: · 1 000;  t → kg: · 1 000;  ga → ar: · 100;  soat → minut: · 60.", D3),
    topic(5, "rate", "20", "🚗", L("Me’yor va birlik narx", "Rates and unit price", "Норма и цена единицы"), "word_problem",
          lv({"kinds": ["rate"], "mode": "choice"}, {"kinds": ["rate", "speed", "work"], "mode": "mixed"}, {"kinds": ["rate", "speed", "work", "price"], "mode": "input"}),
          "Me’yor — bir birlikka to‘g‘ri keladigan miqdor: 1 soatdagi yo‘l, 1 ta narsaning narxi, 1 soatdagi ish.\n"
          "Avval me’yorni topamiz, keyin kerakli miqdorni: 4 ta daftar 12 000 so‘m → 1 tasi 3 000 so‘m → 7 tasi 21 000 so‘m.", D3),
    topic(5, "percent", "21", "💯", L("Foiz", "Percent", "Проценты"), "percent",
          lv({"modes": ["fraction", "decimal"], "mode": "choice"}, {"modes": ["fraction", "decimal", "of"], "mode": "mixed"},
             {"modes": ["of", "discount", "fraction", "decimal"], "mode": "input"}),
          "1% — sonning yuzdan bir qismi: 1% = 1/100 = 0,01.\n"
          "50% = 1/2,  25% = 1/4,  10% = 1/10,  75% = 3/4.\n"
          "Sonning foizini topish: 80 ning 25% i = 80 : 100 · 25 = 20.\n"
          "Chegirma: narx 40 000 so‘m, chegirma 10% → 4 000 so‘m arzon → 36 000 so‘m.", D3),
    test(5, "test3", "N3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["decimals", "units", "rate", "percent"], D3),

    topic(5, "average", "22", "📊", L("O‘rtacha qiymat", "Average", "Среднее арифметическое"), "average",
          lv({"max": 20, "mode": "choice"}, {"max": 60, "mode": "mixed"}, {"max": 99, "mode": "input"}),
          "O‘rtacha qiymat = sonlar yig‘indisi : sonlar soni.\n"
          "12, 15, 18 → (12 + 15 + 18) : 3 = 45 : 3 = 15.\n"
          "Jami qiymat = o‘rtacha qiymat · soni.", D4),
    topic(5, "angles", "23", "📐", L("Burchaklar", "Angles", "Углы"), "angles",
          lv({"modes": ["straight", "right"], "mode": "choice"}, {"modes": ["straight", "vertical", "right"], "mode": "mixed"},
             {"modes": ["straight", "vertical", "right", "triangle"], "mode": "input"}),
          "To‘g‘ri burchak — 90°, yoyiq burchak (to‘g‘ri chiziq) — 180°, to‘liq aylana — 360°.\n"
          "To‘g‘ri chiziqdagi qo‘shni burchaklar yig‘indisi 180°.\n"
          "Vertikal burchaklar (ikki to‘g‘ri chiziq kesishganda qarama-qarshi turadigan) teng.\n"
          "Uchburchak burchaklarining yig‘indisi 180°.", D4),
    topic(5, "equation", "24", "❓", L("Tenglamalar", "Equations", "Уравнения"), "equation",
          lv({"max": 100, "forms": ["x+a", "x-a", "x*a"], "mode": "choice"}, {"max": 500, "mode": "mixed"}, {"max": 1000, "mode": "input"}),
          "Noma’lum komponentni topish qoidalari:\n"
          "qo‘shiluvchi = yig‘indi − boshqa qo‘shiluvchi;  kamayuvchi = ayirma + ayiriluvchi;\n"
          "ayiriluvchi = kamayuvchi − ayirma;  ko‘paytuvchi = ko‘paytma : boshqa ko‘paytuvchi;\n"
          "bo‘linuvchi = bo‘linma · bo‘luvchi;  bo‘luvchi = bo‘linuvchi : bo‘linma.", D4),
    test(5, "test4", "N4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["average", "angles", "equation", "percent", "decimals"], D4),
    test(5, "final", "Y", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
         ["millions", "order", "mul", "div", "to_decimal", "frac_mul", "frac_part", "triangle", "volume", "ratio", "decimals", "percent", "average", "angles", "equation"], D4, level=3),
]


def write(grade, topics):
    for t in topics:
        if t.get("theory") is None:
            t.pop("theory", None)
    data = {
        "subject": "math",
        "ageGroup": f"g{grade}",
        "lessonSize": 8,
        "title": L("Matematika", "Maths", "Математика"),
        "model": "QOIDA → MISOL → MASHQ → NAZORAT",
        "topics": topics,
    }
    path = os.path.join(ROOT, "assets", "data", "school", f"math_g{grade}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(path, len(topics), "mavzu")


write(3, g3)
write(5, g5)

import sys  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_index  # noqa: E402
build_index.build()
