"""Rus tili (o‘zbek maktablari uchun), 3-sinf: assets/data/school/russian_g3.json + bank_russian_g3.json.

Mavzular O‘zbekiston maktab dasturi ("Rus tili", 3-sinf, ≈A1) tartibida; hamma matn va savollar o‘zimizniki.
Lug‘at mavzulari (ranglar, sonlar, hayvonlar, mevalar, kiyimlar) — umumiy `foreign_language.dart` generatorlari,
grammatika va iboralar — savollar banki.
Qayta yaratish: python3 tool/content/school/russian_g3.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("russian", 3, L("Rus tili", "Russian", "Русский язык"))

C1 = "1-chorak. Alifbo va tanishuv"
C2 = "2-chorak. Maktab, ranglar va sonlar"
C3 = "3-chorak. Hayvonlar, mevalar va ot rodi"
C4 = "4-chorak. Kiyim, hafta kunlari va harakatlar"


# ------------------------------------------------------------ yordamchilar
def RQ(q, a, w, say, d=1, x=None, e=None, h=None):
    """Savolda ruscha matn bor: ovozda `say` rus tilida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=say, lang="ru")


def LISTEN(a, w, say, d=1, x=None):
    """Tinglab tushunish: ruscha gap eshitiladi, o‘zbekcha tarjimasi tanlanadi."""
    return Q("Tinglang va tarjimasini tanlang", a, w, d=d, x=x or f"{say} — {a}", say=say, lang="ru")


def SENT(ru, tr, d=1):
    """Ruscha gap tuzish (tinish belgisiz)."""
    end = "?" if tr.endswith("?") else "."
    return ORDER("So‘zlardan gap tuzing", ru, d=d, x=f"{ru}{end} — {tr}", lang="ru")


def RTF(q, a, say, d=1, x=None):
    return TF(q, a, d=d, x=x, say=say, lang="ru")


def vocab_levels(theme):
    return [
        {"themes": [theme], "modes": ["listen", "read"], "options": 3},
        {"themes": [theme], "modes": ["read", "picture_word"], "options": 4, "sameTheme": True},
        {"themes": [theme], "modes": ["picture_word", "listen", "read"], "options": 4, "sameTheme": True},
    ]


ALL_COLORS = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown", "black", "white"]

# ============================================================ 1-chorak
T.topic("alphabet", "🔤", L("Alifbo: tovush va harflar", "Alphabet: sounds and letters", "Алфавит: звуки и буквы"),
        chapter=C1,
        theory="Rus alifbosida 33 ta harf bor: 10 ta unli, 21 ta undosh va 2 ta belgi (ь, ъ).\n"
               "• Unli harflar: а, о, у, ы, э, я, ё, ю, е, и.\n"
               "• Undosh harflar: б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ.\n"
               "• ь (yumshatish belgisi) tovush bildirmaydi, oldingi undoshni yumshatadi: день, соль, мать.\n"
               "So‘zda nechta unli bo‘lsa, shuncha bo‘g‘in bor: ма-ма (2), мо-ло-ко (3).",
        items=[
            Q("Qaysi harf unli?", "а", ["б", "к", "т", "м"], x="А — unli harf: uni cho‘zib aytish mumkin."),
            Q("Qaysi harf unli?", "у", ["п", "с", "л", "д"], x="У — unli harf."),
            Q("Qaysi harf undosh?", "м", ["о", "и", "ы", "э"], x="М — undosh harf; qolganlari unli."),
            Q("Qaysi harf undosh?", "р", ["а", "у", "е", "я"], x="Р — undosh harf; qolganlari unli."),
            Q("Rus alifbosida nechta harf bor?", "33", ["32", "29", "26", "35"],
              x="Rus alifbosida 33 ta harf bor: А dan Я gacha."),
            Q("Rus tilida nechta unli harf bor?", "10", ["6", "5", "21", "8"], d=2,
              x="Unli harflar 10 ta: а, о, у, ы, э, я, ё, ю, е, и."),
            TF("Yumshatish belgisi (ь) alohida tovush bildirmaydi.", True,
               x="ь o‘zi tovush bermaydi, faqat oldingi undoshni yumshatadi."),
            Q("Qaysi so‘zda yumshatish belgisi bor?", "день", ["дом", "стол", "мама", "кот"],
              x="День so‘zi ь bilan tugaydi."),
            Q("Qaysi so‘zda yumshatish belgisi (ь) bor?", "соль", ["сок", "нос", "суп", "сыр"],
              x="Соль so‘zi ь bilan tugaydi."),
            RQ("“Мама” so‘zida nechta bo‘g‘in bor?", "2", ["1", "3", "4"], say="мама",
               x="Ма-ма: 2 ta unli — 2 ta bo‘g‘in."),
            RQ("“Молоко” so‘zida nechta bo‘g‘in bor?", "3", ["2", "4", "1"], say="молоко",
               x="Мо-ло-ко: 3 ta unli — 3 ta bo‘g‘in."),
            RQ("“Кот” so‘zida nechta bo‘g‘in bor?", "1", ["2", "3", "4"], say="кот",
               x="Кот so‘zida bitta unli (о) bor — 1 ta bo‘g‘in."),
            RQ("“Карандаш” so‘zida nechta bo‘g‘in bor?", "3", ["2", "4", "5"], say="карандаш", d=2,
               x="Ка-ран-даш: 3 ta unli — 3 ta bo‘g‘in."),
            RQ("“Книга” so‘zi qaysi harf bilan boshlanadi?", "К", ["Н", "Г", "А"], say="книга",
               x="Книга — К harfi bilan boshlanadi."),
            RQ("“Стол” so‘zida nechta harf bor?", "4", ["3", "5", "6"], say="стол",
               x="С-т-о-л — 4 ta harf."),
            Q("Alifboda А harfidan keyin qaysi harf keladi?", "Б", ["В", "Г", "Д"], d=2,
              x="Alifbo shunday boshlanadi: А, Б, В, Г, Д."),
            Q("Alifboda Л harfidan keyin qaysi harf keladi?", "М", ["Н", "К", "П"], d=2,
              x="… К, Л, М, Н, О …"),
            Q("Alifboning oxirgi harfi qaysi?", "Я", ["А", "Э", "Ю", "Ь"], d=2,
              x="Alifbo Я harfi bilan tugaydi: … Э, Ю, Я."),
            Q("Qaysi so‘zda hamma unlilar bir xil?", "молоко", ["книга", "ручка", "школа"], d=3,
              x="Молоко so‘zida uchta unli ham — о."),
            Q("Qaysi harf so‘z boshida kelmaydi?", "ь", ["а", "м", "о", "с"], d=3,
              x="Yumshatish belgisi (ь) hech qachon so‘z boshida yozilmaydi."),
            MATCH("Bosh va kichik harfni juftlang",
                  [("Б", "б"), ("Д", "д"), ("Ж", "ж"), ("Ё", "ё"), ("Я", "я"), ("Ш", "ш"), ("Ц", "ц")]),
            Q("Qaysi so‘z unli harf bilan boshlanadi?", "окно", ["дом", "книга", "мяч", "стул"], d=2,
              x="Окно so‘zi О unlisi bilan boshlanadi."),
            RTF("“Мяч” so‘zida bitta unli bor.", True, say="мяч", d=2,
                x="Мяч so‘zidagi yagona unli — я."),
            RTF("“Ручка” so‘zida uchta bo‘g‘in bor.", False, say="ручка", d=2,
                x="Руч-ка — 2 ta bo‘g‘in."),
            Q("Qaysi juftlikda ikkala harf ham unli?", "о — у", ["м — а", "с — т", "к — и"], d=3,
              x="О va У — ikkalasi ham unli."),
            RQ("ь ma’noni o‘zgartiradi. “Угол” — burchak. “Уголь” nima?", "ko‘mir", ["burchak", "tuz", "daraxt"],
               say="Угол. Уголь.", d=3, x="Угол — burchak, уголь — ko‘mir: bitta ь so‘z ma’nosini o‘zgartirdi."),
        ])

