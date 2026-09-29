"""Tarix, 5-sinf: tarix fani va manbalar, ibtidoiy davr, Qadimgi Sharq, Yunoniston va Rim, Vatanimizning qadimgi tarixi.

Faqat umumqabul qilingan, darsliklarda keltiriladigan faktlar ishlatilgan; matnlar o‘zimizniki.
Qayta yaratish: python3 tool/content/school/history_g5.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403

rnd = random.Random(505)
T = Course("history", 5, L("Tarix", "History", "История"))

C1 = "1-chorak. Tarix fani va ibtidoiy davr"
C2 = "2-chorak. Qadimgi Sharq"
C3 = "3-chorak. Qadimgi Yunoniston va Rim"
C4 = "4-chorak. Vatanimizning qadimgi tarixi"


def roman(n):
    vals = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


# ============================================================ 1-chorak
items = [
    Q("Tarix fani nimani o‘rganadi?", "Insoniyatning o‘tmishini", ["Faqat hayvonlarni", "Yulduzlarni", "Sonlarni"], x="Tarix — insoniyat o‘tmishi haqidagi fan."),
    Q("Yer ostidan qadimgi buyumlarni qazib o‘rganadigan fan qaysi?", "Arxeologiya", ["Geografiya", "Biologiya", "Matematika"], x="Arxeologlar qazishma o‘tkazadi."),
    Q("Qadimgi qo‘lyozma qanday tarixiy manba?", "Yozma manba", ["Moddiy manba", "Og‘zaki manba", "Manba emas"], x="Unda ma’lumot yozuv orqali yetib kelgan."),
    Q("Qazishmada topilgan sopol ko‘za qanday manba?", "Moddiy manba", ["Yozma manba", "Og‘zaki manba", "Manba emas"], x="Buyumlar, inshootlar, qurollar — moddiy manbalar."),
    Q("Avloddan avlodga og‘zaki aytib kelingan rivoyat qanday manba?", "Og‘zaki manba", ["Yozma manba", "Moddiy manba", "Manba emas"], x="Doston, rivoyat, qo‘shiqlar — og‘zaki manbalar."),
    Q("Tosh mehnat quroli qanday manba?", "Moddiy manba", ["Yozma manba", "Og‘zaki manba", "Manba emas"], x="Qadimgi odamlar yasagan buyum — moddiy manba."),
    Q("Qadimgi tanga qanday manba?", "Moddiy manba", ["Og‘zaki manba", "Yozma manba", "Manba emas"], d=2, x="Tangadagi yozuv ham bor, lekin u asosan buyum sifatida o‘rganiladi."),
    Q("Tarixiy buyumlar saqlanadigan va ko‘rgazmaga qo‘yiladigan joy qanday ataladi?", "Muzey", ["Kutubxona", "Bozor", "Stadion"], x="Muzeyda eksponatlar saqlanadi."),
    Q("“Alpomish” dostoni qanday tarixiy manba hisoblanadi?", "Og‘zaki manba", ["Moddiy manba", "Yozma manba", "Manba emas"], d=2, x="Doston xalq orasida og‘zaki saqlangan."),
    Q("Qoyatoshlarga chizilgan qadimgi rasmlar qanday manba?", "Moddiy manba", ["Yozma manba", "Og‘zaki manba", "Manba emas"], d=2, x="Qoyatosh rasmlari — moddiy manba."),
    TF("Tarixiy manbalar yozma, moddiy va og‘zaki bo‘ladi.", True, x="Bu — manbalarning asosiy turlari."),
    TF("Arxeologlar qazishmalar orqali o‘tmishni o‘rganadi.", True, x="Ular yer ostidagi buyum va inshootlarni topadi."),
    TF("Og‘zaki manba qog‘ozga yozilgan bo‘ladi.", False, x="Og‘zaki manba — og‘izdan og‘izga o‘tgan hikoya, qo‘shiq, doston."),
    MATCH("Manbani turi bilan juftlang", [("qo‘lyozma", "yozma"), ("sopol ko‘za", "moddiy"), ("rivoyat", "og‘zaki")], d=2),
    Q("Tarixchi bitta manbadagi ma’lumotni nima qilishi kerak?", "Boshqa manbalar bilan solishtirishi", ["Tekshirmasdan qabul qilishi", "Yashirib qo‘yishi", "O‘chirib tashlashi"], d=3,
      x="Bir necha manbani solishtirish haqiqatga yaqinlashtiradi."),
]
T.topic("sources", "🏺", L("Tarix fani va tarixiy manbalar", "History and its sources", "История и исторические источники"), C1,
        "Tarix — insoniyat o‘tmishini o‘rganadigan fan. O‘tmish haqidagi bilimlar manbalardan olinadi:\n"
        "• yozma manbalar — qo‘lyozma, yilnoma, xat, kitob;\n"
        "• moddiy manbalar — buyumlar, qurollar, tangalar, inshoot qoldiqlari, qoyatosh rasmlari;\n"
        "• og‘zaki manbalar — rivoyat, doston, qo‘shiq.\n"
        "Arxeologiya yer ostidagi qadimgi buyumlarni qazib o‘rganadi, ular muzeylarda saqlanadi.", items=items)

items = []
for year in (1991, 2024, 1441, 1336, 1483, 1901, 1800, 1200, 500, 100, 2000, 101):
    c = (year - 1) // 100 + 1
    items.append(Q(f"Milodiy {year}-yil nechanchi asrga kiradi?", f"{c}-asr",
                   [f"{k}-asr" for k in (c - 1, c + 1, c + 2) if k > 0], d=1 if year in (1991, 2024, 1441, 1336) else (2 if year not in (1901, 1800, 2000, 101) else 3),
                   x=f"{c}-asr: {(c - 1) * 100 + 1}–{c * 100}-yillar."))
for a, b in [(500, 300), (776, 509), (1000, 100), (2000, 1500)]:
    items.append(Q(f"Qaysi sana qadimiyroq: miloddan avvalgi {a}-yilmi yoki miloddan avvalgi {b}-yilmi?", f"mil. avv. {a}-yil", [f"mil. avv. {b}-yil", "Ikkalasi bir vaqtda"],
                   d=2, x="Miloddan avvalgi sanalarda son qancha katta bo‘lsa, voqea shuncha qadimiy."))
items += [
    Q("Bir asr necha yilga teng?", "100 yil", ["10 yil", "1000 yil", "50 yil"], x="Asr — yuz yil."),
    Q("Ming yillik necha asrga teng?", "10 asr", ["100 asr", "5 asr", "1 asr"], x="1000 yil = 10 × 100 yil."),
    Q("Yillar hisobi qaysi voqeadan boshlab milodiy deb ataladi?", "Milod boshlanishidan", ["Olimpiya o‘yinlaridan", "Piramidalar qurilishidan", "Rim tashkil topishidan"], d=2,
      x="Undan oldingi yillar — miloddan avvalgi (mil. avv.)."),
    TF("Miloddan avvalgi 500-yil miloddan avvalgi 100-yildan oldin bo‘lgan.", True, d=2, x="Miloddan avvalgi sanalar kamayib boradi: 500, 400, … 100."),
    TF("2001-yil 20-asrga kiradi.", False, d=2, x="21-asr 2001-yildan boshlanadi."),
]
T.topic("time", "⏳", L("Vaqt hisobi: yil, asr, ming yillik", "Measuring time: years and centuries", "Счёт времени: год, век"), C1,
        "Asr — 100 yil, ming yillik — 1000 yil. Milodiy yillar milod boshlanishidan sanaladi, undan oldingilar — miloddan avvalgi (mil. avv.).\n"
        "• 1-asr: 1–100-yillar, 20-asr: 1901–2000, 21-asr: 2001–2100.\n"
        "• Asrni topish: yilning yuzliklar sonini olib, 1 qo‘shamiz (1991 → 19 + 1 = 20-asr); 1900, 2000 kabi yillar oldingi asrga kiradi.\n"
        "• Miloddan avvalgi sanada son qancha katta bo‘lsa, voqea shuncha qadimiy.", items=items)

T.topic("centuries", "📅", L("Yil va asr (mashq)", "Years and centuries (practice)", "Год и век (практика)"), C1,
        "Bir asr — yuz yil. Milodiy birinchi asr 1–100-yillar, ikkinchi asr 101–200-yillar. 1901–2000-yillar yigirmanchi asr, "
        "2001–2100-yillar yigirma birinchi asr. Yuzlikning oxirgi yili avvalgi asrga kiradi.",
        gen="timeline", levels=[dict(mode=m) for m in ("choice", "mixed", "input")])

items = [
    Q("Ibtidoiy odamlar dastlab qanday qurollardan foydalanishgan?", "Tosh qurollardan", ["Temir qurollardan", "Plastmassa qurollardan", "Oltin qurollardan"], x="Shuning uchun bu davr tosh davri deyiladi."),
    Q("Ibtidoiy odamlar olovdan nima maqsadda foydalanishgan?", "Isinish, ovqat pishirish, yirtqichlardan saqlanish", ["Faqat o‘yin uchun", "Kitob o‘qish uchun", "Mashina yurgizish uchun"], x="Olov hayotni ancha yengillashtirdi."),
    Q("Ibtidoiy odamlarning dastlabki mashg‘ulotlari qaysilar?", "Ovchilik va termachilik", ["Savdo va sanoat", "Hunarmandchilik va bank ishi", "Dengizchilik"], x="Ular hayvon ovlab, yovvoyi meva va urug‘ terishgan."),
    Q("Keyinchalik qaysi xo‘jalik turlari paydo bo‘ldi?", "Dehqonchilik va chorvachilik", ["Kompyuter sanoati", "Kosmik parvozlar", "Temir yo‘l qurilishi"], d=2, x="Odamlar o‘simlik ekish va hayvon boqishni o‘rgandi."),
    Q("Teshiktosh g‘ori qayerda joylashgan?", "Surxondaryoda, Boysun tog‘larida", ["Toshkent shahri markazida", "Orol dengizi tubida", "Farg‘ona shahrida"], d=2,
      x="Teshiktosh g‘orida qadimgi odam — neandertal bola suyaklari topilgan."),
    Q("Teshiktosh g‘orida nima topilgan?", "Qadimgi odam bolasining suyaklari", ["Oltin toj", "Qadimgi kitob", "Temir qilich"], d=2, x="Bu topilma butun dunyoga mashhur."),
    Q("Qadimgi qoyatosh rasmlari bilan mashhur Sarmishsoy qaysi viloyatda?", "Navoiy viloyatida", ["Andijon viloyatida", "Toshkent viloyatida", "Xorazm viloyatida"], d=3,
      x="Sarmishsoyda minglab qoyatosh rasmlari bor."),
    Q("Zarautsoy qanday yodgorlik bilan mashhur?", "Qoyatosh rasmlari", ["Piramidalar", "Qadimgi masjid", "Qal’a devorlari"], d=3, x="Zarautsoy (Surxondaryo) qoyatosh rasmlarida ov manzaralari tasvirlangan."),
    TF("Tosh davrida odamlar temir qurollardan foydalanishgan.", False, x="Temir ancha keyin o‘zlashtirilgan."),
    TF("Ibtidoiy odamlar jamoa bo‘lib yashashgan.", True, x="Birgalikda ov qilish va yashash osonroq edi."),
    TF("Dehqonchilikning paydo bo‘lishi odamlarni o‘troq hayotga o‘tkazdi.", True, d=2, x="Ekin ekkan odamlar bir joyda qolib yashay boshladi."),
    TF("Olov ibtidoiy odamlarni yirtqich hayvonlardan himoya qilgan.", True, x="Hayvonlar olovdan qo‘rqadi."),
    MATCH("Yodgorlikni topilma bilan juftlang", [("Teshiktosh g‘ori", "qadimgi odam suyaklari"), ("Sarmishsoy", "qoyatosh rasmlari"),
                                               ("Afrosiyob", "qadimgi Samarqand xarobalari")], d=3),
    Q("Qaysi biri ibtidoiy odamlarning uy-joyi bo‘lgan?", "G‘or", ["Ko‘p qavatli uy", "Mehmonxona", "Saroy"], x="Dastlab ular g‘orlarda yashashgan."),
    Q("Odamlar hayvonlarni qo‘lga o‘rgatishi natijasida qaysi xo‘jalik paydo bo‘ldi?", "Chorvachilik", ["Dehqonchilik", "Savdo", "Hunarmandchilik"], d=2, x="Chorvachilik — uy hayvonlarini boqish."),
]
T.topic("stone_age", "🔥", L("Ibtidoiy odamlar hayoti", "Life of early humans", "Жизнь первобытных людей"), C1,
        "Ibtidoiy odamlar tosh qurollar yasagan (tosh davri), g‘orlarda yashagan, ovchilik va termachilik bilan shug‘ullangan.\n"
        "Olov isinish, ovqat pishirish va himoya uchun muhim bo‘lgan. Keyinroq dehqonchilik va chorvachilik paydo bo‘ldi.\n"
        "Vatanimizdagi yodgorliklar: Teshiktosh g‘ori (Surxondaryo, Boysun tog‘lari) — qadimgi odam bolasining suyaklari topilgan;\n"
        "Sarmishsoy (Navoiy) va Zarautsoy (Surxondaryo) — qoyatosh rasmlari.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["sources", "time", "stone_age"], C1)

# ============================================================ 2-chorak
items = [
    Q("Qadimgi Misr qaysi daryo bo‘yida vujudga kelgan?", "Nil", ["Amudaryo", "Dajla", "Xuanxe"], x="Nil daryosi toshqinlari yerni unumdor qilgan."),
    Q("Qadimgi Misr hukmdori qanday atalgan?", "Fir’avn", ["Imperator", "Xon", "Prezident"], x="Fir’avnlar cheksiz hokimiyatga ega bo‘lgan."),
    Q("Misrdagi eng katta piramida qaysi fir’avn uchun qurilgan?", "Xeops", ["Tutanxamon", "Xammurapi", "Sezar"], d=2, x="Xeops piramidasi — eng katta piramida."),
    Q("Qadimgi misrliklar yozuvi qanday nomlanadi?", "Iyeroglif", ["Mixxat", "Lotin yozuvi", "Kirill yozuvi"], x="Iyerogliflar — rasmli belgilar."),
    Q("Misrliklar qaysi o‘simlikdan yozuv materiali tayyorlashgan?", "Papirus", ["Paxta", "Bug‘doy", "Tut"], d=2, x="Papirus qamishidan qog‘ozga o‘xshash material tayyorlangan."),
    Q("Piramidalar nima uchun qurilgan?", "Fir’avnlar maqbarasi sifatida", ["Uy-joy sifatida", "Bozor sifatida", "Maktab sifatida"], x="Piramidalar — fir’avnlarning maqbaralari."),
    TF("Qadimgi Misr Nil daryosi bo‘yida vujudga kelgan.", True, x="Nil — Misr hayotining manbai."),
    TF("Misrliklar mixxatda yozishgan.", False, x="Misrliklar iyerogliflardan foydalangan; mixxat — Mesopotamiyada."),
    Q("Mesopotamiya (Ikki daryo oralig‘i) qaysi daryolar orasida joylashgan?", "Dajla va Frot", ["Nil va Kongo", "Amudaryo va Sirdaryo", "Hind va Gang"], x="Mesopotamiya — “ikki daryo oralig‘i” degani."),
    Q("Mesopotamiyada paydo bo‘lgan yozuv qaysi?", "Mixxat", ["Iyeroglif", "Lotin yozuvi", "Arab yozuvi"], x="Belgilar ho‘l loy taxtachalarga tayoqcha bilan bosilgan."),
    Q("Mixxat nimaga yozilgan?", "Loy taxtachalarga", ["Qog‘ozga", "Ipak matoga", "Shishaga"], d=2, x="Yozilgan taxtachalar quritilgan yoki pishirilgan."),
    Q("Mashhur qadimgi qonunlar to‘plami kimning nomi bilan ataladi?", "Xammurapi", ["Fir’avn", "Sezar", "Aleksandr"], d=2, x="Xammurapi — Bobil podshosi."),
    Q("Xammurapi qaysi davlatning podshosi bo‘lgan?", "Bobil", ["Misr", "Rim", "Xitoy"], d=2, x="Bobil — Mesopotamiyadagi qudratli davlat."),
    MATCH("Qadimgi davlatni belgisi bilan juftlang", [("Misr", "piramidalar"), ("Mesopotamiya", "mixxat"), ("Bobil", "Xammurapi qonunlari")], d=2),
    Q("Qadimgi dehqonlar daryo suvidan qanday foydalanishgan?", "Kanal qazib, dalalarni sug‘organ", ["Suvdan umuman foydalanishmagan", "Faqat baliq tutishgan", "Suvni sotishgan"], d=2,
      x="Sug‘orish dehqonchilik rivojlanishining asosi bo‘lgan."),
]
T.topic("egypt_mesopotamia", "🔺", L("Qadimgi Misr va Mesopotamiya", "Ancient Egypt and Mesopotamia", "Древний Египет и Месопотамия"), C2,
        "• Qadimgi Misr — Nil daryosi bo‘yida. Hukmdori — fir’avn. Piramidalar — fir’avnlar maqbaralari (eng kattasi — Xeops piramidasi).\n"
        "  Yozuvi — iyeroglif, yozuv materiali — papirus.\n"
        "• Mesopotamiya — Dajla va Frot daryolari oralig‘ida. Yozuvi — mixxat (loy taxtachalarga).\n"
        "  Bobil podshosi Xammurapi mashhur qonunlar to‘plamini yaratgan.", items=items)

items = [
    Q("Qadimgi Hindiston qaysi daryolar bo‘yida vujudga kelgan?", "Hind va Gang", ["Nil va Kongo", "Dajla va Frot", "Amudaryo va Sirdaryo"], x="Mamlakat nomi Hind daryosidan olingan."),
    Q("Hozirgi “arab raqamlari” aslida qayerda paydo bo‘lgan?", "Hindistonda", ["Misrda", "Rimda", "Yunonistonda"], d=2, x="Hind raqamlarini arablar Yevropaga yetkazgan."),
    Q("Qadimgi Xitoy qaysi daryolar bo‘yida vujudga kelgan?", "Xuanxe va Yanszi", ["Nil va Frot", "Hind va Gang", "Tibr va Po"], d=2, x="Xuanxe — “Sariq daryo”."),
    Q("Xitoyliklar ko‘chmanchilardan himoyalanish uchun nima qurishgan?", "Buyuk Xitoy devorini", ["Piramidalarni", "Kolizeyni", "Minorani"], x="Buyuk Xitoy devori — dunyodagi eng uzun mudofaa inshooti."),
    Q("Qaysi ixtiro qadimgi Xitoyga tegishli?", "Qog‘oz", ["Telefon", "Samolyot", "Kompyuter"], x="Qog‘oz, ipak, kompas, porox — Xitoy ixtirolari."),
    Q("Xitoyliklar qaysi qurt yordamida mashhur matoni ishlab chiqarishgan?", "Ipak qurti", ["Chuvalchang", "Chumoli", "Asalari"], d=2, x="Ipak Xitoyning mashhur mahsuloti bo‘lgan."),
    Q("Qaysi biri qadimgi Xitoy ixtirosi EMAS?", "Elektr lampochka", ["Qog‘oz", "Kompas", "Porox"], d=2, x="Elektr lampochka XIX asrda ixtiro qilingan."),
    TF("Buyuk Xitoy devori ko‘chmanchilardan himoyalanish uchun qurilgan.", True, x="Devor shimoliy chegara bo‘ylab qurilgan."),
    TF("Qog‘oz qadimgi Rimda ixtiro qilingan.", False, x="Qog‘oz qadimgi Xitoyda ixtiro qilingan."),
    TF("Ipak Xitoydan boshqa mamlakatlarga olib ketilgan qimmatbaho mahsulot bo‘lgan.", True, x="Buyuk ipak yo‘li nomi shundan."),
    MATCH("Mamlakatni ixtiro yoki belgisi bilan juftlang", [("Xitoy", "qog‘oz"), ("Hindiston", "raqamlar"), ("Misr", "papirus"), ("Mesopotamiya", "mixxat")], d=2),
    Q("Xuanxe daryosining boshqa nomi qaysi?", "Sariq daryo", ["Qizil daryo", "Oq daryo", "Moviy daryo"], d=3, x="Suvi sariq loyqa bo‘lgani uchun shunday atalgan."),
    Q("Xitoy imperatorlari qanday unvon bilan atalgan?", "Osmon o‘g‘li", ["Fir’avn", "Konsul", "Xon"], d=3, x="Xitoyda imperator “Osmon o‘g‘li” deb atalgan."),
    Q("Qadimgi Xitoyda qanday qimmatbaho idishlar yasalgan?", "Chinni idishlar", ["Plastik idishlar", "Shisha butilkalar", "Temir bankalar"], d=2, x="Xitoy chinnisi dunyoga mashhur."),
    Q("Qaysi daryo bo‘yida Hindiston tsivilizatsiyasi boshlangan?", "Hind", ["Nil", "Tibr", "Frot"], x="Hind daryosi vodiysida qadimgi shaharlar bo‘lgan."),
]
T.topic("india_china", "🏯", L("Qadimgi Hindiston va Xitoy", "Ancient India and China", "Древняя Индия и Китай"), C2,
        "• Qadimgi Hindiston — Hind va Gang daryolari bo‘yida. Hozirgi raqamlar hind raqamlaridan kelib chiqqan.\n"
        "• Qadimgi Xitoy — Xuanxe (Sariq daryo) va Yanszi bo‘yida. Buyuk Xitoy devori ko‘chmanchilardan himoya uchun qurilgan.\n"
        "• Xitoy ixtirolari: qog‘oz, ipak, chinni, kompas, porox.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["egypt_mesopotamia", "india_china"], C2)

# ============================================================ 3-chorak
items = [
    Q("Birinchi Olimpiya o‘yinlari qachon o‘tkazilgan?", "Miloddan avvalgi 776-yilda", ["Milodiy 1991-yilda", "Miloddan avvalgi 50-yilda", "Milodiy 1500-yilda"], d=2,
      x="Olimpiya o‘yinlari Yunonistonning Olimpiya shahrida o‘tkazilgan."),
    Q("Olimpiya o‘yinlari qaysi mamlakatda paydo bo‘lgan?", "Qadimgi Yunonistonda", ["Qadimgi Misrda", "Qadimgi Xitoyda", "Qadimgi Hindistonda"], x="Olimpiya — Yunonistondagi joy nomi."),
    Q("“Iliada” va “Odisseya” dostonlarining muallifi kim?", "Gomer", ["Sezar", "Xammurapi", "Aristotel"], x="Gomer — qadimgi yunon shoiri."),
    Q("Qaysi yunon shahar-davlatida demokratiya rivojlangan?", "Afina", ["Sparta", "Bobil", "Rim"], d=2, x="Afinada muhim masalalarni fuqarolar yig‘ini hal qilgan."),
    Q("Qaysi yunon shahar-davlati kuchli jangchilar tarbiyasi bilan mashhur?", "Sparta", ["Afina", "Misr", "Bobil"], d=2, x="Spartada bolalar yoshligidan harbiy mashqlarga o‘rgatilgan."),
    Q("Aleksandr Makedonskiyning ustozi kim bo‘lgan?", "Aristotel", ["Gomer", "Sezar", "Xeops"], d=3, x="Aristotel — mashhur yunon faylasufi."),
    Q("Aleksandr Makedonskiyga qarshi kurashgan So‘g‘d sarkardasi kim?", "Spitamen", ["Shiroq", "Alpomish", "Temur"], d=2, x="Spitamen So‘g‘diyonada bosqinchilarga qarshi qo‘zg‘olon ko‘targan."),
    TF("Olimpiya o‘yinlari qadimgi Yunonistonda paydo bo‘lgan.", True, x="Miloddan avvalgi 776-yildan."),
    TF("“Iliada” dostonini Yuliy Sezar yozgan.", False, x="“Iliada” — Gomer asari."),
    Q("Yunonlar xudolari yashaydi deb ishongan tog‘ qaysi?", "Olimp", ["Everest", "Pomir", "Chimyon"], d=2, x="Yunon afsonalarida xudolar Olimp tog‘ida yashagan."),
    Q("“Demokratiya” so‘zining ma’nosi qaysi?", "Xalq hokimiyati", ["Podsho hokimiyati", "Harbiy qo‘shin", "Ibodatxona"], d=2, x="Yunoncha: demos — xalq, kratos — hokimiyat."),
    MATCH("Shaxs yoki joyni belgisi bilan juftlang", [("Gomer", "“Iliada”"), ("Afina", "demokratiya"), ("Sparta", "jangchilar tarbiyasi"),
                                                    ("Olimpiya", "sport o‘yinlari")], d=2),
    Q("Qadimgi Olimpiya o‘yinlarida g‘oliblarga nima kiydirilgan?", "Zaytun novdasidan gulchambar", ["Oltin toj", "Temir dubulg‘a", "Ipak to‘n"], d=3, x="Zaytun gulchambari — g‘alaba ramzi."),
    Q("Aleksandr Makedonskiy qaysi davlatning podshosi bo‘lgan?", "Makedoniya", ["Misr", "Xitoy", "Bobil"], x="U juda katta hududlarni bosib olgan."),
    Q("Yunonlar teatrda qanday asarlarni sahnalashtirgan?", "Tragediya va komediya", ["Faqat operalar", "Faqat filmlar", "Faqat raqslar"], d=2, x="Teatr qadimgi Yunonistonda keng rivojlangan."),
]
T.topic("greece", "🏛️", L("Qadimgi Yunoniston", "Ancient Greece", "Древняя Греция"), C3,
        "• Olimpiya o‘yinlari miloddan avvalgi 776-yilda boshlangan; g‘oliblarga zaytun gulchambari kiydirilgan.\n"
        "• Afina — demokratiya (xalq hokimiyati) vatani; Sparta — kuchli jangchilar tarbiyasi bilan mashhur.\n"
        "• Gomer — “Iliada” va “Odisseya” dostonlari muallifi. Aristotel — faylasuf, Aleksandr Makedonskiyning ustozi.\n"
        "• Aleksandr Makedonskiyga qarshi So‘g‘diyonada Spitamen kurashgan.", items=items)

items = [
    Q("Rim shahri qaysi daryo bo‘yida joylashgan?", "Tibr", ["Nil", "Frot", "Gang"], d=2, x="Rim Italiyada, Tibr daryosi bo‘yida."),
    Q("Rimdagi mashhur ulkan amfiteatr qanday nomlanadi?", "Kolizey", ["Piramida", "Parfenon", "Buyuk devor"], x="Kolizeyda tomoshalar o‘tkazilgan."),
    Q("Rimda arenada bir-biri bilan jang qilgan kishilar kimlar edi?", "Gladiatorlar", ["Fir’avnlar", "Baxshilar", "Olimlar"], x="Gladiatorlar ko‘pincha qullardan bo‘lgan."),
    Q("Qadimgi Rimliklar qaysi tilda so‘zlashgan?", "Lotin tilida", ["Yunon tilida", "Xitoy tilida", "Misr tilida"], x="Lotin tili ko‘plab Yevropa tillariga ta’sir qilgan."),
    Q("Mashhur Rim sarkardasi va davlat arbobi kim?", "Yuliy Sezar", ["Gomer", "Xammurapi", "Konfutsiy"], x="Yuliy Sezar — mashhur Rim sarkardasi."),
    Q("Rimda yillar davomida saylanadigan boshqaruvchilar bilan boshqariladigan tuzum nima deyiladi?", "Respublika", ["Imperiya", "Qabila", "Fir’avnlik"], d=2,
      x="Keyinchalik Rim imperiyaga aylangan."),
    Q("Rimda keyinchalik yakka hukmdor — imperator boshqargan davlat qanday atalgan?", "Imperiya", ["Respublika", "Shahar-davlat", "Jamoa"], d=2, x="Rim imperiyasi juda katta hududni egallagan."),
    TF("Kolizey — Rimdagi mashhur amfiteatr.", True, x="U hozir ham saqlanib qolgan."),
    TF("Qadimgi rimliklar lotin tilida so‘zlashgan.", True, x="Lotin alifbosi ham Rimdan tarqalgan."),
    TF("Gladiatorlar Olimpiya o‘yinlarida qatnashgan yunon sportchilari edi.", False, x="Gladiatorlar Rim arenalarida jang qilgan."),
    Q("Rimliklar suv keltirish uchun qanday inshoot qurishgan?", "Akveduk (suv o‘tkazgich)", ["Piramida", "Minora", "Zikkurat"], d=3, x="Akveduklar orqali shaharga toza suv keltirilgan."),
    Q("Hozirgi o‘zbek lotin alifbosining asosi qaysi yozuv?", "Lotin yozuvi", ["Iyeroglif", "Mixxat", "Kirill yozuvi"], d=2, x="Lotin yozuvi qadimgi Rimdan tarqalgan."),
    MATCH("Atamani ma’nosi bilan juftlang", [("Kolizey", "amfiteatr"), ("Gladiator", "arena jangchisi"), ("Lotin", "rimliklar tili"),
                                           ("Akveduk", "suv o‘tkazgich")], d=2),
    Q("Rim qaysi yarim orolda joylashgan?", "Apennin", ["Arabiston", "Skandinaviya", "Hindiston"], d=3, x="Italiya — Apennin yarim orolida."),
    Q("“Barcha yo‘llar Rimga olib boradi” degan ibora nimani bildiradi?", "Rim juda qudratli markaz bo‘lganini", ["Rimda yo‘l yo‘qligini", "Rim kichik qishloq bo‘lganini", "Rimda faqat dengiz borligini"], d=2,
      x="Rim imperiyasining ko‘plab yo‘llari poytaxtga olib borgan."),
]
T.topic("rome", "🏟️", L("Qadimgi Rim", "Ancient Rome", "Древний Рим"), C3,
        "• Rim — Italiyada (Apennin yarim oroli), Tibr daryosi bo‘yida. Avval respublika, keyin imperiya bo‘lgan.\n"
        "• Mashhur arbob — Yuliy Sezar. Til — lotin tili (lotin yozuvi hozirgi ko‘plab alifbolar asosi).\n"
        "• Kolizey — ulkan amfiteatr; gladiatorlar arenada jang qilgan. Akveduklar shaharlarga suv keltirgan.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["greece", "rome"], C3)

# ============================================================ 4-chorak
items = [
    Q("Vatanimiz hududidagi qadimgi davlatlar qaysilar?", "Baqtriya, So‘g‘diyona, Xorazm", ["Misr, Bobil, Rim", "Afina, Sparta, Troya", "Xitoy, Hindiston, Yaponiya"], x="Ular miloddan avvalgi ming yillikda mavjud bo‘lgan."),
    Q("Qadimgi Samarqand xarobalari qanday ataladi?", "Afrosiyob", ["Kolizey", "Tuproqqal’a", "Teshiktosh"], x="Afrosiyob — qadimgi Samarqand o‘rni."),
    Q("Samarqand shahrining necha yillik yubileyi 2007-yilda nishonlangan?", "2750 yillik", ["500 yillik", "1000 yillik", "100 yillik"], d=2, x="Samarqand — dunyodagi eng qadimiy shaharlardan biri."),
    Q("Buxoro va Xivaning 2500 yillik yubileyi qaysi yilda nishonlangan?", "1997-yilda", ["1991-yilda", "2007-yilda", "1941-yilda"], d=3, x="1997-yilda Buxoro va Xivaning 2500 yilligi nishonlangan."),
    Q("Zardushtiylikning muqaddas kitobi qanday nomlanadi?", "“Avesto”", ["“Boburnoma”", "“Iliada”", "“Xamsa”"], d=2, x="“Avesto” — eng qadimgi yozma manbalardan biri."),
    Q("Massagetlar malikasi To‘maris qaysi fors podshosiga qarshi kurashgan?", "Kir II", ["Aleksandr Makedonskiy", "Yuliy Sezar", "Xammurapi"], d=3, x="To‘maris miloddan avvalgi 530-yilda Kir II qo‘shiniga qarshi kurashgan."),
    Q("Dushman qo‘shinini cho‘lga adashtirib, vatanini qutqargan cho‘pon kim?", "Shiroq", ["Spitamen", "Alpomish", "Gomer"], d=2, x="Shiroq jasorati haqidagi rivoyat mashhur."),
    Q("Aleksandr Makedonskiyga qarshi kurashgan sarkarda kim?", "Spitamen", ["Shiroq", "To‘maris", "Kir II"], d=2, x="Spitamen So‘g‘diyonada qo‘zg‘olonga boshchilik qilgan."),
    TF("Afrosiyob — qadimgi Samarqand o‘rni.", True, x="Afrosiyob tepaligida qadimgi shahar xarobalari bor."),
    TF("Shiroq — Misr fir’avni.", False, x="Shiroq — vatanparvar cho‘pon, xalq qahramoni."),
    TF("To‘maris — massagetlar malikasi.", True, x="U vatan mustaqilligi uchun kurashgan."),
    MATCH("Qahramonni ishi bilan juftlang", [("To‘maris", "Kir II ga qarshi kurashgan malika"), ("Shiroq", "dushmanni cho‘lga adashtirgan cho‘pon"),
                                           ("Spitamen", "Aleksandrga qarshi kurashgan sarkarda")], d=2),
    Q("Qadimgi Xorazm hududi qaysi daryo bo‘yida joylashgan?", "Amudaryo", ["Sirdaryo", "Zarafshon", "Chirchiq"], d=2, x="Xorazm Amudaryoning quyi oqimida."),
    Q("Zarafshon vodiysida joylashgan qadimgi o‘lka qaysi?", "So‘g‘diyona", ["Baqtriya", "Xorazm", "Misr"], d=3, x="Samarqand va Buxoro So‘g‘diyona hududida."),
    Q("Qaysi shahar dunyodagi eng qadimiy shaharlardan biri?", "Samarqand", ["Navoiy", "Zarafshon", "Nurafshon"], x="Samarqand 2750 yildan ortiq tarixga ega."),
]
T.topic("ancient_uz", "🏜️", L("Vatanimizning qadimgi davlatlari va qahramonlari", "Ancient states and heroes of our land", "Древние государства и герои"), C4,
        "• Qadimgi davlatlar: Baqtriya, So‘g‘diyona (Zarafshon vodiysi), Xorazm (Amudaryo quyi oqimi).\n"
        "• Afrosiyob — qadimgi Samarqand o‘rni; Samarqandning 2750 yilligi 2007-yilda, Buxoro va Xivaning 2500 yilligi 1997-yilda nishonlangan.\n"
        "• “Avesto” — zardushtiylikning muqaddas kitobi, eng qadimgi yozma manbalardan.\n"
        "• Qahramonlar: To‘maris (massagetlar malikasi, Kir II ga qarshi), Shiroq (cho‘pon), Spitamen (Aleksandr Makedonskiyga qarshi).", items=items)

items = [
    Q("Buyuk ipak yo‘li qaysi hududlarni bog‘lagan?", "Xitoyni O‘rta yer dengizi bo‘yi bilan", ["Afrika va Amerikani", "Shimoliy va Janubiy qutbni", "Avstraliya va Osiyoni"], x="Savdo yo‘li Sharq va G‘arbni bog‘lagan."),
    Q("Buyuk ipak yo‘li qachon shakllangan?", "Miloddan avvalgi II asrda", ["Milodiy XX asrda", "Tosh davrida", "Milodiy XVIII asrda"], d=2, x="Miloddan avvalgi II asrda Xitoy va G‘arb o‘rtasida muntazam savdo boshlangan."),
    Q("Buyuk ipak yo‘lidagi qaysi shaharlar Vatanimizda joylashgan?", "Samarqand, Buxoro, Termiz", ["Rim, Afina, Iskandariya", "Pekin, Sian, Dunxuan", "Parij, London, Berlin"], x="Ular yirik savdo markazlari bo‘lgan."),
    Q("Yo‘l nomi qaysi mahsulot nomidan olingan?", "Ipak", ["Paxta", "Oltin", "Tuz"], x="Xitoy ipagi eng qimmatbaho mollardan edi."),
    Q("Savdogarlar karvonlarida yuklarni qaysi hayvonlarda tashishgan?", "Tuyalarda", ["Fillarda", "Delfinlarda", "Itlarda"], x="Tuya cho‘l sharoitiga chidamli."),
    Q("Karvonlar dam oladigan mehmonxona qanday atalgan?", "Karvonsaroy", ["Kolizey", "Piramida", "Rasadxona"], d=2, x="Karvonsaroylarda savdogarlar tunab, mol almashgan."),
    Q("Buyuk ipak yo‘li orqali nimalar tarqalgan?", "Mollar, bilimlar va madaniyat", ["Faqat ipak", "Faqat qurol", "Hech narsa"], d=2, x="Yo‘l xalqlar madaniyatini yaqinlashtirgan."),
    TF("Buyuk ipak yo‘li Xitoydan boshlangan.", True, x="Xitoydan G‘arbga qarab yo‘nalgan."),
    TF("Samarqand Buyuk ipak yo‘lidan uzoqda bo‘lgan.", False, x="Samarqand yo‘lning muhim markazi bo‘lgan."),
    TF("Buyuk ipak yo‘li orqali qog‘oz tayyorlash sirlari ham tarqalgan.", True, d=2, x="Samarqand qog‘ozi keyinchalik mashhur bo‘lgan."),
    Q("Buyuk ipak yo‘lida savdo qilgan so‘g‘d savdogarlari qaysi o‘lkadan bo‘lgan?", "So‘g‘diyonadan", ["Misrdan", "Rimdan", "Hindistondan"], d=3, x="So‘g‘dlar mohir savdogarlar sifatida mashhur bo‘lgan."),
    MATCH("Tushunchani ma’nosi bilan juftlang", [("Karvon", "yuk ortilgan tuyalar qatori"), ("Karvonsaroy", "karvon to‘xtaydigan joy"),
                                               ("Ipak", "Xitoyning qimmatbaho matosi"), ("Savdogar", "mol olib sotuvchi")], d=2),
    Q("Qaysi mahsulot Xitoydan G‘arbga olib borilgan?", "Chinni idishlar", ["Kartoshka", "Kofe", "Shokolad"], d=2, x="Ipak va chinni — Xitoyning mashhur mollari."),
    Q("Buyuk ipak yo‘li bo‘ylab savdo nima uchun foydali bo‘lgan?", "Xalqlar bir-biridan kerakli mollarni olgan", ["Hech kimga foyda bermagan", "Faqat urushlar bo‘lgan", "Shaharlar vayron bo‘lgan"], x="Savdo shaharlarning gullab-yashnashiga olib kelgan."),
    Q("Karvonlar cho‘lda qanday yo‘l topishgan?", "Yulduzlar va quduqlarga qarab", ["Svetoforlarga qarab", "Telefon xaritasi bilan", "Temir yo‘l bo‘ylab"], d=3, x="Tunda yulduzlar yo‘l ko‘rsatgan."),
]
T.topic("silk_road", "🐫", L("Buyuk ipak yo‘li", "The Great Silk Road", "Великий шёлковый путь"), C4,
        "Buyuk ipak yo‘li miloddan avvalgi II asrda shakllangan va Xitoyni O‘rta yer dengizi bo‘yi bilan bog‘lagan.\n"
        "Vatanimizdagi Samarqand, Buxoro, Termiz — yo‘lning muhim savdo markazlari. So‘g‘d savdogarlari mashhur bo‘lgan.\n"
        "Karvonlar tuyalarda yuk tashigan, karvonsaroylarda dam olgan. Yo‘l orqali mollar bilan birga bilim va madaniyat ham tarqalgan.", items=items)

SCHOLARS = [
    ("Muhammad al-Xorazmiy", "algebra fani asoschisi, “algoritm” so‘zi uning nomidan"),
    ("Ahmad al-Farg‘oniy", "astronom, Nil daryosi suv o‘lchagichini qurgan"),
    ("Abu Rayhon Beruniy", "Xorazmlik qomusiy olim, Yer globusini yasagan"),
    ("Abu Ali ibn Sino", "tabib, “Tib qonunlari” muallifi"),
    ("Mirzo Ulug‘bek", "Samarqandda rasadxona qurdirgan olim va hukmdor"),
    ("Amir Temur", "buyuk sarkarda va davlat asoschisi, poytaxti Samarqand"),
]
names = [n for n, _ in SCHOLARS]
items = []
for name, fact in SCHOLARS:
    items.append(Q(f"Kim haqida gap ketyapti: {fact}?", name, rnd.sample([n for n in names if n != name], 3), x=f"{name} — {fact}."))
items += [
    Q("“Tib qonunlari” asarining muallifi kim?", "Abu Ali ibn Sino", ["Beruniy", "Ulug‘bek", "Xorazmiy"], x="Asar ko‘p asrlar davomida tibbiyot darsligi bo‘lgan."),
    Q("Ibn Sino qayerda tug‘ilgan?", "Buxoro yaqinidagi Afshona qishlog‘ida", ["Rimda", "Pekinda", "Qohirada"], d=2, x="Ibn Sino 980-yilda Afshonada tug‘ilgan."),
    Q("Amir Temur qaysi yilda tug‘ilgan?", "1336-yilda", ["1441-yilda", "1483-yilda", "1991-yilda"], d=2, x="Amir Temur 1336-yilda Kesh (Shahrisabz) yaqinida tug‘ilgan."),
    Q("Mirzo Ulug‘bek rasadxonasi qaysi shaharda?", "Samarqandda", ["Buxoroda", "Xivada", "Toshkentda"], x="Rasadxona qoldiqlari Samarqandda saqlanib qolgan."),
    Q("“Algoritm” so‘zi qaysi olim nomi bilan bog‘liq?", "Al-Xorazmiy", ["Ibn Sino", "Beruniy", "Farg‘oniy"], x="Uning nomi lotincha “Algoritmi” deb yozilgan."),
    TF("Mirzo Ulug‘bek — Amir Temurning nabirasi.", True, d=2, x="Ulug‘bek — Temurning o‘g‘li Shohruxning farzandi."),
    TF("Beruniy Xorazmda tug‘ilgan.", True, d=2, x="Beruniy — xorazmlik qomusiy olim."),
    TF("Ibn Sino mashhur sarkarda bo‘lgan.", False, x="Ibn Sino — buyuk tabib va olim."),
    MATCH("Allomani sohasi bilan juftlang", [("Xorazmiy", "algebra"), ("Ibn Sino", "tibbiyot"), ("Ulug‘bek", "astronomiya"), ("Beruniy", "qomusiy ilm")], d=2),
]
T.topic("scholars", "🔭", L("Buyuk allomalarimiz", "Our great scholars", "Великие учёные нашего края"), C4,
        "• Muhammad al-Xorazmiy — algebra asoschisi; “algoritm” so‘zi uning nomidan.\n"
        "• Ahmad al-Farg‘oniy — astronom. • Abu Rayhon Beruniy — Xorazmlik qomusiy olim, Yer globusini yasagan.\n"
        "• Abu Ali ibn Sino (980, Afshona) — tabib, “Tib qonunlari” muallifi.\n"
        "• Amir Temur (1336, Kesh yaqinida) — sarkarda, poytaxti Samarqand. • Mirzo Ulug‘bek — Temurning nabirasi, Samarqandda rasadxona qurdirgan.", items=items)

items = [
    Q("O‘zbekiston mustaqilligi qaysi sanada nishonlanadi?", "1-sentabr", ["8-dekabr", "9-may", "21-mart"], x="O‘zbekiston 1991-yilda mustaqil bo‘ldi; Mustaqillik kuni — 1-sentabr."),
    Q("O‘zbekiston qaysi yilda mustaqil davlat bo‘ldi?", "1991-yilda", ["1924-yilda", "2000-yilda", "1945-yilda"], x="1991-yil 31-avgustda mustaqillik e’lon qilingan."),
    Q("O‘zbekiston Respublikasining poytaxti qaysi shahar?", "Toshkent", ["Samarqand", "Buxoro", "Xiva"], x="Toshkent — O‘zbekistonning poytaxti."),
    Q("Konstitutsiya kuni qaysi sanada nishonlanadi?", "8-dekabr", ["1-sentabr", "1-oktabr", "14-yanvar"], d=2, x="Konstitutsiya 1992-yil 8-dekabrda qabul qilingan."),
    Q("Davlat madhiyasi so‘zlari muallifi kim?", "Abdulla Oripov", ["Alisher Navoiy", "Erkin Vohidov", "Oybek"], d=2, x="Musiqasi — Mutal Burhonov."),
    Q("O‘zbekiston davlat ramzlari qaysilar?", "Bayroq, gerb, madhiya", ["Pul, soat, xarita", "Kitob, qalam, daftar", "Tog‘, daryo, cho‘l"], x="Davlat ramzlari — bayroq, gerb va madhiya."),
    Q("Davlat bayrog‘idagi yarim oy va yulduzlar yonidagi yashil rang nimani ifodalaydi?", "Tabiat va hayot", ["Qonni", "Qorni", "Tunni"], d=3,
      x="Moviy — osmon va suv, oq — tinchlik va poklik, yashil — tabiat, qizil chiziqlar — hayot kuchi."),
    TF("O‘zbekiston 1991-yilda mustaqil bo‘ldi.", True, x="Mustaqillik kuni — 1-sentabr."),
    TF("O‘zbekiston poytaxti — Samarqand.", False, x="Poytaxt — Toshkent."),
    TF("Davlat madhiyasi tik turib, qo‘l ko‘krakka qo‘yilgan holda tinglanadi.", True, x="Bu — davlat ramziga hurmat belgisi."),
    MATCH("Sanani bayram bilan juftlang", [("1-sentabr", "Mustaqillik kuni"), ("8-dekabr", "Konstitutsiya kuni"), ("1-oktabr", "O‘qituvchi va murabbiylar kuni")], d=2),
    Q("Davlat bayrog‘ida nechta yulduz tasvirlangan?", "12 ta", ["5 ta", "7 ta", "15 ta"], d=2, x="Bayroqda yarim oy va 12 ta yulduz bor."),
    Q("Davlat gerbida qaysi afsonaviy qush tasvirlangan?", "Humo", ["Burgut", "Laylak", "Tovus"], d=2, x="Humo qushi — baxt va erkinlik ramzi."),
    Q("Davlat bayrog‘i qaysi yilda qabul qilingan?", "1991-yilda", ["1992-yilda", "2000-yilda", "1924-yilda"], d=3, x="Bayroq 1991-yil 18-noyabrda qabul qilingan."),
    Q("Navro‘z bayrami qaysi sanada nishonlanadi?", "21-mart", ["1-yanvar", "1-sentabr", "8-dekabr"], x="Navro‘z — bahor va yangilanish bayrami."),
]
T.topic("independence", "🇺🇿", L("O‘zbekiston — mustaqil davlat", "Independent Uzbekistan", "Независимый Узбекистан"), C4,
        "• O‘zbekiston 1991-yilda mustaqil bo‘ldi; Mustaqillik kuni — 1-sentabr. Poytaxt — Toshkent.\n"
        "• Konstitutsiya kuni — 8-dekabr (1992-yil).\n"
        "• Davlat ramzlari: bayroq (1991-yil 18-noyabr; yarim oy va 12 yulduz), gerb (Humo qushi), madhiya\n"
        "  (so‘zlari Abdulla Oripov, musiqasi Mutal Burhonov). Madhiya tik turib tinglanadi.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["ancient_uz", "silk_road", "scholars", "independence"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["sources", "time", "stone_age", "egypt_mesopotamia", "india_china", "greece", "rome", "ancient_uz", "silk_road", "scholars", "independence"], C4, level=3)

T.write()
