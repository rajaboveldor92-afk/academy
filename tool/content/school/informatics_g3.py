"""Informatika, 3-sinf: assets/data/school/informatics_g3.json va bank_informatics_g3.json.

Mavzular O'zbekiston boshlang'ich sinf informatika dasturi yo'nalishida tuzilgan;
qoida va savollar matni — o'zimizniki (darslikdan ko'chirilmagan).
Qayta yaratish: python3 tool/content/school/informatics_g3.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("informatics", 3, L("Informatika", "Computer science", "Информатика"))

C1 = "1-chorak. Kompyuter bilan tanishuv"
C2 = "2-chorak. Sichqoncha va klaviatura"
C3 = "3-chorak. Ish stoli, fayl va rasm"
C4 = "4-chorak. Axborot va algoritm"


def near(ans, cands, k=4, lo=0):
    """Sonli javob uchun noto'g'ri variantlar: takrorsiz, javobdan farqli, `lo` dan kichik emas."""
    out = []
    for c in cands:
        if c != ans and c >= lo and c not in out:
            out.append(c)
    return out[:k]


# ============================================================ 1-chorak
T.topic("kompyuter", "🖥️", L("Kompyuter va uning qismlari", "The computer and its parts", "Компьютер и его части"),
        chapter=C1,
        theory="Kompyuter — axborot bilan ishlaydigan aqlli yordamchi qurilma.\n"
               "• Tizim bloki — kompyuterning asosiy qismlari joylashgan quti.\n"
               "• Monitor — rasm va matn ko‘rinadigan ekran.\n"
               "• Klaviatura — harf va raqam yozish uchun; sichqoncha — ekrandagi ko‘rsatkichni boshqarish uchun.\n"
               "Qo‘shimcha qurilmalar: karnay, quloqchin, printer, skaner, mikrofon, veb-kamera.",
        items=[
            Q("Kompyuterning qaysi qismida tasvir ko‘rinadi?", "Monitor", ["Klaviatura", "Sichqoncha", "Karnay", "Mikrofon"],
              x="Monitor — kompyuterning ekrani, unda rasm va matn ko‘rinadi.", e="🖥️"),
            Q("Harf va raqamlarni yozish uchun qaysi qurilma kerak?", "Klaviatura", ["Monitor", "Karnay", "Printer", "Veb-kamera"],
              x="Klaviaturada harf va raqam tugmalari bor.", e="⌨️"),
            Q("Ekrandagi ko‘rsatkichni qaysi qurilma boshqaradi?", "Sichqoncha", ["Printer", "Karnay", "Mikrofon", "Skaner"],
              x="Sichqonchani stol ustida sursak, ekrandagi ko‘rsatkich ham suriladi.", e="🖱️"),
            Q("Kompyuterdan tovush qaysi qurilma orqali chiqadi?", "Karnay", ["Skaner", "Klaviatura", "Sichqoncha", "Veb-kamera"],
              x="Karnay (kolonka) musiqa va ovozni eshittiradi.", e="🔊"),
            Q("Matn yoki rasmni qog‘ozga chiqaradigan qurilma qaysi?", "Printer", ["Skaner", "Mikrofon", "Sichqoncha", "Karnay"],
              x="Printer kompyuterdagi matn va rasmni qog‘ozga chop etadi.", e="🖨️"),
            Q("Qog‘ozdagi rasmni kompyuterga o‘tkazadigan qurilma qaysi?", "Skaner", ["Printer", "Karnay", "Monitor", "Quloqchin"],
              x="Skaner qog‘ozdagi rasm va matnni nusxalab, kompyuterga kiritadi."),
            Q("Ovozni kompyuterga yozib olish uchun nima kerak?", "Mikrofon", ["Karnay", "Printer", "Monitor", "Quloqchin"],
              x="Mikrofon ovozimizni kompyuterga kiritadi.", e="🎤"),
            Q("Videoqo‘ng‘iroqda yuzimizni ko‘rsatadigan qurilma qaysi?", "Veb-kamera", ["Karnay", "Skaner", "Klaviatura", "Printer"],
              x="Veb-kamera tasvirimizni olib, kompyuter orqali suhbatdoshga uzatadi."),
            Q("Kompyuterning asosiy qismlari joylashgan quti qanday ataladi?", "Tizim bloki", ["Monitor", "Klaviatura", "Karnay", "Printer"],
              x="Stol kompyuterida asosiy qismlar tizim bloki ichida joylashgan."),
            Q("Musiqani boshqalarga eshittirmay tinglash uchun nima kerak?", "Quloqchin", ["Printer", "Skaner", "Veb-kamera", "Klaviatura"],
              x="Quloqchin tovushni faqat bizning quloqqa yetkazadi.", e="🎧"),
            Q("Qaysi biri kompyuter qurilmasi emas?", "Muzlatgich", ["Sichqoncha", "Monitor", "Klaviatura", "Printer"],
              x="Muzlatgich — oshxona jihozi, u kompyuterning qismi emas."),
            Q("Kompyuter nima bilan ishlaydi?", "Elektr toki bilan", ["Suv bilan", "Benzin bilan", "Ko‘mir bilan"],
              x="Kompyuter elektr tokida ishlaydi, noutbukda esa batareya ham bor.", e="🔌"),
            TF("Monitor — kompyuterning ekrani.", True, x="Monitorda rasm, matn va video ko‘rinadi."),
            TF("Printer ovoz chiqaradi.", False, x="Ovozni karnay chiqaradi, printer esa qog‘ozga chop etadi."),
            TF("Klaviatura yordamida matn yozamiz.", True, x="Klaviatura tugmalarini bosib harf va raqam yozamiz."),
            MATCH("Qurilmani vazifasi bilan juftlang",
                  [("Monitor", "Tasvirni ko‘rsatadi"), ("Klaviatura", "Harflarni yozadi"), ("Karnay", "Tovush chiqaradi"),
                   ("Printer", "Qog‘ozga chop etadi"), ("Mikrofon", "Ovozni yozib oladi"), ("Skaner", "Rasmni nusxalab kiritadi")],
                  x="Har bir qurilmaning o‘z vazifasi bor."),
            MATCH("Rasmni qurilma nomi bilan juftlang",
                  [("🖥️", "Monitor"), ("⌨️", "Klaviatura"), ("🖱️", "Sichqoncha"), ("🖨️", "Printer"), ("🎤", "Mikrofon"),
                   ("🎧", "Quloqchin"), ("💻", "Noutbuk")], x="Qurilmalarni ko‘rinishidan tanib olamiz."),
            Q("Ekran, klaviatura va boshqa qismlar bitta korpusda bo‘lgan ko‘chma kompyuter nima deb ataladi?", "Noutbuk",
              ["Printer", "Skaner", "Karnay"], d=2,
              x="Noutbukda ekran, klaviatura va boshqa qismlar birga yig‘ilgan, uni ko‘tarib yurish mumkin.", e="💻"),
            Q("Noutbukda sichqoncha o‘rniga nimadan foydalanish mumkin?", "Sensorli panel", ["Karnay", "Veb-kamera", "Mikrofon"], d=2,
              x="Sensorli panelda barmoqni yurgizib ko‘rsatkichni boshqaramiz."),
            TF("Printer bo‘lmasa ham kompyuter ishlay oladi.", True, d=2,
               x="Printer qo‘shimcha qurilma: kompyuter usiz ham ishlayveradi."),
            TF("Veb-kamera tovush chiqaradi.", False, d=2, x="Veb-kamera tasvirni oladi, tovushni esa karnay chiqaradi."),
            Q("Qaysi qurilma bo‘lmasa, kompyuterdagi rasmni ko‘ra olmaymiz?", "Monitor", ["Karnay", "Printer", "Mikrofon"], d=2,
              x="Tasvir monitor ekranida ko‘rinadi."),
            Q("Kompyuterni yoqish uchun qaysi tugma bosiladi?", "Quvvat tugmasi", ["Probel", "Enter", "Shift"], d=2,
              x="Quvvat tugmasi kompyuterni yoqadi; stol kompyuterida u tizim blokida bo‘ladi."),
            Q("Planshet va smartfonda harf tugmalari qayerda chiqadi?", "Ekranning o‘zida", ["Tizim blokida", "Printerda", "Karnayda"], d=3,
              x="Planshet va smartfonda harflar sensorli ekranda chiqadi va barmoq bilan bosiladi.", e="📱"),
            Q("Stol kompyuterida hisob-kitobni bajaradigan “miya” — protsessor qayerda joylashgan?", "Tizim blokida",
              ["Monitorda", "Sichqonchada", "Karnayda"], d=3,
              x="Protsessor tizim bloki ichida joylashgan va barcha hisob-kitobni bajaradi."),
            ORDER("So‘zlardan gap tuzing", "Monitor rasm va matnni ko‘rsatadi", d=2),
        ])

T.topic("qurilmalar", "🖨️", L("Kiritish va chiqarish qurilmalari", "Input and output devices", "Устройства ввода и вывода"),
        chapter=C1,
        theory="Kiritish qurilmalari axborotni kompyuterga kiritadi: klaviatura, sichqoncha, mikrofon, skaner, veb-kamera.\n"
               "Chiqarish qurilmalari axborotni kompyuterdan bizga chiqaradi: monitor, printer, karnay, quloqchin.\n"
               "Eslab qoling: “kiritish” — kompyuterga, “chiqarish” — kompyuterdan.\n"
               "Masalan, mikrofonga gapirsak — kiritish, karnaydan qo‘shiq eshitsak — chiqarish.",
        items=[
            Q("Qaysi biri kiritish qurilmasi?", "Klaviatura", ["Monitor", "Printer", "Karnay", "Quloqchin"],
              x="Klaviatura orqali harflarni kompyuterga kiritamiz."),
            Q("Qaysi biri kiritish qurilmasi?", "Mikrofon", ["Karnay", "Printer", "Quloqchin", "Monitor"],
              x="Mikrofon ovozni kompyuterga kiritadi."),
            Q("Qaysi biri kiritish qurilmasi?", "Skaner", ["Printer", "Monitor", "Quloqchin", "Karnay"],
              x="Skaner qog‘ozdagi rasmni kompyuterga kiritadi."),
            Q("Qaysi biri kiritish qurilmasi?", "Sichqoncha", ["Karnay", "Monitor", "Printer", "Quloqchin"],
              x="Sichqoncha orqali kompyuterga buyruq beramiz."),
            Q("Qaysi biri chiqarish qurilmasi?", "Monitor", ["Sichqoncha", "Mikrofon", "Skaner", "Klaviatura"],
              x="Monitor axborotni kompyuterdan ekranga chiqaradi."),
            Q("Qaysi biri chiqarish qurilmasi?", "Printer", ["Klaviatura", "Veb-kamera", "Skaner", "Mikrofon"],
              x="Printer axborotni qog‘ozga chiqaradi."),
            Q("Qaysi biri chiqarish qurilmasi?", "Karnay", ["Mikrofon", "Sichqoncha", "Klaviatura", "Skaner"],
              x="Karnay tovushni kompyuterdan chiqaradi."),
            TF("Sichqoncha — kiritish qurilmasi.", True, x="Sichqoncha buyruqlarni kompyuterga kiritadi."),
            TF("Karnay — kiritish qurilmasi.", False, x="Karnay tovushni kompyuterdan chiqaradi, demak u chiqarish qurilmasi."),
            TF("Printer — chiqarish qurilmasi.", True, x="Printer axborotni kompyuterdan qog‘ozga chiqaradi."),
            TF("Mikrofon — chiqarish qurilmasi.", False, x="Mikrofon ovozni kompyuterga kiritadi, u kiritish qurilmasi."),
            TF("Quloqchin — chiqarish qurilmasi.", True, x="Quloqchin tovushni kompyuterdan bizga yetkazadi."),
            Q("Kompyuterdagi rasmni qog‘ozda ko‘rish uchun qaysi qurilma kerak?", "Printer", ["Skaner", "Mikrofon", "Klaviatura", "Veb-kamera"],
              x="Printer rasmni qog‘ozga chop etadi."),
            MATCH("Qurilmani vazifasi bilan juftlang",
                  [("Mikrofon", "Ovozni kiritadi"), ("Karnay", "Ovozni chiqaradi"), ("Skaner", "Rasmni kiritadi"),
                   ("Printer", "Rasmni qog‘ozga chiqaradi"), ("Klaviatura", "Harflarni kiritadi"), ("Monitor", "Tasvirni ko‘rsatadi")],
                  x="Kiritish qurilmasi kompyuterga, chiqarish qurilmasi kompyuterdan axborot o‘tkazadi."),
            Q("Mikrofon ovozni qayerga uzatadi?", "Kompyuterga", ["Printerga", "Skanerga", "Sichqonchaga"], d=2,
              x="Mikrofon — kiritish qurilmasi, u ovozni kompyuterga kiritadi."),
            TF("Veb-kamera — kiritish qurilmasi.", True, d=2, x="Veb-kamera tasvirni kompyuterga kiritadi."),
            TF("Skaner va printer — ikkalasi ham chiqarish qurilmasi.", False, d=2,
               x="Skaner — kiritish, printer — chiqarish qurilmasi."),
            Q("Qaysi juftlikda ikkala qurilma ham kiritish qurilmasi?", "Klaviatura va sichqoncha",
              ["Monitor va karnay", "Printer va sichqoncha", "Karnay va mikrofon"], d=2,
              x="Klaviatura ham, sichqoncha ham kompyuterga axborot kiritadi."),
            Q("Qaysi juftlikda ikkala qurilma ham chiqarish qurilmasi?", "Monitor va printer",
              ["Skaner va printer", "Mikrofon va karnay", "Klaviatura va monitor"], d=2,
              x="Monitor ekranga, printer qog‘ozga axborot chiqaradi."),
            Q("Ali videoqo‘ng‘iroqda buvisi bilan gaplashmoqda. Buvisining ovozini qaysi qurilma eshittiradi?", "Karnay",
              ["Mikrofon", "Veb-kamera", "Klaviatura"], d=2, x="Ovozni eshittiradigan chiqarish qurilmasi — karnay."),
            Q("Ali videoqo‘ng‘iroqda gapirmoqda. Uning ovozini kompyuterga qaysi qurilma kiritadi?", "Mikrofon",
              ["Karnay", "Monitor", "Printer"], d=2, x="Ovozni kompyuterga mikrofon kiritadi."),
            Q("Zarina qog‘ozga chizgan rasmini kompyuterga o‘tkazmoqchi. Unga nima kerak?", "Skaner",
              ["Printer", "Karnay", "Quloqchin"], d=2, x="Skaner qog‘ozdagi rasmni kompyuterga kiritadi."),
            Q("Sensorli ekran qanday qurilma?", "Ham kiritish, ham chiqarish", ["Faqat kiritish", "Faqat chiqarish", "Faqat tovush chiqarish"],
              d=3, x="Sensorli ekran tasvirni ko‘rsatadi va barmoq tegishini ham qabul qiladi."),
            ORDER("So‘zlardan gap tuzing", "Karnay chiqarish qurilmasi hisoblanadi", d=2),
        ])

T.topic("togri_otirish", "👀", L("Kompyuter oldida to‘g‘ri o‘tirish", "Sitting correctly at the computer", "Правильная посадка за компьютером"),
        chapter=C1,
        theory="Kompyuter oldida sog‘lom bo‘lish qoidalari:\n"
               "• Orqani tik tutib o‘tiring, oyoqlar polda tursin.\n"
               "• Ko‘zdan ekrangacha kamida 50 sm bo‘lsin, ekran ko‘z balandligida yoki biroz pastda tursin.\n"
               "• Xona yorug‘ bo‘lsin; vaqti-vaqti bilan tanaffus qilib, ko‘zga dam bering: uzoqqa qarang, ko‘zni yumib oching.\n"
               "• Ho‘l qo‘l bilan kompyuterga tegmang, simlarni tortmang, kompyuter yonida ovqat yemang.",
        items=[
            Q("Kompyuter oldida qanday o‘tirish kerak?", "Orqani tik tutib", ["Egilib, bukchayib", "Oyoqni stolga qo‘yib", "Yonboshlab yotib"],
              x="Orqa tik bo‘lsa, umurtqa pog‘onasi charchamaydi."),
            Q("Ko‘zdan ekrangacha masofa qancha bo‘lishi kerak?", "Kamida 50 sm", ["5 sm", "10 sm", "20 sm"],
              x="Ekranga juda yaqin o‘tirish ko‘zni charchatadi."),
            TF("Ho‘l qo‘l bilan kompyuterga tegish mumkin.", False, x="Suv tokni o‘tkazadi, bu juda xavfli."),
            TF("Kompyuter yonida choy ichish mumkin emas.", True, x="Choy to‘kilsa, klaviatura va kompyuter buzilishi mumkin."),
            Q("Ko‘z charchasa nima qilish kerak?", "Uzoqqa qarab dam olish", ["Ekranga yaqinroq borish", "Ko‘zni qattiq ishqalash", "Xonani qorong‘i qilish"],
              x="Uzoqqa qarash va ko‘zni yumib ochish ko‘zga dam beradi."),
            TF("Qorong‘i xonada kompyuterda o‘ynash ko‘z uchun foydali.", False,
               x="Qorong‘ida yorug‘ ekran ko‘zni tez charchatadi, xona yorug‘ bo‘lishi kerak."),
            Q("Kompyuter oldida o‘tirganda oyoqlar qayerda bo‘lishi kerak?", "Polda", ["Stol ustida", "Stul ustida bukilgan", "Havoda osilib"],
              x="Oyoqlar polda tursa, gavda to‘g‘ri va qulay turadi."),
            TF("Kompyuter simlarini tortish xavfli.", True, x="Sim uzilib ketsa yoki rozetkadan chiqsa, tok urishi mumkin."),
            TF("Kompyuter buzilsa, uni o‘zim ochib tuzatishim kerak.", False,
               x="Buzilgan kompyuterni faqat kattalar yoki usta tekshiradi."),
            Q("Kompyuterdan kuygan hid kelsa nima qilasiz?", "Kattalarga aytaman", ["O‘ynashda davom etaman", "Ichini ochaman", "Suv sepaman"],
              x="Bunday paytda darhol o‘qituvchi yoki ota-onaga aytish kerak."),
            Q("Ekran qayerda turgani to‘g‘ri?", "Ko‘z balandligida", ["Boshdan ancha yuqorida", "Tizza balandligida", "Polda"],
              x="Ekran ko‘z balandligida yoki biroz pastroqda bo‘lsa, bo‘yin charchamaydi."),
            TF("Uzoq vaqt kompyuterda o‘tirganda tanaffus qilish kerak.", True, x="Tanaffusda ko‘z va gavda dam oladi."),
            TF("Kompyuterda to‘xtovsiz bir necha soat o‘ynash foydali.", False,
               x="Uzoq o‘tirish ko‘z va gavdaga zarar, tanaffus kerak."),
            MATCH("Qoidani foydasi bilan juftlang",
                  [("Tanaffus qilish", "Ko‘z dam oladi"), ("Orqani tik tutish", "Umurtqa charchamaydi"),
                   ("Quruq qo‘l bilan ishlash", "Tok urishidan saqlaydi"), ("Yonida ovqat yemaslik", "Klaviatura toza turadi"),
                   ("Xonani yorug‘ qilish", "Ko‘z zo‘riqmaydi")], d=2,
                  x="Har bir qoida sog‘lig‘imizni yoki kompyuterni asraydi."),
            Q("Klaviaturada yozganda qo‘llar qanday turishi kerak?", "Erkin, tirsakdan bukilgan",
              ["Yelkadan baland ko‘tarilgan", "Qattiq taranglashgan", "Stol chetiga osilgan"], d=2,
              x="Qo‘llar erkin tursa, bilak va yelka charchamaydi."),
            Q("Nima uchun ekranga juda yaqin o‘tirmaslik kerak?", "Ko‘z tez charchaydi", ["Ekran buziladi", "Kompyuter o‘chadi", "Sichqoncha ishlamaydi"], d=2,
              x="Yaqin masofada ko‘z ko‘proq zo‘riqadi."),
            Q("Ko‘z mashqi uchun nima qilish mumkin?", "Ko‘zni yumib ochish", ["Ekranga tikilib turish", "Ko‘zni ishqalash", "Qorong‘ida o‘qish"], d=2,
              x="Ko‘zni yumib ochish, uzoq va yaqinga navbat bilan qarash ko‘zga dam beradi."),
            TF("Ekranga uzoq tikilganda ko‘z quriydi va charchaydi.", True, d=2,
               x="Ekranga tikilganda ko‘zni kam pirpiratamiz, shuning uchun u quriydi."),
            Q("Kompyuter xonasida qanday yurish kerak?", "Tinch, yugurmasdan", ["Yugurib, sakrab", "Simlardan hatlab o‘ynab", "Stullarni surib"], d=2,
              x="Yugurganda simga ilinib, qurilmani tushirib yuborish mumkin."),
            Q("Qaysi odat ko‘z uchun zararli?", "Yotib telefon o‘ynash", ["Uzoqqa qarab dam olish", "Yorug‘ xonada ishlash", "Tanaffus qilish"], d=2,
              x="Yotgan holda ekran ko‘zga juda yaqin va qiyshiq turadi, bu ko‘zni charchatadi."),
            Q("Stulning balandligi qanday bo‘lishi kerak?", "Oyoq polga yetadigan", ["Oyoq osilib qoladigan", "Stoldan baland", "Tizza iyakka tegadigan"], d=3,
              x="Oyoq polga tegsa, gavda to‘g‘ri va barqaror turadi."),
            ORDER("So‘zlardan gap tuzing", "Ekranga juda yaqin o‘tirmang", d=2),
            ORDER("So‘zlardan gap tuzing", "Ho‘l qo‘l bilan kompyuterga tegmang", d=3),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["kompyuter", "qurilmalar", "togri_otirish"], chapter=C1)

# ============================================================ 2-chorak
T.topic("sichqoncha", "🖱️", L("Sichqoncha bilan ishlash", "Using the mouse", "Работа с мышью"),
        chapter=C2,
        theory="Sichqonchada chap va o‘ng tugma hamda g‘ildirakcha bor.\n"
               "• Bosish — chap tugmani bir marta bosib qo‘yib yuborish: belgini tanlaydi.\n"
               "• Ikki marta bosish — chap tugmani tez-tez ikki marta bosish: dastur yoki papkani ochadi.\n"
               "• Sudrab o‘tkazish — chap tugmani bosib turib sichqonchani surish, keyin qo‘yib yuborish.\n"
               "• O‘ng tugma — qo‘shimcha buyruqlar ro‘yxatini (menyu) ochadi; g‘ildirakcha sahifani yuqori-pastga suradi.",
        items=[
            Q("Papkani ochish uchun sichqoncha chap tugmasini necha marta bosamiz?", "Ikki marta", ["Bir marta", "Uch marta", "Besh marta"],
              x="Belgini chap tugma bilan ikki marta tez bosish uni ochadi."),
            Q("Sichqonchaning nechta asosiy tugmasi bor?", "2 ta", ["1 ta", "5 ta", "10 ta"],
              x="Sichqonchada chap va o‘ng tugma, o‘rtasida g‘ildirakcha bo‘ladi."),
            Q("Sahifani yuqoriga va pastga surish uchun sichqonchaning qaysi qismi ishlatiladi?", "G‘ildirakcha", ["Sim", "O‘ng tugma", "Sichqonchaning tagi"],
              x="G‘ildirakchani aylantirsak, sahifa yuqori yoki pastga suriladi."),
            TF("Sichqonchani stolda sursak, ekrandagi ko‘rsatkich ham suriladi.", True,
               x="Ko‘rsatkich sichqoncha bilan birga harakatlanadi."),
            TF("Qo‘shimcha menyu sichqonchaning o‘ng tugmasi bilan ochiladi.", True,
               x="O‘ng tugma bosilganda buyruqlar ro‘yxati — menyu chiqadi."),
            Q("Belgini boshqa joyga ko‘chirish uchun nima qilamiz?", "Sudrab o‘tkazamiz", ["Ikki marta bosamiz", "G‘ildirakchani aylantiramiz", "O‘ng tugmani bosamiz"],
              x="Chap tugmani bosib turib sursak, belgi yangi joyga o‘tadi."),
            Q("Belgini tanlash uchun chap tugmani necha marta bosamiz?", "1 marta", ["2 marta", "3 marta", "5 marta"],
              x="Bir marta bosish belgini tanlaydi — u ajralib ko‘rinadi."),
            TF("Sudrab o‘tkazishda chap tugma bosib turiladi.", True, x="Tugma qo‘yib yuborilganda belgi yangi joyda qoladi."),
            TF("Sichqonchaning g‘ildirakchasi sahifani suradi.", True, x="G‘ildirakcha uzun sahifani ko‘rishga yordam beradi."),
            TF("Sichqoncha — chiqarish qurilmasi.", False, x="Sichqoncha buyruqlarni kompyuterga kiritadi, u kiritish qurilmasi."),
            MATCH("Harakatni natijasi bilan juftlang",
                  [("Bir marta bosish", "Belgini tanlaydi"), ("Ikki marta bosish", "Papkani ochadi"), ("Sudrab o‘tkazish", "Belgini ko‘chiradi"),
                   ("O‘ng tugmani bosish", "Menyuni ochadi"), ("G‘ildirakchani aylantirish", "Sahifani suradi")],
                  x="Sichqonchaning har bir harakati o‘z ishini bajaradi."),
            Q("Ekranda sichqoncha bilan birga yuradigan kichik strelka nima deb ataladi?", "Ko‘rsatkich", ["Belgi", "Oyna", "Papka"],
              x="Ko‘rsatkich (kursor) sichqoncha bilan birga harakatlanadi."),
            Q("Sichqoncha qanday sirt ustida yaxshi ishlaydi?", "Tekis gilamcha ustida", ["Suv ichida", "Qum ustida", "Havoda"],
              x="Sichqoncha tekis sirtda yaxshi suriladi, uning uchun maxsus gilamcha bor."),
            Q("Chap tugma bosib turilganda sichqoncha surilsa, bu nima deyiladi?", "Sudrab o‘tkazish", ["Ikki marta bosish", "Bir marta bosish", "Aylantirish"], d=2,
              x="Sudrab o‘tkazishda tugma qo‘yib yuborilmaydi."),
            Q("Ikki marta bosish qanday bajariladi?", "Chap tugmani tez-tez ikki marta", ["O‘ng tugmani sekin ikki marta", "G‘ildirakchani ikki marta aylantirib", "Ikkala tugmani birga"], d=2,
              x="Ikki bosish orasida oraliq bo‘lmasligi kerak."),
            TF("Ikki marta bosishda tugmani sekin, katta oraliq bilan bosish kerak.", False, d=2,
               x="Oraliq katta bo‘lsa, kompyuter buni ikkita alohida bosish deb tushunadi."),
            Q("Zarina rasmni savatga olib tashlamoqchi. U qaysi usuldan foydalanadi?", "Sudrab o‘tkazish",
              ["G‘ildirakchani aylantirish", "Bir marta bosish", "Ikki marta bosish"], d=2,
              x="Belgini chap tugma bilan bosib turib savat ustiga sudrab olib borish mumkin."),
            Q("O‘ng tugma bosilganda ochiladigan buyruqlar ro‘yxati nima deb ataladi?", "Menyu", ["Papka", "Fayl", "Savat"], d=2,
              x="Menyuda tanlash mumkin bo‘lgan buyruqlar ro‘yxati bor."),
            TF("Sichqonchasiz noutbukda sensorli panel bilan ishlash mumkin.", True, d=2,
               x="Sensorli panel sichqoncha vazifasini bajaradi."),
            Q("Simsiz sichqoncha nima bilan ishlaydi?", "Batareya bilan", ["Suv bilan", "Qog‘oz bilan", "Benzin bilan"], d=2,
              x="Simsiz sichqoncha ichida kichik batareya bo‘ladi."),
            Q("Internet sahifasida ko‘rsatkich qo‘l shakliga o‘tsa, bu nimani bildiradi?", "Havolani bosish mumkin",
              ["Kompyuter o‘chmoqda", "Sichqoncha buzildi", "Sahifa tugadi"], d=3,
              x="Qo‘l shaklidagi ko‘rsatkich bosiladigan havola ustida paydo bo‘ladi."),
            Q("Kompyuter band bo‘lib, kutish kerak bo‘lganda ko‘rsatkich qanday ko‘rinadi?", "Aylanayotgan doira", ["Qo‘l", "Yulduzcha", "Yurakcha"], d=3,
              x="Aylanayotgan doira kompyuter ish bajarayotganini, biroz kutish kerakligini bildiradi."),
            ORDER("So‘zlardan gap tuzing", "Papkani ikki marta bosib oching", d=2),
        ])

T.topic("klaviatura", "⌨️", L("Klaviatura tugmalari", "Keyboard keys", "Клавиши клавиатуры"),
        chapter=C2,
        theory="Klaviaturada harf, raqam va maxsus tugmalar bor.\n"
               "• Probel — eng uzun tugma, so‘zlar orasiga bo‘sh joy qo‘yadi.\n"
               "• Enter — yangi qatorga o‘tkazadi yoki buyruqni tasdiqlaydi.\n"
               "• Backspace — kursordan chapdagi belgini, Delete — o‘ngdagi belgini o‘chiradi.\n"
               "• Shift — bosib turib harf bossak, bosh harf chiqadi; Caps Lock yoqilsa, hamma harflar bosh harf bo‘ladi.",
        items=[
            Q("Klaviaturadagi eng uzun tugma qaysi?", "Probel", ["Enter", "Shift", "Backspace"],
              x="Probel — so‘zlar orasiga bo‘sh joy qo‘yadigan eng uzun tugma."),
            Q("So‘zlar orasiga bo‘sh joy qo‘yish uchun qaysi tugma bosiladi?", "Probel", ["Enter", "Caps Lock", "Shift", "Delete"],
              x="Probel bo‘sh joy qo‘yadi."),
            Q("Yangi qatorga o‘tish uchun qaysi tugma bosiladi?", "Enter", ["Probel", "Shift", "Caps Lock", "Backspace"],
              x="Enter kursorni yangi qatorga o‘tkazadi."),
            Q("Kursordan chapdagi harfni o‘chirish uchun qaysi tugma bosiladi?", "Backspace", ["Enter", "Probel", "Shift", "Caps Lock"],
              x="Backspace kursordan chapdagi belgini o‘chiradi."),
            Q("Bitta bosh harf yozish uchun qaysi tugma bosib turiladi?", "Shift", ["Enter", "Probel", "Backspace", "Delete"],
              x="Shift bosib turilganda harf bosh harf bo‘lib yoziladi."),
            Q("Hamma harflarni bosh harf bilan yozish uchun qaysi tugma yoqiladi?", "Caps Lock", ["Backspace", "Enter", "Probel", "Delete"],
              x="Caps Lock yoqilsa, barcha harflar bosh harf bo‘ladi."),
            TF("Enter tugmasi harfni o‘chiradi.", False, x="Harfni Backspace yoki Delete o‘chiradi, Enter esa yangi qatorga o‘tkazadi."),
            TF("Probel so‘zlar orasiga bo‘sh joy qo‘yadi.", True, x="Probel — bo‘sh joy tugmasi."),
            TF("Klaviaturada raqam tugmalari ham bor.", True, x="Raqamlar harflar ustidagi qatorda joylashgan."),
            MATCH("Tugmani vazifasi bilan juftlang",
                  [("Probel", "Bo‘sh joy qo‘yadi"), ("Enter", "Yangi qatorga o‘tkazadi"), ("Backspace", "Chapdagi belgini o‘chiradi"),
                   ("Shift", "Bosh harf yozadi"), ("Caps Lock", "Doimiy bosh harfni yoqadi"), ("Delete", "O‘ngdagi belgini o‘chiradi")],
                  x="Har bir maxsus tugmaning o‘z vazifasi bor."),
            Q("Klaviaturada raqamlar qatori qayerda joylashgan?", "Harflar ustida", ["Probel tagida", "Faqat chap chetda", "Klaviaturada raqam yo‘q"],
              x="Raqamlar qatori harf tugmalari ustida; ko‘p klaviaturalarda o‘ng tomonda ham raqamlar bloki bor."),
            Q("Matnda harf qayerga yozilishini ko‘rsatuvchi miltillovchi chiziq nima?", "Kursor", ["Probel", "Papka", "Belgi"],
              x="Kursor — miltillab turadigan kichik chiziq, harf shu yerga yoziladi."),
            Q("Caps Lock yoqilganda “olma” so‘zi qanday yoziladi?", "OLMA", ["olma", "Olma", "oLMA"], d=2,
              x="Caps Lock yoqilsa, hamma harflar bosh harf bo‘lib yoziladi."),
            Q("Shift bosib turilib “a” tugmasi bosilsa, ekranda nima chiqadi?", "A", ["a", "1", "Bo‘sh joy"], d=2,
              x="Shift bilan harf bosh harf bo‘lib chiqadi."),
            Q("Kursordan o‘ngdagi belgini qaysi tugma o‘chiradi?", "Delete", ["Backspace", "Enter", "Shift"], d=2,
              x="Delete o‘ngdagi, Backspace chapdagi belgini o‘chiradi."),
            Q("Kursorni chapga, o‘ngga, yuqoriga va pastga suradigan tugmalar qanday ataladi?", "Strelkali tugmalar",
              ["Raqam tugmalari", "Harf tugmalari", "Probel tugmalari"], d=2,
              x="Strelkali tugmalarda yo‘nalish belgisi chizilgan."),
            TF("Caps Lock yoqilgan bo‘lsa, barcha harflar kichik harf bilan yoziladi.", False, d=2,
               x="Aksincha: Caps Lock yoqilganda harflar bosh harf bo‘ladi."),
            TF("Klaviaturada ikkita Shift tugmasi bor: chapda va o‘ngda.", True, d=2,
               x="Ikkala qo‘l bilan qulay ishlash uchun Shift ikki tomonda joylashgan."),
            Q("“Kitobb” deb xato yozdingiz, kursor so‘z oxirida. Ortiqcha “b” ni qaysi tugma o‘chiradi?", "Backspace",
              ["Enter", "Shift", "Caps Lock", "Delete"], d=2,
              x="Backspace kursordan chapdagi, ya’ni oxirgi yozilgan harfni o‘chiradi; Delete esa o‘ngdagini o‘chiradi, o‘ngda esa hech narsa yo‘q."),
            Q("Klaviaturadagi yuqori harflar qatori qaysi harflar bilan boshlanadi?", "Q W E R T Y",
              ["A B C D E F", "Z X C V B N", "O P A S D F"], d=3,
              x="Ko‘p klaviaturalarda yuqori harflar qatori Q, W, E, R, T, Y harflari bilan boshlanadi."),
            Q("Qaysi ikki harf tugmasida barmoq sezadigan bo‘rtiqcha bor?", "F va J", ["A va B", "Q va P", "X va O"], d=3,
              x="F va J dagi bo‘rtiqchalar qaramasdan barmoqlarni to‘g‘ri qo‘yishga yordam beradi."),
            Q("Buyruqni bekor qilish yoki oynadan chiqish uchun ko‘pincha qaysi tugma bosiladi?", "Esc", ["Enter", "Probel", "Shift"], d=3,
              x="Esc — inglizcha “escape”, ya’ni “chiqib ketish” so‘zidan olingan."),
            Q("Undov belgisi “!” ni yozish uchun 1 raqami tugmasi bilan birga qaysi tugma bosib turiladi?", "Shift",
              ["Enter", "Probel", "Backspace"], d=3,
              x="Raqam tugmalari ustidagi belgilar Shift bilan yoziladi: Shift va 1 — undov belgisi."),
            ORDER("So‘zlardan gap tuzing", "Enter yangi qatorga o‘tkazadi"),
        ])

_typing = [
    Q("Kompyuterda matn yozadigan dastur qanday ataladi?", "Matn muharriri", ["Kalkulyator", "O‘yin", "Soat", "Pleyer"],
      x="Matn muharriri — matn yozish va tuzatish dasturi, masalan, Bloknot yoki Word."),
    Q("Gap qanday harf bilan boshlanadi?", "Bosh harf bilan", ["Kichik harf bilan", "Raqam bilan", "Nuqta bilan"],
      x="Har bir gap bosh harf bilan boshlanadi."),
    TF("So‘zlar orasiga bitta Probel qo‘yiladi.", True, x="Bitta bo‘sh joy yetarli, ortiqchasi kerak emas."),
    TF("Darak gap oxiriga nuqta qo‘yiladi.", True, x="Darak gap nuqta bilan tugaydi."),
    Q("Xato yozilgan harfni qaysi tugma bilan o‘chiramiz?", "Backspace", ["Enter", "Shift", "Probel"],
      x="Backspace kursordan chapdagi harfni o‘chiradi."),
    Q("Qaysi dastur matn yozish uchun mo‘ljallangan?", "Word", ["Paint", "Kalkulyator", "Pleyer"],
      x="Word — matn muharriri, Paint esa rasm chizish dasturi."),
    Q("Ism qanday yoziladi?", "Bosh harf bilan", ["Faqat raqam bilan", "Kichik harf bilan", "Nuqta bilan boshlab"],
      x="Ismlar doim bosh harf bilan yoziladi: Ali, Zarina."),
    Q("Terilgan matn qayerda ko‘rinadi?", "Monitor ekranida", ["Printer ichida", "Sichqonchada", "Karnayda"],
      x="Terilgan harflar darhol ekranda paydo bo‘ladi."),
    TF("Vergul va nuqtadan keyin Probel qo‘yiladi.", True, d=2,
       x="Tinish belgisi oldingi so‘zga yopishib yoziladi, undan keyin bo‘sh joy qo‘yiladi."),
    TF("Verguldan oldin Probel qo‘yiladi.", False, d=2, x="Vergul oldingi so‘zga yopishtirib yoziladi."),
    Q("Qaysi gap to‘g‘ri terilgan?", "Men kitob o‘qiyman.", ["men kitob o‘qiyman.", "Men kitob o‘qiyman .", "Menkitob o‘qiyman."], d=2,
      x="Gap bosh harf bilan boshlanadi, so‘zlar orasida bitta bo‘sh joy, nuqta so‘zga yopishgan."),
    Q("Qaysi gap to‘g‘ri terilgan?", "Bugun havo issiq.", ["bugun havo issiq.", "Bugun havo issiq .", "Bugunhavo issiq."], d=2,
      x="Bosh harf, so‘zlar orasida bo‘sh joy va oxirida yopishgan nuqta — to‘g‘ri."),
    Q("She’rning har bir misrasini yangi qatordan yozish uchun qaysi tugma bosiladi?", "Enter", ["Probel", "Shift", "Delete"], d=2,
      x="Enter bosilganda kursor yangi qatorga o‘tadi."),
    Q("“ali” deb yozildi. Ismni to‘g‘ri yozish uchun nima qilish kerak?", "“A” ni Shift bilan yozish",
      ["Oxiriga nuqta qo‘yish", "Probel bosish", "Enter bosish"], d=2,
      x="Ism bosh harf bilan yoziladi: Shift bosib turib “a” ni bossak, “A” chiqadi."),
    TF("Matnni terib bo‘lgach, uni saqlab qo‘yish kerak.", True, d=2,
       x="Saqlanmagan matn dastur yopilganda yo‘qolib qolishi mumkin."),
    Q("Matnni qog‘ozga chiqarish uchun nima qilinadi?", "Printerda chop etiladi", ["Skanerga qo‘yiladi", "Mikrofonga aytiladi", "Karnay yoqiladi"], d=2,
      x="Printer matnni qog‘ozga chop etadi."),
    ORDER("So‘zlardan gap tuzing", "Gap bosh harf bilan boshlanadi"),
]
for word in ["olma", "bola", "kitob", "qalam", "daftar", "maktab", "kompyuter"]:
    n = len(word)
    _typing.append(Q(f"“{word}” so‘zini terish uchun nechta harf tugmasi bosiladi?", n, near(n, [n - 1, n + 1, n + 2, n - 2], lo=1),
                     d=1 if n <= 5 else 2, x=f"“{word}” so‘zida {n} ta harf bor, har bir harf uchun bitta tugma bosiladi."))
for sent in ["Men maktabga boraman", "Ali kitob o‘qiydi", "Bugun havo juda issiq", "Biz kompyuterda rasm chizamiz",
             "Zarina daftarga chiroyli qilib yozdi"]:
    n = len(sent.split()) - 1
    _typing.append(Q(f"“{sent}.” gapini terishda Probel necha marta bosiladi?", n, near(n, [n + 1, n - 1, n + 2, n + 3], lo=1),
                     d=1 if n <= 2 else 2, x=f"Gapda {n + 1} ta so‘z bor, ular orasida {n} ta bo‘sh joy bo‘ladi."))

T.topic("matn_terish", "✏️", L("Matn terish", "Typing text", "Набор текста"),
        chapter=C2,
        theory="Matnni kompyuterda yozish uchun matn muharriridan foydalanamiz, masalan, Bloknot yoki Word.\n"
               "• Gap bosh harf bilan boshlanadi — buning uchun Shift bosib turiladi.\n"
               "• So‘zlar orasiga bitta Probel qo‘yiladi; vergul va nuqta so‘zga yopishib yoziladi, ulardan keyin Probel qo‘yiladi.\n"
               "• Xato harfni Backspace bilan o‘chirib, qaytadan yozamiz; yangi qatorni Enter boshlaydi.\n"
               "Misol: “Men kitob o‘qiyman.” — 3 ta so‘z, 2 ta Probel.",
        items=_typing)

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["sichqoncha", "klaviatura", "matn_terish"], chapter=C2)

# ============================================================ 3-chorak
T.topic("ish_stoli", "💻", L("Ish stoli, belgi va oyna", "Desktop, icons and windows", "Рабочий стол, значки и окна"),
        chapter=C3,
        theory="Kompyuter yoqilganda ekranda ish stoli ko‘rinadi.\n"
               "• Belgi (ikonka) — dastur, papka yoki faylning kichik rasmi. Uni ikki marta bossak, ochiladi.\n"
               "• Ekran pastidagi yo‘lak — vazifalar paneli: unda Pusk tugmasi, ochiq dasturlar va soat bor.\n"
               "• Dastur ochilganda oyna paydo bo‘ladi. Oyna tepasidagi tugmalar: “—” yig‘adi, “□” butun ekranga yoyadi, “×” yopadi.\n"
               "• O‘chirilgan fayllar avval savatga tushadi.",
        items=[
            Q("Kompyuter yoqilganda ko‘rinadigan asosiy ekran nima deb ataladi?", "Ish stoli", ["Tizim bloki", "Klaviatura", "Karnay"],
              x="Ish stoli — belgilar joylashgan asosiy ekran."),
            Q("Dastur yoki papkani ifodalovchi kichik rasm nima deb ataladi?", "Belgi", ["Oyna", "Kursor", "Probel"],
              x="Belgi (ikonka) orqali dastur va papkalarni ochamiz."),
            Q("Oynani yopish uchun qaysi tugma bosiladi?", "×", ["—", "□", "Probel"],
              x="× belgili tugma oynani yopadi."),
            TF("Belgini ikki marta bossak, u ochiladi.", True, x="Ikki marta bosish dastur yoki papkani ochadi."),
            Q("Ish stolining pastidagi uzun yo‘lak odatda nima deb ataladi?", "Vazifalar paneli", ["Sarlavha qatori", "Savat", "Papka"],
              x="Vazifalar panelida Pusk tugmasi, ochiq dasturlar va soat joylashgan."),
            Q("O‘chirilgan fayllar avval qayerga tushadi?", "Savatga", ["Printerga", "Monitorga", "Karnayga"],
              x="Savatdan faylni qaytarib olish ham mumkin.", e="🗑️"),
            TF("Kompyuterda bir vaqtda bir nechta oyna ochish mumkin.", True, x="Masalan, rasm chizib turib, musiqa ham tinglash mumkin."),
            TF("Ish stolida belgilar joylashadi.", True, x="Ish stolida dastur, papka va fayl belgilari bo‘ladi."),
            MATCH("Oyna qismini vazifasi bilan juftlang",
                  [("×", "Oynani yopadi"), ("—", "Oynani yig‘adi"), ("□", "Butun ekranga yoyadi"),
                   ("Sarlavha qatori", "Oyna nomini ko‘rsatadi"), ("Aylantirish yo‘lagi", "Oyna ichini suradi")],
                  x="Oyna tugmalari uning ko‘rinishini boshqaradi."),
            ORDER("So‘zlardan gap tuzing", "Belgini ikki marta bosing"),
            Q("Ish stolining orqa tomonida ko‘rinadigan chiroyli rasm qanday ataladi?", "Fon rasmi", ["Belgi", "Kursor", "Savat"],
              x="Fon rasmini o‘zimiz yoqtirgan rasmga almashtirish mumkin."),
            Q("Vazifalar panelining o‘ng tomonida odatda nima ko‘rinadi?", "Soat va sana", ["Savat", "Klaviatura", "Printer"], d=2,
              x="Vazifalar panelining o‘ng chetida soat va sana turadi."),
            TF("“—” tugmasi bosilganda dastur butunlay yopiladi.", False, d=2,
               x="Yig‘ilgan oyna vazifalar paneliga yashirinadi, dastur esa ishlashda davom etadi."),
            TF("Oynani butun ekranga yoyish uchun “□” tugmasi bosiladi.", True, d=2, x="“□” oynani butun ekranga yoyadi."),
            Q("Oyna nomi yozilgan eng yuqori qator nima deb ataladi?", "Sarlavha qatori", ["Vazifalar paneli", "Savat", "Probel"], d=2,
              x="Sarlavha qatorida dastur yoki fayl nomi yoziladi."),
            Q("Savatdagi faylni qaytarib olish mumkinmi?", "Ha, savat tozalanmaguncha", ["Yo‘q, hech qachon", "Faqat printer bilan", "Faqat ertasiga"], d=2,
              x="Savat tozalanmagan bo‘lsa, faylni qayta tiklash mumkin."),
            Q("Pusk tugmasi qayerda joylashgan?", "Vazifalar panelida", ["Oyna ichida", "Savatda", "Sarlavha qatorida"], d=2,
              x="Pusk tugmasi vazifalar panelida turadi."),
            Q("Pusk tugmasi bosilganda nima ochiladi?", "Dasturlar ro‘yxati", ["Printer", "Savat tozalanadi", "Kompyuter buziladi"], d=2,
              x="Pusk menyusidan kerakli dasturni topib ochish mumkin."),
            Q("Ish stolidagi belgini sudrab qayerga olib borsak, u o‘chiriladi?", "Savatga", ["Soatga", "Pusk tugmasiga", "Fon rasmiga"], d=2,
              x="Savatga sudralgan belgi o‘chiriladi."),
            Q("Kompyuterni to‘g‘ri o‘chirish qanday bajariladi?", "Pusk menyusi orqali", ["Simini sug‘urib", "Faqat monitorni o‘chirib", "Tizim blokini urib"], d=2,
              x="Simini tortib o‘chirish kompyuter va undagi fayllarga zarar yetkazishi mumkin."),
            Q("Ochiq dasturlar belgisi qayerda ko‘rinadi?", "Vazifalar panelida", ["Savatda", "Fon rasmida", "Klaviaturada"], d=2,
              x="Vazifalar panelidagi belgini bossak, o‘sha oyna oldinga chiqadi."),
            Q("Oynada ko‘p matn bo‘lsa, pastini ko‘rish uchun nima qilamiz?", "G‘ildirakchani aylantiramiz", ["Oynani yopamiz", "Enterni bosamiz", "Kompyuterni o‘chiramiz"], d=2,
              x="G‘ildirakcha yoki aylantirish yo‘lagi oyna ichini suradi."),
            Q("Oynani ekranning boshqa joyiga ko‘chirish uchun uning qayeridan sudraymiz?", "Sarlavha qatoridan", ["× tugmasidan", "Oyna ichidagi matndan", "Vazifalar panelidan"], d=3,
              x="Sarlavha qatorini bosib turib sursak, oyna yangi joyga ko‘chadi."),
        ])

T.topic("fayl_papka", "📁", L("Fayl va papka", "Files and folders", "Файлы и папки"),
        chapter=C3,
        theory="Fayl — kompyuterda saqlanadigan ma’lumot: rasm, matn, qo‘shiq yoki video. Har bir faylning nomi bor.\n"
               "Papka — fayllarni tartib bilan saqlaydigan joy, xuddi daftarlar solinadigan sumka kabi.\n"
               "• Papka ichida fayl ham, boshqa papka ham bo‘lishi mumkin.\n"
               "• Yangi papka yaratish: ish stolida o‘ng tugmani bosib, menyudan yangi papka buyrug‘ini tanlaymiz, nomini yozib, Enter bosamiz.\n"
               "• Keraksiz faylni tanlab Delete bossak, u savatga tushadi.",
        items=[
            Q("Fayllarni tartib bilan saqlash uchun nima yaratiladi?", "Papka", ["Printer", "Karnay", "Klaviatura"],
              x="Papkada o‘xshash fayllarni bir joyga yig‘amiz."),
            TF("Papka ichida boshqa papka bo‘lishi mumkin.", True, x="Masalan, “Rasmlar” papkasi ichida “Bayram” papkasi bo‘lishi mumkin."),
            TF("Har bir faylning nomi bor.", True, x="Faylni nomi bo‘yicha topamiz."),
            Q("Qaysi biri kompyuterda fayl bo‘la oladi?", "Rasm", ["Stol", "Sichqoncha", "Stul"],
              x="Rasm, matn, qo‘shiq, video kompyuterda fayl bo‘lib saqlanadi."),
            Q("Kompyuterdagi papka nimaga o‘xshaydi?", "Narsalar solinadigan qutiga", ["Chiroqqa", "Suvga", "Soatga"],
              x="Qutiga narsalarni solgandek, papkaga fayllarni joylaymiz."),
            Q("Keraksiz faylni o‘chirish uchun qaysi tugma bosiladi?", "Delete", ["Enter", "Shift", "Caps Lock"],
              x="Faylni tanlab Delete tugmasini bossak, u savatga tushadi."),
            TF("Faylni o‘chirsak, u avval savatga tushadi.", True, x="Savat tozalanmaguncha faylni qaytarish mumkin."),
            Q("Qo‘shiq kompyuterda qanday saqlanadi?", "Fayl bo‘lib", ["Qog‘ozga yozilib", "Printer ichida", "Saqlab bo‘lmaydi"],
              x="Qo‘shiq, rasm va video kompyuterda fayl sifatida saqlanadi."),
            Q("Papkani ochish uchun nima qilamiz?", "Ikki marta bosamiz", ["O‘ng tugmani bosamiz", "Savatga sudraymiz", "Delete bosamiz"],
              x="Papka belgisini ikki marta bossak, u ochiladi."),
            TF("Fayl faqat rasm bo‘lishi mumkin.", False, x="Fayl matn, qo‘shiq, video yoki dastur ham bo‘lishi mumkin."),
            MATCH("Faylni mos papka bilan juftlang",
                  [("Dengiz rasmi", "Rasmlar"), ("Bolalar qo‘shig‘i", "Musiqa"), ("Multfilm", "Videolar"),
                   ("Ertak matni", "Hujjatlar"), ("Shaxmat o‘yini", "O‘yinlar")],
                  x="O‘xshash fayllarni bitta papkaga yig‘sak, ularni tez topamiz."),
            ORDER("So‘zlardan gap tuzing", "Papkada fayllar saqlanadi"),
            Q("Fayl yoki papkaning nomini o‘zgartirish menyusini ochish uchun sichqonchaning qaysi tugmasi bosiladi?", "O‘ng tugma",
              ["G‘ildirakcha", "Chap tugma ikki marta", "Quvvat tugmasi"], d=2,
              x="O‘ng tugma menyusida nomini o‘zgartirish buyrug‘i bor."),
            Q("Faylni bir papkadan boshqasiga qanday o‘tkazish mumkin?", "Sudrab o‘tkazib", ["Ikki marta bosib", "Enter bosib", "Probel bosib"], d=2,
              x="Faylni bosib turib boshqa papka ustiga sudrab olib boramiz."),
            TF("Bitta papkada mutlaqo bir xil nomli ikkita faylni saqlab bo‘lmaydi.", True, d=2,
               x="Bir papkada har bir fayl nomi boshqacha bo‘lishi kerak, aks holda kompyuter ularni ajrata olmaydi."),
            Q("Zarina rasmlarini bir joyda saqlamoqchi. U nima qilishi kerak?", "“Rasmlar” papkasini yaratishi",
              ["Rasmlarni o‘chirishi", "Printerni yoqishi", "Kompyuterni o‘chirishi"], d=2,
              x="Papka yaratib, barcha rasmlarni unga joylash qulay."),
            Q("Fayl nomi qanday bo‘lgani yaxshi?", "Mazmuniga mos", ["Ma’nosiz harflar", "Juda uzun gap", "Faqat belgilar"], d=2,
              x="“Mening mushugim” degan nom “aaa123” dan ko‘ra tushunarli."),
            TF("Savat tozalangandan keyin undagi fayllar butunlay o‘chadi.", True, d=2,
               x="Savat tozalansa, fayllarni oddiy yo‘l bilan qaytarib bo‘lmaydi."),
            Q("Faylni savatga sudrasak, nima bo‘ladi?", "Fayl o‘chiriladi", ["Fayl chop etiladi", "Fayl ochiladi", "Fayl ikkiga ko‘payadi"], d=2,
              x="Savatga tushgan fayl o‘chirilgan hisoblanadi."),
            Q("Qaysi biri papka nomi uchun eng mos?", "Uy vazifalari", ["qwrt", "!!!!", "1a2b3c"], d=2,
              x="Papka nomi ichidagi fayllar haqida aytib turishi kerak."),
            Q("Papka va fayl o‘rtasidagi farq nima?", "Papka fayllarni saqlaydi", ["Fayl papkalarni saqlaydi", "Ular bir xil narsa", "Papka ovoz chiqaradi"], d=2,
              x="Papka — fayllar uchun joy, fayl esa ma’lumotning o‘zi."),
            Q("Kompyuterda yangi papka yaratish uchun ish stolida qaysi tugmani bosamiz?", "Sichqonchaning o‘ng tugmasini",
              ["Enter tugmasini", "Probelni", "Quvvat tugmasini"], d=2,
              x="O‘ng tugma menyusida yangi papka yaratish buyrug‘i bor."),
            Q("Yangi papkaning nomi yozilgach, uni tasdiqlash uchun qaysi tugma bosiladi?", "Enter", ["Backspace", "Esc", "Shift"], d=3,
              x="Enter yozilgan nomni tasdiqlaydi, Esc esa bekor qiladi."),
        ])

T.topic("paint", "🎨", L("Rasm chizish dasturi", "Drawing program", "Графический редактор"),
        chapter=C3,
        theory="Kompyuterda rasm chizish uchun grafik muharrir ishlatiladi, masalan, Paint dasturi.\n"
               "• Qalam — ingichka chiziq chizadi; cho‘tka — qalinroq chiziq chizadi.\n"
               "• O‘chirg‘ich — rasmning keraksiz qismini o‘chiradi.\n"
               "• Bo‘yoq chelagi — yopiq shaklning ichini bir bosishda bo‘yaydi.\n"
               "• Shakllar — to‘rtburchak, oval, uchburchak, yulduzni tayyor chizadi; rang palitradan tanlanadi.",
        items=[
            Q("Paint dasturi nima uchun kerak?", "Rasm chizish uchun", ["Musiqa tinglash uchun", "Hisoblash uchun", "Xat yuborish uchun"],
              x="Paint — rasm chizish dasturi, ya’ni grafik muharrir.", e="🎨"),
            Q("Paint dasturida ingichka chiziq chizish uchun qaysi asbob olinadi?", "Qalam", ["O‘chirg‘ich", "Bo‘yoq chelagi", "Lupa"],
              x="Qalam ingichka chiziq chizadi.", e="✏️"),
            Q("Rasmning keraksiz qismini qaysi asbob o‘chiradi?", "O‘chirg‘ich", ["Qalam", "Cho‘tka", "Bo‘yoq chelagi"],
              x="O‘chirg‘ich rasmning bir qismini o‘chiradi."),
            Q("Shaklning ichini bir bosishda bo‘yash uchun qaysi asbob kerak?", "Bo‘yoq chelagi", ["Qalam", "O‘chirg‘ich", "Lupa"],
              x="Bo‘yoq chelagi yopiq shaklning ichini tanlangan rang bilan to‘ldiradi."),
            Q("Paint dasturida rang qayerdan tanlanadi?", "Palitradan", ["Savatdan", "Vazifalar panelidan", "Klaviaturadan"],
              x="Palitrada turli ranglar bor, keraklisini bosib tanlaymiz."),
            TF("Paint dasturida tayyor shakllar chizish mumkin.", True, x="Shakllar orasida to‘rtburchak, oval, uchburchak, yulduz bor."),
            TF("O‘chirg‘ich rasmga rang beradi.", False, x="O‘chirg‘ich rasmning bir qismini o‘chiradi, rangni bo‘yoq chelagi yoki qalam beradi."),
            TF("Chizilgan rasmni printerda chop etish mumkin.", True, x="Printer rasmni qog‘ozga chiqaradi."),
            MATCH("Asbobni vazifasi bilan juftlang",
                  [("Qalam", "Ingichka chiziq chizadi"), ("O‘chirg‘ich", "Keraksiz joyni o‘chiradi"), ("Bo‘yoq chelagi", "Shakl ichini bo‘yaydi"),
                   ("Lupa", "Rasmni kattalashtiradi"), ("Palitra", "Rang tanlaydi"), ("Matn asbobi", "Rasmga yozuv qo‘shadi")],
                  x="Har bir asbob o‘z ishini bajaradi."),
            Q("Doira yoki tuxumsimon shakl nima deb ataladi?", "Oval", ["To‘rtburchak", "Uchburchak", "Yulduz"],
              x="Oval — dumaloq yoki cho‘zinchoq dumaloq shakl."),
            Q("Quyosh chizish uchun qaysi shakl eng mos?", "Oval", ["Uchburchak", "To‘rtburchak", "Chiziq"],
              x="Quyosh dumaloq, uni oval shakli bilan chizamiz.", e="☀️"),
            Q("Uyning tomini chizish uchun qaysi shakl mos?", "Uchburchak", ["Oval", "Yulduz", "Yurak"],
              x="Uy tomi ko‘pincha uchburchak shaklida chiziladi.", e="🏠"),
            Q("Rasmga yozuv qo‘shish uchun qaysi asbob kerak?", "Matn asbobi", ["O‘chirg‘ich", "Bo‘yoq chelagi", "Qalam"], d=2,
              x="Matn asbobi “A” harfi bilan belgilangan."),
            Q("Rasmni kattalashtirib ko‘rish uchun qaysi asbob kerak?", "Lupa", ["O‘chirg‘ich", "Cho‘tka", "Qalam"], d=2,
              x="Lupa rasmni kattalashtirib ko‘rsatadi."),
            Q("Chizilgan rasmni kompyuterda qoldirish uchun nima qilish kerak?", "Saqlash", ["O‘chirish", "Saqlamasdan yopish", "Savatga tashlash"], d=2,
              x="Saqlangan rasm fayl bo‘lib kompyuterda qoladi."),
            Q("Qalinroq chiziq chizish uchun qalam o‘rniga nima tanlanadi?", "Cho‘tka", ["O‘chirg‘ich", "Lupa", "Bo‘yoq chelagi"], d=2,
              x="Cho‘tka qalin va chiroyli chiziq chizadi."),
            TF("Paint dasturida sichqoncha qalam vazifasini bajaradi.", True, d=2,
               x="Chap tugmani bosib turib sichqonchani sursak, chiziq chiziladi."),
            Q("Paint dasturida to‘g‘ri chiziq chizish uchun qaysi asbob qulay?", "Chiziq", ["Bo‘yoq chelagi", "O‘chirg‘ich", "Lupa"], d=2,
              x="Chiziq asbobi ikki nuqta orasiga tekis chiziq tortadi."),
            Q("Paint qanday dastur?", "Grafik muharrir", ["Matn muharriri", "O‘yin", "Kalkulyator"], d=2,
              x="Rasm chizish dasturlari grafik muharrir deb ataladi."),
            ORDER("So‘zlardan gap tuzing", "Palitradan qizil rangni tanlang", d=2),
            TF("Bo‘yoq chelagi bilan ochiq shakl bo‘yalsa, bo‘yoq tashqariga ham tarqaladi.", True, d=3,
               x="Shakl chizig‘ida teshik bo‘lsa, bo‘yoq undan chiqib, atrofni ham bo‘yaydi."),
            Q("Xato chizilgan chiziqni tezda bekor qilish uchun qaysi tugmalar bosiladi?", "Ctrl + Z", ["Ctrl + P", "Shift + A", "Alt + 1"], d=3,
              x="Ctrl + Z oxirgi amalni bekor qiladi."),
            Q("Rasmdagi biror rangni aynan olish uchun qaysi asbob kerak?", "Pipetka", ["Lupa", "Qalam", "O‘chirg‘ich"], d=3,
              x="Pipetka rasmdagi rangni “olib”, shu rang bilan chizishga imkon beradi."),
            Q("Paint dasturida oval chizganda Shift tugmasini bosib tursak, nima bo‘ladi?", "Tekis doira chiqadi",
              ["Rasm o‘chadi", "Rang o‘zgaradi", "Dastur yopiladi"], d=3,
              x="Shift bosib turilsa, oval tekis doira, to‘rtburchak esa kvadrat bo‘lib chiziladi."),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["ish_stoli", "fayl_papka", "paint"], chapter=C3)

# ============================================================ 4-chorak
T.topic("axborot", "💡", L("Axborot va uning turlari", "Information and its types", "Информация и её виды"),
        chapter=C4,
        theory="Axborot — atrofimizdagi olam haqida biladigan ma’lumotlarimiz.\n"
               "Biz axborotni sezgi a’zolari orqali olamiz:\n"
               "• ko‘z — ko‘rish, quloq — eshitish, burun — hid bilish,\n"
               "• til — ta’m bilish, teri — sezish (tegib bilish).\n"
               "Eng ko‘p axborotni ko‘z orqali olamiz. Axborotni yig‘amiz, saqlaymiz, uzatamiz va qayta ishlaymiz.",
        items=[
            Q("Gulning hidini qaysi a’zo orqali bilamiz?", "Burun", ["Ko‘z", "Quloq", "Til"], x="Hidni burun orqali sezamiz.", e="🌸"),
            Q("Qo‘ng‘iroq ovozini qaysi a’zo orqali bilamiz?", "Quloq", ["Burun", "Til", "Ko‘z"], x="Tovushni quloq orqali eshitamiz.", e="🔔"),
            Q("Limonning nordonligini qaysi a’zo orqali bilamiz?", "Til", ["Quloq", "Ko‘z", "Burun"], x="Ta’mni til orqali bilamiz.", e="🍋"),
            Q("Svetofor rangini qaysi a’zo orqali bilamiz?", "Ko‘z", ["Quloq", "Burun", "Til"], x="Rangni ko‘z orqali ko‘ramiz.", e="🚦"),
            Q("Qorning sovuqligini qanday bilamiz?", "Teri orqali sezib", ["Hidlab", "Tinglab", "Tatib ko‘rib"],
              x="Issiq-sovuqni teri orqali sezamiz.", e="❄️"),
            Q("Eng ko‘p axborotni qaysi a’zo orqali olamiz?", "Ko‘z", ["Burun", "Til", "Teri"],
              x="Atrofdagi axborotning eng katta qismini ko‘rish orqali olamiz.", e="👀"),
            Q("Kitob o‘qiganda axborotni qaysi a’zo orqali olamiz?", "Ko‘z", ["Burun", "Til", "Quloq"],
              x="Kitobdagi harflarni ko‘z bilan ko‘rib o‘qiymiz.", e="📖"),
            TF("Qo‘shiqni quloq orqali eshitamiz.", True, x="Tovush axborotini quloq qabul qiladi."),
            TF("Shokoladning ta’mini ko‘z bilan bilamiz.", False, x="Ta’mni til orqali bilamiz."),
            TF("Kompyuter matn, rasm, tovush va video bilan ishlay oladi.", True, x="Bular kompyuter qayta ishlaydigan axborot turlari."),
            MATCH("Axborotni a’zo bilan juftlang",
                  [("Musiqa", "Quloq"), ("Rasm", "Ko‘z"), ("Atir hidi", "Burun"), ("Asal ta’mi", "Til"), ("Mushukning yumshoq juni", "Teri")],
                  x="Har bir sezgi a’zosi o‘z axborotini qabul qiladi."),
            Q("Axborot qayerda saqlanishi mumkin?", "Kitobda", ["Havoda", "Suvda", "Shamolda"],
              x="Kitob, daftar, kompyuter xotirasi axborotni saqlaydi."),
            Q("Non yangi yopilganini hididan bildik. Bu qanday axborot?", "Hid orqali olingan", ["Eshitish orqali olingan", "Ta’m orqali olingan", "Ko‘rish orqali olingan"], d=2,
              x="Hidni burun sezadi, bu hid bilish orqali olingan axborot."),
            Q("Issiq choy ekanini piyolaga tegib bildik. Bu qaysi yo‘l bilan olingan axborot?", "Sezish", ["Eshitish", "Ko‘rish", "Hid bilish"], d=2,
              x="Issiqlikni teri orqali sezamiz."),
            Q("Kundalikka uy vazifasini yozib qo‘yish — bu axborot bilan qanday ish?", "Saqlash", ["Uzatish", "Qayta ishlash", "Hidlash"], d=2,
              x="Yozib qo‘yilgan axborot keyin kerak bo‘lguncha saqlanadi."),
            Q("Do‘stga telefonda yangilikni aytish — bu axborot bilan qanday ish?", "Uzatish", ["Saqlash", "Qayta ishlash", "O‘chirish"], d=2,
              x="Axborot bir odamdan boshqasiga yetkazildi — bu uzatish."),
            Q("Misolni yechib, javobni topish — bu axborot bilan qanday ish?", "Qayta ishlash", ["Saqlash", "Uzatish", "Hidlash"], d=2,
              x="Berilgan sonlardan yangi axborot — javob hosil qildik."),
            Q("Kutubxonadan hayvonlar haqida ma’lumot to‘plash — bu qanday ish?", "Yig‘ish", ["Uzatish", "O‘chirish", "Unutish"], d=2,
              x="Turli manbalardan ma’lumot to‘plash — axborotni yig‘ish."),
            Q("Kompyuter qaysi axborotni qabul qila olmaydi?", "Ovqat ta’mini", ["Rasmni", "Matnni", "Ovozni"], d=2,
              x="Oddiy kompyuter ta’m va hidni sezmaydi, u matn, rasm, ovoz va video bilan ishlaydi."),
            MATCH("Axborot ko‘rinishini misol bilan juftlang",
                  [("Matn", "Ertak kitobi"), ("Rasm", "Fotosurat"), ("Tovush", "Qo‘shiq"), ("Son", "Telefon raqami"), ("Video", "Multfilm")], d=2,
                  x="Axborot matn, rasm, tovush, son va video ko‘rinishida bo‘ladi."),
            Q("Soat bizga qanday axborot beradi?", "Vaqt haqida", ["Og‘irlik haqida", "Hid haqida", "Ta’m haqida"], d=2,
              x="Soat vaqtni ko‘rsatadi.", e="⏰"),
            ORDER("So‘zlardan gap tuzing", "Quloq orqali tovushni eshitamiz", d=2),
            TF("Hayvonlar ham bir-biriga axborot beradi.", True, d=3,
               x="Masalan, it vovullab, qushlar sayrab boshqalarga xabar beradi."),
            Q("Tana haroratini bilish uchun qaysi asbob axborot beradi?", "Termometr", ["Soat", "Chizg‘ich", "Tarozi"], d=3,
              x="Termometr haroratni o‘lchab, bizga axborot beradi."),
        ])

_algo = [
    Q("Algoritm nima?", "Buyruqlar ketma-ketligi", ["Kompyuter qismi", "Rasm chizish asbobi", "Klaviatura tugmasi"],
      x="Algoritm — ishni bajarish uchun tartib bilan yozilgan buyruqlar."),
    TF("Algoritmda buyruqlar tartibi muhim.", True, x="Tartib buzilsa, to‘g‘ri natija chiqmaydi."),
    TF("Buyruqlar tartibini almashtirsak ham natija doim bir xil bo‘ladi.", False,
       x="Masalan, choynakka suv quymasdan choyni piyolaga quyib bo‘lmaydi."),
    Q("Tish yuvish algoritmida “tishlarni yuvish”dan oldin qaysi qadam keladi?", "Cho‘tkaga pasta surtish",
      ["Cho‘tkani yuvib qo‘yish", "Sochiqqa artinish", "Uxlashga yotish"],
      x="Avval cho‘tkaga pasta surtiladi, keyin tishlar yuviladi."),
    Q("Choy damlashda choynakka choy solingandan keyin nima qilinadi?", "Qaynoq suv quyiladi",
      ["Piyolaga quyiladi", "Choynak chayiladi", "Choy ichiladi"],
      x="Choy solingandan so‘ng ustidan qaynoq suv quyiladi.", e="🍵"),
    MATCH("Choy damlash algoritmi: qadamni raqami bilan juftlang",
          [("1-qadam", "Choynakni chayish"), ("2-qadam", "Choy solish"), ("3-qadam", "Qaynoq suv quyish"),
           ("4-qadam", "Biroz kutish"), ("5-qadam", "Piyolaga quyish")],
          x="Choy damlash: chayish → choy solish → suv quyish → kutish → piyolaga quyish."),
    Q("Qaysi biri algoritmga misol bo‘ladi?", "Palov pishirish tartibi", ["Qizil rang", "Katta tosh", "Baland daraxt"],
      x="Palov pishirish tartibi — ketma-ket bajariladigan buyruqlar."),
    Q("Retsept bo‘yicha pishiriq tayyorlash — bu nima?", "Algoritmni bajarish", ["Rasm chizish", "Musiqa tinglash", "Uxlash"],
      x="Retsept — pishiriq tayyorlash algoritmi."),
    Q("Qo‘l yuvish algoritmida qaysi qadam eng oxirida bajariladi?", "Qo‘lni sochiqqa artish",
      ["Jo‘mrakni ochish", "Sovun surtish", "Qo‘lni ho‘llash"],
      x="Qo‘l yuvilib, chayilgandan keyin sochiqqa artiladi."),
    MATCH("Tish yuvish algoritmi: qadamni raqami bilan juftlang",
          [("1-qadam", "Cho‘tkani olish"), ("2-qadam", "Pasta surtish"), ("3-qadam", "Tishlarni yuvish"),
           ("4-qadam", "Og‘izni chayish"), ("5-qadam", "Cho‘tkani yuvib qo‘yish")], d=2,
          x="Tish yuvish: cho‘tkani olish → pasta surtish → yuvish → chayish → cho‘tkani yuvib qo‘yish."),
    MATCH("Ertalabki algoritm: qadamni raqami bilan juftlang",
          [("1-qadam", "Uyg‘onish"), ("2-qadam", "Yuz-qo‘lni yuvish"), ("3-qadam", "Nonushta qilish"),
           ("4-qadam", "Sumkani olish"), ("5-qadam", "Maktabga borish")], d=2,
          x="Har kuni ertalab shu tartibda ish qilamiz."),
    Q("Berilganlardan qaysi biri kiyinishda eng oxirida bajariladi?", "Oyoq kiyim kiyish", ["Paypoq kiyish", "Ko‘ylak kiyish", "Shim kiyish"], d=2,
      x="Avval paypoq, ko‘ylak va shim, keyin oyoq kiyim kiyiladi."),
    Q("“Algoritm” so‘zi qaysi olim nomidan kelib chiqqan?", "Al-Xorazmiy", ["Ibn Sino", "Beruniy", "Ulug‘bek"], d=2,
      x="Buyuk vatandoshimiz Muhammad al-Xorazmiy nomi lotin tilida “Algoritmi” deb yozilgan."),
    Q("Yo‘lni svetofordan o‘tish algoritmida yashil chiroq yonganda nima qilinadi?", "Chap va o‘ngga qarab o‘tiladi",
      ["Yugurib o‘tiladi", "Qizil yonguncha kutiladi", "Ko‘zni yumib o‘tiladi"], d=2,
      x="Yashil chiroqda ham avval atrofga qarab, keyin xotirjam o‘tiladi.", e="🚦"),
    Q("Algoritmning har bir buyrug‘i qanday bo‘lishi kerak?", "Aniq va tushunarli", ["Chalkash", "Tushunarsiz", "Noaniq"], d=2,
      x="Buyruq aniq bo‘lsa, uni har kim bir xil bajaradi."),
    TF("Kundalik ishlarimizning ko‘pi algoritm asosida bajariladi.", True, d=2,
       x="Tish yuvish, kiyinish, ovqat tayyorlash — hammasi algoritm."),
    Q("Choy damlash: choynakni chayish, …, qaynoq suv quyish, kutish, piyolaga quyish. Qaysi qadam tushib qolgan?", "Choy solish",
      ["Piyolani yuvish", "Qand solish", "Stolni artish"], d=2,
      x="Choynakka choy solinmasa, choy damlanmaydi."),
    Q("Daraxt ekish algoritmida berilganlardan birinchi nima qilinadi?", "Chuqur qaziladi",
      ["Ko‘chat o‘tqaziladi", "Suv quyiladi", "Tuproq bosiladi"], d=2,
      x="Avval chuqur qaziladi, keyin ko‘chat o‘tqazilib, tuproq bosiladi va suv quyiladi."),
    Q("Qaysi so‘z algoritmdagi buyruq bo‘la oladi?", "Oldinga yur", ["Chiroyli", "Katta", "Qizil"], d=2,
      x="Buyruq nima qilish kerakligini aytadi."),
    TF("Algoritm faqat kompyuter uchun yoziladi.", False, d=2,
       x="Algoritmni odam ham bajaradi: masalan, retsept bo‘yicha ovqat pishiradi."),
    Q("Nima uchun algoritm buyruqlari tartib bilan yoziladi?", "To‘g‘ri natija olish uchun",
      ["Chiroyli ko‘rinishi uchun", "Uzun bo‘lishi uchun", "Qog‘ozni to‘ldirish uchun"], d=2,
      x="Tartib buzilsa, ish to‘g‘ri bajarilmaydi."),
    ORDER("So‘zlardan gap tuzing", "Algoritmda buyruqlar tartibi muhim", d=2),
]
for cmds in [["eshikni och", "xonaga kir", "eshikni yop"],
             ["daftarni och", "sanani yoz", "masalani yech", "daftarni yop"],
             ["ruchkani ol", "qopqog‘ini och", "ismingni yoz", "qopqog‘ini yop", "ruchkani qo‘y"]]:
    n = len(cmds)
    txt = ", ".join(cmds).capitalize()
    _algo.append(Q(f"“{txt}.” Bu algoritmda nechta buyruq bor?", f"{n} ta", [f"{m} ta" for m in near(n, [n - 1, n + 1, n + 2, n - 2], lo=1)],
                   d=1 if n <= 4 else 2, x=f"Buyruqlarni sanaymiz: {n} ta."))

T.topic("algoritm", "📋", L("Algoritm — buyruqlar ketma-ketligi", "Algorithm: a sequence of commands", "Алгоритм — последовательность команд"),
        chapter=C4,
        theory="Algoritm — biror ishni bajarish uchun aniq buyruqlarning tartibli ketma-ketligi.\n"
               "Buyruqlar tartibi muhim: tartib buzilsa, natija chiqmaydi.\n"
               "Misol — choy damlash: 1) choynakni chayamiz, 2) choy solamiz, 3) qaynoq suv quyamiz, 4) biroz kutamiz, 5) piyolaga quyamiz.\n"
               "“Algoritm” so‘zi buyuk olim Muhammad al-Xorazmiy nomidan kelib chiqqan.",
        items=_algo)


def robot_run(start, cmds):
    pos = start
    for c in cmds:
        pos += 1 if c == "oldinga" else -1
        assert pos >= 1
    return pos


_robot = [
    Q("Buyruqlarni bajaruvchi nima deb ataladi?", "Ijrochi", ["Algoritm", "Papka", "Monitor"],
      x="Ijrochi — buyruqlarni bajaruvchi: odam, robot yoki kompyuter.", e="🤖"),
    Q("Qaysi biri ijrochi bo‘la oladi?", "Robot", ["Stol", "Tosh", "Qog‘oz"],
      x="Robot buyruqlarni qabul qilib bajaradi."),
    TF("Odam ham ijrochi bo‘la oladi.", True, x="Masalan, o‘quvchi o‘qituvchining topshirig‘ini bajaradi."),
    TF("Robot o‘zi bilmaydigan buyruqni ham bajaradi.", False,
       x="Ijrochi faqat o‘z buyruqlar tizimidagi buyruqlarni bajaradi."),
    Q("Robot faqat “oldinga”, “orqaga”, “chapga”, “o‘ngga” buyruqlarini biladi. Qaysi buyruqni bajara olmaydi?", "Sakra",
      ["Oldinga", "Chapga", "Orqaga"], x="“Sakra” Robotning buyruqlar tizimida yo‘q."),
    Q("Robot bir katak o‘ngga, keyin bir katak chapga yurdi. U qayerda bo‘ladi?", "Boshlagan joyida",
      ["Ikki katak chapda", "Ikki katak o‘ngda", "Bir katak yuqorida"],
      x="O‘ngga bir qadam va chapga bir qadam bir-birini yo‘qqa chiqaradi."),
    TF("Kalkulyator ham ijrochi: u hisoblash buyruqlarini bajaradi.", True,
       x="Kalkulyator bosilgan tugmalar bo‘yicha hisoblaydi."),
    Q("Printer qanday buyruqni bajaradi?", "Chop etish", ["Rasm chizish", "Yurish", "Qo‘shiq aytish"],
      x="Printer — chop etish buyrug‘ini bajaradigan ijrochi."),
    Q("Ijrochi bajara oladigan buyruqlar to‘plami nima deb ataladi?", "Buyruqlar tizimi", ["Vazifalar paneli", "Ish stoli", "Palitra"], d=2,
      x="Har bir ijrochining o‘z buyruqlar tizimi bor."),
    MATCH("Ijrochini buyrug‘i bilan juftlang",
          [("Printer", "Chop et"), ("Oshpaz", "Osh pishir"), ("Robot-changyutkich", "Polni tozala"),
           ("Haydovchi", "Mashinani yurgiz"), ("Kir yuvish mashinasi", "Kirni yuv")], d=2,
          x="Har bir ijrochi o‘ziga mos buyruqni bajaradi."),
    TF("Buyruq aniq bo‘lmasa, ijrochi uni to‘g‘ri bajara olmaydi.", True, d=2,
       x="“Biroz yur” desak, Robot qancha yurishni bilmaydi."),
    Q("Qaysi buyruq Robot uchun aniq?", "3 qadam oldinga yur", ["Biroz yur", "Qayergadir bor", "Ko‘proq yur"], d=2,
      x="Aniq buyruqda nima qilish va necha marta qilish aytiladi."),
    ORDER("So‘zlardan gap tuzing", "Ijrochi buyruqlarni bajaradi", d=2),
    Q("Robot shimolga qarab turibdi. “O‘ngga buril” buyrug‘idan keyin qaysi tomonga qaraydi?", "Sharqqa",
      ["G‘arbga", "Janubga", "Shimolga"], d=3, x="Shimolga qarab turib o‘ngga burilsak, sharqqa qaraymiz."),
]
for start, cmds, d in [(1, ["oldinga"] * 3, 1), (4, ["orqaga"] * 2, 1), (2, ["oldinga", "oldinga", "orqaga", "oldinga"], 2),
                       (6, ["orqaga", "orqaga", "oldinga", "orqaga"], 2), (3, ["oldinga", "oldinga", "oldinga", "orqaga", "oldinga"], 3)]:
    end = robot_run(start, cmds)
    _robot.append(Q(f"Robot {start}-katakda turibdi. Har bir buyruq uni bir katak suradi. Buyruqlar: {', '.join(cmds)}. Robot nechanchi katakda bo‘ladi?",
                    f"{end}-katakda", [f"{m}-katakda" for m in near(end, [end + 1, end - 1, end + 2, start], lo=1)], d=d,
                    x=f"Har bir “oldinga” — bir katak oldinga, “orqaga” — bir katak orqaga: Robot {end}-katakka keladi."))
for a, b, d in [(2, 5, 1), (3, 9, 2)]:
    n = b - a
    _robot.append(Q(f"Robot {a}-katakda turibdi. {b}-katakka borishi uchun nechta “oldinga” buyrug‘i kerak?", n,
                    near(n, [n + 1, n - 1, b, n + 2], lo=1), d=d, x=f"{b} − {a} = {n}, demak {n} ta “oldinga” kerak."))
for start, right, left in [(5, 3, 2), (4, 2, 3)]:
    end = start + right - left
    _robot.append(Q(f"Robot {start}-katakda. U {right} katak o‘ngga, keyin {left} katak chapga yurdi. Endi nechanchi katakda?",
                    f"{end}-katakda", [f"{m}-katakda" for m in near(end, [start + right, start - left, end + 1, end - 1], lo=1)], d=2,
                    x=f"{start} + {right} − {left} = {end}."))

T.topic("ijrochi", "🤖", L("Ijrochi va buyruqlar", "Executor and commands", "Исполнитель и команды"),
        chapter=C4,
        theory="Ijrochi — buyruqlarni bajaruvchi: odam, robot yoki kompyuter.\n"
               "Har bir ijrochi faqat o‘zi biladigan buyruqlarni bajara oladi — bu uning buyruqlar tizimi.\n"
               "Masalan, Robot buyruqlari: “oldinga”, “orqaga”, “chapga”, “o‘ngga” — har biri bir katak suradi.\n"
               "Robot 1-katakda turibdi va “oldinga” buyrug‘ini 3 marta bajardi — endi u 4-katakda.",
        items=_robot)

T.topic("internet", "🔒", L("Internetda xavfsizlik", "Staying safe online", "Безопасность в интернете"),
        chapter=C4,
        theory="Internet — butun dunyodagi kompyuterlarni bog‘lovchi katta tarmoq. Unda foydali narsa ko‘p, lekin ehtiyot bo‘lish kerak.\n"
               "• Parolingizni hech kimga aytmang — uni faqat siz va ota-onangiz biladi.\n"
               "• Notanish odamga ismingiz, uy manzilingiz, telefon raqamingiz va maktabingizni aytmang.\n"
               "• Notanish odam bilan uchrashmang, noma’lum havola va fayllarni ochmang.\n"
               "• Biror narsa sizni qo‘rqitsa yoki xafa qilsa — darhol kattalarga ayting.",
        items=[
            Q("Parolingizni kim bilishi mumkin?", "Faqat siz va ota-onangiz", ["Sinfdoshingiz", "Internetdagi notanish odam", "Hamma"],
              x="Parol sir: uni boshqalarga aytmaymiz.", e="🔑"),
            TF("Parolni eng yaqin do‘stimga aytsam bo‘ladi.", False, x="Parol sir, uni faqat o‘zingiz va ota-onangiz biladi."),
            Q("Internetda notanish odam uy manzilingizni so‘rasa nima qilasiz?", "Aytmayman va kattalarga aytaman",
              ["Darhol aytaman", "Rasmini yuboraman", "Uchrashuvga boraman"],
              x="Shaxsiy ma’lumotni notanishlarga bermaymiz."),
            TF("Internetdagi notanish odam bilan uchrashish xavfli.", True,
               x="Internetdagi odam o‘zini boshqacha qilib ko‘rsatishi mumkin."),
            Q("Qaysi biri shaxsiy ma’lumot?", "Uy manzili", ["Ob-havo", "Ertak nomi", "Hayvonlar haqidagi fakt"],
              x="Uy manzili, telefon raqami, parol — shaxsiy ma’lumot."),
            Q("Internetda sizni qo‘rqitgan narsa ko‘rsangiz nima qilasiz?", "Kattalarga aytaman",
              ["Hech kimga aytmayman", "Davom etib ko‘raman", "Do‘stlarimga yuboraman"],
              x="Ota-ona yoki o‘qituvchi yordam beradi."),
            Q("O‘yin yoki dastur yuklab olishdan oldin nima qilish kerak?", "Kattalardan ruxsat so‘rash",
              ["Hech kimga aytmaslik", "Parolni yozish", "Hamma tugmani bosish"],
              x="Ba’zi dasturlarda virus bo‘lishi mumkin, kattalar tekshirib beradi."),
            TF("Internetda ham odob bilan muloqot qilish kerak.", True, x="Ekran ortida ham tirik odam o‘tiradi."),
            Q("Internetda boshqalarga qanday yozish kerak?", "Xushmuomala bo‘lib",
              ["Qo‘pol so‘zlar bilan", "Masxara qilib", "Baqirgandek, katta harflar bilan"],
              x="Odobli so‘zlar internetda ham kerak."),
            TF("O‘z rasmimni notanish odamga yuborsam bo‘ladi.", False, x="Rasm ham shaxsiy ma’lumot, uni notanishga yubormaymiz."),
            TF("Internet — dunyodagi kompyuterlarni bog‘lovchi tarmoq.", True, x="Internet orqali boshqa shahar va mamlakatdagi kompyuterlar bog‘lanadi.",
               e="🌐"),
            Q("Internetda qaysi ish foydali?", "Darsga ma’lumot izlash", ["Notanishga manzil berish", "Parol tarqatish", "Birovni masxara qilish"],
              x="Internetdan o‘qish va bilim olish uchun foydalanamiz."),
            ORDER("So‘zlardan gap tuzing", "Parolni hech kimga aytmang"),
            Q("Ekranda “Siz yutdingiz! Sovg‘a olish uchun bosing” degan yozuv chiqdi. Nima qilasiz?", "Bosmayman, kattalarga aytaman",
              ["Darhol bosaman", "Parolimni yozaman", "Manzilimni yozaman"], d=2,
              x="Bunday yozuvlar ko‘pincha aldov bo‘ladi."),
            TF("Internetdagi har bir ma’lumot to‘g‘ri bo‘ladi.", False, d=2,
               x="Internetda xato va yolg‘on ma’lumot ham bor, uni kattalar bilan tekshirish kerak."),
            MATCH("Vaziyatni to‘g‘ri harakat bilan juftlang",
                  [("Notanish telefon raqamingni so‘radi", "Aytmayman"), ("Kimdir seni xafa qildi", "Kattalarga aytaman"),
                   ("Shubhali havola keldi", "Bosmayman"), ("Parolingni so‘rashdi", "Sir saqlayman"),
                   ("Yangi o‘yin yuklamoqchisan", "Ruxsat so‘rayman")], d=2,
                  x="Xavfsizlik qoidalari bizni himoya qiladi."),
            Q("Qaysi parolni topish qiyinroq?", "Qalam7Olma3", ["12345", "aaaa", "ali"], d=2,
              x="Harf va raqamlar aralashgan uzun parolni topish qiyin."),
            Q("Internetda qancha vaqt o‘tirish kerak?", "Kattalar ruxsat bergancha", ["Kun bo‘yi", "Tun bo‘yi", "To‘xtovsiz"], d=2,
              x="Vaqtni chegaralash ko‘z va sog‘liq uchun foydali."),
            Q("Sinfdoshingizni internetda boshqalar masxara qilyapti. Nima qilasiz?", "Kattalarga aytaman",
              ["Men ham kulaman", "Masxarani tarqataman", "Hech narsa qilmayman"], d=2,
              x="Kattalarga aytsangiz, ular do‘stingizni himoya qilishga yordam beradi."),
            TF("Notanish odam yuborgan faylni ochmaslik kerak.", True, d=2,
               x="Bunday faylda kompyuterni buzadigan virus bo‘lishi mumkin."),
            Q("Notanish odam “Maktabing qayerda?” deb so‘radi. To‘g‘ri javob qaysi?", "Aytmayman",
              ["Maktab raqamimni aytaman", "Manzilni yozaman", "Rasmini yuboraman"], d=2,
              x="Maktab ham shaxsiy ma’lumot, uni notanishga aytmaymiz."),
            ORDER("So‘zlardan gap tuzing", "Notanish havolani bosmang", d=2),
            Q("Umumiy kompyuterda ishni tugatganda nima qilish kerak?", "Profildan chiqish",
              ["Parolni ekranga yozib qoldirish", "Parolni stolga yozib qo‘yish", "Profilni ochiq qoldirish"], d=3,
              x="Profildan chiqmasangiz, keyingi odam sizning sahifangizga kirishi mumkin."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["axborot", "algoritm", "ijrochi", "internet"], chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["kompyuter", "qurilmalar", "togri_otirish", "sichqoncha", "klaviatura", "matn_terish",
        "ish_stoli", "fayl_papka", "paint", "axborot", "algoritm", "ijrochi", "internet"], chapter=C4, level=3)

T.write()
