"""Tarix, 6-sinf (Qadimgi dunyo tarixi): ibtidoiy jamiyat, Qadimgi Sharq, Yunoniston va Rim, O‘rta Osiyoning qadimgi davlatlari.

Faqat umumqabul qilingan, darsliklarda keltiriladigan faktlar ishlatilgan; matnlar o‘zimizniki.
5-sinf savollari takrorlanmaydi: mavzular chuqurroq va boshqa tomondan yoritiladi.
Qayta yaratish: python3 tool/content/school/history_g6.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403

rnd = random.Random(606)
T = Course("history", 6, L("Tarix", "History", "История"))

C1 = "1-chorak. Ibtidoiy jamiyat"
C2 = "2-chorak. Qadimgi Sharq davlatlari"
C3 = "3-chorak. Qadimgi Yunoniston va Rim"
C4 = "4-chorak. O‘rta Osiyo qadimgi davrda"

# ============================================================ 1-chorak
items = [
    Q("Tosh davrining eng qadimgi bosqichi qanday ataladi?", "Paleolit (qadimgi tosh davri)", ["Neolit (yangi tosh davri)", "Mezolit (o‘rta tosh davri)", "Bronza davri"],
      x="Tosh davri: paleolit → mezolit → neolit."),
    Q("“Yangi tosh davri” qanday ataladi?", "Neolit", ["Paleolit", "Mezolit", "Eneolit"], x="Neolit — tosh davrining oxirgi bosqichi."),
    Q("O‘rta tosh davri (mezolit)da qanday muhim qurol keng tarqalgan?", "Kamon va o‘q", ["Temir qilich", "Porox", "Kompas"], d=2,
      x="Kamon uzoqdan ov qilish imkonini berdi."),
    Q("Neolit davrida odamlar nimani o‘rgandi?", "Sopol idish yasash va to‘quvchilikni", ["Temir eritishni", "Qog‘oz tayyorlashni", "Tanga zarb qilishni"], d=2,
      x="Neolitda kulolchilik va to‘quvchilik paydo bo‘ldi."),
    Q("Odam qo‘lga o‘rgatgan ilk hayvon qaysi deb hisoblanadi?", "It", ["Ot", "Tuya", "Mushuk"], d=2, x="It ovda va qo‘riqlashda odamga yordamchi bo‘lgan."),
    Q("Qadimgi dehqonlar dastlab qaysi ekinlarni ekishgan?", "Bug‘doy va arpa", ["Kartoshka va makkajo‘xori", "Paxta va choy", "Kofe va kakao"], d=2,
      x="Bug‘doy va arpa — eng qadimgi madaniy ekinlar."),
    Q("Dehqonchilik va chorvachilikka o‘tish tarixda qanday ataladi?", "Neolit inqilobi", ["Sanoat inqilobi", "Olimpiya o‘yinlari", "Buyuk ipak yo‘li"], d=3,
      x="Bu o‘zgarish odamlar hayotini tubdan o‘zgartirgani uchun “inqilob” deyiladi."),
    Q("Dehqonchilik paydo bo‘lgach, odamlar qanday hayotga o‘tdi?", "O‘troq hayotga", ["Faqat ko‘chmanchilikka", "G‘orlarga qaytishga", "Dengizda yashashga"],
      x="Ekin ekkan odamlar bir joyda uy qurib yashay boshladi."),
    Q("Ibtidoiy odamlar olovni qanday hosil qilishgan?", "Yog‘ochni ishqalab yoki toshni urib", ["Gugurt chaqib", "Zajigalka bilan", "Elektr orqali"],
      x="Ishqalanish yoki uchqun olov chiqargan."),
    Q("Qadimgi odamlarning manzilgohi arxeologiyada qanday ataladi?", "Makon", ["Saroy", "Qal’a", "Bozor"], d=2, x="Makonlarda qurollar, suyaklar, gulxan izlari topiladi."),
    Q("Toshkent viloyatidagi paleolit davri g‘ori qaysi?", "Obirahmat", ["Afrosiyob", "Tuproqqal’a", "Kolizey"], d=3, x="Obirahmat g‘orida qadimgi odamlar yashagan."),
    Q("Xorazmdagi neolit davri ovchi va baliqchilari madaniyati qanday ataladi?", "Kaltaminor madaniyati", ["Afrosiyob madaniyati", "Misr madaniyati", "Rim madaniyati"],
      d=3, x="Kaltaminor madaniyati Amudaryo quyi oqimida tarqalgan."),
    Q("Qon-qarindosh kishilarning birgalikda yashovchi jamoasi nima deyiladi?", "Urug‘", ["Davlat", "Imperiya", "Respublika"], x="Urug‘ a’zolari umumiy ajdoddan tarqalgan."),
    Q("Bir necha urug‘ birlashuvidan nima hosil bo‘lgan?", "Qabila", ["Imperiya", "Shahar-davlat", "Respublika"], d=2, x="Qabila — urug‘lar birlashmasi."),
    Q("Neolit tosh qurollari oldingilaridan nimasi bilan farq qiladi?", "Silliqlangan va teshilgan", ["Temirdan yasalgan", "Plastmassadan qilingan", "Oltin bilan qoplangan"],
      d=3, x="Neolitda toshni silliqlash va teshish o‘rganildi."),
    TF("Kamon va o‘q mezolit davrida keng tarqalgan.", True, d=2, x="Kamon — mezolitning muhim ixtirosi."),
    TF("Neolit — tosh davrining eng qadimgi bosqichi.", False, x="Eng qadimgisi — paleolit, neolit esa oxirgi bosqich."),
    TF("Sopol idishlar ovqat pishirish va don saqlashni osonlashtirdi.", True, x="Kulolchilik neolitda paydo bo‘ldi."),
    ORDER("Tosh davri bosqichlarini tartib bilan joylang", "Paleolit → Mezolit → Neolit", sep=" → ", d=1, x="Qadimgi → o‘rta → yangi tosh davri."),
    MATCH("Bosqich yoki yodgorlikni belgisi bilan juftlang", [("Paleolit", "olovdan foydalanish"), ("Mezolit", "kamon va o‘q"), ("Neolit", "dehqonchilik va kulolchilik"),
                                                             ("Obirahmat", "paleolit makoni"), ("Kaltaminor", "Xorazm neolit madaniyati")], d=2),
]
T.topic("prehistory", "🏹", L("Tosh davri bosqichlari", "Stages of the Stone Age", "Этапы каменного века"), C1,
        "Tosh davri uch bosqichga bo‘linadi:\n"
        "• Paleolit (qadimgi tosh davri) — tosh qurollar, olovdan foydalanish, ovchilik va termachilik; odamlar g‘or va makonlarda yashagan\n"
        "  (Obirahmat g‘ori — Toshkent viloyati).\n"
        "• Mezolit (o‘rta tosh davri) — kamon va o‘q keng tarqaldi, it qo‘lga o‘rgatildi.\n"
        "• Neolit (yangi tosh davri) — silliqlangan qurollar, kulolchilik, to‘quvchilik; dehqonchilik (bug‘doy, arpa) va chorvachilik paydo bo‘ldi\n"
        "  (“neolit inqilobi”), odamlar o‘troq hayotga o‘tdi. Xorazmda — Kaltaminor madaniyati.\n"
        "• Jamiyat: urug‘ (qon-qarindoshlar jamoasi) → qabila (urug‘lar birlashmasi).", items=items)

items = [
    Q("Odamlar ilk bor keng o‘zlashtirgan metall qaysi?", "Mis", ["Temir", "Alyuminiy", "Po‘lat"], x="Mis yumshoq bo‘lib, oson ishlov berilgan."),
    Q("Bronza qaysi metallar qotishmasi?", "Mis va qalay", ["Temir va oltin", "Kumush va temir", "Alyuminiy va mis"], x="Bronza misdan qattiqroq."),
    Q("Mis va tosh qurollar birga ishlatilgan davr qanday ataladi?", "Eneolit (mis-tosh davri)", ["Paleolit", "Mezolit", "Neolit"], d=2,
      x="Eneolit — tosh davridan metall davriga o‘tish bosqichi."),
    Q("Temir qurollarning bronzadan afzalligi nimada?", "Mustahkam va ko‘p uchraydi", ["Juda yumshoq", "Yaltiroq bo‘ladi", "Suvda eriydi"], d=2,
      x="Temir rudasi tabiatda ko‘p, qurollari esa mustahkam."),
    Q("Kulolchilik charxi nima uchun kerak bo‘lgan?", "Sopol idishlarni tez va tekis yasash uchun", ["Don yanchish uchun", "Suv tortish uchun", "Mato to‘qish uchun"],
      x="Charx aylanib, idishni tekis shakllantirishga yordam beradi."),
    Q("Hunarmandchilik alohida kasbga aylangach, nima rivojlandi?", "Ayirboshlash va savdo", ["Ovchilikka qaytish", "Olovdan voz kechish", "Termachilik"], d=2,
      x="Hunarmand buyumini dehqon mahsulotiga almashtirgan."),
    Q("Surxondaryodagi bronza davri manzilgohi qaysi?", "Sopollitepa", ["Obirahmat", "Afrosiyob", "Tuproqqal’a"], d=2, x="Sopollitepa — Sherobod tumanidagi yodgorlik."),
    Q("Farg‘ona vodiysidagi qadimgi dehqonlar madaniyati qanday ataladi?", "Chust madaniyati", ["Kaltaminor madaniyati", "Rim madaniyati", "Misr madaniyati"], d=3,
      x="Chust madaniyati bronza va ilk temir davriga oid."),
    Q("Jarqo‘ton qanday yodgorlik?", "Bronza davri qadimgi shahri", ["Paleolit g‘ori", "Rim amfiteatri", "Misr piramidasi"], d=3,
      x="Jarqo‘ton — Surxondaryodagi ilk shahar xarobalari."),
    Q("Davlatning asosiy belgilari qaysilar?", "Hukmdor, qo‘shin, soliq va qonunlar", ["Faqat g‘orlar", "Faqat ov qurollari", "Faqat olov"],
      x="Davlat hudud va aholini boshqaradi, soliq yig‘adi, qonun chiqaradi."),
    Q("Ilk davlatlar asosan qanday joylarda paydo bo‘lgan?", "Katta daryolar vodiylarida", ["Qutb muzliklarida", "Baland tog‘ cho‘qqilarida", "Okean orollarida"],
      x="Nil, Dajla va Frot, Hind, Xuanxe bo‘ylarida."),
    Q("Nima uchun ilk davlatlar daryo bo‘ylarida vujudga kelgan?", "Sug‘orish uchun suv va unumdor yer bo‘lgan", ["Daryoda oltin ko‘p bo‘lgan", "U yerda tog‘lar yo‘q edi",
                                                                                                           "U yerda qish bo‘lmagan"], d=2,
      x="Sug‘orma dehqonchilik ko‘p hosil bergan."),
    Q("Yozuvning paydo bo‘lishi nimaga yordam berdi?", "Bilim va qonunlarni saqlashga", ["Ovchilikni to‘xtatishga", "Olovni o‘chirishga", "Daryolarni quritishga"],
      x="Yozuv orqali bilimlar avlodlarga yetib keldi."),
    Q("Mulkiy tengsizlik paydo bo‘lishiga nima sabab bo‘lgan?", "Ortiqcha mahsulot to‘planishi", ["Olovning ixtiro qilinishi", "G‘orlarda yashash", "Termachilik"], d=3,
      x="Kimdir ko‘proq mahsulot va mulk to‘plab, boyib borgan."),
    TF("Bronza temirdan oldin o‘zlashtirilgan.", True, x="Tartib: mis → bronza → temir."),
    TF("Bronza — temir va oltin qotishmasi.", False, x="Bronza — mis va qalay qotishmasi."),
    TF("G‘ildirak ixtirosi yuk tashishni ancha osonlashtirdi.", True, x="G‘ildirakli aravalar paydo bo‘ldi."),
    ORDER("Davrlarni tartib bilan joylang", "Tosh davri → Mis-tosh davri → Bronza davri → Temir davri", sep=" → ", d=2, x="Metall davrlari tosh davridan keyin keladi."),
    MATCH("Davr yoki yodgorlikni belgisi bilan juftlang", [("Bronza davri", "mis va qalay qotishmasi"), ("Temir davri", "mustahkam temir qurollar"),
                                                          ("Eneolit", "mis va tosh qurollar birga"), ("Sopollitepa", "Surxondaryodagi bronza davri manzilgohi"),
                                                          ("Chust madaniyati", "Farg‘ona vodiysi dehqonlari")], d=2),
]
T.topic("metals", "⚒️", L("Metall davri va ilk davlatlar", "The Metal Age and early states", "Век металлов и первые государства"), C1,
        "Neolitdan keyin metall davri boshlandi:\n"
        "• Eneolit (mis-tosh davri) → bronza davri (bronza — mis va qalay qotishmasi) → temir davri.\n"
        "• Kulolchilik charxi, g‘ildirak ixtiro qilindi; hunarmandchilik alohida kasbga aylanib, ayirboshlash rivojlandi.\n"
        "• Ortiqcha mahsulot mulkiy tengsizlikni keltirib chiqardi; ilk shaharlar va davlatlar katta daryolar vodiylarida paydo bo‘ldi.\n"
        "• Vatanimizda: Sopollitepa va Jarqo‘ton (Surxondaryo), Chust madaniyati (Farg‘ona vodiysi).", items=items)

items = []
for year, d in [(776, 1), (509, 1), (490, 1), (753, 1), (44, 1), (221, 2), (330, 2), (1750, 2), (100, 3), (101, 3)]:
    c = (year - 1) // 100 + 1
    wrong = [f"mil. avv. {k}-asr" for k in (c - 1, c + 1, c + 2) if k > 0] + [f"milodiy {c}-asr"]
    items.append(Q(f"Miloddan avvalgi {year}-yil nechanchi asrga kiradi?", f"mil. avv. {c}-asr", wrong, d=d,
                   x=f"Mil. avv. {c}-asr — mil. avv. {c * 100}–{(c - 1) * 100 + 1}-yillar."))
DIFFS = [
    ("Miloddan avvalgi 1000-yildan miloddan avvalgi 600-yilgacha necha yil o‘tgan?", 1000, 600, 1),
    ("Miloddan avvalgi 2500-yildan miloddan avvalgi 2000-yilgacha necha yil o‘tgan?", 2500, 2000, 1),
    ("Rivoyatga ko‘ra Rim mil. avv. 753-yilda tashkil topgan, respublika esa mil. avv. 509-yilda o‘rnatilgan. Oradan necha yil o‘tgan?", 753, 509, 2),
    ("Birinchi Olimpiya o‘yinlari mil. avv. 776-yilda, Marafon jangi mil. avv. 490-yilda bo‘lgan. Oradan necha yil o‘tgan?", 776, 490, 2),
    ("Aleksandr Makedonskiy mil. avv. 334-yilda yurish boshlab, mil. avv. 323-yilda vafot etgan. Oradan necha yil o‘tgan?", 334, 323, 2),
    ("Ahamoniylar davlati mil. avv. 550-yilda tashkil topib, mil. avv. 330-yilda qulagan. Davlat necha yil mavjud bo‘lgan?", 550, 330, 3),
]
for q, a, b, d in DIFFS:
    diff = a - b
    wrong = [str(a + b), str(diff + 10), str(diff - 10) if diff > 10 else str(diff + 100)]
    items.append(Q(q, str(diff), wrong, d=d, x=f"Ikkala sana ham miloddan avvalgi, shuning uchun ayiramiz: {a} − {b} = {diff}."))
items += [
    Q("Miloddan avvalgi 2500-yil nechanchi ming yillikka kiradi?", "mil. avv. 3-ming yillik", ["mil. avv. 2-ming yillik", "mil. avv. 25-ming yillik", "milodiy 3-ming yillik"],
      d=2, x="Mil. avv. 3-ming yillik — mil. avv. 3000–2001-yillar."),
    Q("Miloddan avvalgi 1200-yil nechanchi ming yillikka kiradi?", "mil. avv. 2-ming yillik", ["mil. avv. 1-ming yillik", "mil. avv. 12-ming yillik", "milodiy 2-ming yillik"],
      d=3, x="Mil. avv. 2-ming yillik — mil. avv. 2000–1001-yillar."),
    Q("Miloddan avvalgi yillar qanday tartibda sanaladi?", "Kattadan kichikka qarab kamayadi", ["Kichikdan kattaga qarab ortadi", "Tasodifiy tartibda", "Faqat yuzliklar bilan"],
      x="Masalan: mil. avv. 776, 775, 774 … 2, 1."),
    Q("Qaysi sana eng qadimiy?", "mil. avv. 753-yil", ["mil. avv. 509-yil", "mil. avv. 44-yil", "milodiy 476-yil"], x="Mil. avv. sanalarda son qancha katta bo‘lsa, shuncha qadimiy."),
    Q("Qaysi sana bizga eng yaqin?", "milodiy 79-yil", ["mil. avv. 44-yil", "mil. avv. 221-yil", "mil. avv. 490-yil"], d=2, x="Milodiy sana har qanday mil. avv. sanadan keyin keladi."),
    TF("Yillar hisobida nolinchi yil yo‘q: mil. avv. 1-yildan keyin milodiy 1-yil keladi.", True, d=3, x="Shuning uchun milod chegarasida “0-yil” bo‘lmaydi."),
    TF("Mil. avv. 490-yil mil. avv. 776-yildan oldin bo‘lgan.", False, x="Mil. avv. sanalarda katta son qadimiyroq: avval 776, keyin 490."),
    ORDER("Sanalarni qadimiydan yangisiga tartiblang", "mil. avv. 776 → mil. avv. 490 → mil. avv. 44 → milodiy 476", sep=" → ", d=2,
          x="Avval mil. avv. sanalar kamayib boradi, keyin milodiy sanalar keladi."),
    MATCH("Sanani asri bilan juftlang", [("mil. avv. 776-yil", "mil. avv. 8-asr"), ("mil. avv. 490-yil", "mil. avv. 5-asr"), ("mil. avv. 221-yil", "mil. avv. 3-asr"),
                                        ("mil. avv. 44-yil", "mil. avv. 1-asr"), ("milodiy 476-yil", "milodiy 5-asr")], d=2),
]
T.topic("time_bc", "⏳", L("Miloddan avvalgi sanalar", "Dates before Christ", "Даты до нашей эры"), C1,
        "Milod boshlanishidan oldingi yillar “miloddan avvalgi” (mil. avv.) deyiladi va teskari tartibda sanaladi: 776, 775, … 2, 1.\n"
        "• Nolinchi yil yo‘q: mil. avv. 1-yildan keyin milodiy 1-yil keladi.\n"
        "• Mil. avv. asr: 1-asr — mil. avv. 100–1-yillar, 8-asr — mil. avv. 800–701-yillar (776 → 8-asr).\n"
        "• Ikki mil. avv. sana orasidagi farq ayirish bilan topiladi: mil. avv. 776 dan mil. avv. 490 gacha 776 − 490 = 286 yil.", items=items)

T.topic("centuries", "📅", L("Asr va yil (mashq)", "Years and centuries (practice)", "Год и век (практика)"), C1,
        "Milodiy asrni topish uchun yildagi yuzliklar soniga 1 qo‘shiladi: 1441 → 14 + 1 = 15-asr. "
        "Yuzlikning oxirgi yili (100, 1900, 2000) o‘sha asrning oxirgi yili: 2000-yil — 20-asr, 2001-yildan 21-asr boshlangan.",
        gen="timeline", levels=[dict(mode=m) for m in ("choice", "mixed", "input")])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["prehistory", "metals", "time_bc"], C1)

# ============================================================ 2-chorak
items = [
    Q("Qadimgi yunon tarixchisi Gerodot Misrni nima deb atagan?", "Nil in’omi", ["Quyosh o‘lkasi", "Qumlar podsholigi", "Tog‘lar yurti"], d=2,
      x="Misr hayoti butunlay Nil daryosiga bog‘liq bo‘lgan."),
    Q("Nil daryosi har yili dehqonlarga qanday foyda keltirgan?", "Toshib, dalalarga unumdor loyqa qoldirgan", ["Muzlab qolgan", "Butunlay qurib qolgan", "Sho‘r suvga aylangan"],
      x="Toshqindan keyin yer serhosil bo‘lgan."),
    Q("Yuqori va Quyi Misr taxminan qachon yagona davlatga birlashgan?", "Mil. avv. 3000-yillar atrofida", ["Milodiy 1000-yilda", "Mil. avv. 100-yilda", "Milodiy 1991-yilda"],
      d=2, x="Misr dunyodagi eng qadimgi davlatlardan biri."),
    Q("Misrliklarning quyosh xudosi qanday atalgan?", "Ra", ["Zevs", "Yupiter", "Axura Mazda"], d=2, x="Misrliklar Ra ni eng ulug‘ xudo deb bilgan."),
    Q("Giza yaqinidagi sher tanli, odam boshli ulkan haykal nima deb ataladi?", "Sfinks", ["Kolizey", "Zikkurat", "Obelisk"], x="Sfinks piramidalar yonida joylashgan."),
    Q("Misrliklar marhumlar jasadini uzoq saqlash uchun nima qilishgan?", "Mumiyolashgan", ["Yoqishgan", "Muzlatishgan", "Daryoga tashlashgan"], d=2,
      x="Maxsus moddalar bilan ishlov berib, mumiyo tayyorlangan."),
    Q("Misr iyerogliflarini birinchi bo‘lib o‘qigan olim kim?", "Fransua Shampolyon", ["Gerodot", "Xammurapi", "Aristotel"], d=3, x="Shampolyon 1822-yilda iyerogliflarni o‘qigan."),
    Q("Iyerogliflarni o‘qishga kalit bo‘lgan tosh qanday nomlanadi?", "Rozetta toshi", ["Qora tosh", "Oltin tosh", "Bobil toshi"], d=3,
      x="Toshda bitta matn uch xil yozuvda, jumladan yunoncha ham yozilgan."),
    Q("Misrliklar yaratgan quyosh kalendarida yil necha kundan iborat bo‘lgan?", "365 kun", ["100 kun", "300 kun", "400 kun"], d=2, x="12 oy × 30 kun + 5 kun = 365 kun."),
    Q("Piramidalarni asosan kimlar qurgan?", "Minglab dehqonlar va hunarmandlar", ["Faqat fir’avnning o‘zi", "Chet ellik sayyohlar", "Rim askarlari"], d=2,
      x="Qurilishda ko‘p ming kishi yillar davomida ishlagan."),
    Q("Maqbarasi 1922-yilda deyarli buzilmagan holda topilgan yosh fir’avn kim?", "Tutanxamon", ["Xeops", "Xammurapi", "Kir II"], d=3,
      x="Tutanxamon maqbarasidan son-sanoqsiz boyliklar topilgan."),
    Q("Misr dehqonlari dalalarni qanday sug‘organ?", "Kanallar va to‘g‘onlar orqali", ["Quvur va nasoslar bilan", "Faqat yomg‘ir suvi bilan", "Qor suvi bilan"],
      x="Nil suvi kanallar orqali dalalarga yetkazilgan."),
    Q("Misrda yozuvni biladigan va hisob-kitob yurituvchi amaldorlar kim edi?", "Kotiblar", ["Gladiatorlar", "Baxshilar", "Legionerlar"], x="Kotiblik hurmatli kasb bo‘lgan."),
    Q("Qadimgi Misrda qaysi fanlar rivojlangan?", "Matematika, astronomiya, tibbiyot", ["Kompyuter va robototexnika", "Kosmonavtika", "Atom fizikasi"],
      x="Toshqin vaqtini hisoblash, yer o‘lchash, davolash zarurati fanlarni rivojlantirgan."),
    Q("Dunyoning yetti mo‘jizasidan qaysi biri bizgacha saqlangan?", "Misr piramidalari", ["Bobil osma bog‘lari", "Zevs haykali", "Iskandariya mayog‘i"], d=3,
      x="Yetti mo‘jizadan faqat Giza piramidalari saqlanib qolgan."),
    TF("Misrliklar yilni 365 kunga bo‘lishgan.", True, x="Bu quyosh kalendari edi."),
    TF("Sfinks — Rimdagi amfiteatr.", False, x="Sfinks — Misrdagi haykal; Rimdagi amfiteatr — Kolizey."),
    TF("Rozetta toshidagi yozuvlar iyerogliflarni o‘qishga yordam bergan.", True, d=2, x="Yunoncha matn bilan solishtirish orqali."),
    MATCH("Tushunchani ma’nosi bilan juftlang", [("fir’avn", "Misr hukmdori"), ("Sfinks", "sher tanli haykal"), ("papirus", "yozuv materiali"),
                                                ("kotib", "yozuvni biluvchi amaldor"), ("Ra", "quyosh xudosi"), ("Rozetta toshi", "iyerogliflar kaliti")], d=2),
    ORDER("So‘zlardan gap tuzing", "Nil daryosi Misrga hayot baxsh etgan", d=1, x="Gerodot Misrni “Nil in’omi” deb atagan."),
]
T.topic("egypt", "🔺", L("Qadimgi Misr", "Ancient Egypt", "Древний Египет"), C2,
        "Qadimgi Misr — Nil vodiysida. Gerodot Misrni “Nil in’omi” deb atagan: har yili Nil toshib, dalalarga unumdor loyqa qoldirgan.\n"
        "• Yuqori va Quyi Misr mil. avv. 3000-yillar atrofida birlashgan. Hukmdor — fir’avn, amaldorlar — kotiblar.\n"
        "• Giza piramidalari va Sfinks; piramidalar — yetti mo‘jizadan bizgacha saqlangan yagonasi. Tutanxamon maqbarasi 1922-yilda topilgan.\n"
        "• Misrliklar 365 kunlik quyosh kalendarini yaratgan; matematika, astronomiya, tibbiyot rivojlangan.\n"
        "• Iyerogliflarni 1822-yilda Fransua Shampolyon Rozetta toshi yordamida o‘qigan.", items=items)

items = [
    Q("Mesopotamiyada ilk shahar-davlatlarni barpo etgan xalq kim?", "Shumerlar", ["Rimliklar", "Spartaliklar", "Finikiyaliklar"], x="Shumerlar — Mesopotamiyaning eng qadimgi aholisi."),
    Q("Shumerlarning qadimgi shahar-davlatlaridan biri qaysi?", "Ur", ["Afina", "Rim", "Memfis"], d=2, x="Ur va Uruk — shumer shaharlari."),
    Q("Mesopotamiyadagi pog‘onali ibodatxona-minora qanday ataladi?", "Zikkurat", ["Piramida", "Kolizey", "Parfenon"], x="Zikkuratlar xom g‘ishtdan qurilgan."),
    Q("Qaysi muhim ixtiro shumerlarga nisbat beriladi?", "G‘ildirak", ["Qog‘oz", "Porox", "Kompas"], d=2, x="Qog‘oz, porox va kompas — Xitoy ixtirolari."),
    Q("Soatning 60 daqiqaga bo‘linishi qaysi xalqlar sanoq tizimidan kelib chiqqan?", "Shumer va bobilliklar", ["Rimliklar", "Xitoyliklar", "Misrliklar"], d=3,
      x="Ular 60 lik sanoq tizimidan foydalangan."),
    Q("Xammurapi qonunlari nimaga o‘yib yozilgan?", "Tosh ustunga", ["Papirusga", "Ipak matoga", "Yog‘och taxtaga"], d=2, x="Qonunlar baland tosh ustunga mixxatda o‘yilgan."),
    Q("Xammurapi qaysi asrda hukmronlik qilgan?", "Mil. avv. XVIII asrda", ["Milodiy XV asrda", "Mil. avv. I asrda", "Milodiy XX asrda"], d=3,
      x="Xammurapi — mil. avv. XVIII asrda yashagan Bobil podshosi."),
    Q("Yetti mo‘jizadan biri bo‘lgan osma bog‘lar qaysi shaharda bo‘lgan?", "Bobil", ["Afina", "Rim", "Memfis"], x="Bobil osma bog‘lari dunyoning yetti mo‘jizasidan biri."),
    Q("Bobil shahri qaysi daryo bo‘yida joylashgan?", "Frot", ["Nil", "Tibr", "Gang"], x="Bobil Frot daryosi bo‘yida qurilgan."),
    Q("Ossuriya podshosi Ashshurbanipal nimasi bilan mashhur?", "Loy taxtachali katta kutubxonasi bilan", ["Piramida qurgani bilan", "Olimpiya o‘yinlarini boshlagani bilan",
                                                                                                          "Qog‘oz ixtiro qilgani bilan"], d=3,
      x="Kutubxonada minglab loy taxtachalar saqlangan."),
    Q("Ilk harfli alifboni yaratgan xalq kim?", "Finikiyaliklar", ["Misrliklar", "Shumerlar", "Xitoyliklar"], d=2, x="Finikiya alifbosi ko‘plab alifbolarga asos bo‘lgan."),
    Q("Finikiyaliklar qanday kasb bilan mashhur edi?", "Dengizchilik va savdo", ["Faqat chorvachilik", "Piramida qurish", "Ipak to‘qish"], x="Ular O‘rta yer dengizida suzgan."),
    Q("Finikiya alifbosi nechta harfdan iborat bo‘lgan?", "22 ta", ["5 ta", "33 ta", "100 ta"], d=3, x="22 ta harf, faqat undosh tovushlar uchun."),
    Q("Qadimgi Forsda Ahamoniylar davlatiga kim asos solgan?", "Kir II", ["Xammurapi", "Yuliy Sezar", "Tutanxamon"], d=2, x="Kir II mil. avv. 550-yilda davlatga asos solgan."),
    Q("Ahamoniylar podshosi Doro I qurdirgan uzun yo‘l qanday ataladi?", "Shoh yo‘li", ["Ipak yo‘li", "Appiy yo‘li", "Temir yo‘l"], d=3,
      x="Shoh yo‘li davlatning uzoq viloyatlarini bog‘lagan."),
    Q("Mixxat belgilari qanday shaklda bo‘lgan?", "Mixga o‘xshash chiziqchalar", ["Hayvon rasmlari", "Doiracha va nuqtalar", "Lotin harflari"],
      x="Belgilar ho‘l loyga uchli tayoqcha bilan bosilgan."),
    TF("Zikkurat — Mesopotamiyadagi pog‘onali ibodatxona.", True, x="Zikkurat tepasida ibodatxona joylashgan."),
    TF("Xammurapi qonunlari papirusga yozilgan.", False, x="Ular tosh ustunga o‘yib yozilgan."),
    TF("Finikiya alifbosi keyinchalik yunon va lotin alifbolariga asos bo‘lgan.", True, d=2, x="Yunonlar unga unli harflarni qo‘shgan."),
    MATCH("Xalq yoki shaxsni yutug‘i bilan juftlang", [("shumerlar", "g‘ildirak va mixxat"), ("Xammurapi", "qonunlar to‘plami"), ("finikiyaliklar", "ilk harfli alifbo"),
                                                      ("Ashshurbanipal", "loy taxtachali kutubxona"), ("Kir II", "Ahamoniylar davlati"), ("Doro I", "Shoh yo‘li")], d=2),
]
T.topic("mesopotamia", "🏺", L("Mesopotamiya va Old Osiyo", "Mesopotamia and the Near East", "Месопотамия и Передняя Азия"), C2,
        "• Mesopotamiya (Dajla va Frot oralig‘i) — shumerlar vatani: ilk shahar-davlatlar (Ur, Uruk), zikkuratlar, mixxat, g‘ildirak;\n"
        "  60 lik sanoq (soatda 60 daqiqa).\n"
        "• Bobil (Frot bo‘yida) podshosi Xammurapi (mil. avv. XVIII asr) qonunlari tosh ustunga o‘yib yozilgan. Bobil osma bog‘lari — yetti mo‘jizadan biri.\n"
        "• Ossuriya podshosi Ashshurbanipal loy taxtachalardan iborat kutubxona to‘plagan.\n"
        "• Finikiyaliklar — dengizchi va savdogarlar; 22 harfli alifboni yaratgan.\n"
        "• Fors Ahamoniylar davlatiga mil. avv. 550-yilda Kir II asos solgan; Doro I “Shoh yo‘li”ni qurdirgan.", items=items)

items = [
    Q("Hind vodiysidagi qadimgi shaharlardan biri qaysi?", "Moxenjo-Daro", ["Ur", "Memfis", "Afina"], x="Xarappa va Moxenjo-Daro — Hind vodiysi shaharlari."),
    Q("Xarappa va Moxenjo-Daro shaharlari nimasi bilan hayratlanarli?", "To‘g‘ri ko‘chalari va kanalizatsiyasi", ["Piramidalari", "Kolizeyi", "Buyuk devori"], d=3,
      x="Shaharlar puxta reja asosida qurilgan."),
    Q("Qadimgi Hindistonda jamiyat nechta varnaga bo‘lingan?", "4 ta", ["2 ta", "7 ta", "10 ta"], d=2, x="Varna — jamiyatdagi tabaqa."),
    Q("Qaysi o‘yin qadimgi Hindistonda paydo bo‘lgan deb hisoblanadi?", "Shaxmat", ["Futbol", "Tennis", "Basketbol"], x="Shaxmatning qadimgi shakli Hindistonda paydo bo‘lgan."),
    Q("Hind matematiklari qaysi muhim tushunchani ishlab chiqqan?", "Nol va o‘nli sanoq", ["Rim raqamlari", "Mixxat", "Iyeroglif"], d=2, x="Bugungi raqamlarimiz hind raqamlaridan kelib chiqqan."),
    Q("Hindistondagi Maurya davlatining mashhur podshosi kim?", "Ashoka", ["Xammurapi", "Kir II", "Yuliy Sezar"], d=3, x="Ashoka — Maurya davlatining qudratli hukmdori."),
    Q("Xitoyni birinchi marta birlashtirgan imperator kim?", "Sin Shixuandi", ["Konfutsiy", "Ashoka", "Xammurapi"], d=2, x="U o‘zini “birinchi imperator” deb e’lon qilgan."),
    Q("Xitoy qachon Sin Shixuandi tomonidan birlashtirilgan?", "Mil. avv. 221-yilda", ["Milodiy 1911-yilda", "Mil. avv. 1000-yilda", "Milodiy 500-yilda"], d=3,
      x="Mil. avv. 221-yilda yagona Xitoy imperiyasi tuzilgan."),
    Q("Sin Shixuandi maqbarasi yonidan topilgan minglab haykallar qanday ataladi?", "Sopol (terrakota) qo‘shin", ["Oltin qo‘shin", "Tosh bog‘", "Bronza otlar"], d=2,
      x="Har bir sopol askarning yuzi o‘ziga xos yasalgan."),
    Q("Qadimgi Xitoyning mashhur faylasufi kim?", "Konfutsiy", ["Gomer", "Aristotel", "Gerodot"], x="Konfutsiy ta’limoti Xitoyda juda mashhur."),
    Q("Konfutsiy ta’limotida nimalar ulug‘langan?", "Kattalarga hurmat, odob va bilim", ["Urush va bosqinchilik", "Dangasalik", "Yolg‘onchilik"],
      x="Konfutsiy oilada va jamiyatda hurmat va odobni ulug‘lagan."),
    Q("An’anaga ko‘ra, qog‘oz tayyorlashni milodiy 105-yilda takomillashtirgan xitoylik kim?", "Say Lun", ["Konfutsiy", "Sin Shixuandi", "Ashoka"], d=3,
      x="Say Lun qog‘oz tayyorlash usulini yaxshilagan."),
    Q("Qaysi xitoy ixtirosi dengizchilarga yo‘l topishda yordam bergan?", "Kompas", ["Porox", "Chinni", "Ipak"], x="Kompas mili shimolni ko‘rsatadi."),
    Q("Buyuk Xitoy devori asosan qaysi tomondan kelgan hujumlardan himoya uchun qurilgan?", "Shimoldan", ["Janubdan", "Dengizdan", "Sharqdagi orollardan"], d=2,
      x="Shimoldagi ko‘chmanchilar hujumidan himoyalanish uchun."),
    TF("Shaxmat qadimgi Hindistonda paydo bo‘lgan deb hisoblanadi.", True, x="Keyin u Eron va arablar orqali dunyoga tarqalgan."),
    TF("Konfutsiy — qadimgi Hindiston podshosi.", False, x="Konfutsiy — qadimgi Xitoy faylasufi."),
    TF("Sin Shixuandi Xitoyni birinchi bo‘lib yagona davlatga birlashtirgan.", True, d=2, x="Mil. avv. 221-yilda."),
    MATCH("Nomni u haqidagi ma’lumot bilan juftlang", [("Moxenjo-Daro", "Hind vodiysi shahri"), ("Ashoka", "Maurya podshosi"),
                                                      ("Sin Shixuandi", "Xitoyning birinchi imperatori"), ("Konfutsiy", "xitoy faylasufi"),
                                                      ("varna", "hind jamiyati tabaqasi"), ("Say Lun", "qog‘oz tayyorlashni yaxshilagan")], d=2),
    ORDER("So‘zlardan gap tuzing", "Shaxmat qadimgi Hindistonda paydo bo‘lgan", d=1, x="Shaxmatning qadimgi shakli Hindistonda yaratilgan."),
]
T.topic("india_china", "🏯", L("Qadimgi Hindiston va Xitoy", "Ancient India and China", "Древняя Индия и Китай"), C2,
        "• Hind vodiysida mil. avv. III ming yillikda Xarappa va Moxenjo-Daro shaharlari bo‘lgan: to‘g‘ri ko‘chalar, kanalizatsiya.\n"
        "• Hind jamiyati 4 varnaga bo‘lingan. Hindlar nol va o‘nli sanoqni ishlab chiqqan, shaxmat Hindistonda paydo bo‘lgan.\n"
        "  Mashhur podsho — Ashoka (Maurya davlati).\n"
        "• Xitoyni mil. avv. 221-yilda Sin Shixuandi birlashtirgan; uning maqbarasi yonida sopol qo‘shin topilgan.\n"
        "• Faylasuf Konfutsiy odob, kattalarga hurmat va bilimni ulug‘lagan. Xitoy ixtirolari: qog‘oz (Say Lun, 105-yil), kompas, porox, chinni.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["egypt", "mesopotamia", "india_china"], C2)

# ============================================================ 3-chorak
items = [
    Q("Qadimgi yunon shahar-davlati qanday ataladi?", "Polis", ["Satraplik", "Varna", "Legion"], x="Afina va Sparta — eng mashhur polislar."),
    Q("Qadimgi Yunoniston asosan qaysi yarim orolda joylashgan?", "Bolqon yarim orolida", ["Apennin yarim orolida", "Arabiston yarim orolida", "Hindiston yarim orolida"],
      x="Yunoniston Bolqon yarim orolining janubida."),
    Q("Afina demokratiyasi eng gullagan davrda uning rahbari kim bo‘lgan?", "Perikl", ["Leonid", "Yuliy Sezar", "Doro I"], d=2, x="Mil. avv. V asrda Perikl davrida Afina gullab-yashnagan."),
    Q("Afinadagi muhim masalalarni hal qilgan fuqarolar yig‘ini qanday atalgan?", "Xalq majlisi", ["Senat", "Kurultoy", "Parlament"], d=2,
      x="Xalq majlisida fuqarolar ovoz berib qaror qabul qilgan."),
    Q("Ma’buda Afina sharafiga qurilgan mashhur ibodatxona qaysi?", "Parfenon", ["Kolizey", "Panteon", "Zikkurat"], x="Parfenon Akropolda joylashgan."),
    Q("Parfenon qaysi tepalikda joylashgan?", "Akropolda", ["Olimpda", "Kapitoliyda", "Gizada"], d=2, x="Akropol — Afinadagi muqaddas tepalik."),
    Q("Marafon jangi qachon bo‘lgan?", "Mil. avv. 490-yilda", ["Mil. avv. 776-yilda", "Milodiy 476-yilda", "Mil. avv. 44-yilda"], d=3,
      x="Marafon jangi yunon-fors urushlarining mashhur jangi."),
    Q("Marafon jangida yunonlar kimga qarshi kurashgan?", "Forslarga", ["Rimliklarga", "Misrliklarga", "Xitoyliklarga"], x="Bu yunon-fors urushlari davri edi."),
    Q("“Marafon” yugurish poygasi nomi qaysi voqea bilan bog‘liq?", "G‘alaba xabarini yetkazgan chopar", ["Olimpda xudolar poygasi", "Rim gladiatorlari",
                                                                                                      "Piramidalar qurilishi"], d=2,
      x="Rivoyatga ko‘ra, chopar Marafondan Afinagacha yugurib, g‘alaba xabarini yetkazgan."),
    Q("Spartada o‘g‘il bolalar necha yoshdan harbiy tarbiyaga berilgan?", "7 yoshdan", ["1 yoshdan", "15 yoshdan", "20 yoshdan"], d=3,
      x="Spartada bolalar yoshligidan chidamli jangchi qilib tarbiyalangan."),
    Q("Fermopil darasida forslarga qarshi turgan Sparta podshosi kim?", "Leonid", ["Perikl", "Yuliy Sezar", "Doro I"], d=3, x="Podsho Leonid 300 spartalik bilan jasorat ko‘rsatgan."),
    Q("Troya urushi haqida hikoya qiluvchi doston qaysi?", "“Iliada”", ["“Avesto”", "“Alpomish”", "“Boburnoma”"], d=2, x="“Iliada” — Gomer dostoni."),
    Q("Afinada kimlar fuqaro hisoblangan?", "Afinalik ota-onadan tug‘ilgan erkaklar", ["Barcha aholi", "Faqat chet elliklar", "Faqat bolalar"], d=3,
      x="Ayollar, qullar va chet elliklar siyosiy huquqqa ega bo‘lmagan."),
    Q("Yunonlar O‘rta yer va Qora dengiz bo‘ylarida nima barpo etgan?", "Koloniyalar (yangi shaharlar)", ["Piramidalar", "Buyuk devor", "Zikkuratlar"], d=3,
      x="Yunon koloniyalari savdo va madaniyatni tarqatgan."),
    TF("Polis — qadimgi yunon shahar-davlati.", True, x="Har bir polis mustaqil davlat bo‘lgan."),
    TF("Parfenon Rimdagi Kapitoliy tepaligida joylashgan.", False, x="Parfenon Afinadagi Akropolda."),
    TF("Marafon jangida yunonlar forslar ustidan g‘alaba qozongan.", True, x="Mil. avv. 490-yilda."),
    MATCH("Nomni ma’nosi bilan juftlang", [("polis", "shahar-davlat"), ("Akropol", "Afinadagi muqaddas tepalik"), ("Parfenon", "ma’buda Afina ibodatxonasi"),
                                          ("Perikl", "Afina rahbari"), ("Leonid", "Sparta podshosi"), ("Marafon", "mil. avv. 490-yilgi jang joyi")], d=2),
    ORDER("So‘zlardan gap tuzing", "Afina demokratiya beshigi hisoblanadi", d=1, x="Demokratiya — xalq hokimiyati — Afinada shakllangan."),
]
T.topic("greece", "🏛️", L("Yunon polislari: Afina va Sparta", "Greek city-states: Athens and Sparta", "Греческие полисы: Афины и Спарта"), C3,
        "Qadimgi Yunoniston — Bolqon yarim orolida. Yunonlar polislarda (shahar-davlatlarda) yashagan, O‘rta yer va Qora dengiz bo‘ylarida koloniyalar barpo etgan.\n"
        "• Afina — demokratiya markazi; gullagan davrida rahbari Perikl bo‘lgan. Akropol tepaligida ma’buda Afina ibodatxonasi — Parfenon.\n"
        "• Sparta — qat’iy harbiy tarbiya: bolalar 7 yoshdan tarbiyaga berilgan; podsho Leonid Fermopilda forslarga qarshi turgan.\n"
        "• Mil. avv. 490-yil Marafon jangida yunonlar forslarni yenggan; “marafon” poygasi shu voqea bilan bog‘liq.\n"
        "• Gomerning “Iliada” dostoni Troya urushi haqida.", items=items)

items = [
    Q("Qadimgi Olimpiya o‘yinlari necha yilda bir marta o‘tkazilgan?", "4 yilda", ["1 yilda", "2 yilda", "10 yilda"], x="To‘rt yillik davr “olimpiada” deb atalgan."),
    Q("Olimpiya o‘yinlari vaqtida yunon polislari nima qilgan?", "Urushlarni to‘xtatib, sulh tuzgan", ["Yangi urush boshlagan", "Shaharlarni yopgan", "Savdoni taqiqlagan"],
      d=2, x="O‘yinlar vaqtida muqaddas sulh e’lon qilingan."),
    Q("Zamonaviy Olimpiya o‘yinlari qachon va qayerda qayta boshlangan?", "1896-yilda Afinada", ["1900-yilda Rimda", "776-yilda Spartada", "1924-yilda Qohirada"], d=3,
      x="Birinchi zamonaviy Olimpiya o‘yinlari Afinada bo‘lib o‘tgan."),
    Q("Olimpiya o‘yinlari qaysi xudo sharafiga o‘tkazilgan?", "Zevs", ["Ra", "Yupiter", "Mars"], d=2, x="Zevs — yunonlarning bosh xudosi."),
    Q("“Tarix otasi” deb kim ataladi?", "Gerodot", ["Gippokrat", "Pifagor", "Arximed"], x="Gerodot yunon-fors urushlari tarixini yozgan."),
    Q("“Tibbiyot otasi” deb kim ataladi?", "Gippokrat", ["Gerodot", "Sokrat", "Evklid"], x="Shifokorlar qasamyodi Gippokrat nomi bilan bog‘liq."),
    Q("To‘g‘ri burchakli uchburchak haqidagi mashhur teorema kimning nomi bilan ataladi?", "Pifagor", ["Arximed", "Platon", "Gomer"], x="Pifagor teoremasi."),
    Q("“Evrika!” (“Topdim!”) deb xitob qilgan olim kim?", "Arximed", ["Pifagor", "Gerodot", "Perikl"], d=2, x="Arximed suyuqlikdagi jism qonunini kashf etgan."),
    Q("Aristotelning ustozi kim bo‘lgan?", "Platon", ["Sokrat", "Gomer", "Pifagor"], d=2, x="Aristotel Platon akademiyasida o‘qigan."),
    Q("Platonning ustozi, suhbat orqali haqiqatni izlagan faylasuf kim?", "Sokrat", ["Aristotel", "Arximed", "Gerodot"], d=2, x="Sokrat savol-javob usulida o‘rgatgan."),
    Q("“Negizlar” asarida geometriya asoslarini bayon qilgan olim kim?", "Evklid", ["Gippokrat", "Gerodot", "Sokrat"], d=3, x="Evklid geometriyasi hozir ham maktabda o‘rganiladi."),
    Q("Moddalar mayda bo‘linmas zarralar — atomlardan tuzilgan degan yunon olimi kim?", "Demokrit", ["Perikl", "Leonid", "Gomer"], d=3, x="“Atom” — yunoncha “bo‘linmas”."),
    Q("Yunon teatrida aktyorlar yuziga nima taqib o‘ynagan?", "Niqob", ["Toj", "Dubulg‘a", "Ko‘zoynak"], x="Niqob qahramon qiyofasi va kayfiyatini ko‘rsatgan."),
    Q("“Faylasuf” so‘zining ma’nosi nima?", "Donolikni sevuvchi", ["Qo‘shin boshlig‘i", "Savdogar", "Sportchi"], d=2, x="Yunoncha: filo — sevaman, sofiya — donolik."),
    Q("Dunyoning yetti mo‘jizasidan qaysi biri Olimpiyada bo‘lgan?", "Zevs haykali", ["Osma bog‘lar", "Piramida", "Iskandariya mayog‘i"], d=3,
      x="Olimpiyadagi ulkan Zevs haykali yetti mo‘jizadan biri bo‘lgan."),
    TF("Sokrat — Platonning ustozi.", True, x="Sokrat → Platon → Aristotel."),
    TF("Gippokrat “tarix otasi” deb ataladi.", False, x="“Tarix otasi” — Gerodot; Gippokrat — “tibbiyot otasi”."),
    TF("Qadimgi Olimpiya o‘yinlari har yili o‘tkazilgan.", False, x="Ular 4 yilda bir marta o‘tkazilgan."),
    MATCH("Olimni sohasi bilan juftlang", [("Gerodot", "tarix"), ("Gippokrat", "tibbiyot"), ("Pifagor", "matematika"), ("Evklid", "geometriya"),
                                          ("Arximed", "fizika va mexanika"), ("Sokrat", "falsafa")], d=2),
    ORDER("Ustoz va shogirdlarni tartib bilan joylang", "Sokrat → Platon → Aristotel → Aleksandr Makedonskiy", sep=" → ", d=2,
          x="Har biri keyingisining ustozi bo‘lgan."),
]
T.topic("greek_culture", "🦉", L("Yunon madaniyati va fani", "Greek culture and science", "Культура и наука Греции"), C3,
        "Yunon madaniyati butun dunyoga ta’sir ko‘rsatgan:\n"
        "• Olimpiya o‘yinlari Zevs sharafiga 4 yilda bir marta o‘tkazilgan, o‘yinlar paytida urushlar to‘xtatilgan. Zamonaviy o‘yinlar 1896-yilda Afinada tiklangan.\n"
        "• Faylasuflar (faylasuf — “donolikni sevuvchi”): Sokrat → shogirdi Platon → uning shogirdi Aristotel.\n"
        "• Olimlar: Pifagor (matematika), Evklid (geometriya), Arximed (fizika, “Evrika!”), Demokrit (atom haqida),\n"
        "  Gippokrat — “tibbiyot otasi”, Gerodot — “tarix otasi”. Teatrda aktyorlar niqob taqib o‘ynagan.", items=items)

items = [
    Q("Rivoyatga ko‘ra, Rim shahriga qaysi aka-ukalar asos solgan?", "Romul va Rem", ["Kastor va Polluks", "Avazxon va Hasanxon", "Farhod va Qays"], x="Shahar Romul nomi bilan atalgan."),
    Q("Rivoyatga ko‘ra, go‘dak Romul va Remni qaysi hayvon boqqan?", "Ona bo‘ri", ["Ayiq", "Sher", "Burgut"], x="Ona bo‘ri haykali — Rim ramzlaridan biri."),
    Q("Rivoyatga ko‘ra, Rim qaysi yili tashkil topgan?", "Mil. avv. 753-yilda", ["Mil. avv. 776-yilda", "Milodiy 476-yilda", "Mil. avv. 221-yilda"], d=2,
      x="Rimliklar yillarni shahar tashkil topgan kundan sanashgan."),
    Q("Rim respublikasida har yili saylanadigan ikki oliy mansabdor kim?", "Konsullar", ["Fir’avnlar", "Satraplar", "Imperatorlar"], d=2, x="Ikki konsul bir-birini nazorat qilgan."),
    Q("Rimdagi zodagonlar kengashi qanday atalgan?", "Senat", ["Kurultoy", "Xalq majlisi", "Varna"], d=2, x="Senat davlat ishlarini muhokama qilgan."),
    Q("Rimdagi zodagon oilalar vakillari qanday atalgan?", "Patritsiylar", ["Plebeylar", "Gladiatorlar", "Legionerlar"], d=3, x="Patritsiylar — Rim zodagonlari."),
    Q("Rimdagi oddiy erkin aholi qanday atalgan?", "Plebeylar", ["Patritsiylar", "Senatorlar", "Konsullar"], d=3, x="Plebeylar huquq uchun uzoq kurashgan."),
    Q("Rim qo‘shinining asosiy bo‘linmasi qanday atalgan?", "Legion", ["Falanga", "Varna", "Polis"], d=2, x="Legion yaxshi qurollangan piyoda askarlardan iborat bo‘lgan."),
    Q("Rim bilan Karfagen o‘rtasidagi urushlar qanday ataladi?", "Punik urushlari", ["Yunon-fors urushlari", "Troya urushi", "Yuz yillik urush"], d=2,
      x="Bu urushlarda Rim g‘olib chiqqan."),
    Q("Fillar bilan Alp tog‘laridan oshib o‘tgan Karfagen sarkardasi kim?", "Gannibal", ["Spartak", "Yuliy Sezar", "Leonid"], x="Gannibal — mashhur Karfagen sarkardasi."),
    Q("Rimda eng yirik qullar qo‘zg‘oloniga kim boshchilik qilgan?", "Spartak", ["Gannibal", "Oktavian", "Perikl"], d=2, x="Spartak qo‘zg‘oloni mil. avv. I asrda bo‘lgan."),
    Q("“Keldim, ko‘rdim, yengdim” degan mashhur so‘zlar kimga tegishli?", "Yuliy Sezar", ["Spartak", "Gannibal", "Romul"], x="Sezar tezkor g‘alabasi haqida shunday yozgan."),
    Q("Rimning birinchi imperatori kim?", "Oktavian Avgust", ["Yuliy Sezar", "Romul", "Spartak"], d=2, x="Oktavian mil. avv. 27-yilda imperator bo‘lgan."),
    Q("Yil oylaridan qaysi biri Oktavian Avgust nomi bilan ataladi?", "Avgust", ["Mart", "Yanvar", "May"], x="Avgust oyi imperator sharafiga nomlangan."),
    Q("Yil oylaridan qaysi biri Yuliy Sezar nomi bilan bog‘liq?", "Iyul", ["Iyun", "Aprel", "Oktabr"], d=2, x="Iyul — Yuliy nomidan."),
    Q("Milodiy 79-yilda Vezuviy vulqoni kuli ostida qolgan shahar qaysi?", "Pompey", ["Afina", "Karfagen", "Iskandariya"], d=3,
      x="Qazishmalar Pompeyda Rim hayotini yaxshi saqlab qolgan."),
    Q("G‘arbiy Rim imperiyasi qaysi yili qulagan?", "Milodiy 476-yilda", ["Mil. avv. 753-yilda", "Milodiy 1453-yilda", "Mil. avv. 44-yilda"], d=3,
      x="476-yil qadimgi dunyo tarixining yakuni hisoblanadi."),
    Q("Yunonlarning Zevsiga Rimda qaysi xudo mos kelgan?", "Yupiter", ["Mars", "Ra", "Neptun"], d=3, x="Rimliklar ko‘p yunon xudolarini boshqa nom bilan ulug‘lagan."),
    TF("Spartak — Karfagen sarkardasi.", False, x="Spartak — Rimdagi qullar qo‘zg‘oloni rahbari; Karfagen sarkardasi — Gannibal."),
    TF("Oktavian Avgust Rimning birinchi imperatori bo‘lgan.", True, x="Undan keyin Rim imperiyaga aylangan."),
    TF("Rim respublikasini bitta konsul boshqargan.", False, x="Har yili ikkita konsul saylangan."),
    MATCH("Atamani ma’nosi bilan juftlang", [("senat", "zodagonlar kengashi"), ("konsul", "saylanadigan oliy mansabdor"), ("legion", "Rim qo‘shini bo‘linmasi"),
                                            ("patritsiy", "zodagon"), ("plebey", "oddiy erkin fuqaro"), ("Punik urushlari", "Rim va Karfagen urushlari")], d=2),
    ORDER("Voqealarni tartib bilan joylang", "Rimning tashkil topishi → Respublika o‘rnatilishi → Imperiya boshlanishi → G‘arbiy Rimning qulashi", sep=" → ", d=3,
          x="Mil. avv. 753 → mil. avv. 509 → mil. avv. 27 → milodiy 476."),
]
T.topic("rome", "🐺", L("Qadimgi Rim: respublikadan imperiyagacha", "Ancient Rome: republic to empire", "Древний Рим: от республики к империи"), C3,
        "• Rivoyatga ko‘ra, Rimga mil. avv. 753-yilda Romul va Rem asos solgan (ularni ona bo‘ri boqqan).\n"
        "• Mil. avv. 509-yildan Rim — respublika: har yili ikki konsul saylangan, senat — zodagonlar kengashi.\n"
        "  Aholi: patritsiylar (zodagonlar) va plebeylar (oddiy fuqarolar). Qo‘shin — legionlar.\n"
        "• Punik urushlarida Rim Karfagenni yengdi (Karfagen sarkardasi Gannibal fillar bilan Alp tog‘laridan o‘tgan). Qullar qo‘zg‘oloniga Spartak boshchilik qilgan.\n"
        "• Yuliy Sezar (“Keldim, ko‘rdim, yengdim”) — iyul oyi uning nomida; birinchi imperator — Oktavian Avgust (mil. avv. 27-yil).\n"
        "• Milodiy 79-yilda Pompey Vezuviy kuli ostida qolgan; G‘arbiy Rim imperiyasi 476-yilda qulagan.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["greece", "greek_culture", "rome"], C3)

# ============================================================ 4-chorak
items = [
    Q("Qadimgi Baqtriya hududiga Vatanimizning qaysi viloyati kirgan?", "Surxondaryo", ["Xorazm", "Qoraqalpog‘iston", "Toshkent"], d=2,
      x="Baqtriya Amudaryoning yuqori oqimida joylashgan."),
    Q("Qadimgi So‘g‘diyona hududida qaysi hozirgi shaharlar joylashgan?", "Samarqand va Buxoro", ["Termiz va Denov", "Nukus va Urganch", "Andijon va Namangan"], d=2,
      x="So‘g‘diyona — Zarafshon vodiysi."),
    Q("Samarqand shahrining qadimgi nomi qaysi?", "Maroqand", ["Baqtra", "Iskandariya", "Memfis"], x="Qadimgi yunon manbalarida Samarqand Maroqand deb atalgan."),
    Q("Qadimgi Baqtriyaning poytaxti qaysi shahar bo‘lgan?", "Baqtra (Balx)", ["Maroqand", "Tuproqqal’a", "Afina"], d=3, x="Baqtra — hozirgi Balx shahri o‘rnida."),
    Q("Qadimgi Xorazm hozirgi qaysi hududlarga to‘g‘ri keladi?", "Xorazm viloyati va Qoraqalpog‘iston", ["Surxondaryo", "Farg‘ona vodiysi", "Toshkent vohasi"], d=2,
      x="Xorazm Amudaryoning quyi oqimida joylashgan."),
    Q("Mil. avv. VI asrda O‘rta Osiyoning katta qismini bosib olgan davlat qaysi?", "Ahamoniylar (Qadimgi Fors)", ["Rim", "Misr", "Xitoy"], d=2,
      x="Kir II va Doro I davrida."),
    Q("O‘rta Osiyoning ko‘chmanchi chorvador qabilalari qanday atalgan?", "Saklar va massagetlar", ["Rimliklar va yunonlar", "Shumerlar va finikiyaliklar", "Misrliklar va hindlar"],
      x="Ular dasht va tog‘ oldi hududlarida yashagan."),
    Q("Ahamoniylar davlatidagi viloyatlar qanday atalgan?", "Satrapliklar", ["Polislar", "Legionlar", "Varnalar"], d=3, x="Satraplikni satrap boshqargan."),
    Q("Qadimgi Xorazm shohlarining qasri joylashgan mashhur yodgorlik qaysi?", "Tuproqqal’a", ["Afrosiyob", "Kolizey", "Parfenon"], x="Tuproqqal’a — Qoraqalpog‘istondagi yodgorlik."),
    Q("Xorazmdagi aylana shaklidagi qadimgi qal’a-ibodatxona qaysi?", "Qo‘yqirilganqal’a", ["Tuproqqal’a", "Afrosiyob", "Sopollitepa"], d=3, x="Qo‘yqirilganqal’a aylana shaklida qurilgan."),
    Q("Qadimgi Xorazm yodgorliklarini o‘rgangan mashhur arxeolog kim?", "Sergey Tolstov", ["Fransua Shampolyon", "Gerodot", "Sokrat"], d=3,
      x="S. P. Tolstov boshchiligidagi ekspeditsiya Xorazmni ko‘p yillar o‘rgangan."),
    Q("Qadimgi Xorazm dehqonchiligining asosi nima bo‘lgan?", "Amudaryodan chiqarilgan kanallar", ["Yomg‘ir suvi", "Dengiz suvi", "Qor suvi"],
      x="Xorazmda sug‘orish tizimi juda qadimdan rivojlangan."),
    Q("So‘g‘dlar Buyuk ipak yo‘lida qanday faoliyat bilan mashhur bo‘lgan?", "Savdogarlik", ["Dengizchilik", "Piramida qurish", "Gladiatorlik"],
      x="So‘g‘d savdogarlari Xitoygacha borgan."),
    Q("So‘g‘d va xorazm yozuvlari qaysi yozuv asosida paydo bo‘lgan?", "Oromiy yozuvi", ["Lotin yozuvi", "Iyeroglif", "Kirill yozuvi"], d=3,
      x="Oromiy yozuvi Ahamoniylar davrida keng tarqalgan."),
    Q("Qadimgi shaharlar qanday himoyalangan?", "Qalin mudofaa devorlari bilan", ["Yog‘och panjaralar bilan", "Hech qanday himoyasiz", "Shisha devorlar bilan"],
      x="Shaharlar atrofi baland devor va xandaq bilan o‘ralgan."),
    TF("Tuproqqal’a — qadimgi Xorazm shohlarining qasri.", True, d=2, x="U Qoraqalpog‘iston hududida joylashgan."),
    TF("Saklar — Misrning o‘troq dehqonlari.", False, x="Saklar — O‘rta Osiyo va dasht hududlaridagi ko‘chmanchi chorvadorlar."),
    TF("Mil. avv. VI asrda O‘rta Osiyoning katta qismi Ahamoniylar davlati tarkibiga kirgan.", True, d=2, x="Bu davr mil. avv. IV asrgacha davom etgan."),
    MATCH("Qadimgi o‘lkani hududi bilan juftlang", [("Xorazm", "Amudaryo quyi oqimi"), ("So‘g‘diyona", "Zarafshon vodiysi"), ("Baqtriya", "Amudaryo yuqori oqimi"),
                                                   ("Dovon", "Farg‘ona vodiysi"), ("Qang‘", "Sirdaryo o‘rta oqimi")], d=2),
]
T.topic("ancient_states", "🏰", L("O‘rta Osiyoning qadimgi o‘lkalari", "Ancient lands of Central Asia", "Древние области Средней Азии"), C4,
        "Mil. avv. I ming yillikda Vatanimiz hududida qadimgi davlatlar va o‘lkalar bo‘lgan:\n"
        "• Xorazm (Amudaryo quyi oqimi; Xorazm viloyati va Qoraqalpog‘iston) — sug‘orish kanallari, Tuproqqal’a (shohlar qasri),\n"
        "  Qo‘yqirilganqal’a (aylana qal’a). Ularni arxeolog Sergey Tolstov o‘rgangan.\n"
        "• So‘g‘diyona (Zarafshon vodiysi; markazi — Maroqand, ya’ni Samarqand), Baqtriya (Amudaryo yuqori oqimi; poytaxti Baqtra).\n"
        "• Ko‘chmanchi chorvadorlar — saklar va massagetlar.\n"
        "• Mil. avv. VI asrda O‘rta Osiyoning katta qismi Ahamoniylar davlatiga qo‘shilgan; viloyatlar — satrapliklar.\n"
        "• So‘g‘d va xorazm yozuvlari oromiy yozuvi asosida paydo bo‘lgan.", items=items)

items = [
    Q("Zardushtiylik ta’limotining asoschisi kim?", "Zardusht", ["Konfutsiy", "Gomer", "Xammurapi"], x="Ta’limot uning nomi bilan ataladi."),
    Q("Zardushtiylikda qaysi narsa muqaddas va poklik ramzi sanalgan?", "Olov", ["Temir", "Oltin", "Tosh"], x="Otashkadalarda olov doim yonib turgan."),
    Q("Zardushtiylikning asosiy axloqiy qoidasi qaysi?", "Ezgu fikr, ezgu so‘z, ezgu amal", ["Kuchli bo‘lsang, hammasi seniki", "Faqat o‘zingni o‘yla", "Boylik — eng oliy maqsad"],
      x="Bu qoida insonni yaxshilikka chorlaydi."),
    Q("“Avesto”da ezgulik timsoli sifatida kim ulug‘langan?", "Axura Mazda", ["Axriman", "Zevs", "Ra"], d=2, x="Axura Mazda — ezgulik va yorug‘lik timsoli."),
    Q("“Avesto”da yovuzlik timsoli kim?", "Axriman", ["Axura Mazda", "Yupiter", "Ra"], d=3, x="Ezgulik va yovuzlik kurashi — ta’limotning asosiy g‘oyasi."),
    Q("Zardushtiylar qaysi tabiat unsurlarini ifloslantirmaslikka chaqirgan?", "Yer, suv, havo va olov", ["Faqat temirni", "Faqat oltinni", "Hech narsani"], d=2,
      x="Tabiatni pok saqlash muqaddas burch hisoblangan."),
    Q("Zardushtiylikdagi olov ibodatxonasi qanday ataladi?", "Otashkada", ["Zikkurat", "Parfenon", "Piramida"], d=3, x="“Otash” — olov degani."),
    Q("“Avesto”da tilga olingan o‘lkalar qaysilar?", "So‘g‘d, Xorazm, Baqtriya, Marg‘iyona", ["Misr, Rim, Yunoniston", "Xitoy, Hindiston, Yaponiya", "Finikiya, Bobil, Ossuriya"],
      d=2, x="Shuning uchun “Avesto” Vatanimiz tarixining muhim manbai."),
    Q("“Avesto” qanday tarixiy manba?", "Eng qadimgi yozma manbalardan biri", ["Rim qonunlari to‘plami", "Yunon dostoni", "Xitoy lug‘ati"],
      x="U O‘rta Osiyo xalqlarining qadimgi hayoti haqida ma’lumot beradi."),
    Q("“Avesto”da qanday mehnat ezgu ish sifatida ulug‘langan?", "Dehqonchilik va chorvachilik", ["Talonchilik", "Dangasalik", "Qimor"], d=2,
      x="Yerni obod qilish, chorva boqish savobli ish deb bilingan."),
    Q("Amudaryo bo‘yidan topilgan mashhur oltin va kumush buyumlar to‘plami qanday ataladi?", "Amudaryo xazinasi", ["Tutanxamon xazinasi", "Troya xazinasi", "Rim xazinasi"],
      d=3, x="Xazina qadimgi zargarlarning yuksak mahoratini ko‘rsatadi."),
    Q("Navro‘z qanday bayram?", "Bahor va yangi yil bayrami", ["Qish bayrami", "Hosil bayrami", "Dengiz bayrami"], x="Navro‘z juda qadimiy bayram, u kun va tun tenglashganda nishonlanadi."),
    Q("Toshkent shahrining 2200 yillik yubileyi qaysi yili nishonlangan?", "2009-yilda", ["1991-yilda", "1997-yilda", "2020-yilda"], d=3, x="Toshkent — qadimiy shaharlarimizdan biri."),
    Q("Termiz shahrining 2500 yillik yubileyi qaysi yili nishonlangan?", "2002-yilda", ["1997-yilda", "2007-yilda", "2016-yilda"], d=3, x="Termiz — Surxondaryodagi qadimiy shahar."),
    TF("Zardusht — “Avesto” ta’limotining asoschisi.", True, x="Zardushtiylik uning nomi bilan ataladi."),
    TF("Axriman — ezgulik timsoli.", False, x="Axriman — yovuzlik timsoli; ezgulik timsoli — Axura Mazda."),
    TF("Zardushtiylikda olov poklik ramzi hisoblangan.", True, x="Shuning uchun olov ibodatxonalari qurilgan."),
    MATCH("Tushunchani ma’nosi bilan juftlang", [("Zardusht", "ta’limot asoschisi"), ("“Avesto”", "muqaddas kitob"), ("Axura Mazda", "ezgulik timsoli"),
                                                ("Axriman", "yovuzlik timsoli"), ("otashkada", "olov ibodatxonasi"), ("Navro‘z", "bahor bayrami")], d=2),
    ORDER("So‘zlardan gap tuzing", "Zardushtiylar olovni poklik ramzi deb bilgan", d=1, x="Olov zardushtiylikda muqaddas sanalgan."),
]
T.topic("avesto", "🔥", L("Zardushtiylik va “Avesto”", "Zoroastrianism and the Avesta", "Зороастризм и «Авеста»"), C4,
        "Zardushtiylik — O‘rta Osiyo va Eronda keng tarqalgan qadimgi ta’limot, asoschisi — Zardusht. Muqaddas kitobi — “Avesto”.\n"
        "• Asosiy qoida: “Ezgu fikr, ezgu so‘z, ezgu amal”. Ezgulik timsoli — Axura Mazda, yovuzlik timsoli — Axriman.\n"
        "• Olov poklik ramzi sanalgan, ibodatxonalar — otashkadalar. Yer, suv, havo va olovni ifloslantirmaslik buyurilgan;\n"
        "  dehqonchilik va chorvachilik ezgu mehnat deb ulug‘langan.\n"
        "• “Avesto”da So‘g‘d, Xorazm, Baqtriya, Marg‘iyona tilga olinadi — u Vatanimiz tarixining muhim manbai.\n"
        "• Qadimiy shaharlarimiz: Termizning 2500 yilligi (2002), Toshkentning 2200 yilligi (2009) nishonlangan.", items=items)

items = [
    Q("Aleksandr Makedonskiy kimning o‘g‘li edi?", "Filipp II", ["Kir II", "Doro I", "Perikl"], d=2, x="Filipp II — Makedoniya podshosi."),
    Q("Aleksandr Makedonskiy Sharqqa yurishni qaysi yili boshlagan?", "Mil. avv. 334-yilda", ["Mil. avv. 776-yilda", "Milodiy 476-yilda", "Mil. avv. 44-yilda"], d=3,
      x="U Ahamoniylar davlatiga qarshi yurish boshlagan."),
    Q("Aleksandr Makedonskiy qo‘shini O‘rta Osiyoga qachon kirib kelgan?", "Mil. avv. 329-yilda", ["Mil. avv. 530-yilda", "Milodiy 79-yilda", "Mil. avv. 221-yilda"],
      x="Mil. avv. 329-yilda Aleksandr Baqtriya va So‘g‘diyonaga kirib keldi."),
    Q("Aleksandr qaysi davlatni tor-mor etib, O‘rta Osiyoga yo‘l ochgan?", "Ahamoniylar davlatini", ["Rim respublikasini", "Xitoy imperiyasini", "Kushon podsholigini"], d=2,
      x="Ahamoniylar davlati mil. avv. 330-yilda qulagan."),
    Q("Aleksandr So‘g‘diyonaning qaysi markaziy shahrini egallagan?", "Maroqand", ["Rim", "Afina", "Memfis"], x="Maroqand — qadimgi Samarqand."),
    Q("Spitamen qaysi o‘lkaning sarkardasi bo‘lgan?", "So‘g‘diyonaning", ["Misrning", "Rimning", "Xitoyning"], x="Spitamen so‘g‘dlarning bosqinchilarga qarshi kurashiga boshchilik qilgan."),
    Q("Spitamen boshchiligidagi kurash qaysi asrda bo‘lgan?", "Mil. avv. IV asrda", ["Milodiy XV asrda", "Mil. avv. VIII asrda", "Milodiy I asrda"], d=2,
      x="Aleksandr yurishi davrida — mil. avv. 329-yildan boshlab."),
    Q("Aleksandr Makedonskiy uylangan mahalliy zodagon qizi kim?", "Roksana", ["Barchin", "To‘maris", "Kleopatra"], d=3, x="Roksana — O‘rta Osiyolik zodagonning qizi."),
    Q("Aleksandr Makedonskiy qachon va qayerda vafot etgan?", "Mil. avv. 323-yilda Bobilda", ["Mil. avv. 329-yilda Maroqandda", "Milodiy 476-yilda Rimda",
                                                                                                "Mil. avv. 490-yilda Marafonda"], d=3,
      x="Uning ulkan davlati vafotidan keyin bo‘linib ketgan."),
    Q("Aleksandr vafotidan keyin O‘rta Osiyo qaysi sulola davlati tarkibiga kirgan?", "Salavkiylar", ["Ahamoniylar", "Kushonlar", "Somoniylar"], d=3,
      x="Salavkiylar — Aleksandr sarkardalaridan biri asos solgan sulola."),
    Q("Mil. avv. III asrda Baqtriyada tashkil topgan davlat qanday ataladi?", "Yunon-Baqtriya podsholigi", ["Kushon podsholigi", "Ahamoniylar davlati", "Rim imperiyasi"],
      d=2, x="Bu davlatda yunon va mahalliy madaniyat qo‘shilib ketgan."),
    Q("Yunon va Sharq madaniyatlari qo‘shilishidan paydo bo‘lgan madaniyat qanday ataladi?", "Ellinistik madaniyat", ["Neolit madaniyati", "Kaltaminor madaniyati",
                                                                                                                     "Shumer madaniyati"], d=2,
      x="“Ellin” — yunonlarning o‘zlarini atagan nomi."),
    Q("Kushon podsholigi qaysi asrlarda mavjud bo‘lgan?", "Milodiy I–IV asrlarda", ["Mil. avv. X asrda", "Milodiy XV asrda", "Milodiy XX asrda"], d=2,
      x="Kushonlar O‘rta Osiyo, Afg‘oniston va Shimoliy Hindistonni birlashtirgan."),
    Q("Kushon podsholigining eng mashhur hukmdori kim?", "Kanishka", ["Kir II", "Ashoka", "Doro I"], x="Kanishka davrida Kushon davlati eng qudratli bo‘lgan."),
    Q("Surxondaryodagi qaysi Kushon davri shahri xarobasidan oltin xazina topilgan?", "Dalvarzintepa", ["Afrosiyob", "Tuproqqal’a", "Obirahmat"], d=3,
      x="Dalvarzintepa xazinasi 1972-yilda topilgan."),
    Q("Kushonlar davrida Hindistondan O‘rta Osiyoga qaysi ta’limot tarqalgan?", "Buddaviylik", ["Zardushtiylik", "Konfutsiylik", "Yunon falsafasi"], d=3,
      x="Termiz yaqinidagi Fayoztepa va Qoratepa — buddaviylik ibodatxonalari xarobalari."),
    Q("Kushonlar davrida Buyuk ipak yo‘li qanday ahvolda bo‘lgan?", "Savdo gullab-yashnagan", ["Butunlay yopilgan", "Hali ochilmagan", "Faqat dengiz yo‘li bo‘lgan"],
      x="Kushon davlati Sharq va G‘arb savdosida vositachi bo‘lgan."),
    Q("Xitoy manbalarida Farg‘ona vodiysidagi qadimgi davlat qanday atalgan?", "Dovon", ["Qang‘", "Baqtra", "Satraplik"], d=2, x="Dovon haqida xitoy elchisi Chjan Szyan xabar bergan."),
    Q("Dovon qanday mashhur otlari bilan dong taratgan?", "“Samoviy otlar” (arg‘umoqlar)", ["Mitti otlar", "Qanotli otlar", "Suv otlari"], d=2,
      x="Xitoy imperatorlari Dovon otlarini juda qadrlagan."),
    TF("Spitamen Aleksandr Makedonskiy qo‘shiniga qarshi kurashgan.", True, x="U vatan ozodligi uchun kurashgan qahramon."),
    TF("Kanishka — Yunon-Baqtriya podsholigining asoschisi.", False, x="Kanishka — Kushon podsholigining mashhur hukmdori."),
    TF("Kushonlar davrida tangalar zarb qilingan va savdo rivojlangan.", True, x="Kushon tangalari ko‘p joylardan topilgan."),
    ORDER("Davrlarni tartib bilan joylang", "Ahamoniylar hukmronligi → Aleksandr yurishi → Yunon-Baqtriya podsholigi → Kushon podsholigi", sep=" → ", d=2,
          x="Mil. avv. VI asr → mil. avv. IV asr → mil. avv. III asr → milodiy I asr."),
    MATCH("Shaxs yoki joyni u haqidagi ma’lumot bilan juftlang", [("Aleksandr Makedonskiy", "mil. avv. 329-yilda O‘rta Osiyoga kelgan"),
                                                                 ("Spitamen", "so‘g‘dlar kurashi rahbari"), ("Roksana", "Aleksandrning rafiqasi"),
                                                                 ("Kanishka", "Kushon hukmdori"), ("Dovon", "samoviy otlar yurti"),
                                                                 ("Dalvarzintepa", "Kushon davri shahri")], d=2),
]
T.topic("alexander_kushan", "⚔️", L("Aleksandr yurishidan Kushon podsholigigacha", "From Alexander to the Kushan Empire", "От Александра до Кушанского царства"), C4,
        "• Mil. avv. 334-yilda Aleksandr Makedonskiy (Filipp II ning o‘g‘li) Sharqqa yurish boshladi, Ahamoniylar davlatini tor-mor etib,\n"
        "  mil. avv. 329-yilda O‘rta Osiyoga kirib keldi, Maroqandni egalladi. So‘g‘d sarkardasi Spitamen boshchiligida xalq qat’iy kurashdi.\n"
        "• Aleksandr mahalliy zodagon qizi Roksanaga uylandi, mil. avv. 323-yilda Bobilda vafot etdi.\n"
        "• Keyin Salavkiylar, mil. avv. III asrdan Yunon-Baqtriya podsholigi; ellinistik madaniyat shakllandi.\n"
        "• Dovon (Farg‘ona) — “samoviy otlar” yurti; Qang‘ — Sirdaryo o‘rta oqimida.\n"
        "• Kushon podsholigi (milodiy I–IV asrlar), mashhur hukmdori — Kanishka. Buyuk ipak yo‘li gullab-yashnadi, buddaviylik tarqaldi;\n"
        "  Dalvarzintepada oltin xazina topilgan.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["ancient_states", "avesto", "alexander_kushan"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["prehistory", "metals", "time_bc", "egypt", "mesopotamia", "india_china", "greece", "greek_culture", "rome", "ancient_states", "avesto", "alexander_kushan"],
       C4, level=3)

T.write()
