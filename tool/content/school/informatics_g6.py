"""Informatika va axborot texnologiyalari, 6-sinf: assets/data/school/informatics_g6.json va bank_informatics_g6.json.

Mavzular O‘zbekiston 6-sinf informatika dasturi yo‘nalishida: axborot o‘lchovi, ikkilik, sakkizlik va o‘n oltilik sanoq sistemalari,
mantiqiy amallar, elektron jadval (katak manzili, formulalar, SUM/AVERAGE/MAX/MIN), matn muharriri (jadval, rasm, ro‘yxat),
taqdimot, algoritm turlari va blok-sxema, Scratch, dastur natijasini aniqlash, tarmoq va internet, kiberxavfsizlik, mualliflik huquqi.
Qoida va savollar matni — o‘zimizniki (darslikdan ko‘chirilmagan).
HAMMA hisoblar Python’da: sanoq sistemalari — bin()/oct()/hex()/int(), jadval formulalari — kichik baholovchi,
psevdokod natijalari — psevdokodni Python’ga o‘girib bajarish orqali, IP-manzillar — ipaddress moduli bilan.
Maktab kelishuvi: 1 KB = 1024 bayt, 1 MB = 1024 KB va hokazo.
Qayta yaratish: python3 tool/content/school/informatics_g6.py
"""
import ipaddress
import os
import re
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("informatics", 6, L("Informatika va axborot texnologiyalari", "Computer science and IT", "Информатика и ИТ"))

C1 = "1-chorak. Axborot, sanoq sistemalari va mantiq"
C2 = "2-chorak. Elektron jadval va ofis dasturlari"
C3 = "3-chorak. Algoritmlar va dasturlash"
C4 = "4-chorak. Tarmoq, xavfsizlik va huquq"

S = "So‘zlardan gap tuzing"


def near(ans, cands, k=4, lo=0):
    """Sonli javob uchun noto'g'ri variantlar: takrorsiz, javobdan farqli, `lo` dan kichik emas."""
    out = []
    for c in cands:
        if c != ans and c >= lo and c not in out:
            out.append(c)
    return out[:k]


def uniq(ans, cands, k=4):
    out = []
    for c in cands:
        if c != ans and c not in out:
            out.append(c)
    return out[:k]


def fmt(n):
    return f"{n:,}".replace(",", " ") if n >= 10000 else str(n)


def b2(n):
    return bin(n)[2:]


def places(s):
    k = len(s)
    return [str(2 ** (k - 1 - i)) for i, ch in enumerate(s) if ch == "1"]


# ============================================================ 1-chorak
_units = []
for n, d in [(5, 1), (12, 2)]:
    _units.append(Q(f"{n} bayt necha bitga teng?", f"{n * 8} bit", [f"{v} bit" for v in near(n * 8, [n, n * 10, n * 1024, n * 4])], d=d,
                    x=f"1 bayt = 8 bit: {n} · 8 = {n * 8} bit."))
