"""Tabiiy fan, 2-sinf: assets/data/school/science_g2.json + bank_science_g2.json.

Mavzular O‘zbekiston maktab dasturi ("Tabiiy fan", 2-sinf) yo‘nalishida: tabiat hodisalari, suvning holatlari,
havo, tuproq, o‘simlik o‘sishi uchun sharoitlar, daraxt, buta va o‘t, madaniy va yovvoyi o‘simliklar,
hayvonlarning oziqlanishi, hayvonlarning qishga tayyorlanishi, O‘zbekiston tabiati, olam tomonlari va kompas,
vaqt (sutka, hafta, oy, yil), salomatlik, tabiatni muhofaza qilish.

2-sinf o‘quvchisi (8 yosh): savollar qisqa, ovozda o‘qib beriladi; ba’zi javoblar — rasm (emoji, faqat Android 9
da bor eskilari, pastda avtomatik tekshiriladi). Hamma qoida matnlari va savollar o‘zimizniki (darslikdan
ko‘chirilmagan), 1- va 3-sinf savollari takrorlanmaydi.
Qayta yaratish: python3 tool/content/school/science_g2.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("science", 2, L("Tabiiy fan", "Science", "Естествознание"))

C1 = "1-chorak. Tabiat hodisalari, suv va havo"
C2 = "2-chorak. O‘simliklar dunyosi"
C3 = "3-chorak. Hayvonlar va Vatanimiz tabiati"
C4 = "4-chorak. Yo‘nalish, vaqt va salomatlik"

S = "So‘zlardan gap tuzing"

# ============================================================ 1-chorak
T.topic("phenomena", "🌈", L("Tabiat hodisalari", "Weather phenomena", "Явления природы"),
        chapter=C1,
        theory="Tabiatda bo‘ladigan o‘zgarishlar — tabiat hodisalari.\n"
               "• Yomg‘ir — bulutdan tushadigan suv tomchilari. Qor — sovuqda bulutdan tushadigan oppoq uchqunlar.\n"
               "• Do‘l — muz donachalari. U ko‘pincha bahor va yozda, momaqaldiroq bilan yog‘adi.\n"
               "• Kamalak yomg‘irdan keyin Quyosh chiqqanda ko‘rinadi, unda 7 ta rang bor.\n"
               "• Shamol — harakatlanayotgan havo. Yengil shamol — shabada, juda kuchli shamol — bo‘ron.\n"
               "Momaqaldiroqda avval chaqmoq ko‘rinadi, keyin gumburlagan ovoz eshitiladi.",
        items=[
            Q("Yomg‘ir nima?", "Bulutdan tushgan suv tomchilari",
              ["Daraxtdan tushgan barglar", "Osmondan tushgan qum", "Tog‘dan tushgan toshlar"], e="🌧️",
              x="Bulutdagi mayda tomchilar qo‘shilib, og‘irlashadi va yomg‘ir bo‘lib tushadi."),
            Q("Qor qachon yog‘adi?", "Havo sovuq bo‘lganda", ["Havo issiq bo‘lganda", "Quyosh qizdirganda",
                                                            "Kamalak chiqqanda"], e="❄️",
              x="Sovuqda bulutdagi suv muzlab, qor uchqunlariga aylanadi."),
            Q("Do‘l nima?", "Muz donachalari", ["Qum donachalari", "Gul urug‘lari", "Tosh parchalari"],
              x="Do‘l — bulutdan tushadigan muz donachalari."),
            Q("Kamalak qachon ko‘rinadi?", "Yomg‘irdan keyin Quyosh chiqqanda",
              ["Qorong‘i tunda", "Qattiq ayozda", "Quyosh botib bo‘lgach"], e="🌈",
              x="Quyosh nuri yomg‘ir tomchilaridan o‘tib, rangli yoy hosil qiladi."),
            Q("Kamalakda nechta rang bor?", "7 ta", ["3 ta", "5 ta", "10 ta"], e="🌈",
              x="Kamalak ranglari: qizil, to‘q sariq, sariq, yashil, havorang, ko‘k, binafsha."),
            Q("Shamol nima?", "Harakatlanayotgan havo", ["Muzlagan suv", "Qizigan tuproq", "Botayotgan Quyosh"],
              e="🌬️", x="Havo bir joydan ikkinchi joyga harakatlansa, shamol esadi."),
            Q("Yengil, yoqimli shamol nima deyiladi?", "Shabada", ["Bo‘ron", "Do‘l", "Tuman"],
              x="Yengil shamol — shabada."),
            Q("Qaysi biri tabiat hodisasi?", "Momaqaldiroq", ["Avtobus", "Bayram", "Dars"], e="⛈️",
              x="Momaqaldiroqni inson yaratmagan, u tabiatda o‘zi bo‘ladi."),
            Q("Qaysi biri tabiat hodisasi emas?", "Konsert", ["Yomg‘ir", "Qor", "Shamol"],
              x="Konsertni odamlar tashkil qiladi, qolganlari tabiat hodisalari."),
            TF("Do‘l ekinlarga zarar yetkazishi mumkin.", True, x="Muz donachalari barg va mevalarni urib shikastlaydi."),
            TF("Kamalak tunda ko‘rinadi.", False, x="Kamalak uchun Quyosh nuri kerak, u kunduzi ko‘rinadi."),
            TF("Qor — muzlagan suv.", True, e="❄️", x="Qor uchqunlari bulutdagi suvdan sovuqda hosil bo‘ladi."),
            TF("Kuchli shamol daraxtlarni tebratadi.", True, x="Shamol qancha kuchli bo‘lsa, shoxlar shuncha tebranadi."),
            Q("Kamalakning birinchi rangi qaysi?", "Qizil", ["Yashil", "Ko‘k", "Binafsha"], d=2,
              x="Kamalak qizil rangdan boshlanadi."),
            Q("Kamalakning oxirgi rangi qaysi?", "Binafsha", ["Qizil", "Sariq", "Yashil"], d=2,
              x="Kamalak binafsha rang bilan tugaydi."),
            Q("Yozgi tongda o‘tlar ustidagi suv tomchilari nima?", "Shudring", ["Do‘l", "Qirov", "Qor"], d=2,
              x="Tunda havo soviydi va o‘tlar ustida shudring tomchilari paydo bo‘ladi."),
            Q("Bo‘ron nimaga zarar yetkazishi mumkin?", "Daraxt shoxlariga", ["Quyosh nuriga", "Kamalakka", "Soyaga"], d=2,
              x="Juda kuchli shamol daraxt shoxlarini sindiradi, tomlarni uchiradi."),
            TF("Momaqaldiroqda baland daraxt tagida turish xavfsiz.", False, d=2,
               x="Chaqmoq ko‘pincha baland narsalarga uriladi, uyga kirish kerak."),
            MATCH("Hodisani ta’rifi bilan juftlang",
                  [("Yomg‘ir", "suv tomchilari"), ("Qor", "oppoq uchqunlar"), ("Do‘l", "muz donachalari"),
                   ("Kamalak", "yetti rangli yoy"), ("Shamol", "harakatlanayotgan havo"), ("Tuman", "yerga yaqin bulut")],
                  d=2, x="Har bir hodisaning o‘z belgisi bor."),
            ORDER(S, "Yomg‘irdan keyin kamalak chiqdi", d=2, x="Kamalak yomg‘irdan keyin Quyosh chiqqanda ko‘rinadi."),
            Q("Momaqaldiroqda avval nima bo‘ladi?", "Chaqmoq ko‘rinadi",
              ["Gumburlagan ovoz eshitiladi", "Kamalak chiqadi", "Qor yog‘adi"], d=3,
              x="Yorug‘lik tovushdan tezroq yetib keladi, shuning uchun chaqmoqni oldin ko‘ramiz."),
            Q("Sovuq tongda shoxlardagi oppoq muz qatlami nima?", "Qirov", ["Shudring", "Kamalak", "Bug‘"], d=3,
              x="Qattiq sovuq tongda havodagi namlik muzlab, qirov bo‘lib qo‘nadi."),
            Q("Do‘l ko‘pincha qaysi fasllarda yog‘adi?", "Bahor va yozda", ["Faqat qishda", "Faqat kuzda", "Hech qachon"],
              d=3, x="Do‘l iliq faslda momaqaldiroqli bulutlardan yog‘adi."),
            Q("Kamalakni ko‘rish uchun Quyosh qayerda bo‘lishi kerak?", "Orqamizda",
              ["Ro‘paramizda", "Ufqdan pastda", "Bulut ortida"], d=3,
              x="Kamalak Quyoshga teskari tomonda, yomg‘ir tomchilarida ko‘rinadi."),
            Q("Qor parchasining nechta nuri bor?", "6 ta", ["3 ta", "4 ta", "8 ta"], d=3, e="❄️",
              x="Qor parchalari har xil naqshli, lekin odatda 6 ta nurli bo‘ladi."),
        ])

T.topic("water", "💧", L("Suv va uning holatlari", "Water and its states", "Вода и её состояния"),
        chapter=C1,
        theory="Suv uch holatda bo‘ladi:\n"
               "• qattiq — muz va qor; • suyuq — oddiy suv; • gaz — bug‘.\n"
               "Sovuqda suv muzlaydi, muz isisa eriydi va yana suvga aylanadi.\n"
               "Suv qizdirilsa qaynaydi va bug‘ga aylanadi. Bug‘ sovuq narsaga tegsa, yana tomchiga aylanadi.\n"
               "Toza suv rangsiz, hidsiz, shaffof va oquvchan. Muz suvdan yengil, shuning uchun suv yuzida suzib yuradi.",
        items=[
            Q("Suv sovuqda nimaga aylanadi?", "Muzga", ["Bug‘ga", "Qumga", "Tuzga"], e="❄️",
              x="Qattiq sovuqda suv muzlab, muzga aylanadi."),
            Q("Muz isisa nima bo‘ladi?", "Eriydi", ["Qotadi", "Yonadi", "Toshga aylanadi"],
              x="Issiqda muz erib, suvga aylanadi."),
            Q("Suv qaynaganda nimaga aylanadi?", "Bug‘ga", ["Muzga", "Qorga", "Tuzga"],
              x="Qaynagan suv bug‘ga aylanib, havoga ko‘tariladi."),
            Q("Muz suvning qaysi holati?", "Qattiq", ["Suyuq", "Gaz"], x="Muz qattiq, uni qo‘lda ushlash mumkin."),
            Q("Jo‘mrakdan oqayotgan suv qaysi holatda?", "Suyuq", ["Qattiq", "Gaz"],
              x="Oddiy suv suyuq, u oqadi."),
            Q("Bug‘ suvning qaysi holati?", "Gaz", ["Qattiq", "Suyuq"], x="Bug‘ — suvning gaz holati."),
            Q("Qaysi biri qattiq holatdagi suv?", "Muz", ["Bug‘", "Yomg‘ir", "Choy"],
              x="Muz va qor — suvning qattiq holati."),
            Q("Toza suvning hidi qanday?", "Hidi yo‘q", ["Gul hidi", "Non hidi", "Olma hidi"],
              x="Toza suv hidsiz bo‘ladi."),
            Q("Toza suv qanday rangda?", "Rangsiz", ["Qizil", "Sariq", "Yashil"], x="Toza suv rangsiz va shaffof."),
            Q("Muzlatgichga suvli idish qo‘ysak, nima bo‘ladi?", "Suv muzlaydi",
              ["Suv qaynaydi", "Suv sutga aylanadi", "Suv qizib ketadi"],
              x="Muzlatgich ichi juda sovuq, suv u yerda muzlaydi."),
            TF("Muz bo‘lagi suvli stakanning tubiga cho‘kadi.", False, x="Muz suvdan yengil, u suv yuzida suzadi."),
            TF("Qor ham muzlagan suv.", True, e="❄️", x="Qor erisa, suvga aylanadi."),
            TF("Issiq kunda ko‘lmaklar quriydi.", True, e="☀️",
               x="Quyosh issig‘ida suv bug‘lanib, havoga ko‘tariladi."),
            TF("Suvsiz hech bir tirik jon yashay olmaydi.", True, x="Odam, hayvon va o‘simliklarga suv kerak."),
            ORDER(S, "Muz isisa suvga aylanadi", x="Issiqda muz eriydi va suvga aylanadi."),
            Q("Ho‘l kiyim quyoshda nega quriydi?", "Suv bug‘lanib ketadi",
              ["Suv muzlaydi", "Suv tuzga aylanadi", "Kiyim suvni yeb qo‘yadi"], d=2,
              x="Quyosh issig‘ida kiyimdagi suv bug‘ga aylanib, havoga uchib ketadi."),
            Q("Sovuq oynaga nafas olsak, nima paydo bo‘ladi?", "Mayda suv tomchilari",
              ["Muz bo‘laklari", "Qum", "Chang"], d=2,
              x="Nafasdagi bug‘ sovuq oynaga tegib, mayda tomchilarga aylanadi."),
            Q("Suvning uch holatini toping", "Muz, suv, bug‘", ["Tosh, qum, loy", "Muz, tosh, havo", "Suv, sut, choy"],
              d=2, x="Qattiq — muz, suyuq — suv, gaz — bug‘."),
            Q("Qaysi suv ichish uchun xavfsiz?", "Qaynatilgan suv", ["Ariq suvi", "Ko‘lmak suvi", "Qor suvi"], d=2,
              x="Qaynatilganda suvdagi mikroblar yo‘qoladi."),
            Q("Dengiz suvi qanday ta’mli?", "Sho‘r", ["Shirin", "Nordon", "Achchiq"], d=2,
              x="Dengiz suvida tuz ko‘p, shuning uchun u sho‘r."),
            TF("Stakandagi suvni kosaga quysak, u kosa shaklini oladi.", True, d=2,
               x="Suv oquvchan: stakanda stakan, shishada shisha shaklida turadi."),
            MATCH("Nima bo‘ladi? Juftlang",
                  [("Muz isisa", "eriydi"), ("Suv sovuqda", "muzlaydi"), ("Suv qaynasa", "bug‘ga aylanadi"),
                   ("Bug‘ sovuq oynaga tegsa", "tomchiga aylanadi"), ("Ho‘l kiyim quyoshda", "quriydi")], d=2,
                  x="Issiq va sovuqda suv bir holatdan boshqasiga o‘tadi."),
            MATCH("Holatni misol bilan juftlang", [("Qattiq", "muz"), ("Suyuq", "yomg‘ir suvi"), ("Gaz", "bug‘")], d=2,
                  x="Muz — qattiq, yomg‘ir suvi — suyuq, bug‘ — gaz."),
            Q("Osmondagi bulutlar nimadan yig‘iladi?", "Ko‘tarilgan suv bug‘idan", ["Tutundan", "Changdan", "Paxtadan"], d=3,
              x="Daryo, dengiz va ko‘llardan suv bug‘lanib, osmonda bulut hosil qiladi."),
            Q("Tabiatda suv qanday aylanadi?", "Bug‘lanadi, bulut bo‘ladi, yomg‘ir yog‘adi",
              ["Doim muz bo‘lib turadi", "Yerdan butunlay yo‘qoladi", "Faqat daryoda oqadi"], d=3,
              x="Suv bug‘lanadi, bulutga aylanadi, yomg‘ir yoki qor bo‘lib yerga qaytadi."),
        ])

T.topic("air", "🎈", L("Havo va uning ahamiyati", "Air and why it matters", "Воздух и его значение"),
        chapter=C1,
        theory="Havo bizni har tomondan o‘rab turadi.\n"
               "• Havo ko‘rinmaydi, rangi va hidi yo‘q, lekin uni sezamiz: shamol esganda yoki shar puflaganda.\n"
               "• Odamlar, hayvonlar va o‘simliklar havo bilan nafas oladi.\n"
               "• Havo bo‘lmasa, olov yonmaydi. Isigan havo yuqoriga ko‘tariladi.\n"
               "Daraxtlar havoni tozalaydi, zavod va mashina tutuni esa havoni ifloslaydi.",
        items=[
            Q("Havoning rangi bormi?", "Yo‘q, rangsiz", ["Ha, ko‘k", "Ha, oq", "Ha, sariq"],
              x="Havo rangsiz va shaffof, shuning uchun uni ko‘rmaymiz."),
            Q("Havo nima uchun kerak?", "Nafas olish uchun", ["Yozish uchun", "Rasm chizish uchun", "Kitob o‘qish uchun"],
              x="Hamma tirik jonzotlar havo bilan nafas oladi."),
            Q("Sharni puflasak, ichida nima bo‘ladi?", "Havo", ["Suv", "Qum", "Tosh"], e="🎈",
              x="Puflaganimizda sharga havo kiradi va u shishadi."),
            Q("Harakatlanayotgan havo nima deyiladi?", "Shamol", ["Bulut", "Tuman", "Bug‘"],
              x="Havo harakatlansa, shamol esadi."),
            Q("Qaysi biri havoni toza qiladi?", "Daraxtlar", ["Mashinalar", "Zavod tutuni", "Gulxan"], e="🌳",
              x="Daraxt va o‘simliklar havoni toza qiladi."),
            Q("Havoni nima ifloslaydi?", "Zavod tutuni", ["Daraxtlar", "Gullar", "Yomg‘ir"],
              x="Tutun va chang havoni ifloslaydi."),
            Q("Kim havo bilan nafas oladi?", "Hamma tiriklar", ["Faqat odamlar", "Faqat qushlar", "Faqat itlar"],
              x="Odamlar ham, hayvonlar ham, o‘simliklar ham nafas oladi."),
            Q("Havoni qachon sezamiz?", "Shamol esganda", ["Ko‘z yumganda", "Uxlaganda", "Kitob o‘qiganda"],
              x="Shamol esganda havo yuzimizga uriladi."),
            TF("Havo ko‘zga ko‘rinmaydi.", True, x="Havo rangsiz va shaffof."),
            TF("Havo bo‘lmasa ham olov yonaveradi.", False, x="Olov yonishi uchun havo kerak."),
            TF("Daraxtlar ham nafas oladi.", True, e="🌳", x="Daraxtlar tirik, ular ham havo bilan nafas oladi."),
            TF("Toza havoda sayr qilish foydali.", True, x="Toza havo tanaga kuch beradi."),
            ORDER(S, "Biz havo bilan nafas olamiz", x="Odam havosiz yashay olmaydi."),
            Q("Bo‘sh stakan aslida nima bilan to‘la?", "Havo bilan", ["Suv bilan", "Qum bilan", "Hech narsa bilan"], d=2,
              x="“Bo‘sh” idish ichida ham havo bor."),
            Q("Varrakni nima uchiradi?", "Shamol", ["Yomg‘ir", "Qor", "Tuman"], d=2,
              x="Shamol varrakni ko‘tarib, havoda ushlab turadi."),
            Q("Toza havo qayerda ko‘p?", "Bog‘ va o‘rmonda", ["Zavod yonida", "Gavjum yo‘l bo‘yida", "Tutunli xonada"],
              d=2, x="Daraxtlar ko‘p joyda havo toza."),
            Q("Xonani nega shamollatamiz?", "Toza havo kirishi uchun",
              ["Chang to‘planishi uchun", "Qorong‘i bo‘lishi uchun", "Shovqin ko‘payishi uchun"], d=2,
              x="Deraza ochilsa, xonaga toza havo kiradi."),
            Q("Velosiped g‘ildiragi ichida nima bor?", "Havo", ["Suv", "Qum", "Paxta"], d=2, e="🚲",
              x="G‘ildirakka nasos bilan havo damlanadi."),
            Q("Shahar havosini toza saqlash uchun nima qilamiz?", "Ko‘proq daraxt ekamiz",
              ["Axlatni yoqamiz", "Daraxtlarni kesamiz", "Ko‘proq tutun chiqaramiz"], d=2,
              x="Daraxtlar havoni tozalaydi."),
            TF("Mashina tutuni havoni ifloslaydi.", True, d=2, e="🚗", x="Tutunda zararli moddalar bor."),
            Q("Yonib turgan shamni stakan bilan yopsak, nima bo‘ladi?", "Sham o‘chadi",
              ["Sham kattalashadi", "Stakan eriydi", "Sham yorqinroq yonadi"], d=3,
              x="Stakan ichidagi havo tugagach, olov o‘chadi."),
            Q("Isigan havo qayoqqa ko‘tariladi?", "Yuqoriga", ["Pastga", "Yer ostiga", "Suv ichiga"], d=3,
              x="Issiq havo yengil, u yuqoriga ko‘tariladi."),
            Q("Bo‘sh shishani suvga botirsak, undan nima chiqadi?", "Havo pufakchalari", ["Qum", "Tosh", "Barg"], d=3,
              x="Shisha ichidagi havo pufakcha bo‘lib chiqadi, o‘rniga suv kiradi."),
            Q("Yelkanli qayiqni nima yurgizadi?", "Shamol", ["Benzin", "Ot", "Qor"], d=3,
              x="Shamol yelkanni puflab, qayiqni oldinga suradi."),
        ])

T.topic("soil", "🌾", L("Tuproq", "Soil", "Почва"),
        chapter=C1,
        theory="Tuproq — yerning o‘simliklar o‘sadigan ustki yumshoq qatlami.\n"
               "• Tuproqda qum, loy, suv, havo va chirindi bor.\n"
               "• Chirindi chirigan barg va o‘simliklardan hosil bo‘ladi. Chirindi ko‘p tuproq qoramtir va unumdor bo‘ladi.\n"
               "• Tuproqda chuvalchang va chumolilar yashaydi. Chuvalchang tuproqni yumshatadi.\n"
               "Tuproq juda ko‘p yillar davomida sekin hosil bo‘ladi, shuning uchun uni asraymiz.",
        items=[
            Q("Ko‘pchilik o‘simliklar qayerda o‘sadi?", "Tuproqda", ["Shishada", "Temirda", "Plastikda"],
              x="O‘simlik ildizi tuproqqa kirib, undan suv va oziq oladi."),
            Q("Tuproqda qaysi jonivor yashaydi?", "Chuvalchang", ["Baliq", "Laylak", "Sigir"],
              x="Chuvalchang tuproq ichida yo‘l ochib yashaydi."),
            Q("Chuvalchang tuproqqa qanday foyda keltiradi?", "Uni yumshatadi", ["Uni quritadi", "Uni qotiradi",
                                                                             "Uni ifloslaydi"],
              x="Chuvalchang ochgan yo‘llardan tuproqqa havo va suv kiradi."),
            Q("Qaysi tuproqda ekin yaxshi o‘sadi?", "Unumdor tuproqda", ["Sho‘r tuproqda", "Toshloq yerda", "Quruq qumda"],
              x="Unumdor tuproqda o‘simlik uchun oziq ko‘p."),
            Q("Tuproqqa suv quysak nima bo‘ladi?", "Suv tuproqqa singadi", ["Suv yonadi", "Tuproq muzlaydi", "Suv qotadi"],
              x="Tuproq suvni shimib oladi."),
            Q("Dehqon ekin ekishdan oldin yerni nima qiladi?", "Haydaydi va yumshatadi",
              ["Asfaltlaydi", "Muzlatadi", "Tosh bilan to‘ldiradi"],
              x="Yumshoq tuproqqa havo va suv yaxshi kiradi."),
            TF("Tuproqda qum va loy bor.", True, x="Tuproq qum, loy, suv, havo va chirindidan iborat."),
            TF("Tuproq bir kunda hosil bo‘ladi.", False, x="Tuproq juda ko‘p yillar davomida, sekin hosil bo‘ladi."),
            TF("Tuproqqa plastik ko‘mish zararli.", True, x="Plastik tuproqda chirimaydi va uni ifloslaydi."),
            TF("Chuvalchanglar tuproq uchun foydali.", True, x="Ular tuproqni yumshatadi."),
            ORDER(S, "Chuvalchang tuproqni yumshatadi", x="Chuvalchang tuproqda yo‘l ochib, uni yumshatadi."),
            Q("Unumdor tuproq qanday rangda?", "Qoramtir", ["Oppoq", "Ko‘k", "Pushti"], d=2,
              x="Chirindi ko‘p tuproq qoramtir bo‘ladi."),
            Q("Tuproqdagi chirindi qanday paydo bo‘ladi?", "Barg va o‘simliklar chirib",
              ["Toshlar maydalanib", "Plastik erib", "Temir zanglab"], d=2,
              x="Barg va o‘simlik qoldiqlari chirib, chirindiga aylanadi."),
            Q("Tuproq ichida havo bormi?", "Ha, bor", ["Yo‘q, umuman yo‘q", "Faqat qishda bor", "Faqat tunda bor"], d=2,
              x="Tuproq bo‘lagini suvga tashlasak, havo pufakchalari chiqadi."),
            Q("Gulga qanday tuproq kerak?", "Yumshoq, unumdor tuproq", ["Quruq qum", "Shag‘al", "Sement"], d=2,
              x="Yumshoq va unumdor tuproqda gul yaxshi o‘sadi."),
            Q("Tuproq unumdor bo‘lishi uchun dehqon nima soladi?", "O‘g‘it", ["Tuz", "Plastik", "Shisha"], d=2,
              x="O‘g‘it tuproqqa oziq moddalar qo‘shadi."),
            Q("O‘simlik tuproqdan nimani shimib oladi?", "Suv va oziq moddalarni", ["Quyosh nurini", "Shamolni", "Tutunni"],
              d=2, x="Ildiz tuproqdan suv va unda erigan oziq moddalarni oladi."),
            Q("Qaysi biri tuproq tarkibida yo‘q?", "Shisha", ["Qum", "Loy", "Chirindi"], d=2,
              x="Tuproqda qum, loy, chirindi, suv va havo bor."),
            Q("Qaysi biri tuproqda chirimaydi?", "Plastik paket", ["Quruq barg", "Olma po‘sti", "Qog‘oz"], d=3,
              x="Plastik juda uzoq yillar chirimaydi, tuproqni ifloslaydi."),
            Q("Tuproqni suvli stakanga solib aralashtirsak, nima birinchi cho‘kadi?", "Qum",
              ["Loy", "Chirindi", "Havo"], d=3,
              x="Qum og‘ir, u tez cho‘kadi; loy sekin cho‘kadi, chirindi esa suv yuzida qoladi."),
            Q("Tog‘ yonbag‘ridagi daraxt va o‘tlar nima uchun kerak?", "Tuproqni yuvilishdan asraydi",
              ["Tuproqni quritadi", "Toshni eritadi", "Qorni ko‘paytiradi"], d=3,
              x="Ildizlar tuproqni ushlab turadi, yomg‘ir uni yuvib keta olmaydi."),
            Q("To‘kilgan barglar tuproqqa nima beradi?", "Chirib, chirindi beradi",
              ["Tuproqni qotiradi", "Tuproqni sho‘r qiladi", "Hech narsa bermaydi"], d=3,
              x="Barglar chirib, tuproqni unumdor qiladi."),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["phenomena", "water", "air", "soil"], chapter=C1)

# ============================================================ 2-chorak
T.topic("plant_needs", "🌻", L("O‘simlik o‘sishi uchun nima kerak", "What plants need", "Что нужно растениям"),
        chapter=C2,
        theory="O‘simlik o‘sishi uchun:\n"
               "• yorug‘lik — barglar Quyosh nurida oziq tayyorlaydi;\n"
               "• suv — ildiz tuproqdan suv shimib oladi;\n"
               "• issiqlik — sovuqda o‘simlik o‘smaydi;\n"
               "• havo va unumdor tuproq ham kerak.\n"
               "Urug‘ unishi uchun namlik va issiqlik kerak. O‘simliklar yorug‘lik tomonga qarab o‘sadi.",
        items=[
            Q("O‘simlikka nima kerak?", "Yorug‘lik va suv", ["Shovqin va chang", "Faqat qorong‘ilik", "Tuz va shakar"],
              x="O‘simlik yorug‘lik, suv, issiqlik, havo va tuproqda o‘sadi."),
            Q("Gul tuvagini qayerga qo‘yamiz?", "Yorug‘ deraza yoniga", ["Qorong‘i shkafga", "Muzlatgichga",
                                                                         "Karavot tagiga"], e="🌷",
              x="Deraza yonida yorug‘lik ko‘p."),
            Q("O‘simlik qaysi qismi bilan Quyosh nurini tutadi?", "Barglari bilan",
              ["Ildizi bilan", "Urug‘i bilan", "Tikanlari bilan"],
              x="Yashil barglar Quyosh nurini tutib, oziq tayyorlaydi."),
            Q("O‘simlikni sug‘ormasak nima bo‘ladi?", "Qurib qoladi", ["Tezroq o‘sadi", "Ko‘proq gullaydi", "Kattalashadi"],
              x="Suvsiz o‘simlik so‘lib, qurib qoladi."),
            Q("Qishda dalada o‘simliklar nega o‘smaydi?", "Havo sovuq", ["Suv ko‘p", "Yorug‘ ko‘p", "Havo issiq"],
              x="Sovuqda o‘simliklar o‘smaydi."),
            Q("Qaysi joy o‘simlik uchun eng yomon?", "Qorong‘i va sovuq yerto‘la",
              ["Yorug‘ deraza tokchasi", "Iliq issiqxona", "Quyoshli bog‘"],
              x="Qorong‘ida va sovuqda o‘simlik o‘smaydi."),
            TF("O‘simlikka faqat suv kerak, yorug‘lik kerak emas.", False,
               x="O‘simlikka suv ham, yorug‘lik ham kerak."),
            TF("Issiqxonada qishda ham sabzavot o‘stiriladi.", True, x="Issiqxonada qishda ham iliq va yorug‘."),
            TF("Nihol katta bo‘lishi uchun unga g‘amxo‘rlik kerak.", True, e="🌱",
               x="Nihol sug‘oriladi, yorug‘ joyda saqlanadi."),
            ORDER(S, "Barglar quyosh nurini tutadi", x="Barglar Quyosh nurida oziq tayyorlaydi."),
            Q("Urug‘ qayerda tezroq unadi?", "Nam va iliq tuproqda",
              ["Quruq va sovuq qutida", "Muz ustida", "Suvsiz shkafda"], d=2,
              x="Urug‘ unishi uchun namlik, issiqlik va havo kerak."),
            Q("Urug‘dan avval nima unib chiqadi?", "Nihol", ["Meva", "Gul", "Katta daraxt"], d=2, e="🌱",
              x="Urug‘dan avval kichik nihol chiqadi, u asta o‘sadi."),
            Q("O‘simliklar qaysi tomonga qarab o‘sadi?", "Yorug‘lik tomonga", ["Qorong‘i tomonga", "Devor tomonga",
                                                                          "Pastga, yer ostiga"], d=2,
              x="Deraza tokchasidagi gullar derazaga qarab egiladi."),
            Q("Xona o‘simligini qachon sug‘oramiz?", "Tuprog‘i quriganda",
              ["Har soatda", "Hech qachon", "Yilda bir marta"], d=2,
              x="Tuproq qurisa, o‘simlikni sug‘oramiz."),
            Q("Qaysi nihol yaxshi o‘sadi?", "Yorug‘da turib, sug‘orilgani",
              ["Qorong‘ida turgani", "Sug‘orilmagani", "Muzlatgichda turgani"], d=2,
              x="Yorug‘lik va suv bor joyda nihol yaxshi o‘sadi."),
            Q("Bahorda dehqonlar urug‘ni qachon ekadi?", "Yer isiganda", ["Yer muzlaganda", "Qor yog‘ganda",
                                                                        "Qish o‘rtasida"], d=2,
              x="Iliq tuproqda urug‘ tez unadi."),
            Q("O‘simliklar ovqatni qayerda tayyorlaydi?", "Bargida", ["Ildizida", "Gulida", "Urug‘ida"], d=2,
              x="Barglar Quyosh nurida o‘simlik uchun oziq tayyorlaydi."),
            Q("O‘simlik nafas olishi uchun nima kerak?", "Havo", ["Tosh", "Qum", "Tutun"], d=2,
              x="O‘simliklar ham havo bilan nafas oladi."),
            TF("Kaktus kam suv bilan ham yashay oladi.", True, d=2, e="🌵", x="Kaktus suvni poyasida saqlaydi."),
            MATCH("Nima kerak, nega? Juftlang",
                  [("Yorug‘lik", "barglar oziq tayyorlaydi"), ("Suv", "ildiz shimib oladi"),
                   ("Issiqlik", "muzlab qolmaydi"), ("Tuproq", "oziq moddalar beradi")], d=2,
                  x="O‘simlikka yorug‘lik, suv, issiqlik va tuproq kerak."),
            Q("Barglari sarg‘aygan o‘simlikka nima yetishmayotgan bo‘lishi mumkin?", "Yorug‘lik",
              ["Shovqin", "Qorong‘ilik", "Chang"], d=3, x="Yorug‘lik yetmasa, barglar sarg‘ayadi."),
            Q("Juda ko‘p suv quyilsa, ildiz bilan nima bo‘ladi?", "Chiriydi", ["Tez o‘sadi", "Gullaydi", "Muzlaydi"], d=3,
              x="Suv ko‘p bo‘lsa, ildizga havo yetmaydi va u chiriydi."),
        ])

T.topic("plant_forms", "🌳", L("Daraxt, buta va o‘t", "Trees, shrubs and herbs", "Деревья, кустарники и травы"),
        chapter=C2,
        theory="O‘simliklar uch xil ko‘rinishda bo‘ladi:\n"
               "• daraxt — bitta yo‘g‘on, baland yog‘och tanasi bor: terak, chinor, tol, yong‘oq, o‘rik;\n"
               "• buta — yerdan bir nechta ingichka yog‘och poya o‘sib chiqadi: atirgul, na’matak, qorag‘at;\n"
               "• o‘t — poyasi yumshoq va yashil: rayhon, yalpiz, beda, lola, bug‘doy.\n"
               "Daraxt va butalar ko‘p yil yashaydi. Archa — ignabargli daraxt, u qishda ham yashil.",
        items=[
            Q("Qaysi biri daraxt?", "Chinor", ["Atirgul", "Rayhon", "Yalpiz"], x="Chinorning bitta yo‘g‘on tanasi bor."),
            Q("Qaysi biri buta?", "Atirgul", ["Terak", "Yong‘oq", "Bug‘doy"], e="🌹",
              x="Atirgulda yerdan bir nechta ingichka poya o‘sib chiqadi."),
            Q("Qaysi biri o‘t o‘simlik?", "Rayhon", ["Tol", "Chinor", "Na’matak"],
              x="Rayhonning poyasi yumshoq va yashil."),
            Q("Daraxtning nechta tanasi bor?", "Bitta", ["Beshta", "O‘nta", "Tanasi yo‘q"],
              x="Daraxtda bitta yo‘g‘on tana bo‘ladi."),
            Q("Butada nechta poya bo‘ladi?", "Bir nechta", ["Bitta yo‘g‘on", "Umuman yo‘q", "Faqat bitta ingichka"],
              x="Butada yerdan bir nechta ingichka poya o‘sadi."),
            Q("Rayhonning poyasi qanday?", "Yumshoq va yashil", ["Yo‘g‘on va yog‘och", "Qalin po‘stloqli", "Temirdek qattiq"],
              x="Rayhon — o‘t o‘simlik, poyasi yumshoq."),
            Q("Odatda qaysi o‘simliklar eng baland bo‘ladi?", "Daraxtlar", ["Butalar", "O‘tlar", "Gullar"],
              x="Daraxtlar butadan ham, o‘tdan ham baland o‘sadi."),
            Q("Qaysi daraxt qishda ham yashil turadi?", "Archa", ["Terak", "Tol", "O‘rik"], e="🌲",
              x="Archaning ignabarglari qishda to‘kilmaydi."),
            TF("Terak — daraxt.", True, x="Terakning bitta baland tanasi bor."),
            TF("Yalpiz — buta.", False, x="Yalpizning poyasi yumshoq — u o‘t o‘simlik."),
            TF("Daraxtlar ko‘p yil yashaydi.", True, x="Ba’zi daraxtlar yuzlab yil yashaydi."),
            TF("Bug‘doy — o‘t o‘simlik.", True, x="Bug‘doyning poyasi yumshoq, u o‘t o‘simlik."),
            MATCH("O‘simlikni turi bilan juftlang", [("Chinor", "daraxt"), ("Atirgul", "buta"), ("Rayhon", "o‘t")],
                  x="Chinor — daraxt, atirgul — buta, rayhon — o‘t."),
            Q("Qaysi o‘simlikning tikani bor?", "Na’matak", ["Rayhon", "Terak", "Bug‘doy"], d=2,
              x="Na’matak va atirgul poyasida tikanlar bor."),
            Q("Qaysi qatorda faqat butalar bor?", "Atirgul, na’matak, qorag‘at",
              ["Terak, atirgul, rayhon", "Chinor, tol, yong‘oq", "Lola, yalpiz, beda"], d=2,
              x="Atirgul, na’matak va qorag‘at — butalar."),
            Q("Qaysi qatorda hammasi daraxt?", "Terak, tol, chinor",
              ["Terak, lola, beda", "Atirgul, yalpiz, rayhon", "Bug‘doy, tol, na’matak"], d=2,
              x="Terak, tol va chinorning bittadan yo‘g‘on tanasi bor."),
            Q("Qaysi qatorda hammasi o‘t?", "Beda, yalpiz, lola",
              ["Chinor, beda, lola", "Na’matak, tol, rayhon", "Yong‘oq, o‘rik, olma"], d=2,
              x="Beda, yalpiz va lolaning poyasi yumshoq."),
            Q("Qaysi biri ortiqcha: terak, tol, chinor, rayhon?", "Rayhon", ["Terak", "Tol", "Chinor"], d=2,
              x="Rayhon — o‘t, qolganlari daraxtlar."),
            Q("Archa qanday daraxt?", "Ignabargli", ["Bargsiz", "Suvda o‘sadigan", "Faqat yozda yashil"], d=2, e="🌲",
              x="Archaning barglari ingichka ignaga o‘xshaydi."),
            Q("Daraxtning qaysi qismidan yog‘och olinadi?", "Tanasidan", ["Bargidan", "Gulidan", "Mevasidan"], d=2,
              x="Daraxt tanasidan taxta va yog‘och olinadi."),
            ORDER(S, "Terak baland bo‘lib o‘sadi", d=2, x="Terak — baland daraxt."),
            Q("Daraxt yoshini qanday bilish mumkin?", "Kesilgan tanadagi halqalardan",
              ["Barglar sonidan", "Rangidan", "Hididan"], d=3,
              x="Daraxt tanasida har yili bitta yangi halqa qo‘shiladi."),
            Q("Qaysi daraxt suv bo‘yida o‘sishni yaxshi ko‘radi?", "Tol", ["Saksovul", "Archa", "Kaktus"], d=3,
              x="Tol ariq va daryo bo‘ylarida ko‘p o‘sadi."),
            TF("Butaning poyasi ham yog‘ochdan iborat.", True, d=3,
               x="Butaning poyalari ingichka, lekin qattiq, yog‘ochlangan."),
        ])

T.topic("crops_wild", "🌾", L("Madaniy va yovvoyi o‘simliklar", "Cultivated and wild plants",
                              "Культурные и дикорастущие растения"),
        chapter=C2,
        theory="• Madaniy o‘simliklarni odamlar ekadi, sug‘oradi va parvarish qiladi: bug‘doy, g‘o‘za, sholi, kartoshka, olma.\n"
               "• Yovvoyi o‘simliklar tabiatda o‘z-o‘zidan o‘sadi: qoqio‘t, yantoq, qamish, shuvoq.\n"
               "Madaniy o‘simliklar guruhlari: don ekinlari (bug‘doy, sholi, makkajo‘xori), sabzavotlar, mevali daraxtlar, "
               "poliz ekinlari (qovun, tarvuz, qovoq).\n"
               "Ekin orasida o‘sadigan keraksiz o‘tlar — begona o‘tlar.",
        items=[
            Q("Madaniy o‘simliklarni kim ekadi?", "Odamlar", ["Shamol", "Qushlar", "Hech kim"],
              x="Madaniy o‘simliklarni odamlar ekib, parvarish qiladi."),
            Q("Qaysi biri madaniy o‘simlik?", "Bug‘doy", ["Qoqio‘t", "Yantoq", "Qamish"],
              x="Bug‘doyni dehqonlar dalaga ekadi."),
            Q("Qaysi biri yovvoyi o‘simlik?", "Qoqio‘t", ["Kartoshka", "Pomidor", "Sholi"],
              x="Qoqio‘tni hech kim ekmaydi, u o‘z-o‘zidan o‘sadi."),
            Q("Yovvoyi o‘simliklar qanday o‘sadi?", "O‘z-o‘zidan", ["Faqat issiqxonada", "Faqat dehqon ekkanda",
                                                                  "Faqat tuvakda"],
              x="Yovvoyi o‘simliklarni hech kim ekmaydi va sug‘ormaydi."),
            Q("Non qaysi o‘simlikdan tayyorlanadi?", "Bug‘doydan", ["G‘o‘zadan", "Kartoshkadan", "Qamishdan"], e="🍞",
              x="Bug‘doy donidan un tortiladi, undan non yopiladi."),
            Q("Paxta qaysi o‘simlikda yetiladi?", "G‘o‘zada", ["Bug‘doyda", "Sholida", "Makkajo‘xorida"],
              x="Paxta — g‘o‘za ko‘sagidagi oq tola."),
            Q("Madaniy o‘simliklar qayerda o‘sadi?", "Dala, bog‘ va tomorqada",
              ["Faqat cho‘lda", "Faqat tog‘ cho‘qqisida", "Faqat suv tagida"],
              x="Odamlar ularni dala, bog‘ va tomorqaga ekadi."),
            TF("Yantoq — yovvoyi o‘simlik.", True, x="Yantoq cho‘lda o‘z-o‘zidan o‘sadi."),
            TF("Kartoshka — yovvoyi o‘simlik.", False, x="Kartoshkani odamlar ekadi — u madaniy o‘simlik."),
            TF("Madaniy o‘simliklarga parvarish kerak.", True, x="Ularni sug‘orish, o‘toq qilish, o‘g‘itlash kerak."),
            TF("Qoqio‘tni hech kim ekmaydi.", True, x="Qoqio‘t — yovvoyi o‘simlik."),
            Q("Palov uchun guruch qaysi ekindan olinadi?", "Sholi", ["Bug‘doy", "Arpa", "G‘o‘za"], d=2,
              x="Guruch — sholining doni."),
            Q("Qaysi biri don ekini?", "Makkajo‘xori", ["Qovun", "Bodring", "Karam"], d=2, e="🌽",
              x="Makkajo‘xori, bug‘doy va sholi — don ekinlari."),
            Q("Qaysi biri poliz ekini?", "Qovoq", ["Bug‘doy", "Sholi", "Olma"], d=2,
              x="Qovun, tarvuz va qovoq — poliz ekinlari."),
            Q("Qoqio‘tning momiq urug‘larini nima tarqatadi?", "Shamol", ["Baliqlar", "Mashinalar", "Qor"], d=2,
              x="Shamol momiq urug‘larni uzoqqa uchirib ketadi."),
            Q("Bodring va pomidor qaysi guruhga kiradi?", "Sabzavotlar",
              ["Don ekinlari", "Yovvoyi o‘tlar", "Mevali daraxtlar"], d=2,
              x="Bodring va pomidor — sabzavot ekinlari."),
            Q("Cho‘lda o‘sadigan, tuyalar yeydigan yovvoyi o‘simlik?", "Yantoq", ["Sholi", "Karam", "Bodring"], d=2,
              x="Yantoq tikanli bo‘lsa ham, tuyalar uni yeydi."),
            Q("Ariq va ko‘l bo‘yida o‘sadigan baland yovvoyi o‘t?", "Qamish", ["Bug‘doy", "Karam", "Kartoshka"], d=2,
              x="Qamish nam joylarda o‘z-o‘zidan o‘sadi."),
            MATCH("Ekinni mahsuloti bilan juftlang",
                  [("Bug‘doy", "non"), ("G‘o‘za", "paxta"), ("Uzum", "mayiz"), ("O‘rik", "turshak"),
                   ("Pomidor", "tomat pastasi")], d=2,
                  x="Bug‘doydan non, g‘o‘zadan paxta, uzumdan mayiz, o‘rikdan turshak olinadi."),
            ORDER(S, "Dehqonlar dalaga bug‘doy ekdi", d=2, x="Bug‘doy — madaniy o‘simlik."),
            Q("Ekin orasida o‘sib, unga xalaqit beradigan o‘tlar nima deyiladi?", "Begona o‘tlar",
              ["Madaniy ekinlar", "Mevali daraxtlar", "Xona gullari"], d=3,
              x="Begona o‘tlar ekinning suvi va oziqini tortib oladi."),
            Q("Qaysi qatorda hammasi madaniy o‘simlik?", "Bug‘doy, g‘o‘za, uzum",
              ["Bug‘doy, yantoq, uzum", "Qoqio‘t, qamish, shuvoq", "Yantoq, g‘o‘za, qamish"], d=3,
              x="Bug‘doy, g‘o‘za va uzumni odamlar ekadi."),
            Q("Mevasi vitaminga boy, ko‘pincha yovvoyi o‘sadigan buta?", "Na’matak", ["Karam", "Sholi", "Bug‘doy"], d=3,
              x="Na’matak mevasidan foydali damlama tayyorlanadi."),
            Q("Qadimda odamlar yovvoyi o‘simliklarni ekib nima qilgan?", "Madaniy o‘simlikka aylantirgan",
              ["Toshga aylantirgan", "Hayvonga aylantirgan", "Ularni yo‘q qilgan"], d=3,
              x="Odamlar eng yaxshi yovvoyi o‘simliklarni ekib, parvarish qilib, madaniy o‘simlik yaratgan."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["plant_needs", "plant_forms", "crops_wild"], chapter=C2)

# ============================================================ 3-chorak
T.topic("animal_food", "🐰", L("Hayvonlar nima yeydi", "What animals eat", "Чем питаются животные"),
        chapter=C3,
        theory="Hayvonlar nima yeyishiga qarab uch guruhga bo‘linadi:\n"
               "• O‘txo‘rlar o‘simlik yeydi: quyon, sigir, qo‘y, ot, echki, fil.\n"
               "• Yirtqichlar boshqa hayvonlarni ovlaydi: bo‘ri, tulki, sher, yo‘lbars, lochin.\n"
               "• Hammaxo‘rlar ham o‘simlik, ham hayvon bilan oziqlanadi: ayiq, qarg‘a.\n"
               "Yirtqichlarning tishlari va tirnoqlari o‘tkir, o‘txo‘rlarning tishlari o‘t chaynashga moslashgan.",
        items=[
            Q("O‘simlik yeydigan hayvonlar nima deyiladi?", "O‘txo‘rlar", ["Yirtqichlar", "Hammaxo‘rlar", "Hasharotlar"],
              x="O‘t, barg va meva yeydigan hayvonlar — o‘txo‘rlar."),
            Q("Boshqa hayvonlarni ovlaydigan hayvonlar nima deyiladi?", "Yirtqichlar",
              ["O‘txo‘rlar", "Hammaxo‘rlar", "Uy hayvonlari"], x="Ov qilib oziqlanadigan hayvonlar — yirtqichlar."),
            Q("Ham o‘t, ham go‘sht yeydigan hayvonlar nima deyiladi?", "Hammaxo‘rlar",
              ["O‘txo‘rlar", "Yirtqichlar", "Hasharotlar"], x="Hammaxo‘rlar o‘simlik ham, hayvon ham yeydi."),
            Q("Qaysi biri o‘txo‘r?", "🐰", ["🐺", "🦁", "🐯"], x="Quyon o‘t, barg va sabzavot yeydi."),
            Q("Qaysi biri yirtqich?", "🦁", ["🐄", "🐑", "🐰"], x="Sher boshqa hayvonlarni ovlaydi."),
            Q("Echki nima yeydi?", "O‘t va barg", ["Go‘sht", "Baliq", "Sichqon"], e="🐐", x="Echki — o‘txo‘r."),
            Q("Bo‘ri nima bilan oziqlanadi?", "Boshqa hayvonlar bilan", ["Faqat o‘t bilan", "Faqat meva bilan",
                                                                        "Faqat don bilan"], e="🐺",
              x="Bo‘ri — yirtqich, u ov qiladi."),
            Q("Fil nima yeydi?", "O‘t, barg va meva", ["Baliq", "Go‘sht", "Hasharot"], e="🐘",
              x="Fil juda katta bo‘lsa ham, o‘txo‘r."),
            TF("Yo‘lbars — yirtqich.", True, e="🐯", x="Yo‘lbars boshqa hayvonlarni ovlaydi."),
            TF("Ot go‘sht yeydi.", False, e="🐎", x="Ot — o‘txo‘r, u o‘t, pichan va arpa yeydi."),
            TF("Ayiq meva ham, baliq ham yeydi.", True, e="🐻", x="Ayiq — hammaxo‘r."),
            TF("Quyonning ozig‘i — o‘t va sabzavot.", True, e="🐰", x="Quyon — o‘txo‘r."),
            MATCH("Hayvonni guruhi bilan juftlang", [("Quyon", "o‘txo‘r"), ("Bo‘ri", "yirtqich"), ("Ayiq", "hammaxo‘r")],
                  x="Quyon — o‘txo‘r, bo‘ri — yirtqich, ayiq — hammaxo‘r."),
            Q("Yirtqichga ov qilishda nima yordam beradi?", "O‘tkir tish va tirnoqlar",
              ["Uzun quloqlar", "Tuyoqlar", "Kalta dum"], d=2, x="O‘tkir tish va tirnoqlar bilan yirtqich o‘ljasini ushlaydi."),
            Q("Qaysi qush yirtqich?", "Lochin", ["Kaptar", "Musicha", "Tovuq"], d=2,
              x="Lochin mayda qushlar va kemiruvchilarni ovlaydi."),
            Q("Qaysi qush hammaxo‘r?", "Qarg‘a", ["Lochin", "Burgut", "Boyqush"], d=2,
              x="Qarg‘a don, meva, qurt va hasharotlarni ham yeydi."),
            Q("Chumchuq nima yeydi?", "Don va hasharotlar", ["Faqat go‘sht", "Faqat baliq", "Tosh"], d=2,
              x="Chumchuq don cho‘qiydi va hasharotlarni ham tutadi."),
            Q("Qo‘y qishda nima yeydi?", "Pichan", ["Baliq", "Go‘sht", "Qor"], d=2, e="🐑",
              x="Yozda o‘rilgan o‘t quritilib, pichan qilinadi va qishda qo‘ylarga beriladi."),
            Q("Oziq zanjirini davom ettiring: o‘t → qo‘y → ...", "Bo‘ri", ["Sigir", "Echki", "Quyon"], d=2,
              x="Qo‘y o‘t yeydi, bo‘ri esa qo‘yni ovlaydi."),
            Q("Qaysi qatorda hammasi o‘txo‘r?", "Ot, echki, fil", ["Ot, sher, fil", "Bo‘ri, tulki, sher",
                                                                   "Echki, burgut, qo‘y"], d=2,
              x="Ot, echki va fil o‘simlik yeydi."),
            MATCH("Hayvonni ozig‘i bilan juftlang",
                  [("Olmaxon", "yong‘oq"), ("Ayiq", "asal"), ("Echki", "barg"), ("Tulki", "quyon"),
                   ("Kapalak", "gul shirasi")], d=2,
                  x="Har bir hayvon o‘ziga mos oziq yeydi."),
            ORDER(S, "Bo‘ri boshqa hayvonlarni ovlaydi", d=2, x="Bo‘ri — yirtqich."),
            Q("Har bir oziq zanjirining boshida nima turadi?", "O‘simlik", ["Yirtqich", "Tosh", "Suv"], d=3,
              x="O‘simlikni o‘txo‘r yeydi, o‘txo‘rni esa yirtqich ovlaydi."),
            Q("O‘txo‘rlarning tishlari nimaga moslashgan?", "O‘t chaynashga", ["Ov qilishga", "Suyak chaqishga", "Uchishga"],
              d=3, x="O‘txo‘rlarning keng tishlari o‘tni maydalab chaynaydi."),
            Q("Yirtqichlar tabiatda qanday foyda keltiradi?", "Kasal va zaif hayvonlarni ovlaydi",
              ["O‘tlarni yeb qo‘yadi", "Daraxt ekadi", "Hech qanday foyda keltirmaydi"], d=3,
              x="Yirtqichlar ko‘pincha kasal va zaif hayvonlarni tutadi, shuning uchun ular ham tabiatga kerak."),
        ])

T.topic("animal_winter", "🐻", L("Hayvonlar qishga tayyorlanadi", "How animals get ready for winter",
                                 "Как животные готовятся к зиме"),
        chapter=C3,
        theory="Kuzda hayvonlar qishga tayyorlanadi:\n"
               "• Ayiq, tipratikan, sug‘ur, toshbaqa, baqa qishki uyquga ketadi.\n"
               "• Olmaxon yong‘oq g‘amlaydi, ko‘p hayvonlarning juni qalin va issiq bo‘ladi.\n"
               "• Laylak, qaldirg‘och, turna issiq o‘lkalarga uchib ketadi — ular ko‘chmanchi qushlar.\n"
               "• Chumchuq, qarg‘a, kaptar, musicha qishda ham shu yerda qoladi — ular qishlovchi qushlar.\n"
               "Qishda hasharotlar yo‘qoladi, shuning uchun ular bilan oziqlanadigan qushlar uchib ketadi.",
        items=[
            Q("Qaysi hayvon qishki uyquga ketadi?", "Tipratikan", ["Bo‘ri", "Quyon", "Tulki"], e="🦔",
              x="Tipratikan qish bo‘yi barglar ostida uxlaydi."),
            Q("Kuzda issiq o‘lkalarga uchib ketadigan qush?", "Laylak", ["Chumchuq", "Qarg‘a", "Kaptar"],
              x="Laylak kuzda janubga uchib ketadi, bahorda qaytadi."),
            Q("Qishda ham bizda qoladigan qush?", "Chumchuq", ["Laylak", "Qaldirg‘och", "Turna"],
              x="Chumchuq qishda ham shu yerda yashaydi."),
            Q("Olmaxon qishga qanday tayyorlanadi?", "Yong‘oq g‘amlaydi",
              ["Issiq o‘lkaga uchadi", "Suvga sho‘ng‘iydi", "Junini to‘kadi"], e="🐿️",
              x="Olmaxon kuzda yong‘oq va urug‘larni yashirib qo‘yadi."),
            Q("Ayiq qishni qayerda o‘tkazadi?", "Inida uxlab", ["Daryo tubida", "Daraxt uchida", "Issiq o‘lkalarda"],
              e="🐻", x="Ayiq qish bo‘yi inida uxlaydi."),
            Q("Quyon va tulkining juni qishda qanday bo‘ladi?", "Qalin va issiq",
              ["Yupqa va siyrak", "Butunlay yo‘q", "Ho‘l va sovuq"],
              x="Qalin jun hayvonni qattiq sovuqdan saqlaydi."),
            Q("Qishlovchi qushni toping", "Kaptar", ["Laylak", "Qaldirg‘och", "Turna"],
              x="Kaptar qishda ham shu yerda qoladi."),
            Q("Qishda qushlar uchun nima yasaymiz?", "Yemlik", ["Qafas", "Tuzoq", "Hovuz"],
              x="Yemlikka don solib qo‘ysak, qushlar och qolmaydi."),
            TF("Olmaxon qish bo‘yi uxlaydi.", False, x="Olmaxon qishda uxlamaydi, g‘amlagan yong‘oqlarini yeydi."),
            TF("Baqa qishni uyquda o‘tkazadi.", True, e="🐸", x="Baqa qishda loy yoki barg ostida uxlaydi."),
            TF("Qarg‘a qishda ham shu yerda qoladi.", True, x="Qarg‘a — qishlovchi qush."),
            ORDER(S, "Kuzda qushlar janubga uchib ketadi", x="Ko‘chmanchi qushlar kuzda issiq o‘lkalarga uchadi."),
            Q("Qushlar nega kuzda issiq o‘lkalarga uchib ketadi?", "Qishda oziq topa olmaydi",
              ["Sayohatni yaxshi ko‘radi", "Uyasi eskiradi", "Patlari to‘kiladi"], d=2,
              x="Qishda hasharotlar yo‘qoladi, suvlar muzlaydi — qushlarga ovqat yetmaydi."),
            Q("Issiq o‘lkalarga uchib ketadigan qushlar nima deyiladi?", "Ko‘chmanchi qushlar",
              ["Qishlovchi qushlar", "Uy parrandalari", "Yirtqich qushlar"], d=2,
              x="Kuzda ketib, bahorda qaytadigan qushlar — ko‘chmanchi qushlar."),
            Q("Qishda ham shu yerda qoladigan qushlar nima deyiladi?", "Qishlovchi qushlar",
              ["Ko‘chmanchi qushlar", "Suv qushlari", "Uchmaydigan qushlar"], d=2,
              x="Chumchuq, qarg‘a, kaptar — qishlovchi qushlar."),
            Q("Kuzda ayiq nima qiladi?", "Ko‘p yeb, semiradi", ["Ozib ketadi", "Juni to‘kiladi", "Uchib ketadi"], d=2,
              x="To‘plangan yog‘ ayiqqa qish bo‘yi uxlashga yetadi."),
            Q("Bahorda qaysi qushlar qaytib keladi?", "Laylak va qaldirg‘och",
              ["Chumchuq va qarg‘a", "Kaptar va musicha", "Tovuq va xo‘roz"], d=2,
              x="Laylak va qaldirg‘och — ko‘chmanchi qushlar."),
            Q("Tipratikan qishni qanday o‘tkazadi?", "Barglar ostida uxlab", ["Daraxtga chiqib", "Uchib ketib",
                                                                             "Suvda suzib"], d=2, e="🦔",
              x="Tipratikan quruq barglardan in qilib, qish bo‘yi uxlaydi."),
            Q("Ko‘chmanchi qushni toping", "Turna", ["Chumchuq", "Musicha", "Qarg‘a"], d=2,
              x="Turnalar kuzda to‘p bo‘lib janubga uchadi."),
            TF("Turnalar kuzda janubga uchib ketadi.", True, d=2, x="Turna — ko‘chmanchi qush."),
            MATCH("Hayvon qishni qanday o‘tkazadi? Juftlang",
                  [("Ayiq", "inida uxlaydi"), ("Olmaxon", "yong‘oq g‘amlaydi"), ("Laylak", "issiq o‘lkaga uchadi"),
                   ("Chumchuq", "shu yerda qishlaydi")], d=2,
                  x="Har bir hayvon qishga o‘zicha tayyorlanadi."),
            Q("Qaysi hayvon qishki uyquga ketmaydi?", "Bo‘ri", ["Ayiq", "Tipratikan", "Sug‘ur"], d=3,
              x="Bo‘ri qishda ham ov qiladi, ayiq, tipratikan va sug‘ur esa uxlaydi."),
            Q("Chumolilar qishda nima qiladi?", "Uyasida harakatsiz qishlaydi",
              ["Issiq o‘lkaga uchadi", "Qor ustida yuguradi", "Daryoga ko‘chadi"], d=3,
              x="Chumolilar uyasining chuqur qismida qishni o‘tkazadi."),
            Q("Ko‘rshapalak qishni qanday o‘tkazadi?", "G‘orda osilib uxlab", ["Issiq o‘lkada", "Qor ustida",
                                                                              "Suv ostida"], d=3,
              x="Ko‘rshapalaklar g‘orlarda boshini pastga qilib osilib, qish bo‘yi uxlaydi."),
        ])

T.topic("uzbekistan", "🏔️", L("O‘zbekiston tabiati", "Nature of Uzbekistan", "Природа Узбекистана"),
        chapter=C3,
        theory="O‘zbekiston — quyoshli o‘lka. Yozi uzun va issiq.\n"
               "• Eng katta daryolarimiz — Amudaryo va Sirdaryo. Zarafshon va Chirchiq daryolari ham bor.\n"
               "• Sharqida va janubida tog‘lar, g‘arbida keng tekisliklar va Qizilqum cho‘li bor.\n"
               "• Tog‘larda archa o‘sadi, qor qoploni yashaydi; cho‘lda saksovul o‘sadi, jayron yashaydi.\n"
               "Poytaxtimiz — Toshkent shahri.",
        items=[
            Q("O‘zbekistonning poytaxti qaysi shahar?", "Toshkent", ["Samarqand", "Buxoro", "Xiva"],
              x="Toshkent — O‘zbekiston poytaxti."),
            Q("O‘zbekistonning eng katta daryolari qaysilar?", "Amudaryo va Sirdaryo",
              ["Chirchiq va Ohangaron", "Nil va Amazonka", "Volga va Dnepr"],
              x="Amudaryo va Sirdaryo — O‘rta Osiyodagi eng katta daryolar."),
            Q("O‘zbekistonda yoz qanday?", "Issiq va quyoshli", ["Juda sovuq va qorli", "Doim yomg‘irli", "Muzli"],
              x="O‘zbekistonda yoz uzun, issiq va quyoshli."),
            Q("Qizilqum nima?", "Cho‘l", ["Daryo", "Tog‘", "Ko‘l"], x="Qizilqum — O‘zbekistondagi katta qumli cho‘l."),
            Q("Tog‘larda qaysi daraxt ko‘p o‘sadi?", "Archa", ["Saksovul", "Tol", "Paxta"], e="🌲",
              x="Archa tog‘ yonbag‘irlarida o‘sadi."),
            Q("Cho‘lda qaysi o‘simlik o‘sadi?", "Saksovul", ["Archa", "Sholi", "Tol"],
              x="Saksovul qumli cho‘lda o‘sadi va qumni ushlab turadi."),
            Q("Jayron qayerda yashaydi?", "Cho‘lda", ["Muzli dengizda", "Daryo tubida", "Shahar markazida"],
              x="Jayron cho‘l va dashtlarda yashaydi, juda tez yuguradi."),
            Q("Qor qoploni qayerda yashaydi?", "Baland tog‘larda", ["Cho‘lda", "Daryoda", "Shaharda"],
              x="Qor qoploni baland tog‘ qoyalarida yashaydi."),
            TF("O‘zbekistonda tog‘lar ham, cho‘llar ham bor.", True, e="🏔️",
               x="Sharqda tog‘lar, g‘arbda cho‘l va tekisliklar bor."),
            TF("Toshkent — O‘zbekiston poytaxti.", True, x="Poytaxtimiz — Toshkent."),
            TF("O‘zbekiston — quyoshli o‘lka.", True, e="☀️", x="O‘zbekistonda yil bo‘yi quyoshli kunlar ko‘p."),
            TF("Amudaryo — O‘zbekistondagi eng katta daryolardan biri.", True, x="Amudaryo va Sirdaryo — eng katta daryolar."),
            Q("O‘zbekiston tabiatini asrash uchun nima qilamiz?", "Daraxt ekamiz, suvni tejaymiz",
              ["Daryoga axlat tashlaymiz", "Jayronlarni ovlaymiz", "Lolalarni yulamiz"],
              x="Tabiatni asrash — hammamizning burchimiz."),
            Q("Samarqand yonidan qaysi daryo oqadi?", "Zarafshon", ["Chirchiq", "Nil", "Volga"], d=2,
              x="Zarafshon daryosi Samarqand va Buxoro vohalarini sug‘oradi."),
            Q("Amudaryo va Sirdaryo qaysi dengizga quyiladi?", "Orol dengiziga",
              ["Qora dengizga", "Kaspiy dengiziga", "O‘rta yer dengiziga"], d=2,
              x="Ikki daryo ham Orol dengiziga quyiladi."),
            Q("Atrofi tog‘lar bilan o‘ralgan mashhur vodiy?", "Farg‘ona vodiysi", ["Qizilqum", "Ustyurt", "Orol"], d=2,
              x="Farg‘ona vodiysini har tomondan tog‘lar o‘rab turadi."),
            Q("O‘zbekistonda qaysi o‘simlik “oq oltin” deyiladi?", "G‘o‘za (paxta)", ["Bug‘doy", "Lola", "Archa"], d=2,
              x="Paxta juda qimmatli bo‘lgani uchun uni “oq oltin” deyishadi."),
            Q("Qaysi hayvon kamyob va muhofaza qilinadi?", "Qor qoploni", ["Uy mushugi", "Tovuq", "Chumchuq"], d=2,
              x="Qor qoploni kamyob, u Qizil kitobga kiritilgan."),
            MATCH("O‘simlikni o‘sadigan joyi bilan juftlang",
                  [("Archa", "tog‘ yonbag‘ri"), ("Saksovul", "qumli cho‘l"), ("Qamish", "daryo bo‘yi"), ("G‘o‘za", "dala")],
                  d=2, x="Har bir o‘simlik o‘ziga mos joyda o‘sadi."),
            ORDER(S, "Amudaryo va Sirdaryo katta daryolar", d=2, x="Ular O‘zbekistonning eng katta daryolari."),
            Q("Orol dengizining hozirgi holati qanday?", "Katta qismi qurib qolgan",
              ["Ikki baravar kattalashgan", "Butunlay muzlab qolgan", "Shirin suvga to‘lgan"], d=3,
              x="Daryolar suvi ko‘p olingani uchun Orol dengizining katta qismi qurib qoldi."),
            Q("Toshkent viloyatidagi mashhur tog‘ dam olish joyi?", "Chimyon", ["Qizilqum", "Orol", "Ustyurt"], d=3,
              x="Chimyon tog‘lari Toshkent viloyatida joylashgan."),
            Q("O‘zbekistonning g‘arbida asosan nima bor?", "Tekislik va cho‘llar", ["Baland qorli tog‘lar", "Okean",
                                                                                 "Muzliklar"], d=3,
              x="G‘arbda tekisliklar va cho‘llar, sharqda tog‘lar bor."),
            Q("Tog‘ daryolari qayerdan boshlanadi?", "Tog‘dagi qor va muzliklardan",
              ["Cho‘ldagi qumdan", "Dengizdan", "Shahar ariqlaridan"], d=3,
              x="Tog‘lardagi qor va muzliklar erib, daryolarni suv bilan to‘ldiradi."),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["animal_food", "animal_winter", "uzbekistan"], chapter=C3)

# ============================================================ 4-chorak
T.topic("directions", "🗺️", L("Olam tomonlari va kompas", "Cardinal directions and the compass",
                              "Стороны света и компас"),
        chapter=C4,
        theory="Olam tomonlari to‘rtta: shimol, janub, sharq, g‘arb.\n"
               "• Quyosh ertalab sharqdan chiqadi, kechqurun g‘arbga botadi.\n"
               "• Tushda Quyosh janub tomonda bo‘ladi, soyamiz esa shimolga tushadi.\n"
               "• Shimolga qarab tursak: o‘ngimizda — sharq, chapimizda — g‘arb, orqamizda — janub.\n"
               "Kompas — tomonlarni aniqlaydigan asbob, uning strelkasi shimolni ko‘rsatadi. Xaritaning tepasi — shimol.",
        items=[
            Q("Olam tomonlari nechta?", "4 ta", ["2 ta", "3 ta", "6 ta"], x="Shimol, janub, sharq va g‘arb."),
            Q("Quyosh qayerdan chiqadi?", "Sharqdan", ["G‘arbdan", "Shimoldan", "Janubdan"], e="🌅",
              x="Quyosh har kuni ertalab sharqdan chiqadi."),
            Q("Quyosh qayerga botadi?", "G‘arbga", ["Sharqqa", "Shimolga", "Janubga"], e="🌇",
              x="Kechqurun Quyosh g‘arbga botadi."),
            Q("Tomonlarni qaysi asbob aniqlaydi?", "Kompas", ["Termometr", "Tarozi", "Soat"],
              x="Kompas strelkasi shimolni ko‘rsatadi."),
            Q("Kompas strelkasi qaysi tomonni ko‘rsatadi?", "Shimolni", ["Sharqni", "G‘arbni", "Pastni"],
              x="Kompasning strelkasi doim shimolga buriladi."),
            Q("Qaysi biri olam tomoni emas?", "Tepa", ["Shimol", "Janub", "Sharq"],
              x="Olam tomonlari: shimol, janub, sharq, g‘arb."),
            Q("Xaritaning tepa tomoni qaysi?", "Shimol", ["Janub", "Sharq", "G‘arb"], e="🗺️",
              x="Xaritada tepa — shimol, past — janub."),
            Q("Shimolning qarama-qarshisi qaysi tomon?", "Janub", ["Sharq", "G‘arb", "Tepa"],
              x="Shimol va janub bir-biriga qarama-qarshi."),
            Q("Adashib qolsak, tomonlarni nima bilan aniqlaymiz?", "Kompas bilan",
              ["Termometr bilan", "Chizg‘ich bilan", "Qoshiq bilan"], x="Kompas yo‘lni topishga yordam beradi."),
            TF("Quyosh g‘arbdan chiqadi.", False, x="Quyosh sharqdan chiqib, g‘arbga botadi."),
            TF("Kompas yo‘lni topishga yordam beradi.", True, x="Kompas tomonlarni ko‘rsatadi."),
            TF("Olam tomonlari: shimol, janub, sharq, g‘arb.", True, x="Olam tomonlari to‘rtta."),
            Q("Sharqning qarama-qarshisi qaysi tomon?", "G‘arb", ["Janub", "Shimol", "Past"], d=2,
              x="Sharq va g‘arb bir-biriga qarama-qarshi."),
            Q("Shimolga qarab tursak, o‘ng qo‘limiz qaysi tomonda?", "Sharqda", ["G‘arbda", "Janubda", "Shimolda"], d=2,
              x="Shimolga qaraganda o‘ngda sharq, chapda g‘arb bo‘ladi."),
            Q("Shimolga qarab tursak, orqamiz qaysi tomonda?", "Janubda", ["Sharqda", "G‘arbda", "Shimolda"], d=2,
              x="Shimolning qarama-qarshisi — janub."),
            Q("Ertalab chiqayotgan Quyoshga qarasak, qaysi tomonga qaragan bo‘lamiz?", "Sharqqa",
              ["G‘arbga", "Shimolga", "Janubga"], d=2, x="Quyosh sharqdan chiqadi."),
            MATCH("Tomonni qarama-qarshisi bilan juftlang",
                  [("Shimol", "janub"), ("Janub", "shimol"), ("Sharq", "g‘arb"), ("G‘arb", "sharq")], d=2,
                  x="Shimol — janub, sharq — g‘arb: ular qarama-qarshi tomonlar."),
            MATCH("Nima qaysi tomonni ko‘rsatadi?",
                  [("Quyosh chiqishi", "sharq"), ("Quyosh botishi", "g‘arb"), ("Kompas strelkasi", "shimol"),
                   ("Tushdagi Quyosh", "janub")], d=2,
                  x="Quyosh sharqdan chiqadi, g‘arbga botadi, tushda janubda bo‘ladi; kompas shimolni ko‘rsatadi."),
            ORDER(S, "Quyosh sharqdan chiqib g‘arbga botadi", d=2, x="Quyosh har kuni shunday harakatlanadi."),
            Q("Shimolga qarab tursak, chap qo‘limiz qaysi tomonda?", "G‘arbda", ["Sharqda", "Janubda", "Shimolda"], d=3,
              x="Shimolga qaraganda chapda g‘arb bo‘ladi."),
            Q("Tushda Quyosh qaysi tomonda bo‘ladi?", "Janubda", ["Shimolda", "G‘arbda", "Sharqda"], d=3,
              x="Bizning o‘lkada tushda Quyosh janub tomonda turadi."),
            Q("Tushda soyamiz qaysi tomonga tushadi?", "Shimolga", ["Janubga", "Sharqqa", "G‘arbga"], d=3,
              x="Quyosh janubda bo‘lganda soya teskari tomonga — shimolga tushadi."),
            Q("Kechasi shimolni qaysi yulduz ko‘rsatadi?", "Qutb yulduzi", ["Quyosh", "Oy", "Kamalak"], d=3,
              x="Qutb yulduzi doim shimol tomonda ko‘rinadi."),
        ])

T.topic("time", "⏰", L("Vaqt: sutka, hafta, yil", "Time: day, week, year", "Время: сутки, неделя, год"),
        chapter=C4,
        theory="• Sutka — 24 soat: kunduz va tun. 1 soat — 60 daqiqa.\n"
               "• Hafta — 7 kun: dushanba, seshanba, chorshanba, payshanba, juma, shanba, yakshanba.\n"
               "• Yil — 12 oy va 4 fasl, har faslda 3 oy.\n"
               "• Qish: dekabr, yanvar, fevral. Bahor: mart, aprel, may.\n"
               "• Yoz: iyun, iyul, avgust. Kuz: sentyabr, oktyabr, noyabr.\n"
               "Yer o‘z o‘qi atrofida bir marta aylanganda bir sutka o‘tadi.",
        items=[
            Q("Bir sutkada necha soat bor?", "24 soat", ["12 soat", "7 soat", "60 soat"],
              x="Sutka — 24 soat: kunduz va tun."),
            Q("Bir haftada necha kun bor?", "7 kun", ["5 kun", "10 kun", "12 kun"], x="Haftada 7 kun bor."),
            Q("Bir yilda necha oy bor?", "12 oy", ["7 oy", "10 oy", "24 oy"], x="Yil 12 oydan iborat."),
            Q("Haftaning birinchi kuni qaysi?", "Dushanba", ["Juma", "Shanba", "Chorshanba"],
              x="Hafta dushanbadan boshlanadi."),
            Q("Dushanbadan keyin qaysi kun keladi?", "Seshanba", ["Payshanba", "Yakshanba", "Juma"],
              x="Dushanba, seshanba, chorshanba..."),
            Q("Shanbadan keyin qaysi kun keladi?", "Yakshanba", ["Dushanba", "Juma", "Seshanba"],
              x="Shanbadan keyin yakshanba keladi."),
            Q("Yilning birinchi oyi qaysi?", "Yanvar", ["Mart", "Sentyabr", "Dekabr"], x="Yil yanvardan boshlanadi."),
            Q("Qaysi oy qishga kiradi?", "Yanvar", ["Iyul", "Aprel", "Sentyabr"],
              x="Qish oylari: dekabr, yanvar, fevral."),
            Q("Qaysi oy yozga kiradi?", "Iyul", ["Yanvar", "Oktyabr", "Mart"], x="Yoz oylari: iyun, iyul, avgust."),
            Q("Vaqtni nima bilan o‘lchaymiz?", "Soat bilan", ["Termometr bilan", "Chizg‘ich bilan", "Tarozi bilan"],
              e="⏰", x="Soat vaqtni ko‘rsatadi."),
            TF("Bir yilda 4 ta fasl bor.", True, x="Qish, bahor, yoz va kuz."),
            TF("Sutka — bu faqat kunduz.", False, x="Sutka kunduz va tundan iborat — 24 soat."),
            ORDER(S, "Bir haftada yetti kun bor", x="Haftada 7 kun bor."),
            Q("Bir soatda necha daqiqa bor?", "60 daqiqa", ["10 daqiqa", "24 daqiqa", "100 daqiqa"], d=2,
              x="1 soat — 60 daqiqa."),
            Q("Yilning oxirgi oyi qaysi?", "Dekabr", ["Yanvar", "Noyabr", "Iyun"], d=2, x="Yil dekabr bilan tugaydi."),
            Q("Haftaning oxirgi kuni qaysi?", "Yakshanba", ["Shanba", "Dushanba", "Juma"], d=2,
              x="Hafta yakshanba bilan tugaydi."),
            Q("Bahor oylari qaysilar?", "Mart, aprel, may",
              ["Iyun, iyul, avgust", "Dekabr, yanvar, fevral", "Sentyabr, oktyabr, noyabr"], d=2,
              x="Bahor oylari: mart, aprel, may."),
            Q("Kuz oylari qaysilar?", "Sentyabr, oktyabr, noyabr",
              ["Mart, aprel, may", "Iyun, iyul, avgust", "Dekabr, yanvar, fevral"], d=2,
              x="Kuz oylari: sentyabr, oktyabr, noyabr."),
            Q("Bugun chorshanba. Ertaga qaysi kun?", "Payshanba", ["Seshanba", "Juma", "Dushanba"], d=2,
              x="Chorshanbadan keyin payshanba keladi."),
            Q("Fevraldan keyin qaysi oy keladi?", "Mart", ["Yanvar", "Aprel", "May"], d=2,
              x="Fevraldan keyin mart — bahorning birinchi oyi."),
            Q("Kunlar, haftalar va oylar yozilgan narsa nima?", "Taqvim", ["Xarita", "Kompas", "Globus"], d=2, e="📅",
              x="Taqvimdan bugun qaysi kun ekanini bilamiz."),
            TF("Har faslda 3 oydan bor.", True, d=2, x="4 fasl × 3 oy = 12 oy."),
            MATCH("Vaqt birligini uzunligi bilan juftlang",
                  [("Sutka", "24 soat"), ("Hafta", "7 kun"), ("Yil", "12 oy"), ("Soat", "60 daqiqa"), ("Fasl", "3 oy")],
                  d=2, x="Sutka — 24 soat, hafta — 7 kun, yil — 12 oy, soat — 60 daqiqa, fasl — 3 oy."),
            Q("Bugun juma. Kecha qaysi kun edi?", "Payshanba", ["Shanba", "Chorshanba", "Yakshanba"], d=3,
              x="Jumadan oldin payshanba keladi."),
            Q("Yer Quyosh atrofini qancha vaqtda aylanib chiqadi?", "1 yilda", ["1 kunda", "1 haftada", "1 soatda"], d=3,
              x="Yer Quyosh atrofini bir yilda bir marta aylanib chiqadi."),
            TF("Yer o‘z o‘qi atrofida aylangani uchun kun va tun almashadi.", True, d=3,
               x="Yerning Quyoshga qaragan tomonida kunduz, teskari tomonida tun bo‘ladi."),
        ])

T.topic("health", "💪", L("Salomatlik", "Health", "Здоровье"),
        chapter=C4,
        theory="Sog‘lom bo‘lish uchun:\n"
               "• To‘g‘ri ovqatlanamiz: meva, sabzavot, sut, non, go‘sht, baliq yeymiz. Shirinlik va gazli ichimliklar — kam.\n"
               "• Har kuni harakat qilamiz: badantarbiya, yugurish, suzish, futbol.\n"
               "• Vaqtida uxlaymiz, toza havoda sayr qilamiz.\n"
               "• Ovqatni shoshilmay, yaxshilab chaynab yeymiz.\n"
               "Kasal bo‘lsak, shifokorga boramiz.",
        items=[
            Q("Qaysi ovqat foydaliroq?", "Meva va sabzavot", ["Chips va gazli suv", "Faqat konfet", "Faqat tort"], e="🥗",
              x="Meva va sabzavotda vitaminlar ko‘p."),
            Q("Tishni nima ko‘proq buzadi?", "Ko‘p shirinlik", ["Olma", "Sut", "Sabzi"], e="🍬",
              x="Shirinlik ko‘p yesak, tishlar tez buziladi."),
            Q("Sut nima uchun foydali?", "Suyak va tishni mustahkamlaydi",
              ["Ko‘zni yumdiradi", "Uyquni qochiradi", "Tishni buzadi"], e="🥛",
              x="Sut va qatiq suyak hamda tishlarni mustahkam qiladi."),
            Q("Qaysi biri sport turi?", "Suzish", ["Uxlash", "Multfilm ko‘rish", "Konfet yeyish"], e="🏊",
              x="Suzish — foydali sport turi."),
            Q("Ovqatni qanday yeymiz?", "Shoshilmay, yaxshilab chaynab", ["Yugurib-yugurib", "Chaynamay yutib",
                                                                          "Gapirib, kulib"],
              x="Yaxshi chaynalgan ovqat oson hazm bo‘ladi."),
            Q("Kasal bo‘lsak kimga boramiz?", "Shifokorga", ["Sartaroshga", "Haydovchiga", "Sotuvchiga"],
              x="Shifokor kasallikni aniqlab, davolaydi."),
            Q("Badantarbiya qachon qilinadi?", "Ertalab", ["Yarim kechada", "Ovqat paytida", "Uxlayotganda"],
              x="Ertalabki badantarbiya tanani uyg‘otadi."),
            Q("Vitaminlar qayerda ko‘p?", "Meva va sabzavotlarda", ["Konfetda", "Gazli suvda", "Chipsda"],
              x="Vitaminlar meva va sabzavotlarda ko‘p bo‘ladi."),
            Q("Sport bilan shug‘ullangan bola qanday bo‘ladi?", "Baquvvat va chaqqon",
              ["Kasalvand", "Tez charchaydigan", "Kuchsiz"], x="Sport muskullarni kuchli qiladi."),
            TF("Har kuni harakat qilish sog‘liqqa foydali.", True, x="Harakat tanani baquvvat qiladi."),
            TF("Gazli shirin ichimliklarni ko‘p ichish foydali.", False,
               x="Ularda shakar juda ko‘p, ular tish va sog‘liqqa zarar."),
            TF("Yaxshi uyqu ham salomatlik uchun muhim.", True, x="Uyquda tana dam oladi va kuch to‘playdi."),
            TF("Nonushta qilmay maktabga borish to‘g‘ri.", False, x="Nonushta kun boshida kuch beradi."),
            TF("Qo‘lni yuvmay ovqatlanish kasallikka olib kelishi mumkin.", True, x="Kir qo‘lda mikroblar bo‘ladi."),
            ORDER(S, "Sport bizni baquvvat qiladi", x="Sport bilan shug‘ullansak, kuchli bo‘lamiz."),
            Q("Partada qanday o‘tiramiz?", "Qaddimizni tik tutib", ["Bukchayib", "Yonboshlab", "Oyoqni stolga qo‘yib"], d=2,
              x="Tik o‘tirsak, umurtqa pog‘onasi qiyshaymaydi."),
            Q("Qaysi biri sog‘lom kun tartibiga mos?", "Erta yotib, erta turish",
              ["Kech yotib, kech turish", "Tunda o‘ynash", "Nonushta qilmaslik"], d=2,
              x="Erta yotgan bola yaxshi uxlaydi va tetik turadi."),
            Q("Ko‘p vaqt telefonga qarash nimaga zarar?", "Ko‘zga", ["Sochga", "Tirnoqqa", "Kiyimga"], d=2,
              x="Ekranga uzoq qarash ko‘zni charchatadi."),
            Q("Chanqaganda eng foydali ichimlik qaysi?", "Toza suv", ["Gazli shirin suv", "Energetik ichimlik",
                                                                     "Juda shirin sharbat"], d=2,
              x="Toza suv chanqoqni yaxshi qondiradi va zarar qilmaydi."),
            Q("Qishda shamollamaslik uchun nima qilamiz?", "Issiq kiyinamiz",
              ["Yengil kiyinamiz", "Ko‘chada muzqaymoq yeymiz", "Ho‘l oyoq bilan yuramiz"], d=2,
              x="Sovuqda issiq kiyinsak, shamollamaymiz."),
            MATCH("Nima nimaga foydali? Juftlang",
                  [("Sut", "suyak va tish"), ("Sabzi", "ko‘z"), ("Sport", "muskullar"), ("Uyqu", "dam olish")], d=2,
                  x="Sut — suyakka, sabzi — ko‘zga, sport — muskulga, uyqu — dam olishga foydali."),
            Q("Kitob o‘qiganda ko‘zdan kitobgacha qancha masofa bo‘lishi kerak?", "30 sm atrofida",
              ["1–2 sm", "5 sm", "3 metr"], d=3, x="Kitobni ko‘zdan taxminan 30 sm uzoqlikda tutamiz."),
            Q("Yozda tushda uzoq quyoshda yursak nima bo‘lishi mumkin?", "Quyosh urishi",
              ["Muzlab qolish", "Tish og‘rig‘i", "Qorda adashish"], d=3,
              x="Issiq kunda bosh kiyimsiz uzoq yursak, quyosh urishi mumkin."),
            Q("Muskullarni kuchli qiladigan ovqatlar qaysi?", "Go‘sht, tuxum, baliq",
              ["Konfet, tort, chips", "Gazli suv, saqich", "Shakar, murabbo"], d=3,
              x="Go‘sht, tuxum va baliqda muskullar uchun kerakli oqsil ko‘p."),
        ])

T.topic("protect", "🌍", L("Tabiatni muhofaza qilish", "Protecting nature", "Охрана природы"),
        chapter=C4,
        theory="Tabiatni muhofaza qilish — uni asrash va ifloslantirmaslik.\n"
               "• Kamyob hayvon va o‘simliklar “Qizil kitob”ga yoziladi va muhofaza qilinadi.\n"
               "• Qo‘riqxonalarda tabiat qo‘riqlanadi: u yerda ov qilish, daraxt kesish mumkin emas.\n"
               "• Chiqindini saralaymiz: qog‘oz, plastik, shisha alohida yig‘iladi va qayta ishlanadi.\n"
               "• Suvni, elektrni tejaymiz, daraxt ekamiz. Har birimiz tabiatga yordam bera olamiz.",
        items=[
            Q("Kamyob hayvon va o‘simliklar qaysi kitobga yoziladi?", "Qizil kitobga",
              ["Yashil kitobga", "Ko‘k kitobga", "Oq kitobga"], x="Qizil kitobga yo‘qolib ketish xavfi bor jonzotlar yoziladi."),
            Q("Tabiat qo‘riqlanadigan joy nima deyiladi?", "Qo‘riqxona", ["Bozor", "Zavod", "Stadion"],
              x="Qo‘riqxonada hayvon va o‘simliklar muhofaza qilinadi."),
            Q("Qo‘riqxonada nima qilish mumkin emas?", "Ov qilish", ["Tabiatni kuzatish", "Qushlarni tomosha qilish",
                                                                    "Rasm chizish"],
              x="Qo‘riqxonada ov qilish va daraxt kesish taqiqlangan."),
            Q("Qog‘oz, plastik va shishani nima qilamiz?", "Alohida yig‘amiz",
              ["Yerga ko‘mamiz", "Daryoga tashlaymiz", "Gulxanda yoqamiz"], e="♻️",
              x="Saralangan chiqindi qayta ishlanadi."),
            Q("Havoni toza saqlash uchun nima qilamiz?", "Daraxt ekamiz",
              ["Axlat yoqamiz", "Daraxt kesamiz", "Ko‘p tutun chiqaramiz"], e="🌳", x="Daraxtlar havoni tozalaydi."),
            Q("Elektrni qanday tejaymiz?", "Xonadan chiqqanda chiroqni o‘chiramiz",
              ["Kun bo‘yi chiroqni yoqib qo‘yamiz", "Televizorni o‘chirmaymiz", "Hamma chiroqni yoqamiz"], e="💡",
              x="Keraksiz yonib turgan chiroq elektrni isrof qiladi."),
            Q("Adirda lolalarni ko‘rsak nima qilamiz?", "Yulmay, tomosha qilamiz",
              ["Guldasta qilib yulamiz", "Ildizi bilan sug‘urib olamiz", "Oyoq osti qilamiz"], e="🌷",
              x="Yovvoyi lolalarni yulmaymiz, ular kelgusi yil ham ochilsin."),
            Q("Qaysi biri tabiatga foyda?", "Nihol ekish",
              ["Daraxt po‘stlog‘ini shilish", "Qush uyasini buzish", "Ariqqa shisha tashlash"],
              x="Ekilgan nihol katta daraxt bo‘lib, havoni tozalaydi."),
            TF("Qizil kitobdagi hayvonlarni ovlash mumkin emas.", True, x="Ular kamyob, ularni muhofaza qilish kerak."),
            TF("Plastik tabiatda tez chirib ketadi.", False, x="Plastik juda ko‘p yillar chirimaydi."),
            TF("Daryoga axlat tashlash baliqlarga zarar.", True, e="🐟", x="Iflos suvda baliqlar kasallanadi."),
            TF("Har bir bola tabiatga yordam bera oladi.", True, x="Masalan, axlatni qutiga tashlab, suvni tejab."),
            ORDER(S, "Biz tabiatni asraymiz", x="Tabiatni asrash — hammamizning ishimiz."),
            Q("Qizil kitob nima uchun kerak?", "Kamyob jonzotlarni asrash uchun",
              ["Rasm chizish uchun", "Ov qilish uchun", "Ertak o‘qish uchun"], d=2,
              x="Qizil kitob qaysi jonzotlarni alohida asrash kerakligini ko‘rsatadi."),
            Q("Eski gazeta va daftarlardan nima qilinadi?", "Yangi qog‘oz", ["Shisha", "Temir", "Plastik"], d=2,
              x="Eski qog‘oz qayta ishlanib, yangi qog‘oz olinadi."),
            Q("Qaysi biri tabiatga zarar?", "Gulxanni o‘chirmay ketish",
              ["Daraxt ekish", "Axlatni qutiga tashlash", "Qushlarga yemlik osish"], d=2,
              x="O‘chirilmagan gulxandan yong‘in chiqishi mumkin."),
            Q("Uyda suvni qanday tejaymiz?", "Tish yuvganda jo‘mrakni yopamiz",
              ["Jo‘mrakni ochiq qoldiramiz", "Idishni oqar suvda uzoq chayamiz", "Suvni o‘ynab sachratamiz"], d=2,
              x="Kerak bo‘lmaganda jo‘mrakni yopib qo‘yamiz."),
            Q("Kamyob qush yoki hayvonni ko‘rsak nima qilamiz?", "Bezovta qilmay, kattalarga aytamiz",
              ["Tutib uyga olib kelamiz", "Tosh otamiz", "Qafasga solamiz"], d=2,
              x="Kamyob jonzotlarni tutmaymiz va qo‘rqitmaymiz."),
            Q("Eski kiyim va o‘yinchoqlarni nima qilgan yaxshi?", "Kerakli odamga beramiz",
              ["Ko‘chaga tashlaymiz", "Ariqqa tashlaymiz", "Yoqib yuboramiz"], d=2,
              x="Buyumdan qayta foydalansak, chiqindi kamayadi."),
            TF("Qo‘riqxonada daraxt kesish mumkin.", False, d=2, x="Qo‘riqxonada tabiat to‘liq qo‘riqlanadi."),
            MATCH("Chiqindini qutisi bilan juftlang",
                  [("Gazeta", "qog‘oz qutisi"), ("Plastik shisha", "plastik qutisi"), ("Shisha banka", "shisha qutisi"),
                   ("Olma po‘sti", "oziq-ovqat qoldig‘i")], d=2,
                  x="Chiqindi turiga qarab alohida qutiga tashlanadi."),
            Q("Sayrga qanday idishda suv olgan ma’qul?", "Qayta ishlatiladigan idishda",
              ["Har safar yangi plastik shishada", "Selofan paketda", "Bir martalik stakanda"], d=3,
              x="Bitta idishdan ko‘p marta foydalansak, plastik chiqindi kamayadi."),
            Q("Do‘konga qanday sumka bilan borgan yaxshi?", "Mato sumka bilan",
              ["Har safar yangi selofan paket bilan", "Bir nechta plastik paket bilan", "Bir martalik xalta bilan"], d=3,
              x="Mato sumka ko‘p yil xizmat qiladi, selofan paket esa tabiatni ifloslaydi."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["directions", "time", "health", "protect"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["phenomena", "water", "air", "soil", "plant_needs", "plant_forms", "crops_wild", "animal_food",
        "animal_winter", "uzbekistan", "directions", "time", "health", "protect"],
       chapter=C4, level=3)


# ------------------------------------------------------------ o'z tekshiruvimiz (imlo belgilari, emoji, soni)
def _new_emoji(cp):
    """Android 9 da yo'q yangi emoji (Emoji 11+) bloklari."""
    ranges = [(0x1F94D, 0x1F94F), (0x1F96C, 0x1F97F), (0x1F998, 0x1F9BF), (0x1F9C1, 0x1F9CF), (0x1F9E7, 0x1F9FF),
              (0x1FA00, 0x1FAFF), (0x1F7E0, 0x1F7EB), (0x1F6D5, 0x1F6DF), (0x1F6F9, 0x1F6FF), (0x1F90C, 0x1F90F),
              (0x1F93F, 0x1F93F), (0x1F971, 0x1F971)]
    return any(a <= cp <= b for a, b in ranges)


