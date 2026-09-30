"""Ona tili, 6-sinf: leksikologiya, iboralar, so‘z yasalishi, ot va sifat turlari, son va olmosh turlari, imlo.

Mavzular 6-sinf ona tili dasturi tartibida (5-sinfdan keyingi bosqich); qoidalar, misollar va savollar
o‘zimizniki. 5-sinfdagi sinonim, omonim, ibora va atama ro‘yxatlari takrorlanmasligi uchun so‘zlar shu faylda
yangidan tanlangan.
Qayta yaratish: python3 tool/content/school/onatili_g6.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403

rnd = random.Random(6)
T = Course("onatili", 6, L("Ona tili", "Native language", "Родной язык"))

C1 = "1-chorak. Leksikologiya: so‘z va ma’no"
C2 = "2-chorak. Lug‘at boyligi va so‘z yasalishi"
C3 = "3-chorak. Ot va sifat"
C4 = "4-chorak. Son, olmosh va imlo"


def others(options, right, k=None):
    rest = [o for o in options if o != right]
    return rnd.sample(rest, k) if k is not None and k < len(rest) else rest


# ============================================================ 1-chorak
# ------------------------------------------------------------ lug‘aviy ma’no, bir va ko‘p ma’noli so‘zlar
POLY6 = [("og‘iz", "bolaning og‘zi", "g‘orning og‘zi"), ("oyoq", "odamning oyog‘i", "stolning oyog‘i"),
         ("qanot", "qushning qanoti", "samolyotning qanoti"), ("tish", "bolaning tishi", "arraning tishi"),
         ("etak", "ko‘ylakning etagi", "tog‘ etagi"), ("quloq", "odamning qulog‘i", "qozonning qulog‘i"),
         ("yoqa", "ko‘ylak yoqasi", "daryo yoqasi"), ("burun", "odamning burni", "kemaning burni")]
MONO6 = ["kislorod", "termometr", "perimetr", "fotosintez", "gerb", "diametr"]
items = []
for n, (w, lit, fig) in enumerate(POLY6):
    if n % 2 == 0:
        items.append(Q(f"“{fig}” birikmasida “{w}” so‘zi qanday ma’noda qo‘llangan?", "Ko‘chma ma’noda", ["O‘z ma’nosida", "Antonim sifatida"],
                       d=1, x=f"“{w}” so‘zi o‘xshashlik asosida boshqa narsaga ko‘chgan: {fig}."))
    else:
        items.append(Q(f"“{lit}” birikmasida “{w}” so‘zi qanday ma’noda qo‘llangan?", "O‘z ma’nosida", ["Ko‘chma ma’noda", "Antonim sifatida"],
                       d=2, x=f"{lit} — so‘zning asosiy, dastlabki ma’nosi."))
for n, (w, lit, fig) in enumerate(POLY6[:5]):
    items.append(Q("Qaysi so‘z ko‘p ma’noli?", w, rnd.sample(MONO6, 3), d=1, x=f"{w}: {lit}, {fig} — ma’nolar o‘zaro bog‘liq."))
for m in MONO6[:3]:
    items.append(Q("Qaysi so‘z bir ma’noli?", m, [w for w, _, _ in rnd.sample(POLY6, 3)], d=2, x=f"“{m}” — atama, u faqat bitta ma’noga ega."))
items += [
    Q("Lug‘aviy ma’no nima?", "So‘zning asosiy, atash ma’nosi", ["Qo‘shimchaning ma’nosi", "So‘zning yozilishi", "So‘zdagi tovushlar soni"],
      x="kitob — o‘qish uchun narsa: bu so‘zning lug‘aviy ma’nosi."),
    Q("“kitoblarimizni” so‘zida lug‘aviy ma’noni qaysi qism ifodalaydi?", "kitob", ["-lar", "-imiz", "-ni"], d=2,
      x="Lug‘aviy ma’no o‘zakda, qo‘shimchalar grammatik ma’no beradi."),
    Q("“daraxtlarga” so‘zida ko‘plik ma’nosini qaysi qism beradi?", "-lar", ["daraxt", "-ga", "-la"], d=2, x="-lar — ko‘plik, -ga — jo‘nalish kelishigi."),
    Q("Grammatik ma’no qanday ifodalanadi?", "Asosan qo‘shimchalar orqali", ["Faqat o‘zak orqali", "Sinonimlar orqali", "Tinish belgilari orqali"], d=2,
      x="kitob-lar (ko‘plik), kitob-ni (tushum kelishigi)."),
    Q("So‘zlarning ma’nosini qaysi lug‘atdan bilib olish mumkin?", "Izohli lug‘at", ["Imlo lug‘ati", "Telefon ma’lumotnomasi", "Dars jadvali"],
      x="Izohli lug‘atda so‘zning barcha ma’nolari izohlanadi."),
    TF("Ko‘p ma’noli so‘zning ma’nolari o‘zaro bog‘liq bo‘ladi.", True, d=2, x="qushning qanoti — samolyotning qanoti: shakli o‘xshash."),
    TF("Atamalar odatda bir ma’noli bo‘ladi.", True, d=2, x="kislorod, perimetr — bitta aniq ma’no."),
    TF("“qozonning qulog‘i” birikmasida “quloq” so‘zi o‘z ma’nosida qo‘llangan.", False, x="Bu ko‘chma ma’no: qozonning tutqichi."),
    MATCH("So‘zni uning ko‘chma ma’nosi bilan juftlang",
          [("qanot", "samolyotning qanoti"), ("tish", "arraning tishi"), ("etak", "tog‘ etagi"), ("yoqa", "daryo yoqasi"),
           ("quloq", "qozonning qulog‘i"), ("og‘iz", "g‘orning og‘zi")], d=2),
]
T.topic("word_meaning", "📘", L("So‘zning lug‘aviy ma’nosi. Bir va ko‘p ma’noli so‘zlar", "Word meaning. Polysemy", "Лексическое значение. Многозначность"), C1,
        "So‘zning lug‘aviy ma’nosi — uning asosiy, atash ma’nosi. Qo‘shimchalar grammatik ma’no beradi: kitob-lar (ko‘plik).\n"
        "• Bir ma’noli so‘zlar faqat bitta ma’noga ega; atamalar odatda bir ma’noli: kislorod, perimetr.\n"
        "• Ko‘p ma’noli so‘zlarning ma’nolari o‘zaro bog‘liq: qushning qanoti — samolyotning qanoti.\n"
        "• Asosiy ma’no — o‘z ma’no; o‘xshatish asosida paydo bo‘lgan ma’no — ko‘chma ma’no: stolning oyog‘i.\n"
        "So‘zlarning ma’nolari izohli lug‘atda beriladi.", items=items)

# ------------------------------------------------------------ sinonim va antonim
SYN6 = [("yordam", "ko‘mak", ["xalaqit", "to‘siq", "dam olish"]), ("sovg‘a", "tuhfa", ["qarz", "narx", "savdo"]),
        ("baland", "yuksak", ["past", "pastak", "sayoz"]), ("ulug‘", "buyuk", ["mayda", "kichik", "oddiy"]),
        ("qadimiy", "ko‘hna", ["yangi", "zamonaviy", "hozirgi"]), ("kamtar", "kamsuqum", ["manman", "maqtanchoq", "takabbur"]),
        ("osmon", "samo", ["yer", "tuproq", "dengiz"]), ("inson", "odam", ["hayvon", "qush", "daraxt"]),
        ("chiroyli", "ko‘rkam", ["xunuk", "eski", "kichik"]), ("qayg‘u", "g‘am", ["shodlik", "quvonch", "kulgi"]),
        ("tilak", "istak", ["rad", "inkor", "gina"]), ("tabassum", "jilmayish", ["yig‘i", "xo‘mrayish", "qovoq solish"])]
ANT6 = [("ko‘p", "oz", ["mo‘l", "ancha", "talay"]), ("uzoq", "yaqin", ["olis", "yiroq", "chekka"]),
        ("chuqur", "sayoz", ["teran", "keng", "uzun"]), ("semiz", "ozg‘in", ["to‘la", "katta", "baquvvat"]),
        ("saxiy", "baxil", ["olijanob", "mehribon", "karamli"]), ("foydali", "zararli", ["kerakli", "qimmatli", "muhim"]),
        ("yorqin", "xira", ["porloq", "charaqli", "yaltiroq"]), ("savol", "javob", ["so‘roq", "masala", "topshiriq"]),
        ("boshlanmoq", "tugamoq", ["davom etmoq", "kelmoq", "o‘smoq"]), ("yoqmoq", "o‘chirmoq", ["yondirmoq", "yoritmoq", "qizdirmoq"]),
        ("quyuq", "suyuq", ["qalin", "zich", "og‘ir"]), ("sog‘", "kasal", ["tetik", "baquvvat", "bardam"])]
items = []
for n, (a, b, wrong) in enumerate(SYN6):
    items.append(Q(f"“{a}” so‘ziga ma’nodosh so‘zni tanlang.", b, wrong, d=1 if n < 8 else 2, x=f"{a} — {b}: sinonimlar."))
for n, (a, b, wrong) in enumerate(ANT6):
    items.append(Q(f"“{a}” so‘ziga qarama-qarshi ma’noli so‘zni tanlang.", b, wrong, d=1 if n < 8 else 2, x=f"{a} — {b}: antonimlar."))
items += [
    Q("Qaysi qatorda sinonimlar berilgan?", "yordam, ko‘mak", ["ko‘p, oz", "savol, javob", "tosh, toshloq"], x="yordam va ko‘mak — ma’nodosh."),
    Q("Qaysi qatorda antonimlar berilgan?", "chuqur, sayoz", ["ulug‘, buyuk", "samo, osmon", "gul, guldon"], x="chuqur va sayoz — zid ma’noli."),
    Q("“yuz, bet, chehra, aft” sinonimik qatoridagi bosh so‘z (dominanta) qaysi?", "yuz", ["bet", "chehra", "aft"], d=3,
      x="“yuz” ma’noni betaraf ifodalaydi; chehra — ko‘tarinki, aft — salbiy bo‘yoqli."),
    Q("Antonimlar odatda qaysi jihatdan bir xil bo‘ladi?", "Bir so‘z turkumiga mansub bo‘ladi", ["Bir xil yoziladi", "Ma’nosi bir xil bo‘ladi", "Tovushlari bir xil bo‘ladi"],
      d=3, x="katta — kichik (sifat), kirmoq — chiqmoq (fe’l)."),
    Q("Qaysi gapda antonimlar qo‘llangan?", "Yaxshidan ot qoladi, yomondan dod qoladi.",
      ["Hunar — hunardan unar.", "Ona yurting — oltin beshiging.", "Kitob — bilim manbai."], d=3,
      x="yaxshi — yomon: zid ma’noli so‘zlar."),
    TF("Sinonimlar nutqda bir so‘zni takrorlamaslikka yordam beradi.", True, x="yordam — ko‘mak, sovg‘a — tuhfa."),
    TF("“ko‘p” va “oz” — sinonimlar.", False, x="Ular antonimlar."),
    MATCH("Sinonimlarni juftlang", [(a, b) for a, b, _ in SYN6[:7]], d=2),
    MATCH("Antonimlarni juftlang", [(a, b) for a, b, _ in ANT6[:7]], d=2),
]
T.topic("syn_ant", "🤝", L("Ma’nodosh va qarama-qarshi ma’noli so‘zlar", "Synonyms and antonyms", "Синонимы и антонимы"), C1,
        "• Ma’nodosh (sinonim) so‘zlar — ma’nosi bir xil yoki yaqin so‘zlar: yordam — ko‘mak, sovg‘a — tuhfa.\n"
        "  Sinonimik qatorda ma’noni betaraf ifodalaydigan bosh so‘z bo‘ladi: yuz — bet — chehra — aft (bosh so‘z: yuz).\n"
        "• Qarama-qarshi ma’noli (antonim) so‘zlar: ko‘p — oz, chuqur — sayoz, yoqmoq — o‘chirmoq.\n"
        "  Antonimlar bir so‘z turkumiga mansub bo‘ladi.\n"
        "Sinonim va antonimlar nutqni boy va ta’sirli qiladi.", items=items)

# ------------------------------------------------------------ omonimlar
HOM6 = [
    ("bog‘", "Bog‘da olmalar pishdi.", "Arqonni mahkam bog‘.", "meva daraxtlari o‘sadigan joy", "bog‘lamoq (harakat)"),
    ("kir", "Ko‘ylakdagi kir yaxshi ketdi.", "Xonaga sekin kir.", "iflos dog‘", "kirmoq (harakat)"),
    ("chang", "Javon ustida chang to‘planibdi.", "Chang — torli cholg‘u asbobi.", "mayda tuproq zarralari", "cholg‘u asbobi"),
    ("ter", "Yugurganda peshonamdan ter oqdi.", "Bog‘dan gilos ter.", "tanadan chiqadigan suyuqlik", "termoq (harakat)"),
    ("yosh", "Ukam hali yosh.", "Uning ko‘zidan yosh oqdi.", "kam yashagan", "ko‘z yoshi"),
    ("tor", "Bu ko‘cha juda tor.", "Dutorning bir tori uzildi.", "keng emas", "cholg‘u asbobining simi"),
    ("qirq", "Bobom maktabda qirq yil ishlagan.", "Qog‘ozni qaychi bilan qirq.", "son (40)", "qirqmoq (harakat)"),
    ("suz", "Hovuzda ehtiyot bo‘lib suz.", "Oshni likopchalarga suz.", "suvda harakatlanmoq", "ovqatni idishga olmoq"),
]
all_meanings = [m for h in HOM6 for m in h[3:]]
items = []
for n, (w, s1, s2, m1, m2) in enumerate(HOM6):
    third = "Ko‘p ma’noli so‘z" if w in ("bog‘", "kir", "chang", "ter", "qirq") else "Iboralar"
    items.append(Q(f"“{s1}” va “{s2}” gaplaridagi “{w}” so‘zlari qanday so‘zlar?", "Omonimlar", ["Sinonimlar", "Antonimlar", third],
                   d=1 if n < 4 else 2, x=f"Yozilishi bir xil, ma’nolari bog‘liq emas: {m1} va {m2}."))
for n, (w, s1, s2, m1, m2) in enumerate(HOM6):
    for k, (s, m, other) in enumerate([(s1, m1, m2), (s2, m2, m1)]):
        wrong = [other] + rnd.sample([x for x in all_meanings if x not in (m1, m2)], 2)
        items.append(Q(f"“{s}” gapidagi “{w}” so‘zi qaysi ma’noda?", m, wrong, d=1 if k == 0 else 2, x=f"Bu gapda “{w}” — {m}."))
items += [
    Q("“qushning qanoti” va “samolyotning qanoti” — bu qaysi hodisa?", "Ko‘p ma’nolilik", ["Omonimlik", "Sinonimlik", "Antonimlik"], d=3,
      x="Ma’nolar o‘xshashlik asosida bog‘langan, demak bu bitta ko‘p ma’noli so‘z."),
    Q("“arraning tishi” va “bolaning tishi” — bu qaysi hodisa?", "Ko‘p ma’nolilik", ["Omonimlik", "Sinonimlik", "Antonimlik"], d=3,
      x="Arraning tishi odam tishiga o‘xshatib nomlangan."),
    Q("“chang” (tuproq zarrasi) va “chang” (cholg‘u asbobi) — bu qaysi hodisa?", "Omonimlik", ["Ko‘p ma’nolilik", "Sinonimlik", "Antonimlik"], d=3,
      x="Ma’nolar o‘zaro bog‘liq emas — omonimlar."),
    TF("Shakldosh so‘zlar omonimlar deb ataladi.", True, x="bog‘ (joy) — bog‘ (harakat)."),
    TF("Omonimlar yozilishi jihatidan farq qiladi.", False, x="Omonimlarning yozilishi va aytilishi bir xil."),
    TF("Omonimlarning ma’nolari o‘zaro bog‘liq emas.", True, d=2, x="Bog‘liq bo‘lsa, bu ko‘p ma’noli so‘z bo‘ladi."),
    ORDER("So‘zlardan gap tuzing", "Ukam bog‘dan qizil gilos terdi", d=1),
]
T.topic("homonyms", "🎭", L("Shakldosh so‘zlar (omonimlar)", "Homonyms", "Омонимы"), C1,
        "Shakldosh (omonim) so‘zlar — aytilishi va yozilishi bir xil, ma’nolari bir-biriga bog‘liq bo‘lmagan so‘zlar:\n"
        "• bog‘ (meva daraxtlari o‘sadigan joy) — bog‘ (arqonni bog‘);\n"
        "• chang (tuproq zarrasi) — chang (cholg‘u asbobi); yosh (kam yashagan) — yosh (ko‘z yoshi).\n"
        "Ko‘p ma’noli so‘zdan farqi: ko‘p ma’noli so‘zning ma’nolari bog‘liq (qushning qanoti — samolyotning qanoti),\n"
        "omonimlarning ma’nolari esa bog‘liq emas.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["word_meaning", "syn_ant", "homonyms"], C1)

# ============================================================ 2-chorak
# ------------------------------------------------------------ eskirgan so‘zlar, neologizmlar, atamalar
OLD6 = [("mudarris", "madrasa o‘qituvchisi"), ("noma", "xat, maktub"), ("karvonsaroy", "karvonlar tunaydigan joy"),
        ("munshiy", "kotib, xat yozuvchi"), ("misqol", "og‘irlik o‘lchovi"), ("o‘rda", "xon saroyi, qarorgohi")]
MODERN = ["kompyuter", "o‘qituvchi", "avtobus", "telefon", "shifokor", "kutubxona"]
NEO6 = ["dron", "bloger", "onlayn", "noutbuk"]
TERMS6 = [("perimetr", "Matematika"), ("ekvator", "Geografiya"), ("undalma", "Ona tili"), ("xlorofill", "Biologiya"),
          ("diametr", "Matematika"), ("materik", "Geografiya"), ("omonim", "Ona tili"), ("bakteriya", "Biologiya"),
          ("ko‘paytma", "Matematika"), ("vulqon", "Geografiya"), ("fonetika", "Ona tili"), ("changlanish", "Biologiya")]
FIELDS = ["Matematika", "Geografiya", "Ona tili", "Biologiya"]
items = []
for n, (w, m) in enumerate(OLD6):
    items.append(Q(f"Tarixiy asarlarda uchraydigan “{w}” so‘zi nimani bildiradi?", m, others([mm for _, mm in OLD6], m, 3), d=1 if n < 3 else 2,
                   x=f"{w} — {m}. Bu so‘z hozir kam ishlatiladi."))
for w, _ in OLD6[:3]:
    items.append(Q("Qaysi so‘z eskirgan so‘z?", w, rnd.sample(MODERN, 3), x=f"“{w}” hozirgi nutqda deyarli ishlatilmaydi."))
for w in NEO6:
    items.append(Q("Qaysi so‘z yaqinda paydo bo‘lgan yangi so‘z (neologizm)?", w, [o for o, _ in rnd.sample(OLD6, 3)],
                   x=f"“{w}” — yangi narsa yoki tushuncha bilan birga tilga kirgan so‘z."))
for n, (t, f) in enumerate(TERMS6):
    items.append(Q(f"“{t}” atamasi qaysi fanga tegishli?", f, others(FIELDS, f), d=1 if n < 8 else 2, x=f"{t} — {f.lower()} atamasi."))
items += [
    Q("Neologizm nima?", "Yangi paydo bo‘lgan so‘z", ["Eskirgan so‘z", "Fan atamasi", "Ma’nodosh so‘z"], x="dron, bloger — neologizmlar."),
    Q("Eskirgan so‘zlar ko‘proq qayerda uchraydi?", "Tarixiy asarlarda", ["Kompyuter o‘yinlarida", "Matematika masalalarida", "Kundalik so‘zlashuvda"],
      x="Tarixiy asarlarda o‘sha davr hayoti tasvirlanadi."),
    Q("Atama nima?", "Fan yoki kasbga oid so‘z", ["Eskirgan so‘z", "Ko‘chma ma’noli so‘z", "Ibora"], x="perimetr, ekvator, undalma — atamalar."),
    TF("Vaqt o‘tishi bilan neologizm hammaga tanish oddiy so‘zga aylanishi mumkin.", True, d=3,
       x="Bir paytlar yangi bo‘lgan “televizor” so‘zi hozir hammaga tanish."),
    TF("“karvonsaroy” — yangi paydo bo‘lgan so‘z.", False, x="karvonsaroy — eskirgan, tarixiy so‘z."),
    MATCH("Tushunchani izohi bilan juftlang",
          [("Sinonim", "ma’nodosh so‘z"), ("Antonim", "zid ma’noli so‘z"), ("Omonim", "shakldosh so‘z"), ("Neologizm", "yangi so‘z"),
           ("Atama", "fan yoki kasb so‘zi")], d=2),
]
T.topic("vocab_layers", "🏺", L("Eskirgan so‘zlar, neologizmlar va atamalar", "Archaic words, neologisms, terms", "Устаревшие слова, неологизмы, термины"), C2,
        "• Eskirgan so‘zlar — hozir kam ishlatiladigan, tarixiy asarlarda uchraydigan so‘zlar: mudarris, munshiy, karvonsaroy, misqol.\n"
        "• Neologizmlar — yangi narsa va tushunchalar bilan birga paydo bo‘lgan so‘zlar: dron, bloger, onlayn.\n"
        "  Vaqt o‘tib ular hammaga tanish oddiy so‘zga aylanadi.\n"
        "• Atamalar — fan, texnika va kasbga oid so‘zlar: perimetr (matematika), ekvator (geografiya), undalma (ona tili).", items=items)

# ------------------------------------------------------------ iboralar (frazeologizmlar)
IDI6 = [
    ("qo‘l qovushtirib o‘tirmoq", "hech ish qilmay o‘tirmoq", ["tez ishlamoq", "qo‘lini yuvmoq", "salomlashmoq"]),
    ("ko‘z qorachig‘idek asramoq", "juda ehtiyot qilib saqlamoq", ["tez yo‘qotmoq", "ko‘zini yummoq", "e’tibor bermaslik"]),
    ("yer bilan osmoncha farq", "juda katta farq", ["hech qanday farq yo‘q", "kichik farq", "bir xil"]),
    ("ko‘ngli joyiga tushmoq", "tinchlanmoq, xotirjam bo‘lmoq", ["xafa bo‘lmoq", "qo‘rqib ketmoq", "kasal bo‘lmoq"]),
    ("boshi qotmoq", "nima qilishini bilmay qolmoq", ["boshi og‘rimoq", "uxlab qolmoq", "xursand bo‘lmoq"]),
    ("qo‘li gul", "hunarmand, mohir", ["dangasa", "gul sotuvchi", "baxil"]),
    ("tilidan bol tomadi", "shirinso‘z", ["qo‘pol", "kamgap", "yolg‘onchi"]),
    ("ignaning ustida o‘tirgandek", "betoqat, bezovta", ["xotirjam", "quvnoq", "charchagan"]),
    ("qulog‘ini ding qilmoq", "diqqat bilan tinglamoq", ["quloq solmaslik", "qichqirmoq", "uxlab qolmoq"]),
    ("suv sepgandek jim bo‘lmoq", "birdan jimib qolmoq", ["baqirib yubormoq", "gul sug‘ormoq", "kulib yubormoq"]),
    ("qosh qo‘yaman deb ko‘z chiqarmoq", "yaxshilik qilaman deb ishni buzmoq", ["chiroyli bezamoq", "yordam bermoq", "ishni tez bitirmoq"]),
    ("bosh qo‘shmoq", "birlashib ish qilmoq", ["urishib qolmoq", "boshini egmoq", "yolg‘iz ishlamoq"]),
    ("ter to‘kmoq", "qattiq mehnat qilmoq", ["dam olmoq", "yuvinmoq", "kasal bo‘lmoq"]),
    ("og‘ziga talqon solmoq", "jim bo‘lmoq, gapirmaslik", ["ko‘p gapirmoq", "ovqatlanmoq", "kulmoq"]),
    ("kapalagi uchib ketmoq", "qattiq qo‘rqib ketmoq", ["xursand bo‘lmoq", "kapalak tutmoq", "shoshilmoq"]),
    ("ko‘kka ko‘tarmoq", "haddan tashqari maqtamoq", ["yerga tashlamoq", "koyimoq", "uchirmoq"]),
    ("chumchuq pir etsa, yuragi shir etadi", "juda qo‘rqoq", ["juda botir", "juda quvnoq", "juda dangasa"]),
]
items = []
for n, (idiom, meaning, wrong) in enumerate(IDI6):
    items.append(Q(f"“{idiom}” iborasi nimani anglatadi?", meaning, wrong, d=1 if n < 9 else 2, x=f"“{idiom}” — {meaning}."))
for k, wrong_k in [(12, (1, 2, 6)), (13, (12, 1, 7)), (5, (8, 13, 1)), (15, (14, 7, 12))]:
    idiom, meaning, _ = IDI6[k]
    items.append(Q(f"Qaysi ibora “{meaning}” ma’nosini bildiradi?", idiom, [IDI6[j][0] for j in wrong_k], d=2, x=f"“{idiom}” — {meaning}."))
items += [
    Q("Qaysi gapda ibora qo‘llangan?", "Dars boshlanishi bilan sinf suv sepgandek jim bo‘ldi.",
      ["Dars boshlanishi bilan sinf jim bo‘ldi.", "Navbatchi gulga suv sepdi.", "Sinfda o‘quvchilar jim o‘tirishdi."], d=2,
      x="suv sepgandek jim bo‘lmoq — birdan jimib qolmoq."),
    Q("Qaysi gapda ibora qo‘llangan?", "Bobom bu bog‘ni yaratish uchun ko‘p ter to‘kkan.",
      ["Bobom issiqda terlab ketdi.", "Bobom bog‘da olma terdi.", "Bobom bog‘ni sug‘ordi."], d=2, x="ter to‘kmoq — qattiq mehnat qilmoq."),
    Q("“kapalagi uchib ketmoq” iborasini qaysi so‘z bilan almashtirish mumkin?", "qo‘rqmoq", ["quvonmoq", "uchmoq", "yugurmoq"], d=2,
      x="Iboraning ma’nosini bitta so‘z bilan berish mumkin."),
    TF("Iboradagi so‘zlarni boshqa so‘z bilan almashtirib bo‘lmaydi.", True, d=2, x="“ter to‘kmoq” o‘rniga “suv to‘kmoq” deyilmaydi."),
    TF("Iboralar faqat o‘z ma’nosida qo‘llanadi.", False, x="Iboralar bir butun ko‘chma ma’no bildiradi."),
    MATCH("Iborani ma’nosi bilan juftlang", [(i, m) for i, m, _ in IDI6[:7]], d=2),
]
T.topic("idioms", "🗣️", L("Iboralar (frazeologizmlar)", "Idioms", "Фразеологизмы"), C2,
        "Ibora (frazeologizm) — ikki yoki undan ortiq so‘zdan tuzilgan, bir butun ko‘chma ma’no bildiradigan turg‘un birikma.\n"
        "• Iboradagi so‘zlarni boshqasiga almashtirib bo‘lmaydi: ter to‘kmoq — qattiq mehnat qilmoq.\n"
        "• Ko‘p iboralarni bitta so‘z bilan almashtirish mumkin: kapalagi uchib ketmoq — qo‘rqmoq.\n"
        "Misollar: qo‘li gul — mohir; tilidan bol tomadi — shirinso‘z; yer bilan osmoncha farq — juda katta farq.", items=items)

# ------------------------------------------------------------ qo‘shma so‘zlar
COMP6 = [("toshbaqa", ["toshloq", "toshli", "toshlar"]), ("belbog‘", ["bog‘bon", "bog‘cha", "bog‘lar"]),
         ("qo‘ziqorin", ["qo‘zichoq", "qo‘zilar", "qo‘zini"]), ("tog‘olcha", ["tog‘li", "tog‘lar", "olchazor"]),
         ("oqsoqol", ["soqolli", "oqish", "soqollar"]), ("kungaboqar", ["kunduzi", "kunlar", "kunlik"]),
         ("qo‘lqop", ["qo‘llar", "qo‘lcha", "qo‘lda"]), ("yerto‘la", ["yerli", "yerlar", "yerda"]),
         ("kamgap", ["gapdon", "gaplar", "gapirdi"])]
items = []
for n, (w, wrong) in enumerate(COMP6):
    items.append(Q("Qaysi so‘z qo‘shma so‘z?", w, wrong, d=1 if n < 7 else 2, x=f"“{w}” ikki o‘zakdan tuzilgan va bitta yangi narsani nomlaydi."))
for w, right, wrong in [("oshqozon", "ovqat hazm qiluvchi a’zo", ["osh pishiradigan qozon", "oshxona idishi", "katta qozon"]),
                        ("toshbaqa", "sudralib yuruvchi hayvon", ["toshdagi baqa", "tosh turi", "baqaning uyi"]),
                        ("qo‘ziqorin", "zamburug‘", ["qo‘zining qorni", "qo‘zi go‘shti", "o‘t-o‘lan"])]:
    items.append(Q(f"“{w}” qo‘shma so‘zi nimani bildiradi?", right, wrong, d=2, x=f"Qo‘shma so‘z yangi yaxlit ma’no bildiradi: {w} — {right}."))
for right, wrong in [("kungaboqar", ["kun gaboqar", "kun-gaboqar", "kunga-boqar"]), ("belbog‘", ["bel bog‘", "bel-bog‘"]),
                     ("qo‘ziqorin", ["qo‘zi qorin", "qo‘zi-qorin"]), ("tog‘olcha", ["tog‘ olcha", "tog‘-olcha"])]:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong, d=2, x=f"Qo‘shma otlar qo‘shib yoziladi: {right}."))
for right, wrong in [("sotib oldi", ["sotiboldi", "sotib-oldi"]), ("olib keldi", ["olibkeldi", "olib-keldi"]),
                     ("yordam berdi", ["yordamberdi", "yordam-berdi"])]:
    items.append(Q("Qaysi yozuv to‘g‘ri?", right, wrong, d=2, x=f"Qo‘shma fe’llar ajratib yoziladi: {right}."))
items += [
    Q("Qo‘shma so‘z nima?", "Ikki va undan ortiq o‘zakdan tuzilgan so‘z", ["O‘zak va qo‘shimchadan tuzilgan so‘z", "Takrorlangan so‘z", "Eskirgan so‘z"],
      x="tosh + baqa = toshbaqa."),
    Q("Qo‘shma otlar qanday yoziladi?", "Qo‘shib", ["Ajratib", "Chiziqcha bilan", "Qo‘shtirnoqda"], x="toshbaqa, belbog‘, qo‘ziqorin."),
    TF("“toshbaqa” so‘zi ikki o‘zakdan tuzilgan.", True, x="tosh + baqa."),
    TF("Qo‘shma so‘z yaxlit bitta yangi ma’noni bildiradi.", True, d=2, x="oshqozon — osh ham, qozon ham emas, balki a’zo."),
    TF("“sotib olmoq” qo‘shib yoziladi.", False, d=2, x="Qo‘shma fe’llar ajratib yoziladi: sotib olmoq."),
    MATCH("Qo‘shma so‘zni ma’nosi bilan juftlang",
          [("toshbaqa", "hayvon"), ("qo‘ziqorin", "zamburug‘"), ("kungaboqar", "o‘simlik"), ("qo‘lqop", "qo‘lga kiyiladigan buyum"),
           ("oqsoqol", "keksa, hurmatli kishi"), ("yerto‘la", "yer ostidagi xona")], d=2),
]
T.topic("compound_words", "🔗", L("Qo‘shma so‘zlar va ularning imlosi", "Compound words", "Сложные слова"), C2,
        "Qo‘shma so‘z — ikki yoki undan ortiq o‘zakdan tuzilgan, bitta yangi ma’no bildiradigan so‘z:\n"
        "tosh + baqa = toshbaqa (hayvon), osh + qozon = oshqozon (a’zo), kungaboqar (o‘simlik).\n"
        "• Qo‘shma otlar qo‘shib yoziladi: belbog‘, qo‘ziqorin, tog‘olcha.\n"
        "• Qo‘shma fe’llar ajratib yoziladi: sotib olmoq, olib kelmoq, yordam bermoq.\n"
        "• Qo‘shma sonlar ham ajratib yoziladi: o‘n besh, yuz yigirma.", items=items)

# ------------------------------------------------------------ juft va takroriy so‘zlar
PAIRS6 = ["ota-ona", "kecha-kunduz", "qozon-tovoq", "kiyim-kechak", "baxt-saodat", "yaxshi-yomon", "opa-singil"]
REPEAT6 = ["katta-katta", "sekin-sekin", "oz-oz", "bitta-bitta", "qator-qator", "asta-asta"]
DERIV = ["ishchi", "gulzor", "tuzsiz", "kitobxon", "mehnatkash", "do‘stlik", "suvli"]
COMPOUNDS = ["toshbaqa", "belbog‘", "kungaboqar", "qo‘ziqorin", "tog‘olcha", "oqsoqol", "qo‘lqop"]
KIND3 = ["Juft so‘z", "Takroriy so‘z", "Qo‘shma so‘z", "Tub so‘z"]
items = []
for n, w in enumerate(PAIRS6[:6]):
    items.append(Q("Qaysi so‘z juft so‘z?", w, [REPEAT6[n], COMPOUNDS[n], DERIV[n]], d=1,
                   x=f"“{w}” — ikki xil so‘zning juftlashuvi, chiziqcha bilan yoziladi."))
for n, w in enumerate(REPEAT6[:5]):
    items.append(Q("Qaysi so‘z takroriy so‘z?", w, [PAIRS6[n], PAIRS6[n + 1], COMPOUNDS[n]], d=1,
                   x=f"“{w}” — bir so‘zning takrorlanishi."))
for right, wrong in [("ota-ona", ["otaona", "ota ona"]), ("kiyim-kechak", ["kiyimkechak", "kiyim kechak"]), ("oz-oz", ["ozoz", "oz oz"]),
                     ("qozon-tovoq", ["qozontovoq", "qozon tovoq"])]:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong, d=1 if right == "ota-ona" else 2,
                   x=f"Juft va takroriy so‘zlar chiziqcha bilan yoziladi: {right}."))
for w, rel in [("yaxshi-yomon", "Zid ma’noli so‘zlardan"), ("o‘y-xayol", "Ma’nodosh so‘zlardan"), ("kecha-kunduz", "Zid ma’noli so‘zlardan"),
               ("baxt-saodat", "Ma’nodosh so‘zlardan"), ("katta-kichik", "Zid ma’noli so‘zlardan")]:
    wrong = [r for r in ("Zid ma’noli so‘zlardan", "Ma’nodosh so‘zlardan") if r != rel] + ["Bir so‘zning takroridan", "O‘zak va qo‘shimchadan"]
    items.append(Q(f"“{w}” juft so‘zi qanday qismlardan tuzilgan?", rel, wrong, d=2, x=f"{w.replace('-', ' va ')} — {rel.lower().replace('lardan', 'lar')}."))
for w, k in [("idish-tovoq", 0), ("qator-qator", 1), ("kungaboqar", 2), ("uy-joy", 0), ("asta-asta", 1), ("qo‘lqop", 2)]:
    items.append(Q(f"“{w}” — qanday so‘z?", KIND3[k], others(KIND3, KIND3[k]), d=2,
                   x=["Ikki xil so‘z juftlashgan, chiziqcha bilan yoziladi.", "Bir so‘z takrorlangan, chiziqcha bilan yoziladi.",
                      "Ikki o‘zak qo‘shilib, qo‘shib yoziladi."][k]))
items += [
    Q("Takroriy so‘z qanday hosil bo‘ladi?", "Bir so‘zni takrorlash bilan", ["Ikki xil so‘zni juftlash bilan", "Qo‘shimcha qo‘shish bilan", "So‘zni qisqartirish bilan"],
      x="sekin-sekin, qator-qator."),
    Q("Juft so‘z qanday hosil bo‘ladi?", "Ikki xil so‘zni juftlash bilan", ["Bir so‘zni takrorlash bilan", "O‘zakka qo‘shimcha qo‘shish bilan", "So‘zni qisqartirish bilan"],
      x="ota-ona, kecha-kunduz."),
    TF("Juft so‘zlar chiziqcha bilan yoziladi.", True, x="ota-ona, opa-singil."),
    TF("Takroriy so‘zlar qo‘shib yoziladi.", False, x="Takroriy so‘zlar chiziqcha bilan yoziladi: katta-katta."),
    TF("“kiyim-kechak” juft so‘zining ikkinchi qismi alohida qo‘llanmaydi.", True, d=3, x="“kechak” so‘zi yolg‘iz ishlatilmaydi."),
    MATCH("Juft so‘z qismlarini juftlang", [("ota", "ona"), ("aka", "uka"), ("opa", "singil"), ("qozon", "tovoq"), ("kiyim", "kechak"), ("kecha", "kunduz")], d=2),
    ORDER("So‘zlardan gap tuzing", "Bolalar qator-qator bo‘lib saf tortishdi", d=2),
]
T.topic("pair_words", "👯", L("Juft va takroriy so‘zlar", "Paired and repeated words", "Парные и повторные слова"), C2,
        "• Juft so‘zlar ikki xil so‘zning juftlashuvidan hosil bo‘ladi va chiziqcha bilan yoziladi: ota-ona, kecha-kunduz, baxt-saodat.\n"
        "  Qismlari ma’nodosh (o‘y-xayol), zid ma’noli (yaxshi-yomon) yoki ma’nosi yaqin (qozon-tovoq) bo‘ladi;\n"
        "  ba’zan bir qismi alohida ishlatilmaydi: kiyim-kechak.\n"
        "• Takroriy so‘zlar bir so‘zning takrorlanishidan hosil bo‘ladi va ular ham chiziqcha bilan yoziladi:\n"
        "  katta-katta, sekin-sekin, qator-qator.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["vocab_layers", "idioms", "compound_words", "pair_words"], C2)

# ============================================================ 3-chorak
# ------------------------------------------------------------ otning ma’noviy turlari
CONCRETE = ["kitob", "daraxt", "tosh", "stol", "olma", "qalam", "non", "ko‘prik"]
ABSTRACT = ["baxt", "do‘stlik", "sevinch", "bilim", "mehr", "orzu", "sabr", "hurmat"]
COLLECTIVE = ["xalq", "poda", "suruv", "gala", "olomon", "jamoa"]
SINGLE = ["qo‘y", "sigir", "qush", "odam", "o‘yinchi", "talaba"]
NT = ["Aniq ot", "Mavhum ot", "Jamlovchi ot"]
items = []
for w in ABSTRACT[:6]:
    items.append(Q("Qaysi ot mavhum ot?", w, rnd.sample(CONCRETE, 3), x=f"“{w}” — his-tuyg‘u yoki tushuncha nomi, uni ushlab bo‘lmaydi."))
for w in CONCRETE[:4]:
    items.append(Q("Qaysi ot aniq ot?", w, rnd.sample(ABSTRACT, 3), x=f"“{w}” — ko‘rish va ushlash mumkin bo‘lgan narsa."))
for w, k in [("sevinch", 1), ("ko‘prik", 0), ("sabr", 1), ("qalam", 0), ("hurmat", 1), ("non", 0)]:
    items.append(Q(f"“{w}” — qanday ot?", NT[k], others(NT, NT[k]), d=2, x=["Aniq ot — ko‘rish mumkin bo‘lgan narsa nomi.", "Mavhum ot — tushuncha yoki his nomi."][k]))
for w in COLLECTIVE[:5]:
    items.append(Q("Qaysi ot jamlovchi ot?", w, rnd.sample(SINGLE, 3), x=f"“{w}” — bir turdagi narsalar to‘plamini bildiradi."))
for q, right, wrong in [("Qushlar to‘dasi qanday ataladi?", "gala", ["suruv", "poda", "olomon"]),
                        ("Sigirlar to‘dasi qanday ataladi?", "poda", ["gala", "olomon", "jamoa"]),
                        ("Qo‘ylar to‘dasi qanday ataladi?", "suruv", ["gala", "olomon", "jamoa"]),
                        ("Bir joyga to‘plangan ko‘p odamlar qanday ataladi?", "olomon", ["gala", "suruv", "poda"])]:
    items.append(Q(q, right, wrong, d=2, x=f"{right} — jamlovchi ot."))
items += [
    Q("Mavhum otlar nimani bildiradi?", "His-tuyg‘u va tushunchani", ["Ko‘rish mumkin bo‘lgan narsani", "Narsaning rangini", "Harakatni"],
      x="baxt, do‘stlik, bilim."),
    Q("Jamlovchi ot nimani bildiradi?", "Bir turdagi narsalar to‘plamini", ["Bitta narsani", "Harakatni", "Belgini"], x="gala — qushlar to‘dasi."),
    TF("“do‘stlik” — mavhum ot.", True, x="Do‘stlikni ko‘rib yoki ushlab bo‘lmaydi, u tushuncha."),
    TF("“daraxt” — mavhum ot.", False, x="daraxt — aniq ot."),
    TF("“xalq” so‘zi ko‘p kishilarni bildiradi, u jamlovchi ot.", True, d=2, x="xalq, jamoa, olomon — jamlovchi otlar."),
    TF("Jamlovchi otlar birlik shaklida ham to‘plamni bildiradi.", True, d=3, x="suruv — bitta so‘z, lekin ko‘p qo‘y."),
    MATCH("Yakka otni jamlovchi ot bilan juftlang", [("qo‘y", "suruv"), ("sigir", "poda"), ("qush", "gala"), ("o‘yinchi", "jamoa"), ("odam", "olomon")], d=2),
]
T.topic("noun_meaning", "📦", L("Otning ma’noviy turlari", "Types of nouns by meaning", "Разряды существительных"), C3,
        "Otlar ma’nosiga ko‘ra turlarga bo‘linadi:\n"
        "• Aniq otlar — ko‘rish, ushlash mumkin bo‘lgan narsalar: kitob, daraxt, tosh.\n"
        "• Mavhum otlar — his-tuyg‘u va tushuncha nomlari: baxt, do‘stlik, bilim, orzu.\n"
        "• Yakka otlar — bitta narsani bildiradi: qo‘y, qush, o‘yinchi.\n"
        "• Jamlovchi otlar — bir turdagi narsalar to‘plamini bildiradi: suruv, gala, jamoa, xalq.", items=items)

# ------------------------------------------------------------ asliy va nisbiy sifatlar
ASLIY = ["oq", "qizil", "katta", "shirin", "achchiq", "baland", "keng", "yumshoq"]
NISBIY = ["kuzgi", "qishki", "tungi", "kechagi", "bugungi", "ichki", "tashqi", "tarixiy"]
AT = ["Asliy sifat", "Nisbiy sifat"]
items = []
for n, (a, b) in enumerate(zip(ASLIY, NISBIY)):
    items.append(Q(f"“{a}” — qanday sifat?", AT[0], [AT[1], "Sifat emas"], d=1 if n < 4 else 2, x="Asliy sifat belgini bevosita bildiradi."))
    items.append(Q(f"“{b}” — qanday sifat?", AT[1], [AT[0], "Sifat emas"], d=1 if n < 4 else 2, x="Nisbiy sifat belgini vaqt, o‘rin yoki narsaga nisbatan bildiradi."))
for w in NISBIY[:4]:
    items.append(Q("Qaysi sifat nisbiy sifat?", w, rnd.sample(ASLIY, 3), x=f"“{w}” — boshqa narsaga nisbatan belgi."))
for w in ASLIY[:3]:
    items.append(Q("Qaysi sifat asliy sifat?", w, rnd.sample(NISBIY, 3), x=f"“{w}” belgini bevosita bildiradi."))
items += [
    Q("Qaysi sifatdan qiyosiy daraja yasash mumkin?", "shirin", ["kuzgi", "kechagi", "tarixiy"], d=2, x="shirinroq — deyiladi, “kuzgiroq” deyilmaydi."),
    Q("Nisbiy sifat belgini qanday bildiradi?", "Boshqa narsaga nisbatan", ["Rang va mazani bevosita", "Harakatning belgisi sifatida", "Narsaning soni orqali"], d=2,
      x="kuzgi kiyim — kuzga oid kiyim."),
    Q("“tarixiy obida” birikmasidagi sifat qaysi so‘zdan yasalgan?", "tarix", ["obida", "tarixchi", "tariq"], d=2, x="tarix + iy = tarixiy."),
    Q("“qishki kiyim” birikmasidagi sifat qaysi so‘zdan yasalgan?", "qish", ["qishloq", "kiyim", "qishki"], d=2, x="qish + ki = qishki."),
    TF("Asliy sifatlar belgini bevosita bildiradi: oq, shirin, katta.", True, x="Ular darajalanadi: oqroq, eng shirin."),
    TF("Nisbiy sifatlar ko‘pincha ot yoki ravishdan yasaladi: kuz — kuzgi.", True, d=2, x="kecha — kechagi, tarix — tarixiy."),
    TF("“kuzgiroq” — to‘g‘ri shakl.", False, d=2, x="Nisbiy sifatlar odatda daraja qo‘shimchasini olmaydi."),
    MATCH("Nisbiy sifatni u yasalgan so‘z bilan juftlang",
          [("kuzgi", "kuz"), ("tungi", "tun"), ("kechagi", "kecha"), ("tarixiy", "tarix"), ("ilmiy", "ilm")], d=2),
]
T.topic("adj_types", "🎨", L("Asliy va nisbiy sifatlar", "Qualitative and relative adjectives", "Качественные и относительные прилагательные"), C3,
        "Sifatlar ma’nosiga ko‘ra ikki turga bo‘linadi:\n"
        "• Asliy sifatlar belgini bevosita bildiradi: oq, shirin, katta, keng. Ular darajalanadi: oqroq, eng shirin.\n"
        "• Nisbiy sifatlar belgini boshqa narsaga (vaqt, o‘rin, tushuncha) nisbatan bildiradi: kuzgi (kuz), tashqi, tarixiy (tarix).\n"
        "  Ular odatda ot yoki ravishdan yasaladi va daraja qo‘shimchasini olmaydi: “kuzgiroq” deyilmaydi.", items=items)

# ------------------------------------------------------------ sifat yasovchi qo‘shimchalar
SUF6 = [("bilimli", "-li"), ("tinimsiz", "-siz"), ("talabchan", "-chan"), ("guldor", "-dor"), ("bahorgi", "-gi"),
        ("iste’dodli", "-li"), ("chegarasiz", "-siz"), ("ta’sirchan", "-chan"), ("mevador", "-dor"), ("tungi", "-gi"),
        ("mazali", "-li"), ("shovqinsiz", "-siz"), ("uyatchan", "-chan"), ("hosildor", "-dor"), ("hozirgi", "-gi"),
        ("quvvatli", "-li"), ("hidsiz", "-siz"), ("vafodor", "-dor")]
SUFS = ["-li", "-siz", "-chan", "-dor", "-gi"]
items = []
for n, (w, s) in enumerate(SUF6):
    items.append(Q(f"“{w}” sifatini qaysi qo‘shimcha yasagan?", s, others(SUFS, s, 3), d=1 if n < 10 else 2, x=f"{w[:len(w) - len(s) + 1]} + {s[1:]} = {w}."))
items += [
    Q("“-siz” qo‘shimchasi qanday ma’no beradi?", "Belgining yo‘qligini", ["Belgining ko‘pligini", "Harakatni", "Joyni"], x="hidsiz — hidi yo‘q."),
    Q("“-li” qo‘shimchasi qanday ma’no beradi?", "Belgi borligini", ["Belgining yo‘qligini", "Kasbni", "Idishni"], x="bilimli — bilimi bor."),
    Q("“-chan” qo‘shimchasi qanday ma’no beradi?", "Biror xususiyatga moyillikni", ["Belgining yo‘qligini", "Joyni", "Idishni"], d=2,
      x="uyatchan — tez uyaladigan, talabchan — talab qo‘yishni yaxshi ko‘radigan."),
    Q("“odobli” so‘zining -siz qo‘shimchali antonimi qaysi?", "odobsiz", ["odobchan", "odobdor", "odobgi"], d=2, x="odobli — odobsiz."),
    Q("“bilimli” so‘zining -siz qo‘shimchali antonimi qaysi?", "bilimsiz", ["bilimchan", "bilimgi", "bilimlar"], d=2, x="bilimli — bilimsiz."),
    Q("Qaysi sifat -dor qo‘shimchasi bilan yasalgan?", "guldor", ["gulli", "gulsiz", "gulchi"], x="gul + dor = guldor (guldor ko‘ylak)."),
    Q("Qaysi sifat old qo‘shimcha yordamida yasalgan?", "serhosil", ["hosildor", "hosilsiz", "hosilli"], d=2, x="ser- old qo‘shimchasi: serhosil."),
    Q("Qaysi sifat old qo‘shimcha yordamida yasalgan?", "beodob", ["odobli", "odobsiz", "odobliroq"], d=2, x="be- old qo‘shimchasi: beodob."),
    Q("“be-” old qo‘shimchasi qanday ma’no beradi?", "Belgining yo‘qligini", ["Belgining ko‘pligini", "Kichraytirishni", "Joyni"], d=3,
      x="beodob — odobi yo‘q (odobsiz)."),
    Q("“ser-” old qo‘shimchasi qanday ma’no beradi?", "Belgining ko‘pligini", ["Belgining yo‘qligini", "Kichraytirishni", "Vaqtni"], d=3,
      x="serhosil — hosili ko‘p."),
    TF("“ta’sirchan” so‘zida -chan qo‘shimchasi bor.", True, x="ta’sir + chan."),
    TF("“mevador” so‘zidagi qo‘shimcha — -dor.", True, x="meva + dor: mevador daraxt."),
    TF("“tinimsiz” so‘zidagi -siz — ot yasovchi qo‘shimcha.", False, d=2, x="-siz sifat yasaydi: tinimsiz mehnat."),
    MATCH("Qo‘shimchani u yasagan sifat bilan juftlang",
          [("-li", "bilimli"), ("-siz", "shovqinsiz"), ("-chan", "talabchan"), ("-dor", "vafodor"), ("-gi", "bahorgi")], d=2),
]
T.topic("adj_suffixes", "🏷️", L("Sifat yasovchi qo‘shimchalar", "Adjective-forming suffixes", "Суффиксы прилагательных"), C3,
        "Sifat yasovchi qo‘shimchalar:\n"
        "• -li — belgi borligi: bilimli, mazali;  • -siz — belgining yo‘qligi: tinimsiz, hidsiz;\n"
        "• -chan — biror xususiyatga moyillik: talabchan, uyatchan;  • -dor — narsaga ega: mevador, vafodor;\n"
        "• -gi (-ki, -qi) — vaqt yoki o‘ringa oidlik: bahorgi, tungi, qishki.\n"
        "Old qo‘shimchalar ham sifat yasaydi: ser- (serhosil), be- (beodob), no- (notinch).", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["noun_meaning", "adj_types", "adj_suffixes"], C3)

# ============================================================ 4-chorak
# ------------------------------------------------------------ son turlari
NUM_KINDS = ["Sanoq son", "Tartib son", "Jamlovchi son", "Taqsim son", "Chama son", "Kasr son"]
NUM6 = [("ikkov", 2), ("beshtadan", 3), ("o‘ntacha", 4), ("beshdan ikki", 5), ("uchala", 2), ("ikkitadan", 3), ("yuzlab", 4),
        ("to‘rtdan uch", 5), ("oltinchi", 1), ("o‘n yetti", 0), ("uchov", 2), ("o‘ntadan", 3), ("yigirmatacha", 4)]
NUM_WHY = ["Sanoq son — miqdorni oddiy sanab bildiradi.", "Tartib son -(i)nchi bilan yasaladi.", "Jamlovchi son -ov, -ala bilan yasaladi.",
           "Taqsim son -tadan bilan yasaladi.", "Chama son taxminiy miqdorni bildiradi (-tacha, -lab).", "Kasr son butunning qismini bildiradi."]
items = []
for n, (w, k) in enumerate(NUM6):
    items.append(Q(f"“{w}” — qanday son?", NUM_KINDS[k], others(NUM_KINDS, NUM_KINDS[k], 3), d=1 if n < 8 else 2, x=NUM_WHY[k]))
items += [
    Q("Jamlovchi son qaysi qo‘shimchalar bilan yasaladi?", "-ov, -ala", ["-tadan", "-tacha", "-inchi"], x="ikkov, uchala."),
    Q("Taqsim son qaysi qo‘shimcha bilan yasaladi?", "-tadan", ["-ov", "-tacha", "-nchi"], x="beshtadan, ikkitadan."),
    Q("Chama son qaysi qo‘shimcha bilan yasalishi mumkin?", "-tacha", ["-tadan", "-ala", "-inchi"], x="o‘ntacha, yuztacha."),
    Q("“ikki” soniga -ov qo‘shilsa, qanday yoziladi?", "ikkov", ["ikkiov", "ikkovv", "ikkiyov"], d=2, x="Unli tushib qoladi: ikki + ov = ikkov."),
    Q("“uch” soniga -ala qo‘shilsa, qanday yoziladi?", "uchala", ["uchalla", "uch-ala", "uchaala"], d=2, x="uch + ala = uchala."),
    Q("2/5 kasri so‘z bilan qanday o‘qiladi?", "beshdan ikki", ["ikkidan besh", "ikki besh", "beshta ikki"], d=2, x="Avval maxraj (5), keyin surat (2) aytiladi."),
    Q("3/4 kasri so‘z bilan qanday o‘qiladi?", "to‘rtdan uch", ["uchdan to‘rt", "to‘rt uch", "uchta to‘rt"], d=2, x="Maxraj -dan bilan, keyin surat."),
    Q("1/2 kasri so‘z bilan qanday o‘qiladi?", "ikkidan bir", ["birdan ikki", "bir ikki", "ikkita bir"], d=2, x="Ikkidan bir — yarim."),
    Q("Qaysi gapda taqsim son qo‘llangan?", "Har bir o‘quvchiga ikkitadan daftar berildi.",
      ["Sinfimizda o‘ttizta o‘quvchi bor.", "Biz ikkovimiz kutubxonaga bordik.", "Men ikkinchi qavatda yashayman."], d=2, x="ikkitadan — taqsim son."),
    Q("Qaysi gapda jamlovchi son qo‘llangan?", "Uchala do‘st birga o‘qiydi.",
      ["Uchta do‘st birga o‘qiydi.", "Uchinchi do‘st kech qoldi.", "Do‘stlarga uchtadan olma berildi."], d=2, x="uchala — jamlovchi son."),
    Q("Qaysi gapda chama son qo‘llangan?", "Maydonga yuzlab odam yig‘ildi.",
      ["Maydonga yuz kishi keldi.", "Yuzinchi mehmon sovg‘a oldi.", "Har biriga yuztadan so‘m berildi."], d=2, x="yuzlab — chama son."),
    Q("Qaysi son miqdor sonlarga kirmaydi?", "Tartib son", ["Sanoq son", "Jamlovchi son", "Taqsim son"], d=3,
      x="Sonlar miqdor va tartib sonlarga bo‘linadi; tartib son narsaning o‘rnini bildiradi."),
    Q("Qaysi yozuv to‘g‘ri?", "XXI asr", ["XXI-asr", "XXI-nchi asr", "XXIinchi asr"], d=2, x="Rim raqamidan keyin chiziqcha qo‘yilmaydi."),
    Q("Qaysi yozuv to‘g‘ri?", "6-sinf", ["6 sinf", "6-nchi sinf", "6-inchi sinf"], x="Arab raqamidan keyin chiziqcha qo‘yiladi."),
    TF("Taqsim son -tadan qo‘shimchasi bilan yasaladi.", True, x="beshtadan, o‘ntadan."),
    TF("“o‘nlab” — chama son.", True, d=2, x="o‘nlab, yuzlab, minglab — taxminiy miqdor."),
    TF("Kasr son o‘qilganda avval surat, keyin maxraj aytiladi.", False, d=2, x="Avval maxraj: beshdan ikki (2/5)."),
    MATCH("Son turini misol bilan juftlang",
          [("Jamlovchi", "uchala"), ("Taqsim", "beshtadan"), ("Chama", "yigirmatacha"), ("Kasr", "o‘ndan uch"), ("Tartib", "to‘qqizinchi"), ("Sanoq", "qirq besh")], d=2),
]
T.topic("numeral_types", "🔢", L("Son turlari", "Types of numerals", "Разряды числительных"), C4,
        "Sonlar ma’nosiga ko‘ra miqdor va tartib sonlarga bo‘linadi. Miqdor sonlar:\n"
        "• Sanoq: besh, o‘n yetti.  • Jamlovchi (-ov, -ala): ikkov, uchov, ikkala, uchala.\n"
        "• Taqsim (-tadan): beshtadan.  • Chama (-tacha, -lab, -larcha): o‘ntacha, yuzlab, o‘nlarcha.\n"
        "• Kasr: beshdan ikki (2/5), to‘rtdan uch (3/4).\n"
        "Tartib son -(i)nchi bilan yasaladi: oltinchi. Rim raqamidan keyin chiziqcha qo‘yilmaydi: XXI asr.", items=items)

# ------------------------------------------------------------ olmosh turlari
PT = ["Kishilik olmoshi", "Ko‘rsatish olmoshi", "So‘roq olmoshi", "O‘zlik olmoshi", "Belgilash olmoshi", "Bo‘lishsizlik olmoshi", "Gumon olmoshi"]
PRON6 = [("men", 0), ("bu", 1), ("kim", 2), ("biz", 0), ("shu", 1), ("nima", 2), ("ular", 0), ("o‘sha", 1), ("qaysi", 2),
         ("o‘z", 3), ("hamma", 4), ("hech kim", 5), ("allakim", 6), ("o‘zim", 3), ("barcha", 4), ("hech nima", 5), ("kimdir", 6),
         ("har bir", 4), ("nimadir", 6)]
items = []
for n, (w, k) in enumerate(PRON6):
    items.append(Q(f"“{w}” — qaysi turdagi olmosh?", PT[k], others(PT, PT[k], 3), d=1 if k <= 2 else 2, x=f"“{w}” — {PT[k].lower()}."))
for sent, w, k in [("Bu kitobni kim yozgan?", "kim", 2), ("Hech kim darsga kechikmadi.", "Hech kim", 5), ("Men vazifani o‘zim bajardim.", "o‘zim", 3),
                   ("Eshikni kimdir taqillatdi.", "kimdir", 6), ("Barcha o‘quvchilar bayramga keldi.", "Barcha", 4),
                   ("O‘sha kuni havo juda issiq edi.", "O‘sha", 1)]:
    items.append(Q(f"“{sent}” gapidagi “{w}” qaysi olmosh?", PT[k], others(PT, PT[k], 3), d=2, x=f"“{w}” — {PT[k].lower()}."))
for right, wrong in [("hech kim", ["hechkim", "hech-kim"]), ("har bir", ["harbir", "har-bir"]), ("allakim", ["alla kim", "alla-kim"]),
                     ("kimdir", ["kim dir", "kim-dir"])]:
    items.append(Q("Qaysi yozuv to‘g‘ri?", right, wrong, d=1 if " " in right else 2,
                   x=f"hech, har so‘zlari ajratib, alla- va -dir qismlari qo‘shib yoziladi: {right}."))
items += [
    Q("O‘zbek tilida olmoshlar ma’nosiga ko‘ra nechta turga bo‘linadi?", "7 ta", ["5 ta", "6 ta", "9 ta"], d=3,
      x="Kishilik, ko‘rsatish, so‘roq, o‘zlik, belgilash, bo‘lishsizlik, gumon."),
    Q("Gumon olmoshlari qaysi qismlar yordamida hosil bo‘ladi?", "alla-, -dir", ["hech, har", "-ov, -ala", "-tadan, -tacha"], d=2,
      x="allakim, allanima, kimdir, nimadir."),
    Q("Bo‘lishsizlik olmoshi bor gapda kesim qanday bo‘ladi?", "Bo‘lishsiz shaklda", ["Bo‘lishli shaklda", "So‘roq shaklda", "Buyruq shaklda"], d=3,
      x="Hech kim kelmadi. Hech nima demadi."),
    TF("“o‘z” — o‘zlik olmoshi.", True, x="o‘zim, o‘zing, o‘zi."),
    TF("“hamma” — so‘roq olmoshi.", False, x="hamma — belgilash olmoshi."),
    TF("Ko‘rsatish olmoshlari narsani ko‘rsatib, unga ishora qiladi.", True, x="bu kitob, o‘sha kun."),
    MATCH("Olmosh turini misol bilan juftlang",
          [("Kishilik", "siz"), ("Ko‘rsatish", "ushbu"), ("So‘roq", "qancha"), ("O‘zlik", "o‘zimiz"), ("Belgilash", "har kim"),
           ("Bo‘lishsizlik", "hech qaysi"), ("Gumon", "allanima")], d=2),
]
T.topic("pronoun_types", "👥", L("Olmosh turlari", "Types of pronouns", "Разряды местоимений"), C4,
        "Olmoshlar ma’nosiga ko‘ra 7 turga bo‘linadi:\n"
        "• Kishilik: men, sen, u, biz, siz, ular.  • Ko‘rsatish: bu, shu, o‘sha, ushbu.\n"
        "• So‘roq: kim, nima, qaysi, qancha.  • O‘zlik: o‘z (o‘zim, o‘zing, o‘zi).\n"
        "• Belgilash: hamma, barcha, har bir, har kim.  • Bo‘lishsizlik: hech kim, hech nima, hech qaysi.\n"
        "• Gumon: allakim, allanima, kimdir, nimadir. Imlo: hech kim, har bir — ajratib; allakim, kimdir — qo‘shib.", items=items)

# ------------------------------------------------------------ imlo va tinish belgilari
items = []
for n, (right, wrong) in enumerate([("hayvon", ["xayvon", "hayvan"]), ("xabar", ["habar", "xabr"]), ("hunarmand", ["xunarmand", "hunarmad"]),
                                    ("xizmat", ["hizmat", "xizmad"]), ("hikoya", ["xikoya", "hikaya"]), ("xalq", ["halq", "xaliq"]),
                                    ("mehribon", ["mexribon", "mehriban"]), ("hovli", ["xovli", "hovly"])]):
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong, d=1 if n < 4 else 2, x=f"To‘g‘ri yozilishi: {right}."))
items += [
    Q("“Daraxtning … shamolda sindi.” Nuqtalar o‘rniga qaysi so‘z mos?", "shoxi", ["shohi", "shoxy"], d=2, x="shox — daraxt shoxi, shoh — podshoh."),
    Q("“Ertakdagi … ulkan saroyda yashardi.” Nuqtalar o‘rniga qaysi so‘z mos?", "shoh", ["shox", "shoq"], d=2, x="shoh — podshoh, shox — daraxt shoxi."),
    Q("Qaysi yozuv to‘g‘ri?", "Keldingmi?", ["Kelding mi?", "Kelding-mi?"], x="-mi yuklamasi qo‘shib yoziladi."),
    Q("Qaysi yozuv to‘g‘ri?", "Senchi?", ["Sen chi?", "Sen-chi?"], d=2, x="-chi yuklamasi qo‘shib yoziladi."),
    Q("Qaysi yozuv to‘g‘ri?", "Navro‘z bayrami", ["navro‘z bayrami", "Navro‘z Bayrami"], x="Bayram nomi bosh harf bilan, “bayrami” kichik harf bilan yoziladi."),
    Q("Qaysi yozuv to‘g‘ri?", "Mustaqillik kuni", ["mustaqillik kuni", "Mustaqillik Kuni"], x="Bayram nomining birinchi so‘zi bosh harf bilan yoziladi."),
    Q("Qaysi gapda tire to‘g‘ri qo‘yilgan?", "Toshkent — O‘zbekiston poytaxti.",
      ["Toshkent O‘zbekiston — poytaxti.", "— Toshkent O‘zbekiston poytaxti.", "Toshkent O‘zbekiston poytaxti —."], d=2,
      x="Ega va kesim ot bilan ifodalanganda orasiga tire qo‘yiladi."),
    Q("Ega va kesim ot bilan ifodalansa, ular orasiga qaysi belgi qo‘yiladi?", "tire (—)", ["vergul", "ikki nuqta", "qo‘shtirnoq"], d=2,
      x="Kitob — bilim manbai."),
    Q("Qaysi gapda ikki nuqta to‘g‘ri qo‘yilgan?", "Bozordan meva oldik: olma, nok, uzum.",
      ["Bozordan: meva oldik olma, nok, uzum.", "Bozordan meva: oldik olma, nok, uzum.", "Bozordan meva oldik olma: nok, uzum."], d=2,
      x="Umumlashtiruvchi so‘z (meva)dan keyin, uyushiq bo‘laklar oldidan ikki nuqta qo‘yiladi."),
    Q("Umumlashtiruvchi so‘zdan keyin uyushiq bo‘laklar kelsa, qaysi belgi qo‘yiladi?", "ikki nuqta", ["tire", "nuqta", "so‘roq belgisi"], d=3,
      x="Sabzavotlar: sabzi, piyoz, kartoshka."),
    Q("Qaysi gapda qo‘shtirnoq to‘g‘ri ishlatilgan?", "Men “Sehrli qalam” kitobini o‘qidim.",
      ["Men Sehrli qalam “kitobini” o‘qidim.", "Men “Sehrli” qalam kitobini o‘qidim.", "Men Sehrli “qalam” kitobini o‘qidim."], d=2,
      x="Kitob nomi qo‘shtirnoqqa olinadi."),
    Q("Qaysi gapda vergul to‘g‘ri qo‘yilgan?", "Albatta, men sizga yordam beraman.",
      ["Albatta men, sizga yordam beraman.", "Albatta men sizga, yordam beraman.", "Albatta men sizga yordam beraman,"], d=2,
      x="Kirish so‘z vergul bilan ajratiladi."),
    Q("“Afsuski” kirish so‘zi gapda qanday ajratiladi?", "Vergul bilan", ["Tire bilan", "Qo‘shtirnoq bilan", "Ikki nuqta bilan"], d=3,
      x="Afsuski, poyezd ketib qolgan edi."),
    Q("Qaysi gapda undalma to‘g‘ri ajratilgan?", "Qadrli do‘stim, xatingni oldim.",
      ["Qadrli, do‘stim xatingni oldim.", "Qadrli do‘stim xatingni, oldim.", "Qadrli do‘stim xatingni oldim,"], x="Undalma vergul bilan ajratiladi."),
    TF("Kirish so‘zlar vergul bilan ajratiladi.", True, x="Menimcha, bu to‘g‘ri."),
    TF("Kitob va jurnal nomlari qo‘shtirnoqqa olinadi.", True, x="“Sehrli qalam” kitobi."),
    TF("-mi so‘roq yuklamasi so‘zdan ajratib yoziladi.", False, x="-mi qo‘shib yoziladi: Keldingmi?"),
    TF("Juft so‘zlar qo‘shib yoziladi.", False, d=2, x="Juft so‘zlar chiziqcha bilan yoziladi: ota-ona."),
    MATCH("Qoidani misol bilan juftlang",
          [("tire", "Toshkent — poytaxt."), ("ikki nuqta", "Meva oldik: olma, nok."), ("qo‘shtirnoq", "“Sehrli qalam” kitobi"),
           ("chiziqcha", "ota-ona"), ("vergul", "Albatta, boraman.")], d=2),
]
T.topic("spelling_punct", "✍️", L("Imlo va tinish belgilari", "Spelling and punctuation", "Орфография и пунктуация"), C4,
        "• h va x ni farqlang: hayvon, hunar, hikoya — xabar, xizmat, xalq. Ma’no farqlanadi: shox (daraxt shoxi) — shoh (podshoh).\n"
        "• -mi, -chi yuklamalari qo‘shib yoziladi: Keldingmi? Senchi?\n"
        "• Ega va kesim ot bilan ifodalansa, orasiga tire qo‘yiladi: Toshkent — O‘zbekiston poytaxti.\n"
        "• Umumlashtiruvchi so‘zdan keyin uyushiq bo‘laklar oldidan ikki nuqta qo‘yiladi: Meva oldik: olma, nok, uzum.\n"
        "• Kirish so‘zlar vergul bilan ajratiladi: Albatta, boraman. Kitob nomlari qo‘shtirnoqqa olinadi.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["numeral_types", "pronoun_types", "spelling_punct"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["word_meaning", "syn_ant", "homonyms", "vocab_layers", "idioms", "compound_words", "pair_words", "noun_meaning", "adj_types",
        "adj_suffixes", "numeral_types", "pronoun_types", "spelling_punct"], C4, level=3)

T.write()
