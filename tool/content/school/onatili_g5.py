"""Ona tili, 5-sinf: fonetika va imlo, leksika, so‘z tarkibi va turkumlari, sintaksis.

Mavzular 5-sinf ona tili dasturi tartibida; qoidalar, misollar va savollar o‘zimizniki.
Qayta yaratish: python3 tool/content/school/onatili_g5.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from uzlang import *  # noqa: E402,F401,F403

rnd = random.Random(5)
T = Course("onatili", 5, L("Ona tili", "Native language", "Родной язык"))

C1 = "1-chorak. Fonetika va imlo"
C2 = "2-chorak. Leksika: so‘z va ma’no"
C3 = "3-chorak. So‘z tarkibi va so‘z turkumlari"
C4 = "4-chorak. Sintaksis: birikma va gap"

# ============================================================ 1-chorak
items = [
    Q("Tovush bilan harfning farqi nimada?", "Tovushni eshitamiz, harfni yozamiz va ko‘ramiz", ["Farqi yo‘q", "Harfni eshitamiz, tovushni yozamiz", "Tovush faqat unli bo‘ladi"],
      x="Tovush — nutqning eng kichik bo‘lagi, harf — tovushning yozuvdagi belgisi."),
    Q("O‘zbek tilida nechta unli tovush bor?", "6 ta", ["5 ta", "8 ta", "10 ta"], x="a, o, u, e, i, o‘."),
    Q("Qaysi qatorda faqat unlilar berilgan?", "a, o, u, e, i, o‘", ["a, b, o, d", "sh, ch, ng, o‘", "e, i, k, l"], x="O‘zbek tilidagi 6 ta unli."),
    Q("Bitta tovushni ikki belgi bilan ifodalaydigan harf birikmasi qaysi?", "sh", ["st", "kt", "rd"], x="sh, ch, ng — harf birikmalari."),
    Q("“shamol” so‘zida nechta tovush bor?", "5 ta", ["6 ta", "4 ta", "7 ta"], d=2, x="sh-a-m-o-l: sh bitta tovush, jami 5 ta."),
    Q("“choynak” so‘zida nechta tovush bor?", "6 ta", ["7 ta", "5 ta", "8 ta"], d=2, x="ch-o-y-n-a-k: 6 ta tovush."),
    Q("“tong” so‘zida nechta tovush bor?", "3 ta", ["4 ta", "2 ta", "5 ta"], d=3, x="t-o-ng: ng bitta tovush."),
    Q("Qaysi harf alohida tovushni bildirmaydi, so‘zni bo‘g‘inlarga ajratib turadi?", "tutuq belgisi (’)", ["o‘", "sh", "ng"], d=2,
      x="Tutuq belgisi (’) tovushni cho‘zib yoki ajratib aytishni bildiradi: ma’no, san’at."),
    TF("Har bir bo‘g‘inda bitta unli bo‘ladi.", True, x="Bo‘g‘inlar soni unlilar soniga teng."),
    TF("“o‘” — undosh tovush.", False, x="“o‘” — unli tovush."),
    TF("“ng” bitta tovushni bildiradi.", True, d=2, x="tong, ming, dengiz so‘zlarida ng — bitta tovush."),
    TF("Tovushni ko‘z bilan ko‘ramiz.", False, x="Tovushni eshitamiz, harfni ko‘ramiz."),
]
for w in ["daraxt", "kutubxona", "o‘quvchi", "bayram", "qaldirg‘och", "shahar", "maktab", "tarvuz"]:
    n = vowel_count(w)
    items.append(Q(f"“{w}” so‘zida nechta bo‘g‘in bor?", f"{n} ta", [f"{k} ta" for k in (n - 1, n + 1, n + 2) if k > 0], d=1 if n <= 2 else 2,
                   x=f"Unlilar: {', '.join(vowels_of(w))} — {n} ta, demak bo‘g‘in ham {n} ta."))
T.topic("phonetics", "🔊", L("Tovush va harf. Unlilar", "Sounds and letters", "Звуки и буквы"), C1,
        "Tovush — nutqning eng kichik bo‘lagi, uni eshitamiz va aytamiz. Harf — tovushning yozuvdagi belgisi.\n"
        "• O‘zbek tilida 6 ta unli: a, o, u, e, i, o‘. Qolganlari — undoshlar.\n"
        "• sh, ch, ng — ikki belgi bilan yoziladigan bitta tovush: shamol (5 tovush), tong (3 tovush).\n"
        "• Bo‘g‘in soni unlilar soniga teng: kitob — 2, kutubxona — 4.", items=items)

items = []
for voiced, voiceless in VOICED_PAIRS:
    items.append(Q(f"“{voiced}” undoshining jarangsiz jufti qaysi?", voiceless, [v for _, v in VOICED_PAIRS if v != voiceless][:3],
                   x=f"{voiced} — {voiceless}: jarangli va jarangsiz juft."))
    items.append(Q(f"“{voiceless}” undoshining jarangli jufti qaysi?", voiced, [v for v, _ in VOICED_PAIRS if v != voiced][:3], d=2,
                   x=f"{voiceless} — {voiced}."))
for v in ["b", "d", "z", "m", "g‘", "r"]:
    items.append(Q("Qaysi undosh jarangli?", v, rnd.sample(VOICELESS, 3), x=f"“{v}” — jarangli undosh: ovoz ishtirok etadi."))
for v in ["p", "s", "sh", "q", "x"]:
    items.append(Q("Qaysi undosh jarangsiz?", v, rnd.sample(VOICED, 3), d=1 if v in ("p", "s") else 2,
                   x=f"“{v}” — jarangsiz undosh: faqat shovqindan hosil bo‘ladi."))
for right, wrong in FINAL_VOICED:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, [wrong, right.rstrip("‘")[:-1]],
                   d=2, x=f"“{right}” so‘zi oxiridagi undosh jarangsiz eshitilsa ham, yozuvda saqlanadi: {right}."))
items += [
    TF("“kitob” so‘zi oxirida “p” eshitilsa ham, “b” yoziladi.", True, x="kitobi, kitobim shakllarida b aniq eshitiladi."),
    TF("Jarangli undoshlar ovoz ishtirokida hosil bo‘ladi.", True, x="Tomoqqa qo‘l qo‘yib “z-z-z” desangiz, titrash seziladi."),
]
T.topic("consonants", "🎙️", L("Jarangli va jarangsiz undoshlar. Imlo", "Voiced and voiceless consonants", "Звонкие и глухие согласные"), C1,
        "Undoshlar jarangli (ovoz ishtirokida) va jarangsiz (faqat shovqin) bo‘ladi.\n"
        "Juftlar: b — p, d — t, g — k, z — s, v — f.\n"
        "Jarangli undoshlar: b, v, g, d, j, z, y, l, m, n, r, g‘. Jarangsizlar: p, f, k, t, s, sh, ch, x, h, q.\n"
        "Imlo: so‘z oxiridagi jarangli undosh jarangsiz eshitilsa ham o‘zgarmay yoziladi:\n"
        "kitob (kitobi), obod (obodi), tog‘ (tog‘i).", items=items)

items = []
for right, wrong in TUTUQ:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong, d=1 if len(items) < 8 else 2,
                   x=f"{right} — tutuq belgisi (’) bilan yoziladi."))
for right, wrong in OG_SPELLING:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong, x=f"To‘g‘ri yozilishi: {right}."))
items += [
    TF("Tutuq belgisi o‘zidan oldingi unlini cho‘ziq yoki ajratib aytishni bildiradi.", True, d=2, x="ma’no, she’r, san’at."),
    TF("“she’r” so‘zi tutuq belgisisiz “sher” deb yozilsa ham ma’nosi o‘zgarmaydi.", False, d=2,
       x="she’r — adabiy asar, sher — yirtqich hayvon. Tutuq belgisi ma’noni farqlaydi."),
    Q("Qaysi juftlikda tutuq belgisi so‘z ma’nosini farqlaydi?", "she’r — sher", ["kitob — kitoblar", "ona — onam", "gul — gullar"], d=3,
      x="she’r (adabiy asar) va sher (hayvon) — turli so‘zlar."),
]
T.topic("spelling", "✍️", L("Imlo: tutuq belgisi, o‘ va g‘", "Spelling: apostrophe, o‘ and g‘", "Орфография: апостроф, o‘ и g‘"), C1,
        "• Tutuq belgisi (’) arab tilidan kirgan ayrim so‘zlarda yoziladi: ma’no, she’r, san’at, ta’lim, e’lon.\n"
        "  U ma’noni farqlashi mumkin: she’r (adabiy asar) — sher (hayvon).\n"
        "• O‘ va G‘ harflari belgisi (‘) bilan yoziladi: o‘qituvchi, g‘isht, bog‘cha, to‘g‘ri.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["phonetics", "consonants", "spelling"], C1)

# ============================================================ 2-chorak
items = []
for a, b, wrong in SYNONYMS_Q[:12]:
    items.append(Q(f"“{a}” so‘zining sinonimini toping.", b, wrong, x=f"{a} — {b}: sinonimlar."))
for a, b, wrong in ANTONYMS_Q[:12]:
    items.append(Q(f"“{a}” so‘zining antonimini toping.", b, wrong, x=f"{a} — {b}: antonimlar."))
for word, s1, s2, m1, m2 in HOMONYMS:
    items.append(Q(f"“{s1}” va “{s2}” gaplaridagi “{word}” so‘zlari qanday so‘zlar?", "Omonimlar",
                   ["Sinonimlar", "Antonimlar", "Iboralar"], d=2, x=f"Yozilishi bir xil, ma’nosi har xil: {m1} va {m2}."))
items += [
    MATCH("Sinonimlarni juftlang", SYNONYMS[:7], d=2),
    MATCH("Antonimlarni juftlang", ANTONYMS[:7], d=2),
    TF("Omonimlar — yozilishi bir xil, ma’nosi har xil so‘zlar.", True, x="ot (hayvon) — ot (ism)."),
    TF("Antonimlar — ma’nosi yaqin so‘zlar.", False, x="Antonimlar — zid ma’noli so‘zlar; ma’nosi yaqinlari — sinonimlar."),
]
T.topic("lexicon", "📘", L("Sinonim, antonim, omonim", "Synonyms, antonyms, homonyms", "Синонимы, антонимы, омонимы"), C2,
        "• Sinonimlar — ma’nosi bir xil yoki yaqin so‘zlar: chiroyli — go‘zal, dono — aqlli.\n"
        "• Antonimlar — zid ma’noli so‘zlar: issiq — sovuq, do‘st — dushman.\n"
        "• Omonimlar — yozilishi va aytilishi bir xil, ma’nosi har xil so‘zlar:\n"
        "  ot (hayvon) — ot (ism), yoz (fasl) — yoz (harakat), o‘t (o‘simlik) — o‘t (olov).", items=items)

items = []
for phrase, word, meaning in FIGURATIVE:
    items.append(Q(f"“{phrase}” birikmasida “{word}” so‘zi qanday ma’noda qo‘llangan?", "Ko‘chma ma’noda", ["O‘z ma’nosida", "Omonim sifatida", "Antonim sifatida"],
                   x=f"“{phrase}” — {meaning}. So‘z boshqa narsaga o‘xshatib ishlatilgan."))
    items.append(Q(f"“{phrase}” birikmasining ma’nosi qaysi?", meaning,
                   rnd.sample([m for _, _, m in FIGURATIVE if m != meaning], 3), d=2, x=f"“{phrase}” — {meaning}."))
for plain in ["oltin uzuk", "temir eshik", "tosh devor", "shirin qovun", "sovuq suv", "achchiq qalampir"]:
    items.append(Q(f"“{plain}” birikmasida birinchi so‘z qanday ma’noda qo‘llangan?", "O‘z ma’nosida", ["Ko‘chma ma’noda", "Ibora tarkibida", "Omonim sifatida"],
                   d=2, x=f"“{plain}” — narsaning haqiqiy belgisi: o‘z ma’no."))
items += [
    TF("“oltin qo‘l” birikmasida “oltin” o‘z ma’nosida qo‘llangan.", False, x="Ko‘chma ma’no: mohir, usta."),
    TF("Bir so‘z bir necha ma’noga ega bo‘lishi mumkin.", True, x="Masalan, “ko‘z”: odamning ko‘zi, uzukning ko‘zi, buloqning ko‘zi."),
]
T.topic("figurative", "🌟", L("O‘z va ko‘chma ma’no", "Literal and figurative meaning", "Прямое и переносное значение"), C2,
        "So‘zning asosiy ma’nosi — o‘z ma’no: oltin uzuk, temir eshik, sovuq suv.\n"
        "So‘z boshqa narsaga o‘xshatib ishlatilsa — ko‘chma ma’no: oltin qo‘l (mohir), temir intizom (qattiq),\n"
        "sovuq javob (iltifotsiz), shirin so‘z (yoqimli).\n"
        "Ko‘p ma’noli so‘z: ko‘z — odamning ko‘zi, uzukning ko‘zi, buloqning ko‘zi.", items=items)

items = []
for idiom, meaning, wrong in IDIOMS:
    items.append(Q(f"“{idiom}” iborasining ma’nosi qaysi?", meaning, wrong, d=1 if len(items) < 9 else 2, x=f"“{idiom}” — {meaning}."))
items += [
    MATCH("Iborani ma’nosi bilan juftlang", [(i, m) for i, m, _ in IDIOMS[:7]], d=2),
    TF("Ibora ikki yoki undan ortiq so‘zdan tuzilib, bir butun ma’no bildiradi.", True, x="og‘zi qulog‘ida — juda xursand."),
    TF("“qo‘li ochiq” iborasi baxil odam haqida aytiladi.", False, x="qo‘li ochiq — saxiy."),
    Q("Qaysi gapda ibora ishlatilgan?", "Sovg‘ani ko‘rib, ukamning og‘zi qulog‘ida bo‘ldi.",
      ["Ukam olmani yuvib yedi.", "Ukam kitob o‘qidi.", "Ukamning qulog‘i og‘rimoqda."], d=3, x="og‘zi qulog‘ida — juda xursand."),
]
T.topic("idioms", "🗣️", L("Iboralar", "Idioms", "Фразеологизмы"), C2,
        "Ibora (frazeologizm) — ikki yoki undan ortiq so‘zdan tuzilgan, bir butun ko‘chma ma’no bildiradigan birikma.\n"
        "Misollar: qo‘li ochiq — saxiy; ko‘zi to‘rt bo‘lmoq — intiqib kutmoq; og‘zi qulog‘ida — juda xursand;\n"
        "ko‘z ochib yumguncha — juda tez. Iboralar nutqni ta’sirli va obrazli qiladi.", items=items)

items = []
for word, meaning in OLD_WORDS:
    items.append(Q(f"Eskirgan “{word}” so‘zining ma’nosi qaysi?", meaning, rnd.sample([m for _, m in OLD_WORDS if m != meaning], 3), d=2,
                   x=f"{word} — {meaning}. Bunday so‘zlar tarixiy asarlarda uchraydi."))
for term, field in TERMS:
    items.append(Q(f"“{term}” qaysi fanga oid atama?", field, [f for f in ("Matematika", "Tabiiy fan", "Ona tili", "Informatika") if f != field],
                   x=f"{term} — {field.lower()} atamasi."))
items += [
    TF("Atama — fan yoki kasbga oid so‘z.", True, x="kasr, sayyora, kesim, algoritm."),
    TF("Eskirgan so‘zlar hozirgi nutqda kam ishlatiladi.", True, x="Ular tarixiy asarlarda uchraydi: mirshab, qozi."),
    Q("Qaysi so‘z yangi paydo bo‘lgan so‘z (neologizm)?", "smartfon", ["mirshab", "chopar", "sarbon"], d=2,
      x="smartfon — yaqinda paydo bo‘lgan narsa nomi."),
]
T.topic("vocab_use", "🏺", L("Eskirgan so‘zlar va atamalar", "Archaic words and terms", "Устаревшие слова и термины"), C2,
        "• Eskirgan so‘zlar — hozir kam ishlatiladigan so‘zlar: mirshab, qozi, chopar, sarbon.\n"
        "• Yangi so‘zlar (neologizmlar) — yangi narsa va tushunchalar nomi: smartfon, planshet.\n"
        "• Atamalar — fan va kasbga oid so‘zlar: kasr (matematika), sayyora (tabiiy fan), kesim (ona tili).", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["lexicon", "figurative", "idioms", "vocab_use"], C2)

# ============================================================ 3-chorak
items = []
for word, base, suf, meaning in DERIVED:
    items.append(Q(f"“{word}” so‘zining o‘zagi qaysi?", base, [word, "-" + suf, base[:-1] if len(base) > 3 else word + "lar"], d=1,
                   x=f"{word} = {base} + {suf}."))
    items.append(Q(f"“{word}” so‘zida qaysi so‘z yasovchi qo‘shimcha bor?", "-" + suf,
                   ["-" + x for x in rnd.sample([s for s in ("chi", "kor", "zor", "don", "li", "siz", "lik", "la", "xon", "kash", "bon") if s != suf], 2)] + ["-" + rnd.choice(FORM_SUFFIXES)],
                   d=2, x=f"{base} + {suf} = {word} ({meaning} bildiruvchi yangi so‘z)."))
items += [
    Q("Qaysi so‘zda shakl yasovchi qo‘shimcha bor?", "kitoblar", ["kitobxon", "ishchi", "gulzor"], d=2,
      x="-lar yangi so‘z yasamaydi, so‘z shaklini o‘zgartiradi (ko‘plik)."),
    Q("Qaysi so‘zda so‘z yasovchi qo‘shimcha bor?", "paxtakor", ["paxtani", "paxtaga", "paxtaning"], d=2, x="paxta + kor — yangi so‘z (kasb egasi)."),
    TF("So‘z yasovchi qo‘shimcha yangi ma’noli so‘z hosil qiladi.", True, x="ish — ishchi, gul — gulzor."),
    TF("“-ning” — so‘z yasovchi qo‘shimcha.", False, x="-ning — kelishik qo‘shimchasi, u shakl yasaydi."),
]
T.topic("morphemes", "🧱", L("So‘z tarkibi va so‘z yasalishi", "Word structure and word formation", "Состав и образование слов"), C3,
        "So‘z tarkibi: o‘zak + qo‘shimchalar. O‘zak — so‘zning asosiy ma’noli qismi.\n"
        "• So‘z yasovchi qo‘shimcha yangi so‘z hosil qiladi: ish+chi, paxta+kor, gul+zor, tuz+don, aql+li, suv+siz, do‘st+lik.\n"
        "• Shakl yasovchi qo‘shimcha so‘zning shaklini o‘zgartiradi: kitob+lar, kitob+ning, kitob+im.\n"
        "Tartib: o‘zak → so‘z yasovchi → shakl yasovchi: ish-chi-lar-imiz.", items=items)

items = []
classes = list(WORD_CLASSES_G5)
for cls, words in WORD_CLASSES_G5.items():
    for w in words:
        wrong = [c for c in classes if c != cls]
        items.append(Q(f"“{w}” so‘zi qaysi so‘z turkumiga kiradi?", cls, rnd.sample(wrong, 3), d=1 if cls in ("Ot", "Sifat", "Son", "Fe’l") else 2,
                       x=f"“{w}” — {cls.lower()}."))
items += [
    MATCH("So‘z turkumini misol bilan juftlang", [("Ot", "bahor"), ("Sifat", "keng"), ("Son", "yigirma"), ("Olmosh", "ular"), ("Fe’l", "yozdi"), ("Ravish", "hamisha")], d=2),
    TF("Olmosh ot, sifat yoki son o‘rnida qo‘llanadi.", True, x="men, sen, u, bu, shu, kim, hamma."),
    TF("Ravish harakatning belgisini bildiradi.", True, x="yayov bordi, birdan to‘xtadi, ataylab qildi."),
]
T.topic("word_classes", "🗂️", L("Mustaqil so‘z turkumlari", "Parts of speech", "Самостоятельные части речи"), C3,
        "• Ot — kim? nima? qayer?: kitob, bahor, do‘stlik.\n"
        "• Sifat — qanday? qanaqa?: aqlli, keng, qizil.\n"
        "• Son — nechta? nechanchi?: yigirma, beshinchi.\n"
        "• Olmosh — ot, sifat, son o‘rnida keladi: men, biz, bu, kim, hamma.\n"
        "• Fe’l — harakat: yozdi, keladi. • Ravish — harakat belgisi: yayov, hamisha, birdan, ertaga.", items=items)

items = []
for word in CASE_WORDS:
    for i, (suf, case, q) in enumerate(CASES):
        form = word + suf
        wrong = [c for _, c, _ in rnd.sample([x for x in CASES if x[1] != case], 3)]
        items.append(Q(f"“{form}” so‘zi qaysi kelishikda?", case, wrong, d=1 if word in ("kitob", "maktab") else 2,
                       x=f"“{form}”: {('-' + suf + ' qo‘shimchasi') if suf else 'qo‘shimchasiz'}, so‘rog‘i: {q}"))
for word, right in DATIVE:
    items.append(Q(f"“{word}” so‘ziga jo‘nalish kelishigi qo‘shimchasini qo‘shing.", right, dative_wrong(word, right), d=2,
                   x=f"{right}: k bilan tugasa -ka, q bilan tugasa -qa, qolganlarda -ga." if not right.endswith("ga") else f"{right}: -ga qo‘shiladi."))
items += [
    MATCH("Kelishikni qo‘shimchasi bilan juftlang", [(c, "-" + s if s else "qo‘shimchasiz") for s, c, _ in CASES], d=2),
    TF("O‘zbek tilida 6 ta kelishik bor.", True, x="bosh, qaratqich, tushum, jo‘nalish, o‘rin-payt, chiqish."),
]
T.topic("cases", "🔀", L("Otlarning kelishiklar bilan turlanishi", "Noun cases", "Падежи существительных"), C3,
        "O‘zbek tilida 6 ta kelishik bor:\n"
        "bosh (—) kim? nima?;  qaratqich (-ning) kimning?;  tushum (-ni) kimni? nimani?;\n"
        "jo‘nalish (-ga, -ka, -qa) kimga? qayerga?;  o‘rin-payt (-da) kimda? qayerda?;  chiqish (-dan) kimdan? qayerdan?\n"
        "Imlo: k bilan tugagan so‘zga -ka (yurakka), q bilan tugaganga -qa (qishloqqa) qo‘shiladi.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["morphemes", "word_classes", "cases"], C3)

# ============================================================ 4-chorak
items = []
for text, kind in PHRASE_OR_SENTENCE:
    items.append(Q(f"“{text}” — bu nima?", kind, [k for k in ("So‘z birikmasi", "Gap", "Ibora", "Qo‘shma so‘z") if k != kind][:3],
                   x="Gap tugal fikr bildiradi; so‘z birikmasi esa narsa yoki harakatni aniqroq nomlaydi."))
items += [
    Q("Qaysi biri so‘z birikmasi?", "qiziqarli kitob", ["Kitob qiziqarli.", "Men o‘qidim.", "Kitob qiziq edi."], x="qiziqarli kitob — hokim so‘z (kitob) va tobe so‘z (qiziqarli)."),
    Q("“yangi maktab” birikmasida hokim so‘z qaysi?", "maktab", ["yangi", "ikkalasi", "hech biri"], d=2, x="qanday maktab? — yangi: tobe so‘z yangi, hokim so‘z maktab."),
    Q("“kitob o‘qimoq” birikmasida hokim so‘z qaysi?", "o‘qimoq", ["kitob", "ikkalasi", "hech biri"], d=3, x="nimani o‘qimoq? — kitob: hokim so‘z o‘qimoq."),
    TF("So‘z birikmasi tugal fikr bildiradi.", False, x="Tugal fikrni gap bildiradi."),
]
T.topic("phrases", "🔗", L("So‘z birikmasi va gap", "Phrases and sentences", "Словосочетание и предложение"), C4,
        "So‘z birikmasi — ikki yoki undan ortiq mustaqil so‘zning ma’no va grammatik jihatdan bog‘lanishi:\n"
        "chiroyli gul, kitob o‘qimoq. Unda hokim so‘z va tobe so‘z bor: qanday gul? — chiroyli (tobe), gul (hokim).\n"
        "Gap — tugal fikr bildiradi va ohang bilan aytiladi: Gul chiroyli.", items=items)

items = []
for sent, subj, pred in SUBJ_PRED:
    words = [w.strip(".") for w in sent.split()]
    others = [w for w in words if w not in subj.split() and w not in pred.split()]
    items.append(Q(f"“{sent}” gapida ega qaysi so‘z?", subj, [pred] + others[:2], x=f"Kim? nima? — {subj}. Ega — gapning bosh bo‘lagi."))
    items.append(Q(f"“{sent}” gapida kesim qaysi?", pred, [subj] + others[:2], d=2, x=f"Nima qildi? — {pred}. Kesim egani ta’riflaydi."))
items += [
    TF("Ega kim? nima? so‘roqlariga javob beradi.", True, x="Ali kitob o‘qidi: kim? — Ali."),
    TF("Kesim ko‘pincha gapning oxirida keladi.", True, x="O‘zbek tilida kesim odatda gap oxirida bo‘ladi."),
    MATCH("Gap bo‘lagini so‘rog‘i bilan juftlang", [("Ega", "kim? nima?"), ("Kesim", "nima qildi? qanday?"), ("To‘ldiruvchi", "kimni? nimani?"),
                                                    ("Aniqlovchi", "qanday? qaysi?"), ("Hol", "qayerda? qachon? qanday qilib?")], d=3),
]
T.topic("sentence_parts", "🏗️", L("Gap bo‘laklari: ega va kesim", "Subject and predicate", "Подлежащее и сказуемое"), C4,
        "Gapning bosh bo‘laklari — ega va kesim.\n"
        "• Ega — kim? nima? so‘roqlariga javob beradi: Bolalar o‘ynashdi.\n"
        "• Kesim — egani ta’riflaydi: nima qildi? nima qilyapti? qanday?: Bolalar o‘ynashdi.\n"
        "Ikkinchi darajali bo‘laklar: to‘ldiruvchi (kimni? nimani?), aniqlovchi (qanday? qaysi?), hol (qayerda? qachon?).", items=items)

items = []
for sent, voc in VOCATIVE:
    words = [w.strip(",.!?") for w in sent.split()]
    others = [w for w in words if w not in voc.split()]
    items.append(Q(f"“{sent}” gapida undalma qaysi?", voc, rnd.sample(others, min(3, len(others))), x=f"{voc} — nutq qaratilgan shaxs; undalmadan keyin vergul qo‘yiladi."))
for sent, parts in HOMOGENEOUS:
    wrong = []
    words = [w.strip(",.") for w in sent.split() if w.strip(",.").lower() not in parts.split(", ") and w.strip(",.") != "va"]
    wrong.append(", ".join(words[:2]).lower())
    wrong.append(parts.split(", ")[0] + ", " + words[-1].lower())
    items.append(Q(f"“{sent}” gapidagi uyushiq bo‘laklarni toping.", parts, wrong + ["uyushiq bo‘lak yo‘q"], d=2,
                   x=f"{parts} — bir xil so‘roqqa javob beradi va bir so‘zga bog‘lanadi."))
items += [
    Q("Qaysi gapda vergul to‘g‘ri qo‘yilgan?", "Anvar, kitobingni olib kel.", ["Anvar kitobingni, olib kel.", "Anvar kitobingni olib, kel.", "Anvar kitobingni olib kel,"],
      x="Undalmadan keyin vergul qo‘yiladi."),
    Q("Qaysi gapda vergul to‘g‘ri qo‘yilgan?", "Bog‘da olma, nok, o‘rik bor.", ["Bog‘da, olma nok o‘rik bor.", "Bog‘da olma nok, o‘rik, bor.", "Bog‘da olma nok o‘rik, bor."],
      d=2, x="Uyushiq bo‘laklar orasiga vergul qo‘yiladi."),
    TF("Uyushiq bo‘laklar “va” bog‘lovchisi bilan bog‘langanda, ular orasiga vergul qo‘yilmaydi.", True, d=3, x="Akam va opam keldi."),
    TF("Undalma gap bo‘lagi hisoblanadi.", False, d=3, x="Undalma gap bo‘lagi emas, u nutq kimga qaratilganini bildiradi."),
]
T.topic("vocative_homogeneous", "📣", L("Undalma va uyushiq bo‘laklar", "Direct address and compound parts", "Обращение и однородные члены"), C4,
        "• Undalma — nutq qaratilgan shaxs yoki narsa: Ali, bu yoqqa kel. Undalma vergul bilan ajratiladi, u gap bo‘lagi emas.\n"
        "• Uyushiq bo‘laklar — bir xil so‘roqqa javob beradigan va bir so‘zga bog‘lanadigan bo‘laklar:\n"
        "  Olma, nok va o‘rik pishdi. Uyushiq bo‘laklar orasiga vergul qo‘yiladi, “va” oldidan qo‘yilmaydi.", items=items)

items = []
for sent, kind in SENTENCE_TYPES_G3:
    items.append(Q(f"“{sent}” — maqsadiga ko‘ra qanday gap?", kind, [k for k in ("Darak gap", "So‘roq gap", "Buyruq gap") if k != kind],
                   x=SENT_EXPLAIN[kind]))
for sent, mark in PUNCT_G3:
    items.append(Q(f"Gap oxiriga qaysi belgi qo‘yiladi: “{sent}…”", mark, [m for m in (".", "?", "!", ",") if m != mark], d=2,
                   x=f"{sent}{mark} — {PUNCT_EXPLAIN[mark]}"))
items += [
    Q("His-hayajon bilan aytilgan gap qanday ataladi?", "Undov gap", ["Darak gap", "So‘roq gap", "Buyruq gap"], d=2, x="Undov gap oxirida undov belgisi qo‘yiladi: Qanday go‘zal!"),
    TF("Buyruq gap oxiriga nuqta yoki undov belgisi qo‘yiladi.", True, d=2, x="Eshikni yoping. Tezroq yuring!"),
]
T.topic("sentence_types", "💬", L("Gap turlari va tinish belgilari", "Sentence types and punctuation", "Виды предложений и знаки"), C4,
        "Maqsadiga ko‘ra: darak (xabar), so‘roq (savol), buyruq (buyruq, iltimos) gaplar.\n"
        "His-hayajon bilan aytilsa — undov gap: Voy, qanday chiroyli!\n"
        "Tinish belgilari: darak gap — nuqta; so‘roq gap — so‘roq belgisi; undov gap — undov belgisi;\n"
        "buyruq gap — nuqta yoki undov belgisi.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["phrases", "sentence_parts", "vocative_homogeneous", "sentence_types"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["phonetics", "consonants", "spelling", "lexicon", "figurative", "idioms", "vocab_use", "morphemes", "word_classes", "cases",
        "phrases", "sentence_parts", "vocative_homogeneous", "sentence_types"], C4, level=3)

T.write()