T.topic("greet", "👋", L("Tanishuv va xushmuomala so‘zlar", "Greetings and polite words", "Знакомство и вежливые слова"),
        chapter=C1,
        theory="Tanishganda shunday so‘raymiz va javob beramiz:\n"
               "• — Как тебя зовут? — Меня зовут Али.\n"
               "• — Как дела? — Хорошо, спасибо.\n"
               "Salomlashish: Здравствуйте! (kattalarga), Привет! (do‘stga). Xayrlashish: До свидания! Пока!\n"
               "Xushmuomala so‘zlar: спасибо (rahmat), пожалуйста (iltimos, marhamat), извините (kechirasiz).",
        items=[
            Q("“Rahmat” ruschasi qanday?", "спасибо", ["пожалуйста", "привет", "извините", "пока"],
              x="Rahmat — спасибо."),
            Q("“Kechirasiz” ruschasi qanday?", "извините", ["спасибо", "здравствуйте", "до свидания"],
              x="Kechirasiz — извините."),
            LISTEN("Isming nima?", ["Ahvoling qanday?", "Sen qayerdasan?", "Bu kim?"], say="Как тебя зовут?"),
            LISTEN("Mening ismim Zarina.", ["Bu Zarina.", "Zarina qayerda?", "Mening onam Zarina."],
                   say="Меня зовут Зарина."),
            Q("O‘qituvchi bilan qanday salomlashamiz?", "Здравствуйте!", ["Привет!", "Пока!", "Спасибо!"],
              x="Kattalarga hurmat bilan “Здравствуйте!” deymiz."),
            Q("Do‘stingiz bilan qanday xayrlashasiz?", "Пока!", ["Здравствуйте!", "Спасибо!", "Извините!"],
              x="Do‘st bilan “Пока!” deb xayrlashamiz."),
            RQ("“Как дела?” savoliga mos javobni tanlang", "Хорошо, спасибо.",
               ["Меня зовут Бобур.", "До свидания.", "Это книга."], say="Как дела?",
               x="Как дела? — Ahvoling qanday? Javob: Хорошо, спасибо."),
            RQ("“Как тебя зовут?” savoliga mos javobni tanlang", "Меня зовут Али.",
               ["Хорошо.", "Мне девять лет.", "Это мама."], say="Как тебя зовут?",
               x="Isming so‘ralganda: Меня зовут … deymiz."),
            Q("“Xayrli tong” ruschasi qanday?", "Доброе утро!", ["Добрый вечер!", "Спокойной ночи!", "Добрый день!"],
              x="Xayrli tong — Доброе утро!"),
            Q("“Xayrli kech” ruschasi qanday?", "Добрый вечер!", ["Доброе утро!", "Добрый день!", "Привет!"], d=2,
              x="Xayrli kech — Добрый вечер!"),
            RQ("“Пожалуйста” o‘zbekchasi qanday?", "iltimos, marhamat", ["rahmat", "kechirasiz", "salom"],
               say="Пожалуйста", x="Пожалуйста — iltimos (yoki marhamat)."),
            SENT("Меня зовут Бобур", "Mening ismim Bobur."),
            SENT("Как тебя зовут", "Isming nima?", d=2),
            SENT("Мне девять лет", "Men 9 yoshdaman.", d=2),
            LISTEN("Men 9 yoshdaman.", ["Men 10 yoshdaman.", "Men 3-sinfda o‘qiyman.", "Bu mening maktabim."],
                   say="Мне девять лет.", d=2),
            Q("Sovg‘a olganingizda nima deysiz?", "Спасибо!", ["Пока!", "Извините!", "Здравствуйте!"],
              x="Sovg‘a uchun rahmat aytamiz — Спасибо!"),
            Q("Bilmasdan birovni turtib yubordingiz. Nima deysiz?", "Извините!", ["Спасибо!", "Привет!", "Доброе утро!"],
              d=2, x="Kechirim so‘raymiz — Извините!"),
            Q("Uxlashdan oldin nima deymiz?", "Спокойной ночи!", ["Доброе утро!", "Добрый день!", "Здравствуйте!"],
              d=2, x="Tunda xayrlashganda — Спокойной ночи! (Xayrli tun!)"),
            MATCH("So‘z va tarjimasini juftlang",
                  [("привет", "salom"), ("спасибо", "rahmat"), ("извините", "kechirasiz"), ("пожалуйста", "iltimos"),
                   ("до свидания", "xayr"), ("да", "ha"), ("нет", "yo‘q")]),
            RQ("“Очень приятно!” qachon aytiladi?", "tanishganda", ["xayrlashganda", "uxlashdan oldin", "ovqatlanganda"],
               say="Очень приятно!", d=3, x="Очень приятно! — Tanishganimdan xursandman!"),
            RTF("“Привет” — do‘stlarga aytiladigan salom.", True, say="Привет",
                x="Привет — do‘stlar orasidagi salom."),
            RTF("“Спасибо” — “kechirasiz” degani.", False, say="Спасибо", x="Спасибо — rahmat; kechirasiz — извините."),
            RQ("Suhbatni to‘ldiring: — Спасибо! — …", "Пожалуйста!", ["Привет!", "Пока!", "Как дела?"],
               say="Спасибо! ...", d=2, x="Rahmatga javoban “Пожалуйста!” (arzimaydi) deymiz."),
            RQ("“Как дела?” o‘zbekchasi qanday?", "Ahvoling qanday?", ["Isming nima?", "Necha yoshdasan?", "Qayerda yashaysan?"],
               say="Как дела?", x="Как дела? — Ahvoling qanday? (Ishlaring qalay?)"),
            SENT("Я живу в Ташкенте", "Men Toshkentda yashayman.", d=3),
        ])