for bits, d in [(64, 1), (256, 2)]:
    _units.append(Q(f"{bits} bit necha baytga teng?", f"{bits // 8} bayt", [f"{v} bayt" for v in near(bits // 8, [bits * 8, bits // 2, bits, bits // 10])], d=d,
                    x=f"8 bit = 1 bayt: {bits} : 8 = {bits // 8} bayt."))
for n, a, b, d in [(3, "KB", "bayt", 2), (2, "MB", "KB", 1), (4, "GB", "MB", 2), (5, "TB", "GB", 3)]:
    v = n * 1024
    _units.append(Q(f"{n} {a} necha {b + ' ga' if b.isupper() else b + 'ga'} teng?", f"{fmt(v)} {b}", [f"{fmt(w)} {b}" for w in near(v, [n * 1000, n * 100, n * 8, n * 1024 * 8])], d=d,
                    x=f"1 {a} = 1024 {b}: {n} · 1024 = {fmt(v)} {b}."))
_units.append(Q("1 KB necha bitga teng?", f"{fmt(1024 * 8)} bit", [f"{fmt(v)} bit" for v in [1024, 8000, 1000]], d=3,
                x=f"1 KB = 1024 bayt = 1024 · 8 = {fmt(1024 * 8)} bit."))
for i, d in [(3, 2), (4, 2), (8, 3)]:
    n = 2 ** i
    _units.append(Q(f"{i} bit yordamida nechta turli kod (qiymat) hosil qilish mumkin?", n, near(n, [i * 2, i, n * 2, n // 2, i * i]), d=d,
                    x=f"Har bir bit 2 xil: 2 ni {i} marta ko‘paytiramiz — 2^{i} = {n}.".replace("^", "")
                    if False else f"Har bir bit 0 yoki 1: 2 ni {i} marta ko‘paytiramiz — {' · '.join(['2'] * i)} = {n}."))
for n, d in [(32, 3), (16, 2)]:
    i = n.bit_length() - 1
    assert 2 ** i == n
    _units.append(Q(f"{n} ta turli belgini kodlash uchun kamida necha bit kerak?", i, near(i, [n // 2, i + 1, i - 1, 8]), d=d,
                    x=f"{' · '.join(['2'] * i)} = {n}, demak {i} bit yetadi."))
for size, fl, d in [(256, 1, 2), (512, 2, 3)]:
    cnt = fl * 1024 // size
    _units.append(Q(f"Fleshka hajmi {fl} GB. Unga {size} MB lik videofayldan nechta sig‘adi?", cnt, near(cnt, [fl * 1000 // size, cnt + 1, cnt * 2, cnt - 1], lo=1), d=d,
                    x=f"{fl} GB = {fl * 1024} MB: {fl * 1024} : {size} = {cnt}."))
_cmp = {"3 KB": 3 * 1024, "3000 bayt": 3000, "24 000 bit": 24000 // 8, "2 KB": 2048}
_best = max(_cmp, key=_cmp.get)
_units.append(Q("Qaysi axborot hajmi eng katta?", _best, [k for k in _cmp if k != _best], d=3,
                x="Hammasini baytga o‘tkazamiz: " + ", ".join(f"{k} = {fmt(v)} bayt" for k, v in _cmp.items()) + "."))
for chars, bpc, d in [(2048, 1, 2), (1024, 2, 3)]:
    kb = chars * bpc // 1024
    _units.append(Q(f"Matnda {fmt(chars)} ta belgi bor, har bir belgi {bpc} bayt bilan kodlangan. Matn hajmi necha KB?", f"{kb} KB",
                    [f"{v} KB" for v in near(kb, [chars * bpc // 1000 + 1, kb * 8, kb * 2, kb + 1], lo=1)], d=d,
                    x=f"{fmt(chars)} · {bpc} = {fmt(chars * bpc)} bayt = {fmt(chars * bpc)} : 1024 = {kb} KB."))

T.topic("olchov", "📏", L("Axborot va uni o‘lchash", "Measuring information", "Измерение информации"),
        chapter=C1,
        theory="Kompyuter axborotni ikkilik kodda — 0 va 1 bilan saqlaydi. Bitta 0 yoki 1 — 1 bit, eng kichik o‘lchov birligi.\n"
               "• 1 bayt = 8 bit; 1 KB = 1024 bayt; 1 MB = 1024 KB; 1 GB = 1024 MB; 1 TB = 1024 GB.\n"
               "• Kichik birlikdan kattasiga o‘tishda bo‘linadi, kattasidan kichigiga o‘tishda ko‘paytiriladi: 3 KB = 3 · 1024 = 3072 bayt.\n"
               "• i bit bilan 2 · 2 · … · 2 (i marta) turli kod hosil bo‘ladi: 3 bit — 8 ta, 8 bit — 256 ta kod.\n"
               "Oddiy kodlashda har bir belgi 1 bayt joy egallaydi.",
        items=[
            Q("1 bit qanday qiymatlardan birini oladi?", "0 yoki 1", ["0 dan 9 gacha", "A dan Z gacha", "Faqat 1"],
              x="Bit — ikkilik raqam: 0 yoki 1."),
            Q("1 bayt necha bitdan iborat?", "8", ["2", "10", "1024"],
              x="1 bayt = 8 bit."),
            Q("Qaysi birlik eng katta?", "Terabayt", ["Gigabayt", "Megabayt", "Kilobayt"],
              x="Bit < bayt < KB < MB < GB < TB."),
            Q("Qaysi birlik eng kichik?", "Bit", ["Bayt", "Kilobayt", "Gigabayt"],
              x="Bit — axborotning eng kichik birligi."),
            TF("1 KB = 1024 bayt.", True, x="Informatikada 1 KB = 2 ning 10-darajasi = 1024 bayt deb olinadi."),
            TF("1 MB 1 GB dan katta.", False, x="1 GB = 1024 MB, ya’ni GB kattaroq."),
            ORDER(S, "Bir bayt sakkiz bitdan iborat"),
            MATCH("Birlikni qiymati bilan juftlang",
                  [("1 bayt", "8 bit"), ("1 KB", "1024 bayt"), ("1 MB", "1024 KB"), ("1 GB", "1024 MB"), ("1 TB", "1024 GB")], d=2,
                  x="Har bir keyingi birlik oldingisidan 1024 marta katta (bayt esa bitdan 8 marta)."),
        ] + _units)

_bin = []
for n, d in [(9, 1), (12, 1), (21, 2), (37, 2), (64, 2), (100, 3), (127, 3), (200, 3)]:
    s = b2(n)
    cands = [b2(n + 1), b2(n - 1), s[::-1], b2(n * 2), b2(n ^ 2), b2(n ^ 4)]
    _bin.append(Q(f"O‘nlik sistemadagi {n} sonini ikkilik sistemada yozing.", s, uniq(s, [c for c in cands if not c.startswith("0")]), d=d,
                  x=f"{n} = {' + '.join(places(s))} → {s}."))
    assert int(s, 2) == n
for s, d in [("1010", 1), ("1111", 1), ("10011", 2), ("101010", 2), ("1000000", 2), ("11001000", 3), ("11111111", 3)]:
    n = int(s, 2)
    cands = [n + 1, n - 1, int(s[::-1], 2), int(s) if int(s) < 1000 else n * 2, n + 2, n // 2]
    _bin.append(Q(f"Ikkilik sistemadagi {s} sonini o‘nlik sistemaga o‘tkazing.", n, near(n, cands), d=d,
                  x=f"{s} = {' + '.join(places(s))} = {n}."))
for a, b, d in [("101", "11", 3), ("1010", "101", 3), ("111", "1", 3)]:
    r = b2(int(a, 2) + int(b, 2))
    cands = [b2(int(a, 2) + int(b, 2) + 1), b2(int(a, 2) + int(b, 2) - 1), str(int(a) + int(b)), r[::-1], b2(int(a, 2) * int(b, 2))]
    _bin.append(Q(f"Ikkilik sistemada qo‘shing: {a} + {b}.", r, uniq(r, [c for c in cands if set(c) <= set("01")]), d=d,
                  x=f"{a} = {int(a, 2)}, {b} = {int(b, 2)}, yig‘indi {int(a, 2) + int(b, 2)} = {r}."))
for n, d in [(100, 3), (30, 2)]:
    k = len(b2(n))
    _bin.append(Q(f"{n} soni ikkilik sistemada necha xonali son bo‘ladi?", k, near(k, [k + 1, k - 1, len(str(n)), 8], lo=1), d=d,
                  x=f"{n} = {b2(n)} — {k} ta raqam."))
_pairs = [("1100", "1011"), ("100000", "11111")]
for a, b in _pairs:
    big = a if int(a, 2) > int(b, 2) else b
    _bin.append(Q(f"Qaysi ikkilik son katta: {a} yoki {b}?", big, [v for v in [a, b, "Ular teng"] if v != big] + ["Taqqoslab bo‘lmaydi"], d=2,
                  x=f"{a} = {int(a, 2)}, {b} = {int(b, 2)}."))
_bin.append(Q("8 xonali eng katta ikkilik son 11111111 o‘nlikda nechaga teng?", int("11111111", 2), [256, 128, 8, 11111111], d=2,
              x=f"128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = {int('11111111', 2)}."))
_bin.append(Q("8 bit bilan 0 dan boshlab nechta turli son yozish mumkin?", 2 ** 8, [255, 8, 128, 16], d=3,
              x=f"0 dan 255 gacha — jami {2 ** 8} ta son."))

_ex = "1011"
T.topic("ikkilik", "🔢", L("Ikkilik sanoq sistemasi (0–255)", "Binary numbers (0–255)", "Двоичная система (0–255)"),
        chapter=C1,
        theory="Ikkilik sistemada faqat ikki raqam bor: 0 va 1. Xona qiymatlari o‘ngdan chapga: 1, 2, 4, 8, 16, 32, 64, 128.\n"
               f"• Ikkilikdan o‘nlikka: 1 turgan xonalar qiymatlari qo‘shiladi: {_ex} = {' + '.join(places(_ex))} = {int(_ex, 2)}.\n"
               f"• O‘nlikdan ikkilikka: sonni xona qiymatlari yig‘indisiga ajratamiz: 200 = {' + '.join(places(b2(200)))} → {b2(200)}.\n"
               "• 8 bit (1 bayt) bilan 0 dan 255 gacha sonlar yoziladi: 255 = 11111111.\n"
               "Ikkilikda qo‘shish: 0 + 0 = 0, 0 + 1 = 1, 1 + 1 = 10 (0 yoziladi, 1 keyingi xonaga o‘tadi).",
        items=[
            Q("Ikkilik sanoq sistemasida nechta raqam bor?", "2", ["8", "10", "16"], x="Faqat 0 va 1."),
            Q("Ikkilik sonning o‘ngdan 4-xonasi qiymati nechaga teng?", "8", ["4", "16", "3"], d=2, x="Xona qiymatlari: 1, 2, 4, 8 — to‘rtinchisi 8."),
            TF("Ikkilik son 0 bilan tugasa, u juft son.", True, d=2, x="Oxirgi xona qiymati 1; u 0 bo‘lsa, son 2 ga bo‘linadi."),
            TF("Ikkilik sistemada 2 raqami ishlatiladi.", False, x="Ikkilik sistemada faqat 0 va 1 bor."),
            MATCH("O‘nlik sonni ikkilik yozuvi bilan juftlang", [(str(n), b2(n)) for n in (2, 5, 8, 10, 15, 16)], d=2,
                  x="Har bir sonni xona qiymatlari 1, 2, 4, 8, 16 yig‘indisiga ajratib tekshiring."),
            ORDER(S, "Kompyuter sonlarni ikkilik sistemada saqlaydi"),
        ] + _bin)

_base = []
for s, d in [("17", 1), ("25", 2), ("100", 2), ("777", 3)]:
    n = int(s, 8)
    _base.append(Q(f"Sakkizlik sistemadagi {s} sonini o‘nlik sistemaga o‘tkazing.", n, near(n, [int(s), n + 1, n - 1, int(s, 16), n + 8]), d=d,
                   x=" + ".join(f"{ch} · {8 ** (len(s) - 1 - i)}" for i, ch in enumerate(s)) + f" = {n}."))
for n, d in [(10, 1), (64, 2), (30, 3)]:
    s = oct(n)[2:]
    _base.append(Q(f"O‘nlik sistemadagi {n} sonini sakkizlik sistemada yozing.", s, uniq(s, [c for c in [oct(n + 1)[2:], oct(n - 1)[2:], str(n), s[::-1], hex(n)[2:].upper(), oct(n + 2)[2:]] if not c.startswith("0")]), d=d,
                   x=f"{n} = " + " + ".join(f"{ch} · {8 ** (len(s) - 1 - i)}" for i, ch in enumerate(s)) + f" → {s}."))
for s, d in [("A", 1), ("D", 1), ("1A", 2), ("20", 2), ("FF", 3)]:
    n = int(s, 16)
    _base.append(Q(f"O‘n oltilik sistemadagi {s} sonini o‘nlik sistemaga o‘tkazing.", n,
                   near(n, [n + 1, n - 1, int(s) if s.isdigit() else n + 10, int(s, 8) if all(c in "01234567" for c in s) else n - 10, n + 16]), d=d,
                   x=(" + ".join(f"{int(ch, 16)} · {16 ** (len(s) - 1 - i)}" for i, ch in enumerate(s)) + f" = {n}.") if len(s) > 1 else f"{s} = {n}."))
for n, d in [(11, 1), (16, 2), (31, 2), (255, 3)]:
    s = format(n, "X")
    _base.append(Q(f"O‘nlik sistemadagi {n} sonini o‘n oltilik sistemada yozing.", s,
                   uniq(s, [c for c in [format(n + 1, "X"), format(n - 1, "X"), str(n), s[::-1] if len(s) > 1 else "A", oct(n)[2:], format(n + 2, "X")] if not c.startswith("0")]), d=d,
                   x=f"{n} = " + (" + ".join(f"{int(ch, 16)} · {16 ** (len(s) - 1 - i)}" for i, ch in enumerate(s))) + f" → {s}."))
for s, d in [("1111", 2), ("10100101", 3)]:
    h = format(int(s, 2), "X")
    _base.append(Q(f"Ikkilik {s} sonini o‘n oltilik sistemada yozing.", h, uniq(h, [format(int(s, 2) + 1, "X"), h[::-1] if len(h) > 1 else "E", str(int(s, 2)), "1F"]), d=d,
                   x="4 tadan guruhlaymiz: " + " ".join(s[i:i + 4] for i in range(0, len(s), 4)) + f" → {h}."))
for s, d in [("101110", 3)]:
    o = oct(int(s, 2))[2:]
    _base.append(Q(f"Ikkilik {s} sonini sakkizlik sistemada yozing.", o, uniq(o, [o[::-1], str(int(s, 2)), format(int(s, 2), "X"), oct(int(s, 2) + 1)[2:]]), d=d,
                   x="3 tadan guruhlaymiz: " + " ".join(s[i:i + 3] for i in range(0, len(s), 3)) + f" → {o}."))
_oct_opts = ["128", "127", "70", "12"]
_bad = [s for s in _oct_opts if any(ch not in "01234567" for ch in s)]
assert _bad == ["128"]
_base.append(Q("Qaysi yozuv sakkizlik sistemadagi son bo‘la olmaydi?", "128", ["127", "70", "12"], d=2,
               x="Sakkizlik sistemada 8 va 9 raqamlari yo‘q, 0–7 raqamlar ishlatiladi."))
assert int("FF0000"[:2], 16) == 255 and int("FF0000"[2:4], 16) == 0

T.topic("sanoq", "🔣", L("Sakkizlik va o‘n oltilik sanoq sistemalari", "Octal and hexadecimal numbers", "Восьмеричная и шестнадцатеричная системы"),
        chapter=C1,
        theory="Sanoq sistemasi asosi — undagi raqamlar soni.\n"
               "• Sakkizlik sistemada 8 ta raqam: 0–7. Xona qiymatlari: 1, 8, 64. Masalan, 17 = 1 · 8 + 7 = 15.\n"
               "• O‘n oltilik sistemada 16 ta raqam: 0–9 va A = 10, B = 11, C = 12, D = 13, E = 14, F = 15. Xona qiymatlari: 1, 16, 256. Masalan, 1A = 1 · 16 + 10 = 26.\n"
               "• Ikkilik son 3 tadan guruhlansa — sakkizlik, 4 tadan guruhlansa — o‘n oltilik raqamlar hosil bo‘ladi: 1111 = F.\n"
               "Veb-sahifa ranglari o‘n oltilik kod bilan yoziladi: #FF0000 — qizil, #FFFFFF — oq, #000000 — qora.",
        items=[
            Q("Sakkizlik sistemada nechta raqam bor?", "8", ["7", "10", "16"], x="0, 1, 2, 3, 4, 5, 6, 7 — jami 8 ta."),
            Q("O‘n oltilik sistemada F raqami o‘nlikda nechaga teng?", str(int("F", 16)), ["16", "6", "14"], x="A = 10, B = 11, …, F = 15."),
            Q("O‘n oltilik sistemada C raqami o‘nlikda nechaga teng?", str(int("C", 16)), ["3", "13", "11"], x="A = 10, B = 11, C = 12."),
            Q("Qaysi sanoq sistemasida A, B, C, D, E, F harflari raqam sifatida ishlatiladi?", "O‘n oltilik", ["Sakkizlik", "Ikkilik", "O‘nlik"],
              x="O‘n oltilik sistemaga 10 dan 15 gacha raqamlar uchun harflar kerak."),
            TF("Sakkizlik sistemada 9 raqami bor.", False, x="Sakkizlik raqamlari faqat 0 dan 7 gacha."),
            TF("Bitta o‘n oltilik raqam 4 ta ikkilik raqamga (bitga) mos keladi.", True, d=2, x="16 = 2 · 2 · 2 · 2, shuning uchun 4 bit."),
            Q("Veb-sahifada #FF0000 kodi qaysi rangni bildiradi?", "Qizil", ["Yashil", "Ko‘k", "Oq"], d=3,
              x=f"Kod uch qismdan iborat: qizil FF = {int('FF', 16)}, yashil 00, ko‘k 00 — faqat qizil yonadi."),
            Q("Veb-sahifada #FFFFFF kodi qaysi rangni bildiradi?", "Oq", ["Qora", "Qizil", "Kulrang"], d=3,
              x="Uchala rang ham eng yorqin — oq rang hosil bo‘ladi."),
            ORDER(S, "O‘n oltilik sistemada o‘n olti raqam bor"),
            MATCH("O‘n oltilik raqamni o‘nlikdagi qiymati bilan juftlang",
                  [("A", "10"), ("B", "11"), ("C", "12"), ("D", "13"), ("E", "14"), ("F", "15")], d=2,
                  x="O‘n oltilik sistemada 10–15 sonlari harflar bilan yoziladi."),
        ] + _base)
for h, n in [("A", 10), ("B", 11), ("C", 12), ("D", 13), ("E", 14), ("F", 15)]:
    assert int(h, 16) == n

# --- Mantiq: barcha qiymatlar Python'da hisoblanadi.
TXT = {True: "Rost", False: "Yolg‘on"}
_log = []
for a, b, op, d in [(1, 0, "VA", 1), (1, 1, "VA", 1), (0, 1, "YOKI", 1), (0, 0, "YOKI", 1), (1, 0, "YOKI", 2), (0, 0, "VA", 2)]:
    r = int((a and b) if op == "VA" else (a or b))
    _log.append(Q(f"A = {a}, B = {b}. “A {op} B” ning qiymati nechaga teng?", str(r), [str(1 - r), "2", "10"], d=d,
                  x=("VA faqat ikkalasi 1 bo‘lsa 1 beradi." if op == "VA" else "YOKI kamida bittasi 1 bo‘lsa 1 beradi.") + f" Javob: {r}."))
for a, d in [(1, 1), (0, 2)]:
    _log.append(Q(f"A = {a}. “EMAS A” ning qiymati nechaga teng?", str(1 - a), [str(a), "2", "−1"], d=d, x="EMAS qiymatni teskarisiga almashtiradi."))
_exprs = [("(7 > 3) VA (2 > 5)", (7 > 3) and (2 > 5), 1), ("(7 > 3) YOKI (2 > 5)", (7 > 3) or (2 > 5), 1), ("EMAS (4 = 4)", not (4 == 4), 2),
          ("(10 < 5) YOKI (3 = 4)", (10 < 5) or (3 == 4), 2), ("EMAS (5 > 8) VA (6 > 1)", (not (5 > 8)) and (6 > 1), 3),
          ("(2 + 2 = 4) VA EMAS (9 < 3)", (2 + 2 == 4) and not (9 < 3), 3)]
for e, v, d in _exprs:
    _log.append(Q("Murakkab mulohazaning qiymatini toping.", TXT[v], [TXT[not v], "Aniqlab bo‘lmaydi", "Mulohaza emas"], d=d, text=e,
                  x=f"Avval qavs ichidagi mulohazalarni baholaymiz. Natija: {TXT[v].lower()}."))
for x_, d in [(4, 2), (7, 3)]:
    v = (x_ > 2) and (x_ < 5)
    _log.append(Q(f"x = {x_} bo‘lsa, mulohaza qanday qiymat oladi?", TXT[v], [TXT[not v], "Aniqlab bo‘lmaydi", "Mulohaza emas"], d=d, text="(x > 2) VA (x < 5)",
                  x=f"x > 2 — {TXT[x_ > 2].lower()}, x < 5 — {TXT[x_ < 5].lower()}; VA natijasi: {TXT[v].lower()}."))
_cand = [4, 2, 7, 6]
_good = [c for c in _cand if c > 3 and c < 6]
assert _good == [4]
_log.append(Q("Qaysi x qiymatida mulohaza rost bo‘ladi?", "4", ["2", "7", "6"], d=3, text="(x > 3) VA (x < 6)",
              x="x 3 dan katta va 6 dan kichik bo‘lishi kerak: faqat 4 mos."))
for n, d in [(2, 2), (3, 3)]:
    _log.append(Q(f"{n} ta o‘zgaruvchili rostlik jadvalida nechta satr (holat) bo‘ladi?", 2 ** n, near(2 ** n, [n, n * 2 + 1, 2 ** n + 2, n * n + 1]), d=d,
                  x=f"Har bir o‘zgaruvchi 2 xil qiymat oladi: {' · '.join(['2'] * n)} = {2 ** n}."))

T.topic("mantiq", "✅", L("Mantiqiy amallar", "Logical operations", "Логические операции"),
        chapter=C1,
        theory="Mulohaza — rost yoki yolg‘on ekanini aytish mumkin bo‘lgan darak gap. Rost — 1, yolg‘on — 0.\n"
               "• VA (konyunksiya): ikkala mulohaza rost bo‘lsagina rost.\n"
               "• YOKI (dizyunksiya): kamida bittasi rost bo‘lsa rost; ikkalasi yolg‘on bo‘lsagina yolg‘on.\n"
               "• EMAS (inkor): qiymatni teskarisiga almashtiradi: EMAS 1 = 0, EMAS 0 = 1.\n"
               "Rostlik jadvali: A VA B — 0 0 → 0, 0 1 → 0, 1 0 → 0, 1 1 → 1; A YOKI B — 0 0 → 0, 0 1 → 1, 1 0 → 1, 1 1 → 1.",
        items=[
            Q("Qaysi gap mulohaza bo‘ladi?", "Toshkent — O‘zbekiston poytaxti", ["Soat necha bo‘ldi?", "Eshikni yoping!", "Qanday chiroyli!"],
              x="Mulohaza — rost yoki yolg‘onligini aytish mumkin bo‘lgan darak gap."),
            Q("“5 + 3 = 9” mulohazasi qanday?", "Yolg‘on", ["Rost", "Mulohaza emas", "Ham rost, ham yolg‘on"],
              x="5 + 3 = 8, demak mulohaza yolg‘on."),
            Q("Qaysi mantiqiy amal ikkala mulohaza rost bo‘lgandagina rost natija beradi?", "VA", ["YOKI", "EMAS", "Hech qaysi"],
              x="VA — konyunksiya, “ham …, ham …” ma’nosida."),
            Q("Qaysi mantiqiy amal qiymatni teskarisiga almashtiradi?", "EMAS", ["VA", "YOKI", "TENG"],
              x="EMAS — inkor: rost yolg‘onga, yolg‘on rostga aylanadi."),
            Q("“Soat necha bo‘ldi?” gapi nima uchun mulohaza emas?", "U so‘roq gap", ["U juda qisqa", "Unda son yo‘q", "U yolg‘on"], d=2,
              x="So‘roq va buyruq gaplar rost yoki yolg‘on bo‘lmaydi."),
            TF("YOKI amali ikkala mulohaza ham yolg‘on bo‘lganda yolg‘on natija beradi.", True, x="Faqat shu holatda YOKI yolg‘on bo‘ladi."),
            TF("EMAS (EMAS A) = A.", True, d=2, x="Ikki marta inkor qilinsa, qiymat o‘z holiga qaytadi."),
            TF("VA amali bitta mulohaza rost bo‘lsa ham rost natija beradi.", False, x="VA uchun ikkalasi ham rost bo‘lishi kerak."),
            ORDER(S, "Mulohaza rost yoki yolg‘on bo‘ladi"),
            MATCH("Amalni ta’rifi bilan juftlang",
                  [("VA", "ikkalasi rost bo‘lsa rost"), ("YOKI", "kamida bittasi rost bo‘lsa rost"), ("EMAS", "qiymatni teskarisiga o‘zgartiradi"),
                   ("Konyunksiya", "VA amalining boshqa nomi"), ("Dizyunksiya", "YOKI amalining boshqa nomi"), ("Inkor", "EMAS amalining boshqa nomi")], d=2,
                  x="Mantiqiy amallarning o‘zbekcha va ilmiy nomlari."),
        ] + _log)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["olchov", "ikkilik", "sanoq", "mantiq"], chapter=C1)

# ============================================================ 2-chorak


def col(n):
    """1 → A, 26 → Z, 27 → AA."""
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def col_num(s):
    n = 0
    for ch in s:
        n = n * 26 + ord(ch) - 64
    return n


assert col(26) == "Z" and col(27) == "AA" and col_num("AA") == 27 and col_num("D") == 4


def rng_cells(a, b):
    ma, mb = re.match(r"([A-Z]+)(\d+)", a), re.match(r"([A-Z]+)(\d+)", b)
    c1, r1, c2, r2 = col_num(ma[1]), int(ma[2]), col_num(mb[1]), int(mb[2])
    return [f"{col(c)}{r}" for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)]


_grid = []
for c, r, d in [(3, 5, 1), (1, 7, 1), (4, 2, 2), (26, 10, 3)]:
    a = f"{col(c)}{r}"
    wrong = uniq(a, [f"{col(r)}{c}" if r <= 26 else f"{col(c + 1)}{r}", f"{r}{col(c)}", f"{col(c + 1)}{r}", f"{col(c)}{r + 1}"])
    _grid.append(Q(f"{c}-ustun va {r}-satr kesishgan katakning manzili qanday?", a, wrong, d=d,
                   x=f"{c}-ustun — {col(c)}, manzil: avval ustun harfi, keyin satr raqami — {a}."))
for a_, d in [("D7", 1), ("B12", 2), ("F3", 2)]:
    m = re.match(r"([A-Z]+)(\d+)", a_)
    cn = col_num(m[1])
    _grid.append(Q(f"{a_} katagi nechanchi ustunda joylashgan?", cn, near(cn, [int(m[2]), cn + 1, cn - 1, cn + 2], lo=1), d=d,
                   x=f"{m[1]} — alifboda {cn}-harf, demak {cn}-ustun."))
for a, b, d in [("A1", "A5", 1), ("B2", "C4", 2), ("A1", "D3", 2), ("C3", "E7", 3)]:
    n = len(rng_cells(a, b))
    ma, mb = re.match(r"([A-Z]+)(\d+)", a), re.match(r"([A-Z]+)(\d+)", b)
    w = col_num(mb[1]) - col_num(ma[1]) + 1
    h = int(mb[2]) - int(ma[2]) + 1
    _grid.append(Q(f"{a}:{b} diapazonida nechta katak bor?", n, near(n, [w + h, n + 1, 2, w * h + w, n - 1], lo=1), d=d,
                   x=f"{w} ta ustun · {h} ta satr = {n} ta katak."))
_grid.append(Q("Z ustunidan keyingi ustun qanday nomlanadi?", col(27), ["ZA", "A1", "Z1", "BB"], d=3,
               x="Harflar tugagach, ikki harfli nomlar boshlanadi: AA, AB, AC …"))

T.topic("jadval", "📊", L("Elektron jadval asoslari", "Spreadsheet basics", "Основы электронных таблиц"),
        chapter=C2,
        theory="Elektron jadval — hisob-kitob uchun dastur: Microsoft Excel, LibreOffice Calc, Google Sheets. Excel fayli .xlsx kengaytmali “kitob”, u varaqlardan iborat.\n"
               "• Ustunlar harflar (A, B, C, …, Z, AA, …), satrlar raqamlar (1, 2, 3, …) bilan belgilanadi.\n"
               "• Katak — ustun va satr kesishmasi. Katak manzili: avval ustun harfi, keyin satr raqami: A1, C5. Tanlangan katak — faol katak.\n"
               "• Diapazon — to‘g‘ri to‘rtburchak shaklidagi kataklar guruhi: A1:B3 — 2 ustun · 3 satr = 6 katak.\n"
               "Katakka son, matn yoki formula (= belgisi bilan boshlanadi) yoziladi. Ma’lumotlardan diagramma yasash mumkin.",
        items=[
            Q("Qaysi dastur elektron jadval dasturi?", "Microsoft Excel", ["Microsoft Word", "Paint", "PowerPoint"],
              x="Excel — elektron jadval, Word — matn, PowerPoint — taqdimot dasturi."),
            Q("Elektron jadvalda ustunlar qanday belgilanadi?", "Harflar bilan", ["Raqamlar bilan", "Ranglar bilan", "Rasmlar bilan"],
              x="Ustunlar A, B, C … harflari bilan nomlanadi."),
            Q("Elektron jadvalda satrlar qanday belgilanadi?", "Raqamlar bilan", ["Harflar bilan", "Belgilar bilan", "Ranglar bilan"],
              x="Satrlar 1, 2, 3 … raqamlari bilan nomlanadi."),
            Q("Ustun va satr kesishgan joy nima deyiladi?", "Katak", ["Varaq", "Diagramma", "Formula"],
              x="Har bir katakning o‘z manzili bor."),
            Q("Excel faylining kengaytmasi qaysi?", "xlsx", ["docx", "pptx", "mp3"],
              x="xlsx — Excel ish kitobi."),
            Q("Elektron jadvalda formula qaysi belgi bilan boshlanadi?", "=", ["+", "#", "@"],
              x="= belgisi dasturga “bu formula, hisobla” deydi."),
            TF("A1:B3 yozuvi — kataklar diapazoni.", True, x="Ikki nuqta diapazonning boshi va oxirini ajratadi."),
            TF("Katak manzilida avval satr raqami, keyin ustun harfi yoziladi.", False, x="Avval ustun harfi, keyin satr raqami: B7."),
            ORDER(S, "Formula tenglik belgisi bilan boshlanadi"),
            Q("Butunning qismlarini (masalan, foizlarni) ko‘rsatish uchun qaysi diagramma qulay?", "Doiraviy", ["Chiziqli", "Ustunli", "Nuqtali"], d=2,
              x="Doiraviy diagramma butun doirani bo‘laklarga ajratib ko‘rsatadi."),
            Q("Haroratning kunlar bo‘yicha o‘zgarishini ko‘rsatish uchun qaysi diagramma qulay?", "Chiziqli", ["Doiraviy", "Hech qaysi", "Faqat jadval"], d=2,
              x="Chiziqli grafik vaqt bo‘yicha o‘zgarishni yaxshi ko‘rsatadi."),
            Q("Ma’lumotlarni kattadan kichikka yoki alifbo bo‘yicha tartiblash nima deyiladi?", "Saralash", ["Filtrlash", "Birlashtirish", "Nusxalash"], d=2,
              x="Saralash (sortirovka) satrlarni tartib bilan joylashtiradi."),
            Q("Excelda son kiritilsa, u odatda katakning qaysi tomoniga tekislanadi?", "O‘ngga", ["Chapga", "Markazga", "Pastga"], d=3,
              x="Sonlar o‘ngga, matn chapga tekislanadi — shundan sonni matndan ajratish mumkin."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Katak", "ustun va satr kesishmasi"), ("Manzil", "B5 kabi nom"), ("Diapazon", "kataklar guruhi"), ("Formula", "= bilan boshlanadi"),
                   ("Varaq", "kitobning bir sahifasi"), ("Diagramma", "ma’lumotlarning grafik tasviri")], d=2,
                  x="Elektron jadvalning asosiy tushunchalari."),
        ] + _grid)

# --- Formulalar: kichik baholovchi (SUM, AVERAGE, MAX, MIN, + - * /).


def ev(formula, cells):
    expr = formula[1:]

    def rng(m):
        return "[" + ",".join(str(cells[c]) for c in rng_cells(m[1], m[2])) + "]"
    expr = re.sub(r"([A-Z]+\d+):([A-Z]+\d+)", rng, expr)
    expr = re.sub(r"\b([A-Z]+\d+)\b", lambda m: str(cells[m[1]]), expr)
    env = {"SUM": lambda xs: sum(xs), "AVERAGE": lambda xs: Fraction(sum(xs), len(xs)), "MAX": max, "MIN": min}
    v = eval(expr.replace("/", "//") if False else expr, {"__builtins__": {}}, env)
    v = Fraction(v)
    assert v.denominator == 1, formula
    return int(v)


def show(cells):
    rows = sorted({int(re.match(r"[A-Z]+(\d+)", k)[1]) for k in cells})
    lines = []
    for r in rows:
        lines.append(", ".join(f"{k} = {v}" for k, v in cells.items() if int(re.match(r"[A-Z]+(\d+)", k)[1]) == r))
    return "\n".join(lines)


G1 = {"A1": 5, "B1": 8, "A2": 12, "B2": 3, "A3": 7, "B3": 10, "A4": 6, "B4": 3}
G2 = {"A1": 20, "B1": 15, "C1": 25, "A2": 30, "B2": 40, "C2": 5}
_form = []
for g, f, d in [(G1, "=A1+B1", 1), (G1, "=A2*B2", 1), (G1, "=B3-A3", 1), (G1, "=SUM(A1:A4)", 1), (G1, "=AVERAGE(B1:B4)", 2), (G1, "=MAX(A1:B4)", 2),
                (G1, "=MIN(B1:B4)", 2), (G1, "=SUM(A1:B2)", 2), (G2, "=AVERAGE(A1:C1)", 2), (G2, "=MAX(A1:C2)-MIN(A1:C2)", 3), (G2, "=SUM(A2:C2)/3", 3),
                (G2, "=(A1+B1)*2", 3), (G1, "=SUM(A1:A4)+SUM(B1:B4)", 3)]:
    v = ev(f, g)
    vals = list(g.values())
    _form.append(Q("Jadvaldagi qiymatlar berilgan. Formula natijasi nechaga teng?", v,
                   near(v, [v + 1, v - 1, sum(vals), max(vals), min(vals), v * 2, v + 10], lo=-100), d=d, text=show(g) + f"\nFormula: {f}",
                   x=f"{f} → {v}."))
_form.append(Q("C1 katagida =A1+B1 formulasi bor. U C2 katagiga nusxalansa, qanday formula hosil bo‘ladi?", "=A2+B2", ["=A1+B1", "=B1+C1", "=A2+B1"], d=3,
               x="Nisbiy manzillar nusxalanganda satr raqami 1 ga oshadi: A1 → A2, B1 → B2."))
_form.append(Q("A1 katagidagi son o‘zgarsa, =A1*2 formulali katak nima bo‘ladi?", "Natija avtomatik qayta hisoblanadi", ["O‘zgarmaydi", "Xato chiqadi", "Katak o‘chadi"], d=2,
               x="Elektron jadvalning asosiy qulayligi — formulalar avtomatik yangilanadi."))
_form.append(Q("Nolga bo‘lish formulasi (masalan, =A1/0) qanday xato chiqaradi?", "#DIV/0!", ["#NAME?", "#####", "0"], d=3,
               x="Nolga bo‘lish mumkin emas, Excel #DIV/0! xatosini chiqaradi."))

T.topic("formula", "📈", L("Formulalar va funksiyalar", "Formulas and functions", "Формулы и функции"),
        chapter=C2,
        theory="Formula = belgisi bilan boshlanadi va katak manzillari, sonlar hamda amallardan tuziladi: + qo‘shish, - ayirish, * ko‘paytirish, / bo‘lish.\n"
               "Misol: A1 = 5, B1 = 8 bo‘lsa, =A1+B1 natijasi 13. Qiymat o‘zgarsa, natija avtomatik qayta hisoblanadi.\n"
               "Asosiy funksiyalar (diapazon bilan):\n"
               "• =SUM(A1:A4) — yig‘indi; =AVERAGE(A1:A4) — o‘rta arifmetik; =MAX(A1:A4) — eng katta; =MIN(A1:A4) — eng kichik qiymat.\n"
               "Formula nusxalanganda nisbiy manzillar o‘zgaradi: C1 dagi =A1+B1 C2 ga ko‘chsa, =A2+B2 bo‘ladi.",
        items=[
            Q("SUM funksiyasi nima hisoblaydi?", "Yig‘indini", ["Eng katta sonni", "O‘rta arifmetikni", "Eng kichik sonni"],
              x="SUM — inglizcha “yig‘indi”."),
            Q("AVERAGE funksiyasi nima hisoblaydi?", "O‘rta arifmetikni", ["Yig‘indini", "Kataklar sonini", "Eng katta sonni"],
              x="AVERAGE — sonlar yig‘indisini ularning soniga bo‘ladi."),
            Q("MAX funksiyasi nima topadi?", "Eng katta qiymatni", ["Eng kichik qiymatni", "Yig‘indini", "O‘rtachani"],
              x="MAX — maksimum."),
            Q("MIN funksiyasi nima topadi?", "Eng kichik qiymatni", ["Eng katta qiymatni", "Yig‘indini", "Ko‘paytmani"],
              x="MIN — minimum."),
            Q("Elektron jadvalda ko‘paytirish qaysi belgi bilan yoziladi?", "*", ["x", "·", ":"],
              x="Formulada ko‘paytirish uchun yulduzcha * ishlatiladi."),
            TF("Formulali katakda ekranda odatda formula emas, uning natijasi ko‘rinadi.", True, x="Formulaning o‘zi formula satrida ko‘rinadi."),
            TF("=SUM(A1:A3) formulasi A1, A2, A3 kataklaridagi sonlarni qo‘shadi.", True, x="A1:A3 diapazoni uchta katakni o‘z ichiga oladi."),
            ORDER(S, "SUM funksiyasi sonlar yig‘indisini hisoblaydi"),
            MATCH("Funksiyani vazifasi bilan juftlang",
                  [("SUM", "yig‘indi"), ("AVERAGE", "o‘rta arifmetik"), ("MAX", "eng katta qiymat"), ("MIN", "eng kichik qiymat"), ("=", "formula boshlanishi")], d=2,
                  x="Asosiy funksiyalarni yodda tuting."),
        ] + _form)

_doc = []
for r, c, d in [(3, 4, 1), (5, 2, 1), (4, 6, 2)]:
    n = r * c
    _doc.append(Q(f"Hujjatga {r} satr va {c} ustunli jadval qo‘yildi. Jadvalda nechta katak bor?", n, near(n, [r + c, n + r, n + c, n - 1], lo=1), d=d,
                  x=f"{r} · {c} = {n} ta katak."))
for r, c, d in [(3, 4, 2), (2, 5, 3)]:
    n = (r + 1) * c
    _doc.append(Q(f"{r} satr va {c} ustunli jadvalga yana 1 ta satr qo‘shildi. Endi nechta katak bor?", n, near(n, [r * c, r * c + 1, r * (c + 1), n + 1], lo=1), d=d,
                  x=f"Endi {r + 1} satr: {r + 1} · {c} = {n}."))
for r, c, m, d in [(3, 3, 3, 3), (4, 4, 2, 3)]:
    n = r * c - m + 1
    _doc.append(Q(f"{r} × {c} jadvalda birinchi satrning {m} ta katagi birlashtirildi. Jadvalda nechta katak qoldi?", n, near(n, [r * c, r * c - m, n + 1, n - 1, n + 2, n - 2], lo=1), d=d,
                  x=f"{m} ta katak bitta bo‘ldi: {r * c} − {m} + 1 = {n}."))
for n, dl, d in [(5, 2, 2), (8, 3, 2)]:
    last = n - dl
    _doc.append(Q(f"Raqamli ro‘yxatda {n} ta band bor edi. {dl} ta band o‘chirildi. Oxirgi band qaysi raqam bilan belgilanadi?", last,
                  near(last, [n, n - 1, dl, last + 1], lo=1), d=d, x=f"Raqamli ro‘yxat avtomatik qayta raqamlanadi: {n} − {dl} = {last}."))

T.topic("hujjat", "📝", L("Matn muharriri: jadval, rasm va ro‘yxat", "Word processor: tables, images, lists", "Текстовый редактор: таблицы, рисунки, списки"),
        chapter=C2,
        theory="Matn muharririda (Word, LibreOffice Writer) hujjatga matndan tashqari jadval, rasm va ro‘yxat qo‘shiladi.\n"
               "• Jadval: “Qo‘yish” → “Jadval”, satr va ustunlar soni tanlanadi. Satr yoki ustun qo‘shish, kataklarni birlashtirish mumkin.\n"
               "• Rasm: “Qo‘yish” → “Rasm”. Rasm atrofida matn joylashuvi “Matn bilan o‘rash” orqali sozlanadi.\n"
               "• Ro‘yxat: markerli (• belgisi bilan) va raqamli (1., 2., 3.). Raqamli ro‘yxatdan band o‘chirilsa, raqamlar avtomatik yangilanadi.\n"
               "Sahifa yo‘nalishi: kitob (tik) yoki albom (yotiq). Imlo xatosi qizil to‘lqinli chiziq bilan belgilanadi. Chop etish — Ctrl+P.",
        items=[
            Q("Hujjatga jadval qo‘shish uchun qaysi menyu ochiladi?", "Qo‘yish", ["Fayl", "Ko‘rinish", "Yordam"],
              x="“Qo‘yish” menyusida jadval, rasm, shakl bor."),
            Q("Har bir bandi • belgisi bilan boshlanadigan ro‘yxat qanday ataladi?", "Markerli ro‘yxat", ["Raqamli ro‘yxat", "Jadval", "Sarlavha"],
              x="Marker — band oldidagi belgi."),
            Q("Bandlari 1., 2., 3. bilan boshlanadigan ro‘yxat qanday ataladi?", "Raqamli ro‘yxat", ["Markerli ro‘yxat", "Diagramma", "Kolontitul"],
              x="Raqamli ro‘yxatda tartib muhim bo‘lgan bandlar yoziladi."),
            Q("Word imlo xatosi bor so‘zni qanday belgilaydi?", "Qizil to‘lqinli chiziq bilan", ["Yashil bo‘yoq bilan", "Qalin shrift bilan", "Kursiv bilan"],
              x="Qizil to‘lqinli chiziq so‘zni tekshirib ko‘rishni eslatadi."),
            Q("Hujjatni chop etish uchun qaysi tugmalar bosiladi?", "Ctrl+P", ["Ctrl+S", "Ctrl+J", "Ctrl+M"],
              x="P — inglizcha Print, ya’ni “chop etish”."),
            Q("Keng jadval sig‘ishi uchun sahifa qaysi yo‘nalishga o‘giriladi?", "Albom (yotiq)", ["Kitob (tik)", "Teskari", "Diagonal"], d=2,
              x="Albom yo‘nalishida sahifa kengroq bo‘ladi."),
            Q("Rasm atrofida matn qanday joylashishini qaysi buyruq sozlaydi?", "Matn bilan o‘rash", ["Saralash", "Saqlash sifatida", "Imlo tekshirish"], d=2,
              x="Rasm matn ichida, yonida yoki ortida turishi mumkin."),
            Q("Jadvaldagi bir nechta katakni bitta katakka aylantirish nima deyiladi?", "Kataklarni birlashtirish", ["Kataklarni bo‘lish", "Saralash", "Formatlash"], d=2,
              x="Birlashtirish odatda jadval sarlavhasi uchun ishlatiladi."),
            Q("Har bir sahifaning yuqori yoki pastki qismida takrorlanadigan matn nima deyiladi?", "Kolontitul", ["Xatboshi", "Marker", "Katak"], d=3,
              x="Kolontitulga sahifa raqami, sarlavha yoki muallif nomi yoziladi."),
            Q("Word’da yangi sahifani majburan boshlash uchun qaysi tugmalar bosiladi?", "Ctrl+Enter", ["Ctrl+N", "Shift+Tab", "Alt+F4"], d=3,
              x="Ctrl+Enter sahifa uzilishini qo‘yadi."),
            TF("Hujjatdagi jadvalga keyin ham satr qo‘shish mumkin.", True, x="Jadval o‘lchamini istalgan payt o‘zgartirish mumkin."),
            TF("Raqamli ro‘yxatdan band o‘chirilsa, qolgan raqamlarni qo‘lda tuzatish shart.", False, x="Raqamlar avtomatik yangilanadi."),
            ORDER(S, "Qo‘yish menyusidan jadval qo‘shiladi"),
            MATCH("Elementni qo‘shish yo‘li bilan juftlang",
                  [("Jadval", "Qo‘yish → Jadval"), ("Rasm", "Qo‘yish → Rasm"), ("Raqamli ro‘yxat", "1, 2, 3 tugmasi"), ("Markerli ro‘yxat", "• tugmasi"),
                   ("Chop etish", "Ctrl+P")], d=2,
                  x="Hujjatni boyitish uchun asosiy buyruqlar."),
        ] + _doc)

_pres = []
for n, sec, d in [(12, 45, 2), (20, 30, 2), (8, 75, 3)]:
    tot = n * sec
    m, s = divmod(tot, 60)
    ans = f"{m} daqiqa" if s == 0 else f"{m} daqiqa {s} soniya"
    wr = [f"{m + 1} daqiqa", f"{n} daqiqa", f"{m - 1} daqiqa" if s == 0 else f"{m} daqiqa", f"{tot // 100} daqiqa"]
    _pres.append(Q(f"Taqdimotda {n} ta slayd, har biri avtomatik ravishda {sec} soniyadan keyin almashadi. Namoyish qancha davom etadi?", ans, uniq(ans, wr), d=d,
                   x=f"{n} · {sec} = {tot} soniya = {ans}."))

T.topic("taqdimot", "🎞️", L("Taqdimot: dizayn, animatsiya va namoyish", "Presentations: design, animation, slideshow", "Презентации: дизайн, анимация, показ"),
        chapter=C2,
        theory="Taqdimot dasturlari: PowerPoint (.pptx), LibreOffice Impress, Google Slides.\n"
               "• Slayd maketi — sarlavha, matn va rasm joylashuvi; dizayn mavzusi — fon, ranglar, shriftlar to‘plami.\n"
               "• O‘tish effekti — slaydlar almashishi; animatsiya — slayd ichidagi obyektning paydo bo‘lishi, ajratib ko‘rsatilishi yoki yo‘qolishi.\n"
               "• Namoyish: F5 — boshidan, Shift+F5 — joriy slayddan, Esc — chiqish. Giperhavola (Ctrl+K) boshqa slayd yoki saytga o‘tkazadi.\n"
               "Slaydlar saralovchi rejimida barcha slaydlar kichik ko‘rinishda ko‘rinadi va tartibi o‘zgartiriladi.",
        items=[
            Q("Namoyishni joriy slayddan boshlash uchun qaysi tugmalar bosiladi?", "Shift+F5", ["F5", "Ctrl+F5", "Esc"],
              x="F5 — boshidan, Shift+F5 — joriy slayddan."),
            Q("Slaydlar almashayotganda chiqadigan effekt nima deyiladi?", "O‘tish effekti", ["Animatsiya", "Maket", "Kolontitul"],
              x="O‘tish effekti ikki slayd orasida bo‘ladi."),
            Q("Slayd ichidagi rasmning uchib kirishi nima deyiladi?", "Animatsiya", ["O‘tish effekti", "Maket", "Dizayn mavzusi"],
              x="Animatsiya slayddagi alohida obyektga qo‘llanadi."),
            Q("Slaydda sarlavha, matn va rasm joylashuvi nima deyiladi?", "Slayd maketi", ["Dizayn mavzusi", "Animatsiya", "Giperhavola"],
              x="Maket slayd “skeleti”."),
            Q("Slayddagi matnni saytga bog‘lash nima deyiladi?", "Giperhavola", ["Animatsiya", "Saralash", "Kolontitul"],
              x="Giperhavola bosilsa, sayt yoki boshqa slayd ochiladi."),
            Q("Taqdimotning barcha slaydlarini kichik ko‘rinishda ko‘rib, tartibini o‘zgartirish rejimi?", "Slaydlar saralovchi", ["Namoyish", "Chop etish", "Oddiy"],
              x="Saralovchi rejimda slaydlarni sudrab joyini almashtirish qulay."),
            TF("Taqdimotga video va tovush qo‘shish mumkin.", True, x="Qo‘yish menyusida video va audio bor."),
            TF("Bitta slaydga iloji boricha ko‘p animatsiya qo‘yish taqdimotni yaxshilaydi.", False, x="Ortiqcha animatsiya tomoshabinni chalg‘itadi."),
            ORDER(S, "Esc tugmasi namoyishni to‘xtatadi"),
            Q("Ma’ruzachi slayd ostiga o‘zi uchun yozib qo‘yadigan matn nima deyiladi?", "Eslatmalar", ["Sarlavha", "Kolontitul", "Marker"], d=2,
              x="Eslatmalar namoyishda tomoshabinlarga ko‘rinmaydi."),
            Q("Taqdimotni boshqa kompyuterda o‘zgarmasdan ochilishi uchun qaysi formatda saqlash qulay?", "PDF", ["TXT", "MP3", "BMP"], d=2,
              x="PDF hujjati har qanday qurilmada bir xil ko‘rinadi."),
            Q("PowerPoint’da animatsiyaning qaysi turi obyektni slayddan yo‘qotadi?", "Chiqish", ["Kirish", "Ajratib ko‘rsatish", "Maket"], d=3,
              x="Kirish — paydo bo‘lish, ajratib ko‘rsatish — urg‘u berish, chiqish — yo‘qolish."),
            Q("Giperhavola qo‘shish uchun qaysi tugmalar bosiladi?", "Ctrl+K", ["Ctrl+H", "Ctrl+L", "Ctrl+G"], d=3,
              x="Ctrl+K — giperhavola qo‘yish oynasini ochadi."),
            Q("Yaxshi slayd uchun qaysi tavsiya to‘g‘ri?", "Bir slaydda bitta asosiy fikr", ["Har slaydda 10 xil shrift", "Butun matnni slaydga ko‘chirish", "Fon va matn rangi bir xil"], d=2,
              x="Qisqa, aniq va o‘qilishi oson slayd tomoshabinga tushunarli."),
            Q("Barcha slaydlarga bir xil fon, rang va shrift berish uchun nima tanlanadi?", "Dizayn mavzusi", ["O‘tish effekti", "Animatsiya", "Eslatmalar"],
              x="Dizayn mavzusi butun taqdimotga yagona ko‘rinish beradi."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Maket", "elementlar joylashuvi"), ("Dizayn mavzusi", "fon va ranglar to‘plami"), ("O‘tish effekti", "slaydlar almashishi"),
                   ("Animatsiya", "obyekt harakati"), ("Giperhavola", "boshqa joyga o‘tish"), ("Eslatmalar", "ma’ruzachi uchun matn")], d=2,
                  x="Taqdimot yaratishning asosiy tushunchalari."),
        ] + _pres)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["jadval", "formula", "hujjat", "taqdimot"], chapter=C2)

# ============================================================ 3-chorak
_flow = []
for x_, d in [(7, 1), (3, 2)]:
    y = x_ * 2 if x_ > 5 else x_ + 10
    _flow.append(Q(f"Blok-sxema: x ga {x_} kiritildi. Romb: “x > 5?”. “Ha” bo‘lsa y = x · 2, “Yo‘q” bo‘lsa y = x + 10. y nechaga teng?", y,
                   near(y, [x_ * 2, x_ + 10, x_, y + 1]), d=d,
                   x=(f"{x_} > 5 — ha: y = {x_} · 2 = {y}." if x_ > 5 else f"{x_} > 5 — yo‘q: y = {x_} + 10 = {y}.")))
for a, b, d in [(8, 13, 2), (15, 9, 2)]:
    m = a if a > b else b
    _flow.append(Q(f"Blok-sxema: a = {a}, b = {b}. Romb: “a > b?”. “Ha” bo‘lsa a chiqariladi, “Yo‘q” bo‘lsa b chiqariladi. Nima chiqariladi?", m,
                   near(m, [a, b, a + b, abs(a - b)]), d=d, x=f"Algoritm ikki sondan kattasini chiqaradi: {m}."))
for n, d in [(4, 2), (6, 3)]:
    s = sum(range(1, n + 1))
    _flow.append(Q(f"Blok-sxema: s = 0, i = 1. Romb: “i ≤ {n}?”. “Ha” bo‘lsa: s = s + i, i = i + 1 va yana romb. “Yo‘q” bo‘lsa s chiqariladi. s nechaga teng?", s,
                   near(s, [sum(range(1, n)), sum(range(1, n + 2)), n, s + 1]), d=d,
                   say=f"Blok-sxema: s = 0, i = 1. Romb: i {n} dan kichik yoki tengmi? Ha bo‘lsa: s = s + i, i = i + 1 va yana romb. Yo‘q bo‘lsa s chiqariladi. s nechaga teng?",
                   x=f"s = 1 + 2 + … + {n} = {s}."))
for n, d in [(20, 3), (15, 3)]:
    k, v, checks = 0, n, 1
    while v > 5:
        v -= 6
        k += 1
        checks += 1
    _flow.append(Q(f"Blok-sxema: n = {n}. Romb: “n > 5?”. “Ha” bo‘lsa n = n − 6 va yana romb, “Yo‘q” bo‘lsa n chiqariladi. Nima chiqariladi?", v,
                   near(v, [v + 6, v - 6 if v >= 6 else v + 1, n % 5, 0, 1], lo=-10), d=d,
                   x=f"n {k} marta 6 ga kamaydi: {n} → {v}. Shart {checks} marta tekshirildi."))
    _flow.append(Q(f"Blok-sxema: n = {n}. Romb: “n > 5?”. “Ha” bo‘lsa n = n − 6 va yana romb. Sikl tanasi necha marta bajariladi?", k,
                   near(k, [k + 1, k - 1, n // 5, checks + 1], lo=0), d=d,
                   x=f"n qiymatlari: " + " → ".join(str(n - 6 * i) for i in range(k + 1)) + f"; tana {k} marta bajarildi."))

T.topic("blok_sxema", "🔷", L("Algoritm turlari va blok-sxemalar", "Algorithm types and flowcharts", "Виды алгоритмов и блок-схемы"),
        chapter=C3,
        theory="Algoritm turlari: chiziqli (buyruqlar ketma-ket), tarmoqlanuvchi (shartga qarab yo‘l tanlanadi), takrorlanuvchi (sikl).\n"
               "Blok-sxema shakllari:\n"
               "• oval — boshlanish va tugash; parallelogramm — kiritish va chiqarish; to‘g‘ri to‘rtburchak — amal (hisoblash);\n"
               "• romb — shart, undan “Ha” va “Yo‘q” deb belgilangan ikki yo‘l chiqadi; strelkalar bajarilish tartibini ko‘rsatadi.\n"
               "Siklda strelka rombga qaytadi: shart rost ekan, tana qayta bajariladi. Masalan, s = 0, i = 1 dan 4 gacha s = s + i → s = 10.",
        items=[
            Q("Blok-sxemada kiritish va chiqarish qaysi shakl bilan belgilanadi?", "Parallelogramm", ["Romb", "Oval", "Doira"],
              x="Parallelogramm — ma’lumot kiritish yoki natijani chiqarish."),
            Q("Blok-sxemada shart qaysi shakl ichiga yoziladi?", "Romb", ["Oval", "To‘g‘ri to‘rtburchak", "Parallelogramm"],
              x="Rombdan “Ha” va “Yo‘q” yo‘llari chiqadi."),
            Q("Blok-sxemada hisoblash amali qaysi shakl ichiga yoziladi?", "To‘g‘ri to‘rtburchak", ["Romb", "Oval", "Uchburchak"],
              x="To‘g‘ri to‘rtburchak — amal bloki."),
            Q("Blok-sxema qaysi shakl bilan boshlanadi va tugaydi?", "Oval", ["Romb", "Parallelogramm", "Kvadrat"],
              x="Oval ichiga “Boshlash” va “Tugash” yoziladi."),
            Q("Shartga qarab ikki yo‘ldan biri tanlanadigan algoritm qanday ataladi?", "Tarmoqlanuvchi", ["Chiziqli", "Takrorlanuvchi", "Tasodifiy"],
              x="Tarmoqlanuvchi algoritmda romb bloki bor."),
            TF("Chiziqli algoritmda buyruqlar birin-ketin, hech narsa tekshirilmasdan bajariladi.", True, x="Chiziqli algoritmda shart ham, sikl ham yo‘q."),
            TF("Siklda strelka oldingi blokka qaytadi.", True, d=2, x="Qaytish strelkasi takrorlanishni ko‘rsatadi."),
            ORDER(S, "Romb ichiga shart yoziladi"),
            Q("“Uyga kelgach, dars qil; agar vaqt qolsa, o‘yna” qaysi algoritm turiga misol?", "Tarmoqlanuvchi", ["Chiziqli", "Takrorlanuvchi", "Algoritm emas"], d=2,
              x="“Agar …” so‘zi shartni bildiradi."),
            Q("“Barcha misollar yechilmaguncha, navbatdagi misolni yech” qaysi algoritm turiga misol?", "Takrorlanuvchi", ["Chiziqli", "Tarmoqlanuvchi", "Tasodifiy"], d=2,
              x="Bir xil ish shart bajarilguncha takrorlanadi."),
            MATCH("Shaklni vazifasi bilan juftlang",
                  [("Oval", "boshlanish va tugash"), ("Parallelogramm", "kiritish va chiqarish"), ("To‘g‘ri to‘rtburchak", "amal"), ("Romb", "shart"),
                   ("Strelka", "bajarilish tartibi")], d=2,
                  x="Blok-sxema shakllari xalqaro qabul qilingan."),
        ] + _flow)

# --- Scratch: skriptlar natijasi Python'da hisoblanadi.
_scr = []


def _s1():
    ball = 0
    for _ in range(5):
        ball += 2
    return ball


def _s2():
    ball = 10
    for _ in range(3):
        ball += -2
    return ball


def _s3():
    x = 0
    for _ in range(4):
        x += 15
    return "G‘alaba!" if x > 50 else "Yana urin!"


def _s4():
    son = 7
    son = son + 1 if son > 10 else son + 5
    return son


def _s5():
    ball = 0
    for _ in range(2):
        for _ in range(3):
            ball += 1
    return ball


def _s6():
    x = 1
    while not x > 20:
        x = x * 2
    return x


def _s7():
    ball = 0
    for i in range(6):
        ball += 3
        if ball > 10:
            ball = 0
    return ball


for script, fn, what, d in [
        ("yashil bayroqcha bosilganda\nball ni 0 ga o‘rnat\n5 marta takrorla: ball ni 2 ga o‘zgartir", _s1, "ball", 1),
        ("yashil bayroqcha bosilganda\nball ni 10 ga o‘rnat\n3 marta takrorla: ball ni -2 ga o‘zgartir", _s2, "ball", 2),
        ("son ni 7 ga o‘rnat\nagar son > 10 bo‘lsa: son ni 1 ga o‘zgartir,\naks holda: son ni 5 ga o‘zgartir", _s4, "son", 2),
        ("ball ni 0 ga o‘rnat\n2 marta takrorla [ 3 marta takrorla [ ball ni 1 ga o‘zgartir ] ]", _s5, "ball", 3),
        ("x ni 1 ga o‘rnat\nx > 20 bo‘lguncha takrorla: x ni x * 2 ga o‘rnat", _s6, "x", 3),
        ("ball ni 0 ga o‘rnat\n6 marta takrorla [ ball ni 3 ga o‘zgartir;\nagar ball > 10 bo‘lsa: ball ni 0 ga o‘rnat ]", _s7, "ball", 3)]:
    v = fn()
    _scr.append(Q(f"Skript bajarilgach, {what} o‘zgaruvchisi nechaga teng bo‘ladi?", v, near(v, [v + 1, v - 1, v + 2, v * 2, 0, 10], lo=-20), d=d, text=script,
                  x=f"Bloklarni tartib bilan bajarsak, {what} = {v}."))
_v3 = _s3()
_scr.append(Q("Skript bajarilgach, sprayt nima deydi?", f"“{_v3}”", ["“Yana urin!”" if _v3 != "Yana urin!" else "“G‘alaba!”", "Hech narsa demaydi", "“60”"], d=3,
              text="x ni 0 ga o‘rnat\n4 marta takrorla: x ni 15 ga o‘zgartir\nagar x > 50 bo‘lsa: “G‘alaba!” de,\naks holda: “Yana urin!” de",
              x="4 · 15 = 60, 60 > 50 — shart rost."))

T.topic("scratch", "🐱", L("Scratch: hodisa, sikl, shart, o‘zgaruvchi", "Scratch: events, loops, conditions, variables", "Scratch: события, циклы, условия, переменные"),
        chapter=C3,
        theory="Scratch’da dastur (skript) bloklardan yig‘iladi.\n"
               "• Hodisalar: “yashil bayroqcha bosilganda”, “sprayt bosilganda”, “probel tugmasi bosilganda”, “xabar olinganda” — skriptni boshlaydi.\n"
               "• Sikllar (Boshqaruv): “10 marta takrorla”, “doimo takrorla”, “… bo‘lguncha takrorla”. Shartlar: “agar … bo‘lsa”, “agar … bo‘lsa … aks holda”.\n"
               "• O‘zgaruvchi — qiymat saqlaydigan “quti” (masalan, ball). “ball ni 0 ga o‘rnat” qiymatni almashtiradi, “ball ni 1 ga o‘zgartir” qiymatga 1 qo‘shadi.\n"
               "• Sezish bloklari (“… ga tegyaptimi?”) va Operatorlar (+, >, “va”, “yoki”, tasodifiy son) shartlarda ishlatiladi.",
        items=[
            Q("Scratch’da o‘yin ochkosini saqlash uchun nima yaratiladi?", "O‘zgaruvchi", ["Kostyum", "Sahna", "Tovush"],
              x="O‘zgaruvchi — qiymat saqlaydigan nomlangan joy."),
            Q("“sprayt bosilganda” bloki qaysi guruhda?", "Hodisalar", ["Harakat", "Operatorlar", "Tovush"],
              x="Hodisalar bloklari skript qachon boshlanishini belgilaydi."),
            Q("“agar … bo‘lsa” bloki qaysi guruhda?", "Boshqaruv", ["Hodisalar", "Ko‘rinish", "Harakat"],
              x="Shart va sikl bloklari Boshqaruv guruhida."),
            Q("“… ga tegyaptimi?” bloki qaysi guruhda?", "Sezish", ["Harakat", "Tovush", "Hodisalar"],
              x="Sezish bloklari spraytning atrofini “sezadi”."),
            Q("“ball ni 0 ga o‘rnat” bloki nima qiladi?", "ball ga 0 qiymatini beradi", ["ball ga 0 qo‘shadi", "ball ni o‘chiradi", "Spraytni yashiradi"],
              x="“o‘rnat” eski qiymatni yangisiga almashtiradi."),
            Q("“ball ni 1 ga o‘zgartir” bloki nima qiladi?", "ball ga 1 qo‘shadi", ["ball ni 1 ga tenglaydi", "ball ni 1 ga bo‘ladi", "ball ni o‘chiradi"],
              x="“o‘zgartir” joriy qiymatga berilgan sonni qo‘shadi."),
            TF("“doimo takrorla” ichidagi bloklar to‘xtatish tugmasi bosilguncha bajariladi.", True, x="Bu cheksiz sikl."),
            TF("Bitta spraytda faqat bitta skript bo‘lishi mumkin.", False, x="Spraytda bir nechta skript bo‘lishi mumkin, har biri o‘z hodisasi bilan."),
            ORDER(S, "O‘zgaruvchi o‘yindagi ballni saqlaydi"),
            Q("Spraytlar bir-biriga signal berishi uchun qaysi blok ishlatiladi?", "xabar yubor", ["kut", "takrorla", "ayt"], d=2,
              x="Bir sprayt xabar yuboradi, boshqasi “xabar olinganda” bloki bilan ishga tushadi."),
            Q("Ikki shartni birlashtiruvchi “… va …” bloki qaysi guruhda?", "Operatorlar", ["Hodisalar", "Sezish", "Harakat"], d=3,
              x="Mantiqiy “va”, “yoki”, “emas” bloklari Operatorlar guruhida."),
            Q("“10 marta takrorla”dan farqli, “doimo takrorla” qachon to‘xtaydi?", "Dastur to‘xtatilganda", ["10 martadan keyin", "Hech qachon ishlamaydi", "Bir martadan keyin"], d=2,
              x="“doimo takrorla” sanamaydi, u to‘xtatilguncha ishlaydi."),
            MATCH("Blokni guruhi bilan juftlang",
                  [("yashil bayroqcha bosilganda", "Hodisalar"), ("agar … bo‘lsa", "Boshqaruv"), ("… ga tegyaptimi?", "Sezish"),
                   ("tasodifiy son tanla", "Operatorlar"), ("ball ni 1 ga o‘zgartir", "O‘zgaruvchilar"), ("10 qadam yur", "Harakat")], d=2,
                  x="Bloklar vazifasiga qarab guruhlangan."),
        ] + _scr)

# --- Psevdokod: satrlar Python'ga o'giriladi va bajariladi (natijalar qo'lda yozilmaydi).


def _stmt(s):
    s = s.strip()
    m = re.match(r"chiqar (.+)$", s)
    if m:
        return [f"out.append(str({m[1]}))" if "," not in m[1] else f"out.append(', '.join(str(v) for v in ({m[1]},)))"]
    return [s]


def _block(stmts, ind):
    lines = []
    for st in stmts.split("; "):
        lines += [" " * ind + ln for ln in _stmt(st)]
    return lines


def to_py(src, delta=0):
    py = []
    for line in src.split("\n"):
        m = re.match(r"agar (.+) bo‘lsa: (.+), aks holda: (.+)$", line)
        if m:
            py += [f"if {m[1]}:"] + _block(m[2], 4) + ["else:"] + _block(m[3], 4)
            continue
        m = re.match(r"agar (.+) bo‘lsa: (.+)$", line)
        if m:
            py += [f"if {m[1]}:"] + _block(m[2], 4)
            continue
        m = re.match(r"(\w+) = (\d+) dan (\d+) gacha takrorla: (.+)$", line)
        if m:
            py += [f"for {m[1]} in range({m[2]}, {int(m[3]) + 1 + delta}):"] + _block(m[4], 4)
            continue
        m = re.match(r"(\d+) marta takrorla: (.+)$", line)
        if m:
            py += [f"for _ in range({int(m[1]) + delta}):"] + _block(m[2], 4)
            continue
        m = re.match(r"toki (.+): (.+)$", line)
        if m:
            py += [f"while {m[1]}:"] + _block(m[2], 4)
            continue
        py += _block(line, 0)
    return "\n".join(py)


def run_prog(src, delta=0):
    env = {"out": []}
    exec(to_py(src, delta), {"__builtins__": {"str": str, "range": range}}, env)
    return ", ".join(env["out"])


_prog = []
for src, d in [
        ("a = 5\nb = a + 3\na = b * 2\nchiqar a", 1),
        ("x = 10\ny = x - 3\nx = x + y\nchiqar x", 1),
        ("a = 7\nb = 2\na = a * b\nb = a - b\nchiqar b", 2),
        ("son = 1234\nchiqar son % 10", 2),
        ("son = 1234\nchiqar son // 10", 2),
        ("n = 17\nq = n // 5\nr = n % 5\nchiqar q + r", 2),
        ("a = 9\nagar a > 5 bo‘lsa: a = a - 5, aks holda: a = a + 5\nchiqar a", 2),
        ("a = 4\nb = 6\nagar a > b bo‘lsa: c = a, aks holda: c = b\nchiqar c", 2),
        ("x = 12\nagar x % 2 == 0 bo‘lsa: chiqar \"juft\", aks holda: chiqar \"toq\"", 2),
        ("s = 0\ni = 1 dan 5 gacha takrorla: s = s + i\nchiqar s", 2),
        ("p = 1\n4 marta takrorla: p = p * 2\nchiqar p", 2),
        ("s = 0\ni = 1 dan 4 gacha takrorla: s = s + i * i\nchiqar s", 3),
        ("n = 20\nk = 0\ntoki n > 5: n = n - 6; k = k + 1\nchiqar k", 3),
        ("a = 1\nb = 1\n3 marta takrorla: c = a + b; a = b; b = c\nchiqar b", 3),
        ("a = 3\nb = 8\nc = a\na = b\nb = c\nchiqar a, b", 3)]:
    ans = run_prog(src)
    cands = []
    for dl in (-1, 1):
        try:
            cands.append(run_prog(src, dl))
        except Exception:
            pass
    if ans.lstrip("-").isdigit():
        v = int(ans)
        cands += [str(c) for c in [v + 1, v - 1, v * 2, v + 10, 0]]
    elif "," in ans:
        p = ans.split(", ")
        cands += [", ".join(reversed(p)), f"{p[1]}, {p[1]}", f"{p[0]}, {p[0]}"]
    else:
        cands += ["toq" if ans == "juft" else "juft", "12", "0"]
    shown = src.replace('"', "“", 1).replace('"', "”", 1).replace('"', "“", 1).replace('"', "”", 1)
    _prog.append(Q("Dastur bajarilgach, ekranga nima chiqadi?", ans, uniq(ans, cands), d=d, text=shown,
                   x="Buyruqlarni tartib bilan bajarib, o‘zgaruvchilar qiymatini kuzatamiz. Natija: " + ans + "."))
assert run_prog("a = 5\nb = a + 3\na = b * 2\nchiqar a") == "16"
assert run_prog("s = 0\ni = 1 dan 5 gacha takrorla: s = s + i\nchiqar s") == "15"
assert run_prog("n = 20\nk = 0\ntoki n > 5: n = n - 6; k = k + 1\nchiqar k") == "3"
assert run_prog("a = 3\nb = 8\nc = a\na = b\nb = c\nchiqar a, b") == "8, 3"
assert 17 // 5 == 3 and 17 % 5 == 2

T.topic("dastur_natija", "💻", L("Dastur natijasini aniqlash", "Tracing a program", "Определение результата программы"),
        chapter=C3,
        theory="Dastur natijasini aniqlash uchun buyruqlarni tartib bilan “qo‘lda” bajaramiz va o‘zgaruvchilar qiymatini yozib boramiz.\n"
               "• a = 5 — a o‘zgaruvchisiga 5 beriladi (eski qiymat o‘chadi); a = a + 1 — a ning qiymati 1 ga oshadi.\n"
               "• Amallar: + qo‘shish, - ayirish, * ko‘paytirish, // butun bo‘lish, % qoldiq: 17 // 5 = 3, 17 % 5 = 2. == — tenglikni tekshirish.\n"
               "• “agar SHART bo‘lsa: …, aks holda: …” — shart rost bo‘lsa birinchi, aks holda ikkinchi buyruq bajariladi.\n"
               "• “3 marta takrorla: …”, “i = 1 dan 4 gacha takrorla: …” — sikl; “toki SHART: …” — shart rost ekan, takrorlanadi. “chiqar a” — a ni ekranga chiqaradi.",
        items=[
            Q("“a = a + 1” buyrug‘i nima qiladi?", "a ning qiymatini 1 ga oshiradi", ["a ni 1 ga tenglaydi", "a ni o‘chiradi", "Xato beradi"],
              x="O‘ng tomon hisoblanadi va natija a ga yoziladi."),
            Q("17 % 5 ifodaning qiymati nechaga teng?", str(17 % 5), [str(17 // 5), "3,4", "12"], d=2,
              x="% — bo‘linmaning qoldig‘i: 17 = 3 · 5 + 2."),
            Q("17 // 5 ifodaning qiymati nechaga teng?", str(17 // 5), [str(17 % 5), "3,4", "85"], d=2,
              x="// — butun bo‘lish: 17 : 5 = 3 (qoldiq 2)."),
            Q("Qaysi buyruq natijani ekranga chiqaradi?", "chiqar", ["takrorla", "agar", "toki"],
              x="“chiqar a” — a ning qiymatini ekranga chiqaradi."),
            Q("“a = 5” buyrug‘idan keyin “a = 8” bajarilsa, a nechaga teng?", "8", ["5", "13", "58"],
              x="Yangi qiymat eskisining o‘rniga yoziladi."),
            TF("O‘zgaruvchiga yangi qiymat berilsa, eski qiymat saqlanib qoladi.", False, x="Eski qiymat o‘chadi, o‘rniga yangisi yoziladi."),
            TF("Dastur buyruqlari yuqoridan pastga tartib bilan bajariladi.", True, x="Sikl va shartlar bu tartibni o‘zgartirishi mumkin."),
            ORDER(S, "O‘zgaruvchi qiymatni saqlaydi"),
            MATCH("Amalni ma’nosi bilan juftlang",
                  [("+", "qo‘shish"), ("-", "ayirish"), ("*", "ko‘paytirish"), ("//", "butun bo‘lish"), ("%", "qoldiq"), ("==", "tenglikni tekshirish")], d=2,
                  x="Dasturlashdagi asosiy amallar."),
        ] + _prog)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["blok_sxema", "scratch", "dastur_natija"], chapter=C3)

# ============================================================ 4-chorak
_net = []
_ips = ["192.168.1.10", "256.10.1.1", "10.0.0", "172.16.300.4", "192.168.1.1.5"]


def valid_ip(s):
    try:
        ipaddress.IPv4Address(s)
        return True
    except ValueError:
        return False


assert [valid_ip(s) for s in _ips] == [True, False, False, False, False]
_net.append(Q("Qaysi yozuv to‘g‘ri IP-manzil?", "192.168.1.10", ["256.10.1.1", "10.0.0", "172.16.300.4", "192.168.1.1.5"], d=2,
              x="IPv4 manzil — nuqta bilan ajratilgan 4 ta son, har biri 0 dan 255 gacha."))
_bad_ip = "10.20.256.1"
assert not valid_ip(_bad_ip) and valid_ip("10.20.255.1") and valid_ip("8.8.8.8") and valid_ip("127.0.0.1")
_net.append(Q("Qaysi IP-manzil noto‘g‘ri yozilgan?", _bad_ip, ["10.20.255.1", "8.8.8.8", "127.0.0.1"], d=3,
              x="256 soni ruxsat etilgan chegaradan (0–255) katta."))
URL = "https://www.maktab.uz/darslar/fizika.html"
_net.append(Q("Manzildagi protokol qaysi?", "https", ["www", "uz", "html"], d=2, text=URL, x="Manzil boshidagi https — ma’lumot almashish qoidasi (protokol)."))
_net.append(Q("Manzildagi domen nomi qaysi?", "www.maktab.uz", ["https", "darslar", "fizika.html"], d=2, text=URL, x="Domen nomi — // dan keyin birinchi / gacha bo‘lgan qism."))
_net.append(Q("Manzildagi fayl nomi qaysi?", "fizika.html", ["darslar", "maktab", "https"], d=3, text=URL, x="Fayl nomi manzilning oxirida joylashgan."))
for size, speed, d in [(80, 10, 2), (5 * 8, 8, 3)]:
    t = size // speed
    _net.append(Q(f"Hajmi {size} Mbit bo‘lgan fayl {speed} Mbit/s tezlikda necha soniyada yuklanadi?", t, near(t, [size * speed, t + 1, t * 8, speed], lo=1), d=d,
                  x=f"{size} : {speed} = {t} soniya.", say=f"Hajmi {size} megabit bo‘lgan fayl sekundiga {speed} megabit tezlikda necha soniyada yuklanadi?"))
_net.append(Q("Hajmi 5 MB bo‘lgan fayl 8 Mbit/s tezlikda necha soniyada yuklanadi?", 5 * 8 // 8, [40, 1, 8], d=3,
              say="Hajmi 5 megabayt bo‘lgan fayl sekundiga 8 megabit tezlikda necha soniyada yuklanadi?",
              x=f"5 MB = 5 · 8 = 40 Mbit; 40 : 8 = {5 * 8 // 8} soniya."))

T.topic("tarmoq", "🌐", L("Kompyuter tarmoqlari va internet", "Computer networks and the internet", "Компьютерные сети и интернет"),
        chapter=C4,
        theory="Kompyuter tarmog‘i — axborot almashish uchun o‘zaro ulangan kompyuterlar. Lokal tarmoq bir xona yoki binoda, global tarmoq — Internet — butun dunyoda.\n"
               "• Server boshqa kompyuterlarga (mijozlarga) xizmat ko‘rsatadi. Internetga ulanish xizmatini provayder beradi.\n"
               "• IP-manzil — tarmoqdagi qurilmaning raqamli manzili: nuqta bilan ajratilgan 4 ta son, har biri 0–255 (192.168.1.10).\n"
               "• Domen nomi — eslab qolish oson nom (maktab.uz); DNS uni IP-manzilga aylantiradi. Zonalar: .uz — O‘zbekiston, .com — tijorat, .org — tashkilotlar.\n"
               "URL: https://www.maktab.uz/darslar/fizika.html — protokol, domen, papka va fayl. Tezlik bit/s da o‘lchanadi.",
        items=[
            Q("Bir xona yoki binodagi kompyuterlarni bog‘lovchi tarmoq qanday ataladi?", "Lokal tarmoq", ["Global tarmoq", "Provayder", "Domen"],
              x="Masalan, maktabning informatika xonasidagi kompyuterlar tarmog‘i."),
            Q("Internetga ulanish xizmatini ko‘rsatuvchi kompaniya nima deyiladi?", "Provayder", ["Server", "Brauzer", "Domen"],
              x="Provayder uy va tashkilotlarni internetga ulaydi."),
            Q("Boshqa kompyuterlarga xizmat ko‘rsatuvchi, saytlar saqlanadigan kompyuter nima?", "Server", ["Mijoz", "Router", "Skaner"],
              x="Server kecha-yu kunduz ishlaydi va so‘rovlarga javob beradi."),
            Q("Tarmoqdagi qurilmaning raqamli manzili nima deyiladi?", "IP-manzil", ["Domen nomi", "Parol", "Kengaytma"],
              x="IP-manzil — Internet Protocol manzili."),
            Q("IPv4 manzilidagi har bir son qaysi oraliqda bo‘ladi?", "0 dan 255 gacha", ["0 dan 100 gacha", "1 dan 1000 gacha", "0 dan 9 gacha"],
              x="Har bir son 8 bit (1 bayt) bilan yoziladi: 0–255."),
            Q("Domen nomini IP-manzilga aylantiruvchi xizmat qaysi?", "DNS", ["HTML", "USB", "PDF"], d=2,
              x="DNS — internetning “telefon kitobi”."),
            Q("“.org” domen zonasi odatda kimlarga tegishli?", "Tashkilotlarga", ["Faqat maktablarga", "Faqat O‘zbekistonga", "Faqat o‘yinlarga"], d=2,
              x=".org — notijorat tashkilotlar zonasi."),
            Q("Ma’lumot uzatish tezligi qanday birlikda o‘lchanadi?", "Bit/s", ["Gramm", "Metr", "Gradus"],
              x="Masalan, 100 Mbit/s — sekundiga 100 megabit."),
            TF("Internet — global kompyuter tarmog‘i.", True, x="Internet butun dunyo tarmoqlarini birlashtiradi."),
            TF("Ikki qurilma bir tarmoqda bir xil IP-manzilga ega bo‘lishi kerak.", False, x="Har bir qurilmaning tarmoqda o‘z noyob manzili bo‘ladi."),
            ORDER(S, "DNS domen nomini IP-manzilga aylantiradi"),
            Q("Hamma kompyuter bitta markaziy qurilmaga ulangan tarmoq tuzilishi qanday ataladi?", "Yulduz", ["Halqa", "Shina", "Daraxt"], d=3,
              x="Yulduz topologiyasida markazda kommutator yoki router turadi."),
            Q("Yaqin masofada (bir necha metr) quloqchin va telefonni simsiz ulash texnologiyasi?", "Bluetooth", ["Wi-Fi router", "DNS", "HTTPS"], d=2,
              x="Bluetooth kichik masofadagi qurilmalarni ulaydi."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Server", "xizmat ko‘rsatuvchi kompyuter"), ("Provayder", "internetga ulovchi kompaniya"), ("IP-manzil", "qurilmaning raqamli manzili"),
                   ("Domen nomi", "saytning eslab qolinadigan nomi"), ("DNS", "nomni IP ga aylantiradi"), ("URL", "sahifaning to‘liq manzili")], d=2,
                  x="Tarmoq va internetning asosiy tushunchalari."),
        ] + _net)

_pin = []
for digits, d in [(4, 2), (6, 3)]:
    n = 10 ** digits
    _pin.append(Q(f"{digits} xonali raqamli PIN-kod uchun nechta turli variant bor?", fmt(n), [fmt(v) for v in near(n, [digits * 10, 10 ** (digits - 1), 9 ** digits, n * 10])], d=d,
                  x=f"Har bir xonaga 10 xil raqam: 10 ni {digits} marta ko‘paytiramiz — {fmt(n)}."))
for per_sec, d in [(100, 3)]:
    t = 10 ** 4 // per_sec
    _pin.append(Q(f"Buzg‘unchi dastur soniyasiga {per_sec} ta variantni tekshiradi. 4 xonali PIN-kodni ko‘pi bilan necha soniyada topadi?", t,
                  near(t, [t * 10, t // 10, 10 ** 4, per_sec], lo=1), d=d,
                  x=f"10 000 : {per_sec} = {t} soniya — qisqa PIN tez topiladi, shuning uchun uzun parol kerak."))
for n, d in [(3, 2)]:
    v = 2 ** n
    _pin.append(Q(f"Parol faqat 0 va 1 raqamlaridan iborat va {n} belgili. Nechta turli parol bo‘lishi mumkin?", v, near(v, [n, n * 2, v * 2, 6], lo=1), d=d,
                  x=f"{' · '.join(['2'] * n)} = {v}."))

T.topic("kiberxavfsizlik", "🛡️", L("Kiberxavfsizlik", "Cybersecurity", "Кибербезопасность"),
        chapter=C4,
        theory="Kiberxavfsizlik — kompyuter, telefon va ma’lumotlarni hujumlardan himoya qilish.\n"
               "• Kuchli parol: kamida 8 belgi (yaxshisi 12 va undan ko‘p), katta va kichik harflar, raqamlar, maxsus belgilar; har bir sayt uchun alohida parol. Ikki bosqichli tekshiruv (parol + SMS-kod) himoyani kuchaytiradi.\n"
               "• Fishing — soxta xat yoki sayt orqali parol va karta ma’lumotini o‘g‘irlash. Belgilari: shoshiltirish, sovg‘a va’dasi, manzilda g‘alati xatolar.\n"
               "• Zararli dasturlar: virus (o‘zidan nusxa ko‘paytiradi), troyan (foydali dastur niqobida), to‘lov talab qiluvchi dastur (fayllarni shifrlab, pul so‘raydi).\n"
               "Himoya: antivirus, tizimni yangilash, fayllarning zaxira nusxasi, SMS-kodni hech kimga aytmaslik.",
        items=[
            Q("Qaysi parol eng kuchli?", "t7#Kitob_Daryo2", ["qwerty123", "11111111", "Aziz2012"],
              x="Uzun, turli belgilar aralashgan parolni topish juda qiyin."),
            Q("Soxta xat yoki sayt orqali parolni o‘g‘irlash nima deyiladi?", "Fishing", ["Spam", "Brauzer", "Zaxira nusxa"],
              x="Fishing — inglizcha “baliq ovlash” so‘zidan: aldab “ilintirish”."),
            Q("Foydali dastur niqobidagi zararli dastur nima deyiladi?", "Troyan", ["Antivirus", "Brauzer", "Drayver"],
              x="Nomi qadimgi “Troya oti” afsonasidan olingan."),
            Q("Fayllarni shifrlab, ochish uchun pul so‘raydigan dastur qanday ataladi?", "To‘lov talab qiluvchi dastur", ["Antivirus", "Arxivator", "Brauzer"],
              x="Bunday hujumdan zaxira nusxa saqlaydi."),
            Q("Bankdan deb qo‘ng‘iroq qilib, SMS-kodni so‘rashdi. Nima qilasiz?", "Kodni aytmayman", ["Kodni aytaman", "Karta raqamini aytaman", "Parolni ham aytaman"],
              x="Haqiqiy bank xodimi hech qachon SMS-kodni so‘ramaydi."),
            Q("Ikki bosqichli tekshiruv nima?", "Parol va qo‘shimcha kod", ["Ikkita brauzer", "Ikki marta kirish", "Ikki xil antivirus"],
              x="Parol o‘g‘irlansa ham, qo‘shimcha kodsiz hisobga kirib bo‘lmaydi."),
            Q("Fayllarni yo‘qolishdan saqlash uchun nima qilinadi?", "Zaxira nusxa olinadi", ["Hammasi o‘chiriladi", "Parol olib tashlanadi", "Antivirus o‘chiriladi"],
              x="Zaxira nusxa boshqa diskda yoki bulutda saqlanadi."),
            TF("Hamma saytlar uchun bitta parol ishlatish xavfsiz.", False, x="Bitta sayt buzilsa, qolganlariga ham kirib olishadi."),
            TF("Operatsion tizim va dasturlarni yangilab turish xavfsizlikni oshiradi.", True, x="Yangilanishlar topilgan zaif joylarni yopadi."),
            ORDER(S, "SMS kodni hech kimga aytmang"),
            Q("Qaysi sayt manzili fishing bo‘lishi mumkin?", "g00gle-login.com", ["google.com", "mail.google.com", "accounts.google.com"], d=2,
              x="Harflar o‘rniga raqamlar (o → 0) — soxta saytning belgisi."),
            Q("Ochiq (parolsiz) Wi-Fi tarmog‘ida nima qilmagan ma’qul?", "Bank kartasi ma’lumotini kiritish", ["Ob-havoni ko‘rish", "Yangiliklarni o‘qish", "Xaritaga qarash"], d=2,
              x="Ochiq tarmoqda ma’lumotni begonalar ushlab qolishi mumkin."),
            Q("“Men robot emasman” tekshiruvi (CAPTCHA) nima uchun kerak?", "Odamni avtomatik dasturdan ajratish", ["Ekranni tozalash", "Internetni tezlashtirish", "Faylni saqlash"], d=3,
              x="CAPTCHA avtomatik dasturlarning ommaviy ro‘yxatdan o‘tishiga yo‘l qo‘ymaydi."),
            MATCH("Tahdidni himoya bilan juftlang",
                  [("Virus", "antivirus"), ("Fishing", "manzilni tekshirish"), ("Parol o‘g‘irlanishi", "ikki bosqichli tekshiruv"),
                   ("Fayllar yo‘qolishi", "zaxira nusxa"), ("Dasturdagi zaif joy", "yangilash")], d=2,
                  x="Har bir xavfning o‘z himoya usuli bor."),
        ] + _pin)

T.topic("mualliflik", "📜", L("Mualliflik huquqi", "Copyright", "Авторское право"),
        chapter=C4,
        theory="Mualliflik huquqi — ijodkorning o‘z asariga (kitob, maqola, rasm, fotosurat, musiqa, film, kompyuter dasturi) bo‘lgan huquqi. Asar yaratilgan paytdan himoyalanadi.\n"
               "• © belgisi mualliflik huquqini bildiradi. Asardan foydalanish shartlari — litsenziya.\n"
               "• Iqtibos keltirilganda muallif va manba ko‘rsatiladi. Birovning asarini o‘ziniki qilib ko‘rsatish — plagiat.\n"
               "• Ruxsatsiz nusxalash va tarqatish — qaroqchilik. Bepul dasturlar bor, ochiq kodli dasturlarni esa o‘rganish va o‘zgartirish ham mumkin (Linux, LibreOffice).\n"
               "Ba’zi mualliflar asarini ochiq litsenziya (masalan, Creative Commons) bilan erkin foydalanishga beradi.",
        items=[
            Q("Mualliflik huquqi belgisi qaysi?", "©", ["@", "#", "%"],
              x="© — inglizcha copyright so‘zining bosh harfi."),
            Q("Birovning ishini o‘ziniki qilib ko‘rsatish nima deyiladi?", "Plagiat", ["Iqtibos", "Litsenziya", "Zaxira nusxa"],
              x="Plagiat — ilmiy va axloqiy qoidabuzarlik."),
            Q("Asardan parcha keltirganda nima qilish kerak?", "Muallif va manbani ko‘rsatish", ["Hech narsa", "Matnni yashirish", "Muallif nomini o‘chirish"],
              x="Manba ko‘rsatilgan iqtibos — halol foydalanish."),
            Q("Dasturdan foydalanish shartlari yozilgan hujjat nima?", "Litsenziya", ["Kengaytma", "Kolontitul", "Protokol"],
              x="Litsenziyada nima qilish mumkin va mumkin emasligi yoziladi."),
            Q("Qaysi biri mualliflik huquqi bilan himoyalanadi?", "Kompyuter dasturi", ["Ob-havo", "Karra jadvali", "Quyosh chiqishi"],
              x="Dastur ham kitob kabi asar hisoblanadi."),
            Q("Ruxsatsiz nusxalangan film yoki dasturni tarqatish nima deyiladi?", "Qaroqchilik", ["Iqtibos", "Arxivlash", "Litsenziya"],
              x="Qaroqchilik mualliflarga zarar keltiradi."),
            TF("Internetdagi har qanday rasmni ruxsatsiz o‘z nomingizdan sotish mumkin.", False, x="Rasmning muallifi bor, uning ruxsati kerak."),
            TF("Referatda foydalanilgan manbalar ro‘yxatini ko‘rsatish kerak.", True, x="Bu muallif mehnatini hurmat qilish belgisi."),
            ORDER(S, "Iqtibos keltirilganda manba ko‘rsatiladi"),
            Q("Kodi ochiq, uni o‘rganish va o‘zgartirish mumkin bo‘lgan dastur qanday ataladi?", "Ochiq kodli", ["Qaroqchilik", "Troyan", "Yopiq"], d=2,
              x="Masalan, Linux va LibreOffice — ochiq kodli dasturlar."),
            Q("Qaysi ofis dasturi ochiq kodli?", "LibreOffice", ["Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint"], d=2,
              x="LibreOffice bepul va ochiq kodli ofis to‘plami."),
            Q("Mualliflik huquqi asarga qachondan boshlab tegishli bo‘ladi?", "Asar yaratilgan paytdan", ["Faqat 100 yildan keyin", "Faqat sotilganda", "Hech qachon"], d=3,
              x="Asarni maxsus ro‘yxatdan o‘tkazish shart emas."),
            Q("Muallif o‘z asaridan erkin foydalanishga ruxsat beradigan mashhur ochiq litsenziya qaysi?", "Creative Commons", ["Windows", "HTTPS", "Bluetooth"], d=3,
              x="Creative Commons belgisi bor asarlardan shartlariga rioya qilib foydalanish mumkin."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Plagiat", "birovning ishini o‘zlashtirish"), ("Iqtibos", "manbasi ko‘rsatilgan parcha"), ("Litsenziya", "foydalanish shartlari"),
                   ("Qaroqchilik", "ruxsatsiz nusxalash"), ("Ochiq kodli dastur", "kodini o‘zgartirish mumkin"), ("©", "mualliflik belgisi")], d=2,
                  x="Mualliflik huquqiga oid asosiy tushunchalar."),
            Q("Maktab loyihasi uchun internetdan rasm olsangiz, nima qilish to‘g‘ri?", "Muallif va manbani yozish", ["Rasmga o‘z ismingizni yozish", "Hech narsa qilmaslik", "Rasmni yashirib qo‘yish"], d=2,
              x="Manba ko‘rsatilsa, boshqa odamning mehnati hurmat qilinadi."),
            Q("Asarni yaratgan odam kim deyiladi?", "Muallif", ["Provayder", "Server", "O‘quvchi"],
              x="Muallif — ijodkor."),
            Q("Qaysi biri asar hisoblanmaydi?", "Karra jadvali faktlari", ["Sinfdoshingiz chizgan rasm", "Bastakor yozgan kuy", "Shoir yozgan she’r"], d=2,
              x="Oddiy faktlar va raqamlar hech kimning ijodiy asari emas, rasm, kuy va she’r esa asar."),
            TF("O‘zingiz olgan fotosuratning muallifi — o‘zingiz.", True, d=2, x="Fotosurat ham ijodiy asar, uni yaratgan odam muallif."),
            Q("Qaysi harakat qonuniy va halol?", "Litsenziyali dasturni sotib olish", ["Qaroqchi diskni sotish", "Kitobni skanerlab sotish", "Birovning she’rini o‘z nomidan chop etish"], d=2,
              x="Litsenziya dasturdan qonuniy foydalanish huquqini beradi."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["tarmoq", "kiberxavfsizlik", "mualliflik"], chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["olchov", "ikkilik", "sanoq", "mantiq", "jadval", "formula", "hujjat", "taqdimot",
        "blok_sxema", "scratch", "dastur_natija", "tarmoq", "kiberxavfsizlik", "mualliflik"], chapter=C4, level=3)

T.write()
