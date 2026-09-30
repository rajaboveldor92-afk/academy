"""Tabiiy fanlar, 6-sinf: assets/data/school/science_g6.json + bank_science_g6.json.

Mavzular O‘zbekiston maktab dasturi ("Tabiiy fanlar", 6-sinf) yo‘nalishida: mexanik harakat va tezlik, massa va zichlik,
bosim, issiqlik uzatish, yorug‘lik, tovush, atom va molekula, oddiy va murakkab moddalar, tirik organizmlar tasnifi,
o‘simlik a’zolari va to‘qimalari, hayvonlar tuzilishi, yer po‘sti harakatlari, ob-havo va iqlim, xarita va koordinatalar,
tabiiy resurslar va ekologiya. Hamma matn o‘zimizniki (darslikdan ko‘chirilmagan).
Barcha sonli javoblar (tezlik, zichlik, bosim, masshtab, harorat va h.k.) Python’da hisoblanadi.
Qayta yaratish: python3 tool/content/school/science_g6.py
"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("science", 6, L("Tabiiy fanlar", "Natural sciences", "Естественные науки"))

C1 = "1-chorak. Harakat, massa va bosim"
C2 = "2-chorak. Yorug‘lik, tovush va moddalar"
C3 = "3-chorak. Tirik organizmlar"
C4 = "4-chorak. Yer, iqlim va ekologiya"

S = "So‘zlardan gap tuzing"


def near(ans, cands, k=4, lo=0):
    """Sonli javob uchun noto'g'ri variantlar: takrorsiz, javobdan farqli, `lo` dan kichik emas."""
    out = []
    for c in cands:
        if c != ans and c >= lo and c not in out:
            out.append(c)
    return out[:k]


def num(x):
    """Son → matn: butun bo'lsa butun, aks holda vergulli o'nli kasr (7.8 → "7,8")."""
    x = Fraction(x)
    if x.denominator == 1:
        n = int(x)
        return f"{n:,}".replace(",", " ") if abs(n) >= 10000 else str(n)
    s = f"{float(x):.3f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def unit_opts(ans, cands, unit, lo=0):
    """Javob va noto'g'ri variantlarni birlik bilan matnga aylantiradi."""
    return f"{num(ans)} {unit}", [f"{num(c)} {unit}" for c in near(ans, cands, lo=lo)]


def temp(t):
    return f"{t} °C".replace("-", "−")


def temp_say(t):
    return f"minus {-t} °C" if t < 0 else f"{t} °C"


# ============================================================ 1-chorak
_mot = []
for s, t, d in [(120, 2, 1), (150, 3, 1), (270, 3, 2), (360, 4, 2)]:
    v = Fraction(s, t)
    assert v.denominator == 1
    a, w = unit_opts(v, [s * t, v + 10, v - 10, s - t, v * 2], "km/soat", lo=1)
    _mot.append(Q(f"Avtomobil {s} km yo‘lni {t} soatda bosib o‘tdi. Uning o‘rtacha tezligi qancha?", a, w, d=d,
                  x=f"v = s : t = {s} : {t} = {num(v)} km/soat."))
for v, t, d in [(60, 3, 1), (80, 2, 2), (15, 4, 2)]:
    s = v * t
    a, w = unit_opts(s, [v + t, s + v, s - v, v * (t + 1)], "km", lo=1)
    _mot.append(Q(f"Jism {v} km/soat tezlik bilan {t} soat harakatlandi. U qancha yo‘l bosdi?", a, w, d=d,
                  x=f"s = v · t = {v} · {t} = {s} km."))
for v, t, d in [(5, 20, 2), (12, 15, 3)]:
    s = v * t
    a, w = unit_opts(s, [v + t, s + v, s - v, s * 2], "m", lo=1)
    _mot.append(Q(f"Velosipedchi {v} m/s tezlik bilan {t} soniya yurdi. U necha metr yo‘l bosdi?", a, w, d=d,
                  x=f"s = v · t = {v} · {t} = {s} m."))
for s, v, unit, d in [(300, 60, "soat", 2), (180, 45, "soat", 2), (400, 8, "soniya", 3)]:
    t = Fraction(s, v)
    assert t.denominator == 1
    a, w = unit_opts(t, [t + 1, t - 1, t * 2, s - v], unit, lo=1)
    su, vu = ("km", "km/soat") if unit == "soat" else ("m", "m/s")
    _mot.append(Q(f"{s} {su} yo‘lni {v} {vu} tezlik bilan necha {unit}da bosib o‘tish mumkin?", a, w, d=d,
                  x=f"t = s : v = {s} : {v} = {num(t)} {unit}."))
for kmh, d in [(36, 2), (72, 3), (54, 3)]:
    ms = Fraction(kmh * 1000, 3600)
    assert ms.denominator == 1
    a, w = unit_opts(ms, [ms + 5, ms - 5, ms * 2, kmh], "m/s", lo=1)
    _mot.append(Q(f"{kmh} km/soat necha m/s ga teng?", a, w, d=d, say=f"{kmh} kilometr soatiga necha metr sekundga teng?",
                  x=f"1 km = 1000 m, 1 soat = 3600 s: {kmh} · 1000 : 3600 = {num(ms)} m/s."))
_ms, _kmh = 20, 54
assert Fraction(_kmh * 1000, 3600) == 15 < _ms
_mot.append(Q(f"Qaysi tezlik katta: {_ms} m/s yoki {_kmh} km/soat?", f"{_ms} m/s", [f"{_kmh} km/soat", "Ikkalasi teng", "Taqqoslab bo‘lmaydi"], d=3,
              x=f"{_kmh} km/soat = {_kmh} · 1000 : 3600 = 15 m/s, bu {_ms} m/s dan kichik."))

T.topic("motion", "🚗", L("Mexanik harakat va tezlik", "Motion and speed", "Механическое движение и скорость"),
        chapter=C1,
        theory="Mexanik harakat — jism vaziyatining boshqa jismlarga nisbatan vaqt o‘tishi bilan o‘zgarishi. Jism qoldirgan chiziq — trayektoriya, uning uzunligi — yo‘l (s).\n"
               "Tezlik — jismning vaqt birligida bosib o‘tgan yo‘li: v = s : t. Bundan s = v · t va t = s : v.\n"
               "• Birliklar: yo‘l — m, km; vaqt — s, soat; tezlik — m/s, km/soat. 1 km = 1000 m, 1 soat = 3600 s, shuning uchun 36 km/soat = 10 m/s.\n"
               "• Teng vaqtlarda teng yo‘l bosilsa — tekis harakat. Tezlikni spidometr ko‘rsatadi.\n"
               "Misol: 120 km ni 2 soatda o‘tgan avtobus tezligi 120 : 2 = 60 km/soat.",
        items=[
            Q("Tezlik qaysi formula bilan topiladi?", "v = s : t", ["v = s · t", "v = t : s", "v = s + t"],
              x="Tezlik — yo‘lning vaqtga nisbati."),
            Q("Jism harakatlanganda qoldirgan chiziq nima deyiladi?", "Trayektoriya", ["Tezlik", "Massa", "Bosim"],
              x="Masalan, samolyotning osmondagi oq izi — uning trayektoriyasi."),
            Q("Avtomobil tezligini qaysi asbob ko‘rsatadi?", "Spidometr", ["Termometr", "Barometr", "Dinamometr"],
              x="Spidometr haydovchiga tezlikni km/soat da ko‘rsatadi."),
            Q("Xalqaro birliklar tizimida tezlik birligi qaysi?", "m/s", ["kg", "N", "Pa"],
              x="Tezlik metr sekundda (m/s) o‘lchanadi."),
            Q("1 soatda necha soniya bor?", "3600", ["60", "360", "1000"],
              x="1 soat = 60 daqiqa = 60 · 60 = 3600 soniya."),
            TF("Poyezdda o‘tirgan yo‘lovchi vagonga nisbatan tinch turibdi.", True,
               x="Harakat nisbiy: yo‘lovchi vagonga nisbatan tinch, yerga nisbatan esa harakatda."),
            TF("Tekis harakatda jism teng vaqtlarda turli yo‘l bosadi.", False,
               x="Tekis harakatda teng vaqtlarda teng yo‘l bosiladi."),
            ORDER(S, "Tezlik yo‘lning vaqtga nisbati"),
            Q("Qaysi harakat egri chiziqli?", "Karusel o‘rindig‘ining aylanishi", ["Liftning ko‘tarilishi", "Tushayotgan tosh", "Tekis yo‘ldagi poyezd"], d=2,
              x="Karusel o‘rindig‘i aylana bo‘ylab harakatlanadi."),
            Q("Eng tez yuguradigan quruqlik hayvoni qaysi?", "Gepard", ["Sher", "Ot", "Quyon"], d=2,
              x="Gepard qisqa masofada taxminan 100 km/soat tezlikka erishadi."),
            MATCH("Kattalikni formulasi bilan juftlang",
                  [("Tezlik", "v = s : t"), ("Yo‘l", "s = v · t"), ("Vaqt", "t = s : v"), ("Zichlik", "ρ = m : V"), ("Bosim", "p = F : S")], d=2,
                  x="Formulalarni harf ma’nosi bilan birga eslab qoling."),
        ] + _mot)

# --- Zichlik: g/sm³ da, Python'da hisoblanadi.
_den = []
for m, V, what, d in [(780, 100, "temir", 2), (270, 100, "alyuminiy", 2), (1930, 100, "oltin", 3), (90, 100, "muz", 2)]:
    rho = Fraction(m, V)
    a, w = unit_opts(rho, [Fraction(m, V * 10), rho + 1, rho * 10, rho * 2], "g/sm³")
    _den.append(Q(f"Hajmi {V} sm³ bo‘lgan {what} bo‘lagining massasi {m} g. Uning zichligi qancha?", a, w, d=d,
                  x=f"ρ = m : V = {m} : {V} = {num(rho)} g/sm³."))
for rho, V, what, d in [(1, 250, "suv", 1), (Fraction(9, 10), 200, "muz", 3), (Fraction(27, 10), 10, "alyuminiy", 3)]:
    m = rho * V
    assert m.denominator == 1
    a, w = unit_opts(m, [V, m + 10, m * 10, m - 10], "g", lo=1)
    _den.append(Q(f"{what.capitalize()}ning zichligi {num(rho)} g/sm³. Hajmi {V} sm³ bo‘lgan {what}ning massasi qancha?", a, w, d=d,
                  x=f"m = ρ · V = {num(rho)} · {V} = {num(m)} g."))
for m, d in [(500, 2), (1500, 2)]:
    V = m  # suv: 1 g/sm³
    a, w = unit_opts(V, [m // 10, m * 10, m + 100, m - 100], "sm³", lo=1)
    _den.append(Q(f"Massasi {m} g bo‘lgan suv qancha hajmni egallaydi? Suvning zichligi 1 g/sm³.", a, w, d=d,
                  x=f"V = m : ρ = {m} : 1 = {V} sm³."))
for t, d in [(3, 1), (5, 2)]:
    kg = t * 1000
    _den.append(Q(f"{t} t necha kilogramm?", f"{kg} kg", [f"{t * 100} kg", f"{t * 10} kg", f"{kg * 10} kg"], d=d,
                  x=f"1 t = 1000 kg, shuning uchun {t} t = {kg} kg."))

T.topic("density", "⚖️", L("Massa va zichlik", "Mass and density", "Масса и плотность"),
        chapter=C1,
        theory="Massa (m) tarozida o‘lchanadi, birligi — kilogramm: 1 t = 1000 kg, 1 kg = 1000 g.\n"
               "Zichlik (ρ) — birlik hajmdagi massa: ρ = m : V. Birliklari: g/sm³ yoki kg/m³.\n"
               "• Suv — 1 g/sm³ (1000 kg/m³), muz — 0,9 g/sm³, alyuminiy — 2,7 g/sm³, temir — 7,8 g/sm³, oltin — 19,3 g/sm³.\n"
               "• Zichligi suvnikidan kichik jism suvda suzadi (muz, yog‘och, yog‘), kattasi cho‘kadi (temir, tosh).\n"
               "Misol: 100 sm³ temirning massasi 780 g, demak ρ = 780 : 100 = 7,8 g/sm³.",
        items=[
            Q("Massa qaysi asbob bilan o‘lchanadi?", "Tarozi", ["Menzurka", "Spidometr", "Barometr"],
              x="Tarozida jismning massasi o‘lchanadi."),
            Q("Zichlik qaysi formula bilan topiladi?", "ρ = m : V", ["ρ = m · V", "ρ = V : m", "ρ = m + V"],
              x="Zichlik — massaning hajmga nisbati."),
            Q("Toza suvning zichligi qancha?", "1 g/sm³", ["10 g/sm³", "0,1 g/sm³", "7,8 g/sm³"],
              x="1 sm³ suvning massasi 1 g."),
            Q("Qaysi jism suvda cho‘kadi?", "Temir mix", ["Muz bo‘lagi", "Yog‘och cho‘p", "Po‘kak"],
              x="Temirning zichligi suvnikidan katta."),
            Q("Muz nima uchun suvda suzadi?", "Zichligi suvnikidan kichik", ["Zichligi suvnikidan katta", "U juda sovuq", "Unda havo yo‘q"],
              x="Muzning zichligi 0,9 g/sm³, suvniki 1 g/sm³."),
            TF("1 litr suvning massasi taxminan 1 kg.", True, x="1 l = 1000 sm³, suv esa 1 g/sm³: 1000 g = 1 kg."),
            TF("Bir xil hajmdagi temir va yog‘ochning massasi teng.", False, x="Temirning zichligi katta, shuning uchun uning massasi ham katta."),
            ORDER(S, "Zichligi kichik jism suvda suzadi"),
            Q("Qaysi metallning zichligi eng katta?", "Oltin", ["Alyuminiy", "Temir", "Mis"], d=2,
              x="Oltin — 19,3 g/sm³, temir — 7,8, alyuminiy — 2,7."),
            Q("Suv yuzasida yog‘ nima uchun suzib yuradi?", "Yog‘ suvdan yengilroq", ["Yog‘ suvdan og‘irroq", "Yog‘ suvda eriydi", "Yog‘ qaynayotgan bo‘ladi"], d=2,
              x="O‘simlik yog‘ining zichligi suvnikidan kichik."),
            MATCH("Moddani zichligi bilan juftlang",
                  [("Suv", "1 g/sm³"), ("Muz", "0,9 g/sm³"), ("Alyuminiy", "2,7 g/sm³"), ("Temir", "7,8 g/sm³"), ("Oltin", "19,3 g/sm³")], d=3,
                  x="Zichlik jadvali moddani aniqlashga yordam beradi."),
        ] + _den)

# --- Bosim: p = F : S (Python'da hisoblanadi).
_prs = []
for F, S_, d in [(600, 3, 1), (900, 3, 2), (1000, Fraction(1, 2), 2), (450, Fraction(3, 20), 3)]:
    p = Fraction(F) / Fraction(S_)
    assert p.denominator == 1
    a, w = unit_opts(p, [F * Fraction(S_), p * 10, Fraction(p, 10), p + 100], "Pa", lo=1)
    _prs.append(Q(f"{F} N kuch {num(S_)} m² yuzaga tik ta’sir qilmoqda. Bosim qancha?", a, w, d=d,
                  x=f"p = F : S = {F} : {num(S_)} = {num(p)} Pa."))
for p, S_, d in [(5000, Fraction(1, 5), 3), (2000, 3, 2)]:
    F = Fraction(p) * Fraction(S_)
    assert F.denominator == 1
    a, w = unit_opts(F, [F * 10, F + 100, p, F // 2, F + 1000], "N", lo=1)
    _prs.append(Q(f"Bosim {p} Pa, yuza {num(S_)} m². Yuzaga qanday kuch ta’sir qilmoqda?", a, w, d=d,
                  x=f"F = p · S = {p} · {num(S_)} = {num(F)} N."))
for kpa, d in [(3, 1), (12, 2)]:
    _prs.append(Q(f"{kpa} kPa necha paskalga teng?", f"{kpa * 1000} Pa", [f"{kpa * 100} Pa", f"{kpa * 10} Pa", f"{kpa * 10000} Pa"], d=d,
                  x=f"1 kPa = 1000 Pa, demak {kpa} kPa = {kpa * 1000} Pa."))

T.topic("pressure", "🎈", L("Bosim", "Pressure", "Давление"),
        chapter=C1,
        theory="Bosim (p) — yuzaga tik ta’sir qilayotgan kuchning shu yuza kattaligiga nisbati: p = F : S. Birligi — paskal (Pa): 1 Pa = 1 N/m², 1 kPa = 1000 Pa.\n"
               "• Yuza kichraysa, bosim ortadi: o‘tkir pichoq, igna. Yuza kattalashsa, bosim kamayadi: chang‘i, traktor zanjiri.\n"
               "• Suyuqlik bosimi chuqurlik ortgan sari ortadi. Gaz va suyuqlik bosimni hamma tomonga bir xil uzatadi.\n"
               "• Atmosfera bosimini barometr o‘lchaydi; normal bosim — 760 mm simob ustuni. Balandlikka chiqqan sari atmosfera bosimi kamayadi.\n"
               "Misol: 600 N kuch 3 m² yuzaga ta’sir qilsa, p = 600 : 3 = 200 Pa.",
        items=[
            Q("Bosim qaysi formula bilan topiladi?", "p = F : S", ["p = F · S", "p = S : F", "p = m : V"],
              x="Bosim — kuchning yuzaga nisbati."),
            Q("Bosim birligi qaysi?", "Paskal", ["Nyuton", "Kilogramm", "Metr"],
              x="Birlik fransuz olimi Blez Paskal sharafiga nomlangan."),
            Q("Atmosfera bosimini qaysi asbob o‘lchaydi?", "Barometr", ["Termometr", "Spidometr", "Tarozi"],
              x="Barometr ob-havoni bashorat qilishda ham ishlatiladi."),
            Q("Pichoqni charxlaganda nima o‘zgaradi?", "Tig‘ yuzasi kichrayib, bosim ortadi", ["Pichoq og‘irlashadi", "Bosim kamayadi", "Kuch yo‘qoladi"],
              x="Yuza kichik bo‘lsa, bir xil kuch katta bosim beradi."),
            Q("Qorda botib ketmaslik uchun nima kiyiladi?", "Chang‘i", ["Tufli", "Konki", "Shippak"],
              x="Chang‘ining yuzasi katta, bosim kichik bo‘ladi."),
            TF("Yuza kattalashsa, bosim kamayadi.", True, x="Bir xil kuch katta yuzaga taqsimlanadi."),
            TF("Tog‘ cho‘qqisida atmosfera bosimi dengiz bo‘yidagidan katta.", False, x="Balandlikka chiqqan sari atmosfera bosimi kamayadi."),
            ORDER(S, "Chuqurlik ortgan sari suv bosimi ortadi"),
            Q("To‘g‘on devori nima uchun pastki qismida qalinroq quriladi?", "Chuqurda suv bosimi katta", ["Pastda suv iliqroq", "Pastda suv kam", "Chiroyli ko‘rinishi uchun"], d=2,
              x="Suyuqlik bosimi chuqurlik bilan ortadi."),
            Q("Puflangan shar nima uchun yumaloq bo‘ladi?", "Gaz bosimni hamma tomonga uzatadi", ["Rezina doim yumaloq", "Shar ichi bo‘sh", "Havo pastga tushadi"], d=2,
              x="Gaz bosimi hamma yo‘nalishda bir xil — bu Paskal qonuni."),
            Q("Traktor va tankka keng zanjir nima uchun kerak?", "Yerga bosimni kamaytirish", ["Tezlikni oshirish", "Og‘irlikni oshirish", "Shovqinni kamaytirish"], d=2,
              x="Keng zanjir og‘irlikni katta yuzaga taqsimlaydi."),
            Q("Normal atmosfera bosimi necha mm simob ustuniga teng?", "760 mm", ["100 mm", "1000 mm", "76 mm"], d=3,
              x="Dengiz sathida havo bosimi 760 mm balandlikdagi simob ustuni bosimiga teng."),
            MATCH("Misolni bosim bilan juftlang",
                  [("O‘tkir igna", "katta bosim"), ("Keng chang‘i", "kichik bosim"), ("Chuqur dengiz tubi", "katta suv bosimi"),
                   ("Baland tog‘ cho‘qqisi", "past atmosfera bosimi"), ("Barometr", "atmosfera bosimini o‘lchaydi")], d=2,
                  x="Bosim kuchga, yuzaga, chuqurlikka va balandlikka bog‘liq."),
        ] + _prs)

T.topic("heat_transfer", "🔥", L("Issiqlik uzatish turlari", "Heat transfer", "Виды теплопередачи"),
        chapter=C1,
        theory="Issiqlik doimo issiqroq jismdan sovuqroq jismga o‘tadi. Uch xil yo‘l bilan uzatiladi:\n"
               "• Issiqlik o‘tkazuvchanlik — jism zarralari orqali: choydagi qoshiq dastasi qiziydi. Metallar yaxshi, havo, jun, yog‘och, penoplast yomon o‘tkazadi.\n"
               "• Konveksiya — suyuqlik va gazlarda isigan qatlamlarning ko‘tarilishi, sovuqlarining tushishi: qozondagi suv, xonadagi batareya.\n"
               "• Nurlanish — bo‘shliq orqali ham o‘tadi: Quyosh issiqligi, gulxan taftini sezish. Qora sirt nurni ko‘proq yutadi, oq va yaltiroq sirt qaytaradi.\n"
               "Termos uchala yo‘lni ham kamaytiradi va issiqni uzoq saqlaydi.",
        items=[
            Q("Issiq choyga solingan metall qoshiq dastasi qiziydi. Bu qaysi issiqlik uzatish turi?", "Issiqlik o‘tkazuvchanlik", ["Konveksiya", "Nurlanish", "Bug‘lanish"],
              x="Issiqlik metall zarralari orqali uzatiladi."),
            Q("Quyosh issiqligi Yerga qaysi yo‘l bilan keladi?", "Nurlanish", ["Konveksiya", "Issiqlik o‘tkazuvchanlik", "Diffuziya"],
              x="Koinotda havo yo‘q, issiqlik faqat nurlanish bilan keladi."),
            Q("Qozondagi suvning pastdan isib, yuqoriga ko‘tarilishi qanday hodisa?", "Konveksiya", ["Nurlanish", "Issiqlik o‘tkazuvchanlik", "Kondensatsiya"],
              x="Isigan suv yengillashib ko‘tariladi, sovug‘i pastga tushadi."),
            Q("Qaysi modda issiqlikni yaxshi o‘tkazadi?", "Mis", ["Jun", "Yog‘och", "Penoplast"],
              x="Metallar issiqlikni yaxshi o‘tkazadi."),
            Q("Qaysi modda issiqlikni yomon o‘tkazadi?", "Jun", ["Temir", "Alyuminiy", "Kumush"],
              x="Jun tolalari orasida havo bor, havo issiqlikni yomon o‘tkazadi."),
            Q("Issiqlik qaysi yo‘nalishda o‘tadi?", "Issiqdan sovuqqa", ["Sovuqdan issiqqa", "Faqat pastdan yuqoriga", "Hech qayerga"],
              x="Issiqlik o‘z-o‘zidan issiqroq jismdan sovuqroq jismga o‘tadi."),
            TF("Nurlanish havosiz bo‘shliqda ham bo‘ladi.", True, x="Quyosh nurlari koinot bo‘shlig‘idan o‘tib keladi."),
            TF("Konveksiya qattiq jismlarda ham bo‘ladi.", False, x="Konveksiya faqat suyuqlik va gazlarda bo‘ladi, qattiq jism zarralari joyidan siljimaydi."),
            TF("Qora kiyim Quyoshda oq kiyimdan ko‘proq qiziydi.", True, x="Qora sirt nurlarni ko‘proq yutadi."),
            ORDER(S, "Issiqlik issiqroq jismdan sovuqroq jismga o‘tadi"),
            Q("Isitish batareyasi nima uchun xonaning pastki qismiga o‘rnatiladi?", "Iliq havo ko‘tarilib, xonani aylanadi", ["Pastda chiroyli turadi", "Sovuq havo ko‘tariladi", "Batareya og‘ir"], d=2,
              x="Iliq havo yuqoriga ko‘tariladi, sovug‘i tushadi — konveksiya xonani isitadi."),
            Q("Konditsioner nima uchun devorning yuqorisiga o‘rnatiladi?", "Sovuq havo pastga tushadi", ["Issiq havo pastda", "U yengil", "Bolalar tegmasin"], d=2,
              x="Sovuq havo og‘ir, u pastga tushib, xonani aralashtiradi."),
            Q("Qozon dastasi nima uchun plastmassa yoki yog‘ochdan qilinadi?", "Ular issiqlikni yomon o‘tkazadi", ["Ular issiqlikni yaxshi o‘tkazadi", "Ular og‘ir", "Ular yaltiraydi"], d=2,
              x="Dasta qizimasa, qo‘l kuymaydi."),
            Q("Qishda qushlar nima uchun patlarini hurpaytiradi?", "Patlar orasida havo qatlami hosil bo‘ladi", ["Uchish oson bo‘ladi", "Rangi chiroyli ko‘rinadi", "Ular isib ketadi"], d=2,
              x="Havo issiqlikni yomon o‘tkazadi va tanani sovuqdan saqlaydi."),
            Q("Gulxan yonida yuzimiz issiqni qaysi yo‘l bilan sezadi?", "Nurlanish", ["Konveksiya", "Issiqlik o‘tkazuvchanlik", "Diffuziya"], d=2,
              x="Gulxandan chiqqan nur yuzga tushib, uni isitadi."),
            Q("Shamol qanday issiqlik hodisasi natijasida paydo bo‘ladi?", "Konveksiya", ["Issiqlik o‘tkazuvchanlik", "Faqat nurlanish", "Erish"], d=3,
              x="Quyosh yerni notekis isitadi, iliq havo ko‘tariladi, o‘rniga sovuq havo keladi."),
            Q("Termos ichidagi ko‘zgusimon yaltiroq devor nima uchun kerak?", "Nurlanishni qaytarish uchun", ["Chiroyli ko‘rinishi uchun", "Suvni tozalash uchun", "Og‘irlikni oshirish uchun"], d=3,
              x="Yaltiroq sirt issiqlik nurlarini ortga qaytaradi."),
            Q("Qo‘sh romli derazalar orasidagi havo nimaga xizmat qiladi?", "Issiqni saqlaydi", ["Yorug‘likni to‘sadi", "Shovqinni oshiradi", "Xonani sovitadi"], d=3,
              x="Havo qatlami issiqlikni yomon o‘tkazadi."),
            MATCH("Misolni issiqlik uzatish turi bilan juftlang",
                  [("Choydagi qoshiq qizishi", "o‘tkazuvchanlik"), ("Qozondagi suv aylanishi", "konveksiya"), ("Quyosh nuri isitishi", "nurlanish"),
                   ("Batareya xonani isitishi", "havo oqimlari"), ("Gulxan tafti", "issiqlik nurlari")], d=2,
                  x="Batareya konveksiya, gulxan nurlanish bilan isitadi."),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["motion", "density", "pressure", "heat_transfer"], chapter=C1)

# ============================================================ 2-chorak
_light = []
for a_in, d in [(30, 1), (45, 2), (60, 2)]:
    _light.append(Q(f"Nurning ko‘zguga tushish burchagi {a_in}°. Qaytish burchagi qancha?", f"{a_in}°",
                    [f"{v}°" for v in near(a_in, [90 - a_in, 2 * a_in, 180 - a_in, a_in + 10])], d=d,
                    x=f"Qaytish burchagi tushish burchagiga teng: {a_in}°."))
for a_in, d in [(25, 2), (40, 3)]:
    tot = 2 * a_in
    _light.append(Q(f"Tushish burchagi {a_in}°. Tushgan va qaytgan nurlar orasidagi burchak qancha?", f"{tot}°",
                    [f"{v}°" for v in near(tot, [a_in, 90 - a_in, 180 - tot, tot + 10])], d=d,
                    x=f"Qaytish burchagi ham {a_in}°, ular yig‘indisi {a_in} + {a_in} = {tot}°."))
for beta, d in [(30, 3), (70, 3)]:
    a_in = 90 - beta
    _light.append(Q(f"Nur bilan ko‘zgu sirti orasidagi burchak {beta}°. Tushish burchagi qancha?", f"{a_in}°",
                    [f"{v}°" for v in near(a_in, [beta, 2 * beta, 180 - beta, 90 + beta])], d=d,
                    x=f"Tushish burchagi nur bilan ko‘zguga o‘tkazilgan tik chiziq orasida: 90° − {beta}° = {a_in}°."))
for dist, d in [(2, 2), (3, 2)]:
    _light.append(Q(f"Bola yassi ko‘zgudan {dist} m uzoqlikda turibdi. Bola bilan uning tasviri orasidagi masofa qancha?", f"{2 * dist} m",
                    [f"{v} m" for v in near(2 * dist, [dist, dist + 1, 3 * dist, dist * 2 + 2])], d=d,
                    x=f"Tasvir ko‘zgu ortida xuddi shuncha — {dist} m masofada: {dist} + {dist} = {2 * dist} m."))
for t, d in [(2, 3)]:
    s = 300000 * t
    _light.append(Q(f"Yorug‘lik tezligi taxminan 300 000 km/s. Yorug‘lik {t} soniyada qancha masofani bosib o‘tadi?", f"{num(s)} km",
                    [f"{num(v)} km" for v in near(s, [300000, 150000, s * 10, 3000])], d=d, x=f"s = v · t = 300 000 · {t} = {num(s)} km."))

T.topic("light", "💡", L("Yorug‘lik hodisalari", "Light: reflection, refraction and lenses", "Световые явления"),
        chapter=C2,
        theory="Bir jinsli muhitda yorug‘lik to‘g‘ri chiziq bo‘ylab tarqaladi, tezligi taxminan 300 000 km/s. Shuning uchun soya hosil bo‘ladi.\n"
               "• Qaytish: nur ko‘zgudan qaytadi, qaytish burchagi tushish burchagiga teng. Yassi ko‘zgudagi tasvir ko‘zgu ortida xuddi shuncha masofada ko‘rinadi.\n"
               "• Sinish: nur bir muhitdan boshqasiga (havodan suvga) o‘tganda yo‘nalishini o‘zgartiradi — suvdagi qoshiq “singandek” ko‘rinadi.\n"
               "• Linzalar: yig‘uvchi (qavariq, o‘rtasi qalin) nurlarni bir nuqta — fokusga yig‘adi; sochuvchi (botiq, o‘rtasi yupqa) nurlarni sochadi. Lupa — yig‘uvchi linza.\n"
               "Oq yorug‘lik 7 rangdan iborat: qizil, to‘q sariq, sariq, yashil, havorang, ko‘k, binafsha.",
        items=[
            Q("Yorug‘lik bir jinsli muhitda qanday tarqaladi?", "To‘g‘ri chiziq bo‘ylab", ["Aylana bo‘ylab", "To‘lqinsimon egri", "Faqat pastga"],
              x="Shuning uchun shaffof bo‘lmagan jism ortida soya hosil bo‘ladi."),
            Q("Ko‘zguda nurning qaytishida qaysi qoida bajariladi?", "Qaytish burchagi tushish burchagiga teng", ["Qaytish burchagi doim 90°", "Nur qaytmaydi", "Qaytish burchagi 2 marta katta"],
              x="Bu yorug‘likning qaytish qonuni."),
            Q("Suvga solingan qoshiq nima uchun “singandek” ko‘rinadi?", "Yorug‘lik sinadi", ["Yorug‘lik qaytadi", "Qoshiq egiladi", "Suv qoshiqni eritadi"],
              x="Nur suvdan havoga o‘tganda yo‘nalishini o‘zgartiradi."),
            Q("Lupa qanday linza?", "Yig‘uvchi linza", ["Sochuvchi linza", "Yassi oyna", "Ko‘zgu"],
              x="Lupa — o‘rtasi qalin qavariq linza, u narsalarni kattalashtiradi."),
            Q("O‘rtasi chetlaridan qalin linza qanday ataladi?", "Yig‘uvchi", ["Sochuvchi", "Yassi", "Botiq"],
              x="Qavariq linza nurlarni fokusga yig‘adi."),
            Q("Kamalak qanday hosil bo‘ladi?", "Quyosh nuri tomchilarda sinib, ranglarga ajraladi", ["Bulutlar bo‘yalib qoladi", "Oy nuri qaytadi", "Chaqmoq yonadi"],
              x="Yomg‘ir tomchilari prizma kabi oq nurni 7 rangga ajratadi."),
            TF("Yassi ko‘zgudagi tasvirda o‘ng va chap tomonlar almashadi.", True, x="O‘ng qo‘lingizni ko‘tarsangiz, tasvir chap qo‘lini ko‘targandek ko‘rinadi."),
            TF("Sochuvchi linzaning o‘rtasi chetlaridan qalin.", False, x="Sochuvchi (botiq) linzaning o‘rtasi yupqa."),
            ORDER("Kamalak ranglarini tartib bilan tuzing", "qizil to‘q-sariq sariq yashil havorang ko‘k binafsha", d=2,
                  x="Kamalak ranglari: qizil, to‘q sariq, sariq, yashil, havorang, ko‘k, binafsha."),
            Q("Hovuz tubi aslidagidan qanday ko‘rinadi?", "Sayozroq", ["Chuqurroq", "Xuddi o‘zidek", "Umuman ko‘rinmaydi"], d=2,
              x="Nurning sinishi tufayli suv tubi yaqinroq, hovuz sayozroq ko‘rinadi."),
            Q("Oy Quyosh va Yer orasiga tushib, Quyoshni to‘sishi nima deyiladi?", "Quyosh tutilishi", ["Oy tutilishi", "To‘lin oy", "Kamalak"], d=2,
              x="Oyning soyasi Yerga tushadi va Quyosh qorayib ko‘rinadi."),
            Q("Yer soyasi Oyga tushishi nima deyiladi?", "Oy tutilishi", ["Quyosh tutilishi", "Yangi oy", "Aks-sado"], d=2,
              x="Oy tutilishida Yer Quyosh va Oy orasida bo‘ladi."),
            Q("Uzoqdagi narsalarni yaxshi ko‘rmaydigan odamga qanday ko‘zoynak kerak?", "Sochuvchi linzali", ["Yig‘uvchi linzali", "Rangli oynali", "Yassi oynali"], d=3,
              x="Yaqindan ko‘rarlik sochuvchi (botiq) linza bilan to‘g‘rilanadi."),
            Q("Ko‘z gavhari qanday linza vazifasini bajaradi?", "Yig‘uvchi linza", ["Sochuvchi linza", "Yassi ko‘zgu", "Prizma"], d=3,
              x="Gavhar nurlarni ko‘zning to‘r pardasiga yig‘adi."),
            MATCH("Asbobni ishlash asosi bilan juftlang",
                  [("Lupa", "yig‘uvchi linza"), ("Periskop", "ko‘zgularda qaytish"), ("Prizma", "oq nurni ranglarga ajratish"),
                   ("Fara", "botiq ko‘zgu nurni yo‘naltiradi"), ("Mikroskop", "bir nechta linza")], d=3,
                  x="Optik asboblar nurning qaytishi va sinishiga asoslangan."),
        ] + _light)

_snd = []
for t, d in [(3, 2), (5, 2), (2, 1)]:
    s = 340 * t
    a, w = unit_opts(s, [340, s + 340, s // 2, s - 340 if s > 680 else s * 2], "m", lo=1)
    _snd.append(Q(f"Chaqmoq chaqqandan {t} soniya keyin momaqaldiroq eshitildi. Chaqmoq qancha uzoqda? Tovush tezligi 340 m/s.", a, w, d=d,
                  x=f"s = v · t = 340 · {t} = {num(s)} m."))
for t, d in [(2, 3), (4, 3)]:
    s = 340 * t // 2
    a, w = unit_opts(s, [340 * t, s + 340, s // 2, 340, s * 3, s + 100], "m", lo=1)
    _snd.append(Q(f"Qoya tomon baqirgan bola aks-sadoni {t} soniyadan keyin eshitdi. Qoyagacha masofa qancha? Tovush tezligi 340 m/s.", a, w, d=d,
                  x=f"Tovush qoyagacha borib qaytdi: 340 · {t} = {340 * t} m, yarmi {num(s)} m."))
for n, t, d in [(200, 2, 2), (1320, 3, 3), (50, 1, 1)]:
    f = Fraction(n, t)
    assert f.denominator == 1
    a, w = unit_opts(f, [n * t, n, f + 100, f * 2, f + 50, f * 3, f + 10, f - 10], "Hz", lo=1)
    _snd.append(Q(f"Tor {t} soniyada {n} marta tebrandi. Tebranish chastotasi qancha?", a, w, d=d,
                  x=f"Chastota — 1 soniyadagi tebranishlar soni: {n} : {t} = {num(f)} Hz."))

T.topic("sound", "🔊", L("Tovush", "Sound", "Звук"),
        chapter=C2,
        theory="Tovush — jismlarning tebranishi natijasida hosil bo‘ladi va havo, suv, qattiq jism orqali tarqaladi. Havosiz bo‘shliqda (vakuumda) tovush tarqalmaydi.\n"
               "• Havoda tovush tezligi taxminan 340 m/s; suvda va qattiq jismlarda undan tezroq.\n"
               "• Chastota — 1 soniyadagi tebranishlar soni, birligi gers (Hz). Chastota katta bo‘lsa, tovush ingichka (baland ton), kichik bo‘lsa — yo‘g‘on.\n"
               "• Inson taxminan 20 Hz dan 20 000 Hz gacha eshitadi. Undan pasti — infratovush, yuqorisi — ultratovush (ko‘rshapalak, delfin eshitadi).\n"
               "To‘siqdan qaytgan tovush — aks-sado. Shovqin balandligi desibelda (dB) o‘lchanadi.",
        items=[
            Q("Tovush qanday hosil bo‘ladi?", "Jismlarning tebranishidan", ["Yorug‘lik sinishidan", "Jism sovishidan", "Zichlik o‘zgarishidan"],
              x="Masalan, gitara tori tebranib, havoni tebratadi."),
            Q("Tovush qayerda tarqalmaydi?", "Havosiz bo‘shliqda", ["Suvda", "Temirda", "Havoda"],
              x="Tovushni uzatadigan zarralar bo‘lmasa, u tarqalmaydi."),
            Q("Chastota birligi qaysi?", "Gers", ["Paskal", "Nyuton", "Metr"],
              x="1 Hz — soniyasiga bitta tebranish."),
            Q("Havoda tovush tezligi taxminan qancha?", "340 m/s", ["3 m/s", "300 000 km/s", "34 000 m/s"],
              x="Tovush havoda soniyasiga taxminan 340 metr yo‘l bosadi."),
            Q("To‘siqdan qaytib eshitilgan tovush nima deyiladi?", "Aks-sado", ["Shovqin", "Ultratovush", "Kamalak"],
              x="Aks-sado tog‘ va katta bo‘sh xonalarda yaxshi eshitiladi."),
            Q("Shovqin balandligi qaysi birlikda o‘lchanadi?", "Desibel", ["Gers", "Paskal", "Kilogramm"],
              x="Juda baland shovqin (100 dB dan ortiq) quloqqa zarar yetkazadi."),
            TF("Tovush suvda havodagiga qaraganda tezroq tarqaladi.", True, x="Suvda tovush tezligi havodagidan taxminan 4 marta katta."),
            TF("Inson ultratovushni yaxshi eshitadi.", False, x="Ultratovush 20 000 Hz dan yuqori, inson uni eshitmaydi."),
            ORDER(S, "Tovush havosiz bo‘shliqda tarqalmaydi"),
            Q("Pashshaning g‘ing‘illashi nima uchun ingichka eshitiladi?", "Qanotlari juda tez tebranadi", ["Pashsha juda kichik", "U qattiq uchadi", "U havoni isitadi"], d=2,
              x="Tebranish chastotasi katta bo‘lsa, ton baland — ovoz ingichka."),
            Q("Qaysi hayvon ultratovush yordamida mo‘ljal oladi?", "Ko‘rshapalak", ["Mushuk", "Tovuq", "Sigir"], d=2,
              x="Ko‘rshapalak ultratovush chiqaradi va uning aks-sadosini eshitadi."),
            Q("20 Hz dan past chastotali tovush nima deyiladi?", "Infratovush", ["Ultratovush", "Aks-sado", "Musiqa"], d=2,
              x="Infratovushni inson eshitmaydi, u zilzila va bo‘ronlarda paydo bo‘ladi."),
            Q("Kosmonavtlar ochiq koinotda bir-biri bilan qanday gaplashadi?", "Radio orqali", ["Baqirib", "Shivirlab", "Hushtak chalib"], d=2,
              x="Koinotda havo yo‘q, tovush tarqalmaydi, radioto‘lqinlar esa tarqaladi."),
            Q("Temir yo‘l relsiga quloq tutsak, poyezd tovushini nega oldinroq eshitamiz?", "Tovush temirda tezroq tarqaladi", ["Temir tovushni kuchaytiradi", "Havo tovushni to‘sadi", "Poyezd relsga yaqin"], d=3,
              x="Qattiq jismlarda tovush havodagidan ancha tez tarqaladi."),
            Q("Kemalarda dengiz chuqurligini o‘lchaydigan ultratovush asbobi nima?", "Exolot", ["Barometr", "Spidometr", "Termometr"], d=3,
              x="Exolot ultratovush yuboradi va dengiz tubidan qaytgan aks-sado vaqtini o‘lchaydi."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Chastota", "1 soniyadagi tebranishlar soni"), ("Aks-sado", "qaytgan tovush"), ("Ultratovush", "20 000 Hz dan yuqori"),
                   ("Infratovush", "20 Hz dan past"), ("Desibel", "shovqin birligi"), ("Vakuum", "tovush tarqalmaydigan bo‘shliq")], d=2,
                  x="Tovush haqidagi asosiy tushunchalar."),
        ] + _snd)

# --- Atom va molekula: formuladagi atomlar soni Python'da hisoblanadi.
FORM = {"H₂O": {"H": 2, "O": 1}, "CO₂": {"C": 1, "O": 2}, "O₂": {"O": 2}, "NaCl": {"Na": 1, "Cl": 1},
        "NH₃": {"N": 1, "H": 3}, "CH₄": {"C": 1, "H": 4}, "N₂": {"N": 2}, "H₂": {"H": 2}}
ELNAME = {"H": "vodorod", "O": "kislorod", "C": "uglerod", "N": "azot", "Na": "natriy", "Cl": "xlor", "Fe": "temir", "Cu": "mis"}
_atoms = []
for f, d in [("H₂O", 1), ("CO₂", 1), ("NH₃", 2), ("CH₄", 2)]:
    n = sum(FORM[f].values())
    _atoms.append(Q(f"{f} molekulasida jami nechta atom bor?", n, near(n, [n - 1, n + 1, len(FORM[f]), n + 2], lo=1), d=d,
                    x=" + ".join(f"{k} {ELNAME[e]}" for e, k in FORM[f].items()) + f" = {n} ta atom."))
for f, el, d in [("CO₂", "O", 1), ("CH₄", "H", 2), ("NH₃", "H", 2)]:
    n = FORM[f][el]
    _atoms.append(Q(f"{f} molekulasida nechta {ELNAME[el]} atomi bor?", n, near(n, [n + 1, n - 1, sum(FORM[f].values()), n + 2], lo=1), d=d,
                    x=f"{el} belgisidan keyingi kichik raqam atomlar sonini ko‘rsatadi: {n} ta."))
for k, f, d in [(2, "H₂O", 2), (3, "CO₂", 3), (4, "O₂", 3)]:
    n = k * sum(FORM[f].values())
    _atoms.append(Q(f"{k} ta {f} molekulasida jami nechta atom bor?", n, near(n, [sum(FORM[f].values()), n + k, n - k, k + sum(FORM[f].values())], lo=1), d=d,
                    x=f"Bitta molekulada {sum(FORM[f].values())} ta atom: {k} · {sum(FORM[f].values())} = {n}."))
for f, d in [("NaCl", 2), ("CH₄", 3)]:
    n = len(FORM[f])
    _atoms.append(Q(f"{f} moddasi nechta kimyoviy elementdan tashkil topgan?", n, near(n, [n + 1, sum(FORM[f].values()), n + 2, 1], lo=1), d=d,
                    x=f"Tarkibida {n} ta element: " + ", ".join(ELNAME[e] for e in FORM[f]) + "."))

T.topic("atoms", "⚛️", L("Atom, molekula va kimyoviy elementlar", "Atoms, molecules and chemical elements", "Атомы, молекулы и химические элементы"),
        chapter=C2,
        theory="Moddalar juda mayda zarralar — molekulalardan, molekulalar esa atomlardan tuzilgan. Atom markazida yadro, atrofida elektronlar harakatlanadi.\n"
               "Kimyoviy element — bir xil turdagi atomlar. Har bir element lotin harfidan iborat belgi bilan yoziladi:\n"
               "• H — vodorod, O — kislorod, C — uglerod, N — azot, Fe — temir, Cu — mis, Na — natriy, Cl — xlor.\n"
               "• Formulada kichik raqam atomlar sonini ko‘rsatadi: H₂O — 2 ta vodorod va 1 ta kislorod atomi (jami 3 ta), CO₂ — 1 ta uglerod va 2 ta kislorod atomi.\n"
               "Elementlar D. I. Mendeleyev tuzgan davriy jadvalda joylashtirilgan.",
        items=[
            Q("Molekulalar qanday zarralardan tuzilgan?", "Atomlardan", ["Hujayralardan", "Kristallardan", "Tomchilardan"],
              x="Molekula — bir nechta atomning birikmasi."),
            Q("“O” belgisi qaysi elementni bildiradi?", "Kislorod", ["Oltin", "Azot", "Uglerod"],
              x="O — kislorod (Oxygenium)."),
            Q("“H” belgisi qaysi elementni bildiradi?", "Vodorod", ["Geliy", "Temir", "Xlor"],
              x="H — vodorod (Hydrogenium)."),
            Q("Temirning kimyoviy belgisi qaysi?", "Fe", ["T", "Te", "F"],
              x="Fe — lotincha Ferrum so‘zidan."),
            Q("Misning kimyoviy belgisi qaysi?", "Cu", ["M", "Ms", "Mi"],
              x="Cu — lotincha Cuprum so‘zidan."),
            Q("Suvning formulasi qaysi?", "H₂O", ["CO₂", "O₂", "NaCl"],
              x="Suv molekulasi 2 ta vodorod va 1 ta kislorod atomidan iborat."),
            Q("Kimyoviy elementlar jadvalini kim tuzgan?", "D. I. Mendeleyev", ["I. Nyuton", "Ibn Sino", "Mirzo Ulug‘bek"],
              x="Mendeleyev 1869-yilda elementlarning davriy jadvalini tuzgan."),
            TF("Bir xil turdagi atomlar kimyoviy element deyiladi.", True, x="Masalan, barcha kislorod atomlari — kislorod elementi."),
            TF("Molekulalarni oddiy ko‘z bilan ko‘rish mumkin.", False, x="Molekulalar juda mayda, ular hatto oddiy mikroskopda ham ko‘rinmaydi."),
            ORDER(S, "Molekulalar atomlardan tuzilgan"),
            Q("“N” belgisi qaysi elementni bildiradi?", "Azot", ["Natriy", "Neon", "Nikel"], d=2,
              x="N — azot (Nitrogenium), natriy esa Na."),
            Q("“C” belgisi qaysi elementni bildiradi?", "Uglerod", ["Mis", "Kalsiy", "Xlor"], d=2,
              x="C — uglerod (Carboneum). Olmos va grafit ham ugleroddan iborat."),
            Q("Osh tuzining formulasi qaysi?", "NaCl", ["H₂O", "CO₂", "CH₄"], d=2,
              x="Osh tuzi natriy (Na) va xlor (Cl) elementlaridan tuzilgan."),
            Q("Atomning markazidagi qismi nima deyiladi?", "Yadro", ["Elektron", "Molekula", "Hujayra"], d=3,
              x="Atom yadrosi atrofida elektronlar harakatlanadi."),
            MATCH("Belgini element nomi bilan juftlang",
                  [("H", "vodorod"), ("O", "kislorod"), ("C", "uglerod"), ("N", "azot"), ("Fe", "temir"), ("Cu", "mis"), ("Na", "natriy"), ("Cl", "xlor")], d=2,
                  x="Kimyoviy belgilar lotincha nomlardan olingan."),
        ] + _atoms)
assert sum(FORM["H₂O"].values()) == 3 and FORM["CO₂"]["O"] == 2

_air = []
for V, d in [(100, 2), (500, 3)]:
    o2 = V * 21 // 100
    n2 = V * 78 // 100
    assert o2 * 100 == V * 21 and n2 * 100 == V * 78
    _air.append(Q(f"{V} litr havoda taxminan necha litr kislorod bor? Havoning 21 foizi kislorod.", f"{o2} l",
                  [f"{v} l" for v in near(o2, [n2, V - o2, o2 * 2, V // 2])], d=d, x=f"{V} · 21 : 100 = {o2} l."))

T.topic("substances", "🧪", L("Oddiy va murakkab moddalar", "Simple and compound substances", "Простые и сложные вещества"),
        chapter=C2,
        theory="• Oddiy modda — bir xil element atomlaridan tuzilgan: kislorod O₂, vodorod H₂, azot N₂, temir Fe, mis Cu, oltin Au.\n"
               "• Murakkab modda — turli element atomlaridan tuzilgan: suv H₂O, karbonat angidrid CO₂, osh tuzi NaCl, metan CH₄.\n"
               "Oddiy moddalar metallar va nometallarga bo‘linadi. Metallar yaltiroq, bolg‘alanuvchan, issiqlik va elektrni yaxshi o‘tkazadi; simob — xona haroratida suyuq metall.\n"
               "Nometallar: kislorod, azot, vodorod, uglerod, xlor, oltingugurt.\n"
               "Havo — aralashma: taxminan 78 % azot, 21 % kislorod, qolgani boshqa gazlar.",
        items=[
            Q("Qaysi modda oddiy modda?", "Kislorod", ["Suv", "Osh tuzi", "Karbonat angidrid"],
              x="Kislorod molekulasi faqat kislorod atomlaridan iborat."),
            Q("Qaysi modda murakkab modda?", "Suv", ["Temir", "Azot", "Mis"],
              x="Suv vodorod va kislorod atomlaridan tuzilgan."),
            Q("Qaysi biri metall?", "Alyuminiy", ["Oltingugurt", "Azot", "Kislorod"],
              x="Alyuminiy — yengil, yaltiroq metall."),
            Q("Qaysi biri nometall?", "Oltingugurt", ["Temir", "Mis", "Kumush"],
              x="Oltingugurt — sariq rangli mo‘rt nometall."),
            Q("Xona haroratida suyuq bo‘ladigan metall qaysi?", "Simob", ["Temir", "Oltin", "Mis"],
              x="Simob — yagona xona haroratida suyuq metall."),
            Q("Havoning asosiy qismini qaysi gaz tashkil etadi?", "Azot", ["Kislorod", "Karbonat angidrid", "Vodorod"],
              x="Havoning taxminan 78 foizi azot."),
            Q("Metallarning umumiy xossasi qaysi?", "Elektrni yaxshi o‘tkazadi", ["Suvda eriydi", "Mo‘rt, tez sinadi", "Yaltiramaydi"],
              x="Metallar yaltiroq, bolg‘alanuvchan va tokni yaxshi o‘tkazadi."),
            TF("Murakkab modda turli element atomlaridan tuzilgan.", True, x="Masalan, CO₂ uglerod va kislorod atomlaridan tuzilgan."),
            TF("Temir — murakkab modda.", False, x="Temir faqat temir atomlaridan iborat, u oddiy modda."),
            ORDER(S, "Suv murakkab modda hisoblanadi"),
            Q("Qaysi guruhda faqat oddiy moddalar bor?", "Temir, mis, kislorod", ["Suv, tuz, temir", "Shakar, suv, azot", "Osh tuzi, CO₂, mis"], d=2,
              x="Temir, mis va kislorod — bir xil atomlardan tuzilgan."),
            Q("Qaysi guruhda faqat murakkab moddalar bor?", "Suv, osh tuzi, CO₂", ["Temir, suv, azot", "Mis, oltin, kislorod", "Vodorod, tuz, oltin"], d=2,
              x="Suv, osh tuzi va karbonat angidrid turli elementlardan tuzilgan."),
            Q("Olmos va grafit qaysi elementdan tuzilgan?", "Uglerod", ["Kremniy", "Temir", "Kislorod"], d=3,
              x="Olmos va grafit — ikkalasi ham uglerod, faqat atomlari turlicha joylashgan."),
            Q("Tabiiy gazning asosiy qismi qaysi modda?", "Metan", ["Kislorod", "Azot", "Suv bug‘i"], d=3,
              x="Metan — CH₄, uglerod va vodoroddan tuzilgan murakkab modda."),
            MATCH("Moddani turi bilan juftlang",
                  [("O₂", "oddiy modda, nometall"), ("Fe", "oddiy modda, metall"), ("H₂O", "murakkab modda"),
                   ("Havo", "aralashma"), ("Simob", "suyuq metall")], d=2,
                  x="Moddalar tarkibiga qarab turlarga ajratiladi."),
            MATCH("Moddani formulasi bilan juftlang",
                  [("Suv", "H₂O"), ("Karbonat angidrid", "CO₂"), ("Osh tuzi", "NaCl"), ("Metan", "CH₄"), ("Kislorod", "O₂"), ("Azot", "N₂")], d=3,
                  x="Formula moddaning tarkibini ko‘rsatadi."),
        ] + _air)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["light", "sound", "atoms", "substances"], chapter=C2)

# ============================================================ 3-chorak
T.topic("classification", "🍄", L("Tirik organizmlarning tasnifi", "Classification of living things", "Классификация живых организмов"),
        chapter=C3,
        theory="Olimlar tirik organizmlarni o‘xshash belgilariga qarab guruhlarga ajratadi — bu tasnif (sistematika). Asosiy birlik — tur.\n"
               "• Bakteriyalar — bir hujayrali, hujayrasida shakllangan yadro yo‘q. Ba’zilari foydali (qatiq, pishloq tayyorlashda), ba’zilari kasallik qo‘zg‘atadi.\n"
               "• Zamburug‘lar — xlorofilli emas, tayyor organik modda bilan oziqlanadi, sporalar bilan ko‘payadi: qo‘ziqorin, mog‘or, achitqi.\n"
               "• O‘simliklar — xlorofill yordamida fotosintez qiladi, hujayrasida qattiq devor bor.\n"
               "• Hayvonlar — tayyor oziq bilan oziqlanadi, ko‘pchiligi faol harakatlanadi. Karl Linney turlarni ikki so‘zli nomlash usulini taklif qilgan.",
        items=[
            Q("Hujayrasida shakllangan yadrosi bo‘lmagan organizmlar qaysilar?", "Bakteriyalar", ["Zamburug‘lar", "O‘simliklar", "Hayvonlar"],
              x="Bakteriyalarning irsiy moddasi hujayrada erkin joylashgan."),
            Q("Fotosintez qila oladigan organizmlar qaysilar?", "O‘simliklar", ["Zamburug‘lar", "Hayvonlar", "Viruslar"],
              x="O‘simliklarda xlorofill bor, ular Quyosh nurida oziq tayyorlaydi."),
            Q("Qo‘ziqorin qaysi guruhga kiradi?", "Zamburug‘lar", ["O‘simliklar", "Hayvonlar", "Bakteriyalar"],
              x="Qo‘ziqorinda xlorofill yo‘q, u sporalar bilan ko‘payadi."),
            Q("Non xamirini ko‘pchitadigan organizm qaysi?", "Achitqi zamburug‘i", ["Mog‘or", "Yomg‘ir chuvalchangi", "Suvo‘t"],
              x="Achitqi karbonat angidrid gazini chiqaradi, xamir ko‘pchiydi."),
            Q("Qatiq va pishloq tayyorlashda qaysi organizmlar ishtirok etadi?", "Sut achituvchi bakteriyalar", ["Mog‘or zamburug‘lari", "Suvo‘tlar", "Hasharotlar"],
              x="Sut achituvchi bakteriyalar sutni qatiqqa aylantiradi."),
            Q("Zamburug‘lar qanday ko‘payadi?", "Sporalar bilan", ["Urug‘ bilan", "Tuxum bilan", "Piyozbosh bilan"],
              x="Spora — juda mayda ko‘payish hujayrasi."),
            Q("Tasnifning asosiy birligi qaysi?", "Tur", ["Oila", "Sinf", "Dunyo"],
              x="Tur — o‘xshash, o‘zaro chatishib nasl beradigan organizmlar guruhi."),
            TF("Zamburug‘lar fotosintez qiladi.", False, x="Zamburug‘larda xlorofill yo‘q, ular tayyor organik modda bilan oziqlanadi."),
            TF("Barcha bakteriyalar zararli.", False, x="Ko‘p bakteriyalar foydali: qatiq, pishloq tayyorlashda, tuproqda chirindi hosil qilishda."),
            TF("O‘simlik hujayrasida qattiq hujayra devori bor.", True, x="Hujayra devori o‘simlikka tayanch bo‘ladi."),
            ORDER(S, "Qo‘ziqorin zamburug‘lar guruhiga kiradi"),
            Q("Nonda paydo bo‘ladigan ko‘kimtir g‘ubor nima?", "Mog‘or zamburug‘i", ["Bakteriya", "Suvo‘t", "Chang"], d=2,
              x="Mog‘or — zamburug‘, mog‘orlagan nonni yeyish mumkin emas."),
            Q("Penitsillin dorisi qaysi organizmdan olingan?", "Mog‘or zamburug‘idan", ["Suvo‘tdan", "Qo‘ziqorindan", "Bakteriyadan"], d=2,
              x="Aleksandr Fleming 1928-yilda penitsill mog‘oridan dori olish mumkinligini aniqlagan."),
            Q("Turlarni ikki so‘zli nomlash usulini kim taklif qilgan?", "Karl Linney", ["Charlz Darvin", "Isaak Nyuton", "Ibn Sino"], d=2,
              x="Linney har bir turga avlod va tur nomidan iborat ikki so‘zli nom bergan."),
            Q("Archa va qarag‘ay o‘simliklarning qaysi guruhiga kiradi?", "Ochiq urug‘lilar", ["Yopiq urug‘lilar", "Yo‘sinlar", "Suvo‘tlar"], d=3,
              x="Ularning urug‘i meva ichida yetilmaydi, qubbalarda hosil bo‘ladi."),
            Q("Lishayniklar qanday organizmlar?", "Zamburug‘ va suvo‘t birgalikda", ["Faqat bakteriyalar", "Mayda hasharotlar", "Yosh daraxtlar"], d=3,
              x="Lishaynikda zamburug‘ suv beradi, suvo‘t esa fotosintez bilan oziq tayyorlaydi."),
            Q("Qaysi organizmlar hujayrali tuzilishga ega emas?", "Viruslar", ["Bakteriyalar", "Zamburug‘lar", "Suvo‘tlar"], d=3,
              x="Viruslar faqat boshqa organizm hujayrasi ichida ko‘payadi."),
            MATCH("Organizmni guruhi bilan juftlang",
                  [("Achitqi", "zamburug‘"), ("Sut achituvchi bakteriya", "bakteriya"), ("Qarag‘ay", "o‘simlik"), ("Chayon", "hayvon"),
                   ("Mog‘or", "mikroskopik zamburug‘"), ("Suvo‘t", "suvda o‘suvchi o‘simlik")], d=2,
                  x="Guruh oziqlanish va hujayra tuzilishiga qarab aniqlanadi."),
            MATCH("Guruhni belgisi bilan juftlang",
                  [("Bakteriyalar", "shakllangan yadrosi yo‘q"), ("Zamburug‘lar", "sporalar bilan ko‘payadi"), ("O‘simliklar", "fotosintez qiladi"),
                   ("Hayvonlar", "tayyor oziq yeydi, faol harakatlanadi"), ("Viruslar", "hujayrasi yo‘q")], d=3,
                  x="Har bir guruhning o‘ziga xos belgilari bor."),
        ])

_rings = []
for n, d in [(25, 1), (40, 1)]:
    _rings.append(Q(f"Kesilgan daraxt tanasida {n} ta yillik halqa sanaldi. Daraxt necha yoshda bo‘lgan?", f"{n} yosh",
                    [f"{v} yosh" for v in near(n, [n * 2, n // 2, n + 10, n - 5])], d=d, x="Har yili bitta yillik halqa hosil bo‘ladi."))
for planted, cut, d in [(2010, 2024, 2), (1998, 2025, 3)]:
    n = cut - planted
    _rings.append(Q(f"Daraxt {planted}-yilda ekilib, {cut}-yilda kesildi. Tanasida taxminan nechta yillik halqa bor?", n,
                    near(n, [n + 1, n - 1, n + 10, n * 2]), d=d, x=f"{cut} − {planted} = {n}: har yili bitta halqa."))

T.topic("plant_organs", "🌿", L("O‘simlik a’zolari va to‘qimalari", "Plant organs and tissues", "Органы и ткани растений"),
        chapter=C3,
        theory="Gulli o‘simlik a’zolari: vegetativ — ildiz, poya, barg; generativ (ko‘payish) — gul, meva, urug‘.\n"
               "• Ildiz tizimi: o‘q ildiz (loviya, kungaboqar, g‘o‘za) va popuk ildiz (bug‘doy, makkajo‘xori, piyoz).\n"
               "• Barg tomirlanishi: to‘rsimon (olma, terak) va parallel (bug‘doy, makkajo‘xori). Barg og‘izchalari orqali gaz almashinadi va suv bug‘lanadi.\n"
               "• To‘qimalar: qoplovchi (himoya), hosil qiluvchi (bo‘linib o‘stiradi), asosiy (fotosintez, zaxira to‘plash), o‘tkazuvchi (suv va oziqni tashiydi), mexanik (tayanch).\n"
               "Daraxt tanasida har yili bitta yillik halqa hosil bo‘ladi — ular soni daraxt yoshini ko‘rsatadi.",
        items=[
            Q("Qaysi biri o‘simlikning vegetativ a’zosi?", "Barg", ["Gul", "Meva", "Urug‘"],
              x="Vegetativ a’zolar — ildiz, poya, barg."),
            Q("Qaysi biri generativ (ko‘payish) a’zosi?", "Gul", ["Ildiz", "Poya", "Barg"],
              x="Gul, meva va urug‘ ko‘payishga xizmat qiladi."),
            Q("Bug‘doyning ildiz tizimi qanday?", "Popuk ildiz", ["O‘q ildiz", "Ildizmeva", "Havo ildiz"],
              x="Bug‘doyda bir xil ingichka ildizlar popuk hosil qiladi."),
            Q("Loviyaning ildiz tizimi qanday?", "O‘q ildiz", ["Popuk ildiz", "Ildizpoya", "Tuganak"],
              x="O‘q ildizda bitta asosiy yo‘g‘on ildiz yaxshi rivojlangan."),
            Q("Barg og‘izchalari nima uchun kerak?", "Gaz almashinuvi va suv bug‘lanishi", ["Hasharot tutish", "Urug‘ saqlash", "Tuproqqa yopishish"],
              x="Og‘izchalar orqali havo kiradi-chiqadi va suv bug‘lanadi."),
            Q("O‘simlikni tashqi ta’sirdan himoya qiladigan to‘qima qaysi?", "Qoplovchi to‘qima", ["O‘tkazuvchi to‘qima", "Asosiy to‘qima", "Hosil qiluvchi to‘qima"],
              x="Barg po‘sti va daraxt po‘kagi — qoplovchi to‘qima."),
            Q("Ildizdan barglarga suv qaysi to‘qima orqali boradi?", "O‘tkazuvchi to‘qima", ["Qoplovchi to‘qima", "Mexanik to‘qima", "Hosil qiluvchi to‘qima"],
              x="O‘tkazuvchi to‘qimaning naylari suv va oziqni tashiydi."),
            TF("Makkajo‘xori bargi parallel tomirlangan.", True, x="Bir urug‘pallali o‘simliklarda barg tomirlari parallel joylashadi."),
            TF("Hosil qiluvchi to‘qima hujayralari bo‘linmaydi.", False, x="Aksincha, ular tez bo‘linib, o‘simlikni o‘stiradi."),
            ORDER(S, "Ildiz poya va barg vegetativ a’zolar"),
            Q("Ildiz va poya uchidagi o‘sishni qaysi to‘qima ta’minlaydi?", "Hosil qiluvchi to‘qima", ["Qoplovchi to‘qima", "Mexanik to‘qima", "O‘tkazuvchi to‘qima"], d=2,
              x="Hosil qiluvchi to‘qima hujayralari bo‘linib, yangi hujayralar beradi."),
            Q("Kartoshka tuganagida kraxmal qaysi to‘qimada to‘planadi?", "Asosiy (zaxira) to‘qimada", ["Qoplovchi to‘qimada", "Mexanik to‘qimada", "O‘tkazuvchi to‘qimada"], d=2,
              x="Asosiy to‘qimaning g‘amlovchi hujayralari zaxira modda to‘playdi."),
            Q("Poyaga mustahkamlik beradigan to‘qima qaysi?", "Mexanik to‘qima", ["Asosiy to‘qima", "Qoplovchi to‘qima", "Hosil qiluvchi to‘qima"], d=2,
              x="Mexanik to‘qima tolalari o‘simlikka tayanch bo‘ladi."),
            Q("Olma bargining tomirlanishi qanday?", "To‘rsimon", ["Parallel", "Yoysimon", "Tomirsiz"], d=2,
              x="Ikki urug‘pallali o‘simliklar bargi to‘rsimon tomirlangan."),
            Q("Barglarda hosil bo‘lgan organik moddalar poya bo‘ylab qayerga tashiladi?", "Pastga, ildizlarga", ["Faqat gulga", "Havoga", "Tuproqqa to‘kiladi"], d=3,
              x="Lub qismidagi elaksimon naylar orqali organik moddalar pastga, ildizga boradi."),
            Q("Daraxt tanasida yillik halqalarni qaysi qatlam hosil qiladi?", "Kambiy", ["Po‘kak", "O‘zak", "Barg po‘sti"], d=3,
              x="Kambiy hujayralari bo‘linib, har yili yangi yog‘ochlik qatlamini hosil qiladi."),
            MATCH("To‘qimani vazifasi bilan juftlang",
                  [("Qoplovchi", "himoya qiladi"), ("Hosil qiluvchi", "bo‘linib o‘stiradi"), ("Asosiy", "fotosintez va zaxira"),
                   ("O‘tkazuvchi", "suv va oziqni tashiydi"), ("Mexanik", "tayanch bo‘ladi")], d=2,
                  x="Har bir to‘qima o‘z vazifasini bajaradi."),
            MATCH("O‘simlikni ildiz tizimi yoki barg tomirlanishi bilan juftlang",
                  [("Bug‘doy", "popuk ildiz"), ("Kungaboqar", "o‘q ildiz"), ("Makkajo‘xori bargi", "parallel tomirlanish"),
                   ("Olma bargi", "to‘rsimon tomirlanish"), ("Piyoz", "popuk ildiz, parallel tomirlar")], d=3,
                  x="Bir urug‘pallalilarda popuk ildiz va parallel tomirlar, ikki urug‘pallalilarda o‘q ildiz va to‘rsimon tomirlar."),
        ] + _rings)

LEGS = {"o‘rgimchak": 8, "chumoli": 6, "qo‘ng‘iz": 6, "chayon": 8, "kapalak": 6}
_legs = []
for (a, na), (b, nb), d in [(("o‘rgimchak", 2), ("chumoli", 3), 2), (("chayon", 1), ("qo‘ng‘iz", 4), 3), (("kapalak", 5), ("o‘rgimchak", 1), 3)]:
    tot = na * LEGS[a] + nb * LEGS[b]
    _legs.append(Q(f"{na} ta {a} va {nb} ta {b}ning jami nechta oyog‘i bor?", tot,
                   near(tot, [(na + nb) * 6, (na + nb) * 8, tot + 2, tot - 2], lo=1), d=d,
                   x=f"{a.capitalize()} — {LEGS[a]} oyoqli, {b} — {LEGS[b]} oyoqli: {na} · {LEGS[a]} + {nb} · {LEGS[b]} = {tot}."))

T.topic("animals", "🦎", L("Hayvonlar tuzilishi: umurtqasiz va umurtqalilar", "Invertebrates and vertebrates", "Беспозвоночные и позвоночные"),
        chapter=C3,
        theory="Hayvonlar ikki katta guruhga bo‘linadi.\n"
               "• Umurtqasizlar — umurtqa pog‘onasi yo‘q: chuvalchanglar, mollyuskalar (shilliqqurt, sakkizoyoq), bo‘g‘imoyoqlilar, meduza. Hasharotlar 6 oyoqli, tanasi 3 bo‘limli (bosh, ko‘krak, qorin); o‘rgimchaksimonlar 8 oyoqli.\n"
               "• Umurtqalilar — ichki skeleti va umurtqa pog‘onasi bor. 5 sinfi: baliqlar, suvda hamda quruqlikda yashovchilar, sudralib yuruvchilar, qushlar, sut emizuvchilar.\n"
               "• Baliqlar jabra bilan nafas oladi; baqa lichinkasi (itbaliq) suvda o‘sadi; sudralib yuruvchilar terisi quruq, muguz tangachali.\n"
               "Qushlar (pat, tumshuq) va sut emizuvchilar (jun, bolasini sut bilan boqadi) — issiqqonli, yuragi 4 kamerali.",
        items=[
            Q("Hasharotlarning nechta oyog‘i bor?", "6 ta", ["4 ta", "8 ta", "10 ta"],
              x="Hasharotlarning 3 juft, ya’ni 6 ta oyog‘i bor."),
            Q("O‘rgimchakning nechta oyog‘i bor?", "8 ta", ["6 ta", "4 ta", "10 ta"],
              x="O‘rgimchaksimonlarning 4 juft oyog‘i bor, ular hasharot emas."),
            Q("Qaysi hayvon umurtqasiz?", "Yomg‘ir chuvalchangi", ["Baqa", "Ilon", "Chumchuq"],
              x="Chuvalchangda umurtqa pog‘onasi yo‘q."),
            Q("Qaysi hayvon umurtqali?", "Kaltakesak", ["O‘rgimchak", "Shilliqqurt", "Meduza"],
              x="Kaltakesak — sudralib yuruvchi umurtqali hayvon."),
            Q("Kit qaysi sinfga kiradi?", "Sut emizuvchilar", ["Baliqlar", "Sudralib yuruvchilar", "Qushlar"],
              x="Kit o‘pka bilan nafas oladi va bolasini sut bilan boqadi."),
            Q("Qaysi hayvonlarning tanasi pat bilan qoplangan?", "Qushlar", ["Baliqlar", "Sut emizuvchilar", "Hasharotlar"],
              x="Pat faqat qushlarga xos."),
            Q("Baliqlar qanday nafas oladi?", "Jabra bilan", ["O‘pka bilan", "Traxeya bilan", "Faqat teri bilan"],
              x="Jabralar suvda erigan kislorodni o‘zlashtiradi."),
            Q("Hasharot tanasi nechta bo‘limdan iborat?", "3 ta", ["2 ta", "4 ta", "6 ta"],
              x="Bosh, ko‘krak va qorin."),
            TF("Ko‘rshapalak — qush.", False, x="Ko‘rshapalak — uchadigan sut emizuvchi, bolasini sut bilan boqadi."),
            TF("Pingvin uchmasa ham qush hisoblanadi.", True, x="Pingvinning pati, tumshug‘i bor va tuxum qo‘yadi."),
            TF("O‘rgimchak — hasharot.", False, x="O‘rgimchakning 8 oyog‘i bor, u o‘rgimchaksimonlarga kiradi."),
            ORDER(S, "Qushlar va sut emizuvchilar issiqqonli"),
            Q("Ilon qaysi sinfga kiradi?", "Sudralib yuruvchilar", ["Suvda hamda quruqlikda yashovchilar", "Baliqlar", "Sut emizuvchilar"], d=2,
              x="Ilonning terisi quruq, muguz tangachalar bilan qoplangan."),
            Q("Baqa qaysi sinfga kiradi?", "Suvda hamda quruqlikda yashovchilar", ["Sudralib yuruvchilar", "Baliqlar", "Qushlar"], d=2,
              x="Baqa lichinkasi suvda jabra bilan, voyaga yetgani o‘pka va teri bilan nafas oladi."),
            Q("Sakkizoyoq qaysi guruhga kiradi?", "Mollyuskalar", ["Baliqlar", "Hasharotlar", "Sut emizuvchilar"], d=2,
              x="Sakkizoyoq — yumshoq tanali mollyuska."),
            Q("Bo‘g‘imoyoqlilar tanasini tashqaridan nima qoplab turadi?", "Qattiq xitin qoplam", ["Pat", "Jun", "Shilimshiq teri"], d=2,
              x="Xitin qoplam — tashqi skelet, o‘sish uchun hayvon uni tullab tashlaydi."),
            Q("Qaysi hayvonlarning yuragi 2 kamerali?", "Baliqlar", ["Qushlar", "Sut emizuvchilar", "Odam"], d=3,
              x="Baliq yuragida bitta bo‘lmacha va bitta qorincha bor."),
            Q("Qaysi hayvonlar issiqqonli?", "Qushlar va sut emizuvchilar", ["Baliqlar va baqalar", "Ilon va toshbaqalar", "Hasharotlar"], d=2,
              x="Ularning tana harorati atrof-muhitga bog‘liq bo‘lmay, doimiy saqlanadi."),
            MATCH("Hayvonni sinfi yoki guruhi bilan juftlang",
                  [("Akula", "baliqlar"), ("Baqa", "suvda-quruqlikda yashovchilar"), ("Toshbaqa", "sudralib yuruvchilar"),
                   ("Tuyaqush", "qushlar"), ("Delfin", "sut emizuvchilar"), ("Chayon", "o‘rgimchaksimonlar")], d=2,
                  x="Tashqi ko‘rinish aldashi mumkin: delfin baliqqa o‘xshasa ham sut emizuvchi."),
        ] + _legs)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["classification", "plant_organs", "animals"], chapter=C3)

# ============================================================ 4-chorak
_plate = []
for cm, years, d in [(5, 100, 2), (3, 1000, 3)]:
    tot = cm * years
    a = f"{num(tot)} sm" if tot < 1000 else f"{num(Fraction(tot, 100))} m"
    wr = [f"{num(v)} sm" for v in near(tot, [cm + years, tot // 10, tot * 10, tot * 2])] if tot < 1000 else \
         [f"{num(Fraction(v, 100))} m" for v in near(tot, [tot // 10, tot * 10, cm * 100, tot * 2, tot // 2])]
    _plate.append(Q(f"Litosfera plitasi yiliga {cm} sm siljiydi. {years} yilda qancha siljiydi?", a, wr, d=d,
                    x=f"{cm} · {years} = {num(tot)} sm" + (f" = {num(Fraction(tot, 100))} m." if tot >= 1000 else ".")))

T.topic("earth_crust", "🌋", L("Yer po‘stining harakatlari: vulqon va zilzila", "Volcanoes and earthquakes", "Движения земной коры: вулканы и землетрясения"),
        chapter=C4,
        theory="Yer po‘sti yaxlit emas: u litosfera plitalaridan iborat. Plitalar yiliga bir necha santimetr sekin siljiydi.\n"
               "• Zilzila (yer qimirlashi) — yer po‘stining silkinishi. U boshlangan joy — o‘choq, uning ustidagi yer yuzasi nuqtasi — episentr. Zilzilani seysmograf yozib oladi, kuchi ballarda baholanadi.\n"
               "• Vulqon — magma yer yuzasiga otilib chiqadigan tog‘. Qismlari: magma o‘chog‘i, bo‘g‘iz, krater. Yer yuzasiga chiqqan magma — lava.\n"
               "• Okean ostidagi kuchli zilzila ulkan to‘lqin — sunami hosil qiladi. Plitalar to‘qnashganda tog‘lar ko‘tariladi (Himolay).\n"
               "O‘zbekiston seysmik faol hududda joylashgan; Toshkentda 1966-yil 26-aprelda kuchli zilzila bo‘lgan.",
        items=[
            Q("Yer po‘stining silkinishi nima deyiladi?", "Zilzila", ["Sunami", "Vulqon", "Ko‘chki"],
              x="Zilzila — yer qimirlashi."),
            Q("Zilzilani yozib oladigan asbob qaysi?", "Seysmograf", ["Barometr", "Termometr", "Kompas"],
              x="Seysmograf yer tebranishlarini qog‘oz yoki ekranda chizib beradi."),
            Q("Vulqondan yer yuzasiga oqib chiqqan qaynoq tog‘ jinsi nima deyiladi?", "Lava", ["Qum", "Muz", "Loy"],
              x="Yer ichidagi magma yer yuzasiga chiqqach lava deyiladi."),
            Q("Vulqon cho‘qqisidagi voronkasimon chuqurlik nima deyiladi?", "Krater", ["Episentr", "Plita", "Daryo o‘zani"],
              x="Krater orqali lava, gaz va kul otilib chiqadi."),
            Q("Zilzila o‘chog‘i ustidagi yer yuzasi nuqtasi nima deyiladi?", "Episentr", ["Krater", "Kon", "Qutb"],
              x="Episentrda silkinish eng kuchli seziladi."),
            Q("Okean tubidagi kuchli zilziladan hosil bo‘lgan ulkan to‘lqin nima?", "Sunami", ["Briz", "Geyzer", "Kamalak"],
              x="Sunami qirg‘oqqa yetganda juda katta vayronagarchilik keltiradi."),
            Q("Zilzila paytida xonada bo‘lsangiz, qayerda panalash xavfsizroq?", "Mustahkam stol tagida", ["Deraza yonida", "Liftda", "Shkaf ustida"],
              x="Mustahkam stol tushayotgan buyumlardan himoya qiladi, derazalardan uzoq turish kerak."),
            TF("O‘zbekiston seysmik faol hududda joylashgan.", True, x="O‘zbekistonda vaqti-vaqti bilan zilzilalar bo‘lib turadi."),
            TF("Litosfera plitalari umuman harakatlanmaydi.", False, x="Plitalar yiliga bir necha santimetr siljiydi."),
            TF("Zilzila paytida liftdan foydalanish mumkin.", False, x="Lift to‘xtab qolishi yoki shikastlanishi mumkin."),
            ORDER(S, "Seysmograf zilzilani yozib oladi"),
            Q("Toshkentdagi kuchli zilzila qaysi yilda bo‘lgan?", "1966-yilda", ["1920-yilda", "1991-yilda", "2000-yilda"], d=2,
              x="1966-yil 26-aprelda Toshkentda kuchli zilzila bo‘lib, shahar qayta qurilgan."),
            Q("Vaqti-vaqti bilan otilib chiqadigan issiq suv favvorasi nima?", "Geyzer", ["Buloq", "Sharshara", "Sunami"], d=2,
              x="Geyzerlar Islandiya va Kamchatkada ko‘p."),
            Q("Italiyadagi mashhur vulqon qaysi?", "Vezuviy", ["Jomolungma", "Elbrus", "Hazrati Sulton"], d=2,
              x="Vezuviy otilishi qadimgi Pompey shahrini kul ostida qoldirgan."),
            Q("Himolay tog‘lari qanday hosil bo‘lgan?", "Litosfera plitalari to‘qnashuvidan", ["Vulqon kulidan", "Daryo yotqiziqlaridan", "Muzlik erishidan"], d=2,
              x="Plitalar bir-biriga siqilib, yer po‘sti burmalanib ko‘tarilgan."),
            Q("Tog‘ jinslarining harorat, suv va shamol ta’sirida yemirilishi nima deyiladi?", "Nurash", ["Zilzila", "Vulqon otilishi", "Konveksiya"], d=3,
              x="Nurash natijasida qoyalar sekin-asta qum va tuproqqa aylanadi."),
            Q("Yer ichidagi erigan qaynoq tog‘ jinsi nima deyiladi?", "Magma", ["Lava", "Kul", "Bazalt"], d=3,
              x="Magma yer yuzasiga chiqqach, lava deb ataladi."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("O‘choq", "zilzila boshlangan joy"), ("Episentr", "o‘choq ustidagi yer yuzasi nuqtasi"), ("Krater", "vulqon cho‘qqisidagi chuqurlik"),
                   ("Lava", "yer yuzasiga chiqqan magma"), ("Sunami", "zilziladan hosil bo‘lgan ulkan to‘lqin"), ("Seysmograf", "tebranishni yozuvchi asbob")], d=2,
                  x="Yer po‘sti harakatlariga oid asosiy tushunchalar."),
        ] + _plate)

_wx = []
for temps, d in [([2, 8, 14, 8], 2), ([-4, 0, 6, 2], 3), ([12, 18, 26, 20], 2)]:
    avg = Fraction(sum(temps), len(temps))
    assert avg.denominator == 1
    shown = ", ".join(temp(t) for t in temps)
    said = ", ".join(temp_say(t) for t in temps)
    a = temp(int(avg))
    w = [temp(int(v)) for v in near(avg, [sum(temps), max(temps), min(temps), avg + 2, avg - 2], lo=-50)]
    _wx.append(Q(f"Sutka davomida harorat o‘lchandi: {shown}. O‘rtacha sutkalik harorat qancha?", a, w, d=d,
                 say=f"Sutka davomida harorat o‘lchandi: {said}. O‘rtacha sutkalik harorat qancha?",
                 x=f"({' + '.join(str(t) for t in temps)}) : {len(temps)} = {int(avg)} °C.".replace("+ -", "− ").replace("(-", "(−")))
for lo_t, hi_t, d in [(3, 15, 2), (-6, 9, 3), (18, 34, 2)]:
    amp = hi_t - lo_t
    a = f"{amp} °C"
    w = [f"{v} °C" for v in near(amp, [hi_t + lo_t, hi_t, abs(lo_t), amp + 2], lo=1)]
    _wx.append(Q(f"Kun davomida eng past harorat {temp(lo_t)}, eng yuqori {temp(hi_t)} bo‘ldi. Harorat amplitudasi qancha?", a, w, d=d,
                 say=f"Kun davomida eng past harorat {temp_say(lo_t)}, eng yuqori {temp_say(hi_t)} bo‘ldi. Harorat amplitudasi qancha?",
                 x=f"Amplituda — eng yuqori va eng past harorat farqi: {hi_t} − ({lo_t}) = {amp} °C.".replace("(-", "(−")
                 if lo_t < 0 else f"Amplituda — eng yuqori va eng past harorat farqi: {hi_t} − {lo_t} = {amp} °C."))
for base, km, d in [(24, 3, 3), (20, 2, 2)]:
    top = base - 6 * km
    _wx.append(Q(f"Tog‘ etagida harorat {temp(base)}. Har 1 km balandlikda harorat taxminan 6 °C pasayadi. {km} km balandlikda harorat qancha?", temp(top),
                 [temp(v) for v in near(top, [base + 6 * km, base - km, base - 6, top - 6], lo=-50)], d=d,
                 x=f"{base} − 6 · {km} = {top} °C."))

T.topic("weather_climate", "⛅", L("Ob-havo va iqlim", "Weather and climate", "Погода и климат"),
        chapter=C4,
        theory="Ob-havo — ma’lum joyda qisqa vaqt ichidagi atmosfera holati; iqlim — shu joyning ko‘p yillik ob-havo tartibi.\n"
               "• Ob-havo elementlari va asboblari: harorat — termometr, atmosfera bosimi — barometr, shamol yo‘nalishi — flyuger, shamol tezligi — anemometr, havo namligi — gigrometr, yog‘in — yog‘in o‘lchagich.\n"
               "• Shamol — havoning yuqori bosimli joydan past bosimli joyga harakati. Balandlikka ko‘tarilgan sari harorat har 1 km da taxminan 6 °C pasayadi.\n"
               "• O‘rtacha sutkalik harorat — o‘lchangan haroratlar yig‘indisi ularning soniga bo‘linadi; amplituda — eng yuqori va eng past harorat farqi.\n"
               "Iqlim mintaqalari: ekvatorial, tropik, mo‘tadil, qutbiy. O‘zbekiston iqlimi — keskin kontinental.",
        items=[
            Q("Ma’lum joydagi ko‘p yillik ob-havo tartibi nima deyiladi?", "Iqlim", ["Ob-havo", "Shamol", "Yog‘in"],
              x="Ob-havo tez o‘zgaradi, iqlim esa ko‘p yillar davomida saqlanadi."),
            Q("Shamol yo‘nalishini qaysi asbob ko‘rsatadi?", "Flyuger", ["Barometr", "Termometr", "Gigrometr"],
              x="Flyuger shamolga qarab buriladi."),
            Q("Shamol tezligini qaysi asbob o‘lchaydi?", "Anemometr", ["Flyuger", "Barometr", "Termometr"],
              x="Anemometr parraklari shamolda aylanib, tezlikni ko‘rsatadi."),
            Q("Havo namligini qaysi asbob o‘lchaydi?", "Gigrometr", ["Barometr", "Spidometr", "Anemometr"],
              x="Gigrometr havodagi suv bug‘i miqdorini ko‘rsatadi."),
            Q("Shamol qayerdan qayerga esadi?", "Yuqori bosimdan past bosimga", ["Past bosimdan yuqori bosimga", "Faqat shimoldan janubga", "Faqat tog‘dan cho‘lga"],
              x="Havo bosim farqi tufayli harakatlanadi."),
            Q("Ob-havoni bashorat qiluvchi mutaxassis kim?", "Sinoptik", ["Geolog", "Astronom", "Seysmolog"],
              x="Sinoptiklar meteostansiya ma’lumotlari asosida ob-havoni oldindan aytadi."),
            Q("O‘zbekiston iqlimi qanday?", "Keskin kontinental", ["Ekvatorial", "Qutbiy", "Musson"],
              x="Yozi issiq va quruq, qishi sovuq, yog‘in kam."),
            TF("Ob-havo bir kun ichida ham o‘zgarishi mumkin.", True, x="Ertalab quyoshli bo‘lsa, kechqurun yomg‘ir yog‘ishi mumkin."),
            TF("Tog‘ga ko‘tarilgan sari havo isiydi.", False, x="Balandlikda havo siyrak va sovuq bo‘ladi."),
            ORDER(S, "Barometr atmosfera bosimini o‘lchaydi"),
            Q("Qaysi iqlim mintaqasida yil bo‘yi issiq va nam?", "Ekvatorial", ["Qutbiy", "Mo‘tadil", "Keskin kontinental"], d=2,
              x="Ekvator yaqinida Quyosh tik tushadi va yomg‘ir ko‘p yog‘adi."),
            Q("Qaysi iqlim mintaqasida yil bo‘yi sovuq?", "Qutbiy", ["Tropik", "Ekvatorial", "Subtropik"], d=2,
              x="Qutblar yaqinida Quyosh nurlari juda qiya tushadi."),
            Q("Qaysi biri yog‘in turi?", "Do‘l", ["Shamol", "Bosim", "Harorat"], d=2,
              x="Yomg‘ir, qor va do‘l — yog‘in turlari."),
            Q("Dengiz bo‘yida kunduzi shamol qayerdan esadi?", "Dengizdan quruqlikka", ["Quruqlikdan dengizga", "Tog‘dan tog‘ga", "Faqat yuqoridan"], d=3,
              x="Kunduzi quruqlik tez isiydi, uning ustida bosim pasayadi va dengizdan salqin havo keladi — bu briz."),
            MATCH("Asbobni o‘lchaydigan kattaligi bilan juftlang",
                  [("Termometr", "harorat"), ("Barometr", "atmosfera bosimi"), ("Flyuger", "shamol yo‘nalishi"), ("Anemometr", "shamol tezligi"),
                   ("Gigrometr", "havo namligi"), ("Yog‘in o‘lchagich", "yog‘in miqdori")], d=2,
                  x="Meteostansiyada bu asboblarning hammasi bor."),
        ] + _wx)

# --- Masshtab va koordinatalar (Python'da hisoblanadi).
_map = []
for scale, sm, d in [(100000, 4, 1), (50000, 6, 2), (1000000, 3, 2), (200000, 5, 2)]:
    km = Fraction(scale * sm, 100000)
    assert km.denominator == 1
    a, w = unit_opts(km, [km * 10, Fraction(km, 10), sm, km + sm], "km")
    _map.append(Q(f"Xarita masshtabi 1 : {num(scale)}. Xaritada ikki shahar orasi {sm} sm. Haqiqiy masofa qancha?", a, w, d=d,
                  x=f"1 sm da {num(Fraction(scale, 100000))} km: {sm} · {num(Fraction(scale, 100000))} = {num(km)} km."))
for scale, km, d in [(200000, 12, 3), (500000, 20, 3)]:
    sm = Fraction(km * 100000, scale)
    assert sm.denominator == 1
    a, w = unit_opts(sm, [km, sm * 10, sm + 2, Fraction(km, 10) if km % 10 == 0 else sm * 2], "sm")
    _map.append(Q(f"Masshtab 1 : {num(scale)}. Haqiqiy masofa {km} km. Xaritada bu masofa necha santimetr bo‘ladi?", a, w, d=d,
                  x=f"1 sm da {num(Fraction(scale, 100000))} km: {km} : {num(Fraction(scale, 100000))} = {num(sm)} sm."))
for scale, d in [(500000, 2), (10000, 3)]:
    per = Fraction(scale, 100000)
    ans = f"1 sm da {num(per)} km" if per >= 1 else f"1 sm da {num(scale // 100)} m"
    w = [f"1 sm da {num(scale)} km", f"1 sm da {num(scale // 1000)} km", f"1 sm da {num(scale // 10)} m"]
    w = [v for v in w if v != ans]
    _map.append(Q(f"1 : {num(scale)} sonli masshtabni nomli masshtabga aylantiring.", ans, w, d=d,
                  x=f"{num(scale)} sm = {num(scale // 100)} m" + (f" = {num(per)} km." if per >= 1 else ".")))
for lat1, lat2, d in [(40, 45, 2), (38, 44, 3)]:
    dl = lat2 - lat1
    km = dl * 111
    _map.append(Q(f"Ikki nuqta bir meridianda: biri {lat1}°, ikkinchisi {lat2}° shimoliy kenglikda. Ular orasi taxminan necha km? Meridianning 1° yoyi taxminan 111 km.",
                  f"{km} km", [f"{v} km" for v in near(km, [dl * 100, dl, km + 111, (lat1 + lat2) * 111 // 10])], d=d,
                  x=f"Kengliklar farqi {lat2}° − {lat1}° = {dl}°, {dl} · 111 = {km} km."))
for peak, foot, d in [(1200, 700, 2), (3309, 1500, 3)]:
    rel = peak - foot
    _map.append(Q(f"Cho‘qqining mutlaq balandligi {num(peak)} m, tog‘ etagi {num(foot)} m balandlikda. Cho‘qqining nisbiy balandligi qancha?",
                  f"{num(rel)} m", [f"{num(v)} m" for v in near(rel, [peak + foot, peak, foot, rel + 100])], d=d,
                  x=f"Nisbiy balandlik — etakdan cho‘qqigacha: {num(peak)} − {num(foot)} = {num(rel)} m."))

T.topic("map_coords", "🗺️", L("Xarita, masshtab va geografik koordinatalar", "Maps, scale and coordinates", "Карта, масштаб и координаты"),
        chapter=C4,
        theory="Masshtab — xaritadagi masofa haqiqiy masofadan necha marta kichikligini ko‘rsatadi. Sonli masshtab 1 : 100 000 — xaritadagi 1 sm joyda 100 000 sm, ya’ni 1 km (nomli masshtab: “1 sm da 1 km”).\n"
               "• Parallellar — ekvatorga parallel aylanalar, meridianlar — qutbdan qutbga o‘tgan chiziqlar. Bosh meridian — Grinvich meridiani.\n"
               "• Geografik kenglik — ekvatordan shimol yoki janubga 0° dan 90° gacha; geografik uzoqlik — bosh meridiandan sharq yoki g‘arbga 0° dan 180° gacha.\n"
               "• Meridianning 1° yoyi taxminan 111 km. Toshkent taxminan 41° shimoliy kenglik va 69° sharqiy uzoqlikda.\n"
               "Mutlaq balandlik dengiz sathidan, nisbiy balandlik esa tog‘ etagidan hisoblanadi.",
        items=[
            Q("Ekvatorning geografik kengligi qancha?", "0°", ["90°", "45°", "180°"],
              x="Kenglik ekvatordan boshlab hisoblanadi."),
            Q("Shimoliy qutbning geografik kengligi qancha?", "90° shimoliy", ["0°", "180°", "45° shimoliy"],
              x="Kenglik qutbda eng katta — 90°."),
            Q("Geografik uzoqlik qaysi chiziqdan hisoblanadi?", "Bosh (Grinvich) meridiandan", ["Ekvatordan", "Qutb doirasidan", "Tropikdan"],
              x="Bosh meridian London yaqinidagi Grinvich rasadxonasidan o‘tadi."),
            Q("Qutbdan qutbga o‘tgan chiziqlar nima deyiladi?", "Meridianlar", ["Parallellar", "Gorizontallar", "Ekvatorlar"],
              x="Barcha meridianlar Shimoliy va Janubiy qutbda tutashadi."),
            Q("Ekvatorga parallel o‘tkazilgan aylanalar nima deyiladi?", "Parallellar", ["Meridianlar", "Masshtablar", "Azimutlar"],
              x="Parallellar kenglikni aniqlashga yordam beradi."),
            TF("Eng uzun parallel — ekvator.", True, x="Qutbga yaqinlashgan sari parallellar qisqarib boradi."),
            TF("Geografik kenglik 0° dan 180° gacha bo‘ladi.", False, x="Kenglik 0° dan 90° gacha, uzoqlik esa 0° dan 180° gacha."),
            TF("O‘zbekiston shimoliy kenglik va sharqiy uzoqlikda joylashgan.", True, x="Toshkent — taxminan 41° shimoliy kenglik, 69° sharqiy uzoqlik."),
            ORDER(S, "Meridianlar qutbdan qutbga o‘tadi"),
            Q("Qaysi masshtab kichik joyni batafsilroq ko‘rsatadi?", "1 : 10 000", ["1 : 1 000 000", "1 : 5 000 000", "1 : 100 000"], d=2,
              x="Ikkinchi son qancha kichik bo‘lsa, masshtab shuncha yirik va batafsil."),
            Q("Bir xil balandlikdagi nuqtalarni tutashtiruvchi chiziqlar nima deyiladi?", "Gorizontallar", ["Parallellar", "Meridianlar", "Masshtablar"], d=3,
              x="Gorizontallar xaritada relyefni ko‘rsatadi."),
            MATCH("Tushunchani ta’rifi bilan juftlang",
                  [("Kenglik", "ekvatordan uzoqlik, 0°–90°"), ("Uzoqlik", "bosh meridiandan uzoqlik, 0°–180°"), ("Parallel", "ekvatorga parallel aylana"),
                   ("Meridian", "qutbdan qutbga chiziq"), ("Masshtab", "kichraytirish darajasi"), ("Gorizontal", "teng balandliklar chizig‘i")], d=2,
                  x="Xarita bilan ishlash uchun bu tushunchalarni bilish kerak."),
        ] + _map)

_save = []
for per_min, minutes, days, d in [(6, 3, 1, 2), (6, 2, 30, 3)]:
    tot = per_min * minutes * days
    txt = f"{minutes} daqiqa tish yuvganda jo‘mrakni yopsak" + (f", {days} kunda" if days > 1 else "")
    _save.append(Q(f"Ochiq jo‘mrakdan daqiqasiga {per_min} l suv oqadi. {txt} necha litr suv tejaladi?", f"{num(tot)} l",
                   [f"{num(v)} l" for v in near(tot, [per_min + minutes, tot // 2, tot * 2, per_min * minutes, tot + per_min, tot - per_min])], d=d,
                   x=f"{per_min} · {minutes}" + (f" · {days}" if days > 1 else "") + f" = {num(tot)} l."))
for kwh, pct, d in [(300, 10, 2), (250, 20, 3)]:
    s = kwh * pct // 100
    assert s * 100 == kwh * pct
    _save.append(Q(f"Oila oyiga {kwh} kVt·soat elektr ishlatadi. Agar {pct} % tejasa, oyiga qancha elektr tejaladi?", f"{s} kVt·soat",
                   [f"{v} kVt·soat" for v in near(s, [pct, kwh - s, s * 2, kwh // pct])], d=d,
                   x=f"{kwh} · {pct} : 100 = {s} kVt·soat."))

T.topic("resources", "♻️", L("Tabiiy resurslar va ekologiya", "Natural resources and ecology", "Природные ресурсы и экология"),
        chapter=C4,
        theory="Tabiiy resurslar — inson foydalanadigan tabiat boyliklari.\n"
               "• Tugaydigan resurslar: tiklanadigan (o‘rmon, tuproq, chuchuk suv, hayvonlar) va tiklanmaydigan (neft, gaz, ko‘mir, rudalar).\n"
               "• Tugamaydigan resurslar: Quyosh va shamol energiyasi. Ulardan foydalanadigan elektr stansiyalari havoni tutun bilan ifloslamaydi.\n"
               "• Ekologik muammolar: havo va suv ifloslanishi, cho‘llanish, tuproq sho‘rlanishi, chiqindilar, karbonat angidrid ko‘payib issiqxona effekti kuchayishi.\n"
               "Ekologiya — organizmlarning o‘zaro va atrof-muhit bilan munosabatini o‘rganadigan fan (atamani E. Gekkel kiritgan).",
        items=[
            Q("Qaysi resurs tiklanmaydi?", "Neft", ["O‘rmon", "Quyosh nuri", "Shamol"],
              x="Neft millionlab yillarda hosil bo‘lgan, qazib olingani qayta tiklanmaydi."),
            Q("Qaysi resurs tugamaydigan hisoblanadi?", "Quyosh energiyasi", ["Ko‘mir", "Tabiiy gaz", "Temir rudasi"],
              x="Quyosh milliardlab yillar davomida nur sochadi."),
            Q("Qaysi elektr stansiyasi havoni tutun bilan ifloslamaydi?", "Quyosh elektr stansiyasi", ["Ko‘mirli issiqlik elektr stansiyasi", "Mazutli qozonxona", "Dizel generator"],
              x="Quyosh panellari yoqilg‘i yoqmaydi."),
            Q("Havoni asosan nima ifloslaydi?", "Transport va zavod chiqindilari", ["Daraxtlar", "Yomg‘ir", "Qushlar"],
              x="Avtomobil va zavod mo‘rilaridan zararli gazlar chiqadi."),
            Q("Ekologiya fani nimani o‘rganadi?", "Organizmlar va muhit munosabatini", ["Faqat tog‘ jinslarini", "Faqat yulduzlarni", "Faqat raqamlarni"],
              x="Ekologiya tirik organizmlarning bir-biri va atrof-muhit bilan aloqasini o‘rganadi."),
            Q("Qaysi resurs tiklanadigan?", "O‘rmon", ["Ko‘mir", "Neft", "Oltin"],
              x="Kesilgan o‘rmon o‘rniga yangi daraxt ekish mumkin."),
            TF("To‘g‘ri foydalanilsa, o‘rmon qayta tiklanishi mumkin.", True, x="Buning uchun kesilgan o‘rniga yangi daraxtlar ekiladi."),
            TF("Chiqindilarni qayta ishlash tabiiy resurslarni tejaydi.", True, x="Masalan, makulaturadan qog‘oz olinsa, kamroq daraxt kesiladi."),
            TF("Shamol energiyasi tugaydigan resurs.", False, x="Shamol doim esadi, u tugamaydigan resurs."),
            ORDER(S, "Quyosh energiyasi tugamaydigan resurs"),
            Q("Havoda karbonat angidrid ko‘payishi qanday hodisani kuchaytiradi?", "Issiqxona effekti", ["Zilzila", "Sunami", "Oy tutilishi"], d=2,
              x="Karbonat angidrid issiqlikni ushlab qolib, sayyorani isitadi."),
            Q("Noto‘g‘ri sug‘orish natijasida tuproqda tuz to‘planishi nima deyiladi?", "Sho‘rlanish", ["Eroziya", "Nurash", "Changlanish"], d=2,
              x="Sho‘rlangan tuproqda ekinlar yomon o‘sadi."),
            Q("Unumdor yerlarning cho‘lga aylanishi nima deyiladi?", "Cho‘llanish", ["Sho‘rlanish", "Konveksiya", "Kondensatsiya"], d=2,
              x="Daraxt kesish va ortiqcha mol boqish cho‘llanishni tezlashtiradi."),
            Q("Tuproqning suv va shamol ta’sirida yuvilib-uchib ketishi nima?", "Eroziya", ["Sho‘rlanish", "Fotosintez", "Diffuziya"], d=3,
              x="Daraxtzorlar va o‘t qoplami tuproqni eroziyadan saqlaydi."),
            Q("“Ekologiya” atamasini fanga kim kiritgan?", "Ernst Gekkel", ["Karl Linney", "Charlz Darvin", "D. I. Mendeleyev"], d=3,
              x="Nemis olimi Ernst Gekkel 1866-yilda bu atamani taklif qilgan."),
            MATCH("Resursni turi bilan juftlang",
                  [("Ko‘mir", "tiklanmaydigan"), ("O‘rmon", "tiklanadigan"), ("Quyosh nuri", "tugamaydigan"), ("Temir rudasi", "qazilma boylik"),
                   ("Chuchuk suv", "cheklangan, tejash kerak")], d=2,
                  x="Resurslardan oqilona foydalanish kelajak avlodlar uchun muhim."),
        ] + _save)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["earth_crust", "weather_climate", "map_coords", "resources"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["motion", "density", "pressure", "heat_transfer", "light", "sound", "atoms", "substances",
        "classification", "plant_organs", "animals", "earth_crust", "weather_climate", "map_coords", "resources"],
       chapter=C4, level=3)


def spoken(q):
    """Ovoz uchun: dvigatel o'qimaydigan qisqartmalarni so'z bilan yozamiz (ekrandagi matn o'zgarmaydi)."""
    import re
    out = q.replace("km/soat", "kilometr soatiga").replace("km/s", "kilometr sekundiga").replace("m/s", "metr sekundiga").replace("g/sm³", "gramm kub santimetrga")
    out = out.replace("kVt·soat", "kilovatt soat").replace("kPa", "kilopaskal").replace("masshtabi 1 : ", "masshtabi birga ")
    out = out.replace("Masshtab 1 : ", "Masshtab birga ").replace("1 : ", "birga ")
    out = re.sub(r"(\d) Pa\b", r"\1 paskal", out)
    out = re.sub(r"(\d) N\b", r"\1 nyuton", out)
    out = re.sub(r"(\d) Hz\b", r"\1 gers", out)
    return out


for _it in T.items:
    if _it["t"] == "choice" and "say" not in _it and spoken(_it["q"]) != _it["q"]:
        _it["say"] = spoken(_it["q"])

T.write()
