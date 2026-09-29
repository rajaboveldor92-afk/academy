"""Informatika va axborot texnologiyalari, 5-sinf: assets/data/school/informatics_g5.json va bank_informatics_g5.json.

Mavzular O'zbekiston 5-sinf informatika dasturi yo'nalishida tuzilgan;
qoida va savollar matni — o'zimizniki (darslikdan ko'chirilmagan).
Ikkilik sanoq, o'lchov birliklari, kodlash va algoritm natijalari Python'da hisoblanadi (qo'lda emas).
Maktab kelishuvi: 1 KB = 1024 bayt, 1 MB = 1024 KB va hokazo (1000 li variantlar chalg'ituvchi sifatida ishlatilmaydi).
Qayta yaratish: python3 tool/content/school/informatics_g5.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("informatics", 5, L("Informatika va axborot texnologiyalari", "Computer science and IT", "Информатика и ИТ"))

C1 = "1-chorak. Axborot va uni o‘lchash"
C2 = "2-chorak. Kompyuter va dasturlar"
C3 = "3-chorak. Matn muharriri va algoritmlar"
C4 = "4-chorak. Scratch va internet"


def near(ans, cands, k=4, lo=0):
    """Noto'g'ri variantlar: takrorsiz, javobdan farqli, `lo` dan kichik emas."""
    out = []
    for c in cands:
        if c != ans and c >= lo and c not in out:
            out.append(c)
    return out[:k]


def fmt(n):
    """1048576 → "1 048 576"."""
    return f"{n:,}".replace(",", " ")


def b2(n):
    return bin(n)[2:]


def places(s):
    """Ikkilik yozuvning xona qiymatlari: "1011" → ["8", "0", "2", "1"]."""
    k = len(s)
    return [str(2 ** (k - 1 - i)) if ch == "1" else "0" for i, ch in enumerate(s)]


def split_pow2(n):
    """13 → "8 + 4 + 1"."""
    s = b2(n)
    return " + ".join(p for p in places(s) if p != "0")


# Qoida matnidagi misollarni tekshirib qo'yamiz.
assert int("1011", 2) == 11 and b2(13) == "1101" and b2(6) == "110" and b2(5) == "101"
assert 3 * 1024 == 3072 and 1024 * 8 == 8192

# ============================================================ 1-chorak
T.topic("axborot", "💡", L("Axborot, uning xossalari va turlari", "Information, its properties and types", "Информация, её свойства и виды"),
        chapter=C1,
        theory="Axborot — atrof-olam haqidagi ma’lumotlar.\n"
               "Qabul qilinishiga ko‘ra: ko‘rish, eshitish, hid, ta’m va sezish orqali. Ifodalanishiga ko‘ra: matnli, sonli, grafik, tovushli, video.\n"
               "Xossalari: ishonchli (haqiqatga mos), to‘liq (yetarli), dolzarb (o‘z vaqtida), tushunarli, foydali, aniq.\n"
               "Axborot bilan jarayonlar: yig‘ish, saqlash, uzatish, qayta ishlash, himoyalash.\n"
               "Uzatish: manba → aloqa kanali → qabul qiluvchi. Masalan, telefon suhbati.",
        items=[
            Q("Haqiqatga mos keladigan axborot qanday ataladi?", "Ishonchli", ["Dolzarb", "To‘liq", "Tushunarli"],
              x="Ishonchli axborot voqelikni to‘g‘ri aks ettiradi."),
            Q("O‘z vaqtida olingan, hozir kerakli axborot qanday ataladi?", "Dolzarb", ["Ishonchli", "To‘liq", "Aniq"],
              x="Dolzarb axborot aynan kerak bo‘lgan paytda keladi."),
            Q("Qaror qabul qilish uchun yetarli bo‘lgan axborot qanday ataladi?", "To‘liq", ["Dolzarb", "Tushunarli", "Foydali"],
              x="To‘liq axborotda kerakli hamma ma’lumot bor."),
            Q("Qabul qiluvchi biladigan tilda berilgan axborot qanday ataladi?", "Tushunarli", ["Dolzarb", "To‘liq", "Ishonchli"],
              x="Tushunarli axborotni qabul qiluvchi anglay oladi."),
            Q("Inson eng ko‘p axborotni qaysi sezgi a’zosi orqali oladi?", "Ko‘z", ["Quloq", "Burun", "Til"],
              x="Axborotning eng katta qismini ko‘rish orqali olamiz."),
            MATCH("Axborot turini misol bilan juftlang",
                  [("Matnli", "Gazeta maqolasi"), ("Sonli", "Telefon raqami"), ("Grafik", "Xarita"), ("Tovushli", "Qo‘shiq"), ("Video", "Multfilm")],
                  x="Axborot matn, son, rasm, tovush va video ko‘rinishida ifodalanadi."),
            MATCH("Sezgi a’zosini axborot bilan juftlang",
                  [("Ko‘z", "Kamalak ranglari"), ("Quloq", "Qush sayrashi"), ("Burun", "Atir hidi"), ("Til", "Asalning shirinligi"),
                   ("Teri", "Muzning sovuqligi")], x="Har bir sezgi a’zosi o‘z turdagi axborotni qabul qiladi."),
            Q("Kundalikka dars jadvalini yozish — axborot bilan qanday jarayon?", "Saqlash", ["Uzatish", "Qayta ishlash", "Himoyalash"],
              x="Yozib qo‘yilgan axborot keyinchalik foydalanish uchun saqlanadi."),
            Q("Do‘stga SMS yuborish — axborot bilan qanday jarayon?", "Uzatish", ["Saqlash", "Qayta ishlash", "Yig‘ish"],
              x="Axborot bir odamdan boshqasiga yetkaziladi."),
            Q("Masalani yechish — axborot bilan qanday jarayon?", "Qayta ishlash", ["Uzatish", "Saqlash", "Yig‘ish"],
              x="Berilganlardan yangi axborot — javob hosil qilinadi."),
            Q("Loyiha uchun kitob va saytlardan ma’lumot to‘plash — qanday jarayon?", "Yig‘ish", ["Himoyalash", "Uzatish", "O‘chirish"],
              x="Turli manbalardan axborot to‘planadi."),
            Q("Qaysi biri axborot tashuvchi?", "Fleshka", ["Havo", "Quyosh nuri", "Shamol"],
              x="Axborot tashuvchi — axborot yozib saqlanadigan narsa: kitob, daftar, fleshka, disk."),
            Q("Qaysi axborot grafik turga kiradi?", "Chizma", ["She’r", "Qo‘shiq", "Telefon raqami"],
              x="Grafik axborot — rasm, chizma, xarita, sxema."),
            Q("Qaysi axborot tovushli turga kiradi?", "Radio eshittirishi", ["Fotosurat", "Jadval", "Kitob matni"],
              x="Radioda axborot tovush orqali uzatiladi."),
            Q("Maktabdagi qo‘ng‘iroq chalinishi qanday axborot?", "Tovushli", ["Grafik", "Matnli", "Sonli"],
              x="Qo‘ng‘iroq ovozini quloq bilan eshitamiz."),
            TF("Kitob, daftar va fleshka — axborot tashuvchilar.", True, x="Ularda axborot yozib saqlanadi."),
            Q("Tekshirilmagan mish-mishda qaysi xossa yo‘q?", "Ishonchlilik", ["Tushunarlilik", "Grafiklik", "Ovozlilik"], d=2,
              x="Mish-mish tekshirilmagan, u haqiqatga mos kelmasligi mumkin."),
            Q("Kechagi ob-havo ma’lumoti bugungi sayohatni rejalash uchun qanday axborot?", "Dolzarb emas",
              ["Tushunarsiz", "Grafik", "Juda dolzarb"], d=2, x="Axborot eskirgan: u bugungi kun uchun o‘z vaqtida emas."),
            Q("“Ertaga soat 9 da uchrashamiz” — joyi aytilmagan. Bu axborot qanday?", "To‘liq emas",
              ["Dolzarb emas", "Tushunarsiz", "Grafik"], d=2, x="Qayerda uchrashish kerakligi aytilmagan — ma’lumot yetarli emas."),
            Q("Yapon tilidagi ko‘rsatma yapon tilini bilmaydigan o‘quvchi uchun qanday axborot?", "Tushunarsiz",
              ["To‘liq emas", "Dolzarb emas", "Sonli"], d=2, x="Axborot qabul qiluvchi bilmaydigan tilda berilgan."),
            TF("Oddiy kompyuter hid va ta’m axborotini qabul qila oladi.", False, d=2,
               x="Oddiy kompyuter matn, son, rasm, tovush va video bilan ishlaydi."),
            TF("Buzuq termometr ko‘rsatgan harorat — ishonchli axborot.", False, d=2,
               x="Buzuq asbob noto‘g‘ri ko‘rsatadi, bunday axborotga ishonib bo‘lmaydi."),
            Q("Telefon suhbatida gapirayotgan odam kim hisoblanadi?", "Axborot manbai", ["Qabul qiluvchi", "Aloqa kanali", "Axborot tashuvchi"], d=2,
              x="Axborotni yuborayotgan odam — manba."),
            Q("Kompyuterga parol qo‘yish — axborot bilan qanday jarayon?", "Himoyalash", ["Uzatish", "Yig‘ish", "Qayta ishlash"], d=2,
              x="Parol axborotni begonalardan himoya qiladi."),
            ORDER("So‘zlardan gap tuzing", "Kompyuter axborotni qayta ishlaydi", d=2),
            Q("Telefon suhbatida telefon aloqasi nima vazifasini bajaradi?", "Aloqa kanali", ["Axborot manbai", "Qabul qiluvchi", "Axborot turi"], d=3,
              x="Aloqa kanali orqali axborot manbadan qabul qiluvchiga yetib boradi."),
            TF("Axborotni boshqa odamga aytib bersak, u bizda ham saqlanib qoladi.", True, d=3,
               x="Axborot uzatilganda manbada kamaymaydi: bilimini ulashgan odamda u qoladi."),
        ])

# --- Kodlash: jadval bo'yicha shifrlash savollari Python'da hisoblanadi.
CODE = {"A": 1, "B": 2, "K": 3, "L": 4, "M": 5, "O": 6, "T": 7, "I": 8}
CODE_STR = ", ".join(f"{c}={v}" for c, v in CODE.items())
VOCAB = ["OTA", "OLMA", "KITOB", "BOLA", "LOLA", "TOLA", "MATO", "ILM", "TOM", "ALI"]


def enc(word):
    return "".join(str(CODE[c]) for c in word)


def code_wrongs(word):
    code = enc(word)
    cands = [code[::-1], code[1] + code[0] + code[2:], code[:-2] + code[-1] + code[-2], code[:-1] + str((int(code[-1]) % 8) + 1)]
    cands += [enc(w) for w in VOCAB if len(w) == len(word) and w != word]
    out = []
    for c in cands:
        if c != code and c not in out:
            out.append(c)
    return out[:4]


_code = [
    Q("Kompyuter axborotni qanday belgilar bilan kodlaydi?", "0 va 1", ["A va B", "Nuqta va vergul", "Faqat harflar"],
      x="Kompyuter har qanday axborotni ikkilik kod — 0 va 1 bilan ifodalaydi."),
    Q("Morze alifbosida qanday belgilar ishlatiladi?", "Nuqta va tire", ["Faqat raqamlar", "Ranglar", "Rasmlar"],
      x="Morze alifbosida har bir harf qisqa (nuqta) va uzun (tire) signallar bilan beriladi."),
    Q("Ko‘zi ojiz odamlar barmoq bilan o‘qiydigan yozuv qanday ataladi?", "Brayl alifbosi", ["Morze alifbosi", "Shtrix-kod", "Notalar"],
      x="Brayl alifbosi qog‘ozdagi bo‘rtma nuqtalardan iborat."),
    Q("Musiqa qanday belgilar bilan yoziladi?", "Notalar", ["Shtrix-kod", "Morze alifbosi", "Yo‘l belgilari"],
      x="Notalar — musiqani yozish kodi.", e="🎵"),
    Q("Do‘kondagi mahsulot ustidagi qora-oq chiziqlar nima?", "Shtrix-kod", ["Nota", "Brayl alifbosi", "Morze alifbosi"],
      x="Shtrix-kodda mahsulot haqidagi axborot kodlangan, uni skaner o‘qiydi."),
    Q("Svetoforning qizil rangi qanday axborotni kodlaydi?", "To‘xta", ["Yur", "Tayyorlan", "Tezlashtir"],
      x="Qizil rang — “to‘xta”, yashil — “yur” degan buyruq.", e="🚦"),
    TF("Kodlash — axborotni boshqa belgilar yordamida ifodalash.", True, x="Masalan, so‘zni harflar bilan yozish ham kodlash."),
    TF("Yo‘l belgilari — axborotni kodlashning bir usuli.", True, x="Har bir belgi haydovchi va piyodaga aniq axborot beradi."),
    TF("Bitta axborotni turli usullar bilan kodlash mumkin.", True,
       x=f"Masalan, 5 sonini raqam bilan, “besh” so‘zi bilan yoki ikkilik kodda {b2(5)} deb yozish mumkin."),
    ORDER("So‘zlardan gap tuzing", "Kompyuter axborotni ikkilik kodda saqlaydi", d=2),
    Q("Koddan asl axborotni tiklash nima deyiladi?", "Dekodlash", ["Kodlash", "Saqlash", "Chop etish"], d=2,
      x="Dekodlash — kodlashga teskari jarayon."),
    MATCH("Kodni qo‘llanish joyi bilan juftlang",
          [("Notalar", "Musiqa"), ("Morze alifbosi", "Telegraf"), ("Brayl alifbosi", "Ko‘zi ojizlar"), ("Shtrix-kod", "Do‘kon mahsulotlari"),
           ("Yo‘l belgilari", "Haydovchilar"), ("Ikkilik kod", "Kompyuter")], d=2,
          x="Har bir kod o‘z sohasida ishlatiladi."),
    Q("Telefon kamerasi bilan o‘qiladigan kvadrat shaklidagi kod qanday ataladi?", "QR-kod", ["Morze kodi", "Nota", "Brayl kodi"], d=2,
      x="QR-kodda sayt manzili yoki matn kodlangan bo‘ladi."),
    Q("Axborotni begonalar tushunmasligi uchun maxfiy kodlash nima deyiladi?", "Shifrlash", ["Chop etish", "Skanerlash", "Nusxalash"], d=2,
      x="Shifrlangan axborotni faqat kalitni biladigan odam o‘qiy oladi."),
    Q("Harflar qanday axborotni kodlaydi?", "Nutqni", ["Musiqani", "Ranglarni", "Haroratni"], d=2,
      x="Harflar yordamida og‘zaki nutqni yozib qo‘yamiz."),
    Q("SOS yordam signali qaysi kod bilan uzatiladi?", "Morze alifbosi", ["Brayl alifbosi", "Shtrix-kod", "Notalar"], d=3,
      x="SOS — Morze alifbosidagi yordam signali: uchta nuqta, uchta tire, uchta nuqta."),
    Q("Brayl alifbosining bitta belgisi nechta nuqtali katakda yoziladi?", "6", ["2", "4", "10"], d=3,
      x="Brayl katagida 6 ta nuqta bor, ulardan qaysilari bo‘rtib turishi harfni bildiradi."),
]
for word, d in [("OTA", 1), ("OLMA", 2), ("KITOB", 3)]:
    code = enc(word)
    _code.append(Q(f"Kod jadvali: {CODE_STR}. “{word}” so‘zi qanday kodlanadi?", code, code_wrongs(word), d=d,
                   x=f"Har bir harfni jadvaldagi raqam bilan almashtiramiz: {word} → {code}."))
for word, d in [("BOLA", 1), ("MATO", 2), ("TOLA", 2)]:
    code = enc(word)
    wrongs = [w for w in VOCAB if w != word and len(w) == len(word)][:3] + [w for w in VOCAB if len(w) != len(word)][:1]
    _code.append(Q(f"Kod jadvali: {CODE_STR}. “{code}” kodi qaysi so‘zni bildiradi?", word, wrongs, d=d,
                   x=f"Har bir raqamni jadvaldagi harf bilan almashtiramiz: {code} → {word}."))
for w in ["OTA", "OLMA", "KITOB", "BOLA", "MATO", "TOLA"] + VOCAB:
    assert all(c in CODE for c in w)

T.topic("kodlash", "🔐", L("Axborotni kodlash", "Encoding information", "Кодирование информации"),
        chapter=C1,
        theory="Kod — axborotni ifodalash uchun belgilar va ularni qo‘llash qoidasi.\n"
               "Kodlash — axborotni kodga aylantirish, dekodlash — koddan asl axborotni tiklash.\n"
               "Misollar: harflar — nutq kodi, notalar — musiqa kodi, Morze alifbosi — nuqta va tire, Brayl alifbosi — ko‘zi ojizlar uchun bo‘rtma nuqtalar, shtrix-kod va QR-kod.\n"
               f"Kompyuter har qanday axborotni faqat ikkita belgi — 0 va 1 bilan kodlaydi (ikkilik kod). Masalan, 5 soni — {b2(5)}.",
        items=_code)

_units = [
    Q("Axborotning eng kichik o‘lchov birligi qaysi?", "Bit", ["Bayt", "Kilobayt", "Megabayt"],
      x="Bit — bitta 0 yoki 1, bundan kichik birlik yo‘q."),
    Q("1 bayt necha bitga teng?", 8, [2, 10, 16, 1024], x="1 bayt = 8 bit."),
    Q("1 KB necha baytga teng?", 1024, [100, 8, 10, 512], x="Maktab informatikasida 1 KB = 1024 bayt."),
    Q("1 MB necha KB ga teng?", 1024, [8, 100, 10, 512], x="1 MB = 1024 KB."),
    Q("1 GB necha MB ga teng?", 1024, [8, 100, 512, 10], x="1 GB = 1024 MB."),
    Q("Qaysi birlik eng katta?", "Terabayt", ["Gigabayt", "Megabayt", "Kilobayt"],
      x="Tartib: bit, bayt, KB, MB, GB, TB — terabayt eng katta."),
    MATCH("Birlikni teng qiymati bilan juftlang",
          [("1 bayt", "8 bit"), ("1 KB", "1024 bayt"), ("1 MB", "1024 KB"), ("1 GB", "1024 MB"), ("1 TB", "1024 GB")],
          x="Baytdan boshlab har bir keyingi birlik oldingisidan 1024 marta katta."),
    TF("1 bit — bitta 0 yoki 1.", True, x="Bit ikkilik kodning bitta xonasi."),
    TF("Megabayt kilobaytdan katta.", True, x="1 MB = 1024 KB."),
    Q("1 TB necha GB ga teng?", 1024, [8, 100, 512, 10], d=2, x="1 TB = 1024 GB."),
    Q("Qaysi qatorda birliklar kichigidan kattasiga qarab yozilgan?", "bit, bayt, KB, MB",
      ["bayt, bit, KB, MB", "KB, bayt, MB, GB", "MB, KB, GB, TB"], d=2, x="To‘g‘ri tartib: bit < bayt < KB < MB < GB < TB."),
    TF("1 KB = 1024 bit.", False, d=2, x=f"1 KB = 1024 bayt = {fmt(1024 * 8)} bit."),
    Q("Qaysi axborot hajmi eng katta?", "1 MB", ["900 KB", "1000 bayt", "8000 bit"], d=2,
      x=f"1 MB = {fmt(1024 * 1024)} bayt, 900 KB = {fmt(900 * 1024)} bayt — 1 MB eng katta."),
    Q("Qaysi axborot hajmi eng kichik?", "16 bit", ["3 bayt", "1 KB", "1 MB"], d=2, x="16 bit = 2 bayt, bu 3 baytdan ham kichik."),
    Q("Qaysi axborot hajmi eng katta?", "2 GB", ["1500 MB", "1 GB", "900 MB"], d=3, x=f"2 GB = {fmt(2 * 1024)} MB, bu 1500 MB dan katta."),
]
assert 1024 * 1024 > 900 * 1024 and 16 // 8 < 3 and 2 * 1024 > 1500
for n, d in [(2, 1), (3, 1), (5, 2)]:
    v = 8 * n
    _units.append(Q(f"{n} bayt necha bit?", v, near(v, [v + 8, v - 8, n * 10, n * 2, n + 8]), d=d,
                    x=f"1 bayt = 8 bit, shuning uchun {n} bayt = {n} · 8 = {v} bit."))
for bits, d in [(16, 1), (32, 2), (64, 2)]:
    n = bits // 8
    _units.append(Q(f"{bits} bit necha bayt?", n, near(n, [n + 1, n - 1, n * 2, bits * 8, bits - 8], lo=1), d=d,
                    x=f"Bitdan baytga o‘tishda 8 ga bo‘lamiz: {bits} : 8 = {n}."))
for n, d in [(2, 1), (3, 2), (4, 2)]:
    v = 1024 * n
    _units.append(Q(f"{n} KB necha bayt?", v, near(v, [v + 1024, v - 1024, 8 * n, 512 * n, v * 8], lo=1), d=d,
                    x=f"1 KB = 1024 bayt, shuning uchun {n} KB = {n} · 1024 = {v} bayt."))
for v, d in [(2048, 2), (5120, 3)]:
    n = v // 1024
    _units.append(Q(f"{v} bayt necha KB?", n, near(n, [n + 1, n - 1, n * 8, n * 2], lo=1), d=d,
                    x=f"Baytdan KB ga o‘tishda 1024 ga bo‘lamiz: {v} : 1024 = {n}."))
for n, d in [(2, 2), (5, 3)]:
    v = 1024 * n
    _units.append(Q(f"{n} MB necha KB?", v, near(v, [v + 1024, v - 1024, 8 * n, 512 * n], lo=1), d=d,
                    x=f"1 MB = 1024 KB, shuning uchun {n} MB = {v} KB."))
for n, d in [(2, 2), (4, 3)]:
    v = 1024 * n
    _units.append(Q(f"{n} GB necha MB?", v, near(v, [v + 1024, v - 1024, 8 * n, 512 * n], lo=1), d=d,
                    x=f"1 GB = 1024 MB, shuning uchun {n} GB = {v} MB."))
_units.append(Q("1 KB necha bit?", fmt(8192), [fmt(v) for v in [1024, 8, 4096, 16384]], d=3,
                x=f"1 KB = 1024 bayt, 1024 · 8 = {fmt(1024 * 8)} bit."))
_units.append(Q("1 MB necha bayt?", fmt(1024 * 1024), [fmt(v) for v in [1024, 8 * 1024 * 1024, 512 * 1024, 2 * 1024 * 1024]], d=3,
                x=f"1 MB = 1024 KB = 1024 · 1024 = {fmt(1024 * 1024)} bayt."))
_units.append(Q("Fleshka hajmi 16 GB. Bu necha MB?", fmt(16 * 1024), [fmt(v) for v in [1024, 2048, 8192, 32768]], d=3,
                x=f"16 · 1024 = {fmt(16 * 1024)} MB."))
_units.append(Q("Bitta rasm 3 MB. Telefonda 30 MB bo‘sh joy bor. Nechta shunday rasm sig‘adi?", 30 // 3, [3, 9, 27, 33], d=2,
                x=f"30 : 3 = {30 // 3}."))
for word, unit, d in [("KITOB", "bayt", 2), ("INFORMATIKA", "bayt", 2), ("KOMPYUTER", "bit", 3)]:
    n = len(word)
    v = n if unit == "bayt" else n * 8
    wr = near(v, [v + 1, v - 1, n * 8 if unit == "bayt" else n, v + 8, v * 2], lo=1)
    _units.append(Q(f"Har bir harf 1 bayt bilan kodlansa, “{word}” so‘zi necha {unit} joy egallaydi?", v, wr, d=d,
                    x=f"“{word}” so‘zida {n} ta harf bor: {n} bayt" + (f" = {n} · 8 = {v} bit." if unit == "bit" else ".")))
for n, d in [(1, 2), (2, 2), (3, 3), (4, 3), (8, 3)]:
    v = 2 ** n
    _units.append(Q(f"{n} bit yordamida nechta turli kod hosil qilish mumkin?", v, near(v, [2 * n, n, v + 2, 2 ** (n + 1), n * n, v - 1], lo=1), d=d,
                    x=f"Har bir bit 2 xil qiymat oladi, {n} bit — 2 ni {n} marta ko‘paytiramiz: {v} ta kod."))
_units.append(Q("3 ta chiroqning har biri yoniq yoki o‘chiq bo‘lishi mumkin. Nechta turli signal berish mumkin?", 2 ** 3, [3, 6, 9, 16], d=3,
                x=f"Har bir chiroq — 2 holat: 2 · 2 · 2 = {2 ** 3}."))

T.topic("olchov", "📏", L("Axborot o‘lchov birliklari", "Units of information", "Единицы измерения информации"),
        chapter=C1,
        theory="Axborotning eng kichik o‘lchov birligi — bit. Bir bit — bitta 0 yoki 1.\n"
               "• 1 bayt = 8 bit;  1 KB (kilobayt) = 1024 bayt.\n"
               "• 1 MB (megabayt) = 1024 KB;  1 GB (gigabayt) = 1024 MB;  1 TB (terabayt) = 1024 GB.\n"
               "Katta birlikdan kichigiga o‘tishda ko‘paytiramiz, kichigidan kattasiga o‘tishda bo‘lamiz: baytdan bitga — 8 ga, qolganlarida — 1024 ga.\n"
               f"Misol: 3 KB = 3 · 1024 = {3 * 1024} bayt;  16 bit = 16 : 8 = {16 // 8} bayt.",
        items=_units)

_bin = [
    Q("Ikkilik sanoq sistemasida nechta raqam bor?", 2, [10, 8, 1], x="Ikkilik sistemada faqat ikkita raqam: 0 va 1."),
    Q("Ikkilik sanoq sistemasining raqamlari qaysilar?", "0 va 1", ["1 va 2", "0 dan 9 gacha", "1 dan 10 gacha"],
      x="Ikkilik sistemada faqat 0 va 1 ishlatiladi."),
    Q("O‘nlik sanoq sistemasida nechta raqam bor?", 10, [2, 8, 9], x="O‘nlik sistemada 0 dan 9 gacha 10 ta raqam bor."),
    TF("Kompyuter ichida sonlar ikkilik sanoq sistemasida saqlanadi.", True, x="Kompyuter xotirasi faqat 0 va 1 ni saqlaydi."),
    Q("Qaysi yozuv ikkilik son bo‘la olmaydi?", "102", ["101", "110", "111"],
      x="Ikkilik sonda faqat 0 va 1 raqamlari bo‘ladi, 2 raqami bo‘lmaydi."),
    Q("Qaysi yozuv ikkilik son bo‘la oladi?", "1001", ["1201", "3001", "1009"], x="1001 da faqat 0 va 1 raqamlari bor."),
    Q("Ikkilik sonda o‘ngdan uchinchi xonaning qiymati nechaga teng?", 4, [3, 8, 2], d=2,
      x="Xona qiymatlari o‘ngdan: 1, 2, 4, 8 — uchinchisi 4."),
    Q("Ikkilik sonda o‘ngdan to‘rtinchi xonaning qiymati nechaga teng?", 8, [4, 16, 6], d=2,
      x="Xona qiymatlari o‘ngdan: 1, 2, 4, 8 — to‘rtinchisi 8."),
    TF("Ikkilikdagi 10 soni o‘nlikdagi 10 ga teng.", False, d=2, x=f"Ikkilikdagi 10 — bu o‘nlikdagi {int('10', 2)}."),
    Q("Ikkilikda sanaganda 11 dan keyin qaysi son keladi?", b2(int("11", 2) + 1), ["12", "111", "20"], d=2,
      x=f"11 = {int('11', 2)}, keyingisi {int('11', 2) + 1} = {b2(int('11', 2) + 1)}."),
    Q("8 soni ikkilikda necha xonali?", len(b2(8)), [3, 8, 1], d=2, x=f"8 = {b2(8)} — {len(b2(8))} xonali."),
    TF("Ikkilikdagi 1000 soni ikkilikdagi 111 sonidan katta.", int("1000", 2) > int("111", 2), d=2,
       x=f"1000 = {int('1000', 2)}, 111 = {int('111', 2)}."),
    Q("Eng kichik uch xonali ikkilik son qaysi?", "100", ["111", "001", "101"], d=2,
      x=f"Uch xonali son 1 bilan boshlanadi, eng kichigi 100 = {int('100', 2)}."),
    MATCH("O‘nlik sonni ikkilik yozuvi bilan juftlang", [(str(n), b2(n)) for n in range(1, 9)], d=2,
          x="Xona qiymatlari 8, 4, 2, 1 yordamida tekshiring."),
    Q("Ikkilik sanoq sistemasida 1 + 1 yig‘indisi qanday yoziladi?", b2(1 + 1), ["11", "0", "1"], d=3,
      x=f"1 + 1 = 2, ikkilikda esa 2 = {b2(2)}."),
    Q("4 xonali eng katta ikkilik son o‘nlikda nechaga teng?", int("1111", 2), [16, 14, 8], d=3,
      x=f"1111 = 8 + 4 + 2 + 1 = {int('1111', 2)}."),
    TF("Ikkilikda 0 bilan tugaydigan son juft bo‘ladi.", True, d=3,
       x="Oxirgi xona qiymati 1; u 0 bo‘lsa, son faqat 2, 4, 8 … lardan yig‘iladi va juft bo‘ladi."),
    MATCH("O‘nlik sonni ikkilik yozuvi bilan juftlang ", [(str(n), b2(n)) for n in range(9, 16)], d=3,
          x="Masalan, 13 = 8 + 4 + 1 = 1101."),
]
assert b2(2) == "10" and int("1111", 2) == 15 and all(n % 2 == 0 for n in range(1, 16) if b2(n).endswith("0"))
for n in range(2, 16):
    s = b2(n)
    d = 1 if n <= 5 else (2 if n <= 10 else 3)
    cands = [n ^ 1, n + 1, n - 1, n ^ 2, n + 2, n - 2, n ^ 4]
    rev = s[::-1]
    if not rev.startswith("0"):
        cands.insert(2, int(rev, 2))
    wrong = []
    for m in cands:
        if m >= 1 and m != n and b2(m) not in wrong:
            wrong.append(b2(m))
    _bin.append(Q(f"O‘nlik sistemadagi {n} sonini ikkilik sistemada yozing.", s, wrong[:4], d=d,
                  x=f"{n} = {split_pow2(n)}, shuning uchun {n} = {s}."))
for n in range(2, 16):
    s = b2(n)
    d = 1 if n <= 5 else (2 if n <= 10 else 3)
    cands = [n + 1, n - 1, int(s[::-1], 2), n + 2, int(s), n - 2]
    wrong = near(n, cands, lo=0)
    _bin.append(Q(f"Ikkilik sistemadagi {s} sonini o‘nlik sistemaga o‘tkazing.", n, wrong, d=d,
                  x=f"{s} = {' + '.join(places(s))} = {n}."))
    assert int(s, 2) == n and sum(int(p) for p in places(s)) == n

_ex = "1011"
T.topic("ikkilik", "🔢", L("Ikkilik sanoq sistemasi", "The binary number system", "Двоичная система счисления"),
        chapter=C1,
        theory="Biz o‘nlik sanoq sistemasida 10 ta raqam (0–9) bilan sanaymiz. Kompyuter esa ikkilik sanoq sistemasida ishlaydi: faqat 2 ta raqam — 0 va 1.\n"
               "Ikkilik sonda xona qiymatlari o‘ngdan chapga: 1, 2, 4, 8, 16 … — har biri oldingisidan 2 marta katta.\n"
               f"• Ikkilikdan o‘nlikka: 1 turgan xonalar qiymatini qo‘shamiz: {_ex} → {' + '.join(places(_ex))} = {int(_ex, 2)}.\n"
               f"• O‘nlikdan ikkilikka: sonni xona qiymatlari yig‘indisiga ajratamiz: 13 = {split_pow2(13)} → {b2(13)}.\n"
               f"Sanash: {', '.join(b2(i) for i in range(9))} …",
        items=_bin)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["axborot", "kodlash", "olchov", "ikkilik"], chapter=C1)

# ============================================================ 2-chorak
T.topic("kompyuter_tuzilishi", "🖥️", L("Kompyuter tuzilishi", "How a computer is built", "Устройство компьютера"),
        chapter=C2,
        theory="Kompyuter axborotni qabul qiladi, saqlaydi, qayta ishlaydi va uzatadi.\n"
               "• Protsessor — kompyuterning “miyasi”: barcha hisob-kitob va buyruqlarni bajaradi.\n"
               "• Operativ xotira — ishlayotgan dastur va ma’lumotlar vaqtincha turadigan tezkor xotira; kompyuter o‘chsa, undagi ma’lumot o‘chib ketadi.\n"
               "• Doimiy xotira — qattiq disk yoki SSD: fayllar kompyuter o‘chganda ham saqlanadi. SSD qattiq diskdan tezroq ishlaydi.\n"
               "• Fleshka va xotira kartasi — ko‘chma xotira. Barcha qismlar ona plataga ulanadi.",
        items=[
            Q("Kompyuterning “miyasi” deb qaysi qism ataladi?", "Protsessor", ["Monitor", "Klaviatura", "Karnay"],
              x="Protsessor barcha hisob-kitob va buyruqlarni bajaradi."),
            Q("Kompyuter o‘chirilganda qaysi xotiradagi ma’lumot o‘chib ketadi?", "Operativ xotira", ["Qattiq disk", "Fleshka", "SSD"],
              x="Operativ xotira faqat kompyuter ishlab turganda ma’lumotni saqlaydi."),
            Q("Fayllar uzoq muddat qayerda saqlanadi?", "Qattiq diskda", ["Operativ xotirada", "Protsessorda", "Monitorda"],
              x="Qattiq disk — doimiy xotira, undagi fayllar kompyuter o‘chganda ham qoladi."),
            Q("Faylni boshqa kompyuterga olib o‘tish uchun qaysi qurilma qulay?", "Fleshka", ["Protsessor", "Operativ xotira", "Ona plata"],
              x="Fleshka — kichik ko‘chma xotira, uni USB uyaga ulaymiz."),
            Q("Stol kompyuterida protsessor, xotira va ona plata qayerda joylashgan?", "Tizim blokida", ["Monitorda", "Klaviaturada", "Printerda"],
              x="Asosiy qismlar tizim bloki ichida bo‘ladi."),
            TF("Operativ xotiradagi ma’lumot kompyuter o‘chganda ham saqlanib qoladi.", False,
               x="Operativ xotira kompyuter o‘chganda tozalanadi."),
            TF("Fleshka — ko‘chma xotira qurilmasi.", True, x="Fleshkani bir kompyuterdan boshqasiga olib o‘tish mumkin."),
            TF("Qattiq disk — doimiy xotira.", True, x="Qattiq diskdagi fayllar tok o‘chganda ham saqlanadi."),
            Q("Qaysi biri kiritish qurilmasi?", "Skaner", ["Printer", "Monitor", "Karnay"], x="Skaner qog‘ozdagi tasvirni kompyuterga kiritadi."),
            Q("Klaviaturadan harf kiritildi, protsessor uni qayta ishladi. Keyin harf qayerda ko‘rinadi?", "Monitorda",
              ["Mikrofonda", "Skanerda", "Sichqonchada"], x="Natija chiqarish qurilmasi — monitorda ko‘rinadi."),
            Q("Noutbuk qanday kompyuter?", "Ko‘chma kompyuter", ["Faqat printer", "Katta televizor", "Faqat skaner"],
              x="Noutbukda barcha qismlar bitta yig‘ma korpusda, uni ko‘tarib yurish mumkin.", e="💻"),
            Q("Kompyuterning barcha qismlari ulanadigan asosiy plata nima deb ataladi?", "Ona plata", ["Videokarta", "Fleshka", "Monitor"], d=2,
              x="Ona plata protsessor, xotira va boshqa qismlarni bir-biri bilan bog‘laydi."),
            Q("Tasvirni monitorga chiqarishga javob beradigan qism qaysi?", "Videokarta", ["Ovoz kartasi", "Quvvat bloki", "Fleshka"], d=2,
              x="Videokarta tasvirni tayyorlab, monitorga uzatadi."),
            Q("Kompyuter qismlarini elektr bilan ta’minlaydigan qism qaysi?", "Quvvat bloki", ["Protsessor", "Videokarta", "Qattiq disk"], d=2,
              x="Quvvat bloki rozetkadagi tokni kompyuter qismlariga mos holga keltiradi."),
            TF("SSD qattiq diskka qaraganda tezroq ishlaydi.", True, d=2,
               x="SSD da aylanadigan qismlar yo‘q, u ma’lumotni tezroq o‘qiydi va yozadi."),
            MATCH("Qismni vazifasi bilan juftlang",
                  [("Protsessor", "Hisob-kitobni bajaradi"), ("Operativ xotira", "Vaqtincha saqlaydi"), ("Qattiq disk", "Fayllarni doimiy saqlaydi"),
                   ("Videokarta", "Tasvirni chiqaradi"), ("Quvvat bloki", "Elektr bilan ta’minlaydi"), ("Ona plata", "Qismlarni bog‘laydi")], d=2,
                  x="Kompyuterning har bir qismi o‘z vazifasini bajaradi."),
            Q("Qaysi biri chiqarish qurilmasi?", "Proyektor", ["Mikrofon", "Klaviatura", "Skaner"], d=2,
              x="Proyektor tasvirni devorga yoki ekranga chiqaradi."),
            Q("Telefon va fotoapparatda ishlatiladigan kichik ko‘chma xotira nima?", "Xotira kartasi", ["Qattiq disk", "Protsessor", "Videokarta"], d=2,
              x="Xotira kartasi rasm, video va boshqa fayllarni saqlaydi."),
            Q("Operativ xotira hajmi odatda qaysi birlikda o‘lchanadi?", "Gigabayt", ["Metr", "Kilogramm", "Litr"], d=2,
              x="Masalan, kompyuterda 8 GB operativ xotira bo‘lishi mumkin."),
            Q("Kompyuter qanday tartibda ishlaydi?", "Kiritish → qayta ishlash → chiqarish",
              ["Chiqarish → kiritish → qayta ishlash", "Qayta ishlash → chiqarish → kiritish", "Chiqarish → qayta ishlash → kiritish"], d=2,
              x="Avval axborot kiritiladi, protsessor uni qayta ishlaydi, natija chiqariladi."),
            Q("Kompyuterning qurilmalari birgalikda qanday ataladi?", "Apparat ta’minoti", ["Dasturiy ta’minot", "Operatsion tizim", "Amaliy dastur"], d=2,
              x="Apparat ta’minoti — kompyuterning qo‘l bilan ushlab ko‘rish mumkin bo‘lgan qismlari."),
            Q("Qaysi qurilma ham kiritish, ham chiqarish vazifasini bajaradi?", "Sensorli ekran", ["Printer", "Mikrofon", "Karnay"], d=2,
              x="Sensorli ekran tasvirni ko‘rsatadi va barmoq tegishini qabul qiladi."),
            ORDER("So‘zlardan gap tuzing", "Protsessor barcha buyruqlarni bajaradi", d=2),
            Q("CD va DVD disklar qanday xotira?", "Optik disk", ["Operativ xotira", "Protsessor", "Ona plata"], d=3,
              x="CD va DVD dagi ma’lumot lazer nuri yordamida o‘qiladi."),
        ])

T.topic("dasturiy", "💿", L("Dasturiy ta’minot", "Software", "Программное обеспечение"),
        chapter=C2,
        theory="Dastur — kompyuter bajaradigan buyruqlar to‘plami. Kompyuterdagi barcha dasturlar — dasturiy ta’minot, qurilmalar esa apparat ta’minoti.\n"
               "• Operatsion tizim — kompyuterni boshqaradigan asosiy dastur: Windows, Linux, macOS; telefonlarda — Android, iOS.\n"
               "• Amaliy dasturlar — aniq ish uchun: matn muharriri (Word), grafik muharrir (Paint), brauzer (Chrome), o‘yinlar, pleyerlar.\n"
               "• Antivirus kompyuterni viruslardan himoya qiladi.\n"
               "Operatsion tizimsiz kompyuterda boshqa dasturlar ishlamaydi.",
        items=[
            Q("Kompyuterni boshqaradigan asosiy dastur nima deb ataladi?", "Operatsion tizim", ["Brauzer", "O‘yin", "Matn muharriri"],
              x="Operatsion tizim qurilmalar va boshqa dasturlarning ishini boshqaradi."),
            Q("Qaysi biri operatsion tizim?", "Windows", ["Paint", "Word", "Chrome"], x="Windows — Microsoft kompaniyasining operatsion tizimi."),
            Q("Qaysi biri operatsion tizim?", "Linux", ["Excel", "Scratch", "Paint"], x="Linux — bepul tarqatiladigan operatsion tizim."),
            Q("Ko‘pchilik smartfonlarda qaysi operatsion tizim o‘rnatilgan?", "Android", ["Paint", "Word", "Scratch"],
              x="Android — smartfon va planshetlar uchun operatsion tizim.", e="📱"),
            Q("Matn yozish uchun qaysi dastur mo‘ljallangan?", "Word", ["Paint", "Windows", "Antivirus"], x="Word — matn muharriri."),
            Q("Internet sahifalarini ko‘rish uchun qaysi dastur kerak?", "Brauzer", ["Paint", "Kalkulyator", "Antivirus"],
              x="Brauzer veb-sahifalarni ochib ko‘rsatadi."),
            Q("Kompyuterni viruslardan qaysi dastur himoya qiladi?", "Antivirus", ["Paint", "Brauzer", "Pleyer"],
              x="Antivirus zararli dasturlarni topib zararsizlantiradi."),
            MATCH("Dasturni vazifasi bilan juftlang",
                  [("Word", "Matn yozish"), ("Paint", "Rasm chizish"), ("Chrome", "Saytlarni ko‘rish"), ("Kalkulyator", "Hisoblash"),
                   ("Antivirus", "Viruslardan himoya"), ("Scratch", "Dastur tuzish")],
                  x="Har bir amaliy dastur o‘z ishiga mo‘ljallangan."),
            TF("Paint — operatsion tizim.", False, x="Paint — rasm chizish uchun amaliy dastur."),
            Q("Qaysi biri brauzer?", "Google Chrome", ["Windows", "Paint", "Word"], x="Google Chrome — keng tarqalgan brauzer."),
            Q("Musiqa va video ijro etadigan dastur qanday ataladi?", "Media pleyer", ["Antivirus", "Matn muharriri", "Operatsion tizim"],
              x="Pleyer audio va video fayllarni ijro etadi."),
            Q("Dasturlarni kim yaratadi?", "Dasturchi", ["Shifokor", "Oshpaz", "Haydovchi"], x="Dasturchi dasturlash tilida dastur yozadi."),
            ORDER("So‘zlardan gap tuzing", "Windows operatsion tizim hisoblanadi"),
            Q("Apple kompyuterlarida qaysi operatsion tizim ishlaydi?", "macOS", ["Android", "Paint", "Word"], d=2,
              x="macOS — Apple kompaniyasining kompyuterlar uchun operatsion tizimi."),
            Q("iPhone telefonlarida qaysi operatsion tizim ishlaydi?", "iOS", ["Windows", "Android", "Paint"], d=2,
              x="iOS — Apple kompaniyasining telefonlar uchun operatsion tizimi."),
            TF("Operatsion tizimsiz kompyuterda boshqa dasturlar ishlamaydi.", True, d=2,
               x="Amaliy dasturlar operatsion tizim yordamida ishga tushadi."),
            Q("Aniq bir ishni bajarish uchun mo‘ljallangan dasturlar qanday ataladi?", "Amaliy dasturlar",
              ["Operatsion tizimlar", "Qurilmalar", "Viruslar"], d=2, x="Matn muharriri, grafik muharrir, o‘yinlar — amaliy dasturlar."),
            Q("Kompyuterdagi barcha dasturlar birgalikda qanday ataladi?", "Dasturiy ta’minot", ["Apparat ta’minoti", "Ona plata", "Tizim bloki"], d=2,
              x="Dasturiy ta’minot — kompyuterdagi barcha dasturlar majmui."),
            Q("Dastur o‘rnatish nima?", "Uni kompyuterga yozib, ishga tayyorlash", ["Uni o‘chirish", "Uni chop etish", "Uni savatga tashlash"], d=2,
              x="O‘rnatilgan dastur kompyuterda ishga tushirishga tayyor bo‘ladi."),
            Q("Kompyuterda jadval tuzib, hisoblash uchun qaysi dastur mos?", "Excel", ["Paint", "Bloknot", "Pleyer"], d=2,
              x="Excel — elektron jadvallar dasturi."),
            Q("Taqdimot slaydlarini tayyorlash uchun qaysi dastur mos?", "PowerPoint", ["Paint", "Kalkulyator", "Antivirus"], d=2,
              x="PowerPoint — taqdimot tayyorlash dasturi."),
            TF("Dasturlarni faqat ishonchli saytlardan yuklab olish kerak.", True, d=2,
               x="Noma’lum saytdan olingan dasturda virus bo‘lishi mumkin."),
            Q("Qaysi biri bepul tarqatiladigan operatsion tizim?", "Linux", ["Paint", "Word", "Excel"], d=2,
              x="Linux — bepul va ochiq kodli operatsion tizim; qolganlari amaliy dasturlar."),
        ])

_ext_files = [("bayram.jpg", "Rasm"), ("sayohat.png", "Rasm"), ("tabiat.mp3", "Musiqa"), ("loyiha.mp4", "Video"),
              ("insho.docx", "Matn"), ("eslatma.txt", "Matn"), ("dars.pptx", "Taqdimot"), ("baholar.xlsx", "Elektron jadval")]
_ext_cats = ["Rasm", "Musiqa", "Video", "Matn", "Taqdimot", "Elektron jadval"]
_ext_rev = [("rasm", "sayohat.jpg"), ("musiqa", "sayohat.mp3"), ("video", "sayohat.mp4"), ("matn", "sayohat.docx"),
            ("taqdimot", "sayohat.pptx")]
_ext_same = ["sayohat.jpg", "sayohat.mp3", "sayohat.mp4", "sayohat.docx", "sayohat.pptx", "sayohat.xlsx"]

_files = [
    Q("Fayl nomidagi nuqtadan keyingi qism nima deb ataladi?", "Kengaytma", ["Papka", "Manzil", "Belgi"],
      x="Kengaytma fayl turini bildiradi: dars.docx faylida kengaytma — docx."),
    Q("Kengaytma nimani bildiradi?", "Fayl turini", ["Fayl hajmini", "Yaratilgan kunni", "Muallifni"],
      x="Kengaytma bo‘yicha kompyuter faylni qaysi dasturda ochishni biladi."),
    MATCH("Kengaytmani fayl turi bilan juftlang",
          [(".txt", "Oddiy matn"), (".mp3", "Musiqa"), (".mp4", "Video"), (".jpg", "Rasm"), (".pptx", "Taqdimot"), (".xlsx", "Elektron jadval")],
          x="Kengaytma fayl turini ko‘rsatadi."),
    TF("Papka ichida boshqa papka bo‘lishi mumkin.", True, x="Papkalar ichma-ich joylashishi mumkin."),
    Q("Faylni o‘chirganda u avval qayerga tushadi?", "Savatga", ["Fleshkaga", "Printerga", "Internetga"],
      x="Savat tozalanmaguncha faylni qayta tiklash mumkin."),
    Q("Fayl hajmi qanday birliklarda o‘lchanadi?", "Bayt, KB, MB", ["Metr, santimetr", "Kilogramm, gramm", "Litr, millilitr"],
      x="Fayl hajmi axborot o‘lchov birliklarida ifodalanadi."),
    ORDER("So‘zlardan gap tuzing", "Kengaytma fayl turini bildiradi"),
    Q("“dars.docx” faylida kengaytma qaysi?", "docx", ["dars", "dars.docx", "doc"], d=2,
      x="Kengaytma — nuqtadan keyingi qism: docx."),
    Q("“oila.jpg” faylining kengaytmasiz nomi qaysi?", "oila", ["jpg", "oila.jpg", ".jpg"], d=2,
      x="Nuqtagacha bo‘lgan qism — faylning nomi."),
    Q("“kitob.pdf” fayli ko‘pincha nima bo‘ladi?", "Hujjat yoki kitob", ["Musiqa", "Video", "O‘yin"], d=2,
      x="PDF formatida hujjat va kitoblar saqlanadi."),
    Q("Fayl manzili: C:\\Maktab\\Rasmlar\\gul.jpg. gul.jpg qaysi papkada turibdi?", "Rasmlar", ["Maktab", "C", "gul"], d=2,
      x="Fayl nomidan oldingi papka — Rasmlar; u esa Maktab papkasi ichida."),
    TF("Bitta papkada nomi va kengaytmasi bir xil bo‘lgan ikkita fayl bo‘lishi mumkin.", False, d=2,
       x="Bir papkada to‘liq nomi bir xil bo‘lgan ikkita fayl saqlanmaydi."),
    Q("Fayl nomini o‘zgartirish qanday ataladi?", "Qayta nomlash", ["Nusxalash", "O‘chirish", "Ko‘chirish"], d=2,
      x="Qayta nomlashda faqat nom o‘zgaradi, mazmun o‘zgarmaydi."),
    Q("Faylning nusxasi boshqa papkada paydo bo‘lib, asli ham joyida qolsa, bu nima?", "Nusxalash", ["Ko‘chirish", "O‘chirish", "Qayta nomlash"], d=2,
      x="Nusxalashda fayl ikkita bo‘ladi."),
    Q("Fayl asl joyidan yo‘qolib, boshqa papkada paydo bo‘lsa, bu nima?", "Ko‘chirish", ["Nusxalash", "Qayta nomlash", "Yaratish"], d=2,
      x="Ko‘chirishda fayl bitta qoladi, faqat joyi o‘zgaradi."),
    Q("Fayl manzili: D:\\O‘yinlar\\Shaxmat\\qoida.txt. Shaxmat papkasi qaysi papka ichida?", "O‘yinlar", ["Shaxmat", "qoida", "txt"], d=3,
      x="Manzil chapdan o‘ngga o‘qiladi: D diski → O‘yinlar → Shaxmat → qoida.txt."),
    Q("Windows tizimida qaysi belgini fayl nomida ishlatib bo‘lmaydi?", "?", ["_", "-", "1"], d=3,
      x="Windows fayl nomida ? * : / kabi maxsus belgilarga ruxsat bermaydi."),
]
for fname, cat in _ext_files:
    wrong = [c for c in _ext_cats if c != cat]
    _files.append(Q(f"“{fname}” faylida nima saqlangan?", cat, wrong[:4], d=1 if cat in ("Rasm", "Musiqa", "Video") else 2,
                    x=f"{fname.split('.')[1]} kengaytmasi — {cat.lower()} fayli."))
for what, fname in _ext_rev:
    wrong = [f for f in _ext_same if f != fname]
    _files.append(Q(f"Qaysi faylda {what} saqlangan?", fname, wrong[:4], d=1 if what in ("rasm", "musiqa", "video") else 2,
                    x=f"{fname.split('.')[1]} kengaytmasi {what} faylini bildiradi."))

T.topic("fayl", "📁", L("Fayl, papka va kengaytmalar", "Files, folders and extensions", "Файлы, папки и расширения"),
        chapter=C2,
        theory="Fayl — diskda nomi bilan saqlanadigan ma’lumot. Fayl nomi ikki qismdan iborat: nom va kengaytma, ular nuqta bilan ajratiladi: dars.docx.\n"
               "Kengaytma fayl turini bildiradi:\n"
               "• .txt, .docx — matn; .pdf — hujjat; .jpg, .png — rasm; .mp3 — musiqa; .mp4 — video; .pptx — taqdimot.\n"
               "Papka (jild) — fayllar va boshqa papkalarni guruhlab saqlaydigan joy.\n"
               "Fayl manzili: C:\\Maktab\\Rasmlar\\gul.jpg — gul.jpg fayli C diskidagi Maktab papkasi ichidagi Rasmlar papkasida.",
        items=_files)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["kompyuter_tuzilishi", "dasturiy", "fayl"], chapter=C2)

# ============================================================ 3-chorak
T.topic("matn_muharriri", "📝", L("Matn muharriri", "Text editor", "Текстовый редактор"),
        chapter=C3,
        theory="Matn muharriri — matn yozish, tahrirlash va bezash dasturi: Bloknot, WordPad, Microsoft Word, LibreOffice Writer.\n"
               "• Kursor — matn qayerga yozilishini ko‘rsatuvchi miltillovchi chiziq.\n"
               "• Shrift — harflarning ko‘rinishi (masalan, Arial, Times New Roman); shrift o‘lchami — harflarning kattaligi.\n"
               "• Bezash tugmalari: B — qalin, I — kursiv (qiya), U — tagiga chizilgan.\n"
               "• Tekislash: chapga, markazga, o‘ngga, kenglik bo‘yicha. Sarlavha odatda markazga tekislanadi.",
        items=[
            Q("Matn yozish va tahrirlash uchun qaysi dastur ishlatiladi?", "Matn muharriri", ["Grafik muharrir", "Antivirus", "Media pleyer"],
              x="Matn muharriri — matn bilan ishlash dasturi."),
            Q("Qaysi biri matn muharriri?", "Microsoft Word", ["Paint", "Google Chrome", "Windows"], x="Word — keng tarqalgan matn muharriri."),
            Q("Harflarni qalin qiladigan tugma qaysi?", "B", ["I", "U", "A"], x="B — inglizcha “bold”, ya’ni “qalin” so‘zidan."),
            Q("Harflarni kursiv (qiya) qiladigan tugma qaysi?", "I", ["B", "U", "S"], x="I — inglizcha “italic”, ya’ni “kursiv” so‘zidan."),
            Q("Matn tagiga chiziq tortadigan tugma qaysi?", "U", ["B", "I", "E"], x="U — inglizcha “underline”, ya’ni “tagiga chizish” so‘zidan."),
            Q("Harflarning ko‘rinishi, masalan, Arial yoki Times New Roman nima deb ataladi?", "Shrift", ["Kursor", "Abzas", "Sahifa"],
              x="Shrift — harflarning chizilish uslubi."),
            Q("Sarlavha odatda qanday tekislanadi?", "Markazga", ["Chapga", "O‘ngga", "Pastga"], x="Markazga tekislangan sarlavha chiroyli ko‘rinadi."),
            Q("Matn qayerga yozilishini ko‘rsatuvchi miltillovchi chiziq nima?", "Kursor", ["Shrift", "Abzas", "Kengaytma"],
              x="Harflar kursor turgan joyga yoziladi."),
            MATCH("Tugmani vazifasi bilan juftlang",
                  [("B", "Qalin"), ("I", "Kursiv"), ("U", "Tagiga chizilgan"), ("Enter", "Yangi abzas"), ("Backspace", "Chapdagi belgini o‘chirish"),
                   ("Delete", "O‘ngdagi belgini o‘chirish")], x="Bu tugmalar matn bilan ishlashda eng ko‘p ishlatiladi."),
            TF("Shrift o‘lchami qancha katta bo‘lsa, harflar shuncha katta ko‘rinadi.", True, x="Shrift o‘lchami harflar kattaligini belgilaydi."),
            Q("Yangi abzas boshlash uchun qaysi tugma bosiladi?", "Enter", ["Shift", "Probel", "Caps Lock"], x="Enter yangi abzas boshlaydi."),
            TF("Word dasturida harflar rangini o‘zgartirish mumkin.", True, x="Shrift rangi tugmasi harflarni istalgan rangga bo‘yaydi."),
            TF("Kursiv harflar qiya yoziladi.", True, x="Kursiv — qiya yozuv."),
            Q("Matnni qog‘ozga chiqarish qanday ataladi?", "Chop etish", ["Saqlash", "Nusxalash", "Belgilash"], x="Chop etish printer orqali bajariladi."),
            Q("Shrift o‘lchami nimani bildiradi?", "Harflar kattaligini", ["Harflar rangini", "Harflar sonini", "Sahifalar sonini"],
              x="Shrift o‘lchami qancha katta bo‘lsa, harflar shuncha katta."),
            Q("Matndagi so‘zlar orasiga nechta Probel qo‘yiladi?", "1 ta", ["2 ta", "3 ta", "4 ta"], x="So‘zlar orasiga bitta bo‘sh joy qo‘yiladi."),
            ORDER("So‘zlardan gap tuzing", "Sarlavhani markazga tekislang"),
            Q("Matnning ikkala cheti ham tekis bo‘lsa, bu qanday tekislash?", "Kenglik bo‘yicha", ["Chapga", "Markazga", "O‘ngga"], d=2,
              x="Kenglik bo‘yicha tekislashda qatorlar chap va o‘ng chetga bir tekis yetadi."),
            Q("Bloknot dasturida saqlangan fayl odatda qanday kengaytmaga ega bo‘ladi?", "txt", ["docx", "jpg", "mp3"], d=2,
              x="Bloknot oddiy matnni .txt faylga saqlaydi."),
            Q("Microsoft Word hujjati odatda qanday kengaytma bilan saqlanadi?", "docx", ["txt", "png", "mp4"], d=2,
              x="Zamonaviy Word hujjatlari .docx kengaytmasiga ega."),
            Q("Matnni belgilash uchun nima qilinadi?", "Sichqoncha bilan bosib sudraladi", ["Enter bosiladi", "Probel bosiladi", "Kompyuter o‘chiriladi"], d=2,
              x="Belgilangan matn rangli fon bilan ajralib turadi."),
            Q("Bezash, ya’ni formatlash nima?", "Matn ko‘rinishini o‘zgartirish", ["Matnni o‘chirish", "Faylni ko‘chirish", "Kompyuterni yoqish"], d=2,
              x="Formatlashda shrift, o‘lcham, rang, tekislash o‘zgartiriladi."),
            Q("Word dasturida so‘zni tez belgilash uchun unga nima qilinadi?", "Ikki marta bosiladi",
              ["O‘ng tugma bilan sudraladi", "Enter bosiladi", "Delete bosiladi"], d=3, x="So‘z ustida ikki marta bosilsa, u belgilanadi."),
            Q("Oddiy matn uchun odatda qaysi shrift o‘lchami qulay?", "12–14", ["1–2", "72–96", "200"], d=3,
              x="Hujjatlarda odatda 12–14 o‘lchamdagi shrift ishlatiladi."),
        ])

_keys = [("C", "Nusxa olish", "Nusxa oladi", 1), ("V", "Qo‘yish", "Qo‘yadi", 1), ("X", "Kesish", "Kesadi", 1),
         ("Z", "Oxirgi amalni bekor qilish", "Oxirgi amalni bekor qiladi", 1), ("S", "Saqlash", "Saqlaydi", 1),
         ("A", "Hammasini belgilash", "Hammasini belgilaydi", 2), ("P", "Chop etish", "Chop etadi", 2), ("F", "Matndan so‘z qidirish", "So‘z qidiradi", 3)]
_edit = [
    MATCH("Tugmalar birikmasini vazifasi bilan juftlang", [(f"Ctrl+{k}", verb) for k, _, verb, _ in _keys[:7]],
          x="Ctrl bilan birga bosiladigan harflar tez ishlash imkonini beradi."),
    TF("Kesilgan matn o‘z joyidan yo‘qoladi.", True, x="Kesishda matn o‘z joyidan olinib, buferga tushadi."),
    TF("Nusxa olinganda matn o‘z joyidan o‘chib ketadi.", False, x="Nusxa olishda matn joyida qoladi, nusxasi buferga tushadi."),
    Q("Kursordan chapdagi belgini qaysi tugma o‘chiradi?", "Backspace", ["Delete", "Enter", "Tab"], x="Backspace chapdagi belgini o‘chiradi."),
    Q("Kursordan o‘ngdagi belgini qaysi tugma o‘chiradi?", "Delete", ["Backspace", "Shift", "Enter"], x="Delete o‘ngdagi belgini o‘chiradi."),
    ORDER("So‘zlardan gap tuzing", "Avval kerakli matnni belgilang"),
    Q("Matnni bir joydan boshqa joyga ko‘chirish uchun qaysi tartib to‘g‘ri?", "Belgilash, Ctrl+X, Ctrl+V",
      ["Ctrl+V, belgilash, Ctrl+X", "Ctrl+X, Ctrl+V, belgilash", "Belgilash, Ctrl+Z, Ctrl+S"], d=2,
      x="Avval belgilaymiz, kesamiz, kursorni yangi joyga qo‘yib, qo‘yamiz."),
    Q("Gapni nusxalab, boshqa joyga ham qo‘yish uchun qaysi tartib to‘g‘ri?", "Belgilash, Ctrl+C, Ctrl+V",
      ["Ctrl+V, Ctrl+C, belgilash", "Belgilash, Ctrl+Z, Ctrl+V", "Ctrl+C, belgilash, Ctrl+S"], d=2,
      x="Belgilab, nusxa olib, yangi joyga qo‘yamiz — asl gap joyida qoladi."),
    Q("Nusxa olingan matn qayerda vaqtincha saqlanadi?", "Almashuv buferida", ["Savatda", "Printerda", "Fleshkada"], d=2,
      x="Almashuv buferi — nusxa olingan yoki kesilgan narsa vaqtincha turadigan joy."),
    Q("Tahrirlashdan oldin matnning kerakli qismi bilan nima qilinadi?", "Belgilanadi", ["Chop etiladi", "O‘chiriladi", "Saqlanadi"], d=2,
      x="Buyruq faqat belgilangan qismga ta’sir qiladi."),
    TF("Ctrl+V bosilganda matn kursor turgan joyga qo‘yiladi.", True, d=2, x="Shuning uchun avval kursorni kerakli joyga qo‘yamiz."),
    Q("Zarina insho yozyapti va kompyuter o‘chib qolishidan qo‘rqadi. U tez-tez qaysi birikmani bosishi kerak?", "Ctrl+S",
      ["Ctrl+Z", "Ctrl+X", "Ctrl+A"], d=2, x="Ctrl+S hujjatni saqlaydi."),
    TF("Bitta nusxa olingan matnni bir necha marta qo‘yish mumkin.", True, d=3,
       x="Buferga yangi narsa tushmaguncha Ctrl+V har safar o‘sha matnni qo‘yadi."),
    Q("Ctrl tugmalari klaviaturaning qayerida joylashgan?", "Pastki qatorning chetlarida",
      ["Eng yuqori qatorning o‘rtasida", "Probel ichida", "Raqamlar qatorida"], d=3, x="Ctrl tugmalari pastki qatorda, chap va o‘ng chetda turadi."),
]
_all_combos = [f"Ctrl+{k}" for k, _, _, _ in _keys]
_all_verbs = [verb for _, _, verb, _ in _keys]
for k, noun, verb, d in _keys:
    combo = f"Ctrl+{k}"
    w1 = [c for c in _all_combos if c != combo]
    w2 = [v for v in _all_verbs if v != verb]
    _edit.append(Q(f"{noun} uchun qaysi tugmalar birikmasi ishlatiladi?", combo, w1[:4], d=d, x=f"{noun} — {combo}."))
    _edit.append(Q(f"{combo} tugmalari nima qiladi?", verb, w2[:4], d=d, x=f"{combo} — {noun.lower()}."))

T.topic("tahrirlash", "⌨️", L("Tahrirlash va tezkor tugmalar", "Editing and keyboard shortcuts", "Редактирование и горячие клавиши"),
        chapter=C3,
        theory="Tahrirlash — matndagi xatolarni tuzatish, qismlarini ko‘chirish yoki o‘chirish. Avval kerakli qism belgilanadi, keyin buyruq beriladi.\n"
               "• Ctrl+C — nusxa olish (matn joyida qoladi);  Ctrl+X — kesish (matn o‘z joyidan olinadi).\n"
               "• Ctrl+V — kursor turgan joyga qo‘yish;  Ctrl+Z — oxirgi amalni bekor qilish.\n"
               "• Ctrl+S — saqlash;  Ctrl+A — hammasini belgilash;  Ctrl+P — chop etish.\n"
               "Nusxa olingan yoki kesilgan matn almashuv buferida vaqtincha saqlanadi.",
        items=_edit)


def run_ops(start, ops):
    v = start
    for op, k in ops:
        if op == "+":
            v += k
        elif op == "-":
            v -= k
        elif op == "*":
            v *= k
        else:
            assert v % k == 0
            v //= k
    return v


OPS_TXT = {"+": "{k} ni qo‘sh", "-": "{k} ni ayir", "*": "{k} ga ko‘paytir", "/": "{k} ga bo‘l"}


def ops_text(ops):
    return ", ".join("“" + OPS_TXT[op].replace("{k}", str(k)) + "”" for op, k in ops)


_alg = [
    Q("Algoritm nima?", "Aniq buyruqlar ketma-ketligi", ["Kompyuter qurilmasi", "Fayl kengaytmasi", "Operatsion tizim"],
      x="Algoritm — natijaga olib boradigan aniq buyruqlar tartibi."),
    Q("“Algoritm” so‘zi kimning nomidan kelib chiqqan?", "Al-Xorazmiy", ["Ibn Sino", "Ulug‘bek", "Beruniy"],
      x="Buyuk vatandoshimiz Muhammad al-Xorazmiy nomi lotin tilida “Algoritmi” deb yozilgan."),
    Q("Buyruqlarni bajaruvchi kim yoki nima deb ataladi?", "Ijrochi", ["Algoritm", "Kengaytma", "Bufer"],
      x="Ijrochi — odam, robot yoki kompyuter bo‘lishi mumkin."),
    Q("Algoritmni tasvirlash usuli qaysi?", "Blok-sxema", ["Fleshka", "Printer", "Kengaytma"],
      x="Algoritm so‘zlar bilan, blok-sxema bilan yoki dastur ko‘rinishida tasvirlanadi."),
    TF("Algoritmni so‘zlar bilan ham yozish mumkin.", True, x="Masalan, taom retsepti so‘zlar bilan yozilgan algoritm."),
    TF("Algoritmni faqat kompyuter bajaradi.", False, x="Algoritmni odam ham, robot ham bajaradi."),
    Q("Qaysi biri algoritmga misol bo‘la oladi?", "Taom retsepti", ["Qizil olma", "Baland tog‘", "Tinch dengiz"],
      x="Retseptda ish tartibi qadam-baqadam yozilgan."),
    Q("Qaysi buyruq Robot ijrochi uchun aniq?", "5 qadam oldinga yur", ["Uzoqroqqa bor", "Tezroq yur", "Biror joyga bor"],
      x="Aniq buyruqda nima qilish va qancha qilish aytiladi."),
    Q("Qaysi ijrochi “chop et” buyrug‘ini bajaradi?", "Printer", ["Mikrofon", "Skaner", "Klaviatura"],
      x="Printer chop etish buyrug‘ini bajaradi."),
    ORDER("So‘zlardan gap tuzing", "Ijrochi algoritmni bajaradi"),
    Q("Ijrochi bajara oladigan buyruqlar to‘plami nima deb ataladi?", "Buyruqlar tizimi", ["Operatsion tizim", "Fayl tizimi", "Sanoq sistemasi"], d=2,
      x="Ijrochi faqat o‘z buyruqlar tizimidagi buyruqlarni bajaradi."),
    Q("Algoritmning alohida qadamlarga bo‘linishi qaysi xossa?", "Diskretlik", ["Ommaviylik", "Natijaviylik", "Tushunarlilik"], d=2,
      x="Diskretlik — algoritm alohida, ketma-ket qadamlardan iborat."),
    Q("Algoritm chekli qadamdan so‘ng natijaga olib kelishi qaysi xossa?", "Natijaviylik", ["Diskretlik", "Ommaviylik", "Aniqlik"], d=2,
      x="Natijaviylik — algoritm oxir-oqibat natija beradi."),
    Q("Algoritmni bir turdagi ko‘p masalalarga qo‘llash mumkinligi qaysi xossa?", "Ommaviylik", ["Diskretlik", "Aniqlik", "Tushunarlilik"], d=2,
      x="Masalan, qo‘shish algoritmi istalgan sonlar uchun ishlaydi."),
    Q("Har bir buyruq bir xil ma’noda tushunilishi qaysi xossa?", "Aniqlik", ["Ommaviylik", "Natijaviylik", "Diskretlik"], d=2,
      x="Aniq buyruqni har qanday ijrochi bir xil bajaradi."),
    Q("Algoritm ijrochiga tushunarli buyruqlardan tuzilishi qaysi xossa?", "Tushunarlilik", ["Ommaviylik", "Diskretlik", "Natijaviylik"], d=2,
      x="Ijrochi bilmaydigan buyruqni bajara olmaydi."),
    MATCH("Xossani ta’rifi bilan juftlang",
          [("Diskretlik", "Qadamlarga bo‘lingan"), ("Aniqlik", "Buyruqlar bir ma’noli"), ("Tushunarlilik", "Ijrochiga tushunarli"),
           ("Natijaviylik", "Natijaga olib keladi"), ("Ommaviylik", "Ko‘p masalaga qo‘llanadi")], d=2,
          x="Algoritmning beshta asosiy xossasi."),
    Q("Dasturlash tilida yozilgan algoritm nima deb ataladi?", "Dastur", ["Fayl kengaytmasi", "Brauzer", "Papka"], d=2,
      x="Dastur — kompyuter tushunadigan tilda yozilgan algoritm."),
    TF("Algoritmdagi buyruqlar tartibi o‘zgarsa, natija ham o‘zgarishi mumkin.", True, d=2,
       x=f"Masalan, 3 ni avval 2 ga ko‘paytirib 4 qo‘shsak {run_ops(3, [('*', 2), ('+', 4)])}, avval 4 qo‘shib 2 ga ko‘paytirsak {run_ops(3, [('+', 4), ('*', 2)])} chiqadi."),
    Q("Algoritm so‘zlar va blok-sxemadan tashqari yana qanday ko‘rinishda tasvirlanadi?", "Dastur ko‘rinishida",
      ["Musiqa ko‘rinishida", "Hid ko‘rinishida", "Fleshka ko‘rinishida"], d=2, x="Algoritm dasturlash tilida dastur sifatida yoziladi."),
    Q("“Biroz tuz sol” buyrug‘ida qaysi xossa buzilgan?", "Aniqlik", ["Diskretlik", "Ommaviylik", "Natijaviylik"], d=3,
      x="“Biroz” har kim uchun har xil — buyruq aniq emas."),
]
for start, ops, d in [(3, [("*", 2), ("+", 4)], 2), (5, [("+", 3), ("*", 2)], 2), (3, [("+", 4), ("*", 2)], 3), (20, [("-", 5), ("/", 3)], 3)]:
    v = run_ops(start, ops)
    _alg.append(Q(f"Ijrochi {start} sonini oldi va buyruqlarni tartib bilan bajardi: {ops_text(ops)}. Natija qanday?", v,
                  near(v, [v + 1, v - 1, v + 2, v * 2, start], lo=0), d=d,
                  x=f"Buyruqlarni birma-bir bajaramiz: natija {v}."))

T.topic("algoritm", "📋", L("Algoritm va uning xossalari", "Algorithms and their properties", "Алгоритм и его свойства"),
        chapter=C3,
        theory="Algoritm — ijrochi natijaga erishishi uchun bajariladigan aniq buyruqlar ketma-ketligi. Bu so‘z vatandoshimiz Muhammad al-Xorazmiy nomidan kelib chiqqan.\n"
               "Xossalari: diskretlik — alohida qadamlarga bo‘lingan; tushunarlilik — ijrochiga tushunarli;\n"
               "aniqlik — har bir buyruq bir xil tushuniladi; natijaviylik — chekli qadamdan so‘ng natija beradi; ommaviylik — bir turdagi ko‘p masalalarga qo‘llanadi.\n"
               "Tasvirlash usullari: so‘zlar bilan, blok-sxema bilan, dastur ko‘rinishida.\n"
               "Ijrochi faqat o‘z buyruqlar tizimidagi buyruqlarni bajara oladi.",
        items=_alg)

_types3 = ["Chiziqli", "Tarmoqlanuvchi", "Takrorlanuvchi"]
_flow = [
    Q("Blok-sxemada boshlanish va tugash qaysi shakl bilan belgilanadi?", "Oval", ["Romb", "To‘g‘ri to‘rtburchak", "Parallelogramm"],
      x="Oval ichiga “Boshlash” va “Tamom” yoziladi."),
    Q("Blok-sxemada shart qaysi shakl bilan belgilanadi?", "Romb", ["Oval", "To‘g‘ri to‘rtburchak", "Parallelogramm"],
      x="Romb ichida shart yoziladi, undan “ha” va “yo‘q” yo‘llari chiqadi.", e="🔷"),
    Q("Blok-sxemada amal, ya’ni hisoblash qaysi shakl bilan belgilanadi?", "To‘g‘ri to‘rtburchak", ["Romb", "Oval", "Parallelogramm"],
      x="To‘g‘ri to‘rtburchak ichida bajariladigan amal yoziladi."),
    Q("Blok-sxemada ma’lumot kiritish va chiqarish qaysi shakl bilan belgilanadi?", "Parallelogramm", ["Romb", "Oval", "To‘g‘ri to‘rtburchak"],
      x="Parallelogramm — kiritish va chiqarish bloki."),
    MATCH("Shaklni vazifasi bilan juftlang",
          [("Oval", "Boshlanish yoki tugash"), ("To‘g‘ri to‘rtburchak", "Amal bajarish"), ("Romb", "Shartni tekshirish"),
           ("Parallelogramm", "Kiritish yoki chiqarish"), ("Strelka", "Bajarilish yo‘nalishi")],
          x="Blok-sxemaning har bir shakli o‘z ma’nosiga ega."),
    Q("Buyruqlar birin-ketin, hech narsa tekshirilmasdan bajariladigan algoritm qanday ataladi?", "Chiziqli", ["Tarmoqlanuvchi", "Takrorlanuvchi", "Tasodifiy"],
      x="Chiziqli algoritmda buyruqlar navbat bilan bir martadan bajariladi."),
    Q("Shartga qarab turli yo‘ldan boradigan algoritm qanday ataladi?", "Tarmoqlanuvchi", ["Chiziqli", "Takrorlanuvchi", "Tasodifiy"],
      x="Tarmoqlanuvchi algoritmda “agar … bo‘lsa” sharti bor."),
    Q("Ba’zi buyruqlari bir necha marta qaytariladigan algoritm qanday ataladi?", "Takrorlanuvchi", ["Chiziqli", "Tarmoqlanuvchi", "Tasodifiy"],
      x="Takrorlanuvchi algoritm sikl deb ham ataladi."),
    Q("Blok-sxemadagi strelkalar nimani ko‘rsatadi?", "Bajarilish tartibini", ["Xatolarni", "Fayl hajmini", "Kompyuter tezligini"],
      x="Strelkalar qaysi blokdan keyin qaysi blok bajarilishini ko‘rsatadi."),
    TF("Tarmoqlanuvchi algoritmda shart tekshiriladi.", True, x="Shart natijasiga qarab yo‘l tanlanadi."),
    TF("Chiziqli algoritmda buyruqlar takrorlanadi.", False, x="Chiziqli algoritmda har bir buyruq bir marta, tartib bilan bajariladi."),
    ORDER("So‘zlardan gap tuzing", "Romb shartni bildiradi"),
    Q("Romb shaklidan nechta chiqish yo‘li bo‘ladi?", "2 ta", ["1 ta", "3 ta", "4 ta"], d=2,
      x="Shart to‘g‘ri bo‘lsa “ha”, noto‘g‘ri bo‘lsa “yo‘q” yo‘li tanlanadi."),
    Q("Romb shaklidan chiquvchi yo‘llar qanday belgilanadi?", "“Ha” va “Yo‘q”", ["“Boshla” va “Tamom”", "“Kirit” va “Chiqar”", "“1” va “2”"], d=2,
      x="Shart bajarilsa — “ha”, bajarilmasa — “yo‘q”."),
    TF("Blok-sxema oval bilan boshlanib, oval bilan tugaydi.", True, d=2, x="Boshlanish va tugash bloklari oval shaklida."),
    Q("Takrorlanuvchi algoritm yana qanday ataladi?", "Sikl", ["Shart", "Kengaytma", "Bufer"], d=2, x="Sikl — takrorlanish."),
]
for text, kind, d in [("Qo‘l yuvish: jo‘mrakni och, qo‘lni sovunla, chay, art.", "Chiziqli", 1),
                      ("Kitobni och, 10-betni top, matnni o‘qi.", "Chiziqli", 1),
                      ("Agar dars tayyor bo‘lsa, sayrga chiq, aks holda darsni tayyorla.", "Tarmoqlanuvchi", 1),
                      ("Agar svetoforda yashil chiroq yonsa, yo‘ldan o‘t, aks holda kut.", "Tarmoqlanuvchi", 2),
                      ("Arqonda 20 marta sakra.", "Takrorlanuvchi", 1),
                      ("Zinapoyaning har bir pog‘onasiga navbat bilan qadam qo‘y, 5-qavatga yetguncha.", "Takrorlanuvchi", 2),
                      ("Qo‘ng‘iroq chalinmaguncha masala yechishni davom ettir.", "Takrorlanuvchi", 3)]:
    _flow.append(Q(f"“{text}” Bu qanday algoritm?", kind, [t for t in _types3 if t != kind] + ["Tasodifiy"], d=d,
                   x={"Chiziqli": "Buyruqlar birin-ketin bir martadan bajariladi.",
                      "Tarmoqlanuvchi": "Shartga qarab ikki yo‘ldan biri tanlanadi.",
                      "Takrorlanuvchi": "Bir xil harakat bir necha marta qaytariladi."}[kind]))
for start, op, k, times, d in [(2, "+", 3, 4, 2), (0, "+", 5, 6, 2), (1, "*", 2, 3, 3), (20, "-", 3, 3, 3)]:
    v = run_ops(start, [(op, k)] * times)
    cmd = OPS_TXT[op].replace("{k}", str(k))
    _flow.append(Q(f"Boshida son {start} ga teng. “Songa {cmd}” buyrug‘i {times} marta takrorlandi. Natija qanday?".replace("Songa " + str(k) + " ga ko‘paytir", "Sonni " + str(k) + " ga ko‘paytir").replace("Songa " + str(k) + " ni ayir", "Sondan " + str(k) + " ni ayir"),
                   v, near(v, [v + k, v - k, start + k, k * times, v + 1], lo=0), d=d,
                   x=f"Buyruqni {times} marta bajaramiz: natija {v}."))
_rule = "Agar son 10 dan katta bo‘lsa, uni 2 ga bo‘l, aks holda unga 5 ni qo‘sh."
for n, d in [(14, 2), (6, 2), (10, 3)]:
    v = n // 2 if n > 10 else n + 5
    assert n <= 10 or n % 2 == 0
    _flow.append(Q(f"{_rule} Son {n} bo‘lsa, natija qanday?", v, near(v, [n // 2 if n <= 10 else n + 5, v + 1, v - 1, n], lo=0), d=d,
                   x=(f"{n} > 10 — shart bajarildi: {n} : 2 = {v}." if n > 10 else f"{n} 10 dan katta emas — “aks holda” yo‘li: {n} + 5 = {v}.")))

T.topic("blok_sxema", "🔷", L("Algoritm turlari va blok-sxema", "Types of algorithms and flowcharts", "Виды алгоритмов и блок-схемы"),
        chapter=C3,
        theory="Algoritm turlari:\n"
               "• Chiziqli — buyruqlar birin-ketin, tartib bilan bajariladi.\n"
               "• Tarmoqlanuvchi — shartga qarab yo‘l tanlanadi: “Agar yomg‘ir yog‘sa, soyabon ol, aks holda soyabonsiz chiq”.\n"
               "• Takrorlanuvchi (sikl) — ba’zi buyruqlar bir necha marta takrorlanadi.\n"
               "Blok-sxema shakllari: oval — boshlanish va tugash; to‘g‘ri to‘rtburchak — amal; romb — shart (“ha” yoki “yo‘q”); parallelogramm — kiritish va chiqarish. Strelkalar bajarilish tartibini ko‘rsatadi.",
        items=_flow)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["matn_muharriri", "tahrirlash", "algoritm", "blok_sxema"], chapter=C3)

# ============================================================ 4-chorak
_scr = [
    Q("Scratch muhitida dastur qanday tuziladi?", "Bloklarni ulab", ["Faqat matn yozib", "Rasm chizib", "Musiqa yozib"],
      x="Scratchda rangli bloklarni sudrab, bir-biriga ulaymiz."),
    Q("Scratch sahnasida harakatlanadigan personaj nima deb ataladi?", "Sprayt", ["Sahna", "Blok", "Skript"],
      x="Sprayt — sahnadagi personaj yoki obyekt."),
    Q("Scratchda yangi loyiha ochilganda qaysi sprayt turadi?", "Mushuk", ["It", "Quyon", "Robot"],
      x="Scratchning belgisi va dastlabki spraytı — mushuk.", e="🐱"),
    Q("Scratch dasturini ishga tushiradigan tugma qaysi?", "Yashil bayroqcha", ["Qizil doira", "Sariq yulduz", "Ko‘k uchburchak"],
      x="Yashil bayroqcha bosilganda dastur boshlanadi."),
    Q("Scratch dasturini to‘xtatadigan tugma qanday rangda?", "Qizil", ["Yashil", "Sariq", "Ko‘k"],
      x="Qizil to‘xtatish tugmasi barcha skriptlarni to‘xtatadi."),
    Q("“10 qadam yur” bloki qaysi guruhda?", "Harakat", ["Ko‘rinish", "Hodisalar", "Tovush"], x="Spraytni suradigan bloklar — Harakat guruhida."),
    TF("Scratch sahnasining foni almashtirilishi mumkin.", True, x="Sahna uchun turli fon rasmlarini tanlash mumkin."),
    TF("Scratch loyihasida bir nechta sprayt bo‘lishi mumkin.", True, x="Har bir spraytning o‘z skriptlari bo‘ladi."),
    Q("Scratch nima uchun yaratilgan?", "Dasturlashni o‘rganish uchun", ["Matn chop etish uchun", "Viruslarni o‘chirish uchun", "Xat yuborish uchun"],
      x="Scratch bolalarga dasturlashni o‘yin tarzida o‘rgatadi."),
    Q("Scratch sahnasi nima?", "Spraytlar harakatlanadigan joy", ["Bloklar ro‘yxati", "Fayl kengaytmasi", "Tovush turi"],
      x="Sahnada spraytlar harakatlanadi va dastur natijasi ko‘rinadi."),
    Q("Harakat bloklari qanday rangda?", "Ko‘k", ["Sariq", "Yashil", "Binafsha"], d=2, x="Scratchda Harakat bloklari ko‘k rangda."),
    Q("“Yashil bayroqcha bosilganda” bloki qaysi guruhda?", "Hodisalar", ["Harakat", "Tovush", "Operatorlar"], d=2,
      x="Hodisalar bloklari skriptni qachon boshlashni belgilaydi."),
    Q("“Salom! deb 2 soniya ayt” bloki qaysi guruhda?", "Ko‘rinish", ["Harakat", "Operatorlar", "Hodisalar"], d=2,
      x="Spraytning gapirishi va kostyumi Ko‘rinish guruhida."),
    Q("“10 marta takrorla” bloki qaysi guruhda?", "Boshqaruv", ["Harakat", "Ko‘rinish", "Tovush"], d=2,
      x="Takrorlash, kutish va shart bloklari — Boshqaruv guruhida."),
    Q("“Doimo takrorla” bloki qanday ishlaydi?", "To‘xtatilmaguncha takrorlaydi", ["Bir marta bajaradi", "Hech narsa bajarmaydi", "Faqat 10 marta bajaradi"], d=2,
      x="“Doimo takrorla” ichidagi bloklar to‘xtatish tugmasi bosilguncha bajariladi."),
    Q("Spraytning turli ko‘rinishlari nima deb ataladi?", "Kostyumlar", ["Sahnalar", "Bloklar", "Hodisalar"], d=2,
      x="Kostyumlarni almashtirib, sprayt harakatini jonlantiramiz."),
    Q("Kostyumlarni tez-tez almashtirsak, nima hosil bo‘ladi?", "Animatsiya", ["Virus", "Kengaytma", "Papka"], d=2,
      x="Rasmlar tez almashsa, harakat ko‘rinadi — bu animatsiya."),
    Q("“1 soniya kut” bloki nima qiladi?", "Dasturni 1 soniya to‘xtatib turadi", ["Spraytni o‘chiradi", "Sahnani almashtiradi", "Tovushni o‘chiradi"], d=2,
      x="Kutish bloki keyingi buyruqni biroz kechiktiradi."),
    Q("Bloklardan tuzilgan dastur Scratchda nima deb ataladi?", "Skript", ["Sprayt", "Kostyum", "Sahna"], d=2,
      x="Skript — bir-biriga ulangan bloklar zanjiri."),
    MATCH("Blokni guruhi bilan juftlang",
          [("10 qadam yur", "Harakat"), ("Salom! deb ayt", "Ko‘rinish"), ("Yashil bayroqcha bosilganda", "Hodisalar"),
           ("10 marta takrorla", "Boshqaruv"), ("Tovushni ijro et", "Tovush"), ("Tasodifiy son tanla", "Operatorlar")], d=2,
          x="Scratch bloklari vazifasiga qarab guruhlarga ajratilgan."),
    ORDER("So‘zlardan gap tuzing", "Yashil bayroqcha dasturni ishga tushiradi", d=2),
    Q("Scratch loyihasi fayli qanday kengaytmaga ega?", "sb3", ["mp3", "docx", "jpg"], d=3, x="Scratch 3 loyihalari .sb3 faylga saqlanadi."),
    Q("Scratch sahnasi markazining koordinatalari qanday?", "x: 0, y: 0", ["x: 100, y: 100", "x: 240, y: 180", "x: 480, y: 360"], d=3,
      x="Sahna markazi — koordinatalar boshi: x = 0, y = 0."),
    Q("“y ni 10 ga o‘zgartir” bloki spraytni qayerga suradi?", "Yuqoriga", ["Pastga", "O‘ngga", "Chapga"], d=3,
      x="y oshsa, sprayt yuqoriga ko‘tariladi."),
    Q("“x ni 10 ga o‘zgartir” bloki spraytni qayerga suradi?", "O‘ngga", ["Chapga", "Yuqoriga", "Pastga"], d=3,
      x="x oshsa, sprayt o‘ngga suriladi."),
]
for times, steps, d in [(5, 10, 2), (4, 25, 2), (3, 20, 2)]:
    v = times * steps
    _scr.append(Q(f"“{times} marta takrorla” bloki ichida “{steps} qadam yur” bor. Sprayt jami necha qadam yuradi?", v,
                  near(v, [times + steps, v + steps, v - steps, steps], lo=1), d=d, x=f"{times} · {steps} = {v} qadam."))
for times, dx in [(3, 10), (4, 15)]:
    v = times * dx
    _scr.append(Q(f"Sprayt x = 0 nuqtada. “x ni {dx} ga o‘zgartir” bloki {times} marta bajarildi. Endi x nechaga teng?", v,
                  near(v, [dx, times + dx, v + dx, v - dx], lo=1), d=3, x=f"x har safar {dx} ga oshadi: {times} · {dx} = {v}."))
_angles = [120, 90, 72, 60, 45, 180]
for n, shape, d in [(4, "kvadrat", 2), (3, "teng tomonli uchburchak", 3), (6, "muntazam oltiburchak", 3)]:
    a = 360 // n
    assert a * n == 360
    _scr.append(Q(f"Scratchda {shape} chizish uchun “{n} marta takrorla” ichida “qadam yur” va “burilish” bloklari bor. Har safar necha gradusga burilish kerak?",
                  f"{a}°", [f"{v}°" for v in _angles if v != a][:4], d=d, x=f"To‘liq aylanish 360°: 360 : {n} = {a}°."))
_scr.append(Q("Scratchda kvadrat chizish uchun “qadam yur” va “90° buril” bloklari necha marta takrorlanishi kerak?", 4, [3, 5, 6, 90], d=2,
              x="Kvadratning 4 ta tomoni bor: 4 · 90° = 360°."))

T.topic("scratch", "🐱", L("Scratch asoslari", "Scratch basics", "Основы Scratch"),
        chapter=C4,
        theory="Scratch — rangli bloklarni ulab dastur tuziladigan dasturlash muhiti. Uni AQShdagi MIT olimlari bolalar uchun yaratgan.\n"
               "• Sprayt — sahnada harakatlanadigan personaj (dastlab — mushuk); sahna — spraytlar harakatlanadigan joy, uning fonini almashtirish mumkin.\n"
               "• Bloklar guruhlarga bo‘lingan: Harakat (ko‘k), Ko‘rinish (binafsha), Tovush, Hodisalar (sariq), Boshqaruv, Operatorlar (yashil).\n"
               "• Yashil bayroqcha dasturni ishga tushiradi, qizil tugma to‘xtatadi.\n"
               "Bloklardan tuzilgan dastur skript deb ataladi. Misol: “4 marta takrorla: 100 qadam yur, 90° buril” — kvadrat chizadi.",
        items=_scr)

T.topic("internet", "🌐", L("Internet, brauzer va qidiruv", "Internet, browsers and search", "Интернет, браузер и поиск"),
        chapter=C4,
        theory="Internet — butun dunyodagi kompyuter tarmoqlarini birlashtirgan global tarmoq.\n"
               "• Brauzer — veb-sahifalarni ko‘rish dasturi: Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari.\n"
               "• Sayt — veb-sahifalar to‘plami; har bir saytning manzili bor, u manzil satriga yoziladi. “.uz” — O‘zbekiston domeni.\n"
               "• Havola — bosilganda boshqa sahifaga o‘tkazadigan matn yoki rasm.\n"
               "• Qidiruv tizimi (Google, Yandex, Bing) kalit so‘zlar bo‘yicha ma’lumot topadi. Topilgan ma’lumotni bir necha manbada tekshiring.",
        items=[
            Q("Veb-sahifalarni ko‘rish uchun qaysi dastur kerak?", "Brauzer", ["Antivirus", "Paint", "Kalkulyator"], x="Brauzer saytlarni ochib ko‘rsatadi."),
            Q("Qaysi biri brauzer?", "Mozilla Firefox", ["Windows", "Word", "Paint"], x="Mozilla Firefox — brauzer."),
            Q("Qaysi biri qidiruv tizimi?", "Google", ["Paint", "Windows", "Excel"], x="Google — dunyodagi eng mashhur qidiruv tizimi."),
            Q("Qaysi biri qidiruv tizimi?", "Yandex", ["Word", "Paint", "Linux"], x="Yandex — qidiruv tizimi."),
            Q("“.uz” domeni qaysi mamlakatga tegishli?", "O‘zbekiston", ["Ukraina", "AQSh", "Italiya"], x="“.uz” — O‘zbekiston milliy domeni."),
            Q("Bosilganda boshqa sahifaga o‘tkazadigan matn yoki rasm nima deb ataladi?", "Havola", ["Kengaytma", "Papka", "Shrift"],
              x="Havola ko‘pincha ko‘k rangda va tagiga chizilgan bo‘ladi."),
            Q("Qidiruv tizimiga yoziladigan so‘zlar nima deb ataladi?", "Kalit so‘zlar", ["Parollar", "Kengaytmalar", "Havolalar"],
              x="Kalit so‘zlar nimani izlayotganimizni bildiradi."),
            TF("Internet — butun dunyo bo‘ylab tarqalgan kompyuter tarmog‘i.", True, x="Internet millionlab kompyuterlarni bog‘laydi."),
            TF("Internetdagi har bir ma’lumot ishonchli.", False, x="Internetda xato ma’lumot ham bor, uni tekshirish kerak."),
            Q("Internet orqali qaysi ishni bajarib bo‘lmaydi?", "Non yopish", ["Xat yuborish", "Video ko‘rish", "Ma’lumot izlash"],
              x="Internet axborot bilan ishlaydi, non yopib bermaydi."),
            ORDER("So‘zlardan gap tuzing", "Brauzer veb-sahifalarni ko‘rsatadi"),
            Q("Sayt manzili yoziladigan joy nima deb ataladi?", "Manzil satri", ["Vazifalar paneli", "Sarlavha qatori", "Savat"], d=2,
              x="Manzil satri brauzer oynasining yuqori qismida joylashgan."),
            TF("Google Chrome — qidiruv tizimi.", False, d=2, x="Google Chrome — brauzer; qidiruv tizimi esa Google."),
            Q("Qurilmalarni simsiz internetga ulaydigan texnologiya qaysi?", "Wi-Fi", ["USB", "HDMI", "Probel"], d=2,
              x="Wi-Fi radio to‘lqinlar orqali simsiz ulanishni ta’minlaydi."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Brauzer", "Sahifalarni ko‘rish dasturi"), ("Sayt", "Veb-sahifalar to‘plami"), ("Havola", "Boshqa sahifaga o‘tkazadi"),
                   ("Qidiruv tizimi", "Ma’lumot izlash xizmati"), ("Manzil satri", "Sayt manzili yoziladi"), ("Internet", "Global kompyuter tarmog‘i")], d=2,
                  x="Internetda ishlash uchun asosiy tushunchalar."),
            Q("Oy haqida ma’lumot izlash uchun qidiruvga qaysi so‘rov eng mos?", "Oy haqida qiziqarli faktlar", ["Salom", "Men", "Qiziq"], d=2,
              x="So‘rovda izlanayotgan narsa aniq aytilishi kerak."),
            Q("Maktab loyihasi uchun olingan ma’lumotni qanday tekshirish kerak?", "Bir necha manbada solishtirib",
              ["Tekshirmaslik kerak", "Faqat bitta saytga ishonib", "Birinchi rasmga qarab"], d=2,
              x="Bir necha ishonchli manba bir xil desa, ma’lumotga ishonsa bo‘ladi."),
            Q("Brauzerda oldingi sahifaga qaytish uchun qaysi tugma bosiladi?", "Orqaga strelkasi", ["Yopish tugmasi", "Yangilash", "Yangi varaq"], d=2,
              x="Orqaga strelkasi avval ochilgan sahifaga qaytaradi."),
            Q("Sahifani qayta yuklaydigan tugma qanday ataladi?", "Yangilash", ["Orqaga", "Yopish", "Saqlash"], d=2,
              x="Yangilash tugmasi sahifani qaytadan yuklaydi."),
            Q("Havola ustiga kelganda sichqoncha ko‘rsatkichi qanday shaklga kiradi?", "Qo‘l", ["Qum soat", "Qalam", "Doira"], d=2,
              x="Qo‘l shaklidagi ko‘rsatkich bu yerni bosish mumkinligini bildiradi."),
            Q("Manzil satrida qulf belgisi va “https” nimani bildiradi?", "Xavfsiz ulanishni", ["Sayt yopiqligini", "Virus borligini", "Internet yo‘qligini"], d=3,
              x="https da ma’lumot shifrlangan holda uzatiladi."),
            Q("Brauzerda bir vaqtda bir nechta saytni ochish uchun nima ochiladi?", "Yangi varaq", ["Yangi papka", "Yangi fayl", "Yangi kengaytma"], d=3,
              x="Har bir varaqda (vkladkada) alohida sayt ochiladi."),
            Q("Yoqqan saytni keyin tez topish uchun brauzerda nima qilinadi?", "Xatcho‘plarga qo‘shiladi", ["O‘chiriladi", "Chop etiladi", "Savatga tashlanadi"], d=3,
              x="Xatcho‘pdagi saytni bir bosishda ochish mumkin."),
            Q("“www” qisqartmasi nimani bildiradi?", "Butunjahon o‘rgimchak to‘ri", ["Windows dasturi", "Wi-Fi tarmog‘i", "Veb-kamera"], d=3,
              x="www — World Wide Web, ya’ni butunjahon o‘rgimchak to‘ri."),
        ])

T.topic("pochta", "📧", L("Elektron pochta", "Email", "Электронная почта"),
        chapter=C4,
        theory="Elektron pochta (e-mail) — internet orqali xat va fayl yuborish xizmati.\n"
               "Manzil tuzilishi: login@domen, masalan, ali2015@pochta.uz: ali2015 — foydalanuvchi nomi, @ — “at” belgisi, pochta.uz — pochta serveri.\n"
               "Xat qismlari: “Kimga” (qabul qiluvchi manzili), “Mavzu”, xat matni; faylni ilova qilib biriktirish mumkin.\n"
               "Papkalar: Kiruvchi, Yuborilgan, Qoralamalar, Spam, Savat.\n"
               "Pochtaga login va parol bilan kiriladi; notanish xatdagi ilova va havolani ochmang.",
        items=[
            Q("Elektron pochta manzilida qaysi belgi albatta bo‘ladi?", "@", ["#", "&", "*"], x="@ belgisi foydalanuvchi nomini domendan ajratadi."),
            Q("Qaysi yozuv elektron pochta manzili bo‘la oladi?", "ali2015@pochta.uz", ["ali2015.pochta.uz", "ali 2015@pochta", "www.ali2015.uz"],
              x="Pochta manzilida @ belgisi bor va bo‘sh joy yo‘q."),
            Q("Kelgan xatlar qaysi papkada saqlanadi?", "Kiruvchi", ["Yuborilgan", "Qoralamalar", "Savat"], x="Yangi xatlar Kiruvchi papkasiga tushadi."),
            Q("Siz yuborgan xatlar qaysi papkada saqlanadi?", "Yuborilgan", ["Kiruvchi", "Spam", "Qoralamalar"], x="Jo‘natilgan xatlarning nusxasi Yuborilgan papkasida turadi."),
            Q("Xatga rasm yoki hujjat qo‘shish nima deyiladi?", "Faylni ilova qilish", ["Faylni o‘chirish", "Faylni chop etish", "Faylni qayta nomlash"],
              x="Ilova qilingan fayl xat bilan birga yuboriladi."),
            Q("Xatning “Kimga” maydoniga nima yoziladi?", "Qabul qiluvchining manzili", ["Xat matni", "Parol", "Sana"],
              x="“Kimga” maydoniga xat boradigan pochta manzili yoziladi."),
            TF("Elektron pochta orqali faqat matn yuborish mumkin, fayl yuborib bo‘lmaydi.", False, x="Rasm, hujjat va boshqa fayllarni ilova qilish mumkin."),
            Q("Pochta qutisiga kirish uchun nima kerak?", "Login va parol", ["Faqat ism", "Faqat rasm", "Telefon rangi"], x="Login va parol pochtani begonalardan himoya qiladi."),
            Q("Notanish odamdan ilovali shubhali xat keldi. Nima qilasiz?", "Ilovani ochmayman", ["Darhol ochaman", "Hammaga yuboraman", "Parolimni yozib javob beraman"],
              x="Shubhali ilovada virus bo‘lishi mumkin."),
            Q("Oddiy pochtaga qaraganda elektron pochtaning afzalligi nima?", "Tez yetib boradi", ["Marka kerak", "Konvert kerak", "Pochtachi olib boradi"],
              x="Elektron xat bir necha soniyada yetib boradi."),
            ORDER("So‘zlardan gap tuzing", "Xatga mavzu yozishni unutmang"),
            Q("“ali2015@pochta.uz” manzilida foydalanuvchi nomi qaysi?", "ali2015", ["pochta.uz", "@", "uz"], d=2,
              x="@ belgisigacha bo‘lgan qism — foydalanuvchi nomi."),
            Q("“ali2015@pochta.uz” manzilida pochta serveri qaysi?", "pochta.uz", ["ali2015", "ali", "@"], d=2,
              x="@ belgisidan keyingi qism — pochta serveri, ya’ni domen."),
            Q("Tugallanmagan, hali yuborilmagan xat qaysi papkada saqlanadi?", "Qoralamalar", ["Kiruvchi", "Yuborilgan", "Spam"], d=2,
              x="Qoralamada xatni keyin davom ettirib yuborish mumkin."),
            Q("Keraksiz reklama xatlari qaysi papkaga tushadi?", "Spam", ["Yuborilgan", "Qoralamalar", "Kiruvchi"], d=2,
              x="Pochta xizmati keraksiz xatlarni Spam papkasiga ajratadi."),
            Q("Xatning qisqacha mazmuni qaysi maydonga yoziladi?", "Mavzu", ["Kimga", "Parol", "Ilova"], d=2,
              x="Mavzu qabul qiluvchiga xat nima haqida ekanini aytadi."),
            MATCH("Papkani vazifasi bilan juftlang",
                  [("Kiruvchi", "Kelgan xatlar"), ("Yuborilgan", "Jo‘natilgan xatlar"), ("Qoralamalar", "Yuborilmagan xatlar"),
                   ("Spam", "Keraksiz reklama"), ("Savat", "O‘chirilgan xatlar")], d=2, x="Pochta papkalari xatlarni tartibda saqlaydi."),
            TF("Elektron pochta manzilida bo‘sh joy bo‘lmaydi.", True, d=2, x="Manzil bitta uzluksiz yozuv: ali2015@pochta.uz."),
            Q("Kelgan xatga javob yozish uchun qaysi tugma bosiladi?", "Javob berish", ["Yo‘naltirish", "O‘chirish", "Spam"], d=2,
              x="Javob berishda qabul qiluvchi manzili o‘zi yoziladi."),
            Q("Qaysi biri elektron pochta xizmati?", "Gmail", ["Paint", "Scratch", "Excel"], d=2, x="Gmail — Google kompaniyasining pochta xizmati."),
            TF("Bitta xatni bir vaqtda bir nechta manzilga yuborish mumkin.", True, d=2, x="“Kimga” maydoniga bir nechta manzil yozish mumkin."),
            Q("Elektron pochta manzilida @ belgisidan keyin nima yoziladi?", "Pochta serveri nomi", ["Parol", "Xat mavzusi", "Foydalanuvchi nomi"], d=2,
              x="Masalan, ali2015@pochta.uz da @ dan keyin pochta.uz — server nomi."),
            Q("Kelgan xatni boshqa odamga jo‘natish nima deyiladi?", "Yo‘naltirish", ["Javob berish", "Qoralama", "O‘chirish"], d=3,
              x="Yo‘naltirishda xat o‘zgarishsiz boshqa manzilga yuboriladi."),
            Q("“@” belgisi xalq orasida qanday nom bilan ham ataladi?", "Kuchukcha", ["Mushukcha", "Qush", "Baliq"], d=3,
              x="@ belgisi shakli jingalak dumli kuchukchaga o‘xshatiladi."),
        ])

T.topic("xavfsizlik", "🛡️", L("Xavfsizlik va odob", "Online safety and etiquette", "Безопасность и этикет в сети"),
        chapter=C4,
        theory="Internetda o‘zingizni va kompyuterni himoya qiling:\n"
               "• Kuchli parol — kamida 8 belgi: katta va kichik harflar, raqamlar, maxsus belgilar (!, #, $). Parolni hech kimga aytmang.\n"
               "• Shubhali havola va notanish ilovalarni ochmang: ular aldashi yoki virus yuqtirishi mumkin.\n"
               "• Virus — kompyuterga zarar yetkazadigan va o‘zidan nusxa ko‘paytiradigan dastur. Antivirus (Kaspersky, ESET NOD32, Microsoft Defender) ularni topib yo‘q qiladi.\n"
               "• Mualliflik huquqi: boshqalarning rasmi, matni, musiqasi — ularning mehnati; foydalansangiz, muallif va manbani ko‘rsating.\n"
               "• Internetda ham odobli bo‘ling: haqorat qilmang, shaxsiy ma’lumotni tarqatmang.",
        items=[
            Q("Qaysi parol eng kuchli?", "Daryo!Kitob7", ["123456", "qwerty", "ali2014"], x="Uzun, katta-kichik harf, raqam va belgi aralashgan parolni topish qiyin."),
            Q("Kuchli parol kamida nechta belgidan iborat bo‘lishi tavsiya etiladi?", 8, [2, 3, 4], x="Qisqa parolni tez topish mumkin, kamida 8 belgi kerak."),
            TF("Parol sifatida tug‘ilgan kuningizni qo‘yish xavfsiz.", False, x="Tug‘ilgan kunni boshqalar bilishi mumkin, uni topish oson."),
            Q("Kompyuterga zarar yetkazadigan va o‘zidan nusxa ko‘paytiradigan dastur nima?", "Virus", ["Antivirus", "Brauzer", "Matn muharriri"],
              x="Virus fayllarni buzishi va boshqa kompyuterlarga tarqalishi mumkin."),
            Q("Viruslarni topib yo‘q qiladigan dastur qanday ataladi?", "Antivirus", ["Brauzer", "Paint", "Pleyer"], x="Antivirus kompyuterni tekshirib, viruslarni zararsizlantiradi."),
            Q("Virus kompyuterga qanday yo‘l bilan tushishi mumkin?", "Notanish fleshka orqali", ["Monitorni artganda", "Klaviaturani tozalaganda", "Kompyuterni o‘chirganda"],
              x="Virus fleshka, internetdan yuklangan fayl yoki xat ilovasi orqali tushishi mumkin."),
            Q("“Tabriklaymiz! Siz telefon yutdingiz, havolani bosing” degan xabar keldi. Nima qilasiz?", "Bosmayman, o‘chiraman",
              ["Darhol bosaman", "Parolimni yuboraman", "Do‘stlarimga tarqataman"], x="Bunday xabarlar ko‘pincha aldov bo‘ladi."),
            Q("Boshqa odamning rasmini o‘z loyihangizda ishlatsangiz, nima qilish kerak?", "Muallifini ko‘rsatish",
              ["O‘zimniki deb aytish", "Rasmni buzib qo‘yish", "Hech narsa qilmaslik"], x="Muallif va manbani ko‘rsatish — mualliflik huquqini hurmat qilish."),
            TF("Internetdagi har qanday rasmni o‘zimniki deb e’lon qilsam bo‘ladi.", False, x="Rasm uni yaratgan muallifga tegishli."),
            Q("Internetda kimdir sizni haqorat qilsa, nima qilasiz?", "Javob bermay, kattalarga aytaman",
              ["Men ham haqorat qilaman", "Parolimni beraman", "Hammaga tarqataman"], x="Kattalar muammoni hal qilishga yordam beradi."),
            Q("Qaysi ma’lumotni ijtimoiy tarmoqda e’lon qilmaslik kerak?", "Uy manzilini", ["Sevimli kitob nomini", "Chizgan rasmimni", "Ob-havo haqidagi fikrni"],
              x="Uy manzili — shaxsiy ma’lumot, uni begonalar bilmasligi kerak."),
            Q("Kuchli parolda nimalar bo‘lishi kerak?", "Harf, raqam va belgilar", ["Faqat ism", "Faqat bitta raqam", "Faqat tug‘ilgan yil"],
              x="Turli belgilar aralashgan parol ishonchliroq."),
            ORDER("So‘zlardan gap tuzing", "Shubhali havolalarni ochmang"),
            Q("Qaysi biri antivirus dasturi?", "Kaspersky", ["Paint", "Word", "Scratch"], d=2, x="Kaspersky — antivirus dasturi."),
            TF("Antivirus dasturini muntazam yangilab turish kerak.", True, d=2,
               x="Yangi viruslar paydo bo‘lib turadi, yangilangan antivirus ularni taniydi."),
            Q("Mualliflik huquqi belgisi qaysi?", "©", ["@", "#", "&"], d=2, x="© belgisi asar muallifga tegishli ekanini bildiradi."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Virus", "Zararli dastur"), ("Antivirus", "Himoya dasturi"), ("Parol", "Maxfiy so‘z"), ("Spam", "Keraksiz reklama xati"),
                   ("Fishing", "Aldab ma’lumot olish"), ("Mualliflik huquqi", "Yaratuvchining huquqi")], d=2,
                  x="Internet xavfsizligining asosiy tushunchalari."),
            TF("Bitta parolni barcha saytlarda ishlatish xavfsiz.", False, d=2,
               x="Bitta parol o‘g‘irlansa, barcha sahifalaringiz xavf ostida qoladi."),
            Q("Umumiy kompyuterda pochtangizdan chiqishni unutsangiz, nima bo‘lishi mumkin?", "Begona odam xatlaringizni o‘qiydi",
              ["Kompyuter tezlashadi", "Parol kuchayadi", "Printer ishlamay qoladi"], d=2, x="Profildan chiqmasangiz, keyingi odam unga kira oladi."),
            Q("Kiberbulling nima?", "Internetda birovni haqorat qilish", ["Kompyuter o‘yini", "Antivirus turi", "Fayl kengaytmasi"], d=2,
              x="Kiberbulling — internet orqali birovni kamsitish, qo‘rqitish; bunday holatda kattalarga aytish kerak."),
            Q("Internetdan yuklangan faylni ochishdan oldin nima qilish kerak?", "Antivirus bilan tekshirish", ["Hammaga yuborish", "Nomini o‘zgartirish", "Chop etish"], d=2,
              x="Antivirus faylda zararli dastur bor-yo‘qligini aniqlaydi."),
            Q("Aldov yo‘li bilan parol va shaxsiy ma’lumotni o‘g‘irlash nima deb ataladi?", "Fishing", ["Formatlash", "Skanerlash", "Arxivlash"], d=3,
              x="Fishingda soxta sayt yoki xat orqali parol so‘raladi."),
            Q("Internetda katta harflar bilan yozish nimani bildiradi deb qabul qilingan?", "Baqirishni", ["Xursandchilikni", "Sirni", "Xatoni"], d=3,
              x="Tarmoq odobida BUTUN MATNNI katta harflarda yozish baqirishga tenglashtiriladi."),
            Q("Ruxsatsiz nusxalangan dasturdan foydalanish nima deb ataladi?", "Qaroqchilik", ["Dasturlash", "Formatlash", "Arxivlash"], d=3,
              x="Qaroqchilik (piratlik) — muallif ruxsatisiz nusxalash, bu qonunga zid."),
            TF("Ikki bosqichli tekshiruv, masalan SMS kod, hisobni qo‘shimcha himoya qiladi.", True, d=3,
               x="Parol o‘g‘irlansa ham, SMS kodsiz hisobga kirib bo‘lmaydi."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["scratch", "internet", "pochta", "xavfsizlik"], chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["axborot", "kodlash", "olchov", "ikkilik", "kompyuter_tuzilishi", "dasturiy", "fayl",
        "matn_muharriri", "tahrirlash", "algoritm", "blok_sxema", "scratch", "internet", "pochta", "xavfsizlik"], chapter=C4, level=3)

T.write()
