"""Informatika, 4-sinf: assets/data/school/informatics_g4.json va bank_informatics_g4.json.

Mavzular O‘zbekiston boshlang‘ich sinf informatika dasturi yo‘nalishida (3 va 5-sinf oralig‘i): qurilmalar, axborot turlari,
o‘n barmoq usulida terish, matn va rasm muharrirlari, fayl va papkalar, taqdimot, internet, xavfsizlik, algoritm va sikl.
Qoida va savollar matni — o‘zimizniki (darslikdan ko‘chirilmagan).
Robot yurishlari, matn tahriri (Backspace/Delete), fayl va slaydlar soni, terish tezligi Python’da hisoblanadi.
Qayta yaratish: python3 tool/content/school/informatics_g4.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("informatics", 4, L("Informatika", "Computer science", "Информатика"))

C1 = "1-chorak. Kompyuter, axborot va klaviatura"
C2 = "2-chorak. Matn va rasm muharrirlari"
C3 = "3-chorak. Fayllar, taqdimot va internet"
C4 = "4-chorak. Xavfsizlik, algoritm va sikl"

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


# ============================================================ 1-chorak
T.topic("qurilmalar", "🖥️", L("Kompyuter qurilmalari", "Computer devices", "Устройства компьютера"),
        chapter=C1,
        theory="Kompyuter — axborotni qabul qiladigan, saqlaydigan, qayta ishlaydigan va uzatadigan qurilma.\n"
               "• Sistema blokida protsessor (kompyuterning “miyasi”) va xotira joylashgan.\n"
               "• Kiritish qurilmalari kompyuterga axborot kiritadi: klaviatura, sichqoncha, mikrofon, skaner, veb-kamera.\n"
               "• Chiqarish qurilmalari axborotni chiqaradi: monitor, printer, karnay (kolonka), quloqchin, proyektor.\n"
               "Fayllarni olib yurish uchun fleshka ishlatiladi. Noutbukda sichqoncha o‘rniga sensorli panel bor.",
        items=[
            Q("Kompyuterning “miyasi” deb qaysi qism ataladi?", "Protsessor", ["Monitor", "Sichqoncha", "Karnay"],
              x="Protsessor barcha hisob-kitob va buyruqlarni bajaradi."),
            Q("Stol kompyuterida protsessor qayerda joylashgan?", "Sistema blokida", ["Monitorda", "Klaviaturada", "Printerda"],
              x="Protsessor, xotira va disklar sistema bloki ichida turadi."),
            Q("Qaysi biri kiritish qurilmasi?", "Mikrofon", ["Monitor", "Printer", "Karnay"], e="🎤",
              x="Mikrofon ovozni kompyuterga kiritadi."),
            Q("Qaysi biri chiqarish qurilmasi?", "Printer", ["Klaviatura", "Skaner", "Sichqoncha"], e="🖨️",
              x="Printer axborotni qog‘ozga chiqaradi."),
            Q("Qog‘ozdagi rasmni kompyuterga kiritadigan qurilma qaysi?", "Skaner", ["Printer", "Proyektor", "Karnay"],
              x="Skaner qog‘ozdagi tasvirni “o‘qib”, kompyuterga kiritadi."),
            Q("Tasvirni katta ekran yoki devorga chiqaradigan qurilma qaysi?", "Proyektor", ["Skaner", "Klaviatura", "Mikrofon"],
              x="Proyektor sinfda taqdimot ko‘rsatish uchun qulay."),
            Q("Video qo‘ng‘iroqda yuzingizni ko‘rsatadigan qurilma qaysi?", "Veb-kamera", ["Karnay", "Printer", "Fleshka"], e="📷",
              x="Veb-kamera tasvirni kompyuterga kiritadi."),
            Q("Fayllarni bir kompyuterdan boshqasiga olib o‘tish uchun qulay qurilma qaysi?", "Fleshka", ["Monitor", "Karnay", "Sichqoncha"],
              x="Fleshka kichik, uni cho‘ntakda olib yurish mumkin."),
            Q("Noutbukda sichqoncha vazifasini nima bajaradi?", "Sensorli panel", ["Ekran qopqog‘i", "Karnay", "Zaryadlovchi"], e="💻",
              x="Sensorli panelda barmoq yurgizib, ko‘rsatkichni boshqaramiz."),
            Q("Qaysi qurilma ovozni kompyuterga kiritadi?", "Mikrofon", ["Karnay", "Quloqchin", "Monitor"],
              x="Karnay va quloqchin ovozni chiqaradi, mikrofon esa kiritadi."),
            TF("Monitor — chiqarish qurilmasi.", True, x="Monitor axborotni tasvir ko‘rinishida chiqaradi."),
            TF("Klaviatura — chiqarish qurilmasi.", False, x="Klaviatura bilan kompyuterga matn kiritamiz."),
            ORDER(S, "Printer matnni qog‘ozga chiqaradi"),
            Q("Musiqani boshqalarni bezovta qilmay tinglash uchun nima kerak?", "Quloqchin", ["Kolonka", "Proyektor", "Skaner"], d=2, e="🎧",
              x="Quloqchindagi ovozni faqat siz eshitasiz."),
            Q("Qaysi qurilma ham kiritish, ham chiqarish vazifasini bajaradi?", "Sensorli ekran", ["Printer", "Karnay", "Mikrofon"], d=2,
              x="Sensorli ekran tasvirni ko‘rsatadi va barmoq tegishini qabul qiladi."),
            Q("Qaysi guruhda faqat kiritish qurilmalari bor?", "Klaviatura, sichqoncha, skaner",
              ["Monitor, printer, karnay", "Klaviatura, printer, monitor", "Karnay, mikrofon, proyektor"], d=2,
              x="Klaviatura, sichqoncha va skaner kompyuterga axborot kiritadi."),
            Q("Qaysi guruhda faqat chiqarish qurilmalari bor?", "Monitor, printer, karnay",
              ["Skaner, mikrofon, klaviatura", "Sichqoncha, monitor, skaner", "Veb-kamera, printer, mikrofon"], d=2,
              x="Monitor, printer va karnay axborotni chiqaradi."),
            Q("Kompyuter ichida fayllar uzoq saqlanadigan qurilma qaysi?", "Qattiq disk", ["Protsessor", "Karnay", "Sichqoncha"], d=2,
              x="Qattiq disk yoki SSD da fayllar kompyuter o‘chganda ham saqlanadi."),
            Q("Kompyuterni to‘g‘ri o‘chirish uchun nima qilinadi?", "Pusk menyusidan “O‘chirish” tanlanadi",
              ["Vilka rozetkadan sug‘uriladi", "Faqat monitor o‘chiriladi", "Sistema bloki silkitiladi"], d=2,
              x="To‘g‘ri o‘chirilsa, ochiq fayllar buzilmaydi."),
            TF("Planshetning sensorli ekrani ham kiritish, ham chiqarish qurilmasi.", True, d=2,
               x="U tasvirni ko‘rsatadi va barmoq bosishini qabul qiladi."),
            MATCH("Qurilmani vazifasi bilan juftlang",
                  [("Klaviatura", "matn kiritadi"), ("Sichqoncha", "ko‘rsatkichni boshqaradi"), ("Monitor", "tasvirni ko‘rsatadi"),
                   ("Printer", "qog‘ozga chop etadi"), ("Skaner", "qog‘ozdagi rasmni kiritadi"), ("Karnay", "ovozni chiqaradi")], d=2,
                  x="Har bir qurilmaning o‘z vazifasi bor."),
            Q("Kompyuter o‘chsa, qaysi xotiradagi ma’lumot o‘chib ketadi?", "Operativ xotira", ["Qattiq disk", "Fleshka", "SSD disk"], d=3,
              x="Operativ xotira faqat kompyuter ishlab turganda ma’lumotni saqlaydi."),
        ])

T.topic("axborot_turlari", "💡", L("Axborot va uning turlari", "Information and its types", "Информация и её виды"),
        chapter=C1,
        theory="Axborot — atrofimizdagi narsa va hodisalar haqidagi ma’lumotlar.\n"
               "• Sezgi a’zolari bo‘yicha: ko‘rish (ko‘z), eshitish (quloq), hid (burun), ta’m (til), sezish (teri) orqali olinadi.\n"
               "• Ko‘rinishi bo‘yicha: matnli, sonli, grafik (rasm, chizma), tovushli va video axborot.\n"
               "• Axborot bilan ishlar: yig‘ish, saqlash, uzatish, qayta ishlash, himoyalash.\n"
               "Axborot tashuvchilar — axborot saqlanadigan narsalar: kitob, daftar, fleshka, disk.",
        items=[
            Q("Svetoforning yashil chirog‘ini qaysi sezgi a’zosi orqali bilamiz?", "Ko‘z", ["Quloq", "Burun", "Til"], e="🚦",
              x="Rangni ko‘z bilan ko‘ramiz."),
            Q("Telefon jiringlashi qanday axborot?", "Tovushli", ["Grafik", "Matnli", "Sonli"], e="📱",
              x="Jiringlashni quloq bilan eshitamiz."),
            Q("Non hidini qaysi a’zo orqali bilamiz?", "Burun", ["Ko‘z", "Quloq", "Teri"], e="🍞",
              x="Hidni burun sezadi."),
            Q("Daftarga yozilgan she’r qanday axborot?", "Matnli", ["Tovushli", "Video", "Sonli"],
              x="She’r harf va so‘zlardan iborat — matnli axborot."),
            Q("Xarita qanday axborot?", "Grafik", ["Tovushli", "Matnli", "Ta’m"],
              x="Xarita — rasm va chizmalar, ya’ni grafik axborot."),
            Q("Multfilm qanday axborot?", "Video", ["Faqat matnli", "Hid", "Ta’m"],
              x="Multfilmda harakatlanuvchi tasvir va tovush bor."),
            Q("Sinfdagi o‘quvchilar soni qanday axborot?", "Sonli", ["Tovushli", "Grafik", "Video"],
              x="Son bilan ifodalangan axborot — sonli axborot."),
            Q("Qaysi biri axborot tashuvchi?", "Daftar", ["Shamol", "Soya", "Yomg‘ir"],
              x="Daftarga yozilgan axborot saqlanib qoladi."),
            Q("Do‘stga xat yozib yuborish axborot bilan qanday ish?", "Uzatish", ["Saqlash", "Yig‘ish", "Himoyalash"],
              x="Axborot bir odamdan boshqasiga yetkaziladi."),
            Q("Telefon raqamini daftarga yozib qo‘yish qanday ish?", "Saqlash", ["Uzatish", "Qayta ishlash", "Yig‘ish"],
              x="Yozib qo‘yilgan raqam keyin kerak bo‘lganda topiladi."),
            Q("Qo‘lingizdagi muzning sovuqligini qaysi a’zo sezadi?", "Teri", ["Quloq", "Ko‘z", "Burun"],
              x="Issiq-sovuqni teri sezadi."),
            TF("Kitob — axborot tashuvchi.", True, x="Kitobda axborot yozib saqlangan."),
            TF("Rasm ham axborot beradi.", True, x="Rasm — grafik axborot."),
            TF("Axborotni faqat ko‘z orqali olamiz.", False, x="Axborot beshta sezgi a’zosi orqali olinadi."),
            ORDER(S, "Kitob axborotni saqlaydi"),
            Q("Qaysi axborotni oddiy kompyuter saqlay olmaydi?", "Gul hidini", ["Rasmni", "Qo‘shiqni", "Matnni"], d=2,
              x="Oddiy kompyuter matn, son, rasm, tovush va video bilan ishlaydi."),
            Q("Ob-havo ma’lumotini radiodan eshitdik. Bu qanday axborot?", "Tovushli", ["Grafik", "Video", "Matnli"], d=2,
              x="Radio axborotni faqat tovush orqali beradi."),
            Q("Ingliz tilidagi so‘zni o‘zbekchaga tarjima qilish qanday ish?", "Qayta ishlash", ["Saqlash", "Uzatish", "Himoyalash"], d=2,
              x="Axborot yangi ko‘rinishga keltirilmoqda — bu qayta ishlash."),
            Q("Sinfdoshlarning bo‘yini o‘lchab, yozib chiqish qanday ish?", "Yig‘ish", ["Uzatish", "O‘chirish", "Himoyalash"], d=2,
              x="Turli joydan ma’lumot to‘planmoqda — bu yig‘ish."),
            Q("Qaysi axborot ham tovush, ham harakatli tasvirdan iborat?", "Video", ["Matn", "Rasm", "Son"], d=2,
              x="Videoda tasvir ham, ovoz ham bor."),
            MATCH("Axborotni turi bilan juftlang",
                  [("Ertak kitobi", "matnli"), ("Soat ko‘rsatgan vaqt", "sonli"), ("Fotosurat", "grafik"), ("Qush sayrashi", "tovushli"), ("Kino", "video")], d=2,
                  x="Axborot turli ko‘rinishda bo‘ladi."),
            MATCH("Ishni axborot jarayoni bilan juftlang",
                  [("Kundalikka yozish", "saqlash"), ("SMS jo‘natish", "uzatish"), ("Misol yechish", "qayta ishlash"),
                   ("Kuzatib yozib olish", "yig‘ish"), ("Parol qo‘yish", "himoyalash")], d=2,
                  x="Axborot bilan beshta asosiy ish bajariladi."),
            Q("Ko‘zi ojiz odam maxsus kitobni qanday o‘qiydi?", "Barmoqlari bilan sezib", ["Hidlab", "Ta’mini bilib", "Quloqqa tutib"], d=3,
              x="Brayl yozuvidagi bo‘rtma nuqtalarni barmoq sezadi."),
            Q("Kompyuter axborotni qanday ko‘rinishda saqlaydi?", "0 va 1 lardan iborat kod", ["Rangli qog‘oz", "Hid", "Ta’m"], d=3,
              x="Kompyuter har qanday axborotni ikkilik kodga aylantiradi."),
        ])

# --- O'n barmoq usuli: barmoqlar va tezlik (Python'da hisoblanadi).
FINGER = {"A": "Chap jimjiloq", "S": "Chap nomsiz barmoq", "D": "Chap o‘rta barmoq", "F": "Chap ko‘rsatkich barmoq",
          "G": "Chap ko‘rsatkich barmoq", "H": "O‘ng ko‘rsatkich barmoq", "J": "O‘ng ko‘rsatkich barmoq", "K": "O‘ng o‘rta barmoq",
          "L": "O‘ng nomsiz barmoq", "E": "Chap o‘rta barmoq", "U": "O‘ng ko‘rsatkich barmoq", "P": "O‘ng jimjiloq"}
_fingers = sorted(set(FINGER.values()))
_typ = []
for key, d in [("F", 1), ("J", 1), ("A", 2), ("K", 2), ("L", 2), ("E", 3), ("P", 3)]:
    ans = FINGER[key]
    _typ.append(Q(f"O‘n barmoq usulida “{key}” tugmasini qaysi barmoq bosadi?", ans, uniq(ans, [f for f in _fingers if f != ans][::2] + _fingers), d=d,
                  x=f"“{key}” tugmasi — {ans.lower()} zonasida."))
for speed, mins, d in [(40, 3, 1), (60, 5, 2), (35, 4, 2)]:
    tot = speed * mins
    _typ.append(Q(f"Zarina 1 daqiqada {speed} ta belgi teradi. U {mins} daqiqada nechta belgi teradi?", tot,
                  near(tot, [speed + mins, tot + speed, tot - speed, speed * (mins + 1)], lo=1), d=d, x=f"{speed} · {mins} = {tot} ta belgi."))
for total, speed, d in [(120, 40, 2), (300, 60, 3)]:
    m = total // speed
    assert m * speed == total
    _typ.append(Q(f"Bobur 1 daqiqada {speed} ta belgi teradi. {total} belgili matnni necha daqiqada teradi?", f"{m} daqiqada",
                  [f"{v} daqiqada" for v in near(m, [m + 1, m - 1, m + 2, total - speed], lo=1)], d=d, x=f"{total} : {speed} = {m} daqiqa."))
for sent, d in [("Ali va Vali Samarqandga bordi", 2), ("Men Toshkentda yashayman", 1), ("Zarina Bobur va Kamola kitob o‘qidi", 3)]:
    n = sum(1 for ch in sent if ch.isupper())
    _typ.append(Q(f"“{sent}.” gapini terishda Shift bilan nechta bosh harf yoziladi?", n, near(n, [n + 1, n - 1, len(sent.split()), n + 2], lo=1), d=d,
                  x=f"Bosh harflar: {', '.join(ch for ch in sent if ch.isupper())} — jami {n} ta."))

T.topic("tez_terish", "⌨️", L("O‘n barmoq usulida terish", "Touch typing", "Слепой десятипальцевый набор"),
        chapter=C1,
        theory="O‘n barmoq usulida har bir barmoq o‘z tugmalarini bosadi va klaviaturaga qaramasdan teriladi.\n"
               "• Tayanch qator: chap qo‘l barmoqlari A, S, D, F; o‘ng qo‘l barmoqlari J, K, L, ; tugmalarida turadi. F va J dagi bo‘rtiqlar barmoqlarni ko‘rmasdan topishga yordam beradi.\n"
               "• Ko‘rsatkich barmoqlar: chap — F va G, o‘ng — J va H. Probelni bosh barmoq bosadi. Tugmani bosgach, barmoq tayanch qatorga qaytadi.\n"
               "• Bosh harf uchun Shift, hamma harfni bosh harf qilish uchun Caps Lock ishlatiladi.\n"
               "Terish tezligi — 1 daqiqada terilgan belgilar soni. Avval xatosiz, keyin tez terishni o‘rganing.",
        items=[
            Q("Klaviaturaga qaramasdan o‘n barmoq bilan terish usuli nima deyiladi?", "Ko‘r usulda terish", ["Bir barmoqda terish", "Sichqoncha bilan terish", "Ovoz bilan terish"],
              x="Bu usulda barmoqlar tugmalar joyini “yod” biladi."),
            Q("Qaysi tugmalarda barmoqlar uchun bo‘rtiq bor?", "F va J", ["A va L", "Q va P", "Enter va Shift"],
              x="Bo‘rtiqlar ko‘rsatkich barmoqlarning joyini ko‘rsatadi."),
            Q("Probel tugmasini qaysi barmoq bosadi?", "Bosh barmoq", ["Jimjiloq", "O‘rta barmoq", "Nomsiz barmoq"],
              x="Probel pastda, uni bosh barmoq bosadi."),
            Q("Tayanch qatorda chap qo‘l barmoqlari qaysi tugmalarda turadi?", "A, S, D, F", ["Q, W, E, R", "Z, X, C, V", "J, K, L, ;"],
              x="Chap jimjiloq A da, ko‘rsatkich barmoq F da turadi."),
            Q("Tayanch qatorda o‘ng qo‘l barmoqlari qaysi tugmalarda turadi?", "J, K, L, ;", ["A, S, D, F", "U, I, O, P", "M, N, B, V"],
              x="O‘ng ko‘rsatkich J da, jimjiloq ; da turadi."),
            Q("Katta harf yozish uchun harf bilan birga qaysi tugma bosiladi?", "Shift", ["Enter", "Tab", "Esc"],
              x="Shift bosib turilsa, harf bosh harf bo‘lib yoziladi."),
            Q("Hamma harflarni bosh harf bilan yozish rejimini qaysi tugma yoqadi?", "Caps Lock", ["Shift", "Enter", "Delete"],
              x="Caps Lock qayta bosilsa, rejim o‘chadi."),
            Q("Terish tezligi qanday o‘lchanadi?", "1 daqiqada terilgan belgilar soni", ["Klaviatura og‘irligi", "Ekran kattaligi", "Barmoqlar soni"],
              x="Masalan, 1 daqiqada 60 ta belgi."),
            TF("O‘n barmoq usulida klaviaturaga qarab terish kerak.", False, x="Bu usulda ekranga qaraladi, klaviaturaga emas."),
            TF("Har bir tugmani belgilangan barmoq bosadi.", True, x="Shunda barmoqlar chalkashmaydi va terish tezlashadi."),
            TF("Terishni o‘rganayotganda avval xatosiz, keyin tez terish kerak.", True, x="Tezlik mashq bilan o‘zi keladi."),
            ORDER(S, "Barmoqlar tayanch qatorda turadi"),
            Q("Tugmani bosib bo‘lgach, barmoq qayerga qaytadi?", "Tayanch qatorga", ["Sichqonchaga", "Stol ustiga", "Monitorga"], d=2,
              x="Har safar tayanch qatorga qaytish barmoqlarga yo‘l topishni osonlashtiradi."),
            Q("Enter tugmasini qaysi barmoq bosadi?", "O‘ng jimjiloq", ["Chap bosh barmoq", "Chap ko‘rsatkich barmoq", "O‘ng o‘rta barmoq"], d=3,
              x="Enter klaviaturaning o‘ng tomonida, uni o‘ng jimjiloq bosadi."),
            MATCH("Tugmani uni bosadigan barmoq bilan juftlang",
                  [("A", "chap jimjiloq"), ("S", "chap nomsiz barmoq"), ("D", "chap o‘rta barmoq"), ("F", "chap ko‘rsatkich barmoq"),
                   ("K", "o‘ng o‘rta barmoq"), ("Probel", "bosh barmoq")], d=2,
                  x="Tayanch qatordagi har bir tugma o‘z barmog‘iga ega."),
        ] + _typ)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["qurilmalar", "axborot_turlari", "tez_terish"], chapter=C1)

# ============================================================ 2-chorak
# --- Matn tahriri: kursor "|" belgisi bilan ko'rsatiladi, natija Python'da hisoblanadi.


def edit(s, key, n):
    i = s.index("|")
    w = s.replace("|", "")
    return w[:max(0, i - n)] + w[i:] if key == "Backspace" else w[:i] + w[i + n:]


_edit = []
for s, key, n, d in [("KITOBLAR|", "Backspace", 3, 1), ("MAKTAB|LAR", "Delete", 3, 1), ("OQ|QUSH", "Backspace", 2, 2),
                     ("TOSH|KENT", "Delete", 4, 2), ("KITOB|XONA", "Backspace", 5, 2), ("QALAMDON|", "Backspace", 3, 2)]:
    ans = edit(s, key, n)
    other = "Delete" if key == "Backspace" else "Backspace"
    wrong = uniq(ans, [edit(s, other, n), edit(s, key, n - 1), edit(s, key, n + 1), s.replace("|", "")])
    wrong = [w_ if w_ else "(bo‘sh)" for w_ in wrong]
    _edit.append(Q(f"Kursor chiziqcha turgan joyda. {key} tugmasi {n} marta bosilsa, qanday so‘z qoladi?", ans, wrong, d=d, text=s,
                   x=f"{key} kursordan {'chapdagi' if key == 'Backspace' else 'o‘ngdagi'} belgini o‘chiradi: {s} → {ans}."))
for sent, act, d in [("Men har kuni kitob o‘qiyman", "nusxa", 2), ("Bugun havo juda issiq", "qirq", 2), ("Biz maktabda rasm chizdik", "o‘chir", 3)]:
    n = len(sent.split())
    res = n + 1 if act == "nusxa" else (n if act == "qirq" else n - 1)
    desc = {"nusxa": "Bitta so‘z nusxalanib (Ctrl+C), gapning oxiriga qo‘yildi (Ctrl+V).",
            "qirq": "Bitta so‘z qirqib olinib (Ctrl+X), gapning boshqa joyiga qo‘yildi (Ctrl+V).",
            "o‘chir": "Bitta so‘z qirqib olindi (Ctrl+X), lekin hech qayerga qo‘yilmadi."}[act]
    _edit.append(Q(f"“{sent}.” gapida {n} ta so‘z bor. {desc} Endi gapda nechta so‘z bor?", res,
                   near(res, [n, n + 1, n - 1, n + 2], lo=1), d=d,
                   x={"nusxa": f"Nusxalashda so‘z joyida qoladi va yana bittasi qo‘shiladi: {n} + 1 = {res}.",
                      "qirq": f"Qirqilgan so‘z boshqa joyga qo‘yildi, so‘zlar soni o‘zgarmadi: {res}.",
                      "o‘chir": f"Qirqilgan so‘z qo‘yilmadi: {n} − 1 = {res}."}[act]))

T.topic("matn_tahrir", "📝", L("Matn yozish va tahrirlash", "Typing and editing text", "Набор и редактирование текста"),
        chapter=C2,
        theory="Matn muharririda (Bloknot, Word) matn yoziladi va tahrirlanadi. Kursor — matn yoziladigan joyni ko‘rsatuvchi miltillovchi chiziq.\n"
               "• Backspace — kursordan chapdagi belgini, Delete — o‘ngdagi belgini o‘chiradi. Enter — yangi xatboshi boshlaydi.\n"
               "• Belgilash: sichqoncha bilan sudrab; so‘zni ikki marta bosib; hamma matnni — Ctrl+A.\n"
               "• Belgilangan matnni nusxalash — Ctrl+C, qirqish — Ctrl+X, qo‘yish — Ctrl+V. Xato amalni bekor qilish — Ctrl+Z.\n"
               "Nusxalashda matn joyida qoladi, qirqishda esa eski joyidan olib tashlanadi.",
        items=[
            Q("Kursordan chapdagi belgini qaysi tugma o‘chiradi?", "Backspace", ["Delete", "Enter", "Shift"],
              x="Backspace orqaga qarab o‘chiradi."),
            Q("Kursordan o‘ngdagi belgini qaysi tugma o‘chiradi?", "Delete", ["Backspace", "Enter", "Tab"],
              x="Delete kursordan keyingi belgini o‘chiradi."),
            Q("Yangi xatboshini qaysi tugma boshlaydi?", "Enter", ["Backspace", "Esc", "Delete"],
              x="Enter kursorni yangi qatorga o‘tkazadi."),
            Q("Butun matnni belgilash uchun qaysi tugmalar bosiladi?", "Ctrl+A", ["Ctrl+Z", "Ctrl+S", "Ctrl+P"],
              x="A — inglizcha All, ya’ni “hammasi”."),
            Q("Belgilangan matnni nusxalash uchun qaysi tugmalar bosiladi?", "Ctrl+C", ["Ctrl+V", "Ctrl+X", "Ctrl+A"],
              x="Ctrl+C matnni xotiraga nusxalaydi."),
            Q("Nusxalangan matnni qo‘yish uchun qaysi tugmalar bosiladi?", "Ctrl+V", ["Ctrl+C", "Ctrl+Z", "Ctrl+B"],
              x="Ctrl+V xotiradagi matnni kursor turgan joyga qo‘yadi."),
            Q("Belgilangan matnni qirqib olish uchun qaysi tugmalar bosiladi?", "Ctrl+X", ["Ctrl+C", "Ctrl+V", "Ctrl+S"],
              x="Qirqilgan matn joyidan yo‘qoladi va xotiraga olinadi."),
            Q("Oxirgi xato amalni bekor qilish uchun qaysi tugmalar bosiladi?", "Ctrl+Z", ["Ctrl+X", "Ctrl+A", "Ctrl+C"],
              x="Ctrl+Z oxirgi amalni ortga qaytaradi."),
            Q("Matn yoziladigan joyni ko‘rsatuvchi miltillovchi chiziq nima?", "Kursor", ["Belgi", "Ikonka", "Oyna"],
              x="Harflar kursor turgan joyga yoziladi."),
            TF("Nusxalashda matn eski joyida qoladi.", True, x="Nusxalashda matnning ikkinchi nusxasi paydo bo‘ladi."),
            TF("Qirqishda matn eski joyida qoladi.", False, x="Qirqishda matn eski joyidan olib tashlanadi."),
            ORDER(S, "Backspace kursordan chapdagi belgini o‘chiradi"),
            Q("So‘zni tez belgilash uchun unga nima qilinadi?", "Ikki marta bosiladi", ["O‘ng tugma bir marta bosiladi", "Enter bosiladi", "Delete bosiladi"], d=2,
              x="So‘z ustida sichqonchani ikki marta bossangiz, butun so‘z belgilanadi."),
            MATCH("Tugmalarni amal bilan juftlang",
                  [("Ctrl+C", "nusxalash"), ("Ctrl+X", "qirqish"), ("Ctrl+V", "qo‘yish"), ("Ctrl+Z", "bekor qilish"), ("Ctrl+A", "hammasini belgilash")], d=2,
                  x="Bu tugmalar deyarli barcha dasturlarda ishlaydi."),
        ] + _edit)

T.topic("matn_bezash", "🔤", L("Matnni bezash va saqlash", "Formatting and saving text", "Оформление и сохранение текста"),
        chapter=C2,
        theory="Matnni bezash (formatlash) — uning ko‘rinishini o‘zgartirish. Bezashdan oldin matn belgilanadi.\n"
               "• Shrift — harflar shakli (Arial, Times New Roman); shrift o‘lchami — harflar kattaligi: son qancha katta bo‘lsa, harf shuncha yirik.\n"
               "• B — qalin, I — kursiv (qiya), U — tagiga chizilgan. Shrift rangi ostida rangli chizig‘i bor “A” tugmasi bilan o‘zgartiriladi.\n"
               "• Tekislash: chapga, markazga, o‘ngga va kenglik bo‘yicha (ikki chetga). Sarlavha odatda markazga tekislanadi.\n"
               "• Saqlash — Ctrl+S; yangi nom yoki joy bilan — “Saqlash sifatida”. Word hujjati .docx, Bloknot matni .txt kengaytmali.",
        items=[
            Q("Harflarning shakli nima deb ataladi?", "Shrift", ["Kursor", "Xatboshi", "Papka"],
              x="Masalan, Arial va Times New Roman — turli shriftlar."),
            Q("Shrift o‘lchami 12 dan 20 ga o‘zgartirildi. Harflar qanday bo‘ladi?", "Kattaroq", ["Kichikroq", "Qiya", "Rangli"],
              x="O‘lcham soni oshsa, harflar yiriklashadi."),
            Q("B tugmasi matnni qanday qiladi?", "Qalin", ["Qiya", "Tagiga chizilgan", "Qizil"],
              x="B — inglizcha Bold, ya’ni “qalin”."),
            Q("I tugmasi matnni qanday qiladi?", "Kursiv (qiya)", ["Qalin", "Tagiga chizilgan", "Katta"],
              x="I — inglizcha Italic, ya’ni “qiya”."),
            Q("U tugmasi matnni qanday qiladi?", "Tagiga chizilgan", ["Qalin", "Qiya", "Yashirin"],
              x="U — inglizcha Underline, ya’ni “tagiga chizish”."),
            Q("Sarlavha odatda qanday tekislanadi?", "Markazga", ["Chapga", "O‘ngga", "Pastga"],
              x="Markazdagi sarlavha chiroyli va ko‘zga tashlanadi."),
            Q("Hujjatni saqlash uchun qaysi tugmalar bosiladi?", "Ctrl+S", ["Ctrl+Z", "Ctrl+P", "Ctrl+A"],
              x="S — inglizcha Save, ya’ni “saqlash”."),
            Q("Matnni bezashdan oldin nima qilish kerak?", "Uni belgilash", ["Uni o‘chirish", "Kompyuterni o‘chirish", "Faylni yopish"],
              x="Bezash faqat belgilangan matnga qo‘llanadi."),
            Q("Qaysi shrift o‘lchamida harflar eng kichik?", "8", ["12", "16", "24"],
              x="O‘lcham soni qancha kichik bo‘lsa, harflar shuncha mayda."),
            TF("Saqlanmagan hujjat kompyuter o‘chsa yo‘qolib qolishi mumkin.", True, x="Shuning uchun ishni tez-tez saqlab turish kerak."),
            TF("Shrift o‘lchami qancha kichik bo‘lsa, harflar shuncha katta.", False, x="Aksincha: o‘lcham kichik — harflar mayda."),
            ORDER(S, "Sarlavhani markazga tekislaymiz"),
            Q("Word hujjati qaysi kengaytma bilan saqlanadi?", "docx", ["mp3", "jpg", "exe"], d=2,
              x="docx — Word hujjatlari kengaytmasi."),
            Q("Hujjatni yangi nom bilan saqlash uchun qaysi buyruq tanlanadi?", "Saqlash sifatida", ["Ochish", "Chop etish", "Yopish"], d=2,
              x="“Saqlash sifatida” oynasida yangi nom va joy tanlanadi."),
            Q("Harflar rangini o‘zgartiradigan tugma qanday ko‘rinadi?", "Ostida rangli chiziqli “A”", ["“B” harfi", "Qaychi rasmi", "Disket rasmi"], d=2,
              x="“A” ostidagi chiziq tanlangan rangni ko‘rsatadi."),
            Q("Matn ikki chetga ham tekis tegib turishi uchun qanday tekislash tanlanadi?", "Kenglik bo‘yicha", ["Chapga", "Markazga", "O‘ngga"], d=2,
              x="Kenglik bo‘yicha tekislashda qatorlar ikki chetga ham tegib turadi."),
            Q("Qalin shrift uchun qaysi tugmalar bosiladi?", "Ctrl+B", ["Ctrl+I", "Ctrl+U", "Ctrl+C"], d=2,
              x="Ctrl+B — qalin, Ctrl+I — kursiv, Ctrl+U — tagiga chizish."),
            TF("Bir so‘zni ham qalin, ham kursiv qilish mumkin.", True, d=2, x="Bir nechta bezash birga qo‘llanishi mumkin."),
            MATCH("Tugmani vazifasi bilan juftlang",
                  [("B", "qalin"), ("I", "kursiv"), ("U", "tagiga chizish"), ("Ctrl+S", "saqlash"), ("Ctrl+E", "markazga tekislash")], d=2,
                  x="Tugmalarni eslab qolsangiz, ish tezlashadi."),
            Q("Matnni markazga tekislash uchun qaysi tugmalar bosiladi?", "Ctrl+E", ["Ctrl+L", "Ctrl+R", "Ctrl+J"], d=3,
              x="Ctrl+L — chapga, Ctrl+E — markazga, Ctrl+R — o‘ngga, Ctrl+J — kenglik bo‘yicha."),
            Q("Disket rasmi tushirilgan tugma nima qiladi?", "Hujjatni saqlaydi", ["Hujjatni o‘chiradi", "Chop etadi", "Matnni bo‘yaydi"], d=3,
              x="Disket — qadimgi axborot tashuvchi, u “saqlash” belgisi bo‘lib qolgan."),
        ])

T.topic("rasm_muharriri", "🎨", L("Rasm muharriri", "Graphics editor", "Графический редактор"),
        chapter=C2,
        theory="Rasm muharriri (masalan, Paint) — kompyuterda rasm chizish dasturi.\n"
               "• Asboblar: qalam — ingichka chiziq, cho‘tka — qalin chiziq, o‘chirg‘ich — o‘chiradi, bo‘yoq chelak — yopiq sohani bo‘yaydi, pipetka — rasmdagi rangni oladi, lupa — kattalashtiradi, “A” — matn yozadi.\n"
               "• Shakllar: chiziq, to‘g‘ri to‘rtburchak, oval va boshqalar. Shift bosib turib chizilsa, oval — aylana, to‘rtburchak — kvadrat bo‘ladi.\n"
               "• Ranglar palitrada. Rang 1 sichqonchaning chap tugmasi, Rang 2 (fon rangi) o‘ng tugmasi bilan ishlatiladi.\n"
               "Rasm .png yoki .jpg fayl sifatida saqlanadi. Xato bo‘lsa — Ctrl+Z.",
        items=[
            Q("Yopiq shaklni bir bosishda bo‘yaydigan asbob qaysi?", "Bo‘yoq chelak", ["Qalam", "Lupa", "O‘chirg‘ich"],
              x="Chelak bilan bosilgan yopiq soha butunlay bo‘yaladi."),
            Q("Rasmning bir qismini o‘chiradigan asbob qaysi?", "O‘chirg‘ich", ["Cho‘tka", "Pipetka", "Qalam"],
              x="O‘chirg‘ich o‘chirilgan joyni fon rangiga bo‘yaydi."),
            Q("Rasmdagi rangni “olib” beradigan asbob qaysi?", "Pipetka", ["Lupa", "Chelak", "Cho‘tka"],
              x="Pipetka bilan rasmdagi nuqta bosilsa, uning rangi tanlanadi."),
            Q("Rasmni kattalashtirib ko‘rsatadigan asbob qaysi?", "Lupa", ["Pipetka", "Qalam", "Chelak"],
              x="Lupa mayda qismlarni chizishga yordam beradi."),
            Q("Rasmga yozuv qo‘shish uchun qaysi asbob tanlanadi?", "“A” — matn", ["O‘chirg‘ich", "Chelak", "Pipetka"],
              x="“A” asbobi bilan rasm ustiga matn yoziladi."),
            Q("Ingichka erkin chiziq chizadigan asbob qaysi?", "Qalam", ["Chelak", "Lupa", "O‘chirg‘ich"],
              x="Qalam bilan xuddi qog‘ozdagidek chiziladi."),
            Q("Paint oynasidagi ranglar to‘plami nima deb ataladi?", "Palitra", ["Menyu", "Papka", "Shrift"],
              x="Palitradan kerakli rang tanlanadi."),
            Q("Xato chizilgan chiziqni tez bekor qilish uchun qaysi tugmalar bosiladi?", "Ctrl+Z", ["Ctrl+S", "Ctrl+A", "Ctrl+P"],
              x="Ctrl+Z oxirgi amalni bekor qiladi."),
            Q("Rasm qanday axborot turiga kiradi?", "Grafik", ["Tovushli", "Sonli", "Matnli"],
              x="Rasm, chizma, xarita — grafik axborot."),
            TF("Paint — rasm chizish dasturi.", True, x="Paint Windows tarkibidagi oddiy rasm muharriri."),
            TF("O‘chirg‘ich rasmni rangli bo‘yaydi.", False, x="O‘chirg‘ich chizilgan narsani o‘chiradi."),
            ORDER(S, "Bo‘yoq chelak yopiq shaklni bo‘yaydi"),
            Q("Aylana chizish uchun oval chizayotganda qaysi tugma bosib turiladi?", "Shift", ["Ctrl", "Enter", "Alt"], d=2,
              x="Shift bilan oval teng tomonli — aylana bo‘ladi."),
            Q("Kvadrat chizish uchun nima qilinadi?", "To‘rtburchak Shift bilan chiziladi", ["Oval Ctrl bilan chiziladi", "Chiziq Enter bilan chiziladi", "Chelak bilan bosiladi"], d=2,
              x="Shift bosilganda to‘rtburchakning hamma tomoni teng bo‘ladi."),
            Q("Paint’da rasm qaysi kengaytma bilan saqlanishi mumkin?", "png", ["docx", "mp3", "pptx"], d=2,
              x="Rasm fayllari: png, jpg, bmp."),
            Q("Rasmning bir qismini belgilab, boshqa joyga surish uchun qaysi asbob kerak?", "Belgilash", ["Pipetka", "Chelak", "Lupa"], d=2,
              x="Belgilangan qismni sichqoncha bilan sudrab ko‘chirish mumkin."),
            TF("Pipetka bilan olingan rangni keyin boshqa joyda ishlatish mumkin.", True, d=2, x="Olingan rang Rang 1 ga o‘rnatiladi."),
            MATCH("Asbobni vazifasi bilan juftlang",
                  [("Qalam", "ingichka chiziq"), ("Cho‘tka", "qalin chiziq"), ("O‘chirg‘ich", "o‘chiradi"), ("Bo‘yoq chelak", "yopiq sohani bo‘yaydi"),
                   ("Pipetka", "rangni oladi"), ("Lupa", "kattalashtiradi")], d=2,
                  x="Har bir asbobning o‘z vazifasi bor."),
            Q("Chiziqlari tutashmagan shakl chelak bilan bo‘yalsa nima bo‘ladi?", "Bo‘yoq tashqariga ham to‘kiladi", ["Hech narsa bo‘lmaydi", "Shakl o‘chib ketadi", "Faqat chegarasi bo‘yaladi"], d=3,
              x="Chelak faqat yopiq sohani bo‘yaydi, tirqish bo‘lsa, rang tashqariga “oqadi”."),
            Q("Sichqonchaning chap tugmasi bilan chizilganda qaysi rang ishlatiladi?", "Rang 1", ["Rang 2", "Doim oq", "Doim qora"], d=3,
              x="Chap tugma — Rang 1, o‘ng tugma — Rang 2."),
            Q("Kompyuter ekranidagi har bir rang qaysi uch rang aralashmasidan hosil bo‘ladi?", "Qizil, yashil, ko‘k", ["Qizil, sariq, ko‘k", "Oq, qora, kulrang", "Sariq, binafsha, jigarrang"], d=3,
              x="Ekrandagi har bir nuqta qizil, yashil va ko‘k nurlarning aralashmasidan iborat."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["matn_tahrir", "matn_bezash", "rasm_muharriri"], chapter=C2)

# ============================================================ 3-chorak
_files = []
for n, move, copy, d in [(7, 2, 3, 2), (10, 4, 1, 2), (8, 5, 2, 3)]:
    left = n - move
    dest = move + copy
    _files.append(Q(f"“Rasmlar” papkasida {n} ta fayl bor. {move} tasi “Albom” papkasiga ko‘chirildi, {copy} tasi “Albom”ga nusxalandi. “Rasmlar”da nechta fayl qoldi?",
                    left, near(left, [n - move - copy, n, n + copy, left + 1], lo=0), d=d,
                    x=f"Ko‘chirilgan fayllar ketadi, nusxalanganlar qoladi: {n} − {move} = {left}."))
    _files.append(Q(f"Bo‘sh “Albom” papkasiga {move} ta fayl ko‘chirildi va {copy} ta fayl nusxalandi. “Albom”da nechta fayl bor?",
                    dest, near(dest, [move, copy, dest + 1, n], lo=0), d=d,
                    x=f"Ko‘chirilgan ham, nusxalangan ham yangi papkada paydo bo‘ladi: {move} + {copy} = {dest}."))
for n, dl, back, d in [(6, 3, 1, 2), (9, 4, 2, 3)]:
    now = n - dl + back
    _files.append(Q(f"Papkada {n} ta fayl bor edi. {dl} tasi o‘chirildi, keyin {back} tasi Savatdan tiklandi. Papkada nechta fayl bor?",
                    now, near(now, [n - dl, n, now + 1, dl + back], lo=0), d=d,
                    x=f"{n} − {dl} + {back} = {now}. Savatda {dl - back} ta fayl qoldi."))

T.topic("fayllar", "📁", L("Fayl va papkalar bilan ishlash", "Working with files and folders", "Работа с файлами и папками"),
        chapter=C3,
        theory="Fayl — nomi bilan saqlangan ma’lumot (matn, rasm, musiqa). Papka — fayllar va boshqa papkalarni saqlaydigan joy.\n"
               "• Yangi papka: bo‘sh joyda o‘ng tugma → “Yaratish” → “Papka”. Nomini o‘zgartirish — F2 tugmasi.\n"
               "• Nusxalash (Ctrl+C, keyin Ctrl+V) — fayl eski joyida ham qoladi, yangi joyda nusxasi paydo bo‘ladi.\n"
               "• Ko‘chirish (Ctrl+X, keyin Ctrl+V) — fayl eski joyidan yangi joyga o‘tadi.\n"
               "• O‘chirilgan fayl avval Savatga tushadi, undan tiklash mumkin. Savat tozalansa, fayl butunlay o‘chadi.",
        items=[
            Q("Fayl nusxalanganda asl fayl bilan nima bo‘ladi?", "Joyida qoladi", ["O‘chib ketadi", "Savatga tushadi", "Nomi o‘zgaradi"],
              x="Nusxalashda asl fayl joyida qoladi, yangi joyda nusxasi paydo bo‘ladi."),
            Q("O‘chirilgan fayllar avval qayerga tushadi?", "Savatga", ["Fleshkaga", "Printerga", "Ish stolidagi papkaga"],
              x="Savatdagi faylni keyin tiklash mumkin."),
            Q("Savatdagi faylni qaytarish nima deyiladi?", "Tiklash", ["Nusxalash", "Chop etish", "Qirqish"],
              x="“Tiklash” buyrug‘i faylni avvalgi joyiga qaytaradi."),
            Q("Fayllar va boshqa papkalarni saqlaydigan joy nima?", "Papka", ["Kursor", "Shrift", "Palitra"], e="📁",
              x="Papkalar fayllarni tartibli saqlashga yordam beradi."),
            Q("Yangi papka yaratish uchun bo‘sh joyda nima qilinadi?", "O‘ng tugma → Yaratish → Papka", ["Chap tugma ikki marta bosiladi", "Delete bosiladi", "Enter bosiladi"],
              x="O‘ng tugma kontekst menyuni ochadi."),
            Q("Faylni o‘chirish uchun uni belgilab qaysi tugma bosiladi?", "Delete", ["Enter", "F2", "Shift"],
              x="Delete faylni Savatga yuboradi."),
            Q("Faylni ochish uchun unga nima qilinadi?", "Ikki marta bosiladi", ["O‘ng tugma bir marta bosiladi", "Delete bosiladi", "F2 bosiladi"],
              x="Sichqonchaning chap tugmasi bilan ikki marta bosilsa, fayl ochiladi."),
            TF("Bir papka ichida boshqa papka bo‘lishi mumkin.", True, x="Masalan, “Maktab” papkasi ichida “Rasmlar” papkasi."),
            ORDER(S, "O‘chirilgan fayl Savatga tushadi"),
            Q("Fayl nomini o‘zgartirish uchun qaysi tugma bosiladi?", "F2", ["F1", "Esc", "Tab"], d=2,
              x="Faylni belgilab F2 bosilsa, nomini yozish mumkin."),
            Q("Fayl ko‘chirilganda asl joyda nima qoladi?", "Hech narsa", ["Asl fayl", "Faylning nusxasi", "Faylning nomi"], d=2,
              x="Ko‘chirishda fayl eski joydan yangi joyga to‘liq o‘tadi."),
            Q("Faylni ko‘chirish uchun qaysi tugmalar ketma-ket bosiladi?", "Ctrl+X, keyin Ctrl+V", ["Ctrl+C, keyin Ctrl+Z", "Ctrl+A, keyin Delete", "Ctrl+S, keyin Ctrl+P"], d=2,
              x="Qirqish va qo‘yish — ko‘chirish."),
            Q("Faylni nusxalash uchun qaysi tugmalar ketma-ket bosiladi?", "Ctrl+C, keyin Ctrl+V", ["Ctrl+X, keyin Delete", "Ctrl+Z, keyin Ctrl+V", "Ctrl+A, keyin Ctrl+S"], d=2,
              x="Nusxalash va qo‘yish — nusxa hosil qiladi."),
            Q("“rasm.png” faylida “png” nima?", "Kengaytma", ["Papka nomi", "Disk nomi", "Parol"], d=2,
              x="Kengaytma fayl turini bildiradi: png — rasm."),
            Q("Qaysi kengaytma musiqa fayliniki?", "mp3", ["docx", "png", "txt"], d=2,
              x="mp3 — musiqa, docx — matn hujjati, png — rasm."),
            TF("Savat tozalansa, undagi fayllar butunlay o‘chadi.", True, d=2, x="Tozalangan Savatdan faylni oddiy yo‘l bilan qaytarib bo‘lmaydi."),
            MATCH("Amalni natijasi bilan juftlang",
                  [("Nusxalash", "asl fayl joyida qoladi"), ("Ko‘chirish", "fayl yangi joyga o‘tadi"), ("O‘chirish", "fayl Savatga tushadi"),
                   ("Tiklash", "fayl Savatdan qaytadi"), ("Nomini o‘zgartirish", "fayl yangi nom oladi")], d=2,
                  x="Fayllar bilan asosiy amallar."),
            Q("Qaysi papka nomini Windows qabul qiladi?", "Sayohat rasmlari", ["Rasmlar?", "Dars:1", "Uy/vazifa"], d=3,
              x="Papka va fayl nomlarida \\ / : * ? \" < > | belgilari ishlatilmaydi."),
            TF("Bir papkada nomi va kengaytmasi bir xil ikki fayl bo‘lishi mumkin.", False, d=3,
               x="Bir papkada bir xil to‘liq nomli ikki fayl bo‘lolmaydi."),
        ] + _files)

_slides = []
for n, sec, d in [(10, 30, 1), (12, 20, 2), (6, 60, 2), (15, 40, 3)]:
    total = n * sec
    m = total // 60
    assert m * 60 == total
    _slides.append(Q(f"Taqdimotda {n} ta slayd bor. Har bir slayd {sec} soniya ko‘rsatiladi. Butun namoyish necha daqiqa davom etadi?", f"{m} daqiqa",
                     [f"{v} daqiqa" for v in near(m, [n, m + 1, m - 1, m * 2, n + sec // 10], lo=1)], d=d,
                     x=f"{n} · {sec} = {total} soniya = {total} : 60 = {m} daqiqa."))
for n, dl, add, d in [(8, 2, 3, 2), (5, 1, 4, 2)]:
    res = n - dl + add
    _slides.append(Q(f"Taqdimotda {n} ta slayd bor edi. {dl} tasi o‘chirildi, {add} ta yangi slayd qo‘shildi. Endi nechta slayd bor?", res,
                     near(res, [n + add, n - dl, res + 1, res - 1], lo=1), d=d, x=f"{n} − {dl} + {add} = {res}."))

T.topic("taqdimot", "📊", L("Taqdimot tayyorlash", "Making a presentation", "Создание презентации"),
        chapter=C3,
        theory="Taqdimot — slaydlar ketma-ketligi, u ma’ruza yoki loyihani ko‘rsatish uchun tayyorlanadi. Dasturlar: PowerPoint, LibreOffice Impress.\n"
               "• Slayd — taqdimotning bitta sahifasi. Unda sarlavha, matn, rasm, jadval bo‘lishi mumkin. Birinchi slaydga mavzu va muallif yoziladi.\n"
               "• Yangi slayd — Ctrl+M. Rasm qo‘shish — “Qo‘yish” → “Rasm”. “Dizayn” bo‘limida slayd foni va mavzusi tanlanadi.\n"
               "• Namoyishni boshlash — F5, to‘xtatish — Esc. Fayl .pptx kengaytmasi bilan saqlanadi.\n"
               "Yaxshi slayd: qisqa matn, yirik shrift, mos rasm, ko‘zga yoqimli ranglar.",
        items=[
            Q("Taqdimotning bitta sahifasi nima deyiladi?", "Slayd", ["Varaq", "Papka", "Katak"],
              x="Taqdimot slaydlardan iborat."),
            Q("Qaysi dastur taqdimot tayyorlaydi?", "PowerPoint", ["Paint", "Kalkulyator", "Bloknot"],
              x="PowerPoint — taqdimot dasturi."),
            Q("Taqdimot namoyishini boshidan boshlash uchun qaysi tugma bosiladi?", "F5", ["F2", "Esc", "Delete"],
              x="F5 namoyishni birinchi slayddan boshlaydi."),
            Q("Namoyishdan chiqish uchun qaysi tugma bosiladi?", "Esc", ["F5", "Enter", "Shift"],
              x="Esc namoyishni to‘xtatadi."),
            Q("Slaydga rasm qo‘shish uchun qaysi menyu ochiladi?", "Qo‘yish", ["Fayl", "Ko‘rinish", "Yordam"],
              x="“Qo‘yish” menyusida rasm, jadval, shakl qo‘shiladi."),
            Q("Slayddagi matn qanday bo‘lgani yaxshi?", "Qisqa va yirik", ["Uzun va mayda", "Rangsiz va xira", "Butun sahifaga to‘la"],
              x="Tomoshabin qisqa va yirik matnni oson o‘qiydi."),
            TF("Slaydga rasm qo‘shish mumkin.", True, x="Rasm slaydni qiziqarli qiladi."),
            TF("Slaydga iloji boricha ko‘p mayda matn yozish kerak.", False, x="Ko‘p mayda matnni tomoshabin o‘qiy olmaydi."),
            ORDER(S, "F5 tugmasi namoyishni boshlaydi"),
            Q("Yangi slayd qo‘shish uchun qaysi tugmalar bosiladi?", "Ctrl+M", ["Ctrl+S", "Ctrl+Z", "Ctrl+P"], d=2,
              x="Ctrl+M yangi slayd qo‘shadi."),
            Q("Birinchi slaydga odatda nima yoziladi?", "Mavzu va muallif", ["Faqat rasm", "Oxirgi xulosa", "Hech narsa"], d=2,
              x="Birinchi slayd — taqdimotning “muqovasi”."),
            Q("PowerPoint taqdimoti fayli qaysi kengaytmaga ega?", "pptx", ["docx", "mp3", "png"], d=2,
              x="pptx — PowerPoint taqdimotlari kengaytmasi."),
            Q("Slaydlar almashganda chiqadigan effekt nima deyiladi?", "O‘tish effekti", ["Shrift", "Kengaytma", "Kursor"], d=2,
              x="O‘tish effekti bir slayddan ikkinchisiga chiroyli o‘tishni ta’minlaydi."),
            Q("Slayddagi rasmning harakatlanib paydo bo‘lishi nima deyiladi?", "Animatsiya", ["Fon", "Maket", "Sarlavha"], d=2,
              x="Animatsiya slayd ichidagi obyektlarga qo‘llanadi."),
            Q("Slayd foni va rang mavzusi qayerda tanlanadi?", "Dizayn bo‘limida", ["Savatda", "Kalkulyatorda", "Sichqoncha sozlamasida"], d=2,
              x="Dizayn bo‘limida tayyor mavzular bor."),
            Q("Sinf oldida taqdimot ko‘rsatish uchun qaysi qurilma qulay?", "Proyektor", ["Skaner", "Mikrofon", "Printer"], d=2,
              x="Proyektor slaydni katta ekranga chiqaradi."),
            TF("Taqdimotda slaydlar tartibini o‘zgartirish mumkin.", True, d=2, x="Slaydni sichqoncha bilan sudrab, boshqa joyga qo‘yish mumkin."),
            MATCH("Amalni tugma yoki buyruq bilan juftlang",
                  [("Namoyishni boshlash", "F5"), ("Namoyishdan chiqish", "Esc"), ("Yangi slayd", "Ctrl+M"), ("Rasm qo‘shish", "Qo‘yish → Rasm"),
                   ("Saqlash", "Ctrl+S")], d=2,
                  x="Taqdimot bilan ishlashning asosiy amallari."),
        ] + _slides)

T.topic("internet", "🌐", L("Internet va brauzer", "The internet and browsers", "Интернет и браузер"),
        chapter=C3,
        theory="Internet — butun dunyodagi kompyuterlarni bog‘lovchi ulkan tarmoq.\n"
               "• Brauzer — saytlarni ochib ko‘rsatadigan dastur: Google Chrome, Mozilla Firefox, Microsoft Edge, Opera.\n"
               "• Sayt — veb-sahifalar to‘plami. Sayt manzili brauzerning manzil satriga yoziladi. Havola bosilsa, boshqa sahifa ochiladi.\n"
               "• Qidiruv tizimi (Google, Yandex) kalit so‘zlar bo‘yicha ma’lumot topadi. Topilgan ma’lumotni bir necha manbada solishtiring.\n"
               "Wi-Fi — kompyuter va telefonni internetga simsiz ulash usuli.",
        items=[
            Q("Butun dunyo kompyuterlarini bog‘lovchi tarmoq qanday ataladi?", "Internet", ["Paint", "Bloknot", "Kalkulyator"], e="🌐",
              x="Internet orqali istalgan mamlakatdagi saytni ochish mumkin."),
            Q("Google Chrome qanday dastur?", "Brauzer", ["Rasm muharriri", "O‘yin", "Antivirus"],
              x="Chrome — saytlarni ko‘rish dasturi."),
            Q("Google va Yandex nima?", "Qidiruv tizimlari", ["Matn muharrirlari", "Printerlar", "Fayl turlari"],
              x="Ular kalit so‘zlar bo‘yicha saytlarni topadi."),
            Q("Sayt manzili brauzerning qayeriga yoziladi?", "Manzil satriga", ["Savatga", "Ish stoliga", "Paint oynasiga"],
              x="Manzil satri brauzer oynasining yuqorisida joylashgan."),
            Q("Sayt nima?", "Veb-sahifalar to‘plami", ["Kompyuter qismi", "Rasm chizish dasturi", "Fayl kengaytmasi"],
              x="Saytda bir-biriga havolalar bilan bog‘langan sahifalar bor."),
            Q("Sahifadagi bosilsa boshqa sahifa ochiladigan so‘z yoki rasm nima?", "Havola", ["Sarlavha", "Kursor", "Papka"],
              x="Havola ustiga kelganda ko‘rsatkich qo‘lcha shakliga kiradi."),
            Q("Internetdan faylni o‘z kompyuteringizga olish nima deyiladi?", "Yuklab olish", ["Chop etish", "O‘chirish", "Qirqish"],
              x="Yuklab olingan fayl odatda “Yuklanmalar” papkasiga tushadi."),
            Q("Internet orqali qaysi ishni qilish mumkin?", "Video darsni ko‘rish", ["Olma yeyish", "Uxlash", "Suv ichish"],
              x="Internetda darsliklar, video darslar va ensiklopediyalar bor."),
            TF("Internet orqali boshqa shahardagi do‘st bilan gaplashish mumkin.", True, x="Video qo‘ng‘iroq va xabarlar internet orqali ishlaydi."),
            TF("Brauzer — rasm chizish dasturi.", False, x="Brauzer saytlarni ko‘rsatadi, rasm chizadigan dastur esa Paint."),
            ORDER(S, "Brauzer saytlarni ochib ko‘rsatadi"),
            Q("Olma navlari haqida ma’lumot topish uchun qaysi so‘rov eng mos?", "olma navlari", ["menga nimadir kerak", "salom", "internet"], d=2,
              x="Qisqa va aniq kalit so‘zlar yaxshi natija beradi."),
            Q("Telefondagi Wi-Fi belgisi nimani bildiradi?", "Simsiz internet aloqasi", ["Batareya quvvati", "Soat", "Ovoz balandligi"], d=2,
              x="Wi-Fi — simsiz tarmoq aloqasi."),
            Q("Internetdan topilgan ma’lumotni qanday tekshiramiz?", "Bir nechta manbada solishtiramiz", ["Birinchi saytga ishonamiz", "Hech tekshirmaymiz", "Faqat rasmiga qaraymiz"], d=2,
              x="Bir nechta ishonchli manbada bir xil bo‘lsa, ma’lumot to‘g‘ri bo‘lishi ehtimoli katta."),
            Q("Brauzerda sahifani yangilash uchun qaysi tugma bosiladi?", "F5", ["F2", "Esc", "Delete"], d=2,
              x="F5 sahifani qayta yuklaydi."),
            Q("Qaysi biri brauzer emas?", "Paint", ["Google Chrome", "Mozilla Firefox", "Microsoft Edge"], d=2,
              x="Paint — rasm muharriri."),
            TF("Bitta brauzerda bir nechta sahifani alohida varaqlarda ochish mumkin.", True, d=2, x="Har bir sahifa alohida varaq (tab) da ochiladi."),
            MATCH("So‘zni ma’nosi bilan juftlang",
                  [("Internet", "dunyo kompyuterlari tarmog‘i"), ("Brauzer", "saytlarni ochuvchi dastur"), ("Sayt", "veb-sahifalar to‘plami"),
                   ("Havola", "boshqa sahifaga o‘tkazadi"), ("Qidiruv tizimi", "ma’lumot topadi"), ("Wi-Fi", "simsiz ulanish")], d=2,
                  x="Internetga oid asosiy so‘zlar."),
            Q("Qidiruv natijalari ro‘yxatidagi ko‘k sarlavhalar nima?", "Saytlarga havolalar", ["Fayl nomlari", "Parollar", "Rasm asboblari"], d=3,
              x="Sarlavha bosilsa, o‘sha sayt ochiladi."),
            Q("Uyda internetni Wi-Fi orqali tarqatadigan qurilma qaysi?", "Router", ["Skaner", "Proyektor", "Printer"], d=3,
              x="Router internet aloqasini uydagi qurilmalarga simsiz tarqatadi."),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["fayllar", "taqdimot", "internet"], chapter=C3)

# ============================================================ 4-chorak
T.topic("xavfsizlik", "🔒", L("Internetda xavfsizlik va odob", "Online safety and manners", "Безопасность и этикет в интернете"),
        chapter=C4,
        theory="Internetda o‘zingizni va kompyuterni himoya qiling.\n"
               "• Parol — sir. Yaxshi parol uzun bo‘ladi, unda harf va raqamlar aralash keladi. Parolni hech kimga aytmang (ota-onangizdan tashqari).\n"
               "• Shaxsiy ma’lumot — ism-familiya, manzil, telefon raqami, maktab, rasm. Uni notanishlarga bermang.\n"
               "• Notanish havola va fayllarni ochmang — ularda virus bo‘lishi mumkin. Antivirus kompyuterni viruslardan himoya qiladi.\n"
               "• Internetda ham odobli bo‘ling: haqorat qilmang, boshqalarning rasmini ruxsatsiz tarqatmang. Muammo bo‘lsa — kattalarga ayting.",
        items=[
            Q("Qaysi parol yaxshiroq?", "Olma7Daryo2", ["1111", "abc", "parol"], e="🔑",
              x="Uzun, harf va raqamlar aralashgan parolni topish qiyin."),
            Q("Do‘stingiz o‘yindagi parolingizni so‘radi. Nima qilasiz?", "Aytmayman", ["Aytaman", "Qog‘ozga yozib beraman", "Hammaga e’lon qilaman"],
              x="Parolni eng yaqin do‘stga ham aytmaymiz."),
            Q("Kompyuterga zarar yetkazadigan dastur nima deyiladi?", "Virus", ["Brauzer", "Paint", "Kalkulyator"],
              x="Virus fayllarni buzishi yoki ma’lumotni o‘g‘irlashi mumkin."),
            Q("Kompyuterni viruslardan himoya qiluvchi dastur qaysi?", "Antivirus", ["Bloknot", "Paint", "PowerPoint"],
              x="Antivirus viruslarni topib, yo‘q qiladi."),
            Q("Pochtaga notanish odamdan fayl keldi. Nima qilasiz?", "Ochmayman, kattalarga aytaman", ["Darhol ochaman", "Do‘stlarimga yuboraman", "Parolimni yozaman"],
              x="Notanish faylda virus bo‘lishi mumkin."),
            Q("Ekran oldida juda uzoq o‘tirish nimaga zarar?", "Ko‘z va qomatga", ["Tirnoqqa", "Kiyimga", "Sochga"],
              x="Ko‘z charchaydi, uzoq o‘tirishdan qomat buziladi."),
            Q("Yaxshi parolda nimalar bo‘ladi?", "Harf va raqamlar aralash", ["Faqat bitta harf", "Faqat ismingiz", "Faqat 1234"],
              x="Aralash belgilar parolni mustahkam qiladi."),
            Q("Internetdagi notanish odam uchrashishni taklif qildi. Nima qilasiz?", "Rad etib, kattalarga aytaman", ["Yolg‘iz boraman", "Manzilimni beraman", "Hech kimga aytmayman"],
              x="Internetdagi odam o‘zini boshqacha ko‘rsatishi mumkin."),
            TF("Antivirus viruslarni topib yo‘q qiladi.", True, x="Antivirusni muntazam yangilab turish kerak."),
            TF("Notanish odamga telefon raqamingizni yozish mumkin.", False, x="Telefon raqami — shaxsiy ma’lumot."),
            ORDER(S, "Shaxsiy ma’lumotni notanishlarga bermang"),
            Q("Qaysi biri shaxsiy ma’lumot emas?", "Sevimli ertak nomi", ["Uy manzili", "Telefon raqami", "Parol"], d=2,
              x="Uy manzili, telefon va parol — maxfiy shaxsiy ma’lumot."),
            Q("Onlayn o‘yinda bir o‘yinchi sizni masxara qilyapti. To‘g‘ri harakat qaysi?", "Kattalarga aytib, javob bermaslik", ["Uni ham haqorat qilish", "Parolni berish", "Uchrashuvga borish"], d=2,
              x="Qo‘pollikka qo‘pollik bilan javob bermaymiz, kattalar yordam beradi."),
            Q("Qaysi xabar aldov bo‘lishi mumkin?", "“Telefon yutdingiz, parolni yozing”", ["“Ertaga dars soat 8 da”", "“Tug‘ilgan kuning muborak”", "“Kitobni olib kel”"], d=2,
              x="Parol va pul so‘raydigan “yutuq” xabarlari — aldov."),
            Q("Sinfdoshingizning rasmini internetga qo‘yishdan oldin nima qilish kerak?", "Undan ruxsat so‘rash", ["Hech narsa", "Rasmni buzib qo‘yish", "Yashirincha qo‘yish"], d=2,
              x="Boshqa odamning rasmi — uning shaxsiy ma’lumoti."),
            Q("Umumiy kompyuterdan ketayotganda nima qilish kerak?", "Profildan chiqish", ["Parolni ekranga yozish", "Hammasini ochiq qoldirish", "Parolni stolga yozib qo‘yish"], d=2,
              x="Aks holda keyingi odam sizning sahifangizga kirishi mumkin."),
            TF("Parolni vaqti-vaqti bilan almashtirish foydali.", True, d=2, x="Yangi parol eski parol tarqalib ketgan bo‘lsa ham himoya qiladi."),
            TF("Internetdan har qanday o‘yinni so‘ramasdan yuklab olish xavfsiz.", False, d=2, x="Ruxsatsiz yuklangan o‘yinda virus bo‘lishi mumkin."),
            MATCH("Vaziyatni to‘g‘ri harakat bilan juftlang",
                  [("Kompyuterda reklama ko‘payib ketdi", "antivirus bilan tekshirish"), ("Ekran oldida 1 soat o‘tirdim", "ko‘zga dam berish"),
                   ("Notanish uchrashuvga chaqirdi", "rad etib, kattalarga aytish"), ("Do‘stning rasmi", "ruxsatsiz tarqatmaslik"),
                   ("Umumiy kompyuterda ish tugadi", "profildan chiqish")], d=2,
                  x="Xavfsizlik qoidalari bizni himoya qiladi."),
            Q("Kompyuter virus yuqtirganining belgisi qaysi bo‘lishi mumkin?", "Kutilmagan reklama va sekinlashish", ["Klaviatura toza", "Monitor yorqin", "Sichqoncha yangi"], d=3,
              x="Virus kompyuterni sekinlashtiradi va keraksiz oynalar ochadi."),
        ])

# --- Robot katakli maydonda: natijalar Python'da hisoblanadi.
MOVE = {"o‘ngga": (1, 0), "chapga": (-1, 0), "yuqoriga": (0, 1), "pastga": (0, -1)}
OPP = {"o‘ngga": "chapga", "chapga": "o‘ngga", "yuqoriga": "pastga", "pastga": "yuqoriga"}


def run(start, cmds):
    c, r = start
    for m in cmds:
        c, r = c + MOVE[m][0], r + MOVE[m][1]
    return c, r


def cell(p):
    return f"{p[0]}-ustun, {p[1]}-qator"


_rob = []
for start, cmds, d in [((2, 1), ["yuqoriga", "yuqoriga", "o‘ngga"], 1), ((3, 3), ["chapga", "pastga", "chapga"], 2),
                       ((1, 4), ["pastga", "pastga", "o‘ngga", "o‘ngga", "o‘ngga"], 2), ((4, 2), ["yuqoriga", "chapga", "yuqoriga", "chapga", "pastga"], 3),
                       ((2, 2), ["o‘ngga", "yuqoriga", "chapga", "pastga"], 2)]:
    end = run(start, cmds)
    flipped = run(start, [{"yuqoriga": "pastga", "pastga": "yuqoriga"}.get(m, m) for m in cmds])
    cands = [(end[1], end[0]), flipped, run(start, cmds[:-1]), (end[0] + 1, end[1]), (end[0], end[1] + 1), (end[0] - 1, end[1]), (end[0], end[1] - 1)]
    wrong = uniq(cell(end), [cell(p) for p in cands if p[0] >= 1 and p[1] >= 1])
    _rob.append(Q(f"Robot {cell(start)}da turibdi. Buyruqlar: {', '.join(cmds)}. Robot qayerga keladi?", cell(end), wrong, d=d,
                  x=f"Har bir buyruq bir katak suradi: {cell(start)} → {cell(end)}."))
for start, cmds, d in [((1, 1), ["o‘ngga", "yuqoriga"], 2), ((2, 3), ["yuqoriga", "yuqoriga", "chapga"], 3), ((3, 1), ["o‘ngga", "o‘ngga", "yuqoriga"], 3)]:
    back = [OPP[m] for m in reversed(cmds)]
    opts = [cmds, [OPP[m] for m in cmds[:-1]], back[:-1] + [back[-1], back[-1]], [OPP[cmds[0]]] * len(cmds)]
    wrong = []
    for o in opts:
        if run(run(start, cmds), o) != start and ", ".join(o) not in wrong:
            wrong.append(", ".join(o))
    assert run(run(start, cmds), back) == start
    _rob.append(Q(f"Robot {cell(start)}dan “{', '.join(cmds)}” buyruqlarini bajardi. Qaysi buyruqlar uni boshlang‘ich katakka qaytaradi?",
                  ", ".join(back), wrong[:4], d=d, x=f"Teskari tartibda teskari yo‘nalishda yuramiz: {', '.join(back)}."))
for a, b, d in [((1, 1), (4, 3), 2), ((5, 4), (1, 1), 3)]:
    n = abs(a[0] - b[0]) + abs(a[1] - b[1])
    _rob.append(Q(f"Robot {cell(a)}dan {cell(b)}ga borishi uchun kamida nechta buyruq kerak?", n,
                  near(n, [abs(a[0] - b[0]), abs(a[1] - b[1]), n + 1, n - 1, n + 2], lo=1), d=d,
                  x=f"Ustun bo‘yicha {abs(a[0] - b[0])} ta, qator bo‘yicha {abs(a[1] - b[1])} ta qadam: jami {n}."))

T.topic("algoritm", "🤖", L("Algoritm va Robot ijrochi", "Algorithms and the Robot", "Алгоритм и исполнитель Робот"),
        chapter=C4,
        theory="Algoritm — maqsadga olib boradigan aniq buyruqlar ketma-ketligi. Buyruqlarni bajaruvchi — ijrochi.\n"
               "Robot ijrochi katakli maydonda yuradi. Buyruqlari: yuqoriga, pastga, chapga, o‘ngga — har biri 1 katak suradi.\n"
               "Katak joyi ustun va qator raqami bilan aytiladi: ustunlar chapdan o‘ngga, qatorlar pastdan yuqoriga raqamlangan.\n"
               "• “o‘ngga” — ustun raqami 1 ga oshadi, “chapga” — 1 ga kamayadi; “yuqoriga” — qator raqami 1 ga oshadi, “pastga” — kamayadi.\n"
               "Misol: Robot 1-ustun, 1-qatorda. “o‘ngga, o‘ngga, yuqoriga” → 3-ustun, 2-qator.",
        items=[
            Q("Algoritm nima?", "Aniq buyruqlar ketma-ketligi", ["Kompyuter qismi", "Rasm turi", "Fayl nomi"],
              x="Algoritm ijrochini maqsadga olib boradi."),
            Q("Buyruqlarni bajaruvchi nima deyiladi?", "Ijrochi", ["Algoritm", "Dastur nomi", "Kursor"],
              x="Ijrochi — odam, robot yoki kompyuter."),
            Q("Robotning qaysi buyrug‘i qator raqamini oshiradi?", "yuqoriga", ["pastga", "chapga", "o‘ngga"],
              x="Qatorlar pastdan yuqoriga raqamlangan."),
            Q("Robotning qaysi buyrug‘i ustun raqamini kamaytiradi?", "chapga", ["o‘ngga", "yuqoriga", "pastga"],
              x="Ustunlar chapdan o‘ngga raqamlangan."),
            Q("Qaysi biri algoritmga misol?", "Choy damlash tartibi", ["Qizil rang", "Baland daraxt", "Shirin olma"],
              x="Choy damlash — ketma-ket bajariladigan qadamlar."),
            Q("“o‘ngga” buyrug‘idan keyin “chapga” bajarilsa, Robot qayerda bo‘ladi?", "Avvalgi katagida", ["2 katak o‘ngda", "1 katak yuqorida", "Maydondan tashqarida"],
              x="Qarama-qarshi buyruqlar bir-birini yo‘qqa chiqaradi."),
            TF("Algoritmda buyruqlar tartibi muhim.", True, x="Tartib o‘zgarsa, natija ham o‘zgarishi mumkin."),
            TF("Robot o‘zi bilmagan buyruqni ham bajaradi.", False, x="Ijrochi faqat o‘z buyruqlar tizimidagi buyruqlarni bajaradi."),
            ORDER(S, "Robot buyruqlarni birin-ketin bajaradi"),
            Q("Robot “uch qadam tashla” buyrug‘ini bajarmadi. Nima uchun?", "Bu buyruq uning ro‘yxatida yo‘q", ["Robot charchadi", "Buyruq juda qisqa", "Maydon katta"], d=2,
              x="Robot faqat yuqoriga, pastga, chapga, o‘ngga buyruqlarini biladi."),
            MATCH("Buyruqni natija bilan juftlang",
                  [("o‘ngga", "ustun 1 ga oshadi"), ("chapga", "ustun 1 ga kamayadi"), ("yuqoriga", "qator 1 ga oshadi"), ("pastga", "qator 1 ga kamayadi"),
                   ("o‘ngga, chapga", "joyida qoladi")], d=2,
                  x="Har bir buyruq Robotni bir katakka suradi."),
            Q("Robot maydonning eng o‘ng ustunida. “o‘ngga” buyrug‘i berilsa nima bo‘ladi?", "Bajara olmaydi, devor bor", ["Chapga yuradi", "Yuqoriga yuradi", "Maydon kengayadi"], d=3,
              x="Maydon chegarasidan chiqib bo‘lmaydi — Robot xato haqida xabar beradi."),
        ] + _rob)

_loop = []
for start, times, body, d in [((1, 1), 3, ["o‘ngga"], 1), ((1, 1), 2, ["o‘ngga", "yuqoriga"], 2), ((2, 5), 3, ["pastga"], 1),
                              ((1, 2), 3, ["o‘ngga", "o‘ngga", "yuqoriga"], 3), ((5, 1), 2, ["chapga", "yuqoriga", "yuqoriga"], 3)]:
    end = run(start, body * times)
    cands = [run(start, body), run(start, body * (times - 1)), run(start, body * (times + 1)), (end[1], end[0]), (end[0] + 1, end[1]), (end[0], end[1] - 1)]
    wrong = uniq(cell(end), [cell(p) for p in cands if p[0] >= 1 and p[1] >= 1])
    _loop.append(Q(f"Robot {cell(start)}da. Algoritm: “takrorla {times} marta: {', '.join(body)}”. Robot qayerga keladi?", cell(end), wrong, d=d,
                   x=f"“{', '.join(body)}” {times} marta bajariladi: {cell(start)} → {cell(end)}."))
for times, body, d in [(4, ["o‘ngga"], 1), (3, ["o‘ngga", "yuqoriga"], 2), (5, ["qarsak chal", "sakra"], 2), (6, ["chapga", "chapga", "pastga"], 3)]:
    n = times * len(body)
    _loop.append(Q(f"“takrorla {times} marta: {', '.join(body)}” algoritmida jami nechta buyruq bajariladi?", n,
                   near(n, [times, len(body), times + len(body), n + times, n - 1], lo=1), d=d,
                   x=f"{times} · {len(body)} = {n} ta buyruq."))
for seq, times, body, d in [(["o‘ngga"] * 5, 5, ["o‘ngga"], 1), (["o‘ngga", "yuqoriga"] * 3, 3, ["o‘ngga", "yuqoriga"], 2),
                            (["pastga", "pastga", "chapga"] * 2, 2, ["pastga", "pastga", "chapga"], 3)]:
    assert body * times == seq
    ans = f"takrorla {times} marta: {', '.join(body)}"
    wrong = [f"takrorla {times + 1} marta: {', '.join(body)}", f"takrorla {len(seq)} marta: {', '.join(body)}",
             f"takrorla {times} marta: {', '.join(OPP[b] for b in body)}", f"takrorla {times - 1} marta: {', '.join(body)}"]
    _loop.append(Q(f"“{', '.join(seq)}” buyruqlarini sikl bilan qanday qisqa yozish mumkin?", ans, uniq(ans, wrong), d=d,
                   x=f"“{', '.join(body)}” guruhi {times} marta takrorlangan."))
for outer, inner, d in [(2, 3, 3), (3, 4, 3)]:
    n = outer * inner
    _loop.append(Q(f"Tashqi sikl {outer} marta takrorlanadi, uning ichidagi sikl esa {inner} marta “qarsak chal” buyrug‘ini bajaradi. Jami necha marta qarsak chalinadi?", n,
                   near(n, [outer + inner, inner, outer, n + 1], lo=1), d=d, x=f"{outer} · {inner} = {n}."))

T.topic("sikl", "🔁", L("Takrorlash (sikl)", "Loops", "Циклы"),
        chapter=C4,
        theory="Sikl (takrorlash) — bir xil buyruqlarni bir necha marta bajarish.\n"
               "Yozilishi: “takrorla 4 marta: o‘ngga” — bu “o‘ngga, o‘ngga, o‘ngga, o‘ngga” bilan bir xil, lekin qisqa.\n"
               "Sikl ichida bir nechta buyruq bo‘lishi mumkin: “takrorla 3 marta: o‘ngga, yuqoriga” — 6 ta buyruq bajariladi.\n"
               "• Bajarilgan buyruqlar soni = takrorlar soni · sikl ichidagi buyruqlar soni.\n"
               "Kundalik hayotda ham sikl bor: har kuni tish yuvish, zinadan qadam-baqadam chiqish.",
        items=[
            Q("Bir xil buyruqlarni bir necha marta bajarish nima deyiladi?", "Sikl (takrorlash)", ["Tarmoqlanish", "Saqlash", "O‘chirish"],
              x="Sikl algoritmni qisqa va tushunarli qiladi."),
            Q("Sikl nima uchun qulay?", "Algoritm qisqa yoziladi", ["Kompyuter o‘chadi", "Buyruqlar yo‘qoladi", "Robot to‘xtaydi"],
              x="Bir xil buyruqni 10 marta yozish o‘rniga “takrorla 10 marta” deymiz."),
            TF("“takrorla 3 marta: o‘ngga” va “o‘ngga, o‘ngga, o‘ngga” bir xil natija beradi.", True, x="Ikkalasida ham Robot 3 katak o‘ngga yuradi."),
            TF("Sikl ichida faqat bitta buyruq bo‘lishi mumkin.", False, x="Sikl ichida bir nechta buyruq bo‘lishi mumkin."),
            ORDER(S, "Sikl buyruqlarni bir necha marta takrorlaydi"),
            Q("Qaysi ish siklga misol?", "Har kuni ertalab badantarbiya qilish", ["Bir marta tug‘ilish", "Bitta olmani yeyish", "Eshikni bir marta ochish"], d=2,
              x="Har kuni takrorlanadigan ish — sikl."),
            MATCH("Siklni natijasi bilan juftlang",
                  [("takrorla 2 marta: o‘ngga", "2 katak o‘ngga"), ("takrorla 3 marta: yuqoriga", "3 katak yuqoriga"), ("takrorla 4 marta: chapga", "4 katak chapga"),
                   ("takrorla 5 marta: pastga", "5 katak pastga"), ("takrorla 2 marta: o‘ngga, chapga", "joyida qoladi")], d=2,
                  x="Takrorlar soni Robot necha katak yurishini ko‘rsatadi."),
        ] + _loop)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["xavfsizlik", "algoritm", "sikl"], chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["qurilmalar", "axborot_turlari", "tez_terish", "matn_tahrir", "matn_bezash", "rasm_muharriri",
        "fayllar", "taqdimot", "internet", "xavfsizlik", "algoritm", "sikl"], chapter=C4, level=3)

T.write()
