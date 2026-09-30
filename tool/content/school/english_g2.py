"""Ingliz tili, 2-sinf: assets/data/school/english_g2.json + bank_english_g2.json.

2-sinf (8 yosh) — 1-sinfdan keyingi bosqich: alifbo va so‘z boshidagi tovush, sonlar 1–20, o‘zi haqida
gapirish (How old are you? Where are you from?), hafta kunlari, ob-havo, kiyimlar va ranglar
(What colour is it?), uy va xonalar, taomlar (I like / I don't like), I have, this / that, ko‘plik (-s),
I can. Ko‘rsatma o‘zbekcha o‘qib beriladi, inglizcha so‘z va gaplar `say` orqali ingliz ovozida eshitiladi;
asosiy savol turi — tinglab rasm yoki tarjima tanlash, qo‘shimcha — qisqa gap tuzish (3–4 so‘z).
Hamma matn va savollar o‘zimizniki (darslikdan ko‘chirilmagan). Imlo — britancha (colour).
Qayta yaratish: python3 tool/content/school/english_g2.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("english", 2, L("Ingliz tili", "English", "Английский язык"))

C1 = "1-chorak. Alifbo, sonlar va tanishuv"
C2 = "2-chorak. Kunlar, ob-havo va kiyimlar"
C3 = "3-chorak. Uyim, taomlar va narsalarim"
C4 = "4-chorak. Bu nima? Ko‘plik va harakatlar"

# ------------------------------------------------------------ lug‘at: so‘z → (rasm, o‘zbekcha)
VOC = {
    # so‘z boshidagi tovush
    "bee": ("🐝", "ari"), "bus": ("🚌", "avtobus"), "duck": ("🦆", "o‘rdak"), "door": ("🚪", "eshik"),
    "frog": ("🐸", "qurbaqa"), "fish": ("🐟", "baliq"), "moon": ("🌙", "oy"), "monkey": ("🐵", "maymun"),
    "snake": ("🐍", "ilon"), "sun": ("☀️", "quyosh"), "train": ("🚂", "poyezd"), "tiger": ("🐯", "yo‘lbars"),
    "cow": ("🐮", "sigir"), "cake": ("🍰", "tort"), "lion": ("🦁", "sher"), "lemon": ("🍋", "limon"),
    "rabbit": ("🐰", "quyon"), "robot": ("🤖", "robot"), "horse": ("🐴", "ot"), "pen": ("🖊️", "ruchka"),
    "apple": ("🍎", "olma"), "egg": ("🥚", "tuxum"), "umbrella": ("☂️", "soyabon"), "zebra": ("🦓", "zebra"),
    "goat": ("🐐", "echki"), "dog": ("🐶", "it"), "cat": ("🐱", "mushuk"), "bird": ("🐦", "qush"),
    "ball": ("⚽", "to‘p"), "bike": ("🚲", "velosiped"), "book": ("📕", "kitob"), "car": ("🚗", "mashina"),
    # ob-havo
    "sunny": ("☀️", "quyoshli"), "rainy": ("🌧️", "yomg‘irli"), "cloudy": ("☁️", "bulutli"),
    "windy": ("💨", "shamolli"), "snowy": ("❄️", "qorli"), "hot": (None, "issiq"), "cold": (None, "sovuq"),
    "rainbow": ("🌈", "kamalak"), "snowman": ("⛄", "qor odam"),
    # kiyimlar
    "T-shirt": ("👕", "futbolka"), "trousers": ("👖", "shim"), "dress": ("👗", "ko‘ylak"), "hat": ("👒", "shlyapa"),
    "cap": ("🧢", "kepka"), "coat": ("🧥", "palto"), "scarf": ("🧣", "sharf"), "gloves": ("🧤", "qo‘lqop"),
    "socks": ("🧦", "paypoq"), "boots": ("👢", "etik"), "shoes": ("👟", "poyabzal"), "skirt": (None, "yubka"),
    # uy
    "house": ("🏠", "uy"), "bed": ("🛏️", "karavot"), "bath": ("🛁", "vanna"), "sofa": ("🛋️", "divan"),
    "TV": ("📺", "televizor"), "kitchen": (None, "oshxona"), "bedroom": (None, "yotoqxona"),
    "bathroom": (None, "vannaxona"), "living room": (None, "mehmonxona"), "garden": (None, "bog‘"),
    "window": (None, "deraza"), "table": (None, "stol"), "chair": (None, "stul"), "room": (None, "xona"),
    # taomlar
    "bread": ("🍞", "non"), "milk": ("🥛", "sut"), "cheese": ("🧀", "pishloq"), "soup": ("🍲", "sho‘rva"),
    "rice": ("🍚", "guruch"), "tea": ("🍵", "choy"), "water": ("💧", "suv"), "ice cream": ("🍦", "muzqaymoq"),
    "chocolate": ("🍫", "shokolad"), "honey": ("🍯", "asal"), "meat": ("🍖", "go‘sht"), "juice": (None, "sharbat"),
    # harakatlar
    "swim": ("🏊", "suzmoq"), "run": ("🏃", "yugurmoq"), "dance": ("💃", "raqsga tushmoq"),
    "sing": ("🎤", "qo‘shiq aytmoq"), "read": ("📖", "o‘qimoq"), "write": ("✍️", "yozmoq"),
    "draw": ("🎨", "rasm chizmoq"), "ride a bike": ("🚴", "velosiped haydamoq"),
    "climb": ("🧗", "tirmashib chiqmoq"), "jump": (None, "sakramoq"), "fly": (None, "uchmoq"),
}

# Harf nomlari (britancha talaffuz, o‘zbekcha yozuvda taxminan).
NAMES = {"A": "ey", "B": "bi:", "C": "si:", "D": "di:", "E": "i:", "F": "ef", "G": "ji:", "H": "eych", "I": "ay",
         "J": "jey", "K": "key", "L": "el", "M": "em", "N": "en", "O": "ou", "P": "pi:", "Q": "kyu:", "R": "a:",
         "S": "es", "T": "ti:", "U": "yu:", "V": "vi:", "W": "dabl yu:", "X": "eks", "Y": "uay", "Z": "zed"}


# ------------------------------------------------------------ yordamchilar
def _end(s):
    return s if s[-1] in ".!?" else s + "."


def _pic(k):
    em = VOC[k][0]
    assert em, f"{k}: rasm yo‘q"
    return em


def PIC(word, wrong, d=1, say=None, x=None, q="Tinglang va rasmini toping"):
    """Tinglab rasm tanlash: inglizcha so‘z (yoki gap) eshitiladi, javob — emoji."""
    return Q(q, _pic(word), [_pic(k) for k in wrong], d=d, x=x or f"{word} — {VOC[word][1]} {_pic(word)}",
             say=say or word, lang="en")


def TR(word, wrong, d=1, x=None, q="Tinglang va tarjimasini toping"):
    """Tinglab tarjima tanlash: inglizcha so‘z eshitiladi, javob — o‘zbekcha so‘z."""
    em, uz = VOC[word]
    return Q(q, uz, [VOC[k][1] for k in wrong], d=d, x=x or f"{word} — {uz}" + (f" {em}" if em else ""),
             say=word, lang="en")


def SAME(word, shown, d=1, x=None, q="Tinglang: so‘z rasmga mosmi?"):
    """To‘g‘ri / noto‘g‘ri: rasm ko‘rsatiladi, inglizcha so‘z eshitiladi."""
    em = _pic(shown)
    ok = word == shown
    if x is None:
        x = (_end(f"To‘g‘ri: {word} — {VOC[word][1]} {em}") if ok else
             _end(f"Rasmda — {VOC[shown][1]} ({shown}). {word} esa — {VOC[word][1]}"))
    return TF(q, ok, d=d, x=x, e=em, say=word, lang="en")


def MATCHE(words, q="So‘zni rasmga moslang", d=2):
    return MATCH(q, [(k, _pic(k)) for k in words], d=d, lang="en")


def MATCHU(words, q="So‘zni tarjimasi bilan juftlang", d=2):
    return MATCH(q, [(k, VOC[k][1]) for k in words], d=d, lang="en")


def LISTEN(say, a, w, d=1, x=None, q="Tinglang va tarjimasini toping", e=None):
    """Tinglab tushunish: inglizcha gap eshitiladi, o‘zbekcha tarjimasi tanlanadi."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", e=e, say=say, lang="en")


