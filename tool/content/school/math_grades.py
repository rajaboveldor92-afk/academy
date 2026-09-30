"""Matematika: 1, 2, 4, 6, 7, 8-sinf dasturlari (3 va 5-sinf — math_curricula.py).

Generatorlar: lib/learning/generators/school/math_school.dart (1–5-sinf mavzulari) va
math_upper.dart (6–8-sinf: butun sonlar, algebra, geometriya). Mavzular O'zbekiston maktab dasturi
tartibida; qoida matnlari o'zimizniki. Ishga tushirish: python3 tool/content/school/math_grades.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import Course, L  # noqa: E402

TITLE = L("Matematika", "Maths", "Математика")


def lv(*levels):
    return [dict(x) for x in levels]


def grade(n, chapters, final_level=3):
    T = Course("math", n, TITLE)
    all_keys = []
    for ci, (chapter, topics) in enumerate(chapters, 1):
        keys = []
        for key, emoji, title, gen, levels, theory in topics:
            T.topic(key, emoji, L(*title), chapter=chapter, theory=theory, gen=gen, levels=levels)
            keys.append(key)
        all_keys += keys
        T.test(f"test{ci}", L(f"{ci}-nazorat ishi", f"Test {ci}", f"Контрольная работа {ci}"), keys, chapter=chapter)
    T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"), all_keys,
           chapter=chapters[-1][0], level=final_level)
    T.write()


def modes(ms, **extra):
    """Uch daraja: tanlash → aralash → yozish."""
    return lv({"modes": ms[0], "mode": "choice", **extra}, {"modes": ms[1], **extra}, {"modes": ms[2], "mode": "input", **extra})


# ================================================================== 1-sinf
grade(1, [
    ("1-chorak. 10 ichida sonlar", [
        ("compare10", "⚖️", ("Sonlarni taqqoslash", "Comparing numbers", "Сравнение чисел"), "compare",
         lv({"min": 1, "max": 9}, {"min": 1, "max": 10}, {"min": 1, "max": 10}),
         "Ikki sonni taqqoslaymiz: katta, kichik yoki teng.\n"
         "• 7 > 5 — yetti beshdan katta (“og‘iz” katta songa qaragan).\n"
         "• 3 < 8 — uch sakkizdan kichik.\n"
         "• 4 = 4 — sonlar teng. Sanoqda keyin keladigan son katta."),
        ("add10", "➕", ("10 ichida qo‘shish va ayirish", "Adding and subtracting within 10", "Сложение и вычитание в пределах 10"), "add_sub",
         lv({"min": 1, "max": 5, "ops": ["+"], "mode": "choice"}, {"min": 1, "max": 5, "ops": ["+"]}, {"min": 2, "max": 10, "ops": ["-"]}),
         "Qo‘shish — narsalar ko‘payadi: 3 ta olmaga 2 ta qo‘shsak, 5 ta bo‘ladi: 3 + 2 = 5.\n"
         "Ayirish — narsalar kamayadi: 5 ta olmadan 2 tasini yesak, 3 ta qoladi: 5 − 2 = 3.\n"
         "Barmoqlar yoki sanoq tayoqchalari bilan tekshirib ko‘ring."),
    ]),
    ("2-chorak. 20 ichida qo‘shish va ayirish", [
        ("add20", "🔟", ("O‘nlikdan o‘tib qo‘shish", "Adding across ten", "Сложение с переходом через десяток"), "add_sub",
         lv({"min": 3, "max": 9, "ops": ["+"], "mode": "choice"}, {"min": 4, "max": 10, "ops": ["+"]}, {"min": 5, "max": 10, "ops": ["+"], "mode": "input"}),
         "O‘nlikdan o‘tib qo‘shish: avval 10 gacha to‘ldiramiz, keyin qolganini qo‘shamiz.\n"
         "8 + 5: 8 + 2 = 10, yana 3 qoldi → 10 + 3 = 13.\n"
         "10 ni tashkil qiluvchi juftlarni eslang: 1 va 9, 2 va 8, 3 va 7, 4 va 6, 5 va 5."),
        ("sub20", "➖", ("20 ichida ayirish", "Subtracting within 20", "Вычитание в пределах 20"), "add_sub",
         lv({"min": 6, "max": 12, "ops": ["-"], "mode": "choice"}, {"min": 8, "max": 18, "ops": ["-"]}, {"min": 10, "max": 20, "ops": ["-"], "mode": "input"}),
         "O‘nlikdan o‘tib ayirish: avval 10 gacha ayiramiz, keyin qolganini.\n"
         "14 − 6: 14 − 4 = 10, yana 2 ni ayiramiz → 10 − 2 = 8.\n"
         "Tekshirish: 8 + 6 = 14 — javob to‘g‘ri."),
    ]),
    ("3-chorak. Ikki xonali sonlar", [
        ("tens", "🔢", ("O‘nliklar va birliklar", "Tens and ones", "Десятки и единицы"), "place_value",
         lv({"min": 11, "max": 99, "modes": ["place"], "mode": "choice"}, {"min": 11, "max": 99, "modes": ["place", "expanded"]},
            {"min": 11, "max": 99, "modes": ["expanded", "write"], "mode": "input"}),
         "Ikki xonali son o‘nliklar va birliklardan iborat.\n"
         "• 36 = 3 ta o‘nlik va 6 ta birlik = 30 + 6.\n"
         "• Chapdagi raqam — o‘nliklar, o‘ngdagisi — birliklar.\n"
         "“Qirq besh” deb aytilsa, 45 deb yoziladi."),
        ("compare100", "⚖️", ("100 gacha sonlarni taqqoslash", "Comparing numbers to 100", "Сравнение чисел до 100"), "compare",
         lv({"min": 10, "max": 50}, {"min": 10, "max": 99}, {"min": 10, "max": 99}),
         "Ikki xonali sonlarni taqqoslashda avval o‘nliklarni solishtiramiz: 52 > 48, chunki 5 o‘nlik 4 o‘nlikdan ko‘p.\n"
         "O‘nliklar teng bo‘lsa, birliklarni solishtiramiz: 63 < 67."),
    ]),
    ("4-chorak. Masalalar va tenglamalar", [
        ("problems", "📖", ("Sodda masalalar", "Simple word problems", "Простые задачи"), "word_problem",
         lv({"kinds": ["sum"], "max": 10, "mode": "choice"}, {"kinds": ["sum", "diff"], "max": 15}, {"kinds": ["sum", "diff"], "max": 20, "mode": "input"}),
         "Masalani o‘qing va savolini toping.\n"
         "• “Hammasi bo‘lib”, “jami” — qo‘shamiz.\n"
         "• “Qoldi”, “nechta kam” — ayiramiz.\n"
         "Javobni yozishdan oldin masalani qayta o‘qib, tekshirib ko‘ring."),
        ("unknown", "❓", ("Noma’lum sonni topish", "Find the missing number", "Найди неизвестное"), "equation",
         lv({"max": 10, "forms": ["x+a"], "mode": "choice"}, {"max": 15, "forms": ["x+a", "x-a"]}, {"max": 20, "forms": ["x+a", "x-a", "a-x"], "mode": "input"}),
         "Noma’lum qo‘shiluvchini topish uchun yig‘indidan ma’lum qo‘shiluvchini ayiramiz:\n"
         "x + 3 = 8 → x = 8 − 3 = 5.\n"
         "Noma’lum kamayuvchini topish uchun ayirmaga ayriluvchini qo‘shamiz: x − 4 = 6 → x = 10."),
    ]),
], final_level=2)

# ================================================================== 2-sinf
grade(2, [
    ("1-chorak. 100 ichida sonlar", [
        ("numbers100", "💯", ("100 ichida sonlar", "Numbers to 100", "Числа до 100"), "place_value",
         lv({"min": 11, "max": 99, "modes": ["place", "expanded"], "mode": "choice"}, {"min": 11, "max": 99, "modes": ["place", "expanded", "write"]},
            {"min": 11, "max": 99, "modes": ["expanded", "write"], "mode": "input"}),
         "Har qanday ikki xonali son — o‘nliklar va birliklar yig‘indisi: 74 = 70 + 4.\n"
         "100 — bu 10 ta o‘nlik, birinchi uch xonali son.\n"
         "Sonni so‘z bilan aytganda avval o‘nliklar, keyin birliklar aytiladi: 74 — yetmish to‘rt."),
        ("compare", "⚖️", ("Taqqoslash", "Comparing", "Сравнение"), "compare",
         lv({"min": 10, "max": 99}, {"min": 10, "max": 99}, {"min": 10, "max": 100}),
         "Avval o‘nliklarni, ular teng bo‘lsa — birliklarni solishtiring.\n"
         "• 81 > 79: 8 o‘nlik 7 o‘nlikdan ko‘p.\n"
         "• 45 < 49: o‘nliklar teng, 5 birlik 9 birlikdan kam."),
    ]),
    ("2-chorak. 100 ichida qo‘shish va ayirish", [
        ("add", "➕", ("Ikki xonali sonlarni qo‘shish", "Adding two-digit numbers", "Сложение двузначных чисел"), "add_sub",
         lv({"min": 10, "max": 40, "ops": ["+"], "mode": "choice"}, {"min": 10, "max": 50, "ops": ["+"]}, {"min": 15, "max": 50, "ops": ["+"], "mode": "input"}),
         "O‘nliklarni o‘nliklarga, birliklarni birliklarga qo‘shamiz:\n"
         "34 + 25 = (30 + 20) + (4 + 5) = 50 + 9 = 59.\n"
         "Birliklar 10 dan oshsa, bitta o‘nlik hosil bo‘ladi: 38 + 45 = 70 + 13 = 83."),
        ("sub", "➖", ("Ikki xonali sonlarni ayirish", "Subtracting two-digit numbers", "Вычитание двузначных чисел"), "add_sub",
         lv({"min": 20, "max": 60, "ops": ["-"], "mode": "choice"}, {"min": 20, "max": 99, "ops": ["-"]}, {"min": 30, "max": 99, "ops": ["-"], "mode": "input"}),
         "O‘nliklardan o‘nliklarni, birliklardan birliklarni ayiramiz: 68 − 25 = 43.\n"
         "Birliklar yetmasa, bitta o‘nlikni 10 ta birlikka aylantiramiz: 52 − 17 = 35.\n"
         "Tekshirish: 35 + 17 = 52."),
    ]),
    ("3-chorak. Ko‘paytirish va bo‘lish", [
        ("table", "✖️", ("Ko‘paytirish jadvali (2–5)", "Times tables 2–5", "Таблица умножения 2–5"), "mul_table",
         lv({"min": 2, "max": 3, "division": False, "mode": "choice"}, {"min": 2, "max": 5, "division": False}, {"min": 2, "max": 5, "division": True, "mode": "input"}),
         "Ko‘paytirish — bir xil sonlarni qo‘shishning qisqa yozuvi: 3 · 4 = 3 + 3 + 3 + 3 = 12.\n"
         "Ko‘paytuvchilar o‘rnini almashtirsa, natija o‘zgarmaydi: 3 · 4 = 4 · 3.\n"
         "Bo‘lish — teng bo‘laklarga ajratish: 12 : 4 = 3, chunki 3 · 4 = 12."),
        ("unknown", "❓", ("Noma’lum sonni topish", "Find the unknown", "Найди неизвестное"), "equation",
         lv({"max": 30, "forms": ["x+a", "x-a"], "mode": "choice"}, {"max": 50, "forms": ["x+a", "x-a", "a-x"]}, {"max": 99, "forms": ["x+a", "x-a", "a-x"], "mode": "input"}),
         "Tenglama — noma’lum son qatnashgan tenglik.\n"
         "• x + 15 = 40 → x = 40 − 15 = 25.\n"
         "• 50 − x = 20 → x = 50 − 20 = 30.\n"
         "Javobni tenglamaga qo‘yib tekshiring."),
    ]),
    ("4-chorak. Kattaliklar va masalalar", [
        ("length", "📏", ("Uzunlik va vaqt birliklari", "Length and time units", "Единицы длины и времени"), "units",
         lv({"kinds": ["length"], "modes": ["simple"], "max": 5, "mode": "choice"}, {"kinds": ["length", "time"], "modes": ["simple"], "max": 9},
            {"kinds": ["length", "time"], "modes": ["simple", "reverse"], "max": 9, "mode": "input"}),
         "Uzunlik birliklari: 1 dm = 10 sm, 1 m = 10 dm = 100 sm.\n"
         "Vaqt birliklari: 1 soat = 60 minut, 1 sutka = 24 soat.\n"
         "Katta birlikdan kichigiga o‘tganda son ko‘payadi: 3 dm = 30 sm."),
        ("problems", "📖", ("Masalalar", "Word problems", "Задачи"), "word_problem",
         lv({"kinds": ["sum", "diff"], "max": 50, "mode": "choice"}, {"kinds": ["sum", "diff"], "max": 99}, {"kinds": ["sum", "diff"], "max": 99, "mode": "input"}),
         "Masalani yechish tartibi:\n"
         "1) shartni o‘qing va nima ma’lumligini ayting;\n"
         "2) savolni toping — nima topilishi kerak;\n"
         "3) amalni tanlang: “jami” — qo‘shish, “qoldi” — ayirish;\n"
         "4) javobni yozing va tekshiring."),
    ]),
])

# ================================================================== 4-sinf
grade(4, [
    ("1-chorak. Ko‘p xonali sonlar", [
        ("multi", "🔢", ("Ko‘p xonali sonlar", "Multi-digit numbers", "Многозначные числа"), "place_value",
         lv({"min": 10000, "max": 999999, "modes": ["place", "expanded"], "mode": "choice"},
            {"min": 10000, "max": 999999, "modes": ["place", "expanded", "write", "count"]},
            {"min": 100000, "max": 999999, "modes": ["write", "expanded", "count"], "mode": "input"}),
         "Ko‘p xonali son sinflarga ajratiladi: birlar sinfi (birlar, o‘nlar, yuzlar) va minglar sinfi.\n"
         "345 207 — uch yuz qirq besh ming ikki yuz yetti.\n"
         "Sinflar orasida bo‘sh joy qoldirib yoziladi, bo‘sh xonaga 0 qo‘yiladi."),
        ("round", "🎯", ("Yaxlitlash", "Rounding", "Округление"), "round",
         lv({"max": 9999, "places": ["10", "100"], "mode": "choice"}, {"max": 99999, "places": ["10", "100", "1000"]},
            {"max": 999999, "places": ["100", "1000"], "mode": "input"}),
         "Yaxlitlashda keyingi xonadagi raqamga qaraymiz:\n"
         "• 0, 1, 2, 3, 4 bo‘lsa — raqam o‘zgarmaydi: 4 328 ≈ 4 300.\n"
         "• 5, 6, 7, 8, 9 bo‘lsa — 1 qo‘shiladi: 4 378 ≈ 4 400.\n"
         "Keyingi xonalar nolga aylanadi."),
    ]),
    ("2-chorak. Ko‘paytirish va bo‘lish", [
        ("mul", "✖️", ("Ko‘p xonali sonni ko‘paytirish", "Long multiplication", "Умножение многозначных чисел"), "mul_div",
         lv({"aMin": 100, "aMax": 999, "bMin": 2, "bMax": 9, "modes": ["mul"], "mode": "choice"},
            {"aMin": 100, "aMax": 9999, "bMin": 11, "bMax": 30, "modes": ["mul"]},
            {"aMin": 100, "aMax": 9999, "bMin": 11, "bMax": 99, "modes": ["mul"], "mode": "input"}),
         "Ikki xonali songa ko‘paytirish: 234 · 26 = 234 · 20 + 234 · 6 = 4 680 + 1 404 = 6 084.\n"
         "Ustun usulida: avval birlarga, keyin o‘nlarga ko‘paytiring va natijalarni qo‘shing."),
        ("div", "➗", ("Bo‘lish va qoldiq", "Division with remainder", "Деление с остатком"), "mul_div",
         lv({"aMin": 100, "aMax": 999, "bMin": 2, "bMax": 9, "modes": ["div"], "mode": "choice"},
            {"aMin": 1000, "aMax": 9999, "bMin": 2, "bMax": 9, "modes": ["div", "remainder"]},
            {"aMin": 1000, "aMax": 99999, "bMin": 11, "bMax": 50, "modes": ["div", "remainder"], "mode": "input"}),
         "Burchak usulida bo‘lish: bo‘linuvchining boshidan bo‘luvchiga yetadigan qismini ajratamiz.\n"
         "Qoldiq har doim bo‘luvchidan kichik: 47 : 5 = 9 (qoldiq 2), chunki 9 · 5 + 2 = 47."),
        ("order", "🧮", ("Amallar tartibi", "Order of operations", "Порядок действий"), "order_ops",
         lv({"max": 20, "parens": False, "mode": "choice"}, {"max": 50, "parens": True}, {"max": 99, "parens": True, "mode": "input"}),
         "Amallar tartibi:\n"
         "1) qavs ichidagi amallar;\n"
         "2) ko‘paytirish va bo‘lish (chapdan o‘ngga);\n"
         "3) qo‘shish va ayirish (chapdan o‘ngga).\n"
         "Misol: 20 − 3 · 4 = 20 − 12 = 8."),
    ]),
    ("3-chorak. Kasrlar va kattaliklar", [
        ("fractions", "🍕", ("Kasrlar", "Fractions", "Дроби"), "fraction_ops",
         lv({"modes": ["compare"], "maxDen": 10, "mode": "choice"}, {"modes": ["compare", "add", "sub"], "maxDen": 12},
            {"modes": ["add", "sub"], "maxDen": 12, "mode": "input"}),
         "Kasr — butunning teng bo‘laklari: 3/8 — butun 8 bo‘lakka bo‘lingan, 3 tasi olingan.\n"
         "Maxrajlari bir xil kasrlarni qo‘shishda suratlar qo‘shiladi: 2/7 + 3/7 = 5/7.\n"
         "Maxrajlari bir xil bo‘lsa, surati katta kasr katta."),
        ("frac_part", "🥧", ("Sonning qismini topish", "Fraction of a number", "Часть числа"), "fraction_part",
         lv({"dens": ["2", "3", "4", "5"], "max": 10, "mode": "choice"}, {"max": 15}, {"max": 20, "inverse": True, "mode": "input"}),
         "Sonning qismini topish: songa maxrajga bo‘lib, suratga ko‘paytiramiz.\n"
         "24 ning 3/4 qismi: 24 : 4 = 6, 6 · 3 = 18.\n"
         "Qismiga ko‘ra sonni topish: qismni suratga bo‘lib, maxrajga ko‘paytiramiz."),
        ("units", "⚖️", ("Kattaliklar", "Quantities", "Величины"), "units",
         lv({"kinds": ["length", "mass"], "modes": ["simple"], "max": 20, "mode": "choice"},
            {"kinds": ["length", "mass", "time", "area"], "modes": ["simple", "compound"], "max": 20},
            {"kinds": ["length", "mass", "time", "area"], "modes": ["simple", "compound", "reverse"], "max": 50, "mode": "input"}),
         "Asosiy birliklar: 1 km = 1 000 m, 1 m = 100 sm, 1 t = 1 000 kg, 1 kg = 1 000 g, 1 soat = 60 minut, 1 m² = 100 dm².\n"
         "Katta birlikdan kichigiga o‘tishda ko‘paytiramiz, kichigidan kattasiga o‘tishda bo‘lamiz."),
    ]),
    ("4-chorak. Geometriya va masalalar", [
        ("perimeter", "📐", ("Perimetr va yuza", "Perimeter and area", "Периметр и площадь"), "perimeter_area",
         lv({"max": 15, "modes": ["perimeter", "area"], "mode": "choice"}, {"max": 25, "modes": ["perimeter", "area", "square"]},
            {"max": 30, "modes": ["perimeter", "area", "square", "inverse"], "mode": "input"}),
         "To‘g‘ri to‘rtburchak perimetri P = (a + b) · 2, yuzi S = a · b.\n"
         "Kvadrat: P = a · 4, S = a · a.\n"
         "Misol: tomonlari 6 sm va 4 sm → P = 20 sm, S = 24 sm²."),
        ("motion", "🚗", ("Harakatga doir masalalar", "Motion problems", "Задачи на движение"), "word_problem",
         lv({"kinds": ["speed"], "mode": "choice"}, {"kinds": ["speed", "price"]}, {"kinds": ["speed", "work", "price"], "mode": "input"}),
         "Masofa = tezlik · vaqt: S = v · t.\n"
         "Tezlik = masofa : vaqt; vaqt = masofa : tezlik.\n"
         "Misol: avtomobil soatiga 60 km tezlik bilan 3 soat yursa, 180 km yo‘l bosadi."),
        ("equation", "❓", ("Tenglamalar", "Equations", "Уравнения"), "equation",
         lv({"max": 200, "mode": "choice"}, {"max": 500}, {"max": 1000, "mode": "input"}),
         "Noma’lum ko‘paytuvchi = ko‘paytma : ma’lum ko‘paytuvchi: x · 7 = 63 → x = 9.\n"
         "Noma’lum bo‘linuvchi = bo‘linma · bo‘luvchi: x : 4 = 25 → x = 100.\n"
         "Noma’lum bo‘luvchi = bo‘linuvchi : bo‘linma: 72 : x = 8 → x = 9."),
    ]),
])

# ================================================================== 6-sinf
grade(6, [
    ("1-chorak. Bo‘linish va oddiy kasrlar", [
        ("divisibility", "➗", ("EKUB, EKUK va tub sonlar", "GCD, LCM and primes", "НОД, НОК и простые числа"), "divisibility",
         modes([["gcd", "prime"], ["gcd", "lcm", "prime", "divisors"], ["gcd", "lcm", "factor"]]),
         "Tub son faqat 1 ga va o‘ziga bo‘linadi: 2, 3, 5, 7, 11, 13 …\n"
         "EKUB — eng katta umumiy bo‘luvchi: EKUB(12; 18) = 6.\n"
         "EKUK — eng kichik umumiy karrali: EKUK(4; 6) = 12.\n"
         "Sonlarni tub ko‘paytuvchilarga ajratish ikkalasini topishga yordam beradi: 60 = 2 · 2 · 3 · 5."),
        ("fractions", "🍕", ("Kasrlar ustida amallar", "Operations with fractions", "Действия с дробями"), "fraction_ops",
         modes([["compare", "add"], ["add", "sub", "mul"], ["add", "sub", "mul", "mul_nat"]], maxDen=12),
         "Kasrlarni qo‘shish va ayirish: maxrajlari bir xil bo‘lsa — suratlar qo‘shiladi (ayiriladi).\n"
         "Kasrlarni ko‘paytirish: surat suratga, maxraj maxrajga: 2/3 · 3/5 = 6/15 = 2/5.\n"
         "Javobni qisqartiring: surat va maxrajni EKUB ga bo‘ling."),
    ]),
    ("2-chorak. O‘nli kasrlar va proporsiya", [
        ("decimals", "🔟", ("O‘nli kasrlar ustida amallar", "Decimal operations", "Действия с десятичными дробями"), "decimal_ops",
         modes([["add", "sub"], ["add", "sub", "mul"], ["add", "sub", "mul", "div"]], mixed=True),
         "O‘nli kasrlarni qo‘shish va ayirish: vergulni vergul tagiga yozamiz: 3,45 + 2,5 = 5,95.\n"
         "Butun songa ko‘paytirish: vergulga e’tibor bermay ko‘paytirib, verguldan keyin shuncha xona ajratamiz: 1,25 · 4 = 5.\n"
         "Butun songa bo‘lish: butun qism tugagach, bo‘linmaga vergul qo‘yamiz: 7,2 : 3 = 2,4."),
        ("proportion", "⚖️", ("Nisbat va proporsiya", "Ratio and proportion", "Отношение и пропорция"), "proportion",
         modes([["solve", "direct"], ["solve", "direct", "inverse"], ["solve", "inverse", "scale"]]),
         "Proporsiya — ikki nisbatning tengligi: 2 : 5 = 6 : 15.\n"
         "Asosiy xossa: chetki hadlar ko‘paytmasi o‘rta hadlar ko‘paytmasiga teng: 2 · 15 = 5 · 6.\n"
         "To‘g‘ri proporsiya: biri necha marta ortsa, ikkinchisi ham shuncha ortadi. Teskari proporsiyada — kamayadi."),
    ]),
    ("3-chorak. Butun sonlar va koordinatalar", [
        ("integers", "➖", ("Musbat va manfiy sonlar", "Positive and negative numbers", "Положительные и отрицательные числа"), "integers",
         modes([["compare", "abs", "add"], ["add", "sub", "mul"], ["add", "sub", "mul", "div", "chain"]], max=20),
         "Manfiy sonlar noldan kichik: −5 < 0. Son o‘qida noldan chapda joylashadi.\n"
         "• Ishoralari bir xil sonlarni qo‘shish: modullar qo‘shiladi, ishora saqlanadi: −3 + (−4) = −7.\n"
         "• Ishoralari har xil: kattasidan kichigi ayiriladi, kattasining ishorasi olinadi: −8 + 5 = −3.\n"
         "• Ko‘paytirish: ishoralar bir xil — musbat, har xil — manfiy."),
        ("coords", "📍", ("Koordinatalar tekisligi", "The coordinate plane", "Координатная плоскость"), "coords",
         modes([["quadrant", "distance"], ["quadrant", "distance", "symmetric"], ["symmetric", "distance", "midpoint"]]),
         "Nuqtaning o‘rni ikki son bilan beriladi: abssissa x va ordinata y.\n"
         "Choraklar: I — x > 0, y > 0; II — x < 0, y > 0; III — x < 0, y < 0; IV — x > 0, y < 0.\n"
         "Son o‘qidagi ikki nuqta orasidagi masofa — koordinatalar ayirmasining moduli."),
    ]),
    ("4-chorak. Tenglama, foiz va aylana", [
        ("equations", "❓", ("Tenglamalar", "Equations", "Уравнения"), "linear_eq",
         lv({"modes": ["one"], "mode": "choice"}, {"modes": ["one", "paren"], "neg": True}, {"modes": ["one", "paren", "both"], "neg": True, "mode": "input"}),
         "Tenglamani yechish: noma’lumli hadlarni bir tomonga, sonlarni ikkinchi tomonga o‘tkazamiz.\n"
         "Had boshqa tomonga o‘tganda ishorasi o‘zgaradi: 3x − 5 = 16 → 3x = 21 → x = 7.\n"
         "Qavs oldidagi sonni qavs ichidagi har bir hadga ko‘paytiring: 2(x + 3) = 2x + 6."),
        ("percent", "💯", ("Foizlar", "Percentages", "Проценты"), "percent",
         lv({"modes": ["of", "fraction"], "mode": "choice"}, {"modes": ["of", "discount", "fraction"]}, {"modes": ["of", "discount", "decimal"], "mode": "input"}),
         "1% — sonning yuzdan bir qismi. 25% = 1/4, 50% = 1/2, 20% = 1/5.\n"
         "Sonning foizini topish: songa foizni ko‘paytirib, 100 ga bo‘lamiz: 80 ning 15% i = 80 · 15 : 100 = 12.\n"
         "Chegirmadan keyingi narx = narx − chegirma."),
        ("circle", "⭕", ("Aylana va doira", "Circle", "Окружность и круг"), "circle",
         modes([["length", "diameter"], ["length", "area"], ["length", "area", "diameter"]]),
         "Aylana uzunligi C = 2 · π · r = π · d, doira yuzi S = π · r · r.\n"
         "π ≈ 3,14 — har qanday aylana uzunligining diametriga nisbati.\n"
         "Misol: r = 5 sm → C = 31,4 sm, S = 78,5 sm²."),
    ]),
])

# ================================================================== 7-sinf
grade(7, [
    ("1-chorak. Darajalar va ifodalar", [
        ("powers", "🚀", ("Natural ko‘rsatkichli daraja", "Powers", "Степени"), "powers",
         modes([["value", "pow10"], ["value", "neg_base", "mul_rule"], ["neg_base", "mul_rule", "div_rule"]]),
         "aⁿ — a sonini o‘ziga n marta ko‘paytirish: 2⁵ = 2 · 2 · 2 · 2 · 2 = 32.\n"
         "Xossalar: aᵐ · aⁿ = aᵐ⁺ⁿ, aᵐ : aⁿ = aᵐ⁻ⁿ.\n"
         "Manfiy son juft darajada musbat, toq darajada manfiy: (−2)³ = −8, (−2)⁴ = 16."),
        ("expressions", "🔤", ("Algebraik ifodalar", "Algebraic expressions", "Алгебраические выражения"), "expr",
         modes([["eval"], ["eval", "like_terms"], ["eval", "like_terms", "expand"]]),
         "Harfli ifodaning qiymati: harflar o‘rniga sonlar qo‘yiladi. a = −2 bo‘lsa, 3a + 1 = 3 · (−2) + 1 = −5.\n"
         "O‘xshash hadlar — harfiy qismi bir xil hadlar: 5x + 3x − 2x = 6x.\n"
         "Qavsni ochish: 4(x − 3) = 4x − 12."),
    ]),
    ("2-chorak. Tenglama va qisqa ko‘paytirish", [
        ("equations", "❓", ("Chiziqli tenglamalar", "Linear equations", "Линейные уравнения"), "linear_eq",
         lv({"modes": ["one", "paren"], "neg": True}, {"modes": ["paren", "both"], "neg": True}, {"modes": ["both", "paren"], "neg": True, "mode": "input"}),
         "ax + b = c ko‘rinishidagi tenglama chiziqli tenglama deyiladi.\n"
         "Yechish: 5x + 7 = 2x − 8 → 5x − 2x = −8 − 7 → 3x = −15 → x = −5.\n"
         "Tekshirish: topilgan sonni tenglamaga qo‘ying."),
        ("abridged", "✨", ("Qisqa ko‘paytirish formulalari", "Special products", "Формулы сокращённого умножения"), "abridged",
         modes([["square_sum", "factor"], ["square_sum", "factor", "diff_num"], ["square_num", "diff_num", "square_sum"]]),
         "(a + b)² = a² + 2ab + b²,  (a − b)² = a² − 2ab + b²,  a² − b² = (a − b)(a + b).\n"
         "Misol: (x + 4)² = x² + 8x + 16;  51² − 49² = 2 · 100 = 200.\n"
         "Formulalar hisoblashni ancha tezlashtiradi."),
    ]),
    ("3-chorak. Funksiya va sistemalar", [
        ("functions", "📈", ("Chiziqli funksiya", "Linear function", "Линейная функция"), "linear_func",
         modes([["value", "intercept"], ["value", "root", "intercept"], ["root", "slope", "value"]]),
         "y = kx + b — chiziqli funksiya, grafigi to‘g‘ri chiziq.\n"
         "• k — burchak koeffitsiyenti, b — grafikning OY o‘qi bilan kesishish nuqtasi.\n"
         "• OX o‘qi bilan kesishish: y = 0 → kx + b = 0.\n"
         "Misol: y = 2x − 6 → x = 3 da y = 0."),
        ("systems", "🔗", ("Tenglamalar sistemasi", "Systems of equations", "Системы уравнений"), "system",
         modes([["sumdiff", "word"], ["sumdiff", "elim", "word"], ["elim", "word", "sumdiff"]]),
         "Ikki noma’lumli ikki tenglama — sistema. Qo‘shish usuli: tenglamalarni qo‘shib yoki ayirib, bitta noma’lumni yo‘qotamiz.\n"
         "x + y = 10, x − y = 4 → 2x = 14 → x = 7, y = 3.\n"
         "Topilgan qiymatlarni ikkala tenglamaga qo‘yib tekshiring."),
    ]),
    ("4-chorak. Geometriya va statistika", [
        ("angles", "📐", ("Uchburchak va ko‘pburchak burchaklari", "Angles of polygons", "Углы многоугольников"), "polygon_angles",
         modes([["triangle"], ["triangle", "sum"], ["triangle", "sum", "regular"]]),
         "Uchburchak burchaklari yig‘indisi 180°.\n"
         "n burchakli qavariq ko‘pburchak ichki burchaklari yig‘indisi (n − 2) · 180°.\n"
         "Muntazam ko‘pburchakning hamma burchaklari teng: oltiburchakda (6 − 2) · 180° : 6 = 120°."),
        ("statistics", "📊", ("Statistika", "Statistics", "Статистика"), "stats",
         modes([["mean", "range"], ["mean", "median", "mode"], ["mean", "median", "mode", "range"]]),
         "O‘rta arifmetik — sonlar yig‘indisini ularning soniga bo‘lish.\n"
         "Mediana — tartiblangan qatorning o‘rtasidagi son. Moda — eng ko‘p uchraydigan son.\n"
         "Kenglik — eng katta va eng kichik son ayirmasi."),
    ]),
])

# ================================================================== 8-sinf
grade(8, [
    ("1-chorak. Kvadrat ildiz", [
        ("roots", "🔍", ("Kvadrat ildiz", "Square roots", "Квадратный корень"), "roots",
         modes([["sqrt", "estimate"], ["sqrt", "estimate", "product"], ["simplify", "product", "estimate"]]),
         "√a — kvadrati a ga teng bo‘lgan manfiy bo‘lmagan son: √81 = 9.\n"
         "Xossalar: √(a · b) = √a · √b;  √(k² · a) = k√a: √50 = 5√2.\n"
         "√50 — 7 va 8 orasida, chunki 49 < 50 < 64."),
        ("quadratic", "🎯", ("Kvadrat tenglamalar", "Quadratic equations", "Квадратные уравнения"), "quadratic",
         modes([["incomplete"], ["incomplete", "roots"], ["roots", "disc"]]),
         "ax² + bx + c = 0 — kvadrat tenglama. Diskriminant D = b² − 4ac.\n"
         "D > 0 — ikki ildiz, D = 0 — bitta ildiz, D < 0 — haqiqiy ildiz yo‘q.\n"
         "Chala tenglamalar: x² − 25 = 0 → x = ±5;  x² − 7x = 0 → x = 0 yoki x = 7."),
    ]),
    ("2-chorak. Viyet teoremasi va tengsizliklar", [
        ("vieta", "🔑", ("Viyet teoremasi", "Vieta’s theorem", "Теорема Виета"), "quadratic",
         modes([["vieta_sum", "vieta_prod"], ["vieta_sum", "vieta_prod", "roots"], ["roots", "vieta_sum", "disc"]]),
         "x² + px + q = 0 keltirilgan tenglamada: x₁ + x₂ = −p, x₁ · x₂ = q.\n"
         "Misol: x² − 7x + 12 = 0 → yig‘indisi 7, ko‘paytmasi 12 → ildizlar 3 va 4.\n"
         "Butun ildizlarni tanlash uchun ko‘paytmaning bo‘luvchilarini ko‘rib chiqing."),
        ("inequalities", "⚖️", ("Chiziqli tengsizliklar", "Linear inequalities", "Линейные неравенства"), "inequality",
         modes([["min_int", "max_int"], ["min_int", "max_int", "count"], ["count", "min_int", "max_int"]]),
         "Tengsizlik tenglamadek yechiladi. Manfiy songa ko‘paytirish yoki bo‘lishda belgi teskarisiga o‘zgaradi.\n"
         "2x − 3 > 7 → 2x > 10 → x > 5; eng kichik butun yechim — 6.\n"
         "“≥”, “≤” belgilarida chegara ham yechimga kiradi."),
    ]),
    ("3-chorak. To‘rtburchaklar va Pifagor teoremasi", [
        ("pythagoras", "📐", ("Pifagor teoremasi", "Pythagorean theorem", "Теорема Пифагора"), "pythagoras",
         modes([["hyp"], ["hyp", "leg"], ["hyp", "leg", "check"]]),
         "To‘g‘ri burchakli uchburchakda gipotenuza kvadrati katetlar kvadratlari yig‘indisiga teng: c² = a² + b².\n"
         "Misol: katetlar 6 va 8 → c² = 36 + 64 = 100 → c = 10.\n"
         "Mashhur uchliklar: 3, 4, 5;  5, 12, 13;  8, 15, 17."),
        ("areas", "🟦", ("To‘rtburchaklar yuzasi", "Areas of quadrilaterals", "Площади четырёхугольников"), "polygon_area",
         modes([["parallelogram", "rhombus"], ["parallelogram", "trapezoid", "rhombus"], ["trapezoid", "rhombus", "parallelogram"]]),
         "Parallelogramm: S = a · h. Romb: S = d₁ · d₂ : 2.\n"
         "Trapetsiya: S = (a + b) : 2 · h — asoslar yig‘indisining yarmi balandlikka ko‘paytiriladi.\n"
         "Misol: asoslari 7 va 5, balandligi 4 → S = 24."),
    ]),
    ("4-chorak. Takrorlash", [
        ("polygons", "🔷", ("Ko‘pburchak burchaklari", "Polygon angles", "Углы многоугольников"), "polygon_angles",
         modes([["sum", "regular"], ["regular", "exterior", "sum"], ["regular", "exterior", "triangle"]]),
         "Ichki burchaklar yig‘indisi (n − 2) · 180°, tashqi burchaklar yig‘indisi har doim 360°.\n"
         "Muntazam n burchakli ko‘pburchakning tashqi burchagi 360° : n.\n"
         "Masalan, muntazam o‘nburchakda tashqi burchak 36°, ichki burchak 144°."),
        ("review", "🧠", ("Algebra: takrorlash", "Algebra review", "Алгебра: повторение"), "linear_func",
         modes([["value", "root"], ["root", "slope", "intercept"], ["slope", "root", "value"]]),
         "Chiziqli funksiya y = kx + b: k > 0 bo‘lsa funksiya o‘suvchi, k < 0 bo‘lsa kamayuvchi.\n"
         "Ikki nuqtadan o‘tuvchi to‘g‘ri chiziq: k = (y₂ − y₁) : (x₂ − x₁).\n"
         "Grafik OY o‘qini (0; b) nuqtada kesib o‘tadi."),
    ]),
])