def _self_check():
    import re
    bad = []
    texts = []
    for t in T.topics:
        texts.append((t["id"], t["emoji"]))
        texts.append((t["id"], t.get("theory", {}).get("uz", "")))
        texts.append((t["id"], t["chapter"]))
    for it in T.items:
        for f in ("q", "a", "x", "h", "e"):
            if isinstance(it.get(f), str):
                texts.append((it["id"], it[f]))
        for w in it.get("w", []) + [s for p in it.get("pairs", []) for s in p] + it.get("parts", []):
            texts.append((it["id"], w))
    for key, s in texts:
        if re.search(r"['`ʻʼ]", s):
            bad.append(f"{key}: noto‘g‘ri apostrof: {s}")
        if re.search(r"(?<![oOgG])‘", s):
            bad.append(f"{key}: ‘ faqat o‘/g‘ da: {s}")
        if re.search(r"[oOgG]’", s):
            bad.append(f"{key}: o’/g’ (U+2019) — o‘/g‘ bo‘lishi kerak: {s}")
        for ch in s:
            if _new_emoji(ord(ch)):
                bad.append(f"{key}: yangi emoji {ch} (U+{ord(ch):X})")
    by = {}
    for it in T.items:
        by.setdefault(it["topic"], []).append(it)
        if it["t"] == "order" and not 3 <= len(it["parts"]) <= 7:
            bad.append(f"{it['id']}: ORDER 3–7 so‘zli bo‘lsin")
    for tid, its in by.items():
        if len(its) < 18 or sum(1 for i in its if i.get("d", 1) == 1) < 8:
            bad.append(f"{tid}: {len(its)} savol, d=1: {sum(1 for i in its if i.get('d', 1) == 1)}")
        nox = [i["id"] for i in its if not i.get("x")]
        if nox:
            bad.append(f"{tid}: izohsiz savollar: {nox}")
    if bad:
        raise SystemExit("\n".join(bad))


_self_check()
T.write()
