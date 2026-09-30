"""Mantiq: 1–8-sinf dasturlari.

Generatorlar: lib/learning/generators/school/logic_school.dart (maktab mantiqi),
lib/learning/generators/logic_senior.dart (rasmli mantiq), school_practice.dart (qonuniyat, tartib, to'plamlar).
3 va 5-sinfdagi eski mavzu kalitlari (sequence, ordering, sets, matrix2/3, coding, sudoku) saqlangan — bolaning
natijalari yo'qolmaydi. Ishga tushirish: python3 tool/content/school/logic_curricula.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import Course, L, Q, TF, MATCH  # noqa: E402

TITLE = L("Mantiq", "Logic", "Логика")

TH = {
    "picture": (
        "Naqsh — takrorlanib turadigan tartib. Avval qaysi rasmlar navbat bilan kelayotganini toping:\n"
        "• 🍎🍌🍎🍌 — ikki rasm navbatma-navbat (AB);\n"
        "• 🔴🔴🔵🔴🔴🔵 — ikki qizil, bir ko‘k (AAB).\n"
        "Tartibni topgach, keyingi rasmni ayting."
    ),
    "odd": (
        "Ortiqchasini topish: hamma narsalarda umumiy belgini qidiring — rang, shakl, o‘lcham yoki guruh.\n"
        "Bitta narsada shu belgi bo‘lmasa — u ortiqcha.\n"
        "Misol: olma, nok, banan, sabzi — sabzi meva emas."
    ),
    "classify": (
        "Guruhlash — narsalarni umumiy belgisi bo‘yicha ajratish: mevalar va sabzavotlar, hayvonlar va qushlar.\n"
        "Har bir narsani olib, “u qaysi guruhga kiradi?” deb so‘rang.\n"
        "Bitta narsa faqat bitta guruhga tushadi."
    ),
    "analogy": (
        "O‘xshatish (analogiya): birinchi juftlikdagi bog‘lanishni toping va ikkinchisiga qo‘llang.\n"
        "Misol: mushuk — sut, quyon — ? . Mushuk sut ichadi, quyon sabzi yeydi → sabzi.\n"
        "Avval juftlikdagi bog‘lanishni so‘z bilan ayting."
    ),
    "maze": (
        "Labirintdan chiqish: yo‘lni oxiridan boshlab ham izlash mumkin.\n"
        "• Devorlardan o‘tib bo‘lmaydi.\n"
        "• Berk ko‘chaga kirsangiz, oxirgi burilishga qayting.\n"
        "Barmog‘ingiz bilan yo‘lni chizib, maqsadga yetib boring."
    ),
    "grid": (
        "Joylashuv: chap — o‘ng, yuqori — past, oldin — keyin.\n"
        "Tartib son: birinchi, ikkinchi, uchinchi …\n"
        "Katakli maydonda avval qatorni, keyin ustunni toping."
    ),
    "sudoku": (
        "Sudoku: har bir qatorda va har bir ustunda har bir belgi faqat bir martadan uchraydi.\n"
        "Bo‘sh katak uchun: shu qator va ustunda qaysi belgilar bor — ularni chiqarib tashlang.\n"
        "Qolgan yagona belgi — javob."
    ),
    "numbers": (
        "Sonli qator: har bir son oldingisidan qanday hosil bo‘lganini toping.\n"
        "Misol: 2, 4, 6, 8 — har safar 2 qo‘shiladi, keyingisi 10.\n"
        "Kamayib borsa — ayirilmoqda: 20, 17, 14 → 11."
    ),
    "sequence": (
        "Ketma-ketlikda sonlar qanday o‘zgarayotganini aniqlang: bir xil son qo‘shilyaptimi yoki bir xil songa ko‘paytirilyaptimi?\n"
        "Qoidani har bir qo‘shni juftlikka qo‘llab tekshiring.\n"
        "Misol: 3, 6, 12, 24 — har safar 2 ga ko‘paytiriladi."
    ),
    "pattern": (
        "Shakllar qatori: har qadamda shakl nimasi bilan o‘zgaradi — rangi, soni yoki burilishi?\n"
        "Bitta belgini kuzating, keyin ikkinchisini.\n"
        "O‘zgarish qoidasini topgach, keyingi shaklni tanlang."
    ),
    "matrix": (
        "Matritsa: satr va ustunlarda shakl, rang yoki miqdor qanday o‘zgarayotganini tekshiring.\n"
        "Yetishmagan katak ham shu qoidaga mos kelishi kerak.\n"
        "Avval satr bo‘yicha, keyin ustun bo‘yicha solishtiring."
    ),
    "rotation": (
        "Aylantirish: shakl burilganda uning qismlari joyi o‘zgaradi, lekin shaklning o‘zi o‘zgarmaydi.\n"
        "Bitta belgili qismni (nuqta, burchak) kuzating — u qayerga ketdi?\n"
        "Chorak burilish — soat mili bo‘yicha 3 dan 6 ga o‘tganday."
    ),
    "problems": (
        "Mantiqiy masala: shartdagi har bir gapni alohida yozib oling.\n"
        "• “Ali Validan baland, Vali Zarinadan baland” → Ali > Vali > Zarina.\n"
        "• “Ustida ham emas, ostida ham emas” → qolgan joy — yonida.\n"
        "Xulosani faqat berilgan ma’lumotdan chiqaring."
    ),
    "emoji": (
        "Rasmli tenglama: bir xil rasm — bir xil son.\n"
        "Avval bitta rasm qatnashgan qatorni yeching: 🍎 + 🍎 = 8 → 🍎 = 4.\n"
        "Keyin topilgan sonni keyingi qatorga qo‘ying: 🍎 + 🍌 = 10 → 🍌 = 6."
    ),
    "calendar": (
        "Hafta kunlari har 7 kunda takrorlanadi: dushanba, seshanba, chorshanba, payshanba, juma, shanba, yakshanba.\n"
        "Misol: bugun dushanba, 10 kundan keyin: 10 = 7 + 3 → payshanba.\n"
        "Vaqt: 1 soat = 60 minut. 8:40 + 30 minut = 9:10."
    ),
    "ordering": (
        "Taqqoslashdan xulosa: A B dan baland, B esa C dan baland bo‘lsa, tartib A → B → C bo‘ladi.\n"
        "Demak A eng baland, C eng past.\n"
        "Chiziq chizib, har bir odamni o‘z joyiga qo‘yib chiqing."
    ),
    "think": (
        "O‘ylangan sonni topish: amallarni oxiridan boshlab teskarisiga bajaramiz.\n"
        "• Qo‘shilgan bo‘lsa — ayiramiz, ayirilgan bo‘lsa — qo‘shamiz.\n"
        "• Ko‘paytirilgan bo‘lsa — bo‘lamiz, bo‘lingan bo‘lsa — ko‘paytiramiz.\n"
        "Misol: +7, keyin × 3 → 45. Teskari: 45 : 3 = 15, 15 − 7 = 8."
    ),
    "table": (
        "“Kim nima?” masalasi: jadval chizing — qatorlarga odamlar, ustunlarga narsalar.\n"
        "• “Alining iti yo‘q” → Ali va it kesishgan katakka ✗.\n"
        "• Qatorda bitta bo‘sh katak qolsa — o‘sha javob (✓), uning ustunidagi boshqa kataklar ✗.\n"
        "Har kimda faqat bitta narsa, har bir narsa faqat bitta odamda."
    ),
    "magic": (
        "Sehrli kvadrat: har bir qator, ustun va ikkala diagonal yig‘indisi bir xil.\n"
        "• Avval to‘liq qator yoki ustun yig‘indisini toping.\n"
        "• “?” turgan qatordagi ma’lum sonlarni shu yig‘indidan ayiring.\n"
        "Misol: yig‘indi 15, qatorda 4 va 3 → ? = 15 − 4 − 3 = 8."
    ),
    "knights": (
        "Rostgo‘ylar har doim rost, yolg‘onchilar har doim yolg‘on gapiradi.\n"
        "Usul: birinchi odamni rostgo‘y deb faraz qiling va uning gapidan kelib chiqib, qolganlarini tekshiring.\n"
        "Qarama-qarshilik chiqsa — faraz noto‘g‘ri, u yolg‘onchi.\n"
        "Misol: A: «Ikkalamiz ham yolg‘onchimiz». Rostgo‘y bunday demaydi → A yolg‘onchi, demak B rostgo‘y."
    ),
    "pigeonhole": (
        "Dirixle prinsipi: 3 ta quyonni 2 ta katakka joylasak, qaysidir katakda kamida 2 ta quyon bo‘ladi.\n"
        "“Albatta” degan savolda eng omadsiz holatni tasavvur qiling.\n"
        "Misol: 2 rangdagi paypoqlardan albatta bir juft chiqishi uchun 3 ta olish yetarli: 2 + 1."
    ),
    "combin": (
        "Kombinatorika — variantlarni sanash.\n"
        "• Ko‘paytirish qoidasi: 3 ta ko‘ylak va 4 ta shim → 3 × 4 = 12 xil kiyinish.\n"
        "• Qo‘l berishish: har kim qolganlar bilan bir marta — n × (n − 1) : 2.\n"
        "Variantlarni tartib bilan yozib chiqsangiz, birortasi ham tushib qolmaydi."
    ),
    "sets": (
        "Ikki guruhdagi odamlarni qo‘shganda ikkala guruhga kiradiganlar ikki marta sanaladi.\n"
        "Umumiy son = birinchi guruh + ikkinchi guruh − ikkala guruhdagilar.\n"
        "Misol: 8 + 7 − 3 = 12. Doiralar (Eyler–Venn diagrammasi) chizish yordam beradi."
    ),
    "coding": (
        "Buyruqlarni qahramon turgan katakdan boshlab bajaring. Har bir o‘q bitta katakka yurishni bildiradi.\n"
        "Chegaradan yoki to‘siqdan o‘tmasdan maqsadga olib boradigan yo‘lni tanlang.\n"
        "Buyruqlarni bittadan bajarib, barmog‘ingiz bilan kuzatib boring."
    ),
    "ages": (
        "Yosh masalalari: yillar o‘tgan sari hammaning yoshi bir xil ortadi, shuning uchun yoshlar farqi o‘zgarmaydi.\n"
        "Misol: aka 12, uka 7 yoshda — farq 5. Uka 10 yoshga to‘lganda aka 15 yoshda bo‘ladi.\n"
        "“Necha marta katta” savolida farqdan foydalaning."
    ),
    "patterns": (
        "Murakkab qonuniyatlar:\n"
        "• navbatlashuvchi amallar: +5, −2, +5, −2 …;\n"
        "• farqlar o‘sib boradi: +1, +2, +3 …;\n"
        "• har bir son oldingi ikkitasining yig‘indisi: 1, 1, 2, 3, 5, 8 …;\n"
        "• kvadratlar va kublar: 1, 4, 9, 16 … va 1, 8, 27 …"
    ),
    "statements": (
        "Mulohaza — rost yoki yolg‘onligini aniqlash mumkin bo‘lgan darak gap.\n"
        "“7 — tub son” — rost mulohaza; “5 > 9” — yolg‘on mulohaza. Savol va buyruq gaplar mulohaza emas.\n"
        "Inkor — mulohazaga “emas” qo‘shish: rost mulohazaning inkori yolg‘on, yolg‘onining inkori rost.\n"
        "“Hamma”ning inkori — “ba’zilari … emas”, “ba’zi”ning inkori — “hech biri … emas”."
    ),
    "logic_ops": (
        "Mulohazalarni bog‘lovchi mantiqiy amallar:\n"
        "• VA — ikkala mulohaza rost bo‘lsagina rost;\n"
        "• YOKI — kamida bittasi rost bo‘lsa rost;\n"
        "• EMAS — rostni yolg‘onga, yolg‘onni rostga aylantiradi.\n"
        "Misol: “2 juft VA 3 toq” — rost; “2 toq YOKI 3 juft” — yolg‘on."
    ),
    "chance": (
        "Ehtimollik = qulay holatlar soni : barcha holatlar soni.\n"
        "Misol: o‘yin kubigida 6 ta yon bor, juft sonlar — 2, 4, 6 (3 ta). Ehtimol = 3/6 = 1/2.\n"
        "Javobni qisqartirilgan kasr ko‘rinishida yozing."
    ),
}

STATEMENTS = [
    Q("Qaysi gap mulohaza?", "Toshkent — O‘zbekiston poytaxti.", ["Soat necha bo‘ldi?", "Eshikni yoping!", "Qanday chiroyli!"],
      x="Darak gap: uni rost yoki yolg‘on deyish mumkin."),
    TF("“Kvadratning to‘rtta tomoni bor” — rost mulohaza.", True, x="Kvadratning 4 ta teng tomoni bor."),
    TF("“12 soni toq” — rost mulohaza.", False, x="12 juft son, shuning uchun bu mulohaza yolg‘on."),
    TF("“Bugun qaysi dars bor?” — mulohaza.", False, x="Savol gap mulohaza emas: uni rost yoki yolg‘on deb bo‘lmaydi."),
    Q("“Mushuk — qush” mulohazasining inkori qaysi?", "Mushuk qush emas.", ["Mushuk — hayvon.", "Qush — mushuk.", "Mushuk — baliq."],
      x="Inkor — mulohazaga “emas” qo‘shish."),
    Q("Rost mulohazaning inkori qanday bo‘ladi?", "Yolg‘on", ["Rost", "Ba’zan rost", "Mulohaza bo‘lmaydi"]),
    TF("Yolg‘on mulohazaning inkori — rost mulohaza.", True),
    Q("Qaysi mulohaza yolg‘on?", "Uchburchakning to‘rtta burchagi bor.", ["Bir haftada 7 kun bor.", "Yil 12 oydan iborat.", "Kvadratning hamma tomoni teng."],
      x="Uchburchakning 3 ta burchagi bor."),
    TF("“Ba’zi sonlar juft” — rost mulohaza.", True, x="Masalan, 2, 4, 6 juft sonlar."),
    TF("“Hech bir qush ucha olmaydi” — rost mulohaza.", False, x="Ko‘p qushlar ucha oladi, demak mulohaza yolg‘on."),
    Q("Qaysi gap mulohaza emas?", "Kitobni menga ber.", ["Olma — meva.", "3 + 4 = 8.", "Oy — Yerning yo‘ldoshi."],
      x="Buyruq gap rost ham, yolg‘on ham bo‘lmaydi. “3 + 4 = 8” — yolg‘on, lekin baribir mulohaza."),
    Q("“Hamma mushuklar mo‘ylovli” — rost. Momiq — mushuk. Qaysi xulosa to‘g‘ri?", "Momiq mo‘ylovli.",
      ["Momiq mo‘ylovsiz.", "Momiq — it.", "Xulosa chiqarib bo‘lmaydi."]),
    Q("Qaysi mulohaza rost?", "Eng kichik tub son — 2.", ["Eng kichik tub son — 1.", "9 — tub son.", "Hamma tub sonlar toq."], d=2,
      x="2 — yagona juft tub son; 1 tub son hisoblanmaydi."),
    Q("“Hamma o‘quvchilar a’lochi” mulohazasining inkori qaysi?", "Ba’zi o‘quvchilar a’lochi emas.",
      ["Hech bir o‘quvchi a’lochi emas.", "Ba’zi o‘quvchilar a’lochi.", "Hamma o‘quvchilar yomon o‘qiydi."], d=2,
      x="“Hamma”ning inkori — “kamida bittasi … emas”, ya’ni “ba’zilari … emas”."),
    Q("“x + 2 = 5” gapi qachon rost mulohaza bo‘ladi?", "x = 3 bo‘lganda", ["x = 5 bo‘lganda", "x = 7 bo‘lganda", "Hech qachon"], d=2),
    TF("“5 soni 10 dan kichik” mulohazasining inkori: “5 soni 10 dan katta yoki unga teng”.", True, d=2),
    TF("“Ali sinfdagi eng baland bola” mulohazasining inkori: “Ali sinfdagi eng past bola”.", False, d=2,
       x="Inkor: “Ali sinfdagi eng baland bola emas”. Eng baland bo‘lmasa, eng past bo‘lishi shart emas."),
    TF("“3 + 4 = 8” — mulohaza emas, chunki u noto‘g‘ri.", False, d=2,
       x="Yolg‘on bo‘lsa ham, u mulohaza: rost-yolg‘onligini aniqlash mumkin."),
    Q("“Ba’zi mevalar nordon” mulohazasining inkori qaysi?", "Hech bir meva nordon emas.",
      ["Ba’zi mevalar nordon emas.", "Hamma mevalar nordon.", "Mevalar shirin."], d=3,
      x="“Ba’zilari … bor”ning inkori — “hech biri … emas”."),
    Q("“Hamma baliqlar suvda yashaydi” — rost. Delfin suvda yashaydi. Qaysi xulosa to‘g‘ri?",
      "Delfinning baliq ekani bundan kelib chiqmaydi.", ["Delfin — baliq.", "Delfin quruqlikda yashaydi.", "Hamma suv hayvonlari baliq."], d=3,
      x="Suvda yashaydiganlarning hammasi ham baliq emas. Aslida delfin — sutemizuvchi."),
]

LOGIC_OPS = [
    TF("“2 — juft son VA 5 — toq son” — rost.", True, x="Ikkala qismi ham rost."),
    TF("“4 — toq son VA 7 — toq son” — rost.", False, x="Birinchi qismi yolg‘on, VA uchun ikkalasi rost bo‘lishi kerak."),
    TF("“4 — toq son YOKI 7 — toq son” — rost.", True, x="Ikkinchi qismi rost, YOKI uchun bittasi yetarli."),
    TF("“3 > 5 YOKI 2 > 6” — rost.", False, x="Ikkala qismi ham yolg‘on."),
    Q("A — rost, B — yolg‘on. “A VA B” qanday?", "Yolg‘on", ["Rost", "Aniqlab bo‘lmaydi"]),
    Q("A — rost, B — yolg‘on. “A YOKI B” qanday?", "Rost", ["Yolg‘on", "Aniqlab bo‘lmaydi"]),
    Q("A — yolg‘on. “EMAS A” qanday?", "Rost", ["Yolg‘on", "Aniqlab bo‘lmaydi"]),
    Q("A — yolg‘on, B — yolg‘on. “A YOKI B” qanday?", "Yolg‘on", ["Rost", "Aniqlab bo‘lmaydi"]),
    Q("A — rost, B — rost. “A VA B” qanday?", "Rost", ["Yolg‘on", "Aniqlab bo‘lmaydi"]),
    Q("Qaysi holda “A VA B” rost bo‘ladi?", "A rost, B rost", ["A rost, B yolg‘on", "A yolg‘on, B rost", "A yolg‘on, B yolg‘on"]),
    Q("Qaysi holda “A YOKI B” yolg‘on bo‘ladi?", "A yolg‘on, B yolg‘on", ["A rost, B yolg‘on", "A yolg‘on, B rost", "A rost, B rost"]),
    MATCH("Amal va uning ma’nosini juftlang", [("VA", "ikkalasi ham rost"), ("YOKI", "kamida bittasi rost"), ("EMAS", "teskarisi")]),
    Q("x = 4 bo‘lsa, qaysi mulohaza rost?", "x > 3 VA x < 5", ["x > 5 VA x < 10", "x < 3 YOKI x > 6", "x — toq son"], d=2),
    Q("Qaysi son uchun “x juft VA x > 10” rost?", "12", ["8", "11", "15"], d=2),
    Q("Qaysi son uchun “x < 3 YOKI x > 8” yolg‘on?", "5", ["1", "9", "12"], d=2),
    TF("Agar A rost bo‘lsa, “A YOKI B” har doim rost.", True, d=2),
    TF("Agar A yolg‘on bo‘lsa, “A VA B” har doim yolg‘on.", True, d=2),
    TF("Agar A rost bo‘lsa, “A VA B” har doim rost.", False, d=2, x="B yolg‘on bo‘lsa, “A VA B” yolg‘on bo‘ladi."),
    Q("Ikki mulohaza uchun rostlik jadvalida nechta qator bo‘ladi?", "4", ["2", "3", "8"], d=2, x="Har biri rost yoki yolg‘on: 2 × 2 = 4 holat."),
    Q("Uch mulohaza uchun rostlik jadvalida nechta qator bo‘ladi?", "8", ["6", "4", "9"], d=3, x="2 × 2 × 2 = 8 holat."),
    Q("“A VA B” yolg‘on ekanini bilsak, qaysi fikr albatta to‘g‘ri?", "Kamida bittasi yolg‘on", ["Ikkalasi ham yolg‘on", "Ikkalasi ham rost", "A rost"], d=3,
      x="VA yolg‘on bo‘lishi uchun bitta yolg‘on qism yetarli."),
    Q("“A YOKI B” rost ekanini bilsak, qaysi fikr albatta to‘g‘ri?", "Kamida bittasi rost", ["Ikkalasi ham rost", "A rost", "B yolg‘on"], d=3),
]


def lv(*levels):
    return [dict(x) for x in levels]


def grade(n, chapters, final_level=3):
    T = Course("logic", n, TITLE, model="QOIDA → MISOL → MASHQ → NAZORAT")
    all_keys = []
    for ci, (chapter, topics) in enumerate(chapters, 1):
        keys = []
        for key, emoji, title, th, gen, levels in topics:
            if gen == "bank":
                T.topic(key, emoji, L(*title), chapter=chapter, theory=TH[th], items=levels)
            else:
                T.topic(key, emoji, L(*title), chapter=chapter, theory=TH[th], gen=gen, levels=levels)
            keys.append(key)
        all_keys += keys
        T.test(f"test{ci}", L(f"{ci}-nazorat ishi", f"Test {ci}", f"Контрольная работа {ci}"), keys, chapter=chapter)
    T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"), all_keys,
           chapter=chapters[-1][0], level=final_level)
    T.write()


CH = ["1-chorak", "2-chorak", "3-chorak", "4-chorak"]

PICTURE = lv({"patterns": ["ABC", "AAB"], "kinds": ["emoji", "shape"], "shown": 5},
             {"patterns": ["AABB", "ABB", "ABC"], "kinds": ["emoji", "shape", "color"], "shown": 6, "growth": True},
             {"patterns": ["AABB", "ABBC", "ABCB"], "kinds": ["shape", "color"], "shown": 6, "growth": True})
NUMBERS = lv({"steps": ["1", "2"], "max": 20, "length": 4},
             {"steps": ["2", "3", "-1", "-2"], "max": 30, "length": 4, "missingInside": True},
             {"steps": ["3", "4", "5", "-3", "10"], "max": 60, "length": 4, "missingInside": True})
MATRIX2 = lv({"size": 2, "drag": True}, {"size": 2}, {"size": 2, "rules": ["shape_color", "count"]})
MATRIX3 = lv({"size": 3, "rules": ["shape_color", "count"]}, {"size": 3, "rules": ["count", "shape_color"]},
             {"size": 3, "rules": ["count", "shape_color"]})
CODING3 = lv({"rows": 3, "cols": 3, "minSteps": 2, "maxSteps": 3}, {"rows": 4, "cols": 4, "obstacles": 2, "minSteps": 3, "maxSteps": 5},
             {"rows": 4, "cols": 4, "obstacles": 3, "minSteps": 3, "maxSteps": 6, "build": True})
CODING5 = lv({"rows": 4, "cols": 4, "obstacles": 2, "minSteps": 3, "maxSteps": 5},
             {"rows": 4, "cols": 4, "obstacles": 3, "minSteps": 3, "maxSteps": 6, "build": True},
             {"rows": 4, "cols": 4, "obstacles": 3, "minSteps": 3, "maxSteps": 6, "build": True})
SUDOKU3 = lv({"size": 4, "minBlanks": 3, "maxBlanks": 4, "symbols": ["emoji"]},
             {"size": 4, "minBlanks": 5, "maxBlanks": 7, "symbols": ["emoji", "colors"]},
             {"size": 4, "minBlanks": 8, "maxBlanks": 10, "symbols": ["numbers", "emoji"]})
SUDOKU5 = lv({"size": 4, "minBlanks": 5, "maxBlanks": 7, "symbols": ["emoji", "colors"]},
             {"size": 4, "minBlanks": 8, "maxBlanks": 10, "symbols": ["numbers", "emoji"]},
             {"size": 4, "minBlanks": 8, "maxBlanks": 10, "symbols": ["numbers", "emoji"]})


def rule_seq(multiply):
    return lv(*[{"maxStart": 10 + lvl * 10, "maxStep": lvl + 2, "multiply": multiply, "mode": "choice" if lvl == 1 else "mixed"}
                for lvl in (1, 2, 3)])


ORDERING = lv({"options": 2}, {"options": 3}, {"options": 4})

# ------------------------------------------------------------------ 1-sinf
grade(1, [
    (f"{CH[0]}. Naqsh va farq", [
        ("pattern", "🔁", ("Naqshni davom ettir", "Continue the pattern", "Продолжи узор"), "picture", "picture_sequence", PICTURE),
        ("odd", "🔍", ("Ortiqchasini top", "Find the odd one out", "Найди лишнее"), "odd", "odd_attribute",
         lv({"items": 4}, {"items": 4}, {"items": 5})),
    ]),
    (f"{CH[1]}. Guruhlash va o‘xshatish", [
        ("classify", "🧺", ("Guruhlarga ajrat", "Sort into groups", "Разложи по группам"), "classify", "classify",
         lv({"bins": 2, "items": 6}, {"bins": 2, "items": 8}, {"bins": 3, "items": 9})),
        ("analogy", "🔗", ("O‘xshatish", "Analogies", "Аналогии"), "analogy", "analogy6",
         lv({"relations": ["eats", "gives", "goes_with"], "options": 3}, {"relations": ["lives", "uses", "weather"], "options": 4},
            {"relations": ["eats", "gives", "lives", "uses", "weather", "goes_with"], "options": 4})),
    ]),
    (f"{CH[2]}. Yo‘l va joy", [
        ("maze", "🌀", ("Labirint", "Mazes", "Лабиринты"), "maze", "maze6",
         lv({"rows": 5, "cols": 5, "extraOpenings": 1}, {"rows": 6, "cols": 6}, {"rows": 7, "cols": 7})),
        ("grid", "📍", ("Qayerda turibdi?", "Where is it?", "Где находится?"), "grid", "grid_position",
         lv({"modes": ["ordinal"], "items": 5}, {"modes": ["grid"]}, {"modes": ["grid", "ordinal"], "items": 7})),
    ]),
    (f"{CH[3]}. Boshqotirmalar", [
        ("sudoku", "🔢", ("Kichik sudoku", "Mini sudoku", "Мини-судоку"), "sudoku", "sudoku",
         lv({"size": 4, "minBlanks": 2, "maxBlanks": 3, "symbols": ["emoji"]}, {"size": 4, "minBlanks": 3, "maxBlanks": 5, "symbols": ["emoji"]},
            {"size": 4, "minBlanks": 5, "maxBlanks": 7, "symbols": ["emoji", "colors"]})),
        ("numbers", "➕", ("Sonli qator", "Number rows", "Числовые ряды"), "numbers", "number_sequence", NUMBERS),
    ]),
], final_level=2)

# ------------------------------------------------------------------ 2-sinf
grade(2, [
    (f"{CH[0]}. Qonuniyatlar", [
        ("sequence", "🔢", ("Sonli qonuniyatlar", "Number patterns", "Числовые закономерности"), "sequence", "rule_sequence", rule_seq(False)),
        ("pattern", "🔷", ("Shakllar qatori", "Shape patterns", "Ряды фигур"), "pattern", "pattern6",
         lv({"modes": ["attr"]}, {"modes": ["rotate", "attr"]}, {"modes": ["rotate"]})),
    ]),
    (f"{CH[1]}. Shakllar mantiqi", [
        ("matrix2", "🧩", ("Matritsa", "Matrices", "Матрицы"), "matrix", "matrix", MATRIX2),
        ("rotation", "🔄", ("Aylantirish", "Rotation", "Повороты"), "rotation", "rotation",
         lv({"options": 2}, {"options": 3}, {"options": 4})),
    ]),
    (f"{CH[2]}. Mantiqiy masalalar", [
        ("problems", "🤔", ("Mantiqiy masalalar", "Logic problems", "Логические задачи"), "problems", "logic_problem",
         lv({"types": ["where", "taller"]}, {"types": ["taller", "order", "where"]}, {"types": ["order", "syllogism", "taller"]})),
        ("emoji", "🍎", ("Rasmli tenglamalar", "Picture equations", "Уравнения с картинками"), "emoji", "emoji_eq",
         lv({"depth": 1, "mode": "choice"}, {"depth": 1}, {"depth": 2})),
    ]),
    (f"{CH[3]}. Kun, vaqt va sudoku", [
        ("calendar", "📅", ("Hafta kunlari va vaqt", "Days and time", "Дни недели и время"), "calendar", "calendar",
         lv({"kinds": ["weekday", "yesterday"], "days": 7}, {"kinds": ["weekday", "yesterday"], "days": 14},
            {"kinds": ["weekday", "time_add"], "days": 20})),
        ("sudoku", "🔢", ("Sudoku", "Sudoku", "Судоку"), "sudoku", "sudoku", SUDOKU3),
    ]),
])

# ------------------------------------------------------------------ 3-sinf (eski kalitlar saqlangan)
grade(3, [
    (f"{CH[0]}. Qonuniyat va taqqoslash", [
        ("sequence", "🔢", ("Sonli qonuniyatlar", "Number patterns", "Числовые закономерности"), "sequence", "rule_sequence", rule_seq(False)),
        ("ordering", "📏", ("Taqqoslashdan xulosa", "Conclusions from comparisons", "Выводы из сравнений"), "ordering", "ordering", ORDERING),
    ]),
    (f"{CH[1]}. Sonli jumboqlar", [
        ("emoji", "🍎", ("Rasmli tenglamalar", "Picture equations", "Уравнения с картинками"), "emoji", "emoji_eq",
         lv({"depth": 1}, {"depth": 1}, {"depth": 2})),
        ("think", "💭", ("O‘ylangan son", "Guess my number", "Задуманное число"), "think", "number_think",
         lv({"ops": 2, "max": 12, "mode": "choice"}, {"ops": 2, "max": 15}, {"ops": 2, "max": 20, "mode": "input"})),
    ]),
    (f"{CH[2]}. Jadval va kvadrat", [
        ("table", "📋", ("Kim nima? (jadval)", "Who has what?", "Кто что?"), "table", "table_logic",
         lv({"people": 3, "positive": True, "cats": ["pets", "colors"]}, {"people": 3}, {"people": 3})),
        ("magic", "✨", ("Sehrli kvadrat", "Magic squares", "Магические квадраты"), "magic", "magic",
         lv({"sum": True, "mode": "choice"}, {"sum": True}, {"sum": False})),
        ("matrix2", "🧩", ("Matritsa", "Matrices", "Матрицы"), "matrix", "matrix", MATRIX2),
    ]),
    (f"{CH[3]}. Sudoku va kodlash", [
        ("sudoku", "🔢", ("Sudoku", "Sudoku", "Судоку"), "sudoku", "sudoku", SUDOKU3),
        ("coding", "🤖", ("Kodlash", "Coding", "Программирование"), "coding", "coding", CODING3),
    ]),
])

# ------------------------------------------------------------------ 4-sinf
grade(4, [
    (f"{CH[0]}. Qonuniyat va vaqt", [
        ("patterns", "🔢", ("Murakkab qonuniyatlar", "Harder patterns", "Сложные закономерности"), "patterns", "seq",
         lv({"kinds": ["arith", "arith_down"]}, {"kinds": ["arith", "alt", "diff"]}, {"kinds": ["alt", "diff", "geom"], "inside": True})),
        ("calendar", "📅", ("Kalendar va soat", "Calendar and clock", "Календарь и часы"), "calendar", "calendar",
         lv({"kinds": ["weekday", "yesterday"], "days": 30}, {"kinds": ["weekday", "time_add"], "days": 60},
            {"kinds": ["weekday_back", "time_add", "duration"], "days": 60})),
    ]),
    (f"{CH[1]}. Mantiqiy fikrlash", [
        ("knights", "🗣️", ("Rostgo‘y va yolg‘onchi", "Knights and knaves", "Рыцари и лжецы"), "knights", "knights",
         lv({"people": 2}, {"people": 2}, {"people": 2})),
        ("table", "📋", ("Kim nima? (jadval)", "Who has what?", "Кто что?"), "table", "table_logic",
         lv({"people": 3}, {"people": 3}, {"people": 4})),
    ]),
    (f"{CH[2]}. Sonli jumboqlar", [
        ("magic", "✨", ("Sehrli kvadrat", "Magic squares", "Магические квадраты"), "magic", "magic",
         lv({"sum": True}, {"sum": False}, {"sum": False, "blanks": 2})),
        ("emoji", "🍎", ("Rasmli tenglamalar", "Picture equations", "Уравнения с картинками"), "emoji", "emoji_eq",
         lv({"depth": 1}, {"depth": 2}, {"depth": 2})),
    ]),
    (f"{CH[3]}. Hisoblab ko‘rish", [
        ("pigeonhole", "🧦", ("Albatta nechta?", "How many for sure?", "Сколько наверняка?"), "pigeonhole", "pigeonhole",
         lv({"kinds": ["pair_any"]}, {"kinds": ["pair_any", "one_color"]}, {"kinds": ["pair_any", "one_color", "months"]})),
        ("combin", "👕", ("Variantlarni sanash", "Counting options", "Подсчёт вариантов"), "combin", "combin",
         lv({"kinds": ["outfit", "routes"]}, {"kinds": ["outfit", "routes", "handshake"]}, {"kinds": ["handshake", "queue", "routes"], "direct": True})),
    ]),
])

# ------------------------------------------------------------------ 5-sinf (eski kalitlar saqlangan)
grade(5, [
    (f"{CH[0]}. Qonuniyatlar", [
        ("sequence", "🔢", ("Sonli qonuniyatlar", "Number patterns", "Числовые закономерности"), "sequence", "rule_sequence", rule_seq(True)),
        ("patterns", "🔣", ("Murakkab qonuniyatlar", "Harder patterns", "Сложные закономерности"), "patterns", "seq",
         lv({"kinds": ["geom", "alt", "diff"]}, {"kinds": ["alt_op", "fib", "squares"]}, {"kinds": ["alt_op", "fib", "squares", "two"], "inside": True})),
        ("ordering", "📏", ("Taqqoslashdan xulosa", "Conclusions from comparisons", "Выводы из сравнений"), "ordering", "ordering", ORDERING),
    ]),
    (f"{CH[1]}. To‘plam va mantiq", [
        ("sets", "⭕", ("Kesishuvchi guruhlar", "Overlapping groups", "Пересекающиеся группы"), "sets", "set_count",
         lv({"mode": "choice"}, {"mode": "mixed"}, {"mode": "input"})),
        ("knights", "🗣️", ("Rostgo‘y va yolg‘onchi", "Knights and knaves", "Рыцари и лжецы"), "knights", "knights",
         lv({"people": 2}, {"people": 2}, {"people": 3})),
        ("matrix3", "🧩", ("3 × 3 matritsa", "3 × 3 matrices", "Матрицы 3 × 3"), "matrix", "matrix", MATRIX3),
    ]),
    (f"{CH[2]}. Kombinatorika va yoshlar", [
        ("combin", "👕", ("Kombinatorika", "Combinatorics", "Комбинаторика"), "combin", "combin",
         lv({"kinds": ["outfit", "handshake", "routes"], "three": True}, {"kinds": ["tournament", "digits", "queue"]},
            {"kinds": ["tournament", "digits", "queue", "routes"], "direct": True})),
        ("ages", "🎂", ("Yosh masalalari", "Age problems", "Задачи на возраст"), "ages", "ages",
         lv({"kinds": ["simple", "later"]}, {"kinds": ["later", "sum_diff"]}, {"kinds": ["sum_diff", "times_future"]})),
    ]),
    (f"{CH[3]}. Sudoku, kodlash, jadval", [
        ("sudoku", "🔢", ("Sudoku", "Sudoku", "Судоку"), "sudoku", "sudoku", SUDOKU5),
        ("coding", "🤖", ("Kodlash", "Coding", "Программирование"), "coding", "coding", CODING5),
        ("table", "📋", ("Kim nima? (jadval)", "Who has what?", "Кто что?"), "table", "table_logic",
         lv({"people": 3}, {"people": 4}, {"people": 4})),
    ]),
])

# ------------------------------------------------------------------ 6-sinf
grade(6, [
    (f"{CH[0]}. Qonuniyat va kvadrat", [
        ("patterns", "🔣", ("Murakkab qonuniyatlar", "Harder patterns", "Сложные закономерности"), "patterns", "seq",
         lv({"kinds": ["squares", "fib", "alt_op"]}, {"kinds": ["two", "mult_inc", "fib"], "inside": True},
            {"kinds": ["two", "mult_inc", "squares", "tri"], "inside": True})),
        ("magic", "✨", ("Sehrli kvadrat", "Magic squares", "Магические квадраты"), "magic", "magic",
         lv({"sum": False, "scale": 2}, {"sum": False, "scale": 2, "blanks": 2}, {"sum": False, "scale": 3, "shift": 20, "blanks": 2})),
    ]),
    (f"{CH[1]}. Mantiqiy xulosa", [
        ("knights", "🗣️", ("Rostgo‘ylar oroli", "Island of knights", "Остров рыцарей"), "knights", "knights",
         lv({"people": 2}, {"people": 3}, {"people": 3})),
        ("pigeonhole", "🧦", ("Dirixle prinsipi", "Pigeonhole principle", "Принцип Дирихле"), "pigeonhole", "pigeonhole",
         lv({"kinds": ["pair_any", "one_color"]}, {"kinds": ["one_color", "two_color", "months"]}, {"kinds": ["two_color", "three_same", "months"]})),
    ]),
    (f"{CH[2]}. Kombinatorika va yoshlar", [
        ("combin", "🔀", ("Kombinatorika", "Combinatorics", "Комбинаторика"), "combin", "combin",
         lv({"kinds": ["digits", "queue", "choose2"]}, {"kinds": ["digits", "tournament", "routes"], "repeat": True, "twice": True, "direct": True},
            {"kinds": ["digits", "tournament", "choose2", "queue"], "repeat": True, "twice": True})),
        ("ages", "🎂", ("Yosh masalalari", "Age problems", "Задачи на возраст"), "ages", "ages",
         lv({"kinds": ["later", "sum_diff"]}, {"kinds": ["sum_diff", "times_future"]}, {"kinds": ["times_future", "times_past"]})),
    ]),
    (f"{CH[3]}. Sonli jumboqlar", [
        ("think", "💭", ("O‘ylangan son", "Guess my number", "Задуманное число"), "think", "number_think",
         lv({"ops": 2, "max": 30}, {"ops": 3, "max": 30}, {"ops": 3, "max": 40, "mode": "input"})),
        ("emoji", "🍎", ("Rasmli tenglamalar", "Picture equations", "Уравнения с картинками"), "emoji", "emoji_eq",
         lv({"depth": 2}, {"depth": 3}, {"depth": 3, "mode": "input"})),
    ]),
])

# ------------------------------------------------------------------ 7-sinf
grade(7, [
    (f"{CH[0]}. Qonuniyat va mulohaza", [
        ("patterns", "🔣", ("Murakkab qonuniyatlar", "Harder patterns", "Сложные закономерности"), "patterns", "seq",
         lv({"kinds": ["tri", "cubes", "primes"]}, {"kinds": ["tri", "cubes", "primes", "two"], "inside": True},
            {"kinds": ["cubes", "primes", "fib", "mult_inc", "two"], "inside": True})),
        ("statements", "💬", ("Mulohaza va inkor", "Statements and negation", "Высказывания и отрицание"), "statements", "bank", STATEMENTS),
    ]),
    (f"{CH[1]}. Mantiqiy masalalar", [
        ("knights", "🗣️", ("Rostgo‘ylar oroli", "Island of knights", "Остров рыцарей"), "knights", "knights",
         lv({"people": 3}, {"people": 3}, {"people": 3})),
        ("table", "📋", ("Kim nima? (jadval)", "Who has what?", "Кто что?"), "table", "table_logic",
         lv({"people": 4}, {"people": 4}, {"people": 4})),
    ]),
    (f"{CH[2]}. Kombinatorika", [
        ("combin", "🔀", ("Kombinatorika", "Combinatorics", "Комбинаторика"), "combin", "combin",
         lv({"kinds": ["paths", "choose2", "digits"], "repeat": True}, {"kinds": ["paths", "tournament", "queue"], "twice": True},
            {"kinds": ["paths", "tournament", "digits", "routes"], "twice": True, "repeat": True, "direct": True})),
        ("pigeonhole", "🧦", ("Dirixle prinsipi", "Pigeonhole principle", "Принцип Дирихле"), "pigeonhole", "pigeonhole",
         lv({"kinds": ["one_color", "two_color"]}, {"kinds": ["three_same", "months"]}, {"kinds": ["three_same", "months", "two_color"]})),
    ]),
    (f"{CH[3]}. Yosh va vaqt", [
        ("ages", "🎂", ("Yosh masalalari", "Age problems", "Задачи на возраст"), "ages", "ages",
         lv({"kinds": ["sum_diff", "times_future"]}, {"kinds": ["times_future", "times_past"]}, {"kinds": ["times_future", "times_past"], "mode": "input"})),
        ("calendar", "📅", ("Kalendar va vaqt", "Calendar and time", "Календарь и время"), "calendar", "calendar",
         lv({"kinds": ["weekday", "weekday_back"], "days": 100}, {"kinds": ["weekday_back", "duration"], "days": 200},
            {"kinds": ["weekday", "weekday_back", "duration"], "days": 365})),
    ]),
])

# ------------------------------------------------------------------ 8-sinf
grade(8, [
    (f"{CH[0]}. Mantiq algebrasi", [
        ("logic_ops", "💡", ("Mantiqiy amallar: VA, YOKI, EMAS", "Logical operations", "Логические операции"), "logic_ops", "bank", LOGIC_OPS),
        ("knights", "🗣️", ("Rostgo‘ylar oroli", "Island of knights", "Остров рыцарей"), "knights", "knights",
         lv({"people": 3}, {"people": 3}, {"people": 3})),
    ]),
    (f"{CH[1]}. Kombinatorika va ehtimollik", [
        ("combin", "🔀", ("Kombinatorika", "Combinatorics", "Комбинаторика"), "combin", "combin",
         lv({"kinds": ["paths", "queue", "choose2"]}, {"kinds": ["paths", "digits", "tournament"], "repeat": True, "twice": True},
            {"kinds": ["paths", "queue", "digits", "choose2"], "repeat": True})),
        ("chance", "🎲", ("Ehtimollik", "Probability", "Вероятность"), "chance", "combin",
         lv({"kinds": ["chance"]}, {"kinds": ["chance"]}, {"kinds": ["chance"]})),
    ]),
    (f"{CH[2]}. Qonuniyat va kvadrat", [
        ("patterns", "🔣", ("Murakkab qonuniyatlar", "Harder patterns", "Сложные закономерности"), "patterns", "seq",
         lv({"kinds": ["primes", "cubes", "fib"], "inside": True}, {"kinds": ["mult_inc", "tri", "two", "cubes"], "inside": True},
            {"kinds": ["primes", "cubes", "fib", "mult_inc", "two", "tri"], "inside": True, "mode": "input"})),
        ("magic", "✨", ("Sehrli kvadrat", "Magic squares", "Магические квадраты"), "magic", "magic",
         lv({"sum": False, "scale": 3, "shift": 20}, {"sum": False, "scale": 3, "shift": 30, "blanks": 2},
            {"sum": False, "scale": 5, "shift": 50, "blanks": 2, "mode": "input"})),
    ]),
    (f"{CH[3]}. Masalalar", [
        ("ages", "🎂", ("Yosh masalalari", "Age problems", "Задачи на возраст"), "ages", "ages",
         lv({"kinds": ["times_future", "times_past"]}, {"kinds": ["times_future", "times_past", "sum_diff"]},
            {"kinds": ["times_future", "times_past"], "mode": "input"})),
        ("think", "💭", ("O‘ylangan son", "Guess my number", "Задуманное число"), "think", "number_think",
         lv({"ops": 3, "max": 30}, {"ops": 3, "max": 40}, {"ops": 4, "max": 40, "mode": "input"})),
    ]),
])
