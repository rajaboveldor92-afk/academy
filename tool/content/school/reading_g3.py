"""O‘qish, 3-sinf: matnni tushunish, maqollar, topishmoqlar, janrlar, bolalar adabiyoti.

Hikoyalar va topishmoqlar o‘zimiz yozgan (darsliklardan ko‘chirilmagan); maqollar — xalq og‘zaki ijodi.
Qayta yaratish: python3 tool/content/school/reading_g3.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from readlit import *  # noqa: E402,F401,F403

rnd = random.Random(33)
T = Course("reading", 3, L("O‘qish", "Reading", "Чтение"))

C1 = "1-chorak. Matnni o‘qib tushunamiz"
C2 = "2-chorak. Xalq og‘zaki ijodi"
C3 = "3-chorak. Adabiy asarlar va janrlar"
C4 = "4-chorak. O‘qib, fikrlaymiz"

S1 = ("Sardor yangi maktabga keldi. U hech kimni tanimasdi, shuning uchun tanaffusda yolg‘iz o‘tirdi. "
      "Buni ko‘rgan Malika uning yoniga keldi va o‘yinga taklif qildi. Tez orada Sardor sinfdoshlari bilan "
      "do‘stlashib oldi. Ertasi kuni u maktabga quvonib bordi.")
S2 = ("Qish kelib, hamma yoqni qor qopladi. Qushlarga don topish qiyinlashdi. Zarina bobosi bilan yog‘ochdan "
      "kichik yemlik yasadi. Ular yemlikni bog‘dagi daraxtga osib, ichiga don sepishdi. Ertalab yemlik atrofida "
      "chumchuqlar chug‘urlashib yurardi. Zarina ularni derazadan kuzatib, xursand bo‘ldi.")
S3 = ("Anvar tishini yuvayotganda jo‘mrakni ochiq qoldirardi. Bir kuni dadasi unga: “Toza suv — bebaho boylik, "
      "har tomchisini asrash kerak”, dedi. Shundan keyin Anvar tish yuvayotganda jo‘mrakni yopib qo‘yadigan bo‘ldi. "
      "U buni singlisiga ham o‘rgatdi.")
S4 = ("Lola kutubxonadan “Hayvonlar olami” degan kitob oldi. Kitobda turli o‘lkalarda yashaydigan hayvonlar haqida "
      "qiziqarli ma’lumotlar bor edi. Lolaga eng ko‘p qor qoploni haqidagi sahifa yoqdi. U o‘qiganlarini darsda "
      "sinfdoshlariga so‘zlab berdi. O‘qituvchi uni maqtadi va qor qoploni rasmini chizishni topshirdi.")
S5 = ("Bahor keldi. Mahalla ahli hasharga yig‘ildi. Kattalar ko‘chaga ko‘chat o‘tqazdi, bolalar esa ariqlarni "
      "tozaladi. Buvijonlar hammaga issiq non va choy olib chiqishdi. Kechga borib ko‘cha ko‘rkam bo‘ldi. "
      "Hamma charchagan bo‘lsa ham, mamnun edi.")
S6 = ("Bobur do‘kondan non olib qaytayotib, sotuvchi qaytimni ko‘p berib yuborganini payqadi. U ortiga qaytib, "
      "ortiqcha pulni sotuvchiga berdi. Sotuvchi Boburga rahmat aytdi va: “Rostgo‘y bola ekansan”, dedi. "
      "Uyda bu voqeani eshitgan onasi o‘g‘li bilan faxrlandi.")

items = [
    Q("Sardor tanaffusda nima uchun yolg‘iz o‘tirdi?", "Hech kimni tanimasdi", ["Kasal edi", "Kitob o‘qiyotgan edi", "Charchagan edi"], text=S1, x="Matnda: “U hech kimni tanimasdi”."),
    Q("Sardorni o‘yinga kim taklif qildi?", "Malika", ["O‘qituvchi", "Akasi", "Qo‘shnisi"], text=S1, x="Malika uning yoniga kelib, o‘yinga taklif qildi."),
    Q("Ertasi kuni Sardor maktabga qanday bordi?", "Quvonib", ["Yig‘lab", "Istamay", "Kechikib"], text=S1, x="Do‘st orttirgach, u maktabga quvonib bordi."),
    Q("Hikoyaga eng mos sarlavhani tanlang.", "Yangi do‘st", ["Qishki ta’til", "Yo‘qolgan kitob", "Bog‘dagi daraxt"], text=S1, d=2, x="Hikoya Sardorning do‘st orttirgani haqida."),
    Q("Malikaning qaysi fazilati ko‘rindi?", "Mehribonligi", ["Dangasaligi", "Maqtanchoqligi", "Qo‘rqoqligi"], text=S1, d=2, x="U yolg‘iz bolaga e’tibor berib, yordam qo‘lini cho‘zdi."),
    Q("Qushlarga nima qiyin bo‘lib qoldi?", "Don topish", ["Uchish", "Sayrash", "Uya qurish"], text=S2, x="Qor qoplagani uchun don topish qiyinlashdi."),
    Q("Zarina yemlikni kim bilan yasadi?", "Bobosi bilan", ["Onasi bilan", "Dugonasi bilan", "Yolg‘iz o‘zi"], text=S2, x="“Zarina bobosi bilan … yemlik yasadi.”"),
    Q("Yemlik nimadan yasaldi?", "Yog‘ochdan", ["Temirdan", "Qog‘ozdan", "Shishadan"], text=S2, x="Yemlik yog‘ochdan yasaldi."),
    Q("Yemlik qayerga osildi?", "Bog‘dagi daraxtga", ["Deraza tokchasiga", "Uy tomiga", "Darvozaga"], text=S2, x="Ular yemlikni bog‘dagi daraxtga osishdi."),
    Q("Matnning asosiy fikri qaysi?", "Qishda qushlarga g‘amxo‘rlik qilish kerak", ["Qishda uydan chiqmaslik kerak", "Qushlar qishda uxlaydi", "Qor faqat zarar keltiradi"],
      text=S2, d=2, x="Zarina va bobosi qushlarga yordam berishdi."),
    Q("Anvar avval qanday xato qilardi?", "Jo‘mrakni ochiq qoldirardi", ["Tishini yuvmasdi", "Kech yotardi", "Nonushta qilmasdi"], text=S3, x="U tish yuvayotganda jo‘mrakni ochiq qoldirardi."),
    Q("Dadasi Anvarga nimani tushuntirdi?", "Suvni asrash kerakligini", ["Tishni qanday yuvishni", "Darsni qanday qilishni", "Qanday o‘ynashni"], text=S3, x="“Toza suv — bebaho boylik”."),
    Q("Anvar o‘rganganini kimga o‘rgatdi?", "Singlisiga", ["Akasiga", "Dadasiga", "Do‘stiga"], text=S3, x="U buni singlisiga ham o‘rgatdi."),
    Q("Hikoyaga mos maqolni tanlang.", "Tomchi-tomchi ko‘l bo‘lur.", ["Ko‘z qo‘rqoq, qo‘l botir.", "Bir kun tuz ichgan joyga qirq kun salom ber.", "Sabr tagi — sariq oltin."],
      text=S3, d=3, x="Har tomchi suvni asrasak, ko‘p suv tejaladi."),
    TF("Malika Sardorni o‘yinga taklif qildi.", True, text=S1, x="Matnda shunday yozilgan."),
    TF("Zarina chumchuqlarni hovlida quvlab yurdi.", False, text=S2, x="Zarina ularni derazadan kuzatib, xursand bo‘ldi."),
    TF("Anvar dadasining gapidan keyin suvni tejay boshladi.", True, text=S3, x="U jo‘mrakni yopib qo‘yadigan bo‘ldi."),
]
T.topic("understand_story", "📖", L("Hikoyani o‘qib tushunamiz", "Understanding a story", "Понимаем рассказ"), C1,
        "Matnni tushunib o‘qish uchun:\n"
        "• Kim? Nima qildi? Qayerda? Qachon? Nima uchun? degan savollarga matndan javob toping.\n"
        "• Asosiy fikr — muallif aytmoqchi bo‘lgan eng muhim gap.\n"
        "• Sarlavha matnning mazmunini qisqa ifodalaydi.", items=items)

items = [
    Q("Lola qanday kitob oldi?", "“Hayvonlar olami”", ["“Ertaklar”", "“Qiziqarli matematika”", "“O‘simliklar dunyosi”"], text=S4, x="Kitob nomi — “Hayvonlar olami”."),
    Q("Lolaga qaysi hayvon haqidagi sahifa eng ko‘p yoqdi?", "Qor qoploni", ["Fil", "Delfin", "Jirafa"], text=S4, x="Unga qor qoploni haqidagi sahifa yoqdi."),
    Q("Lola o‘qiganlarini kimlarga so‘zlab berdi?", "Sinfdoshlariga", ["Buvisiga", "Qo‘shnisiga", "Ukasiga"], text=S4, x="U darsda sinfdoshlariga so‘zlab berdi."),
    Q("O‘qituvchi Lolaga nima topshirdi?", "Qor qoploni rasmini chizishni", ["She’r yodlashni", "Kitobni qaytarishni", "Masala yechishni"], text=S4, x="Matnning oxirgi gapida aytilgan."),
    Q("Hashar qaysi faslda bo‘ldi?", "Bahorda", ["Qishda", "Yozda", "Kuzda"], text=S5, x="“Bahor keldi.”"),
    Q("Hasharda bolalar nima qilishdi?", "Ariqlarni tozalashdi", ["Ko‘chat o‘tqazishdi", "Non yopishdi", "Uy qurishdi"], text=S5, x="Kattalar ko‘chat o‘tqazdi, bolalar ariqlarni tozaladi."),
    Q("Buvijonlar hammaga nima olib chiqishdi?", "Issiq non va choy", ["Meva va sharbat", "Gul va ko‘chat", "Kitob va daftar"], text=S5, x="Buvijonlar issiq non va choy olib chiqishdi."),
    Q("“Hashar” so‘zining ma’nosi qaysi?", "Birgalikda bajariladigan ish", ["Bayram tantanasi", "Sport musobaqasi", "Dam olish kuni"], text=S5, d=2, x="Hasharda qo‘ni-qo‘shnilar yig‘ilib, birgalikda ishlaydi."),
    Q("Matnning asosiy fikri qaysi?", "Birgalikda qilingan ish natija beradi", ["Bahorda ko‘p uxlash kerak", "Faqat kattalar ishlashi kerak", "Charchash yomon narsa"], text=S5, d=2, x="Hamma birga ishlab, ko‘chani ko‘rkam qildi."),
    Q("Bobur nimani payqadi?", "Qaytim ko‘p berilganini", ["Non qotib qolganini", "Do‘kon yopilganini", "Pulini yo‘qotganini"], text=S6, x="Sotuvchi qaytimni ko‘p berib yuborgan edi."),
    Q("Bobur ortiqcha pulni nima qildi?", "Sotuvchiga qaytardi", ["O‘ziga oldi", "Konfet oldi", "Do‘stiga berdi"], text=S6, x="U ortiga qaytib, pulni sotuvchiga berdi."),
    Q("Sotuvchi Boburni qanday bola dedi?", "Rostgo‘y", ["Sho‘x", "Dangasa", "Qo‘rqoq"], text=S6, x="“Rostgo‘y bola ekansan”, dedi."),
    Q("Hikoyada qanday fazilat ulug‘langan?", "Halollik", ["Shoshqaloqlik", "Maqtanchoqlik", "Yalqovlik"], text=S6, d=2, x="Bobur birovning haqini qaytarib, halollik qildi."),
    Q("Onasi nima uchun faxrlandi?", "O‘g‘li halol ish qilgani uchun", ["O‘g‘li non olib kelgani uchun", "O‘g‘li tez yugurgani uchun", "Do‘kon arzonlashgani uchun"], text=S6, d=3, x="Bobur ortiqcha pulni qaytarib, rostgo‘ylik qildi."),
    TF("Lola kitobni do‘kondan sotib oldi.", False, text=S4, x="U kitobni kutubxonadan oldi."),
    TF("Hasharda hamma charchagan bo‘lsa ham, mamnun edi.", True, text=S5, x="Matnning oxirgi gapi."),
    TF("Bobur ortiqcha pulni o‘zida qoldirdi.", False, text=S6, x="U pulni sotuvchiga qaytardi."),
]
T.topic("infer", "🧠", L("Matndan xulosa chiqaramiz", "Drawing conclusions", "Делаем выводы"), C1,
        "Xulosa chiqarish uchun qahramon nima qilgani va bu nimaga olib kelganini o‘ylang.\n"
        "• Sabab → natija: qor yog‘di → qushlarga don topish qiyinlashdi.\n"
        "• Qahramonning ishiga qarab uning fazilatini aniqlang: pulni qaytardi → halol.\n"
        "Javobni doim matndagi dalil bilan tekshiring.", items=items)

T.topic("understand", "📚", L("Matnni tushunish (aralash)", "Reading practice", "Понимание текста"), C1,
        "Matnni boshidan oxirigacha o‘qing. Kim, nima, qayerda va nima sababdan degan savollarga matndan dalil toping. "
        "Sarlavha matndagi asosiy voqeani ifodalashi kerak.",
        gen="comprehension", levels=[dict(options=n, infer=False) for n in (2, 3, 4)])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["understand_story", "infer"], C1)

# ============================================================ 2-chorak
items = []
endings = [b for _, b, _ in PROVERBS]
for a, b, theme in PROVERBS:
    items.append(Q(f"Maqolni davom ettiring: “{a} …”", b, rnd.sample([e for e in endings if e != b], 3), d=1 if len(items) < 12 else 2,
                   x=f"{a} {b} Mavzusi: {theme.lower()}."))
themes = sorted({t for _, _, t in PROVERBS})
for a, b, theme in PROVERBS[:12]:
    items.append(Q(f"“{a} {b}” maqoli nima haqida?", theme, rnd.sample([t for t in themes if t != theme], 3), d=2,
                   x=f"Bu maqol {theme.lower()} haqida."))
items += [
    TF("Maqol — xalq donoligi, qisqa va ta’sirli ibratli gap.", True, x="Maqollarni xalq yaratgan, avloddan avlodga o‘tib kelgan."),
    TF("Maqollarni bitta yozuvchi yozgan.", False, x="Maqollar — xalq og‘zaki ijodi, muallifi xalq."),
    MATCH("Maqolning boshini oxiri bilan juftlang", [(a.rstrip(",— ").strip(), b) for a, b, _ in PROVERBS[:6]], d=2),
]
T.topic("proverbs", "💎", L("Maqollar", "Proverbs", "Пословицы"), C2,
        "Maqol — xalq yaratgan qisqa, ibratli gap. U hayot tajribasini ifodalaydi.\n"
        "Misollar: “Birlashgan o‘zar, birlashmagan to‘zar.” (birlik haqida)\n"
        "“Olim bo‘lsang, olam seniki.” (ilm haqida)\n"
        "Maqolni o‘qib, u qaysi fazilatni ulug‘lashini o‘ylang.", items=items)

items = []
for riddle, answer, wrong in RIDDLES:
    items.append(Q(f"Topishmoqni toping: “{riddle}”", answer, wrong, d=1 if len(items) < 12 else 2, x=f"Javob: {answer.lower()}."))
items += [
    TF("Topishmoqda narsa nomi aytilmaydi, uning belgilari ta’riflanadi.", True, x="Tinglovchi belgilarga qarab narsani topadi."),
    Q("Topishmoq nima?", "Narsaning belgilarini yashirin ta’riflab, topishni so‘rash", ["Uzun hikoya", "Qo‘shiq", "Ibratli qisqa gap"], d=2,
      x="Maqol — ibratli gap, topishmoq esa jumboq."),
]
T.topic("riddles", "🧩", L("Topishmoqlar", "Riddles", "Загадки"), C2,
        "Topishmoqda narsaning nomi aytilmaydi — uning belgilari ta’riflanadi.\n"
        "Javob topish uchun har bir belgini o‘ylang: qanday? nima qiladi? qayerda bo‘ladi?\n"
        "Misol: “Oyog‘i yo‘q — yuradi, tili yo‘q — vaqtni aytadi.” (soat)", items=items)

items = []
for work, kind in FOLK:
    items.append(Q(f"{work} qanday asar?", kind, [k for k in ("Xalq ertagi", "Xalq dostoni", "Maqol", "Topishmoq") if k != kind],
                   x=f"{work} — {kind.lower()}, xalq og‘zaki ijodi namunasi."))
items += [
    Q("Ertaklar qanday yaratilgan?", "Xalq og‘zaki ijodida", ["Bitta olim yozgan", "Gazetada chiqqan", "Kompyuterda yaratilgan"], x="Ertaklarni xalq to‘qigan, og‘izdan og‘izga o‘tib kelgan."),
    Q("Ko‘pchilik ertaklar qanday so‘zlar bilan boshlanadi?", "Bor ekan-u, yo‘q ekan…", ["Hurmatli do‘stlar…", "Bugun darsda…", "Ob-havo ma’lumoti…"], x="An’anaviy ertak boshlanmasi."),
    Q("Ertaklarda odatda nima g‘alaba qiladi?", "Yaxshilik", ["Yomonlik", "Dangasalik", "Yolg‘on"], x="Ertaklarda yaxshilik yomonlik ustidan g‘alaba qozonadi."),
    Q("“Zumrad va Qimmat” ertagida mehnatkash va odobli qiz kim?", "Zumrad", ["Qimmat", "O‘gay ona", "Kampir"], d=2, x="Zumrad — mehnatkash va odobli, Qimmat esa dangasa va qo‘pol."),
    Q("“Alpomish” dostonining bosh qahramoni kim?", "Alpomish", ["Go‘ro‘g‘li", "Zumrad", "Nasriddin"], d=2, x="Doston uning nomi bilan ataladi."),
    Q("Dostonlarni xalq orasida kim kuylab aytgan?", "Baxshilar", ["Sotuvchilar", "Dehqonlar", "Hunarmandlar"], d=2, x="Baxshilar dostonlarni do‘mbira jo‘rligida kuylaydi."),
    TF("Ertaklarda hayvonlar ham gapirishi mumkin.", True, x="Masalan, hayvonlar haqidagi ertaklarda."),
    TF("Xalq ertaklarining bitta aniq muallifi bor.", False, x="Ertaklar — xalq og‘zaki ijodi."),
    TF("“Ur to‘qmoq” — o‘zbek xalq ertagi.", True, x="U xalq og‘zaki ijodiga mansub."),
    MATCH("Asarni turi bilan juftlang", [("“Zumrad va Qimmat”", "ertak"), ("“Alpomish”", "doston"), ("“Olim bo‘lsang, olam seniki”", "maqol"),
                                         ("“Oyog‘i yo‘q — yuradi”", "topishmoq")], d=2),
    Q("Qaysi biri xalq og‘zaki ijodiga kirmaydi?", "Gazeta maqolasi", ["Ertak", "Maqol", "Topishmoq"], d=2, x="Gazeta maqolasini muayyan muallif yozadi."),
    Q("Ertakdagi “Bor ekan-u, yo‘q ekan” qismi nima deyiladi?", "Ertak boshlanmasi", ["Ertak oxiri", "Maqol", "Sarlavha"], d=3, x="Ertaklar ko‘pincha an’anaviy boshlanma bilan boshlanadi."),
]
T.topic("folk", "🏺", L("Ertak va dostonlar", "Folk tales and epics", "Сказки и дастаны"), C2,
        "Xalq og‘zaki ijodi — xalq yaratgan va og‘izdan og‘izga o‘tib kelgan asarlar: ertak, doston, maqol, topishmoq, qo‘shiq.\n"
        "• Ertak — to‘qima voqea; ko‘pincha “Bor ekan-u, yo‘q ekan…” deb boshlanadi. Unda yaxshilik g‘alaba qiladi.\n"
        "• Doston — qahramonlar haqida kuylab aytiladigan katta asar: “Alpomish”, “Go‘ro‘g‘li”. Dostonlarni baxshilar kuylaydi.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["proverbs", "riddles", "folk"], C2)

# ============================================================ 3-chorak
items = [
    Q("She’rning bir qatori nima deyiladi?", "Misra", ["Band", "Sarlavha", "Xat"], x="She’r misralardan tuziladi."),
    Q("She’rdagi misralar guruhi nima deyiladi?", "Band", ["Misra", "Qofiya", "Bob"], x="Bir necha misra bandni tashkil etadi."),
    Q("Misralar oxiridagi ohangdosh so‘zlar nima deyiladi?", "Qofiya", ["Band", "Sarlavha", "Maqol"], x="Masalan: bahor — qor, gul — bulbul."),
    Q("Qaysi so‘zlar qofiyadosh?", "tong — rang", ["kitob — daftar", "olma — nok", "uy — maktab"], d=2, x="tong va rang oxiri ohangdosh: -ng."),
    Q("Qaysi so‘zlar qofiyadosh?", "gul — bulbul", ["gul — daraxt", "qush — suv", "kitob — qalam"], x="gul — bulbul: oxiri “-ul”."),
    Q("Qaysi so‘zlar qofiyadosh?", "bahor — anor", ["bahor — kuz", "anor — olma", "qor — yomg‘ir"], x="bahor — anor: oxiri “-or”."),
    Q("Qaysi so‘zlar qofiyadosh?", "tog‘ — bog‘", ["tog‘ — daryo", "bog‘ — gul", "tosh — suv"], x="tog‘ — bog‘: oxiri “-og‘”."),
    Q("Hikoya she’rdan nimasi bilan farq qiladi?", "Oddiy gaplar bilan, misralarsiz yoziladi", ["Doim qofiyali bo‘ladi", "Faqat kuylanadi", "Ikki so‘zdan iborat bo‘ladi"], d=2,
      x="She’r misralarga bo‘linadi va ohangdor bo‘ladi, hikoya — nasr."),
    Q("Masalning oxirida odatda nima bo‘ladi?", "Ibratli xulosa", ["Topishmoq", "Qofiya", "Savol"], d=2, x="Masalda voqeadan ibrat chiqariladi."),
    Q("Masallarda ko‘pincha kimlar odamlarday gapiradi?", "Hayvonlar", ["Faqat podshohlar", "Faqat bolalar", "Hech kim"], x="Hayvonlar orqali odamlarning fe’l-atvori ko‘rsatiladi."),
    TF("She’r misra va bandlardan tuziladi.", True, x="Misralar birlashib band hosil qiladi."),
    TF("Hikoyada qofiya bo‘lishi shart.", False, x="Hikoya nasrda yoziladi, qofiya shart emas."),
    TF("Masaldan ibrat chiqariladi.", True, x="Masal — ibratli qisqa hikoya."),
    MATCH("Janrni ta’rifi bilan juftlang", [("Ertak", "to‘qima voqea, yaxshilik g‘alaba qiladi"), ("She’r", "misra va qofiyali asar"),
                                          ("Masal", "hayvonlar orqali ibrat"), ("Hikoya", "hayotiy voqea haqida nasriy asar"),
                                          ("Topishmoq", "narsa belgilari yashirin ta’riflanadi")], d=2),
    ORDER("So‘zlardan gap tuzing", "She’r misra va bandlardan tuziladi", d=1),
    ORDER("So‘zlardan gap tuzing", "Masaldan ibrat olamiz", d=1),
]
T.topic("genres", "🎭", L("She’r, hikoya, masal", "Poems, stories, fables", "Стихи, рассказы, басни"), C3,
        "• She’r — misralarga bo‘linadigan, ohangdor asar. Misralar bandga birlashadi, oxiridagi ohangdosh so‘zlar — qofiya\n"
        "  (gul — bulbul, tog‘ — bog‘).\n"
        "• Hikoya — hayotiy voqea haqidagi kichik nasriy asar.\n"
        "• Masal — hayvonlar orqali odamlarga ibrat beradigan qisqa asar; oxirida xulosa bo‘ladi.", items=items)

items = []
for work, author in WORKS[:9]:
    items.append(Q(f"{work} asarining muallifi kim?", author, rnd.sample([a for a in AUTHORS if a != author], 3),
                   d=1 if work in ("“Shum bola”", "“Sariq devni minib”", "“Bolalik”", "“O‘tkan kunlar”", "“Xamsa”", "“Boburnoma”") else 2, x=f"{work} — {author} asari."))
items += [
    Q("O‘zbekiston Respublikasi Davlat madhiyasi so‘zlarining muallifi kim?", "Abdulla Oripov", ["Alisher Navoiy", "G‘afur G‘ulom", "Oybek"],
      x="Madhiya so‘zlari — Abdulla Oripov, musiqasi — Mutal Burhonov."),
    Q("Buyuk shoir Alisher Navoiy qaysi shaharda tug‘ilgan?", "Hirotda", ["Samarqandda", "Buxoroda", "Toshkentda"], d=2, x="Alisher Navoiy 1441-yilda Hirotda tug‘ilgan."),
    Q("Zahiriddin Muhammad Bobur qaysi shaharda tug‘ilgan?", "Andijonda", ["Xivada", "Termizda", "Nukusda"], d=2, x="Bobur 1483-yilda Andijonda tug‘ilgan."),
    Q("Zulfiya kim bo‘lgan?", "Shoira", ["Rassom", "Olim", "Bastakor"], d=2, x="Zulfiya — mashhur o‘zbek shoirasi."),
    TF("“Shum bola” asarini G‘afur G‘ulom yozgan.", True, x="Bu — G‘afur G‘ulomning mashhur qissasi."),
    TF("“Sariq devni minib” asarini Alisher Navoiy yozgan.", False, x="Uni Xudoyberdi To‘xtaboyev yozgan."),
    TF("Oybek “Bolalik” asarida o‘z bolaligi haqida hikoya qiladi.", True, d=2, x="“Bolalik” — Oybekning xotira qissasi."),
    MATCH("Asarni muallifi bilan juftlang", [(w, a) for w, a in WORKS[:6]], d=2),
]
T.topic("authors", "✒️", L("Adiblar va asarlar", "Writers and their works", "Писатели и произведения"), C3,
        "Bilib qo‘ying:\n"
        "• Alisher Navoiy (1441, Hirot) — buyuk shoir, “Xamsa” muallifi.\n"
        "• Zahiriddin Muhammad Bobur (1483, Andijon) — “Boburnoma” muallifi.\n"
        "• G‘afur G‘ulom — “Shum bola”; Oybek — “Bolalik”; Xudoyberdi To‘xtaboyev — “Sariq devni minib”.\n"
        "• Abdulla Oripov — O‘zbekiston Davlat madhiyasi so‘zlari muallifi.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["genres", "authors"], C3)

# ============================================================ 4-chorak
K1 = ("Kuz kirdi. Bog‘dagi daraxtlar sarg‘aya boshladi. Dilnoza buvisiga olma terishda yordam berdi. "
      "Ular eng chiroyli olmalarni savatga solib, qo‘shnilarga ham ulashishdi. Qo‘shni xola ularga rahmat aytib, "
      "issiq somsa chiqardi. Dilnoza: “Yaxshilik qilsang, yaxshilik qaytar ekan”, deb o‘yladi.")
K2 = ("Jasur futbol musobaqasida gol ura olmadi va xafa bo‘ldi. Murabbiy uning yelkasiga qo‘lini qo‘yib: "
      "“Har bir mag‘lubiyat — yangi saboq. Ertadan ko‘proq mashq qilamiz”, dedi. Jasur har kuni mashq qildi. "
      "Keyingi o‘yinda u ikki gol urdi va jamoasi g‘alaba qozondi.")
K3 = ("Ukam Bekzod qo‘g‘irchoq teatriga birinchi marta bordi. Sahnada tulki va quyon haqida ertak ko‘rsatildi. "
      "Tulki quyonni aldamoqchi bo‘ldi, ammo aqlli quyon uning hiylasini sezib qoldi. Tomosha oxirida hamma qarsak chaldi. "
      "Uyga qaytgach, Bekzod ertakni boshidan oxirigacha menga so‘zlab berdi.")
items = [
    Q("Voqea qaysi faslda bo‘ldi?", "Kuzda", ["Bahorda", "Yozda", "Qishda"], text=K1, x="“Kuz kirdi.”"),
    Q("Dilnoza kimga yordam berdi?", "Buvisiga", ["Onasiga", "O‘qituvchisiga", "Ukasiga"], text=K1, x="U buvisiga olma terishda yordam berdi."),
    Q("Ular olmalarni kimlarga ulashishdi?", "Qo‘shnilarga", ["Sotuvchilarga", "Sinfdoshlarga", "Mehmonlarga"], text=K1, x="Qo‘shnilarga ham ulashishdi."),
    Q("Hikoyaning asosiy fikri qaysi?", "Yaxshilik qilsang, yaxshilik qaytadi", ["Olma faqat kuzda pishadi", "Somsa mazali taom", "Bog‘da ishlash qiyin"], text=K1, d=2,
      x="Dilnozaning o‘yi hikoyaning asosiy fikrini aytadi."),
    Q("Jasur nima uchun xafa bo‘ldi?", "Gol ura olmadi", ["Jarohat oldi", "O‘yinga kechikdi", "To‘pi yo‘qoldi"], text=K2, x="U musobaqada gol ura olmadi."),
    Q("Murabbiy Jasurga nima dedi?", "Mag‘lubiyat — yangi saboq, ko‘proq mashq qilamiz", ["Futbolni tashla", "Sen eng yomon o‘yinchisan", "Endi o‘ynamaysan"], text=K2,
      x="Murabbiy uni ruhlantirdi."),
    Q("Keyingi o‘yinda Jasur nechta gol urdi?", "Ikkita", ["Bitta", "Uchta", "Hech qancha"], text=K2, x="U ikki gol urdi."),
    Q("Hikoyadan qanday xulosa chiqadi?", "Qunt bilan mashq qilgan kishi yutadi", ["Xafa bo‘lsang, tashlab ketish kerak", "Futbol zararli", "Murabbiylar qattiqqo‘l"], text=K2, d=2,
      x="Jasur har kuni mashq qilib, natijaga erishdi."),
    Q("Bekzod qayerga bordi?", "Qo‘g‘irchoq teatriga", ["Hayvonot bog‘iga", "Sirkka", "Kutubxonaga"], text=K3, x="U qo‘g‘irchoq teatriga birinchi marta bordi."),
    Q("Ertakda kim kimni aldamoqchi bo‘ldi?", "Tulki quyonni", ["Quyon tulkini", "Bo‘ri quyonni", "Ayiq tulkini"], text=K3, x="Tulki quyonni aldamoqchi bo‘ldi."),
    Q("Quyon qanday ekan?", "Aqlli", ["Dangasa", "Qo‘rqoq", "Maqtanchoq"], text=K3, x="“Aqlli quyon uning hiylasini sezib qoldi.”"),
    Q("Hikoya kimning tilidan aytilgan?", "Bekzodning akasi yoki opasining", ["Tulkining", "Quyonning", "Bekzodning o‘zining"], text=K3, d=3,
      x="“Ukam Bekzod …” — hikoyachi Bekzodning akasi yoki opasi."),
    TF("Dilnoza olmalarni bozorga sotib yubordi.", False, text=K1, x="Ular olmalarni qo‘shnilarga ulashishdi."),
    TF("Jasur mag‘lubiyatdan keyin har kuni mashq qildi.", True, text=K2, x="Matnda shunday yozilgan."),
    TF("Tomosha oxirida hamma qarsak chaldi.", True, text=K3, x="Matnda shunday yozilgan."),
    TF("Bekzod qo‘g‘irchoq teatriga ko‘p marta borgan edi.", False, text=K3, x="U birinchi marta bordi."),
]
T.topic("think", "💡", L("O‘qib, fikrlaymiz", "Read and think", "Читаем и думаем"), C4,
        "Hikoyani o‘qigach:\n"
        "• voqea qachon va qayerda bo‘lganini aniqlang;\n"
        "• qahramonlar nima qilganini va nima uchun qilganini o‘ylang;\n"
        "• hikoyadan qanday saboq olish mumkinligini bir gap bilan ayting.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["think", "genres", "proverbs"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["understand_story", "infer", "proverbs", "riddles", "folk", "genres", "authors", "think"], C4, level=3)

T.write()
