"""Ona tili, 4-sinf: tovush va bo‘g‘in, so‘z tarkibi, ot, sifat, son, olmosh, fe’l, gap va matn.

Mavzular 4-sinf ona tili dasturi tartibida (3 va 5-sinf oralig‘idagi bosqich); qoidalar, misollar, gaplar va
matnlar o‘zimizniki. 3 va 5-sinf savollari takrorlanmasligi uchun so‘z va gap ro‘yxatlari shu faylda yangidan
tuzilgan (uzlang.py dan faqat yordamchi funksiyalar olinadi).
Qayta yaratish: python3 tool/content/school/onatili_g4.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from uzlang import letters  # noqa: E402

rnd = random.Random(4)
T = Course("onatili", 4, L("Ona tili", "Native language", "Родной язык"))

C1 = "1-chorak. Tovush, bo‘g‘in va so‘z tarkibi"
C2 = "2-chorak. Ot va qo‘shimchalar imlosi"
C3 = "3-chorak. Sifat, son, olmosh va fe’l"
C4 = "4-chorak. Gap va matn"


def others(options, right, k=None):
    """`options` ichidan `right` dan boshqalari (ixtiyoriy: tasodifiy `k` tasi)."""
    rest = [o for o in options if o != right]
    return rnd.sample(rest, k) if k is not None and k < len(rest) else rest


# ============================================================ 1-chorak
# ------------------------------------------------------------ tovush va harf
items = []
for w, d in [("qovun", 1), ("bulbul", 1), ("yulduz", 1), ("qishloq", 1), ("chiroq", 1), ("g‘isht", 2), ("o‘quvchi", 2),
             ("shaftoli", 2), ("bodring", 2), ("ming", 2), ("sichqon", 2), ("qo‘shiq", 2)]:
    parts = letters(w)
    n = len(parts)
    items.append(Q(f"“{w}” so‘zida nechta tovush bor?", f"{n} ta", [f"{k} ta" for k in (n - 1, n + 1, n + 2)], d=d,
                   x=f"{'-'.join(parts)} — {n} ta tovush" + (" (sh, ch, ng, o‘, g‘ — bitta tovush)." if any(len(p) > 1 for p in parts) else ".")))
V_START = ["anor", "ilon", "uzum", "echki", "o‘rik", "olcha"]
C_START = ["nok", "behi", "tarvuz", "gilos", "shaftoli", "chumoli", "sabzi", "limon"]
for w in V_START:
    items.append(Q("Qaysi so‘z unli tovush bilan boshlanadi?", w, rnd.sample(C_START, 3), d=1,
                   x=f"“{w}” so‘zi “{letters(w)[0]}” unlisi bilan boshlanadi."))
for w in C_START[:4]:
    items.append(Q("Qaysi so‘z undosh tovush bilan boshlanadi?", w, rnd.sample(V_START, 3), d=1,
                   x=f"“{w}” so‘zi “{letters(w)[0]}” undoshi bilan boshlanadi."))
for right, wrong in [("va’da", ["vada", "vaada"]), ("in’om", ["inom", "inoom"]), ("mas’ul", ["masul", "masuul"]),
                     ("a’zo", ["azo", "aazo"]), ("ta’mir", ["tamir", "taamir"]), ("ma’rifat", ["marifat", "maarifat"])]:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong + [right.replace("’", "") + "a"], d=2,
                   x=f"“{right}” so‘zi tutuq belgisi (’) bilan yoziladi."))
items += [
    Q("Qaysi harf birikmalari bitta tovushni bildiradi?", "sh, ch, ng", ["st, sk, nt", "rt, lm, nd", "ts, kh, ph"], d=1,
      x="sh, ch, ng ikki belgi bilan yoziladi, lekin bitta tovushni bildiradi."),
    Q("“Poyezd katta … bilan yurdi.” Nuqtalar o‘rniga qaysi so‘z mos?", "sur’at", ["surat", "sura’t", "suvrat"], d=3,
      x="sur’at — tezlik, surat — rasm: tutuq belgisi ma’noni farqlaydi."),
    Q("“Devorga chiroyli … ilindi.” Nuqtalar o‘rniga qaysi so‘z mos?", "surat", ["sur’at", "sura’t", "su’rat"], d=3,
      x="surat — rasm, sur’at — tezlik."),
    TF("“ch” ikki belgi bilan yozilsa ham, bitta tovushni bildiradi.", True, x="choy: ch-o-y — 3 ta tovush."),
    TF("“qishloq” so‘zida 7 ta tovush bor.", False, x="q-i-sh-l-o-q — 6 ta tovush, chunki sh bitta tovush."),
    TF("O‘zbek tilida undosh tovushlar unlilardan ko‘p.", True, d=2, x="Unlilar atigi 6 ta, qolgan tovushlarning hammasi undosh."),
    TF("Har bir bo‘g‘inning markazida unli tovush turadi.", True, d=2, x="Unli bo‘lmasa, bo‘g‘in ham bo‘lmaydi."),
    MATCH("So‘zni undagi tovushlar soni bilan juftlang",
          [("ming", "3 ta"), ("g‘isht", "4 ta"), ("chiroq", "5 ta"), ("qishloq", "6 ta"), ("shaftoli", "7 ta")], d=2,
          x="sh, ch, ng, o‘, g‘ — bitta tovush."),
]
T.topic("sounds_letters", "🔤", L("Tovush va harf", "Sounds and letters", "Звуки и буквы"), C1,
        "Tovushni eshitamiz va aytamiz, harfni ko‘ramiz va yozamiz.\n"
        "• Unli tovushlar 6 ta: a, o, u, e, i, o‘. Qolgan tovushlar — undoshlar.\n"
        "• sh, ch, ng ikki belgi bilan yoziladi, lekin bitta tovushni bildiradi: qishloq — q-i-sh-l-o-q (6 tovush).\n"
        "• Tutuq belgisi (’) ayrim so‘zlarda yoziladi: va’da, a’zo, mas’ul.\n"
        "  U ma’noni farqlashi mumkin: sur’at (tezlik) — surat (rasm).", items=items)

# ------------------------------------------------------------ bo‘g‘in ko‘chirish
SYL4 = {
    "sabzavot": ["sab", "za", "vot"], "tuxum": ["tu", "xum"], "qovoq": ["qo", "voq"], "qishloq": ["qish", "loq"],
    "sichqon": ["sich", "qon"], "qaldirg‘och": ["qal", "dir", "g‘och"], "sandiq": ["san", "diq"],
    "yostiq": ["yos", "tiq"], "ko‘ylak": ["ko‘y", "lak"], "darslik": ["dars", "lik"], "qo‘shiq": ["qo‘", "shiq"],
    "lochin": ["lo", "chin"], "bedana": ["be", "da", "na"], "musiqa": ["mu", "si", "qa"], "dasturxon": ["das", "tur", "xon"],
    "bayroq": ["bay", "roq"],
}


def hyph(syl, k):
    return "".join(syl[:k]) + "-" + "".join(syl[k:])


def hyph_wrong(syl, k):
    """Chegarani bir harfga surish va sh/ch ni bo‘lish — noto‘g‘ri ko‘chirishlar."""
    left, right = letters("".join(syl[:k])), letters("".join(syl[k:]))
    out = []
    if len(left) > 1:
        out.append("".join(left[:-1]) + "-" + "".join([left[-1]] + right))
    if len(right) > 1:
        out.append("".join(left + [right[0]]) + "-" + "".join(right[1:]))
    word = "".join(syl)
    for dg in ("sh", "ch"):
        i = word.find(dg)
        if 0 < i < len(word) - 2:
            out.append(word[:i + 1] + "-" + word[i + 1:])
    return list(dict.fromkeys(out))


items = []
for n, (w, syl) in enumerate(SYL4.items()):
    k = 1 if len(syl) == 2 or n % 2 == 0 else 2
    right = hyph(syl, k)
    wrong = [x for x in hyph_wrong(syl, k) if x != right]
    items.append(Q(f"“{w}” so‘zi qaysi qatorda to‘g‘ri ko‘chirilgan?", right, wrong, d=1 if len(syl) == 2 else 2,
                   x=f"Bo‘g‘inlar: {'-'.join(syl)}. So‘z bo‘g‘in chegarasidan ko‘chiriladi."))
CAN_BREAK = ["kitob", "daftar", "qalam", "bola", "tuxum", "gilam", "chiroq", "hovli", "sandiq", "maktab"]
for w, syl in [("uzum", "u-zum"), ("ayiq", "a-yiq"), ("ilon", "i-lon"), ("ariq", "a-riq"), ("o‘rik", "o‘-rik"),
               ("uka", "u-ka"), ("tosh", None), ("qo‘l", None)]:
    why = f"{syl}: birinchi bo‘g‘in bitta harfdan iborat, uni qatorda qoldirib bo‘lmaydi." if syl else "Bir bo‘g‘inli so‘z bo‘linmaydi."
    items.append(Q("Qaysi so‘zni bo‘g‘inga bo‘lib ko‘chirib bo‘lmaydi?", w, rnd.sample(CAN_BREAK, 3), d=1 if syl is None else 2, x=why))
for w in ["sabzavot", "bedana", "dasturxon", "musiqa", "tuxum", "yostiq"]:
    n = len(SYL4[w])
    items.append(Q(f"“{w}” so‘zida nechta bo‘g‘in bor?", f"{n} ta", [f"{k} ta" for k in (n - 1, n + 1, n + 2)], d=1,
                   x=f"{'-'.join(SYL4[w])} — {n} ta bo‘g‘in."))
for s in ["be-da-na", "po-mi-dor", "das-tur-xon", "kar-tosh-ka"]:
    items.append(ORDER("Bo‘g‘inlardan so‘z tuzing", s, sep="-", d=1 if len(s) < 10 else 2, x=f"{s.replace('-', '')}: {s}."))
items += [
    Q("“ta’lim” so‘zi qanday ko‘chiriladi?", "ta’-lim", ["ta-’lim", "t-a’lim", "ta’l-im"], d=3,
      x="Tutuq belgisi o‘zidan oldingi harf bilan birga qoladi: ta’-lim."),
    TF("sh va ch harf birikmalari ko‘chirishda bo‘linmaydi.", True, x="qish-loq, lo-chin."),
    TF("“uzum” so‘zini “u-zum” tarzida ko‘chirish mumkin.", False, d=2, x="Bitta harfli bo‘g‘in qatorda qoldirilmaydi."),
    TF("Bir bo‘g‘inli so‘zni bo‘lib ko‘chirib bo‘lmaydi.", True, x="tosh, non, qo‘l — butunligicha yangi qatorga o‘tadi."),
    TF("So‘z qatordan qatorga bo‘g‘in bo‘yicha ko‘chiriladi.", True, x="san-diq, yos-tiq."),
]
T.topic("hyphenation", "✂️", L("Bo‘g‘in va so‘zni ko‘chirish", "Syllables and hyphenation", "Слог и перенос"), C1,
        "So‘z qatordan qatorga bo‘g‘in bo‘yicha ko‘chiriladi: san-diq, ko‘y-lak, sab-zavot.\n"
        "• Bitta harfli bo‘g‘in qatorda qoldirilmaydi va yangi qatorga o‘tkazilmaydi: u-zum, a-yiq so‘zlari bo‘linmaydi.\n"
        "• Bir bo‘g‘inli so‘z bo‘linmaydi: tosh, qo‘l.\n"
        "• sh, ch harf birikmalari bo‘linmaydi: qish-loq (qis-hloq emas).\n"
        "• Tutuq belgisi oldingi harf bilan qoladi: ta’-lim.", items=items)

# ------------------------------------------------------------ so‘z tarkibi
DERIVED4 = [("baliqchi", "baliq", "chi"), ("o‘yinchi", "o‘yin", "chi"), ("paxtazor", "paxta", "zor"), ("tokzor", "tok", "zor"),
            ("guldon", "gul", "don"), ("siyohdon", "siyoh", "don"), ("toshloq", "tosh", "loq"), ("o‘tloq", "o‘t", "loq"),
            ("odobli", "odob", "li"), ("tinchlik", "tinch", "lik"), ("bolalik", "bola", "lik"), ("ishchan", "ish", "chan"),
            ("ovla", "ov", "la"), ("tishla", "tish", "la"), ("kuzgi", "kuz", "gi"), ("uyqusiz", "uyqu", "siz")]
DER_SUFFIXES = ["chi", "zor", "don", "loq", "li", "lik", "chan", "la", "gi", "siz"]
bases = [b for _, b, _ in DERIVED4]
items = []
for n, (w, base, suf) in enumerate(DERIVED4):
    if n % 2 == 0:
        items.append(Q(f"“{w}” so‘zida o‘zak qaysi?", base, [w, "-" + suf, rnd.choice([b for b in bases if b not in w])], d=1,
                       x=f"{w} = {base} (o‘zak) + {suf}."))
    else:
        items.append(Q(f"“{w}” so‘zini qaysi so‘z yasovchi qo‘shimcha hosil qilgan?", "-" + suf,
                       ["-" + s for s in others(DER_SUFFIXES, suf, 2)] + ["-lar"], d=2,
                       x=f"{base} + {suf} = {w}: yangi ma’noli so‘z."))
items += [
    Q("Qaysi so‘zda shakl yasovchi qo‘shimcha bor?", "gullar", ["guldon", "gulchi", "gulla"], d=1,
      x="-lar yangi so‘z yasamaydi, faqat ko‘plik shaklini beradi."),
    Q("Qaysi so‘zda shakl yasovchi qo‘shimcha bor?", "ishimiz", ["ishchi", "ishchan", "ishla"], d=2,
      x="-imiz — egalik qo‘shimchasi, u so‘z shaklini o‘zgartiradi."),
    Q("Qaysi so‘zda so‘z yasovchi qo‘shimcha bor?", "baliqchi", ["baliqlar", "baliqni", "baliqning"], d=1,
      x="baliq + chi — yangi so‘z (kasb egasi)."),
    Q("Qaysi so‘zda so‘z yasovchi qo‘shimcha bor?", "tokzor", ["toklar", "tokda", "tokni"], d=2, x="tok + zor — yangi so‘z (joy)."),
    Q("“-lar” qanday qo‘shimcha?", "Shakl yasovchi", ["So‘z yasovchi", "O‘zak", "Bog‘lovchi"], d=1, x="-lar ko‘plik shaklini beradi, yangi so‘z yasamaydi."),
    Q("“-chi” qanday qo‘shimcha?", "So‘z yasovchi", ["Shakl yasovchi", "O‘zak", "Kelishik qo‘shimchasi"], d=1,
      x="-chi yangi so‘z yasaydi: baliq — baliqchi."),
    Q("Qaysi qatorda o‘zakdosh so‘zlar berilgan?", "ish, ishchi, ishla", ["ish, ilon, iz", "gul, gilam, gilos", "tosh, tog‘, tovuq"], d=2,
      x="Uchala so‘zda bir xil o‘zak bor: ish."),
    Q("Qaysi so‘z “tosh” so‘zi bilan o‘zakdosh?", "toshloq", ["tovush", "to‘shak", "tog‘li"], d=1,
      x="tosh + loq = toshloq: o‘zagi tosh."),
    Q("“baliqchilarimiz” so‘zi qanday tuzilgan?", "baliq + chi + lar + imiz",
      ["baliqchi + larim + iz", "bali + qchi + lar + imiz", "baliq + chilar + imiz"], d=3,
      x="O‘zak (baliq), so‘z yasovchi (-chi), shakl yasovchilar (-lar, -imiz)."),
    TF("“baliq” va “baliqchi” — ma’nosi har xil so‘zlar.", True, x="baliq — suv jonivori, baliqchi — baliq tutuvchi kishi."),
    TF("Shakl yasovchi qo‘shimcha yangi so‘z yasamaydi.", True, x="kitob — kitoblar: so‘z o‘sha, faqat shakli o‘zgardi."),
    TF("“guldon” so‘zidagi “-don” — shakl yasovchi qo‘shimcha.", False, d=2, x="-don yangi so‘z (idish nomi) yasaydi."),
    TF("So‘zga avval so‘z yasovchi, keyin shakl yasovchi qo‘shimcha qo‘shiladi.", True, d=2, x="baliq-chi-lar: -chi, keyin -lar."),
    MATCH("Yasama so‘zni o‘zagi bilan juftlang",
          [("baliqchi", "baliq"), ("paxtazor", "paxta"), ("guldon", "gul"), ("toshloq", "tosh"), ("ishchan", "ish"), ("tishla", "tish")], d=2),
    MATCH("Qo‘shimchani ma’nosi bilan juftlang",
          [("-chi", "kasb egasi"), ("-zor", "ko‘p o‘sadigan joy"), ("-don", "idish"), ("-lar", "ko‘plik"), ("-siz", "belgining yo‘qligi")], d=2),
]
T.topic("word_structure", "🧱", L("So‘z tarkibi: o‘zak va qo‘shimchalar", "Word structure", "Состав слова"), C1,
        "So‘z o‘zak va qo‘shimchalardan tuziladi. O‘zak — so‘zning asosiy ma’noli qismi.\n"
        "• So‘z yasovchi qo‘shimcha yangi ma’noli so‘z hosil qiladi: baliq — baliqchi, paxta — paxtazor, gul — guldon.\n"
        "• Shakl yasovchi qo‘shimcha yangi so‘z yasamaydi, so‘z shaklini o‘zgartiradi: baliq — baliqlar, baliqni.\n"
        "• Avval so‘z yasovchi, keyin shakl yasovchi qo‘shiladi: baliq-chi-lar-imiz.\n"
        "Bir o‘zakli so‘zlar o‘zakdosh so‘zlar deyiladi: ish, ishchi, ishla, ishchan.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["sounds_letters", "hyphenation", "word_structure"], C1)

# ============================================================ 2-chorak
# ------------------------------------------------------------ ot: atoqli va turdosh, birlik va ko‘plik
items = [
    Q("Qaysi so‘z atoqli ot?", "Jizzax", ["shahar", "viloyat", "tuman"], x="Jizzax — shahar nomi, atoqli ot."),
    Q("Qaysi so‘z atoqli ot?", "Nodira", ["qiz", "o‘quvchi", "opa"], x="Nodira — kishi ismi, atoqli ot."),
    Q("Qaysi so‘z atoqli ot?", "Aydarko‘l", ["ko‘l", "dengiz", "daryo"], x="Aydarko‘l — ko‘l nomi, atoqli ot."),
    Q("Qaysi so‘z turdosh ot?", "mamlakat", ["Qozog‘iston", "Guliston", "Jahongir"], x="mamlakat — umumiy nom, turdosh ot."),
    Q("Qaysi so‘z turdosh ot?", "kuchukcha", ["Olapar", "Oydin", "Urganch"], x="kuchukcha — bir turdagi hayvonlarning umumiy nomi."),
    Q("Qaysi so‘z shahar nomi?", "Guliston", ["Olapar", "Aydarko‘l", "Oydin"], d=2, x="Guliston — shahar."),
    Q("Qaysi so‘z ko‘l nomi?", "Aydarko‘l", ["Qarshi", "Nodira", "Olapar"], d=2, x="Aydarko‘l — ko‘l."),
    Q("Qaysi so‘z mamlakat nomi?", "Qozog‘iston", ["Jizzax", "Aydarko‘l", "Jahongir"], d=2, x="Qozog‘iston — mamlakat."),
]
for sent, word, kind in [("Olapar hovlini qo‘riqlaydi.", "Olapar", "Atoqli ot"), ("Bizning itimiz hovlini qo‘riqlaydi.", "itimiz", "Turdosh ot"),
                         ("Yozda Aydarko‘lga bordik.", "Aydarko‘lga", "Atoqli ot"), ("Yozda ko‘lga bordik.", "ko‘lga", "Turdosh ot"),
                         ("Jahongir maktabga shoshildi.", "Jahongir", "Atoqli ot"), ("Bola maktabga shoshildi.", "Bola", "Turdosh ot")]:
    items.append(Q(f"“{sent}” gapidagi “{word}” so‘zi qanday ot?", kind, [k for k in ("Atoqli ot", "Turdosh ot") if k != kind] + ["Sifat", "Fe’l"],
                   d=2, x="Atoqli ot — yakka nom (bosh harf bilan), turdosh ot — umumiy nom."))
for right, wrong in [("qushlar", ["qushcha", "qushni", "qushga"]), ("tovuqlar", ["tovuqni", "tovuqqa", "tovuqda"]),
                     ("ko‘chalar", ["ko‘chada", "ko‘chaga", "ko‘chani"]), ("mevalar", ["mevali", "mevazor", "mevani"])]:
    items.append(Q("Qaysi so‘z ko‘plik shaklida?", right, wrong, x=f"{right}: -lar qo‘shimchasi ko‘plikni bildiradi."))
for right, wrong in [("beshta olma", ["beshta olmalar", "besh olmalar"]), ("uchta daftar", ["uchta daftarlar", "uch daftarlar"]),
                     ("o‘nta qush", ["o‘nta qushlar", "o‘n qushlar"])]:
    items.append(Q("Qaysi birikma to‘g‘ri?", right, wrong, d=2, x=f"Sondan keyin ot birlikda keladi: {right}."))
items += [
    Q("Qaysi gapda atoqli ot to‘g‘ri yozilgan?", "Biz Jizzaxga bordik.", ["Biz jizzaxga bordik.", "biz jizzaxga bordik.", "Biz jizzaxga Bordik."],
      x="Joy nomi gapning o‘rtasida ham bosh harf bilan yoziladi."),
    Q("“Bobom keldilar.” gapida “-lar” qanday ma’noni bildiradi?", "Hurmat", ["Ko‘plik", "Egalik", "Kelishik"], d=3,
      x="Bobom — bitta kishi; -lar bu yerda hurmat ma’nosida."),
    Q("Kitob, gazeta va jurnal nomlari qanday yoziladi?", "Qo‘shtirnoqda, bosh harf bilan", ["Kichik harf bilan", "Qavs ichida", "Chiziqcha bilan"],
      d=3, x="Masalan: “Gulxan” jurnali."),
    TF("Atoqli otlar gapning o‘rtasida ham bosh harf bilan yoziladi.", True, x="Biz Guliston shahriga bordik."),
    TF("Hayvonlarga qo‘yilgan nomlar ham atoqli ot hisoblanadi.", True, d=2, x="Olapar — itning nomi, atoqli ot."),
    TF("Sondan keyin kelgan ot odatda birlik shaklida bo‘ladi.", True, d=2, x="uchta kitob, o‘nta qush."),
    MATCH("Turdosh otni atoqli ot bilan juftlang",
          [("shahar", "Guliston"), ("ko‘l", "Aydarko‘l"), ("mamlakat", "Qozog‘iston"), ("it", "Olapar"), ("qiz", "Nodira"), ("o‘g‘il bola", "Jahongir")], d=2),
]
T.topic("nouns", "🏙️", L("Ot: atoqli va turdosh, birlik va ko‘plik", "Nouns: proper, common, plural", "Существительное"), C2,
        "Ot kim? nima? qayer? so‘roqlariga javob beradi.\n"
        "• Turdosh ot — bir turdagi narsalarning umumiy nomi: shahar, ko‘l, it, qiz.\n"
        "• Atoqli ot — yakka nom, bosh harf bilan yoziladi: Jizzax, Aydarko‘l, Olapar, Nodira.\n"
        "• Ko‘plik -lar bilan yasaladi: qush — qushlar. Sondan keyin ot birlikda keladi: beshta olma.\n"
        "• -lar hurmatni ham bildiradi: Bobom keldilar.", items=items)

# ------------------------------------------------------------ egalik qo‘shimchalari
PERSONS = [("mening", "m", "im"), ("sening", "ng", "ing"), ("uning", "si", "i"), ("bizning", "miz", "imiz"), ("sizning", "ngiz", "ingiz")]


def poss(word, p, alt=False):
    vowel = word[-1] in "aoueiy"
    _, v_suf, c_suf = PERSONS[p]
    return word + ((c_suf if vowel else v_suf) if alt else (v_suf if vowel else c_suf))


items = []
for word, ps in [("oila", (3, 0)), ("mahalla", (2, 3)), ("ko‘cha", (1, 4)), ("ruchka", (2, 0)),
                 ("sinf", (3, 1)), ("do‘st", (0, 2)), ("maktab", (3, 4)), ("bog‘", (1, 2))]:
    for p in ps:
        right = poss(word, p)
        wrong = [poss(word, p, alt=True)] + [poss(word, q) for q in others(range(5), p, 2)]
        items.append(Q(f"To‘g‘ri shaklni tanlang: {PERSONS[p][0]} … (“{word}”)", right, wrong, d=1 if p < 3 else 2,
                       x=f"{PERSONS[p][0]} {right}: {'unli' if word[-1] in 'aoueiy' else 'undosh'} bilan tugagan so‘zga -{right[len(word):]}."))
for word, right, wrong in [("yurak", "yuragim", ["yurakim", "yurakkim"]), ("qishloq", "qishlog‘im", ["qishloqim", "qishlogim"]),
                           ("o‘rtoq", "o‘rtog‘im", ["o‘rtoqim", "o‘rtogim"]), ("eshik", "eshigim", ["eshikim", "eshikkim"]),
                           ("tayoq", "tayog‘im", ["tayoqim", "tayoqqim"]), ("chelak", "chelagim", ["chelakim", "chelakkim"]),
                           ("qoshiq", "qoshig‘im", ["qoshiqim", "qoshigim"])]:
    items.append(Q(f"“{word}” so‘ziga “-im” qo‘shilganda qanday yoziladi?", right, wrong, d=2,
                   x=f"Ko‘p bo‘g‘inli so‘z oxiridagi {word[-1]} undoshi {'g' if word[-1] == 'k' else 'g‘'} ga aylanadi: {right}."))
for word, right, wrong in [("og‘iz", "og‘zim", ["og‘izim", "og‘izm"]), ("burun", "burnim", ["burunim", "burunm"]),
                           ("o‘g‘il", "o‘g‘lim", ["o‘g‘ilim", "o‘g‘ilm"]), ("singil", "singlim", ["singilim", "singilm"])]:
    items.append(Q(f"“{word}” so‘ziga “-im” qo‘shilganda qanday yoziladi?", right, wrong, d=3,
                   x=f"Bu so‘zda ikkinchi bo‘g‘indagi unli tushib qoladi: {word} — {right}."))
items += [
    Q("Egalik qo‘shimchasi nimani bildiradi?", "Narsa kimga qarashli ekanini", ["Narsaning sonini", "Harakat vaqtini", "Narsaning rangini"],
      x="kitobim — mening kitobim."),
    Q("“daftarimiz” so‘zi kimga qarashli narsani bildiradi?", "bizga", ["menga", "senga", "sizga"], d=2, x="bizning daftarimiz: -imiz."),
    TF("Unli bilan tugagan so‘zga III shaxs egalik qo‘shimchasi -si shaklida qo‘shiladi.", True, x="oila — oilasi, ko‘cha — ko‘chasi."),
    TF("“yurak” so‘ziga -im qo‘shilsa, “yurakim” deb yoziladi.", False, d=2, x="To‘g‘ri: yuragim (k — g ga aylanadi)."),
    MATCH("Olmoshni egalik shakli bilan juftlang",
          [("mening", "sinfim"), ("sening", "sinfing"), ("uning", "sinfi"), ("bizning", "sinfimiz"), ("sizning", "sinfingiz")], d=2),
]
T.topic("possessive", "👜", L("Egalik qo‘shimchalari", "Possessive suffixes", "Аффиксы принадлежности"), C2,
        "Egalik qo‘shimchalari narsa kimga qarashli ekanini bildiradi:\n"
        "• unli bilan tugagan so‘zga: oila-m, oila-ng, oila-si, oila-miz, oila-ngiz;\n"
        "• undosh bilan tugagan so‘zga: sinf-im, sinf-ing, sinf-i, sinf-imiz, sinf-ingiz.\n"
        "• Ko‘p bo‘g‘inli so‘z oxiridagi k — g ga, q — g‘ ga aylanadi: yurak — yuragim, qishloq — qishlog‘im.\n"
        "• Ayrim so‘zlarda unli tushib qoladi: og‘iz — og‘zim, burun — burnim.", items=items)

# ------------------------------------------------------------ kelishiklar
CASE_NAMES = ["Bosh kelishik", "Qaratqich kelishigi", "Tushum kelishigi", "Jo‘nalish kelishigi", "O‘rin-payt kelishigi", "Chiqish kelishigi"]
CASE_QS = ["kim? nima?", "kimning? nimaning?", "kimni? nimani?", "kimga? qayerga?", "kimda? qayerda?", "kimdan? qayerdan?"]
CASE_SENT = [
    ("Quyosh charaqlab chiqdi.", "Quyosh", 0), ("Ukamning velosipedi yangi.", "Ukamning", 1), ("Opam gullarni sug‘ordi.", "gullarni", 2),
    ("Biz daryoga bordik.", "daryoga", 3), ("Qushlar daraxtda sayrayapti.", "daraxtda", 4), ("Dadam ishdan qaytdi.", "ishdan", 5),
    ("Bolalar hovlida o‘ynashdi.", "Bolalar", 0), ("Daraxtning barglari sarg‘aydi.", "Daraxtning", 1), ("Men xatni pochtaga olib bordim.", "xatni", 2),
    ("Dadam ukamga to‘p olib berdi.", "ukamga", 3), ("Kitoblar javonda turibdi.", "javonda", 4), ("Daryodan salqin shabada esdi.", "Daryodan", 5),
]
items = []
for n, (sent, word, c) in enumerate(CASE_SENT):
    items.append(Q(f"“{sent}” gapidagi “{word}” so‘zi qaysi kelishikda?", CASE_NAMES[c], others(CASE_NAMES, CASE_NAMES[c], 3),
                   d=1 if n < 6 else 2, x=f"“{word}” — {CASE_QS[c]} so‘rog‘iga javob beradi: {CASE_NAMES[c].lower()}."))
for c, name in enumerate(CASE_NAMES):
    items.append(Q(f"{name} qaysi so‘roqlarga javob beradi?", CASE_QS[c], others(CASE_QS, CASE_QS[c], 3), d=1 if c % 2 == 0 else 2,
                   x=f"{name}: {CASE_QS[c]}"))
for suf, c in [("-ning", 1), ("-ni", 2), ("-da", 4)]:
    items.append(Q(f"“{suf}” qaysi kelishik qo‘shimchasi?", CASE_NAMES[c], others(CASE_NAMES, CASE_NAMES[c], 3), x=f"{suf} — {CASE_NAMES[c].lower()}."))
items += [
    Q("Qaysi kelishikning maxsus qo‘shimchasi yo‘q?", "Bosh kelishik", CASE_NAMES[1:4], x="Bosh kelishikdagi so‘z qo‘shimchasiz keladi: Quyosh chiqdi."),
    Q("“Men … kitob oldim.” Nuqtalar o‘rniga mos so‘zni tanlang.", "kutubxonadan", ["kutubxonaning", "kutubxonani", "kutubxona"], d=2,
      x="qayerdan oldim? — kutubxonadan (chiqish kelishigi)."),
    Q("“Men … kitobini o‘qidim.” Nuqtalar o‘rniga mos so‘zni tanlang.", "akamning", ["akamni", "akamga", "akamdan"], d=2,
      x="kimning kitobini? — akamning (qaratqich kelishigi)."),
    Q("“Ali … yordam berdi.” Nuqtalar o‘rniga mos so‘zni tanlang.", "onasiga", ["onasini", "onasining", "onasidan"], d=2,
      x="kimga yordam berdi? — onasiga (jo‘nalish kelishigi)."),
    TF("O‘rin-payt kelishigi “qayerdan?” so‘rog‘iga javob beradi.", False, x="O‘rin-payt — qayerda?, chiqish — qayerdan?"),
    TF("Qaratqich kelishigining qo‘shimchasi — -ning.", True, x="ukamning, daraxtning."),
    MATCH("Kelishikni so‘rog‘i bilan juftlang", list(zip(CASE_NAMES, CASE_QS)), d=2),
]
T.topic("cases", "🔀", L("Kelishik qo‘shimchalari", "Noun cases", "Падежи"), C2,
        "Ot gapdagi boshqa so‘zlar bilan kelishik qo‘shimchalari orqali bog‘lanadi. O‘zbek tilida 6 ta kelishik bor:\n"
        "• Bosh (qo‘shimchasiz) — kim? nima?  • Qaratqich (-ning) — kimning? nimaning?\n"
        "• Tushum (-ni) — kimni? nimani?  • Jo‘nalish (-ga, -ka, -qa) — kimga? qayerga?\n"
        "• O‘rin-payt (-da) — kimda? qayerda?  • Chiqish (-dan) — kimdan? qayerdan?\n"
        "Misol: Dadam ishdan (qayerdan?) qaytdi.", items=items)

# ------------------------------------------------------------ qo‘shimchalar imlosi
items = []
DATIVE4 = [("eshik", "eshikka"), ("chelak", "chelakka"), ("bilak", "bilakka"), ("ko‘prik", "ko‘prikka"), ("qoshiq", "qoshiqqa"),
           ("quloq", "quloqqa"), ("tayoq", "tayoqqa"), ("bayroq", "bayroqqa"), ("tuproq", "tuproqqa"), ("barg", "bargga"),
           ("bulut", "bulutga"), ("daryo", "daryoga")]
for n, (w, right) in enumerate(DATIVE4):
    wrong = [f for f in (w + "ga", w + "ka", w + "qa") if f != right]
    rule = "k bilan tugagan so‘zga -ka" if w.endswith("k") else ("q bilan tugagan so‘zga -qa" if w.endswith("q") else "k, q dan boshqa tovush bilan tugagan so‘zga -ga")
    items.append(Q(f"“{w}” + jo‘nalish kelishigi — qaysi yozuv to‘g‘ri?", right, wrong, d=1 if n < 8 else 2, x=f"{rule}: {right}."))
for right, wrong in [("kuzgi", ["kuzki", "kuzqi"]), ("yozgi", ["yozki", "yozqi"]), ("bahorgi", ["bahorki", "bahorqi"]),
                     ("qishki", ["qishgi", "qishqi"]), ("kechki", ["kechgi", "kechqi"]), ("ichki", ["ichgi", "ichqi"]),
                     ("tashqi", ["tashki", "tashgi"]), ("tungi", ["tunki", "tunqi"])]:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong, d=2, x=f"To‘g‘ri yozilishi: {right}."))
for verb, right in [("ek", "ekkan"), ("tik", "tikkan"), ("chiq", "chiqqan"), ("yoq", "yoqqan")]:
    wrong = [f for f in (verb + "gan", verb + "kan", verb + "qan") if f != right]
    items.append(Q(f"“{verb}” fe’liga “-gan” qo‘shilsa, qanday yoziladi?", right, wrong, d=3,
                   x=f"{'k' if verb.endswith('k') else 'q'} bilan tugagan so‘zga -{'kan' if verb.endswith('k') else 'qan'} qo‘shiladi: {right}."))
for right, wrong in [("eshikda", ["eshikta", "eshigda"]), ("kitobdan", ["kitobtan", "kitopdan"]), ("qishloqda", ["qishloqta", "qishlog‘da"]),
                     ("tayoqlar", ["tayog‘lar", "tayoqqlar"])]:
    items.append(Q("Qaysi so‘z to‘g‘ri yozilgan?", right, wrong, d=2 if right != "eshikda" else 1,
                   x=f"-da, -dan, -lar qo‘shimchalari o‘zgarmaydi va o‘zak ham o‘zgarmaydi: {right}."))
items += [
    TF("k bilan tugagan so‘zga jo‘nalish kelishigi -ka shaklida qo‘shiladi.", True, x="eshik — eshikka, chelak — chelakka."),
    TF("q bilan tugagan so‘zga jo‘nalish kelishigi -qa shaklida qo‘shiladi.", True, x="quloq — quloqqa, tayoq — tayoqqa."),
    TF("Adabiy tilda “eshikta” emas, “eshikda” deb yoziladi.", True, x="-da qo‘shimchasi o‘zgarmaydi."),
    TF("“qishki” so‘zi “qishgi” deb yoziladi.", False, d=2, x="To‘g‘ri: qishki."),
    TF("“bulut” so‘ziga jo‘nalish kelishigi -ga shaklida qo‘shiladi.", True, d=2, x="bulutga: faqat k va q dan keyin -ka, -qa bo‘ladi."),
    MATCH("So‘zni to‘g‘ri shakli bilan juftlang",
          [("quloq", "quloqqa"), ("chelak", "chelakka"), ("barg", "bargga"), ("bulut", "bulutga"), ("tayoq", "tayoqqa")], d=2),
]
T.topic("suffix_spelling", "✍️", L("Qo‘shimchalar imlosi", "Spelling of suffixes", "Правописание аффиксов"), C2,
        "Qo‘shimchalar yozilishi:\n"
        "• Jo‘nalish kelishigi: k bilan tugagan so‘zga -ka (eshikka), q bilan tugaganga -qa (quloqqa), qolganlarga -ga (bargga, bulutga).\n"
        "• -gan qo‘shimchasi ham shunday: ek — ekkan, chiq — chiqqan.\n"
        "• -da, -dan o‘zgarmaydi: eshikda, kitobdan (eshikta, kitobtan emas).\n"
        "• -gi qo‘shimchali so‘zlar: kuzgi, yozgi, tungi; lekin qishki, kechki, ichki, tashqi.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["nouns", "possessive", "cases", "suffix_spelling"], C2)

# ============================================================ 3-chorak
# ------------------------------------------------------------ sifat darajalari
DEG = ["Oddiy daraja", "Qiyosiy daraja", "Orttirma daraja"]
items = []
for n, (form, deg) in enumerate([("keng", 0), ("shirinroq", 1), ("eng baland", 2), ("issiq", 0), ("yumshoqroq", 1), ("juda chiroyli", 2),
                                 ("yorug‘", 0), ("tezroq", 1), ("eng toza", 2), ("kichikroq", 1), ("qip-qizil", 2), ("oppoq", 2),
                                 ("nihoyatda katta", 2), ("sovuqroq", 1)]):
    items.append(Q(f"“{form}” sifati qaysi darajada?", DEG[deg], others(DEG, DEG[deg]) + ["Sifat emas"], d=1 if n < 9 else 2,
                   x=["Belgi oddiy holda — oddiy daraja.", "-roq qo‘shimchasi — qiyosiy daraja.", "Belgi juda kuchli — orttirma daraja."][deg]))
for adj in ["baland", "shirin", "keng", "yumshoq"]:
    items.append(Q("Qaysi sifat qiyosiy darajada?", adj + "roq", [adj, "eng " + adj, "juda " + adj], d=1, x=f"{adj} + roq = {adj}roq."))
for right, wrong in [("eng chiroyli", ["chiroyli", "chiroyliroq", "chiroylicha"]), ("juda issiq", ["issiq", "issiqroq", "iliqroq"]),
                     ("qop-qora", ["qora", "qoraroq", "qoramtir"])]:
    items.append(Q("Qaysi sifat orttirma darajada?", right, wrong, d=1 if right.startswith("eng") else 2, x=f"{right} — belgi juda kuchli."))
items += [
    Q("“oq” sifatining orttirma darajasi qaysi?", "oppoq", ["oqroq", "op-oq", "oq-oq"], d=3, x="oppoq qo‘shib yoziladi."),
    Q("Qaysi yozuv to‘g‘ri?", "kattaroq", ["katta roq", "katta-roq"], d=2, x="-roq qo‘shimchasi qo‘shib yoziladi."),
    Q("Qaysi yozuv to‘g‘ri?", "eng baland", ["engbaland", "eng-baland"], d=2, x="“eng” so‘zi sifatdan ajratib yoziladi."),
    Q("Qaysi yozuv to‘g‘ri?", "qip-qizil", ["qipqizil", "qip qizil"], d=2, x="Takrorlangan bo‘g‘in chiziqcha bilan yoziladi: qip-qizil, yam-yashil."),
    Q("Sifat qaysi so‘roqlarga javob beradi?", "qanday? qanaqa?", ["kim? nima?", "nima qildi?", "nechta?"], x="qanday olma? — qizil olma."),
    TF("-roq qo‘shimchasi sifatning qiyosiy darajasini hosil qiladi.", True, x="shirin — shirinroq."),
    TF("“eng” so‘zi sifatdan ajratib yoziladi.", True, x="eng katta, eng a’lo."),
    TF("“qip-qizil” — oddiy darajadagi sifat.", False, d=2, x="qip-qizil — orttirma daraja."),
    TF("Orttirma daraja belgining juda kuchli ekanini bildiradi.", True, d=2, x="eng baland, juda shirin, oppoq."),
    MATCH("Sifatni u bildirgan belgi bilan juftlang",
          [("sariq", "rang"), ("nordon", "maza"), ("dumaloq", "shakl"), ("ulkan", "hajm"), ("kamtar", "xarakter"), ("xushbo‘y", "hid")], d=2),
]
T.topic("adjectives", "🎨", L("Sifat darajalari", "Degrees of adjectives", "Степени прилагательных"), C3,
        "Sifat narsaning belgisini bildiradi va qanday? qanaqa? so‘roqlariga javob beradi.\n"
        "Sifat darajalari:\n"
        "• Oddiy daraja — belgi oddiy holda: shirin, baland.\n"
        "• Qiyosiy daraja — -roq qo‘shimchasi bilan, belgi solishtiriladi: shirinroq, balandroq.\n"
        "• Orttirma daraja — belgi juda kuchli: eng baland, juda shirin, qip-qizil, oppoq.", items=items)

# ------------------------------------------------------------ son
KINDS = ["Sanoq son", "Tartib son", "Dona son"]
ORDINALS = [("bir", "birinchi"), ("ikki", "ikkinchi"), ("uch", "uchinchi"), ("olti", "oltinchi"), ("besh", "beshinchi"), ("yetti", "yettinchi"),
            ("to‘rt", "to‘rtinchi"), ("sakkiz", "sakkizinchi"), ("to‘qqiz", "to‘qqizinchi"), ("o‘n", "o‘ninchi"), ("yigirma", "yigirmanchi"),
            ("qirq", "qirqinchi")]
items = []
for n, (num, right) in enumerate(ORDINALS):
    vowel = num[-1] in "aoueiy"
    alt = num + ("inchi" if vowel else "nchi")
    items.append(Q(f"“{num}” sonidan tartib son yasang.", right, [alt, num + "ta", num + "chi"], d=1 if n < 6 else 2,
                   x=f"{'Unli' if vowel else 'Undosh'} bilan tugagan songa -{'nchi' if vowel else 'inchi'} qo‘shiladi: {right}."))
for n, (w, k) in enumerate([("yettinchi", 1), ("o‘n ikki", 0), ("beshta", 2), ("uchinchi", 1), ("to‘qqiz", 0), ("yigirmata", 2),
                            ("birinchi", 1), ("qirq", 0), ("o‘nta", 2)]):
    items.append(Q(f"“{w}” qanday son?", KINDS[k], others(KINDS, KINDS[k]) + ["Sifat"], d=1 if n < 6 else 2,
                   x=["Sanoq son — necha? qancha?", "Tartib son — nechanchi? (-inchi, -nchi)", "Dona son — nechta? (-ta)"][k]))
items += [
    Q("Tartib son qaysi so‘roqqa javob beradi?", "nechanchi?", ["nechta?", "qanday?", "kim?"], x="nechanchi sinf? — to‘rtinchi sinf."),
    Q("Dona son qaysi so‘roqqa javob beradi?", "nechta?", ["nechanchi?", "qanday?", "qayerda?"], x="nechta olma? — beshta olma."),
    Q("Qaysi yozuv to‘g‘ri?", "4-sinf", ["4 sinf", "4-chi sinf", "4-inchi sinf"], d=1, x="Raqam bilan yozilgan tartib sondan keyin chiziqcha qo‘yiladi."),
    Q("Qaysi yozuv to‘g‘ri?", "1-sentabr", ["1 sentabr", "1-chi sentabr", "1-inchi sentabr"], d=2, x="Sana ham tartib son: 1-sentabr."),
    Q("Qaysi son to‘g‘ri yozilgan?", "o‘n besh", ["o‘nbesh", "o‘n-besh"], d=2, x="Qo‘shma sonlar ajratib yoziladi."),
    Q("Qaysi son to‘g‘ri yozilgan?", "yigirma uch", ["yigirmauch", "yigirma-uch"], d=2, x="Qo‘shma sonlar ajratib yoziladi."),
    Q("“Men 4-sinfda o‘qiyman.” gapidagi “4-” qanday o‘qiladi?", "to‘rtinchi", ["to‘rt", "to‘rtta", "to‘rtov"], d=2,
      x="Chiziqcha tartib sonni bildiradi: to‘rtinchi sinf."),
    TF("Tartib son -inchi yoki -nchi qo‘shimchasi bilan yasaladi.", True, x="uch — uchinchi, ikki — ikkinchi."),
    TF("“olti” so‘ziga -inchi qo‘shilib, “oltiinchi” deb yoziladi.", False, d=2, x="Unli bilan tugagani uchun -nchi: oltinchi."),
    TF("“o‘n besh” soni qo‘shib yoziladi.", False, d=2, x="Qo‘shma sonlar ajratib yoziladi: o‘n besh."),
    MATCH("Raqamli yozuvni so‘z bilan juftlang",
          [("2-qavat", "ikkinchi qavat"), ("5-uy", "beshinchi uy"), ("8-mart", "sakkizinchi mart"), ("1-o‘rin", "birinchi o‘rin"), ("10-bet", "o‘ninchi bet")], d=2),
]
T.topic("numerals", "🔢", L("Son: sanoq, tartib va dona sonlar", "Numerals", "Числительное"), C3,
        "Son narsaning miqdorini yoki tartibini bildiradi.\n"
        "• Sanoq son — necha? qancha?: uch, o‘n besh, yuz.\n"
        "• Tartib son — nechanchi?: undosh bilan tugagan songa -inchi (uchinchi), unli bilan tugaganga -nchi (ikkinchi).\n"
        "• Dona son — nechta?: -ta qo‘shimchasi bilan: beshta, o‘nta.\n"
        "Raqam bilan yozilgan tartib sondan keyin chiziqcha qo‘yiladi: 4-sinf. Qo‘shma sonlar ajratib yoziladi: o‘n besh.", items=items)

# ------------------------------------------------------------ kishilik olmoshlari
NOT_PRON = ["bola", "kitob", "yaxshi", "keldi", "ona", "daraxt", "uch", "tez"]
items = []
for p in ["men", "sen", "biz", "siz", "ular"]:
    items.append(Q("Qaysi so‘z kishilik olmoshi?", p, rnd.sample(NOT_PRON, 3), x=f"“{p}” — kishilik olmoshi."))
for sg, pl, wrong in [("men", "biz", ["siz", "ular", "menlar"]), ("sen", "siz", ["biz", "ular", "senlar"]), ("u", "ular", ["biz", "siz", "ulas"])]:
    items.append(Q(f"“{sg}” olmoshining ko‘plik shakli qaysi?", pl, wrong, x=f"{sg} — {pl}."))
PERS = {"men": "I shaxs birlik", "biz": "I shaxs ko‘plik", "sen": "II shaxs birlik", "siz": "II shaxs ko‘plik", "u": "III shaxs birlik", "ular": "III shaxs ko‘plik"}
for p in ["biz", "sen", "ular", "men"]:
    items.append(Q(f"“{p}” olmoshi qaysi shaxs va sonni bildiradi?", PERS[p], others(list(PERS.values()), PERS[p], 3), d=2, x=f"{p} — {PERS[p]}."))
for p, s, right, wrong, d in [("men", "ga", "menga", ["meniga", "menka", "mega"], 1), ("men", "ni", "meni", ["menni", "menini", "mni"], 1),
                              ("sen", "ga", "senga", ["seniga", "senka", "sega"], 1), ("u", "ga", "unga", ["uga", "uniga", "unka"], 2),
                              ("u", "ning", "uning", ["uni", "unning", "uing"], 2), ("u", "da", "unda", ["uda", "unida", "u-da"], 2),
                              ("u", "dan", "undan", ["udan", "unidan", "u-dan"], 2)]:
    items.append(Q(f"“{p}” olmoshiga “-{s}” qo‘shilsa, qanday yoziladi?", right, wrong, d=d, x=f"To‘g‘ri yozilishi: {right}."))
for text, pron, right, wrong in [("Sardor futbolni yaxshi ko‘radi. U har kuni mashq qiladi.", "U", "Sardor", ["futbol", "mashq", "har kuni"]),
                                 ("Zarina va Laylo bog‘ga borishdi. Ular gul terishdi.", "Ular", "Zarina va Laylo", ["bog‘", "gullar", "Laylo"]),
                                 ("Bolalar hovlida o‘ynashdi. Keyin ular uyga kirishdi.", "ular", "bolalar", ["hovli", "uy", "o‘yin"])]:
    items.append(Q(f"Ikkinchi gapdagi “{pron}” olmoshi kimni bildiradi?", right, wrong, d=2, text=text, e="👥",
                   x=f"Olmosh takrorlanmasligi uchun “{right}” o‘rnida kelgan."))
for q, right, wrong, d in [("“Biz ertaga muzeyga …” — mos so‘zni tanlang.", "boramiz", ["boraman", "borasan", "borasiz"], 1),
                           ("“Men har kuni erta …” — mos so‘zni tanlang.", "turaman", ["turasan", "turamiz", "turasiz"], 1),
                           ("“Sen uy vazifasini …?” — mos so‘zni tanlang.", "bajardingmi", ["bajardimmi", "bajardikmi", "bajardimi"], 2),
                           ("“Ular kutubxonaga …” — mos so‘zni tanlang.", "borishdi", ["bordim", "bording", "bordik"], 2)]:
    items.append(Q(q, right, wrong, d=d, x="Fe’l olmosh bilan shaxs va sonda moslashadi."))
items += [
    Q("Kishilik olmoshlari qaysi so‘z turkumi o‘rnida qo‘llanadi?", "Ot", ["Sifat", "Son", "Fe’l"], d=2, x="Sardor keldi — U keldi: olmosh ot o‘rnida."),
    TF("“Siz” olmoshi bir kishiga hurmat bilan murojaat qilganda ham ishlatiladi.", True, x="Ustoz, siz bizga yordam berdingiz."),
    TF("Kishilik olmoshlari oltita: men, sen, u, biz, siz, ular.", True, x="Uchta birlikda, uchta ko‘plikda."),
    TF("“ular” — birlikdagi olmosh.", False, x="ular — III shaxs ko‘plik."),
    MATCH("Olmoshni fe’l bilan juftlang",
          [("men", "o‘qidim"), ("sen", "o‘qiding"), ("biz", "o‘qidik"), ("siz", "o‘qidingiz"), ("ular", "o‘qishdi")], d=2),
]
T.topic("pronouns", "👤", L("Kishilik olmoshlari", "Personal pronouns", "Личные местоимения"), C3,
        "Olmosh ot o‘rnida kelib, so‘z takrorlanmasligiga yordam beradi: Sardor futbol o‘ynaydi. U har kuni mashq qiladi.\n"
        "Kishilik olmoshlari:\n"
        "• I shaxs: men (birlik), biz (ko‘plik); II shaxs: sen, siz; III shaxs: u, ular.\n"
        "• “Siz” bir kishiga hurmat bilan murojaatda ham ishlatiladi.\n"
        "• Qo‘shimchalar bilan: menga, meni, mening; unga, uni, uning, unda, undan.", items=items)

# ------------------------------------------------------------ fe’l: zamon, bo‘lishli va bo‘lishsiz
TENSES = ["O‘tgan zamon", "Hozirgi zamon", "Kelasi zamon"]
TENSE_SENT = [
    ("Kecha biz hayvonot bog‘iga bordik.", "bordik", 0), ("Hozir onam non yopyapti.", "yopyapti", 1), ("Ertaga biz sayohatga boramiz.", "boramiz", 2),
    ("Ukam kecha chiroyli rasm chizdi.", "chizdi", 0), ("Men hozir kitob o‘qiyapman.", "o‘qiyapman", 1),
    ("Keyingi yil men beshinchi sinfga o‘taman.", "o‘taman", 2), ("Bugun ertalab qor yog‘di.", "yog‘di", 0),
    ("Qarang, bolalar hovlida o‘ynayapti.", "o‘ynayapti", 1), ("Ertaga dars soat sakkizda boshlanadi.", "boshlanadi", 2),
    ("O‘tgan yozda biz tog‘ga chiqdik.", "chiqdik", 0), ("Ayni paytda dadam mashinani tuzatmoqda.", "tuzatmoqda", 1),
    ("Kelasi yozda men suzishni o‘rganaman.", "o‘rganaman", 2),
]
items = []
for n, (sent, verb, t) in enumerate(TENSE_SENT):
    items.append(Q(f"“{sent}” gapidagi “{verb}” fe’li qaysi zamonda?", TENSES[t], others(TENSES, TENSES[t]), d=1 if n < 6 else 2,
                   x=["Harakat bo‘lib o‘tgan: o‘tgan zamon.", "Harakat hozir bo‘lyapti: hozirgi zamon.", "Harakat hali bo‘ladi: kelasi zamon."][t]))
NEG = [("keldi", "kelmadi", ["kelmaydi", "keldimi", "kelmas"]), ("yozadi", "yozmaydi", ["yozmadi", "yozadimi", "yozmayapti"]),
       ("chizdi", "chizmadi", ["chizmaydi", "chizdimi", "chizmayapti"]), ("bordik", "bormadik", ["bormaymiz", "bordikmi", "bormadim"]),
       ("o‘qiyapti", "o‘qimayapti", ["o‘qimadi", "o‘qiyaptimi", "o‘qimaydi"]), ("ishlayapti", "ishlamayapti", ["ishlamadi", "ishlamaydi", "ishlayaptimi"]),
       ("o‘ynaydi", "o‘ynamaydi", ["o‘ynamadi", "o‘ynaydimi", "o‘ynamayapti"]), ("kuldi", "kulmadi", ["kulmaydi", "kuldimi", "kulmayapti"])]
for n, (v, right, wrong) in enumerate(NEG):
    items.append(Q(f"“{v}” fe’lining bo‘lishsiz shaklini toping.", right, wrong, d=1 if n < 4 else 2, x=f"-ma qo‘shimchasi: {v} — {right}."))
items += [
    Q("Qaysi fe’l o‘tgan zamonda?", "o‘qidi", ["o‘qiyapti", "o‘qimoqda", "o‘qimoqchi"], x="o‘qidi — nima qildi?: o‘tgan zamon."),
    Q("Qaysi fe’l hozirgi zamonda?", "yozyapti", ["yozdi", "yozdik", "yozmoqchi"], x="yozyapti — nima qilyapti?: hozirgi zamon."),
    Q("Qaysi fe’l bo‘lishsiz?", "kelmadi", ["keldi", "keladi", "kelyapti"], x="-ma qo‘shimchasi harakat bajarilmaganini bildiradi."),
    Q("Qaysi fe’l bo‘lishsiz?", "o‘qimayapti", ["o‘qiyapti", "o‘qidi", "o‘qiydi"], d=2, x="o‘qi-ma-yapti: -ma bor."),
    Q("Bo‘lishsiz fe’l qaysi qo‘shimcha bilan yasaladi?", "-ma", ["-mi", "-lar", "-da"], x="kel — kelma, yoz — yozma."),
    Q("O‘tgan zamon fe’li qaysi so‘roqqa javob beradi?", "nima qildi?", ["nima qilyapti?", "qanday?", "kim?"], x="keldi, yozdi — nima qildi?"),
    Q("Hozirgi zamon fe’li qaysi so‘roqqa javob beradi?", "nima qilyapti?", ["nima qildi?", "qanday?", "nechta?"], d=2, x="yozyapti — nima qilyapti?"),
    Q("Kelasi zamon fe’li qaysi so‘roqqa javob beradi?", "nima qiladi?", ["nima qildi?", "nima qilyapti?", "qanday?"], d=2,
      x="Ertaga boradi — nima qiladi?"),
    Q("“Men shifokor bo‘lmoqchiman.” gapidagi fe’l qaysi zamonda?", "Kelasi zamon", ["O‘tgan zamon", "Hozirgi zamon"], d=3,
      x="-moqchi niyatni, kelajakdagi harakatni bildiradi."),
    TF("“-di” qo‘shimchasi o‘tgan zamonni bildiradi.", True, x="yozdi, keldi, o‘qidi."),
    TF("“-yap” qo‘shimchasi kelasi zamonni bildiradi.", False, x="-yap hozirgi zamonni bildiradi: yozyapti."),
    TF("“bormadim” — bo‘lishsiz fe’l.", True, x="bor-ma-dim: -ma bor."),
    TF("“yozyapti” — bo‘lishsiz fe’l.", False, x="yozyapti — bo‘lishli; bo‘lishsizi — yozmayapti."),
    MATCH("Fe’lni bo‘lishsiz shakli bilan juftlang",
          [("yurdi", "yurmadi"), ("sakradi", "sakramadi"), ("uxlayapti", "uxlamayapti"), ("tinglaydi", "tinglamaydi"), ("aytdi", "aytmadi"), ("yuvyapti", "yuvmayapti")], d=2),
    ORDER("So‘zlardan gap tuzing", "Ertaga biz bog‘da daraxt ekamiz", d=2),
    ORDER("So‘zlardan gap tuzing", "Kecha men buvimga xat yozdim", d=2),
    ORDER("So‘zlardan gap tuzing", "Hozir ukam multfilm ko‘ryapti", d=1),
]
T.topic("verbs", "🏃", L("Fe’l zamonlari. Bo‘lishli va bo‘lishsiz fe’l", "Verb tenses and negation", "Времена глагола"), C3,
        "Fe’l harakatni bildiradi. Fe’l zamonlari:\n"
        "• O‘tgan zamon — nima qildi?: yozdi, bordik (kecha).\n"
        "• Hozirgi zamon — nima qilyapti?: yozyapti, o‘qimoqda (hozir).\n"
        "• Kelasi zamon — nima qiladi?: boramiz, o‘qimoqchi (ertaga).\n"
        "Bo‘lishsiz fe’l -ma qo‘shimchasi bilan yasaladi: keldi — kelmadi, yozyapti — yozmayapti.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["adjectives", "numerals", "pronouns", "verbs"], C3)

# ============================================================ 4-chorak
# ------------------------------------------------------------ gap bo‘laklari
SP4 = [  # gap, ega, kesim, ikkinchi darajali bo‘lak, boshqa so‘z
    ("Mushuk sichqonni tutdi.", "Mushuk", "tutdi", "sichqonni"), ("Zarina gullarga suv quydi.", "Zarina", "quydi", "gullarga"),
    ("Buvim bizga ertak aytdi.", "Buvim", "aytdi", "ertak"), ("Sinfimizga yangi o‘quvchi keldi.", "o‘quvchi", "keldi", "yangi"),
    ("Ukam har kuni erta uyg‘onadi.", "Ukam", "uyg‘onadi", "erta"), ("Tog‘dan sovuq shamol esdi.", "shamol", "esdi", "sovuq"),
    ("Dadam bog‘da olma ko‘chati ekdi.", "Dadam", "ekdi", "bog‘da"), ("Osmonda yorqin yulduzlar charaqladi.", "yulduzlar", "charaqladi", "yorqin"),
    ("Bobur chiroyli rasm chizdi.", "Bobur", "chizdi", "chiroyli"), ("Ertalab quyosh chiqdi.", "quyosh", "chiqdi", "Ertalab"),
]
items = []
for n, (sent, subj, pred, sec) in enumerate(SP4):
    items.append(Q(f"“{sent}” gapining egasini toping.", subj, [pred, sec], d=1 if n < 6 else 2, x=f"Kim? nima? — {subj}."))
    items.append(Q(f"“{sent}” gapining kesimini toping.", pred, [subj, sec], d=1 if n < 4 else 2, x=f"Ega haqida nima deyilgan? — {pred}."))
    if n % 2 == 1:
        items.append(Q(f"“{sent}” gapidagi qaysi so‘z ikkinchi darajali bo‘lak?", sec, [subj, pred], d=2,
                       x=f"“{sec}” bosh bo‘laklarni izohlaydi; {subj} — ega, {pred} — kesim."))
items += [
    Q("“Olmalar shirin.” gapining kesimi qaysi?", "shirin", ["Olmalar", "gapda kesim yo‘q"], d=3, x="Olmalar qanday? — shirin: kesim sifat bilan ifodalangan."),
    Q("“Bu daftar yangi.” gapining egasi qaysi?", "daftar", ["Bu", "yangi"], d=3, x="Nima yangi? — daftar."),
    Q("Gapning bosh bo‘laklari qaysilar?", "Ega va kesim", ["Ega va hol", "Kesim va aniqlovchi", "To‘ldiruvchi va hol"], x="Ega va kesim — gapning asosi."),
    Q("Ega qaysi so‘roqlarga javob beradi?", "kim? nima?", ["nima qildi?", "qanday?", "qayerda?"], x="Mushuk sichqonni tutdi: nima? — mushuk."),
    Q("Kesim qaysi so‘roqlarga javob beradi?", "nima qildi? nima qilyapti?", ["kim? nima?", "qayerda? qachon?", "kimning? nimaning?"], x="tutdi — nima qildi?"),
    Q("Ikkinchi darajali bo‘laklar qaysilar?", "To‘ldiruvchi, aniqlovchi, hol", ["Ega, kesim, hol", "Ega, aniqlovchi, undalma", "Kesim, to‘ldiruvchi, undalma"],
      d=2, x="Ikkinchi darajali bo‘laklar uchta: to‘ldiruvchi, aniqlovchi, hol."),
    TF("Ikkinchi darajali bo‘laklar bosh bo‘laklarni izohlab keladi.", True, d=2, x="Kichkina qiz gul terdi: kichkina — qiz so‘zini izohlaydi."),
    TF("Kesim ko‘pincha gapning boshida keladi.", False, x="O‘zbek tilida kesim ko‘pincha gap oxirida bo‘ladi."),
    MATCH("Gapni egasi bilan juftlang",
          [("Mushuk sichqonni tutdi", "mushuk"), ("Buvim ertak aytdi", "buvim"), ("Tog‘dan shamol esdi", "shamol"), ("Bobur rasm chizdi", "Bobur"),
           ("Ertalab quyosh chiqdi", "quyosh")], d=2),
    ORDER("So‘zlardan gap tuzing", "Kichkina qiz bog‘dan gul terdi", d=2),
    ORDER("So‘zlardan gap tuzing", "Opam menga kitob sovg‘a qildi", d=2),
]
T.topic("sentence_parts", "🏗️", L("Gap bo‘laklari", "Parts of a sentence", "Члены предложения"), C4,
        "Gap bo‘laklari — gapda biror so‘roqqa javob bo‘lib kelgan so‘zlar.\n"
        "• Bosh bo‘laklar: ega (kim? nima?) va kesim (nima qildi? qanday?).\n"
        "  Mushuk sichqonni tutdi: ega — mushuk, kesim — tutdi.\n"
        "• Ikkinchi darajali bo‘laklar — to‘ldiruvchi, aniqlovchi, hol. Ular bosh bo‘laklarni izohlaydi:\n"
        "  Kichkina (qanday?) qiz gul (nimani?) terdi. Kesim ko‘pincha gap oxirida keladi.", items=items)

# ------------------------------------------------------------ uyushiq bo‘laklar va undalma
HOMO4 = [
    ("Hovlida tovuqlar, o‘rdaklar va g‘ozlar yuribdi.", "tovuqlar, o‘rdaklar, g‘ozlar", ["hovlida, yuribdi", "tovuqlar, yuribdi"]),
    ("Hovlida Sardor, Jasur va Bobur futbol o‘ynashdi.", "Sardor, Jasur, Bobur", ["hovlida, futbol", "Bobur, o‘ynashdi"]),
    ("Men bahorni, yozni va kuzni yaxshi ko‘raman.", "bahorni, yozni, kuzni", ["men, yaxshi", "kuzni, ko‘raman"]),
    ("Savatda qizil, sariq, yashil olmalar bor.", "qizil, sariq, yashil", ["savatda, bor", "olmalar, bor"]),
    ("Opam kir yuvdi, dazmolladi va taxladi.", "yuvdi, dazmolladi, taxladi", ["opam, kir", "kir, taxladi"]),
    ("Bayramga buvim, bobom va amakim keldi.", "buvim, bobom, amakim", ["bayramga, keldi", "amakim, keldi"]),
]
VOC4 = [("Sardor, darsga kechikma.", "Sardor"), ("Ustoz, savol bersam maylimi?", "Ustoz"), ("Qadrli do‘stlar, sizni bayram bilan tabriklayman!", "Qadrli do‘stlar"),
        ("Buvijon, sizga gul olib keldim.", "Buvijon"), ("Sen, Laylo, ertaga navbatchisan.", "Laylo"), ("Rahmat sizga, dadajon.", "dadajon"),
        ("Quyosh, bizni isit!", "Quyosh"), ("Aziz o‘quvchilar, ta’til boshlandi.", "Aziz o‘quvchilar")]
items = []
for n, (sent, parts, wrong) in enumerate(HOMO4):
    items.append(Q(f"“{sent}” gapidagi uyushiq bo‘laklarni toping.", parts, wrong + ["uyushiq bo‘lak yo‘q"], d=1 if n < 4 else 2,
                   x=f"{parts} — bir xil so‘roqqa javob beradi va bir so‘zga bog‘lanadi."))
for n, (sent, voc) in enumerate(VOC4):
    words = [w.strip(",.!?") for w in sent.split()]
    rest = [w for w in words if w not in voc.split()]
    items.append(Q(f"“{sent}” gapida undalma qaysi?", voc, rnd.sample(rest, min(3, len(rest))), d=1 if n < 5 else 2,
                   x=f"{voc} — nutq qaratilgan {'narsa' if voc == 'Quyosh' else 'shaxs'}, vergul bilan ajratilgan."))
items += [
    Q("Qaysi gapda vergul to‘g‘ri qo‘yilgan?", "Qalam, daftar va chizg‘ich oldim.",
      ["Qalam daftar, va chizg‘ich oldim.", "Qalam, daftar, va chizg‘ich oldim.", "Qalam daftar va chizg‘ich, oldim."], x="Uyushiq bo‘laklar orasiga vergul qo‘yiladi, “va” oldidan qo‘yilmaydi."),
    Q("Qaysi gapda vergul to‘g‘ri qo‘yilgan?", "Uyimiz kichik, lekin shinam.",
      ["Uyimiz kichik lekin, shinam.", "Uyimiz, kichik lekin shinam.", "Uyimiz kichik lekin shinam,"], d=2, x="“lekin” oldidan vergul qo‘yiladi."),
    Q("Qaysi gapda undalma to‘g‘ri ajratilgan?", "Bugun, bolalar, ekskursiyaga boramiz.",
      ["Bugun bolalar, ekskursiyaga boramiz.", "Bugun, bolalar ekskursiyaga boramiz.", "Bugun bolalar ekskursiyaga, boramiz."], d=3,
      x="Gap o‘rtasidagi undalma ikki tomondan vergul bilan ajratiladi."),
    Q("Qaysi gapda undalma to‘g‘ri ajratilgan?", "Rahmat sizga, onajon.", ["Rahmat, sizga onajon.", "Rahmat sizga onajon,", "Rahmat, sizga, onajon."], d=2,
      x="Gap oxiridagi undalmadan oldin vergul qo‘yiladi."),
    Q("Qaysi gapda undalma to‘g‘ri ajratilgan?", "Jasur, oynani och.", ["Jasur oynani, och.", "Jasur, oynani, och.", "Jasur oynani och"],
      x="Gap boshidagi undalmadan keyin vergul qo‘yiladi."),
    Q("Uyushiq bo‘laklar orasida qaysi bog‘lovchi kelsa, vergul qo‘yilmaydi?", "va", ["lekin", "ammo", "biroq"], d=2, x="Olma va nok — vergulsiz."),
    Q("Undalma nimani bildiradi?", "Nutq qaratilgan shaxs yoki narsani", ["Harakatning vaqtini", "Narsaning belgisini", "Gapning egasini"],
      x="Sardor, darsga kechikma: nutq Sardorga qaratilgan."),
    TF("Uyushiq bo‘laklar bir xil so‘roqqa javob beradi.", True, x="nimalar? — tovuqlar, o‘rdaklar, g‘ozlar."),
    TF("“lekin”, “ammo” bog‘lovchilaridan oldin vergul qo‘yiladi.", True, d=2, x="Uy kichik, lekin shinam."),
    TF("Undalma faqat gapning boshida keladi.", False, x="Undalma gap o‘rtasida va oxirida ham keladi."),
    TF("Gap o‘rtasidagi undalma ikki tomondan vergul bilan ajratiladi.", True, d=2, x="Sen, Laylo, ertaga navbatchisan."),
]
T.topic("homogeneous_vocative", "📣", L("Uyushiq bo‘laklar va undalma", "Compound parts and direct address", "Однородные члены и обращение"), C4,
        "• Uyushiq bo‘laklar — bir xil so‘roqqa javob beradigan va bir so‘zga bog‘lanadigan bo‘laklar:\n"
        "  Hovlida tovuqlar, o‘rdaklar va g‘ozlar yuribdi. Ular orasiga vergul qo‘yiladi;\n"
        "  “va” oldidan vergul qo‘yilmaydi, “lekin”, “ammo” oldidan qo‘yiladi.\n"
        "• Undalma — nutq qaratilgan shaxs yoki narsa: Sardor, darsga kechikma. Undalma gap bo‘lagi emas.\n"
        "  Gap o‘rtasidagi undalma ikki tomondan vergul bilan ajratiladi: Sen, Laylo, ertaga navbatchisan.", items=items)

# ------------------------------------------------------------ gap turlari
ST = ["Darak gap", "So‘roq gap", "Buyruq gap", "His-hayajon gap"]
ST4 = [
    ("Kuzda barglar sarg‘ayadi.", 0), ("Siz qaysi sinfda o‘qiysiz?", 1), ("Kitobni ehtiyot qiling.", 2), ("Voy, qanday katta tarvuz!", 3),
    ("Buvim bizga palov damladi.", 0), ("Bu gullarni kim ekdi?", 1), ("Derazani ochib qo‘y.", 2), ("Ura, ta’til boshlandi!", 3),
    ("Kecha kutubxonadan kitob oldim.", 0), ("Kutubxona soat nechada ochiladi?", 1), ("Iltimos, sekinroq gapiring.", 2), ("Qanday go‘zal kun!", 3),
    ("Men rasm chizishni yaxshi ko‘raman.", 0), ("Uy vazifasini bajardingmi?", 1), ("Ukangga yordam ber.", 2), ("Oh, bu gullar qanchalar xushbo‘y!", 3),
    ("Bizning sinfda o‘ttiz nafar o‘quvchi bor.", 0), ("Ertaga havo qanday bo‘ladi?", 1), ("Stolni artib qo‘ying.", 2), ("Qoyil, zo‘r javob berding!", 3),
]
ST_WHY = ["Darak gap xabar beradi, oxirida nuqta.", "So‘roq gap savol bildiradi, oxirida so‘roq belgisi.",
          "Buyruq gap buyruq yoki iltimos bildiradi.", "Kuchli his bilan aytilgan, oxirida undov belgisi."]
items = []
for n, (sent, k) in enumerate(ST4):
    wrong = ["So‘roq gap", "Buyruq gap"] if k == 3 else others(ST, ST[k])
    items.append(Q(f"Bu qanday gap: “{sent}”", ST[k], wrong, d=1 if n < 12 else 2, x=ST_WHY[k]))
for n, (sent, k) in enumerate([(s, k) for s, k in ST4 if k != 2][:6]):
    bare = sent.rstrip(".?!")
    mark = [".", "?", None, "!"][k]
    items.append(Q(f"Gap oxiriga qaysi belgi qo‘yiladi: “{bare}…”", mark, [m for m in (".", "?", "!", ",") if m != mark], d=2, x=ST_WHY[k]))
items += [
    Q("Qaysi gap so‘roq gap?", "Siz qachon qaytasiz?", ["Biz uyga qaytdik.", "Tezroq qayting.", "Voy, qanday yaxshi!"], x="Savol bildiradi, oxirida so‘roq belgisi."),
    Q("Qaysi gap buyruq gap?", "Chiroqni o‘chir.", ["Chiroq yondi.", "Chiroq yoniqmi?", "Voh, qanday yorug‘!"], x="Buyruq bildiradi."),
    Q("Qaysi gap his-hayajon gap?", "Voh, qanday chiroyli qor!", ["Qor yog‘di.", "Qor yog‘yaptimi?", "Yo‘lakdagi qorni tozalang."], x="Kuchli his bilan aytilgan."),
    Q("Qaysi gap darak gap?", "Qishda kunlar qisqa bo‘ladi.", ["Qishda kunlar qisqami?", "Issiq kiyining.", "Voy, qanday sovuq!"], x="Xabar beradi."),
    Q("Qaysi yuklama gapga so‘roq ma’nosini beradi?", "-mi", ["-lar", "-ni", "-da"], x="Bajardingmi? Kelasanmi?"),
    TF("His-hayajon gap oxiriga undov belgisi qo‘yiladi.", True, x="Ura, ta’til boshlandi!"),
    TF("So‘roq gap nuqta bilan tugaydi.", False, x="So‘roq gap so‘roq belgisi bilan tugaydi."),
    TF("Buyruq gap iltimosni ham bildirishi mumkin.", True, d=2, x="Iltimos, sekinroq gapiring."),
    ORDER("So‘zlardan so‘roq gap tuzing", "Sen qaysi kitobni o‘qiyapsan", d=2, x="Sen qaysi kitobni o‘qiyapsan?"),
    ORDER("So‘zlardan so‘roq gap tuzing", "Kutubxona qachon ochiladi", d=2, x="Kutubxona qachon ochiladi?"),
]
T.topic("sentence_types", "💬", L("Gap turlari", "Types of sentences", "Виды предложений"), C4,
        "Maqsadiga ko‘ra gaplar:\n"
        "• Darak gap — xabar beradi: Kuzda barglar sarg‘ayadi.\n"
        "• So‘roq gap — savol bildiradi, so‘roq so‘zlari yoki -mi yordamida tuziladi: Siz qaysi sinfda o‘qiysiz?\n"
        "• Buyruq gap — buyruq, maslahat yoki iltimos bildiradi: Kitobni ehtiyot qiling.\n"
        "His-hayajon bilan aytilgan gap oxiriga undov belgisi qo‘yiladi: Voy, qanday katta tarvuz!", items=items)

# ------------------------------------------------------------ matn va reja
TXT_AUTUMN = ("Kuz keldi. Daraxtlarning barglari sarg‘ayib, to‘kila boshladi. Bog‘larda olma va anorlar pishdi. "
              "Dalada paxta terimi boshlandi. Qushlar issiq o‘lkalarga uchib ketmoqda.")
TXT_PUPPY = ("Bir kuni ukam Sardor ko‘chadan kichkina kuchukcha topib keldi. Kuchukcha och va sovqotgan edi. "
             "Biz unga sut berdik va issiq joy tayyorladik. Samarqand — qadimiy shahar. Endi kuchukcha bizning eng yaqin do‘stimiz.")
TXT_MORNING = ("Ertalab soat yettida uyg‘ondim. Yuz-qo‘limni yuvib, nonushta qildim. Keyin sumkamni olib, maktabga yo‘l oldim. "
               "Darsda yangi mavzuni o‘rgandik.")
TXT_CLASS = ("Bizning sinfxonamiz keng va yorug‘. Uning derazalari katta, ulardan quyosh nuri tushib turadi. "
             "Devorlarda rasmlar va xaritalar osilgan. Partalar tartib bilan terilgan.")
TXT_BOOKS = ("Kitob o‘qish juda foydali. Chunki kitob bizga yangi bilimlar beradi. U nutqimizni boyitadi va xayolimizni o‘stiradi. "
             "Shuning uchun har kuni kitob o‘qish kerak.")
items = [
    Q("Matnga mos sarlavhani tanlang.", "Oltin kuz", ["Qishki o‘yinlar", "Bahor bayrami", "Mening mushugim"], text=TXT_AUTUMN, e="🍂",
      x="Matnda kuz fasli haqida gap boradi."),
    Q("Matnning mavzusi nima?", "Kuz fasli", ["Qish fasli", "Maktab hayoti", "Uy hayvonlari"], text=TXT_AUTUMN, e="🍂", x="Hamma gaplar kuz haqida."),
    Q("Matnda nechta gap bor?", "5 ta", ["4 ta", "6 ta", "3 ta"], d=2, text=TXT_AUTUMN, e="🍂", x="Har bir gap nuqta bilan tugagan: 5 ta."),
    Q("Qaysi gap matnga aloqador emas?", "Samarqand — qadimiy shahar.", ["Kuchukcha och va sovqotgan edi.", "Biz unga sut berdik va issiq joy tayyorladik.",
                                                                          "Endi kuchukcha bizning eng yaqin do‘stimiz."],
      text=TXT_PUPPY, e="🐶", x="Matn kuchukcha haqida; shahar haqidagi gap mavzuga aloqasiz."),
    Q("Matnga mos sarlavhani tanlang.", "Kichkina do‘st", ["Qadimiy shahar", "Yozgi ta’til", "Bizning maktab"], text=TXT_PUPPY, e="🐶",
      x="Matn topib olingan kuchukcha haqida."),
    Q("Matnning asosiy fikri qaysi?", "Hayvonlarga mehribon bo‘lish kerak", ["Kuchukchalar sut ichmaydi", "Ko‘chada o‘ynash kerak", "Shaharlar qadimiy bo‘ladi"],
      d=2, text=TXT_PUPPY, e="🐶", x="Bolalar och kuchukchaga g‘amxo‘rlik qilishdi."),
    Q("Matn rejasining to‘g‘ri tartibini toping.", "Uyg‘onish → Nonushta → Maktabga yo‘l → Dars",
      ["Nonushta → Uyg‘onish → Dars → Maktabga yo‘l", "Dars → Maktabga yo‘l → Nonushta → Uyg‘onish", "Uyg‘onish → Dars → Nonushta → Maktabga yo‘l"],
      d=2, text=TXT_MORNING, e="⏰", x="Reja bandlari matndagi voqealar tartibida bo‘ladi."),
    Q("Matnda voqealar qanday tartibda berilgan?", "Bo‘lib o‘tgan vaqt tartibida", ["Tartibsiz", "Oxiridan boshiga", "Faqat bitta voqea bor"],
      d=2, text=TXT_MORNING, e="⏰", x="Avval uyg‘ondi, keyin nonushta qildi, so‘ng maktabga bordi."),
    Q("Matnga mos sarlavhani tanlang.", "Bizning sinfxonamiz", ["Yozgi ta’til", "Mening do‘stim", "Oltin kuz"], text=TXT_CLASS, e="🏫",
      x="Matnda sinfxona tasvirlangan."),
    Q("Bu matnda nima tasvirlangan?", "Sinfxonaning ko‘rinishi", ["Sayohat voqeasi", "Dars jadvali", "O‘yin qoidalari"], text=TXT_CLASS, e="🏫",
      x="Matn sinfxona qanday ekanini ko‘rsatadi."),
    Q("Bu matn qaysi turga kiradi?", "Tasviriy matn", ["Hikoya matn", "Muhokama matn"], d=3, text=TXT_CLASS, e="🏫",
      x="Matnda voqea emas, narsaning qanday ekani tasvirlangan."),
    Q("Matnning asosiy fikri qaysi?", "Har kuni kitob o‘qish kerak", ["Kitoblar qimmat turadi", "Kitobni faqat maktabda o‘qish mumkin", "Kitob o‘qish zerikarli"],
      text=TXT_BOOKS, e="📚", x="Xulosa gapda asosiy fikr aytilgan."),
    Q("Qaysi gap matnning xulosasi?", "Shuning uchun har kuni kitob o‘qish kerak.", ["Kitob o‘qish juda foydali.", "Chunki kitob bizga yangi bilimlar beradi.",
                                                                                     "U nutqimizni boyitadi va xayolimizni o‘stiradi."],
      d=2, text=TXT_BOOKS, e="📚", x="Xulosa matn oxirida keladi va fikrni yakunlaydi."),
    Q("Bu matn qaysi turga kiradi?", "Muhokama matn", ["Hikoya matn", "Tasviriy matn"], d=3, text=TXT_BOOKS, e="📚",
      x="Matnda fikr aytilib, “chunki” bilan isbotlangan va xulosa chiqarilgan."),
    Q("Matn nima?", "Mazmunan bog‘langan gaplar", ["Bir-biriga aloqasiz gaplar", "Alohida so‘zlar ro‘yxati", "Faqat bitta so‘z"],
      x="Matndagi gaplar bir mavzuga bog‘langan bo‘ladi."),
    Q("Reja nima uchun tuziladi?", "Fikrni tartib bilan bayon qilish uchun", ["Harflarni o‘rganish uchun", "So‘zlarni sanash uchun", "Matnni qisqartirmaslik uchun"],
      x="Reja matn qismlarining tartibini ko‘rsatadi."),
    Q("Matn odatda qanday qismlardan iborat bo‘ladi?", "Kirish, asosiy qism, xulosa", ["Ega, kesim, hol", "O‘zak va qo‘shimcha", "Unli va undosh"],
      x="Kirish — boshlanish, asosiy qism — voqea yoki fikr, xulosa — yakun."),
    Q("Sarlavha nimani ko‘rsatadi?", "Matnning mavzusi yoki asosiy fikrini", ["Matndagi gaplar sonini", "Muallifning yoshini", "Matndagi eng uzun so‘zni"],
      x="Sarlavhani o‘qib, matn nima haqida ekanini bilish mumkin."),
    TF("Matndagi gaplar bir mavzuga bog‘langan bo‘ladi.", True, x="Aloqasiz gap matnni buzadi."),
    TF("Matnning har bir gapi boshqa-boshqa mavzuda bo‘lishi kerak.", False, x="Matndagi gaplar bir mavzuga bog‘lanadi."),
    TF("Xulosa qismi matnning oxirida keladi.", True, x="Xulosa fikrni yakunlaydi."),
]
T.topic("text_plan", "📖", L("Matn va reja", "Text and outline", "Текст и план"), C4,
        "Matn — bir mavzuga bog‘langan, ma’no jihatdan izchil gaplar.\n"
        "• Sarlavha matnning mavzusi yoki asosiy fikrini ko‘rsatadi.\n"
        "• Matn qismlari: kirish, asosiy qism, xulosa.\n"
        "• Reja — matn qismlarining tartibli ro‘yxati; u fikrni tartib bilan bayon qilishga yordam beradi.\n"
        "• Matn turlari: hikoya (voqea), tasvir (narsa qanday ekani), muhokama (fikr va uning sababi).", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["sentence_parts", "homogeneous_vocative", "sentence_types", "text_plan"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["sounds_letters", "hyphenation", "word_structure", "nouns", "possessive", "cases", "suffix_spelling", "adjectives", "numerals",
        "pronouns", "verbs", "sentence_parts", "homogeneous_vocative", "sentence_types", "text_plan"], C4, level=3)

T.write()
