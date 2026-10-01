"""O‘qish, 1-sinf: so‘z va bo‘g‘inlarni o‘qish, qisqa matnni tushunish, oila, do‘stlik, odob, hayvonlar, fasllar,
topishmoq va tez aytish, she’r va qofiya, ertak, maqol, Vatan va bayramlar.

1-sinf o‘quvchisi (7 yosh) endigina o‘qishni o‘rganyapti: matnlar juda qisqa (2–4 gap), savol ovozda o‘qib beriladi,
matnni (`text=`) esa bola o‘zi o‘qiydi. Javoblar qisqa, ko‘pincha rasm (emoji).
Hikoyalar, ertaklar, she’rlar, topishmoqlar va tez aytishlar o‘zimiz yozgan (darsliklardan ko‘chirilmagan);
maqollar — xalq og‘zaki ijodi. Emoji — faqat Android 9 da bor oddiylari.
Qayta yaratish: python3 tool/content/school/reading_g1.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403

rnd = random.Random(11)
T = Course("reading", 1, L("O‘qish", "Reading", "Чтение"))

C1 = "1-chorak. Salom, maktab!"
C2 = "2-chorak. Oilam va do‘stlarim"
C3 = "3-chorak. Tabiat va hayvonlar"
C4 = "4-chorak. Ertak, maqol va bayramlar"


# ============================================================ 1-chorak
def PIC(word, em, wrong, d=1):
    """So‘zni o‘qib, rasmini topish: so‘z ekranda, javob — emoji."""
    return Q("So‘zni o‘qing va rasmini toping", em, wrong, d=d, text=word, x=f"“{word}” — {em}")


def WORD(em, word, wrong, d=1):
    """Rasmga qarab, to‘g‘ri yozilgan so‘zni o‘qib topish."""
    return Q("Rasmga mos so‘zni toping", word, wrong, d=d, e=em, x=f"{em} — “{word}”. Har bir harfga qarang.")


items = [
    PIC("olma", "🍎", ["🍐", "🍇", "🍌"]),
    PIC("nok", "🍐", ["🍎", "🍋", "🍇"]),
    PIC("uzum", "🍇", ["🍉", "🍓", "🍐"]),
    PIC("tarvuz", "🍉", ["🍈", "🍅", "🍎"]),
    PIC("baliq", "🐟", ["🐸", "🐦", "🐢"]),
    PIC("mushuk", "🐱", ["🐶", "🐭", "🐰"]),
    PIC("it", "🐶", ["🐱", "🐎", "🐑"]),
    PIC("ot", "🐎", ["🐶", "🐄", "🐑"]),
    PIC("oy", "🌙", ["🏠", "☀️", "⭐"]),
    PIC("uy", "🏠", ["🌙", "🏫", "🚗"]),
    PIC("quyon", "🐰", ["🐱", "🐻", "🦊"]),
    PIC("kitob", "📖", ["✏️", "🎒", "⏰"]),
    PIC("sut", "🥛", ["🍞", "🥚", "🍯"]),
    PIC("tuxum", "🥚", ["🍞", "🥛", "🍋"], d=2),
    PIC("kapalak", "🦋", ["🐝", "🐞", "🐦"], d=2),
    PIC("daraxt", "🌳", ["🌷", "🌵", "🍄"], d=2),
    WORD("🌙", "oy", ["uy", "ot", "oq"]),
    WORD("🐎", "ot", ["it", "o‘t", "ol"], d=2),
    WORD("☀️", "quyosh", ["quyon", "qoshiq", "qovoq"], d=2),
    WORD("🐰", "quyon", ["quyosh", "qovun", "qo‘y"], d=2),
    WORD("🐱", "mushuk", ["kuchuk", "mushak", "musiqa"], d=2),
    WORD("✏️", "qalam", ["qadam", "qalpoq", "qanot"], d=2),
    WORD("❄️", "qor", ["qo‘y", "qop", "qosh"], d=3),
    Q("Qaysi so‘z ortiqcha?", "mushuk", ["olma", "nok", "uzum"], text="olma   nok   mushuk   uzum", d=2,
      x="Olma, nok, uzum — mevalar. Mushuk esa hayvon."),
    Q("Qaysi so‘z ortiqcha?", "qalam", ["sigir", "ot", "qo‘y"], text="sigir   ot   qalam   qo‘y", d=2,
      x="Sigir, ot, qo‘y — hayvonlar. Qalam esa o‘quv quroli."),
    TF("So‘z rasmga mos keladi.", True, text="baliq", e="🐟", x="To‘g‘ri: “baliq” — 🐟."),
    TF("So‘z rasmga mos keladi.", False, text="quyon", e="🐱", x="Rasmda — mushuk 🐱. “quyon” esa — 🐰."),
    MATCH("Meva nomini rasmga moslang", [("olma", "🍎"), ("nok", "🍐"), ("uzum", "🍇"), ("tarvuz", "🍉"), ("limon", "🍋"),
                                         ("gilos", "🍒")], d=1, x="Har bir so‘zni bo‘g‘inlab o‘qing va uning rasmini toping."),
    MATCH("Hayvon nomini rasmga moslang", [("mushuk", "🐱"), ("it", "🐶"), ("sigir", "🐄"), ("ot", "🐎"), ("quyon", "🐰"),
                                           ("baliq", "🐟")], d=2, x="“it” va “ot” so‘zlari bitta harf bilan farq qiladi — diqqat qiling."),
]
T.topic("words", "📖", L("So‘zni o‘qiymiz", "Reading words", "Читаем слова"), C1,
        "So‘zni bo‘g‘inlab, shoshmasdan o‘qing: ol-ma → olma.\n"
        "• O‘qigan so‘zingizni rasm bilan solishtiring: olma — 🍎, baliq — 🐟.\n"
        "• Bitta harf o‘zgarsa, so‘z ham o‘zgaradi: oy 🌙 — uy 🏠, ot 🐎 — it 🐶.\n"
        "Har bir harfga diqqat qiling!", items=items)


def SYL(word, n, wrong, split, d=1):
    return Q("Bu so‘zda nechta bo‘g‘in bor?", n, wrong, d=d, text=word,
             x=f"{split} — {n} bo‘g‘in. So‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bo‘ladi.")


def PART(text, em, a, wrong, word, d=1):
    return Q("Qaysi bo‘g‘in yetishmayapti?", a, wrong, d=d, text=text, e=em, x=f"{word} {em}")


items = [
    SYL("non", "1 ta", ["2 ta", "3 ta"], "non"),
    SYL("olma", "2 ta", ["1 ta", "3 ta"], "ol-ma"),
    SYL("kitob", "2 ta", ["1 ta", "3 ta"], "ki-tob"),
    SYL("uy", "1 ta", ["2 ta", "3 ta"], "uy"),
    SYL("bola", "2 ta", ["1 ta", "3 ta", "4 ta"], "bo-la"),
    SYL("kapalak", "3 ta", ["1 ta", "2 ta", "4 ta"], "ka-pa-lak", d=2),
    SYL("chumoli", "3 ta", ["1 ta", "2 ta", "4 ta"], "chu-mo-li", d=2),
    SYL("o‘qituvchi", "4 ta", ["2 ta", "3 ta", "5 ta"], "o‘-qi-tuv-chi", d=3),
    PART("ol…", "🍎", "ma", ["mo", "na", "ta"], "ol + ma = olma"),
    PART("ki…", "📖", "tob", ["top", "tub", "bot"], "ki + tob = kitob"),
    PART("…lam", "✏️", "qa", ["ka", "qo", "ga"], "qa + lam = qalam"),
    PART("ba…", "🐟", "liq", ["loq", "lik", "lish"], "ba + liq = baliq"),
    PART("qu…", "🐰", "yon", ["yosh", "yun", "von"], "qu + yon = quyon", d=2),
    PART("qu…", "☀️", "yosh", ["yon", "yoz", "yol"], "qu + yosh = quyosh", d=2),
    PART("…vuz", "🍉", "tar", ["tor", "ter", "dar"], "tar + vuz = tarvuz", d=2),
    ORDER("Bo‘g‘inlardan so‘z yasang", "da-raxt", sep="-", x="da + raxt = daraxt 🌳"),
    ORDER("Bo‘g‘inlardan so‘z yasang", "ka-pa-lak", sep="-", x="ka + pa + lak = kapalak 🦋"),
    ORDER("Bo‘g‘inlardan so‘z yasang", "ma-shi-na", sep="-", d=2, x="ma + shi + na = mashina 🚗"),
    ORDER("Bo‘g‘inlardan so‘z yasang", "po-mi-dor", sep="-", d=2, x="po + mi + dor = pomidor 🍅"),
    ORDER("Bo‘g‘inlardan so‘z yasang", "o‘-yin-choq", sep="-", d=3, x="o‘ + yin + choq = o‘yinchoq"),
    Q("Qaysi so‘z bir bo‘g‘inli?", "gul", ["olma", "kitob", "bola"], x="gul — bitta bo‘g‘in: unda bitta unli (u) bor."),
    Q("Qaysi so‘z uch bo‘g‘inli?", "pomidor", ["non", "olma", "uzum"], d=2, x="po-mi-dor — uchta bo‘g‘in."),
    Q("Qaysi harf unli?", "a", ["b", "k", "m"], x="Unlilar: a, o, u, e, i, o‘. Bo‘g‘in unli harf atrofida yasaladi."),
    Q("“qalam” so‘zi qanday bo‘g‘inlanadi?", "qa-lam", ["q-alam", "qala-m", "qal-a-m"], d=2, x="qa-lam: har bir bo‘g‘inda bitta unli bor."),
    TF("“ona” so‘zida 2 ta bo‘g‘in bor.", True, x="o-na — 2 ta bo‘g‘in."),
    TF("“tog‘” so‘zida 2 ta bo‘g‘in bor.", False, x="tog‘ — bitta bo‘g‘in: unda bitta unli (o) bor."),
    MATCH("So‘zni bo‘g‘inlari bilan juftlang", [("olma", "ol-ma"), ("kitob", "ki-tob"), ("bola", "bo-la"), ("daftar", "daf-tar"),
                                               ("quyosh", "qu-yosh"), ("kapalak", "ka-pa-lak")], d=1,
          x="So‘z bo‘g‘inlarga ajratilganda chiziqcha qo‘yiladi: ol-ma."),
]
T.topic("syllables", "🔤", L("Bo‘g‘inlab o‘qiymiz", "Reading by syllables", "Читаем по слогам"), C1,
        "Bo‘g‘in — so‘zning bir nafasda aytiladigan qismi.\n"
        "• So‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bo‘ladi. Unlilar: a, o, u, e, i, o‘.\n"
        "• Misollar: non (1 bo‘g‘in), ol-ma (2 bo‘g‘in), ka-pa-lak (3 bo‘g‘in).\n"
        "Uzun so‘zni bo‘g‘inlab o‘qisangiz, oson bo‘ladi.", items=items)

M1 = "Bugun Ali birinchi marta maktabga bordi. Uning sumkasi yangi. Ustoz bolalarni jilmayib kutib oldi."
M2 = "Zarina daftariga harflar yozdi. Harflar chiroyli chiqdi. Ustoz uni maqtadi."
M3 = "Qo‘ng‘iroq chalindi. Tanaffus boshlandi. Bolalar hovlida o‘ynashdi."
M4 = "Bobur qalamini uyda unutib qoldirdi. Sardor unga o‘z qalamini berdi. Bobur: “Rahmat!” — dedi."
M5 = "Sinfimiz katta va yorug‘. Derazada gullar bor. Biz ularga navbat bilan suv quyamiz."
items = [
    Q("Ali qayerga bordi?", "Maktabga", ["Bozorga", "Bog‘ga", "Do‘konga"], text=M1, x="“Ali birinchi marta maktabga bordi.”"),
    Q("Alining nimasi yangi?", "Sumkasi", ["Kitobi", "Qalami", "Velosipedi"], text=M1, x="“Uning sumkasi yangi.”"),
    Q("Bolalarni kim kutib oldi?", "Ustoz", ["Onasi", "Bobosi", "Oshpaz"], text=M1, x="Ustoz bolalarni jilmayib kutib oldi."),
    TF("Ali maktabga birinchi marta bordi.", True, text=M1, x="Matnda shunday yozilgan."),
    Q("Zarina daftariga nima yozdi?", "Harflar", ["Sonlar", "She’r", "Ismini"], text=M2, x="“Zarina daftariga harflar yozdi.”"),
    Q("Zarinani kim maqtadi?", "Ustoz", ["Dugonasi", "Buvisi", "Akasi"], text=M2, x="Harflar chiroyli chiqqani uchun ustoz uni maqtadi."),
    TF("Zarinaning harflari xunuk chiqdi.", False, text=M2, x="Harflar chiroyli chiqdi."),
    Q("Qo‘ng‘iroq chalingach, nima boshlandi?", "Tanaffus", ["Dars", "Bayram", "Konsert"], text=M3, x="“Qo‘ng‘iroq chalindi. Tanaffus boshlandi.”"),
    Q("Bolalar qayerda o‘ynashdi?", "Hovlida", ["Sinfda", "Uyda", "Bog‘chada"], text=M3, x="“Bolalar hovlida o‘ynashdi.”"),
    Q("Bobur nimani uyda qoldirdi?", "Qalamini", ["Kitobini", "Sumkasini", "Daftarini"], text=M4, x="Bobur qalamini uyda unutib qoldirdi."),
    Q("Boburga kim yordam berdi?", "Sardor", ["Ustoz", "Zarina", "Onasi"], text=M4, x="Sardor unga o‘z qalamini berdi."),
    Q("Bobur Sardorga nima dedi?", "Rahmat!", ["Salom!", "Xayr!", "Kechirasiz!"], text=M4, x="Yordam olganda “Rahmat!” deymiz."),
    Q("Sardor qanday bola?", "Mehribon", ["Dangasa", "Maqtanchoq", "Qo‘pol"], text=M4, d=2,
      x="U do‘stiga o‘z qalamini berib, yordam qildi."),
    Q("Derazada nima bor?", "Gullar", ["Kitoblar", "Mushuk", "Soat"], text=M5, x="“Derazada gullar bor.”"),
    Q("Bolalar gullarga nima qilishadi?", "Suv quyishadi", ["Uzishadi", "Sotishadi", "Bo‘yashadi"], text=M5, d=2,
      x="“Biz ularga navbat bilan suv quyamiz.”"),
    TF("Sinf kichik va qorong‘i.", False, text=M5, x="Sinf katta va yorug‘."),
    Q("Hikoyaga mos sarlavhani tanlang.", "Maktabdagi birinchi kun", ["Qishki o‘yin", "Bog‘dagi mushuk", "Bozorda"], text=M1, d=2,
      x="Hikoya Alining maktabdagi birinchi kuni haqida."),
    Q("Maktabda bizga kim dars beradi?", "O‘qituvchi", ["Shifokor", "Haydovchi", "Sotuvchi"], e="🏫", x="O‘qituvchi — ustoz bizga dars beradi."),
    Q("Qaysi biri o‘quv quroli?", "Qalam", ["Qoshiq", "Choynak", "Yostiq"], e="🎒", x="Qalam bilan yozamiz — u o‘quv quroli."),
    ORDER("So‘zlardan gap tuzing", "Men maktabga boraman", x="Gap katta harf bilan boshlanadi: Men maktabga boraman."),
    ORDER("So‘zlardan gap tuzing", "Ustoz bizga ertak o‘qib berdi", d=2, x="Kim? — Ustoz. Nima qildi? — ertak o‘qib berdi."),
    MATCH("O‘quv qurolini rasmga moslang", [("kitob", "📖"), ("qalam", "✏️"), ("daftar", "📓"), ("sumka", "🎒"), ("qaychi", "✂️"),
                                           ("chizg‘ich", "📏")], d=1, x="Bular — maktabda kerak bo‘ladigan o‘quv qurollari."),
]
T.topic("school", "🏫", L("Maktabga birinchi qadam", "First steps at school", "Первые шаги в школе"), C1,
        "Maktab — bilim uyi. Maktabda ustoz bizga o‘qish va yozishni o‘rgatadi.\n"
        "• Matnni o‘qigach, savolga javobni matndan toping: Kim? Nima qildi? Qayerda?\n"
        "• Misol: “Ali maktabga bordi.” Kim? — Ali. Qayerga bordi? — maktabga.\n"
        "Javob topolmasangiz, matnni yana bir marta sekin o‘qing.", items=items)

T.topic("understand", "📚", L("Matnni tushunish (aralash)", "Reading practice", "Понимание текста"), C1,
        "Matnni boshidan oxirigacha o‘qing. Kim, nima, qayerda va nima sababdan degan savollarga matndan dalil toping. "
        "Sarlavha matndagi asosiy voqeani ifodalashi kerak.",
        gen="comprehension", levels=[dict(options=n, infer=False) for n in (2, 3, 4)])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["words", "syllables", "school"], C1)

# ============================================================ 2-chorak
F1 = "Bu — Madinaning oilasi. Uning dadasi, onasi, akasi va ukasi bor. Ular kechqurun birga choy ichishadi."
F2 = "Buvim tandirda non yopdi. Non issiq va mazali. Men buvimga rahmat aytdim."
F3 = "Dadam ishdan charchab keldi. Men unga shippagini olib keldim. Dadam meni quchoqladi."
F4 = "Onam bilan bozorga bordik. Biz olma va sabzi oldik. Men sumkani ko‘tarishga yordam berdim."
F5 = "Bobom bog‘da ishlayotgan edi. Men unga suv olib bordim. Bobom menga eng katta olmani uzib berdi."
items = [
    Q("Matn kimning oilasi haqida?", "Madinaning", ["Alining", "Zarinaning", "Ustozning"], text=F1, x="“Bu — Madinaning oilasi.”"),
    Q("Oila kechqurun nima qiladi?", "Birga choy ichadi", ["Futbol o‘ynaydi", "Bozorga boradi", "Kino ko‘radi"], text=F1,
      x="“Ular kechqurun birga choy ichishadi.”"),
    TF("Madinaning ukasi bor.", True, text=F1, x="Matnda: “Uning dadasi, onasi, akasi va ukasi bor.”"),
    Q("Oilada nechta bola bor?", "3 ta", ["1 ta", "2 ta", "4 ta"], text=F1, d=3, x="Madina, uning akasi va ukasi — 3 ta bola."),
    Q("Buvi nima yopdi?", "Non", ["Somsa", "Palov", "Chuchvara"], text=F2, x="“Buvim tandirda non yopdi.”"),
    Q("Non qanday ekan?", "Issiq va mazali", ["Sovuq va qattiq", "Kuygan", "Sho‘r"], text=F2, x="“Non issiq va mazali.”"),
    Q("Bola buvisiga nima dedi?", "Rahmat", ["Xayr", "Kechirasiz", "Salom"], text=F2, x="“Men buvimga rahmat aytdim.”"),
    Q("Dada qayerdan keldi?", "Ishdan", ["Bozordan", "Maktabdan", "Bog‘dan"], text=F3, x="“Dadam ishdan charchab keldi.”"),
    Q("Bola dadasiga nima olib keldi?", "Shippagini", ["Choyini", "Gazetasini", "Kitobini"], text=F3, x="Bola dadasiga shippagini olib keldi."),
    Q("Dada bolani nima qildi?", "Quchoqladi", ["Urishdi", "Uxlatdi", "Chaqirdi"], text=F3, x="“Dadam meni quchoqladi.”"),
    Q("Bola qanday ekan?", "G‘amxo‘r", ["Dangasa", "Injiq", "Qo‘pol"], text=F3, d=2, x="U charchagan dadasiga g‘amxo‘rlik qildi."),
    Q("Ular qayerga borishdi?", "Bozorga", ["Maktabga", "Bog‘ga", "Mehmonga"], text=F4, x="“Onam bilan bozorga bordik.”"),
    Q("Ular nima olishdi?", "Olma va sabzi", ["Non va sut", "Nok va uzum", "Guruch va go‘sht"], text=F4, x="“Biz olma va sabzi oldik.”"),
    Q("Bola onasiga qanday yordam berdi?", "Sumkani ko‘tardi", ["Pul sanadi", "Ovqat pishirdi", "Idish yuvdi"], text=F4,
      x="“Men sumkani ko‘tarishga yordam berdim.”"),
    Q("Bobo qayerda ishlayotgan edi?", "Bog‘da", ["Dalada", "Do‘konda", "Maktabda"], text=F5, x="“Bobom bog‘da ishlayotgan edi.”"),
    Q("Bola bobosiga nima olib bordi?", "Suv", ["Non", "Choy", "Olma"], text=F5, x="“Men unga suv olib bordim.”"),
    TF("Bobo nevarasiga eng kichik olmani berdi.", False, text=F5, x="Bobo eng katta olmani uzib berdi."),
    Q("Dadamning otasi kim bo‘ladi?", "Bobom", ["Amakim", "Tog‘am", "Akam"], d=2, x="Dadamning otasi — bobom."),
    Q("Onamning singlisi kim bo‘ladi?", "Xolam", ["Ammam", "Buvim", "Opam"], d=2, x="Onaning opa-singlisi — xola, otaning opa-singlisi — amma."),
    MATCH("Kim kim bo‘ladi? Juftlang", [("dadamning otasi", "bobom"), ("onamning onasi", "buvim"), ("dadamning akasi", "amakim"),
                                        ("onamning akasi", "tog‘am"), ("onamning opasi", "xolam"), ("dadamning opasi", "ammam")], d=3,
          x="Otaning aka-ukasi — amaki, onaning aka-ukasi — tog‘a."),
    ORDER("So‘zlardan gap tuzing", "Men oilamni yaxshi ko‘raman", x="Oila — eng yaqin odamlarimiz."),
    ORDER("So‘zlardan gap tuzing", "Dadam bilan bog‘da ishladik", d=2, x="Kim bilan? — dadam bilan. Qayerda? — bog‘da."),
]
T.topic("family", "👪", L("Mening oilam", "My family", "Моя семья"), C2,
        "Oila — eng yaqin odamlarimiz: ota-ona, aka-uka, opa-singil, bobo va buvi.\n"
        "• Oila a’zolari bir-biriga yordam beradi, bir-birini hurmat qiladi.\n"
        "• Matnni o‘qib, kim nima qilganini toping: “Buvim non yopdi.” Kim? — buvim. Nima qildi? — non yopdi.", items=items)

D1 = "Lola va Nigora — dugona. Ular birga rasm chizishadi. Lola Nigoraga qizil qalam berdi, Nigora esa Lolaga ko‘k qalam."
D2 = "Olimning to‘pi daraxtga ilinib qoldi. Umid uzun tayoq olib keldi. Ikkovi to‘pni birga tushirishdi."
D3 = "Kamola yiqilib, tizzasini og‘ritdi. Iroda uni o‘rnidan turg‘izdi. Keyin bu haqda ustozga aytdi."
D4 = "Jasurning olmasi bor edi. U olmani ikkiga bo‘lib, yarmini do‘stiga berdi. Ikkalasi ham xursand bo‘ldi."
D5 = "Temur Anvarning qalamini sindirib qo‘ydi. U darhol: “Uzr, bilmay qoldim”, — dedi. Anvar uni kechirdi."
items = [
    Q("Lola va Nigora kim?", "Dugonalar", ["Opa-singil", "Ona va qiz", "Ustoz va o‘quvchi"], text=D1, x="“Lola va Nigora — dugona.”"),
    Q("Qizlar birga nima qilishadi?", "Rasm chizishadi", ["Qo‘shiq aytishadi", "Yugurishadi", "Ovqat pishirishadi"], text=D1,
      x="“Ular birga rasm chizishadi.”"),
    Q("Nigora Lolaga qanday qalam berdi?", "Ko‘k", ["Qizil", "Sariq", "Yashil"], text=D1, d=2, x="Lola qizil, Nigora esa ko‘k qalam berdi."),
    Q("Olimning nimasi daraxtga ilinib qoldi?", "To‘pi", ["Varragi", "Kitobi", "Qalpog‘i"], text=D2, x="“Olimning to‘pi daraxtga ilinib qoldi.”"),
    Q("Umid nima olib keldi?", "Uzun tayoq", ["Narvon", "Arqon", "Stul"], text=D2, x="“Umid uzun tayoq olib keldi.”"),
    Q("To‘pni kim tushirdi?", "Olim va Umid birga", ["Faqat Olim", "Faqat Umid", "Kattalar"], text=D2, d=2,
      x="“Ikkovi to‘pni birga tushirishdi.”"),
    Q("Kim yiqildi?", "Kamola", ["Iroda", "Ustoz", "Lola"], text=D3, x="“Kamola yiqilib, tizzasini og‘ritdi.”"),
    Q("Iroda nima qildi?", "Kamolani turg‘izdi", ["Kulib yubordi", "Uyga ketdi", "Yig‘ladi"], text=D3, x="“Iroda uni o‘rnidan turg‘izdi.”"),
    Q("Keyin Iroda kimga aytdi?", "Ustozga", ["Onasiga", "Shifokorga", "Dugonasiga"], text=D3, x="“Keyin bu haqda ustozga aytdi.”"),
    Q("Jasurda nima bor edi?", "Olma", ["Nok", "Konfet", "Non"], text=D4, x="“Jasurning olmasi bor edi.”"),
    Q("Jasur olmani nima qildi?", "Do‘sti bilan bo‘lishdi", ["O‘zi yedi", "Tashlab yubordi", "Yashirib qo‘ydi"], text=D4,
      x="U olmaning yarmini do‘stiga berdi."),
    Q("Jasur qanday bola?", "Saxiy", ["Xasis", "Dangasa", "Qo‘rqoq"], text=D4, d=2, x="Borini do‘sti bilan bo‘lishgan bola — saxiy."),
    Q("Temur nima qildi?", "Qalamni sindirib qo‘ydi", ["Qalamni yo‘qotdi", "Qalam sotib oldi", "Qalamni yashirdi"], text=D5,
      x="“Temur Anvarning qalamini sindirib qo‘ydi.”"),
    Q("Temur qanday so‘z aytdi?", "Uzr", ["Rahmat", "Xayr", "Salom"], text=D5, x="Xato qilganda “Uzr” deymiz."),
    TF("Anvar Temurni kechirdi.", True, text=D5, x="“Anvar uni kechirdi.”"),
    Q("Yaxshi do‘st nima qiladi?", "Yordam beradi", ["Masxara qiladi", "Urishadi", "Aldaydi"], x="Yaxshi do‘st qiyin paytda yordam beradi."),
    Q("Do‘stingiz xafa bo‘lib o‘tiribdi. Nima qilasiz?", "Yoniga borib, ko‘nglini ko‘taraman", ["E’tibor bermayman", "Ustidan kulaman", "Uzoqlashib ketaman"],
      d=2, x="Do‘st xafa bo‘lsa, uning yonida bo‘lamiz."),
    TF("Yaxshi do‘st o‘yinchog‘ini bo‘lishadi.", True, x="Bo‘lishish do‘stlikni mustahkamlaydi."),
    TF("Do‘st uzr so‘rasa, uni kechirmaslik kerak.", False, x="Do‘st uzr so‘rasa, uni kechiramiz."),
    ORDER("So‘zlardan gap tuzing", "Biz do‘stlar bilan birga o‘ynaymiz", d=2, x="Kim? — biz. Nima qilamiz? — o‘ynaymiz."),
]
T.topic("friends", "🤝", L("Do‘stlik", "Friendship", "Дружба"), C2,
        "Do‘st — birga o‘ynaydigan, qiyin paytda yordam beradigan yaqin odam.\n"
        "• Yaxshi do‘st bo‘lishadi, yordam beradi, xafa qilmaydi.\n"
        "• Xato qilsangiz, “Uzr” deng. Do‘stingiz uzr so‘rasa, uni kechiring.", items=items)

P1 = "Nodira do‘konga kirdi. U sotuvchiga salom berdi. “Iltimos, bitta non bering”, — dedi. Keyin “Rahmat!” deb chiqdi."
items = [
    Q("Ertalab ustozni ko‘rdingiz. Nima deysiz?", "Assalomu alaykum!", ["Xayr!", "Rahmat!", "Kechirasiz!"], x="Uchrashganda salom beramiz."),
    Q("Sizga sovg‘a berishdi. Nima deysiz?", "Rahmat!", ["Salom!", "Xayr!", "Uzr!"], e="🎁", x="Sovg‘a olganda “Rahmat!” deymiz."),
    Q("Bilmasdan birovni turtib yubordingiz. Nima deysiz?", "Kechirasiz!", ["Rahmat!", "Salom!", "Xayrli tun!"], x="Xato qilganda “Kechirasiz!” deymiz."),
    Q("Onangizdan suv so‘ramoqchisiz. Qaysi so‘zni qo‘shasiz?", "Iltimos", ["Tezroq", "Bo‘ldi", "Xayr"], x="Biror narsa so‘raganda “iltimos” deymiz."),
    Q("Uxlashdan oldin oilangizga nima deysiz?", "Xayrli tun!", ["Xayrli tong!", "Salom!", "Rahmat!"], e="🌙", x="Kechasi, uxlashdan oldin “Xayrli tun!” deymiz."),
    Q("Ertalab uyg‘onganda nima deysiz?", "Xayrli tong!", ["Xayrli tun!", "Xayr!", "Uzr!"], e="🌅", x="Ertalab “Xayrli tong!” deymiz."),
    Q("Mehmonlar ketayotganda nima deysiz?", "Xayr, yana keling!", ["Salom!", "Kechirasiz!", "Iltimos"], x="Xayrlashganda “Xayr!” deymiz."),
    Q("Qaysi so‘z — sehrli so‘z?", "Rahmat", ["Ket", "Jim", "Ber"], x="Sehrli so‘zlar: rahmat, iltimos, kechirasiz, salom."),
    Q("Avtobusda buvi tik turibdi. Nima qilasiz?", "Joy beraman", ["O‘tiraveraman", "Uxlayman", "Derazaga qarayman"], d=2,
      x="Kattalarga joy berish — odob."),
    Q("Kattalar gapirayotganda nima qilamiz?", "Gapini bo‘lmaymiz", ["Baqiramiz", "Gapini bo‘lamiz", "Qochib ketamiz"], d=2,
      x="Kattalar gapini oxirigacha tinglaymiz."),
    Q("Ovqat pishirgan onangizga nima deysiz?", "Rahmat, juda mazali!", ["Tezroq bering!", "Yoqmadi!", "Bu nima?"], d=2,
      x="Mehnati uchun minnatdorchilik bildiramiz."),
    Q("Nodira sotuvchiga avval nima qildi?", "Salom berdi", ["Pul berdi", "Kuldi", "Baqirdi"], text=P1, x="“U sotuvchiga salom berdi.”"),
    Q("Nodira nima so‘radi?", "Non", ["Sut", "Olma", "Konfet"], text=P1, x="“Iltimos, bitta non bering.”"),
    Q("Nodira qanday qiz?", "Odobli", ["Qo‘pol", "Dangasa", "Injiq"], text=P1, d=2, x="U salom berdi, “iltimos” va “rahmat” dedi."),
    Q("Nodira do‘konda nechta sehrli so‘z ishlatdi?", "3 ta", ["1 ta", "2 ta", "5 ta"], text=P1, d=3, x="Salom, iltimos, rahmat — 3 ta."),
    TF("Kattalarga salom berish — odob.", True, x="Kichiklar kattalarga birinchi bo‘lib salom beradi."),
    TF("Biror narsa so‘raganda “iltimos” deyish shart emas.", False, x="So‘raganda doim “iltimos” deymiz."),
    TF("Yordam olganda “rahmat” deymiz.", True, x="Yordam uchun minnatdorchilik bildiramiz."),
    MATCH("Vaziyatni so‘z bilan juftlang", [("uchrashganda", "Salom!"), ("xayrlashganda", "Xayr!"), ("sovg‘a olganda", "Rahmat!"),
                                           ("xato qilganda", "Kechirasiz!"), ("so‘raganda", "Iltimos"), ("uxlashdan oldin", "Xayrli tun!")], d=2,
          x="Har bir vaziyatning o‘z odobli so‘zi bor."),
    ORDER("So‘zlardan gap tuzing", "Men ustozga salom berdim", x="Ustozni ko‘rganda salom beramiz."),
]
T.topic("polite", "😊", L("Sehrli so‘zlar", "Polite words", "Вежливые слова"), C2,
        "Sehrli so‘zlar odamlarni xursand qiladi:\n"
        "• Salom! Assalomu alaykum! — uchrashganda. Xayr! — xayrlashganda.\n"
        "• Rahmat! — yordam yoki sovg‘a uchun. Iltimos — biror narsa so‘raganda.\n"
        "• Kechirasiz! Uzr! — xato qilganda.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["family", "friends", "polite"], C2)

# ============================================================ 3-chorak
H1 = "Bizning uyda mushuk bor. Uning nomi Momiq. Momiq sut ichishni yaxshi ko‘radi."
H2 = "Tovuq hovlida don cho‘qiydi. Uning sariq jo‘jalari bor. Jo‘jalar “chiy-chiy” deydi."
H3 = "Bizning sigirimiz bor. U har kuni sut beradi. Buvim sutdan qatiq ivitadi."
H4 = "Olmaxon daraxtda yashaydi. U kuzda yong‘oq yig‘adi. Qishda o‘sha yong‘oqlarni yeydi."
H5 = "Kuchugim Bo‘ribosar hovlini qo‘riqlaydi. Begona odamni ko‘rsa, vovullaydi. Bizni ko‘rsa, dumini likillatadi."
H6 = "Ayiq o‘rmonda yashaydi. U asalni yaxshi ko‘radi. Qishda ayiq uyquga ketadi."
items = [
    Q("Uyda qanday hayvon bor?", "Mushuk", ["Kuchuk", "Quyon", "To‘tiqush"], text=H1, x="“Bizning uyda mushuk bor.”"),
    Q("Mushukning nomi nima?", "Momiq", ["Bo‘ribosar", "Oqtosh", "Paxmoq"], text=H1, x="“Uning nomi Momiq.”"),
    Q("Momiq nimani yaxshi ko‘radi?", "Sut", ["Non", "Olma", "Sabzi"], text=H1, x="Momiq sut ichishni yaxshi ko‘radi."),
    Q("Tovuq hovlida nima qiladi?", "Don cho‘qiydi", ["Suzadi", "Uxlaydi", "Vovullaydi"], text=H2, x="“Tovuq hovlida don cho‘qiydi.”"),
    Q("Jo‘jalar qanday rangda?", "Sariq", ["Qora", "Ko‘k", "Qizil"], text=H2, x="“Uning sariq jo‘jalari bor.”"),
    Q("Sigir nima beradi?", "Sut", ["Tuxum", "Jun", "Asal"], text=H3, x="“U har kuni sut beradi.”"),
    Q("Buvi sutdan nima tayyorlaydi?", "Qatiq", ["Non", "Choy", "Murabbo"], text=H3, x="“Buvim sutdan qatiq ivitadi.”"),
    Q("Olmaxon qayerda yashaydi?", "Daraxtda", ["Suvda", "Qumda", "Uyda"], text=H4, x="“Olmaxon daraxtda yashaydi.”"),
    Q("Olmaxon nima uchun yong‘oq yig‘adi?", "Qishda yeyish uchun", ["O‘ynash uchun", "Sotish uchun", "Uya qurish uchun"], text=H4, d=2,
      x="U kuzda yig‘gan yong‘oqlarni qishda yeydi."),
    Q("Kuchukning nomi nima?", "Bo‘ribosar", ["Momiq", "Olapar", "Oqtosh"], text=H5, x="“Kuchugim Bo‘ribosar…”"),
    Q("Kuchuk begonani ko‘rsa, nima qiladi?", "Vovullaydi", ["Miyovlaydi", "Uxlaydi", "Qochadi"], text=H5, x="Begona odamni ko‘rsa, vovullaydi."),
    Q("Kuchuk egalarini ko‘rsa, nima qiladi?", "Dumini likillatadi", ["Vovullaydi", "Tishlaydi", "Yashirinadi"], text=H5, d=2,
      x="Egalarini ko‘rsa, xursand bo‘lib dumini likillatadi."),
    Q("Ayiq qayerda yashaydi?", "O‘rmonda", ["Dengizda", "Cho‘lda", "Hovlida"], text=H6, x="“Ayiq o‘rmonda yashaydi.”"),
    Q("Ayiq nimani yaxshi ko‘radi?", "Asalni", ["Sabzini", "Qatiqni", "Nonni"], text=H6, x="“U asalni yaxshi ko‘radi.”"),
    TF("Ayiq qishda uyquga ketadi.", True, text=H6, x="Matnda shunday yozilgan."),
    Q("Qaysi hayvon tuxum qo‘yadi?", "Tovuq", ["Sigir", "Mushuk", "It"], e="🥚", x="Tovuq tuxum qo‘yadi, tuxumdan jo‘ja chiqadi."),
    Q("Qaysi hayvon suvda yashaydi?", "Baliq", ["Ot", "Quyon", "Qo‘y"], e="🌊", x="Baliq suvda yashaydi va suzadi."),
    Q("Qo‘y bizga nima beradi?", "Jun", ["Asal", "Tuxum", "Yong‘oq"], d=2, e="🐑", x="Qo‘yning junidan ip yigiriladi, paypoq to‘qiladi."),
    Q("Asalari nima beradi?", "Asal", ["Sut", "Jun", "Tuxum"], e="🐝", x="Asalari gul shirasidan asal tayyorlaydi."),
    Q("Ot qanday ovoz chiqaradi?", "Kishnaydi", ["Miyovlaydi", "Vovullaydi", "Sayraydi"], e="🐎", d=2, x="Ot kishnaydi."),
    TF("Baliq daraxtda yashaydi.", False, x="Baliq suvda yashaydi."),
    MATCH("Hayvonni ovozi bilan juftlang", [("mushuk", "miyovlaydi"), ("it", "vovullaydi"), ("sigir", "mo‘raydi"), ("ot", "kishnaydi"),
                                           ("qo‘y", "ma’raydi"), ("xo‘roz", "qichqiradi")], d=2, x="Har bir hayvonning o‘z ovozi bor."),
    ORDER("So‘zlardan gap tuzing", "Mushuk sut ichdi", x="Kim? — mushuk. Nima qildi? — sut ichdi."),
]
T.topic("animals", "🐾", L("Hayvonlar haqida", "About animals", "О животных"), C3,
        "Hayvonlar haqidagi matnda bilib oling:\n"
        "• Hayvon qayerda yashaydi? (baliq — suvda, olmaxon — daraxtda)\n"
        "• Qanday ovoz chiqaradi? (mushuk miyovlaydi, it vovullaydi)\n"
        "• Odamga qanday foyda beradi? (sigir — sut, tovuq — tuxum)", items=items)

S1 = "Qish keldi. Hamma yoq oppoq qor. Bolalar qordan odam yasashdi."
S2 = "Bahor keldi. Qaldirg‘ochlar uchib keldi. Daraxtlar gulladi."
S3 = "Yozda kunlar issiq. Bolalar hovuzda suzishadi. Bog‘da o‘rik va gilos pishdi."
S4 = "Kuz keldi. Barglar sarg‘aydi. Bog‘da olma va uzum pishdi. Bolalar maktabga borishdi."
S5 = "Yomg‘ir yog‘di. Aziz soyabon oldi. Yomg‘irdan keyin osmonda kamalak chiqdi."
items = [
    Q("Matn qaysi fasl haqida?", "Qish", ["Bahor", "Yoz", "Kuz"], text=S1, x="“Qish keldi.”"),
    Q("Hamma yoq qanday?", "Oppoq", ["Yashil", "Sariq", "Qizil"], text=S1, x="“Hamma yoq oppoq qor.”"),
    Q("Bolalar nima yasashdi?", "Qordan odam", ["Qum qasr", "Varrak", "Qog‘oz qayiq"], text=S1, x="“Bolalar qordan odam yasashdi.”"),
    Q("Matn qaysi fasl haqida?", "Bahor", ["Qish", "Yoz", "Kuz"], text=S2, x="“Bahor keldi.”"),
    Q("Qanday qushlar uchib keldi?", "Qaldirg‘ochlar", ["Qarg‘alar", "Chumchuqlar", "Kaptarlar"], text=S2, x="Bahorda qaldirg‘ochlar qaytib keladi."),
    Q("Bahorda daraxtlar nima qildi?", "Gulladi", ["Qurib qoldi", "Barg to‘kdi", "Qorga burkandi"], text=S2, x="“Daraxtlar gulladi.”"),
    Q("Yozda kunlar qanday?", "Issiq", ["Sovuq", "Qorli", "Salqin"], text=S3, x="“Yozda kunlar issiq.”"),
    Q("Bog‘da nimalar pishdi?", "O‘rik va gilos", ["Olma va behi", "Anor va xurmo", "Limon va apelsin"], text=S3, x="“Bog‘da o‘rik va gilos pishdi.”"),
    Q("Kuzda barglar qanday bo‘ldi?", "Sariq", ["Yashil", "Oq", "Ko‘k"], text=S4, x="“Barglar sarg‘aydi.”"),
    Q("Kuzda bolalar qayerga borishdi?", "Maktabga", ["Dengizga", "Tog‘ga", "Hovuzga"], text=S4, x="“Bolalar maktabga borishdi.”"),
    TF("Kuzda bog‘da olma va uzum pishdi.", True, text=S4, x="Matnda shunday yozilgan."),
    Q("Aziz nima oldi?", "Soyabon", ["To‘p", "Kitob", "Chana"], text=S5, x="Yomg‘ir yog‘gani uchun Aziz soyabon oldi."),
    Q("Yomg‘irdan keyin osmonda nima chiqdi?", "Kamalak", ["Oy", "Qor", "Yulduz"], text=S5, x="“Yomg‘irdan keyin osmonda kamalak chiqdi.”"),
    Q("Qaysi faslda eng ko‘p qor yog‘adi?", "Qishda", ["Yozda", "Kuzda", "Bahorda"], e="❄️", x="Qish — eng sovuq fasl, qor ko‘p yog‘adi."),
    Q("Bir yilda nechta fasl bor?", "4 ta", ["2 ta", "3 ta", "12 ta"], x="Qish, bahor, yoz, kuz — 4 ta fasl."),
    Q("Qishdan keyin qaysi fasl keladi?", "Bahor", ["Yoz", "Kuz"], x="Qish → bahor → yoz → kuz."),
    Q("Yozdan keyin qaysi fasl keladi?", "Kuz", ["Qish", "Bahor"], d=2, x="Yoz → kuz → qish → bahor."),
    Q("Qaysi faslda daraxtlarning barglari to‘kiladi?", "Kuzda", ["Bahorda", "Yozda"], d=2, e="🍂", x="Kuzda barglar sarg‘ayib, to‘kiladi."),
    Q("Qaysi faslda qaldirg‘ochlar issiq o‘lkalarga uchib ketadi?", "Kuzda", ["Bahorda", "Yozning boshida"], d=2,
      x="Kuzda sovuq tushadi, qushlar issiq o‘lkalarga uchib ketadi."),
    TF("Yozda daraxtlar qor bilan qoplanadi.", False, x="Qor qishda yog‘adi, yozda havo issiq."),
    ORDER("Bahordan boshlab fasllarni tartib bilan tering", "bahor → yoz → kuz → qish", sep=" → ", d=2,
          x="Bahordan keyin yoz, keyin kuz, keyin qish keladi."),
]
T.topic("seasons", "🍂", L("Fasllar", "Seasons", "Времена года"), C3,
        "Yilda to‘rt fasl bor: qish, bahor, yoz, kuz.\n"
        "• Qish — sovuq, qor yog‘adi. Bahor — daraxtlar gullaydi, qushlar qaytadi.\n"
        "• Yoz — issiq, mevalar pishadi. Kuz — barglar sarg‘ayadi, maktab boshlanadi.", items=items)

# (topishmoq, javob-rasm, [noto‘g‘ri rasmlar], javob so‘zi) — o‘zimiz tuzgan
RIDDLES1 = [
    ("Dumi kalta, qulog‘i uzun, sakrab-sakrab yuradi.", "🐰", ["🐱", "🐻", "🐭"], "quyon"),
    ("Boshida qizil toji bor, tongda qichqirib, hammani uyg‘otadi.", "🐓", ["🐱", "🐶", "🦆"], "xo‘roz"),
    ("Qip-qizil, dumaloq, daraxtda pishadi, tishlasang, “qirs” etadi.", "🍎", ["🍅", "🍋", "🍇"], "olma"),
    ("Sap-sariq, uzunchoq, po‘stini archib yeysan.", "🍌", ["🍎", "🍇", "🍒"], "banan"),
    ("Kechasi osmonda miltillaydi, shunchalik ko‘pki, sanab bo‘lmaydi.", "⭐", ["☀️", "☁️", "🌈"], "yulduz"),
    ("Qishda yerga oq ko‘rpa yopadi, bahorda erib, ariqqa oqadi.", "❄️", ["🌧️", "☁️", "🌈"], "qor"),
    ("Ko‘lmak bo‘yida “vaq-vaq” qiladi, uzun tili bilan pashsha tutadi.", "🐸", ["🐟", "🦆", "🐢"], "qurbaqa"),
    ("Burni juda uzun — xartum, qulog‘i yelpig‘ichday katta.", "🐘", ["🦒", "🐫", "🐻"], "fil"),
    ("Qanoti bor, lekin qush emas; ichida odamlar o‘tirib, osmonda uchadi.", "✈️", ["🚌", "🚂", "🚲"], "samolyot"),
    ("Ko‘chada yuradi, ko‘p odam tashiydi, har bekatda to‘xtaydi.", "🚌", ["✈️", "🚲", "⛵"], "avtobus"),
    ("Ertalab chiqadi, kechqurun botadi, hammaga nur sochadi.", "☀️", ["🌙", "⭐", "☁️"], "quyosh"),
    ("Mo‘ynasi qizg‘ish, dumi paxmoq, ayyor deb nom olgan.", "🦊", ["🐺", "🐻", "🐿️"], "tulki"),
    ("Ikki oyog‘i — ikki tig‘, ochilib-yopilib qog‘oz kesadi.", "✂️", ["📏", "✏️", "📖"], "qaychi"),
    ("Unga harf va raqam yozamiz, har kuni sumkamizda yuradi.", "📓", ["✏️", "📏", "⏰"], "daftar"),
    ("Oq-qora yo‘l-yo‘l to‘n kiygan, otga o‘xshaydi.", "🦓", ["🐎", "🐄", "🦒"], "zebra"),
    ("O‘tloqda o‘t yeydi, shoxi bor, har kuni sut beradi.", "🐄", ["🐑", "🐎", "🐫"], "sigir"),
    ("Yumshoq juni bor, ma’raydi, junidan paypoq to‘qiladi.", "🐑", ["🐄", "🐶", "🐰"], "qo‘y"),
]
TWISTERS1 = [
    ("Sariq sichqon sakkiz somsa sanadi.", "s", ["q", "b", "t"]),
    ("Bobur bobosiga bodom berdi.", "b", ["d", "s", "q"]),
    ("Qora qo‘y qorda qoldi.", "q", ["k", "s", "b"]),
    ("To‘rtta toychoq toqqa tomon talpindi.", "t", ["d", "ch", "q"]),
    ("Katta kaptar ko‘kka ko‘tarildi.", "k", ["q", "t", "g"]),
    ("Shirin shaftolini shamol shoxdan tushirdi.", "sh", ["s", "ch", "t"]),
    ("Chumoli chuqurchadan chiqdi.", "ch", ["sh", "j", "s"]),
]
items = []
for n, (riddle, em, wrong, word) in enumerate(RIDDLES1):
    items.append(Q(f"Topishmoqni toping: “{riddle}”", em, wrong, d=1 if n < 11 else 2, x=f"Javob: {word} {em}."))
for n, (text, sound, wrong) in enumerate(TWISTERS1):
    items.append(Q("Bu tez aytishda qaysi tovush ko‘p eshitiladi?", sound, wrong, text=text, d=1 if n < 4 else 2,
                   x=f"Bu tez aytishda “{sound}” tovushi qayta-qayta keladi."))
items += [
    Q("Topishmoqda nima aytilmaydi?", "Narsaning nomi", ["Narsaning rangi", "Narsaning ishi"], d=2,
      x="Topishmoqda narsaning nomi yashiriladi, faqat belgilari aytiladi."),
    TF("Tez aytishni avval sekin, keyin tez aytamiz.", True, x="Avval har bir tovushni aniq aytib olamiz."),
    ORDER("So‘zlardan tez aytish tuzing", "Qora qo‘y qorda qoldi", d=2, x="Bu tez aytishda hamma so‘z “q” bilan boshlanadi."),
]
T.topic("riddles", "❓", L("Topishmoq va tez aytish", "Riddles and tongue twisters", "Загадки и скороговорки"), C3,
        "Topishmoqda narsaning nomi aytilmaydi — faqat belgilari aytiladi. Belgilarga qarab javobni topamiz.\n"
        "Misol: “Mo‘ynasi qizg‘ish, dumi paxmoq, ayyor deb nom olgan.” — tulki 🦊.\n"
        "Tez aytish — bir xil tovush ko‘p takrorlanadigan qisqa gap. Avval sekin, keyin tez ayting:\n"
        "“Qora qo‘y qorda qoldi.” (q tovushi)", items=items)

PM1 = "Bahor keldi, gul ochildi,\nBog‘ga iliq nur sochildi."
PM2 = "Bizning uyda bor bir mushuk,\nUning do‘sti — oq kuchuk."
PM3 = "Yoz keldi, havo soz,\nKo‘lda suzar oppoq g‘oz."
PM4 = "Oppoq-oppoq yog‘di qor,\nQuvnoq-quvnoq bolalar bor."
PM5 = "Qushcha qoqar qanotini,\nBola minar oq otini."
RHYMES1 = [
    ("mushuk", "kuchuk", ["sigir", "quyon", "baliq"]),
    ("bola", "lola", ["gul", "qiz", "o‘yin"]),
    ("kuz", "muz", ["barg", "qish", "yomg‘ir"]),
    ("qish", "tish", ["qor", "sovuq", "chana"]),
    ("ot", "qanot", ["eshak", "dala", "yol"]),
    ("non", "jon", ["sut", "choy", "tandir"]),
    ("quyosh", "tosh", ["oy", "nur", "osmon"]),
    ("qush", "kumush", ["uya", "pat", "tuxum"]),
]
items = []
for n, (w, a, wrong) in enumerate(RHYMES1):
    items.append(Q(f"Qaysi so‘z “{w}” so‘ziga qofiyadosh?", a, wrong, d=1 if n < 6 else 2, x=f"{w} — {a}: so‘zlarning oxiri bir xil eshitiladi."))
items += [
    Q("She’r qaysi fasl haqida?", "Bahor", ["Qish", "Yoz", "Kuz"], text=PM1, x="“Bahor keldi, gul ochildi.”"),
    Q("She’rdagi qofiyadosh so‘zlarni toping.", "ochildi — sochildi", ["bahor — gul", "keldi — bog‘ga", "iliq — nur"], text=PM1, d=2,
      x="ochildi — sochildi: oxiri bir xil eshitiladi."),
    Q("Mushukning do‘sti kim?", "Oq kuchuk", ["Sariq jo‘ja", "Kulrang sichqon", "Qora qo‘y"], text=PM2, x="“Uning do‘sti — oq kuchuk.”"),
    Q("She’r nechta misradan iborat?", "2 ta", ["1 ta", "3 ta", "4 ta"], text=PM2, d=2, x="She’rda 2 ta qator — 2 ta misra bor."),
    Q("Ko‘lda kim suzadi?", "Oppoq g‘oz", ["Qora o‘rdak", "Kichik baliq", "Yashil qurbaqa"], text=PM3, x="“Ko‘lda suzar oppoq g‘oz.”"),
    Q("“soz” so‘ziga she’rdagi qaysi so‘z qofiyadosh?", "g‘oz", ["ko‘l", "oppoq", "keldi"], text=PM3, d=2, x="soz — g‘oz: oxiri “-oz”."),
    Q("“qor” so‘ziga she’rdagi qaysi so‘z qofiyadosh?", "bor", ["oppoq", "quvnoq", "bolalar"], text=PM4, d=2, x="qor — bor: oxiri “-or”."),
    Q("She’rda bola nimani minadi?", "Oq otini", ["Velosipedini", "Eshagini", "Chanasini"], text=PM5, x="“Bola minar oq otini.”"),
    Q("She’rni kim yozadi?", "Shoir", ["Sotuvchi", "Shifokor", "Oshpaz"], x="She’r yozadigan ijodkor — shoir."),
    Q("She’rning har bir qatori nima deyiladi?", "Misra", ["Qofiya", "Sarlavha", "Harf"], d=2, x="She’rning bir qatori — misra."),
    TF("Qofiyadosh so‘zlarning oxiri bir xil eshitiladi.", True, x="Masalan: mushuk — kuchuk."),
    TF("“qish” va “yoz” — qofiyadosh so‘zlar.", False, x="qish — yoz: oxiri har xil. “qish” so‘ziga “tish” qofiyadosh."),
    MATCH("Qofiyadosh so‘zlarni juftlang", [("mushuk", "kuchuk"), ("bola", "lola"), ("kuz", "muz"), ("ot", "qanot"), ("non", "jon"),
                                           ("quyosh", "tosh")], d=2, x="Qofiyadosh so‘zlarning oxiri bir xil eshitiladi."),
]
T.topic("rhymes", "🎵", L("She’r va qofiya", "Poems and rhymes", "Стихи и рифмы"), C3,
        "She’r — qatorlarga bo‘lib yozilgan ohangdor matn. She’rning har bir qatori — misra.\n"
        "• Misralar oxirida oxiri bir xil eshitiladigan so‘zlar keladi — ular qofiyadosh so‘zlar.\n"
        "• Misol: mushuk — kuchuk, bola — lola, yoz — g‘oz.\n"
        "She’rni ifodali, shoshmasdan o‘qing.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["animals", "seasons", "riddles", "rhymes"], C3)

# ============================================================ 4-chorak
E1 = "Bor ekan-u, yo‘q ekan, bir quyoncha bor ekan. U sabzisini do‘stlari bilan bo‘lishibdi. Hamma quyonchani yaxshi ko‘rib qolibdi."
E2 = "Bor ekan-u, yo‘q ekan, bir chumoli bor ekan. U yozda tinmay don tashibdi. Qishda uning uyi to‘q va issiq bo‘libdi."
E3 = "Kichkina jo‘ja onasidan adashib qolibdi. U “chiy-chiy” deb yig‘labdi. O‘rdak uni tovuqning oldiga olib boribdi."
E4 = "Olmaxon yerdan bitta yong‘oq topib olibdi. Bu yong‘oq tipratikanniki ekan. Olmaxon uni egasiga qaytarib beribdi."
E5 = ("Bor ekan-u, yo‘q ekan, bir bolaning sehrli qalami bor ekan. U nima chizsa, hammasi haqiqiy bo‘lib qolar ekan. "
      "Bola buvisiga issiq ro‘mol chizib beribdi.")
items = [
    Q("Ertak kim haqida?", "Quyoncha", ["Tulki", "Ayiqcha", "Bo‘ri"], text=E1, x="“Bir quyoncha bor ekan.”"),
    Q("Quyoncha sabzisini nima qildi?", "Do‘stlari bilan bo‘lishdi", ["Yolg‘iz yedi", "Yashirib qo‘ydi", "Tashlab yubordi"], text=E1,
      x="“U sabzisini do‘stlari bilan bo‘lishibdi.”"),
    Q("Ertak qanday so‘zlar bilan boshlandi?", "Bor ekan-u, yo‘q ekan", ["Bir kuni ertalab", "Salom, bolalar", "Qish kelibdi"], text=E1,
      x="Ertaklar ko‘pincha “Bor ekan-u, yo‘q ekan” deb boshlanadi."),
    Q("Chumoli yozda nima qildi?", "Don tashidi", ["Uxladi", "Qo‘shiq aytdi", "O‘ynadi"], text=E2, x="“U yozda tinmay don tashibdi.”"),
    Q("Qishda chumolining uyi qanday bo‘ldi?", "To‘q va issiq", ["Bo‘sh va sovuq", "Qorga ko‘milgan", "Buzilgan"], text=E2,
      x="Yozda mehnat qilgani uchun qishda uyi to‘q bo‘ldi."),
    Q("Ertakdan qanday saboq olamiz?", "Mehnat qilgan to‘q bo‘ladi", ["Yozda uxlash kerak", "Qish yomon fasl", "Don tashish shart emas"], text=E2, d=2,
      x="Chumoli yozda mehnat qilib, qishda to‘q yashadi."),
    Q("Jo‘ja kimdan adashib qoldi?", "Onasidan", ["Do‘stidan", "Akasidan", "O‘rdakdan"], text=E3, x="“Kichkina jo‘ja onasidan adashib qolibdi.”"),
    Q("Jo‘jaga kim yordam berdi?", "O‘rdak", ["Mushuk", "Tulki", "Qarg‘a"], text=E3, x="O‘rdak uni tovuqning oldiga olib boribdi."),
    Q("O‘rdak qanday ekan?", "Mehribon", ["Ayyor", "Dangasa", "Qo‘rqoq"], text=E3, d=2, x="U adashgan jo‘jaga yordam berdi."),
    Q("Olmaxon nima topib oldi?", "Yong‘oq", ["Olma", "Qo‘ziqorin", "Tanga"], text=E4, x="“Olmaxon yerdan bitta yong‘oq topib olibdi.”"),
    Q("Yong‘oq kimniki ekan?", "Tipratikanniki", ["Quyonniki", "Ayiqniki", "Olmaxonniki"], text=E4, x="“Bu yong‘oq tipratikanniki ekan.”"),
    Q("Olmaxonning qaysi fazilati ko‘rindi?", "Halolligi", ["Ochko‘zligi", "Dangasaligi", "Qo‘rqoqligi"], text=E4, d=2,
      x="U topib olgan narsani egasiga qaytardi — bu halollik."),
    Q("Bolaning qanday qalami bor ekan?", "Sehrli", ["Qizil", "Singan", "Uzun"], text=E5, x="“Bir bolaning sehrli qalami bor ekan.”"),
    Q("Bola buvisiga nima chizib berdi?", "Issiq ro‘mol", ["Katta uy", "Qizil olma", "Shirin tort"], text=E5, x="“Bola buvisiga issiq ro‘mol chizib beribdi.”"),
    TF("Bolaning chizganlari haqiqiy bo‘lib qolardi.", True, text=E5, x="Chunki qalam sehrli edi."),
    Q("Bu qanday ertak?", "Sehrli ertak", ["Hayvonlar haqida ertak", "Topishmoq", "She’r"], text=E5, d=3,
      x="Ertakda sehrli qalam bor — bu sehrli ertak."),
    Q("Ertaklarda kim g‘alaba qiladi?", "Yaxshi qahramon", ["Yolg‘onchi", "Ochko‘z", "Dangasa"], x="Ertaklarda yaxshilik doim yutadi."),
    TF("Ertakda tulki ham, quyon ham gapira oladi.", True, x="Ertakda hayvonlar odamlarday gapiradi."),
    Q("Bu nima?", "Ertak", ["She’r", "Topishmoq"], text="Bor ekan-u, yo‘q ekan, bir mitti sichqon bor ekan.",
      x="“Bor ekan-u, yo‘q ekan” — ertak boshlanishi."),
    Q("Bu nima?", "She’r", ["Ertak", "Topishmoq"], text="Quyosh chiqdi charaqlab,\nGullar ochildi yayrab.",
      x="Qatorlarga bo‘lingan, ohangdor — bu she’r."),
    Q("Bu nima?", "Topishmoq", ["Ertak", "She’r"], text="Kechasi osmonda yarqiraydi, kunduzi ko‘rinmaydi. Bu nima?", d=2,
      x="Narsaning nomi aytilmagan, belgisi aytilgan — bu topishmoq."),
    ORDER("So‘zlardan gap tuzing", "Buvim menga ertak aytib berdi", x="Kim? — buvim. Nima qildi? — ertak aytib berdi."),
]
T.topic("tales", "🦊", L("Ertaklar olamida", "The world of tales", "В мире сказок"), C4,
        "Ertak — to‘qib chiqarilgan ajoyib hikoya.\n"
        "• Ertak ko‘pincha “Bor ekan-u, yo‘q ekan…” deb boshlanadi.\n"
        "• Ertakda hayvonlar gapiradi, sehrli narsalar bo‘ladi.\n"
        "• Ertakda yaxshilik doim yutadi.", items=items)

# (bo‘sh joyli maqol, tushib qolgan so‘z, noto‘g‘ri so‘zlar, to‘liq maqol, ma’nosi) — maqollar xalq og‘zaki ijodi
PROV1 = [
    ("Harakatda — …", "barakat", ["uyqu", "o‘yin", "kulgi"], "Harakatda — barakat.", "mehnat qilgan kishi yutadi"),
    ("Oz bo‘lsa ham, … bo‘lsin.", "soz", ["ko‘p", "katta", "tez"], "Oz bo‘lsa ham, soz bo‘lsin.", "narsaning ko‘pi emas, yaxshisi qadrli"),
    ("Hovli olma, … ol.", "qo‘shni", ["mashina", "gilam", "sigir"], "Hovli olma, qo‘shni ol.", "yaxshi qo‘shni juda qadrli"),
    ("Bir qo‘ldan … chiqmas.", "qarsak", ["suv", "qalam", "non"], "Bir qo‘ldan qarsak chiqmas.", "ishni birgalikda qilish kerak"),
    ("Nima eksang, shuni …", "o‘rasan", ["sotasan", "tashlaysan", "unutasan"], "Nima eksang, shuni o‘rasan.",
     "qanday ish qilsang, shunday natija olasan"),
    ("Ilm — aql …", "chirog‘i", ["qulfi", "sumkasi", "uyqusi"], "Ilm — aql chirog‘i.", "bilim odamni dono qiladi"),
    ("Sog‘ tanda — sog‘ …", "aql", ["qo‘l", "ko‘ylak", "uy"], "Sog‘ tanda — sog‘ aql.", "sog‘lom odamning fikri ham tiniq bo‘ladi"),
    ("Qo‘shning tinch — … tinch.", "sen", ["ko‘cha", "shahar", "mushuk"], "Qo‘shning tinch — sen tinch.", "qo‘shnilar bilan ahil yashash kerak"),
    ("Yaxshi niyat — yarim …", "davlat", ["non", "olma", "yo‘l"], "Yaxshi niyat — yarim davlat.", "yaxshi niyat baxt keltiradi"),
    ("Yolg‘onning umri …", "qisqa", ["uzun", "shirin", "katta"], "Yolg‘onning umri qisqa.", "yolg‘on tez ochilib qoladi"),
    ("Yuz so‘ming bo‘lmasin, yuz … bo‘lsin.", "do‘sting", ["mushuging", "qalaming", "kitobing"],
     "Yuz so‘ming bo‘lmasin, yuz do‘sting bo‘lsin.", "do‘st puldan qimmat"),
]
full1 = [p[3] for p in PROV1]
items = []
for n, (blank, ans, wrong, full, meaning) in enumerate(PROV1):
    items.append(Q(f"Maqoldagi tushib qolgan so‘zni toping: “{blank}”", ans, wrong, d=1 if n < 8 else 2,
                   x=f"{full} Ya’ni {meaning}."))
items += [
    Q("“Yolg‘onning umri qisqa” maqoli nimaga o‘rgatadi?", "Rost gapirishga", ["Tez yugurishga", "Ko‘p uxlashga", "Yolg‘on gapirishga"], d=2,
      x="Yolg‘on tez ochilib qoladi, shuning uchun rost gapirish kerak."),
    Q("“Yuz so‘ming bo‘lmasin, yuz do‘sting bo‘lsin” maqoli nima haqida?", "Do‘stlik haqida", ["Pul yig‘ish haqida", "Ovqat haqida", "Ob-havo haqida"],
      d=2, x="Maqol do‘st puldan qimmatroq ekanini aytadi."),
    Q("“Harakatda — barakat” maqoli nima haqida?", "Mehnat haqida", ["Uyqu haqida", "Ob-havo haqida", "Hayvonlar haqida"], d=2,
      x="Harakat qilgan, mehnat qilgan kishi natijaga erishadi."),
    Q("“Hovli olma, qo‘shni ol” maqoli nima haqida?", "Yaxshi qo‘shni haqida", ["Uy sotish haqida", "Bog‘ haqida", "Maktab haqida"], d=2,
      x="Yaxshi qo‘shni uydan ham qadrliroq."),
    Q("“Bir qo‘ldan qarsak chiqmas” maqoli nimaga o‘rgatadi?", "Birga ishlashga", ["Qarsak chalishga", "Yolg‘iz o‘ynashga", "Qo‘l yuvishga"], d=2,
      x="Ko‘p ishni bir kishi emas, hamma birga qiladi."),
    Q("“Sog‘ tanda — sog‘ aql” maqoli nima haqida?", "Sog‘liq haqida", ["Do‘stlik haqida", "Pul haqida", "Fasllar haqida"], d=2,
      x="Tani sog‘ odamning fikri ham tiniq bo‘ladi."),
    Q("Vaziyatga mos maqolni toping.", "Bir qo‘ldan qarsak chiqmas.", rnd.sample([p for p in full1 if p != "Bir qo‘ldan qarsak chiqmas."], 3),
      text="Zarina, Malika va Lola sinfni birga tozalashdi. Ish tez tugadi.", d=3, x="Ish birgalikda qilingani uchun tez bitdi."),
    Q("Vaziyatga mos maqolni toping.", "Yolg‘onning umri qisqa.", rnd.sample([p for p in full1 if p != "Yolg‘onning umri qisqa."], 3),
      text="Ali “uy vazifasini qildim” deb aldadi. Ertasi kuni ustoz hammasini bilib qoldi.", d=3, x="Yolg‘on tez ochilib qoldi."),
    TF("Maqolni xalq yaratgan.", True, x="Maqollar xalqdan-xalqqa, avloddan-avlodga o‘tib kelgan."),
    TF("Maqol — uzun ertak.", False, x="Maqol — qisqa, ibratli gap."),
    MATCH("Maqolning boshini oxiri bilan juftlang", [("Harakatda —", "barakat"), ("Hovli olma,", "qo‘shni ol"), ("Yolg‘onning", "umri qisqa"),
                                                   ("Oz bo‘lsa ham,", "soz bo‘lsin"), ("Ilm —", "aql chirog‘i"), ("Qo‘shning tinch —", "sen tinch")],
          d=2, x="Maqolni to‘liq aytib ko‘ring."),
]
T.topic("proverbs", "💎", L("Maqollar", "Proverbs", "Пословицы"), C4,
        "Maqol — xalq donoligi, qisqa va ibratli gap. Maqolni xalq yaratgan.\n"
        "• “Harakatda — barakat.” — mehnat qilgan kishi yutadi.\n"
        "• “Yolg‘onning umri qisqa.” — yolg‘on tez ochilib qoladi, rost gapirish kerak.\n"
        "Maqolni o‘qib, u nimaga o‘rgatayotganini o‘ylang.", items=items)

B1 = "Bahor keldi. Navro‘z bayrami boshlandi. Buvim sumalak pishirdi. Hamma qo‘shnilar yig‘ildi."
B2 = "1-sentabr — Mustaqillik kuni. Ko‘chalar bayroqlar bilan bezandi. Kechqurun osmonda rang-barang mushaklar otildi."
B3 = "Bizning Vatanimiz — O‘zbekiston. Poytaxtimiz — Toshkent. Men Vatanimni sevaman."
B4 = "Yangi yil kechasi archani bezadik. Archaga rangli o‘yinchoqlar osdik. Hamma bir-biriga yaxshi tilaklar tiladi."
items = [
    Q("Matn qaysi bayram haqida?", "Navro‘z", ["Yangi yil", "Mustaqillik kuni", "Tug‘ilgan kun"], text=B1, x="“Navro‘z bayrami boshlandi.”"),
    Q("Buvi nima pishirdi?", "Sumalak", ["Palov", "Somsa", "Chuchvara"], text=B1, x="“Buvim sumalak pishirdi.”"),
    Q("Navro‘z qaysi faslda keladi?", "Bahorda", ["Qishda", "Yozda", "Kuzda"], text=B1, x="“Bahor keldi. Navro‘z bayrami boshlandi.”"),
    Q("Navro‘zda kimlar yig‘ildi?", "Qo‘shnilar", ["Sinfdoshlar", "Sportchilar", "Sayyohlar"], text=B1, x="“Hamma qo‘shnilar yig‘ildi.”"),
    Q("Mustaqillik kuni qachon nishonlanadi?", "1-sentabrda", ["21-martda", "1-yanvarda", "1-iyunda"], text=B2, x="“1-sentabr — Mustaqillik kuni.”"),
    Q("Ko‘chalar nima bilan bezandi?", "Bayroqlar bilan", ["Qor bilan", "Barglar bilan", "Archalar bilan"], text=B2, x="“Ko‘chalar bayroqlar bilan bezandi.”"),
    Q("Kechqurun osmonda nima bo‘ldi?", "Mushaklar otildi", ["Qor yog‘di", "Kamalak chiqdi", "Yomg‘ir yog‘di"], text=B2,
      x="Bayram kechasi osmonda mushaklar otildi."),
    Q("Poytaxtimiz qaysi shahar?", "Toshkent", ["Samarqand", "Buxoro", "Xiva"], text=B3, x="“Poytaxtimiz — Toshkent.”"),
    TF("Bizning Vatanimiz — O‘zbekiston.", True, text=B3, x="Matnda shunday yozilgan."),
    Q("Matndagi bola nimani sevadi?", "Vatanini", ["Qishni", "Konfetni", "Televizorni"], text=B3, x="“Men Vatanimni sevaman.”"),
    Q("Yangi yil kechasi nima bezatildi?", "Archa", ["Deraza", "Mashina", "Maktab"], text=B4, x="“Yangi yil kechasi archani bezadik.”"),
    Q("Archaga nima osildi?", "Rangli o‘yinchoqlar", ["Olma va nok", "Kitoblar", "Paypoqlar"], text=B4, x="“Archaga rangli o‘yinchoqlar osdik.”"),
    Q("Navro‘zda qaysi taom pishiriladi?", "Sumalak", ["Muzqaymoq", "Tort", "Shokolad"], e="🌷", x="Navro‘zda bug‘doy maysasidan sumalak pishiriladi."),
    Q("Navro‘z qaysi kuni nishonlanadi?", "21-martda", ["1-sentabrda", "1-yanvarda", "1-iyunda"], d=2, x="Navro‘z — 21-mart, bahor bayrami."),
    Q("Yangi yil qaysi kuni boshlanadi?", "1-yanvarda", ["21-martda", "1-sentabrda", "1-iyunda"], d=2, e="🎄", x="Yangi yil 1-yanvarda boshlanadi."),
    Q("O‘zbekiston bayrog‘ida qaysi ranglar bor?", "Ko‘k, oq, yashil va qizil", ["Qora va sariq", "Faqat qizil", "Pushti va jigarrang"], d=2,
      x="Bayrog‘imiz ko‘k, oq, yashil rangli, ular orasida ingichka qizil chiziqlar bor."),
    Q("Bayrog‘imizda nechta yulduz bor?", "12 ta", ["5 ta", "7 ta", "10 ta"], d=3, x="Bayrog‘imizda yangi oy va 12 ta yulduz bor."),
    TF("Navro‘z — bahor bayrami.", True, x="Navro‘z 21-martda, bahorda nishonlanadi."),
    TF("Mustaqillik kuni qishda nishonlanadi.", False, x="Mustaqillik kuni — 1-sentabr, kuzning birinchi kuni."),
    MATCH("Bayramni rasm bilan juftlang", [("Yangi yil", "🎄"), ("Tug‘ilgan kun", "🎂"), ("Navro‘z", "🌷"), ("Mustaqillik kuni", "🇺🇿"),
                                          ("Birinchi qo‘ng‘iroq", "🔔")], d=2, x="Har bir bayramning o‘z belgisi bor."),
    ORDER("So‘zlardan gap tuzing", "Men Vatanimni sevaman", x="Vatan — biz tug‘ilib o‘sgan yurt."),
    ORDER("So‘zlardan gap tuzing", "Navro‘zda buvim sumalak pishirdi", d=2, x="Qachon? — Navro‘zda. Kim? — buvim. Nima qildi? — sumalak pishirdi."),
]
T.topic("holidays", "🎉", L("Vatanim va bayramlar", "Homeland and holidays", "Родина и праздники"), C4,
        "Vatanimiz — O‘zbekiston, poytaxti — Toshkent.\n"
        "• Navro‘z — bahor bayrami, 21-martda nishonlanadi. Navro‘zda sumalak pishiriladi.\n"
        "• Mustaqillik kuni — 1-sentabr. Yangi yil — 1-yanvar.\n"
        "• Bayrog‘imiz ko‘k, oq, yashil rangli, ingichka qizil chiziqlari bor; unda yangi oy va 12 ta yulduz bor.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["tales", "proverbs", "holidays"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["words", "syllables", "school", "family", "friends", "polite", "animals", "seasons", "riddles", "rhymes", "tales", "proverbs",
        "holidays"], C4, level=3)

T.write()
