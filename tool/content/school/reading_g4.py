"""O‘qish, 4-sinf: xalq og‘zaki ijodi, Vatan va tabiat haqidagi matnlar, adiblar va asarlar, janrlar va adabiy tushunchalar.

Hikoyalar, ertaklar, masallar, she’rlar, topishmoqlar va tez aytishlar o‘zimiz yozgan (darsliklardan ko‘chirilmagan);
maqollar — xalq og‘zaki ijodi. Asar–muallif ma’lumotlari faqat umumma’lum faktlardan olingan.
Qayta yaratish: python3 tool/content/school/reading_g4.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403
from readlit import *  # noqa: E402,F401,F403

rnd = random.Random(44)
T = Course("reading", 4, L("O‘qish", "Reading", "Чтение"))

C1 = "1-chorak. Xalq og‘zaki ijodi"
C2 = "2-chorak. Vatan va tabiat"
C3 = "3-chorak. Adiblar va ularning asarlari"
C4 = "4-chorak. Janrlar va adabiy tushunchalar"

# ============================================================ 1-chorak
# (bo‘sh joyli maqol, tushib qolgan so‘z, noto‘g‘ri so‘zlar, to‘liq maqol, mavzu)
P4 = [
    ("Yetti o‘lchab, bir …", "kes", ["tik", "ol", "sot"], "Yetti o‘lchab, bir kes.", "har ishni o‘ylab qilish"),
    ("Bugungi ishni … qo‘yma.", "ertaga", ["kechqurunga", "ta’tilga", "bayramga"], "Bugungi ishni ertaga qo‘yma.", "ishni o‘z vaqtida bajarish"),
    ("Ko‘rpangga qarab … uzat.", "oyoq", ["qo‘l", "bosh", "gap"], "Ko‘rpangga qarab oyoq uzat.", "imkoniyatga qarab ish tutish"),
    ("Sabr qilsang, g‘o‘radan … bitar.", "holva", ["non", "olma", "choy"], "Sabr qilsang, g‘o‘radan holva bitar.", "sabr-toqat"),
    ("Bulbul chamanni sevar, odam — …", "Vatanni", ["bog‘ni", "gulni", "qushni"], "Bulbul chamanni sevar, odam — Vatanni.", "Vatanga muhabbat"),
    ("Ona yurting omon bo‘lsa, rangi ro‘ying … bo‘lmas.", "somon", ["oltin", "qizil", "oppoq"],
     "Ona yurting omon bo‘lsa, rangi ro‘ying somon bo‘lmas.", "Vatan tinchligi"),
    ("Oz-oz o‘rganib dono bo‘lur, qatra-qatra yig‘ilib … bo‘lur.", "daryo", ["bulut", "tosh", "tuproq"],
     "Oz-oz o‘rganib dono bo‘lur, qatra-qatra yig‘ilib daryo bo‘lur.", "ilmni oz-ozdan o‘rganish"),
    ("Ish ishtaha ochar, dangasa … qochar.", "ishdan", ["uydan", "do‘stdan", "oshdan"], "Ish ishtaha ochar, dangasa ishdan qochar.", "mehnatsevarlik"),
    ("Do‘st achitib gapirar, dushman — …", "kuldirib", ["yig‘latib", "qo‘rqitib", "baqirib"], "Do‘st achitib gapirar, dushman — kuldirib.", "chin do‘stlik"),
    ("Yolg‘onchining uyi yonibdi, hech kim …", "ishonmabdi", ["kelmabdi", "ko‘rmabdi", "eshitmabdi"],
     "Yolg‘onchining uyi yonibdi, hech kim ishonmabdi.", "rostgo‘ylik"),
    ("Qo‘rqqanga qo‘sh …", "ko‘rinar", ["yugurar", "uxlar", "kular"], "Qo‘rqqanga qo‘sh ko‘rinar.", "qo‘rquv va jasorat"),
    ("Yigitga yetmish hunar ham …", "oz", ["ko‘p", "og‘ir", "yetarli"], "Yigitga yetmish hunar ham oz.", "hunar o‘rganish"),
    ("Kuch — …", "birlikda", ["pulda", "bo‘yda", "yoshda"], "Kuch — birlikda.", "birlik va hamjihatlik"),
    ("Mehnatning tagi — …", "rohat", ["charchoq", "uyqu", "qayg‘u"], "Mehnatning tagi — rohat.", "mehnat"),
]
full4 = [p[3] for p in P4]
items = []
for n, (blank, ans, wrong, full, theme) in enumerate(P4):
    items.append(Q(f"Maqoldagi tushib qolgan so‘zni toping: “{blank}”", ans, wrong, d=1 if n < 10 else 2,
                   x=f"{full} Mavzusi: {theme}."))
MEANINGS = [
    ("Yetti o‘lchab, bir kes.", "Ishni boshlashdan oldin yaxshilab o‘ylash kerak", ["Ishni tezroq bitirish kerak", "Ko‘p gapirish kerak", "Matoni qisqa kesish kerak"]),
    ("Ko‘rpangga qarab oyoq uzat.", "Imkoniyatingga qarab ish tut", ["Ko‘proq uxla", "Oyog‘ingni issiq tut", "Katta ko‘rpa sotib ol"]),
    ("Bugungi ishni ertaga qo‘yma.", "Ishni o‘z vaqtida bajar", ["Hamma ishni ertaga qil", "Faqat dam ol", "Ishni boshqalarga topshir"]),
    ("Qo‘rqqanga qo‘sh ko‘rinar.", "Qo‘rqoqqa xavf kattaroq ko‘rinadi", ["Ikki kishi bir kishidan kuchli", "Ko‘zi yomon ikkita ko‘radi", "Qo‘rqqan odam ko‘p ishlaydi"]),
    ("Do‘st achitib gapirar, dushman — kuldirib.", "Chin do‘st kamchilikni ochiq aytadi", ["Do‘st doim hazillashadi", "Dushman har doim rost gapiradi", "Do‘st bilan gaplashmaslik kerak"]),
]
for proverb, meaning, wrong in MEANINGS:
    short = proverb[:-1]
    items.append(Q(f"“{short}” maqolining ma’nosi qaysi?", meaning, wrong, d=2, x=f"Maqolning ko‘chma ma’nosi: {meaning.lower()}."))
SITUATIONS4 = [
    ("Aziz uy vazifasini “ertaga qilaman” deb qoldirdi. Ertasi kuni esa vaqti yetmay, darsga tayyorlanmay bordi.", "Bugungi ishni ertaga qo‘yma."),
    ("Nilufar ko‘ylak tikishdan oldin matoni bir necha bor o‘lchab chiqdi va hech xato qilmadi.", "Yetti o‘lchab, bir kes."),
    ("Sinfdoshlar birgalikda ishlab, katta devoriy gazetani bir kunda tayyorlab qo‘yishdi.", "Kuch — birlikda."),
    ("Jamshid qorong‘ida devordagi o‘z soyasini ko‘rib, uni katta ayiq deb o‘yladi va cho‘chib ketdi.", "Qo‘rqqanga qo‘sh ko‘rinar."),
]
for situation, proverb in SITUATIONS4:
    items.append(Q("Vaziyatga mos maqolni toping.", proverb, rnd.sample([p for p in full4 if p != proverb], 3), text=situation, d=2,
                   x=f"Vaziyat mazmuni shu maqolga mos: {proverb}"))
items += [
    Q("Qaysi maqol Vatan haqida?", "Bulbul chamanni sevar, odam — Vatanni.", ["Ko‘rpangga qarab oyoq uzat.", "Qo‘rqqanga qo‘sh ko‘rinar.", "Yetti o‘lchab, bir kes."],
      d=1, x="Bulbul chamanni sevganidek, inson o‘z Vatanini sevadi."),
    Q("Qaysi maqol mehnat haqida?", "Ish ishtaha ochar, dangasa ishdan qochar.", ["Kuch — birlikda.", "Qo‘rqqanga qo‘sh ko‘rinar.", "Bulbul chamanni sevar, odam — Vatanni."],
      d=2, x="Maqol mehnatsevarlikni ulug‘lab, dangasalikni qoralaydi."),
    Q("Qaysi maqol rostgo‘ylik haqida?", "Yolg‘onchining uyi yonibdi, hech kim ishonmabdi.", ["Mehnatning tagi — rohat.", "Yetti o‘lchab, bir kes.", "Kuch — birlikda."],
      d=2, x="Yolg‘onchi rost gapirganda ham unga ishonmay qo‘yishadi."),
    TF("Maqolning muallifi — xalq.", True, x="Maqollarni xalq yaratgan, ular avloddan avlodga o‘tib kelgan."),
    TF("Maqollar uzun hikoyalardan iborat bo‘ladi.", False, x="Maqol — qisqa, lo‘nda hikmatli gap."),
    MATCH("Maqolning boshini oxiri bilan juftlang", [("Yetti o‘lchab,", "bir kes"), ("Ko‘rpangga qarab", "oyoq uzat"), ("Bugungi ishni", "ertaga qo‘yma"),
                                                   ("Qo‘rqqanga", "qo‘sh ko‘rinar"), ("Mehnatning tagi —", "rohat"), ("Kuch —", "birlikda")], d=2),
    ORDER("So‘zlardan gap tuzing", "Maqollar xalq donoligini ifodalaydi", d=1, x="Maqollarda xalqning ko‘p asrlik tajribasi jamlangan."),
]
T.topic("proverbs", "🗝️", L("Maqollarning ma’nosi", "The meaning of proverbs", "Смысл пословиц"), C1,
        "Maqol — xalq donoligi aks etgan qisqa, ibratli gap. Ko‘p maqollarning to‘g‘ri va ko‘chma ma’nosi bor.\n"
        "• “Yetti o‘lchab, bir kes” — faqat mato kesish haqida emas, har ishni o‘ylab qilish haqida.\n"
        "• Maqollar Vatan, mehnat, ilm, do‘stlik, rostgo‘ylik kabi mavzularda bo‘ladi.\n"
        "Maqolni nutqda o‘rinli ishlatsangiz, fikringiz ta’sirli chiqadi.", items=items)

RIDDLES4 = [
    ("Uyini orqasida olib yuradi, shoshmay odimlaydi, xavf sezsa, boshini ichiga tortadi.", "Toshbaqa", ["Tipratikan", "Kaltakesak", "Qurbaqa"]),
    ("Tikanli to‘n kiyib olgan, xavf sezsa, yumaloq bo‘lib oladi.", "Tipratikan", ["Toshbaqa", "Olmaxon", "Sichqon"]),
    ("Qanoti rang-barang, gul ustida raqs tushadi, avval qurtcha bo‘lgan.", "Kapalak", ["Asalari", "Ninachi", "Chumchuq"]),
    ("Kechasi xonani yoritadi, kunduzi dam oladi, tugmani bossang uyg‘onadi.", "Chiroq", ["Deraza", "Oyna", "Soat"]),
    ("Ikki g‘ildiragi bor, pedalini aylantirsang, shamoldek yeladi.", "Velosiped", ["Avtobus", "Poyezd", "Arava"]),
    ("Ichiga xat solinadi, ustiga manzil yoziladi, pochta orqali uzoq yo‘l bosadi.", "Konvert", ["Daftar", "Gazeta", "Kitob"]),
    ("Yozda to‘ni yashil, kuzda sariq, qishda yalang‘och qoladi.", "Bargli daraxt", ["Archa", "Qarag‘ay", "Kaktus"]),
    ("Paxtadek oppoq, osmondan uchib tushadi, kaftingga qo‘nsa, erib ketadi.", "Qor", ["Yomg‘ir", "Tuman", "Shamol"]),
    ("Daraxtni “taq-taq” chertib, po‘stloq ostidan qurt topadi — o‘rmon tabibi.", "Qizilishton", ["Chumchuq", "Musicha", "Kaptar"]),
    ("Bahorda uchib keladi, loydan uya yasab, ayvon shiftiga yopishtiradi.", "Qaldirg‘och", ["Qarg‘a", "Boyqush", "Kaptar"]),
    ("To‘rt oyog‘i bor, lekin yurmaydi; suyanchig‘i bor, ustiga o‘tirasan.", "Stul", ["Stol", "Karavot", "Javon"]),
    ("Suvda suzadi, oyoqlari pardali, tumshug‘i yassi, patlari suv o‘tkazmaydi.", "O‘rdak", ["Tovuq", "Baqa", "Laylak"]),
    ("Po‘sti to‘q sariq, ichi bo‘lak-bo‘lak, qishda dasturxonga chiqadi.", "Mandarin", ["Olma", "Anor", "Uzum"]),
    ("Osmonda suzadi, goh oq, goh qora; qorayib ketsa, yomg‘ir yog‘diradi.", "Bulut", ["Oy", "Kamalak", "Yulduz"]),
    ("Ignasi yo‘q — to‘r to‘qiydi, to‘riga pashsha ilinadi.", "O‘rgimchak", ["Chumoli", "Asalari", "Kapalak"]),
    ("Siyohi bor — dengizi yo‘q, qog‘ozga iz qoldiradi.", "Ruchka", ["O‘chirg‘ich", "Chizg‘ich", "Qaychi"]),
]
TWISTERS = [
    ("Sobir sakkiz savat sariq sabzi sotdi.", "s", ["q", "b", "l"]),
    ("Qizil qopqoqli qozonda qovoq qaynaydi.", "q", ["s", "sh", "r"]),
    ("Bahodir bobo bozordan besh bodring olib keldi.", "b", ["d", "t", "l"]),
    ("Shodmon shoshib shaftoli sharbatini ichdi.", "sh", ["ch", "s", "j"]),
    ("Chaqqon chumchuq chinor ustida chirqilladi.", "ch", ["sh", "j", "k"]),
    ("Lola bilan Laylo lagan to‘la lavlagi oldi.", "l", ["r", "n", "m"]),
    ("Rahim rangli rasmlarni ramkaga joyladi.", "r", ["l", "n", "t"]),
]
items = []
for n, (riddle, answer, wrong) in enumerate(RIDDLES4):
    items.append(Q(f"Topishmoqni toping: “{riddle}”", answer, wrong, d=1 if n < 10 else 2, x=f"Javob: {answer.lower()}."))
for n, (text, sound, wrong) in enumerate(TWISTERS):
    items.append(Q("Tez aytishda qaysi tovush ko‘p takrorlanadi?", sound, wrong, text=text, d=1 if n < 4 else 2,
                   x=f"Bu tez aytishda “{sound}” tovushi qayta-qayta keladi."))
items += [
    Q("Tez aytish nima uchun aytiladi?", "Talaffuzni ravon qilish uchun", ["Uxlab qolish uchun", "Sonlarni hisoblash uchun", "Rasm chizish uchun"],
      x="Tez aytish tilni “charxlaydi”, nutqni ravon va aniq qiladi."),
    Q("Tez aytishni qanday mashq qilgan ma’qul?", "Avval sekin, keyin tezroq", ["Faqat bir marta", "Faqat pichirlab", "Faqat yozib"], d=2,
      x="Avval har bir tovushni aniq aytib, keyin tezlikni oshirish kerak."),
    TF("Topishmoqda narsaning nomi ochiq aytiladi.", False, x="Topishmoqda nom yashiriladi, faqat belgilari ta’riflanadi."),
    TF("Tez aytishlarda bir xil tovushlar ko‘p takrorlanadi.", True, x="Aynan shu takror talaffuzni qiyinlashtirib, mashq beradi."),
    MATCH("Topishmoqni javobi bilan juftlang", [("tikanli to‘n kiygan", "tipratikan"), ("uyini orqasida tashiydi", "toshbaqa"),
                                              ("loydan uya yasaydi", "qaldirg‘och"), ("to‘r to‘qiydi", "o‘rgimchak"),
                                              ("daraxtni chertadi", "qizilishton"), ("kaftda eriydi", "qor")], d=2),
    Q("Qaysi biri xalq og‘zaki ijodining kichik janri emas?", "Roman", ["Maqol", "Topishmoq", "Tez aytish"], d=2,
      x="Roman — yozuvchi yaratgan katta hajmli asar."),
]
T.topic("riddles", "🧩", L("Topishmoq va tez aytishlar", "Riddles and tongue twisters", "Загадки и скороговорки"), C1,
        "Topishmoq — narsaning nomi aytilmay, belgilari yashirin ta’riflanadigan jumboq.\n"
        "• Javobni topish uchun har bir belgini o‘ylang: tashqi ko‘rinishi, nima qiladi, qayerda bo‘ladi.\n"
        "Tez aytish — bir xil tovushlar ko‘p takrorlanadigan qisqa gap. U nutqni ravon qiladi.\n"
        "Misol: “Sobir sakkiz savat sariq sabzi sotdi.” (s tovushi). Avval sekin, keyin tez ayting.", items=items)

E1 = ("Bor ekan-u, yo‘q ekan, bir qishloqda Qobil ismli mehnatkash yigit yashagan ekan. Bir kuni u daryo bo‘yida qanoti "
      "shikastlangan oq laylakni ko‘rib qolibdi. Qobil laylakning qanotini bog‘lab, uni bir hafta parvarish qilibdi. Laylak "
      "sog‘ayib, uchib ketar chog‘ida Qobilga bitta sehrli urug‘ tashlab ketibdi. Qobil urug‘ni ekibdi, undan oltin olma "
      "beradigan daraxt o‘sib chiqibdi. Qobil olmalarni qishloqdagi hamma odamlarga ulashibdi. Shu-shu el-yurt farovon "
      "yashab, murod-maqsadiga yetibdi.")
E2 = ("Bor ekan-u, yo‘q ekan, o‘rmonda maqtanchoq Tulki va kamtar Tipratikan yashar ekan. Bir kuni ular kim birinchi bo‘lib "
      "daryo bo‘yidagi eski tolga yetib borishi haqida bahslashibdi. Tulki: “Men yugurishda tengsizman!” deb maqtanibdi va "
      "yo‘l-yo‘lakay kapalak quvlab ketibdi. Tipratikan esa yo‘lning qisqasini bilar ekan: u so‘qmoqdan borib, tolga birinchi "
      "yetib kelibdi. Tulki uyalib qolibdi va shundan keyin boshqa maqtanmaydigan bo‘libdi.")
items = [
    Q("Qobil kimga yordam berdi?", "Qanoti shikastlangan laylakka", ["Adashgan qo‘zichoqqa", "Qari cho‘ponga", "Kichik baliqqa"], text=E1,
      x="U laylakning qanotini bog‘lab, bir hafta parvarish qildi."),
    Q("Laylak Qobilga nima tashlab ketdi?", "Sehrli urug‘", ["Oltin tanga", "Uchar gilam", "Kumush qalam"], text=E1, x="Laylak unga bitta sehrli urug‘ tashlab ketdi."),
    Q("Urug‘dan qanday daraxt o‘sib chiqdi?", "Oltin olma beradigan daraxt", ["Kumush barg chiqaradigan daraxt", "Oddiy tol", "Qurigan daraxt"], text=E1,
      x="Daraxt oltin olma berar edi."),
    Q("Qobil oltin olmalarni nima qildi?", "Hammaga ulashdi", ["Yashirib qo‘ydi", "Bozorda sotdi", "Podshohga berdi"], text=E1,
      x="U olmalarni qishloqdagi hamma odamlarga ulashdi."),
    Q("Ertakdagi sehrli narsa qaysi?", "Urug‘", ["Daryo", "Qanot", "Qishloq"], text=E1, d=2, x="Oddiy urug‘dan oltin olma beradigan daraxt o‘sgani — sehr."),
    Q("Ertakda Qobilning qaysi fazilatlari ulug‘langan?", "Mehribonlik va saxiylik", ["Dangasalik va xasislik", "Maqtanchoqlik", "Qo‘rqoqlik"], text=E1, d=2,
      x="U laylakka g‘amxo‘rlik qildi va boyligini el bilan baham ko‘rdi."),
    Q("Ertakning ibrati qaysi?", "Yaxshilik qilgan yaxshilik topadi", ["Qushlarga yaqinlashmaslik kerak", "Boylikni yashirish kerak", "Daryo bo‘yiga bormaslik kerak"],
      text=E1, d=2, x="Qobilning yaxshiligi unga va butun qishloqqa baxt keltirdi."),
    Q("Ertakda kimlar bahslashdi?", "Tulki va Tipratikan", ["Bo‘ri va Quyon", "Ayiq va Tulki", "Tipratikan va Kapalak"], text=E2,
      x="Maqtanchoq Tulki va kamtar Tipratikan bahslashdi."),
    Q("Ular qayerga birinchi yetib borish uchun bahslashdi?", "Daryo bo‘yidagi eski tolga", ["Tog‘ cho‘qqisiga", "Qishloq bozoriga", "O‘rmon ichidagi ko‘lga"], text=E2,
      x="Maqsad — daryo bo‘yidagi eski tol."),
    Q("Tulki yo‘lda nima qildi?", "Kapalak quvlab ketdi", ["Uxlab qoldi", "Tipratikanga yordam berdi", "Ovqat izladi"], text=E2,
      x="Tulki maqtanib, yo‘l-yo‘lakay kapalak quvlab ketdi."),
    Q("Tipratikan nima uchun birinchi yetib keldi?", "Qisqa yo‘lni bilgani uchun", ["Tez yugurgani uchun", "Tulki yo‘l bo‘shatgani uchun", "Uni qush olib borgani uchun"],
      text=E2, d=2, x="U so‘qmoqdan — yo‘lning qisqasidan borgan."),
    Q("Bu qanday ertak?", "Hayvonlar haqidagi ertak", ["Sehrli ertak", "Hayotiy ertak", "Doston"], text=E2, d=2,
      x="Ertak qahramonlari — odamlarday gapiradigan hayvonlar."),
    Q("Ertakdan qanday saboq olamiz?", "Maqtanchoqlik yaxshilikka olib bormaydi", ["Doim tez yugurish kerak", "Kapalaklarni quvlash foydali", "Bahslashish shart"],
      text=E2, d=2, x="Maqtangan Tulki uyalib qoldi."),
    TF("Qobil laylakni bir hafta parvarish qildi.", True, text=E1, x="Matnda shunday yozilgan."),
    TF("Tipratikan tolga Tulkidan keyin yetib keldi.", False, text=E2, x="Tipratikan tolga birinchi yetib keldi."),
    Q("Ertaklar ko‘pincha qanday so‘zlar bilan tugaydi?", "Murod-maqsadiga yetibdi", ["Bor ekan-u, yo‘q ekan", "Qadim zamonda", "Tinglang, do‘stlar"],
      x="Ertakning an’anaviy yakuni — qahramonlar murod-maqsadiga yetadi."),
    Q("Ertaklarda qahramon ko‘pincha nechta sinovdan o‘tadi?", "Uchta", ["Bitta", "O‘nta", "Yuzta"], d=2,
      x="Ertaklarda uch aka-uka, uch sinov kabi “uch” soni ko‘p uchraydi."),
    MATCH("Ertak qahramonini xislati bilan juftlang", [("Qobil", "mehribon yigit"), ("Tulki", "maqtanchoq"), ("Tipratikan", "kamtar va zukko"),
                                                      ("Laylak", "minnatdor qush"), ("Zumrad", "mehnatkash va odobli qiz")], d=2),
    ORDER("So‘zlardan gap tuzing", "Ertaklarda yaxshilik yomonlik ustidan g‘alaba qiladi", d=1, x="Bu — xalq ertaklarining asosiy g‘oyasi."),
]
T.topic("tales", "🦊", L("Ertaklar olamida", "The world of folk tales", "В мире сказок"), C1,
        "Ertak — xalq to‘qigan, xayoliy voqealar haqidagi og‘zaki hikoya.\n"
        "• Ertak odatda “Bor ekan-u, yo‘q ekan…” deb boshlanadi va “murod-maqsadiga yetibdi” deb tugaydi.\n"
        "• Qahramonlar ijobiy (mehribon, mard) va salbiy (maqtanchoq, ochko‘z) bo‘ladi; “uch” soni ko‘p takrorlanadi.\n"
        "• Sehrli ertaklarda sehrli buyumlar, hayvonlar haqidagi ertaklarda gapiradigan hayvonlar uchraydi.", items=items)

T.topic("understand", "📚", L("Matnni o‘qib tushunish", "Reading practice", "Понимание текста"), C1,
        "Matnni oxirigacha diqqat bilan o‘qing. Avval kim, nima, qayerda degan savollarga javob toping, "
        "keyin qahramon nima uchun shunday qilganini o‘ylang. Xulosani doim matndagi dalil bilan tekshiring.",
        gen="comprehension", levels=[dict(options=2, infer=False), dict(options=3, infer=True), dict(options=4, infer=True)])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["proverbs", "riddles", "tales"], C1)

# ============================================================ 2-chorak
V1 = ("Bizning Vatanimiz — O‘zbekiston. Uning poytaxti — Toshkent shahri. Yurtimizda baland tog‘lar, keng dalalar, "
      "bepoyon cho‘llar va shiddatli daryolar bor. Amudaryo va Sirdaryo — O‘rta Osiyoning eng katta daryolari. "
      "Samarqand, Buxoro va Xiva kabi qadimiy shaharlarimizga butun dunyodan sayyohlar keladi. "
      "Vatanni sevish uni obod qilishdan, tabiatini asrashdan boshlanadi.")
V2 = ("Madinaning bobosi yoshligida qishloqda maktab qurishga yordam bergan ekan. Har yili bahorda bobosi Madinani o‘sha "
      "maktab hovlisiga olib boradi. Ular birga ko‘chat o‘tqazishadi. “Bu daraxtlar ham, sen ham ulg‘ayasan. Katta "
      "bo‘lganingda, yurtimizni bundan ham go‘zal qilasan”, deydi bobosi. Madina har gal ko‘chatlarga qarab, ular qachon "
      "soya beradigan bo‘lishini sabrsizlik bilan kutadi.")
V3 = ("Mustaqillik kuni arafasida sinfimizda “Mening yurtim” mavzusida suhbat bo‘ldi. Jasur tug‘ilgan shahri Namangandagi "
      "gullar bayrami haqida gapirdi. Nilufar esa Xorazmda pishiriladigan mazali tuxum barak haqida so‘zlab berdi. "
      "Oxirida o‘qituvchimiz: “Har bir viloyatimiz o‘ziga xos, lekin hammamiz bitta katta oilamiz”, dedi.")
items = [
    Q("Vatanimizning poytaxti qaysi shahar?", "Toshkent", ["Samarqand", "Buxoro", "Xiva"], text=V1, x="“Uning poytaxti — Toshkent shahri.”"),
    Q("Matnda qaysi daryolar tilga olingan?", "Amudaryo va Sirdaryo", ["Zarafshon va Chirchiq", "Nil va Frot", "Volga va Dnepr"], text=V1,
      x="Amudaryo va Sirdaryo — O‘rta Osiyoning eng katta daryolari."),
    Q("Matnga ko‘ra, qaysi shaharlarga dunyodan sayyohlar keladi?", "Samarqand, Buxoro va Xiva", ["Nukus, Termiz va Qarshi", "Andijon, Farg‘ona va Qo‘qon",
                                                                                              "Navoiy, Jizzax va Guliston"], text=V1,
      x="Matnda aynan shu qadimiy shaharlar tilga olingan."),
    Q("Matnga ko‘ra, Vatanni sevish nimadan boshlanadi?", "Uni obod qilib, tabiatini asrashdan", ["Ko‘p sayohat qilishdan", "Faqat she’r yodlashdan",
                                                                                                  "Chet elga ketishdan"], text=V1, d=2,
      x="Matnning oxirgi gapi — uning bosh fikri."),
    Q("Matnning mavzusi nima?", "Vatanimiz O‘zbekiston", ["Qishki o‘yinlar", "Dengiz hayvonlari", "Kosmik sayohat"], text=V1,
      x="Matn Vatanimiz tabiati va shaharlari haqida."),
    Q("Madinaning bobosi yoshligida nima qilgan?", "Maktab qurishga yordam bergan", ["Ko‘prik qurgan", "Kitob yozgan", "Uzoq safarga ketgan"], text=V2,
      x="U qishloqda maktab qurishga yordam bergan."),
    Q("Madina bobosi bilan har bahorda nima qiladi?", "Ko‘chat o‘tqazadi", ["Baliq ovlaydi", "Rasm chizadi", "Gul teradi"], text=V2,
      x="Ular maktab hovlisiga borib, ko‘chat o‘tqazishadi."),
    Q("Bobosi Madinadan nimani umid qiladi?", "Yurtini yanada go‘zal qilishini", ["Uzoq shaharga ketishini", "Ko‘p pul topishini", "Faqat o‘ynashini"], text=V2,
      d=2, x="“Katta bo‘lganingda, yurtimizni bundan ham go‘zal qilasan”."),
    Q("Madina nimani sabrsizlik bilan kutadi?", "Ko‘chatlar soya berishini", ["Yozgi ta’tilni", "Tug‘ilgan kunini", "Qor yog‘ishini"], text=V2, d=2,
      x="U ko‘chatlar qachon soya beradigan bo‘lishini kutadi."),
    Q("Hikoyaga eng mos sarlavhani tanlang.", "Bobomning ko‘chatlari", ["Qishki o‘yinlar", "Dengiz sayohati", "Yo‘qolgan mushuk"], text=V2, d=2,
      x="Hikoya bobo va nevaraning ko‘chat o‘tqazishi haqida."),
    Q("Suhbat qanday mavzuda bo‘ldi?", "“Mening yurtim”", ["“Mening oilam”", "“Kuzgi bog‘”", "“Sevimli o‘yinim”"], text=V3,
      x="Sinfda “Mening yurtim” mavzusida suhbat bo‘ldi."),
    Q("Jasur qaysi shaharda tug‘ilgan?", "Namanganda", ["Xivada", "Toshkentda", "Termizda"], text=V3, x="Jasur tug‘ilgan shahri Namangan haqida gapirdi."),
    Q("Nilufar qaysi taom haqida so‘zlab berdi?", "Tuxum barak", ["Palov", "Somsa", "Norin"], text=V3, x="U Xorazmda pishiriladigan tuxum barak haqida gapirdi."),
    Q("Suhbat qaysi bayram arafasida bo‘ldi?", "Mustaqillik kuni", ["Navro‘z", "Yangi yil", "Bilimlar kuni"], text=V3, x="“Mustaqillik kuni arafasida…”"),
    Q("O‘qituvchining so‘zlari qanday fikrni ifodalaydi?", "Barcha viloyatlar ahli — bir oila", ["Viloyatlar bir-biriga o‘xshamaydi", "Faqat poytaxt muhim",
                                                                                               "Har kim o‘z uyida o‘tirishi kerak"], text=V3, d=2,
      x="“Hammamiz bitta katta oilamiz” — Vatan birligi haqidagi fikr."),
    TF("Madina bobosi bilan ko‘chat o‘tqazadi.", True, text=V2, x="Matnda shunday yozilgan."),
    TF("Nilufar Namangandagi gullar bayrami haqida gapirdi.", False, text=V3, x="Bu haqda Jasur gapirdi, Nilufar tuxum barak haqida so‘zladi."),
    TF("Matnda Amudaryo va Sirdaryo tilga olingan.", True, text=V1, x="Ular O‘rta Osiyoning eng katta daryolari deb aytilgan."),
    Q("“Vatan” so‘ziga ma’nodosh so‘zni toping.", "Yurt", ["Uy", "Ko‘cha", "Maktab"], x="Vatan, yurt, diyor, ona yurt — ma’nodosh so‘zlar."),
    ORDER("So‘zlardan gap tuzing", "Vatanimizni obod qilish har birimizning burchimiz", d=2, x="Vatanni sevish — uni obod qilish demakdir."),
]
T.topic("homeland", "🇺🇿", L("Vatanim — O‘zbekiston", "My homeland Uzbekistan", "Моя Родина — Узбекистан"), C2,
        "Vatan haqidagi matnni o‘qiganda:\n"
        "• matnda qaysi joylar, shaharlar va odamlar tilga olinganini aniqlang;\n"
        "• muallif Vatanga qanday munosabat bildirganini toping;\n"
        "• matnning bosh fikrini bir gap bilan ayting.\n"
        "Masalan: “Vatanni sevish uni obod qilishdan boshlanadi” — bosh fikr.", items=items)

N1 = ("Erta bahorda tog‘ yonbag‘irlarida lolaqizg‘aldoqlar ochiladi. Ko‘p o‘tmay qirlar qip-qizil gilamga o‘xshab qoladi. "
      "Asalarilar gul shirasini yig‘ish uchun ertalabdan kechgacha g‘uvillaydi. Qishloq bolalari gullarni uzmasdan, faqat "
      "ularni tomosha qilib, suratga olishadi. Chunki uzilgan gul tezda so‘lib qoladi, qirdagi gul esa hammaga quvonch ulashadi.")
N2 = ("Kuz kelishi bilan qaldirg‘ochlar janubga uchib ketadi. Sovuq tushib, hasharotlar kamayadi, qaldirg‘ochlarga esa ozuqa "
      "topish qiyinlashadi. Ular issiq o‘lkalarda qishlab, bahorda yana o‘z uyalariga qaytib keladi. Bobom: “Qaldirg‘och "
      "qaytdimi — bahor keldi”, deydi.")
N3 = ("Aziz dam olish kuni dadasi bilan daryo bo‘yiga baliq ovlagani bordi. Qirg‘oqda kimdir tashlab ketgan plastik idishlar "
      "va qog‘ozlar sochilib yotardi. Aziz dadasi bilan ularni qopga yig‘ib, axlat qutisiga tashladi. Shu payt qirg‘oqqa bir "
      "oila kelib, joy toza ekanini ko‘rib, xursand bo‘ldi. Dadasi: “Tabiat — umumiy uyimiz, uni asrash hammaning burchi”, dedi.")
items = [
    Q("Matnga ko‘ra, erta bahorda tog‘ yonbag‘rida qanday gullar ochiladi?", "Lolaqizg‘aldoqlar", ["Atirgullar", "Kungaboqarlar", "Lolalar va nargislar"], text=N1,
      x="Matnning birinchi gapida aytilgan."),
    Q("Qirlar nimaga o‘xshab qoladi?", "Qip-qizil gilamga", ["Oppoq dengizga", "Yashil o‘rmonga", "Sariq cho‘lga"], text=N1,
      x="“Qirlar qip-qizil gilamga o‘xshab qoladi.”"),
    Q("Asalarilar nima uchun g‘uvillaydi?", "Gul shirasini yig‘ish uchun", ["Uya qurish uchun", "Qishlash uchun", "Bolalarni qo‘rqitish uchun"], text=N1,
      x="Ular gul shirasini yig‘ishadi."),
    Q("Bolalar gullarni nima uchun uzmaydi?", "Uzilgan gul tez so‘lgani uchun", ["Gullar tikanli bo‘lgani uchun", "Kattalar urishgani uchun",
                                                                               "Gullar baland bo‘lgani uchun"], text=N1, d=2,
      x="Uzilgan gul so‘ladi, qirdagi gul esa hammaga quvonch ulashadi."),
    Q("“Qirlar qip-qizil gilamga o‘xshab qoladi” gapida qanday tasvir bor?", "O‘xshatish", ["Jonlantirish", "Mubolag‘a", "Savol"], text=N1, d=3,
      x="Qirlar gilamga o‘xshatilgan."),
    Q("Matnda qaysi qush haqida so‘z boradi?", "Qaldirg‘och", ["Laylak", "Bulbul", "Chumchuq"], text=N2, x="Matn qaldirg‘ochlar haqida."),
    Q("Qaldirg‘ochlar qaysi faslda janubga uchib ketadi?", "Kuzda", ["Bahorda", "Yozda", "Qishning oxirida"], text=N2, x="“Kuz kelishi bilan…”"),
    Q("Qaldirg‘ochlarga nima uchun ozuqa topish qiyinlashadi?", "Hasharotlar kamaygani uchun", ["Daraxtlar kesilgani uchun", "Daryolar qurigani uchun",
                                                                                                "Uyalari buzilgani uchun"], text=N2,
      x="Sovuq tushib, hasharotlar kamayadi."),
    Q("Qaldirg‘ochlar qachon qaytib keladi?", "Bahorda", ["Kuzda", "Qishda", "Yoz oxirida"], text=N2, x="Ular bahorda o‘z uyalariga qaytadi."),
    Q("Bobosining so‘zlari nimani bildiradi?", "Qaldirg‘och qaytishi — bahor belgisi", ["Qaldirg‘ochlar qishni yaxshi ko‘radi", "Bahorda qushlar uchib ketadi",
                                                                                          "Qaldirg‘ochlar hech qachon qaytmaydi"], text=N2, d=2,
      x="Qaldirg‘ochlar qaytib kelsa, demak bahor kelgan."),
    Q("Aziz dadasi bilan qayerga bordi?", "Daryo bo‘yiga", ["Tog‘ga", "Bozorga", "Hayvonot bog‘iga"], text=N3, x="Ular daryo bo‘yiga baliq ovlagani borishdi."),
    Q("Qirg‘oqda nimalar sochilib yotardi?", "Plastik idishlar va qog‘ozlar", ["Toshlar va chig‘anoqlar", "Barglar va shoxlar", "Baliqlar va qurtlar"], text=N3,
      x="Kimdir tashlab ketgan plastik idishlar va qog‘ozlar."),
    Q("Aziz va dadasi axlatni nima qilishdi?", "Axlat qutisiga tashlashdi", ["Daryoga oqizishdi", "Yoqib yuborishdi", "Qumga ko‘mishdi"], text=N3,
      x="Ular axlatni qopga yig‘ib, axlat qutisiga tashlashdi."),
    Q("Matnning bosh fikri qaysi?", "Tabiatni asrash hammaning burchi", ["Baliq ovlash qiziqarli", "Dam olish kuni uyda o‘tirish kerak", "Daryo suvi sovuq bo‘ladi"],
      text=N3, d=2, x="Dadasining so‘zlari matnning bosh fikrini ifodalaydi."),
    TF("Aziz qirg‘oqdagi axlatni yig‘ib oldi.", True, text=N3, x="U dadasi bilan axlatni qopga yig‘di."),
    TF("Qaldirg‘ochlar qishni o‘z uyalarida o‘tkazadi.", False, text=N2, x="Ular issiq o‘lkalarda qishlaydi."),
    TF("Bolalar lolaqizg‘aldoqlarni uzib, uyga olib ketishdi.", False, text=N1, x="Bolalar gullarni uzmay, faqat tomosha qilishadi."),
    MATCH("Tabiat nomini turi bilan juftlang", [("lolaqizg‘aldoq", "gul"), ("tol", "daraxt"), ("qaldirg‘och", "qush"), ("asalari", "hasharot"),
                                               ("Sirdaryo", "daryo"), ("Chimyon", "tog‘")], d=1),
    ORDER("So‘zlardan gap tuzing", "Tabiatni asrash hammamizning burchimiz", d=1, x="Tabiat — umumiy uyimiz, uni hamma asrashi kerak."),
]
T.topic("nature", "🏞️", L("Tabiat va fasllar", "Nature and seasons", "Природа и времена года"), C2,
        "Tabiat haqidagi matnda muallif manzarani so‘z bilan chizadi.\n"
        "• Qaysi fasl, qaysi joy tasvirlanganini aniqlang.\n"
        "• Tasviriy so‘zlarga e’tibor bering: “qip-qizil gilam”, “g‘uvillaydi”.\n"
        "• Muallif tabiatga qanday munosabatda bo‘lishga chaqirayotganini toping. Masalan: tabiatni asrash — hammaning burchi.", items=items)

PM1 = "Tong otdi-yu, quyosh kuldi,\nDalalarga nurlar to‘ldi.\nQaldirg‘ochlar kelib qo‘ndi,\nBog‘da yashil maysa undi."
PM2 = "Javonimda turar kitob,\nSavolimga berar javob.\nHar sahifa — yangi olam,\nO‘qib, dono bo‘lar odam."
items = [
    Q("She’rda qaysi fasl tasvirlangan?", "Bahor", ["Qish", "Kuz", "Yoz oxiri"], text=PM1, x="Qaldirg‘ochlar qaytishi, maysa unishi — bahor belgilari."),
    Q("She’rning birinchi misrasida kim kuldi?", "Quyosh", ["Qaldirg‘och", "Maysa", "Dala"], text=PM1, x="“Tong otdi-yu, quyosh kuldi”."),
    Q("She’r nechta misradan iborat?", "4 ta", ["2 ta", "3 ta", "6 ta"], text=PM1, x="She’rda to‘rt qator — to‘rt misra bor."),
    Q("“kuldi” so‘zi bilan qaysi so‘z qofiyadosh?", "to‘ldi", ["quyosh", "dala", "maysa"], text=PM1, x="kuldi — to‘ldi: oxiri “-ldi”."),
    Q("“qo‘ndi” so‘zi bilan qaysi so‘z qofiyadosh?", "undi", ["kuldi", "bog‘", "yashil"], text=PM1, d=2, x="qo‘ndi — undi: oxiri “-ndi”."),
    Q("“Quyosh kuldi” — bu qanday tasvir?", "Jonlantirish", ["O‘xshatish", "Mubolag‘a", "Topishmoq"], text=PM1, d=2,
      x="Quyoshga insonga xos harakat — kulish berilgan."),
    Q("She’rning kayfiyati qanday?", "Quvnoq", ["G‘amgin", "Qo‘rqinchli", "Jahldor"], text=PM1, x="Bahor kelgani quvonch bilan tasvirlangan."),
    Q("She’r nima haqida?", "Kitob haqida", ["Maktab bog‘i haqida", "Do‘stlik haqida", "Ona haqida"], text=PM2, x="She’r kitobning foydasi haqida."),
    Q("“kitob” so‘ziga qaysi so‘z qofiyadosh?", "javob", ["javon", "sahifa", "savol"], text=PM2, x="kitob — javob: oxiri “-ob”."),
    Q("“olam” so‘ziga qaysi so‘z qofiyadosh?", "odam", ["dono", "sahifa", "yangi"], text=PM2, x="olam — odam: oxiri “-am”."),
    Q("She’rning bosh fikri qaysi?", "Kitob o‘qigan odam dono bo‘ladi", ["Kitobni javonda saqlash kerak", "Savol berish yomon", "Sahifalar ko‘p bo‘lishi kerak"],
      text=PM2, d=2, x="Oxirgi misra: “O‘qib, dono bo‘lar odam”."),
    Q("“Har sahifa — yangi olam” misrasining ma’nosi qaysi?", "Har sahifada yangi bilim bor", ["Kitobda xarita bor", "Sahifalar katta", "Kitob yangi sotib olingan"],
      text=PM2, d=3, x="Shoir har sahifani yangi dunyoga qiyoslab, bilim ko‘pligini aytmoqda."),
    Q("Bir necha misradan tashkil topgan she’r qismi nima deyiladi?", "Band", ["Misra", "Sarlavha", "Bob"], d=1, x="Misralar birlashib bandni hosil qiladi."),
    Q("She’r yozadigan ijodkor kim deyiladi?", "Shoir", ["Rassom", "Bastakor", "Haykaltarosh"], x="She’rni shoir yozadi."),
    Q("She’rni ifodali o‘qish uchun nimaga e’tibor berish kerak?", "Ohang, to‘xtam va urg‘uga", ["Faqat tezlikka", "Faqat ovoz balandligiga", "Hech narsaga"], d=2,
      x="Ifodali o‘qishda to‘xtam, ohang va urg‘u muhim."),
    TF("She’r oddiy gaplar bilan, misralarsiz yoziladi.", False, d=2, x="She’r — nazm, u misralarga bo‘linib yoziladi."),
    TF("Qofiya she’rga ohang va jarangdorlik beradi.", True, x="Ohangdosh so‘zlar she’rni yodlashni ham osonlashtiradi."),
    MATCH("Atamani ta’rifi bilan juftlang", [("misra", "she’rning bir qatori"), ("band", "misralar guruhi"), ("qofiya", "ohangdosh so‘zlar"),
                                            ("shoir", "she’r yozuvchi ijodkor"), ("sarlavha", "asarning nomi")], d=2),
    ORDER("So‘zlardan gap tuzing", "Shoir bahor haqida she’r yozdi", d=1, x="Gapda ega (shoir) boshida, kesim (yozdi) oxirida keladi."),
]
T.topic("poem", "🎶", L("She’r o‘qiymiz", "Reading poems", "Читаем стихи"), C2,
        "She’r — misralarga bo‘lib yoziladigan ohangdor asar (nazm). She’r yozuvchi ijodkor — shoir.\n"
        "• Misra — she’rning bir qatori; band — bir necha misradan iborat qism.\n"
        "• Qofiya — misralar oxirida keladigan ohangdosh so‘zlar: kitob — javob, olam — odam.\n"
        "• She’rni ifodali o‘qing: to‘xtam va ohangga e’tibor bering, shoirning kayfiyatini his qiling.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["homeland", "nature", "poem"], C2)

# ============================================================ 3-chorak
items = [
    Q("Xudoyberdi To‘xtaboyev qaysi asarni yozgan?", "“Sariq devni minib”", ["“Shum bola”", "“Bolalik”", "“O‘tkan kunlar”"],
      x="“Sariq devni minib” — Xudoyberdi To‘xtaboyevning sarguzasht romani."),
    Q("“Sariq devni minib” romanining bosh qahramoni kim?", "Hoshimjon", ["Otabek", "Alpomish", "Farhod"], d=2,
      x="Asar Hoshimjon ismli bolaning sarguzashtlari haqida."),
    Q("G‘afur G‘ulom qalamiga mansub qissa qaysi?", "“Shum bola”", ["“Sariq devni minib”", "“Kecha va kunduz”", "“Boburnoma”"],
      x="“Shum bola” — G‘afur G‘ulomning kulgili sarguzashtlarga boy qissasi."),
    Q("Oybek o‘z bolaligi xotiralarini qaysi asarida yozgan?", "“Bolalik”", ["“Shum bola”", "“Navoiy”", "“Sariq devni minib”"], d=2,
      x="“Bolalik” — Oybekning xotira qissasi."),
    Q("Zahiriddin Muhammad Bobur o‘z hayoti haqida qaysi asarni yozgan?", "“Boburnoma”", ["“Xamsa”", "“Shum bola”", "“Bolalik”"],
      x="“Boburnoma” — Boburning hayoti va zamonasi haqidagi asar."),
    Q("Alisher Navoiy qanday ijodkor bo‘lgan?", "Buyuk shoir va mutafakkir", ["Rassom", "Sarkarda", "Me’mor"], x="Navoiy — o‘zbek mumtoz adabiyotining buyuk vakili."),
    Q("Abdulla Oripov qaysi mashhur matn muallifi?", "O‘zbekiston Davlat madhiyasi", ["“Alpomish” dostoni", "“Shum bola” qissasi", "“Boburnoma”"], d=2,
      x="Madhiya so‘zlari — Abdulla Oripov, musiqasi — Mutal Burhonov."),
    Q("Anvar Obidjon kim?", "Bolalar shoiri va yozuvchisi", ["Rassom", "Bastakor", "Sportchi"], x="Anvar Obidjon bolalar uchun kulgili she’r va hikoyalar yozgan."),
    Q("Quddus Muhammadiy ko‘proq kimlar uchun she’r yozgan?", "Bolalar uchun", ["Faqat olimlar uchun", "Faqat sportchilar uchun", "Faqat shifokorlar uchun"],
      x="Quddus Muhammadiy — taniqli bolalar shoiri."),
    Q("Qaysi biri bolalar shoiri?", "Po‘lat Mo‘min", ["Amir Temur", "Mirzo Ulug‘bek", "Abu Ali ibn Sino"], x="Po‘lat Mo‘min bolalar uchun ko‘plab she’r va qo‘shiqlar yozgan."),
    Q("Zafar Diyor kim bo‘lgan?", "Bolalar shoiri", ["Sarkarda", "Me’mor", "Tabib"], d=2, x="Zafar Diyor bolalar uchun she’rlar yozgan."),
    Q("Hamza Hakimzoda Niyoziy qaysi sahna asarini yozgan?", "“Boy ila xizmatchi”", ["“Shum bola”", "“Bolalik”", "“Alpomish”"], d=3,
      x="“Boy ila xizmatchi” — Hamzaning mashhur dramasi."),
    Q("Hamza Hakimzoda Niyoziy qaysi shaharda tug‘ilgan?", "Qo‘qonda", ["Xivada", "Termizda", "Nukusda"], d=3, x="Hamza Qo‘qon shahrida tug‘ilgan."),
    Q("Hamid Olimjonning ertak-dostoni qaysi?", "“Oygul bilan Baxtiyor”", ["“Alpomish”", "“Shum bola”", "“Bolalik”"], d=2,
      x="“Oygul bilan Baxtiyor” — Hamid Olimjon yozgan ertak-doston."),
    Q("Qaysi asar kulgili sarguzashtlarga boy qissa?", "“Shum bola”", ["“Xamsa”", "“Boburnoma”", "“Alpomish”"], d=2,
      x="“Shum bola” qahramonining sho‘xliklari kitobxonni kuldiradi."),
    Q("Hikoya, qissa yoki roman yozadigan ijodkor kim deyiladi?", "Yozuvchi", ["Shoir", "Bastakor", "Rassom"], d=2, x="Nasriy asar muallifi — yozuvchi."),
    Q("Kitob muqovasida odatda nima yoziladi?", "Muallif ismi va asar nomi", ["Ob-havo", "Dars jadvali", "Telefon raqami"], x="Muqovada muallif va asar nomi bo‘ladi."),
    TF("“Sariq devni minib” asari Xudoyberdi To‘xtaboyev qalamiga mansub.", True, x="Bu — adibning eng mashhur romani."),
    TF("Anvar Obidjon bolalar uchun kulgili she’r va hikoyalar yozgan.", True, x="Uning asarlari hazil-mutoyibaga boy."),
    TF("“Shum bola” — she’rlar to‘plami.", False, x="“Shum bola” — G‘afur G‘ulomning qissasi."),
    MATCH("Adibni asari bilan juftlang", [("Xudoyberdi To‘xtaboyev", "“Sariq devni minib”"), ("G‘afur G‘ulom", "“Shum bola”"), ("Oybek", "“Bolalik”"),
                                         ("Hamid Olimjon", "“Oygul bilan Baxtiyor”"), ("Zahiriddin Muhammad Bobur", "“Boburnoma”"),
                                         ("Hamza Hakimzoda Niyoziy", "“Boy ila xizmatchi”")], d=2),
]
T.topic("writers", "✒️", L("Adiblar va asarlar", "Writers and their works", "Писатели и их произведения"), C3,
        "Bolalar uchun ko‘plab ajoyib asarlar yozilgan:\n"
        "• Xudoyberdi To‘xtaboyev — “Sariq devni minib” (bosh qahramon — Hoshimjon).\n"
        "• G‘afur G‘ulom — “Shum bola” qissasi; Oybek — “Bolalik” qissasi.\n"
        "• Hamid Olimjon — “Oygul bilan Baxtiyor”; Hamza Hakimzoda Niyoziy (Qo‘qon) — “Boy ila xizmatchi”.\n"
        "• Quddus Muhammadiy, Po‘lat Mo‘min, Zafar Diyor, Anvar Obidjon — bolalar shoirlari.", items=items)

F1 = ("Sherzod bilan Rustam qo‘shni edi. Bir kuni Rustam oyog‘ini lat yeydirib, bir hafta maktabga bora olmadi. Sherzod har "
      "kuni darsdan keyin uning uyiga kelib, o‘tilgan mavzularni tushuntirib berdi. Rustam maktabga qaytganida, hech narsadan "
      "orqada qolmagan edi. U do‘stiga: “Sen haqiqiy do‘st ekansan”, dedi.")
F2 = ("Gulnora sinfga yangi kelgan Dilbarga qalam va o‘chirg‘ichini berib turdi. Tanaffusda ular birga rasm chizishdi. "
      "Ma’lum bo‘lishicha, ikkalasi ham rasm chizishni yaxshi ko‘rar ekan. Endi ular har shanba kuni maktabdagi tasviriy "
      "san’at to‘garagiga birga qatnashadi.")
F3 = ("Kamol bilan Anvar futbol o‘ynayotganda to‘p qo‘shnining derazasiga tegib, oynani sindirdi. Anvar qo‘rqib, qochib "
      "ketmoqchi bo‘ldi. Kamol esa: “Xato qildik, kechirim so‘rashimiz kerak”, dedi. Ular qo‘shni amakining oldiga borib, "
      "uzr so‘rashdi. Amaki bolalarning rostgo‘yligidan ta’sirlanib, ularni kechirdi va yangi oynani birga o‘rnatishga chaqirdi.")
items = [
    Q("Rustam nima uchun maktabga bora olmadi?", "Oyog‘i lat yegani uchun", ["Shamollagani uchun", "Safarga ketgani uchun", "Dars qilmagani uchun"], text=F1,
      x="U oyog‘ini lat yeydirgan edi."),
    Q("Sherzod har kuni nima qildi?", "Rustamga darslarni tushuntirdi", ["Rustam bilan futbol o‘ynadi", "Rustamga sovg‘a olib keldi", "Rustamni shifokorga olib bordi"],
      text=F1, x="U darsdan keyin kelib, o‘tilgan mavzularni tushuntirdi."),
    Q("Rustam maktabga qaytganida qanday ahvolda edi?", "Hech narsadan orqada qolmagan edi", ["Hamma narsani unutgan edi", "Juda charchagan edi",
                                                                                                "Sinfdan ko‘chib ketgan edi"], text=F1, d=2,
      x="Sherzodning yordami tufayli u darslardan orqada qolmadi."),
    Q("Sherzodning qaysi fazilati ko‘rindi?", "Sadoqatli do‘stligi", ["Maqtanchoqligi", "Dangasaligi", "Hasadgo‘yligi"], text=F1, d=2,
      x="U do‘stini qiyin paytda yolg‘iz qoldirmadi."),
    Q("Hikoyaga mos maqolni tanlang.", "Do‘stsiz boshim — tuzsiz oshim.", ["Ko‘rpangga qarab oyoq uzat.", "Qo‘rqqanga qo‘sh ko‘rinar.", "Yetti o‘lchab, bir kes."],
      text=F1, d=3, x="Hikoya do‘stlikning qadri haqida."),
    Q("Gulnora Dilbarga nima berib turdi?", "Qalam va o‘chirg‘ich", ["Kitob va daftar", "Ruchka va chizg‘ich", "Bo‘yoq va mo‘yqalam"], text=F2,
      x="U qalam va o‘chirg‘ichini berib turdi."),
    Q("Qizlar tanaffusda nima qilishdi?", "Rasm chizishdi", ["Kitob o‘qishdi", "Arqon sakrashdi", "Qo‘shiq aytishdi"], text=F2, x="Ular birga rasm chizishdi."),
    Q("Qizlar qaysi to‘garakka qatnashadi?", "Tasviriy san’at to‘garagiga", ["Raqs to‘garagiga", "Shaxmat to‘garagiga", "Suzish to‘garagiga"], text=F2,
      x="Ikkalasi ham rasm chizishni yaxshi ko‘radi."),
    Q("Qizlar to‘garakka qachon qatnashadi?", "Har shanba kuni", ["Har dushanba kuni", "Har kuni ertalab", "Faqat ta’tilda"], text=F2, x="“Har shanba kuni…”"),
    Q("Qizlarning do‘stligi nimadan boshlandi?", "Kichik yordamdan", ["Janjaldan", "Musobaqadan", "Tasodifiy xatodan"], text=F2, d=2,
      x="Gulnora yangi kelgan qizga qalam va o‘chirg‘ich berib turdi."),
    Q("To‘p nimaga tegdi?", "Qo‘shnining derazasiga", ["Daraxt shoxiga", "Mashina oynasiga", "Maktab eshigiga"], text=F3, x="To‘p qo‘shnining derazasiga tegdi."),
    Q("Anvar avval nima qilmoqchi bo‘ldi?", "Qochib ketmoqchi bo‘ldi", ["Uzr so‘ramoqchi bo‘ldi", "Oynani o‘zi tuzatmoqchi bo‘ldi", "Kattalarni chaqirmoqchi bo‘ldi"],
      text=F3, x="Anvar qo‘rqib, qochib ketmoqchi bo‘ldi."),
    Q("Kamol nima taklif qildi?", "Kechirim so‘rashni", ["Qochib ketishni", "Hech kimga aytmaslikni", "Boshqa joyda o‘ynashni"], text=F3,
      x="“Xato qildik, kechirim so‘rashimiz kerak”."),
    Q("Amaki bolalarni nima uchun kechirdi?", "Rostgo‘ylik qilganlari uchun", ["Pul berganlari uchun", "Qochib ketganlari uchun", "Futbolni yaxshi o‘ynaganlari uchun"],
      text=F3, d=2, x="Amaki ularning rostgo‘yligidan ta’sirlandi."),
    Q("Hikoyaning bosh fikri qaysi?", "Xatoni tan olish — mardlik", ["Futbol o‘ynash yomon", "Qo‘shnilar jahldor bo‘ladi", "Oyna tez sinadi"], text=F3, d=2,
      x="Bolalar xatosini tan olib, kechirim so‘rashdi."),
    TF("Sherzod Rustamni kasalligida yolg‘iz qoldirdi.", False, text=F1, x="U har kuni kelib, darslarni tushuntirdi."),
    TF("Gulnora va Dilbar rasm chizishni yaxshi ko‘rar ekan.", True, text=F2, x="Matnda shunday yozilgan."),
    TF("Kamol va Anvar qo‘shni amakidan uzr so‘rashdi.", True, text=F3, x="Ular amakining oldiga borib, uzr so‘rashdi."),
    ORDER("So‘zlardan gap tuzing", "Haqiqiy do‘st qiyin paytda yordam beradi", d=1, x="Do‘st qiyin kunda sinaladi."),
]
T.topic("friendship", "🤝", L("Do‘stlik va mehr", "Friendship and kindness", "Дружба и доброта"), C3,
        "Do‘stlik haqidagi hikoyalarda qahramonlarning xatti-harakatiga e’tibor bering:\n"
        "• Kim kimga yordam berdi? Nima uchun?\n"
        "• Qahramonning ishidan uning fazilatini aniqlang: yordam berdi → mehribon, xatoni tan oldi → rostgo‘y.\n"
        "• Hikoyadan olingan saboqni o‘z hayotingiz bilan solishtiring.", items=items)

M1 = ("Bir kuni Qarg‘a daraxt shoxida o‘tirib, o‘z ovozini maqtadi: “Mening ovozim bulbulnikidan ham yoqimli!” Bulbul hech "
      "narsa demay, sayrashda davom etdi. O‘rmondagi jonivorlar Bulbulning qo‘shig‘ini tinglash uchun yig‘ilishdi, "
      "Qarg‘aning qag‘illashiga esa hech kim quloq solmadi. Qissadan hissa: o‘zini maqtagan emas, ishi bilan ko‘ringan qadrlanadi.")
M2 = ("Tovuq ertalabdan kechgacha don izlab, jo‘jalarini boqardi. Tovus esa patlarini yoyib, hovlida kerilib yurar, har kimga: "
      "“Mendan chiroyli qush yo‘q!” derdi. Bir kuni hovliga mehmonlar kelishdi. Ular Tovusga bir qarab qo‘yishdi-yu, "
      "jo‘jalarini parvarish qilayotgan g‘amxo‘r Tovuqni uzoq maqtashdi. Qissadan hissa: kishini chiroyi emas, mehnati va mehri bezaydi.")
M3 = ("Soat Qalamga maqtandi: “Men bir daqiqa ham to‘xtamay ishlayman, sen esa ko‘pincha qutida yotasan”. Qalam javob berdi: "
      "“Men kam ishlayman, ammo har safar izim qoladi: bola men bilan xat yozadi, rasm chizadi”. Shunda Daftar: “Ikkalangiz "
      "ham keraklisiz: biringiz vaqtni o‘lchaysiz, biringiz bilim yozasiz. Har kim o‘z ishi bilan qadrli”, dedi.")
items = [
    Q("Masalda kim o‘zini maqtadi?", "Qarg‘a", ["Bulbul", "Tulki", "Kaptar"], text=M1, x="Qarg‘a ovozim bulbulnikidan yoqimli deb maqtandi."),
    Q("Jonivorlar kimning qo‘shig‘ini tinglash uchun yig‘ilishdi?", "Bulbulning", ["Qarg‘aning", "Kaptarning", "Laylakning"], text=M1,
      x="Ular Bulbulning qo‘shig‘ini tinglashdi."),
    Q("Bulbul Qarg‘aning maqtanishiga qanday javob qaytardi?", "Hech narsa demay, sayrashda davom etdi", ["U bilan urishdi", "Uchib ketdi", "U ham maqtandi"],
      text=M1, d=2, x="Bulbul so‘z bilan emas, ishi bilan javob berdi."),
    Q("Masalning ibrati qaysi?", "Kishini maqtovi emas, ishi ko‘rsatadi", ["Qarg‘alar yaxshi kuylaydi", "Daraxtga chiqish xavfli", "Ko‘p gapirish kerak"],
      text=M1, d=2, x="Qissadan hissada shunday deyilgan."),
    Q("Tovus nima deb maqtanardi?", "“Mendan chiroyli qush yo‘q!”", ["“Men eng tez yuguraman!”", "“Men eng ko‘p don topaman!”", "“Men eng baland uchaman!”"],
      text=M2, x="Tovus chiroyi bilan kerilib yurardi."),
    Q("Mehmonlar kimni uzoq maqtashdi?", "Tovuqni", ["Tovusni", "Jo‘jalarni", "Xo‘rozni"], text=M2, x="Ular g‘amxo‘r Tovuqni maqtashdi."),
    Q("Masalda qanday xislatlar ulug‘langan?", "Mehnat va mehr", ["Chiroy va kerilish", "Dangasalik", "Maqtanchoqlik"], text=M2, d=2,
      x="“Kishini chiroyi emas, mehnati va mehri bezaydi.”"),
    Q("Masaldagi Tovus qanday odamlarni eslatadi?", "Maqtanchoq odamlarni", ["Mehnatkash odamlarni", "Kamtar odamlarni", "G‘amxo‘r odamlarni"], text=M2, d=2,
      x="Masal qahramonlari odamlarning fe’l-atvorini eslatadi."),
    Q("Soat nima deb maqtandi?", "To‘xtamay ishlashini", ["Chiroyli ekanini", "Qimmat ekanini", "Qutida yotishini"], text=M3,
      x="Soat bir daqiqa ham to‘xtamay ishlashini aytdi."),
    Q("Qalamning izi nimada qoladi?", "Bola yozgan xat va chizgan rasmda", ["Soat millarida", "Daftar muqovasida", "Stol ustida"], text=M3,
      x="“Bola men bilan xat yozadi, rasm chizadi”."),
    Q("Bahsni kim hal qildi?", "Daftar", ["Soat", "Qalam", "O‘chirg‘ich"], text=M3, x="Daftar ikkalasini ham kerakli dedi."),
    Q("Masalning xulosasi qaysi?", "Har kim o‘z ishi bilan qadrli", ["Faqat soat kerak", "Qalam keraksiz", "Daftar hammadan muhim"], text=M3, d=2,
      x="Daftar: “Har kim o‘z ishi bilan qadrli”, dedi."),
    Q("Masal qanday asar?", "Ibratli qisqa asar", ["Uzun tarixiy roman", "Qofiyali topishmoq", "Ilmiy maqola"],
      x="Masalda hayvonlar yoki narsalar odamlarday gapirib, ibrat beradi."),
    Q("Masal oxiridagi ibratli xulosa nima deyiladi?", "Qissadan hissa", ["Boshlanma", "Sarlavha", "Qofiya"], d=3, x="Masal “qissadan hissa” bilan tugaydi."),
    Q("Mashhur qadimgi yunon masalchisi kim?", "Ezop", ["Gomer", "Alisher Navoiy", "Bobur"], d=3, x="Ezop — qadimgi Yunonistonda yashagan masalchi."),
    TF("Masallarda hayvonlar va narsalar odamlarday gapirishi mumkin.", True, x="Ular orqali odamlarning xislatlari ko‘rsatiladi."),
    TF("Masaldan hech qanday ibrat chiqmaydi.", False, x="Masalning asosiy maqsadi — ibrat berish."),
    MATCH("Masal qahramonini xislati bilan juftlang", [("Qarg‘a", "o‘zini maqtaydi"), ("Bulbul", "ishi bilan ko‘rinadi"), ("Tovus", "chiroyi bilan kerilib yuradi"),
                                                      ("Tovuq", "jo‘jalarini boqadi"), ("Daftar", "bahsni hal qiladi")], d=2),
    ORDER("So‘zlardan gap tuzing", "Masal qisqa va ibratli asar", d=1, x="Masal oxirida “qissadan hissa” — ibratli xulosa bo‘ladi."),
]
T.topic("fables", "🐓", L("Masallar", "Fables", "Басни"), C3,
        "Masal — hayvonlar, qushlar yoki narsalar ishtirokida yozilgan qisqa ibratli asar.\n"
        "• Masal qahramonlari odamlarday gapiradi va odamlarning fe’l-atvorini eslatadi.\n"
        "• Masal oxirida ibratli xulosa bo‘ladi, u “qissadan hissa” deb ataladi.\n"
        "• Qadimgi yunon masalchisi Ezop, o‘zbek adabiyotida Gulxaniy masallari mashhur.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["writers", "friendship", "fables"], C3)

# ============================================================ 4-chorak
GENRE_SAMPLES = [
    ("Bor ekan-u, yo‘q ekan, bir podshohning uchta o‘g‘li bor ekan. Kenja o‘g‘il sehrli qushni izlab yo‘lga chiqibdi.", "Ertak"),
    ("Oppoq qorlar uchadi,\nYerni mayin quchadi.", "She’r"),
    ("Maqtanchoq Xo‘roz: “Quyoshni men uyg‘otaman!” der ekan. Bir kuni u uxlab qolibdi, quyosh esa baribir chiqibdi. "
     "Qissadan hissa: maqtanchoqlik kulgiga qoldiradi.", "Masal"),
    ("Kecha dadam bilan shahardagi yangi kutubxonaga bordim. U yerda kitoblar juda ko‘p ekan. Men sarguzasht kitobini tanladim.", "Hikoya"),
    ("Aytishlaricha, qadim zamonlarda bu tepalik yonida mard bir cho‘pon yashagan ekan. Qishloq nomi o‘sha cho‘pon sharafiga qo‘yilgan emish.", "Rivoyat"),
    ("Mehnatning tagi — rohat.", "Maqol"),
    ("Tikanli to‘n kiygan, xavf sezsa, yumaloq bo‘lib oladi.", "Topishmoq"),
]
GENRE_NAMES = [g for _, g in GENRE_SAMPLES]
items = []
for n, (sample, genre) in enumerate(GENRE_SAMPLES):
    items.append(Q("Bu parcha qaysi janrga mansub?", genre, rnd.sample([g for g in GENRE_NAMES if g != genre], 3), text=sample, d=1 if n < 6 else 2,
                   x=f"Parcha — {genre.lower()} namunasi."))
items += [
    Q("Qaysi janrda voqea to‘qima bo‘lib, sehrli narsalar uchraydi?", "Ertak", ["Hikoya", "Maqol", "Rivoyat"], x="Ertakda xayoliy, sehrli voqealar bo‘ladi."),
    Q("Hayotda bo‘lishi mumkin bo‘lgan voqea haqidagi kichik nasriy asar qaysi?", "Hikoya", ["Ertak", "She’r", "Topishmoq"], x="Hikoya hayotiy voqeani tasvirlaydi."),
    Q("Joy nomlari yoki mashhur kishilar haqidagi, haqiqatga yaqin og‘zaki hikoya qaysi?", "Rivoyat", ["Masal", "Ertak", "She’r"], d=2,
      x="Rivoyatda voqea haqiqatga yaqin bo‘ladi."),
    Q("Qaysi asar oxirida “qissadan hissa” bo‘ladi?", "Masal", ["Hikoya", "Topishmoq", "Rivoyat"], x="Masal ibratli xulosa bilan tugaydi."),
    Q("Nasr nima?", "Oddiy gaplar bilan yozilgan matn", ["Misrali matn", "Qo‘shiq ohangi", "Rasmli kitob"], d=2, x="Hikoya, ertak, masal ko‘pincha nasrda yoziladi."),
    Q("Nazm nima?", "She’riy (misrali) matn", ["Oddiy gaplardan iborat matn", "Rasmlar to‘plami", "Lug‘at"], d=2, x="Nazm — she’r bilan yozilgan matn."),
    Q("Qaysi biri yozuvchi yaratgan asar?", "“Sariq devni minib”", ["“Zumrad va Qimmat”", "“Alpomish”", "“Ur to‘qmoq”"], d=2,
      x="Uni Xudoyberdi To‘xtaboyev yozgan, qolganlari xalq og‘zaki ijodi."),
    TF("Hikoya nasrda yoziladi.", True, x="Hikoya oddiy gaplar bilan, misralarsiz yoziladi."),
    TF("Rivoyat — misralarga bo‘lingan she’r.", False, x="Rivoyat — haqiqatga yaqin og‘zaki hikoya."),
    MATCH("Janr va uning belgisini juftlang", [("ertak", "“Bor ekan-u, yo‘q ekan…”"), ("she’r", "misra va qofiya"), ("masal", "qissadan hissa"),
                                              ("rivoyat", "joy nomi tarixi"), ("hikoya", "hayotiy voqea"), ("topishmoq", "yashirin ta’rif")], d=2),
    ORDER("So‘zlardan gap tuzing", "Rivoyat joy nomlari haqida hikoya qiladi", d=2, x="Ko‘p rivoyatlar qishloq, tepalik, buloq nomlarining kelib chiqishini tushuntiradi."),
]
T.topic("genres", "🎭", L("Adabiy janrlar", "Literary genres", "Литературные жанры"), C4,
        "Adabiy asarlar janrlarga bo‘linadi:\n"
        "• She’r — misra va qofiyali ohangdor asar (nazm). Hikoya — hayotiy voqea haqidagi kichik nasriy asar.\n"
        "• Ertak — xayoliy, sehrli voqealar haqidagi xalq asari.\n"
        "• Masal — hayvon yoki narsalar orqali ibrat beruvchi asar; oxirida “qissadan hissa” bo‘ladi.\n"
        "• Rivoyat — joy nomlari yoki mashhur kishilar haqidagi, haqiqatga yaqin og‘zaki hikoya.", items=items)

A1 = ("Shanba kuni ertalab Laylo buvisinikiga ketayotgan edi. Bekatda u bir keksa kishining sumkasi og‘irligini ko‘rdi. "
      "Laylo sumkani avtobusga olib chiqishga yordam berdi. Keksa kishi unga chin dildan rahmat aytdi. Buvisinikiga yetib "
      "kelgach, Laylo bu voqeani so‘zlab berdi. Buvisi: “Yaxshilik hech qachon izsiz ketmaydi”, dedi.")
A2 = ("Kuz. Daraxtlardan sariq barglar to‘kilmoqda. Maktab hovlisida bolalar barg yig‘ish hasharini boshlashdi. Eng ko‘p "
      "gapirgan Farrux edi, lekin eng ko‘p barg yig‘gan — jimgina ishlagan Sanjar bo‘ldi. O‘qituvchi: “Kam gapirib, ko‘p "
      "ishlagan yutadi”, dedi.")
items = [
    Q("Hikoyaning bosh qahramoni kim?", "Laylo", ["Buvisi", "Keksa kishi", "Haydovchi"], text=A1, x="Voqealar Laylo atrofida kechadi."),
    Q("Voqea qachon bo‘lgan?", "Shanba kuni ertalab", ["Dushanba kuni kechqurun", "Yakshanba kuni tushda", "Juma kuni tunda"], text=A1, x="“Shanba kuni ertalab…”"),
    Q("Asosiy voqea qayerda bo‘lgan?", "Bekatda", ["Maktabda", "Bozorda", "Kutubxonada"], text=A1, x="Laylo bekatda keksa kishiga yordam berdi."),
    Q("Hikoyaning bosh fikri qaysi?", "Yaxshilik hech qachon izsiz ketmaydi", ["Avtobusda yurish qiyin", "Sumkalar og‘ir bo‘ladi", "Buvilar ko‘p gapiradi"], text=A1,
      d=2, x="Buvisining so‘zlari — hikoyaning bosh fikri."),
    Q("Hikoyaga eng mos sarlavhani tanlang.", "Bekatdagi yaxshilik", ["Buvimning bog‘i", "Qishki ta’til", "Futbol musobaqasi"], text=A1, d=2,
      x="Sarlavha asosiy voqeani ifodalaydi."),
    ORDER("Hikoya rejasini tartib bilan tuzing", "Buvisinikiga yo‘l → Og‘ir sumka → Laylo yordam berdi → Buvining so‘zlari", sep=" → ", d=2,
          x="Reja voqealar ketma-ketligini aks ettiradi."),
    Q("Voqea qaysi faslda bo‘lgan?", "Kuzda", ["Bahorda", "Yozda", "Qishda"], text=A2, x="“Kuz. Daraxtlardan sariq barglar to‘kilmoqda.”"),
    Q("Eng ko‘p barg yig‘gan kim?", "Sanjar", ["Farrux", "O‘qituvchi", "Hamma teng"], text=A2, x="Jimgina ishlagan Sanjar eng ko‘p barg yig‘di."),
    Q("Matnning bosh fikri qaysi?", "Kam gapirib, ko‘p ishlagan yutadi", ["Kuzda barglar to‘kiladi", "Hashar qiyin ish", "Ko‘p gapirish foydali"], text=A2, d=2,
      x="O‘qituvchining xulosasi — matnning bosh fikri."),
    Q("Sarlavha nima?", "Asarning nomi", ["Asarning oxirgi gapi", "Muallifning ismi", "Kitob narxi"], x="Sarlavha asar mazmunini qisqa ifodalaydi."),
    Q("Bosh fikr nima?", "Muallif aytmoqchi bo‘lgan eng muhim fikr", ["Matnning birinchi so‘zi", "Qahramonning ismi", "Kitobning sahifasi"],
      x="Bosh fikr — asarning asosiy g‘oyasi."),
    Q("Asarni yozgan kishi kim deyiladi?", "Muallif", ["Qahramon", "Kitobxon", "Sotuvchi"], x="Asar muallifi uni yaratgan ijodkordir."),
    Q("Asardagi voqealarda ishtirok etgan shaxslar nima deyiladi?", "Qahramonlar", ["Mualliflar", "Tomoshabinlar", "Kitobxonlar"], x="Voqea ishtirokchilari — qahramonlar."),
    Q("Ijobiy qahramon qanday bo‘ladi?", "Yaxshi fazilatlarga ega", ["Doim yolg‘on gapiradi", "Hammani xafa qiladi", "Hech narsa qilmaydi"],
      x="Ijobiy qahramon mehribon, halol, mard bo‘ladi."),
    Q("Reja nima?", "Matn qismlarining qisqa tartibli ro‘yxati", ["Matnning sarlavhasi", "Matndagi eng uzun gap", "Muallif haqida ma’lumot"], d=2,
      x="Reja matnni qayta hikoya qilishga yordam beradi."),
    TF("Reja matnni qayta hikoya qilishga yordam beradi.", True, x="Reja bandlari voqealar tartibini eslatadi."),
    TF("Sarlavha doim matnning oxirida yoziladi.", False, x="Sarlavha matn boshida yoziladi."),
    MATCH("Atamani ma’nosi bilan juftlang", [("sarlavha", "asarning nomi"), ("muallif", "asarni yozgan kishi"), ("qahramon", "voqea ishtirokchisi"),
                                            ("reja", "qismlar tartibi"), ("bosh fikr", "eng muhim fikr"), ("yakun", "voqeaning tugashi")], d=2),
]
T.topic("terms", "🔖", L("Qahramon, sarlavha, reja, bosh fikr", "Character, title, plan, main idea", "Герой, заглавие, план, главная мысль"), C4,
        "Asarni tahlil qilishda quyidagi tushunchalar yordam beradi:\n"
        "• Muallif — asarni yozgan kishi; qahramon — voqea ishtirokchisi (ijobiy yoki salbiy).\n"
        "• Sarlavha — asarning nomi, u mazmunni qisqa ifodalaydi.\n"
        "• Reja — matn qismlarining tartibli ro‘yxati: boshlanma → voqealar rivoji → yakun.\n"
        "• Bosh fikr — muallif aytmoqchi bo‘lgan eng muhim fikr.", items=items)

R1 = ("Nodira har kuni kechqurun kundalik yozardi. U kun davomida nima o‘rganganini, kimga yordam berganini va qanday xato "
      "qilganini qayd etardi. Yil oxirida kundalikni varaqlab, qanchalik o‘sganini ko‘rib hayron qoldi. Endi u "
      "sinfdoshlariga ham kundalik yuritishni maslahat beradi.")
R2 = ("Qishloqdagi eski ko‘prik yiqilish arafasida edi. Kattalar uni tuzatishni “ertaga, indinga” deb kechiktirishardi. Bir "
      "kuni Ahmad ismli bola maktabdagi do‘stlari bilan maslahatlashib, mahalla oqsoqoliga xat yozdi. Oqsoqol xatni o‘qib, "
      "hasharni e’lon qildi. Bir hafta ichida yangi, mustahkam ko‘prik qurildi.")
R3 = ("Bahodir yangi velosiped olgach, uni hech kimga bermay qo‘ydi. Bir kuni u yo‘lda yiqilib, velosipedining zanjiri tushib "
      "ketdi. Uni tuzatishga Sardor yordam berdi, garchi Bahodir unga velosipedini bermagan bo‘lsa ham. Shundan so‘ng Bahodir "
      "do‘stlariga velosipedini navbat bilan minishni taklif qildi.")
items = [
    Q("Nodira har kuni kechqurun nima qilardi?", "Kundalik yozardi", ["Televizor ko‘rardi", "Rasm chizardi", "Sayrga chiqardi"], text=R1, x="U har kuni kundalik yozardi."),
    Q("Nodira kundalikka nimalarni yozardi?", "O‘rganganlari, yordamlari va xatolarini", ["Faqat ob-havoni", "Faqat o‘yinlarini", "Do‘stlarining sirlarini"], text=R1,
      x="U nima o‘rganganini, kimga yordam berganini va xatolarini qayd etardi."),
    Q("Yil oxirida Nodira nimani ko‘rdi?", "Qanchalik o‘sganini", ["Daftari tugaganini", "Xatolari ko‘payganini", "Kundalik yo‘qolganini"], text=R1,
      x="U kundalikni varaqlab, o‘sganini ko‘rdi."),
    Q("Nodiraning odatidan qanday xulosa chiqadi?", "O‘z ustida ishlash o‘sishga yordam beradi", ["Kundalik yozish vaqtni yo‘qotadi", "Xatolarni yashirish kerak",
                                                                                                  "Faqat kattalar kundalik yozadi"], text=R1, d=2,
      x="Kundalik Nodiraga o‘z yutuq va xatolarini ko‘rishga yordam berdi."),
    Q("Ko‘prik qanday ahvolda edi?", "Yiqilish arafasida edi", ["Yangi qurilgan edi", "Suv ostida qolgan edi", "Juda keng edi"], text=R2,
      x="“Eski ko‘prik yiqilish arafasida edi.”"),
    Q("Ahmad kimga xat yozdi?", "Mahalla oqsoqoliga", ["O‘qituvchisiga", "Gazetaga", "Buvisiga"], text=R2, x="U mahalla oqsoqoliga xat yozdi."),
    Q("Oqsoqol xatni o‘qib nima qildi?", "Hasharni e’lon qildi", ["Xatni tashlab yubordi", "Ko‘prikni yopib qo‘ydi", "Ahmadni urishdi"], text=R2,
      x="Oqsoqol hashar e’lon qildi."),
    Q("Yangi ko‘prik qancha vaqtda qurildi?", "Bir hafta ichida", ["Bir yilda", "Bir kunda", "Bir oyda"], text=R2, x="“Bir hafta ichida yangi ko‘prik qurildi.”"),
    Q("Ahmadning qaysi fazilati namoyon bo‘ldi?", "Tashabbuskorligi", ["Dangasaligi", "Qo‘rqoqligi", "Maqtanchoqligi"], text=R2, d=2,
      x="Kattalar kechiktirgan ishni u boshlab berdi."),
    Q("Hikoyaga mos maqolni tanlang.", "Birlashgan o‘zar, birlashmagan to‘zar.", ["Qo‘rqqanga qo‘sh ko‘rinar.", "Ko‘rpangga qarab oyoq uzat.", "Qush uyasida ko‘rganini qiladi."],
      text=R2, d=3, x="Mahalla birlashib, ko‘prikni bir haftada qurdi."),
    ORDER("Hikoya rejasini tartib bilan tuzing", "Eski ko‘prik → Ahmadning xati → Hashar → Yangi ko‘prik", sep=" → ", d=2,
          x="Reja voqealar tartibini ko‘rsatadi."),
    Q("Bahodir avval qanday edi?", "Velosipedini hech kimga bermasdi", ["Velosiped minishni bilmasdi", "Hammaga velosiped berardi", "Velosipedni sotmoqchi edi"],
      text=R3, x="U velosipedini hech kimga bermay qo‘ydi."),
    Q("Zanjirni tuzatishga kim yordam berdi?", "Sardor", ["Bahodirning dadasi", "Usta", "Hech kim"], text=R3, x="Sardor yordam berdi."),
    Q("Bahodir nima uchun o‘zgardi?", "Sardorning yaxshiligi ta’sir qildi", ["Velosipedi buzilib qoldi", "Kattalar majbur qildi", "Velosiped eskirdi"], text=R3, d=2,
      x="Sardor unga beg‘araz yordam berdi va bu Bahodirni o‘zgartirdi."),
    Q("Bahodirda qanday o‘zgarish yuz berdi?", "Xasislikdan saxiylikka o‘tdi", ["Mehribonlikdan jahldorlikka o‘tdi", "Umuman o‘zgarmadi", "Velosipedni tashlab ketdi"],
      text=R3, d=3, x="Endi u do‘stlariga velosipedini navbat bilan minishni taklif qildi."),
    TF("Nodira sinfdoshlariga kundalik yuritishni maslahat beradi.", True, text=R1, x="Matnning oxirgi gapi."),
    TF("Kattalar ko‘prikni darhol tuzatishdi.", False, text=R2, x="Kattalar ishni kechiktirishardi, hasharni Ahmadning xati boshlab berdi."),
    TF("Sardor Bahodirga yordam bermadi.", False, text=R3, x="Sardor zanjirni tuzatishga yordam berdi."),
    ORDER("So‘zlardan gap tuzing", "Yaxshilik odamni o‘zgartiradi", d=1, x="Sardorning yaxshiligi Bahodirni saxiy qildi."),
]
T.topic("reflect", "💡", L("O‘qib, xulosa chiqaramiz", "Read and reflect", "Читаем и делаем выводы"), C4,
        "Hikoyani o‘qigach, o‘zingizga savol bering:\n"
        "• Voqea nimadan boshlandi va qanday tugadi? (sabab → natija)\n"
        "• Qahramon qanday o‘zgardi va nima uchun?\n"
        "• Hikoyaga qaysi maqol mos keladi? Qisqa reja tuzib, hikoyani qayta so‘zlab bering.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["genres", "terms", "reflect"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["proverbs", "riddles", "tales", "homeland", "nature", "poem", "writers", "friendship", "fables", "genres", "terms", "reflect"], C4, level=3)

T.write()
