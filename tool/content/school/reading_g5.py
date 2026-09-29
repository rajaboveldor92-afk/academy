"""Adabiyot, 5-sinf: xalq og‘zaki ijodi, mumtoz adabiyot, yangi davr adabiyoti, adabiyot nazariyasi.

Faktlar — darsliklarda keltiriladigan umumma’lum ma’lumotlar; misol matnlar o‘zimiz yozgan.
Qayta yaratish: python3 tool/content/school/reading_g5.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from readlit import *  # noqa: E402,F401,F403

rnd = random.Random(55)
T = Course("reading", 5, L("Adabiyot", "Literature", "Литература"))

C1 = "1-chorak. Xalq og‘zaki ijodi"
C2 = "2-chorak. Mumtoz adabiyot"
C3 = "3-chorak. Yangi davr o‘zbek adabiyoti"
C4 = "4-chorak. Adabiyot nazariyasi va matn tahlili"

# ============================================================ 1-chorak
SITUATIONS = [
    ("Sinf jamoasi birgalikda ishlab, maktab bog‘ini tez obodonlashtirdi.", "Birlashgan o‘zar, birlashmagan to‘zar."),
    ("Ali har kuni oz-ozdan so‘z yodlab, yil oxirida ingliz tilida bemalol gapiradigan bo‘ldi.", "Tomchi-tomchi ko‘l bo‘lur."),
    ("Dilnoza qiyin masaladan qo‘rqdi, lekin boshlab yuborgach, oson yechib qo‘ydi.", "Ko‘z qo‘rqoq, qo‘l botir."),
    ("Bobur gapirishdan oldin yaxshilab o‘ylab oldi va hech kimni xafa qilmadi.", "Avval o‘yla, keyin so‘yla."),
    ("Kichkina Jasur kattalar ham topa olmagan jumboqni yechdi.", "Aql yoshda emas, boshda."),
    ("Malika yillar davomida qunt bilan o‘qib, taniqli olima bo‘ldi.", "Olim bo‘lsang, olam seniki."),
]
items = []
all_proverbs = [f"{a} {b}" for a, b, _ in PROVERBS]
for situation, proverb in SITUATIONS:
    items.append(Q("Vaziyatga mos maqolni tanlang.", proverb, rnd.sample([p for p in all_proverbs if p != proverb], 3), text=situation, d=2,
                   x=f"Vaziyatning mazmuni maqolga mos: {proverb}"))
endings = [b for _, b, _ in PROVERBS]
for a, b, theme in PROVERBS:
    items.append(Q(f"Maqolni davom ettiring: “{a} …”", b, rnd.sample([e for e in endings if e != b], 3), x=f"{a} {b} ({theme.lower()})"))
items += [
    Q("Maqol bilan topishmoqning farqi nimada?", "Maqol ibrat beradi, topishmoq narsani topishni so‘raydi",
      ["Ikkalasi bir xil", "Maqol faqat she’rda bo‘ladi", "Topishmoqni yozuvchi yozadi"], d=2, x="Maqol — hikmatli xulosa, topishmoq — jumboq."),
    TF("Maqollar xalq og‘zaki ijodining namunasi.", True, x="Muallifi — xalq."),
]
T.topic("proverbs", "💎", L("Maqollar va ularning qo‘llanishi", "Proverbs in use", "Пословицы"), C1,
        "Maqol — xalqning ko‘p asrlik tajribasidan tug‘ilgan, qisqa va obrazli hikmatli gap.\n"
        "Maqol nutqda fikrni isbotlash va ta’sirli qilish uchun qo‘llanadi.\n"
        "Maqolni tushunish uchun uning ko‘chma ma’nosini toping: “Tomchi-tomchi ko‘l bo‘lur” — oz-ozdan to‘plangan narsa\n"
        "ko‘payadi.", items=items)

items = [
    Q("Ertaklar mazmuniga ko‘ra qanday turlarga bo‘linadi?", "Hayvonlar haqidagi, sehrli, hayotiy", ["Qisqa va uzun", "Kulgili va qayg‘uli", "Yozma va og‘zaki"],
      x="Ertaklar: hayvonlar haqidagi, sehrli-fantastik va hayotiy (maishiy) ertaklar."),
    Q("Qaysi ertakda voqealar hayvonlar orasida kechadi va ular odamlarday gapiradi?", "Hayvonlar haqidagi ertakda", ["Hayotiy ertakda", "Rivoyatda", "Dostonda"],
      x="Masalan, tulki, bo‘ri, quyon ishtirok etadigan ertaklar."),
    Q("Sehrli ertakda nima bo‘ladi?", "G‘ayritabiiy kuchlar va sehrli buyumlar", ["Faqat haqiqiy voqealar", "Tarixiy sanalar", "Ilmiy tajribalar"],
      x="Sehrli ertaklarda dev, pari, uchar gilam kabi to‘qima obrazlar bo‘ladi."),
    Q("“Ur to‘qmoq” ertagidagi o‘z-o‘zidan uradigan to‘qmoq qanday buyum?", "Sehrli buyum", ["Oddiy mehnat quroli", "Tarixiy yodgorlik", "O‘yinchoq"], d=2,
      x="U buyruq bilan o‘z-o‘zidan uradi — sehrli buyum."),
    Q("Afsona qanday asar?", "To‘qima, g‘ayrioddiy voqealar haqidagi og‘zaki hikoya", ["Aniq tarixiy hujjat", "Ilmiy maqola", "Rasmiy xat"], d=2,
      x="Afsonada xayoliy voqea va obrazlar bo‘ladi."),
    Q("Rivoyat afsonadan nimasi bilan farq qiladi?", "Haqiqatga yaqin, ko‘pincha tarixiy shaxs haqida bo‘ladi", ["Doim she’r bilan aytiladi", "Faqat hayvonlar haqida bo‘ladi", "Muallifi aniq bo‘ladi"], d=2,
      x="Masalan, Shiroq va To‘maris haqidagi rivoyatlar."),
    Q("Vatanini himoya qilib, dushman qo‘shinini cho‘lga adashtirgan cho‘pon haqidagi rivoyat qahramoni kim?", "Shiroq", ["Alpomish", "Go‘ro‘g‘li", "Spitamen"], d=2,
      x="Shiroq haqidagi rivoyat vatanparvarlikni ulug‘laydi."),
    Q("Massagetlar malikasi, mard ayol haqidagi rivoyat qahramoni kim?", "To‘maris", ["Barchin", "Zumrad", "Qimmat"], d=3, x="To‘maris — massagetlar malikasi."),
    TF("Ertaklarda ko‘pincha yaxshilik yomonlik ustidan g‘alaba qiladi.", True, x="Bu — xalq orzusining ifodasi."),
    TF("Afsona tarixiy hujjat hisoblanadi.", False, x="Afsona — to‘qima, xayoliy hikoya."),
    TF("Ertak, afsona, rivoyat — xalq og‘zaki ijodi janrlari.", True, x="Ularni xalq yaratgan."),
    MATCH("Janrni belgisi bilan juftlang", [("Ertak", "to‘qima voqea, yaxshilik g‘alabasi"), ("Afsona", "xayoliy, g‘ayrioddiy hikoya"),
                                           ("Rivoyat", "tarixiy shaxs haqidagi hikoya"), ("Maqol", "qisqa hikmatli gap"),
                                           ("Topishmoq", "yashirin ta’rif, jumboq")], d=2),
    Q("Qaysi biri hayotiy (maishiy) ertakning belgisi?", "Oddiy odamlar hayotidagi voqealar", ["Devlar va parilar", "Uchar gilam", "Gapiradigan daraxt"], d=2,
      x="Hayotiy ertaklarda sehr kam, voqealar kundalik hayotga yaqin."),
    Q("Ertaklarning an’anaviy boshlanmasi qaysi?", "Bor ekan-u, yo‘q ekan…", ["Qadrli o‘quvchilar…", "Xulosa qilib aytganda…", "Mavzu:"], x="Ertaklar ko‘pincha shunday boshlanadi."),
    Q("Xalq og‘zaki ijodi asarlari qanday saqlanib kelgan?", "Og‘izdan og‘izga, avloddan avlodga o‘tib", ["Faqat kitoblarda", "Faqat toshga yozilib", "Radio orqali"],
      x="Keyinchalik ular yozib olinib, to‘plamlarda nashr etilgan."),
]
T.topic("tales", "🐉", L("Ertak, afsona, rivoyat", "Tales, myths and legends", "Сказки, мифы, предания"), C1,
        "• Ertak — to‘qima voqea; turlari: hayvonlar haqidagi, sehrli, hayotiy (maishiy) ertaklar.\n"
        "• Afsona — xayoliy, g‘ayrioddiy voqealar haqidagi og‘zaki hikoya.\n"
        "• Rivoyat — haqiqatga yaqin, ko‘pincha tarixiy shaxs haqidagi hikoya: Shiroq, To‘maris haqidagi rivoyatlar.\n"
        "Bularning barchasi xalq og‘zaki ijodiga kiradi.", items=items)

items = [
    Q("“Alpomish” qanday asar?", "Xalq qahramonlik dostoni", ["Roman", "G‘azal", "Masal"], x="“Alpomish” — o‘zbek xalqining qahramonlik dostoni."),
    Q("“Alpomish” dostonining bosh qahramoni kim?", "Alpomish", ["Go‘ro‘g‘li", "Shiroq", "Farhod"], x="Doston uning nomi bilan ataladi."),
    Q("Alpomishning sevgan qizi (qallig‘i) kim?", "Barchin", ["Zumrad", "Layli", "Shirin"], x="Barchinoy — Alpomishning qallig‘i."),
    Q("Alpomishning oti qanday nomlanadi?", "Boychibor", ["G‘irot", "Duldul", "Qorabayir"], d=2, x="Boychibor — Alpomishning sadoqatli oti."),
    Q("Dostonlarni xalq orasida kim kuylab ijro etadi?", "Baxshilar", ["Kotiblar", "Savdogarlar", "Hunarmandlar"], x="Baxshilar dostonni do‘mbira jo‘rligida kuylaydi."),
    Q("Baxshilar dostonni qaysi cholg‘u jo‘rligida kuylaydi?", "Do‘mbira", ["Pianino", "Skripka", "Baraban"], d=2, x="Do‘mbira — baxshilarning an’anaviy cholg‘usi."),
    Q("“Alpomish” dostonining eng mashhur variantini qaysi baxshi aytgan?", "Fozil Yo‘ldosh o‘g‘li", ["Alisher Navoiy", "Abdulla Qodiriy", "Gulxaniy"], d=3,
      x="Mashhur baxshi Fozil Yo‘ldosh o‘g‘lidan yozib olingan variant eng mashhuri."),
    Q("“Alpomish” dostonida qanday fazilatlar ulug‘lanadi?", "Vatanparvarlik, sadoqat, mardlik", ["Xiyonat va qo‘rqoqlik", "Dangasalik", "Maqtanchoqlik"], x="Doston qahramonlik va sadoqatni ulug‘laydi."),
    Q("“Go‘ro‘g‘li” qanday asar?", "Xalq dostonlari turkumi", ["Roman", "Ertak", "Ruboiy"], d=2, x="Go‘ro‘g‘li haqidagi dostonlar turkumi mavjud."),
    Q("G‘irot kimning oti?", "Go‘ro‘g‘lining", ["Alpomishning", "Farhodning", "Shiroqning"], d=3, x="G‘irot — Go‘ro‘g‘lining mashhur oti."),
    TF("Dostonlar nasrda va she’rda aralash aytiladi.", True, d=2, x="Dostonda she’riy qismlar va nasriy parchalar almashib keladi."),
    TF("“Alpomish” dostonini Alisher Navoiy yozgan.", False, x="U xalq og‘zaki ijodi — muallifi xalq."),
    TF("Boychibor — Alpomishning oti.", True, x="Boychibor egasiga sodiq qoladi."),
    TF("Baxshilar dostonlarni yod bilib, kuylab aytgan.", True, x="Dostonlar og‘zaki holda saqlangan."),
    MATCH("Qahramonni dostondagi o‘rni bilan juftlang", [("Alpomish", "bosh qahramon"), ("Barchin", "Alpomishning qallig‘i"),
                                                        ("Boychibor", "Alpomishning oti"), ("Baxshi", "dostonni kuylovchi")], d=2),
]
T.topic("epic", "🐎", L("“Alpomish” dostoni", "The epic Alpomish", "Дастан «Алпамыш»"), C1,
        "Doston — xalq og‘zaki ijodidagi katta hajmli, she’r va nasr aralash asar. Dostonlarni baxshilar do‘mbira jo‘rligida kuylaydi.\n"
        "“Alpomish” — o‘zbek xalqining qahramonlik dostoni. Bosh qahramon — Alpomish, qallig‘i — Barchin, oti — Boychibor.\n"
        "Dostonda vatanparvarlik, sadoqat va mardlik ulug‘lanadi. Eng mashhur variant — Fozil Yo‘ldosh o‘g‘lidan yozib olingan.", items=items)

T.topic("understand", "📚", L("Matndan xulosa chiqarish", "Reading and inferring", "Выводы из текста"), C1,
        "Matnni boshidan oxirigacha o‘qing. Kim, nima, qayerda va nima sababdan degan savollarga matndan dalil toping. "
        "Xulosa matndagi voqea va qahramon xatti-harakatiga asoslansin.",
        gen="comprehension", levels=[dict(options=n, infer=True) for n in (2, 3, 4)])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["proverbs", "tales", "epic"], C1)

# ============================================================ 2-chorak
items = [
    Q("Alisher Navoiy qaysi yilda tug‘ilgan?", "1441-yilda", ["1336-yilda", "1483-yilda", "1991-yilda"], x="Alisher Navoiy 1441-yil 9-fevralda Hirotda tug‘ilgan."),
    Q("Alisher Navoiy qaysi shaharda tug‘ilgan?", "Hirotda", ["Samarqandda", "Andijonda", "Xivada"], x="Hirot — Temuriylar davrining madaniy markazi."),
    Q("“Xamsa” nechta dostondan iborat?", "5 ta", ["3 ta", "7 ta", "10 ta"], x="“Xamsa” — “beshlik” degani."),
    Q("Qaysi doston “Xamsa” tarkibiga kiradi?", "“Farhod va Shirin”", ["“Alpomish”", "“Go‘ro‘g‘li”", "“Oygul bilan Baxtiyor”"], x="“Xamsa”: “Hayrat ul-abror”, “Farhod va Shirin”, “Layli va Majnun”, “Sab’ai sayyor”, “Saddi Iskandariy”."),
    Q("Qaysi doston “Xamsa” tarkibiga kirmaydi?", "“Alpomish”", ["“Layli va Majnun”", "“Saddi Iskandariy”", "“Sab’ai sayyor”"], d=2, x="“Alpomish” — xalq dostoni."),
    Q("“Xamsa”ning birinchi dostoni qaysi?", "“Hayrat ul-abror”", ["“Farhod va Shirin”", "“Saddi Iskandariy”", "“Layli va Majnun”"], d=3, x="“Hayrat ul-abror” — “Xamsa”ning birinchi dostoni."),
    Q("Navoiyning nasriy asari qaysi?", "“Mahbub ul-qulub”", ["“Xamsa”", "“Boburnoma”", "“Shum bola”"], d=2, x="“Mahbub ul-qulub” — nasr bilan yozilgan hikmatli asar."),
    Q("Alisher Navoiy qaysi til rivojiga katta hissa qo‘shgan?", "Turkiy (eski o‘zbek) til", ["Lotin tili", "Ingliz tili", "Xitoy tili"], d=2,
      x="U “Muhokamat ul-lug‘atayn” asarida turkiy tilning boyligini isbotlagan."),
    TF("Alisher Navoiy — o‘zbek adabiy tilining asoschisi hisoblanadi.", True, x="U turkiy tilda buyuk asarlar yaratgan."),
    TF("“Xamsa” — bitta doston.", False, x="“Xamsa” — besh dostondan iborat."),
    TF("“Layli va Majnun” — “Xamsa” tarkibidagi doston.", True, x="U “Xamsa”ning uchinchi dostoni."),
    MATCH("Asarni turi bilan juftlang", [("“Xamsa”", "besh dostonli asar"), ("“Mahbub ul-qulub”", "nasriy hikmatli asar"),
                                        ("“Farhod va Shirin”", "“Xamsa” dostoni"), ("“Muhokamat ul-lug‘atayn”", "tillar qiyosi haqida asar")], d=2),
    Q("Navoiy asarlarida qanday fazilatlar ulug‘lanadi?", "Ilm, odob, mehnat, sadoqat", ["Xasislik", "Yolg‘onchilik", "Dangasalik"], x="Navoiy insonni ezgulikka chorlaydi."),
    Q("Navoiy qaysi davrda yashagan?", "Temuriylar davrida", ["Mustaqillik davrida", "Qadimgi Misr davrida", "XX asrda"], d=2, x="U Husayn Boyqaro saroyida xizmat qilgan."),
    Q("Navoiy bilan yaqin do‘st bo‘lgan hukmdor kim?", "Husayn Boyqaro", ["Amir Temur", "Aleksandr Makedonskiy", "Mirzo Ulug‘bek"], d=3,
      x="Husayn Boyqaro — Xuroson hukmdori, Navoiyning bolalikdagi do‘sti."),
]
T.topic("navoi", "📜", L("Alisher Navoiy", "Alisher Navoi", "Алишер Навои"), C2,
        "Alisher Navoiy (1441–1501) — buyuk shoir va mutafakkir, Hirotda tug‘ilgan. U o‘zbek adabiy tilining asoschisi hisoblanadi.\n"
        "• “Xamsa” (beshlik): “Hayrat ul-abror”, “Farhod va Shirin”, “Layli va Majnun”, “Sab’ai sayyor”, “Saddi Iskandariy”.\n"
        "• “Mahbub ul-qulub” — nasriy hikmatli asar; “Muhokamat ul-lug‘atayn” — turkiy va fors tillari qiyosi.\n"
        "Navoiy asarlarida ilm, odob, mehnat va sadoqat ulug‘lanadi.", items=items)

items = [
    Q("Zahiriddin Muhammad Bobur qaysi yilda tug‘ilgan?", "1483-yilda", ["1441-yilda", "1336-yilda", "1924-yilda"], x="Bobur 1483-yilda Andijonda tug‘ilgan."),
    Q("Bobur qaysi shaharda tug‘ilgan?", "Andijonda", ["Hirotda", "Samarqandda", "Buxoroda"], x="Andijon — Farg‘ona vodiysidagi shahar."),
    Q("“Boburnoma” qanday asar?", "Bobur hayoti va zamonasi haqidagi xotira asari", ["Ertaklar to‘plami", "Doston", "Lug‘at"], x="Unda voqealar, shaharlar, tabiat va odamlar tasvirlangan."),
    Q("Bobur qaysi mamlakatda yangi saltanatga asos solgan?", "Hindistonda", ["Misrda", "Xitoyda", "Rimda"], d=2, x="Bobur Hindistonda Boburiylar saltanatiga asos solgan."),
    Q("Bobur faqat hukmdor emas, yana kim edi?", "Shoir va yozuvchi", ["Futbolchi", "Rassom", "Kosmonavt"], x="U g‘azal va ruboiylar ham yozgan."),
    Q("To‘rt misrali she’r nima deyiladi?", "Ruboiy", ["G‘azal", "Doston", "Masal"], d=2, x="Boburning ruboiylari mashhur."),
    TF("“Boburnoma”ni Alisher Navoiy yozgan.", False, x="Uni Zahiriddin Muhammad Bobur yozgan."),
    TF("Bobur Andijonda tug‘ilgan.", True, x="1483-yilda."),
    Q("“Qutadg‘u bilig” asarining muallifi kim?", "Yusuf Xos Hojib", ["Mahmud Koshg‘ariy", "Gulxaniy", "Bobur"], d=1, x="“Qutadg‘u bilig” — “Baxtga eltuvchi bilim” ma’nosini beradi."),
    Q("“Devonu lug‘otit turk” asarining muallifi kim?", "Mahmud Koshg‘ariy", ["Yusuf Xos Hojib", "Alisher Navoiy", "Ogahiy"], d=2, x="Bu — turkiy so‘zlar lug‘ati va qomusi."),
    Q("“Zarbulmasal” asarining muallifi kim?", "Gulxaniy", ["Bobur", "Navoiy", "Qodiriy"], d=2, x="“Zarbulmasal” — masallar va maqollarga boy asar."),
    Q("“Zarbulmasal”da voqealar kimlar orqali hikoya qilinadi?", "Qushlar orqali", ["Podshohlar orqali", "Olimlar orqali", "Dengizchilar orqali"], d=3,
      x="Asar qahramonlari — boyqush, qarg‘a kabi qushlar."),
    Q("Nodira kim bo‘lgan?", "Shoira", ["Sarkarda", "Me’mor", "Olim"], d=2, x="Nodira — XIX asr o‘zbek shoirasi."),
    MATCH("Asarni muallifi bilan juftlang", [(w, a) for w, a in WORKS if a in ("Zahiriddin Muhammad Bobur", "Yusuf Xos Hojib", "Mahmud Koshg‘ariy", "Gulxaniy", "Alisher Navoiy")], d=2),
    TF("Mumtoz adabiyot — o‘tmishda yaratilgan namunali adabiyot.", True, x="Navoiy, Bobur, Gulxaniy asarlari mumtoz adabiyotga kiradi."),
]
T.topic("classics", "🏰", L("Bobur va mumtoz adabiyot", "Babur and classical literature", "Бабур и классическая литература"), C2,
        "• Zahiriddin Muhammad Bobur (1483–1530) — Andijonda tug‘ilgan hukmdor, shoir; “Boburnoma” muallifi.\n"
        "  Hindistonda Boburiylar saltanatiga asos solgan; ruboiylari mashhur (ruboiy — to‘rt misrali she’r).\n"
        "• Yusuf Xos Hojib — “Qutadg‘u bilig”; Mahmud Koshg‘ariy — “Devonu lug‘otit turk”.\n"
        "• Gulxaniy — “Zarbulmasal” (qushlar tilidan hikoya, maqollarga boy).", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["navoi", "classics"], C2)

# ============================================================ 3-chorak
MODERN = [
    ("“O‘tkan kunlar”", "Abdulla Qodiriy"), ("“Mehrobdan chayon”", "Abdulla Qodiriy"), ("“Kecha va kunduz”", "Abdulhamid Cho‘lpon"),
    ("“Bolalik”", "Oybek"), ("“Navoiy” romani", "Oybek"), ("“Shum bola”", "G‘afur G‘ulom"), ("“Sen yetim emassan”", "G‘afur G‘ulom"),
    ("“Oygul bilan Baxtiyor”", "Hamid Olimjon"), ("“O‘g‘ri” hikoyasi", "Abdulla Qahhor"), ("“Sarob”", "Abdulla Qahhor"),
    ("“Dunyoning ishlari”", "O‘tkir Hoshimov"), ("“Sariq devni minib”", "Xudoyberdi To‘xtaboyev"), ("“O‘zbegim”", "Erkin Vohidov"),
]
modern_authors = sorted({a for _, a in MODERN})
items = []
for work, author in MODERN:
    items.append(Q(f"{work} asarining muallifi kim?", author, rnd.sample([a for a in modern_authors if a != author], 3),
                   d=1 if work in ("“O‘tkan kunlar”", "“Bolalik”", "“Shum bola”", "“Sariq devni minib”", "“Kecha va kunduz”", "“Dunyoning ishlari”") else 2,
                   x=f"{work} — {author} asari."))
items += [
    Q("Birinchi o‘zbek romani qaysi?", "“O‘tkan kunlar”", ["“Boburnoma”", "“Alpomish”", "“Shum bola”"], x="“O‘tkan kunlar”ni Abdulla Qodiriy yozgan."),
    Q("O‘zbekiston Davlat madhiyasi so‘zlari muallifi kim?", "Abdulla Oripov", ["Erkin Vohidov", "Hamid Olimjon", "Oybek"], x="Musiqasi — Mutal Burhonov."),
    Q("“Shum bola” qanday janrdagi asar?", "Qissa", ["G‘azal", "Masal", "Ruboiy"], d=2, x="Qissa — hikoyadan katta, romandan kichik nasriy asar."),
    Q("Zulfiya kim bo‘lgan?", "Shoira", ["Rassom", "Bastakor", "Olim"], x="Zulfiya — mashhur o‘zbek shoirasi."),
    TF("“Bolalik” — Oybekning o‘z bolaligi haqidagi qissasi.", True, x="Asar muallif xotiralari asosida yozilgan."),
    TF("“O‘tkan kunlar” romanini Cho‘lpon yozgan.", False, x="“O‘tkan kunlar” — Abdulla Qodiriy romani."),
    MATCH("Adibni asari bilan juftlang", [("Abdulla Qodiriy", "“O‘tkan kunlar”"), ("Oybek", "“Bolalik”"), ("G‘afur G‘ulom", "“Shum bola”"),
                                         ("Cho‘lpon", "“Kecha va kunduz”"), ("O‘tkir Hoshimov", "“Dunyoning ishlari”")], d=2),
]
T.topic("modern", "📕", L("Yangi davr o‘zbek adabiyoti", "Modern Uzbek literature", "Современная узбекская литература"), C3,
        "• Abdulla Qodiriy — “O‘tkan kunlar” (birinchi o‘zbek romani), “Mehrobdan chayon”.\n"
        "• Cho‘lpon — “Kecha va kunduz”. • Oybek — “Bolalik”, “Navoiy”. • G‘afur G‘ulom — “Shum bola”, “Sen yetim emassan”.\n"
        "• Hamid Olimjon — “Oygul bilan Baxtiyor”; Zulfiya — shoira. • Abdulla Qahhor — “O‘g‘ri”, “Sarob”.\n"
        "• O‘tkir Hoshimov — “Dunyoning ishlari”; Xudoyberdi To‘xtaboyev — “Sariq devni minib”.\n"
        "• Abdulla Oripov — Davlat madhiyasi so‘zlari muallifi; Erkin Vohidov — “O‘zbegim”.", items=items)

H1 = ("Qishloq chekkasida keksa tut daraxti bor edi. Bolalar uning soyasida o‘ynashar, qushlar shoxlariga in qurishardi. "
      "Bir kuni kuchli bo‘ron turib, daraxtning katta shoxi sindi. Ertasi kuni bolalar bobolari bilan kelib, singan joyni "
      "bog‘lab qo‘yishdi, atrofini chopib, suv berishdi. Bahorda tut yana yashnadi, shoxlarida yangi kurtaklar ko‘rindi.")
H2 = ("Nodir rasm tanlovida ikkinchi o‘rinni oldi. Birinchi o‘rin uning do‘sti Sanjarga nasib etdi. Nodir avvaliga xafa bo‘ldi, "
      "keyin esa Sanjarning oldiga borib, uni chin dildan tabrikladi. “Keyingi safar birga chizamiz, sen menga soya berishni "
      "o‘rgat”, dedi u. Sanjar jilmayib, bosh irg‘adi.")
items = [
    Q("Hikoyaning mavzusi nima?", "Tabiatga g‘amxo‘rlik", ["Sport musobaqasi", "Maktab bayrami", "Uzoq safar"], text=H1, x="Bolalar sinib qolgan daraxtni asrab qolishdi."),
    Q("Hikoyaning g‘oyasi qaysi?", "Tabiatni asrasak, u bizga yana quvonch beradi", ["Daraxtlar keraksiz", "Bo‘ron foydali", "Bolalar faqat o‘ynashi kerak"], text=H1, d=1,
      x="G‘oya — muallif aytmoqchi bo‘lgan asosiy fikr."),
    Q("Daraxtning shoxi nima sababdan sindi?", "Kuchli bo‘rondan", ["Bolalar sindirgani uchun", "Qurib qolgani uchun", "Qor og‘irligidan"], text=H1, x="“Kuchli bo‘ron turib, daraxtning katta shoxi sindi.”"),
    Q("Matnda qaysi tasvir usuli bor: “Bahorda tut yana yashnadi”?", "Tabiat tasviri (peyzaj)", ["Portret", "Dialog", "Monolog"], text=H1, d=2,
      x="Tabiat manzarasining tasviri — peyzaj."),
    Q("Nodir qaysi o‘rinni oldi?", "Ikkinchi", ["Birinchi", "Uchinchi", "Hech qanday"], text=H2, x="U ikkinchi o‘rinni oldi."),
    Q("Nodirning qaysi fazilati namoyon bo‘ldi?", "Do‘stining yutug‘idan quvona olishi", ["Hasadgo‘yligi", "Maqtanchoqligi", "Dangasaligi"], text=H2, d=1,
      x="U xafa bo‘lsa ham, do‘stini chin dildan tabrikladi."),
    Q("Nodir va Sanjarning suhbati qanday tasvir usuli?", "Dialog", ["Peyzaj", "Portret", "Qofiya"], text=H2, d=2, x="Qahramonlarning o‘zaro suhbati — dialog."),
    Q("Hikoyaga mos maqolni tanlang.", "Do‘stsiz boshim — tuzsiz oshim.", ["Ko‘z qo‘rqoq, qo‘l botir.", "Hunar — hunardan unar.", "Tomchi-tomchi ko‘l bo‘lur."], text=H2, d=3,
      x="Hikoya do‘stlik qadri haqida."),
    TF("Bolalar singan shoxni bog‘lab, daraxtga suv berishdi.", True, text=H1, x="Matnda shunday yozilgan."),
    TF("Nodir Sanjarni tabriklamadi.", False, text=H2, x="U Sanjarni chin dildan tabrikladi."),
    Q("Asarning mavzusi va g‘oyasi qanday farqlanadi?", "Mavzu — nima haqida, g‘oya — asosiy fikr", ["Ular bir xil", "Mavzu — muallif ismi", "G‘oya — sarlavha"], d=2,
      x="Mavzu: asar nima haqida; g‘oya: muallif nimani aytmoqchi."),
    Q("Qahramonning tashqi ko‘rinishi tasviri nima deyiladi?", "Portret", ["Peyzaj", "Dialog", "Syujet"], x="Portret — qahramon tashqi qiyofasining tasviri."),
    Q("Asardagi voqealar tizimi nima deyiladi?", "Syujet", ["Qofiya", "Portret", "Band"], d=2, x="Syujet — voqealarning bog‘lanib, rivojlanib borishi."),
    Q("Bitta qahramonning o‘z-o‘zi bilan yoki uzoq gapirishi nima deyiladi?", "Monolog", ["Dialog", "Peyzaj", "Portret"], d=2, x="Monolog — bir kishi nutqi."),
    MATCH("Atamani ta’rifi bilan juftlang", [("Mavzu", "asar nima haqida"), ("G‘oya", "asosiy fikr"), ("Peyzaj", "tabiat tasviri"),
                                            ("Portret", "tashqi qiyofa tasviri"), ("Dialog", "ikki kishi suhbati")], d=2),
]
T.topic("analysis", "🔍", L("Badiiy matn tahlili", "Analysing a text", "Анализ текста"), C3,
        "Asarni tahlil qilishda:\n"
        "• Mavzu — asar nima haqida; g‘oya — muallif aytmoqchi bo‘lgan asosiy fikr.\n"
        "• Syujet — voqealar rivoji; qahramon — voqea ishtirokchisi.\n"
        "• Tasvir usullari: portret (tashqi qiyofa), peyzaj (tabiat), dialog (suhbat), monolog (bir kishi nutqi).", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["modern", "analysis"], C3)

# ============================================================ 4-chorak
KINDS = [("hikoya", "Epik"), ("roman", "Epik"), ("qissa", "Epik"), ("g‘azal", "Lirik"), ("ruboiy", "Lirik"), ("she’r", "Lirik"),
         ("komediya", "Dramatik"), ("drama", "Dramatik"), ("tragediya", "Dramatik")]
items = []
for genre, kind in KINDS:
    items.append(Q(f"“{genre}” qaysi adabiy turga mansub?", f"{kind} tur", [f"{k} tur" for k in ("Epik", "Lirik", "Dramatik") if k != kind] + ["Xalq og‘zaki ijodi"],
                   d=1 if genre in ("hikoya", "roman", "she’r", "komediya") else 2, x=f"{genre} — {kind.lower()} tur."))
items += [
    Q("Qaysi turda voqea hikoya qilinadi?", "Epik", ["Lirik", "Dramatik", "Hech qaysi"], x="Epik asarlarda voqealar hikoya qilinadi: hikoya, qissa, roman."),
    Q("Qaysi turda his-tuyg‘u ifodalanadi?", "Lirik", ["Epik", "Dramatik", "Hech qaysi"], x="Lirik asar — she’r, g‘azal, ruboiy."),
    Q("Qaysi tur sahnada ijro etish uchun yoziladi?", "Dramatik", ["Epik", "Lirik", "Hech qaysi"], x="Dramatik asar qahramonlar nutqi (dialog) asosida quriladi."),
    Q("Hajmi jihatidan eng katta epik asar qaysi?", "Roman", ["Hikoya", "Qissa", "Masal"], d=2, x="Hikoya < qissa < roman."),
    TF("Komediya — kulgili dramatik asar.", True, x="Komediya kamchiliklarni kulgi orqali fosh etadi."),
    TF("Roman lirik turga mansub.", False, x="Roman — epik tur."),
    MATCH("Janrni turi bilan juftlang", [("roman", "epik"), ("g‘azal", "lirik"), ("komediya", "dramatik")], d=2),
]
T.topic("kinds", "🎭", L("Adabiy tur va janrlar", "Literary kinds and genres", "Роды и жанры"), C4,
        "Adabiyot uch turga bo‘linadi:\n"
        "• Epik — voqea hikoya qilinadi: hikoya, qissa, roman (hajmi hikoyadan romanga qarab ortadi).\n"
        "• Lirik — his-tuyg‘u ifodalanadi: she’r, g‘azal, ruboiy.\n"
        "• Dramatik — sahnada ijro etish uchun: drama, komediya, tragediya.", items=items)

DEVICES = [
    ("Qizning yuzi oydek go‘zal.", "O‘xshatish"), ("Qor paxtadek oppoq.", "O‘xshatish"), ("Bola sherdek botir.", "O‘xshatish"),
    ("Shamol qo‘shiq kuyladi.", "Jonlantirish"), ("Daraxtlar bir-biriga nimadir shivirlashdi.", "Jonlantirish"), ("Quyosh bizga jilmaydi.", "Jonlantirish"),
    ("Ko‘z yoshi daryo bo‘lib oqdi.", "Mubolag‘a"), ("Alp bir sakrab, tog‘dan oshib o‘tdi.", "Mubolag‘a"), ("Ming yil kutdim seni!", "Mubolag‘a"),
    ("oltin kuz", "Sifatlash"), ("kumush qor", "Sifatlash"), ("zangori osmon", "Sifatlash"),
]
DEVICE_X = {"O‘xshatish": "Narsa boshqasiga qiyoslangan (-dek, -day, kabi).",
            "Jonlantirish": "Jonsiz narsaga insonga xos harakat berilgan.",
            "Mubolag‘a": "Belgi ataylab kuchaytirib, oshirib tasvirlangan.",
            "Sifatlash": "Narsaning obrazli, bo‘yoqdor belgisi ko‘rsatilgan."}
items = []
for example, device in DEVICES:
    items.append(Q(f"“{example}” — qaysi badiiy tasvir vositasi?", device, [d for d in ("O‘xshatish", "Jonlantirish", "Mubolag‘a", "Sifatlash") if d != device],
                   d=1 if device in ("O‘xshatish", "Jonlantirish") else 2, x=DEVICE_X[device]))
items += [
    Q("O‘xshatishda ko‘pincha qaysi qo‘shimcha yoki so‘z qatnashadi?", "-dek, -day, kabi", ["-lar, -ning", "-ga, -da", "-chi, -kor"], d=2, x="oydek, sherday, paxta kabi."),
    TF("“Gullar kuldi” — jonlantirish.", True, x="Gullarga insonga xos harakat (kulish) berilgan."),
    TF("“Qor paxtadek oppoq” — mubolag‘a.", False, x="Bu — o‘xshatish: qor paxtaga qiyoslangan."),
    MATCH("Vositani misol bilan juftlang", [("O‘xshatish", "sherdek botir"), ("Jonlantirish", "shamol kuyladi"), ("Mubolag‘a", "ko‘z yoshi daryo bo‘ldi"),
                                           ("Sifatlash", "oltin kuz")], d=2),
]
T.topic("devices", "🎨", L("Badiiy tasvir vositalari", "Figures of speech", "Средства выразительности"), C4,
        "• O‘xshatish — bir narsani boshqasiga qiyoslash: sherdek botir, paxtadek oppoq.\n"
        "• Jonlantirish — jonsiz narsaga insonga xos xususiyat berish: shamol kuyladi, quyosh jilmaydi.\n"
        "• Mubolag‘a — belgini ataylab oshirib tasvirlash: ko‘z yoshi daryo bo‘ldi.\n"
        "• Sifatlash — obrazli, bo‘yoqdor sifat: oltin kuz, kumush qor.", items=items)

items = [
    Q("She’rning bir qatori nima deyiladi?", "Misra", ["Band", "Bayt", "Qofiya"], x="Misra — she’rning bir qatori."),
    Q("Ikki misradan iborat she’riy birlik nima deyiladi?", "Bayt", ["Band", "Ruboiy", "Radif"], x="G‘azal baytlardan tuziladi."),
    Q("To‘rt misrali mustaqil she’r nima deyiladi?", "Ruboiy", ["G‘azal", "Doston", "Masal"], x="Boburning ruboiylari mashhur."),
    Q("Misralar oxirida ohangdosh so‘zlarning kelishi nima deyiladi?", "Qofiya", ["Radif", "Bayt", "Band"], x="bahor — anor, tog‘ — bog‘."),
    Q("Qofiyadan keyin takrorlanib keladigan so‘z nima deyiladi?", "Radif", ["Qofiya", "Misra", "Band"], d=2, x="Radif — qofiyadan keyin aynan takrorlanadigan so‘z yoki so‘zlar."),
    Q("G‘azalning birinchi bayti nima deyiladi?", "Matla’", ["Maqta’", "Radif", "Band"], d=3, x="Matla’ — g‘azal boshlanmasi."),
    Q("G‘azalning oxirgi bayti nima deyiladi?", "Maqta’", ["Matla’", "Ruboiy", "Qofiya"], d=3, x="Maqta’da ko‘pincha shoirning taxallusi keladi."),
    Q("Shoirning adabiy nomi nima deyiladi?", "Taxallus", ["Radif", "Sarlavha", "Band"], d=2, x="Masalan, Alisher Navoiyning taxalluslari: Navoiy, Foniy."),
    Q("Qaysi so‘zlar qofiyadosh?", "diyor — bahor", ["kitob — maktab", "olma — anor", "tog‘ — daryo"], x="Oxiri ohangdosh: -or."),
    Q("Qaysi so‘zlar qofiyadosh?", "gul — bulbul", ["gul — lola", "bulbul — qush", "gul — daraxt"], x="Oxiri ohangdosh: -ul."),
    TF("Band bir necha misradan iborat bo‘ladi.", True, x="Masalan, to‘rt misrali band."),
    TF("Bayt uch misradan iborat.", False, x="Bayt — ikki misra."),
    TF("Ruboiy to‘rt misradan iborat.", True, x="Ruboiy — to‘rtlik."),
    MATCH("Atamani ta’rifi bilan juftlang", [("Misra", "she’rning bir qatori"), ("Bayt", "ikki misra"), ("Ruboiy", "to‘rt misrali she’r"),
                                            ("Qofiya", "ohangdosh so‘zlar"), ("Radif", "qofiyadan keyin takrorlanadigan so‘z")], d=2),
    ORDER("So‘zlardan gap tuzing", "G‘azal baytlardan tuziladi", d=1),
]
T.topic("verse", "🎼", L("She’r tuzilishi", "The structure of a poem", "Строение стиха"), C4,
        "• Misra — she’rning bir qatori; band — misralar guruhi.\n"
        "• Bayt — ikki misra; g‘azal baytlardan tuziladi: birinchi bayt — matla’, oxirgi bayt — maqta’.\n"
        "• Ruboiy — to‘rt misrali she’r.\n"
        "• Qofiya — ohangdosh so‘zlar (bahor — diyor); radif — qofiyadan keyin takrorlanadigan so‘z.\n"
        "• Taxallus — shoirning adabiy nomi.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["kinds", "devices", "verse"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["proverbs", "tales", "epic", "navoi", "classics", "modern", "analysis", "kinds", "devices", "verse"], C4, level=3)

T.write()
