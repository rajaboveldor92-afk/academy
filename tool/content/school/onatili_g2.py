"""Ona tili, 2-sinf: alifbo tartibi, unli va undosh, jarangli va jarangsiz undoshlar, bo‘g‘in va so‘zni ko‘chirish,
o‘/g‘ va tutuq belgisi, qo‘sh undoshli so‘zlar, ma’nodosh va qarama-qarshi ma’noli so‘zlar, kim? nima?, birlik va
ko‘plik, atoqli otlar, belgi va harakatni bildirgan so‘zlar, gap turlari, so‘zlardan gap tuzish.

2-sinf o‘quvchisi (8 yosh): savollar ovozda o‘qib beriladi, javoblar qisqa (harf, bo‘g‘in, 1–3 so‘z yoki qisqa gap).
1-sinf (onatili_g1.py) mavzularini davom ettiradi; 1- va 3-sinf savollari takrorlanmasligi uchun so‘z ro‘yxatlari
shu faylda yangidan tuzilgan. Bo‘g‘inlar, unlilar soni va alifbo tartibi pastda avtomatik tekshiriladi.
Hamma matn, so‘z va gaplar o‘zimizniki (darslikdan ko‘chirilmagan).
Qayta yaratish: python3 tool/content/school/onatili_g2.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from uzlang import VOWELS, alpha_key, letters, vowel_count, vowels_of  # noqa: E402

T = Course("onatili", 2, L("Ona tili", "Native language", "Родной язык"))

C1 = "1-chorak. Tovush, harf va alifbo"
C2 = "2-chorak. Bo‘g‘in va imlo"
C3 = "3-chorak. So‘z ma’nosi va narsa nomlari"
C4 = "4-chorak. Belgi, harakat va gap"


def nta(n):
    """“n ta” javobi uchun noto‘g‘ri variantlar (0 va manfiy sonlarsiz)."""
    return [f"{n + k} ta" for k in (-1, 1, 2) if n + k > 0]


def check_syl(word, syl):
    assert "".join(syl) == word, (word, syl)
    assert len(syl) == vowel_count(word), (word, syl)


# ============================================================ 1-chorak
# ------------------------------------------------------------ alifbo tartibi
items = []
FIRST = [(["fil", "baliq", "tovuq", "qo‘y"], 1), (["sut", "non", "asal", "choy"], 1), (["qor", "yomg‘ir", "bulut", "shamol"], 1),
         (["limon", "gilos", "nok", "uzum"], 1), (["eshik", "deraza", "hovli", "tom"], 1), (["mushuk", "kuchuk", "quyon", "tulki"], 1),
         (["bola", "bulut", "bahor", "bedana"], 2), (["qush", "qalam", "qor", "qiz"], 2), (["tovuq", "tuxum", "tarvuz", "tikan"], 2),
         (["sut", "sabzi", "sichqon", "soat"], 2), (["yo‘l", "zebra", "shar", "o‘rdak"], 3), (["sher", "tulki", "chumchuq", "g‘oz"], 3)]
LAST = [(["ruchka", "daftar", "kitob", "qalam"], 1), (["olma", "anor", "uzum", "nok"], 1), (["mushuk", "mashina", "meva", "mix"], 2),
        (["g‘oz", "o‘rik", "zebra", "yong‘oq"], 3)]


def alpha_explain(group, word, d):
    if d == 3:
        return f"Alifbo oxiri: … X, Y, Z, O‘, G‘, Sh, Ch, Ng. Javob — {word}."
    pos = 0 if d == 1 else 1
    marks = ", ".join(letters(w)[pos] for w in group)
    if pos == 0:
        return f"Birinchi harflarni solishtiramiz: {marks}. Javob — {word}."
    return f"Birinchi harf bir xil, ikkinchi harflarni solishtiramiz: {marks}. Javob — {word}."


for group, d in FIRST:
    first = min(group, key=alpha_key)
    items.append(Q("Lug‘atda qaysi so‘z birinchi turadi?", first, [w for w in group if w != first], d=d,
                   x=alpha_explain(group, first, d)))
for group, d in LAST:
    last = max(group, key=alpha_key)
    items.append(Q("Lug‘atda qaysi so‘z oxirgi turadi?", last, [w for w in group if w != last], d=d,
                   x=alpha_explain(group, last, d)))
for seq, d in [("asal bulut gilos", 1), ("daraxt kuchuk sut", 1), ("qalam qor qush", 2), ("zebra o‘rdak sher", 3)]:
    words = seq.split()
    assert words == sorted(words, key=alpha_key), seq
    items.append(ORDER("So‘zlarni alifbo tartibida joylang", seq, d=d, x=", ".join(words) + "."))
items += [
    Q("Lug‘atda so‘zlar qanday tartibda yoziladi?", "Alifbo tartibida", ["Uzunligi bo‘yicha", "Istalgan tartibda",
                                                                       "Bo‘g‘inlar soni bo‘yicha"],
      x="Lug‘atda so‘zlar alifbo tartibida turadi, shuning uchun kerakli so‘zni tez topamiz."),
    Q("Qaysi harflar alifboning oxirida turadi?", "O‘, G‘, Sh, Ch, Ng", ["A, B, D, E, F", "K, L, M, N, O", "P, Q, R, S, T"],
      x="Alifbo shunday tugaydi: … X, Y, Z, O‘, G‘, Sh, Ch, Ng."),
    Q("“bola” va “bulut” so‘zlarini qaysi harf bo‘yicha solishtiramiz?", "Ikkinchi harf",
      ["Birinchi harf", "Oxirgi harf", "Uchinchi harf"], d=2,
      x="Birinchi harf (b) bir xil, shuning uchun ikkinchi harfga qaraymiz: o — u dan oldin. Demak, “bola” oldin turadi."),
    Q("Sinf ro‘yxatida qaysi ism birinchi yoziladi?", "Aziz", ["Malika", "Zarina", "Sardor"],
      x="Ro‘yxat alifbo tartibida tuziladi: A harfi birinchi keladi."),
    Q("Sinf ro‘yxatida qaysi ism oxirgi yoziladi?", "Shahzod", ["Jasur", "Laylo", "Zafar"], d=3,
      x="Sh harfi alifboda Z dan keyin turadi: Jasur, Laylo, Zafar, Shahzod."),
    Q("Lug‘atda qaysi so‘z “ot” va “qor” so‘zlari orasida turadi?", "piyoz", ["anor", "uzum", "yong‘oq"], d=2,
      x="Alifboda O, P, Q ketma-ket keladi: ot, piyoz, qor."),
    TF("Lug‘atda “daryo” so‘zi “anor” so‘zidan oldin turadi.", False, x="A harfi D dan oldin keladi: anor, daryo."),
    TF("Lug‘atda “kalit” so‘zi “kitob” so‘zidan oldin turadi.", True, d=2,
       x="Birinchi harf bir xil (k). Ikkinchi harflar: a va i — a oldin keladi."),
    TF("Lug‘atda “olma” so‘zi “o‘rik” so‘zidan oldin turadi.", True, d=2,
       x="O harfi alifbo o‘rtasida, O‘ esa Z dan keyin keladi."),
    TF("Lug‘atda “choy” so‘zi “yong‘oq” so‘zidan keyin turadi.", True, d=3,
       x="Ch alifbo oxirida turadi, Y dan ancha keyin keladi."),
]
T.topic("alphabet_order", "🔤", L("Alifbo tartibi", "Alphabetical order", "Алфавитный порядок"), C1,
        "O‘zbek alifbosi: A B D E F G H I J K L M N O P Q R S T U V X Y Z O‘ G‘ Sh Ch Ng.\n"
        "• Lug‘atda so‘zlar alifbo tartibida turadi.\n"
        "• Avval birinchi harflarni solishtiramiz: asal, bulut, gilos.\n"
        "• Birinchi harflar bir xil bo‘lsa, ikkinchi harfga qaraymiz: qalam, qor, qush.\n"
        "• O‘, G‘, Sh, Ch alifbo oxirida: “zebra” dan keyin “o‘rdak”, undan keyin “sher” keladi.", items=items)

# ------------------------------------------------------------ unli va undosh tovushlar
items = []
for w, d in [("qovoq", 1), ("lagan", 1), ("sichqon", 1), ("o‘rmon", 2), ("kamalak", 2), ("chumchuq", 2), ("televizor", 3)]:
    vs = vowels_of(w)
    items.append(Q(f"“{w}” so‘zida nechta unli bor?", f"{len(vs)} ta", nta(len(vs)), d=d,
                   x=f"{w}: {', '.join(vs)} — {len(vs)} ta unli."))
for w, d in [("bulut", 1), ("shamol", 2), ("daraxt", 2)]:
    cons = [c for c in letters(w) if c not in VOWELS]
    n = len(cons)
    items.append(Q(f"“{w}” so‘zida nechta undosh bor?", f"{n} ta", nta(n), d=d,
                   x=f"{w}: {', '.join(cons)} — {n} ta undosh." + (" sh — bitta tovush." if "sh" in cons else "")))
for text, pic, right, wrong, word in [("s … bzi", "🥕", "a", ["o", "u", "i"], "sabzi"),
                                      ("q … vun", "🍈", "o", ["a", "u", "i"], "qovun"),
                                      ("b … lut", "☁️", "u", ["a", "o", "e"], "bulut"),
                                      ("t … xum", "🥚", "u", ["o", "a", "i"], "tuxum"),
                                      ("l … mon", "🍋", "i", ["a", "u", "o‘"], "limon")]:
    assert text.replace(" … ", right) == word
    items.append(Q("Tushib qolgan unlini toping.", right, wrong, text=text, e=pic, x=f"{word}: “{right}” unlisi tushib qolgan."))
items += [
    Q("Qaysi so‘z unli tovush bilan boshlanadi?", "eshak", ["mushuk", "quyon", "tulki"],
      x="eshak — e unlisi bilan boshlanadi; qolganlari undosh bilan boshlanadi."),
    Q("Qaysi so‘z undosh tovush bilan boshlanadi?", "bulut", ["olma", "uzum", "anor"],
      x="bulut — b undoshi bilan; olma, uzum, anor — unli bilan boshlanadi."),
    Q("Qaysi qatorda faqat unli harflar yozilgan?", "a, e, o‘", ["a, b, e", "m, o, u", "i, k, l"],
      x="a, e, o‘ — uchalasi ham unli. b, m, k, l — undoshlar."),
    Q("Qaysi qatorda faqat undosh harflar yozilgan?", "b, sh, q", ["b, a, q", "o, sh, l", "e, i, t"], d=2,
      x="b, sh, q — undoshlar. a, o, e, i — unlilar."),
    Q("Qaysi so‘zda faqat bitta unli bor?", "qush", ["olma", "bulut", "anor"],
      x="qush — bitta unli (u). olma, bulut, anor — ikkitadan unli."),
    Q("Qaysi so‘zda unlilar eng ko‘p?", "kamalak", ["bulut", "qor", "sabzi"], d=2,
      x="ka-ma-lak — 3 ta unli; bulut va sabzi — 2 ta, qor — 1 ta."),
    Q("“gilam” so‘zidagi undoshlar qaysilar?", "g, l, m", ["g, i, m", "i, a", "l, a, m"], d=2,
      x="gilam: g, l, m — undosh; i, a — unli."),
    Q("“kuchuk” so‘zida nechta tovush bor?", "5 ta", ["6 ta", "4 ta", "7 ta"], d=2,
      x="k-u-ch-u-k — 5 ta tovush, chunki ch — bitta tovush."),
    TF("“i” — unli tovush.", True, x="Unlilar: a, o, u, e, i, o‘."),
    TF("“qor” so‘zi unli bilan boshlanadi.", False, x="qor — q undoshi bilan boshlanadi."),
    TF("“kamalak” so‘zidagi hamma unlilar bir xil.", True, d=2, x="ka-ma-lak: uchala unli ham — a."),
    TF("“y” — unli tovush.", False, d=2, x="y — undosh: uy, oy, yo‘l."),
    TF("Har bir so‘zda kamida bitta unli bo‘ladi.", True, d=2, x="Unlisiz so‘z bo‘lmaydi: uy, qor, ot."),
    MATCH("So‘zni birinchi unlisi bilan juftlang",
          [("bulut", "u"), ("sabzi", "a"), ("qor", "o"), ("piyoz", "i"), ("tez", "e"), ("ko‘l", "o‘")], d=2,
          x="Har bir so‘zdagi birinchi unlini topamiz: bulut — u, sabzi — a, qor — o, piyoz — i, tez — e, ko‘l — o‘."),
]
T.topic("sounds", "🅰️", L("Unli va undosh tovushlar", "Vowels and consonants", "Гласные и согласные"), C1,
        "Tovushlar ikki xil bo‘ladi: unli va undosh.\n"
        "• Unlilar 6 ta: a, o, u, e, i, o‘. Ularni cho‘zib aytish mumkin.\n"
        "• Qolgan tovushlar — undoshlar: b, d, k, l, m, q, y, sh, ch …\n"
        "• Har bir so‘zda kamida bitta unli bor.\n"
        "Misol: “bulut” so‘zida u, u — unli; b, l, t — undosh.", items=items)

# ------------------------------------------------------------ jarangli va jarangsiz undoshlar
PAIRS = [("b", "p"), ("d", "t"), ("g", "k"), ("z", "s"), ("v", "f"), ("j", "ch")]
items = []
for v, u, wrong, d in [("b", "p", ["d", "m", "v"], 1), ("d", "t", ["b", "n", "s"], 1), ("g", "k", ["q", "d", "t"], 1),
                       ("z", "s", ["j", "t", "f"], 1), ("v", "f", ["b", "p", "x"], 2), ("j", "ch", ["z", "s", "t"], 2)]:
    assert (v, u) in PAIRS
    items.append(Q(f"“{v}” ning jarangsiz jufti qaysi?", u, wrong, d=d, x=f"{v} — {u}: {v} jarangli, {u} esa jarangsiz."))
for u, v, wrong, d in [("t", "d", ["b", "z", "g"], 1), ("s", "z", ["d", "j", "v"], 1), ("k", "g", ["b", "d", "z"], 1),
                       ("ch", "j", ["z", "d", "g"], 2)]:
    assert (v, u) in PAIRS
    items.append(Q(f"“{u}” ning jarangli jufti qaysi?", v, wrong, d=d, x=f"{v} — {u}: {u} jarangsiz, uning jarangli jufti — {v}."))
items += [
    Q("Qaysi undosh jarangli?", "z", ["s", "t", "k"], x="z — jarangli: aytganda tomoq titraydi. s, t, k — jarangsiz."),
    Q("Qaysi undosh jarangli?", "d", ["t", "p", "f"], x="d — jarangli. t, p, f — jarangsiz."),
    Q("Qaysi undosh jarangsiz?", "p", ["b", "d", "z"], x="p — jarangsiz, ovozsiz aytiladi. b, d, z — jarangli."),
    Q("Qaysi undosh jarangsiz?", "ch", ["j", "b", "g"], d=2, x="ch — jarangsiz. j, b, g — jarangli."),
    Q("Qaysi so‘z jarangli undosh bilan boshlanadi?", "baliq", ["piyoz", "tovuq", "sabzi"], d=2,
      x="baliq — b jarangli. piyoz (p), tovuq (t), sabzi (s) — jarangsiz undosh bilan boshlanadi."),
    Q("Qaysi so‘z jarangsiz undosh bilan boshlanadi?", "kalit", ["gilam", "daraxt", "zina"], d=2,
      x="kalit — k jarangsiz. gilam (g), daraxt (d), zina (z) — jarangli undosh bilan boshlanadi."),
    Q("“gul” so‘zidagi “g” ni “k” ga almashtirsak, qaysi so‘z hosil bo‘ladi?", "kul", ["kel", "gil", "kun"], e="🌸", d=2,
      x="gul — kul: bitta tovush almashsa, so‘zning ma’nosi ham o‘zgaradi."),
    Q("Qaysi juftlik to‘g‘ri?", "g — k", ["g — t", "b — d", "z — ch"], d=2, x="g — k: jarangli va jarangsiz juft undoshlar."),
    Q("Qaysi juftlik to‘g‘ri?", "v — f", ["v — p", "d — s", "j — k"], d=3, x="v — f: jarangli va jarangsiz juft undoshlar."),
    Q("“daraxt” so‘zidagi birinchi tovush qanday?", "Jarangli undosh", ["Jarangsiz undosh", "Unli"], d=2,
      x="daraxt so‘zi d bilan boshlanadi, d — jarangli undosh."),
    Q("“sabzi” so‘zidagi birinchi tovush qanday?", "Jarangsiz undosh", ["Jarangli undosh", "Unli"], d=2,
      x="sabzi so‘zi s bilan boshlanadi, s — jarangsiz undosh."),
    TF("“b” va “p” — juft undoshlar.", True, x="b — jarangli, p — jarangsiz."),
    TF("“s” — jarangli undosh.", False, x="s — jarangsiz; uning jarangli jufti — z."),
    TF("Jarangli undosh aytilganda tomoq titraydi.", True, d=2,
       x="Kaftingizni tomog‘ingizga qo‘yib “z-z-z” deng — titraydi; “s-s-s” deganda titramaydi."),
    TF("“gul” va “kul” so‘zlari bitta tovush bilan farq qiladi.", True, d=2, x="g va k — juft undoshlar: gul — kul."),
    TF("“m” undoshining jarangsiz jufti yo‘q.", True, d=3, x="m, n, l, r — jarangli undoshlar, lekin ularning jarangsiz jufti yo‘q."),
    MATCH("Jarangli undoshni jarangsiz jufti bilan juftlang", PAIRS, x="Juft undoshlar: b–p, d–t, g–k, z–s, v–f, j–ch."),
]
T.topic("voiced", "🔔", L("Jarangli va jarangsiz undoshlar", "Voiced and voiceless consonants", "Звонкие и глухие согласные"), C1,
        "Undoshlar jarangli va jarangsiz bo‘ladi.\n"
        "• Jarangli undosh ovoz bilan aytiladi, tomoq titraydi: b, d, g, z, v, j.\n"
        "• Jarangsiz undosh ovozsiz, faqat shovqin bilan aytiladi: p, t, k, s, f, ch.\n"
        "• Ular juft bo‘ladi: b–p, d–t, g–k, z–s, v–f, j–ch.\n"
        "Sinab ko‘ring: kaftingizni tomog‘ingizga qo‘yib “z” va “s” ni ayting.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["alphabet_order", "sounds", "voiced"], C1)

# ============================================================ 2-chorak
# ------------------------------------------------------------ bo‘g‘in va so‘zni ko‘chirish
SYL2 = {"sichqon": ["sich", "qon"], "o‘rmon": ["o‘r", "mon"], "lagan": ["la", "gan"], "qaldirg‘och": ["qal", "dir", "g‘och"],
        "chumchuq": ["chum", "chuq"], "go‘sht": ["go‘sht"], "televizor": ["te", "le", "vi", "zor"], "ruchka": ["ruch", "ka"],
        "sumka": ["sum", "ka"], "kuchuk": ["ku", "chuk"], "bulbul": ["bul", "bul"], "qishloq": ["qish", "loq"],
        "ko‘cha": ["ko‘", "cha"], "kamalak": ["ka", "ma", "lak"], "ananas": ["a", "na", "nas"], "tongda": ["tong", "da"]}
for w, s in SYL2.items():
    check_syl(w, s)
items = []
for w, d in [("go‘sht", 1), ("lagan", 1), ("sumka", 1), ("bulbul", 1), ("qaldirg‘och", 2), ("televizor", 3)]:
    syl = SYL2[w]
    n = len(syl)
    items.append(Q(f"“{w}” so‘zida nechta bo‘g‘in bor?", f"{n} ta", nta(n), d=d,
                   x=f"{'-'.join(syl)} — {n} ta bo‘g‘in, chunki {n} ta unli bor."))
for w, wrong, d, why in [("ruchka", ["ru-chka", "ruc-hka", "ruchk-a"], 1, "ch — bitta tovush, uni bo‘lib bo‘lmaydi."),
                         ("ko‘cha", ["ko‘c-ha", "ko‘ch-a", "k-o‘cha"], 1, "ch bo‘linmaydi va bitta harf qolmaydi."),
                         ("sichqon", ["si-chqon", "sic-hqon", "sichq-on"], 1, "har bir bo‘g‘inda bitta unli, ch bo‘linmaydi."),
                         ("qishloq", ["qis-hloq", "qi-shloq", "qishl-oq"], 2, "sh — bitta tovush, u bo‘linmaydi."),
                         ("kuchuk", ["kuc-huk", "kuch-uk", "k-uchuk"], 2, "ch bo‘linmaydi."),
                         ("tongda", ["ton-gda", "to-ngda", "tongd-a"], 3, "ng — bitta tovush, u bo‘linmaydi.")]:
    right = "-".join(SYL2[w])
    assert right not in wrong and all(x.replace("-", "") == w for x in wrong)
    items.append(Q(f"“{w}” so‘zi qanday ko‘chiriladi?", right, wrong, d=d, x=f"{right}: {why}"))
items += [
    Q("“kamalak” so‘zini qanday ko‘chirish mumkin?", "kama-lak", ["kam-alak", "kamal-ak", "k-amalak"], d=2,
      x="ka-ma-lak: bo‘g‘in chegarasida ko‘chiramiz — ka-malak yoki kama-lak."),
    Q("“ananas” so‘zini qanday ko‘chirish mumkin?", "ana-nas", ["a-nanas", "anan-as", "an-anas"], d=3,
      x="a-na-nas: bitta “a” ni qatorda qoldirib bo‘lmaydi, shuning uchun ana-nas."),
    Q("Qaysi so‘zni ko‘chirib bo‘lmaydi?", "uka", ["sumka", "ruchka", "lagan"],
      x="u-ka: bitta “u” harfini qatorda qoldirib bo‘lmaydi."),
    Q("Qaysi so‘zni ko‘chirib bo‘lmaydi?", "non", ["sabzi", "bulbul", "o‘rmon"],
      x="non — bir bo‘g‘inli so‘z, u ko‘chirilmaydi."),
    Q("Qaysi so‘zni ko‘chirib bo‘lmaydi?", "ilon", ["sichqon", "kuchuk", "chumchuq"], d=2,
      x="i-lon: bitta “i” harfi qolib ketadi, shuning uchun ko‘chirilmaydi."),
    Q("Qaysi so‘zni ko‘chirib bo‘lmaydi?", "go‘sht", ["go‘zal", "ko‘cha", "qo‘zi"], d=2,
      x="go‘sht — bir bo‘g‘inli so‘z. go‘-zal, ko‘-cha, qo‘-zi esa ko‘chiriladi."),
    Q("Qaysi so‘zni ko‘chirib bo‘lmaydi?", "o‘rik", ["o‘rmon", "olma", "archa"], d=3,
      x="o‘-rik: o‘ — bitta harf, uni qatorda qoldirib bo‘lmaydi. o‘r-mon, ol-ma, ar-cha esa ko‘chiriladi."),
    Q("Qaysi so‘zni ko‘chirish mumkin?", "sumka", ["ona", "uy", "ari"],
      x="sum-ka. “ona” va “ari” da bitta harf qoladi, “uy” — bir bo‘g‘inli so‘z."),
    Q("Nima uchun “uka” so‘zini ko‘chirib bo‘lmaydi?", "Bitta harf qolib ketadi", ["So‘z juda uzun", "Unda unli yo‘q",
                                                                                 "U katta harf bilan yoziladi"], d=2,
      x="u-ka: birinchi bo‘g‘in bitta harfdan iborat, uni qatorda qoldirib bo‘lmaydi."),
    TF("“sh” ni ko‘chirishda bo‘lib yuborish mumkin.", False, x="sh, ch, ng — bitta tovush, ular bo‘linmaydi: qish-loq."),
    TF("Bir bo‘g‘inli so‘z ko‘chirilmaydi.", True, x="non, qor, go‘sht — keyingi qatorga butunligicha yoziladi."),
    TF("“sum-ka” — to‘g‘ri ko‘chirilgan.", True, x="sum-ka: har bir bo‘g‘inda bitta unli bor."),
    TF("“u-zum” — to‘g‘ri ko‘chirilgan.", False, d=2, x="Bitta “u” harfini qatorda qoldirib bo‘lmaydi; “uzum” ko‘chirilmaydi."),
    MATCH("So‘zni bo‘g‘inlari bilan juftlang",
          [(w, "-".join(SYL2[w])) for w in ["sichqon", "chumchuq", "ruchka", "o‘rmon", "bulbul", "qaldirg‘och"]], d=2,
          x="Har bir bo‘g‘inda bitta unli bor."),
]
T.topic("syllables", "✂️", L("Bo‘g‘in va so‘zni ko‘chirish", "Syllables and hyphenation", "Слог и перенос слов"), C2,
        "Har bir bo‘g‘inda bitta unli bor: mak-tab, ki-tob.\n"
        "• Qatorga sig‘masa, so‘z bo‘g‘inlab ko‘chiriladi: mak- (keyingi qatorda) tab.\n"
        "• Bitta harfni qatorda qoldirib ham, keyingi qatorga o‘tkazib ham bo‘lmaydi: “ona”, “uka” ko‘chirilmaydi.\n"
        "• Bir bo‘g‘inli so‘z ko‘chirilmaydi: non, go‘sht.\n"
        "• sh, ch, ng bo‘linmaydi: qish-loq, ko‘-cha, tong-da.", items=items)

# ------------------------------------------------------------ o‘, g‘ va tutuq belgisi
items = []
for right, wrong, pic, d, why in [
        ("qog‘oz", ["qogoz", "qo‘g‘oz", "qog‘o‘z"], "📄", 1, "qog‘oz — faqat g‘ harfi belgili, o harflari belgisiz."),
        ("yomg‘ir", ["yomgir", "yo‘mg‘ir", "yomg‘ur"], "🌧️", 1, "yomg‘ir — g‘ harfi bilan."),
        ("ko‘ylak", ["koylak", "ko‘ylik", "kuylak"], "👗", 1, "ko‘ylak — o‘ harfi bilan."),
        ("o‘quvchi", ["oquvchi", "o‘qivchi", "uquvchi"], None, 1, "o‘quvchi — o‘qiydigan bola; o‘ harfi bilan boshlanadi."),
        ("qarg‘a", ["qarga", "qarg‘o", "qarqa"], None, 1, "qarg‘a — g‘ harfi bilan."),
        ("sog‘lom", ["soglom", "so‘g‘lom", "sog‘lim"], None, 2, "sog‘lom — g‘ harfi bilan, o harfi belgisiz."),
        ("qo‘ng‘iz", ["qong‘iz", "qo‘ngiz", "qongiz"], "🐞", 2, "qo‘ng‘iz — ikkala belgi ham kerak: o‘ va g‘."),
        ("yog‘och", ["yogoch", "yo‘g‘och", "yog‘uch"], None, 2, "yog‘och — g‘ harfi bilan."),
        ("a’lochi", ["alochi", "al’ochi", "a’lochiy"], None, 1, "a’lochi — a’lo o‘qiydigan o‘quvchi; tutuq belgisi a dan keyin."),
        ("va’da", ["vada", "vad’a", "vaada"], None, 3, "va’da — tutuq belgisi a dan keyin yoziladi.")]:
    items.append(Q("To‘g‘ri yozilgan so‘zni toping.", right, wrong, e=pic, d=d, x=why))
items += [
    Q("Gapni to‘ldiring: “Piyola … qoldi.”", "bo‘sh", ["bosh", "bush", "bo‘st"], d=2,
      x="bo‘sh — ichida hech narsa yo‘q. bosh — tananing qismi."),
    Q("Gapni to‘ldiring: “Baliqchi suvga … tashladi.”", "to‘r", ["tor", "tur", "to‘rt"], d=2,
      x="to‘r — baliq tutadigan narsa; tor — keng emas."),
    Q("Gapni to‘ldiring: “Bu ko‘cha juda …”", "tor", ["to‘r", "tur", "to‘rt"], d=2,
      x="tor — keng emas. to‘r esa baliq tutadigan narsa."),
    Q("Gapni to‘ldiring: “Ovqatdan oldin … yuvamiz.”", "qo‘limizni", ["qolimizni", "qulimizni", "qo‘limizini"], d=2,
      x="qo‘l so‘zi o‘ harfi bilan yoziladi: qo‘limizni."),
    Q("To‘g‘ri yozilgan ismni toping.", "Ra’no", ["Rano", "Ran’o", "Raano"], d=2, x="Ra’no — tutuq belgisi a dan keyin keladi."),
    Q("Gapni to‘ldiring: “Olmaning … juda shirin.”", "ta’mi", ["tami", "tam’i", "taami"], d=2,
      x="ta’m so‘zi tutuq belgisi bilan yoziladi: ta’mi."),
    Q("Qaysi so‘zda tutuq belgisi bor?", "ta’m", ["tom", "tosh", "tut"], x="ta’m — tutuq belgisi (’) bilan yoziladi."),
    Q("Qaysi ismda tutuq belgisi bor?", "Ma’mura", ["Malika", "Madina", "Marjona"], x="Ma’mura — tutuq belgisi a dan keyin."),
    Q("Gapni to‘ldiring: “Men chiroyli … chizdim.”", "surat", ["sur’at", "suratt", "sura’t"], d=3,
      x="surat — rasm, u tutuq belgisisiz yoziladi. sur’at esa tezlikni bildiradi."),
    TF("“bosh” va “bo‘sh” — har xil so‘zlar.", True, x="bosh — tananing qismi, bo‘sh — ichida hech narsa yo‘q."),
    TF("“to‘r” va “tor” so‘zlari bir xil ma’noni bildiradi.", False, x="to‘r — baliq tutadigan narsa, tor — keng emas."),
    TF("“o‘quvchi” so‘zi o‘ harfi bilan boshlanadi.", True, x="o‘-quv-chi: birinchi harf — o‘."),
    TF("“qog‘oz” so‘zida ikkita g‘ harfi bor.", False, d=2, x="qo-g‘oz: faqat bitta g‘ bor."),
    MATCH("So‘zni ma’nosi bilan juftlang", [("bosh", "tananing qismi"), ("bo‘sh", "ichida hech narsa yo‘q"), ("tor", "keng emas"),
                                            ("to‘r", "baliq tutadigan narsa"), ("ot", "hayvon"), ("o‘t", "maysa, ko‘kat")], d=2,
          x="o‘ harfining belgisi tushib qolsa, so‘zning ma’nosi o‘zgaradi."),
]
T.topic("og_tutuq", "✏️", L("O‘, G‘ va tutuq belgisi", "O‘, G‘ and the apostrophe", "O‘, G‘ и знак тутук"), C2,
        "O‘ va G‘ harflari o va g ga ‘ belgisi qo‘shib yoziladi: o‘rmon, qog‘oz, qo‘ng‘iz.\n"
        "• Belgi tushib qolsa, so‘z o‘zgaradi: bosh — bo‘sh, tor — to‘r.\n"
        "• Tutuq belgisi (’) ba’zi so‘zlarda yoziladi: a’lochi, ta’m, va’da, Ra’no.\n"
        "• Tutuq belgisi ham so‘zni farqlaydi: sher — she’r.", items=items)

# ------------------------------------------------------------ qo‘sh undoshli so‘zlar
items = []
for right, wrong, d, why in [("katta", ["kata", "kaata", "katto"], 1, "katta — ikkita t: kat-ta."),
                             ("ikki", ["iki", "ikkiy", "iiki"], 1, "ikki — ikkita k: ik-ki."),
                             ("issiq", ["isiq", "isseq", "issik"], 1, "issiq — ikkita s: is-siq."),
                             ("yetti", ["yeti", "yette", "yatti"], 1, "yetti — ikkita t: yet-ti."),
                             ("bitta", ["bita", "bitte", "biita"], 1, "bitta — ikkita t: bit-ta."),
                             ("sakkiz", ["sakiz", "sakkez", "saqqiz"], 1, "sakkiz — ikkita k: sak-kiz."),
                             ("to‘qqiz", ["to‘qiz", "toqqiz", "to‘qquz"], 2, "to‘qqiz — ikkita q: to‘q-qiz."),
                             ("o‘ttiz", ["o‘tiz", "ottiz", "o‘ttuz"], 2, "o‘ttiz — ikkita t: o‘t-tiz."),
                             ("tikka", ["tika", "tiqqa", "tikko"], 2, "tikka — ikkita k: tik-ka."),
                             ("oppoq", ["opoq", "oppaq", "oppok"], 2, "oppoq — ikkita p: op-poq."),
                             ("hamma", ["hama", "xamma", "hamme"], 2, "hamma — ikkita m: ham-ma."),
                             ("mitti", ["miti", "mitte", "mittiy"], 2, "mitti — ikkita t: mit-ti.")]:
    items.append(Q("To‘g‘ri yozilgan so‘zni toping.", right, wrong, d=d, x=why))
items += [
    Q("Qaysi so‘zda qo‘sh undosh bor?", "katta", ["kichik", "uzun", "baland"], x="katta — ikkita t."),
    Q("Qaysi so‘zda qo‘sh undosh bor?", "yetti", ["olti", "besh", "to‘rt"], x="yetti — ikkita t; olti — bitta t."),
    Q("Qaysi so‘zda qo‘sh undosh bor?", "issiq", ["sovuq", "iliq", "salqin"], x="issiq — ikkita s."),
    Q("Qaysi so‘zda qo‘sh undosh bor?", "gullar", ["kitoblar", "olmalar", "uylar"], d=2, x="gul + lar = gullar: ikkita l."),
    Q("“qo‘l” so‘ziga “-lar” qo‘shing.", "qo‘llar", ["qo‘lar", "qo‘lllar", "qollar"], d=2, x="qo‘l + lar = qo‘llar: ikkita l."),
    Q("“katta” so‘zi qanday ko‘chiriladi?", "kat-ta", ["ka-tta", "katt-a", "k-atta"], d=2,
      x="Qo‘sh undosh ko‘chirishda ikkiga bo‘linadi: kat-ta."),
    Q("“ikki” so‘zi qanday ko‘chiriladi?", "ik-ki", ["i-kki", "ikk-i"], d=3,
      x="ik-ki: qo‘sh undosh ikki bo‘g‘inga bo‘linadi, bitta harf qolmaydi."),
    Q("Gapni to‘ldiring: “Qalampir juda … bo‘ladi.”", "achchiq", ["achiq", "achchik", "ochchiq"], d=2,
      x="achchiq — ikkita ch: ach-chiq."),
    TF("“katta” so‘zida ikkita “t” bor.", True, x="kat-ta: ikkita t."),
    TF("“kitob” so‘zi ikkita “t” bilan yoziladi.", False, x="kitob — bitta t: ki-tob."),
    TF("“sakkiz” so‘zida qo‘sh undosh bor.", True, x="sak-kiz — ikkita k."),
    TF("“olti” so‘zi qo‘sh “t” bilan yoziladi.", False, d=2, x="olti — bitta t; yetti esa ikkita t bilan yoziladi."),
    MATCH("Sonni so‘z bilan juftlang", [("2", "ikki"), ("7", "yetti"), ("8", "sakkiz"), ("9", "to‘qqiz"), ("30", "o‘ttiz"),
                                        ("50", "ellik")], d=2, x="Bu son nomlarining hammasida qo‘sh undosh bor."),
]
T.topic("double_cons", "✍️", L("Qo‘sh undoshli so‘zlar", "Double consonants", "Удвоенные согласные"), C2,
        "Ba’zi so‘zlarda bir xil undosh ikki marta yoziladi: katta, ikki, tikka, issiq, achchiq.\n"
        "• Bunday so‘zda undosh cho‘ziqroq eshitiladi: kat-ta.\n"
        "• Ko‘chirganda qo‘sh undosh ikkiga bo‘linadi: kat-ta, ik-ki.\n"
        "• -lar qo‘shilganda ham qo‘sh undosh paydo bo‘lishi mumkin: gul + lar = gullar.\n"
        "• Bitta undoshli so‘zga ortiqcha harf qo‘shmang: kitob, olti.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["syllables", "og_tutuq", "double_cons"], C2)

# ============================================================ 3-chorak
# ------------------------------------------------------------ ma’nodosh va qarama-qarshi ma’noli so‘zlar
SYN2 = [("qo‘shiq", "ashula", ["raqs", "rasm", "o‘yin"], 1),
        ("shifokor", "doktor", ["haydovchi", "oshpaz", "sotuvchi"], 1),
        ("ota", "dada", ["aka", "bobo", "amaki"], 1),
        ("kichkina", "mitti", ["ulkan", "baland", "uzun"], 1),
        ("yugurmoq", "chopmoq", ["yurmoq", "o‘tirmoq", "uxlamoq"], 1),
        ("sekin", "asta", ["tez", "shoshib", "darhol"], 1),
        ("oz", "kam", ["ko‘p", "mo‘l", "katta"], 2),
        ("xafa", "g‘amgin", ["xursand", "quvnoq", "kulgili"], 2),
        ("mazali", "lazzatli", ["bemaza", "sovuq", "qattiq"], 2),
        ("eski", "ko‘hna", ["yangi", "toza", "katta"], 2),
        ("baqirmoq", "qichqirmoq", ["shivirlamoq", "kulmoq", "tinglamoq"], 2),
        ("o‘qituvchi", "muallim", ["o‘quvchi", "shifokor", "quruvchi"], 2),
        ("baland", "yuksak", ["past", "pastak", "keng"], 3),
        ("charchamoq", "horimoq", ["dam olmoq", "uxlamoq", "o‘ynamoq"], 3)]
ANT_CTX = [("Fil katta, sichqon esa …", "kichik", ["ulkan", "baland", "semiz"], "🐘", 1),
           ("Yozda havo issiq, qishda esa …", "sovuq", ["iliq", "qaynoq", "quruq"], None, 1),
           ("Quyon tez yuguradi, toshbaqa esa … yuradi.", "sekin", ["tez", "chaqqon", "uzoq"], "🐢", 1),
           ("Maktab uyimizga yaqin, bozor esa …", "uzoq", ["yaqin", "katta", "yangi"], None, 1),
           ("Jirafa baland, toshbaqa esa …", "past", ["uzun", "baland", "katta"], "🦒", 1),
           ("Kitob qalin, daftar esa …", "yupqa", ["qalin", "og‘ir", "katta"], None, 2),
           ("Mushuk ichkarida, it esa …", "tashqarida", ["ichkarida", "uyda", "xonada"], None, 2),
           ("Ertalab quyosh chiqadi, … esa botadi.", "kechqurun", ["ertalab", "tongda", "tushda"], None, 2)]
ANT2 = [("ochiq", "yopiq", ["keng", "katta", "toza"], 1),
        ("o‘ng", "chap", ["old", "tepa", "o‘rta"], 1),
        ("ko‘p", "oz", ["mo‘l", "katta", "uzun"], 1),
        ("semiz", "oriq", ["katta", "og‘ir", "baland"], 2),
        ("sog‘", "kasal", ["baquvvat", "kuchli", "quvnoq"], 2),
        ("bormoq", "kelmoq", ["ketmoq", "yurmoq", "chopmoq"], 2),
        ("topmoq", "yo‘qotmoq", ["izlamoq", "olmoq", "ko‘rmoq"], 2),
        ("savol", "javob", ["so‘z", "gap", "xat"], 2),
        ("chuqur", "sayoz", ["keng", "uzun", "katta"], 3),
        ("yutmoq", "yutqazmoq", ["o‘ynamoq", "topmoq", "olmoq"], 3)]
items = []
for a, b, wrong, d in SYN2:
    items.append(Q(f"“{a}” so‘zining ma’nodoshini toping.", b, wrong, d=d, x=f"“{a}” va “{b}” — ma’nodosh so‘zlar: ma’nosi bir xil."))
for text, right, wrong, pic, d in ANT_CTX:
    full = text.replace("…", right)
    full = full if full.endswith(".") else full + "."
    items.append(Q(f"Qarama-qarshi ma’noli so‘zni qo‘ying: “{text}”", right, wrong, e=pic, d=d,
                   x=f"{full} Bu gapda qarama-qarshi ma’noli so‘zlar bor."))
for a, b, wrong, d in ANT2:
    items.append(Q(f"“{a}” so‘ziga qarama-qarshi ma’noli so‘zni toping.", b, wrong, d=d,
                   x=f"“{a}” — “{b}”: ma’nosi bir-biriga qarama-qarshi."))
items += [
    Q("“ism — nom” — qanday so‘zlar?", "Ma’nodosh so‘zlar", ["Qarama-qarshi ma’noli so‘zlar", "Bir xil yoziladigan so‘zlar"],
      x="ism va nom — bir xil ma’noni bildiradi: ma’nodosh so‘zlar."),
    Q("“birinchi — oxirgi” — qanday so‘zlar?", "Qarama-qarshi ma’noli so‘zlar", ["Ma’nodosh so‘zlar", "Bir xil yoziladigan so‘zlar"],
      x="birinchi va oxirgi — ma’nosi bir-biriga qarama-qarshi."),
    TF("“yirik” va “katta” — ma’nodosh so‘zlar.", True, x="Ikkalasi ham kattalikni bildiradi: yirik olma — katta olma."),
    TF("“qalin” va “yupqa” — ma’nodosh so‘zlar.", False, x="qalin va yupqa — qarama-qarshi ma’noli so‘zlar."),
    MATCH("Ma’nodosh so‘zlarni juftlang", [("qo‘shiq", "ashula"), ("shifokor", "doktor"), ("ota", "dada"), ("sekin", "asta"),
                                           ("kichkina", "mitti"), ("oz", "kam")], d=2, x="Ma’nodosh so‘zlarning ma’nosi bir xil."),
    MATCH("Qarama-qarshi ma’noli so‘zlarni juftlang", [("yaqin", "uzoq"), ("qalin", "yupqa"), ("semiz", "oriq"), ("ochiq", "yopiq"),
                                                       ("o‘ng", "chap"), ("savol", "javob")], d=2,
          x="Qarama-qarshi ma’noli so‘zlarning ma’nosi bir-biriga zid."),
]
T.topic("word_meaning", "↔️", L("Ma’nodosh va qarama-qarshi ma’noli so‘zlar", "Synonyms and antonyms", "Синонимы и антонимы"), C3,
        "• Ma’nodosh (sinonim) so‘zlar — yozilishi har xil, ma’nosi bir xil yoki yaqin so‘zlar:\n"
        "  qo‘shiq — ashula, shifokor — doktor, sekin — asta.\n"
        "• Qarama-qarshi ma’noli (antonim) so‘zlar — ma’nosi bir-biriga zid so‘zlar:\n"
        "  yaqin — uzoq, qalin — yupqa, ochiq — yopiq.\n"
        "Misol: Fil katta, sichqon esa kichik.", items=items)

# ------------------------------------------------------------ kim? nima?
items = []
for right, wrong, d, why in [("quruvchi", ["g‘isht", "uy", "devor"], 1, "quruvchi — odam, kasb egasi."),
                             ("opa", ["olma", "o‘rdak", "oyna"], 1, "opa — odam."),
                             ("sotuvchi", ["sumka", "do‘kon", "tarozi"], 1, "sotuvchi — odam, kasb egasi."),
                             ("o‘quvchi", ["o‘rdak", "o‘rik", "o‘tin"], 1, "o‘quvchi — odam."),
                             ("Zarina", ["zina", "zebra", "zanjir"], 2, "Zarina — qizning ismi.")]:
    items.append(Q("Qaysi so‘z “kim?” so‘rog‘iga javob beradi?", right, wrong, d=d,
                   x=f"{why} Odamni bildirgan so‘z kim? so‘rog‘iga javob beradi."))
for right, wrong, d, why in [("daftar", ["o‘qituvchi", "opa", "bobo"], 1, "daftar — narsa."),
                             ("chinor", ["bog‘bon", "dadam", "amakim"], 1, "chinor — daraxt."),
                             ("kapalak", ["qizcha", "ukam", "buvim"], 1, "kapalak — hasharot."),
                             ("qo‘zichoq", ["cho‘pon", "bola", "dehqon"], 2, "qo‘zichoq — hayvon.")]:
    items.append(Q("Qaysi so‘z “nima?” so‘rog‘iga javob beradi?", right, wrong, d=d,
                   x=f"{why} Narsa, hayvon va o‘simlik nomlari nima? so‘rog‘iga javob beradi."))
for ask, right, wrong, text, d, why in [
        ("kim?", "Buvim", ["mazali", "palov", "pishirdi"], "Buvim mazali palov pishirdi.", 2, "Kim pishirdi? — Buvim."),
        ("nima?", "velosiped", ["Dadam", "yangi", "oldi"], "Dadam yangi velosiped oldi.", 2, "Dadam nima oldi? — velosiped."),
        ("nimalar?", "Qushlar", ["daraxtda", "sayrayapti"], "Qushlar daraxtda sayrayapti.", 3, "Nimalar sayrayapti? — Qushlar."),
        ("kimlar?", "O‘quvchilar", ["maktabga", "kelishdi"], "O‘quvchilar maktabga kelishdi.", 3, "Kimlar kelishdi? — O‘quvchilar.")]:
    items.append(Q(f"Gapdagi “{ask}” so‘rog‘iga javob bo‘ladigan so‘zni toping.", right, wrong, text=text, d=d, x=why))
items += [
    Q("“kitoblar” so‘zi qaysi so‘roqqa javob beradi?", "nimalar?", ["kimlar?", "kim?", "qanday?"], d=2,
      x="kitoblar — ko‘p narsa: nimalar?"),
    Q("“bolalar” so‘zi qaysi so‘roqqa javob beradi?", "kimlar?", ["nimalar?", "nima?", "qanday?"], d=2,
      x="bolalar — ko‘p odam: kimlar?"),
    Q("Hayvon nomlari qaysi so‘roqqa javob beradi?", "nima?", ["kim?", "qanday?", "nima qildi?"],
      x="Hayvon nomlari nima? so‘rog‘iga javob beradi: mushuk, quyon, qo‘zichoq."),
    Q("Kasb nomlari qaysi so‘roqqa javob beradi?", "kim?", ["nima?", "qanday?", "nima qildi?"],
      x="Kasb egasi — odam: shifokor, haydovchi — kim?"),
    Q("Qaysi so‘z ortiqcha?", "stol", ["haydovchi", "oshpaz", "duradgor"], d=2,
      x="haydovchi, oshpaz, duradgor — kim? so‘rog‘iga, stol esa nima? so‘rog‘iga javob beradi."),
    Q("Qaysi so‘z ortiqcha?", "nabira", ["qalam", "chizg‘ich", "o‘chirg‘ich"], d=2,
      x="qalam, chizg‘ich, o‘chirg‘ich — nima?; nabira esa odam: kim?"),
    Q("Rasmga qarang. Uning nomi qaysi so‘roqqa javob beradi?", "nima?", ["kim?", "qanday?"], e="🚂", x="Bu — poyezd, narsa: nima?"),
    Q("Rasmga qarang. Uni qaysi so‘roq bilan so‘raymiz?", "kim?", ["nima?", "qanday?"], e="👶", x="Bu — chaqaloq, odam: kim?"),
    TF("“daryo” so‘zi “nima?” so‘rog‘iga javob beradi.", True, x="daryo — odam emas: nima?"),
    TF("“ukam” so‘zi “nima?” so‘rog‘iga javob beradi.", False, x="ukam — odam: kim?"),
    TF("“qo‘g‘irchoq” so‘zi “kim?” so‘rog‘iga javob beradi.", False, d=2, x="qo‘g‘irchoq — o‘yinchoq, narsa: nima?"),
    TF("“chumoli” so‘zi “nima?” so‘rog‘iga javob beradi.", True, d=2, x="Hasharot nomlari ham nima? so‘rog‘iga javob beradi."),
]
T.topic("who_what", "❓", L("Kim? Nima? Narsa nomini bildirgan so‘zlar", "Who? What? Naming words", "Кто? Что? Слова-предметы"), C3,
        "Shaxs va narsa nomini bildirgan so‘zlar kim? yoki nima? so‘rog‘iga javob beradi.\n"
        "• kim? — odamlar: dadam, opa, quruvchi, Zarina.\n"
        "• nima? — narsa, hayvon, o‘simlik: daftar, qo‘zichoq, chinor.\n"
        "• Ko‘p bo‘lsa: kimlar? — o‘quvchilar; nimalar? — qushlar.", items=items)

# ------------------------------------------------------------ birlik va ko‘plik
items = [
    Q("Rasmga mos so‘zni tanlang.", "olma", ["olmalar", "olmala", "olmaler"], e="🍎", x="Rasmda bitta olma — birlik."),
    Q("Rasmga mos so‘zni tanlang.", "olmalar", ["olma", "olmala", "olmaler"], e="🍎🍎🍎", x="Rasmda ko‘p olma — ko‘plik: olma + lar."),
    Q("Rasmga mos so‘zni tanlang.", "baliqlar", ["baliq", "baliqla", "baliqler"], e="🐟🐟🐟", x="Ko‘p baliq — baliq + lar."),
    Q("Rasmga mos so‘zni tanlang.", "yulduz", ["yulduzlar", "yulduzla", "yulduzler"], e="⭐", x="Rasmda bitta yulduz — birlik."),
]
for one, many, wrong, d in [("qalam", "qalamlar", ["qalamla", "qalamler", "qalami"], 1),
                            ("quyon", "quyonlar", ["quyonla", "quyonler", "quyoni"], 1),
                            ("eshik", "eshiklar", ["eshikla", "eshikler", "eshigi"], 1),
                            ("nok", "noklar", ["nokla", "nokler", "noki"], 1),
                            ("piyola", "piyolalar", ["piyolar", "piyolala", "piyolaler"], 2),
                            ("yo‘l", "yo‘llar", ["yo‘lar", "yo‘lllar", "yollar"], 2)]:
    assert many == one + "lar"
    items.append(Q(f"Bitta — {one}, ko‘p — …?", many, wrong, d=d, x=f"{one} + lar = {many}."))
items += [
    Q("Ko‘p — lolalar, bitta — …?", "lola", ["lolalar", "lolala", "lollar"], x="lolalar = lola + lar. Bitta bo‘lsa: lola."),
    Q("Qaysi so‘z ko‘plikda?", "o‘yinchoqlar", ["qo‘g‘irchoq", "koptok", "kubik"], x="o‘yinchoq + lar — ko‘plik."),
    Q("Qaysi so‘z ko‘plikda?", "bulutlar", ["osmon", "quyosh", "yomg‘ir"], x="bulut + lar — ko‘plik."),
    Q("Qaysi so‘z birlikda?", "chumoli", ["asalarilar", "qo‘ng‘izlar", "kapalaklar"], x="chumoli — bitta; qolgan so‘zlarda -lar bor."),
    Q("Qaysi so‘z birlikda?", "o‘quvchi", ["qizlar", "bolalar", "o‘g‘illar"], d=2, x="o‘quvchi — bitta; qolgan so‘zlarda -lar bor."),
    Q("Ko‘plik qaysi qo‘shimcha bilan yasaladi?", "-lar", ["-li", "-chi", "-siz"], x="Ko‘plik -lar qo‘shimchasi bilan yasaladi: qalam — qalamlar."),
    Q("Qaysi birikma to‘g‘ri?", "uchta qush", ["uchta qushlar", "uchtalar qush", "uchta qushla"], d=2,
      x="Son bilan kelganda -lar qo‘shilmaydi: uchta qush."),
    Q("Qaysi birikma to‘g‘ri?", "beshta olma", ["beshta olmalar", "beshtalar olma", "beshta olmala"], d=2,
      x="Son bilan kelganda -lar qo‘shilmaydi: beshta olma."),
    Q("Gapni to‘ldiring: “Bog‘da ikkita … bor.”", "chinor", ["chinorlar", "chinorla", "chinorlari"], d=3,
      x="Son bilan -lar qo‘shilmaydi: Bog‘da ikkita chinor bor."),
    TF("“yulduzlar” so‘zi ko‘p narsani bildiradi.", True, x="yulduz + lar — ko‘plik."),
    TF("“to‘rtta kitoblar” deb yozish to‘g‘ri.", False, d=2, x="Son bilan -lar qo‘shilmaydi: to‘rtta kitob."),
    TF("“gul” so‘zining ko‘plik shakli “gular”.", False, d=2, x="gul + lar = gullar: ikkita l."),
    MATCH("Birlikni ko‘plik bilan juftlang", [("uy", "uylar"), ("gul", "gullar"), ("non", "nonlar"), ("tog‘", "tog‘lar"),
                                              ("qo‘l", "qo‘llar"), ("ot", "otlar")], x="Ko‘plik -lar qo‘shimchasi bilan yasaladi."),
]
T.topic("plural", "🍎", L("Birlik va ko‘plik", "Singular and plural", "Единственное и множественное число"), C3,
        "Bitta narsani bildirgan so‘z birlikda bo‘ladi: qalam, qush.\n"
        "Ko‘p narsani bildirgan so‘z ko‘plikda bo‘ladi. Ko‘plik -lar qo‘shimchasi bilan yasaladi: qalamlar, qushlar.\n"
        "• -lar doim bir xil yoziladi: uy — uylar, gul — gullar.\n"
        "• Son bilan kelganda -lar qo‘shilmaydi: uchta qalam, beshta qush.", items=items)

# ------------------------------------------------------------ atoqli otlar
items = []
for right, wrong, d, why in [("urganch", ["shahar", "ko‘cha", "maktab"], 1, "Urganch — shahar nomi."),
                             ("chirchiq", ["daryo", "suv", "ko‘prik"], 1, "Chirchiq — daryo nomi."),
                             ("dilshod", ["do‘st", "o‘rtoq", "sinfdosh"], 1, "Dilshod — bolaning ismi."),
                             ("jizzax", ["viloyat", "tuman", "qishloq"], 1, "Jizzax — shahar nomi."),
                             ("olapar", ["it", "kuchuk", "mushuk"], 2, "Olapar — itga qo‘yilgan nom."),
                             ("karimov", ["o‘qituvchi", "bola", "qo‘shni"], 2, "Karimov — familiya."),
                             ("norin", ["daryo", "ko‘l", "buloq"], 2, "Norin — daryo nomi.")]:
    items.append(Q("Qaysi so‘z gap o‘rtasida ham bosh harf bilan yoziladi?", right, wrong, d=d,
                   x=f"{why} U doim bosh harf bilan yoziladi: {right.capitalize()}."))
items += [
    Q("To‘g‘ri yozilganini toping.", "Ali Karimov", ["ali karimov", "Ali karimov", "ali Karimov"],
      x="Ism ham, familiya ham bosh harf bilan yoziladi."),
    Q("To‘g‘ri yozilganini toping.", "Urganch shahri", ["urganch shahri", "Urganch Shahri", "urganch Shahri"], d=2,
      x="Shahar nomi bosh harf bilan, “shahri” so‘zi esa kichik harf bilan yoziladi."),
    Q("To‘g‘ri yozilganini toping.", "Chirchiq daryosi", ["chirchiq daryosi", "Chirchiq Daryosi", "chirchiq Daryosi"], d=2,
      x="Daryo nomi bosh harf bilan, “daryosi” so‘zi esa kichik harf bilan yoziladi."),
    Q("To‘g‘ri yozilgan gapni toping.", "Ukamning ismi Jamshid.", ["ukamning ismi Jamshid.", "Ukamning ismi jamshid.",
                                                                   "Ukamning Ismi Jamshid."],
      x="Gapning birinchi so‘zi va ism bosh harf bilan yoziladi."),
    Q("To‘g‘ri yozilgan gapni toping.", "Biz Jizzaxga bordik.", ["biz Jizzaxga bordik.", "Biz jizzaxga bordik.",
                                                                 "Biz Jizzaxga Bordik."], d=2,
      x="Gap boshi va shahar nomi bosh harf bilan yoziladi."),
    Q("To‘g‘ri yozilgan gapni toping.", "Itimning nomi Olapar.", ["itimning nomi Olapar.", "Itimning nomi olapar.",
                                                                  "Itimning Nomi Olapar."], d=2,
      x="Gap boshi va itning nomi bosh harf bilan yoziladi."),
    Q("To‘g‘ri yozilgan gapni toping.", "Zarina Rahimova a’lo o‘qiydi.", ["Zarina rahimova a’lo o‘qiydi.",
                                                                          "zarina Rahimova a’lo o‘qiydi.",
                                                                          "Zarina Rahimova A’lo o‘qiydi."], d=3,
      x="Ism va familiya bosh harf bilan, qolgan so‘zlar kichik harf bilan yoziladi."),
    Q("Gapdagi qaysi so‘z bosh harf bilan yozilishi kerak?", "otabek", ["do‘stim", "futbol", "o‘ynaydi"],
      text="Mening do‘stim otabek futbol o‘ynaydi.", x="Otabek — bolaning ismi, u bosh harf bilan yoziladi."),
    Q("Gapdagi qaysi so‘z bosh harf bilan yozilishi kerak?", "qoradaryo", ["qishlog‘imiz", "yonidan", "oqadi"],
      text="Qishlog‘imiz yonidan qoradaryo oqadi.", d=2, x="Qoradaryo — daryo nomi, u bosh harf bilan yoziladi."),
    Q("Gapdagi qaysi so‘z bosh harf bilan yozilishi kerak?", "urganchda", ["Buvim", "yashaydi"],
      text="Buvim urganchda yashaydi.", d=2, x="Urganch — shahar nomi: Buvim Urganchda yashaydi."),
    TF("Familiya bosh harf bilan yoziladi.", True, x="Masalan: Karimov, Rahimova."),
    TF("Kishi ismini kichik harf bilan ham yozsa bo‘ladi.", False, x="Ism doim bosh harf bilan yoziladi: Dilshod."),
    TF("Hayvonga qo‘yilgan nom kichik harf bilan yoziladi.", False, d=2, x="Itning nomi Olapar — bosh harf bilan yoziladi."),
    TF("“Norin daryosi” birikmasida “daryosi” so‘zi kichik harf bilan yoziladi.", True, d=3,
       x="Faqat daryoning nomi — Norin — bosh harf bilan yoziladi."),
    MATCH("Nomni nima ekani bilan juftlang", [("Dilshod", "ism"), ("Karimov", "familiya"), ("Urganch", "shahar"), ("Norin", "daryo"),
                                              ("Olapar", "it"), ("O‘zbekiston", "mamlakat")], d=2,
          x="Bularning hammasi atoqli otlar — bosh harf bilan yoziladi."),
]
T.topic("proper_names", "🏙️", L("Ism va joy nomlari bosh harf bilan", "Capitalizing names", "Имена собственные с заглавной буквы"), C3,
        "Kishilarning ismi va familiyasi, shahar, qishloq va daryo nomlari bosh harf bilan yoziladi:\n"
        "Ali Karimov, Jizzax, Chirchiq.\n"
        "• Hayvonlarga qo‘yilgan nomlar ham bosh harf bilan yoziladi: Olapar.\n"
        "• “shahar”, “daryo” so‘zlari kichik harf bilan yoziladi: Urganch shahri, Norin daryosi.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["word_meaning", "who_what", "plural", "proper_names"], C3)

# ============================================================ 4-chorak
# ------------------------------------------------------------ belgini bildirgan so‘zlar
items = []
for right, wrong, d, why in [("qizil", ["qalam", "chizdi", "qiz"], 1, "qizil — rang: qanday qalam? qizil qalam."),
                             ("nordon", ["limon", "nok", "yedi"], 1, "nordon — ta’m: qanday limon? nordon limon."),
                             ("sovuq", ["muz", "qish", "muzladi"], 1, "sovuq — belgi: qanday muz? sovuq muz."),
                             ("aqlli", ["kitob", "o‘qidi", "maktab"], 1, "aqlli — belgi: qanday bola? aqlli bola."),
                             ("baland", ["tog‘", "chiqdi", "cho‘qqi"], 1, "baland — belgi: qanday tog‘? baland tog‘."),
                             ("dumaloq", ["to‘p", "dumaladi", "doira"], 2, "dumaloq — shakl: qanday to‘p? dumaloq to‘p.")]:
    items.append(Q("Qaysi so‘z belgini bildiradi?", right, wrong, d=d, x=why))
for text, right, d in [("Bog‘da sariq lolalar ochildi.", "sariq", 1), ("Ukam shirin qovun yedi.", "shirin", 1),
                       ("Dadam katta baliq tutdi.", "katta", 1), ("Osmonda oppoq bulutlar suzyapti.", "oppoq", 2),
                       ("Mehribon buvim ertak aytdi.", "Mehribon", 2)]:
    words = text.rstrip(".").split()
    assert right in words
    noun = words[words.index(right) + 1]
    items.append(Q("Gapdagi belgini bildirgan so‘zni toping.", right, [w for w in words if w != right], text=text, d=d,
                   x=f"Qanday {noun}? — {right.lower()}."))
for ask, noun, right, wrong, pic in [("qorga", "qor", "oppoq", ["qip-qizil", "issiq", "shirin"], "❄️"),
                                     ("limonga", "limon", "nordon", ["ko‘k", "issiq", "sho‘r"], "🍋"),
                                     ("asalga", "asal", "shirin", ["achchiq", "sho‘r", "nordon"], "🍯"),
                                     ("quyoshga", "quyosh", "issiq", ["sovuq", "ho‘l", "nordon"], "☀️"),
                                     ("jirafaning bo‘yniga", "bo‘yin", "uzun", ["kalta", "qisqa", "yumaloq"], "🦒"),
                                     ("filga", "fil", "ulkan", ["mitti", "kichkina", "yengil"], "🐘")]:
    items.append(Q(f"Qaysi belgi {ask} mos?", right, wrong, e=pic, x=f"Qanday {noun}? — {right} {noun}."))
items += [
    Q("Belgini bildirgan so‘zlar qaysi so‘roqqa javob beradi?", "qanday?", ["kim?", "nima?", "nima qildi?"],
      x="Belgini bildirgan so‘zlar qanday? qanaqa? so‘roqlariga javob beradi."),
    Q("Qaysi so‘z rangni bildiradi?", "yashil", ["yaxshi", "yengil", "yupqa"], d=2, x="yashil — rang: yashil barg."),
    Q("Qaysi so‘z ta’mni bildiradi?", "sho‘r", ["sariq", "silliq", "sovuq"], d=2, x="sho‘r — ta’m: tuz sho‘r bo‘ladi."),
    TF("“qattiq” so‘zi belgini bildiradi.", True, x="Qanday yong‘oq? — qattiq yong‘oq."),
    TF("“yugurdi” so‘zi belgini bildiradi.", False, x="yugurdi — harakat: nima qildi?"),
    TF("Belgini bildirgan so‘z “qanaqa?” so‘rog‘iga ham javob beradi.", True, d=2, x="Qanaqa ko‘ylak? — chiroyli ko‘ylak."),
    MATCH("Narsani belgisi bilan juftlang", [("qor", "oppoq"), ("asal", "shirin"), ("limon", "nordon"), ("fil", "ulkan"),
                                             ("chumoli", "mitti"), ("pomidor", "qizil")], d=2,
          x="Belgini bildirgan so‘z qanday? so‘rog‘iga javob beradi: qanday qor? — oppoq."),
]
T.topic("sign_words", "🎨", L("Belgini bildirgan so‘zlar", "Describing words", "Слова-признаки"), C4,
        "Belgini bildirgan so‘zlar qanday? qanaqa? so‘rog‘iga javob beradi. Ular narsaning:\n"
        "• rangini bildiradi: qizil, sariq, yashil;\n"
        "• ta’mini bildiradi: shirin, nordon, sho‘r;\n"
        "• kattaligi va shaklini bildiradi: katta, mitti, uzun, dumaloq.\n"
        "Misol: Qanday olma? — Shirin olma.", items=items)

# ------------------------------------------------------------ harakatni bildirgan so‘zlar
items = []
for right, wrong, d, why in [("sakradi", ["sariq", "sakkiz", "sabzi"], 1, "sakradi — harakat: nima qildi?"),
                             ("yuvdi", ["yuz", "yumshoq", "yulduz"], 1, "yuvdi — harakat: nima qildi?"),
                             ("chizyapti", ["chiziq", "chiroyli", "chiroq"], 1, "chizyapti — harakat: nima qilyapti?"),
                             ("uchdi", ["qush", "qanot", "osmon"], 1, "uchdi — harakat: nima qildi?"),
                             ("o‘ynaydi", ["o‘yinchoq", "o‘yin", "o‘ng"], 2, "o‘ynaydi — harakat: nima qiladi?")]:
    items.append(Q("Qaysi so‘z harakatni bildiradi?", right, wrong, d=d, x=why))
for text, right, ask, d in [("Opam gullarga suv quydi.", "quydi", "Opam nima qildi?", 1),
                            ("Kuchukcha hovlida yugurdi.", "yugurdi", "Kuchukcha nima qildi?", 1),
                            ("Bobom gazeta o‘qiyapti.", "o‘qiyapti", "Bobom nima qilyapti?", 1),
                            ("Biz bayramda qo‘shiq aytdik.", "aytdik", "Biz nima qildik?", 2)]:
    words = text.rstrip(".").split()
    items.append(Q("Gapdagi harakatni bildirgan so‘zni toping.", right, [w for w in words if w != right], text=text, d=d,
                   x=f"{ask} — {right}."))
items += [
    Q("“yozyapti” so‘zi qaysi so‘roqqa javob beradi?", "nima qilyapti?", ["nima qildi?", "nima qiladi?", "qanday?"], d=2,
      x="yozyapti — hozir bo‘layotgan harakat: nima qilyapti?"),
    Q("“chizdi” so‘zi qaysi so‘roqqa javob beradi?", "nima qildi?", ["nima qilyapti?", "nima qiladi?", "nima?"], d=2,
      x="chizdi — bo‘lib o‘tgan harakat: nima qildi?"),
    Q("“suzadi” so‘zi qaysi so‘roqqa javob beradi?", "nima qiladi?", ["nima qildi?", "nima qilyapti?", "qanday?"], d=3,
      x="suzadi — odatda bo‘ladigan harakat: baliq suvda suzadi."),
    Q("Hozir bo‘layotgan harakatni toping.", "o‘qiyapti", ["o‘qidi", "o‘qiydi", "o‘qish"], d=2,
      x="-yap- qo‘shimchasi hozir bo‘layotgan harakatni bildiradi: o‘qiyapti."),
    Q("Bo‘lib o‘tgan harakatni toping.", "keldi", ["kelyapti", "keladi", "kelaman"], d=2,
      x="keldi — harakat bo‘lib o‘tgan: nima qildi?"),
    Q("Novvoy nima qiladi?", "non yopadi", ["dars beradi", "mashina haydaydi", "davolaydi"], x="Novvoy non yopadi."),
    Q("Shifokor nima qiladi?", "davolaydi", ["non yopadi", "uy quradi", "soch oladi"], x="Shifokor kasallarni davolaydi."),
    Q("Gapni to‘ldiring: “Ari gulga …”", "qo‘ndi", ["suzdi", "yugurdi", "o‘qidi"], e="🐝", d=2, x="Ari gulga qo‘ndi."),
    Q("Gapni to‘ldiring: “Kecha men ertak …”", "o‘qidim", ["o‘qiyapman", "o‘qiyman", "o‘qiydi"], d=3,
      x="“Kecha” — o‘tgan vaqt, “men” — o‘zim: Kecha men ertak o‘qidim."),
    Q("Gapni to‘ldiring: “Ertaga biz bog‘ga …”", "boramiz", ["bordik", "bording", "bordi"], d=3,
      x="“Ertaga” — keyingi kun, “biz” — ko‘pchilik: Ertaga biz bog‘ga boramiz."),
    TF("“yozdi” so‘zi harakatni bildiradi.", True, x="Nima qildi? — yozdi."),
    TF("“qalam” so‘zi harakatni bildiradi.", False, x="qalam — narsa: nima?"),
    TF("“keldi” so‘zi “nima qilyapti?” so‘rog‘iga javob beradi.", False, d=2, x="keldi — bo‘lib o‘tgan harakat: nima qildi?"),
    MATCH("Kasb egasini uning ishi bilan juftlang", [("novvoy", "non yopadi"), ("shifokor", "davolaydi"), ("oshpaz", "ovqat pishiradi"),
                                                     ("o‘qituvchi", "dars beradi"), ("sartarosh", "soch oladi"),
                                                     ("quruvchi", "uy quradi")], d=2,
          x="Ishni bildirgan so‘zlar harakatni bildiradi: nima qiladi?"),
]
T.topic("action_words", "🏃", L("Harakatni bildirgan so‘zlar", "Action words", "Слова-действия"), C4,
        "Harakatni bildirgan so‘zlar nima qildi? nima qilyapti? nima qiladi? so‘roqlariga javob beradi.\n"
        "• nima qildi? — bo‘lib o‘tgan harakat: yozdi, o‘qidi.\n"
        "• nima qilyapti? — hozir bo‘layotgan harakat: yozyapti, o‘qiyapti.\n"
        "• nima qiladi? — odatda yoki keyin bo‘ladigan harakat: yozadi, o‘qiydi.", items=items)

# ------------------------------------------------------------ gap turlari
KINDS = ["Darak gap", "So‘roq gap", "Undov gap"]
KIND_WHY = {"Darak gap": "Bu gap xabar beradi, oxirida nuqta — darak gap.",
            "So‘roq gap": "Bu gapda savol bor, oxirida so‘roq belgisi — so‘roq gap.",
            "Undov gap": "Bu gap kuchli his bilan aytiladi, oxirida undov belgisi — undov gap."}
END = {"Darak gap": ".", "So‘roq gap": "?", "Undov gap": "!"}
SENT2 = [("Akam maktabdan qaytdi.", "Darak gap", 1), ("Kuzda barglar sarg‘ayadi.", "Darak gap", 1),
         ("Mening mushugim oppoq.", "Darak gap", 2), ("Daraxtda qushcha sayrayapti.", "Darak gap", 2),
         ("Sen qaysi sinfda o‘qiysan?", "So‘roq gap", 1), ("Qalaming bormi?", "So‘roq gap", 1),
         ("Kim derazani ochdi?", "So‘roq gap", 2), ("Mushuk qayerga yashirindi?", "So‘roq gap", 2),
         ("Voy, qanday katta tarvuz!", "Undov gap", 1), ("Ura, ta’til boshlandi!", "Undov gap", 1),
         ("Qanday shirin olma!", "Undov gap", 2), ("Barakalla, juda yaxshi chizibsan!", "Undov gap", 2)]
items = []
for s, kind, d in SENT2:
    assert s.endswith(END[kind])
    items.append(Q(f"“{s}” Bu qanday gap?", kind, [k for k in KINDS if k != kind], d=d, x=KIND_WHY[kind]))
MARK_WHY = {".": "xabar beradigan gap oxiriga nuqta qo‘yiladi.", "?": "savol beradigan gap oxiriga so‘roq belgisi qo‘yiladi.",
            "!": "kuchli his bilan aytilgan gap oxiriga undov belgisi qo‘yiladi."}
for s, mark, d in [("Bugun yomg‘ir yog‘di", ".", 1), ("Bizning sinfimizda o‘ttiz bola bor", ".", 2),
                   ("Ertaga qayerga borasan", "?", 1), ("Sening qalaming qani", "?", 2),
                   ("Voy, qanday chiroyli kapalak", "!", 1), ("Oh, qanday mazali palov", "!", 2)]:
    items.append(Q(f"“{s}” Bu gap oxiriga qaysi belgi qo‘yiladi?", mark, [m for m in (".", "?", "!") if m != mark], d=d,
                   x=f"{s}{mark} — {MARK_WHY[mark]}"))
items += [
    Q("Qaysi gap savol bildiradi?", "Sen qachon uxlaysan", ["Men erta uxlayman", "Ukam uxlab qoldi", "Mushuk divanda uxlayapti"], d=2,
      x="“qachon” — so‘roq so‘zi. To‘g‘ri yozilishi: Sen qachon uxlaysan?"),
    Q("Qaysi so‘z so‘roq so‘zi?", "qayerda", ["uyda", "bog‘da", "maktabda"], x="qayerda, kim, nima, qachon — so‘roq so‘zlari."),
    Q("Qaysi so‘z so‘roq so‘zi?", "qachon", ["bugun", "kecha", "ertaga"], d=2, x="qachon — so‘roq so‘zi: Sen qachon kelasan?"),
    Q("Qaysi gap to‘g‘ri yozilgan?", "Bugun havo juda sovuq.", ["Bugun havo juda sovuq?", "bugun havo juda sovuq.",
                                                                "Bugunhavo juda sovuq."],
      x="Gap bosh harf bilan boshlanadi, so‘zlar alohida yoziladi, oxirida nuqta qo‘yiladi."),
    Q("Qaysi gap to‘g‘ri yozilgan?", "Sen qayerda yashaysan?", ["Sen qayerda yashaysan.", "sen qayerda yashaysan?",
                                                                "Sen qayerda yashaysan!"], d=2,
      x="So‘roq gap bosh harf bilan boshlanib, so‘roq belgisi bilan tugaydi."),
    Q("Qaysi gap to‘g‘ri yozilgan?", "Ura, biz g‘olib bo‘ldik!", ["Ura, biz g‘olib bo‘ldik?", "ura, biz g‘olib bo‘ldik!",
                                                                  "Ura, biz g‘olib bo‘ldik"], d=2,
      x="Undov gap bosh harf bilan boshlanib, undov belgisi bilan tugaydi."),
    Q("Qaysi gap to‘g‘ri yozilgan?", "Kuzda qushlar uchib ketadi.", ["kuzda qushlar uchib ketadi.", "Kuzda qushlar uchib ketadi?",
                                                                     "Kuzda qushlar uchibketadi."], d=2,
      x="Gap bosh harf bilan boshlanadi, so‘zlar alohida yoziladi, oxirida nuqta qo‘yiladi."),
    TF("Undov gap oxiriga undov belgisi qo‘yiladi.", True, x="Masalan: Qanday shirin olma!"),
    TF("“Kim derazani ochdi?” — darak gap.", False, x="Bu gapda savol bor — so‘roq gap."),
    TF("Darak gap oxiriga so‘roq belgisi qo‘yiladi.", False, x="Darak gap oxiriga nuqta qo‘yiladi: Akam maktabdan qaytdi."),
]
T.topic("sentence_types", "💬", L("Gap turlari va gap oxiridagi belgilar", "Types of sentences and end marks",
                                  "Виды предложений и знаки в конце"), C4,
        "Gap tugal fikr bildiradi va bosh harf bilan boshlanadi.\n"
        "• Darak gap xabar beradi, oxirida nuqta (.): Akam maktabdan qaytdi.\n"
        "• So‘roq gap savol bildiradi, oxirida so‘roq belgisi (?): Sen qaysi sinfda o‘qiysan?\n"
        "• Undov gap kuchli his bilan aytiladi, oxirida undov belgisi (!): Voy, qanday katta tarvuz!", items=items)

# ------------------------------------------------------------ so‘zlardan gap tuzish
items = []
for s, d, pic in [("Qushlar janubga uchdi", 1, "🐦"), ("Mushugim sut ichdi", 1, "🐱"), ("Bolalar archa bezashdi", 1, "🎄"),
                  ("Dadam daraxt o‘tqazdi", 1, "🌳"), ("Opam xonani yig‘ishtirdi", 1, None), ("Toshbaqa sekin yuradi", 1, "🐢"),
                  ("Qishda ko‘l muzlaydi", 1, "❄️"), ("Quyosh charaqlab turibdi", 1, "☀️"),
                  ("Ukam yangi to‘p oldi", 2, "⚽"), ("Dadam mazali shashlik pishirdi", 2, None),
                  ("Mening singlim qo‘g‘irchoq o‘ynadi", 2, None), ("Kichkina jo‘jalar don cho‘qiyapti", 2, "🐤"),
                  ("Hovlimizda katta chinor bor", 2, None), ("Quyoncha shirin sabzi kemiryapti", 2, "🐰"),
                  ("Mening akam futbolni yaxshi ko‘radi", 3, None), ("Mening opam shifokor bo‘lib ishlaydi", 3, None),
                  ("Aqlli qizcha savolga javob berdi", 3, None)]:
    assert 3 <= len(s.split()) <= 5, s
    items.append(ORDER("So‘zlardan gap tuzing", s, d=d, e=pic, x=f"{s}."))
items += [
    ORDER("So‘zlardan gap tuzing", "Sigirlar yaylovda o‘tlayapti", extra=["o‘tlayapman"], e="🐮", d=3,
          x="Sigirlar yaylovda o‘tlayapti. (sigirlar … o‘tlayapti)"),
    ORDER("So‘zlardan gap tuzing", "Qo‘zichoq maysa yeyapti", extra=["yeyapman"], e="🐑", d=3,
          x="Qo‘zichoq maysa yeyapti. (qo‘zichoq … yeyapti)"),
    Q("Qaysi qatorda gap bor?", "Ukam rasm chizdi.", ["ukam va rasm", "chiroyli rasm", "rasm uchun"],
      x="Gap tugal fikr bildiradi: kim? — ukam, nima qildi? — chizdi."),
    Q("Gapni to‘ldiring: “Men har kuni ertalab badantarbiya …”", "qilaman", ["qildi", "qilyapsan", "qilishdi"], d=2,
      x="“Men” so‘ziga “qilaman” mos keladi: Men har kuni ertalab badantarbiya qilaman."),
    Q("Gapni to‘ldiring: “Biz kecha kinoga …”", "bordik", ["boramiz", "bordim", "bordi"], d=2,
      x="“Biz” va “kecha” so‘zlariga “bordik” mos keladi."),
    Q("Gapni to‘ldiring: “Sen qachon …?”", "kelding", ["keldim", "keldi", "keldik"], d=2,
      x="“Sen” so‘ziga “kelding” mos keladi: Sen qachon kelding?"),
    TF("“Mushugim sut ichdi.” gapida harakatni bildirgan so‘z — “ichdi”.", True, x="Mushugim nima qildi? — ichdi."),
    TF("“Qishda ko‘l muzlaydi.” gapida 4 ta so‘z bor.", False, x="Qishda | ko‘l | muzlaydi — 3 ta so‘z."),
]
T.topic("build_sentence", "🧩", L("So‘zlardan gap tuzish", "Building sentences", "Составление предложений"), C4,
        "Gap tuzish uchun so‘zlarni ma’nosiga qarab tartib bilan qo‘yamiz.\n"
        "• Avval kim? yoki nima? haqida gap borishini aytamiz: Ukam …\n"
        "• Harakatni bildirgan so‘z ko‘pincha gap oxirida keladi: Ukam yangi to‘p oldi.\n"
        "• Belgini bildirgan so‘z narsa nomidan oldin turadi: yangi to‘p, shirin sabzi.\n"
        "• Gapni bosh harf bilan boshlab, oxiriga belgi qo‘yamiz.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["sign_words", "action_words", "sentence_types", "build_sentence"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["alphabet_order", "sounds", "voiced", "syllables", "og_tutuq", "double_cons", "word_meaning", "who_what", "plural",
        "proper_names", "sign_words", "action_words", "sentence_types", "build_sentence"], C4, level=3)


# ------------------------------------------------------------ qo‘shimcha tekshiruv (imlo belgilari, kirill harflari)
def _strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _strings(v)


_BAD = [(re.compile(r"[oOgG][’'`ʻʼ]"), "o/g dan keyin ‘ (U+2018) bo‘lishi kerak"),
        (re.compile(r"(?<![oOgG\s])‘"), "‘ faqat o/g dan keyin keladi"),
        (re.compile(r"[Ѐ-ӿ]"), "kirill harfi"),
        (re.compile(r"[{}]"), "{ } belgilari")]
_problems = []
for _t in T.topics:
    for _s in _strings({"t": _t.get("theory", ""), "c": _t["chapter"], "u": _t["title"]["uz"]}):
        for _rx, _msg in _BAD:
            if _rx.search(_s):
                _problems.append(f"{_t['id']}: {_msg}: {_s}")
for _it in T.items:
    for _s in _strings({k: v for k, v in _it.items() if k not in ("topic", "id")}):
        for _rx, _msg in _BAD:
            if _rx.search(_s):
                _problems.append(f"{_it['id']}: {_msg}: {_s}")
    if _it["t"] == "choice":
        assert 2 <= len(_it["w"]) <= 4, _it
if _problems:
    raise SystemExit("\n".join(_problems))

T.write()
