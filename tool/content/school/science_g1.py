"""Tabiiy fan, 1-sinf: assets/data/school/science_g1.json + bank_science_g1.json.

Mavzular O‘zbekiston maktab dasturi ("Tabiiy fan", 1-sinf) yo‘nalishida: men va tanam, sezgi a’zolari, gigiyena va
kun tartibi, tirik va jonsiz tabiat, yil fasllari, ob-havo, kun va tun, o‘simlik qismlari, mevalar va sabzavotlar,
uy va yovvoyi hayvonlar va ularning bolalari, qushlar, baliqlar, hasharotlar, yo‘l va uydagi xavfsizlik,
suvni va tabiatni asrash.

1-sinf o‘quvchisi (7 yosh) hali yaxshi o‘qiy olmaydi: savollar ovozda o‘qib beriladi, shuning uchun ular qisqa,
ko‘p javoblar — rasm (emoji). Emoji — faqat Android 9 da bor eski, oddiylari (pastda avtomatik tekshiriladi).
Hamma qoida matnlari va savollar o‘zimizniki (darslikdan ko‘chirilmagan), 3-sinf savollari takrorlanmaydi.
Qayta yaratish: python3 tool/content/school/science_g1.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("science", 1, L("Tabiiy fan", "Science", "Естествознание"))

C1 = "1-chorak. Men va atrofimdagi olam"
C2 = "2-chorak. Yil fasllari va ob-havo"
C3 = "3-chorak. O‘simliklar va hayvonlar"
C4 = "4-chorak. Xavfsizlik va tabiatni asrash"

# ============================================================ 1-chorak
T.topic("my_body", "👦", L("Mening tanam", "My body", "Моё тело"),
        chapter=C1,
        theory="Inson tanasi qismlari: bosh, bo‘yin, gavda, qo‘llar va oyoqlar.\n"
               "• Boshda ko‘z, quloq, burun va og‘iz bor.\n"
               "• Bizda 2 ta qo‘l va 2 ta oyoq bor. Har bir qo‘lda 5 tadan barmoq.\n"
               "• Qo‘l bilan ushlaymiz, yozamiz; oyoq bilan yuramiz, yuguramiz.\n"
               "Hamma odamlar bir-biriga o‘xshaydi, lekin har kim o‘ziga xos: bo‘yi, sochi, ko‘zining rangi har xil.",
        items=[
            Q("Bizda nechta qo‘l bor?", "2 ta", ["1 ta", "3 ta", "5 ta"], e="✋",
              x="Odamning 2 ta qo‘li bor: o‘ng qo‘l va chap qo‘l."),
            Q("Bir qo‘lda nechta barmoq bor?", "5 ta", ["3 ta", "4 ta", "10 ta"], e="🖐️",
              x="Har bir qo‘lda 5 tadan barmoq bor."),
            Q("Bizda nechta ko‘z bor?", "2 ta", ["1 ta", "3 ta", "4 ta"], e="👀",
              x="Odamning 2 ta ko‘zi bor."),
            Q("Bizda nechta burun bor?", "1 ta", ["2 ta", "3 ta", "4 ta"], e="👃",
              x="Yuzimizning o‘rtasida bitta burun bor."),
            Q("Biz nima bilan yuramiz?", "Oyoq bilan", ["Qo‘l bilan", "Quloq bilan", "Burun bilan"],
              x="Oyoqlar bilan yuramiz, yuguramiz va sakraymiz."),
            Q("Qalamni nima bilan ushlaymiz?", "Qo‘l bilan", ["Oyoq bilan", "Tizza bilan", "Quloq bilan"], e="✏️",
              x="Qo‘l barmoqlari bilan qalamni ushlab, yozamiz va rasm chizamiz."),
            Q("Ko‘z, quloq va burun qayerda?", "Boshda", ["Qo‘lda", "Oyoqda", "Qorinda"],
              x="Ko‘z, quloq, burun va og‘iz boshda joylashgan."),
            Q("Ovqatni nima bilan chaynaymiz?", "Tish bilan", ["Burun bilan", "Quloq bilan", "Barmoq bilan"], e="🦷",
              x="Ovqatni og‘izda tishlarimiz bilan chaynaymiz."),
            Q("Qaysi rasmda qo‘l bor?", "✋", ["👂", "👃", "👀"],
              x="✋ — bu qo‘l kafti va barmoqlar."),
            Q("Qaysi rasmda quloq bor?", "👂", ["✋", "👃", "👅"],
              x="👂 — bu quloq, u bilan eshitamiz."),
            TF("Odamning 2 ta oyog‘i bor.", True, x="Odamning 2 ta oyog‘i bor: o‘ng va chap."),
            TF("Odamning 3 ta qulog‘i bor.", False, e="👂", x="Odamning 2 ta qulog‘i bor: boshning ikki yonida."),
            TF("Yuzda ko‘z, burun va og‘iz bor.", True, x="Ko‘z, burun va og‘iz — yuzimizning qismlari."),
            Q("Ikki qo‘lda jami nechta barmoq bor?", "10 ta", ["5 ta", "8 ta", "12 ta"], d=2,
              x="Har qo‘lda 5 tadan: 5 + 5 = 10."),
            Q("Boshni gavda bilan nima tutashtiradi?", "Bo‘yin", ["Tizza", "Tirsak", "Barmoq"], d=2,
              x="Bo‘yin boshni gavdaga tutashtiradi, u bilan boshimizni buramiz."),
            Q("Tizza qayerda bo‘ladi?", "Oyoqda", ["Qo‘lda", "Boshda", "Bo‘yinda"], d=2,
              x="Tizza oyoqni bukishga yordam beradi."),
            Q("Tirsak qayerda bo‘ladi?", "Qo‘lda", ["Oyoqda", "Boshda", "Yuzda"], d=2,
              x="Tirsak qo‘lni bukishga yordam beradi."),
            Q("Qaysi biri ortiqcha: qo‘l, oyoq, bosh, to‘p?", "To‘p", ["Qo‘l", "Oyoq", "Bosh"], d=2,
              x="To‘p — o‘yinchoq, qolganlari tana qismlari."),
            Q("Bola o‘sganda nima o‘zgaradi?", "Bo‘yi uzayadi", ["Qo‘llari uchta bo‘ladi", "Burni ikkita bo‘ladi",
                                                                 "Ko‘zlari uchta bo‘ladi"], d=2,
              x="Bola o‘sib, bo‘yi uzayadi va kuchi ortadi."),
            TF("Hamma odamning sochi bir xil rangda.", False, d=2,
               x="Soch qora, sariq, jigarrang bo‘ladi — har xil."),
            TF("Yurak tinmay urib turadi.", True, d=2, e="❤️",
               x="Yurak kechasi ham, kunduzi ham, uxlaganimizda ham uradi."),
            MATCH("Tana qismini ishi bilan juftlang",
                  [("Oyoq", "yuguradi"), ("Qo‘l", "rasm chizadi"), ("Tish", "ovqatni chaynaydi"),
                   ("Bo‘yin", "boshni buradi"), ("Tizza", "oyoqni bukadi")], d=2,
                  x="Oyoq bilan yuguramiz, qo‘l bilan chizamiz, tish bilan chaynaymiz."),
            Q("Yurak tananing qayerida?", "Ko‘krakda", ["Boshda", "Oyoqda", "Qo‘lda"], d=3, e="❤️",
              x="Yurak ko‘krak ichida, sal chap tomonda urib turadi."),
            Q("Sut tishi tushgach, o‘rniga qanday tish chiqadi?", "Doimiy tish",
              ["Yana sut tishi", "Hech qanday tish", "Ikkita tish"], d=3, e="🦷",
              x="6–7 yoshda sut tishlari tushib, o‘rniga doimiy tishlar chiqadi. Ularni asrash kerak."),
        ])

T.topic("senses", "👀", L("Sezgi a’zolari", "The senses", "Органы чувств"),
        chapter=C1,
        theory="Atrofimizni 5 ta sezgi a’zosi bilan bilib olamiz:\n"
               "• ko‘z 👀 — ko‘ramiz; quloq 👂 — eshitamiz;\n"
               "• burun 👃 — hid bilamiz; til 👅 — ta’m bilamiz;\n"
               "• teri ✋ — issiq va sovuqni, qattiq va yumshoqni sezamiz.\n"
               "Ta’mlar: shirin (asal), nordon (limon), sho‘r (tuz), achchiq (qalampir).\n"
               "Sezgi a’zolarini asraymiz: ko‘zni ishqalamaymiz, quloqqa narsa tiqmaymiz.",
        items=[
            Q("Biz nima bilan ko‘ramiz?", "👀", ["👂", "👃", "👅"], x="Ko‘z bilan ko‘ramiz."),
            Q("Biz nima bilan eshitamiz?", "👂", ["👀", "👅", "✋"], x="Quloq bilan eshitamiz."),
            Q("Biz nima bilan hid bilamiz?", "👃", ["👂", "👀", "✋"], x="Burun bilan hid bilamiz."),
            Q("Biz nima bilan ta’m bilamiz?", "👅", ["👃", "👂", "👀"],
              x="Til shirin, nordon, sho‘r va achchiqni sezadi."),
            Q("Gulni hidlaganda qaysi a’zo ishlaydi?", "Burun", ["Quloq", "Tirsak", "Tizza"], e="🌷",
              x="Gulning hidini burun sezadi."),
            Q("Kamalak ranglarini nima bilan ko‘ramiz?", "Ko‘z bilan", ["Quloq bilan", "Burun bilan", "Til bilan"],
              e="🌈", x="Ranglarni ko‘z bilan ko‘ramiz."),
            Q("Mushukning miyovlashini nima bilan eshitamiz?", "Quloq bilan",
              ["Ko‘z bilan", "Til bilan", "Burun bilan"], e="🐱", x="Tovushlarni quloq eshitadi."),
            Q("Asalning shirinligini nima sezadi?", "Til", ["Quloq", "Ko‘z", "Soch"], e="🍯",
              x="Ta’mni til sezadi."),
            Q("Qorning sovuqligini nima sezadi?", "Teri", ["Quloq", "Ko‘z", "Burun"], e="❄️",
              x="Teri issiq va sovuqni sezadi."),
            Q("Limon qanday ta’mli?", "Nordon", ["Shirin", "Sho‘r", "Achchiq"], e="🍋",
              x="Limon nordon bo‘ladi."),
            Q("Shakar qanday ta’mli?", "Shirin", ["Nordon", "Sho‘r", "Achchiq"],
              x="Shakar va asal shirin bo‘ladi."),
            TF("Biz quloq bilan ko‘ramiz.", False, x="Biz ko‘z bilan ko‘ramiz, quloq bilan esa eshitamiz."),
            TF("Burun hidlarni sezadi.", True, e="👃", x="Burun — hid bilish a’zosi."),
            TF("Teri issiq va sovuqni sezadi.", True, x="Teri issiq-sovuqni, qattiq-yumshoqni sezadi."),
            TF("Til ta’mni sezadi.", True, e="👅", x="Til — ta’m bilish a’zosi."),
            MATCH("A’zoni sezgisi bilan juftlang",
                  [("👀 ko‘z", "ko‘rish"), ("👂 quloq", "eshitish"), ("👃 burun", "hid bilish"),
                   ("👅 til", "ta’m bilish"), ("✋ teri", "sezish")],
                  x="Ko‘z — ko‘rish, quloq — eshitish, burun — hid, til — ta’m, teri — sezish."),
            Q("Tuz qanday ta’mli?", "Sho‘r", ["Shirin", "Nordon", "Achchiq"], d=2,
              x="Tuz sho‘r bo‘ladi."),
            Q("Qalampir qanday ta’mli?", "Achchiq", ["Shirin", "Sho‘r", "Nordon"], d=2, e="🌶️",
              x="Qalampir achchiq bo‘ladi, u tilni achishtiradi."),
            Q("Sezgi a’zolari jami nechta?", "5 ta", ["2 ta", "3 ta", "10 ta"], d=2,
              x="Ko‘z, quloq, burun, til va teri — 5 ta."),
            Q("Ko‘zga nima zarar?", "Telefonga uzoq qarash",
              ["Yashil daraxtlarga qarash", "Yorug‘da o‘qish", "Ko‘zni yumib dam olish"], d=2,
              x="Ekranga uzoq qarash ko‘zni charchatadi."),
            Q("Quloqni asrash uchun nima qilamiz?", "Qattiq shovqindan saqlanamiz",
              ["Quloqqa cho‘p tiqamiz", "Juda baland musiqa tinglaymiz", "Quloqqa qichqiramiz"], d=2,
              x="Qattiq shovqin quloqqa zarar qiladi."),
            Q("Ko‘zga chang tushsa nima qilamiz?", "Toza suv bilan yuvamiz",
              ["Qattiq ishqalaymiz", "Kir qo‘l bilan ushlaymiz", "E’tibor bermaymiz"], d=2,
              x="Ko‘zni ishqalamaymiz: toza suv bilan yuvib, kattalarga aytamiz."),
            MATCH("Nimani qaysi a’zo sezadi?",
                  [("Qo‘ng‘iroq ovozi", "quloq"), ("Non hidi", "burun"), ("Olma ta’mi", "til"),
                   ("Kitobdagi rasm", "ko‘z"), ("Mushukning yumshoq juni", "teri")], d=2,
                  x="Ovozni quloq, hidni burun, ta’mni til, rasmni ko‘z, yumshoqlikni teri sezadi."),
            Q("Ko‘zni yumsak, nima qila olmaymiz?", "Ko‘ra olmaymiz",
              ["Eshita olmaymiz", "Hid bila olmaymiz", "Ta’m bila olmaymiz"], d=3,
              x="Ko‘z yumilsa, ko‘rmaymiz, lekin eshitish, hid va ta’m bilish ishlayveradi."),
            Q("Ko‘zi bog‘langan bola olmani qanday taniydi?", "Hidi va ta’midan",
              ["Rangidan", "Ovozidan", "Soyasidan"], d=3, e="🍎",
              x="Rangni ko‘rmaydi, lekin burun va til olmani tanib oladi."),
        ])

T.topic("hygiene", "🚿", L("Gigiyena va kun tartibi", "Hygiene and daily routine", "Гигиена и режим дня"),
        chapter=C1,
        theory="Toza bola — sog‘lom bola.\n"
               "• Ovqatdan oldin va ko‘chadan kelgach qo‘lni sovun bilan yuvamiz.\n"
               "• Tishni kuniga 2 marta tozalaymiz: ertalab va kechasi uxlashdan oldin.\n"
               "• Tish cho‘tkasi, sochiq, taroq — har kimniki alohida.\n"
               "Kun tartibi: ertalab turamiz, badantarbiya qilamiz, yuvinamiz, nonushta qilamiz, maktabga boramiz.\n"
               "Kechqurun vaqtida uxlaymiz — yaxshi uxlagan bola darsda charchamaydi.",
        items=[
            Q("Ovqatdan oldin nima qilamiz?", "Qo‘l yuvamiz", ["Yugurib o‘ynaymiz", "Uxlaymiz", "Rasm chizamiz"],
              e="✋", x="Ovqatdan oldin qo‘lni sovun bilan yuvamiz."),
            Q("Qo‘lni nima bilan yuvamiz?", "Sovun va suv bilan", ["Faqat sochiq bilan", "Qum bilan", "Qog‘oz bilan"],
              e="💧", x="Sovun kir va mikroblarni yuvib ketadi."),
            Q("Tishni kuniga necha marta tozalaymiz?", "2 marta", ["Haftada 1 marta", "Oyda 1 marta", "Hech qachon"],
              e="🦷", x="Tishni kuniga 2 marta — ertalab va kechqurun tozalaymiz."),
            Q("Uxlashdan oldin nima qilamiz?", "Tishni tozalaymiz",
              ["Shirinlik yeymiz", "Ko‘chaga chiqamiz", "Telefonda o‘ynaymiz"],
              x="Uxlashdan oldin tishni tozalasak, tishlar sog‘lom bo‘ladi."),
            Q("Kimning tish cho‘tkasidan foydalanamiz?", "Faqat o‘zimiznikidan",
              ["Akamnikidan", "Do‘stimnikidan", "Kimniki bo‘lsa ham"],
              x="Tish cho‘tkasi, sochiq va taroq — har kimniki alohida."),
            Q("Ko‘chadan kelgach nima qilamiz?", "Qo‘limizni yuvamiz",
              ["Darhol non olamiz", "Qo‘limizni yalaymiz", "Ko‘zimizni ishqalaymiz"],
              x="Ko‘chada qo‘lga chang va mikrob yuqadi, uni yuvamiz."),
            Q("Mevani yeyishdan oldin nima qilamiz?", "Yuvamiz", ["Yerga tashlaymiz", "Changga belaymiz", "Tuzlaymiz"],
              e="🍎", x="Meva va sabzavotni yuvib yeymiz."),
            Q("Ertalab turgach nima qilamiz?", "Yuvinamiz", ["Yana yotib olamiz", "Darsga kechikamiz", "Kechki ovqat yeymiz"],
              x="Ertalab yuz-qo‘limizni yuvib, tishimizni tozalaymiz."),
            TF("Tirnoqlarni vaqtida olib turish kerak.", True,
               x="Uzun tirnoq ostida kir va mikroblar to‘planadi."),
            TF("Tish cho‘tkasini do‘st bilan almashib ishlatsa bo‘ladi.", False,
               x="Tish cho‘tkasi har kimniki alohida bo‘ladi."),
            TF("Ovqatdan oldin qo‘l yuvish shart emas.", False,
               x="Ovqatdan oldin qo‘l yuvish shart, aks holda mikroblar og‘izga tushadi."),
            TF("Badantarbiya tanani baquvvat qiladi.", True,
               x="Ertalabki badantarbiya tanani uyg‘otadi va kuchli qiladi."),
            Q("Kir qo‘lda nima bo‘lishi mumkin?", "Mikroblar", ["Vitaminlar", "Gullar", "Yulduzlar"], d=2,
              x="Mikroblar ko‘zga ko‘rinmaydi, ular kasallik tarqatadi."),
            Q("Kun tartibiga amal qilgan bola nima qiladi?", "Hamma ishga ulguradi",
              ["Darsga kechikadi", "Kech yotadi", "Nonushta qilmaydi"], d=2,
              x="Kun tartibi bo‘lsa, o‘qishga ham, o‘yinga ham, dam olishga ham vaqt yetadi."),
            Q("Kichik o‘quvchi kechasi qancha uxlashi kerak?", "10 soatga yaqin",
              ["1 soat", "3 soat", "20 soat"], d=2,
              x="Kichik maktab o‘quvchisiga kechasi taxminan 10 soat uyqu kerak."),
            Q("Aksirganda nima qilamiz?", "Og‘izni ro‘molcha bilan to‘samiz",
              ["Odamlarga qarab aksiramiz", "Ovqat ustiga aksiramiz", "Qo‘limizni yalaymiz"], d=2,
              x="Shunda mikroblar boshqalarga yuqmaydi."),
            Q("Cho‘milgach badanni nima bilan artamiz?", "O‘z sochig‘imiz bilan",
              ["Do‘stimizning sochig‘i bilan", "Gazeta bilan", "Parda bilan"], d=2, e="🛁",
              x="Har kim faqat o‘z sochig‘idan foydalanadi."),
            MATCH("Buyumni ishi bilan juftlang",
                  [("Sovun", "qo‘l yuvish"), ("Tish cho‘tkasi", "tish tozalash"), ("Taroq", "soch tarash"),
                   ("Sochiq", "artinish"), ("Ro‘molcha", "burun artish")], d=2,
                  x="Har bir gigiyena buyumining o‘z vazifasi bor."),
            TF("Tishni faqat ertalab tozalash yetarli.", False, d=2,
               x="Tishni ertalab va kechqurun — kuniga 2 marta tozalaymiz."),
            Q("Darsdan keyin nima qilish foydali?", "Toza havoda o‘ynash",
              ["Kun bo‘yi telefon o‘ynash", "Tushlik qilmaslik", "Hech harakat qilmaslik"], d=2,
              x="Toza havoda harakat qilish tanaga kuch beradi."),
            Q("Qaysi tartib to‘g‘ri?", "Turish, yuvinish, nonushta",
              ["Nonushta, turish, yuvinish", "Yuvinish, uxlash, turish", "Nonushta, uxlash, turish"], d=3,
              x="Avval turamiz, keyin yuvinamiz, so‘ng nonushta qilamiz."),
            TF("Kech yotgan bola ertalab charchab turadi.", True, d=3,
               x="Yaxshi uxlamasa, bola darsda charchaydi va diqqatini jamlay olmaydi."),
        ])

T.topic("living", "🌳", L("Tirik va jonsiz tabiat", "Living and non-living nature", "Живая и неживая природа"),
        chapter=C1,
        theory="Atrofimizda tabiat va inson yasagan narsalar bor.\n"
               "• Tabiat — uni odam yasamagan: quyosh, suv, tosh, daraxt, qush, baliq.\n"
               "• Inson yasagan narsalar: uy, mashina, stol, kitob.\n"
               "Tabiat ikki xil:\n"
               "• tirik tabiat — o‘simliklar, hayvonlar, odamlar: ular nafas oladi, oziqlanadi, o‘sadi;\n"
               "• jonsiz tabiat — quyosh, suv, havo, tosh, qum: ular o‘smaydi va nafas olmaydi.",
        items=[
            Q("Qaysi biri tirik?", "🐶", ["⭐", "💧", "🏠"], x="It nafas oladi, ovqat yeydi, o‘sadi — u tirik."),
            Q("Qaysi biri tirik?", "🌳", ["🚗", "🌙", "⛄"], x="Daraxt o‘sadi, suv ichadi — u tirik."),
            Q("Qaysi biri jonsiz tabiat?", "Tosh", ["Mushuk", "Gul", "Chumchuq"],
              x="Tosh o‘smaydi va nafas olmaydi — u jonsiz."),
            Q("Qaysi biri jonsiz tabiat?", "💧", ["🐟", "🌷", "🐝"], x="Suv tabiatda bor, lekin u jonsiz."),
            Q("Qaysi narsani inson yasagan?", "🚗", ["🌳", "🌞", "🐦"], x="Mashinani odamlar zavodda yasaydi."),
            Q("Qaysi narsani inson yasagan?", "🏠", ["⭐", "🐄", "🌷"], x="Uyni quruvchilar quradi."),
            Q("Qaysi biri tabiat?", "Daryo", ["Stol", "Velosiped", "Qalam"],
              x="Daryoni hech kim yasamagan — u tabiat."),
            Q("Tirik narsalar nima qiladi?", "O‘sadi", ["Sinadi", "Eriydi", "Zanglaydi"],
              x="Tiriklar o‘sadi, oziqlanadi va nafas oladi."),
            Q("Qaysi biri o‘sadi?", "Kuchukcha", ["Tosh", "Koptok", "Qoshiq"], e="🐶",
              x="Kuchukcha o‘sib, katta it bo‘ladi."),
            TF("Gul — tirik.", True, e="🌷", x="Gul o‘sadi, suv ichadi va ochiladi — u tirik."),
            TF("Quyosh — tirik.", False, e="🌞", x="Quyosh jonsiz tabiatga kiradi, u nafas olmaydi."),
            TF("Odam ham tirik tabiatga kiradi.", True, x="Odam nafas oladi, oziqlanadi, o‘sadi."),
            TF("Tosh o‘sib kattalashadi.", False, x="Tosh — jonsiz, u o‘smaydi."),
            TF("Mashinani tabiat yaratgan.", False, e="🚗", x="Mashinani odamlar yasagan."),
            TF("O‘simliklarga ham suv kerak.", True, e="🌱", x="O‘simliklar ham tirik, ularga suv kerak."),
            Q("Qaysi biri ortiqcha: it, mushuk, tosh, sigir?", "Tosh", ["It", "Mushuk", "Sigir"], d=2,
              x="Tosh — jonsiz, qolganlari tirik hayvonlar."),
            Q("Qaysi biri ortiqcha: suv, havo, tosh, qush?", "Qush", ["Suv", "Havo", "Tosh"], d=2,
              x="Qush — tirik, qolganlari jonsiz tabiat."),
            Q("Tiriklarga nima kerak?", "Suv va ovqat", ["Faqat tosh", "Faqat qum", "Faqat shovqin"], d=2,
              x="Hamma tirik narsalarga suv va oziq kerak."),
            Q("Bulut tirikmi?", "Yo‘q, jonsiz", ["Ha, u hayvon", "Ha, u o‘simlik", "Ha, u odam"], d=2, e="☁️",
              x="Bulut — suv tomchilari, u jonsiz."),
            TF("Kitobni inson yasagan.", True, d=2, e="📖", x="Kitobni odamlar yozadi va bosmaxonada chop etadi."),
            Q("Jo‘ja nima qiladi, tosh qilmaydi?", "O‘sib tovuq bo‘ladi",
              ["Hech o‘zgarmaydi", "Eriydi", "Sinib ketadi"], d=2, e="🐤",
              x="Jo‘ja tirik, u o‘sadi. Tosh esa o‘smaydi."),
            Q("Qaysi guruhda hammasi tirik?", "🐱 🌷 🐟", ["🐱 ⭐ 🐟", "🌷 💧 🐝", "🏠 🌳 🐦"], d=3,
              x="Mushuk, gul va baliq — uchalasi ham tirik."),
            Q("Qaysi guruhda hammasi jonsiz?", "⭐ 💧 🌙", ["⭐ 🐦 🌙", "🌳 💧 🌞", "🐟 ❄️ 🌙"], d=3,
              x="Yulduz, suv va Oy — jonsiz tabiat."),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["my_body", "senses", "hygiene", "living"], chapter=C1)

# ============================================================ 2-chorak
T.topic("seasons", "🍂", L("Yil fasllari", "Seasons of the year", "Времена года"),
        chapter=C2,
        theory="Bir yilda 4 ta fasl bor: kuz, qish, bahor, yoz.\n"
               "• Kuz 🍂: barglar sarg‘ayib to‘kiladi, hosil yig‘iladi, qushlar issiq o‘lkalarga uchib ketadi.\n"
               "• Qish ❄️: sovuq, qor yog‘adi, kunlar qisqa.\n"
               "• Bahor 🌷: havo iliydi, qor eriydi, daraxtlar gullaydi, qushlar qaytib keladi.\n"
               "• Yoz 🌞: issiq, kunlar uzun, mevalar pishadi.\n"
               "Fasllar har yili shu tartibda almashinadi.",
        items=[
            Q("Bir yilda nechta fasl bor?", "4 ta", ["2 ta", "3 ta", "7 ta"],
              x="Kuz, qish, bahor va yoz — 4 ta fasl."),
            Q("Qaysi fasl eng sovuq?", "Qish", ["Yoz", "Bahor", "Kuz"], e="⛄",
              x="Qish — eng sovuq fasl, qor yog‘adi."),
            Q("Qaysi fasl eng issiq?", "Yoz", ["Qish", "Bahor", "Kuz"], e="🌞",
              x="Yoz — eng issiq fasl."),
            Q("Barglar sarg‘ayib to‘kiladigan fasl qaysi?", "Kuz", ["Yoz", "Bahor", "Qish"], e="🍂",
              x="Kuzda barglar sarg‘ayadi va to‘kiladi."),
            Q("Mevali daraxtlar qaysi faslda gullaydi?", "Bahorda", ["Kuzda", "Qishda", "Yozning oxirida"], e="🌸",
              x="Bahorda o‘rik, olma, gilos daraxtlari gullaydi."),
            Q("Qaysi rasm qishga mos?", "⛄", ["🌷", "🍂", "🏖️"], x="Qishda qordan odam yasaymiz."),
            Q("Qaysi rasm bahorga mos?", "🌷", ["⛄", "🍂", "❄️"], x="Bahorda lolalar ochiladi."),
            Q("Qaysi rasm kuzga mos?", "🍂", ["🌷", "⛄", "🏖️"], x="Kuzda barglar to‘kiladi."),
            Q("Qaysi rasm yozga mos?", "🏖️", ["⛄", "🍂", "❄️"], x="Yozda issiq, odamlar suv bo‘yida dam oladi."),
            Q("Qishdan keyin qaysi fasl keladi?", "Bahor", ["Yoz", "Kuz", "Yana qish"],
              x="Qish tugagach, bahor keladi."),
            Q("Yozdan keyin qaysi fasl keladi?", "Kuz", ["Bahor", "Qish", "Yana yoz"],
              x="Yoz tugagach, kuz keladi."),
            Q("Qishda nima kiyamiz?", "Issiq kurtka", ["Kalta shim", "Yengil mayka", "Shippak"], e="❄️",
              x="Qishda sovuq, issiq kiyinamiz."),
            Q("Yozda qanday kiyinamiz?", "Yengil kiyinamiz", ["Po‘stin kiyamiz", "Qo‘lqop taqamiz", "Telpak kiyamiz"],
              e="🌞", x="Yozda issiq, yengil kiyim kiyamiz."),
            TF("Bahorda qor eriydi.", True, x="Bahorda havo iliydi va qor eriydi."),
            TF("Yoz — eng sovuq fasl.", False, x="Yoz — eng issiq fasl, eng sovuq fasl — qish."),
            TF("Kuzda hosil yig‘iladi.", True, x="Kuzda dalalarda va bog‘larda hosil yig‘iladi."),
            Q("Kuzdan keyin qaysi fasl keladi?", "Qish", ["Yoz", "Bahor", "Yana kuz"], d=2,
              x="Kuz tugagach, qish keladi."),
            Q("Bahordan keyin qaysi fasl keladi?", "Yoz", ["Qish", "Kuz", "Yana bahor"], d=2,
              x="Bahor tugagach, yoz keladi."),
            Q("Navro‘z bayrami qaysi faslda?", "Bahorda", ["Qishda", "Yozda", "Kuzda"], d=2,
              x="Navro‘z 21-martda — bahorda nishonlanadi."),
            Q("Yangi yil qaysi faslda keladi?", "Qishda", ["Yozda", "Bahorda", "Kuzda"], d=2,
              x="Yangi yil 1-yanvarda — qishda keladi."),
            TF("Qushlar bahorda issiq o‘lkalardan qaytib keladi.", True, d=2,
               x="Kuzda uchib ketgan laylak va qaldirg‘ochlar bahorda qaytadi."),
            MATCH("Faslni belgisi bilan juftlang",
                  [("Qish", "qor yog‘adi"), ("Bahor", "daraxtlar gullaydi"), ("Yoz", "eng issiq"),
                   ("Kuz", "barglar to‘kiladi")], d=2,
                  x="Qishda qor, bahorda gul, yozda issiq, kuzda xazon."),
            Q("Qaysi faslda kunlar eng uzun?", "Yozda", ["Qishda", "Kuzda", "Bahorda"], d=3,
              x="Yozda Quyosh erta chiqib, kech botadi."),
            Q("Qaysi faslda kunlar eng qisqa?", "Qishda", ["Yozda", "Bahorda", "Kuzda"], d=3,
              x="Qishda Quyosh kech chiqib, erta botadi."),
            Q("Erta bahorda birinchilardan ochiladigan gul?", "Boychechak", ["Kungaboqar", "Atirgul", "G‘o‘za guli"], d=3,
              x="Boychechak erta bahorda, qor endi eriganda ochiladi."),
            Q("Kuzda qaysi meva pishadi?", "Anor", ["Gilos", "O‘rik", "Tut"], d=3,
              x="Anor kuzda pishadi, gilos, o‘rik va tut esa yoz boshida."),
        ])

T.topic("weather", "🌦️", L("Ob-havo", "Weather", "Погода"),
        chapter=C2,
        theory="Ob-havo — hozir tashqarida havo qanday ekani.\n"
               "• Kun quyoshli, bulutli, yomg‘irli, qorli yoki shamolli bo‘ladi.\n"
               "• Havo issiq yoki sovuq bo‘ladi. Buni termometr ko‘rsatadi.\n"
               "• Yomg‘irda soyabon olamiz, sovuqda issiq kiyinamiz.\n"
               "Ob-havo har kuni o‘zgarib turadi.",
        items=[
            Q("Yomg‘ir yog‘yapti. Ko‘chaga nima olamiz?", "Soyabon", ["Quyosh ko‘zoynagi", "Chana", "Varrak"], e="🌧️",
              x="Soyabon bizni yomg‘irdan saqlaydi."),
            Q("Qaysi rasm yomg‘irli kunni ko‘rsatadi?", "🌧️", ["☀️", "❄️", "⛄"], x="🌧️ — bulutdan yomg‘ir yog‘yapti."),
            Q("Qaysi rasm qorli kunni ko‘rsatadi?", "❄️", ["☀️", "🌧️", "🌈"], x="❄️ — qor parchasi."),
            Q("Qaysi rasm quyoshli kunni ko‘rsatadi?", "☀️", ["🌧️", "❄️", "☁️"], x="☀️ — charaqlagan Quyosh."),
            Q("Havo issiq yoki sovuqligini nima ko‘rsatadi?", "Termometr", ["Soat", "Chizg‘ich", "Tarozi"], e="🌡️",
              x="Termometr havo qanchalik issiq yoki sovuqligini ko‘rsatadi."),
            Q("Yomg‘ir nimadan yog‘adi?", "Bulutdan", ["Quyoshdan", "Oydan", "Daraxtdan"], e="☁️",
              x="Yomg‘ir bulutdan yog‘adi."),
            Q("Yomg‘irdan keyin quyosh chiqsa, osmonda nima ko‘rinadi?", "Kamalak", ["Oy", "Yulduzlar", "Qor"], e="🌈",
              x="Quyosh nuri yomg‘ir tomchilaridan o‘tib, kamalak hosil qiladi."),
            Q("Qorli kunda nima o‘ynaymiz?", "Qordan odam yasaymiz",
              ["Daryoda cho‘milamiz", "Quyoshda toblanamiz", "Qovun uzamiz"], e="⛄",
              x="Qishda qor yog‘sa, qordan odam yasaymiz, chana uchamiz."),
            Q("Issiq quyoshli kunda boshga nima kiyamiz?", "Yengil kepka", ["Qalin telpak", "Qo‘lqop", "Sharf"],
              e="☀️", x="Yengil bosh kiyim boshni quyosh urishidan saqlaydi."),
            TF("Ob-havo har kuni bir xil bo‘ladi.", False, x="Ob-havo o‘zgarib turadi: bugun quyoshli, ertaga yomg‘irli."),
            TF("Sovuq kunda issiq kiyinish kerak.", True, x="Issiq kiyim bizni sovuqdan saqlaydi."),
            TF("Yomg‘ir bulutdan yog‘adi.", True, e="🌧️", x="Bulut — mayda suv tomchilari, ulardan yomg‘ir yog‘adi."),
            Q("Daraxt shoxlari tebranyapti. Tashqarida nima bor?", "Shamol", ["Qor", "Tuman", "Kamalak"], d=2, e="🌳",
              x="Shamol daraxt shoxlarini tebratadi."),
            Q("Yer ho‘l, ko‘lmaklar bor. Nima bo‘lgan?", "Yomg‘ir yoqqan",
              ["Shamol esgan", "Qattiq ayoz bo‘lgan", "Kun quruq va issiq bo‘lgan"], d=2,
              x="Yomg‘irdan keyin yer ho‘l bo‘ladi, ko‘lmaklar paydo bo‘ladi."),
            Q("Ayoz nima?", "Qattiq sovuq", ["Kuchli issiq", "Kuchli yomg‘ir", "Kamalak"], d=2,
              x="Ayoz — qishdagi qattiq sovuq."),
            Q("Yomg‘irda oyoqqa nima kiyamiz?", "Rezina etik", ["Shippak", "Sandal", "Hech narsa"], d=2,
              x="Rezina etik suv o‘tkazmaydi, oyoq quruq qoladi."),
            Q("Qora bulutlar osmonni qopladi. Nima bo‘lishi mumkin?", "Yomg‘ir yog‘adi",
              ["Osmon tiniq bo‘ladi", "Yulduzlar ko‘rinadi", "Quyosh charaqlaydi"], d=2,
              x="Qora bulutlar yomg‘ir yog‘ishidan darak beradi."),
            TF("Termometr havoning issiq yoki sovuqligini ko‘rsatadi.", True, d=2, e="🌡️",
               x="Termometr — harorat o‘lchaydigan asbob."),
            TF("Yozda ham yomg‘ir yog‘ishi mumkin.", True, d=2,
               x="Yozda ham ba’zan yomg‘ir yog‘adi."),
            MATCH("Ob-havoga mos buyumni toping",
                  [("Yomg‘ir", "soyabon"), ("Qor", "chana"), ("Issiq quyosh", "kepka"), ("Shamol", "varrak")], d=2,
                  x="Yomg‘irda soyabon, qorda chana, issiqda kepka, shamolda varrak."),
            Q("Juda kuchli shamol nima deyiladi?", "Bo‘ron", ["Shabada", "Kamalak", "Shudring"], d=3,
              x="Juda kuchli shamol — bo‘ron, yengil shamol — shabada."),
            Q("Tuman tushganda nima bo‘ladi?", "Uzoq ko‘rinmaydi",
              ["Havo juda issiq bo‘ladi", "Kamalak chiqadi", "Qor eriydi"], d=3,
              x="Tumanda havoda mayda suv tomchilari ko‘p, uzoqdagi narsalar ko‘rinmaydi."),
            Q("Chaqmoq chaqsa, qayerda turamiz?", "Uy ichida", ["Baland daraxt tagida", "Ochiq dalada", "Suv ichida"],
              d=3, x="Momaqaldiroqda daraxt tagida va ochiq joyda turish xavfli, uyga kiramiz."),
        ])

T.topic("day_night", "🌙", L("Kun va tun, Quyosh va Oy", "Day and night, the Sun and the Moon", "День и ночь, Солнце и Луна"),
        chapter=C2,
        theory="Sutka kunduz va tundan iborat.\n"
               "• Kunduzi Quyosh charaqlaydi: atrof yorug‘ va iliq.\n"
               "• Kechasi osmonda Oy va yulduzlar ko‘rinadi, atrof qorong‘i.\n"
               "• Kun qismlari: ertalab, kunduzi, kechqurun, kechasi.\n"
               "Quyosh — juda katta va issiq yulduz. Oy o‘zi nur sochmaydi, Quyosh nurida yarqiraydi.\n"
               "Quyoshga tik qaramaymiz — ko‘zga zarar!",
        items=[
            Q("Kunduzi osmonda nima charaqlaydi?", "🌞", ["🌙", "⭐", "🌈"],
              x="Kunduzi osmonda Quyosh charaqlaydi."),
            Q("Kechasi osmonda nima ko‘rinadi?", "🌙", ["🌞", "🌈", "🍂"], x="Kechasi Oy va yulduzlar ko‘rinadi."),
            Q("Yulduzlarni qachon ko‘ramiz?", "Kechasi", ["Kunduzi", "Tushda", "Ertalab"],
              x="Yulduzlar kechasi, qorong‘ida ko‘rinadi."),
            Q("Quyosh chiqqanda nima boshlanadi?", "Tong", ["Tun", "Yarim kecha", "Kechqurun"],
              x="Quyosh chiqqanda tong otadi."),
            Q("Quyosh botgach nima bo‘ladi?", "Qorong‘i tushadi",
              ["Tong otadi", "Kun yorishadi", "Quyosh yana chiqadi"],
              x="Quyosh botgach asta-sekin qorong‘i tushadi."),
            Q("Kechasi nima qilamiz?", "Uxlaymiz", ["Maktabga boramiz", "Nonushta qilamiz", "Quyoshda toblanamiz"],
              x="Kechasi uxlab, dam olamiz."),
            Q("Ertalab nima qilamiz?", "Uyg‘onamiz", ["Uyquga yotamiz", "Kechki ovqat yeymiz", "Yulduz sanaymiz"],
              x="Ertalab uyg‘onib, maktabga tayyorlanamiz."),
            Q("Bizga yorug‘lik va issiqlikni nima beradi?", "Quyosh", ["Oy", "Bulut", "Shamol"], e="🌞",
              x="Quyosh Yerni yoritadi va isitadi."),
            Q("Qaysi rasm tunga mos?", "🌃", ["🏖️", "🌻", "🌈"], x="🌃 — yulduzli tun."),
            Q("Qaysi rasm tongga mos?", "🌅", ["🌃", "🌙", "⭐"], x="🌅 — Quyosh chiqyapti, tong otyapti."),
            TF("Oy kechasi osmonda ko‘rinadi.", True, e="🌙", x="Kechasi osmonda Oy ko‘rinadi."),
            TF("Quyoshga tik qarash ko‘zga zarar.", True, x="Quyosh nuri juda kuchli, u ko‘zni shikastlaydi."),
            TF("Yulduzlar kunduzi charaqlab ko‘rinadi.", False,
               x="Kunduzi Quyosh juda yorug‘, shuning uchun yulduzlar ko‘rinmaydi."),
            Q("Kunning nechta qismi bor?", "4 ta", ["2 ta", "7 ta", "10 ta"], d=2,
              x="Ertalab, kunduzi, kechqurun va kechasi — 4 ta."),
            Q("Quyosh qanday?", "Juda katta va issiq", ["Kichik va sovuq", "Muzdan iborat", "Yerdan kichik"], d=2,
              x="Quyosh Yerdan juda katta va juda issiq."),
            Q("Quyosh nima?", "Yulduz", ["Bulut", "Oy", "Tosh"], d=2,
              x="Quyosh — bizga eng yaqin yulduz."),
            Q("Tushlikni kunning qaysi qismida qilamiz?", "Kunduzi", ["Kechasi", "Tongda", "Yarim kechada"], d=2,
              x="Tushlik — kunduzgi ovqat."),
            TF("Oy o‘zi nur sochadi.", False, d=2,
               x="Oy Quyosh nurini qaytaradi, shuning uchun yarqirab ko‘rinadi."),
            MATCH("Kun qismini ishi bilan juftlang",
                  [("Ertalab", "nonushta"), ("Kunduzi", "tushlik"), ("Kechqurun", "kechki ovqat"), ("Kechasi", "uyqu")],
                  d=2, x="Ertalab nonushta, kunduzi tushlik, kechqurun kechki ovqat, kechasi uyqu."),
            Q("Kun qismlari to‘g‘ri tartibda qaysi?", "Ertalab, kunduzi, kechqurun, kechasi",
              ["Kechasi, kunduzi, ertalab, kechqurun", "Kunduzi, ertalab, kechasi, kechqurun",
               "Kechqurun, ertalab, kechasi, kunduzi"], d=3,
              x="Ertalabdan keyin kunduz, keyin kechqurun, so‘ng kecha keladi."),
            TF("Oy har kecha bir xil ko‘rinmaydi.", True, d=3, e="🌙",
               x="Oy goh to‘lin (yumaloq), goh o‘roqsimon bo‘lib ko‘rinadi."),
            Q("Quyosh bo‘lmasa, Yerda qanday bo‘lardi?", "Doim qorong‘i va sovuq",
              ["Doim yorug‘ va issiq", "Hech narsa o‘zgarmasdi", "Gullar ko‘payardi"], d=3,
              x="Yorug‘lik va issiqlikni Quyosh beradi."),
            Q("Odamlar Oyga nimada uchib borgan?", "Raketada", ["Samolyotda", "Havo sharida", "Poyezdda"], d=3, e="🚀",
              x="Oyga faqat raketa va kosmik kemada uchib borish mumkin."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["seasons", "weather", "day_night"], chapter=C2)

# ============================================================ 3-chorak
T.topic("plants", "🌱", L("O‘simlik qismlari", "Parts of a plant", "Части растения"),
        chapter=C3,
        theory="O‘simlikning qismlari: ildiz, poya, barg, gul va meva.\n"
               "• Ildiz yer ostida bo‘ladi: suv ichadi va o‘simlikni ushlab turadi.\n"
               "• Poya barg va gullarni ko‘tarib turadi. Daraxtning poyasi — tana.\n"
               "• Barglar ko‘pincha yashil bo‘ladi.\n"
               "• Guldan meva hosil bo‘ladi, meva ichida urug‘ bor.\n"
               "Urug‘ ekilsa, undan yangi o‘simlik unib chiqadi.",
        items=[
            Q("O‘simlikning qaysi qismi yer ostida?", "Ildiz", ["Barg", "Gul", "Meva"],
              x="Ildiz yer ostida o‘sadi."),
            Q("O‘simlik qaysi qismi bilan suv ichadi?", "Ildizi bilan", ["Guli bilan", "Mevasi bilan", "Urug‘i bilan"],
              x="Ildiz tuproqdan suv ichadi."),
            Q("Barglar ko‘pincha qanday rangda?", "Yashil", ["Ko‘k", "Qora", "Binafsha"], e="🍃",
              x="Ko‘pchilik barglar yashil bo‘ladi."),
            Q("Olma o‘simlikning qaysi qismi?", "Meva", ["Ildiz", "Barg", "Poya"], e="🍎",
              x="Olma — olma daraxtining mevasi."),
            Q("Urug‘ ekilsa, nima o‘sib chiqadi?", "Yangi o‘simlik", ["Tosh", "Qush", "Baliq"], e="🌱",
              x="Urug‘dan yangi o‘simlik unib chiqadi."),
            Q("Gulni nima ko‘tarib turadi?", "Poya", ["Ildiz", "Urug‘", "Tuproq"], e="🌷",
              x="Poya barg va gullarni ko‘tarib turadi."),
            Q("Olma urug‘ini qayerdan topamiz?", "Olmaning ichidan", ["Bargidan", "Ildizidan", "Shoxidan"], e="🍎",
              x="Urug‘lar mevaning ichida bo‘ladi."),
            Q("Qaysi biri gul?", "🌷", ["🍎", "🍃", "🌳"], x="🌷 — lola guli."),
            Q("Qaysi biri daraxt?", "🌳", ["🌷", "🌻", "🍄"], x="🌳 — daraxt, uning yo‘g‘on tanasi bor."),
            Q("Daraxt kuzda nimasini to‘kadi?", "Barglarini", ["Ildizlarini", "Tanasini", "Tuprog‘ini"],
              e="🍂", x="Kuzda ko‘p daraxtlar barglarini to‘kadi."),
            Q("O‘simlikning qaysi qismi chiroyli ochiladi?", "Gul", ["Ildiz", "Poya", "Urug‘"], e="🌸",
              x="Gul ochiladi, keyin uning o‘rnida meva hosil bo‘ladi."),
            TF("Ildiz yer ostida o‘sadi.", True, x="Ildiz tuproq ichida bo‘ladi."),
            TF("Barg — o‘simlikning yer ostidagi qismi.", False, x="Barglar yer ustida, poyada o‘sadi."),
            TF("Guldan meva paydo bo‘ladi.", True, e="🌸", x="Gul o‘rnida meva hosil bo‘ladi."),
            Q("Daraxtning tanasi — uning qaysi qismi?", "Poyasi", ["Ildizi", "Bargi", "Guli"], d=2, e="🌳",
              x="Daraxtning yo‘g‘on, qattiq poyasi tana deyiladi."),
            Q("Gul o‘rnida keyin nima paydo bo‘ladi?", "Meva", ["Ildiz", "Tosh", "Poya"], d=2,
              x="Gul to‘kilgach, uning o‘rnida meva o‘sadi."),
            Q("O‘simlikka o‘sish uchun nima kerak?", "Suv va quyosh nuri", ["Konfet", "Qorong‘ilik", "Shovqin"], d=2,
              x="O‘simlik suv, yorug‘lik va issiqlikda yaxshi o‘sadi."),
            Q("Sabzining biz yeydigan qismi qayerda o‘sadi?", "Yer ostida",
              ["Daraxt shoxida", "Gul ichida", "Suv ustida"], d=2, e="🥕",
              x="Sabzining biz yeydigan qismi — yo‘g‘on ildiz, u yer ostida o‘sadi."),
            Q("Qaysi biri o‘simlikning qismi emas?", "Qanot", ["Ildiz", "Barg", "Poya"], d=2,
              x="Qanot qushlarda bo‘ladi, o‘simlikda emas."),
            Q("Qaysi daraxtning mevasini yeymiz?", "O‘rik", ["Terak", "Archa", "Tol"], d=2,
              x="O‘rik — mevali daraxt, terak, archa va tolning mevasi yeyilmaydi."),
            TF("Kaktusning ham ildizi bor.", True, d=2, e="🌵", x="Kaktus ham o‘simlik, uning ham ildizi bor."),
            MATCH("O‘simlik qismini ishi bilan juftlang",
                  [("Ildiz", "suv ichadi"), ("Poya", "gulni ko‘tarib turadi"), ("Gul", "o‘rnida meva bo‘ladi"),
                   ("Urug‘", "yangi o‘simlik beradi"), ("Meva", "ichida urug‘ bor")], d=2,
                  x="Har bir qism o‘simlik uchun kerak."),
            Q("Nihol nima?", "Yosh o‘simlik", ["Katta tosh", "Qushning uyasi", "Quruq barg"], d=3, e="🌱",
              x="Nihol — endi o‘sib chiqqan yosh o‘simlik."),
            Q("Ildiz nima uchun kerak?", "O‘simlikni yerda ushlab turadi",
              ["O‘simlikni uchiradi", "Gulni bo‘yaydi", "Barglarni to‘kadi"], d=3,
              x="Ildiz o‘simlikni mahkam ushlaydi va tuproqdan suv oladi."),
        ])

T.topic("fruits_veg", "🍎", L("Mevalar va sabzavotlar", "Fruits and vegetables", "Фрукты и овощи"),
        chapter=C3,
        theory="• Mevalar daraxtda o‘sadi: olma, nok, o‘rik, shaftoli, gilos. Uzum tokda pishadi.\n"
               "• Sabzavotlar dalada va tomorqada o‘sadi: sabzi, piyoz, kartoshka, karam, bodring, pomidor.\n"
               "• Qovun va tarvuz polizda o‘sadi.\n"
               "Meva va sabzavotlarda vitaminlar ko‘p, ular bizni sog‘lom qiladi.\n"
               "Ularni yeyishdan oldin albatta yuvamiz.",
        items=[
            Q("Qaysi biri meva?", "🍎", ["🥕", "🌽", "🥔"], x="Olma daraxtda o‘sadi — u meva."),
            Q("Qaysi biri sabzavot?", "🥕", ["🍎", "🍐", "🍒"], x="Sabzi — sabzavot, u yer ostida o‘sadi."),
            Q("Qaysi biri meva?", "Nok", ["Piyoz", "Kartoshka", "Karam"], e="🍐", x="Nok daraxtda o‘sadi — u meva."),
            Q("Qaysi biri sabzavot?", "Kartoshka", ["Olma", "Gilos", "O‘rik"], e="🥔",
              x="Kartoshka — sabzavot."),
            Q("Olma qayerda o‘sadi?", "Daraxtda", ["Yer ostida", "Suvda", "Qumda"], e="🍎",
              x="Olma olma daraxtida o‘sadi."),
            Q("Kartoshka qayerda o‘sadi?", "Yer ostida", ["Daraxt shoxida", "Tokda", "Suv ostida"], e="🥔",
              x="Kartoshka tuganaklari yer ostida o‘sadi."),
            Q("Limon qanday rangda?", "Sariq", ["Ko‘k", "Binafsha", "Qora"], e="🍋", x="Pishgan limon sariq bo‘ladi."),
            Q("Bodring qanday rangda?", "Yashil", ["Qizil", "Ko‘k", "Oq"], e="🥒", x="Bodring yashil bo‘ladi."),
            Q("Pishgan pomidor ko‘pincha qanday rangda?", "Qizil", ["Ko‘k", "Oq", "Kulrang"], e="🍅",
              x="Pishgan pomidor odatda qizil bo‘ladi."),
            MATCH("Rasmni nomi bilan juftlang",
                  [("🍋", "limon"), ("🍐", "nok"), ("🍇", "uzum"), ("🍒", "gilos"), ("🍑", "shaftoli"), ("🍉", "tarvuz")],
                  x="Rasmga qarab, mevani nomi bilan topamiz."),
            MATCH("Sabzavot rasmini nomi bilan juftlang",
                  [("🥕", "sabzi"), ("🥔", "kartoshka"), ("🥒", "bodring"), ("🍅", "pomidor"), ("🍆", "baqlajon")],
                  x="Rasmga qarab, sabzavotni nomi bilan topamiz."),
            TF("Sabzi — sabzavot.", True, e="🥕", x="Sabzi dalada o‘sadi — u sabzavot."),
            TF("Gilos — sabzavot.", False, e="🍒", x="Gilos daraxtda o‘sadi — u meva."),
            TF("Mevani yuvmasdan yeyish mumkin.", False, x="Mevada chang va mikrob bo‘ladi, uni yuvib yeymiz."),
            TF("Mevalar sog‘liq uchun foydali.", True, x="Mevalarda vitaminlar ko‘p."),
            Q("Uzum qayerda pishadi?", "Tokda", ["Yer ostida", "Archada", "Terakda"], d=2, e="🍇",
              x="Uzum tok novdalarida shingil-shingil bo‘lib pishadi."),
            Q("Meva va sabzavotlarda nima ko‘p?", "Vitaminlar", ["Tosh", "Qum", "Tuz"], d=2,
              x="Vitaminlar bizni sog‘lom va baquvvat qiladi."),
            Q("Qaysi biri ortiqcha: olma, nok, sabzi, o‘rik?", "Sabzi", ["Olma", "Nok", "O‘rik"], d=2,
              x="Sabzi — sabzavot, qolganlari mevalar."),
            Q("Qaysi biri ortiqcha: piyoz, karam, bodring, gilos?", "Gilos", ["Piyoz", "Karam", "Bodring"], d=2,
              x="Gilos — meva, qolganlari sabzavotlar."),
            Q("Qaysi meva juda nordon?", "Limon", ["Banan", "Qovun", "Tarvuz"], d=2, x="Limon juda nordon bo‘ladi."),
            Q("Qaysi sabzavotni to‘g‘raganda ko‘zdan yosh chiqadi?", "Piyoz", ["Sabzi", "Bodring", "Kartoshka"], d=2,
              x="Piyoz to‘g‘ralganda ko‘zni achishtiradi."),
            Q("Qaysi biri polizda o‘sadi?", "Tarvuz", ["Olma", "O‘rik", "Gilos"], d=2, e="🍉",
              x="Tarvuz va qovun polizda o‘sadi, olma, o‘rik va gilos esa daraxtda."),
            TF("Qovun polizda o‘sadi.", True, d=2, e="🍈", x="Qovun — poliz ekini."),
            Q("Palovga qaysi sabzavot ko‘p solinadi?", "Sabzi", ["Bodring", "Karam", "Baqlajon"], d=3, e="🥕",
              x="Palovga guruch, go‘sht, piyoz va ko‘p sabzi solinadi."),
            Q("Qaysi meva yozda pishadi?", "O‘rik", ["Anor", "Behi", "Xurmo"], d=3,
              x="O‘rik yoz boshida pishadi, anor, behi va xurmo esa kuzda."),
        ])

T.topic("animals", "🐄", L("Uy va yovvoyi hayvonlar", "Domestic and wild animals", "Домашние и дикие животные"),
        chapter=C3,
        theory="• Uy hayvonlarini odamlar boqadi: sigir, qo‘y, echki, ot, it, mushuk, tovuq.\n"
               "• Yovvoyi hayvonlar o‘rmonda, tog‘da, cho‘lda o‘zi yashaydi: bo‘ri, tulki, ayiq, quyon.\n"
               "Hayvonlarning bolalari:\n"
               "• sigir — buzoq, ot — toy, qo‘y — qo‘zi, echki — uloq;\n"
               "• it — kuchukcha, mushuk — mushukcha, tovuq — jo‘ja.\n"
               "Uy hayvonlariga mehr bilan qaraymiz: boqamiz, suv beramiz.",
        items=[
            Q("Qaysi biri uy hayvoni?", "🐄", ["🐺", "🦊", "🐻"], x="Sigirni odamlar boqadi, u sut beradi."),
            Q("Qaysi biri yovvoyi hayvon?", "🐺", ["🐶", "🐱", "🐔"], x="Bo‘ri o‘rmon va tog‘da o‘zi yashaydi."),
            Q("Sigirning bolasi kim?", "Buzoq", ["Qo‘zi", "Uloq", "Jo‘ja"], e="🐄", x="Sigirning bolasi — buzoq."),
            Q("Qo‘yning bolasi kim?", "Qo‘zi", ["Buzoq", "Toy", "Kuchukcha"], e="🐑", x="Qo‘yning bolasi — qo‘zi."),
            Q("Echkining bolasi kim?", "Uloq", ["Qo‘zi", "Buzoq", "Jo‘ja"], e="🐐", x="Echkining bolasi — uloq."),
            Q("Otning bolasi kim?", "Toy", ["Buzoq", "Uloq", "Mushukcha"], e="🐎", x="Otning bolasi — toy."),
            Q("Tovuqning bolasi kim?", "Jo‘ja", ["Qo‘zi", "Kuchukcha", "Uloq"], e="🐔", x="Tovuqning bolasi — jo‘ja."),
            Q("Itning bolasi kim?", "Kuchukcha", ["Mushukcha", "Buzoq", "Jo‘ja"], e="🐶", x="Itning bolasi — kuchukcha."),
            Q("Qaysi rasmda jo‘ja bor?", "🐤", ["🐶", "🐱", "🐄"], x="🐤 — sariq jo‘ja."),
            Q("Bizga sut beradigan hayvonni toping", "🐄", ["🐔", "🐶", "🐱"], e="🥛",
              x="Sigir sut beradi, sutdan qatiq, qaymoq, pishloq qilinadi."),
            Q("Tuxum qo‘yadigan uy parrandasini toping", "🐔", ["🐄", "🐑", "🐶"], e="🥚",
              x="Tovuq tuxum qo‘yadi."),
            Q("Kim “miyov” deydi?", "🐱", ["🐶", "🐄", "🐔"], x="Mushuk miyovlaydi."),
            Q("Kim “vov-vov” deydi?", "🐶", ["🐱", "🐑", "🐎"], x="It vovullaydi."),
            MATCH("Hayvonni bolasi bilan juftlang",
                  [("🐄 sigir", "buzoq"), ("🐎 ot", "toy"), ("🐑 qo‘y", "qo‘zi"), ("🐐 echki", "uloq"),
                   ("🐶 it", "kuchukcha"), ("🐔 tovuq", "jo‘ja")],
                  x="Sigir — buzoq, ot — toy, qo‘y — qo‘zi, echki — uloq, it — kuchukcha, tovuq — jo‘ja."),
            TF("Mushuk — uy hayvoni.", True, e="🐱", x="Mushuk odamlar bilan uyda yashaydi."),
            TF("Yovvoyi hayvonlarni odam boqadi.", False, x="Yovvoyi hayvonlar ovqatni o‘zi topadi."),
            TF("Uy hayvonlariga mehr bilan qarash kerak.", True, x="Ularni boqamiz, suv beramiz, urmaymiz."),
            Q("Buzoqning onasi kim?", "Sigir", ["Qo‘y", "Echki", "Ot"], d=2, x="Buzoq — sigirning bolasi."),
            Q("Qo‘zining onasi kim?", "Qo‘y", ["Sigir", "Echki", "Tovuq"], d=2, x="Qo‘zi — qo‘yning bolasi."),
            Q("Uyni kim qo‘riqlaydi?", "🐶", ["🐱", "🐔", "🐑"], d=2, x="It uyni qo‘riqlaydi, begonani ko‘rsa, vovullaydi."),
            Q("Sichqon tutadigan uy hayvoni kim?", "Mushuk", ["Sigir", "Qo‘y", "Tovuq"], d=2, e="🐭",
              x="Mushuk sichqonlarni tutadi."),
            Q("Qaysi hayvon o‘rmonda yashaydi?", "Ayiq", ["Sigir", "Mushuk", "Tovuq"], d=2, e="🌲",
              x="Ayiq — yovvoyi hayvon, u o‘rmon va tog‘larda yashaydi."),
            Q("Uzun quloqli, sakrab yuradigan hayvon kim?", "Quyon", ["Ayiq", "Sigir", "Tovuq"], d=2,
              x="Quyonning qulog‘i uzun, u sakrab yuguradi."),
            MATCH("Hayvonni ovozi bilan juftlang",
                  [("It", "vovullaydi"), ("Mushuk", "miyovlaydi"), ("Qo‘y", "ma’raydi"), ("Sigir", "mo‘raydi"),
                   ("Ot", "kishnaydi"), ("Xo‘roz", "qichqiradi")], d=2,
                  x="Har bir hayvonning o‘z ovozi bor."),
            Q("Kim kishnaydi?", "Ot", ["It", "Mushuk", "Qo‘y"], d=2, x="Ot kishnaydi."),
            Q("Ertaklarda ayyor deb ataladigan malla hayvon kim?", "Tulki", ["Quyon", "Sigir", "Echki"], d=3, e="🦊",
              x="Ertaklarda tulki ayyor bo‘ladi, uning dumi yo‘g‘on va malla."),
            Q("Tuyaning bolasi kim?", "Bo‘taloq", ["Toy", "Uloq", "Qo‘zi"], d=3, e="🐫", x="Tuyaning bolasi — bo‘taloq."),
            Q("Eshakning bolasi kim?", "Xo‘tik", ["Buzoq", "Kuchukcha", "Jo‘ja"], d=3, x="Eshakning bolasi — xo‘tik."),
            Q("Qaysi guruhda hammasi uy hayvoni?", "🐄 🐑 🐔", ["🐄 🐺 🐔", "🦊 🐑 🐻", "🐻 🐺 🦊"], d=3,
              x="Sigir, qo‘y va tovuqni odamlar boqadi."),
            Q("Qaysi guruhda hammasi yovvoyi?", "🐺 🦊 🐻", ["🐶 🦊 🐻", "🐺 🐱 🐄", "🐔 🐑 🐐"], d=3,
              x="Bo‘ri, tulki va ayiq — yovvoyi hayvonlar."),
        ])

T.topic("creatures", "🐦", L("Qushlar, baliqlar, hasharotlar", "Birds, fish and insects", "Птицы, рыбы, насекомые"),
        chapter=C3,
        theory="• Qushlarning pati, qanoti va tumshug‘i bor. Ular tuxum qo‘yadi. Ko‘p qushlar uchadi: chumchuq, kaptar, laylak.\n"
               "• Baliqlar suvda yashaydi va suzadi. Ularning suzgichlari va tangachasi bor.\n"
               "• Hasharotlar kichkina, ularning 6 ta oyog‘i bor: asalari, kapalak, chumoli, ninachi.\n"
               "Asalari gul shirasidan asal tayyorlaydi.",
        items=[
            Q("Qaysi biri qush?", "🐦", ["🐟", "🐝", "🐱"], x="🐦 — qush, uning pati va qanoti bor."),
            Q("Qaysi biri baliq?", "🐟", ["🐦", "🦋", "🐶"], x="🐟 — baliq, u suvda suzadi."),
            Q("Qaysi biri hasharot?", "🦋", ["🐟", "🐦", "🐄"], x="Kapalak — hasharot."),
            Q("Kim suvda yashaydi?", "🐟", ["🐔", "🐝", "🐑"], x="Baliq suvda yashaydi."),
            Q("Qush nimasi bilan uchadi?", "Qanoti bilan", ["Dumi bilan", "Oyog‘i bilan", "Tumshug‘i bilan"],
              x="Qush qanotlarini qoqib uchadi."),
            Q("Baliq nima qiladi?", "Suzadi", ["Uchadi", "Yuguradi", "Daraxtga chiqadi"], x="Baliq suvda suzadi."),
            Q("Asal tayyorlaydigan hasharotni toping", "🐝", ["🦋", "🐜", "🐞"],
              x="Asalari gul shirasidan asal tayyorlaydi."),
            Q("Qushlar tuxumini qayerga qo‘yadi?", "Uyasiga", ["Daryoga", "Muzlatgichga", "Shkafga"],
              x="Qushlar uya qurib, tuxumini o‘sha yerga qo‘yadi."),
            Q("Jo‘ja nimadan chiqadi?", "Tuxumdan", ["Guldan", "Suvdan", "Tuproqdan"], e="🐣",
              x="Jo‘ja tuxumni yorib chiqadi."),
            MATCH("Rasmni nomi bilan juftlang",
                  [("🐦", "qush"), ("🐟", "baliq"), ("🦋", "kapalak"), ("🐝", "asalari"), ("🐜", "chumoli"),
                   ("🐞", "xonqizi")], x="Rasmga qarab, jonivorni nomi bilan topamiz."),
            TF("Qushlar tuxum qo‘yadi.", True, x="Hamma qushlar tuxum qo‘yadi."),
            TF("Kapalak — qush.", False, e="🦋", x="Kapalak — hasharot, uning pati yo‘q."),
            TF("Chumoli — hasharot.", True, e="🐜", x="Chumolining 6 ta oyog‘i bor — u hasharot."),
            TF("Baliq suvsiz yashay olmaydi.", True, e="🐟", x="Baliq faqat suvda nafas oladi."),
            Q("Chumolining nechta oyog‘i bor?", "6 ta", ["2 ta", "4 ta", "8 ta"], d=2, e="🐜",
              x="Hasharotlarning 6 ta oyog‘i bor."),
            Q("Baliqning suzishiga nima yordam beradi?", "Suzgich va dum",
              ["Qanot va pat", "Oyoq va tirnoq", "Tumshuq va tish"], d=2,
              x="Baliq suzgichlari va dumini qimirlatib suzadi."),
            Q("Qaysi biri qush emas?", "Kapalak", ["Chumchuq", "Kaptar", "Laylak"], d=2,
              x="Kapalak — hasharot, qolganlari qushlar."),
            Q("Qaysi biri hasharot emas?", "Baliq", ["Ninachi", "Chumoli", "Kapalak"], d=2,
              x="Baliq — suv jonivori, qolganlari hasharotlar."),
            Q("Gul shirasini yig‘ib, asal qiladigan hasharot kim?", "Asalari", ["Pashsha", "Chivin", "Chigirtka"], d=2,
              x="Asalari gul shirasidan asal qiladi."),
            Q("Kechasi uchadigan, katta ko‘zli qush kim?", "Boyqush", ["Tovuq", "Chumchuq", "Kaptar"], d=2,
              x="Boyqush kunduzi uxlaydi, kechasi uchib ov qiladi."),
            Q("Qaysi qush suvda suzadi?", "O‘rdak", ["Chumchuq", "Musicha", "Boyqush"], d=2,
              x="O‘rdakning oyoq barmoqlari orasida parda bor, u suzadi."),
            Q("Qushning og‘zi nima deyiladi?", "Tumshuq", ["Suzgich", "Dum", "Qanot"], d=2,
              x="Qush tumshug‘i bilan don cho‘qiydi."),
            TF("Hamma qushlar suvda yashaydi.", False, d=2, x="Ko‘p qushlar daraxtda va uylar tomida yashaydi."),
            Q("Yozda kechasi g‘ing‘illab, chaqadigan hasharot?", "Chivin", ["Kapalak", "Ninachi", "Xonqizi"], d=3,
              x="Chivin chaqsa, terimiz qichiydi."),
            Q("Uzun oyoqli, uyasini baland joyga quradigan qush?", "Laylak", ["Chumchuq", "Tovuq", "Kaptar"], d=3,
              x="Laylakning oyoqlari va tumshug‘i uzun, uyasini baland joyga quradi."),
            Q("Kapalak avval kim bo‘lgan?", "Qurt", ["Baliq", "Qush", "Chumoli"], d=3, e="🦋",
              x="Kapalak tuxumidan qurt chiqadi, qurt g‘umbakka, g‘umbak esa kapalakka aylanadi."),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["plants", "fruits_veg", "animals", "creatures"], chapter=C3)

# ============================================================ 4-chorak
T.topic("road_safety", "🚦", L("Yo‘l harakati xavfsizligi", "Road safety", "Безопасность на дороге"),
        chapter=C4,
        theory="Svetofor bizga yo‘l ko‘rsatadi:\n"
               "• qizil — to‘xta, yo‘ldan o‘tmaymiz;\n"
               "• sariq — tayyorlan, kut;\n"
               "• yashil — yo‘ldan o‘tish mumkin.\n"
               "Yo‘lni faqat piyodalar o‘tish joyidan (“zebra”dan) o‘tamiz. Avval chapga, keyin o‘ngga qaraymiz.\n"
               "Yo‘l yonida o‘ynamaymiz, katta yo‘ldan kattalarning qo‘lidan ushlab o‘tamiz.",
        items=[
            Q("Svetoforning qaysi rangida to‘xtaymiz?", "Qizil", ["Yashil", "Ko‘k", "Oq"], e="🚦",
              x="Qizil chiroq — to‘xta!"),
            Q("Svetoforning qaysi rangida yo‘ldan o‘tamiz?", "Yashil", ["Qizil", "Sariq", "Qora"], e="🚦",
              x="Yashil chiroqda atrofga qarab, yo‘ldan o‘tamiz."),
            Q("Sariq chiroq nima deydi?", "Tayyorlan, kut", ["Yugur", "O‘yna", "Yo‘lga chiq"], e="🚦",
              x="Sariq chiroq — tayyorlan, kut."),
            Q("Yo‘lni qayerdan kesib o‘tamiz?", "Piyodalar o‘tish joyidan",
              ["Mashinalar orasidan", "Burilishdan", "Istalgan joydan"], e="🚸",
              x="Yo‘lni faqat piyodalar o‘tish joyidan o‘tamiz."),
            Q("Ko‘chada qayerda o‘ynash mumkin?", "Bolalar maydonchasida",
              ["Yo‘lning o‘rtasida", "Mashinalar yonida", "Yo‘l chetida"],
              x="Bolalar maydonchasi xavfsiz, yo‘lda o‘ynash xavfli."),
            Q("Yo‘ldan qanday o‘tamiz?", "Shoshmasdan, yurib", ["Yugurib", "Telefonga qarab", "Sakrab o‘ynab"],
              x="Yo‘ldan yugurmasdan, atrofga qarab, yurib o‘tamiz."),
            TF("Qizil chiroqda yo‘ldan o‘tish mumkin.", False, e="🚦", x="Qizil chiroqda to‘xtab, kutamiz."),
            TF("Yo‘lda to‘p o‘ynash xavfli.", True, e="⚽", x="Yo‘lda mashinalar yuradi, u yerda o‘ynamaymiz."),
            TF("Kichkina bola katta yo‘ldan yolg‘iz o‘tishi kerak.", False,
               x="Kichkina bola katta yo‘ldan kattalarning qo‘lidan ushlab o‘tadi."),
            MATCH("Svetofor rangini ma’nosi bilan juftlang",
                  [("Qizil", "to‘xta"), ("Sariq", "kut"), ("Yashil", "yur")],
                  x="Qizil — to‘xta, sariq — kut, yashil — yur."),
            Q("Piyodalar svetoforida yashil odamcha nima deydi?", "O‘tish mumkin", ["To‘xta", "Orqaga qayt", "Yugur"],
              x="Yashil odamcha yonsa, yo‘ldan o‘tish mumkin."),
            Q("Mashinalar svetoforida nechta chiroq bor?", "3 ta", ["2 ta", "5 ta", "7 ta"], d=2, e="🚦",
              x="Qizil, sariq va yashil — 3 ta chiroq."),
            Q("Piyodalar o‘tish joyi qanday chiziladi?", "Oq yo‘l-yo‘l chiziqlar",
              ["Qizil doira", "Ko‘k yulduzcha", "Yashil uchburchak"], d=2,
              x="Oq yo‘l-yo‘l chiziqlar zebraga o‘xshaydi, shuning uchun uni “zebra” deymiz."),
            Q("Yo‘ldan o‘tishdan oldin qayoqqa qaraymiz?", "Avval chapga, keyin o‘ngga",
              ["Faqat tepaga", "Faqat pastga", "Hech qayoqqa"], d=2,
              x="Avval chapdan, keyin o‘ngdan mashina kelmayotganini tekshiramiz."),
            Q("Piyoda qayerda yuradi?", "Yo‘lakda (trotuarda)", ["Yo‘lning o‘rtasida", "Mashina yo‘lida", "Temir yo‘lda"],
              d=2, x="Piyodalar uchun alohida yo‘lak — trotuar bor."),
            Q("Mashinada bola qanday o‘tiradi?", "Bolalar o‘rindig‘ida, kamar taqib",
              ["Tik turib", "Haydovchining tizzasida", "Oynadan boshini chiqarib"], d=2, e="🚗",
              x="Bolalar o‘rindig‘i va kamar bolani asraydi."),
            Q("Velosipedda yurganda boshga nima kiyiladi?", "Himoya dubulg‘asi", ["Do‘ppi", "Kepka", "Telpak"], d=2, e="🚲",
              x="Dubulg‘a yiqilganda boshni urilishdan saqlaydi."),
            TF("Yashil chiroqda ham atrofga qarab o‘tamiz.", True, d=2,
               x="Yashil chiroqda ham mashina kelmayotganiga ishonch hosil qilamiz."),
            TF("Yo‘ldan telefonga qarab o‘tish xavfli.", True, d=2,
               x="Telefonga qarasak, mashinani ko‘rmay qolamiz."),
            Q("Svetoforning eng tepadagi chirog‘i qaysi rangda?", "Qizil", ["Yashil", "Sariq", "Ko‘k"], d=3, e="🚦",
              x="Mashinalar svetoforida qizil chiroq eng tepada bo‘ladi."),
            Q("Avtobusdan tushgach nima qilamiz?", "Avtobus ketishini kutamiz",
              ["Darhol avtobus oldidan yuguramiz", "Yo‘lda o‘ynaymiz", "Ko‘zni yumib o‘tamiz"], d=3, e="🚌",
              x="Turgan avtobus yo‘lni to‘sib turadi, orqasidan mashina chiqib qolishi mumkin."),
            Q("Kechasi haydovchi bolani yaxshi ko‘rishi uchun nima kerak?", "Nur qaytaruvchi belgi",
              ["Qora kiyim", "Ko‘zoynak", "Soyabon"], d=3,
              x="Mashina chirog‘i tushganda nur qaytaruvchi belgi yaltirab ko‘rinadi."),
        ])

T.topic("home_safety", "🔥", L("Olov va elektrdan ehtiyot bo‘lamiz", "Fire and electrical safety",
                               "Осторожно: огонь и электричество"),
        chapter=C4,
        theory="Uyda ham ehtiyot bo‘lish kerak.\n"
               "• Gugurt, zajigalka bilan o‘ynamaymiz, gaz plitani o‘zimiz yoqmaymiz.\n"
               "• Rozetkaga barmoq va narsa tiqmaymiz, ho‘l qo‘l bilan elektr asboblarini ushlamaymiz.\n"
               "• Dori, pichoq, qaychini kattalarsiz olmaymiz.\n"
               "Yong‘in chiqsa — kattalarga aytamiz va uydan chiqamiz.\n"
               "Yong‘in xizmati — 101, tez yordam — 103.",
        items=[
            Q("Gugurt bilan o‘ynasa bo‘ladimi?", "Yo‘q, xavfli", ["Ha, qiziq", "Ha, kechasi", "Ha, yolg‘iz qolganda"],
              e="🔥", x="Gugurt bilan o‘ynasak, yong‘in chiqishi mumkin."),
            Q("Rozetkaga nima qilamiz?", "Hech narsa tiqmaymiz", ["Barmoq tiqamiz", "Mix tiqib ko‘ramiz", "Suv sepamiz"],
              e="🔌", x="Rozetkada elektr toki bor, u juda xavfli."),
            Q("Yong‘in chiqsa, birinchi nima qilamiz?", "Kattalarga aytamiz",
              ["Karavot tagiga yashirinamiz", "Shkafga kiramiz", "Indamaymiz"],
              x="Yong‘inni ko‘rsak, darhol kattalarga aytamiz va uydan chiqamiz."),
            Q("Yong‘inni qaysi mashina o‘chiradi?", "🚒", ["🚑", "🚓", "🚌"], x="🚒 — o‘t o‘chirish mashinasi."),
            Q("Kasalni shifoxonaga qaysi mashina olib boradi?", "🚑", ["🚒", "🚜", "🚛"], x="🚑 — tez yordam mashinasi."),
            Q("Dorini kim beradi?", "Kattalar yoki shifokor", ["O‘zimiz olib ichamiz", "Ukamiz", "Qo‘shni bola"],
              e="💊", x="Dorini faqat kattalar yoki shifokor beradi."),
            Q("Qaysi narsa bilan o‘ynash xavfli?", "Gugurt", ["Koptok", "Kubik", "Qo‘g‘irchoq"], e="🔥",
              x="Gugurt — o‘yinchoq emas."),
            Q("Qaysi narsa elektr bilan ishlaydi?", "Televizor", ["Kitob", "Qalam", "To‘p"], e="📺",
              x="Televizor elektr toki bilan ishlaydi."),
            TF("Gaz plitani bolalar o‘zi yoqmaydi.", True, x="Gaz plitani faqat kattalar yoqadi."),
            TF("Rozetkaga mix tiqish xavfli.", True, e="🔌", x="Elektr toki urishi mumkin."),
            TF("Pichoq va qaychi bilan o‘ynash xavfli.", True, e="✂️", x="O‘tkir narsalar qo‘lni kesishi mumkin."),
            Q("Yong‘in o‘chiruvchilarni qaysi raqam bilan chaqiramiz?", "101", ["103", "104", "100"], d=2, e="🚒",
              x="101 — yong‘in xavfsizligi xizmati."),
            Q("Tez yordamni qaysi raqam bilan chaqiramiz?", "103", ["101", "104", "105"], d=2, e="🚑",
              x="103 — tez tibbiy yordam."),
            Q("Elektr asbobini qanday qo‘l bilan ushlaymiz?", "Quruq qo‘l bilan",
              ["Ho‘l qo‘l bilan", "Sovunli qo‘l bilan", "Suvli qo‘l bilan"], d=2, e="🔌",
              x="Suv elektr tokini o‘tkazadi, ho‘l qo‘l bilan ushlash xavfli."),
            Q("Ochiq yotgan elektr simini ko‘rsak nima qilamiz?", "Tegmaymiz, kattalarga aytamiz",
              ["Qo‘l bilan ushlaymiz", "Tortib o‘ynaymiz", "Ustidan sakraymiz"], d=2,
              x="Simda tok bo‘lishi mumkin, unga tegmaymiz."),
            Q("Notanish odam shirinlik bersa, nima qilamiz?", "Olmaymiz, kattalarga aytamiz",
              ["Olib, u bilan ketamiz", "Uyimiz manzilini aytamiz", "Mashinasiga o‘tiramiz"], d=2,
              x="Notanish odamdan hech narsa olmaymiz va u bilan ketmaymiz."),
            Q("Hovuz va daryoda kim bilan cho‘milamiz?", "Faqat kattalar bilan",
              ["Yolg‘iz o‘zimiz", "Kechasi qorong‘ida", "Kichik ukamiz bilan"], d=2,
              x="Suvda kattalar yonida bo‘lsak, xavfsiz bo‘ladi."),
            TF("Yoqilgan dazmol juda issiq bo‘ladi.", True, d=2, x="Yoqilgan dazmolga tegsak, qo‘l kuyadi."),
            TF("Yong‘inda karavot tagiga yashirinish kerak.", False, d=2,
               x="Yashirinish xavfli: tezda uydan chiqib, kattalarga aytamiz."),
            Q("Uyda gaz hidi kelsa nima qilamiz?", "Kattalarga aytamiz, deraza ochamiz",
              ["Gugurt chaqamiz", "Chiroqni yoqib ko‘ramiz", "Hech narsa qilmaymiz"], d=3,
              x="Gaz hidi kelganda olov yoqish va chiroqni yoqish xavfli."),
            Q("Uyda yolg‘iz qolganda eshik taqillasa?", "Ochmaymiz, ota-onaga qo‘ng‘iroq qilamiz",
              ["Darhol ochamiz", "Notanishni uyga kiritamiz", "Eshikni ochib, ko‘chaga chiqamiz"], d=3,
              x="Kattalarsiz eshikni notanish odamga ochmaymiz."),
            MATCH("Raqamni xizmat bilan juftlang",
                  [("101", "yong‘in xizmati"), ("103", "tez yordam"), ("104", "gaz xizmati")], d=3,
                  x="101 — yong‘in, 103 — tez yordam, 104 — gaz xizmati."),
        ])

T.topic("protect", "💧", L("Suvni va tabiatni asraymiz", "Saving water and nature", "Бережём воду и природу"),
        chapter=C4,
        theory="Tabiat — hammamizning umumiy uyimiz, uni asraymiz.\n"
               "• Suvni tejaymiz: tish yuvayotganda jo‘mrakni yopib turamiz.\n"
               "• Axlatni yerga emas, axlat qutisiga tashlaymiz.\n"
               "• Daraxt va gul ekamiz, shoxlarni sindirmaymiz, gullarni yulmaymiz.\n"
               "• Qushlarga qishda don beramiz, ularning uyasini buzmaymiz.\n"
               "Toza tabiatda odamlar ham, hayvonlar ham sog‘lom yashaydi.",
        items=[
            Q("Qog‘oz va o‘ramni qayerga tashlaymiz?", "Axlat qutisiga", ["Yerga", "Ariqqa", "Daraxt tagiga"], e="🗑️",
              x="Axlatni faqat axlat qutisiga tashlaymiz."),
            Q("Tish yuvayotganda jo‘mrakni nima qilamiz?", "Yopib turamiz",
              ["Ochiq qoldiramiz", "Kattaroq ochamiz", "Sindiramiz"], e="💧",
              x="Jo‘mrakni yopib tursak, suv behuda oqmaydi."),
            Q("Qishda qushlarga qanday g‘amxo‘rlik qilamiz?", "Don sepamiz", ["Uyasini buzamiz", "Tosh otamiz", "Qo‘rqitamiz"],
              e="🐦", x="Qishda qushlar ovqat topa olmaydi, ularga don sepamiz."),
            Q("Bog‘dagi gullarni nima qilamiz?", "Yulmaymiz, hidlaymiz", ["Yulib olamiz", "Oyoq osti qilamiz", "Sindiramiz"],
              e="🌷", x="Gullar hammaga quvonch beradi, ularni yulmaymiz."),
            Q("Tabiatga qanday yordam beramiz?", "Daraxt ekamiz", ["Shox sindiramiz", "Axlat tashlaymiz", "Gul yulamiz"],
              e="🌳", x="Daraxt havoni tozalaydi va soya beradi."),
            Q("Suv kimlarga kerak?", "Hamma tiriklarga", ["Faqat baliqqa", "Faqat gulga", "Hech kimga"], e="💧",
              x="Odamlar, hayvonlar va o‘simliklar suvsiz yashay olmaydi."),
            TF("Daraxt shoxlarini sindirish yaxshi emas.", True, x="Shoxi singan daraxt kasal bo‘ladi."),
            TF("Suvni behuda oqizish yaxshi.", False, x="Suvni tejash kerak."),
            TF("Qush uyasini buzmaslik kerak.", True, e="🐦", x="Uyada qushning tuxumlari va jo‘jalari bo‘ladi."),
            TF("Yerga tashlangan axlat tabiatni ifloslaydi.", True, e="🗑️", x="Axlat yer, suv va havoni ifloslaydi."),
            Q("Jo‘mrakdan suv tomchilayapti. Nima qilamiz?", "Kattalarga aytamiz",
              ["Indamaymiz", "Yana ochamiz", "Tomosha qilib o‘tiramiz"], d=2,
              x="Tomchilagan jo‘mrakdan ko‘p suv isrof bo‘ladi, uni tuzatish kerak."),
            Q("Ariq va daryo toza bo‘lishi uchun nima qilamiz?", "Axlat tashlamaymiz",
              ["Shisha otamiz", "Yuvindi to‘kamiz", "Plastik tashlaymiz"], d=2,
              x="Ariq va daryoga axlat tashlamasak, suv toza bo‘ladi."),
            Q("Kim tabiatni asrayapti?", "Ali nihol ekdi",
              ["Vali gul yuldi", "Zarina yerga qog‘oz tashladi", "Bobur shox sindirdi"], d=2,
              x="Nihol ekish — tabiatga yordam."),
            Q("Tabiat qo‘ynida dam olgach, nima qilamiz?", "Axlatni yig‘ib olamiz",
              ["Axlatni qoldirib ketamiz", "Gulxanni yonib qoldiramiz", "Shishalarni sindiramiz"], d=2,
              x="Dam olgan joyimizni toza qoldiramiz."),
            Q("Kapalakni qanday tomosha qilamiz?", "Ushlamay, uzoqdan", ["Qanotidan ushlab", "Qutiga qamab", "Tayoq bilan urib"],
              d=2, e="🦋", x="Kapalakning qanoti nozik, uni ushlamaymiz."),
            Q("Ko‘chada yerda qog‘oz yotibdi. Nima qilamiz?", "Olib, axlat qutisiga tashlaymiz",
              ["Tepib o‘tamiz", "Yoniga yana tashlaymiz", "Ariqqa uloqtiramiz"], d=2,
              x="Ko‘chani toza saqlash — hammamizning ishimiz."),
            TF("Chumoli uyasini tayoq bilan buzish mumkin.", False, d=2, e="🐜",
               x="Chumolilar ham tabiatga foyda keltiradi, ularning uyasini buzmaymiz."),
            TF("Daraxtlar havoni tozalaydi.", True, d=2, e="🌳", x="Daraxtlar havoni toza va yoqimli qiladi."),
            MATCH("Kimga qanday g‘amxo‘rlik qilamiz?",
                  [("Qushlar", "don sepamiz"), ("Gullar", "suv quyamiz"), ("Daraxt", "shoxini sindirmaymiz"),
                   ("Mushuk", "ovqat beramiz"), ("Baliqlar", "suvni toza saqlaymiz")], d=2,
                  x="Har bir tirik jonzotga g‘amxo‘rlik qilamiz."),
            Q("Plastik shishalarni nima qilamiz?", "Alohida qutiga yig‘amiz",
              ["Daryoga tashlaymiz", "Yerga ko‘mamiz", "Gulxanda yoqamiz"], d=3, e="♻️",
              x="Yig‘ilgan plastikdan qayta yangi buyumlar yasash mumkin."),
            Q("O‘rmonda gulxanni o‘chirmay ketsak nima bo‘ladi?", "Yong‘in chiqishi mumkin",
              ["Gullar ochiladi", "Yomg‘ir yog‘adi", "Hech narsa bo‘lmaydi"], d=3, e="🔥",
              x="O‘chirilmagan gulxandan o‘rmonga o‘t ketishi mumkin."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["road_safety", "home_safety", "protect"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["my_body", "senses", "hygiene", "living", "seasons", "weather", "day_night", "plants", "fruits_veg",
        "animals", "creatures", "road_safety", "home_safety", "protect"],
       chapter=C4, level=3)


# ------------------------------------------------------------ o'z tekshiruvimiz (imlo belgilari, emoji, soni)
def _new_emoji(cp):
    """Android 9 da yo'q yangi emoji (Emoji 11+) bloklari. 🦷 (U+1F9B7) ataylab ruxsat etilgan."""
    if cp == 0x1F9B7:
        return False
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
        if it["t"] == "choice" and len(it["w"]) < 3:
            bad.append(f"{it['id']}: noto‘g‘ri javoblar 3 tadan kam")
        if it["t"] == "order":
            bad.append(f"{it['id']}: 1-sinfda ORDER ishlatilmaydi")
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