def EN(q, a, w, say, d=1, x=None, e=None, h=None, text=None):
    """Savol matnida inglizcha qism bor — u ingliz ovozida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, text=text, say=say, lang="en")


def ENW(uz, a, w, d=1, x=None, e=None):
    """“dushanba” inglizcha qanday? (inglizcha so‘zni o‘qib tanlash)"""
    return Q(f"“{uz}” inglizcha qanday?", a, w, d=d, x=x or f"{uz} — {a}", e=e)


def FORM(word, what, a, w, d=1, x=None):
    """“cat” so‘zining ko‘plik shakli — so‘z ingliz ovozida aytiladi."""
    return Q(f"“{word}” {what}", a, w, d=d, x=x or f"{word} → {a}", say=word, lang="en")


def TFE(q, a, say, d=1, x=None, e=None, text=None):
    return TF(q, a, d=d, x=x, e=e, text=text, say=say, lang="en")


def GAP(sentence, a, w, d=1, x=None, note=None, e=None, h=None):
    """Bo‘sh joyli inglizcha gap: ekranda ko‘rsatma + gap, ovozda — faqat gap (ingliz tilida)."""
    q = f"Bo‘sh joyga mos so‘zni tanlang: {sentence}" + (f" ({note})" if note else "")
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=sentence, lang="en")


def SENT(en, d=1, x=None, q="So‘zlardan gap tuzing"):
    """Inglizcha gap tuzish (tinish belgisiz, javob ovozda aytilmaydi)."""
    return ORDER(q, en, d=d, x=x, lang="en")


def QSENT(en, d=1, x=None):
    return SENT(en, d=d, x=x, q="So‘zlardan savol tuzing")


def LET(letter, wrong, d=1):
    """Harf nomini tinglab, harfni topish."""
    return Q("Tinglang va harfni toping", letter, wrong, d=d, x=f"{letter} {letter.lower()} harfi [{NAMES[letter]}] deb aytiladi.",
             say=f"Find the letter {letter}.", lang="en")


def FS(letter, word, wrong, d=1):
    """Shu harf bilan boshlanadigan rasmni topish."""
    return Q(f"“{letter}” harfi bilan boshlanadigan rasmni toping", _pic(word), [_pic(k) for k in wrong], d=d,
             x=f"{word} — {VOC[word][1]} {_pic(word)}: birinchi harfi {letter}.",
             say=f"Which one starts with {letter}?", lang="en")


def FL(word, letter, wrong, d=1, x=None):
    """So‘z eshitiladi (rasmi ko‘rinadi) — birinchi harfini topish."""
    return Q("Tinglang: so‘z qaysi harf bilan boshlanadi?", letter, wrong, d=d, e=_pic(word),
             x=x or f"{word} — {VOC[word][1]}: birinchi harfi {letter}.", say=word, lang="en")


def NUM(word, number, wrong, d=1, say=None):
    return Q("Tinglang va sonni toping", number, wrong, d=d, x=f"{say or word} — {number}", say=say or word,
             lang="en")


def DAY(day, a, w, d=1, say=None):
    return Q("Tinglang: qaysi kun?", a, w, d=d, x=f"{day} — {a}", say=say or day, lang="en")


# ============================================================ 1-chorak
T.topic("alphabet", "🔤", L("Ingliz alifbosi", "The alphabet", "Английский алфавит"),
        chapter=C1,
        theory="Ingliz alifbosida 26 ta harf bor: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.\n"
               "Har bir harfning bosh va kichik shakli bor: A a, B b, G g, Q q.\n"
               "Harflarning nomi o‘zbekchadan boshqacha: A — [ey], E — [i:], I — [ay], G — [ji:], J — [jey],\n"
               "H — [eych], R — [a:], W — [dabl yu:], Y — [uay].\n"
               "Unli harflar: A, E, I, O, U.",
        items=[
            LET("B", ["D", "P"]),
            LET("M", ["N", "W"]),
            LET("S", ["X", "Z"]),
            LET("T", ["D", "B"]),
            LET("O", ["U", "A"]),
            LET("F", ["S", "H"]),
            EN("Tinglang: qaysi harf tushib qoldi?", "C", ["E", "G", "O"], say="A, B, ..., D", x="A, B, C, D."),
            Q("Ingliz alifbosining birinchi harfi qaysi?", "A", ["B", "Z", "O"], x="Alifbo A harfi bilan boshlanadi."),
            Q("Ingliz alifbosining oxirgi harfi qaysi?", "Z", ["Y", "X", "A"], x="Alifbo Z harfi bilan tugaydi."),
            TF("Ingliz alifbosida “O‘” harfi yo‘q.", True,
               x="To‘g‘ri: O‘ va G‘ harflari o‘zbek alifbosida bor, ingliz alifbosida esa yo‘q."),
            LET("A", ["E", "I"], d=2),
            LET("E", ["I", "A"], d=2),
            LET("G", ["J", "Z"], d=2),
            LET("J", ["G", "K"], d=2),
            EN("Tinglang: qaysi harf tushib qoldi?", "F", ["G", "H", "B"], say="D, E, ..., G", d=2, x="D, E, F, G."),
            Q("Ingliz alifbosida nechta harf bor?", "26", ["24", "29", "33"], d=2, x="Ingliz alifbosida 26 ta harf bor."),
            MATCH("Bosh va kichik harfni juftlang",
                  [("A", "a"), ("B", "b"), ("D", "d"), ("G", "g"), ("Q", "q"), ("R", "r")], d=2, lang="en"),
            MATCH("Kichik harfni bosh harf bilan juftlang",
                  [("e", "E"), ("h", "H"), ("l", "L"), ("n", "N"), ("t", "T"), ("y", "Y")], d=2, lang="en"),
            Q("Qaysi harf unli?", "E", ["B", "K", "T"], d=2, x="Unli harflar: A, E, I, O, U."),
            ORDER("Harflarni alifbo tartibida qo‘ying", "A B C D", d=2, lang="en", x="A, B, C, D."),
            TFE("Tinglang: bu “G” harfi.", False, say="The letter J.", d=2,
                x="Bu J harfi [jey]. G harfi esa [ji:] deb aytiladi."),
            LET("H", ["A", "K"], d=3),
            LET("W", ["U", "V"], d=3),
            LET("Y", ["I", "W"], d=3),
            EN("Tinglang: qaysi harf tushib qoldi?", "Y", ["W", "V", "U"], say="X, ..., Z", d=3, x="X, Y, Z."),
            Q("Qaysi harf unli emas?", "M", ["A", "O", "U"], d=3, x="M — undosh harf; A, O, U — unli harflar."),
            Q("Qaysi harf ingliz alifbosida bor, lekin o‘zbek alifbosida yo‘q?", "W", ["A", "M", "B"], d=3,
              x="W harfi o‘zbek lotin alifbosida yo‘q; A, M, B esa ikkala alifboda ham bor."),
            ORDER("Harflarni alifbo tartibida qo‘ying", "W X Y Z", d=3, lang="en", x="W, X, Y, Z."),
        ])

T.topic("first_sounds", "👂", L("Harf va birinchi tovush", "First sounds", "Первый звук в слове"),
        chapter=C1, prereq=["alphabet"],
        theory="So‘z boshidagi harf ko‘pincha so‘zning birinchi tovushini beradi:\n"
               "• B — bee 🐝, bus 🚌;  D — duck 🦆, door 🚪;  F — frog 🐸, fish 🐟.\n"
               "• M — moon 🌙, monkey 🐵;  S — sun ☀️, snake 🐍;  T — train 🚂, tiger 🐯.\n"
               "• C ko‘pincha [k] deb o‘qiladi: cow 🐮, cake 🍰, cat 🐱.\n"
               "So‘zni ichingizda ayting va birinchi tovushni eshiting: fish — F.",
        items=[
            FS("B", "bee", ["sun", "moon"]),
            FS("D", "duck", ["fish", "cow"]),
            FS("F", "fish", ["bee", "lion"]),
            FS("M", "moon", ["sun", "tiger"]),
            FS("S", "sun", ["moon", "duck"]),
            FS("T", "train", ["bus", "rabbit"]),
            FS("L", "lion", ["tiger", "bee"]),
            FL("dog", "D", ["B", "P"]),
            FL("sun", "S", ["Z", "T"]),
            FL("moon", "M", ["N", "W"]),
            FL("tiger", "T", ["D", "P"]),
            TFE("“fish” so‘zi “F” harfi bilan boshlanadi.", True, say="fish", e="🐟", x="To‘g‘ri: fish — F."),
            TFE("“zebra” so‘zi “Z” harfi bilan boshlanadi.", True, say="zebra", e="🦓", x="To‘g‘ri: zebra — Z."),
            FS("H", "hat", ["cake", "sun"], d=2),
            FS("P", "pen", ["bus", "lemon"], d=2),
            FS("Z", "zebra", ["snake", "sun"], d=2),
            FS("G", "goat", ["duck", "moon"], d=2),
            FS("A", "apple", ["egg", "umbrella"], d=2),
            FL("bus", "B", ["P", "D"], d=2),
            FL("horse", "H", ["A", "K"], d=2),
            TFE("“cow” so‘zi “K” harfi bilan boshlanadi.", False, say="cow", e="🐮", d=2,
                x="cow C harfi bilan yoziladi, lekin [k] deb o‘qiladi: cow, cake, cat."),
            MATCH("Harfni rasmga moslang",
                  [("B", "🐝"), ("D", "🦆"), ("F", "🐸"), ("M", "🐵"), ("S", "🐍"), ("T", "🐯")], d=2, lang="en"),
            MATCH("Rasmni birinchi harfi bilan juftlang",
                  [("🍎", "A"), ("🥚", "E"), ("🦁", "L"), ("🤖", "R"), ("🚪", "D"), ("☀️", "S")], d=2, lang="en"),
            FS("U", "umbrella", ["apple", "egg"], d=3),
            FL("cat", "C", ["K", "S", "G"], d=3,
               x="cat C harfi bilan yoziladi, lekin [k] deb o‘qiladi."),
            Q("Rasmga qarang: bu inglizcha so‘z qaysi harf bilan boshlanadi?", "S", ["Z", "T", "N"], d=3, e="🐍",
              x="snake (ilon) — S."),
            EN("Tinglang: qaysi so‘z shu so‘z bilan bir xil harfdan boshlanadi?", "bag", ["dog", "pen", "cat"],
               say="ball", d=3, x="ball va bag — ikkalasi ham B bilan boshlanadi."),
        ])

T.topic("numbers", "🔢", L("Sonlar 1–20", "Numbers 1–20", "Числа 1–20"),
        chapter=C1,
        theory="1–10: one, two, three, four, five, six, seven, eight, nine, ten.\n"
               "11 — eleven, 12 — twelve, 13 — thirteen, 14 — fourteen, 15 — fifteen,\n"
               "16 — sixteen, 17 — seventeen, 18 — eighteen, 19 — nineteen, 20 — twenty.\n"
               "13 dan 19 gacha sonlar oxirida -teen bor: fourteen (14), sixteen (16).\n"
               "How many? — Nechta? — Twelve pencils. — O‘n ikkita qalam.",
        items=[
            NUM("eleven", "11", ["7", "17"]),
            NUM("twelve", "12", ["20", "2"], say="twelve pencils"),
            NUM("fourteen", "14", ["4", "15"]),
            NUM("sixteen", "16", ["6", "19"]),
            NUM("eighteen", "18", ["8", "13"]),
            NUM("twenty", "20", ["12", "2"], say="twenty stars"),
            NUM("nineteen", "19", ["9", "15"]),
            NUM("ten", "10", ["1", "11"]),
            TFE("“sixteen” — 16 degani.", True, say="sixteen", x="To‘g‘ri: sixteen — 16."),
            TFE("“twelve” — 20 degani.", False, say="twelve", x="twelve — 12; 20 esa — twenty."),
            NUM("thirteen", "13", ["3", "18"], d=2, say="thirteen birds"),
            NUM("seventeen", "17", ["7", "11"], d=2),
            NUM("fifteen", "15", ["5", "16"], d=2, say="fifteen balls"),
            Q("Sanang: nechta? Inglizcha tanlang", "twelve", ["eleven", "twenty", "ten"], d=2,
              text="⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐", x="12 ta yulduz — twelve."),
            EN("Tinglang va hisoblang", "15", ["14", "16", "5"], say="ten plus five", d=2,
               x="ten plus five — 10 + 5 = 15."),
            EN("Tinglang va hisoblang", "12", ["11", "13", "20"], say="six plus six", d=2,
               x="six plus six — 6 + 6 = 12."),
            EN("Tinglang: qaysi son tushib qoldi?", "14", ["15", "13", "4"], say="twelve, thirteen, ..., fifteen", d=2,
               x="12, 13, 14, 15 — fourteen."),
            EN("Tinglang: qaysi son tushib qoldi?", "17", ["16", "7", "19"], say="sixteen, ..., eighteen", d=2,
               x="16, 17, 18 — seventeen."),
            Q("18 inglizcha qanday?", "eighteen", ["eighty", "eight", "thirteen"], d=2, x="18 — eighteen."),
            MATCH("Son va so‘zni juftlang",
                  [("15", "fifteen"), ("17", "seventeen"), ("18", "eighteen"), ("20", "twenty"), ("10", "ten"),
                   ("12", "twelve")], d=2, lang="en"),
            TFE("Tinglang: son to‘g‘rimi?", True, say="seven chicks", text="🐤 🐤 🐤 🐤 🐤 🐤 🐤", d=2,
                x="To‘g‘ri: 7 ta jo‘ja — seven chicks."),
            Q("Sanang: nechta? Inglizcha tanlang", "eleven", ["seven", "twelve", "nine"], d=3,
              text="🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎 🍎", x="11 ta olma — eleven."),
            EN("Tinglang va hisoblang", "20", ["19", "12", "18"], say="eleven plus nine", d=3,
               x="eleven plus nine — 11 + 9 = 20."),
            EN("Tinglang va hisoblang", "10", ["9", "11", "20"], say="twenty minus ten", d=3,
               x="twenty minus ten — 20 − 10 = 10."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "twelve", ["twelf", "twelwe", "tvelve"], d=3, x="12 — twelve."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "eleven", ["elewen", "eleeven", "elevn"], d=3, x="11 — eleven."),
        ])

T.topic("about_me", "🙋", L("Men haqimda", "About me", "Обо мне"),
        chapter=C1, prereq=["numbers"],
        theory="What is your name? — Isming nima? — My name is Aziza. — Mening ismim Aziza.\n"
               "How old are you? — Necha yoshdasan? — I am eight. (I am eight years old.) — Men sakkiz yoshdaman.\n"
               "Where are you from? — Qayerdansan? — I am from Uzbekistan. — Men O‘zbekistondanman.\n"
               "I am a pupil. 🎒 — Men o‘quvchiman.",
        items=[
            EN("Tinglang: bola necha yoshda?", "8", ["7", "9", "18"], say="I am eight.",
               x="I am eight. — Men sakkiz yoshdaman."),
            EN("Tinglang: bola necha yoshda?", "7", ["6", "8", "17"], say="I'm seven years old.",
               x="I'm seven years old. — Men yetti yoshdaman."),
            EN("Tinglang: bola necha yoshda?", "9", ["5", "19", "8"], say="I am nine years old.",
               x="I am nine years old. — Men to‘qqiz yoshdaman."),
            EN("Tinglang: qizning ismi nima?", "Madina", ["Malika", "Mohira", "Munisa"], say="Hi! My name is Madina.",
               x="My name is Madina. — Mening ismim Madina."),
            EN("Tinglang: bola qayerdan?", "O‘zbekistondan", ["Angliyadan", "Rossiyadan", "Turkiyadan"],
               say="I am from Uzbekistan.", x="I am from Uzbekistan. — Men O‘zbekistondanman."),
            LISTEN("Where are you from?", "Qayerdansan?", ["Necha yoshdasan?", "Isming nima?", "Qalaysan?"]),
            EN("Tinglang: bu savolda nima so‘ralyapti?", "yosh", ["ism", "kayfiyat"], say="How old are you?",
               x="How old are you? — Necha yoshdasan? (old — yosh)"),
            EN("Tinglang: bu savolda nima so‘ralyapti?", "ism", ["yosh", "kayfiyat"], say="What is your name?",
               x="What is your name? — Isming nima? (name — ism)"),
            TFE("“I am eight.” — “Men sakkiz yoshdaman.” degani.", True, say="I am eight.",
                x="To‘g‘ri: eight — sakkiz."),
            EN("Tinglang: bola qayerdan?", "Angliyadan", ["O‘zbekistondan", "Rossiyadan", "Qozog‘istondan"],
               say="I am from England.", d=2, x="I am from England. — Men Angliyadanman."),
            LISTEN("I am a pupil.", "Men o‘quvchiman.", ["Men o‘qituvchiman.", "Men chaqaloqman.", "Men shifokorman."],
                   d=2),
            EN("Tinglang va javobni tanlang", "I am seven.", ["I am Ali.", "I am fine.", "I am from Tashkent."],
               say="How old are you?", d=2, x="Yosh so‘ralsa: I am seven. — Men yetti yoshdaman."),
            EN("Tinglang va javobni tanlang", "I am from Uzbekistan.",
               ["I am eight.", "My name is Jamshid.", "I am fine, thanks."], say="Where are you from?", d=2,
               x="Qayerdanligi so‘ralsa: I am from … — Men …danman."),
            EN("Tinglang va javobni tanlang", "My name is Umid.", ["I am seven.", "I am from Samarkand.", "Thank you!"],
               say="What is your name?", d=2, x="Ism so‘ralsa: My name is …"),
            GAP("I ... eight.", "am", ["is", "are", "my"], d=2, x="I bilan am ishlatiladi: I am eight."),
            GAP("I am ... Uzbekistan.", "from", ["name", "old", "is"], d=2,
                x="I am from Uzbekistan. — Men O‘zbekistondanman."),
            TFE("“Where are you from?” — “Isming nima?” degani.", False, say="Where are you from?", d=2,
                x="Where are you from? — Qayerdansan? Isming nima? esa — What is your name?"),
            SENT("I am eight", d=2, x="I am eight. — Men sakkiz yoshdaman."),
            SENT("I am from Tashkent", d=2, x="I am from Tashkent. — Men Toshkentdanman."),
            MATCH("Savolni javobi bilan juftlang",
                  [("What is your name?", "My name is Aziz."), ("How old are you?", "I am eight."),
                   ("Where are you from?", "I am from Uzbekistan."), ("How are you?", "I am fine."),
                   ("Nice to meet you!", "Nice to meet you too!")], d=3, lang="en"),
            QSENT("Where are you from", d=3, x="Where are you from? — Qayerdansan?"),
            Q("“Men yetti yoshdaman.” inglizcha qanday?", "I am seven.", ["I is seven.", "I seven am.", "I am seventeen."],
              d=3, x="yetti — seven: I am seven."),
            Q("Qaysi gap to‘g‘ri?", "I am from Bukhara.", ["I from am Bukhara.", "I is from Bukhara.", "I am Bukhara from."],
              d=3, x="To‘g‘ri tartib: I am from Bukhara. — Men Buxorodanman."),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["alphabet", "first_sounds", "numbers", "about_me"], chapter=C1)

# ============================================================ 2-chorak
DAY_ORDER = "Kunlarni tartib bilan qo‘ying"
NEXT_DAY = "Tinglang: bu kundan keyin qaysi kun keladi?"

T.topic("days", "📅", L("Hafta kunlari", "Days of the week", "Дни недели"),
        chapter=C2,
        theory="Hafta kunlari (days of the week) doim bosh harf bilan yoziladi:\n"
               "Monday — dushanba, Tuesday — seshanba, Wednesday — chorshanba, Thursday — payshanba,\n"
               "Friday — juma, Saturday — shanba, Sunday — yakshanba.\n"
               "Adashtirmang: Tuesday (seshanba) — Thursday (payshanba).\n"
               "Today is Monday. — Bugun dushanba.",
        items=[
            DAY("Monday", "dushanba", ["seshanba", "yakshanba"]),
            DAY("Tuesday", "seshanba", ["payshanba", "juma"]),
            DAY("Wednesday", "chorshanba", ["dushanba", "shanba"], say="It is Wednesday."),
            DAY("Thursday", "payshanba", ["seshanba", "yakshanba"]),
            DAY("Friday", "juma", ["shanba", "dushanba"]),
            DAY("Saturday", "shanba", ["yakshanba", "chorshanba"]),
            DAY("Sunday", "yakshanba", ["shanba", "juma"], say="It is Sunday."),
            TFE("“Saturday” — shanba.", True, say="Saturday", x="To‘g‘ri: Saturday — shanba."),
            TFE("“Tuesday” — payshanba.", False, say="Tuesday", d=2,
                x="Tuesday — seshanba; payshanba esa — Thursday."),
            EN(NEXT_DAY, "Wednesday", ["Monday", "Friday", "Sunday"], say="Tuesday", d=2,
               x="Tuesday, Wednesday — seshanbadan keyin chorshanba."),
            EN(NEXT_DAY, "Monday", ["Saturday", "Tuesday", "Friday"], say="Sunday", d=2,
               x="Sunday, Monday — yakshanbadan keyin dushanba."),
            EN("Tinglang: qaysi kun tushib qoldi?", "Thursday", ["Tuesday", "Monday", "Sunday"],
               say="Tuesday, Wednesday, ..., Friday", d=2, x="Tuesday, Wednesday, Thursday, Friday."),
            EN("Tinglang: nechta kun aytildi?", "3", ["2", "4", "5"], say="Monday, Tuesday, Wednesday", d=2,
               x="Monday, Tuesday, Wednesday — uchta kun."),
            ORDER(DAY_ORDER, "Monday Tuesday Wednesday Thursday", d=2, lang="en",
                  x="Monday, Tuesday, Wednesday, Thursday."),
            ORDER(DAY_ORDER, "Friday Saturday Sunday", d=2, lang="en", x="Friday, Saturday, Sunday."),
            LISTEN("Today is Sunday.", "Bugun yakshanba.", ["Bugun shanba.", "Ertaga yakshanba.", "Bugun dushanba."], d=2),
            Q("Qaysi kun “W” harfi bilan boshlanadi?", "Wednesday", ["Monday", "Friday", "Tuesday"], d=2,
              x="Wednesday — chorshanba; W bilan boshlanadi."),
            ENW("payshanba", "Thursday", ["Tuesday", "Saturday", "Sunday"], d=2),
            Q("Yakshanba — dam olish kuni. “Yakshanba” inglizcha qanday?", "Sunday", ["Monday", "Saturday", "Friday"],
              d=2, x="yakshanba — Sunday."),
            SENT("I like Saturday", d=2, x="I like Saturday. — Men shanbani yaxshi ko‘raman."),
            MATCH("Kunni undan keyingi kun bilan juftlang",
                  [("Monday", "Tuesday"), ("Wednesday", "Thursday"), ("Friday", "Saturday"), ("Saturday", "Sunday"),
                   ("Sunday", "Monday")], d=3, lang="en"),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "Tuesday", ["Tusday", "Tuesdey", "tuesday"], d=3,
              x="Tuesday — t-u-e-s-d-a-y; kun nomi bosh harf bilan yoziladi."),
            LISTEN("See you on Monday!", "Dushanba kuni ko‘rishamiz!",
                   ["Juma kuni ko‘rishamiz!", "Bugun dushanba.", "Dushanba kuni dam olamiz."], d=3),
        ])

WEATHER_NEED = "Tinglang: bunday havoda nima kerak bo‘ladi?"

T.topic("weather", "🌦️", L("Ob-havo", "Weather", "Погода"),
        chapter=C2,
        theory="What's the weather like? — Havo qanday?\n"
               "It's sunny. ☀️ — Havo quyoshli.  It's rainy. 🌧️ — Yomg‘ir yog‘yapti.\n"
               "It's cloudy. ☁️ — Havo bulutli.  It's windy. 💨 — Shamol esyapti.  It's snowy. ❄️ — Qor yog‘yapti.\n"
               "It's hot. — Havo issiq.  It's cold. — Havo sovuq.\n"
               "rainbow 🌈 — kamalak, snowman ⛄ — qor odam, umbrella ☂️ — soyabon.",
        items=[
            PIC("sunny", ["rainy", "snowy"], say="It's sunny.", x="It's sunny. — Havo quyoshli. ☀️"),
            PIC("rainy", ["sunny", "windy"], say="It's rainy.", x="It's rainy. — Yomg‘ir yog‘yapti. 🌧️"),
            PIC("cloudy", ["snowy", "sunny"], say="It's cloudy.", x="It's cloudy. — Havo bulutli. ☁️"),
            PIC("windy", ["cloudy", "rainy"], say="It's windy.", x="It's windy. — Shamol esyapti. 💨"),
            PIC("snowy", ["sunny", "rainy"], say="It's snowy.", x="It's snowy. — Qor yog‘yapti. ❄️"),
            LISTEN("It's hot.", "Havo issiq.", ["Havo sovuq.", "Havo bulutli.", "Qor yog‘yapti."]),
            LISTEN("It's cold.", "Havo sovuq.", ["Havo issiq.", "Havo quyoshli.", "Shamol esyapti."]),
            SAME("sunny", "sunny"),
            SAME("snowy", "rainy"),
            PIC("rainbow", ["sunny", "cloudy"], d=2),
            PIC("snowman", ["rainbow", "umbrella"], d=2),
            PIC("umbrella", ["rainbow", "snowman"], d=2),
            EN(WEATHER_NEED, "☂️", ["🕶️", "⚽"], say="It's rainy.", d=2,
               x="Yomg‘irda soyabon (umbrella) kerak. ☂️"),
            EN(WEATHER_NEED, "🧤", ["🕶️", "🍦"], say="It's snowy and cold.", d=2,
               x="Qorli sovuq kunda qo‘lqop (gloves) kerak. 🧤"),
            EN(WEATHER_NEED, "🕶️", ["☂️", "🧤"], say="It's sunny and hot.", d=2,
               x="Quyoshli issiq kunda quyosh ko‘zoynagi kerak. 🕶️"),
            MATCHE(["sunny", "rainy", "cloudy", "windy", "snowy", "rainbow"]),
            MATCHU(["hot", "cold", "sunny", "cloudy", "windy", "rainy"]),
            GAP("It's ... today.", "sunny", ["snowy", "rainy", "windy"], d=2, e="☀️",
                x="Rasmda quyosh: It's sunny today. — Bugun havo quyoshli."),
            GAP("It's ... today.", "snowy", ["sunny", "hot", "cloudy"], d=2, e="❄️",
                x="Rasmda qor: It's snowy today. — Bugun qor yog‘yapti."),
            LISTEN("What's the weather like?", "Havo qanday?", ["Soat necha?", "Bugun qaysi kun?", "Isming nima?"], d=2),
            SENT("It is rainy today", d=2, x="It is rainy today. — Bugun yomg‘ir yog‘yapti."),
            Q("Yozda O‘zbekistonda havo qanday bo‘ladi? Inglizcha tanlang", "It's hot.",
              ["It's snowy.", "It's cold.", "It's snowy and cold."], d=2,
              x="O‘zbekistonda yoz issiq bo‘ladi — It's hot."),
            SENT("It is very cold", d=3, x="It is very cold. — Havo juda sovuq."),
            Q("Qaysi so‘z ob-havo haqida emas?", "banana", ["sunny", "windy", "cloudy"], d=3,
              x="banana — banan; sunny, windy, cloudy — ob-havo so‘zlari."),
            EN("Tinglang: qaysi rasm mos?", "🌈", ["❄️", "💨"], say="Look! A rainbow!", d=3,
               x="Look! A rainbow! — Qara! Kamalak! 🌈"),
        ])

COLOUR_ASK = "Rasmga qarang va tinglang. Javob qaysi?"

T.topic("clothes", "👕", L("Kiyimlar va ranglar", "Clothes and colours", "Одежда и цвета"),
        chapter=C2,
        theory="Kiyimlar (clothes): T-shirt 👕 — futbolka, trousers 👖 — shim, dress 👗 — ko‘ylak, skirt — yubka.\n"
               "hat 👒 — shlyapa, cap 🧢 — kepka, coat 🧥 — palto, scarf 🧣 — sharf, gloves 🧤 — qo‘lqop.\n"
               "shoes 👟 — poyabzal, boots 👢 — etik, socks 🧦 — paypoq.\n"
               "What colour is it? — U qanday rangda? — It's blue. — U ko‘k.\n"
               "Avval rang, keyin narsa: a red dress — qizil ko‘ylak, green socks — yashil paypoq.",
        items=[
            PIC("T-shirt", ["dress", "coat"]),
            PIC("trousers", ["socks", "T-shirt"]),
            PIC("dress", ["T-shirt", "hat"]),
            PIC("hat", ["socks", "gloves"]),
            PIC("coat", ["dress", "trousers"]),
            PIC("socks", ["gloves", "boots"]),
            PIC("gloves", ["socks", "scarf"]),
            TR("skirt", ["trousers", "dress"]),
            SAME("coat", "coat"),
            SAME("socks", "gloves"),
            PIC("cap", ["hat", "scarf"], d=2),
            PIC("scarf", ["gloves", "coat"], d=2),
            PIC("boots", ["shoes", "socks"], d=2),
            PIC("shoes", ["boots", "gloves"], d=2),
            LISTEN("a red dress", "qizil ko‘ylak", ["qizil shlyapa", "ko‘k ko‘ylak", "sariq ko‘ylak"], d=2),
            LISTEN("green socks", "yashil paypoq", ["yashil sharf", "qora paypoq", "yashil etik"], d=2),
            EN(COLOUR_ASK, "It's yellow.", ["It's blue.", "It's green.", "It's black."], say="What colour is it?",
               e="🍌", d=2, x="Banan sariq: It's yellow."),
            EN(COLOUR_ASK, "It's green.", ["It's red.", "It's white.", "It's pink."], say="What colour is it?",
               e="🐸", d=2, x="Qurbaqa yashil: It's green."),
            GAP("What ... is it? — It's green.", "colour", ["name", "old", "is"], d=2,
                x="What colour is it? — U qanday rangda?"),
            MATCHE(["T-shirt", "trousers", "dress", "coat", "scarf", "socks", "boots"], q="Kiyimni rasmga moslang"),
            Q("Qo‘lga nima kiyamiz? Inglizcha tanlang", "gloves", ["socks", "boots", "a cap"], d=2,
              x="Qo‘lga qo‘lqop kiyamiz — gloves. 🧤"),
            Q("Boshga nima kiyamiz? Inglizcha tanlang", "a hat", ["socks", "gloves", "trousers"], d=2,
              x="Boshga shlyapa kiyamiz — a hat. 👒"),
            SENT("My hat is red", d=2, x="My hat is red. — Mening shlyapam qizil."),
            QSENT("What colour is it", d=2, x="What colour is it? — U qanday rangda?"),
            GAP("My ... are black.", "shoes", ["hat", "coat", "dress"], d=3,
                x="are — ko‘plik uchun: shoes (poyabzal) ko‘plikda. My shoes are black."),
            Q("Bo‘yinga nima o‘raymiz? Inglizcha tanlang", "a scarf", ["a hat", "socks", "boots"], d=3,
              x="Bo‘yinga sharf o‘raymiz — a scarf. 🧣"),
            EN("Tinglang: qaysi kiyim kerak?", "🧥", ["👕", "👗"], say="It's cold. Put on your coat!", d=3,
               x="Put on your coat! — Paltongizni kiying! 🧥"),
            Q("“Qizil ko‘ylak” inglizcha qanday?", "a red dress", ["a dress red", "red a dress", "a dress is red"], d=3,
              x="Avval rang, keyin narsa: a red dress."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["days", "weather", "clothes", "numbers"], chapter=C2)

# ============================================================ 3-chorak
ROOM_DO = "Tinglang: bu xonada nima qilamiz?"

T.topic("house", "🏠", L("Mening uyim", "My house", "Мой дом"),
        chapter=C3,
        theory="My house 🏠 — mening uyim. Xonalar (rooms):\n"
               "kitchen — oshxona, bedroom — yotoqxona, bathroom — vannaxona, living room — mehmonxona.\n"
               "garden — bog‘, door 🚪 — eshik, window — deraza.\n"
               "Narsalar: bed 🛏️ — karavot, bath 🛁 — vanna, sofa 🛋️ — divan, TV 📺 — televizor,\n"
               "table — stol, chair — stul.  Mum is in the kitchen. — Onam oshxonada.",
        items=[
            PIC("house", ["door", "bed"]),
            PIC("door", ["bed", "bath"]),
            PIC("bed", ["sofa", "bath"]),
            PIC("bath", ["bed", "TV"]),
            PIC("sofa", ["bed", "door"]),
            PIC("TV", ["door", "sofa"]),
            TR("kitchen", ["bedroom", "garden"]),
            TR("bedroom", ["kitchen", "bathroom"]),
            TR("window", ["door", "table"]),
            SAME("bed", "bed"),
            SAME("door", "sofa"),
            TR("bathroom", ["bedroom", "living room"], d=2),
            TR("living room", ["kitchen", "bathroom"], d=2),
            TR("garden", ["house", "room"], d=2),
            TR("table", ["chair", "window"], d=2),
            TR("chair", ["table", "door"], d=2),
            EN(ROOM_DO, "ovqat pishiramiz", ["uxlaymiz", "yuvinamiz"], say="kitchen", d=2,
               x="kitchen — oshxona. Oshxonada ovqat pishiramiz."),
            EN(ROOM_DO, "uxlaymiz", ["ovqat pishiramiz", "yuvinamiz"], say="bedroom", d=2,
               x="bedroom — yotoqxona. Yotoqxonada uxlaymiz."),
            LISTEN("Mum is in the kitchen.", "Onam oshxonada.", ["Onam bog‘da.", "Dadam oshxonada.", "Onam yotoqxonada."],
                   d=2),
            LISTEN("The cat is in the garden.", "Mushuk bog‘da.", ["Mushuk oshxonada.", "It bog‘da.", "Mushuk karavotda."],
                   d=2),
            MATCHE(["door", "bed", "sofa", "TV", "house", "bath"], q="Narsani rasmga moslang"),
            MATCHU(["kitchen", "bedroom", "bathroom", "garden", "window", "table"]),
            GAP("Dad is ... the garden.", "in", ["on", "under", "is"], d=2,
                x="Xona yoki bog‘ ichida — in: in the garden."),
            SENT("This is my house", d=2, x="This is my house. — Bu mening uyim."),
            SENT("My room is big", d=2, x="My room is big. — Mening xonam katta."),
            EN(ROOM_DO, "yuvinamiz", ["uxlaymiz", "ovqat pishiramiz"], say="bathroom", d=3,
               x="bathroom — vannaxona. Vannaxonada yuvinamiz."),
            Q("Qaysi so‘z xona emas?", "apple", ["kitchen", "bedroom", "bathroom"], d=3,
              x="apple — olma; qolganlari xonalar."),
            Q("“Buvim bog‘da.” inglizcha qanday?", "Granny is in the garden.",
              ["Granny is in the kitchen.", "Granny is the garden.", "Granny in is the garden."], d=3,
              x="bog‘da — in the garden."),
        ])

T.topic("food", "🍞", L("Taomlar: I like / I don't like", "Food: I like / I don't like", "Еда: I like / I don't like"),
        chapter=C3,
        theory="Taomlar (food): bread 🍞 — non, egg 🥚 — tuxum, cheese 🧀 — pishloq, soup 🍲 — sho‘rva, rice 🍚 — guruch.\n"
               "meat 🍖 — go‘sht, cake 🍰 — tort, ice cream 🍦 — muzqaymoq, honey 🍯 — asal, chocolate 🍫 — shokolad.\n"
               "Ichimliklar (drinks): milk 🥛 — sut, tea 🍵 — choy, water 💧 — suv, juice — sharbat.\n"
               "I like milk. — Men sutni yaxshi ko‘raman.\n"
               "I don't like soup. — Men sho‘rvani yoqtirmayman.",
        items=[
            PIC("bread", ["cheese", "cake"]),
            PIC("milk", ["tea", "water"]),
            PIC("egg", ["bread", "cheese"]),
            PIC("cheese", ["bread", "cake"]),
            PIC("soup", ["rice", "tea"]),
            PIC("rice", ["soup", "bread"]),
            PIC("cake", ["bread", "ice cream"]),
            PIC("ice cream", ["cake", "chocolate"]),
            PIC("honey", ["milk", "cheese"]),
            SAME("milk", "milk"),
            SAME("cheese", "egg"),
            PIC("tea", ["milk", "soup"], d=2),
            PIC("water", ["milk", "tea"], d=2),
            PIC("meat", ["egg", "bread"], d=2),
            PIC("chocolate", ["cake", "honey"], d=2),
            TR("juice", ["water", "tea"], d=2),
            PIC("cheese", ["honey", "egg"], say="I like cheese.", d=2, x="I like cheese. — Men pishloqni yaxshi ko‘raman."),
            PIC("honey", ["cheese", "bread"], say="I like honey.", d=2, x="I like honey. — Men asalni yaxshi ko‘raman."),
            LISTEN("I don't like soup.", "Men sho‘rvani yoqtirmayman.",
                   ["Men sho‘rvani yaxshi ko‘raman.", "Menda sho‘rva bor.", "Men nonni yoqtirmayman."], d=2),
            LISTEN("I like ice cream.", "Men muzqaymoqni yaxshi ko‘raman.",
                   ["Men muzqaymoqni yoqtirmayman.", "Men tortni yaxshi ko‘raman.", "Menda muzqaymoq bor."], d=2),
            Q("Qaysi biri ichimlik?", "milk", ["bread", "cheese", "egg"], d=2, x="milk — sut, u ichimlik. 🥛"),
            GAP("I ... milk.", "like", ["am", "is", "are"], d=2, x="I like milk. — Men sutni yaxshi ko‘raman."),
            MATCHE(["bread", "milk", "egg", "cheese", "soup", "cake", "ice cream"], q="Taomni rasmga moslang"),
            MATCHU(["rice", "tea", "water", "meat", "honey", "juice"], q="Taomni tarjimasi bilan juftlang"),
            SENT("I like apples", d=2, x="I like apples. — Men olmani yaxshi ko‘raman."),
            Q("Qaysi biri ichimlik emas?", "rice", ["tea", "water", "milk"], d=3,
              x="rice — guruch; tea, water, milk — ichimliklar."),
            GAP("I don't ... fish.", "like", ["am", "is", "no"], d=3, x="I don't like fish. — Men baliqni yoqtirmayman."),
            SENT("I don't like tea", d=3, x="I don't like tea. — Men choyni yoqtirmayman."),
            EN("Tinglang: bola nimani yoqtirmaydi?", "🍲", ["🍰", "🍦"],
               say="I like cake and ice cream. I don't like soup.", d=3,
               x="I don't like soup. — Men sho‘rvani yoqtirmayman. 🍲"),
        ])

HAVE_Q = "Tinglang va rasmini toping"
HAVE_TF = "Tinglang: gap rasmga mosmi?"

T.topic("have", "🎁", L("I have: menda bor", "I have …", "У меня есть …"),
        chapter=C3,
        theory="I have … — Menda … bor.\n"
               "I have a cat. 🐱 — Mening mushugim bor.  I have a ball. ⚽ — Mening to‘pim bor.\n"
               "I have two brothers. — Mening ikkita akam (ukam) bor.\n"
               "Do you have a dog? — Sening iting bormi? — Yes, I do. — Ha, bor. / No, I don't. — Yo‘q.",
        items=[
            PIC("dog", ["cat", "rabbit"], say="I have a dog.", x="I have a dog. — Mening itim bor. 🐶"),
            PIC("ball", ["bike", "robot"], say="I have a ball.", x="I have a ball. — Mening to‘pim bor. ⚽"),
            PIC("bike", ["ball", "car"], say="I have a bike.", x="I have a bike. — Mening velosipedim bor. 🚲"),
            PIC("robot", ["ball", "book"], say="I have a robot.", x="I have a robot. — Mening robotim bor. 🤖"),
            PIC("fish", ["bird", "cat"], say="I have a fish.", x="I have a fish. — Mening baliqcham bor. 🐟"),
            PIC("book", ["ball", "bike"], say="I have a new book.", x="I have a new book. — Mening yangi kitobim bor. 📕"),
            TFE(HAVE_TF, True, say="I have a red car.", e="🚗", x="To‘g‘ri: I have a red car. — Mening qizil mashinam bor."),
            TFE(HAVE_TF, False, say="I have a bird.", e="🐟", x="Rasmda baliq — fish. bird esa — qush."),
            LISTEN("I have a rabbit.", "Mening quyonim bor.", ["Mening mushugim bor.", "Mening quyonim yo‘q.", "Uning quyoni bor."]),
            EN(HAVE_Q, "🐱🐱", ["🐱", "🐱🐱🐱"], say="I have two cats.", d=2,
               x="I have two cats. — Mening ikkita mushugim bor."),
            EN(HAVE_Q, "⚽⚽⚽", ["⚽", "⚽⚽"], say="I have three balls.", d=2,
               x="I have three balls. — Mening uchta to‘pim bor."),
            LISTEN("I have a sister.", "Mening opam (singlim) bor.", ["Mening akam bor.", "Mening opam yo‘q.", "Mening buvim bor."],
                   d=2),
            LISTEN("Do you have a cat?", "Sening mushuging bormi?", ["Mening mushugim bor.", "Mushuk qayerda?", "Bu mushukmi?"],
                   d=2),
            GAP("I ... a new bag.", "have", ["am", "is", "are"], d=2, x="I have a new bag. — Mening yangi sumkam bor."),
            MATCH("Gapni tarjimasi bilan juftlang",
                  [("I have a cat.", "Mening mushugim bor."), ("I have a dog.", "Mening itim bor."),
                   ("I have a ball.", "Mening to‘pim bor."), ("I have a bike.", "Mening velosipedim bor."),
                   ("I have a book.", "Mening kitobim bor.")], d=2, lang="en"),
            SENT("I have a dog", d=2, x="I have a dog. — Mening itim bor."),
            TFE("“I have a kite.” — “Mening varragim bor.” degani.", True, say="I have a kite.", d=2,
                x="To‘g‘ri: kite — varrak."),
            EN("Tinglang: bolada nechta qalam bor?", "3", ["2", "4", "5"], say="I have three pencils.", d=2,
               x="I have three pencils. — Mening uchta qalamim bor."),
            EN("Sizdan “Do you have a dog?” deb so‘rashdi. Itingiz bor. Javob qaysi?", "Yes, I do.",
               ["Yes, I am.", "Yes, it is.", "Yes, I can."], say="Do you have a dog?", d=3,
               x="Do you have …? savoliga: Yes, I do. / No, I don't."),
            Q("“Mening kitobim bor.” inglizcha qanday?", "I have a book.", ["I am a book.", "I like a book.", "It is a book."],
              d=3, x="Menda … bor — I have …"),
            Q("Qaysi gap to‘g‘ri?", "I have a red car.", ["I have a car red.", "I red have a car.", "I has a red car."], d=3,
              x="I have + rang + narsa: I have a red car."),
            SENT("I have two sisters", d=3, x="I have two sisters. — Mening ikkita opam (singlim) bor."),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["house", "food", "have", "clothes"], chapter=C3)

# ============================================================ 4-chorak
YN = "Rasmga qarang va tinglang. Javob qaysi?"
POINT = "Tinglang: bola nimani ko‘rsatyapti?"

T.topic("this_that", "👉", L("This va that: Bu nima?", "This and that", "This и that"),
        chapter=C4,
        theory="this — bu (yaqindagi, qo‘limdagi narsa): This is my pen. — Bu mening ruchkam.\n"
               "that — anavi (uzoqdagi narsa): That is a bird. — Anavi — qush.\n"
               "What is this? — Bu nima? — It is a ball. — Bu to‘p.\n"
               "Is it a cat? — Bu mushukmi? — Yes, it is. — Ha. / No, it isn't. — Yo‘q.",
        items=[
            EN(YN, "Yes, it is.", ["No, it isn't.", "Yes, I do.", "I am fine."], say="Is it a cat?", e="🐱",
               x="Rasmda mushuk: Yes, it is."),
            EN(YN, "No, it isn't.", ["Yes, it is.", "No, I don't.", "Yes, I can."], say="Is it a rabbit?", e="🐶",
               x="Rasmda it, quyon emas: No, it isn't."),
            EN(YN, "Yes, it is.", ["No, it isn't.", "Yes, I have.", "It is a cat."], say="Is it a fish?", e="🐟",
               x="Rasmda baliq: Yes, it is."),
            EN(YN, "No, it isn't.", ["Yes, it is.", "It is a banana.", "Yes, I do."], say="Is it a banana?", e="🍎",
               x="Rasmda olma, banan emas: No, it isn't."),
            EN(POINT, "🐦", ["🐶", "🐟"], say="That is a bird.", x="That is a bird. — Anavi — qush. 🐦"),
            EN(POINT, "✈️", ["🚗", "🚲"], say="That is a plane.", x="That is a plane. — Anavi — samolyot. ✈️"),
            EN(POINT, "🖊️", ["📕", "🎒"], say="This is my pen.", x="This is my pen. — Bu mening ruchkam. 🖊️"),
            TFE("“that” — uzoqdagi narsa uchun ishlatiladi.", True, say="that", x="To‘g‘ri: that — anavi (uzoqda)."),
            TFE("“this” — yaqindagi narsa uchun ishlatiladi.", True, say="this", x="To‘g‘ri: this — bu (yaqinda)."),
            EN("Rasmga qarang. Savolga javob bering", "It is a ball.", ["It is a doll.", "It is a dog.", "Yes, it is."],
               say="What is this?", e="⚽", d=2, x="What is this? — It is a ball. ⚽"),
            EN("Rasmga qarang. Savolga javob bering", "It is a bike.", ["It is a car.", "It is a bus.", "No, it isn't."],
               say="What is this?", e="🚲", d=2, x="What is this? — It is a bike. 🚲"),
            LISTEN("This is my pen.", "Bu mening ruchkam.", ["Anavi mening ruchkam.", "Bu mening qalamim.", "Bu sening ruchkang."],
                   d=2),
            LISTEN("That is a big tree.", "Anavi — katta daraxt.", ["Bu — kichik daraxt.", "Anavi — katta uy.", "Bu — katta daraxt."],
                   d=2),
            GAP("... is my pencil.", "This", ["That", "These", "Those"], note="qo‘limda, yaqinda", d=2,
                x="Yaqindagi narsa — this: This is my pencil."),
            GAP("... is the moon.", "That", ["This", "These", "Those"], note="uzoqda, osmonda", d=2,
                x="Uzoqdagi narsa — that: That is the moon."),
            Q("“Bu nima?” inglizcha qanday?", "What is this?", ["Who is this?", "What is that?", "Where is this?"], d=2,
              x="Bu nima? — What is this? Anavi nima? — What is that?"),
            TFE("“this” — “anavi” degani.", False, say="this", d=2, x="this — bu; anavi esa — that."),
            MATCH("So‘z va iborani tarjimasi bilan juftlang",
                  [("this", "bu"), ("that", "anavi"), ("What is this?", "Bu nima?"), ("What is that?", "Anavi nima?"),
                   ("Yes, it is.", "Ha, shunday."), ("No, it isn't.", "Yo‘q, unday emas.")], d=2, lang="en"),
            SENT("That is my cat", d=2, x="That is my cat. — Anavi — mening mushugim."),
            QSENT("What is this", d=2, x="What is this? — Bu nima?"),
            Q("“Anavi nima?” inglizcha qanday?", "What is that?", ["What is this?", "Who is that?", "Is that a cat?"], d=3,
              x="Anavi nima? — What is that?"),
            QSENT("Is it a dog", d=3, x="Is it a dog? — Bu itmi?"),
            EN(YN, "No, it isn't. It's a cat.", ["Yes, it is.", "No, it isn't. It's a cow.", "Yes, it's a dog."],
               say="Is it a dog?", e="🐱", d=3, x="Rasmda mushuk: No, it isn't. It's a cat."),
        ])

COUNT_Q = "Tinglang va rasmini toping"
PLURAL_TF = "Tinglang: bu so‘z ko‘plikdami (ko‘p narsa)?"

T.topic("plurals", "🎈", L("Bitta va ko‘p: cats, dogs", "One and many", "Один и много"),
        chapter=C4, prereq=["numbers"],
        theory="Bitta narsa: a cat 🐱, a book 📕, an apple 🍎.\n"
               "Ko‘p narsa — so‘z oxiriga -s qo‘shiladi: two cats 🐱🐱, three books, five apples.\n"
               "Ko‘plikda a / an qo‘yilmaydi: a ball — balls.\n"
               "How many? — Nechta? — How many dogs? — Four dogs. 🐶🐶🐶🐶",
        items=[
            EN(COUNT_Q, "🐱🐱", ["🐱", "🐱🐱🐱"], say="two cats", x="two cats — ikkita mushuk."),
            EN(COUNT_Q, "🐶🐶🐶", ["🐶🐶", "🐶"], say="three dogs", x="three dogs — uchta it."),
            EN(COUNT_Q, "🍎", ["🍎🍎", "🍎🍎🍎"], say="one apple", x="one apple — bitta olma."),
            EN(COUNT_Q, "⚽", ["⚽⚽", "⚽⚽⚽"], say="a ball", x="a ball — bitta to‘p (a — bitta)."),
            EN(COUNT_Q, "🐦🐦", ["🐦", "🐦🐦🐦"], say="two birds", x="two birds — ikkita qush."),
            EN(COUNT_Q, "🚗🚗🚗", ["🚗", "🚗🚗"], say="three cars", x="three cars — uchta mashina."),
            EN("Tinglang va sanang", "3", ["2", "4", "5"], say="How many apples?", text="🍎 🍎 🍎",
               x="How many apples? — Three apples."),
            EN("Tinglang va sanang", "5", ["4", "6", "3"], say="How many chicks?", text="🐤 🐤 🐤 🐤 🐤",
               x="How many chicks? — Five chicks."),
            EN("Tinglang va sanang", "2", ["3", "4", "1"], say="How many balloons?", text="🎈 🎈",
               x="How many balloons? — Two balloons."),
            TFE(PLURAL_TF, True, say="books", x="To‘g‘ri: books — kitoblar (oxirida -s)."),
            TFE(PLURAL_TF, False, say="pen", x="pen — bitta ruchka; ko‘pi — pens."),
            TFE(PLURAL_TF, True, say="apples", d=2, x="To‘g‘ri: apples — olmalar (oxirida -s)."),
            EN(COUNT_Q, "⭐⭐⭐⭐", ["⭐⭐⭐", "⭐⭐⭐⭐⭐"], say="four stars", d=2, x="four stars — to‘rtta yulduz."),
            FORM("cat", "so‘zining ko‘plik shakli qaysi?", "cats", ["cat", "cates", "a cats"], d=2,
                 x="Ko‘plikda -s qo‘shiladi: cat → cats."),
            FORM("pen", "so‘zining ko‘plik shakli qaysi?", "pens", ["pen", "penes", "a pens"], d=2,
                 x="Ko‘plikda -s qo‘shiladi: pen → pens."),
            FORM("apple", "so‘zining ko‘plik shakli qaysi?", "apples", ["apple", "an apples", "applees"], d=2,
                 x="Ko‘plikda -s qo‘shiladi: apple → apples."),
            Q("Nechta? Inglizcha javobni tanlang", "four dogs", ["four dog", "a dogs", "three dogs"], d=2,
              text="🐶 🐶 🐶 🐶", x="4 ta it — four dogs."),
            Q("Nechta? Inglizcha javobni tanlang", "two bananas", ["two banana", "a bananas", "three bananas"], d=2,
              text="🍌 🍌", x="2 ta banan — two bananas."),
            GAP("I have two ...", "dogs", ["dog", "a dog", "a dogs"], d=2, x="two — ko‘p: two dogs."),
            GAP("I have one ...", "cat", ["cats", "two cats", "cates"], d=2, x="one — bitta: one cat."),
            MATCH("Birlik va ko‘plik shaklini juftlang",
                  [("a cat", "cats"), ("a dog", "dogs"), ("a pen", "pens"), ("an apple", "apples"), ("a book", "books"),
                   ("a car", "cars")], d=2, lang="en"),
            SENT("I have three pens", d=2, x="I have three pens. — Mening uchta ruchkam bor."),
            Q("Qaysi so‘z ko‘plikda?", "balls", ["ball", "a ball", "one ball"], d=2, x="balls — to‘plar (oxirida -s)."),
            Q("Qaysi birikma to‘g‘ri?", "five pencils", ["five pencil", "a pencils", "five a pencil"], d=3,
              x="five — ko‘p: five pencils."),
            Q("“Uchta kitob” inglizcha qanday?", "three books", ["three book", "a three books", "three a book"], d=3,
              x="uchta kitob — three books."),
            SENT("I see five birds", d=3, x="I see five birds. — Men beshta qushni ko‘ryapman."),
        ])

CAN_Q = "Tinglang va javob bering"

T.topic("can", "🏃", L("I can: qila olaman", "I can", "I can: я умею"),
        chapter=C4,
        theory="I can … — Men … olaman: I can run. 🏃 — Men yugura olaman.  I can swim. 🏊 — Men suza olaman.\n"
               "I can't … — Men … olmayman: I can't fly. — Men ucha olmayman.\n"
               "Harakatlar: jump — sakramoq, dance 💃 — raqsga tushmoq, sing 🎤 — qo‘shiq aytmoq, read 📖 — o‘qimoq,\n"
               "write ✍️ — yozmoq, draw 🎨 — rasm chizmoq, ride a bike 🚴 — velosiped haydamoq, climb 🧗 — tirmashib chiqmoq.\n"
               "Can you swim? — Suza olasanmi? — Yes, I can. / No, I can't.",
        items=[
            PIC("run", ["swim", "dance"]),
            PIC("swim", ["run", "sing"]),
            PIC("dance", ["read", "swim"]),
            PIC("sing", ["dance", "write"]),
            PIC("read", ["write", "sing"]),
            PIC("write", ["read", "run"]),
            PIC("ride a bike", ["run", "swim"]),
            PIC("dance", ["swim", "read"], say="I can dance.", x="I can dance. — Men raqsga tusha olaman. 💃"),
            TR("jump", ["fly", "run"]),
            SAME("sing", "sing"),
            SAME("swim", "run"),
            PIC("draw", ["write", "read"], d=2),
            PIC("climb", ["swim", "dance"], d=2),
            TR("fly", ["jump", "swim"], d=2),
            LISTEN("I can draw.", "Men rasm chiza olaman.", ["Men rasm chiza olmayman.", "U rasm chiza oladi.", "Men yoza olaman."],
                   d=2),
            LISTEN("I can't sing.", "Men qo‘shiq ayta olmayman.",
                   ["Men qo‘shiq ayta olaman.", "U qo‘shiq ayta oladi.", "Men raqsga tusha olmayman."], d=2),
            EN(CAN_Q, "Yes, it can.", ["No, it can't.", "Yes, I am.", "It is a duck."], say="Can a duck swim?", d=2,
               x="O‘rdak suza oladi: Yes, it can."),
            EN(CAN_Q, "No, it can't.", ["Yes, it can.", "No, I don't.", "It is a cow."], say="Can a cow fly?", d=2,
               x="Sigir ucha olmaydi: No, it can't."),
            EN(CAN_Q, "Yes, it can.", ["No, it can't.", "Yes, it is.", "It is a frog."], say="Can a frog jump?", d=2,
               x="Qurbaqa sakray oladi: Yes, it can."),
            GAP("I ... run fast.", "can", ["am", "is", "have"], d=2, x="I can run fast. — Men tez yugura olaman."),
            MATCHE(["swim", "run", "dance", "sing", "read", "write", "ride a bike"], q="Harakatni rasmga moslang"),
            SENT("I can jump", d=2, x="I can jump. — Men sakray olaman."),
            SENT("I can read books", d=2, x="I can read books. — Men kitob o‘qiy olaman."),
            TFE("A cow can climb trees.", False, say="A cow can climb trees.", e="🐮", d=2,
                x="Sigir daraxtga chiqa olmaydi: A cow can't climb trees."),
            QSENT("Can you dance", d=3, x="Can you dance? — Sen raqsga tusha olasanmi?"),
            Q("“Men yugura olaman.” inglizcha qanday?", "I can run.", ["I can't run.", "I run can.", "I cans run."], d=3,
              x="Men … olaman — I can …: I can run."),
            TFE("A rabbit can jump.", True, say="A rabbit can jump.", e="🐰", d=3, x="To‘g‘ri: quyon sakray oladi."),
            EN("Tinglang: bola nima qila olmaydi?", "🏊", ["🏃", "💃"], say="I can run and dance. I can't swim.", d=3,
               x="I can't swim. — Men suza olmayman. 🏊"),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["this_that", "plurals", "can", "have"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["alphabet", "first_sounds", "numbers", "about_me", "days", "weather", "clothes", "house", "food", "have",
        "this_that", "plurals", "can"], chapter=C4, level=3)

T.write()
