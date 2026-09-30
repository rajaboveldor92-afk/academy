"""Mental arifmetika: 1–8-sinf dasturlari (generatorlar — lib/learning/generators/school/mental_gen.dart).

Har sinf: 4 chorak, har chorakda 2 mavzu va nazorat ishi; oxirida yillik takrorlash.
Ishga tushirish: python3 tool/content/school/mental_curricula.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import Course, L  # noqa: E402

TITLE = L("Mental arifmetika", "Mental arithmetic", "Ментальная арифметика")

# ------------------------------------------------------------------ qoidalar
TH = {
    "abacus_read": (
        "Abakus (soroban) — sanash taxtachasi. Har bir ustunda 5 ta munchoq bor:\n"
        "• to‘sindan yuqoridagi 1 ta munchoq — 5 ga teng;\n"
        "• pastdagi 4 ta munchoq — har biri 1 ga teng.\n"
        "Faqat to‘singa surilgan munchoqlar sanaladi. Misol: yuqori munchoq va 2 ta pastki munchoq = 7."
    ),
    "abacus_set": (
        "Sonni abakusga qo‘yish:\n"
        "• 1–4: pastki munchoqlarni to‘singa ko‘taramiz;\n"
        "• 5: yuqori munchoqni to‘singa tushiramiz;\n"
        "• 6–9: yuqori munchoq va kerakli pastki munchoqlar.\n"
        "Munchoqni bosing — u to‘singa suriladi, yana bosing — joyiga qaytadi."
    ),
    "abacus_read2": (
        "Ko‘p xonali son: har bir ustun — bitta xona. O‘ngdagi ustun — birlar, chapdagisi — o‘nliklar, undan keyin — yuzliklar.\n"
        "To‘sindagi nuqta birlar ustunini ko‘rsatadi.\n"
        "Misol: o‘nliklarda 3, birlarda 7 — bu 37."
    ),
    "abacus_set2": (
        "Ko‘p xonali sonni chapdan o‘ngga qo‘yamiz: avval eng katta xona, keyin qolganlari.\n"
        "Misol: 406 — yuzliklarga 4, o‘nliklar bo‘sh qoladi (0), birlarga 6.\n"
        "Bo‘sh ustun — nol: unda birorta munchoq to‘singa surilmaydi."
    ),
    "simple": (
        "Oddiy qo‘shish va ayirish: kerakli munchoqlar bo‘sh bo‘lsa, ularni to‘g‘ridan-to‘g‘ri suramiz.\n"
        "• 2 + 2: yana 2 ta pastki munchoqni ko‘taramiz = 4.\n"
        "• 7 − 2: 2 ta pastki munchoqni tushiramiz = 5.\n"
        "Avval abakusda, keyin ko‘z oldingizda (xayolan) bajaring."
    ),
    "friends5": (
        "Kichik do‘stlar — yig‘indisi 5 bo‘lgan juftlar: 1 va 4, 2 va 3.\n"
        "Pastda munchoq yetmasa, 5 dan foydalanamiz:\n"
        "• +4 = +5 − 1   • +3 = +5 − 2   • +2 = +5 − 3   • +1 = +5 − 4\n"
        "Misol: 3 + 4 — yuqori munchoqni tushiramiz (+5) va 1 ta pastki munchoqni olamiz (−1) = 7."
    ),
    "friends5_sub": (
        "Kichik do‘st bilan ayirish: pastda kerakli munchoqlar bo‘lmasa, 5 ni olib, ortiqchasini qaytaramiz.\n"
        "• −4 = −5 + 1   • −3 = −5 + 2   • −2 = −5 + 3   • −1 = −5 + 4\n"
        "Misol: 6 − 3 — yuqori munchoqni ko‘taramiz (−5) va 2 ta pastki munchoqni qo‘shamiz (+2) = 3."
    ),
    "flash": (
        "Flesh-anzan — sonlar ekranda birin-ketin tez ko‘rinadi. Har bir sonni ko‘z oldingizdagi abakusga qo‘shib boring.\n"
        "• “Boshlash” tugmasini bosing va diqqat bilan kuzating.\n"
        "• Oxirida natijani yozing.\n"
        "Xato qilsangiz, sonlarni yana bir bor ko‘rish mumkin."
    ),
    "friends10": (
        "Katta do‘stlar — yig‘indisi 10 bo‘lgan juftlar: 1 va 9, 2 va 8, 3 va 7, 4 va 6, 5 va 5.\n"
        "Ustunda joy yetmasa, o‘nliklar ustunidan foydalanamiz:\n"
        "• +9 = +10 − 1   • +8 = +10 − 2   • +7 = +10 − 3\n"
        "Misol: 8 + 7 — o‘nliklarga 1 qo‘shamiz (+10), birlardan 3 ni olamiz (−3) = 15."
    ),
    "friends10_sub": (
        "Katta do‘st bilan ayirish: birlarda munchoq yetmasa, o‘nliklardan 1 ni olib, katta do‘stni qo‘shamiz.\n"
        "• −9 = −10 + 1   • −8 = −10 + 2   • −6 = −10 + 4\n"
        "Misol: 13 − 8 — o‘nliklardan 1 ni olamiz (−10), birlarga 2 ni qo‘shamiz (+2) = 5."
    ),
    "mixed": (
        "Aralash formula — katta va kichik do‘st birga ishlaydi.\n"
        "• +6 = +1 − 5 + 10   • +7 = +2 − 5 + 10   • +8 = +3 − 5 + 10   • +9 = +4 − 5 + 10\n"
        "Misol: 5 + 6 — birlarga +1 (6), −5 (1), o‘nliklarga +10 → 11.\n"
        "Ayirishda: −6 = −10 + 5 − 1."
    ),
    "chain": (
        "Zanjirli hisob: sonlarni chapdan o‘ngga ketma-ket qo‘shib-ayirib boramiz.\n"
        "Misol: 12 + 7 − 5 + 20: 12 + 7 = 19, 19 − 5 = 14, 14 + 20 = 34.\n"
        "Oraliq natijani abakusdagidek xayolda saqlang."
    ),
    "double_half": (
        "Ikkilantirish va yarmini olish — tez hisobning asosi.\n"
        "• Ikkilantirish: 37 × 2 = 30 × 2 + 7 × 2 = 60 + 14 = 74.\n"
        "• Yarmi: 74 : 2 = 60 : 2 + 14 : 2 = 30 + 7 = 37.\n"
        "• +9 = +10 − 1: 47 + 9 = 57 − 1 = 56."
    ),
    "table": (
        "Karra jadvalini tez aytish — mental hisobning poydevori.\n"
        "• O‘rnini almashtirsa ham natija o‘zgarmaydi: 7 × 8 = 8 × 7 = 56.\n"
        "• 9 ga ko‘paytirish: 10 ga ko‘paytirib, sonning o‘zini ayiramiz: 9 × 7 = 70 − 7 = 63.\n"
        "• 10 va 100 ga ko‘paytirishda son oxiriga nol yoziladi: 36 × 10 = 360."
    ),
    "x5": (
        "5 ga ko‘paytirish: avval 10 ga ko‘paytirib, keyin yarmini olamiz: 48 × 5 = 480 : 2 = 240.\n"
        "5 ga bo‘lish: 2 ga ko‘paytirib, 10 ga bo‘lamiz: 85 : 5 = 170 : 10 = 17.\n"
        "10, 100 ga ko‘paytirish: son oxiriga 1 yoki 2 ta nol yoziladi."
    ),
    "x9": (
        "9 ga ko‘paytirish: 10 ga ko‘paytirib, sonning o‘zini ayiramiz: 23 × 9 = 230 − 23 = 207.\n"
        "4 ga ko‘paytirish: ikki marta ikkilantiramiz: 18 × 4 = 36 × 2 = 72.\n"
        "8 ga ko‘paytirish: uch marta ikkilantiramiz: 15 → 30 → 60 → 120."
    ),
    "x11": (
        "11 ga ko‘paytirish (ikki xonali son): raqamlarni ajratib, o‘rtasiga ularning yig‘indisini yozamiz.\n"
        "• 36 × 11: 3 _ 6, o‘rtaga 3 + 6 = 9 → 396.\n"
        "• 58 × 11: 5 + 8 = 13 — o‘rtaga 3, chapdagi 5 ga 1 qo‘shiladi → 638."
    ),
    "x25": (
        "25 ga ko‘paytirish: 100 ga ko‘paytirib, 4 ga bo‘lamiz: 36 × 25 = 3600 : 4 = 900.\n"
        "Yaxlit songa yaqin sonlar: 346 + 99 = 346 + 100 − 1 = 445; 520 − 98 = 520 − 100 + 2 = 422.\n"
        "Yaxlit songacha to‘ldirib, keyin farqni tuzatamiz."
    ),
    "split": (
        "Sonni xonalarga ajratib ko‘paytirish: 47 × 6 = 40 × 6 + 7 × 6 = 240 + 42 = 282.\n"
        "Uch xonali son: 213 × 4 = 200 × 4 + 13 × 4 = 800 + 52 = 852.\n"
        "Avval kattasini, keyin kichigini hisoblab, qo‘shing."
    ),
    "sq5": (
        "5 bilan tugaydigan sonning kvadrati: o‘nliklar sonini keyingi songa ko‘paytiramiz va oxiriga 25 yozamiz.\n"
        "• 35 × 35: 3 × 4 = 12 → 1225.\n"
        "• 75 × 75: 7 × 8 = 56 → 5625."
    ),
    "x99": (
        "99 ga ko‘paytirish: 100 ga ko‘paytirib, sonning o‘zini ayiramiz: 37 × 99 = 3700 − 37 = 3663.\n"
        "15 ga ko‘paytirish: 10 ga ko‘paytiramiz va uning yarmini qo‘shamiz: 24 × 15 = 240 + 120 = 360.\n"
        "11–19 ga ko‘paytirish: 23 × 14 = 230 + 23 × 4 = 230 + 92 = 322."
    ),
    "percent": (
        "Foizlarni xayolan topish:\n"
        "• 10% — sonni 10 ga bo‘lamiz: 340 ning 10% i = 34.\n"
        "• 50% — yarmi, 25% — to‘rtdan biri, 20% — beshdan biri.\n"
        "Misol: 80 ning 25% i = 80 : 4 = 20."
    ),
    "percent_hard": (
        "Murakkabroq foizlar:\n"
        "• 5% — 10% ning yarmi; 15% = 10% + 5%; 30% — 10% ning 3 barobari.\n"
        "• 75% — to‘rtdan uchi; 1% — sonni 100 ga bo‘lish.\n"
        "Misol: 240 ning 15% i = 24 + 12 = 36."
    ),
    "diffsq": (
        "Yaxlit son atrofida ko‘paytirish: 48 × 52 = (50 − 2) × (50 + 2) = 50 × 50 − 2 × 2 = 2500 − 4 = 2496.\n"
        "Ikkala son yaxlit o‘nlikdan bir xil uzoqlikda bo‘lsa, shu usul juda qulay."
    ),
    "near100": (
        "100 ga yaqin sonlarni ko‘paytirish: 97 × 96.\n"
        "• 100 dan farqlari: 3 va 4.\n"
        "• 97 − 4 = 93 — javobning boshi.\n"
        "• 3 × 4 = 12 — oxirgi ikki raqam. Javob: 9312."
    ),
    "divisible": (
        "Bo‘linish belgilari:\n"
        "• 3 ga — raqamlar yig‘indisi 3 ga bo‘linsa: 471 (4 + 7 + 1 = 12).\n"
        "• 9 ga — raqamlar yig‘indisi 9 ga bo‘linsa: 738 (7 + 3 + 8 = 18).\n"
        "• 4 ga — oxirgi ikki raqam 4 ga bo‘linsa: 316. 6 ga — son juft va 3 ga bo‘linsa."
    ),
    "x125": (
        "125 ga ko‘paytirish: 1000 ga ko‘paytirib, 8 ga bo‘lamiz: 48 × 125 = 48000 : 8 = 6000.\n"
        "25 ga ko‘paytirish: 100 ga ko‘paytirib, 4 ga bo‘lamiz.\n"
        "Yodda tuting: 125 × 8 = 1000, 25 × 4 = 100."
    ),
    "pow2": (
        "2 ning darajalari: 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024.\n"
        "Har safar oldingi sonni ikkilantiramiz.\n"
        "2 ning 10-darajasi = 1024 ni eslab qoling — kompyuterda 1 KB = 1024 bayt."
    ),
    "neg": (
        "Manfiy sonlar bilan zanjir: natija noldan kichik bo‘lishi mumkin.\n"
        "Misol: 5 − 12 = −7; −7 + 20 = 13.\n"
        "Son o‘qida chapga yurish — ayirish, o‘ngga yurish — qo‘shish. Javobda minus belgisini qo‘yishni unutmang."
    ),
    "sq50": (
        "50 ga yaqin sonning kvadrati: 50 dan farqni 25 ga qo‘shamiz (yuzlar) va farqning kvadratini qo‘shamiz.\n"
        "• 53 × 53: 25 + 3 = 28 → 2800; 3 × 3 = 9 → 2809.\n"
        "• 47 × 47: 25 − 3 = 22 → 2200; 3 × 3 = 9 → 2209."
    ),
    "sqrt": (
        "Kvadrat ildizni topish: 1–9 sonlar kvadratlarining oxirgi raqamini eslang: 1, 4, 9, 16, 25, 36, 49, 64, 81.\n"
        "Misol: 576 — oxiri 6, demak ildiz 4 yoki 6 bilan tugaydi.\n"
        "20 × 20 = 400 va 30 × 30 = 900 orasida → 24 × 24 = 576."
    ),
    "gauss": (
        "Ketma-ket sonlar yig‘indisi (Gauss usuli): 1 + 2 + … + 100.\n"
        "Chetdagi juftlar: 1 + 100 = 101, 2 + 99 = 101 … — jami 50 ta juft.\n"
        "101 × 50 = 5050. Qoida: (birinchi + oxirgi) × sonlar soni : 2."
    ),
    "sq2d": (
        "Istalgan ikki xonali sonning kvadrati: 34 × 34 = 30 × 30 + 2 × 30 × 4 + 4 × 4 = 900 + 240 + 16 = 1156.\n"
        "Bu (a + b) × (a + b) = a × a + 2 × a × b + b × b formulasi.\n"
        "Kub: 6 × 6 × 6 = 36 × 6 = 216."
    ),
    "pct_change": (
        "Sonni foizga oshirish va kamaytirish:\n"
        "• 200 ni 15 foizga oshirish: 200 ning 15% i = 30; 200 + 30 = 230.\n"
        "• 80 ni 25 foizga kamaytirish: 80 : 4 = 20; 80 − 20 = 60.\n"
        "Sonning qismi: 360 ning 3/4 qismi = 360 : 4 × 3 = 270."
    ),
}


def lv(*levels):
    return [dict(x) for x in levels]


def grade(n, chapters, final_level=3):
    """chapters: [(chorak nomi, [(key, emoji, (uz, en, ru), theory_key, gen, levels), ...]), ...]"""
    T = Course("mental", n, TITLE, model="QOIDA → ABAKUS → XAYOLAN → NAZORAT")
    all_keys = []
    for ci, (chapter, topics) in enumerate(chapters, 1):
        keys = []
        for key, emoji, title, th, gen, levels in topics:
            T.topic(key, emoji, L(*title), chapter=chapter, theory=TH[th], gen=gen, levels=levels)
            keys.append(key)
        all_keys += keys
        T.test(f"test{ci}", L(f"{ci}-nazorat ishi", f"Test {ci}", f"Контрольная работа {ci}"), keys, chapter=chapter)
    T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"), all_keys,
           chapter=chapters[-1][0], level=final_level)
    T.write()


CH = ["1-chorak", "2-chorak", "3-chorak", "4-chorak"]

# ------------------------------------------------------------------ 1-sinf
grade(1, [
    (f"{CH[0]}. Abakus bilan tanishuv", [
        ("abacus", "🧮", ("Abakus: sonni o‘qish", "The abacus: reading numbers", "Абакус: читаем числа"), "abacus_read", "abacus_read",
         lv({"rods": 1, "options": 3}, {"rods": 1, "options": 4}, {"rods": 1, "options": 4, "mode": "input"})),
        ("set", "✋", ("Sonni abakusga qo‘yish", "Setting numbers", "Ставим числа"), "abacus_set", "abacus_set",
         lv({"rods": 1, "expr": 35}, {"rods": 1, "expr": 50}, {"rods": 1, "expr": 70})),
    ]),
    (f"{CH[1]}. Oddiy hisob", [
        ("simple", "➕", ("Oddiy qo‘shish va ayirish", "Simple adding and subtracting", "Простое сложение и вычитание"), "simple", "chain",
         lv({"n": 2, "rule": "simple", "mode": "choice"}, {"n": 3, "rule": "simple"}, {"n": 4, "rule": "simple", "mode": "input"})),
        ("flash_simple", "⚡", ("Flesh-anzan: oddiy", "Flash cards: simple", "Флеш-анзан: просто"), "flash", "flash",
         lv({"n": 2, "rule": "simple", "ms": 2000}, {"n": 3, "rule": "simple", "ms": 1800}, {"n": 3, "rule": "simple", "ms": 1500})),
    ]),
    (f"{CH[2]}. Kichik do‘stlar", [
        ("friends5", "🤝", ("Kichik do‘stlar: qo‘shish", "Little friends: adding", "Маленькие друзья: сложение"), "friends5", "friends5",
         lv({"types": ["pair", "how", "calc"], "plus": True, "options": 3}, {"types": ["how", "calc"], "plus": True},
            {"types": ["calc", "chain"], "plus": True, "n": 3, "mode": "input"})),
        ("friends5_sub", "🖐️", ("Kichik do‘stlar: ayirish", "Little friends: subtracting", "Маленькие друзья: вычитание"), "friends5_sub", "friends5",
         lv({"types": ["how", "calc"], "options": 3}, {"types": ["how", "calc", "chain"], "n": 3},
            {"types": ["calc", "chain"], "n": 4, "mode": "input"})),
    ]),
    (f"{CH[3]}. Tez ko‘rish", [
        ("abacus2", "🔢", ("Ikki xonali son abakusda", "Two-digit numbers", "Двузначные числа"), "abacus_read2", "abacus_read",
         lv({"rods": 2, "options": 3}, {"rods": 2, "options": 4}, {"rods": 2, "options": 4, "mode": "input"})),
        ("flash5", "⚡", ("Flesh-anzan: kichik do‘stlar", "Flash cards: little friends", "Флеш-анзан: маленькие друзья"), "flash", "flash",
         lv({"n": 3, "rule": "five", "ms": 1800}, {"n": 3, "rule": "five", "ms": 1500}, {"n": 4, "rule": "five", "ms": 1300})),
    ]),
], final_level=2)

# ------------------------------------------------------------------ 2-sinf
grade(2, [
    (f"{CH[0]}. Takrorlash va ikki xonali sonlar", [
        ("review5", "🤝", ("Kichik do‘stlar zanjiri", "Little friends chains", "Цепочки с маленькими друзьями"), "friends5", "friends5",
         lv({"types": ["how", "calc", "chain"], "n": 3}, {"types": ["calc", "chain"], "n": 4}, {"types": ["chain"], "n": 5, "mode": "input"})),
        ("set2", "✋", ("Ikki xonali sonni qo‘yish", "Setting two-digit numbers", "Ставим двузначные числа"), "abacus_set2", "abacus_set",
         lv({"rods": 2, "expr": 0}, {"rods": 2, "expr": 30}, {"rods": 2, "expr": 60})),
    ]),
    (f"{CH[1]}. Katta do‘stlar", [
        ("friends10", "🔟", ("Katta do‘stlar: qo‘shish", "Big friends: adding", "Большие друзья: сложение"), "friends10", "friends10",
         lv({"types": ["pair", "how", "calc"], "plus": True, "options": 3}, {"types": ["how", "calc"], "plus": True},
            {"types": ["calc", "chain"], "plus": True, "n": 3, "mode": "input"})),
        ("friends10_sub", "🔟", ("Katta do‘stlar: ayirish", "Big friends: subtracting", "Большие друзья: вычитание"), "friends10_sub", "friends10",
         lv({"types": ["how", "calc"], "options": 3}, {"types": ["how", "calc", "chain"], "n": 3},
            {"types": ["calc", "chain"], "n": 4, "mode": "input"})),
    ]),
    (f"{CH[2]}. Aralash formula", [
        ("mixed", "🧩", ("Aralash formula", "Mixed formula", "Смешанная формула"), "mixed", "friends10",
         lv({"types": ["mixed"], "plus": True, "options": 3}, {"types": ["mixed", "calc"], "plus": True},
            {"types": ["mixed", "calc", "chain"], "n": 4, "max": 99})),
        ("flash10", "⚡", ("Flesh-anzan: katta do‘stlar", "Flash cards: big friends", "Флеш-анзан: большие друзья"), "flash", "flash",
         lv({"n": 3, "rule": "ten", "ms": 1800}, {"n": 4, "rule": "ten", "ms": 1500}, {"n": 5, "rule": "ten", "ms": 1300})),
    ]),
    (f"{CH[3]}. Tez hisob", [
        ("double", "✌️", ("Ikkilantirish va yarmi", "Doubling and halving", "Удвоение и половина"), "double_half", "tricks",
         lv({"kinds": ["double", "plus9"], "mode": "choice"}, {"kinds": ["double", "half", "plus9"]}, {"kinds": ["double", "half", "plus9"], "mode": "input"})),
        ("chain2", "🔗", ("Zanjirli hisob", "Number chains", "Цепочки вычислений"), "chain", "chain",
         lv({"n": 4, "rule": "ten"}, {"n": 5, "rule": "ten"}, {"n": 6, "rule": "ten", "mode": "input"})),
    ]),
])

# ------------------------------------------------------------------ 3-sinf
grade(3, [
    (f"{CH[0]}. Uch xonali sonlar", [
        ("abacus3", "🧮", ("Uch xonali son abakusda", "Three-digit numbers", "Трёхзначные числа"), "abacus_read2", "abacus_read",
         lv({"rods": 3, "options": 3}, {"rods": 3, "options": 4}, {"rods": 3, "options": 4, "mode": "input"})),
        ("set3", "✋", ("Abakusda hisoblash", "Calculating on the abacus", "Считаем на абакусе"), "abacus_set2", "abacus_set",
         lv({"rods": 3, "expr": 20}, {"rods": 3, "expr": 50}, {"rods": 3, "expr": 80})),
    ]),
    (f"{CH[1]}. Zanjir va flesh", [
        ("chain2d", "🔗", ("Ikki xonali sonlar zanjiri", "Two-digit chains", "Цепочки двузначных чисел"), "chain", "chain",
         lv({"n": 2, "digits": 2}, {"n": 3, "digits": 2}, {"n": 3, "digits": 2, "mode": "input"})),
        ("flash1d", "⚡", ("Flesh-anzan: tezroq", "Flash cards: faster", "Флеш-анзан: быстрее"), "flash", "flash",
         lv({"n": 4, "rule": "ten", "ms": 1300}, {"n": 5, "rule": "ten", "ms": 1100}, {"n": 6, "rule": "ten", "ms": 1000})),
    ]),
    (f"{CH[2]}. Tez ko‘paytirish", [
        ("table", "✖️", ("Karra jadvali va 10 ga ko‘paytirish", "Times tables and ×10", "Таблица умножения и ×10"), "table", "tricks",
         lv({"kinds": ["table", "x10"], "mode": "choice"}, {"kinds": ["table", "x10"]}, {"kinds": ["table", "x10", "x9"], "mode": "input"})),
        ("x5", "🖐️", ("5 ga ko‘paytirish va bo‘lish", "Multiplying and dividing by 5", "Умножение и деление на 5"), "x5", "tricks",
         lv({"kinds": ["x5", "x10"]}, {"kinds": ["x5", "div5"]}, {"kinds": ["x5", "div5", "x4"], "mode": "input"})),
    ]),
    (f"{CH[3]}. Ikki xonali flesh", [
        ("x9", "🎯", ("9, 4 va 8 ga ko‘paytirish", "Multiplying by 9, 4 and 8", "Умножение на 9, 4 и 8"), "x9", "tricks",
         lv({"kinds": ["x9", "x4"]}, {"kinds": ["x9", "x4", "x8"]}, {"kinds": ["x9", "x4", "x8", "plus9"], "mode": "input"})),
        ("flash2d", "⚡", ("Flesh-anzan: ikki xonali", "Flash cards: two-digit", "Флеш-анзан: двузначные"), "flash", "flash",
         lv({"n": 2, "digits": 2, "ms": 2000}, {"n": 3, "digits": 2, "ms": 1800}, {"n": 3, "digits": 2, "ms": 1500})),
    ]),
])

# ------------------------------------------------------------------ 4-sinf
grade(4, [
    (f"{CH[0]}. Katta sonlar", [
        ("abacus4", "🧮", ("To‘rt xonali son abakusda", "Four-digit numbers", "Четырёхзначные числа"), "abacus_read2", "abacus_read",
         lv({"rods": 4, "options": 3}, {"rods": 4, "options": 4}, {"rods": 4, "options": 4, "mode": "input"})),
        ("chain2d", "🔗", ("Ikki xonali zanjir", "Two-digit chains", "Цепочки двузначных"), "chain", "chain",
         lv({"n": 3, "digits": 2}, {"n": 4, "digits": 2}, {"n": 5, "digits": 2, "mode": "input"})),
    ]),
    (f"{CH[1]}. 11 va 25 ga ko‘paytirish", [
        ("x11", "🎯", ("11 ga ko‘paytirish", "Multiplying by 11", "Умножение на 11"), "x11", "tricks",
         lv({"kinds": ["x11"]}, {"kinds": ["x11", "x11c"]}, {"kinds": ["x11c"], "mode": "input"})),
        ("x25", "💯", ("25 ga ko‘paytirish, 99 bilan hisob", "×25 and ±99", "×25 и ±99"), "x25", "tricks",
         lv({"kinds": ["x25", "plus99"]}, {"kinds": ["x25", "plus99", "minus99"]}, {"kinds": ["x25", "plus99", "minus99", "x8"], "mode": "input"})),
    ]),
    (f"{CH[2]}. Xayolan ko‘paytirish", [
        ("split", "✖️", ("Xonalarga ajratib ko‘paytirish", "Splitting to multiply", "Умножение по разрядам"), "split", "tricks",
         lv({"kinds": ["x2d1d", "double"]}, {"kinds": ["x2d1d", "half", "double"]}, {"kinds": ["x2d1d", "x3d1d"], "mode": "input"})),
        ("flash2d", "⚡", ("Flesh-anzan: ikki xonali", "Flash cards: two-digit", "Флеш-анзан: двузначные"), "flash", "flash",
         lv({"n": 3, "digits": 2, "ms": 1600}, {"n": 4, "digits": 2, "ms": 1400}, {"n": 5, "digits": 2, "ms": 1200})),
    ]),
    (f"{CH[3]}. Tezlik", [
        ("chain3d", "🔗", ("Uch xonali zanjir", "Three-digit chains", "Цепочки трёхзначных"), "chain", "chain",
         lv({"n": 2, "digits": 3}, {"n": 3, "digits": 3}, {"n": 3, "digits": 3, "mode": "input"})),
        ("flash_fast", "🚀", ("Flesh-anzan: tezkor", "Flash cards: speed", "Флеш-анзан: скорость"), "flash", "flash",
         lv({"n": 6, "rule": "ten", "ms": 900}, {"n": 7, "rule": "ten", "ms": 800}, {"n": 8, "rule": "ten", "ms": 700})),
    ]),
])

# ------------------------------------------------------------------ 5-sinf
grade(5, [
    (f"{CH[0]}. Takrorlash", [
        ("review", "🎯", ("Tez usullar: takrorlash", "Quick methods: review", "Быстрые приёмы: повторение"), "x11", "tricks",
         lv({"kinds": ["x11c", "x25", "x2d1d"]}, {"kinds": ["x11c", "x25", "x2d1d", "x9"]}, {"kinds": ["x11c", "x25", "x3d1d", "x8"], "mode": "input"})),
        ("chain3d", "🔗", ("Uch xonali zanjir", "Three-digit chains", "Цепочки трёхзначных"), "chain", "chain",
         lv({"n": 3, "digits": 3}, {"n": 4, "digits": 3}, {"n": 4, "digits": 3, "mode": "input"})),
    ]),
    (f"{CH[1]}. Kvadratlar va 99", [
        ("sq5", "⭐", ("5 bilan tugaydigan son kvadrati", "Squares ending in 5", "Квадраты чисел на 5"), "sq5", "tricks",
         lv({"kinds": ["sq5", "x5"]}, {"kinds": ["sq5", "x25"]}, {"kinds": ["sq5", "x25", "x11c"], "mode": "input"})),
        ("x99", "💯", ("99, 15 va 11–19 ga ko‘paytirish", "×99, ×15, ×11–19", "×99, ×15, ×11–19"), "x99", "tricks",
         lv({"kinds": ["x99", "x15"]}, {"kinds": ["x99", "x15", "x2d2d"]}, {"kinds": ["x99", "x15", "x2d2d"], "mode": "input"})),
    ]),
    (f"{CH[2]}. Foizlar", [
        ("percent", "💯", ("Foizlarni xayolan topish", "Percentages in your head", "Проценты в уме"), "percent", "tricks",
         lv({"kinds": ["pct_easy"]}, {"kinds": ["pct_easy", "pct"]}, {"kinds": ["pct"], "mode": "input"})),
        ("split3", "✖️", ("Uch xonali sonni ko‘paytirish", "Multiplying three-digit numbers", "Умножение трёхзначных"), "split", "tricks",
         lv({"kinds": ["x3d1d"]}, {"kinds": ["x3d1d", "x2d2d"]}, {"kinds": ["x3d1d", "x2d2d"], "mode": "input"})),
    ]),
    (f"{CH[3]}. Flesh-anzan", [
        ("flash2d", "⚡", ("Flesh-anzan: ikki xonali tez", "Flash cards: two-digit fast", "Флеш-анзан: двузначные быстро"), "flash", "flash",
         lv({"n": 4, "digits": 2, "ms": 1300}, {"n": 5, "digits": 2, "ms": 1100}, {"n": 6, "digits": 2, "ms": 1000})),
        ("flash3d", "🚀", ("Flesh-anzan: uch xonali", "Flash cards: three-digit", "Флеш-анзан: трёхзначные"), "flash", "flash",
         lv({"n": 2, "digits": 3, "ms": 2200}, {"n": 3, "digits": 3, "ms": 1900}, {"n": 3, "digits": 3, "ms": 1600})),
    ]),
])

# ------------------------------------------------------------------ 6-sinf
grade(6, [
    (f"{CH[0]}. Qulay ko‘paytirish", [
        ("diffsq", "🎯", ("Yaxlit son atrofida", "Around a round number", "Вокруг круглого числа"), "diffsq", "tricks",
         lv({"kinds": ["diffsq", "sq5"]}, {"kinds": ["diffsq", "sq5", "x99"]}, {"kinds": ["diffsq", "x99", "x15"], "mode": "input"})),
        ("near100", "💯", ("100 ga yaqin sonlar", "Numbers near 100", "Числа около 100"), "near100", "tricks",
         lv({"kinds": ["near100", "x99"]}, {"kinds": ["near100", "diffsq"]}, {"kinds": ["near100", "diffsq", "x2d2d"], "mode": "input"})),
    ]),
    (f"{CH[1]}. Bo‘linish va foizlar", [
        ("divisible", "➗", ("Bo‘linish belgilari", "Divisibility rules", "Признаки делимости"), "divisible", "tricks",
         lv({"kinds": ["divisible"]}, {"kinds": ["divisible", "div5"]}, {"kinds": ["divisible", "half", "div5"]})),
        ("x125", "💯", ("125 ga ko‘paytirish va foizlar", "×125 and percentages", "×125 и проценты"), "x125", "tricks",
         lv({"kinds": ["x125", "x25", "pct"]}, {"kinds": ["x125", "pct_hard", "pct"]}, {"kinds": ["x125", "pct_hard"], "mode": "input"})),
    ]),
    (f"{CH[2]}. Darajalar va manfiy sonlar", [
        ("pow2", "🚀", ("2 ning darajalari", "Powers of 2", "Степени двойки"), "pow2", "tricks",
         lv({"kinds": ["pow2", "double"]}, {"kinds": ["pow2", "double", "half"]}, {"kinds": ["pow2", "x8", "x125"], "mode": "input"})),
        ("neg", "➖", ("Manfiy sonlar zanjiri", "Chains with negatives", "Цепочки с отрицательными"), "neg", "chain",
         lv({"n": 3, "digits": 1, "neg": True}, {"n": 4, "digits": 2, "neg": True}, {"n": 5, "digits": 2, "neg": True})),
    ]),
    (f"{CH[3]}. Flesh-anzan", [
        ("flash3d", "⚡", ("Flesh-anzan: uch xonali", "Flash cards: three-digit", "Флеш-анзан: трёхзначные"), "flash", "flash",
         lv({"n": 3, "digits": 3, "ms": 1700}, {"n": 4, "digits": 3, "ms": 1500}, {"n": 4, "digits": 3, "ms": 1300})),
        ("flash_neg", "🧠", ("Flesh-anzan: manfiy natija", "Flash cards: negatives", "Флеш-анзан: отрицательные"), "flash", "flash",
         lv({"n": 5, "digits": 1, "neg": True, "ms": 1200}, {"n": 6, "digits": 1, "neg": True, "ms": 1000},
            {"n": 4, "digits": 2, "neg": True, "ms": 1300})),
    ]),
])

# ------------------------------------------------------------------ 7-sinf
grade(7, [
    (f"{CH[0]}. Kvadratlar", [
        ("sq50", "⭐", ("50 ga yaqin son kvadrati", "Squares near 50", "Квадраты около 50"), "sq50", "tricks",
         lv({"kinds": ["sq50", "sq5"]}, {"kinds": ["sq50", "sq5", "diffsq"]}, {"kinds": ["sq50", "diffsq", "near100"], "mode": "input"})),
        ("mult2d", "✖️", ("Ikki xonali sonlarni ko‘paytirish", "Two-digit multiplication", "Умножение двузначных"), "x99", "tricks",
         lv({"kinds": ["x2d2d", "x11c"]}, {"kinds": ["x2d2d", "x15", "x99"]}, {"kinds": ["x2d2d", "near100", "diffsq"], "mode": "input"})),
    ]),
    (f"{CH[1]}. Ildiz va yig‘indilar", [
        ("sqrt", "🔍", ("Kvadrat ildiz", "Square roots", "Квадратный корень"), "sqrt", "tricks",
         lv({"kinds": ["sqrt", "sq5"]}, {"kinds": ["sqrt", "sq50"]}, {"kinds": ["sqrt", "sq50", "pow2"], "mode": "input"})),
        ("gauss", "🧠", ("Gauss usuli", "Gauss’s method", "Метод Гаусса"), "gauss", "tricks",
         lv({"kinds": ["gauss", "x25"]}, {"kinds": ["gauss", "x125"]}, {"kinds": ["gauss", "x125", "divisible"]})),
    ]),
    (f"{CH[2]}. Istalgan kvadrat va foizlar", [
        ("sq2d", "⭐", ("Ikki xonali son kvadrati va kub", "Squares and cubes", "Квадраты и кубы"), "sq2d", "tricks",
         lv({"kinds": ["sq2d", "sq5"]}, {"kinds": ["sq2d", "cube"]}, {"kinds": ["sq2d", "cube", "sq50"], "mode": "input"})),
        ("percent7", "💯", ("Foizlar: murakkabroq", "Harder percentages", "Проценты посложнее"), "percent_hard", "tricks",
         lv({"kinds": ["pct", "pct_hard"]}, {"kinds": ["pct_hard"]}, {"kinds": ["pct_hard", "x125"], "mode": "input"})),
    ]),
    (f"{CH[3]}. Flesh-anzan", [
        ("flash3d", "🚀", ("Flesh-anzan: uch xonali tez", "Flash cards: three-digit fast", "Флеш-анзан: трёхзначные быстро"), "flash", "flash",
         lv({"n": 4, "digits": 3, "ms": 1400}, {"n": 5, "digits": 3, "ms": 1200}, {"n": 5, "digits": 3, "ms": 1000})),
        ("neg3", "➖", ("Manfiy sonlar: katta zanjir", "Long chains with negatives", "Длинные цепочки с отрицательными"), "neg", "chain",
         lv({"n": 4, "digits": 2, "neg": True}, {"n": 5, "digits": 2, "neg": True}, {"n": 4, "digits": 3, "neg": True})),
    ]),
])

# ------------------------------------------------------------------ 8-sinf
grade(8, [
    (f"{CH[0]}. Ko‘paytirish usullari", [
        ("squares", "⭐", ("Kvadratlar: barcha usullar", "Squares: all methods", "Квадраты: все приёмы"), "sq2d", "tricks",
         lv({"kinds": ["sq2d", "sq50", "sq5"]}, {"kinds": ["sq2d", "sq50", "diffsq"]}, {"kinds": ["sq2d", "near100", "diffsq", "cube"], "mode": "input"})),
        ("mult", "✖️", ("Tez ko‘paytirish", "Fast multiplication", "Быстрое умножение"), "x99", "tricks",
         lv({"kinds": ["x2d2d", "x99", "x125"]}, {"kinds": ["x2d2d", "x99", "x125", "near100"]}, {"kinds": ["x3d1d", "x2d2d", "near100", "x11c"], "mode": "input"})),
    ]),
    (f"{CH[1]}. Foizlar va qismlar", [
        ("pct_change", "💯", ("Foizga oshirish va kamaytirish", "Percentage increase and decrease", "Увеличение и уменьшение на процент"),
         "pct_change", "tricks",
         lv({"kinds": ["pct_up", "pct_down"]}, {"kinds": ["pct_up", "pct_down", "frac_of"]}, {"kinds": ["pct_up", "pct_down", "frac_of", "pct_hard"], "mode": "input"})),
        ("frac", "🍕", ("Sonning qismi va foizi", "Fractions and percentages of a number", "Доля и процент числа"), "percent_hard", "tricks",
         lv({"kinds": ["frac_of", "pct"]}, {"kinds": ["frac_of", "pct_hard"]}, {"kinds": ["frac_of", "pct_hard", "pct_up"], "mode": "input"})),
    ]),
    (f"{CH[2]}. Darajalar va ildizlar", [
        ("powers", "🚀", ("Darajalar va kublar", "Powers and cubes", "Степени и кубы"), "pow2", "tricks",
         lv({"kinds": ["pow2", "cube"]}, {"kinds": ["pow2", "cube", "sq2d"]}, {"kinds": ["pow2", "cube", "sqrt"], "mode": "input"})),
        ("roots", "🔍", ("Ildizlar va bo‘linish", "Roots and divisibility", "Корни и делимость"), "sqrt", "tricks",
         lv({"kinds": ["sqrt", "divisible"]}, {"kinds": ["sqrt", "divisible", "gauss"]}, {"kinds": ["sqrt", "gauss", "divisible"]})),
    ]),
    (f"{CH[3]}. Flesh-anzan", [
        ("flash_neg", "🧠", ("Flesh-anzan: manfiy sonlar", "Flash cards: negatives", "Флеш-анзан: отрицательные"), "flash", "flash",
         lv({"n": 4, "digits": 2, "neg": True, "ms": 1300}, {"n": 5, "digits": 2, "neg": True, "ms": 1100},
            {"n": 6, "digits": 2, "neg": True, "ms": 1000})),
        ("flash3d", "🚀", ("Flesh-anzan: uch xonali", "Flash cards: three-digit", "Флеш-анзан: трёхзначные"), "flash", "flash",
         lv({"n": 5, "digits": 3, "ms": 1200}, {"n": 5, "digits": 3, "ms": 1000}, {"n": 6, "digits": 3, "ms": 900})),
    ]),
])
