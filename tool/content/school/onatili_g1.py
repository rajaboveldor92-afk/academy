"""Ona tili, 1-sinf (“Alifbe” va ona tili): tovush va harf, unli va undosh, sh/ch/ng, o‘/g‘, tutuq belgisi,
bo‘g‘in, alifbo, katta harf, so‘z va gap.

1-sinf o‘quvchisi (7 yosh) endigina o‘qishni o‘rganyapti: savollar ovozda o‘qib beriladi, shuning uchun ular qisqa,
javoblar — bitta harf, bo‘g‘in, 1–2 so‘z yoki rasm (emoji). Ko‘p savolda rasm (`e=`) bor: bola rasmdagi narsani
nomlab, tovushini topadi. Bo‘g‘in va harflardan so‘z yig‘ish — `WORD` (bo‘laklar qo‘shib yoziladi, ajratgichsiz).
Hamma matn, so‘z va gaplar o‘zimizniki (darslikdan ko‘chirilmagan). 3–4-sinf savollari takrorlanmasligi uchun
so‘z ro‘yxatlari shu faylda yangidan tuzilgan; bo‘g‘in va tovush sonlari pastda avtomatik tekshiriladi.
Qayta yaratish: python3 tool/content/school/onatili_g1.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from uzlang import letters  # noqa: E402

rnd = random.Random(1)
T = Course("onatili", 1, L("Ona tili", "Native language", "Родной язык"))

C1 = "1-chorak. Tovush va harf"
C2 = "2-chorak. Harf birikmalari va bo‘g‘in"
C3 = "3-chorak. So‘z va alifbo"
C4 = "4-chorak. So‘z va gap"

VOWELS1 = ["a", "o", "u", "e", "i", "o‘"]
CONS1 = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z"]


def vcount(word):
    """Unlilar soni (= bo‘g‘inlar soni). o‘ ham bitta unli: undagi “o” bir marta sanaladi."""
    return sum(1 for ch in word.lower() if ch in "aeiou")


def nta(n):
    """“n ta” javobi uchun noto‘g‘ri variantlar (0 va manfiy sonlarsiz)."""
    return [f"{n + k} ta" for k in (-1, 1, 2) if n + k > 0]


def WORD(q, parts, **kw):
    """Bo‘laklardan (bo‘g‘in yoki harflardan) so‘z yig‘ish: bo‘laklar qo‘shib yoziladi.

    `ORDER(sep="")` so‘zni alohida belgilarga bo‘lib yuboradi (o‘, sh buziladi), shuning uchun bo‘laklar “|” bilan
    ajratiladi va keyin ajratgich bo‘sh qilinadi: ekranda “ba” + “liq” → “baliq” (gap oxiridagi nuqtasiz).
    """
    it = ORDER(q, "|".join(parts), sep="|", **kw)
    it["sep"] = ""
    return it


def check_syl(word, syl):
    assert "".join(syl) == word, (word, syl)
    assert len(syl) == vcount(word), (word, syl, vcount(word))


# ============================================================ 1-chorak
# ------------------------------------------------------------ tovush va harf
items = []
for word, pic, right, wrong in [("non", "🍞", "N", ["M", "L", "B"]), ("kitob", "📖", "K", ["Q", "T", "G"]),
                                ("lola", "🌷", "L", ["N", "R", "O"]), ("tarvuz", "🍉", "T", ["D", "K", "F"]),
                                ("uy", "🏠", "U", ["O", "I", "Y"]), ("daraxt", "🌳", "D", ["T", "B", "R"])]:
    items.append(Q("Rasmdagi narsa qaysi harf bilan boshlanadi?", right, wrong, e=pic,
                   x=f"Bu — {word}. “{word}” so‘zi “{right.lower()}” tovushi bilan boshlanadi."))
for word, pic, right, wrong, d in [("mushuk", "🐱", "k", ["q", "g", "sh"], 1), ("gul", "🌸", "l", ["n", "r", "g"], 1),
                                   ("baliq", "🐟", "q", ["k", "g", "x"], 1), ("limon", "🍋", "n", ["m", "l", "o"], 2)]:
    items.append(Q(f"“{word}” so‘zi qaysi harf bilan tugaydi?", right, wrong, e=pic, d=d,
                   x=f"{word}: oxirgi tovush — “{right}”."))
for word, pic, d in [("ot", "🐴", 1), ("non", "🍞", 1), ("gul", "🌸", 1), ("olma", "🍎", 1), ("qalam", "✏️", 2),
                     ("tarvuz", "🍉", 2)]:
    parts = letters(word)
    n = len(parts)
    items.append(Q(f"“{word}” so‘zida nechta tovush bor?", f"{n} ta", nta(n), e=pic, d=d,
                   x=f"{'-'.join(parts)} — {n} ta tovush."))
items += [
    Q("“ot” so‘zidagi birinchi tovush qaysi?", "o", ["t", "u", "a"], e="🐴", x="o-t: birinchi tovush — o."),
    Q("Tovushni nima qilamiz?", "Eshitamiz va aytamiz", ["Ko‘ramiz va yozamiz", "Bo‘yaymiz", "Hidlaymiz"],
      x="Tovushni eshitamiz va aytamiz, harfni esa ko‘ramiz va yozamiz."),
    Q("Harfni nima qilamiz?", "Ko‘ramiz va yozamiz", ["Faqat eshitamiz", "Hidlaymiz", "Tatib ko‘ramiz"], d=2,
      x="Harf — tovushning yozuvdagi belgisi: uni ko‘ramiz va yozamiz."),
    TF("Harfni ko‘ramiz va yozamiz.", True, x="Tovushni esa eshitamiz va aytamiz."),
    TF("“non” so‘zida 4 ta tovush bor.", False, x="n-o-n — 3 ta tovush."),
    TF("“olma” so‘zi “o” tovushi bilan boshlanadi.", True, e="🍎", x="o-l-m-a: birinchi tovush — o."),
    WORD("Harflardan so‘z yasang", ["o", "t"], e="🐴", x="o + t = ot."),
    WORD("Harflardan so‘z yasang", ["n", "o", "n"], e="🍞", x="n + o + n = non."),
    WORD("Harflardan so‘z yasang", ["g", "u", "l"], e="🌸", d=2, x="g + u + l = gul."),
    MATCH("Katta harfni kichik harfi bilan juftlang", [("A", "a"), ("B", "b"), ("D", "d"), ("M", "m"), ("Q", "q"), ("R", "r")],
          d=2, x="Har bir harfning katta va kichik shakli bor."),
]
T.topic("sound_letter", "👂", L("Tovush va harf", "Sounds and letters", "Звуки и буквы"), C1,
        "Tovushni eshitamiz va aytamiz, harfni ko‘ramiz va yozamiz.\n"
        "• So‘z tovushlardan tuziladi: n-o-n (3 ta tovush).\n"
        "• Harf — tovushning yozuvdagi belgisi.\n"
        "• Har bir harfning katta va kichik shakli bor: A a, M m, Q q.\n"
        "Misol: “ot” so‘zida 2 ta tovush bor: o, t.", items=items)

# ------------------------------------------------------------ unli tovushlar
items = []
for word, pic, right, d in [("olma", "🍎", "O", 1), ("uzum", "🍇", "U", 1), ("ilon", "🐍", "I", 1), ("echki", "🐐", "E", 1),
                            ("ari", "🐝", "A", 1), ("o‘rdak", "🦆", "O‘", 2)]:
    wrong = ["O", "U", "A"] if right == "O‘" else rnd.sample([v.upper() for v in VOWELS1 if v.upper() != right], 3)
    items.append(Q("Rasmdagi so‘z qaysi unli bilan boshlanadi?", right, wrong, e=pic, d=d,
                   x=f"Bu — {word}. “{word}” so‘zi “{right.lower()}” unlisi bilan boshlanadi."))
for sound, right, name, wrong, d in [("a", "🐻", "ayiq", ["🐟", "🍇", "🐶"], 1), ("u", "🏠", "uy", ["🐴", "🐍", "🌙"], 1),
                                     ("e", "🚪", "eshik", ["🐝", "🐴", "🍇"], 1), ("o", "🐴", "ot", ["🐝", "🏠", "🐍"], 1),
                                     ("o‘", "🦆", "o‘rdak", ["🐴", "🍇", "🐝"], 2)]:
    items.append(Q(f"Qaysi rasmdagi so‘z “{sound}” tovushi bilan boshlanadi?", right, wrong, d=d,
                   x=f"{right} — {name}: birinchi tovush “{sound}”."))
for word, pic, d in [("gul", "🌸", 1), ("non", "🍞", 1), ("fil", "🐘", 1), ("sham", "🕯️", 1), ("qo‘l", "✋", 2)]:
    right = [c for c in letters(word) if c in VOWELS1][0]
    items.append(Q(f"“{word}” so‘zidagi unli qaysi?", right, [v for v in VOWELS1 if v != right][:3] if right != "o‘" else ["o", "u", "a"],
                   e=pic, d=d, x=f"{word}: unli — “{right}”, qolganlari undosh."))
for word, d in [("ona", 1), ("ari", 1), ("lola", 1), ("qurbaqa", 2), ("pomidor", 2), ("velosiped", 3)]:
    n = vcount(word)
    vs = [c for c in letters(word) if c in VOWELS1]
    items.append(Q(f"“{word}” so‘zida nechta unli bor?", f"{n} ta", nta(n), d=d, x=f"{word}: {', '.join(vs)} — {n} ta unli."))
for v in ["a", "e", "i", "u"]:
    items.append(Q("Unli harfni toping.", v, rnd.sample(CONS1, 3), x=f"“{v}” — unli. Unlilar: a, o, u, e, i, o‘."))
items += [
    Q("Nechta unli tovush bor?", "6 ta", ["5 ta", "4 ta", "8 ta"], x="Unlilar: a, o, u, e, i, o‘ — 6 ta."),
    TF("“o‘” — unli tovush.", True, x="o‘ — oltita unlidan biri: o‘rdak, qo‘l."),
    TF("“b” — unli tovush.", False, x="b — undosh. Unlilar: a, o, u, e, i, o‘."),
    TF("Unli tovushni cho‘zib aytish mumkin: a-a-a, o-o-o.", True, x="Unli aytilganda havo erkin chiqadi."),
    MATCH("Rasmni birinchi unlisi bilan juftlang", [("🍎", "o"), ("🍇", "u"), ("🐍", "i"), ("🐐", "e"), ("🐝", "a"), ("🦆", "o‘")],
          d=2, x="olma — o, uzum — u, ilon — i, echki — e, ari — a, o‘rdak — o‘."),
]
T.topic("vowels", "🅰️", L("Unli tovushlar", "Vowels", "Гласные звуки"), C1,
        "Unli tovushlar 6 ta: a, o, u, e, i, o‘.\n"
        "• Unlini cho‘zib aytish mumkin: a-a-a. Havo og‘izdan erkin chiqadi.\n"
        "• Har bir so‘zda unli bor: ot, uy, ari.\n"
        "Misol: “ona” so‘zida 2 ta unli bor: o, a.", items=items)

# ------------------------------------------------------------ undosh tovushlar
items = []
for c in ["m", "b", "s", "t", "q"]:
    items.append(Q("Undosh harfni toping.", c, rnd.sample(VOWELS1, 3), x=f"“{c}” — undosh. Unlilar: a, o, u, e, i, o‘."))
for word, pic, right, wrong, d in [("mushuk", "🐱", "M", ["N", "B", "P"], 1), ("baliq", "🐟", "B", ["P", "D", "V"], 1),
                                   ("fil", "🐘", "F", ["V", "P", "X"], 1), ("zebra", "🦓", "Z", ["S", "J", "D"], 1),
                                   ("pomidor", "🍅", "P", ["B", "F", "T"], 1), ("raketa", "🚀", "R", ["L", "N", "D"], 1),
                                   ("xat", "✉️", "X", ["H", "Q", "K"], 2), ("qurbaqa", "🐸", "Q", ["K", "G", "X"], 2)]:
    items.append(Q("Rasmdagi narsa qaysi undosh bilan boshlanadi?", right, wrong, e=pic, d=d,
                   x=f"Bu — {word}. “{word}” so‘zi “{right.lower()}” undoshi bilan boshlanadi."))
for sound, right, name, wrong, d in [("m", "🐱", "mushuk", ["🐟", "🍎", "🐔"], 1), ("s", "🥕", "sabzi", ["🍅", "🐱", "🍇"], 1),
                                     ("t", "🐔", "tovuq", ["🦆", "🐟", "🍎"], 1), ("b", "🐺", "bo‘ri", ["🐑", "🍇", "🐍"], 1),
                                     ("k", "🔑", "kalit", ["🐸", "🍎", "🐟"], 2)]:
    items.append(Q(f"Qaysi rasmdagi so‘z “{sound}” tovushi bilan boshlanadi?", right, wrong, d=d,
                   x=f"{right} — {name}: birinchi tovush “{sound}”."))
for word, d in [("non", 1), ("olma", 1), ("ot", 1), ("kitob", 2), ("tarvuz", 2)]:
    cons = [c for c in letters(word) if c not in VOWELS1]
    n = len(cons)
    items.append(Q(f"“{word}” so‘zida nechta undosh bor?", f"{n} ta", nta(n), d=d,
                   x=f"{word}: {', '.join(cons)} — {n} ta undosh."))
items += [
    TF("“m” — undosh tovush.", True, x="m — undosh: mushuk, non."),
    TF("“e” — undosh tovush.", False, x="e — unli tovush."),
    TF("“non” so‘zi undosh bilan boshlanib, undosh bilan tugaydi.", True, d=2, x="n-o-n: boshida ham, oxirida ham n."),
    MATCH("Rasmni birinchi harfi bilan juftlang", [("🐱", "M"), ("🐟", "B"), ("🍞", "N"), ("🐔", "T"), ("🥕", "S"), ("🐘", "F")],
          d=2, x="mushuk — M, baliq — B, non — N, tovuq — T, sabzi — S, fil — F."),
]
T.topic("consonants", "🅱️", L("Undosh tovushlar", "Consonants", "Согласные звуки"), C1,
        "Unlidan boshqa tovushlar — undoshlar: b, d, k, l, m, n, q, s, t …\n"
        "• Undosh aytilganda havo lab, til yoki tishga uriladi.\n"
        "• Undosh unli bilan qo‘shilib aytiladi: ma, no, ti.\n"
        "Misol: “non” so‘zida n, n — undosh, o — unli.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["sound_letter", "vowels", "consonants"], C1)

# ============================================================ 2-chorak
# ------------------------------------------------------------ sh, ch, ng
items = [
    Q("Rasmdagi narsa qaysi harf bilan boshlanadi?", "Sh", ["S", "Ch", "X"], e="🦁", x="Bu — sher. “sher” so‘zi “sh” bilan boshlanadi."),
    Q("Rasmdagi narsa qaysi harf bilan boshlanadi?", "Ch", ["Sh", "J", "S"], e="🍵", x="Bu — choy. “choy” so‘zi “ch” bilan boshlanadi."),
]
for word, pic, right, wrong, d in [("sham", "🕯️", "Sh", ["S", "Ch", "X"], 1), ("chana", "🛷", "Ch", ["Sh", "J", "S"], 1),
                                   ("shim", "👖", "Sh", ["Ch", "S", "J"], 1), ("chumoli", "🐜", "Ch", ["Sh", "S", "J"], 2)]:
    items.append(Q(f"“{word}” so‘zi qaysi harf bilan boshlanadi?", right, wrong, e=pic, d=d,
                   x=f"{word}: “{right.lower()}” — ikki harf bilan yoziladigan bitta tovush."))
for word, pic, right, wrong, d in [("qush", "🐦", "sh", ["s", "ch", "x"], 1), ("tong", "🌅", "ng", ["n", "g", "k"], 1),
                                   ("quyosh", "☀️", "sh", ["s", "ch", "j"], 1), ("ming", None, "ng", ["n", "g", "m"], 2),
                                   ("bodring", "🥒", "ng", ["n", "g", "k"], 2)]:
    items.append(Q(f"“{word}” so‘zi qaysi harf bilan tugaydi?", right, wrong, e=pic, d=d, x=f"{word}: oxirgi tovush — “{right}”."))
for word, d in [("shar", 1), ("choy", 1), ("qush", 1), ("tong", 1), ("chana", 2), ("quyosh", 2), ("bodring", 3)]:
    parts = letters(word)
    n = len(parts)
    items.append(Q(f"“{word}” so‘zida nechta tovush bor?", f"{n} ta", nta(n), d=d,
                   x=f"{'-'.join(parts)} — {n} ta tovush. sh, ch, ng — bitta tovush."))
items += [
    Q("Qaysi rasmdagi so‘zda “sh” tovushi bor?", "🦁", ["🐟", "🍇", "🐘"], x="🦁 — sher: sh-e-r."),
    Q("Qaysi rasmdagi so‘zda “ch” tovushi bor?", "🐜", ["🍎", "🐟", "🌷"], x="🐜 — chumoli: ch-u-m-o-l-i."),
    Q("Qaysi rasmdagi so‘zda “ng” tovushi bor?", "🥒", ["🍋", "🐟", "🍎"], d=2, x="🥒 — bodring: oxirida ng. Limon so‘zida esa faqat n bor."),
    WORD("Harflardan so‘z yasang", ["sh", "a", "m"], e="🕯️", x="sh + a + m = sham."),
    WORD("Harflardan so‘z yasang", ["ch", "o", "y"], e="🍵", x="ch + o + y = choy."),
    WORD("Harflardan so‘z yasang", ["q", "u", "sh"], e="🐦", x="q + u + sh = qush."),
    WORD("Harflardan so‘z yasang", ["t", "o", "ng"], e="🌅", d=2, x="t + o + ng = tong."),
    TF("“ng” — bitta tovush.", True, x="ng ikki harf bilan yoziladi, lekin bitta tovush: tong, ming."),
    TF("“shar” so‘zida 4 ta tovush bor.", False, x="sh-a-r — 3 ta tovush, chunki sh — bitta tovush."),
    TF("“chana” so‘zi “ch” tovushi bilan boshlanadi.", True, e="🛷", x="ch-a-n-a."),
    MATCH("Rasmni so‘z bilan juftlang", [("🦁", "sher"), ("🍵", "choy"), ("🌅", "tong"), ("🐜", "chumoli"), ("🕯️", "sham"), ("🛷", "chana")],
          d=2, x="sh, ch, ng — ikki harf bilan yoziladigan bitta tovush."),
]
T.topic("digraphs", "🔠", L("Sh, Ch va Ng", "Sh, Ch and Ng", "Sh, Ch и Ng"), C2,
        "Ba’zi tovushlar ikki harf bilan yoziladi, lekin bitta tovush bo‘lib aytiladi:\n"
        "• sh — sher, sham, qush;\n"
        "• ch — choy, chana, chumoli;\n"
        "• ng — tong, ming, bodring.\n"
        "Misol: “qush” so‘zida 3 ta tovush bor: q-u-sh.", items=items)

# ------------------------------------------------------------ o‘ va g‘
items = [
    Q("Rasmdagi narsa qaysi harf bilan boshlanadi?", "O‘", ["O", "U", "G‘"], e="🦆", x="Bu — o‘rdak. “o‘rdak” so‘zi “o‘” bilan boshlanadi."),
    Q("Rasmdagi narsa qaysi harf bilan boshlanadi?", "G‘", ["G", "Q", "O‘"], e="🧱", x="Bu — g‘isht. “g‘isht” so‘zi “g‘” bilan boshlanadi."),
    Q("Rasmdagi hayvon nomida qaysi unli bor?", "o", ["o‘", "u"], e="🐴", x="Bu — ot: o-t. Unli — o."),
    Q("Rasmdagi hayvon nomida qaysi unli bor?", "o‘", ["o", "u"], e="🐑", x="Bu — qo‘y: q-o‘-y. Unli — o‘."),
    Q("Rasmdagi narsa nomida qaysi unli bor?", "o", ["o‘", "u"], e="🍞", x="Bu — non: n-o-n. Unli — o."),
    Q("Rasmdagi narsa nomida qaysi unli bor?", "o‘", ["o", "u"], e="⚽", d=2, x="Bu — to‘p: t-o‘-p. Unli — o‘."),
    Q("Rasmdagi narsa nomi qaysi harf bilan tugaydi?", "g‘", ["g", "q"], e="⛰️", d=2, x="Bu — tog‘: oxirida g‘."),
    Q("Rasmdagi narsa nomi qaysi harf bilan tugaydi?", "g", ["g‘", "k"], e="🍁", d=2, x="Bu — barg: oxirida g."),
]
for word, pic, wrong, d in [("ot", "🐴", ["o‘t", "ut"], 1), ("qo‘l", "✋", ["qol", "qul"], 1), ("tog‘", "⛰️", ["tog", "toq"], 1),
                            ("ko‘z", "👁️", ["koz", "kuz"], 1), ("qo‘y", "🐑", ["qoy", "quy"], 1), ("to‘p", "⚽", ["top", "tup"], 2),
                            ("sovg‘a", "🎁", ["sovga", "sovqa"], 2)]:
    items.append(Q("Rasmga mos so‘zni tanlang.", word, wrong, e=pic, d=d,
                   x=f"To‘g‘ri yozilishi: {word}." + (" o‘ va g‘ belgisi (‘) tushib qolsa, so‘z buziladi." if "‘" in word else "")))
items += [
    Q("“o‘” — unli yoki undosh?", "Unli", ["Undosh", "Harf birikmasi"], x="o‘ — oltita unlidan biri."),
    Q("“g‘” — unli yoki undosh?", "Undosh", ["Unli", "Harf birikmasi"], x="g‘ — undosh: g‘isht, tog‘."),
    WORD("Harflardan so‘z yasang", ["q", "o‘", "y"], e="🐑", x="q + o‘ + y = qo‘y."),
    WORD("Harflardan so‘z yasang", ["t", "o", "g‘"], e="⛰️", x="t + o + g‘ = tog‘."),
    WORD("Harflardan so‘z yasang", ["k", "o‘", "z"], e="👁️", d=2, x="k + o‘ + z = ko‘z."),
    TF("“ot” va “o‘t” — har xil so‘zlar.", True, x="ot — hayvon, o‘t — o‘simlik yoki olov."),
    TF("“tog‘” so‘zi “g” harfi bilan tugaydi.", False, x="tog‘ so‘zi g‘ harfi bilan tugaydi."),
    TF("O‘ va G‘ — alifbodagi alohida harflar.", True, x="Ular o va g harfiga ‘ belgisi qo‘shib yoziladi."),
    MATCH("Rasmni so‘z bilan juftlang", [("🦆", "o‘rdak"), ("⛰️", "tog‘"), ("👁️", "ko‘z"), ("🐑", "qo‘y"), ("🎁", "sovg‘a"), ("🔨", "bolg‘a")],
          d=2, x="o‘ va g‘ — alohida harflar."),
]
T.topic("og_letters", "✏️", L("O‘ va G‘ harflari", "Letters O‘ and G‘", "Буквы O‘ и G‘"), C2,
        "O‘ va G‘ — alohida harflar. Ular o va g harfiga ‘ belgisi qo‘shib yoziladi.\n"
        "• o‘ — unli: o‘rdak, qo‘l, ko‘z.\n"
        "• g‘ — undosh: g‘isht, tog‘, sovg‘a.\n"
        "• Belgi tushib qolsa, so‘z o‘zgaradi: ot (hayvon) — o‘t (o‘simlik).", items=items)

# ------------------------------------------------------------ tutuq belgisi
items = []
for right, wrong in [("she’r", ["sher", "shar", "sham"]), ("ma’no", ["mana", "mato", "maysa"]), ("sa’va", ["savat", "sabzi", "sariq"]),
                     ("a’lo", ["ari", "ana", "ota"]), ("ta’til", ["tartib", "tayoq", "tulki"]), ("e’lon", ["eshik", "echki", "etik"])]:
    items.append(Q("Qaysi so‘zda tutuq belgisi bor?", right, wrong, x=f"“{right}” so‘zi tutuq belgisi (’) bilan yoziladi."))
items += [
    Q("“Men … yod oldim.” Qaysi so‘z mos?", "she’r", ["sher", "shar", "sham"], x="Men she’r yod oldim. sher — hayvon."),
    Q("“… — hayvonlar shohi.” Qaysi so‘z mos?", "Sher", ["She’r", "Shar", "Sham"], e="🦁", x="Sher — hayvon, uning nomida tutuq belgisi yo‘q."),
    Q("“Yozgi … boshlandi.” Qaysi so‘z mos?", "ta’til", ["tatil", "tartib", "tayoq"], d=2, x="Yozgi ta’til — tutuq belgisi bilan yoziladi."),
    Q("“Ukam … baho oldi.” Qaysi so‘z mos?", "a’lo", ["alo", "ari", "ana"], d=2, x="a’lo — juda yaxshi; tutuq belgisi bilan yoziladi."),
    Q("Tutuq belgisi — harfmi yoki belgimi?", "Belgi", ["Unli harf", "Undosh harf"], x="Tutuq belgisi (’) harf emas, yozuvdagi belgi."),
    Q("Rasmdagi hayvon nomi qanday yoziladi?", "sher", ["she’r", "shir", "sheer"], e="🦁", d=2,
      x="Hayvon nomi — sher. she’r esa yod olinadigan asar."),
    WORD("Bo‘g‘inlardan so‘z yasang", ["ma’", "no"], x="ma’ + no = ma’no."),
    WORD("Bo‘g‘inlardan so‘z yasang", ["ta’", "til"], x="ta’ + til = ta’til."),
    WORD("Bo‘g‘inlardan so‘z yasang", ["sa’", "va"], x="sa’ + va = sa’va."),
    WORD("Bo‘g‘inlardan so‘z yasang", ["a’", "lo"], d=2, x="a’ + lo = a’lo."),
    WORD("Bo‘g‘inlardan so‘z yasang", ["e’", "lon"], d=2, x="e’ + lon = e’lon."),
    TF("“she’r” va “sher” — har xil so‘zlar.", True, x="she’r — yod olinadigan asar, sher — hayvon."),
    TF("“ma’no” so‘zida tutuq belgisi bor.", True, x="ma’no — a harfidan keyin tutuq belgisi."),
    TF("“eshik” so‘zida tutuq belgisi bor.", False, x="eshik — tutuq belgisiz yoziladi."),
    MATCH("Bo‘g‘inlarni juftlab so‘z yasang", [("ma’", "no"), ("ta’", "til"), ("sa’", "va"), ("e’", "lon"), ("a’", "lo")], d=2,
          x="ma’no, ta’til, sa’va, e’lon, a’lo."),
]
T.topic("tutuq", "✍️", L("Tutuq belgisi", "The apostrophe (tutuq)", "Знак тутук (’)"), C2,
        "Tutuq belgisi (’) — harf emas, yozuvdagi belgi. U ba’zi so‘zlarda yoziladi:\n"
        "ma’no, she’r, sa’va, a’lo, ta’til, e’lon.\n"
        "• Unlidan keyin kelsa, shu unli biroz cho‘zib aytiladi: ma’no.\n"
        "• Tutuq belgisi so‘zni farqlaydi: sher — hayvon, she’r — yod olinadigan asar.", items=items)

# ------------------------------------------------------------ bo‘g‘in
SYL1 = {
    "fil": ["fil"], "ari": ["a", "ri"], "baliq": ["ba", "liq"], "echki": ["ech", "ki"], "ilon": ["i", "lon"], "gilos": ["gi", "los"],
    "limon": ["li", "mon"], "mushuk": ["mu", "shuk"], "tuya": ["tu", "ya"], "qurbaqa": ["qur", "ba", "qa"],
    "pomidor": ["po", "mi", "dor"], "baraban": ["ba", "ra", "ban"], "samolyot": ["sa", "mol", "yot"],
    "velosiped": ["ve", "lo", "si", "ped"],
}
for w, s in SYL1.items():
    check_syl(w, s)
PIC1 = {"fil": "🐘", "ari": "🐝", "baliq": "🐟", "echki": "🐐", "ilon": "🐍", "gilos": "🍒", "limon": "🍋", "mushuk": "🐱",
        "qurbaqa": "🐸", "pomidor": "🍅", "baraban": "🥁", "samolyot": "✈️", "velosiped": "🚲"}
items = []
for w, pic in PIC1.items():
    syl = SYL1[w]
    n = len(syl)
    items.append(Q(f"“{w}” so‘zini bo‘g‘inlab ayting. Nechta bo‘g‘in bor?", f"{n} ta", nta(n), e=pic, d=min(3, max(1, n - 1)),
                   x=f"{'-'.join(syl)} — {n} ta bo‘g‘in, chunki {n} ta unli bor."))
items += [
    Q("Qaysi so‘zda bitta bo‘g‘in bor?", "fil", ["ari", "baliq", "ilon"], x="fil — bitta unli, bitta bo‘g‘in."),
    Q("Qaysi so‘zda bitta bo‘g‘in bor?", "qo‘y", ["qo‘zi", "tovuq", "echki"], x="qo‘y — bitta unli (o‘), bitta bo‘g‘in."),
    Q("Qaysi so‘zda uchta bo‘g‘in bor?", "qurbaqa", ["baliq", "limon", "sham"], d=2, x="qur-ba-qa — 3 ta bo‘g‘in."),
    Q("Bo‘g‘inlar sonini qanday bilamiz?", "Unlilarni sanab", ["Undoshlarni sanab", "So‘zlarni sanab"], d=2,
      x="So‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bo‘ladi."),
    Q("“baliq” so‘zining birinchi bo‘g‘ini qaysi?", "ba", ["bal", "liq", "b"], e="🐟", x="ba-liq: birinchi bo‘g‘in — ba."),
    Q("“limon” so‘zining oxirgi bo‘g‘ini qaysi?", "mon", ["li", "on", "lim"], e="🍋", x="li-mon: oxirgi bo‘g‘in — mon."),
    Q("“qurbaqa” so‘zining o‘rtadagi bo‘g‘ini qaysi?", "ba", ["qur", "qa", "rba"], e="🐸", d=2, x="qur-ba-qa: o‘rtadagi bo‘g‘in — ba."),
    TF("“fil” so‘zi bitta bo‘g‘indan iborat.", True, e="🐘", x="fil — bitta unli (i)."),
    TF("“ari” so‘zida 3 ta bo‘g‘in bor.", False, e="🐝", x="a-ri: 2 ta unli — 2 ta bo‘g‘in."),
    TF("So‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bo‘ladi.", True, x="o-na: 2 ta unli — 2 ta bo‘g‘in."),
    MATCH("So‘zni bo‘g‘inlari bilan juftlang", [(w, "-".join(SYL1[w])) for w in ["baliq", "ilon", "echki", "limon", "gilos", "tuya"]], d=2,
          x="Har bir bo‘g‘inda bitta unli bor."),
]
T.topic("syllable_count", "👏", L("Bo‘g‘in", "Syllables", "Слог"), C2,
        "So‘z bo‘g‘inlarga bo‘linadi. So‘zni qarsak chalib ayting: a-ri (2 ta qarsak).\n"
        "• Har bir bo‘g‘inda bitta unli bor.\n"
        "• So‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bo‘ladi:\n"
        "  fil (1), ba-liq (2), qur-ba-qa (3).", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["digraphs", "og_letters", "tutuq", "syllable_count"], C2)

# ============================================================ 3-chorak
# ------------------------------------------------------------ bo‘g‘inlardan so‘z
BUILD1 = [
    ("mushuk", ["mu", "shuk"], "🐱", 1, None), ("baliq", ["ba", "liq"], "🐟", 1, None), ("ayiq", ["a", "yiq"], "🐻", 1, None),
    ("bo‘ri", ["bo‘", "ri"], "🐺", 1, None), ("qaychi", ["qay", "chi"], "✂️", 1, None), ("kalit", ["ka", "lit"], "🔑", 1, None),
    ("bulut", ["bu", "lut"], "☁️", 1, None), ("archa", ["ar", "cha"], "🌲", 1, None),
    ("qurbaqa", ["qur", "ba", "qa"], "🐸", 2, None), ("raketa", ["ra", "ke", "ta"], "🚀", 2, None),
    ("gitara", ["gi", "ta", "ra"], "🎸", 2, None), ("telefon", ["te", "le", "fon"], "📱", 2, None),
    ("jirafa", ["ji", "ra", "fa"], "🦒", 2, None), ("kamalak", ["ka", "ma", "lak"], "🌈", 2, None),
    ("samolyot", ["sa", "mol", "yot"], "✈️", 3, ["mo"]), ("avtobus", ["av", "to", "bus"], "🚌", 3, ["ta"]),
    ("velosiped", ["ve", "lo", "si", "ped"], "🚲", 3, None),
]
items = []
for w, syl, pic, d, extra in BUILD1:
    check_syl(w, syl)
    items.append(WORD("Bo‘g‘inlardan so‘z yasang", syl, e=pic, d=d, extra=extra, x=f"{' + '.join(syl)} = {w}."))
for text, pic, right, wrong, word, d in [("mu …", "🐱", "shuk", ["shik", "chuk", "suk"], "mu-shuk", 1),
                                         ("… ri", "🐝", "a", ["o", "u", "i"], "a-ri", 1),
                                         ("li …", "🍋", "mon", ["mun", "non", "mo"], "li-mon", 1),
                                         ("ji … fa", "🦒", "ra", ["ro", "la", "ri"], "ji-ra-fa", 2),
                                         ("ka ma …", "🌈", "lak", ["lik", "nak", "laq"], "ka-ma-lak", 2),
                                         ("te … fon", "📱", "le", ["la", "li", "ne"], "te-le-fon", 2)]:
    items.append(Q("Tushib qolgan bo‘g‘inni toping.", right, wrong, text=text, e=pic, d=d, x=f"{word} = {word.replace('-', '')}."))
items += [
    WORD("Harflardan so‘z yasang", ["f", "i", "l"], e="🐘", x="f + i + l = fil."),
    WORD("Harflardan so‘z yasang", ["u", "y"], e="🏠", x="u + y = uy."),
    WORD("Harflardan so‘z yasang", ["i", "t"], e="🐶", x="i + t = it."),
    WORD("Harflardan so‘z yasang", ["sh", "e", "r"], e="🦁", d=2, x="sh + e + r = sher."),
    TF("“ka” va “lit” bo‘g‘inlaridan “kalit” so‘zi hosil bo‘ladi.", True, e="🔑", x="ka + lit = kalit."),
    TF("“lit” va “ka” bo‘g‘inlarini shu tartibda qo‘shsak, “kalit” bo‘ladi.", False, d=2,
       x="Bo‘g‘inlar tartibi muhim: ka-lit. lit-ka — so‘z emas."),
]
T.topic("syllable_build", "🧩", L("Bo‘g‘inlardan so‘z", "Building words from syllables", "Слова из слогов"), C3,
        "Bo‘g‘inlarni qo‘shib o‘qisak, so‘z hosil bo‘ladi: ba + liq = baliq.\n"
        "• Bo‘g‘inlar tartibi muhim: ka-lit — so‘z, lit-ka — so‘z emas.\n"
        "• Harflardan ham so‘z yasaymiz: f + i + l = fil.\n"
        "Misol: qur + ba + qa = qurbaqa.", items=items)

# ------------------------------------------------------------ alifbo
items = [Q("Alifboning birinchi harfi qaysi?", "A", ["B", "O", "Y"], x="Alifbo A harfi bilan boshlanadi: A, B, D, E …")]
for a, right, wrong, d in [("K", "L", ["J", "M", "Q"], 1), ("S", "T", ["R", "U", "Z"], 1), ("M", "N", ["L", "O", "H"], 1),
                           ("U", "V", ["W", "F", "T"], 2), ("X", "Y", ["Z", "H", "W"], 2), ("Z", "O‘", ["A", "G‘", "Y"], 2)]:
    items.append(Q(f"Alifboda “{a}” dan keyingi harf qaysi?", right, wrong, d=d, x=f"Alifboda {a} dan keyin {right} keladi."))
for a, right, wrong, d in [("D", "B", ["C", "E", "A"], 1), ("F", "E", ["G", "D", "H"], 1), ("Q", "P", ["R", "O", "K"], 2),
                           ("I", "H", ["J", "G", "K"], 2)]:
    items.append(Q(f"Alifboda “{a}” dan oldingi harf qaysi?", right, wrong, d=d,
                   x=f"Alifboda {right} dan keyin {a} keladi." + (" O‘zbek alifbosida C harfi yo‘q." if "C" in wrong else "")))
for right, wrong in [("D", ["K", "R"]), ("G", ["N", "U"]), ("E", ["M", "Z"])]:
    items.append(Q("Qaysi harf alifboda oldin keladi?", right, wrong, x=f"Alifbo tartibi: A B D E F G H I J K L M N …"))
items += [
    ORDER("Harflarni alifbo tartibida joylang", "D E F G", x="D, E, F, G."),
    ORDER("Harflarni alifbo tartibida joylang", "P Q R S", x="P, Q, R, S."),
    ORDER("Harflarni alifbo tartibida joylang", "T U V X", d=2, x="T, U, V, X — alifboda W harfi yo‘q."),
    ORDER("Harflarni alifbo tartibida joylang", "O‘ G‘ Sh Ch", d=3, x="Alifbo oxiri: O‘, G‘, Sh, Ch, Ng."),
    Q("Qaysi rasmdagi so‘z alifboda birinchi turadi?", "🐟", ["🍎", "🐱"], d=2, x="baliq (B), mushuk (M), olma (O): B oldin keladi."),
    Q("Qaysi rasmdagi so‘z alifboda birinchi turadi?", "🐝", ["🐟", "🐴"], d=2, x="ari (A), baliq (B), ot (O): A birinchi."),
    TF("Alifboda “L” harfi “M” dan oldin keladi.", True, x="K, L, M, N."),
    TF("Alifboda “R” harfi “P” dan oldin keladi.", False, x="P, Q, R: P oldin keladi."),
    TF("“O‘” harfi alifboda “Z” dan keyin keladi.", True, d=2, x="… X, Y, Z, O‘, G‘, Sh, Ch, Ng."),
    MATCH("Harfni keyingi harf bilan juftlang", [("A", "B"), ("D", "E"), ("K", "L"), ("M", "N"), ("S", "T"), ("X", "Y")], d=2,
          x="Alifbo tartibi: A B D E F G H I J K L M N O P Q R S T U V X Y Z O‘ G‘ Sh Ch Ng."),
]
T.topic("alphabet", "🔤", L("Alifbo", "The alphabet", "Алфавит"), C3,
        "Harflarning belgilangan tartibi — alifbo.\n"
        "A B D E F G H I J K L M N O P Q R S T U V X Y Z O‘ G‘ Sh Ch Ng\n"
        "• Alifbo A harfi bilan boshlanadi.\n"
        "• O‘, G‘, Sh, Ch, Ng alifbo oxirida keladi.\n"
        "• O‘zbek alifbosida C va W harflari yo‘q.", items=items)

# ------------------------------------------------------------ katta va kichik harf
items = []
for right, wrong in [("R", ["r", "n", "m"]), ("G", ["g", "q", "d"]), ("E", ["e", "a", "o"])]:
    items.append(Q("Katta harfni toping.", right, wrong, x=f"“{right}” — katta harf, “{right.lower()}” — kichik harf."))
for right, wrong in [("b", ["B", "D", "P"]), ("h", ["H", "N", "K"]), ("sh", ["Sh", "Ch", "S"])]:
    items.append(Q("Kichik harfni toping.", right, wrong, x=f"“{right}” — kichik harf, uning katta shakli — “{right.capitalize()}”."))
for small, right, wrong, d in [("d", "D", ["B", "P", "Q"], 1), ("q", "Q", ["G", "O", "P"], 1), ("o‘", "O‘", ["O", "G‘", "U"], 2),
                               ("ch", "Ch", ["Sh", "C", "Ng"], 2)]:
    items.append(Q(f"“{small}” harfining katta shakli qaysi?", right, wrong, d=d, x=f"{right} — {small}."))
for right, wrong, why, d in [("laylo", ["qiz", "sumka", "non"], "Laylo — qizning ismi", 1),
                             ("jasur", ["bola", "to‘p", "uy"], "Jasur — bolaning ismi", 1),
                             ("navoiy", ["shahar", "ko‘cha", "bog‘"], "Navoiy — shahar nomi", 1),
                             ("aziza", ["opa", "olma", "kitob"], "Aziza — qizning ismi", 1),
                             ("qo‘qon", ["shahar", "daryo", "tog‘"], "Qo‘qon — shahar nomi", 2)]:
    items.append(Q("Qaysi so‘zni katta harf bilan yozamiz?", right, wrong, d=d, x=f"{why}. Ism va shahar nomlari katta harf bilan yoziladi."))
items += [
    Q("To‘g‘ri yozilgan gapni toping.", "Ali maktabga bordi.", ["ali maktabga bordi.", "Ali Maktabga bordi.", "ali Maktabga bordi."], d=2,
      x="Gap va ism katta harf bilan boshlanadi; “maktabga” — kichik harf bilan."),
    Q("To‘g‘ri yozilgan gapni toping.", "Biz Navoiyda yashaymiz.", ["biz Navoiyda yashaymiz.", "Biz navoiyda yashaymiz.", "biz navoiyda yashaymiz."],
      d=2, x="Gap boshi va shahar nomi katta harf bilan yoziladi."),
    Q("To‘g‘ri yozilgan gapni toping.", "Kamola rasm chizdi.", ["kamola rasm chizdi.", "Kamola Rasm chizdi.", "kamola Rasm chizdi."], d=2,
      x="Kamola — ism, gap boshida ham. “rasm” — kichik harf bilan."),
    TF("“jasur” ismini kichik harf bilan boshlash kerak.", False, x="Ismlar katta harf bilan yoziladi: Jasur."),
    TF("Gapning birinchi so‘zi katta harf bilan boshlanadi.", True, x="Bugun havo iliq."),
    TF("Shahar nomi katta harf bilan yoziladi: Qarshi.", True, x="Qarshi — shahar nomi."),
    TF("“mushuk” so‘zi gap o‘rtasida ham katta harf bilan yoziladi.", False, d=2,
       x="mushuk — ism emas; u gap boshida kelsagina katta harf bilan yoziladi."),
    MATCH("Katta harfni kichik harfi bilan juftlang",
          [("E", "e"), ("G", "g"), ("N", "n"), ("T", "t"), ("Y", "y"), ("Sh", "sh"), ("O‘", "o‘")], x="Har bir harfning katta va kichik shakli bor."),
]
T.topic("capital", "🔡", L("Katta va kichik harf", "Capital and small letters", "Заглавные и строчные буквы"), C3,
        "Har bir harfning katta va kichik shakli bor: A a, B b, Sh sh, O‘ o‘.\n"
        "Katta harf bilan yoziladi:\n"
        "• gapning birinchi so‘zi: Bugun havo iliq.\n"
        "• kishi ismlari: Ali, Laylo, Jasur;\n"
        "• shahar nomlari: Navoiy, Qarshi, Qo‘qon.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["syllable_build", "alphabet", "capital"], C3)

# ============================================================ 4-chorak
# ------------------------------------------------------------ kim? nima? qanday? nima qildi?
WHY = {"kim?": "odamni bildiradi — kim? savoliga javob beradi.",
       "nima?": "narsa yoki hayvonni bildiradi — nima? savoliga javob beradi.",
       "qanday?": "belgini bildiradi — qanday? savoliga javob beradi.",
       "nima qildi?": "harakatni bildiradi — nima qildi? savoliga javob beradi."}
KINDS = list(WHY)
items = []
for word, kind, pic, d in [("ona", "kim?", "👩", 1), ("o‘qituvchi", "kim?", None, 1), ("buvi", "kim?", "👵", 1), ("shifokor", "kim?", None, 1),
                           ("olma", "nima?", "🍎", 1), ("kitob", "nima?", "📖", 1), ("quyosh", "nima?", "☀️", 1), ("mushuk", "nima?", "🐱", 2),
                           ("sariq", "qanday?", None, 1), ("kichkina", "qanday?", None, 1), ("issiq", "qanday?", None, 1),
                           ("mazali", "qanday?", None, 2), ("o‘ynadi", "nima qildi?", None, 1), ("uchdi", "nima qildi?", None, 1),
                           ("suzdi", "nima qildi?", None, 1), ("ichdi", "nima qildi?", None, 2)]:
    items.append(Q(f"“{word}” so‘zi qaysi savolga javob beradi?", kind, [k for k in KINDS if k != kind], e=pic, d=d,
                   x=f"“{word}” {WHY[kind]}"))
items += [
    Q("Qaysi so‘z “kim?” savoliga javob beradi?", "bobo", ["olma", "mushuk", "stol"], d=2,
      x="bobo — odam. Mushuk — hayvon, u nima? savoliga javob beradi."),
    Q("Qaysi so‘z “qanday?” savoliga javob beradi?", "yumshoq", ["yostiq", "ota", "yotdi"], x="yumshoq — belgi: qanday yostiq? yumshoq."),
    Q("Qaysi so‘z “nima qildi?” savoliga javob beradi?", "yugurdi", ["yo‘l", "bola", "katta"], x="yugurdi — harakat."),
]
for animal, pic, right, wrong, d in [("It", "🐶", "vovullaydi", ["miyovlaydi", "kishnaydi", "sayraydi"], 1),
                                     ("Mushuk", "🐱", "miyovlaydi", ["vovullaydi", "mo‘raydi", "qaqillaydi"], 1),
                                     ("Ot", "🐴", "kishnaydi", ["miyovlaydi", "vovullaydi", "vaqillaydi"], 1),
                                     ("Sigir", "🐮", "mo‘raydi", ["kishnaydi", "sayraydi", "miyovlaydi"], 2),
                                     ("Qurbaqa", "🐸", "vaqillaydi", ["kishnaydi", "mo‘raydi", "vovullaydi"], 2),
                                     ("Tovuq", "🐔", "qaqillaydi", ["vovullaydi", "mo‘raydi", "kishnaydi"], 2)]:
    items.append(Q(f"{animal} nima qiladi?", right, wrong, e=pic, d=d, x=f"{animal} {right}. Bu so‘z harakatni bildiradi."))
items += [
    TF("“mushuk” so‘zi “kim?” savoliga javob beradi.", False, e="🐱", x="Hayvon nomlari nima? savoliga javob beradi."),
    TF("“shirin” so‘zi belgini bildiradi.", True, x="Qanday olma? — shirin olma."),
    TF("“sakradi” so‘zi harakatni bildiradi.", True, x="Nima qildi? — sakradi."),
    MATCH("So‘zni savoli bilan juftlang", [("buvi", "kim?"), ("olma", "nima?"), ("qizil", "qanday?"), ("sakradi", "nima qildi?")], d=2,
          x="buvi — kim?, olma — nima?, qizil — qanday?, sakradi — nima qildi?"),
    MATCH("Hayvonni ovozi bilan juftlang", [("it", "vovullaydi"), ("mushuk", "miyovlaydi"), ("ot", "kishnaydi"), ("sigir", "mo‘raydi"),
                                             ("tovuq", "qaqillaydi"), ("qurbaqa", "vaqillaydi")], d=2),
]
T.topic("word_kinds", "❓", L("Kim? Nima? Qanday? Nima qildi?", "Who? What? What kind? What did it do?", "Кто? Что? Какой? Что сделал?"), C4,
        "So‘zlar har xil savolga javob beradi:\n"
        "• kim? — odamlar: ona, bobo, o‘qituvchi.\n"
        "• nima? — narsa va hayvonlar: kitob, olma, mushuk.\n"
        "• qanday? — belgi: sariq, katta, shirin.\n"
        "• nima qildi? — harakat: yugurdi, uchdi, o‘ynadi.", items=items)

# ------------------------------------------------------------ so‘z va gap
items = []
for sent, pic in [("Quyosh chiqdi.", "☀️"), ("Qor yog‘di.", "❄️"), ("Mushuk sut ichdi.", "🐱"), ("Onam non yopdi.", "🍞"),
                  ("Qushlar daraxtda sayrayapti.", "🐦"), ("Ukam chiroyli rasm chizdi.", "🎨"), ("Biz hovlida to‘p o‘ynadik.", "⚽"),
                  ("Dadam menga velosiped olib keldi.", "🚲")]:
    n = len(sent.split())
    items.append(Q(f"“{sent}” Bu gapda nechta so‘z bor?", f"{n} ta", nta(n), e=pic, d=1 if n <= 3 else (2 if n == 4 else 3),
                   x=f"{' | '.join(w.strip('.') for w in sent.split())} — {n} ta so‘z."))
MARK_WHY = {".": "Xabar beradigan gap oxiriga nuqta qo‘yiladi.", "?": "Savol beradigan gap oxiriga so‘roq belgisi qo‘yiladi.",
            "!": "Kuchli his bilan aytilgan gap oxiriga undov belgisi qo‘yiladi."}
for sent, mark, d in [("Ertaga yakshanba", ".", 1), ("Olmalar qizardi", ".", 1), ("Sening isming nima", "?", 1),
                      ("Soat necha bo‘ldi", "?", 1), ("Bu kimning sumkasi", "?", 1), ("Biz parkka bordik", ".", 1),
                      ("Qanday go‘zal kapalak", "!", 2), ("Voy, qor yog‘yapti", "!", 2), ("Ura, dadam keldi", "!", 2)]:
    items.append(Q(f"“{sent}” — bu gapning oxirida qaysi belgi bo‘ladi?", mark, [m for m in (".", "?", "!") if m != mark], d=d,
                   x=f"{sent}{mark} {MARK_WHY[mark]}"))
items += [
    Q("Qaysi belgi — so‘roq belgisi?", "?", [".", "!", ","], x="So‘roq belgisi: ?"),
    Q("Qaysi belgi — undov belgisi?", "!", ["?", ".", ","], x="Undov belgisi: !"),
    Q("Qaysi belgi — nuqta?", ".", ["?", "!", ","], x="Nuqta: ."),
    Q("Qaysi qatorda gap yozilgan?", "Qushlar uchdi.", ["qushlar", "kichkina qush", "qush va"], d=2, x="Gap tugal fikr bildiradi: Qushlar uchdi."),
    Q("Qaysi qatorda gap yozilgan?", "Gullar ochildi.", ["gullar", "qizil gul", "gul va"], d=2, x="Gap tugal fikr bildiradi: Gullar ochildi."),
    Q("“Onam non yopdi.” gapidagi oxirgi so‘z qaysi?", "yopdi", ["Onam", "non"], x="Onam | non | yopdi — oxirgi so‘z: yopdi."),
    Q("“Quyon sabzi yedi.” gapidagi birinchi so‘z qaysi?", "Quyon", ["sabzi", "yedi"], e="🐰", x="Quyon | sabzi | yedi — birinchi so‘z: Quyon."),
    TF("“quyosh chiqdi.” gapi to‘g‘ri yozilgan.", False, x="Gap katta harf bilan boshlanadi: Quyosh chiqdi."),
    TF("Gapdagi so‘zlar alohida yoziladi.", True, x="Mushuk | sut | ichdi — so‘zlar orasida bo‘sh joy bor."),
    TF("So‘roq gap oxiriga nuqta qo‘yiladi.", False, x="So‘roq gap oxiriga so‘roq belgisi (?) qo‘yiladi."),
]
T.topic("word_sentence", "💬", L("So‘z va gap", "Words and sentences", "Слово и предложение"), C4,
        "Gap so‘zlardan tuziladi va tugal fikr bildiradi: Quyosh chiqdi.\n"
        "• Gapdagi so‘zlar alohida yoziladi.\n"
        "• Gap katta harf bilan boshlanadi.\n"
        "• Gap oxirida nuqta (.), so‘roq (?) yoki undov (!) belgisi turadi:\n"
        "  Qor yog‘di. Soat necha bo‘ldi? Ura, dadam keldi!", items=items)

# ------------------------------------------------------------ so‘zlardan gap tuzish
items = []
for sent, pic, d in [("Mushuk uxladi", "🐱", 1), ("Kaptarlar uchdi", "🕊️", 1), ("Gullar ochildi", "🌷", 1), ("Quyon sabzi yedi", "🐰", 1),
                     ("Baliq suvda suzadi", "🐟", 1), ("Ali to‘p o‘ynadi", "⚽", 1), ("Sigir sut beradi", "🐮", 1),
                     ("It suyak kemirdi", "🐶", 1), ("Laylo rasm chizdi", "🎨", 1), ("Biz bog‘da o‘ynadik", "🌳", 1),
                     ("Bobom bog‘da olma terdi", "👴", 2), ("Men maktabga yugurib bordim", "🏫", 2),
                     ("Ukam kichkina jo‘jani ushladi", "🐤", 2), ("Onam bozordan non oldi", "🍞", 2)]:
    items.append(ORDER("So‘zlardan gap tuzing", sent, e=pic, d=d, x=f"{sent}."))
items += [
    ORDER("So‘zlardan gap tuzing", "Kichkina qiz qo‘shiq aytdi", extra=["aytdim"], d=3, x="Kichkina qiz qo‘shiq aytdi. (qiz … aytdi)"),
    ORDER("So‘zlardan gap tuzing", "Bolalar qor o‘ynashdi", extra=["o‘ynadim"], e="❄️", d=3, x="Bolalar qor o‘ynashdi. (bolalar … o‘ynashdi)"),
    Q("Gapni to‘ldiring: “Qushlar osmonda …”", "uchadi", ["suzadi", "o‘qiydi", "yig‘laydi"], e="🐦", x="Qushlar osmonda uchadi."),
    Q("Gapni to‘ldiring: “Men har kuni tishimni …”", "yuvaman", ["ichaman", "o‘qiyman", "uchaman"], e="🦷", x="Men har kuni tishimni yuvaman."),
    Q("Gapni to‘ldiring: “Onam bozordan olma …”", "oldi", ["uchdi", "suzdi", "sayradi"], e="🍎", x="Onam bozordan olma oldi."),
    TF("“qizil va” — gap.", False, x="Bu so‘zlar tugal fikr bildirmaydi. Gap: Olma qizil."),
    TF("Gap tuzganda so‘zlarni to‘g‘ri tartibda qo‘yish kerak.", True, x="Mushuk uxladi — to‘g‘ri; Uxladi mushuk — noto‘g‘ri tartib."),
    TF("“Kaptarlar uchdi.” — gap.", True, e="🕊️", x="Tugal fikr bor: kim? — kaptarlar, nima qildi? — uchdi."),
]
T.topic("build_sentence", "🧱", L("So‘zlardan gap tuzish", "Building sentences", "Составление предложений"), C4,
        "So‘zlarni to‘g‘ri tartibda qo‘ysak, gap hosil bo‘ladi.\n"
        "• Avval kim? yoki nima? haqida gap borishini aytamiz, oxirida nima qildi? keladi:\n"
        "  Quyon sabzi yedi. Kaptarlar uchdi.\n"
        "• Gapni katta harf bilan boshlab, oxiriga nuqta qo‘yamiz.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["word_kinds", "word_sentence", "build_sentence"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["sound_letter", "vowels", "consonants", "digraphs", "og_letters", "tutuq", "syllable_count", "syllable_build", "alphabet",
        "capital", "word_kinds", "word_sentence", "build_sentence"], C4, level=3)

T.write()
