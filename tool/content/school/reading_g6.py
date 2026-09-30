"""Adabiyot, 6-sinf: dostonlar va xalq og‘zaki ijodi, mumtoz adabiyot, XX asr o‘zbek adabiyoti, adabiyot nazariyasi.

Faktlar — darsliklarda keltiriladigan umumma’lum ma’lumotlar; misol matnlar, she’r parchalari va hikoyalar o‘zimiz yozgan.
5-sinf savollari takrorlanmaydi: mavzular chuqurroq va boshqa tomondan yoritiladi.
Qayta yaratish: python3 tool/content/school/reading_g6.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F401,F403

rnd = random.Random(66)
T = Course("reading", 6, L("Adabiyot", "Literature", "Литература"))

C1 = "1-chorak. Dostonlar va xalq og‘zaki ijodi"
C2 = "2-chorak. Mumtoz adabiyot"
C3 = "3-chorak. XX asr o‘zbek adabiyoti"
C4 = "4-chorak. Adabiyot nazariyasi"

# ============================================================ 1-chorak
items = [
    Q("Alpomishning asl ismi nima?", "Hakimbek", ["Qorajon", "Ultontoz", "Yodgor"], x="Dostonda Alpomishning asl ismi — Hakimbek."),
    Q("Alpomishning otasi kim?", "Boybo‘ri", ["Boysari", "Toychixon", "Ultontoz"], x="Alpomish — Boybo‘rining o‘g‘li."),
    Q("Barchinning otasi kim?", "Boysari", ["Boybo‘ri", "Qorajon", "Toychixon"], d=2, x="Barchin — Boysarining qizi."),
    Q("Alpomish qaysi elning qahramoni?", "Qo‘ng‘irot", ["Chambil", "Kalmoq", "Hirot"], x="Alpomish — Qo‘ng‘irot elining botiri."),
    Q("Alpomishga do‘st tutingan kalmoq botiri kim?", "Qorajon", ["Ultontoz", "Toychixon", "Avazxon"], x="Qorajon Alpomishga do‘st tutinib, unga yordam bergan."),
    Q("Alpomish yo‘qligida taxtni egallab olgan kim?", "Ultontoz", ["Qorajon", "Yodgor", "Boysari"], d=2, x="Ultontoz xiyonat qilib, taxtni egallaydi."),
    Q("Alpomishning singlisi kim?", "Qaldirg‘och", ["Barchin", "Oygul", "Zumrad"], d=2, x="Qaldirg‘ochoy — Alpomishning singlisi."),
    Q("Alpomishning o‘g‘li kim?", "Yodgor", ["Qorajon", "Hakimbek", "Avazxon"], d=2, x="Yodgor — Alpomish va Barchinning o‘g‘li."),
    Q("Alpomish necha yil zindonda qolgan?", "7 yil", ["1 yil", "3 yil", "40 yil"], d=2, x="Dostonda Alpomish yetti yil zindonda qoladi."),
    Q("Boysari ko‘chib ketgan va Alpomish Barchinni izlab borgan yurt qaysi?", "Kalmoq yurti", ["Chambil", "Misr", "Rim"], d=2,
      x="Boysari kalmoq yurtiga ko‘chib ketadi, Alpomish uni izlab boradi."),
    Q("“Alpomish” dostonining necha yillik yubileyi 1999-yilda nishonlangan?", "1000 yillik", ["100 yillik", "500 yillik", "3000 yillik"],
      x="1999-yilda “Alpomish” dostoni yaratilganining 1000 yilligi keng nishonlangan."),
    Q("Baxshi dostondagi she’riy qismlarni qanday ijro etadi?", "Kuylab", ["Rasmga chizib", "Raqs bilan", "Ichida o‘qib"], x="She’riy qismlar do‘mbira jo‘rligida kuylanadi."),
    Q("Dostonda qahramonning kuch-qudrati qanday tasvirlanadi?", "Oshirib, mubolag‘a bilan", ["Kichraytirib", "Umuman tasvirlanmaydi", "Faqat raqamlar bilan"], d=2,
      x="Xalq dostonlarida qahramon kuchi mubolag‘a bilan ulug‘lanadi."),
    Q("“Alpomish” dostonining asosiy g‘oyasi qaysi?", "El birligi va sadoqat", ["Boylik orttirish", "Sayohat qilish", "Maqtanchoqlik"],
      x="Doston el-yurt birligi, vafo va sadoqatni ulug‘laydi."),
    TF("Alpomishning asl ismi — Hakimbek.", True, x="Alpomish — uning laqabi, asl ismi Hakimbek."),
    TF("Qorajon Alpomishning ashaddiy dushmani bo‘lib qolgan.", False, x="Qorajon Alpomishga do‘st tutinib, unga yordam bergan."),
    TF("Ultontoz — Alpomishga sodiq qolgan qahramon.", False, d=2, x="Ultontoz xoinlik qilib, taxtni egallab oladi."),
    MATCH("Doston qahramonini u haqidagi ma’lumot bilan juftlang", [("Hakimbek", "Alpomishning asl ismi"), ("Boybo‘ri", "Alpomishning otasi"),
                                                                   ("Boysari", "Barchinning otasi"), ("Qorajon", "Alpomishning do‘sti"),
                                                                   ("Ultontoz", "taxtni egallagan xoin"), ("Yodgor", "Alpomishning o‘g‘li"),
                                                                   ("Qaldirg‘och", "Alpomishning singlisi")], d=2),
    ORDER("So‘zlardan gap tuzing", "Alpomish elini xoinlardan qutqardi", d=1, x="Dostonning yakunida Alpomish qaytib, elini Ultontoz zulmidan qutqaradi."),
]
T.topic("alpomish", "🐎", L("“Alpomish” dostoni qahramonlari", "Heroes of the epic Alpomish", "Герои дастана «Алпамыш»"), C1,
        "“Alpomish” — o‘zbek xalqining qahramonlik dostoni; 1999-yilda uning 1000 yilligi nishonlangan.\n"
        "• Alpomish (asl ismi Hakimbek) — Qo‘ng‘irot elidan, otasi Boybo‘ri. Qallig‘i Barchin — Boysarining qizi.\n"
        "• Boysari kalmoq yurtiga ko‘chib ketadi; Alpomish uni izlab borib, kalmoq botiri Qorajon bilan do‘stlashadi.\n"
        "• Alpomish yetti yil zindonda qoladi, bu orada Ultontoz taxtni egallaydi. Alpomish qaytib, elini xoinlardan qutqaradi.\n"
        "• Singlisi — Qaldirg‘och, o‘g‘li — Yodgor.", items=items)

items = [
    Q("Go‘ro‘g‘li ismi qanday rivoyat bilan bog‘lanadi?", "Go‘rda tug‘ilgan bola", ["Tog‘da o‘sgan bola", "Dengizdan kelgan bola", "Oydan tushgan bola"], d=2,
      x="Rivoyatga ko‘ra, u go‘rda tug‘ilgan, shuning uchun “go‘r o‘g‘li” — Go‘ro‘g‘li deb atalgan."),
    Q("Go‘ro‘g‘li hukmronlik qilgan yurt qanday ataladi?", "Chambil", ["Qo‘ng‘irot", "Kalmoq", "Hirot"], x="Go‘ro‘g‘li — Chambil yurtining botir hukmdori."),
    Q("Go‘ro‘g‘lining asrandi o‘g‘illaridan biri kim?", "Avazxon", ["Alpomish", "Qorajon", "Farhod"], x="Go‘ro‘g‘li Avazxonni o‘g‘il qilib olgan."),
    Q("Go‘ro‘g‘lining yana bir asrandi o‘g‘li kim?", "Hasanxon", ["Yodgor", "Ultontoz", "Bahrom"], d=2, x="Avazxon va Hasanxon — Go‘ro‘g‘lining asrandi o‘g‘illari."),
    Q("Qaysi doston “Go‘ro‘g‘li” turkumiga kiradi?", "“Malika ayyor”", ["“Alpomish”", "“Layli va Majnun”", "“Oygul bilan Baxtiyor”"],
      x="“Malika ayyor” — Go‘ro‘g‘li turkumidagi dostonlardan biri."),
    Q("Qaysi doston ham “Go‘ro‘g‘li” turkumiga mansub?", "“Yunus pari”", ["“Farhod va Shirin”", "“Alpomish”", "“Sab’ai sayyor”"], d=2,
      x="“Yunus pari” — Go‘ro‘g‘li turkumiga kiradi."),
    Q("“Turkum” deganda nima tushuniladi?", "Bir qahramon haqidagi dostonlar majmui", ["Bitta qisqa she’r", "Maqollar lug‘ati", "Topishmoqlar to‘plami"],
      x="Go‘ro‘g‘li, uning o‘g‘illari va nabiralari haqidagi dostonlar bitta turkumni tashkil etadi."),
    Q("Go‘ro‘g‘li haqidagi dostonlar qayerda mashhur?", "Ko‘plab turkiy xalqlar orasida", ["Faqat bitta qishloqda", "Faqat Yevropada", "Hech qayerda"], d=2,
      x="Go‘ro‘g‘li (Ko‘ro‘g‘li) haqidagi dostonlar turkman, ozarbayjon va boshqa xalqlarda ham bor."),
    Q("Qaysi doston qahramonlik dostoni?", "“Alpomish”", ["“Tohir va Zuhra”", "“Layli va Majnun”", "“Sab’ai sayyor”"],
      x="“Alpomish” — xalq qahramonlik dostoni."),
    Q("“Tohir va Zuhra” qanday doston?", "Ishqiy-romantik doston", ["Qahramonlik dostoni", "Masal", "Roman"], d=2,
      x="Unda ikki yoshning sof muhabbati kuylanadi."),
    Q("Xalq dostonlari mavzusiga ko‘ra qanday turlarga bo‘linadi?", "Qahramonlik, ishqiy-romantik, tarixiy", ["Qisqa va uzun", "Kulgili va qayg‘uli", "Yangi va eski"],
      d=2, x="Masalan: “Alpomish” — qahramonlik, “Tohir va Zuhra” — ishqiy-romantik doston."),
    Q("Qo‘rg‘on dostonchilik maktabining mashhur baxshisi kim?", "Ergash Jumanbulbul o‘g‘li", ["Alisher Navoiy", "Abdulla Qodiriy", "Gulxaniy"], d=3,
      x="Ergash Jumanbulbul o‘g‘li — Qo‘rg‘on maktabining yirik vakili."),
    Q("Quyidagilardan qaysi biri mashhur xalq baxshisi?", "Po‘lkan shoir", ["Zahiriddin Bobur", "Hamid Olimjon", "Abdulla Oripov"], d=2,
      x="Xalq orasida baxshilar “shoir” deb ham atalgan: Po‘lkan shoir, Islom shoir."),
    Q("Dostonni yod bilib, kuylab ijro etuvchi xalq ijodkori yana qanday ataladi?", "Dostonchi", ["Kotib", "Muallim", "Me’mor"], d=2,
      x="Baxshi — dostonchi, xalq dostonlari ijrochisi."),
    Q("Dostonlarda nasriy va she’riy qismlar qanday keladi?", "Almashinib keladi", ["Faqat nasr bo‘ladi", "Faqat bitta misra bo‘ladi", "Umuman bo‘lmaydi"],
      x="Voqea nasrda hikoya qilinadi, qahramonlar nutqi va kechinmalari she’rda kuylanadi."),
    TF("“Go‘ro‘g‘li” turkumida ko‘plab dostonlar bor.", True, x="Turkum Go‘ro‘g‘li va uning avlodlari haqidagi ko‘p dostonlarni o‘z ichiga oladi."),
    TF("Avazxon — Go‘ro‘g‘lining dushmani.", False, x="Avazxon — Go‘ro‘g‘lining asrandi o‘g‘li."),
    TF("Baxshilar uzun dostonlarni bir necha kecha davomida kuylagan.", True, d=2, x="Katta dostonlar bir necha kechada to‘liq aytib berilgan."),
    MATCH("Nomni u bog‘liq doston yoki tushuncha bilan juftlang", [("Chambil", "Go‘ro‘g‘li yurti"), ("G‘irot", "Go‘ro‘g‘lining oti"), ("Avazxon", "asrandi o‘g‘il"),
                                                                  ("Qo‘ng‘irot", "Alpomish eli"), ("“Tohir va Zuhra”", "ishqiy-romantik doston"),
                                                                  ("Ergash Jumanbulbul o‘g‘li", "mashhur baxshi")], d=2),
]
T.topic("gorogly", "🏇", L("“Go‘ro‘g‘li” turkumi va baxshilar", "The Gorogly cycle and bakhshis", "Цикл «Гёроглы» и бахши"), C1,
        "“Go‘ro‘g‘li” — bir qahramon atrofida birlashgan dostonlar turkumi; u ko‘plab turkiy xalqlarda mashhur.\n"
        "• Go‘ro‘g‘li — Chambil yurtining botir hukmdori, oti — G‘irot. Nomi “go‘rda tug‘ilgan” degan rivoyat bilan bog‘lanadi.\n"
        "• Asrandi o‘g‘illari — Avazxon va Hasanxon. Turkumdagi dostonlar: “Avazxon”, “Malika ayyor”, “Yunus pari” va boshqalar.\n"
        "• Dostonlar turlari: qahramonlik (“Alpomish”), ishqiy-romantik (“Tohir va Zuhra”), tarixiy.\n"
        "• Mashhur baxshilar: Ergash Jumanbulbul o‘g‘li, Fozil Yo‘ldosh o‘g‘li, Po‘lkan shoir, Islom shoir.", items=items)

items = [
    Q("Onalar bolani uxlatayotganda aytadigan qo‘shiq qanday ataladi?", "Alla", ["Yor-yor", "Lapar", "Terma"], x="Alla — mehr va orzu-umid to‘la ona qo‘shig‘i."),
    Q("Kelinni kuzatishda aytiladigan to‘y qo‘shig‘i qaysi?", "Yor-yor", ["Alla", "“Sust xotin”", "“Boychechak”"], x="Yor-yor — to‘y marosimi qo‘shig‘i."),
    Q("Yomg‘ir chaqirish uchun aytilgan marosim qo‘shig‘i qaysi?", "“Sust xotin”", ["“Yor-yor”", "Alla", "“Boychechak”"], d=2,
      x="Qurg‘oqchilikda yomg‘ir so‘rab “Sust xotin” aytilgan."),
    Q("Bahor kelishi bilan bolalar aytadigan qo‘shiq qaysi?", "“Boychechak”", ["“Sust xotin”", "“Yor-yor”", "Alla"], x="Boychechak — bahorning ilk guli."),
    Q("Yigit va qiz navbatma-navbat aytadigan hazil qo‘shiq qanday ataladi?", "Lapar", ["Alla", "Terma", "Ruboiy"], d=2, x="Lapar — aytishuv tarzidagi qo‘shiq."),
    Q("Kulgili qisqa xalq hikoyasi qanday ataladi?", "Latifa", ["Doston", "Rivoyat", "G‘azal"], x="Latifa — kutilmagan kulgili yakunli qisqa hikoya."),
    Q("O‘zbek latifalarining mashhur qahramoni kim?", "Nasriddin Afandi", ["Alpomish", "Go‘ro‘g‘li", "Farhod"], x="Afandi latifalari xalq orasida juda mashhur."),
    Q("So‘z o‘yiniga asoslangan hazil-mutoyiba bahsi qanday ataladi?", "Askiya", ["Alla", "Doston", "Sanama"], d=2, x="Askiyada ikki yoki bir necha kishi so‘z o‘yini bilan bahslashadi."),
    Q("Askiya ko‘proq qaysi hududda rivojlangan?", "Farg‘ona vodiysida", ["Xorazmda", "Qoraqalpog‘istonda", "Surxondaryoda"], d=3,
      x="Askiya ayniqsa Farg‘ona vodiysi shaharlarida keng tarqalgan."),
    Q("Baxshi dostonni boshlashdan oldin aytadigan qisqa she’riy parcha nima deyiladi?", "Terma", ["Latifa", "Alla", "Maqol"], d=3,
      x="Terma bilan baxshi tinglovchilarni doston tinglashga hozirlaydi."),
    Q("O‘yinda kim boshlashini aniqlash uchun aytiladigan bolalar she’ri qanday ataladi?", "Sanama", ["Alla", "Yor-yor", "Terma"], d=2,
      x="Sanama aytilayotganda so‘zlar bolalarga navbatma-navbat “sanaladi”."),
    Q("Dalada yer haydash paytida aytilgan qo‘shiq qaysi turga kiradi?", "Mehnat qo‘shiqlari", ["Marosim qo‘shiqlari", "Alla", "Latifa"], d=2,
      x="Mehnat qo‘shiqlari ishni yengillashtirgan, ritm bergan."),
    Q("Xalq qo‘shiqlari qaysi adabiy turga yaqin?", "Lirika", ["Epos", "Drama", "Publitsistika"], d=3, x="Qo‘shiqlarda his-tuyg‘u ifodalanadi — bu lirikaning belgisi."),
    Q("Latifa odatda qanday tugaydi?", "Kutilmagan, kulgili xulosa bilan", ["Qayg‘uli yakun bilan", "Qofiya bilan", "Uzun ro‘yxat bilan"], d=2,
      x="Latifaning kuchi — kutilmagan va topqir yakunida."),
    TF("Alla — to‘y qo‘shig‘i.", False, x="Alla — bolani uxlatish uchun aytiladigan qo‘shiq; to‘y qo‘shig‘i — yor-yor."),
    TF("Latifalarda kulgi orqali odamlarning kamchiliklari fosh etiladi.", True, x="Masalan, xasislik, maqtanchoqlik, dangasalik ustidan kulinadi."),
    TF("“Boychechak” — bahor bilan bog‘liq qo‘shiq.", True, x="Uni bolalar bahorning ilk gullarini ko‘tarib, uyma-uy yurib aytishgan."),
    MATCH("Janrni u aytiladigan vaziyat bilan juftlang", [("alla", "bola uxlatishda"), ("yor-yor", "to‘yda kelin kuzatishda"), ("“Sust xotin”", "yomg‘ir chaqirishda"),
                                                         ("“Boychechak”", "bahorni kutib olishda"), ("sanama", "o‘yinda navbat tanlashda"),
                                                         ("terma", "doston boshlanishida")], d=2),
    ORDER("So‘zlardan gap tuzing", "Ona bolasiga mayin alla aytdi", d=1, x="Alla — onaning mehr qo‘shig‘i."),
]
T.topic("folk_genres", "🎵", L("Xalq qo‘shiqlari, latifa va askiya", "Folk songs, anecdotes and askiya", "Народные песни, анекдоты и аския"), C1,
        "Xalq og‘zaki ijodida kichik janrlar ko‘p:\n"
        "• Qo‘shiqlar: alla (bola uxlatishda), yor-yor (to‘yda), lapar (yigit-qiz aytishuvi), mehnat qo‘shiqlari,\n"
        "  marosim qo‘shiqlari (“Boychechak” — bahorni kutib olish, “Sust xotin” — yomg‘ir chaqirish).\n"
        "• Bolalar folklori: sanama, tez aytish, topishmoq.\n"
        "• Latifa — kulgili qisqa hikoya (qahramoni — Nasriddin Afandi); askiya — so‘z o‘yiniga asoslangan hazil bahsi.\n"
        "• Terma — baxshi doston oldidan aytadigan she’riy parcha.", items=items)

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["alpomish", "gorogly", "folk_genres"], C1)

# ============================================================ 2-chorak
XAMSA = ["“Hayrat ul-abror”", "“Farhod va Shirin”", "“Layli va Majnun”", "“Sab’ai sayyor”", "“Saddi Iskandariy”"]
items = [
    Q("“Xamsa”ning ikkinchi dostoni qaysi?", "“Farhod va Shirin”", ["“Hayrat ul-abror”", "“Saddi Iskandariy”", "“Sab’ai sayyor”"],
      x="Tartib: “Hayrat ul-abror”, “Farhod va Shirin”, “Layli va Majnun”, “Sab’ai sayyor”, “Saddi Iskandariy”."),
    Q("“Xamsa”ning uchinchi dostoni qaysi?", "“Layli va Majnun”", ["“Farhod va Shirin”", "“Hayrat ul-abror”", "“Saddi Iskandariy”"], d=2,
      x="“Layli va Majnun” — “Xamsa”ning uchinchi dostoni."),
    Q("“Xamsa”ning to‘rtinchi dostoni qaysi?", "“Sab’ai sayyor”", ["“Layli va Majnun”", "“Farhod va Shirin”", "“Hayrat ul-abror”"], d=3,
      x="“Sab’ai sayyor” — to‘rtinchi doston."),
    Q("“Xamsa”ning oxirgi, beshinchi dostoni qaysi?", "“Saddi Iskandariy”", ["“Sab’ai sayyor”", "“Hayrat ul-abror”", "“Layli va Majnun”"],
      x="“Saddi Iskandariy” — “Xamsa”ning yakunlovchi dostoni."),
    ORDER("“Xamsa” dostonlarini tartib bilan joylang", " → ".join(XAMSA), sep=" → ", d=3, x="“Xamsa” shu tartibda tuzilgan."),
    Q("Farhod qaysi yurtning shahzodasi edi?", "Chin (Xitoy)", ["Armaniston", "Rim", "Hindiston"], d=2, x="Farhod — Chin xoqonining o‘g‘li."),
    Q("Shirin qaysi yurtdan edi?", "Armaniston", ["Chin", "Misr", "Yunoniston"], d=3, x="Shirin — Armaniston malikasi Mehinbonuning jiyani."),
    Q("Farhod qanday qahramon sifatida tasvirlangan?", "Ko‘p hunar egallagan mehnatkash", ["Dangasa va maqtanchoq", "Faqat ovchi", "Hech narsa bilmaydigan"], d=2,
      x="Farhod toshtaroshlik, me’morlik kabi hunarlarni egallagan, el uchun ariq qazigan."),
    Q("Majnunning asl ismi nima?", "Qays", ["Farhod", "Bahrom", "Iskandar"], x="“Majnun” — laqab, asl ismi Qays."),
    Q("“Sab’ai sayyor” dostonining bosh qahramoni kim?", "Bahrom", ["Farhod", "Qays", "Iskandar"], d=3, x="Doston shoh Bahrom haqida."),
    Q("“Saddi Iskandariy” dostoni kim haqida?", "Iskandar haqida", ["Farhod haqida", "Majnun haqida", "Bahrom haqida"], x="Doston Iskandar (Aleksandr Makedonskiy) haqida."),
    Q("“Sab’ai sayyor” nomining ma’nosi qaysi?", "Yetti sayyora", ["Besh do‘st", "Ikki oshiq", "Uch botir"], d=3,
      x="“Sab’a” — yetti; dostonda yetti hikoya aytiladi."),
    Q("Navoiy turkiy she’rlarida qaysi taxallusni qo‘llagan?", "Navoiy", ["Foniy", "Bobur", "Zahiriddin"], x="Turkiy she’rlarda — Navoiy, forsiy she’rlarda — Foniy."),
    Q("Navoiy forsiy she’rlarida qaysi taxallusni qo‘llagan?", "Foniy", ["Navoiy", "Nodira", "Cho‘lpon"], d=2, x="Navoiy forsiy tilda Foniy taxallusi bilan yozgan."),
    Q("Navoiyning to‘rt devondan iborat she’rlar to‘plami qanday ataladi?", "“Xazoyin ul-maoniy”", ["“Xamsa”", "“Boburnoma”", "“Mahbub ul-qulub”"], d=3,
      x="“Xazoyin ul-maoniy” — “Ma’nolar xazinasi”, to‘rt devondan iborat."),
    Q("Navoiyning qushlar tilidan yozilgan falsafiy dostoni qaysi?", "“Lison ut-tayr”", ["“Farhod va Shirin”", "“Zarbulmasal”", "“Saddi Iskandariy”"], d=3,
      x="“Lison ut-tayr” — “Qush tili” degani."),
    Q("Navoiy “Xamsa”ni qaysi yillarda yozgan?", "1483–1485-yillarda", ["1441–1443-yillarda", "1500–1510-yillarda", "1526–1530-yillarda"], d=3,
      x="Navoiy “Xamsa”ni taxminan ikki yil ichida yaratgan."),
    Q("Alisher Navoiy qaysi yilda vafot etgan?", "1501-yilda", ["1441-yilda", "1530-yilda", "1483-yilda"], x="Navoiy 1441–1501-yillarda yashagan."),
    Q("Navoiyning otasi kim bo‘lgan?", "G‘iyosiddin Kichkina", ["Umarshayx Mirzo", "Husayn Boyqaro", "Amir Temur"], d=3, x="Navoiyning otasi — G‘iyosiddin Kichkina."),
    TF("“Farhod va Shirin” dostonida Farhod mehnatkash va hunarli qahramon sifatida tasvirlangan.", True, x="Farhod hunari bilan el hurmatini qozonadi."),
    TF("Majnunning asl ismi — Bahrom.", False, x="Majnunning asl ismi — Qays; Bahrom — “Sab’ai sayyor” qahramoni."),
    MATCH("Dostonni u haqidagi ma’lumot bilan juftlang", [("“Hayrat ul-abror”", "birinchi doston, pand-nasihat"), ("“Farhod va Shirin”", "hunarmand shahzoda"),
                                                         ("“Layli va Majnun”", "Qays ismli oshiq"), ("“Sab’ai sayyor”", "Bahrom va yetti hikoya"),
                                                         ("“Saddi Iskandariy”", "Iskandar haqida")], d=2),
]
T.topic("navoi", "📜", L("Alisher Navoiy va “Xamsa”", "Alisher Navoi and Khamsa", "Алишер Навои и «Хамса»"), C2,
        "Alisher Navoiy (1441–1501) turkiy she’rlarida “Navoiy”, forsiy she’rlarida “Foniy” taxallusini qo‘llagan.\n"
        "• “Xamsa” (1483–1485): “Hayrat ul-abror” → “Farhod va Shirin” → “Layli va Majnun” → “Sab’ai sayyor” → “Saddi Iskandariy”.\n"
        "• Qahramonlar: Farhod — Chin shahzodasi, ko‘p hunarli; Shirin — Armaniston malikasi; Majnun (asl ismi Qays); Bahrom; Iskandar.\n"
        "• Boshqa asarlari: “Xazoyin ul-maoniy” (to‘rt devon), “Lison ut-tayr” (qushlar tilidan doston).", items=items)

items = [
    Q("Boburning otasi kim bo‘lgan?", "Umarshayx Mirzo", ["Husayn Boyqaro", "Amir Temur", "G‘iyosiddin Kichkina"], d=2, x="Umarshayx Mirzo — Farg‘ona hukmdori."),
    Q("Bobur necha yoshida Farg‘ona taxtiga o‘tirgan?", "12 yoshida", ["5 yoshida", "30 yoshida", "50 yoshida"], d=2, x="Otasi vafotidan so‘ng, 1494-yilda."),
    Q("Bobur qaysi sulolaga mansub edi?", "Temuriylar", ["Somoniylar", "Qoraxoniylar", "Shayboniylar"], x="Bobur — Amir Temur avlodi, temuriy shahzoda."),
    Q("Bobur Hindistonda asos solgan sulola qanday ataladi?", "Boburiylar", ["Somoniylar", "Shayboniylar", "Qoraxoniylar"], x="Boburiylar Hindistonni uzoq yillar boshqargan."),
    Q("Bobur Hindistonda saltanatga qaysi yili asos solgan?", "1526-yilda", ["1483-yilda", "1441-yilda", "1494-yilda"], d=2, x="1526-yil Panipat jangidan so‘ng."),
    Q("Bobur qaysi yilda vafot etgan?", "1530-yilda", ["1501-yilda", "1483-yilda", "1526-yilda"], d=2, x="Bobur 1483–1530-yillarda yashagan."),
    Q("“Boburnoma” qaysi tilda yozilgan?", "Turkiy (eski o‘zbek) tilda", ["Lotin tilida", "Ingliz tilida", "Xitoy tilida"], x="Asar ona tilimizning go‘zal namunasi."),
    Q("“Boburnoma”ning boshqa nomi qaysi?", "“Vaqoye’”", ["“Xamsa”", "“Devon”", "“Lison ut-tayr”"], d=3, x="“Vaqoye’” — “voqealar” degani."),
    Q("“Boburnoma”da nimalar tasvirlangan?", "Voqealar, shaharlar, tabiat, odamlar", ["Faqat ertaklar", "Faqat matematik masalalar", "Faqat qo‘shiqlar"],
      x="Bobur ko‘rgan shaharlar, o‘simlik va hayvonlar, odamlarni aniq tasvirlagan."),
    Q("Boburning she’riy yo‘lda yozilgan huquqiy asari qaysi?", "“Mubayyin”", ["“Boburnoma”", "“Xamsa”", "“Zarbulmasal”"], d=3, x="“Mubayyin” — she’riy yo‘lda yozilgan."),
    Q("Bobur ruboiylarida qaysi tuyg‘u ayniqsa kuchli?", "Vatan sog‘inchi", ["Dengizga muhabbat", "Kosmosga qiziqish", "Sportga ishtiyoq"], d=2,
      x="Bobur uzoq yurtlarda Vatanini sog‘inib, ta’sirli ruboiylar yozgan."),
    Q("Boburning qizi, “Humoyunnoma” muallifi kim?", "Gulbadanbegim", ["Nodira", "Zulfiya", "Uvaysiy"], d=3, x="Gulbadanbegim — Boburning qizi, tarixiy asar muallifi."),
    Q("Boburdan keyin Hindistonda taxtga o‘tirgan o‘g‘li kim?", "Humoyun", ["Akbar", "Umarshayx", "Shohrux"], d=3, x="Humoyun — Boburning o‘g‘li va vorisi."),
    Q("Bobur tug‘ilgan Andijon qaysi vodiyda joylashgan?", "Farg‘ona vodiysida", ["Zarafshon vodiysida", "Surxon vohasida", "Xorazm vohasida"],
      x="Andijon — Farg‘ona vodiysining qadimiy shahri."),
    Q("Boburning g‘azal va ruboiylari jamlangan to‘plam qanday ataladi?", "Devon", ["Xamsa", "Doston", "Roman"], d=2, x="Shoir she’rlari to‘plami — devon."),
    TF("Bobur Temuriylar sulolasiga mansub.", True, x="Bobur — Amir Temurning avlodi."),
    TF("“Boburnoma” forsiy tilda yozilgan.", False, x="“Boburnoma” turkiy (eski o‘zbek) tilda yozilgan."),
    TF("“Boburnoma” ko‘plab xorijiy tillarga tarjima qilingan.", True, x="Asar ingliz, fransuz, nemis va boshqa tillarda nashr etilgan."),
    MATCH("Shaxsni Boburga qarindoshligi bilan juftlang", [("Umarshayx Mirzo", "Boburning otasi"), ("Humoyun", "Boburning o‘g‘li"), ("Gulbadanbegim", "Boburning qizi"),
                                                          ("Akbar", "Boburning nabirasi"), ("Amir Temur", "Boburning ulug‘ bobosi")], d=2),
]
T.topic("bobur", "👑", L("Zahiriddin Muhammad Bobur", "Zahiriddin Muhammad Babur", "Захириддин Мухаммад Бабур"), C2,
        "Zahiriddin Muhammad Bobur (1483–1530) — Temuriylar sulolasidan, otasi Umarshayx Mirzo Farg‘ona hukmdori bo‘lgan.\n"
        "• 12 yoshida Farg‘ona taxtiga o‘tirgan; 1526-yilda Hindistonda Boburiylar saltanatiga asos solgan.\n"
        "• “Boburnoma” (“Vaqoye’”) — turkiy tilda yozilgan xotira asari: voqealar, shaharlar, tabiat va odamlar tasviri.\n"
        "• She’rlari devonga jamlangan, ruboiylarida Vatan sog‘inchi kuchli; “Mubayyin” — she’riy yo‘lda yozilgan asar.\n"
        "• O‘g‘li Humoyun, qizi Gulbadanbegim (“Humoyunnoma” muallifi), nabirasi Akbar.", items=items)

items = [
    Q("Faqat bir baytdan iborat mustaqil she’r nima deyiladi?", "Fard", ["G‘azal", "Ruboiy", "Qasida"], x="Fard — ikki misrali (bir baytli) mustaqil she’r."),
    Q("Qofiyasi shakldosh (omonim) so‘zlardan tuzilgan to‘rtlik nima deyiladi?", "Tuyuq", ["Ruboiy", "Fard", "Masnaviy"], d=3,
      x="Tuyuqda qofiyadosh so‘zlar bir xil yoziladi, lekin ma’nosi har xil."),
    Q("Ruboiyda odatda qaysi misralar o‘zaro qofiyalanadi?", "1-, 2- va 4-misralar", ["Faqat 1- va 3-misralar", "Hech biri", "Faqat 3-misra"], d=2,
      x="Ruboiyning qofiyalanish tartibi odatda a-a-b-a."),
    Q("G‘azalda matla’dan keyingi baytlarning qaysi misrasi matla’ bilan qofiyalanadi?", "Ikkinchi misrasi", ["Birinchi misrasi", "Hech qaysi", "Faqat oxirgi bayt"], d=3,
      x="G‘azal qofiyasi: a-a, b-a, v-a…"),
    Q("Har bayti o‘zaro qofiyalanadigan, dostonlar yoziladigan she’r shakli qaysi?", "Masnaviy", ["Ruboiy", "Fard", "Tuyuq"], d=3,
      x="Masnaviyda qofiya a-a, b-b, v-v tarzida bo‘ladi; “Xamsa” dostonlari shu shaklda."),
    Q("Besh misrali bandlardan tuzilgan she’r nima deyiladi?", "Muxammas", ["Musaddas", "Ruboiy", "Fard"], x="“Muxammas” — “beshlik” degani."),
    Q("Olti misrali bandlardan tuzilgan she’r nima deyiladi?", "Musaddas", ["Muxammas", "Murabba’", "Tuyuq"], d=3, x="“Musaddas” — “oltilik”."),
    Q("To‘rt misrali bandlardan tuzilgan mumtoz she’r nima deyiladi?", "Murabba’", ["Muxammas", "Fard", "Masnaviy"], d=3, x="“Murabba’” — “to‘rtlik”."),
    Q("Mumtoz she’riyatda eng keng tarqalgan lirik shakl qaysi?", "G‘azal", ["Roman", "Qissa", "Drama"], x="Navoiy, Bobur, Ogahiy va boshqa shoirlar ko‘plab g‘azal yozgan."),
    Q("G‘azal asosan qanday mavzuda yoziladi?", "Ishq va go‘zallik", ["Matematika", "Sport", "Ob-havo"], x="G‘azalning an’anaviy mavzusi — ishq, go‘zallik, vafo."),
    Q("Mumtoz she’riyatdagi vazn tizimi qanday ataladi?", "Aruz", ["Barmoq", "Sarbast", "Qofiya"], x="Mumtoz she’rlar aruz vaznida yozilgan."),
    Q("Aruz vazni nimaga asoslanadi?", "Cho‘ziq va qisqa bo‘g‘inlar navbatiga", ["So‘zlar soniga", "Harflar shakliga", "Gaplar uzunligiga"], d=2,
      x="Aruzda cho‘ziq va qisqa bo‘g‘inlar ma’lum tartibda almashinadi."),
    Q("Shoir she’rlari jamlangan to‘plam mumtoz adabiyotda nima deyiladi?", "Devon", ["Xamsa", "Tazkira", "Qasida"], d=2, x="Masalan, Boburning devoni."),
    Q("Biror kishini yoki voqeani madh etuvchi katta hajmli lirik she’r qaysi?", "Qasida", ["Fard", "Tuyuq", "Ruboiy"], d=3, x="Qasida — tantanali, madhiya ohangidagi she’r."),
    Q("Shoirlar haqidagi ma’lumotlar jamlangan asar nima deyiladi?", "Tazkira", ["Devon", "Doston", "Qasida"], d=3, x="Tazkirada shoirlar hayoti va she’rlaridan namunalar beriladi."),
    Q("Alisher Navoiyning shoirlar haqidagi tazkirasi qaysi?", "“Majolis un-nafois”", ["“Lison ut-tayr”", "“Hayrat ul-abror”", "“Boburnoma”"], d=3,
      x="“Majolis un-nafois” — Navoiy davri shoirlari haqidagi tazkira."),
    TF("Fard — ikki misrali mustaqil she’r.", True, x="Fard bir baytdan, ya’ni ikki misradan iborat."),
    TF("Tuyuq qofiyasida shakldosh (omonim) so‘zlar ishlatiladi.", True, d=2, x="Bu tuyuqning asosiy belgisi."),
    TF("Masnaviy shaklida faqat bitta bayt bo‘ladi.", False, x="Masnaviy ko‘p baytli; har bayt o‘zaro qofiyalanadi."),
    MATCH("She’r shaklini tuzilishi bilan juftlang", [("fard", "bir bayt"), ("ruboiy", "to‘rt misra, a-a-b-a"), ("muxammas", "besh misrali bandlar"),
                                                     ("musaddas", "olti misrali bandlar"), ("masnaviy", "baytlari o‘zaro qofiyalanadi"),
                                                     ("g‘azal", "matla’ bilan boshlanadi")], d=2),
]
T.topic("classic_forms", "🖋️", L("Mumtoz she’r shakllari", "Classical verse forms", "Формы классического стиха"), C2,
        "Mumtoz she’riyat shakllari:\n"
        "• G‘azal — baytlardan tuziladi; matla’dan keyingi baytlarning ikkinchi misrasi matla’ bilan qofiyalanadi (a-a, b-a, v-a).\n"
        "• Ruboiy — to‘rt misra, qofiyasi odatda a-a-b-a; tuyuq — qofiyasi shakldosh so‘zlardan tuzilgan to‘rtlik; fard — bir bayt.\n"
        "• Masnaviy — har bayti o‘zaro qofiyalanadi (dostonlar shu shaklda); murabba’, muxammas, musaddas — 4, 5, 6 misrali bandli she’rlar.\n"
        "• Vazn — aruz (cho‘ziq va qisqa bo‘g‘inlar navbati). She’rlar to‘plami — devon, shoirlar haqidagi asar — tazkira.", items=items)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["navoi", "bobur", "classic_forms"], C2)

# ============================================================ 3-chorak
items = [
    Q("“O‘tkan kunlar” romanining bosh qahramonlari kimlar?", "Otabek va Kumush", ["Anvar va Ra’no", "Farhod va Shirin", "Tohir va Zuhra"],
      x="Roman Otabek va Kumushning muhabbati va taqdiri haqida."),
    Q("“Mehrobdan chayon” romanining bosh qahramonlari kimlar?", "Anvar va Ra’no", ["Otabek va Kumush", "Oygul va Baxtiyor", "Layli va Majnun"], d=2,
      x="“Mehrobdan chayon” — Abdulla Qodiriyning ikkinchi romani."),
    Q("Abdulla Qodiriy hajviy asarlarida qaysi taxallusni qo‘llagan?", "Julqunboy", ["Foniy", "Cho‘lpon", "Hamza"], d=3, x="Julqunboy — Qodiriyning hajviy taxallusi."),
    Q("Abdulla Qodiriy qaysi shaharda tug‘ilgan?", "Toshkentda", ["Andijonda", "Hirotda", "Qo‘qonda"], x="Qodiriy 1894-yilda Toshkentda tug‘ilgan."),
    Q("Cho‘lpon qaysi shaharda tug‘ilgan?", "Andijonda", ["Toshkentda", "Buxoroda", "Xivada"], d=2, x="Cho‘lpon — andijonlik shoir va yozuvchi."),
    Q("Cho‘lponning asl ismi nima?", "Abdulhamid", ["Muso", "Hamid", "G‘afur"], d=2, x="Uning to‘liq ismi — Abdulhamid Sulaymon o‘g‘li Yunusov."),
    Q("“Cho‘lpon” taxallusining ma’nosi nima?", "Tong yulduzi", ["Tog‘ cho‘qqisi", "Katta daryo", "Bahor shamoli"], d=2, x="Cho‘lpon — tongda porlaydigan yorug‘ yulduz."),
    Q("Cho‘lponning mashhur romani qaysi?", "“Kecha va kunduz”", ["“O‘tkan kunlar”", "“Qutlug‘ qon”", "“Sarob”"], x="“Kecha va kunduz” — Cho‘lpon romani."),
    Q("Cho‘lponning ilk she’rlar to‘plami qaysi?", "“Uyg‘onish”", ["“Bolalik”", "“Navoiy”", "“Anor”"], d=3, x="“Uyg‘onish” to‘plami 1922-yilda chop etilgan."),
    Q("Oybekning asl ismi nima?", "Muso Toshmuhammad o‘g‘li", ["Abdulhamid Sulaymon o‘g‘li", "Hamid Olimjon", "G‘afur G‘ulom"], d=3, x="Oybek — Muso Toshmuhammad o‘g‘lining taxallusi."),
    Q("Oybekning Alisher Navoiy hayotiga bag‘ishlangan romani qaysi?", "“Navoiy”", ["“Bolalik”", "“O‘tkan kunlar”", "“Kecha va kunduz”"],
      x="“Navoiy” romanida buyuk shoir hayoti tasvirlangan."),
    Q("Oybekning “Qutlug‘ qon” asari qaysi janrda?", "Roman", ["G‘azal", "Masal", "Ruboiy"], d=2, x="“Qutlug‘ qon” — Oybekning romani."),
    Q("Abdulla Qahhorning hikoyasi qaysi?", "“Anor”", ["“Kecha va kunduz”", "“Navoiy”", "“Mehrobdan chayon”"], d=2, x="“Anor” — Abdulla Qahhorning mashhur hikoyasi."),
    Q("Abdulla Qahhor ko‘proq qaysi janr ustasi sifatida mashhur?", "Hikoya", ["Doston", "G‘azal", "Qasida"], d=2, x="U o‘zbek hikoyachiligining yirik ustasi."),
    Q("“Shum bola” qissasining asosiy ohangi qanday?", "Yumor (kulgi)", ["Tragik qayg‘u", "Ilmiy bayon", "Rasmiy uslub"], x="Qissa kulgili sarguzashtlarga boy."),
    Q("G‘afur G‘ulom qaysi shaharda tug‘ilgan?", "Toshkentda", ["Samarqandda", "Namanganda", "Termizda"], d=3, x="G‘afur G‘ulom 1903-yilda Toshkentda tug‘ilgan."),
    TF("Kumush — “O‘tkan kunlar” romani qahramoni.", True, x="Kumush — Otabekning suyukli rafiqasi."),
    TF("“Kecha va kunduz” romanini Oybek yozgan.", False, x="“Kecha va kunduz” — Cho‘lpon romani."),
    TF("Cho‘lpon ham shoir, ham nosir bo‘lgan.", True, x="U she’rlar bilan birga roman va hikoyalar ham yozgan."),
    MATCH("Adibni taxallusi yoki asl ismi bilan juftlang", [("Oybek", "Muso Toshmuhammad o‘g‘li"), ("Cho‘lpon", "Abdulhamid Sulaymon o‘g‘li"),
                                                           ("Abdulla Qodiriy", "Julqunboy"), ("Alisher Navoiy", "Foniy"), ("Bobur", "Zahiriddin Muhammad")], d=2),
    MATCH("Qahramonni asari bilan juftlang", [("Otabek", "“O‘tkan kunlar”"), ("Ra’no", "“Mehrobdan chayon”"), ("Farhod", "“Xamsa”"),
                                             ("Hakimbek", "“Alpomish”"), ("Hoshimjon", "“Sariq devni minib”")], d=2),
]
T.topic("prose20", "📕", L("XX asr o‘zbek nasri", "20th-century Uzbek prose", "Узбекская проза XX века"), C3,
        "XX asr o‘zbek nasri:\n"
        "• Abdulla Qodiriy (Toshkent; hajviy taxallusi — Julqunboy) — “O‘tkan kunlar” (Otabek va Kumush), “Mehrobdan chayon” (Anvar va Ra’no).\n"
        "• Cho‘lpon (Abdulhamid Sulaymon o‘g‘li; Andijon) — shoir va nosir: “Kecha va kunduz” romani, “Uyg‘onish” to‘plami.\n"
        "  “Cho‘lpon” — tong yulduzi.\n"
        "• Oybek (Muso Toshmuhammad o‘g‘li) — “Navoiy”, “Qutlug‘ qon” romanlari, “Bolalik” qissasi.\n"
        "• G‘afur G‘ulom — “Shum bola” qissasi; Abdulla Qahhor — hikoya ustasi (“Anor”, “O‘g‘ri”).", items=items)

items = [
    Q("Hamid Olimjon qaysi shaharda tug‘ilgan?", "Jizzaxda", ["Andijonda", "Qo‘qonda", "Xivada"], d=2, x="Hamid Olimjon 1909-yilda Jizzaxda tug‘ilgan."),
    Q("“Oygul bilan Baxtiyor” qanday asar?", "Ertak-doston", ["Roman", "Komediya", "Ruboiy"], x="Hamid Olimjon xalq ertaklari asosida yozgan ertak-doston."),
    Q("Zulfiya qaysi shoirning umr yo‘ldoshi bo‘lgan?", "Hamid Olimjon", ["Oybek", "Cho‘lpon", "Erkin Vohidov"], x="Zulfiya — Hamid Olimjonning rafiqasi."),
    Q("Zulfiyaning Hamid Olimjon xotirasiga bag‘ishlangan mashhur she’ri qaysi?", "“Bahor keldi seni so‘roqlab”", ["“O‘zbegim”", "“Sen yetim emassan”", "“Uyg‘onish”"],
      d=3, x="She’rda sadoqat va sog‘inch tuyg‘ulari kuylangan."),
    Q("G‘afur G‘ulomning urush yillarida yozilgan mashhur she’ri qaysi?", "“Sen yetim emassan”", ["“O‘zbegim”", "“Bahor keldi seni so‘roqlab”", "“Kecha va kunduz”"],
      x="She’r urush yillarida yetim bolalarni bag‘riga olgan xalq haqida."),
    Q("“Sen yetim emassan” she’rining asosiy g‘oyasi qaysi?", "Mehr-oqibat va insonparvarlik", ["Boylik orttirish", "Sayohatga chaqiriq", "Tabiat tasviri"], d=2,
      x="She’r xalqning olijanobligi, mehr-oqibatini ulug‘laydi."),
    Q("Erkin Vohidovning “O‘zbegim” asari qanday she’r?", "Qasida", ["Masal", "Ertak", "Roman"], d=3, x="“O‘zbegim” — xalqimizni madh etuvchi qasida."),
    Q("Erkin Vohidovning mashhur dostoni qaysi?", "“Ruhlar isyoni”", ["“Alpomish”", "“Farhod va Shirin”", "“Oygul bilan Baxtiyor”"], d=3,
      x="“Ruhlar isyoni” — Erkin Vohidovning dostoni."),
    Q("Erkin Vohidovning komediyasi qaysi?", "“Oltin devor”", ["“Boy ila xizmatchi”", "“Kecha va kunduz”", "“Shum bola”"], d=3,
      x="“Oltin devor” — Erkin Vohidovning sahna asari (komediya)."),
    Q("Abdulla Oripov qaysi viloyatda tug‘ilgan?", "Qashqadaryoda", ["Xorazmda", "Namanganda", "Andijonda"], d=3, x="Abdulla Oripov Qashqadaryo viloyatida tug‘ilgan."),
    Q("Davlat madhiyasining musiqasi muallifi kim?", "Mutal Burhonov", ["Abdulla Oripov", "Erkin Vohidov", "Hamid Olimjon"], x="So‘zlari — Abdulla Oripov, musiqasi — Mutal Burhonov."),
    Q("Abdulla Oripov va Erkin Vohidov qanday oliy unvonga sazovor bo‘lgan?", "O‘zbekiston Qahramoni", ["Olimpiya chempioni", "Xalq rassomi", "Faxriy sportchi"], d=3,
      x="Ikkala shoir ham “O‘zbekiston Qahramoni” unvoniga sazovor bo‘lgan."),
    Q("She’rda shoirning his-tuyg‘ularini ifodalovchi obraz qanday ataladi?", "Lirik qahramon", ["Epik qahramon", "Salbiy qahramon", "Dramatik personaj"], d=2,
      x="Lirik qahramon — she’rdagi “men”, uning kechinmalari."),
    Q("Hamid Olimjon va Zulfiya qaysi asr adabiyoti vakillari?", "XX asr", ["XV asr", "XII asr", "XVIII asr"], x="Ular XX asr o‘zbek she’riyatining yirik vakillari."),
    TF("“Oygul bilan Baxtiyor” — Hamid Olimjon asari.", True, x="Bu — Hamid Olimjonning ertak-dostoni."),
    TF("“O‘zbegim” qasidasini Abdulla Qodiriy yozgan.", False, x="“O‘zbegim” — Erkin Vohidov qasidasi."),
    TF("Abdulla Oripov — O‘zbekiston Davlat madhiyasi so‘zlari muallifi.", True, x="Madhiya 1992-yilda qabul qilingan."),
    MATCH("Shoirni asari bilan juftlang", [("Hamid Olimjon", "“Oygul bilan Baxtiyor”"), ("Erkin Vohidov", "“Ruhlar isyoni”"), ("G‘afur G‘ulom", "“Sen yetim emassan”"),
                                          ("Zulfiya", "“Bahor keldi seni so‘roqlab”"), ("Abdulla Oripov", "Davlat madhiyasi so‘zlari")], d=2),
    ORDER("So‘zlardan gap tuzing", "Zulfiya sadoqat va sog‘inchni kuyladi", d=2, x="Zulfiya she’rlarida sadoqat, sog‘inch va ona yurt mehri kuylanadi."),
]
T.topic("poetry20", "🌹", L("XX asr o‘zbek she’riyati", "20th-century Uzbek poetry", "Узбекская поэзия XX века"), C3,
        "XX asr o‘zbek she’riyati:\n"
        "• Hamid Olimjon (Jizzax) — “Oygul bilan Baxtiyor” ertak-dostoni; rafiqasi Zulfiya — shoira (“Bahor keldi seni so‘roqlab”).\n"
        "• G‘afur G‘ulom — “Sen yetim emassan” she’ri (mehr-oqibat, insonparvarlik).\n"
        "• Abdulla Oripov (Qashqadaryo) — Davlat madhiyasi so‘zlari muallifi (musiqasi Mutal Burhonov).\n"
        "• Erkin Vohidov — “O‘zbegim” qasidasi, “Ruhlar isyoni” dostoni, “Oltin devor” komediyasi.\n"
        "She’rdagi shoir kechinmalarini ifodalovchi obraz — lirik qahramon.", items=items)

G1 = ("Qishloq chekkasidagi eski tegirmonni hamma unutgan edi. Bir kuni o‘n ikki yoshli Sanjar bobosidan tegirmon tarixini "
      "eshitib qoldi. U sinfdoshlarini yig‘ib, tegirmonni tozalashga kirishdi. Kattalar bolalar ustidan kulishdi: “Bu "
      "xarobadan hech narsa chiqmaydi”. Lekin bolalar taslim bo‘lishmadi. Bahorga kelib, tegirmon g‘ildiragi yana aylana "
      "boshladi, qishloqqa esa uzoq-uzoqlardan sayyohlar kela boshladi.")
G2 = ("Buvim har tong derazani ochib, ayvondagi gullarni sug‘orardi. Uning qo‘llari ajin bosgan, lekin juda epchil edi. "
      "Ko‘zlaridan esa hamisha mehr yog‘ilib turardi. Men kichikligimda buvimning eski ro‘molchasini juda yaxshi ko‘rardim: "
      "unga ipak ip bilan mayda lolalar tikilgan edi. Hozir ham o‘sha ro‘molchani ko‘rsam, buvimning iliq kaftlarini eslayman.")
G3 = ("Kuz oqshomi edi. Osmon qo‘rg‘oshinday og‘ir tortib, bog‘ ustiga cho‘kdi. Shamol yerga to‘kilgan sarg‘ish barglarni "
      "to‘p-to‘p qilib quvlab yurar, qayoqqadir olib ketardi. Bog‘ning yolg‘iz qorovuli — keksa tut shoxlarini yozib, "
      "kimnidir kutayotgan edi.")
items = [
    Q("Hikoyada voqealarni boshlab bergan hodisa (tugun) qaysi?", "Sanjar tegirmon tarixini eshitdi", ["Sayyohlar keldi", "G‘ildirak aylandi", "Kattalar kulishdi"],
      text=G1, d=2, x="Shu voqeadan keyin Sanjar tegirmonni tiklashga kirishdi."),
    Q("Hikoyadagi to‘qnashuv (konflikt) nimada?", "Bolalar intilishi va kattalar ishonchsizligi", ["Ikki qishloq o‘rtasidagi bahs", "Sanjarning bobosi bilan janjali",
                                                                                                  "Tabiat va odam kurashi"], text=G1, d=3,
      x="Kattalar “hech narsa chiqmaydi” deb kulishdi, bolalar esa taslim bo‘lmadi."),
    Q("Voqealar yechimi qaysi?", "Tegirmon g‘ildiragi yana aylandi", ["Kattalar kulishdi", "Sanjar bobosidan so‘radi", "Bolalar tozalashga kirishdi"], text=G1, d=2,
      x="Yechim — voqealarning yakuniy natijasi."),
    Q("Sanjar qanday xarakterga ega?", "Tashabbuskor va qat’iyatli", ["Dangasa va loqayd", "Qo‘rqoq va ikkilanuvchan", "Maqtanchoq va xudbin"], text=G1,
      x="U ishni boshlab, oxiriga yetkazdi."),
    Q("Hikoyaning g‘oyasi qaysi?", "Qat’iyat va birdamlik natija beradi", ["Eski narsalar keraksiz", "Kattalar doim haq", "Sayyohlar tegirmonni yaxshi ko‘radi"],
      text=G1, x="Bolalar birgalikda harakat qilib, maqsadga erishdi."),
    Q("Hikoya kimning tilidan aytilgan?", "Nevaraning o‘z tilidan (“men”)", ["Buvining tilidan", "Muallifning chetdan kuzatuvidan", "Ro‘molchaning tilidan"],
      text=G2, d=2, x="Hikoyachi birinchi shaxsda so‘zlaydi: “Men kichikligimda…”."),
    Q("“Qo‘llari ajin bosgan, lekin juda epchil edi” — qanday tasvir?", "Portret", ["Peyzaj", "Dialog", "Monolog"], text=G2, x="Qahramonning tashqi qiyofasi tasvirlangan."),
    Q("Matndagi eski ro‘molcha qanday vazifani bajaradi?", "Xotirani uyg‘otuvchi badiiy detal", ["Voqeaning tuguni", "Qahramonning ismi", "Asarning sarlavhasi"],
      text=G2, d=3, x="Kichik buyum hikoyachida buvisiga bo‘lgan mehrni uyg‘otadi — bu badiiy detal."),
    Q("Matnning mavzusi nima?", "Buviga mehr va xotira", ["Gul yetishtirish", "Tikuvchilik hunari", "Kuzgi bog‘"], text=G2, x="Hikoyachi buvisini mehr bilan eslaydi."),
    Q("Matnda qanday tasvir ustun?", "Peyzaj (tabiat tasviri)", ["Portret", "Dialog", "Monolog"], text=G3, x="Kuz oqshomidagi bog‘ manzarasi tasvirlangan."),
    Q("“Osmon qo‘rg‘oshinday og‘ir tortib” — qaysi badiiy vosita?", "O‘xshatish", ["Jonlantirish", "Mubolag‘a", "Takror"], text=G3, d=2,
      x="Osmon qo‘rg‘oshinga o‘xshatilgan (-day qo‘shimchasi)."),
    Q("“Keksa tut shoxlarini yozib, kimnidir kutayotgan edi” — qaysi vosita?", "Jonlantirish", ["O‘xshatish", "Mubolag‘a", "Tazod"], text=G3, d=2,
      x="Daraxtga insonga xos harakat — kutish berilgan."),
    Q("Matnning kayfiyati qanday?", "Mahzun, sokin", ["Quvnoq, shodon", "Hazil-mutoyiba", "Qahramonona"], text=G3, d=2,
      x="Og‘ir osmon, to‘kilgan barglar, yolg‘iz daraxt — mahzun kayfiyat beradi."),
    TF("Kattalar boshidanoq bolalarni qo‘llab-quvvatlashdi.", False, text=G1, x="Kattalar avval bolalar ustidan kulishdi."),
    TF("Buvining ro‘molchasiga lolalar tikilgan edi.", True, text=G2, x="“Unga ipak ip bilan mayda lolalar tikilgan edi.”"),
    Q("Asardagi qarama-qarshi kuchlar yoki fikrlar to‘qnashuvi nima deyiladi?", "Konflikt", ["Peyzaj", "Qofiya", "Portret"], x="Konflikt syujetni harakatga keltiradi."),
    Q("Asar voqealarining eng keskin, hal qiluvchi nuqtasi nima deyiladi?", "Kulminatsiya", ["Tugun", "Yechim", "Ekspozitsiya"], d=2,
      x="Kulminatsiyada ziddiyat eng yuqori darajaga chiqadi."),
    Q("Voqealardan oldingi vaziyat va qahramonlar bilan tanishtirish nima deyiladi?", "Ekspozitsiya", ["Kulminatsiya", "Yechim", "Tugun"], d=3,
      x="Ekspozitsiya — syujetning tanishtiruv qismi."),
    ORDER("Syujet unsurlarini tartib bilan joylang", "Ekspozitsiya → Tugun → Voqealar rivoji → Kulminatsiya → Yechim", sep=" → ", d=2,
          x="Syujet shu tartibda rivojlanadi."),
    MATCH("Atamani ta’rifi bilan juftlang", [("tugun", "voqealarni boshlab bergan hodisa"), ("kulminatsiya", "eng keskin nuqta"), ("yechim", "voqealar natijasi"),
                                            ("konflikt", "qarama-qarshi kuchlar to‘qnashuvi"), ("badiiy detal", "ma’noli kichik tafsilot"),
                                            ("hikoyachi", "voqeani so‘zlab beruvchi")], d=2),
]
T.topic("text_analysis", "🔍", L("Syujet va kompozitsiya", "Plot and composition", "Сюжет и композиция"), C3,
        "Badiiy asar tahlilida syujet unsurlarini aniqlang:\n"
        "• ekspozitsiya (tanishtiruv) → tugun (voqeani boshlab bergan hodisa) → voqealar rivoji → kulminatsiya (eng keskin nuqta) → yechim.\n"
        "• Konflikt — qarama-qarshi kuchlar yoki fikrlar to‘qnashuvi.\n"
        "• Badiiy detal — katta ma’no yuklangan kichik tafsilot (masalan, eski ro‘molcha).\n"
        "• Hikoyachi voqeani birinchi shaxsda (“men”) yoki uchinchi shaxsda so‘zlashi mumkin.", items=items)

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["prose20", "poetry20", "text_analysis"], C3)

# ============================================================ 4-chorak
SYLLABLES = [
    ("Bahor keldi, gul ochildi", 8, "Ba-hor-kel-di-gul-o-chil-di"),
    ("Tog‘lar oshib kelar shamol", 8, "Tog‘-lar-o-shib-ke-lar-sha-mol"),
    ("Ona yurtim, ko‘hna diyor", 8, "O-na-yur-tim-ko‘h-na-di-yor"),
    ("Oydin kecha, jim-jit bog‘", 7, "Oy-din-ke-cha-jim-jit-bog‘"),
    ("Ko‘klam kelib, dalalarga nur to‘ldi", 11, "Ko‘k-lam-ke-lib-da-la-lar-ga-nur-to‘l-di"),
]
items = []
for n, (line, count, split) in enumerate(SYLLABLES):
    items.append(Q(f"Misradagi bo‘g‘inlar sonini toping: “{line}”", str(count), [str(count - 1), str(count + 1), str(count + 2)], d=1 if n < 3 else 2,
                   x=f"{split} — {count} bo‘g‘in (har bir unli — bitta bo‘g‘in)."))
RADIF = "Ko‘nglim ochar bahor keldi,\nGul-u lola qator keldi."
CROSS = "Osmonda oy kuldi,\nYulduzlar charaqladi.\nBog‘ga sokin tun to‘ldi,\nShamol barglarni varaqladi."
PAIRED = "Ertalab tong otdi,\nKo‘cha nurga botdi.\nBolalar yugurdi,\nMaktab sari yurdi."
items += [
    Q("Barmoq vazni nimaga asoslanadi?", "Misralardagi bo‘g‘inlar soni tengligiga", ["Cho‘ziq-qisqa bo‘g‘inlarga", "Qofiya yo‘qligiga", "So‘zlarning ma’nosiga"],
      x="Barmoqda misralar bo‘g‘in soni bo‘yicha teng bo‘ladi (masalan, 8 tadan)."),
    Q("Misra ichidagi ohang bo‘laklari nima deyiladi?", "Turoq", ["Radif", "Band", "Bayt"], d=3, x="Masalan: “Bahor keldi, | gul ochildi” — 4+4 turoq."),
    Q("Vazn va qofiya talablaridan erkin she’r nima deyiladi?", "Sarbast", ["Barmoq", "Aruz", "Ruboiy"], d=2, x="Sarbast — erkin she’r."),
    Q("O‘zbek xalq qo‘shiqlari va dostonlari asosan qaysi vaznda?", "Barmoq", ["Aruz", "Sarbast", "Gekzametr"], d=2, x="Barmoq — xalq og‘zaki ijodining milliy vazni."),
    Q("Qaysi juftlik qofiyadosh?", "yulduz — kunduz", ["yulduz — osmon", "kunduz — tun", "oy — quyosh"], x="Oxiri ohangdosh: “-duz”."),
    Q("Qaysi juftlik qofiyadosh?", "qalam — olam", ["qalam — daftar", "olam — dunyo", "kitob — varaq"], x="Oxiri ohangdosh: “-lam”."),
    Q("Misralardagi radifni toping.", "keldi", ["bahor", "qator", "ko‘nglim"], text=RADIF, d=2, x="“keldi” qofiyadan keyin aynan takrorlanmoqda — bu radif."),
    Q("Shu misralardagi qofiyadosh so‘zlar qaysi?", "bahor — qator", ["ko‘nglim — gul", "keldi — keldi", "ochar — lola"], text=RADIF, d=3,
      x="Qofiya radifdan oldin keladi: bahor — qator."),
    Q("Bu bandda qofiyalanish tartibi qanday?", "a-b-a-b", ["a-a-b-b", "a-b-b-a", "a-a-a-a"], text=CROSS, d=3,
      x="kuldi — to‘ldi (1- va 3-misra), charaqladi — varaqladi (2- va 4-misra)."),
    Q("Bu bandda qofiyalanish tartibi qanday?", "a-a-b-b", ["a-b-a-b", "a-b-b-a", "a-a-a-a"], text=PAIRED, d=3,
      x="otdi — botdi (1–2), yugurdi — yurdi (3–4) — juft qofiya."),
    TF("Sarbastda qofiya bo‘lishi shart emas.", True, x="Sarbast vazn va qofiya talablaridan erkin."),
    TF("Barmoq vaznida misralardagi bo‘g‘inlar soni odatda teng bo‘ladi.", True, x="Barmoqning asosi — bo‘g‘inlar soni."),
    TF("Radif qofiyadan oldin keladi.", False, x="Radif qofiyadan keyin takrorlanadi."),
    MATCH("Vazn yoki atamani ta’rifi bilan juftlang", [("barmoq", "bo‘g‘inlar soniga asoslangan vazn"), ("aruz", "cho‘ziq-qisqa bo‘g‘inlar vazni"),
                                                      ("sarbast", "erkin she’r"), ("turoq", "misra ichidagi ohang bo‘lagi"),
                                                      ("radif", "qofiyadan keyingi takror so‘z"), ("band", "misralar guruhi")], d=2),
]
T.topic("verse", "🎼", L("She’r tuzilishi va vazni", "Verse structure and metre", "Строение и размер стиха"), C4,
        "She’r vazni — misralardagi ohang o‘lchovi:\n"
        "• Barmoq — bo‘g‘inlar soni tengligiga asoslanadi (xalq og‘zaki ijodi, ko‘p zamonaviy she’rlar); misra turoqlarga bo‘linadi:\n"
        "  “Ba-hor kel-di, | gul o-chil-di” (4+4). Bo‘g‘inni sanash uchun unlilarni sanang.\n"
        "• Aruz — cho‘ziq va qisqa bo‘g‘inlar navbati (mumtoz she’riyat). Sarbast — vazn va qofiyadan erkin she’r.\n"
        "• Qofiyalanish tartibi: a-a-b-b, a-b-a-b, a-b-b-a. Radif — qofiyadan keyin aynan takrorlanadigan so‘z.", items=items)

ARTS = ["Tashbeh (o‘xshatish)", "Tashxis (jonlantirish)", "Mubolag‘a", "Sifatlash (epitet)", "Tazod", "Takrir"]
EXAMPLES = [
    ("Uning qalbi tog‘day mustahkam.", "Tashbeh (o‘xshatish)", 1, "Qalb tog‘ga qiyoslangan (-day)."),
    ("Tong shabadasi gullarni erkalab uyg‘otdi.", "Tashxis (jonlantirish)", 1, "Shabadaga insonga xos harakat berilgan."),
    ("Oy bulut ortiga uyalib yashirindi.", "Tashxis (jonlantirish)", 1, "Oy odamdek uyaladi."),
    ("Uning ovozidan tog‘lar larzaga keldi.", "Mubolag‘a", 1, "Ovoz kuchi ataylab oshirib tasvirlangan."),
    ("Bir qadamda yetti daryodan o‘tdi.", "Mubolag‘a", 2, "Haqiqatda bo‘lmaydigan darajada oshirilgan."),
    ("zumrad maysa, baxmal tun", "Sifatlash (epitet)", 1, "Obrazli, bo‘yoqdor sifatlar."),
    ("Yaxshidan bog‘ qoladi, yomondan — dog‘.", "Tazod", 2, "Zid tushunchalar qarshilantirilgan: yaxshi — yomon."),
    ("“Kecha va kunduz” (roman nomi)", "Tazod", 2, "Kecha va kunduz — zid tushunchalar."),
    ("Vatan, Vatan, jonim Vatan!", "Takrir", 2, "So‘z ta’kid uchun takrorlangan."),
]
items = []
for example, art, d, why in EXAMPLES:
    items.append(Q(f"“{example}” — qaysi badiiy san’at?" if not example.startswith("“") else f"{example} — qaysi badiiy san’at?", art,
                   rnd.sample([a for a in ARTS if a != art], 3), d=d, x=why))
items += [
    Q("“Tashbeh” so‘zining ma’nosi qaysi?", "O‘xshatish", ["Jonlantirish", "Zidlash", "Kuchaytirish"], x="Tashbeh — o‘xshatish san’ati."),
    Q("“Tashxis” so‘zining ma’nosi qaysi?", "Jonlantirish", ["O‘xshatish", "Zidlash", "Takrorlash"], d=2, x="Tashxis — jonsiz narsaga jonli xususiyat berish."),
    Q("Zid ma’noli so‘zlarni yonma-yon keltirib, fikrni kuchaytirish nima deyiladi?", "Tazod", ["Tashbeh", "Tashxis", "Takrir"], x="Masalan: yaxshi — yomon, kecha — kunduz."),
    Q("O‘xshatish vositasisiz, bir narsani boshqa narsa nomi bilan atash nima deyiladi?", "Istiora", ["Tazod", "Takrir", "Sifatlash"], d=3,
      x="Istiora — yashirin o‘xshatish (metafora)."),
    Q("Mashhur voqea yoki qahramonlarga ishora qilish nima deyiladi?", "Talmeh", ["Tazod", "Mubolag‘a", "Takrir"], d=3,
      x="Masalan, Farhod yoki Majnun nomini eslatib, mehnat yoki ishqqa ishora qilish."),
    Q("Hayvon yoki jonsiz narsalarni odamdek gapirtirish nima deyiladi?", "Intoq", ["Tazod", "Talmeh", "Takrir"], d=3, x="Intoq — “gapirtirish” degani."),
    Q("O‘xshatishda qaysi so‘zlar vosita bo‘lib keladi?", "kabi, singari, misoli, go‘yo", ["va, ham, bilan", "lekin, ammo, biroq", "uchun, sari, qadar"], d=2,
      x="Ular narsalarni qiyoslash uchun xizmat qiladi."),
    Q("O‘xshatish (tashbeh) nechta asosiy unsurdan iborat?", "4 ta", ["2 ta", "6 ta", "8 ta"], d=3,
      x="O‘xshatiluvchi, o‘xshatiladigan narsa, o‘xshatish asosi va o‘xshatish vositasi."),
    TF("Tazod — o‘xshatish vositasi yordamida narsalarni qiyoslash.", False, x="Bu — tashbeh; tazod — zid tushunchalarni qarshilantirish."),
    TF("Mubolag‘ada belgi ataylab oshirib tasvirlanadi.", True, x="Masalan: “Ovozidan tog‘lar larzaga keldi”."),
    MATCH("San’atni misoli bilan juftlang", [("tashbeh", "tog‘day mustahkam"), ("tashxis", "oy uyalib yashirindi"), ("mubolag‘a", "ovozidan tog‘lar larzaga keldi"),
                                            ("tazod", "kecha va kunduz"), ("takrir", "Vatan, Vatan, jonim Vatan"), ("sifatlash", "zumrad maysa")], d=2),
]
T.topic("devices", "🎨", L("Badiiy san’atlar", "Literary devices", "Художественные приёмы"), C4,
        "Badiiy san’atlar nutqni obrazli va ta’sirli qiladi:\n"
        "• Tashbeh (o‘xshatish) — tog‘day mustahkam; vositalari: -day, -dek, kabi, singari, misoli, go‘yo. Istiora — vositasiz, yashirin o‘xshatish.\n"
        "• Tashxis (jonlantirish) — oy uyalib yashirindi; intoq — hayvon yoki narsani gapirtirish.\n"
        "• Mubolag‘a — oshirib tasvirlash; sifatlash (epitet) — zumrad maysa, baxmal tun.\n"
        "• Tazod — zid tushunchalarni qarshilantirish (“Kecha va kunduz”); takrir — so‘z takrori; talmeh — mashhur voqea yoki qahramonga ishora.", items=items)

items = [
    Q("“O‘tkan kunlar” qaysi janrdagi asar?", "Roman", ["Hikoya", "Qissa", "Doston"], x="“O‘tkan kunlar” — birinchi o‘zbek romani."),
    Q("Abdulla Qahhorning “Anor” asari qaysi janrda?", "Hikoya", ["Roman", "Doston", "Komediya"], x="“Anor” — kichik hajmli nasriy asar, hikoya."),
    Q("Oybekning “Bolalik” asari qaysi janrda?", "Qissa", ["Roman", "G‘azal", "Komediya"], d=2, x="“Bolalik” — xotira qissasi."),
    Q("Hamzaning “Maysaraning ishi” asari qaysi janrda?", "Komediya", ["Tragediya", "Roman", "Ruboiy"], d=2, x="“Maysaraning ishi” — kulgili sahna asari."),
    Q("Hamzaning “Boy ila xizmatchi” asari qaysi adabiy turga mansub?", "Drama (dramatik tur)", ["Lirika", "Epos", "Xalq og‘zaki ijodi"], d=2,
      x="U sahnada ijro etish uchun yozilgan."),
    Q("Dramatik asarda muallifning qavs ichidagi izohi nima deyiladi?", "Remarka", ["Monolog", "Radif", "Qofiya"], d=3,
      x="Remarkada qahramonning holati, harakati yoki sahna tasvirlanadi."),
    Q("Dramatik asarning katta qismlari nima deyiladi?", "Parda", ["Band", "Bayt", "Misra"], d=2, x="Pardalar ko‘rinishlarga bo‘linadi."),
    Q("Dramatik asar qaysi nutq shakllari asosida quriladi?", "Dialog va monolog", ["Faqat qofiya", "Faqat muallif hikoyasi", "Faqat tasvir"],
      x="Dramada voqea qahramonlar nutqi orqali ochiladi."),
    Q("Qahramonning og‘ir qismati tasvirlangan dramatik janr qaysi?", "Tragediya", ["Komediya", "Masal", "Ruboiy"], d=2, x="Tragediya — fojiali yakunli asar."),
    Q("Hayotiy kamchiliklarni kulgi orqali fosh etuvchi dramatik janr qaysi?", "Komediya", ["Tragediya", "Doston", "G‘azal"], x="Komediya kulgi orqali tarbiyalaydi."),
    Q("Ham epik, ham lirik xususiyatga ega janr qaysi?", "Doston", ["G‘azal", "Komediya", "Ruboiy"], d=3,
      x="Dostonda voqea hikoya qilinadi va his-tuyg‘u kuylanadi — liro-epik janr."),
    Q("Qissa hajmi jihatidan qayerda turadi?", "Hikoyadan katta, romandan kichik", ["Romandan katta", "Hikoyadan kichik", "Ruboiydan kichik"],
      x="Hikoya < qissa < roman."),
    Q("Romanning hikoyadan asosiy farqi nimada?", "Ko‘p qahramon va keng voqealar", ["Qofiyali bo‘lishi", "Sahnada o‘ynalishi", "To‘rt misradan iboratligi"], d=2,
      x="Roman — keng qamrovli, ko‘p qahramonli katta epik asar."),
    Q("Lirik asarning asosiy xususiyati qaysi?", "His-tuyg‘u va kechinma ifodasi", ["Ko‘p voqealar tizimi", "Sahnaviy harakat", "Ilmiy dalillar"],
      x="Lirikada shoirning ichki olami ochiladi."),
    Q("Masal qaysi adabiy turga mansub?", "Epos (epik tur)", ["Lirika", "Drama", "Hech qaysi"], d=2, x="Masalda voqea hikoya qilinadi — u kichik epik janr."),
    Q("Adabiyotda nechta asosiy adabiy tur bor?", "3 ta", ["2 ta", "5 ta", "7 ta"], x="Epos, lirika, drama."),
    TF("Doston — liro-epik janr: unda voqea ham, his-tuyg‘u ham bor.", True, d=2, x="Shuning uchun doston epik va lirik turlar oralig‘ida turadi."),
    TF("Remarka — lirik she’rning oxirgi bayti.", False, x="Remarka — dramatik asardagi muallif izohi."),
    TF("“Boy ila xizmatchi” — dramatik asar.", True, x="U sahnada ijro etish uchun yozilgan."),
    MATCH("Asarni janri bilan juftlang", [("“O‘tkan kunlar”", "roman"), ("“Anor”", "hikoya"), ("“Bolalik”", "qissa"), ("“Maysaraning ishi”", "komediya"),
                                         ("“O‘zbegim”", "qasida"), ("“Alpomish”", "doston")], d=2),
    ORDER("So‘zlardan gap tuzing", "Adabiyot epos lirika va drama turlariga bo‘linadi", d=2, x="Adabiyotning uch turi: epos, lirika, drama."),
]
T.topic("kinds", "🎭", L("Adabiy turlar va janrlar", "Literary kinds and genres", "Роды и жанры литературы"), C4,
        "Adabiyot uch turga bo‘linadi: epos (voqea hikoya qilinadi), lirika (his-tuyg‘u ifodalanadi), drama (sahnada ijro uchun).\n"
        "• Epik janrlar: hikoya < qissa < roman, masal; doston — liro-epik janr (voqea ham, tuyg‘u ham bor).\n"
        "• Lirik janrlar: she’r, g‘azal, ruboiy, qasida.\n"
        "• Dramatik janrlar: tragediya, komediya, drama. Dramatik asar pardalarga bo‘linadi, dialog va monologdan tuziladi;\n"
        "  muallif izohi — remarka.\n"
        "• Misollar: “O‘tkan kunlar” — roman, “Bolalik” — qissa, “Anor” — hikoya, “Maysaraning ishi” — komediya.", items=items)

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["verse", "devices", "kinds"], C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["alpomish", "gorogly", "folk_genres", "navoi", "bobur", "classic_forms", "prose20", "poetry20", "text_analysis", "verse", "devices", "kinds"],
       C4, level=3)

T.write()
