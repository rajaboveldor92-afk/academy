"""O‘zbek tili savollari uchun ma’lumotlar va yordamchilar (ona tili dasturlari uchun).

Barcha ro‘yxatlar qo‘lda tuzilgan va tekshirilgan: noto‘g‘ri variantlar orasida ikkinchi to‘g‘ri javob
bo‘lmasligi uchun sinonim/antonim chalg‘ituvchilari ham qo‘lda yozilgan.
"""

VOWELS = {"a", "o", "u", "e", "i", "o‘"}
ALPHABET = ["a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "x", "y", "z", "o‘", "g‘", "sh", "ch", "ng"]


def letters(word):
    """So‘zni o‘zbek harflariga ajratadi: o‘, g‘, sh, ch, ng — bitta harf."""
    w = word.lower()
    out = []
    i = 0
    while i < len(w):
        two = w[i:i + 2]
        if two in ("o‘", "g‘", "sh", "ch"):
            out.append(two)
            i += 2
            continue
        if two == "ng" and (i + 2 == len(w) or w[i + 2] not in "aoueiy"):
            out.append("ng")
            i += 2
            continue
        out.append(w[i])
        i += 1
    return out


def vowels_of(word):
    return [c for c in letters(word) if c in VOWELS]


def vowel_count(word):
    return len(vowels_of(word))


def alpha_key(word):
    return [ALPHABET.index(c) if c in ALPHABET else 99 for c in letters(word)]


# So‘z → bo‘g‘inlar (har bir bo‘g‘inda bitta unli).
SYLLABLES = {
    "kitob": ["ki", "tob"], "daftar": ["daf", "tar"], "maktab": ["mak", "tab"], "qalam": ["qa", "lam"],
    "olma": ["ol", "ma"], "bola": ["bo", "la"], "ona": ["o", "na"], "deraza": ["de", "ra", "za"],
    "kapalak": ["ka", "pa", "lak"], "chumoli": ["chu", "mo", "li"], "shaftoli": ["shaf", "to", "li"],
    "o‘qituvchi": ["o‘", "qi", "tuv", "chi"], "qo‘g‘irchoq": ["qo‘", "g‘ir", "choq"], "tarvuz": ["tar", "vuz"],
    "quyosh": ["qu", "yosh"], "yulduz": ["yul", "duz"], "kabutar": ["ka", "bu", "tar"], "mehribon": ["meh", "ri", "bon"],
    "piyola": ["pi", "yo", "la"], "soyabon": ["so", "ya", "bon"], "supurgi": ["su", "pur", "gi"], "sabzi": ["sab", "zi"],
    "daryo": ["dar", "yo"], "osmon": ["os", "mon"], "paxta": ["pax", "ta"], "bug‘doy": ["bug‘", "doy"],
    "oshxona": ["osh", "xo", "na"], "bahor": ["ba", "hor"], "tulki": ["tul", "ki"], "sigir": ["si", "gir"],
    "tovuq": ["to", "vuq"], "lola": ["lo", "la"], "anor": ["a", "nor"], "uzum": ["u", "zum"], "o‘rik": ["o‘", "rik"],
    "dehqon": ["deh", "qon"], "shifokor": ["shi", "fo", "kor"], "kutubxona": ["ku", "tub", "xo", "na"],
    "chiroyli": ["chi", "roy", "li"], "toshbaqa": ["tosh", "ba", "qa"], "mashina": ["ma", "shi", "na"],
    "non": ["non"], "uy": ["uy"], "qor": ["qor"], "gul": ["gul"], "kun": ["kun"], "tog‘": ["tog‘"],
}


def wrong_splits(syl):
    """Bo‘g‘in chegarasini bitta harfga surib, noto‘g‘ri bo‘linishlar hosil qiladi."""
    parts = [letters(s) for s in syl]
    out = []
    for i in range(len(parts) - 1):
        left, right = parts[i], parts[i + 1]
        if len(left) > 1:
            p = [list(x) for x in parts]
            p[i + 1] = [p[i][-1]] + p[i + 1]
            p[i] = p[i][:-1]
            out.append("-".join("".join(x) for x in p))
        if len(right) > 1:
            p = [list(x) for x in parts]
            p[i] = p[i] + [p[i + 1][0]]
            p[i + 1] = p[i + 1][1:]
            out.append("-".join("".join(x) for x in p))
    return [o for o in dict.fromkeys(out) if all(x for x in o.split("-"))]


# (so‘z, ma’nodoshi, [ma’nodosh bo‘lmagan chalg‘ituvchilar])
SYNONYMS_Q = [
    ("chiroyli", "go‘zal", ["xunuk", "katta", "tez"]),
    ("aqlli", "dono", ["dangasa", "nodon", "baland"]),
    ("botir", "jasur", ["qo‘rqoq", "yalqov", "sekin"]),
    ("xursand", "shod", ["g‘amgin", "xafa", "charchagan"]),
    ("katta", "ulkan", ["mitti", "kichik", "past"]),
    ("qiyin", "mushkul", ["oson", "yengil", "qisqa"]),
    ("oson", "yengil", ["qiyin", "mushkul", "uzun"]),
    ("toza", "ozoda", ["iflos", "eski", "qorong‘i"]),
    ("do‘st", "o‘rtoq", ["dushman", "begona", "raqib"]),
    ("baxt", "saodat", ["g‘am", "qayg‘u", "kasallik"]),
    ("yuz", "chehra", ["oyoq", "qo‘l", "yelka"]),
    ("kuch", "quvvat", ["zaiflik", "holsizlik", "dangasalik"]),
    ("vatan", "yurt", ["mehmon", "sayohat", "chegara"]),
    ("bahor", "ko‘klam", ["kuz", "qish", "yoz"]),
    ("tong", "sahar", ["kech", "tun", "oqshom"]),
    ("oqshom", "kechqurun", ["ertalab", "tong", "tush"]),
    ("bilim", "ilm", ["jaholat", "o‘yin", "uyqu"]),
    ("tinch", "osoyishta", ["shovqinli", "notinch", "g‘alayonli"]),
    ("xato", "yanglish", ["to‘g‘ri", "aniq", "rost"]),
    ("gapirmoq", "so‘zlamoq", ["jim turmoq", "uxlamoq", "yugurmoq"]),
]
SYNONYMS = [(a, b) for a, b, _ in SYNONYMS_Q]

# (so‘z, zid ma’nolisi, [antonim bo‘lmagan chalg‘ituvchilar])
ANTONYMS_Q = [
    ("katta", "kichik", ["ulkan", "baland", "keng"]),
    ("issiq", "sovuq", ["iliq", "qaynoq", "yumshoq"]),
    ("baland", "past", ["uzun", "katta", "yuqori"]),
    ("uzun", "qisqa", ["baland", "keng", "katta"]),
    ("keng", "tor", ["katta", "uzun", "yassi"]),
    ("yangi", "eski", ["toza", "chiroyli", "katta"]),
    ("oq", "qora", ["sariq", "yashil", "ko‘k"]),
    ("kun", "tun", ["tong", "bahor", "soat"]),
    ("yorug‘", "qorong‘i", ["oq", "issiq", "tiniq"]),
    ("shirin", "achchiq", ["mazali", "totli", "yumshoq"]),
    ("yaxshi", "yomon", ["chiroyli", "katta", "a’lo"]),
    ("do‘st", "dushman", ["o‘rtoq", "qo‘shni", "mehmon"]),
    ("kulmoq", "yig‘lamoq", ["jilmaymoq", "gapirmoq", "sakramoq"]),
    ("ochmoq", "yopmoq", ["kirmoq", "olmoq", "yuvmoq"]),
    ("qattiq", "yumshoq", ["mustahkam", "og‘ir", "sovuq"]),
    ("og‘ir", "yengil", ["qattiq", "katta", "sekin"]),
    ("to‘la", "bo‘sh", ["katta", "og‘ir", "keng"]),
    ("ho‘l", "quruq", ["nam", "sovuq", "toza"]),
    ("erta", "kech", ["tez", "tong", "sahar"]),
    ("rost", "yolg‘on", ["to‘g‘ri", "haqiqat", "aniq"]),
    ("boy", "kambag‘al", ["badavlat", "saxiy", "kuchli"]),
    ("dono", "nodon", ["aqlli", "bilimdon", "ziyrak"]),
    ("mehnatkash", "dangasa", ["tirishqoq", "g‘ayratli", "chaqqon"]),
    ("quvnoq", "g‘amgin", ["xursand", "shod", "sho‘x"]),
    ("olmoq", "bermoq", ["tutmoq", "ushlamoq", "yig‘moq"]),
    ("arzon", "qimmat", ["tekin", "oson", "yangi"]),
    ("kirmoq", "chiqmoq", ["o‘tmoq", "bormoq", "tushmoq"]),
    ("tez", "sekin", ["chaqqon", "jadal", "shoshqin"]),
]
ANTONYMS = [(a, b) for a, b, _ in ANTONYMS_Q]

# So‘z va uning qismlari: [o‘zak, qo‘shimcha, ...]
ROOTS_G3 = [
    ("kitoblar", ["kitob", "lar"]), ("gullar", ["gul", "lar"]), ("maktabda", ["maktab", "da"]), ("qalamni", ["qalam", "ni"]),
    ("shaharga", ["shahar", "ga"]), ("ishchi", ["ish", "chi"]), ("suvli", ["suv", "li"]), ("tuzsiz", ["tuz", "siz"]),
    ("bog‘bon", ["bog‘", "bon"]), ("kitobxon", ["kitob", "xon"]), ("ovchi", ["ov", "chi"]), ("tog‘li", ["tog‘", "li"]),
    ("daftarlarim", ["daftar", "lar", "im"]), ("bolalarga", ["bola", "lar", "ga"]), ("uylarimiz", ["uy", "lar", "imiz"]),
    ("do‘stlarim", ["do‘st", "lar", "im"]), ("daraxtlardan", ["daraxt", "lar", "dan"]), ("ukamning", ["uka", "m", "ning"]),
]

WORD_CLASSES_G3 = {
    "Ot": ["kitob", "daftar", "maktab", "bola", "daraxt", "gul", "daryo", "qush", "shahar", "ona", "stol", "olma"],
    "Sifat": ["qizil", "katta", "shirin", "chiroyli", "baland", "yashil", "aqlli", "yumshoq", "keng", "toza", "oppoq", "mehribon"],
    "Son": ["uch", "besh", "o‘n", "yigirma", "yetti", "ikkinchi", "beshinchi", "o‘ttiz", "to‘qqiz", "ming", "bir", "birinchi"],
    "Fe’l": ["o‘qidi", "yozdi", "yugurdi", "keldi", "kuldi", "chizdi", "sakradi", "uxladi", "ishladi", "yuvdi", "tingladi", "sanadi"],
}
CLASS_QUESTION = {
    "Ot": "kim? nima? qayer?",
    "Sifat": "qanday? qanaqa?",
    "Son": "nechta? qancha? nechanchi?",
    "Fe’l": "nima qildi? nima qiladi?",
    "Olmosh": "ot, sifat yoki son o‘rnida keladi",
    "Ravish": "qanday? qachon? qayerda? (harakat belgisi)",
}

PROPER_NOUNS = ["Toshkent", "Samarqand", "Buxoro", "Xiva", "Farg‘ona", "Andijon", "Namangan", "Termiz", "Nukus",
                "Amudaryo", "Sirdaryo", "Zarafshon", "O‘zbekiston", "Anvar", "Dilnoza", "Sardor", "Malika", "Bobur"]
COMMON_NOUNS = ["shahar", "daryo", "qishloq", "ko‘cha", "bola", "qiz", "tog‘", "kitob", "maktab", "dengiz", "mamlakat",
                "poytaxt", "viloyat", "o‘quvchi", "do‘st"]

PLURAL_WORDS = ["kitob", "daftar", "olma", "bola", "gul", "uy", "daraxt", "qush", "mashina", "ruchka", "o‘quvchi", "tog‘"]

GENITIVE = {"men": "mening", "sen": "sening", "u": "uning"}
POSSESSIVE_G3 = [
    ("ona", ["onam", "onang", "onasi"]), ("ota", ["otam", "otang", "otasi"]), ("uka", ["ukam", "ukang", "ukasi"]),
    ("olma", ["olmam", "olmang", "olmasi"]), ("xona", ["xonam", "xonang", "xonasi"]),
    ("kitob", ["kitobim", "kitobing", "kitobi"]), ("daftar", ["daftarim", "daftaring", "daftari"]),
    ("uy", ["uyim", "uying", "uyi"]), ("qalam", ["qalamim", "qalaming", "qalami"]), ("gul", ["gulim", "guling", "guli"]),
]


def possessive_wrong(base, right):
    forms = [base + s for s in ("m", "ng", "si", "im", "ing", "i")]
    return [f for f in forms if f != right][:5]


ADJ_NOUN = [("qizil", "olma"), ("katta", "uy"), ("shirin", "qovun"), ("aqlli", "bola"), ("baland", "tog‘"), ("yangi", "kitob"),
            ("toza", "xona"), ("sovuq", "suv"), ("yashil", "barg"), ("mehribon", "ona"), ("keng", "ko‘cha"), ("oppoq", "qor")]
VERBS_G3 = ["o‘qidi", "yozdi", "yugurdi", "keldi", "kuldi", "chizdi", "sakradi", "uxladi", "ishladi", "yuvdi", "tingladi", "sanadi"]

SENTENCE_TYPES_G3 = [
    ("Bugun havo iliq.", "Darak gap"), ("Bog‘da gullar ochildi.", "Darak gap"), ("Men uchinchi sinfda o‘qiyman.", "Darak gap"),
    ("Buvim bizga ertak aytib berdi.", "Darak gap"), ("Qishda qor yog‘adi.", "Darak gap"), ("Akam futbol o‘ynadi.", "Darak gap"),
    ("Sen qayerda yashaysan?", "So‘roq gap"), ("Dars qachon boshlanadi?", "So‘roq gap"), ("Bu kitob kimniki?", "So‘roq gap"),
    ("Siz choy ichasizmi?", "So‘roq gap"), ("Nega kech qolding?", "So‘roq gap"), ("Ertaga maktabga borasanmi?", "So‘roq gap"),
    ("Eshikni yoping.", "Buyruq gap"), ("Kitobni stolga qo‘y.", "Buyruq gap"), ("Darsni diqqat bilan tinglang.", "Buyruq gap"),
    ("Menga qalam bering.", "Buyruq gap"), ("Gullarga suv quying.", "Buyruq gap"), ("Qo‘lingni yuv.", "Buyruq gap"),
]
SENT_EXPLAIN = {
    "Darak gap": "Darak gap biror voqea haqida xabar beradi va nuqta bilan tugaydi.",
    "So‘roq gap": "So‘roq gap savol bildiradi va so‘roq belgisi bilan tugaydi.",
    "Buyruq gap": "Buyruq gap buyruq yoki iltimos bildiradi.",
}

PUNCT_G3 = [
    ("Ertalab quyosh chiqdi", "."), ("Biz kutubxonaga bordik", "."), ("Mushuk divanda uxlayapti", "."),
    ("Dadam ishdan qaytdi", "."), ("Olmalar pishdi", "."), ("Bolalar hovlida o‘ynashyapti", "."),
    ("Sen nima o‘qiyapsan", "?"), ("Ukang necha yoshda", "?"), ("Qayerga ketyapsiz", "?"), ("Bugun dars bormi", "?"),
    ("Kim birinchi keldi", "?"), ("Nega yig‘layapsan", "?"),
    ("Voy, qanday chiroyli gul", "!"), ("Yashasin, bayram keldi", "!"), ("Qanday go‘zal manzara", "!"), ("Ura, biz yutdik", "!"),
]
PUNCT_EXPLAIN = {
    ".": "xabar beruvchi gap nuqta bilan tugaydi.",
    "?": "savol bildiruvchi gap so‘roq belgisi bilan tugaydi.",
    "!": "kuchli his bilan aytilgan gap undov belgisi bilan tugaydi.",
}

ORDER_SENTENCES_G3 = [
    "Qizil olma pishdi", "Kichkina mushuk uxlayapti", "Oppoq qor yog‘di", "Mening ukam kuldi", "Chiroyli kapalak uchdi",
    "Katta daraxt gulladi", "Sariq barglar to‘kildi", "Onam mazali osh pishirdi", "Aqlli bola kitob o‘qidi",
    "Opam chiroyli rasm chizdi", "Dadam yangi mashina oldi", "Buvim issiq non yopdi",
]


# ============================================================ 5-sinf ma’lumotlari
VOICED_PAIRS = [("b", "p"), ("d", "t"), ("g", "k"), ("z", "s"), ("v", "f")]
VOICED = ["b", "d", "g", "z", "v", "j", "l", "m", "n", "r", "y", "g‘"]
VOICELESS = ["p", "t", "k", "s", "f", "sh", "ch", "x", "h", "q"]

# So‘z oxiridagi jarangli undosh jarangsiz eshitilsa ham yozuvda saqlanadi.
FINAL_VOICED = [("kitob", "kitop"), ("maktab", "maktap"), ("javob", "javop"), ("sabab", "sabap"), ("obod", "obot"),
                ("ozod", "ozot"), ("avlod", "avlot"), ("farzand", "farzant"), ("xursand", "xursant"), ("qand", "qant"),
                ("barg", "bark"), ("tog‘", "toq"), ("bog‘", "boq"), ("yog‘", "yoq")]

# Tutuq belgisi (’) bilan yoziladigan so‘zlar va uning xato yozilishlari.
TUTUQ = [("ma’no", ["mano", "maano", "m’ano"]), ("she’r", ["sher", "sheer", "sh’er"]), ("san’at", ["sanat", "sanaat", "sa’nat"]),
         ("ta’lim", ["talim", "taalim", "tal’im"]), ("e’lon", ["elon", "eelon", "el’on"]), ("a’lo", ["alo", "aalo", "al’o"]),
         ("qal’a", ["qala", "qalaa", "qa’la"]), ("ma’lum", ["malum", "maalum", "mal’um"]), ("ta’til", ["tatil", "taatil", "tat’il"]),
         ("ta’sir", ["tasir", "taasir", "tas’ir"]), ("e’tibor", ["etibor", "eetibor", "et’ibor"]), ("jur’at", ["jurat", "juraat", "ju’rat"])]

OG_SPELLING = [("o‘qituvchi", ["oqituvchi", "o‘qituvchy", "uqituvchi"]), ("g‘isht", ["gisht", "g‘ish", "qisht"]),
               ("bog‘cha", ["bogcha", "boqcha", "bog‘ja"]), ("to‘g‘ri", ["tog‘ri", "to‘gri", "togri"]),
               ("o‘g‘il", ["og‘il", "o‘gil", "ugil"]), ("qo‘ng‘iroq", ["qong‘iroq", "qo‘ngiroq", "qongiroq"])]

# Omonimlar: so‘z → uning ikki ma’nosi (gap bilan)
HOMONYMS = [
    ("ot", "Otga yem berdik.", "Mening otim Anvar.", "hayvon", "ism"),
    ("yoz", "Yozda dam oldik.", "Xatni chiroyli yoz.", "fasl", "harakat"),
    ("o‘t", "O‘tloqda o‘t o‘sdi.", "Gulxanda o‘t yondi.", "o‘simlik", "olov"),
    ("qo‘y", "Qo‘ylar yaylovda o‘tlayapti.", "Kitobni javonga qo‘y.", "hayvon", "harakat"),
    ("yuz", "Yuzingni yuv.", "Kitob yuz betdan iborat.", "a’zo", "son"),
    ("tut", "Tut pishdi.", "Qo‘limdan mahkam tut.", "daraxt", "harakat"),
    ("oy", "Osmonda oy chiqdi.", "Bir yilda o‘n ikki oy bor.", "osmon jismi", "vaqt"),
    ("soch", "Qizning sochi uzun.", "Qushlarga don soch.", "tana qismi", "harakat"),
    ("tush", "Kecha qiziq tush ko‘rdim.", "Zinadan sekin tush.", "uyqudagi ko‘rinish", "harakat"),
    ("bosh", "Boshimga do‘ppi kiydim.", "Ishni ertalab bosh.", "tana qismi", "harakat"),
]

# Iboralar (frazeologizmlar) va ma’nosi
IDIOMS = [
    ("qo‘li ochiq", "saxiy", ["baxil", "dangasa", "qo‘rqoq"]),
    ("ko‘zi to‘rt bo‘lmoq", "intiqib kutmoq", ["uxlab qolmoq", "yaxshi ko‘rmoq", "xafa bo‘lmoq"]),
    ("boshi osmonga yetmoq", "juda xursand bo‘lmoq", ["kasal bo‘lmoq", "adashib qolmoq", "charchamoq"]),
    ("og‘zi qulog‘ida", "juda xursand", ["juda och", "juda charchagan", "juda qo‘rqqan"]),
    ("yuragi taka-puka bo‘lmoq", "qattiq qo‘rqmoq", ["xursand bo‘lmoq", "tez yugurmoq", "qo‘shiq aytmoq"]),
    ("ko‘z ochib yumguncha", "juda tez", ["juda sekin", "uzoq vaqt", "kechqurun"]),
    ("tarvuzi qo‘ltig‘idan tushmoq", "umidi puchga chiqmoq", ["tarvuz sotmoq", "xursand bo‘lmoq", "sovg‘a olmoq"]),
    ("qovog‘idan qor yog‘moq", "qattiq qahri kelgan, xo‘mraygan", ["juda sovqotgan", "quvnoq", "qor o‘ynayotgan"]),
    ("burnini osiltirmoq", "xafa bo‘lmoq", ["kulmoq", "maqtanmoq", "shoshilmoq"]),
    ("qulog‘iga quymoq", "yaxshilab uqtirmoq", ["qulog‘ini yuvmoq", "baqirmoq", "yashirmoq"]),
    ("tilini tishlamoq", "gapirmay o‘zini tutmoq", ["ovqat yemoq", "ko‘p gapirmoq", "qo‘shiq aytmoq"]),
    ("dilini og‘ritmoq", "xafa qilmoq", ["davolamoq", "xursand qilmoq", "maqtamoq"]),
    ("ikki qo‘li burnining ustida", "hech narsasiz, quruq qo‘l bilan", ["juda baquvvat", "qo‘li band", "qo‘li og‘riyapti"]),
    ("tepa sochi tikka bo‘lmoq", "juda qo‘rqib ketmoq", ["sochini taramoq", "xursand bo‘lmoq", "soch oldirmoq"]),
]

# Ko‘chma ma’noli birikmalar: birikma, ko‘chma ma’noli so‘z, ma’nosi
FIGURATIVE = [
    ("oltin qo‘l", "oltin", "mohir, usta"), ("tosh yurak", "tosh", "shafqatsiz"), ("temir intizom", "temir", "qattiq, mustahkam"),
    ("shirin so‘z", "shirin", "yoqimli"), ("achchiq haqiqat", "achchiq", "yoqimsiz, og‘ir"), ("sovuq javob", "sovuq", "iltifotsiz"),
    ("yumshoq tabiat", "yumshoq", "muloyim"), ("iliq kutib olmoq", "iliq", "samimiy"),
]

OLD_WORDS = [("mirshab", "tungi qorovul, tartib saqlovchi"), ("qozi", "sudya"), ("chopar", "xabar yetkazuvchi"),
             ("sarbon", "karvonboshi"), ("mirzo", "kotib, xat yozuvchi"), ("dorilfunun", "universitet")]
TERMS = [("kasr", "Matematika"), ("sayyora", "Tabiiy fan"), ("kesim", "Ona tili"), ("protsessor", "Informatika"),
         ("uchburchak", "Matematika"), ("fotosintez", "Tabiiy fan"), ("kelishik", "Ona tili"), ("algoritm", "Informatika"),
         ("tenglama", "Matematika"), ("hujayra", "Tabiiy fan"), ("sinonim", "Ona tili"), ("fayl", "Informatika")]

# So‘z yasovchi qo‘shimchalar: yasama so‘z, asos, qo‘shimcha, ma’nosi
DERIVED = [("ishchi", "ish", "chi", "kasb egasi"), ("ovchi", "ov", "chi", "kasb egasi"), ("temirchi", "temir", "chi", "kasb egasi"),
           ("paxtakor", "paxta", "kor", "kasb egasi"), ("ijodkor", "ijod", "kor", "shaxs"), ("bog‘bon", "bog‘", "bon", "kasb egasi"),
           ("kitobxon", "kitob", "xon", "shaxs"), ("mehnatkash", "mehnat", "kash", "shaxs"), ("gulzor", "gul", "zor", "joy"),
           ("olmazor", "olma", "zor", "joy"), ("tuzdon", "tuz", "don", "idish"), ("choydon", "choy", "don", "idish"),
           ("aqlli", "aql", "li", "belgi"), ("kuchli", "kuch", "li", "belgi"), ("suvsiz", "suv", "siz", "belgi"),
           ("tuzsiz", "tuz", "siz", "belgi"), ("do‘stlik", "do‘st", "lik", "tushuncha"), ("yaxshilik", "yaxshi", "lik", "tushuncha"),
           ("ishla", "ish", "la", "harakat"), ("tuzla", "tuz", "la", "harakat")]
FORM_SUFFIXES = ["lar", "ning", "ni", "ga", "da", "dan", "im", "ing", "i"]

WORD_CLASSES_G5 = {
    "Ot": ["kitob", "maktab", "daryo", "bahor", "do‘stlik", "o‘quvchi", "shahar", "bilim"],
    "Sifat": ["chiroyli", "baland", "aqlli", "qizil", "shirin", "mehribon", "keng", "yumshoq"],
    "Son": ["uch", "o‘n", "yigirma", "beshinchi", "ming", "ikkinchi", "to‘qqiz", "yetti"],
    "Olmosh": ["men", "sen", "biz", "ular", "bu", "shu", "kim", "hamma"],
    "Fe’l": ["o‘qidi", "yozyapti", "keldi", "kuldi", "ishlaydi", "chizdi", "yugurdi", "tingladi"],
    "Ravish": ["yayov", "hamisha", "birdan", "ataylab", "zo‘rg‘a", "jimgina", "astoydil", "ertaga"],
}

CASES = [("", "Bosh kelishik", "kim? nima?"), ("ning", "Qaratqich kelishigi", "kimning? nimaning?"),
         ("ni", "Tushum kelishigi", "kimni? nimani?"), ("ga", "Jo‘nalish kelishigi", "kimga? nimaga? qayerga?"),
         ("da", "O‘rin-payt kelishigi", "kimda? nimada? qayerda?"), ("dan", "Chiqish kelishigi", "kimdan? nimadan? qayerdan?")]
CASE_WORDS = ["kitob", "maktab", "shahar", "daftar", "bog‘", "uy"]
DATIVE = [("yurak", "yurakka"), ("qishloq", "qishloqqa"), ("tilak", "tilakka"), ("o‘rtoq", "o‘rtoqqa"), ("terak", "terakka"),
          ("buloq", "buloqqa"), ("tog‘", "tog‘ga"), ("bog‘", "bog‘ga"), ("maktab", "maktabga"), ("uy", "uyga")]


def dative_wrong(word, right):
    forms = {word + "ga", word + "ka", word + "qa", word + "g‘a"}
    return sorted(f for f in forms if f != right)


# Gap: (gap, ega, kesim)
SUBJ_PRED = [("Ali kitob o‘qidi.", "Ali", "o‘qidi"), ("Bolalar hovlida o‘ynashdi.", "Bolalar", "o‘ynashdi"),
             ("Onam mazali osh pishirdi.", "Onam", "pishirdi"), ("Qushlar janubga uchib ketdi.", "Qushlar", "uchib ketdi"),
             ("Kecha qor yog‘di.", "qor", "yog‘di"), ("Dilnoza she’r yodladi.", "Dilnoza", "yodladi"),
             ("O‘qituvchi yangi mavzuni tushuntirdi.", "O‘qituvchi", "tushuntirdi"), ("Bog‘da atirgullar ochildi.", "atirgullar", "ochildi"),
             ("Akam futbol o‘ynaydi.", "Akam", "o‘ynaydi"), ("Daryo shovqin bilan oqadi.", "Daryo", "oqadi"),
             ("Men har kuni erta turaman.", "Men", "turaman"), ("Shamol daraxt shoxlarini tebratdi.", "Shamol", "tebratdi")]

PHRASE_OR_SENTENCE = [("chiroyli gul", "So‘z birikmasi"), ("Gul chiroyli.", "Gap"), ("maktab hovlisi", "So‘z birikmasi"),
                      ("Maktab hovlisi keng.", "Gap"), ("kitob o‘qimoq", "So‘z birikmasi"), ("Men kitob o‘qidim.", "Gap"),
                      ("qizil olma", "So‘z birikmasi"), ("Olma qizardi.", "Gap"), ("baland tog‘", "So‘z birikmasi"),
                      ("Tog‘lar baland.", "Gap"), ("do‘stimning uyi", "So‘z birikmasi"), ("Do‘stim uyga keldi.", "Gap")]

# Undalmali va uyushiq bo‘lakli gaplar
VOCATIVE = [("Ali, bu yoqqa kel.", "Ali"), ("Bolalar, darsga kech qolmang.", "Bolalar"), ("Onajon, sizni sog‘indim.", "Onajon"),
            ("Do‘stim, menga yordam ber.", "Do‘stim"), ("Hurmatli ustoz, rahmat sizga!", "Hurmatli ustoz"),
            ("Zarina, kitobingni olib kel.", "Zarina"), ("Aziz vatandoshlar, bayram muborak!", "Aziz vatandoshlar"),
            ("Dilshod, uy vazifasini bajardingmi?", "Dilshod")]
HOMOGENEOUS = [("Olma, nok va o‘rik pishdi.", "olma, nok, o‘rik"), ("Bolalar kuldi, sakradi, o‘ynadi.", "kuldi, sakradi, o‘ynadi"),
               ("Bog‘da qizil, sariq, oq gullar ochildi.", "qizil, sariq, oq"), ("Men kitob, daftar va ruchka oldim.", "kitob, daftar, ruchka"),
               ("Bozordan olma, uzum va anor oldik.", "olma, uzum, anor"), ("Akam va opam kutubxonaga borishdi.", "akam, opam")]