T.topic("family", "👪", L("Mening oilam", "My family", "Моя семья"),
        chapter=C1,
        theory="Oila a’zolari: мама (ona), папа (ota), брат (aka, uka), сестра (opa, singil), бабушка (buvi), дедушка (bobo).\n"
               "• Erkak kishi — мой: мой папа, мой брат, мой дедушка.\n"
               "• Ayol kishi — моя: моя мама, моя сестра, моя бабушка.\n"
               "Diqqat: папа va дедушка -а bilan tugasa ham, мой deymiz.\n"
               "Misol: Это моя семья. Это мой папа.",
        items=[
            Q("“Ona” ruschasi qanday?", "мама", ["папа", "сестра", "бабушка", "брат"], x="Ona — мама."),
            Q("“Ota” ruschasi qanday?", "папа", ["мама", "дедушка", "брат", "сын"], x="Ota — папа."),
            Q("“Buvi” ruschasi qanday?", "бабушка", ["дедушка", "мама", "сестра"], x="Buvi — бабушка."),
            Q("“Bobo” ruschasi qanday?", "дедушка", ["бабушка", "папа", "брат"], x="Bobo — дедушка."),
            RQ("“Сестра” o‘zbekchasi qanday?", "opa yoki singil", ["aka yoki uka", "ona", "buvi"], say="сестра",
               x="Сестра — opa yoki singil."),
            RQ("“Брат” o‘zbekchasi qanday?", "aka yoki uka", ["opa yoki singil", "ota", "bobo"], say="брат",
               x="Брат — aka yoki uka."),
            RQ("Mos so‘zni tanlang: … папа", "мой", ["моя", "моё", "мои"], say="... папа",
               x="Папа — erkak kishi, shuning uchun мой папа."),
            RQ("Mos so‘zni tanlang: … мама", "моя", ["мой", "моё", "мои"], say="... мама",
               x="Мама — ayol kishi, shuning uchun моя мама."),
            RQ("Mos so‘zni tanlang: … дедушка", "мой", ["моя", "моё"], say="... дедушка", d=2,
               x="Дедушка -а bilan tugasa ham erkak kishi: мой дедушка."),
            RQ("Mos so‘zni tanlang: … сестра", "моя", ["мой", "моё"], say="... сестра",
               x="Сестра — ayol kishi: моя сестра."),
            LISTEN("Mening onam", ["Mening otam", "Mening opam", "Mening buvim"], say="Моя мама."),
            LISTEN("Bu mening bobom.", ["Bu mening otam.", "Bu mening akam.", "Bu mening buvim."],
                   say="Это мой дедушка."),
            LISTEN("Mening oilam katta.", ["Mening oilam kichik.", "Mening uyim katta.", "Mening sinfim katta."],
                   say="Моя семья большая.", d=2),
            MATCH("So‘z va tarjimasini juftlang",
                  [("мама", "ona"), ("папа", "ota"), ("бабушка", "buvi"), ("дедушка", "bobo"), ("семья", "oila"),
                   ("сын", "o‘g‘il"), ("дочь", "qiz (farzand)")]),
            SENT("Это моя семья", "Bu mening oilam."),
            SENT("Мой брат читает книгу", "Akam kitob o‘qiyapti.", d=3),
            SENT("Моя бабушка добрая", "Buvim mehribon.", d=2),
            RQ("“Семья” o‘zbekchasi qanday?", "oila", ["uy", "sinf", "do‘st"], say="семья", x="Семья — oila."),
            Q("Qaysi so‘z ortiqcha?", "стол", ["мама", "папа", "брат"], d=2,
              x="Стол — stol, u oila a’zosi emas."),
            Q("Onaning onasi kim?", "бабушка", ["сестра", "дедушка", "мама"], d=2,
              x="Onaning onasi — buvi, ya’ni бабушка."),
            Q("Otaning otasi kim?", "дедушка", ["брат", "бабушка", "папа"], d=2,
              x="Otaning otasi — bobo, ya’ni дедушка."),
            RTF("“Моя бабушка” — to‘g‘ri birikma.", True, say="Моя бабушка", d=2,
                x="Бабушка — ayol kishi: моя бабушка."),
            RTF("“Мой сестра” — to‘g‘ri birikma.", False, say="Мой сестра", d=2,
                x="Сестра — ayol kishi, to‘g‘risi: моя сестра."),
            RQ("Gapni to‘ldiring: Это мой …", "брат", ["сестра", "мама", "бабушка"], say="Это мой ...", d=2,
               x="Мой — erkak kishi bilan: мой брат."),
            RQ("Gapni to‘ldiring: Это моя …", "сестра", ["папа", "брат", "дедушка"], say="Это моя ...", d=2,
               x="Моя — ayol kishi bilan: моя сестра."),
            LISTEN("Mening otam — shifokor.", ["Mening otam — o‘qituvchi.", "Mening akam — shifokor.",
                                              "Mening onam — shifokor."], say="Мой папа — врач.", d=3),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["alphabet", "greet", "family"], chapter=C1)

# ============================================================ 2-chorak
T.topic("school", "🏫", L("Maktab va o‘yinchoqlar", "School and toys", "Школа и игрушки"),
        chapter=C2,
        theory="Narsa haqida so‘raganda — Что это? (Bu nima?). Odam yoki hayvon haqida — Кто это? (Bu kim?).\n"
               "• — Что это? — Это книга. Это ручка. Это мяч.\n"
               "• — Кто это? — Это учитель. Это кошка. (Hayvon uchun ham Кто?)\n"
               "Maktab narsalari: книга, тетрадь, ручка, карандаш, линейка, рюкзак, пенал, доска.\n"
               "O‘yinchoqlar: мяч (koptok), кукла (qo‘g‘irchoq), мишка (ayiqcha), машинка, кубики.",
        items=[
            Q("“Kitob” ruschasi qanday?", "книга", ["тетрадь", "ручка", "линейка", "парта"], e="📖", x="Kitob — книга."),
            Q("“Daftar” ruschasi qanday?", "тетрадь", ["книга", "карандаш", "доска"], e="📓", x="Daftar — тетрадь."),
            Q("“Qalam” ruschasi qanday?", "карандаш", ["линейка", "рюкзак", "тетрадь"], e="✏️", x="Qalam — карандаш."),
            Q("“Chizg‘ich” ruschasi qanday?", "линейка", ["тетрадь", "ручка", "парта"], e="📏", x="Chizg‘ich — линейка."),
            RQ("“Доска” o‘zbekchasi qanday?", "doska", ["parta", "deraza", "eshik"], say="доска",
               x="Доска — sinfdagi doska."),
            RQ("Rasmga qarang. Что это?", "Это книга.", ["Это ручка.", "Это линейка.", "Это тетрадь."],
               say="Что это?", e="📕", x="Rasmda kitob: Это книга."),
            RQ("Rasmga qarang. Что это?", "Это рюкзак.", ["Это пенал.", "Это доска.", "Это парта."],
               say="Что это?", e="🎒", x="Rasmda ryukzak: Это рюкзак."),
            RQ("Rasmga qarang. Кто это?", "Это мальчик.", ["Это девочка.", "Это стол.", "Это книга."],
               say="Кто это?", e="👦", x="Rasmda o‘g‘il bola: Это мальчик."),
            RQ("Mos so‘roq so‘zni tanlang: … это? — Это кошка.", "Кто", ["Что", "Где", "Как"],
               say="... это? Это кошка.", x="Hayvon va odam haqida “Кто это?” deb so‘raymiz."),
            RQ("Mos so‘roq so‘zni tanlang: … это? — Это тетрадь.", "Что", ["Кто", "Где", "Как"],
               say="... это? Это тетрадь.", x="Narsa haqida “Что это?” deb so‘raymiz."),
            RQ("Mos so‘roq so‘zni tanlang: … это? — Это мама.", "Кто", ["Что", "Где", "Как"],
               say="... это? Это мама.", d=2, x="Odam haqida — Кто это?"),
            RQ("Mos so‘roq so‘zni tanlang: … это? — Это собака.", "Кто", ["Что", "Где", "Как"],
               say="... это? Это собака.", d=2, x="Rus tilida hayvon haqida ham “Кто это?” deymiz."),
            RQ("Mos so‘roq so‘zni tanlang: … это? — Это доска.", "Что", ["Кто", "Где", "Как"],
               say="... это? Это доска.", d=2, x="Doska — narsa: Что это?"),
            RTF("Hayvon haqida “Что это?” deb so‘raymiz.", False, say="Что это?", d=2,
                x="Hayvon haqida “Кто это?” deymiz: Кто это? — Это собака."),
            MATCH("So‘z va tarjimasini juftlang",
                  [("книга", "kitob"), ("тетрадь", "daftar"), ("карандаш", "qalam"), ("линейка", "chizg‘ich"),
                   ("школа", "maktab"), ("класс", "sinf"), ("учитель", "o‘qituvchi")]),
            SENT("Это мой новый рюкзак", "Bu mening yangi ryukzagim.", d=3),
            SENT("Это моя школа", "Bu mening maktabim."),
            LISTEN("Bu mening daftarim.", ["Bu mening kitobim.", "Bu mening qalamim.", "Bu mening maktabim."],
                   say="Это моя тетрадь.", d=2),
            LISTEN("Bu kim? Bu o‘qituvchi.", ["Bu nima? Bu kitob.", "Bu kim? Bu o‘quvchi.", "Bu nima? Bu doska."],
                   say="Кто это? Это учитель.", d=2),
            Q("“O‘quvchi” (o‘g‘il bola) ruschasi qanday?", "ученик", ["учитель", "урок", "класс"], d=2,
              x="O‘quvchi — ученик; o‘qituvchi — учитель."),
            Q("“Dars” ruschasi qanday?", "урок", ["класс", "школа", "ученик"], d=2, x="Dars — урок."),
            Q("Qaysi so‘z maktab narsasi emas?", "банан", ["ручка", "тетрадь", "линейка"],
              x="Банан — meva, qolganlari maktab narsalari."),
            Q("“Koptok” ruschasi qanday?", "мяч", ["кукла", "машинка", "кубик"], e="⚽", x="Koptok — мяч."),
            Q("“Qo‘g‘irchoq” ruschasi qanday?", "кукла", ["мяч", "мишка", "пенал"], x="Qo‘g‘irchoq — кукла."),
            LISTEN("Bu mening koptogim.", ["Bu mening qo‘g‘irchog‘im.", "Bu mening mashinam.", "Bu mening kitobim."],
                   say="Это мой мяч.", d=2),
        ])

T.topic("colors", "🎨", L("Ranglar", "Colours", "Цвета"), chapter=C2, gen="colors",
        theory="Ranglar (цвета): красный — qizil, жёлтый — sariq, зелёный — yashil, синий — ko‘k,\n"
               "оранжевый — to‘q sariq, фиолетовый — binafsha, розовый — pushti, коричневый — jigarrang,\n"
               "чёрный — qora, белый — oq.\n"
               "Rang so‘zi otga moslashadi: красный мяч, красная машина, красное яблоко.\n"
               "Savol: Какого цвета? — Мяч красный.",
        levels=[
            {"colors": ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown"], "options": 3,
             "modes": ["listen", "read"]},
            {"colors": ALL_COLORS, "options": 4, "modes": ["read", "picture_word", "listen"]},
            {"colors": ALL_COLORS, "options": 4, "modes": ["picture_word", "object", "read"]},
        ])

T.topic("numbers", "🔢", L("Sonlar 1–20", "Numbers 1–20", "Числа от 1 до 20"), chapter=C2, gen="numbers",
        theory="1–10: один, два, три, четыре, пять, шесть, семь, восемь, девять, десять.\n"
               "11–19 “-надцать” bilan tugaydi: одиннадцать, двенадцать, тринадцать … девятнадцать.\n"
               "20 — двадцать.\n"
               "Savol: Сколько? (Nechta?)  Сколько тебе лет? — Мне девять лет.",
        levels=[
            {"min": 1, "max": 10, "modes": ["listen_digit", "read_word"]},
            {"min": 1, "max": 20, "modes": ["listen_digit", "read_word"], "options": 4},
            {"min": 1, "max": 20, "modes": ["read_word", "match", "listen_digit"], "pairs": 4, "options": 4},
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["school", "colors", "numbers"], chapter=C2)

# ============================================================ 3-chorak
T.topic("animals", "🐶", L("Hayvonlar", "Animals", "Животные"), chapter=C3, gen="vocab",
        theory="Uy hayvonlari: кошка (mushuk), собака (it), корова (sigir), лошадь (ot), овца (qo‘y).\n"
               "Yovvoyi hayvonlar: лев (sher), тигр (yo‘lbars), медведь (ayiq), волк (bo‘ri), лиса (tulki), слон (fil).\n"
               "Hayvon haqida “Кто это?” deb so‘raymiz: — Кто это? — Это собака.",
        levels=vocab_levels("animals"))

T.topic("fruits_veg", "🍎", L("Mevalar va sabzavotlar", "Fruits and vegetables", "Фрукты и овощи"), chapter=C3,
        gen="vocab",
        theory="Mevalar (фрукты): яблоко (olma), груша (nok), банан, виноград (uzum), арбуз (tarvuz), дыня (qovun).\n"
               "Sabzavotlar (овощи): морковь (sabzi), помидор, огурец (bodring), картофель (kartoshka), капуста (karam).\n"
               "Misol: Что это? — Это яблоко. Это морковь.",
        levels=vocab_levels("fruits_veg"))

T.topic("gender", "🏷️", L("Ot rodi: он, она, оно", "Noun gender", "Род существительных"), chapter=C3,
        theory="Rus tilida otlar uch rodda bo‘ladi:\n"
               "• он — стол, дом, мяч (undosh bilan tugaydi) → мой стол\n"
               "• она — мама, книга, земля (-а, -я bilan tugaydi) → моя книга\n"
               "• оно — окно, море, яблоко (-о, -е bilan tugaydi) → моё окно\n"
               "Diqqat: папа, дедушка -а bilan tugasa ham — он (мой папа).",
        items=[
            RQ("“Стол” qaysi rodda?", "он", ["она", "оно"], say="стол", x="Стол undosh bilan tugaydi — он."),
            RQ("“Книга” qaysi rodda?", "она", ["он", "оно"], say="книга", x="Книга -а bilan tugaydi — она."),
            RQ("“Окно” qaysi rodda?", "оно", ["он", "она"], say="окно", x="Окно -о bilan tugaydi — оно."),
            RQ("“Мяч” qaysi rodda?", "он", ["она", "оно"], say="мяч", x="Мяч undosh bilan tugaydi — он."),
            RQ("“Школа” qaysi rodda?", "она", ["он", "оно"], say="школа", x="Школа -а bilan tugaydi — она."),
            RQ("“Море” qaysi rodda?", "оно", ["он", "она"], say="море", x="Море -е bilan tugaydi — оно."),
            RQ("“Яблоко” qaysi rodda?", "оно", ["он", "она"], say="яблоко", x="Яблоко -о bilan tugaydi — оно."),
            RQ("“Папа” qaysi rodda?", "он", ["она", "оно"], say="папа", d=2,
               x="Папа -а bilan tugasa ham erkak kishi — он."),
            RQ("Qaysi so‘z “она” rodida?", "ручка", ["карандаш", "окно", "дом"], say="она", x="Ручка -а bilan tugaydi — она."),
            RQ("Qaysi so‘z “оно” rodida?", "солнце", ["луна", "стул", "машина"], say="оно", d=2,
              x="Солнце -е bilan tugaydi — оно."),
            RQ("Qaysi so‘z “он” rodida?", "дом", ["лампа", "окно", "кукла"], say="он", x="Дом undosh bilan tugaydi — он."),
            RQ("Mos so‘zni tanlang: … окно", "моё", ["мой", "моя"], say="... окно", x="Окно — оно: моё окно."),
            RQ("Mos so‘zni tanlang: … книга", "моя", ["мой", "моё"], say="... книга", x="Книга — она: моя книга."),
            RQ("Mos so‘zni tanlang: … карандаш", "мой", ["моя", "моё"], say="... карандаш",
               x="Карандаш — он: мой карандаш."),
            RQ("Mos so‘zni tanlang: … яблоко", "моё", ["мой", "моя"], say="... яблоко", d=2,
               x="Яблоко — оно: моё яблоко."),
            RQ("Mos so‘zni tanlang: … кошка", "моя", ["мой", "моё"], say="... кошка", d=2,
               x="Кошка — она: моя кошка."),
            RQ("Olmoshni qo‘ying: Где мяч? — … здесь.", "Он", ["Она", "Оно"], say="Где мяч? ... здесь.", d=2,
               x="Мяч — он: Он здесь."),
            RQ("Olmoshni qo‘ying: Где книга? — … здесь.", "Она", ["Он", "Оно"], say="Где книга? ... здесь.", d=2,
               x="Книга — она: Она здесь."),
            RQ("Olmoshni qo‘ying: Где платье? — … здесь.", "Оно", ["Он", "Она"], say="Где платье? ... здесь.", d=3,
               x="Платье -е bilan tugaydi — оно: Оно здесь."),
            RTF("“Дом” — оно rodida.", False, say="дом", x="Дом undosh bilan tugaydi — он."),
            RTF("“Машина” — она rodida.", True, say="машина", x="Машина -а bilan tugaydi — она."),
            RTF("“Папа” -а bilan tugagani uchun она rodida.", False, say="папа", d=3,
                x="Папа — erkak kishi, u он rodida."),
            Q("Qaysi birikma to‘g‘ri?", "моё окно", ["мой окно", "моя окно", "мои окно"], d=2,
              x="Окно — оно, shuning uchun моё окно."),
            Q("Qaysi birikma to‘g‘ri?", "моя сумка", ["мой сумка", "моё сумка"], d=2,
              x="Сумка — она, shuning uchun моя сумка."),
            Q("Qaysi birikma to‘g‘ri?", "мой папа", ["моя папа", "моё папа"], d=3,
              x="Папа — erkak kishi: мой папа."),
            SENT("Это моё яблоко", "Bu mening olmam.", d=2),
            SENT("Где мой мяч", "Mening koptogim qayerda?", d=2),
            Q("Qaysi so‘zning rodi boshqacha?", "окно", ["книга", "ручка", "лампа"], d=3,
              x="Книга, ручка, лампа — она; окно — оно."),
        ])

T.topic("plural", "📚", L("Birlik va ko‘plik", "Singular and plural", "Единственное и множественное число"),
        chapter=C3,
        theory="Ko‘plikda otlarning oxiri o‘zgaradi:\n"
               "• -ы: стол — столы, лампа — лампы, машина — машины.\n"
               "• -и (г, к, х, ж, ш, ч, щ dan keyin): книга — книги, мяч — мячи, карандаш — карандаши.\n"
               "• -а, -я (оно rodidagi so‘zlar): окно — окна, море — моря.\n"
               "Bitta narsa: Это стол. Ko‘p narsa: Это столы. Ko‘plikda — мои: мои книги.",
        items=[
            RQ("“Стол” so‘zining ko‘plik shakli qanday?", "столы", ["столи", "стола", "столу"], say="стол",
               x="Стол — столы (-ы qo‘shiladi)."),
            RQ("“Книга” so‘zining ko‘plik shakli qanday?", "книги", ["книгы", "книгов", "книгу"], say="книга",
               x="Г dan keyin -и yoziladi: книги."),
            RQ("“Окно” so‘zining ko‘plik shakli qanday?", "окна", ["окны", "окни", "окну"], say="окно",
               x="-о → -а: окно — окна."),
            RQ("“Ручка” ko‘plikda qanday?", "ручки", ["ручкы", "ручку", "ручкой"], say="ручка",
               x="К dan keyin -и: ручки."),
            RQ("“Мяч” ko‘plikda qanday?", "мячи", ["мячы", "мяча", "мячу"], say="мяч", d=2,
               x="Ч dan keyin -и: мячи."),
            RQ("“Машина” ko‘plikda qanday?", "машины", ["машини", "машину", "машиной"], say="машина",
               x="-а → -ы: машины."),
            RQ("“Море” ko‘plikda qanday?", "моря", ["мори", "моры", "морю"], say="море", d=3,
               x="-е → -я: море — моря."),
            RQ("“Карандаш” ko‘plikda qanday?", "карандаши", ["карандашы", "карандаша", "карандашу"], say="карандаш",
               d=2, x="Ш dan keyin -и: карандаши."),
            RQ("“Кошка” ko‘plikda qanday?", "кошки", ["кошкы", "кошку", "кошкой"], say="кошка",
               x="К dan keyin -и: кошки."),
            RQ("“Лампа” ko‘plikda qanday?", "лампы", ["лампи", "лампу", "лампой"], say="лампа",
               x="-а → -ы: лампы."),
            RQ("“Шары” so‘zining birlik shakli qanday?", "шар", ["шара", "шару", "шаром"], say="шары", d=2,
               x="Шары — шар (bitta shar)."),
            RQ("“Тетради” so‘zining birlik shakli qanday?", "тетрадь", ["тетрада", "тетраду", "тетрадо"],
               say="тетради", d=2, x="Тетради — тетрадь (bitta daftar)."),
            Q("Qaysi so‘z ko‘plikda?", "столы", ["стол", "книга", "окно"], x="Столы — ko‘p stol."),
            Q("Qaysi so‘z birlikda?", "ручка", ["книги", "окна", "мячи"], x="Ручка — bitta ruchka."),
            RQ("Mos so‘zni tanlang: Это … книги.", "мои", ["мой", "моя", "моё"], say="Это ... книги.", d=2,
               x="Книги — ko‘plik: мои книги."),
            LISTEN("Bu mashinalar.", ["Bu mashina.", "Bu mushuklar.", "Bu lampalar."], say="Это машины.", d=2),
            LISTEN("Bu kitob.", ["Bu kitoblar.", "Bu daftar.", "Bu daftarlar."], say="Это книга."),
            MATCH("Birlik va ko‘plikni juftlang",
                  [("стол", "столы"), ("книга", "книги"), ("окно", "окна"), ("мяч", "мячи"), ("лампа", "лампы"),
                   ("море", "моря"), ("ручка", "ручки")], d=2),
            RTF("“Книга” ko‘plikda “книги” bo‘ladi.", True, say="книга, книги", x="Г dan keyin -и: книги."),
            RTF("“Окно” ko‘plikda “окны” bo‘ladi.", False, say="окно", d=2, x="To‘g‘risi: окна."),
            SENT("Это мои книги", "Bu mening kitoblarim."),
            SENT("Где мои карандаши", "Mening qalamlarim qayerda?", d=2),
            RQ("“Банан” ko‘plikda qanday?", "бананы", ["банани", "банана", "банану"], say="банан",
               x="Банан — бананы (-ы qo‘shiladi)."),
            Q("Qaysi juftlik to‘g‘ri?", "сумка — сумки", ["сумка — сумкы", "окно — окны", "стол — столи"], d=3,
              x="К dan keyin -и: сумки."),
            Q("Qaysi so‘z ko‘plikda -и bilan tugaydi?", "книга", ["стол", "лампа", "окно"], d=3,
              x="Книга — книги; стол — столы, лампа — лампы, окно — окна."),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["animals", "fruits_veg", "gender", "plural"],
       chapter=C3)

# ============================================================ 4-chorak
T.topic("clothes", "👕", L("Kiyimlar", "Clothes", "Одежда"), chapter=C4, gen="vocab",
        theory="Kiyimlar (одежда): футболка (futbolka), брюки (shim), платье (ko‘ylak), пальто (palto),\n"
               "шарф (sharf), перчатки (qo‘lqop), носки (paypoq), кепка (kepka), кроссовки (krossovka).\n"
               "Kiyim nomi ham rodga ega: мой шарф, моя футболка, моё пальто, мои носки.\n"
               "Misol: Что это? — Это моё платье.",
        levels=vocab_levels("clothes"))

T.topic("days", "📅", L("Hafta kunlari", "Days of the week", "Дни недели"), chapter=C4,
        theory="Hafta kunlari (дни недели): понедельник (dushanba), вторник (seshanba), среда (chorshanba),\n"
               "четверг (payshanba), пятница (juma), суббота (shanba), воскресенье (yakshanba).\n"
               "• Kun nomlari kichik harf bilan yoziladi.\n"
               "• Qachon? — в понедельник, в среду, в субботу.\n"
               "Savol: Какой сегодня день? — Сегодня пятница.",
        items=[
            Q("“Dushanba” ruschasi qanday?", "понедельник", ["вторник", "среда", "пятница", "суббота"],
              x="Dushanba — понедельник."),
            Q("“Juma” ruschasi qanday?", "пятница", ["четверг", "суббота", "среда"], x="Juma — пятница."),
            Q("“Yakshanba” ruschasi qanday?", "воскресенье", ["суббота", "понедельник", "вторник"],
              x="Yakshanba — воскресенье."),
            RQ("“Среда” o‘zbekchasi qanday?", "chorshanba", ["seshanba", "payshanba", "juma"], say="среда",
               x="Среда — chorshanba."),
            RQ("“Четверг” o‘zbekchasi qanday?", "payshanba", ["chorshanba", "juma", "shanba"], say="четверг",
               x="Четверг — payshanba."),
            RQ("“Суббота” o‘zbekchasi qanday?", "shanba", ["yakshanba", "juma", "dushanba"], say="суббота",
               x="Суббота — shanba."),
            RQ("“Вторник” o‘zbekchasi qanday?", "seshanba", ["dushanba", "chorshanba", "payshanba"], say="вторник",
               x="Вторник — seshanba."),
            RQ("“Понедельник” kunidan keyin qaysi kun keladi?", "вторник", ["среда", "воскресенье", "четверг"],
               say="понедельник", x="Понедельник, вторник … — dushanbadan keyin seshanba."),
            RQ("“Пятница” kunidan keyin qaysi kun keladi?", "суббота", ["четверг", "воскресенье", "среда"],
               say="пятница", d=2, x="Jumadan keyin shanba: пятница, суббота."),
            RQ("“Среда” kunidan oldin qaysi kun keladi?", "вторник", ["четверг", "понедельник", "пятница"],
               say="среда", d=2, x="Chorshanbadan oldin seshanba: вторник, среда."),
            Q("Haftada nechta kun bor?", "7", ["5", "6", "8"], x="Haftada 7 kun bor."),
            Q("Haftaning birinchi kuni qaysi?", "понедельник", ["воскресенье", "суббота", "среда"],
              x="Hafta dushanba (понедельник) kuni boshlanadi."),
            Q("Haftaning oxirgi kuni qaysi?", "воскресенье", ["суббота", "пятница", "понедельник"], d=2,
              x="Hafta yakshanba (воскресенье) kuni tugaydi."),
            MATCH("Kun va tarjimasini juftlang",
                  [("понедельник", "dushanba"), ("вторник", "seshanba"), ("среда", "chorshanba"),
                   ("четверг", "payshanba"), ("пятница", "juma"), ("суббота", "shanba"),
                   ("воскресенье", "yakshanba")]),
            LISTEN("Bugun chorshanba.", ["Bugun payshanba.", "Ertaga chorshanba.", "Bugun seshanba."],
                   say="Сегодня среда.", d=2),
            LISTEN("Ertaga juma.", ["Bugun juma.", "Ertaga shanba.", "Kecha juma edi."], say="Завтра пятница.", d=3),
            Q("“Bugun” ruschasi qanday?", "сегодня", ["завтра", "вчера", "неделя"], d=2, x="Bugun — сегодня."),
            Q("“Ertaga” ruschasi qanday?", "завтра", ["сегодня", "вчера", "утро"], d=2, x="Ertaga — завтра."),
            Q("“Hafta” ruschasi qanday?", "неделя", ["день", "месяц", "год"], d=2, x="Hafta — неделя."),
            SENT("Какой сегодня день", "Bugun qanday kun?", d=2),
            SENT("Сегодня очень хороший день", "Bugun juda yaxshi kun.", d=3),
            TF("Rus tilida hafta kunlari bosh harf bilan yoziladi.", False, d=2,
               x="Kun nomlari kichik harf bilan yoziladi: понедельник, среда."),
            RTF("“Суббота” — shanba.", True, say="суббота", x="Суббота — shanba."),
            RQ("Qatorni to‘ldiring: понедельник, вторник, …, четверг", "среда", ["пятница", "суббота", "воскресенье"],
               say="понедельник, вторник, ..., четверг", x="Seshanbadan keyin chorshanba — среда."),
            RQ("Qatorni to‘ldiring: пятница, …, воскресенье", "суббота", ["четверг", "понедельник", "среда"],
               say="пятница, ..., воскресенье", d=2, x="Jumadan keyin shanba — суббота."),
            RQ("To‘g‘ri variantni tanlang: Я рисую …", "в субботу", ["в суббота", "в субботе", "на суббота"],
               say="Я рисую ...", d=3, x="Qachon? — в субботу (-а → -у)."),
        ])

T.topic("verbs", "🏃", L("Hozirgi zamon fe’llari", "Present tense verbs", "Глаголы настоящего времени"), chapter=C4,
        theory="Hozirgi zamonda fe’l shaxsga qarab o‘zgaradi (читать — o‘qimoq):\n"
               "• я читаю, ты читаешь, он/она читает\n"
               "• мы читаем, вы читаете, они читают\n"
               "Xuddi shunday: играть — я играю, ты играешь, он играет; рисовать — я рисую, он рисует.\n"
               "Misol: Я читаю книгу. Мама читает газету.",
        items=[
            RQ("Mos fe’lni tanlang: Я … книгу.", "читаю", ["читаешь", "читает", "читают"], say="Я ... книгу.",
               x="Я — читаю."),
            RQ("Mos fe’lni tanlang: Ты … в футбол.", "играешь", ["играю", "играет", "играем"], say="Ты ... в футбол.",
               x="Ты — играешь."),
            RQ("Mos fe’lni tanlang: Мама … газету.", "читает", ["читаю", "читаешь", "читаем"], say="Мама ... газету.",
               x="Мама (она) — читает."),
            RQ("Mos fe’lni tanlang: Мы … в парке.", "гуляем", ["гуляю", "гуляет", "гуляешь"], say="Мы ... в парке.",
               d=2, x="Мы — гуляем."),
            RQ("Mos fe’lni tanlang: Они … музыку.", "слушают", ["слушаю", "слушаешь", "слушаем"],
               say="Они ... музыку.", d=2, x="Они — слушают."),
            RQ("Mos fe’lni tanlang: Вы … уроки.", "делаете", ["делаю", "делает", "делают"], say="Вы ... уроки.", d=3,
               x="Вы — делаете."),
            RQ("Mos olmoshni tanlang: … читаю.", "Я", ["Ты", "Он", "Мы"], say="... читаю.", x="Читаю — я."),
            RQ("Mos olmoshni tanlang: … играешь.", "Ты", ["Я", "Она", "Они"], say="... играешь.", x="Играешь — ты."),
            RQ("Mos olmoshni tanlang: … рисует.", "Он", ["Я", "Ты", "Мы"], say="... рисует.", d=2,
               x="Рисует — он (yoki она)."),
            RQ("Mos olmoshni tanlang: … гуляют.", "Они", ["Я", "Он", "Ты"], say="... гуляют.", d=2,
               x="Гуляют — они."),
            Q("“O‘qimoq” ruschasi qanday?", "читать", ["писать", "играть", "рисовать"], x="O‘qimoq — читать."),
            Q("“O‘ynamoq” ruschasi qanday?", "играть", ["читать", "гулять", "слушать"], x="O‘ynamoq — играть."),
            RQ("“Рисовать” o‘zbekchasi qanday?", "rasm chizmoq", ["yozmoq", "o‘qimoq", "tinglamoq"], say="рисовать",
               x="Рисовать — rasm chizmoq."),
            RQ("“Писать” o‘zbekchasi qanday?", "yozmoq", ["o‘qimoq", "o‘ynamoq", "sayr qilmoq"], say="писать",
               x="Писать — yozmoq."),
            LISTEN("Men kitob o‘qiyapman.", ["Sen kitob o‘qiyapsan.", "Men xat yozyapman.", "U kitob o‘qiyapti."],
                   say="Я читаю книгу."),
            LISTEN("Bola futbol o‘ynayapti.", ["Qiz futbol o‘ynayapti.", "Bola kitob o‘qiyapti.",
                                              "Biz futbol o‘ynayapmiz."], say="Мальчик играет в футбол.", d=2),
            LISTEN("Biz rasm chizyapmiz.", ["Ular rasm chizyapti.", "Biz qo‘shiq aytyapmiz.", "Men rasm chizyapman."],
                   say="Мы рисуем.", d=2),
            MATCH("Olmosh va fe’lni juftlang",
                  [("я", "читаю"), ("ты", "читаешь"), ("он", "читает"), ("мы", "читаем"), ("вы", "читаете"),
                   ("они", "читают")], d=2),
            SENT("Я читаю интересную книгу", "Men qiziqarli kitob o‘qiyapman.", d=3),
            SENT("Папа читает газету", "Otam gazeta o‘qiyapti."),
            SENT("Дети играют в парке", "Bolalar parkda o‘ynayapti.", d=2),
            RTF("“Ты играешь” — to‘g‘ri birikma.", True, say="Ты играешь", x="Ты — играешь."),
            RTF("“Он читаю” — to‘g‘ri birikma.", False, say="Он читаю", d=2, x="To‘g‘risi: он читает."),
            Q("Qaysi gap to‘g‘ri?", "Сестра рисует.", ["Сестра рисую.", "Сестра рисуешь.", "Сестра рисуем."], d=2,
              x="Сестра (она) — рисует."),
            RQ("Mos fe’lni tanlang: Я … письмо.", "пишу", ["пишет", "пишешь", "пишут"], say="Я ... письмо.", d=3,
               x="Писать: я пишу, ты пишешь, он пишет."),
        ])

T.topic("prepositions", "📦", L("Qayerda? в va на", "Where? в and на", "Где? Предлоги в и на"), chapter=C4,
        theory="“Где?” (Qayerda?) savoliga javobda в va на ishlatiladi, so‘z oxiri ko‘pincha -е bo‘ladi:\n"
               "• в — ichida: в школе, в классе, в парке, в сумке.\n"
               "• на — ustida: на стуле, на диване, на полке, на стене.\n"
               "Misol: — Где мама? — Мама в магазине. — Где кошка? — Кошка на диване.\n"
               "здесь — shu yerda, там — u yerda.",
        items=[
            RQ("Mos predlogni tanlang: Дети … школе.", "в", ["на", "под"], say="Дети ... школе.",
               x="Maktab ichida — в школе."),
            RQ("Mos predlogni tanlang: Кошка … диване.", "на", ["в", "под"], say="Кошка ... диване.",
               x="Divan ustida — на диване."),
            RQ("Mos predlogni tanlang: Мы гуляем … парке.", "в", ["на", "под"], say="Мы гуляем ... парке.",
               x="Park ichida — в парке."),
            RQ("Mos predlogni tanlang: Картина … стене.", "на", ["в", "под"], say="Картина ... стене.",
               x="Devorda (ustida) — на стене."),
            RQ("Mos predlogni tanlang: Птица сидит … дереве.", "на", ["в", "под"], say="Птица сидит ... дереве.", d=2,
               x="Daraxt ustida — на дереве."),
            RQ("Mos predlogni tanlang: Я живу … Ташкенте.", "в", ["на", "под"], say="Я живу ... Ташкенте.",
               x="Shahar ichida — в Ташкенте."),
            RQ("Mos predlogni tanlang: Книги … полке.", "на", ["в", "под"], say="Книги ... полке.", d=2,
               x="Javon ustida — на полке."),
            RQ("To‘g‘ri variantni tanlang: Где папа? — Папа …", "в магазине", ["в магазин", "на магазине", "магазин"],
               say="Где папа? Папа ...", d=2, x="Где? — в магазине (-е)."),
            RQ("To‘g‘ri variantni tanlang: Где мяч? — Мяч …", "на стуле", ["на стул", "в стуле", "стул"],
               say="Где мяч? Мяч ...", d=2, x="Где? — на стуле (-е)."),
            RQ("To‘g‘ri variantni tanlang: Где ученики? — Ученики …", "в классе", ["в класс", "на классе", "класс"],
               say="Где ученики? Ученики ...", d=3, x="Где? — в классе (-е)."),
            Q("“Qayerda?” ruschasi qanday?", "где", ["что", "кто", "как"], x="Qayerda? — Где?"),
            RQ("“Где книга?” o‘zbekchasi qanday?", "Kitob qayerda?", ["Bu kitobmi?", "Kitob nima?", "Kitob kimniki?"],
               say="Где книга?", x="Где? — qayerda?"),
            LISTEN("Mushuk divanda.", ["Mushuk stulda.", "It divanda.", "Mushuk bog‘da."], say="Кошка на диване."),
            LISTEN("Onam do‘konda.", ["Onam maktabda.", "Otam do‘konda.", "Onam uyda."], say="Мама в магазине.", d=2),
            LISTEN("Kitob javonda.", ["Kitob sumkada.", "Daftar javonda.", "Kitob stulda."], say="Книга на полке.",
                   d=2),
            RQ("Qaysi javob “Где?” savoliga mos?", "в парке", ["парк", "в парк", "парка"], say="Где?", d=3,
              x="Где? — в парке (в + -е)."),
            SENT("Мяч на стуле", "Koptok stulda."),
            SENT("Мой брат в школе", "Akam maktabda."),
            SENT("Мы гуляем в парке", "Biz parkda sayr qilyapmiz.", d=2),
            SENT("Где твоя сумка", "Sumkang qayerda?", d=2),
            RTF("“На стуле” — “stulning ustida” degani.", True, say="на стуле", x="На стуле — stulda (ustida)."),
            RTF("“В школе” — “maktabga” degani.", False, say="в школе", d=2,
                x="В школе — maktabda (qayerda?)."),
            MATCH("Birikma va tarjimasini juftlang",
                  [("в школе", "maktabda"), ("в парке", "parkda"), ("на стуле", "stulda"), ("в сумке", "sumkada"),
                   ("на стене", "devorda"), ("в городе", "shaharda")], d=2),
            RQ("“Здесь” o‘zbekchasi qanday?", "shu yerda", ["u yerda", "qayerda", "ichida"], say="здесь", d=2,
               x="Здесь — shu yerda; там — u yerda."),
            RQ("“Там” o‘zbekchasi qanday?", "u yerda", ["shu yerda", "qachon", "qayerda"], say="там", d=2,
               x="Там — u yerda."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["clothes", "days", "verbs", "prepositions"],
       chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["alphabet", "greet", "family", "school", "colors", "numbers", "animals", "fruits_veg", "gender", "plural",
        "clothes", "days", "verbs", "prepositions"], chapter=C4, level=3)

T.write()
