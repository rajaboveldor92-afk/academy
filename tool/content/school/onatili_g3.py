"""Ona tili, 3-sinf: tovush va harf, bo‘g‘in, so‘z ma’nosi, so‘z tarkibi, so‘z turkumlari, gap.

Mavzular 3-sinf ona tili dasturi tartibida; matnlar va misollar o‘zimizniki. So‘z ro‘yxatlaridan savollar
dastur bilan yaratiladi (javob hisoblab topiladi), qoidalar qo‘lda yozilgan.
Qayta yaratish: python3 tool/content/school/onatili_g3.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from uzlang import *  # noqa: E402,F401,F403

rnd = random.Random(3)
T = Course("onatili", 3, L("Ona tili", "Native language", "Родной язык"))

C1 = "1-chorak. Tovush, harf va bo‘g‘in"
C2 = "2-chorak. So‘z va uning ma’nosi"
C3 = "3-chorak. So‘z turkumlari"
C4 = "4-chorak. Gap va tinish belgilari"

# ============================================================ 1-chorak
items = []
for w in ["kitob", "daftar", "maktab", "qalam", "olma", "bola", "deraza", "kapalak", "chumoli", "shaftoli",
          "o‘qituvchi", "qo‘g‘irchoq", "tarvuz", "quyosh", "yulduz"]:
    n = vowel_count(w)
    items.append(Q(f"“{w}” so‘zida nechta unli tovush bor?", f"{n} ta", [f"{k} ta" for k in (n - 1, n + 1, n + 2) if k > 0],
                   d=1 if len(w) <= 6 else 2, x=f"{w}: {', '.join(vowels_of(w))} — {n} ta unli."))
vowel_letters = ["a", "o", "u", "e", "i", "o‘"]
cons_letters = ["b", "d", "k", "m", "s", "t", "r", "l", "n", "q", "sh", "ch", "g‘", "x", "z"]
for v in vowel_letters:
    items.append(Q("Qaysi harf unli tovushni bildiradi?", v, rnd.sample(cons_letters, 4),
                   x=f"O‘zbek tilida 6 ta unli bor: a, o, u, e, i, o‘. “{v}” — unli."))
for c in ["b", "sh", "q", "ch"]:
    items.append(Q("Qaysi harf undosh tovushni bildiradi?", c, rnd.sample(vowel_letters, 4), d=1,
                   x=f"“{c}” — undosh tovush. Unlilar: a, o, u, e, i, o‘."))
items += [
    TF("O‘zbek tilida 6 ta unli tovush bor.", True, x="Unlilar: a, o, u, e, i, o‘."),
    TF("“sh” harf birikmasi bitta tovushni bildiradi.", True, x="sh, ch, ng — ikki belgi bilan yoziladigan bitta tovush."),
    TF("Unli tovush aytilganda havo to‘siqqa uchramaydi.", True, d=2, x="Unlini cho‘zib aytish mumkin: a-a-a."),
    TF("“o‘” — undosh tovush.", False, x="“o‘” — unli tovush."),
    TF("Har bir bo‘g‘inda bitta unli bo‘ladi.", True, d=2, x="Shuning uchun so‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bo‘ladi."),
    MATCH("Harfni shu harf bilan boshlanadigan so‘z bilan juftlang",
          [("o‘", "o‘rik"), ("sh", "shamol"), ("ch", "choy"), ("g‘", "g‘oz"), ("q", "qovun"), ("x", "xona")], d=2),
]
T.topic("sounds", "🔤", L("Unli va undosh tovushlar", "Vowels and consonants", "Гласные и согласные звуки"), C1,
        "Tovushni eshitamiz va aytamiz, harfni ko‘ramiz va yozamiz.\n"
        "• Unli tovushlar (6 ta): a, o, u, e, i, o‘. Ular cho‘zib aytiladi, havo to‘siqsiz chiqadi.\n"
        "• Qolgan tovushlar — undoshlar: b, d, k, m, q, s, t …\n"
        "• sh, ch, ng — ikki belgi bilan yoziladigan bitta tovush: shamol, choy, tong.\n"
        "Misol: “olma” so‘zida o, a — 2 ta unli; l, m — 2 ta undosh.", items=items)

items = []
for w, syl in SYLLABLES.items():
    n = len(syl)
    items.append(Q(f"“{w}” so‘zida nechta bo‘g‘in bor?", f"{n} ta", [f"{k} ta" for k in (n - 1, n + 1, n + 2) if k > 0],
                   d=1 if n <= 2 else 2, x=f"{'-'.join(syl)} — {n} ta bo‘g‘in (unlilar soni ham {n} ta)."))
for w, syl in list(SYLLABLES.items()):
    if len(syl) < 2:
        continue
    right = "-".join(syl)
    wrong = sorted(set(wrong_splits(syl)) - {right})
    if len(wrong) >= 2:
        items.append(Q(f"“{w}” so‘zi bo‘g‘inlarga qaysi qatorda to‘g‘ri ajratilgan?", right, wrong[:4], d=2 if len(syl) == 2 else 3,
                       x=f"Har bir bo‘g‘inda bitta unli: {right}."))
items += [
    TF("“kitob” so‘zida 2 ta bo‘g‘in bor.", True, x="ki-tob: 2 ta unli — 2 ta bo‘g‘in."),
    TF("Bo‘g‘in unlisiz ham bo‘ladi.", False, x="Har bir bo‘g‘inda albatta bitta unli bo‘ladi."),
    TF("Bitta harfdan iborat bo‘g‘in qator oxirida qoldirilmaydi va yangi qatorga ko‘chirilmaydi.", True, d=3,
       x="Masalan, “o-na” so‘zini “o-” qoldirib ko‘chirib bo‘lmaydi."),
]
T.topic("syllables", "✂️", L("Bo‘g‘in va so‘zni ko‘chirish", "Syllables and hyphenation", "Слог и перенос слов"), C1,
        "So‘z bo‘g‘inlarga bo‘linadi. Har bir bo‘g‘inda bitta unli bo‘ladi: ki-tob, maк-tab.\n"
        "So‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bor: o-na (2), chu-mo-li (3).\n"
        "• So‘z qatordan qatorga bo‘g‘in bo‘yicha ko‘chiriladi: mak-tab.\n"
        "• Bitta harfli bo‘g‘in qatorda qoldirilmaydi va ko‘chirilmaydi: o-na so‘zini bo‘lib bo‘lmaydi.".replace("maк", "mak"),
        items=items)

items = []
alpha_words = ["anor", "bodring", "daryo", "echki", "futbol", "gilos", "havo", "ilon", "jo‘ja", "kitob", "lola", "mushuk",
               "non", "olma", "paxta", "qovun", "ruchka", "sabzi", "tulki", "uzum", "vaqt", "xona", "yulduz", "zanjir",
               "o‘rik", "g‘oz", "shamol", "choy"]
simple_words = [w for w in alpha_words if not w.startswith(("o‘", "g‘", "sh", "ch"))]
hard_words = [w for w in alpha_words if w not in simple_words]
seen_groups = set()
while len(seen_groups) < 17:
    k = len(seen_groups)
    group = rnd.sample(simple_words, 4) if k < 12 else rnd.sample(simple_words, 3) + [hard_words[k % len(hard_words)]]
    rnd.shuffle(group)
    if tuple(sorted(group)) in seen_groups:
        continue
    seen_groups.add(tuple(sorted(group)))
    first = min(group, key=alpha_key)
    items.append(Q(f"Qaysi so‘z alifbo tartibida birinchi keladi: {', '.join(group)}?", first, [w for w in group if w != first],
                   d=1 if k < 8 else (2 if k < 12 else 3), x=f"Birinchi harflarni alifbo bo‘yicha solishtiramiz: {first}."))
items += [
    Q("O‘zbek lotin alifbosi qaysi harf bilan boshlanadi?", "A", ["B", "O", "Z"], x="Alifbo A harfi bilan boshlanadi."),
    Q("Alifboda “B” harfidan keyin qaysi harf keladi?", "D", ["C", "V", "E"], x="O‘zbek alifbosida C harfi yo‘q: A, B, D, E …"),
    Q("Qaysi harf alifboning oxirgi harflaridan biri?", "Ng", ["A", "K", "M"], d=2, x="Alifbo oxirida: O‘, G‘, Sh, Ch, Ng."),
    Q("O‘zbek lotin alifbosida nechta harf bor?", "29 ta", ["26 ta", "33 ta", "24 ta"], d=2,
      x="26 ta harf va 3 ta harf birikmasi (sh, ch, ng) bilan jami 29 ta."),
    TF("O‘zbek lotin alifbosida “C” harfi yo‘q.", True, d=2, x="“ch” harf birikmasi bor, lekin alohida C harfi yo‘q."),
    ORDER("Harflarni alifbo tartibida joylashtiring", "A B D E", d=1, x="A, B, D, E — alifbo boshi."),
    ORDER("Harflarni alifbo tartibida joylashtiring", "K L M N", d=1, x="K, L, M, N."),
]
T.topic("alphabet", "🔠", L("Alifbo tartibi", "Alphabetical order", "Алфавитный порядок"), C1,
        "O‘zbek lotin alifbosi: A B D E F G H I J K L M N O P Q R S T U V X Y Z O‘ G‘ Sh Ch Ng.\n"
        "• Lug‘atlarda va ro‘yxatlarda so‘zlar alifbo tartibida yoziladi.\n"
        "• Birinchi harflar bir xil bo‘lsa, ikkinchi harf solishtiriladi: bola, bosh, bug‘doy.\n"
        "• O‘, G‘, Sh, Ch alifbo oxirida turadi: “shamol” so‘zi “tulki”dan keyin keladi.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["sounds", "syllables", "alphabet"], C1)

# ============================================================ 2-chorak
items = []
for a, b, wrong in SYNONYMS_Q:
    items.append(Q(f"“{a}” so‘zining ma’nodoshini (sinonimini) toping.", b, wrong,
                   d=1 if len(items) < 12 else 2, x=f"“{a}” va “{b}” — ma’nodosh so‘zlar."))
items += [
    TF("“chiroyli” va “go‘zal” — ma’nodosh so‘zlar.", True, x="Ikkalasi bir xil ma’noni bildiradi."),
    TF("“katta” va “kichik” — ma’nodosh so‘zlar.", False, x="Ular zid ma’noli so‘zlar."),
    MATCH("Ma’nodosh so‘zlarni juftlang", SYNONYMS[:8], d=2),
]
T.topic("synonyms", "🤝", L("Ma’nodosh so‘zlar", "Synonyms", "Синонимы"), C2,
        "Ma’nodosh (sinonim) so‘zlar — yozilishi har xil, ma’nosi bir xil yoki yaqin so‘zlar.\n"
        "Misollar: chiroyli — go‘zal, aqlli — dono, botir — jasur, xursand — shod.\n"
        "Ma’nodosh so‘zlar nutqni boy qiladi, bir so‘zni takrorlamaslikka yordam beradi.", items=items)

items = []
for a, b, wrong in ANTONYMS_Q:
    items.append(Q(f"“{a}” so‘zining zid ma’nolisini (antonimini) toping.", b, wrong,
                   d=1 if len(items) < 14 else 2, x=f"“{a}” — “{b}”: zid ma’noli so‘zlar."))
items += [
    TF("“issiq” va “sovuq” — zid ma’noli so‘zlar.", True, x="Ular qarama-qarshi ma’noni bildiradi."),
    TF("“dono” va “aqlli” — zid ma’noli so‘zlar.", False, x="Ular ma’nodosh so‘zlar."),
    MATCH("Zid ma’noli so‘zlarni juftlang", ANTONYMS[:8], d=2),
    Q("Maqolni to‘ldiring: “Yaxshi so‘z — jon ozig‘i, … so‘z — bosh qozig‘i.”", "yomon", ["shirin", "chiroyli", "katta"], d=3,
      x="Yaxshi — yomon: maqolda zid ma’noli so‘zlar ishlatilgan."),
]
T.topic("antonyms", "↔️", L("Zid ma’noli so‘zlar", "Antonyms", "Антонимы"), C2,
        "Zid ma’noli (antonim) so‘zlar qarama-qarshi ma’noni bildiradi.\n"
        "Misollar: katta — kichik, issiq — sovuq, kun — tun, kulmoq — yig‘lamoq.\n"
        "Maqol va she’rlarda zid ma’noli so‘zlar fikrni ta’sirli qiladi.", items=items)

items = []
all_roots = [parts[0] for _, parts in ROOTS_G3]
for word, parts in ROOTS_G3:
    root = parts[0]
    wrong = [word, "-" + parts[1]]
    if len(parts) > 2:
        wrong.append(root + parts[1])
    else:
        wrong.append(rnd.choice([r for r in all_roots if r != root and r not in word]))
    items.append(Q(f"“{word}” so‘zining o‘zagini toping.", root, wrong, d=1 if len(parts) == 2 else 2,
                   x=f"{word} = {' + '.join(parts)}. O‘zak — so‘zning asosiy ma’noli qismi."))
for word, parts in ROOTS_G3:
    if len(parts) != 2:
        continue
    suf = parts[1]
    items.append(Q(f"“{word}” so‘ziga qaysi qo‘shimcha qo‘shilgan?", f"-{suf}",
                   [f"-{x}" for x in ("lar", "im", "ga", "ni", "da", "chi", "li") if x != suf][:4], d=2,
                   x=f"{parts[0]} + {suf} = {word}."))
items += [
    TF("O‘zak — so‘zning asosiy ma’noli qismi.", True, x="Qo‘shimchalar o‘zakka qo‘shiladi."),
    TF("“-lar” qo‘shimchasi ko‘plikni bildiradi.", True, x="kitob — kitoblar, bola — bolalar."),
    TF("Qo‘shimcha so‘zning boshiga qo‘shiladi.", False, x="O‘zbek tilida qo‘shimchalar o‘zakdan keyin qo‘shiladi."),
]
T.topic("word_parts", "🧱", L("So‘z tarkibi: o‘zak va qo‘shimcha", "Root and suffix", "Корень и суффикс"), C2,
        "So‘z o‘zak va qo‘shimchadan tuzilishi mumkin.\n"
        "• O‘zak — so‘zning asosiy ma’noli qismi: kitob, gul, bola.\n"
        "• Qo‘shimcha o‘zakdan keyin qo‘shiladi: kitob+lar, gul+chi, bola+ga.\n"
        "Misol: daftarlarim = daftar (o‘zak) + lar + im.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["synonyms", "antonyms", "word_parts"], C2)

# ============================================================ 3-chorak
items = []
for cls, words in WORD_CLASSES_G3.items():
    for w in words:
        items.append(Q(f"“{w}” so‘zi qaysi so‘z turkumiga kiradi?", cls, [c for c in WORD_CLASSES_G3 if c != cls],
                       d=1, x=f"“{w}” {CLASS_QUESTION[cls]} degan so‘roqqa javob beradi — {cls.lower()}."))
for cls in WORD_CLASSES_G3:
    for right in rnd.sample(WORD_CLASSES_G3[cls], 3):
        wrong = [rnd.choice(WORD_CLASSES_G3[c]) for c in WORD_CLASSES_G3 if c != cls]
        items.append(Q(f"Qaysi so‘z {cls.lower()}?", right, wrong, d=2, x=f"“{right}” — {cls.lower()}: {CLASS_QUESTION[cls]}"))
items += [MATCH("So‘z turkumini so‘rog‘i bilan juftlang", [(c, CLASS_QUESTION[c]) for c in WORD_CLASSES_G3], d=2)]
T.topic("word_classes", "🗂️", L("So‘z turkumlari", "Parts of speech", "Части речи"), C3,
        "So‘zlar ma’nosi va so‘rog‘iga qarab turkumlarga bo‘linadi:\n"
        "• Ot — kim? nima? qayer?: bola, kitob, maktab.\n"
        "• Sifat — qanday? qanaqa?: katta, qizil, chiroyli.\n"
        "• Son — nechta? qancha? nechanchi?: uch, o‘n, beshinchi.\n"
        "• Fe’l — nima qildi? nima qilyapti?: o‘qidi, yozyapti, yugurdi.", items=items)

items = []
for p in PROPER_NOUNS:
    commons = rnd.sample(COMMON_NOUNS, 3)
    items.append(Q("Qaysi so‘z bosh harf bilan yozilishi kerak?", p.lower(), commons, d=1 if len(items) < 14 else 2,
                   x=f"{p} — atoqli ot, u bosh harf bilan yoziladi."))
for p in PROPER_NOUNS[:8]:
    items.append(Q(f"“{p}” qanday ot?", "Atoqli ot", ["Turdosh ot", "Sifat", "Fe’l"], d=1,
                   x=f"{p} — yakka nom (ism yoki joy nomi), shuning uchun atoqli ot."))
for c in COMMON_NOUNS[:6]:
    items.append(Q(f"“{c}” qanday ot?", "Turdosh ot", ["Atoqli ot", "Sifat", "Son"], d=2,
                   x=f"“{c}” — bir turdagi narsalarning umumiy nomi, turdosh ot."))
items += [
    TF("Kishi ismlari bosh harf bilan yoziladi.", True, x="Anvar, Dilnoza, Sardor."),
    TF("“daryo” so‘zi bosh harf bilan yoziladi.", False, x="daryo — turdosh ot. Daryo nomi esa (Amudaryo) bosh harf bilan yoziladi."),
    TF("Shahar nomlari bosh harf bilan yoziladi.", True, x="Toshkent, Samarqand, Buxoro."),
]
T.topic("proper_nouns", "🏙️", L("Atoqli va turdosh otlar", "Proper and common nouns", "Собственные и нарицательные"), C3,
        "Ot kim? nima? qayer? so‘roqlariga javob beradi.\n"
        "• Turdosh ot — bir xil narsalarning umumiy nomi: shahar, daryo, qiz, kitob.\n"
        "• Atoqli ot — yakka nom: kishi ismi, shahar, daryo, mamlakat nomi. U bosh harf bilan yoziladi:\n"
        "  Dilnoza, Toshkent, Amudaryo, O‘zbekiston.", items=items)

items = []
for word in PLURAL_WORDS:
    items.append(Q(f"“{word}” so‘zining ko‘plik shaklini toping.", word + "lar", [word + "ler", word + "la", word], d=1,
                   x=f"{word} + lar = {word}lar. Ko‘plik -lar qo‘shimchasi bilan yasaladi."))
for base, forms in POSSESSIVE_G3:
    for person, suffix_word in zip(["men", "sen", "u"], forms):
        wrong = possessive_wrong(base, suffix_word)
        items.append(Q(f"“{base}” so‘ziga egalik qo‘shimchasini qo‘shing: {GENITIVE[person]} …", suffix_word, wrong,
                       d=1 if person == "men" else 2, x=f"{GENITIVE[person]} {suffix_word}."))
items += [
    TF("“-lar” qo‘shimchasi so‘zga ko‘plik ma’nosini beradi.", True, x="gul — gullar, uy — uylar."),
    TF("“kitobim” so‘zida “-im” egalik qo‘shimchasi.", True, x="kitob + im: mening kitobim."),
]
T.topic("noun_forms", "📚", L("Otning birlik va ko‘plik, egalik shakllari", "Plural and possessive forms", "Число и принадлежность"), C3,
        "• Ko‘plik -lar qo‘shimchasi bilan: daftar — daftarlar, olma — olmalar.\n"
        "• Egalik qo‘shimchalari narsa kimga tegishli ekanini bildiradi:\n"
        "  unli bilan tugagan so‘zga: ona-m, ona-ng, ona-si;\n"
        "  undosh bilan tugagan so‘zga: kitob-im, kitob-ing, kitob-i.", items=items)

items = []
for adj, noun in ADJ_NOUN:
    items.append(Q(f"“{adj} {noun}” birikmasida “{adj}” so‘zi qaysi so‘z turkumi?", "Sifat", ["Ot", "Fe’l", "Son"], d=1,
                   x=f"“{adj}” — {noun} qanday? degan so‘roqqa javob beradi, u sifat."))
for verb in VERBS_G3[:10]:
    items.append(Q("Qaysi so‘z “nima qildi?” so‘rog‘iga javob beradi?", verb,
                   [rnd.choice([a for a, _ in ADJ_NOUN]), rnd.choice(WORD_CLASSES_G3["Ot"]), rnd.choice(WORD_CLASSES_G3["Son"])],
                   d=1, x=f"“{verb}” — harakatni bildiradi, u fe’l."))
items += [
    TF("Sifat narsaning belgisini bildiradi.", True, x="rang, hajm, ta’m, xususiyat: qizil, katta, shirin, aqlli."),
    TF("Fe’l harakatni bildiradi.", True, x="yozdi, o‘qiyapti, yuguradi."),
    TF("“yashil” so‘zi — fe’l.", False, x="“yashil” — rang, belgi: sifat."),
]
T.topic("adj_verb", "🎨", L("Sifat va fe’l", "Adjectives and verbs", "Прилагательное и глагол"), C3,
        "• Sifat — narsaning belgisini bildiradi va qanday? qanaqa? so‘rog‘iga javob beradi:\n"
        "  qizil olma, katta uy, shirin qovun, aqlli bola.\n"
        "• Fe’l — harakatni bildiradi va nima qildi? nima qilyapti? nima qiladi? so‘roqlariga javob beradi:\n"
        "  o‘qidi, yozyapti, yuguradi.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["word_classes", "proper_nouns", "noun_forms", "adj_verb"], C3)

# ============================================================ 4-chorak
items = []
for sent, kind in SENTENCE_TYPES_G3:
    items.append(Q(f"“{sent}” — maqsadiga ko‘ra qanday gap?", kind, [k for k in ("Darak gap", "So‘roq gap", "Buyruq gap") if k != kind],
                   d=1 if len(items) < 12 else 2, x=f"{SENT_EXPLAIN[kind]}"))
items += [
    TF("So‘roq gap oxiriga so‘roq belgisi qo‘yiladi.", True, x="Masalan: Sen qayerga ketyapsan?"),
    TF("Darak gap biror narsa haqida xabar beradi.", True, x="Masalan: Bugun havo iliq."),
    TF("Buyruq gapda savol so‘raladi.", False, x="Buyruq gapda buyruq yoki iltimos bildiriladi: Eshikni yoping."),
]
T.topic("sentence_types", "💬", L("Gap turlari", "Types of sentences", "Виды предложений"), C4,
        "Gap — tugal fikr bildiradigan so‘z yoki so‘zlar.\n"
        "Maqsadiga ko‘ra gaplar:\n"
        "• Darak gap — xabar beradi: Bugun havo iliq. (oxirida nuqta)\n"
        "• So‘roq gap — savol bildiradi: Sen qayerga ketyapsan? (oxirida so‘roq belgisi)\n"
        "• Buyruq gap — buyruq, iltimos bildiradi: Eshikni yoping. (nuqta yoki undov belgisi)\n"
        "Kuchli his bilan aytilgan gap oxiriga undov belgisi qo‘yiladi: Qanday chiroyli!", items=items)

items = []
for sent, mark in PUNCT_G3:
    items.append(Q(f"Gap oxiriga qaysi belgi qo‘yiladi: “{sent}…”", mark, [m for m in (".", "?", "!", ",") if m != mark],
                   d=1 if len(items) < 12 else 2, x=f"{sent}{mark} — {PUNCT_EXPLAIN[mark]}"))
items += [
    Q("Qaysi gap to‘g‘ri yozilgan?", "Bugun biz bog‘ga bordik.", ["bugun biz bog‘ga bordik.", "Bugun biz bog‘ga bordik", "bugun biz bog‘ga bordik"],
      x="Gap bosh harf bilan boshlanadi va oxiriga tinish belgisi qo‘yiladi."),
    Q("Qaysi gap to‘g‘ri yozilgan?", "Anvar Samarqandga ketdi.", ["anvar Samarqandga ketdi.", "Anvar samarqandga ketdi.", "anvar samarqandga ketdi"],
      d=2, x="Gap boshi, ism va shahar nomi bosh harf bilan yoziladi."),
    Q("Qaysi gap to‘g‘ri yozilgan?", "Siz qachon kelasiz?", ["Siz qachon kelasiz.", "siz qachon kelasiz?", "Siz qachon kelasiz"],
      x="So‘roq gap bosh harf bilan boshlanib, so‘roq belgisi bilan tugaydi."),
    TF("Gap har doim bosh harf bilan boshlanadi.", True, x="Masalan: Kitob o‘qish foydali."),
]
T.topic("punctuation", "❗", L("Gap oxirida tinish belgilari", "End punctuation", "Знаки в конце предложения"), C4,
        "Gap bosh harf bilan boshlanadi. Gap oxiriga maqsad va ohangga qarab belgi qo‘yiladi:\n"
        "• nuqta (.) — darak va oddiy buyruq gapda;\n"
        "• so‘roq belgisi (?) — so‘roq gapda;\n"
        "• undov belgisi (!) — kuchli his bilan aytilgan gapda: Voy, qanday go‘zal!", items=items)

items = []
for s in ORDER_SENTENCES_G3:
    items.append(ORDER("So‘zlardan gap tuzing", s, d=1 if len(s.split()) <= 4 else 2))
items += [
    Q("Qaysi so‘zlar birikmasi gap bo‘ladi?", "Qushlar sayrayapti.", ["qushlar va", "chiroyli qush", "daraxtdagi"], x="Gap tugal fikr bildiradi."),
    Q("Qaysi so‘zlar birikmasi gap bo‘ladi?", "Men kitob o‘qiyman.", ["kitob va daftar", "qiziq kitob", "kitobning"], x="Gap tugal fikr bildiradi."),
    Q("Qaysi so‘zlar birikmasi gap bo‘ladi?", "Bahorda gullar ochiladi.", ["bahorgi gullar", "gullar va", "bahorda"], d=2, x="Gap tugal fikr bildiradi."),
    TF("Gapdagi so‘zlar ma’no jihatdan bog‘langan bo‘ladi.", True, x="So‘zlar bog‘lanib, tugal fikr hosil qiladi."),
]
T.topic("sentence_build", "🧩", L("Gap tuzish", "Building sentences", "Составление предложений"), C4,
        "Gap tugal fikr bildiradi. Gapdagi so‘zlar ma’no jihatdan bog‘lanadi.\n"
        "O‘zbek tilida odatda avval kim? nima? (ega), oxirida nima qildi? (kesim) keladi:\n"
        "Bolalar hovlida o‘ynashyapti. Onam mazali osh pishirdi.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["sentence_types", "punctuation", "sentence_build"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["sounds", "syllables", "alphabet", "synonyms", "antonyms", "word_parts", "word_classes", "proper_nouns", "noun_forms",
        "adj_verb", "sentence_types", "punctuation", "sentence_build"], C4, level=3)

T.write()
