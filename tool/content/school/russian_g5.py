"""Rus tili (o‘zbek maktablari uchun), 5-sinf: assets/data/school/russian_g5.json + bank_russian_g5.json.

Mavzular O‘zbekiston maktab dasturi ("Rus tili", 5-sinf, ≈A1+/A2) tartibida; hamma matn va savollar o‘zimizniki
(o‘qish matnlari ham darslikdan ko‘chirilmagan).
Lug‘at mavzulari (transport, kasblar, rasmga qarab gap) — umumiy `foreign_language.dart` generatorlari,
grammatika, iboralar va o‘qish — savollar banki.
Qayta yaratish: python3 tool/content/school/russian_g5.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("russian", 5, L("Rus tili", "Russian", "Русский язык"))

C1 = "1-chorak. Ot, sifat va olmosh"
C2 = "2-chorak. Fe’l va mening kunim"
C3 = "3-chorak. Sonlar, vaqt va shahar"
C4 = "4-chorak. Kasblar, fasllar va do‘kon"


# ------------------------------------------------------------ yordamchilar
def RQ(q, a, w, say, d=1, x=None, e=None, h=None):
    """Savolda ruscha matn bor: ovozda `say` rus tilida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=say, lang="ru")


def LISTEN(a, w, say, d=1, x=None):
    """Tinglab tushunish: ruscha gap eshitiladi, o‘zbekcha tarjimasi tanlanadi."""
    return Q("Tinglang va tarjimasini tanlang", a, w, d=d, x=x or f"{say} — {a}", say=say, lang="ru")


def HEAR(q, a, w, say, d=1, x=None):
    """Tinglab son yoki vaqtni tanlash."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", say=say, lang="ru")


def SENT(ru, tr, d=1):
    """Ruscha gap tuzish (tinish belgisiz)."""
    end = "?" if tr.endswith("?") else "."
    return ORDER("So‘zlardan gap tuzing", ru, d=d, x=f"{ru}{end} — {tr}", lang="ru")


def RTF(q, a, say, d=1, x=None):
    return TF(q, a, d=d, x=x, say=say, lang="ru")


def READ(text, emoji, questions):
    """O‘qish matni: bir matnga bir nechta savol (Q yoki TF) — `text` maydoni to‘ldiriladi."""
    out = []
    for it in questions:
        out.append({**it, "text": text, "e": emoji})
    return out


def vocab_levels(theme):
    return [
        {"themes": [theme], "modes": ["listen", "read"], "options": 3},
        {"themes": [theme], "modes": ["read", "picture_word", "listen"], "options": 4, "sameTheme": True},
        {"themes": [theme], "modes": ["picture_word", "listen", "read"], "options": 4, "sameTheme": True},
    ]


# ============================================================ 1-chorak
T.topic("nouns", "📘", L("Ot: rod va son", "Nouns: gender and number", "Существительное: род и число"), chapter=C1,
        theory="Otning rodi so‘z oxiridan aniqlanadi:\n"
               "• он: стол, город, музей — этот, мой;  она: книга, земля — эта, моя;  оно: окно, поле — это, моё.\n"
               "• -ь bilan tugagan so‘zlar rodini yodlang: день — он, тетрадь — она.\n"
               "Ko‘plik: -ы / -и (столы, книги), -а / -я (окна, поля).\n"
               "Istisnolar: город — города, друг — друзья, брат — братья, ребёнок — дети, человек — люди.",
        items=[
            RQ("“Город” qaysi rodda?", "он", ["она", "оно"], say="город", x="Город undosh bilan tugaydi — он."),
            RQ("“Земля” qaysi rodda?", "она", ["он", "оно"], say="земля", x="Земля -я bilan tugaydi — она."),
            RQ("“Поле” qaysi rodda?", "оно", ["он", "она"], say="поле", x="Поле -е bilan tugaydi — оно."),
            RQ("“Музей” qaysi rodda?", "он", ["она", "оно"], say="музей", d=2, x="Музей -й bilan tugaydi — он."),
            RQ("“Тетрадь” qaysi rodda?", "она", ["он", "оно"], say="тетрадь", d=3,
               x="-ь bilan tugagan so‘z rodini yodlaymiz: тетрадь — она (моя тетрадь)."),
            RQ("“День” qaysi rodda?", "он", ["она", "оно"], say="день", d=3,
               x="День — он: мой день, хороший день."),
            RQ("Mos so‘zni tanlang: … город очень красивый.", "Этот", ["Эта", "Это", "Эти"],
               say="... город очень красивый.", d=2, x="Город — он: этот город."),
            RQ("Mos so‘zni tanlang: … книга интересная.", "Эта", ["Этот", "Это", "Эти"],
               say="... книга интересная.", d=2, x="Книга — она: эта книга."),
            RQ("Mos so‘zni tanlang: … окно большое.", "Это", ["Этот", "Эта", "Эти"], say="... окно большое.", d=2,
               x="Окно — оно: это окно."),
            RQ("Mos so‘zni tanlang: … ручки новые.", "Эти", ["Этот", "Эта", "Это"], say="... ручки новые.", d=3,
               x="Ручки — ko‘plik: эти ручки."),
            RQ("“Город” ko‘plikda qanday?", "города", ["городы", "городи", "городов"], say="город", d=3,
               x="Город — istisno: города (xuddi дом — дома)."),
            RQ("“Друг” ko‘plikda qanday?", "друзья", ["други", "друга", "другу"], say="друг", d=2,
               x="Друг — istisno: друзья."),
            RQ("“Ребёнок” ko‘plikda qanday?", "дети", ["ребёнки", "детей", "ребёнка"], say="ребёнок", d=2,
               x="Ребёнок — дети (boshqa so‘z bilan)."),
            RQ("“Человек” ko‘plikda qanday?", "люди", ["человеки", "человеков", "человека"], say="человек", d=2,
               x="Человек — люди."),
            RQ("“Слово” ko‘plikda qanday?", "слова", ["словы", "слови", "слову"], say="слово",
               x="-о → -а: слово — слова."),
            RQ("“Картина” ko‘plikda qanday?", "картины", ["картини", "картину", "картиной"], say="картина",
               x="-а → -ы: картины."),
            RQ("“Девочка” ko‘plikda qanday?", "девочки", ["девочкы", "девочку", "девочкой"], say="девочка",
               x="К dan keyin -и yoziladi: девочки."),
            RQ("“Словари” so‘zining birlik shakli qanday?", "словарь", ["словар", "словаря", "словарём"],
               say="словари", d=2, x="Словари — словарь (он)."),
            RQ("Qaysi so‘z “оно” rodida?", "здание", ["улица", "парк", "площадь"], say="оно", x="Здание -е bilan tugaydi — оно."),
            RQ("Qaysi so‘z “она” rodida?", "площадь", ["музей", "театр", "кино"], say="она", d=3,
               x="Площадь -ь bilan tugaydi, u она rodida: большая площадь."),
            RQ("Qaysi so‘z “он” rodida?", "портфель", ["ручка", "окно", "доска"], say="он", d=3,
               x="Портфель — он: мой портфель."),
            MATCH("Birlik va ko‘plikni juftlang (istisnolar)",
                  [("брат", "братья"), ("друг", "друзья"), ("ребёнок", "дети"), ("человек", "люди"), ("дом", "дома"),
                   ("стул", "стулья")], d=2),
            RTF("“Окно” so‘zining ko‘plik shakli — “окна”.", True, say="окно, окна", x="Окно — окна."),
            RTF("“Мама” — оно rodida.", False, say="мама", x="Мама — она."),
            SENT("Эти книги очень интересные", "Bu kitoblar juda qiziqarli.", d=2),
            SENT("Этот парк большой и красивый", "Bu park katta va chiroyli.", d=3),
            Q("Qaysi so‘z ko‘plikda?", "улицы", ["улица", "театр", "окно"], x="Улицы — ko‘p ko‘cha."),
            Q("Qaysi so‘z birlikda?", "музей", ["города", "книги", "дети"], x="Музей — bitta muzey."),
        ])

T.topic("adjectives", "🌈", L("Sifat va ot moslashuvi", "Adjective agreement", "Согласование прилагательных"),
        chapter=C1,
        theory="Sifat otning rodi va soniga moslashadi:\n"
               "• он — какой? красный мяч, новый дом, синий шарф, большой город\n"
               "• она — какая? красная машина, новая книга, синяя куртка\n"
               "• оно — какое? красное яблоко, новое окно, синее море\n"
               "• они — какие? красные цветы, новые книги, синие ручки",
        items=[
            RQ("Mos sifatni tanlang: … мяч", "красный", ["красная", "красное", "красные"], say="... мяч",
               x="Мяч — он: красный мяч."),
            RQ("Mos sifatni tanlang: … машина", "красная", ["красный", "красное", "красные"], say="... машина",
               x="Машина — она: красная машина."),
            RQ("Mos sifatni tanlang: … яблоко", "красное", ["красный", "красная", "красные"], say="... яблоко",
               x="Яблоко — оно: красное яблоко."),
            RQ("Mos sifatni tanlang: … цветы", "красные", ["красный", "красная", "красное"], say="... цветы",
               x="Цветы — ko‘plik: красные цветы."),
            RQ("Mos sifatni tanlang: … дом", "новый", ["новая", "новое", "новые"], say="... дом",
               x="Дом — он: новый дом."),
            RQ("Mos sifatni tanlang: … книга", "интересная", ["интересный", "интересное", "интересные"],
               say="... книга", x="Книга — она: интересная книга."),
            RQ("Mos sifatni tanlang: … море", "синее", ["синий", "синяя", "синие"], say="... море", d=2,
               x="Море — оно: синее море."),
            RQ("Mos sifatni tanlang: … куртка", "синяя", ["синий", "синее", "синие"], say="... куртка", d=2,
               x="Куртка — она: синяя куртка."),
            RQ("Mos sifatni tanlang: … город", "большой", ["большая", "большое", "большие"], say="... город",
               x="Город — он: большой город."),
            RQ("Mos sifatni tanlang: Сегодня … погода.", "хорошая", ["хороший", "хорошее", "хорошие"],
               say="Сегодня ... погода.", d=2, x="Погода — она: хорошая погода."),
            RQ("Mos so‘roq so‘zni tanlang: … платье? — Белое.", "Какое", ["Какой", "Какая", "Какие"],
               say="... платье? Белое.", d=2, x="Платье — оно: какое платье?"),
            RQ("Mos so‘roq so‘zni tanlang: … стол? — Круглый.", "Какой", ["Какая", "Какое", "Какие"],
               say="... стол? Круглый.", d=2, x="Стол — он: какой стол?"),
            RQ("Mos so‘roq so‘zni tanlang: … сумка? — Новая.", "Какая", ["Какой", "Какое", "Какие"],
               say="... сумка? Новая.", d=2, x="Сумка — она: какая сумка?"),
            Q("“Katta” ruschasi qanday?", "большой", ["маленький", "новый", "старый"], x="Katta — большой."),
            RQ("“Старый” o‘zbekchasi qanday?", "eski, qari", ["yangi", "katta", "kichik"], say="старый",
               x="Старый — eski (narsa) yoki qari (odam)."),
            MATCH("Qarama-qarshi sifatlarni juftlang",
                  [("большой", "маленький"), ("новый", "старый"), ("весёлый", "грустный"), ("длинный", "короткий"),
                   ("холодный", "горячий"), ("белый", "чёрный")], d=2),
            MATCH("Sifat va tarjimasini juftlang",
                  [("красивый", "chiroyli"), ("умный", "aqlli"), ("добрый", "mehribon"), ("высокий", "baland"),
                   ("быстрый", "tez"), ("вкусный", "mazali")]),
            Q("Qaysi birikma to‘g‘ri?", "зелёное яблоко", ["зелёный яблоко", "зелёная яблоко", "зелёные яблоко"], d=2,
              x="Яблоко — оно: зелёное яблоко."),
            Q("Qaysi birikma to‘g‘ri?", "тёплая куртка", ["тёплый куртка", "тёплое куртка", "тёплые куртка"], d=2,
              x="Куртка — она: тёплая куртка."),
            Q("Qaysi birikma to‘g‘ri?", "маленькие котята", ["маленький котята", "маленькая котята",
                                                          "маленькое котята"], d=3,
              x="Котята — ko‘plik: маленькие котята."),
            LISTEN("Mening mushugim oq va yumshoq.", ["Mening itim oq va katta.", "Mening mushugim qora va kichkina.",
                                                    "Uning mushugi oq va yumshoq."],
                   say="Моя кошка белая и мягкая.", d=2),
            LISTEN("Bu yangi maktab.", ["Bu eski maktab.", "Bu yangi kitob.", "Bu katta maktab."],
                   say="Это новая школа."),
            SENT("У меня новый синий рюкзак", "Mening yangi ko‘k ryukzagim bor.", d=3),
            SENT("Это очень вкусное мороженое", "Bu juda mazali muzqaymoq.", d=2),
            RTF("“Красивая город” — to‘g‘ri birikma.", False, say="красивая город", d=2,
                x="Город — он: красивый город."),
            RTF("“Жёлтое солнце” — to‘g‘ri birikma.", True, say="жёлтое солнце", d=2,
                x="Солнце — оно: жёлтое солнце."),
            RQ("Qaysi sifat “она” rodidagi otga mos keladi?", "весёлая", ["весёлый", "весёлое", "весёлые"], say="она",
               x="Она rodida sifat -ая bilan tugaydi: весёлая."),
        ])

T.topic("pronouns", "🙋", L("Kishilik va egalik olmoshlari", "Personal and possessive pronouns",
                            "Личные и притяжательные местоимения"), chapter=C1,
        theory="Kishilik olmoshlari: я (men), ты (sen), он, она, оно (u), мы (biz), вы (siz), они (ular).\n"
               "Egalik olmoshlari — чей? чья? чьё? чьи? (kimning?):\n"
               "• мой, моя, моё, мои — mening;  твой, твоя, твоё, твои — sening\n"
               "• наш, наша, наше, наши — bizning;  ваш, ваша, ваше, ваши — sizning\n"
               "• его (uning — erkak), её (uning — ayol), их (ularning) o‘zgarmaydi: его книга, её брат, их дом.",
        items=[
            Q("“Biz” ruschasi qanday?", "мы", ["вы", "они", "я"], x="Biz — мы."),
            Q("“Ular” ruschasi qanday?", "они", ["мы", "вы", "оно"], x="Ular — они."),
            Q("“Sen” ruschasi qanday?", "ты", ["я", "вы", "он"], x="Sen — ты."),
            RQ("“Вы” o‘zbekchasi qanday?", "siz", ["biz", "ular", "sen"], say="вы", x="Вы — siz."),
            RQ("Olmosh bilan almashtiring: Мама читает. → … читает.", "Она", ["Он", "Оно", "Они"],
               say="Мама читает. ... читает.", x="Мама — ayol kishi: она."),
            RQ("Olmosh bilan almashtiring: Али и Бобур играют. → … играют.", "Они", ["Мы", "Он", "Вы"],
               say="Али и Бобур играют. ... играют.", x="Ikki kishi — они."),
            RQ("Olmosh bilan almashtiring: Окно открыто. → … открыто.", "Оно", ["Он", "Она", "Они"],
               say="Окно открыто. ... открыто.", d=2, x="Окно — оно."),
            RQ("Olmosh bilan almashtiring: Я и мама гуляем. → … гуляем.", "Мы", ["Вы", "Они", "Я"],
               say="Я и мама гуляем. ... гуляем.", d=2, x="Men va onam — biz: мы."),
            RQ("Mos olmoshni tanlang: Это … (bizning) школа.", "наша", ["наш", "наше", "наши"], say="Это ... школа.",
               x="Школа — она: наша школа."),
            RQ("Mos olmoshni tanlang: Это … (sizning) дом.", "ваш", ["ваша", "ваше", "ваши"], say="Это ... дом.", d=2,
               x="Дом — он: ваш дом."),
            RQ("Mos olmoshni tanlang: Где … (sening) тетради?", "твои", ["твой", "твоя", "твоё"],
               say="Где ... тетради?", d=2, x="Тетради — ko‘plik: твои тетради."),
            RQ("Mos olmoshni tanlang: Это … (sening) письмо.", "твоё", ["твой", "твоя", "твои"],
               say="Это ... письмо.", d=2, x="Письмо — оно: твоё письмо."),
            RQ("Mos olmoshni tanlang: Это Анвар. Это … велосипед.", "его", ["её", "их"],
               say="Это Анвар. Это ... велосипед.", d=2, x="Anvar — erkak kishi: его велосипед."),
            RQ("Mos olmoshni tanlang: Это Лола. Это … сумка.", "её", ["его", "их"],
               say="Это Лола. Это ... сумка.", d=2, x="Lola — ayol kishi: её сумка."),
            Q("“Ularning uyi” ruschasi qanday?", "их дом", ["его дом", "её дом", "наш дом"], d=2,
              x="Ularning — их (o‘zgarmaydi): их дом."),
            RQ("Mos so‘roq so‘zni tanlang: … это книга? — Моя.", "Чья", ["Чей", "Чьё", "Чьи"],
               say="... это книга? Моя.", d=3, x="Книга — она: чья книга?"),
            RQ("Mos so‘roq so‘zni tanlang: … это рюкзак? — Мой.", "Чей", ["Чья", "Чьё", "Чьи"],
               say="... это рюкзак? Мой.", d=3, x="Рюкзак — он: чей рюкзак?"),
            MATCH("Olmosh va tarjimasini juftlang",
                  [("я", "men"), ("ты", "sen"), ("мы", "biz"), ("вы", "siz"), ("они", "ular"), ("наш", "bizning"),
                   ("твой", "sening")]),
            LISTEN("Bu bizning sinfimiz.", ["Bu sizning sinfingiz.", "Bu ularning sinfi.", "Bu bizning maktabimiz."],
                   say="Это наш класс."),
            LISTEN("Uning onasi — o‘qituvchi.", ["Mening onam — o‘qituvchi.", "Uning otasi — o‘qituvchi.",
                                                "Uning onasi — shifokor."], say="Её мама — учительница.", d=2),
            SENT("Это наша новая школа", "Bu bizning yangi maktabimiz.", d=2),
            SENT("Где твой брат", "Akang (ukang) qayerda?"),
            RTF("“Их” so‘zi “ularning” degani.", True, say="их", x="Их — ularning: их дом, их школа."),
            RTF("“Наша дом” — to‘g‘ri birikma.", False, say="наша дом", d=2, x="Дом — он: наш дом."),
            Q("Qaysi birikma to‘g‘ri?", "ваши друзья", ["ваш друзья", "ваша друзья", "ваше друзья"], d=3,
              x="Друзья — ko‘plik: ваши друзья."),
        ])

T.topic("sentences", "💬", L("Rasmga qarab gap", "Picture sentences", "Предложения по картинке"), chapter=C1,
        gen="sentence",
        theory="Rus tilida hozirgi zamonda “bo‘lmoq” fe’li aytilmaydi: Мяч красный. (To‘p qizil.)\n"
               "• Это … — Bu …: Это мяч. Это кошка.\n"
               "• Sifat otga moslashadi: Мяч красный. Машина красная. Яблоко красное.\n"
               "• Kim nima qiladi: Кошка спит. Птица летит.",
        levels=[
            {"types": ["this", "color"], "modes": ["read", "picture"]},
            {"types": ["color", "action"], "modes": ["read", "picture", "listen"]},
            {"types": ["color", "action"], "modes": ["picture", "listen", "build"]},
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["nouns", "adjectives", "pronouns", "sentences"],
       chapter=C1)

# ============================================================ 2-chorak
T.topic("conjugation", "🗣️", L("Fe’l tuslanishi", "Verb conjugation", "Спряжение глаголов"), chapter=C2,
        theory="Hozirgi zamonda fe’llar ikki xil tuslanadi:\n"
               "• I tuslanish (-е-): читать — я читаю, ты читаешь, он читает, мы читаем, вы читаете, они читают.\n"
               "• II tuslanish (-и-): говорить — я говорю, ты говоришь, он говорит, мы говорим, вы говорите, они говорят.\n"
               "II tuslanishga ko‘pincha -ить bilan tugagan fe’llar kiradi: говорить, учить, звонить, любить (я люблю).\n"
               "Diqqat: смотреть ham II tuslanish — ты смотришь, они смотрят.",
        items=[
            RQ("Mos fe’lni tanlang: Я … по-русски.", "говорю", ["говоришь", "говорит", "говорят"],
               say="Я ... по-русски.", x="Я — говорю."),
            RQ("Mos fe’lni tanlang: Ты … по-узбекски.", "говоришь", ["говорю", "говорим", "говорят"],
               say="Ты ... по-узбекски.", x="Ты — говоришь."),
            RQ("Mos fe’lni tanlang: Они … по-английски.", "говорят", ["говорит", "говорим", "говорите"],
               say="Они ... по-английски.", d=2, x="II tuslanish: они говорят."),
            RQ("Mos fe’lni tanlang: Мы … текст.", "читаем", ["читаю", "читают", "читаешь"], say="Мы ... текст.",
               x="Мы — читаем."),
            RQ("Mos fe’lni tanlang: Вы … стихи.", "учите", ["учишь", "учит", "учим"], say="Вы ... стихи.", d=2,
               x="Вы — учите."),
            RQ("Mos fe’lni tanlang: Бабушка … телевизор.", "смотрит", ["смотрю", "смотришь", "смотрят"],
               say="Бабушка ... телевизор.", d=2, x="Бабушка (она) — смотрит."),
            RQ("Mos fe’lni tanlang: Я … маму.", "люблю", ["любит", "любишь", "любим"], say="Я ... маму.", d=2,
               x="Любить: я люблю, ты любишь."),
            RQ("Mos fe’lni tanlang: Сестра … письмо.", "пишет", ["пишу", "пишешь", "пишут"],
               say="Сестра ... письмо.", d=2, x="Сестра (она) — пишет."),
            RQ("Mos fe’lni tanlang: Дети … в футбол.", "играют", ["играет", "играем", "играешь"],
               say="Дети ... в футбол.", x="Дети (они) — играют."),
            RQ("Mos fe’lni tanlang: Папа … другу.", "звонит", ["звоню", "звоним", "звонят"], say="Папа ... другу.",
               d=3, x="Папа (он) — звонит."),
            Q("Qaysi fe’l II tuslanishga kiradi?", "говорить", ["читать", "играть", "гулять"], d=2,
              x="Говорить -ить bilan tugaydi: ты говоришь."),
            Q("Qaysi fe’l I tuslanishga kiradi?", "делать", ["говорить", "учить", "звонить"], d=2,
              x="Делать: ты делаешь, он делает (-е-)."),
            Q("“Gapirmoq” ruschasi qanday?", "говорить", ["смотреть", "слушать", "делать"], x="Gapirmoq — говорить."),
            RQ("“Смотреть” o‘zbekchasi qanday?", "ko‘rmoq, tomosha qilmoq", ["tinglamoq", "gapirmoq", "yozmoq"],
               say="смотреть", x="Смотреть — ko‘rmoq, tomosha qilmoq."),
            RQ("“Учить” o‘zbekchasi qanday?", "o‘rganmoq, o‘rgatmoq", ["o‘ynamoq", "qo‘ng‘iroq qilmoq", "sevmoq"],
               say="учить", d=2, x="Учить — o‘rganmoq (учить стихи) yoki o‘rgatmoq."),
            MATCH("Olmosh va fe’lni juftlang",
                  [("я", "говорю"), ("ты", "говоришь"), ("он", "говорит"), ("мы", "говорим"), ("вы", "говорите"),
                   ("они", "говорят")], d=2),
            MATCH("Fe’l va tarjimasini juftlang",
                  [("читать", "o‘qimoq"), ("писать", "yozmoq"), ("говорить", "gapirmoq"), ("слушать", "tinglamoq"),
                   ("смотреть", "tomosha qilmoq"), ("звонить", "qo‘ng‘iroq qilmoq")]),
            LISTEN("Men ruscha gapiraman.", ["Sen ruscha gapirasan.", "Men ruscha o‘qiyman.", "Biz ruscha gapiramiz."],
                   say="Я говорю по-русски."),
            LISTEN("Ular multfilm ko‘ryapti.", ["Biz multfilm ko‘ryapmiz.", "Ular kitob o‘qiyapti.",
                                               "U multfilm ko‘ryapti."], say="Они смотрят мультфильм.", d=2),
            SENT("Мы говорим по-русски", "Biz ruscha gapiramiz."),
            SENT("Мой брат учит английский язык", "Akam ingliz tilini o‘rganyapti.", d=3),
            RTF("“Он говорит” — to‘g‘ri shakl.", True, say="Он говорит", x="Он — говорит."),
            RTF("“Они говорют” — to‘g‘ri shakl.", False, say="Они говорют", d=2, x="II tuslanish: они говорят."),
            Q("Qaysi gap to‘g‘ri?", "Ты смотришь фильм.", ["Ты смотрит фильм.", "Ты смотрю фильм.",
                                                          "Ты смотрят фильм."], x="Ты — смотришь."),
        ])

T.topic("past", "⏪", L("O‘tgan zamon", "Past tense", "Прошедшее время"), chapter=C2,
        theory="O‘tgan zamonda fe’l oxiridagi -ть o‘rniga -л qo‘yiladi va rod-songa moslashadi:\n"
               "• читать: он читал, она читала, оно читало, они читали\n"
               "• быть: он был, она была, оно было, они были\n"
               "Fe’l shaxsga emas, rod va songa qarab o‘zgaradi: Али читал, Лола читала, мы читали.\n"
               "Misol: Вчера я был в парке (o‘g‘il bola). Вчера я была в парке (qiz bola).",
        items=[
            RQ("Mos fe’lni tanlang: Вчера папа … газету.", "читал", ["читала", "читало", "читали"],
               say="Вчера папа ... газету.", x="Папа — он: читал."),
            RQ("Mos fe’lni tanlang: Вчера мама … суп.", "варила", ["варил", "варило", "варили"],
               say="Вчера мама ... суп.", d=2, x="Мама — она: варила."),
            RQ("Mos fe’lni tanlang: Вчера мы … в парке.", "гуляли", ["гулял", "гуляла", "гуляло"],
               say="Вчера мы ... в парке.", x="Мы — ko‘plik: гуляли."),
            RQ("Mos fe’lni tanlang: Лола … письмо.", "писала", ["писал", "писало", "писали"],
               say="Лола ... письмо.", x="Лола — она: писала."),
            RQ("Mos fe’lni tanlang: Вчера … холодно.", "было", ["был", "была", "были"], say="Вчера ... холодно.", d=3,
               x="Холодно — rodsiz so‘z, shuning uchun оно shakli ishlatiladi: было холодно."),
            RQ("Bobur aytadi: Вчера я … в школе.", "был", ["была", "было", "были"], say="Вчера я ... в школе.", d=2,
               x="Bobur — o‘g‘il bola: я был."),
            RQ("Zarina aytadi: Вчера я … в музее.", "была", ["был", "было", "были"], say="Вчера я ... в музее.", d=2,
               x="Zarina — qiz bola: я была."),
            RQ("Mos fe’lni tanlang: Летом дети … на море.", "были", ["был", "была", "было"],
               say="Летом дети ... на море.", d=2, x="Дети — ko‘plik: были."),
            RQ("Mos fe’lni tanlang: Утром солнце … ярко.", "светило", ["светил", "светила", "светили"],
               say="Утром солнце ... ярко.", d=3, x="Солнце — оно: светило."),
            RQ("“Читать” fe’lining o‘tgan zamon shakli (он) qanday?", "читал", ["читает", "читать", "читаю"],
               say="читать", x="Читать → читал."),
            RQ("“Играть” fe’lining o‘tgan zamon shakli (они) qanday?", "играли", ["играют", "играл", "играла"],
               say="играть", d=2, x="Они — играли."),
            Q("Qaysi fe’l o‘tgan zamonda?", "рисовал", ["рисует", "рисую", "рисовать"],
              x="Рисовал — -л qo‘shimchasi o‘tgan zamonni bildiradi."),
            Q("Qaysi so‘z o‘tgan zamonni bildiradi?", "вчера", ["сегодня", "завтра", "сейчас"],
              x="Вчера — kecha."),
            Q("“Kecha” ruschasi qanday?", "вчера", ["завтра", "сегодня", "утром"], x="Kecha — вчера."),
            LISTEN("Kecha men kitob o‘qidim.", ["Bugun men kitob o‘qiyapman.", "Ertaga men kitob o‘qiyman.",
                                               "Kecha men xat yozdim."], say="Вчера я читал книгу."),
            LISTEN("Yozda biz Samarqandda edik.", ["Qishda biz Samarqandda edik.", "Yozda biz Buxoroda edik.",
                                                  "Yozda biz Samarqandga boramiz."],
                   say="Летом мы были в Самарканде.", d=2),
            LISTEN("Qiz rasm chizdi.", ["Bola rasm chizdi.", "Qiz rasm chizyapti.", "Qiz qo‘shiq aytdi."],
                   say="Девочка рисовала.", d=2),
            MATCH("Hozirgi va o‘tgan zamonni juftlang",
                  [("читает", "читал"), ("пишет", "писал"), ("играет", "играл"), ("говорит", "говорил"),
                   ("смотрит", "смотрел"), ("живёт", "жил")], d=2),
            SENT("Вчера мы были в театре", "Kecha biz teatrda edik.", d=2),
            SENT("Мама купила хлеб", "Onam non sotib oldi."),
            SENT("Летом я отдыхал в деревне", "Yozda men qishloqda dam oldim.", d=3),
            RTF("“Она читал” — to‘g‘ri shakl.", False, say="Она читал", x="Она — читала."),
            RTF("“Они были” — to‘g‘ri shakl.", True, say="Они были", x="Они — были."),
            Q("Qaysi gap to‘g‘ri?", "Вчера была хорошая погода.", ["Вчера был хорошая погода.",
                                                                  "Вчера было хорошая погода.",
                                                                  "Вчера были хорошая погода."], d=3,
              x="Погода — она: была хорошая погода."),
        ])

T.topic("my_day", "⏰", L("Mening kunim", "My day", "Мой день"), chapter=C2,
        theory="Kun tartibi (режим дня):\n"
               "• Утром я встаю, умываюсь, делаю зарядку и завтракаю.\n"
               "• Днём я учусь в школе, потом обедаю и делаю уроки.\n"
               "• Вечером я ужинаю, читаю и ложусь спать.\n"
               "Kun qismlari: утром (ertalab), днём (kunduzi), вечером (kechqurun), ночью (kechasi).",
        items=[
            Q("“Ertalab” ruschasi qanday?", "утром", ["вечером", "днём", "ночью"], x="Ertalab — утром."),
            Q("“Kechqurun” ruschasi qanday?", "вечером", ["утром", "днём", "вчера"], x="Kechqurun — вечером."),
            RQ("“Завтракать” o‘zbekchasi qanday?", "nonushta qilmoq", ["tushlik qilmoq", "kechki ovqat yemoq",
                                                                     "uxlamoq"], say="завтракать",
               x="Завтракать — nonushta qilmoq (завтрак — nonushta)."),
            RQ("“Обедать” o‘zbekchasi qanday?", "tushlik qilmoq", ["nonushta qilmoq", "kechki ovqat yemoq",
                                                                 "yuvinmoq"], say="обедать",
               x="Обедать — tushlik qilmoq (обед — tushlik)."),
            RQ("“Ужинать” o‘zbekchasi qanday?", "kechki ovqat yemoq", ["nonushta qilmoq", "tushlik qilmoq",
                                                                     "o‘rnidan turmoq"], say="ужинать", d=2,
               x="Ужинать — kechki ovqat yemoq (ужин — kechki ovqat)."),
            Q("“O‘rnidan turmoq” ruschasi qanday?", "вставать", ["ложиться", "умываться", "гулять"], d=2,
              x="O‘rnidan turmoq — вставать: я встаю."),
            RQ("Mos so‘zni tanlang: Утром я … зубы.", "чищу", ["читаю", "играю", "пишу"], say="Утром я ... зубы.",
               d=2, x="Чистить зубы — tish yuvmoq: я чищу зубы."),
            RQ("Mos so‘zni tanlang: Я … в школу в 8 часов.", "иду", ["сплю", "ужинаю", "читаю"],
               say="Я ... в школу в восемь часов.", x="Я иду в школу — men maktabga boraman."),
            RQ("Mos so‘zni tanlang: Вечером я ложусь …", "спать", ["завтракать", "в школу", "утром"],
               say="Вечером я ложусь ...", d=2, x="Ложиться спать — uxlashga yotmoq."),
            RQ("Mos so‘zni tanlang: После уроков я делаю …", "уроки", ["утро", "ночь", "сон"],
               say="После уроков я делаю ...", d=2, x="Делать уроки — uy vazifasini bajarmoq."),
            Q("Qaysi ish ertalab qilinadi?", "завтракать", ["ужинать", "ложиться спать"], d=2,
              x="Ertalab nonushta qilamiz — завтракать."),
            LISTEN("Men soat 7 da turaman.", ["Men soat 8 da turaman.", "Men soat 7 da uxlayman.",
                                             "Men soat 7 da maktabga boraman."], say="Я встаю в семь часов."),
            LISTEN("Kechqurun men kitob o‘qiyman.", ["Ertalab men kitob o‘qiyman.", "Kechqurun men televizor ko‘raman.",
                                                    "Kechqurun men uy vazifasini qilaman."],
                   say="Вечером я читаю книгу."),
            LISTEN("Darslardan keyin men tushlik qilaman.", ["Darslardan oldin men nonushta qilaman.",
                                                            "Darslardan keyin men sayr qilaman.",
                                                            "Darsda men yozaman."], say="После уроков я обедаю.",
                   d=2),
            MATCH("So‘z va tarjimasini juftlang",
                  [("утром", "ertalab"), ("днём", "kunduzi"), ("вечером", "kechqurun"), ("ночью", "kechasi"),
                   ("после уроков", "darslardan keyin"), ("каждый день", "har kuni")]),
            SENT("Утром я делаю зарядку", "Ertalab men badantarbiya qilaman."),
            SENT("Я встаю в семь часов", "Men soat yettida turaman.", d=2),
            SENT("После обеда я гуляю в парке", "Tushlikdan keyin men parkda sayr qilaman.", d=3),
            Q("To‘g‘ri tartibni tanlang", "встаю — завтракаю — иду в школу",
              ["иду в школу — встаю — завтракаю", "завтракаю — встаю — иду в школу",
               "ложусь спать — встаю — завтракаю"], d=2,
              x="Avval turamiz, keyin nonushta qilamiz, so‘ng maktabga boramiz."),
            RTF("“Ужинать” — nonushta qilish degani.", False, say="ужинать",
                x="Ужинать — kechki ovqat yemoq; nonushta — завтракать."),
            RTF("“Каждый день” — “har kuni” degani.", True, say="каждый день", x="Каждый день — har kuni."),
            RQ("“Зарядка” nima?", "ertalabki badantarbiya", ["kechki ovqat", "uy vazifasi", "tushlik"],
               say="зарядка", d=2, x="Зарядка — ertalabki badantarbiya mashqlari."),
            RQ("Gapni to‘ldiring: Днём я … в школе.", "учусь", ["сплю", "ужинаю", "ложусь"],
               say="Днём я ... в школе.", d=3, x="Учиться — o‘qimoq (maktabda): я учусь в школе."),
            Q("Qaysi so‘z kun qismini bildirmaydi?", "завтра", ["утро", "день", "вечер"], d=2,
              x="Завтра — ertaga; утро, день, вечер — kun qismlari."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"), ["conjugation", "past", "my_day"], chapter=C2)

# ============================================================ 3-chorak
T.topic("numbers", "💯", L("Sonlar 100 gacha", "Numbers to 100", "Числа до 100"), chapter=C3,
        theory="O‘nliklar: 20 — двадцать, 30 — тридцать, 40 — сорок, 50 — пятьдесят, 60 — шестьдесят,\n"
               "70 — семьдесят, 80 — восемьдесят, 90 — девяносто, 100 — сто.\n"
               "Murakkab son ikki so‘zdan tuziladi: 25 — двадцать пять, 47 — сорок семь, 99 — девяносто девять.\n"
               "• Diqqat: 40 — сорок, 90 — девяносто (boshqacha tuzilgan).\n"
               "Savol: Сколько тебе лет? — Мне одиннадцать лет.",
        items=[
            RQ("“Сорок” qaysi son?", "40", ["14", "4", "30"], say="сорок", x="Сорок — 40."),
            RQ("“Девяносто” qaysi son?", "90", ["19", "9", "70"], say="девяносто", x="Девяносто — 90."),
            RQ("“Пятьдесят” qaysi son?", "50", ["15", "5", "60"], say="пятьдесят", x="Пятьдесят — 50."),
            RQ("“Сто” qaysi son?", "100", ["10", "1000", "70"], say="сто", x="Сто — 100."),
            Q("30 ruschada qanday?", "тридцать", ["тринадцать", "три", "триста"], x="30 — тридцать; 13 — тринадцать."),
            Q("12 ruschada qanday?", "двенадцать", ["двадцать", "два", "двести"], x="12 — двенадцать; 20 — двадцать."),
            Q("70 ruschada qanday?", "семьдесят", ["семнадцать", "семь", "восемьдесят"],
              x="70 — семьдесят; 17 — семнадцать."),
            HEAR("Tinglang va sonni tanlang", "63", ["36", "73", "53"], say="шестьдесят три", d=2),
            HEAR("Tinglang va sonni tanlang", "18", ["80", "81", "8"], say="восемнадцать", d=2),
            HEAR("Tinglang va sonni tanlang", "44", ["14", "40", "54"], say="сорок четыре", d=2),
            HEAR("Tinglang va sonni tanlang", "99", ["19", "90", "89"], say="девяносто девять", d=2),
            Q("25 ruschada qanday?", "двадцать пять", ["двенадцать пять", "пятьдесят два", "двадцать четыре"], d=2,
              x="25 = 20 + 5: двадцать пять."),
            RQ("Hisoblang: двадцать + десять = ?", "тридцать", ["двадцать один", "сорок", "тринадцать"],
               say="двадцать плюс десять", d=2, x="20 + 10 = 30 — тридцать."),
            RQ("Hisoblang: сорок + сорок = ?", "восемьдесят", ["восемнадцать", "сорок восемь", "девяносто"],
               say="сорок плюс сорок", d=2, x="40 + 40 = 80 — восемьдесят."),
            Q("Qaysi son eng katta?", "девяносто", ["девятнадцать", "девять", "восемьдесят"], d=2,
              x="Девяносто — 90, qolganlari: 19, 9, 80."),
            Q("Qaysi son eng kichik?", "одиннадцать", ["двадцать", "тридцать один", "сорок"], d=2,
              x="Одиннадцать — 11, qolganlari: 20, 31, 40."),
            MATCH("O‘nliklar: son va so‘zni juftlang",
                  [("20", "двадцать"), ("30", "тридцать"), ("40", "сорок"), ("50", "пятьдесят"), ("60", "шестьдесят"),
                   ("80", "восемьдесят"), ("90", "девяносто")]),
            MATCH("11–19: son va so‘zni juftlang",
                  [("11", "одиннадцать"), ("13", "тринадцать"), ("15", "пятнадцать"), ("16", "шестнадцать"),
                   ("17", "семнадцать"), ("19", "девятнадцать")]),
            RQ("Qatorni davom ettiring: десять, двадцать, тридцать, …", "сорок",
               ["четырнадцать", "пятьдесят", "тридцать один"], say="десять, двадцать, тридцать, ...",
               x="10, 20, 30, 40 — сорок."),
            LISTEN("Mening bobom 70 yoshda.", ["Mening bobom 17 yoshda.", "Mening buvim 70 yoshda.",
                                              "Mening bobom 60 yoshda."], say="Моему дедушке семьдесят лет.", d=3),
            RQ("“Сколько тебе лет?” savoliga to‘g‘ri javob", "Мне одиннадцать лет.",
               ["Меня зовут Одиннадцать.", "Я одиннадцать.", "Мне одиннадцать год."], say="Сколько тебе лет?", d=2,
               x="Yosh shunday aytiladi: Мне одиннадцать лет."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "пятьдесят", ["пядесят", "пятдесят", "пятьдесять"], d=3,
              x="To‘g‘ri yozilishi: пятьдесят (ь o‘rtada)."),
            RTF("“Восемьдесят” — 18.", False, say="восемьдесят", x="Восемьдесят — 80; 18 — восемнадцать."),
            RQ("Hisoblang: сто − один = ?", "девяносто девять", ["девяносто один", "десять", "восемьдесят девять"],
               say="сто минус один", d=3, x="100 − 1 = 99 — девяносто девять."),
            SENT("В нашем классе двадцать пять учеников", "Bizning sinfimizda 25 ta o‘quvchi bor.", d=3),
        ])

T.topic("time", "🕒", L("Soat necha?", "What time is it?", "Который час?"), chapter=C3,
        theory="Vaqtni so‘rash: Который час? (Soat necha?)\n"
               "• 1 — час: Сейчас час.\n"
               "• 2, 3, 4 — часа: два часа, три часа, четыре часа.\n"
               "• 5–12 — часов: пять часов, семь часов, двенадцать часов.\n"
               "Qachon? — в: Урок начинается в восемь часов. 8:30 — восемь тридцать (половина девятого).",
        items=[
            RQ("Mos so‘zni tanlang: Сейчас два …", "часа", ["час", "часов"], say="Сейчас два ...",
               x="2, 3, 4 dan keyin — часа."),
            RQ("Mos so‘zni tanlang: Сейчас пять …", "часов", ["час", "часа"], say="Сейчас пять ...",
               x="5 dan keyin — часов."),
            RQ("Mos so‘zni tanlang: Сейчас три …", "часа", ["час", "часов"], say="Сейчас три ...",
               x="3 dan keyin — часа."),
            RQ("Mos so‘zni tanlang: Сейчас десять …", "часов", ["час", "часа"], say="Сейчас десять ...",
               x="10 dan keyin — часов."),
            RQ("Mos so‘zni tanlang: Сейчас четыре …", "часа", ["час", "часов"], say="Сейчас четыре ...", d=2,
               x="4 dan keyin — часа."),
            RQ("Soat 7:00. Который час?", "Семь часов.", ["Семь часа.", "Семнадцать часов.", "Шесть часов."],
               say="Который час?", e="🕖", x="7:00 — семь часов."),
            RQ("Soat 3:00. Который час?", "Три часа.", ["Три часов.", "Тринадцать часов.", "Два часа."],
               say="Который час?", e="🕒", x="3:00 — три часа."),
            RQ("Soat 12:00. Который час?", "Двенадцать часов.", ["Двенадцать часа.", "Два часа.", "Двадцать часов."],
               say="Который час?", e="🕛", d=2, x="12:00 — двенадцать часов."),
            RQ("Soat 1:00. Который час?", "Час.", ["Один часов.", "Одиннадцать часов.", "Два часа."],
               say="Который час?", e="🕐", d=3, x="1:00 — (Сейчас) час."),
            RQ("“Который час?” o‘zbekchasi qanday?", "Soat necha?", ["Nechta soat bor?", "Bu qanday soat?",
                                                                   "Soat qayerda?"], say="Который час?",
               x="Который час? — Soat necha?"),
            HEAR("Tinglang va vaqtni tanlang", "8:00", ["9:00", "18:00", "7:00"], say="Восемь часов."),
            HEAR("Tinglang va vaqtni tanlang", "6:30", ["6:00", "7:30", "16:30"], say="Шесть тридцать.", d=2),
            HEAR("Tinglang va vaqtni tanlang", "9:15", ["9:50", "19:15", "5:15"], say="Девять пятнадцать.", d=2),
            RQ("“Половина девятого” — soat necha?", "8:30", ["9:30", "9:00", "8:00"], say="половина девятого", d=3,
               x="Половина девятого — to‘qqizinchi soatning yarmi, ya’ni 8:30."),
            RQ("Mos so‘zni tanlang: Уроки начинаются … восемь часов.", "в", ["на", "из"],
               say="Уроки начинаются ... восемь часов.", d=2, x="Qachon? — в восемь часов."),
            RQ("“Во сколько ты встаёшь?” savoliga to‘g‘ri javob", "В семь часов.",
               ["Семь часов.", "Семь лет.", "В семь лет."], say="Во сколько ты встаёшь?", d=3,
               x="Во сколько? — В семь часов (в bilan)."),
            LISTEN("Men soat 9 da uxlashga yotaman.", ["Men soat 9 da turaman.", "Men soat 10 da uxlashga yotaman.",
                                                      "Hozir soat 9."], say="Я ложусь спать в девять часов.", d=2),
            MATCH("Vaqt va yozuvni juftlang",
                  [("1:00", "час"), ("2:00", "два часа"), ("4:00", "четыре часа"), ("5:00", "пять часов"),
                   ("11:00", "одиннадцать часов"), ("12:00", "двенадцать часов")]),
            SENT("Урок начинается в восемь часов", "Dars soat sakkizda boshlanadi.", d=2),
            SENT("Сейчас ровно три часа", "Hozir roppa-rosa soat uch.", d=3),
            RTF("“Пять часа” — to‘g‘ri.", False, say="пять часа", x="5 dan keyin — часов: пять часов."),
            RTF("“Два часа” — to‘g‘ri.", True, say="два часа", x="2 dan keyin — часа: два часа."),
            RQ("“Ровно” o‘zbekchasi qanday?", "roppa-rosa", ["yarim", "chorak", "kech"], say="ровно", d=2,
               x="Ровно три часа — roppa-rosa soat uch."),
            RQ("Mos sonni tanlang: В часе … минут.", "шестьдесят", ["сто", "тридцать", "двадцать четыре"],
               say="В часе ... минут.", d=2, x="Bir soatda 60 minut: шестьдесят минут."),
        ])

T.topic("cases", "📍", L("Qayerda? Qayerga? Kimni? Nimani?", "Where? Where to? Whom? What?",
                         "Где? Куда? Кого? Что?"), chapter=C3,
        theory="Otning oxiri savolga qarab o‘zgaradi:\n"
               "• Кого? Что? (tushum): Я вижу маму. Я читаю книгу. (-а → -у, -я → -ю)\n"
               "• Куда? (qayerga?) — в/на + tushum: в школу, в парк, на работу.\n"
               "• Где? (qayerda?) — в/на + -е: в школе, в парке, на работе.\n"
               "Misol: Я иду в школу. Я учусь в школе.",
        items=[
            RQ("Mos shaklni tanlang: Я иду в …", "школу", ["школа", "школе", "школы"], say="Я иду в ...",
               x="Куда? — в школу."),
            RQ("Mos shaklni tanlang: Я учусь в …", "школе", ["школа", "школу", "школы"], say="Я учусь в ...",
               x="Где? — в школе."),
            RQ("Mos shaklni tanlang: Мы идём в …", "парк", ["парке", "парка", "парку"], say="Мы идём в ...",
               x="Куда? — в парк."),
            RQ("Mos shaklni tanlang: Мы гуляем в …", "парке", ["парк", "парка", "парку"], say="Мы гуляем в ...",
               x="Где? — в парке."),
            RQ("Mos shaklni tanlang: Я читаю …", "книгу", ["книга", "книге", "книгой"], say="Я читаю ...",
               x="Что? (tushum) — книгу."),
            RQ("Mos shaklni tanlang: Я люблю …", "маму", ["мама", "маме", "мамой"], say="Я люблю ...",
               x="Кого? — маму."),
            RQ("Mos shaklni tanlang: Я вижу …", "брата", ["брат", "брату", "братом"], say="Я вижу ...", d=3,
               x="Кого? — брата (jonli, он rodi: -а qo‘shiladi)."),
            RQ("Mos shaklni tanlang: Папа едет на …", "работу", ["работа", "работе", "работой"],
               say="Папа едет на ...", d=2, x="Куда? — на работу."),
            RQ("Mos shaklni tanlang: Папа сейчас на …", "работе", ["работа", "работу", "работой"],
               say="Папа сейчас на ...", d=2, x="Где? — на работе."),
            RQ("Mos so‘roq so‘zni tanlang: … ты идёшь? — В магазин.", "Куда", ["Где", "Кто", "Что"],
               say="... ты идёшь? В магазин.", x="В магазин — qayerga? Куда?"),
            RQ("Mos so‘roq so‘zni tanlang: … ты живёшь? — В Ташкенте.", "Где", ["Куда", "Кого", "Что"],
               say="... ты живёшь? В Ташкенте.", x="В Ташкенте — qayerda? Где?"),
            RQ("Mos so‘roq so‘zni tanlang: … ты видишь? — Сестру.", "Кого", ["Что", "Где", "Куда"],
               say="... ты видишь? Сестру.", d=2, x="Сестру — odam: Кого?"),
            RQ("Mos so‘roq so‘zni tanlang: … ты пишешь? — Письмо.", "Что", ["Кого", "Где", "Куда"],
               say="... ты пишешь? Письмо.", d=2, x="Письмо — narsa: Что?"),
            RQ("“Куда?” o‘zbekchasi qanday?", "qayerga?", ["qayerda?", "kimni?", "nimani?"], say="Куда?",
               x="Куда? — qayerga?"),
            RQ("“Где?” o‘zbekchasi qanday?", "qayerda?", ["qayerga?", "qachon?", "kimni?"], say="Где?",
               x="Где? — qayerda?"),
            LISTEN("Biz muzeyga boryapmiz.", ["Biz muzeydamiz.", "Biz maktabga boryapmiz.", "Ular muzeyga boryapti."],
                   say="Мы идём в музей.", d=2),
            LISTEN("Qiz kutubxonada.", ["Qiz kutubxonaga boryapti.", "Qiz maktabda.", "Bola kutubxonada."],
                   say="Девочка в библиотеке.", d=2),
            MATCH("Savol va javobni juftlang",
                  [("Кто?", "мама"), ("Кого?", "маму"), ("Где?", "в школе"), ("Куда?", "в школу"),
                   ("Что?", "книгу")], d=3),
            SENT("Летом мы едем на море", "Yozda biz dengizga boramiz.", d=2),
            SENT("Я иду в библиотеку", "Men kutubxonaga boryapman."),
            SENT("Бабушка живёт в деревне", "Buvim qishloqda yashaydi.", d=2),
            RTF("“В школу” — “Куда?” savoliga javob.", True, say="в школу", x="В школу — qayerga? Куда?"),
            RTF("“В парке” — “Куда?” savoliga javob.", False, say="в парке", d=2,
                x="В парке — Где? (qayerda?); Куда? — в парк."),
            Q("Qaysi gap to‘g‘ri?", "Я иду в кино.", ["Я иду в кине.", "Я иду в кину.", "Я иду в кином."], d=3,
              x="Кино so‘zi o‘zgarmaydi: в кино."),
            Q("Qaysi gap to‘g‘ri?", "Мама работает в больнице.", ["Мама работает в больница.",
                                                                 "Мама работает в больницу.",
                                                                 "Мама работает в больницей."], d=2,
              x="Где? — в больнице (-е)."),
        ])

T.topic("transport", "🚌", L("Shahar transporti", "City transport", "Городской транспорт"), chapter=C3,
        gen="vocab",
        theory="Transport: автобус, трамвай, метро, такси, машина, поезд, самолёт, велосипед.\n"
               "Nimada boramiz? — ехать на …: Я еду на автобусе. Мы едем на метро (метро o‘zgarmaydi).\n"
               "Piyoda — пешком: Я иду в школу пешком.\n"
               "Shaharda: улица (ko‘cha), площадь (maydon), светофор (svetofor), остановка (bekat).",
        levels=vocab_levels("transport"))

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"), ["numbers", "time", "cases", "transport"],
       chapter=C3)

# ============================================================ 4-chorak
T.topic("professions", "👷", L("Kasblar", "Professions", "Профессии"), chapter=C4, gen="vocab",
        theory="Kasblar: врач (shifokor), учитель (o‘qituvchi), повар (oshpaz), водитель (haydovchi),\n"
               "строитель (quruvchi), пожарный (o‘t o‘chiruvchi), пилот (uchuvchi), художник (rassom).\n"
               "Savol: Кем работает твой папа? — Он работает врачом.\n"
               "Ish joyi: врач — в больнице, учитель — в школе, продавец — в магазине.",
        levels=vocab_levels("jobs_places"))

T.topic("seasons", "⛅", L("Fasllar va ob-havo", "Seasons and weather", "Времена года и погода"), chapter=C4,
        theory="Fasllar (времена года): зима (qish), весна (bahor), лето (yoz), осень (kuz).\n"
               "Qachon? — зимой, весной, летом, осенью.\n"
               "Ob-havo (погода): тепло (iliq), холодно (sovuq), жарко (issiq).\n"
               "Идёт дождь. Идёт снег. Светит солнце. Дует ветер.\n"
               "Misol: Летом жарко. Зимой идёт снег.",
        items=[
            Q("“Qish” ruschasi qanday?", "зима", ["весна", "лето", "осень"], x="Qish — зима."),
            Q("“Bahor” ruschasi qanday?", "весна", ["зима", "лето", "осень"], x="Bahor — весна."),
            RQ("“Лето” o‘zbekchasi qanday?", "yoz", ["qish", "bahor", "kuz"], say="лето", x="Лето — yoz."),
            RQ("“Осень” o‘zbekchasi qanday?", "kuz", ["yoz", "bahor", "qish"], say="осень", x="Осень — kuz."),
            Q("“Qishda” ruschasi qanday?", "зимой", ["летом", "весной", "зима"], d=2,
              x="Qishda — зимой (qachon?)."),
            RQ("Mos so‘zni tanlang: … идёт снег.", "Зимой", ["Летом", "Жарко", "Весна"], say="... идёт снег.",
               x="Qor qishda yog‘adi: Зимой идёт снег."),
            RQ("Mos so‘zni tanlang: Летом очень …", "жарко", ["холодно", "снег", "зима"], say="Летом очень ...",
               x="Yozda issiq bo‘ladi: Летом жарко."),
            LISTEN("Yomg‘ir yog‘yapti.", ["Qor yog‘yapti.", "Quyosh charaqlayapti.", "Shamol esyapti."],
                   say="Идёт дождь."),
            LISTEN("Bugun havo iliq.", ["Bugun havo sovuq.", "Kecha havo iliq edi.", "Bugun havo issiq."],
                   say="Сегодня тепло.", d=2),
            LISTEN("Kuzda barglar sarg‘ayadi.", ["Bahorda barglar ko‘karadi.", "Kuzda yomg‘ir yog‘adi.",
                                                "Yozda barglar sarg‘ayadi."], say="Осенью листья желтеют.", d=3),
            RQ("“Погода” o‘zbekchasi qanday?", "ob-havo", ["fasl", "shamol", "osmon"], say="погода",
               x="Погода — ob-havo."),
            Q("Qaysi fasl yozdan keyin keladi?", "осень", ["весна", "зима", "лето"], x="Yozdan keyin kuz — осень."),
            Q("Qaysi fasl qishdan keyin keladi?", "весна", ["осень", "лето", "зима"], d=2,
              x="Qishdan keyin bahor — весна."),
            RQ("Mos so‘zni tanlang: Дует сильный …", "ветер", ["снег", "солнце", "дождь"], say="Дует сильный ...",
               d=2, x="Дует ветер — shamol esyapti."),
            RQ("Mos so‘zni tanlang: На небе светит …", "солнце", ["дождь", "снег", "ветер"],
               say="На небе светит ...", d=2, x="Светит солнце — quyosh charaqlayapti."),
            Q("Qaysi oylar qish oylari?", "декабрь, январь, февраль", ["июнь, июль, август", "март, апрель, май",
                                                                      "сентябрь, октябрь, ноябрь"], d=2,
              x="Qish oylari: декабрь, январь, февраль."),
            Q("Sentabr qaysi faslga kiradi?", "осень", ["лето", "зима", "весна"], d=2,
              x="Сентябрь — kuzning birinchi oyi."),
            MATCH("So‘z va tarjimasini juftlang",
                  [("зима", "qish"), ("весна", "bahor"), ("лето", "yoz"), ("осень", "kuz"), ("дождь", "yomg‘ir"),
                   ("снег", "qor"), ("ветер", "shamol")]),
            SENT("Зимой дети играют в снежки", "Qishda bolalar qorbo‘ron o‘ynaydi.", d=3),
            SENT("Сегодня идёт дождь", "Bugun yomg‘ir yog‘yapti."),
            SENT("Весной цветут деревья", "Bahorda daraxtlar gullaydi.", d=2),
            RTF("“Жарко” — “sovuq” degani.", False, say="жарко", x="Жарко — issiq; холодно — sovuq."),
            RTF("Yil to‘rt fasldan iborat: зима, весна, лето, осень.", True, say="зима, весна, лето, осень",
                x="To‘rt fasl: qish, bahor, yoz, kuz."),
            RQ("“Какая сегодня погода?” savoliga mos javob", "Сегодня солнечно и тепло.",
               ["Сегодня пятница.", "Сегодня я в школе.", "Сегодня мой день рождения."],
               say="Какая сегодня погода?", d=2, x="Ob-havo so‘ralgan: Сегодня солнечно и тепло."),
            RQ("Mos so‘zni tanlang: Осенью часто идёт …", "дождь", ["жарко", "лето", "солнце"],
               say="Осенью часто идёт ...", d=3, x="Kuzda tez-tez yomg‘ir yog‘adi: идёт дождь."),
        ])

T.topic("food", "🛒", L("Ovqat va do‘kon", "Food and shopping", "Еда и магазин"), chapter=C4,
        theory="Ovqatlar: хлеб (non), молоко (sut), сыр (pishloq), мясо (go‘sht), рис (guruch), суп (sho‘rva), чай (choy), сок (sharbat).\n"
               "Do‘konda:\n"
               "• — Сколько стоит хлеб? — Пять тысяч сумов.\n"
               "• — Дайте, пожалуйста, молоко. — Вот, пожалуйста.\n"
               "Yoqtirish: Я люблю чай. Я не люблю лук. Мне нравится плов.",
        items=[
            Q("“Non” ruschasi qanday?", "хлеб", ["сыр", "мясо", "сок"], e="🍞", x="Non — хлеб."),
            Q("“Sut” ruschasi qanday?", "молоко", ["масло", "мясо", "мёд"], e="🥛", x="Sut — молоко."),
            Q("“Go‘sht” ruschasi qanday?", "мясо", ["рыба", "хлеб", "каша"], x="Go‘sht — мясо."),
            RQ("“Сыр” o‘zbekchasi qanday?", "pishloq", ["sariyog‘", "sut", "tuxum"], say="сыр", x="Сыр — pishloq."),
            RQ("“Сок” o‘zbekchasi qanday?", "sharbat", ["choy", "suv", "sut"], say="сок", x="Сок — sharbat."),
            Q("“Do‘kon” ruschasi qanday?", "магазин", ["рынок", "аптека", "школа"], x="Do‘kon — магазин."),
            RQ("“Сколько стоит?” o‘zbekchasi qanday?", "Qancha turadi?", ["Nechta bor?", "Qayerda sotiladi?",
                                                                         "Soat necha?"], say="Сколько стоит?",
               x="Сколько стоит? — Qancha turadi? (narxi qancha?)"),
            RQ("Mos so‘zni tanlang: Дайте, …, хлеб.", "пожалуйста", ["спасибо", "здравствуйте", "до свидания"],
               say="Дайте, ..., хлеб.", x="Iltimos qilganda — пожалуйста."),
            RQ("Mos shaklni tanlang: Папа купил … (tarvuz).", "арбуз", ["арбуза", "арбузу", "арбузом"],
               say="Папа купил ...", d=3, x="Что купил? — арбуз (он rodi, narsa — o‘zgarmaydi)."),
            RQ("Mos shaklni tanlang: Бабушка готовит … (palov).", "плов", ["плова", "плову", "пловом"],
               say="Бабушка готовит ...", d=2, x="Что готовит? — плов."),
            Q("“Menga palov yoqadi” ruschasi qanday?", "Мне нравится плов.", ["Я нравится плов.", "Мне нравится плова.",
                                                                            "Меня нравится плов."], d=3,
              x="Yoqadi — мне нравится: Мне нравится плов."),
            LISTEN("Menga non va sut bering, iltimos.", ["Menga non va choy bering, iltimos.", "Non va sut qancha turadi?",
                                                        "Menga pishloq bering, iltimos."],
                   say="Дайте, пожалуйста, хлеб и молоко.", d=2),
            LISTEN("Olmalar qancha turadi?", ["Olmalar qayerda?", "Noklar qancha turadi?", "Menga olma bering."],
                   say="Сколько стоят яблоки?", d=2),
            LISTEN("Men choyni yaxshi ko‘raman.", ["Men choyni yoqtirmayman.", "Men sharbatni yaxshi ko‘raman.",
                                                  "Men choy ichyapman."], say="Я люблю чай."),
            RQ("“Я не люблю лук” o‘zbekchasi qanday?", "Men piyozni yoqtirmayman.",
               ["Men piyozni yaxshi ko‘raman.", "Men sabzini yoqtirmayman.", "Menda piyoz yo‘q."],
               say="Я не люблю лук.", d=2, x="Не люблю — yoqtirmayman; лук — piyoz."),
            MATCH("So‘z va tarjimasini juftlang",
                  [("хлеб", "non"), ("молоко", "sut"), ("мясо", "go‘sht"), ("рис", "guruch"), ("чай", "choy"),
                   ("масло", "sariyog‘"), ("яйцо", "tuxum")]),
            Q("Qaysi so‘z ichimlikni bildiradi?", "сок", ["хлеб", "сыр", "мясо"], x="Сок — sharbat, uni ichamiz."),
            Q("Qaysi so‘z ortiqcha?", "стул", ["хлеб", "сыр", "рис"], x="Стул — stul, u ovqat emas."),
            RQ("“Рынок” o‘zbekchasi qanday?", "bozor", ["do‘kon", "oshxona", "restoran"], say="рынок", d=2,
               x="Рынок — bozor; магазин — do‘kon."),
            SENT("Я хочу купить хлеб", "Men non sotib olmoqchiman.", d=2),
            SENT("Мама покупает молоко в магазине", "Onam do‘kondan sut sotib olyapti.", d=3),
            SENT("Я люблю сладкий чай", "Men shirin choyni yaxshi ko‘raman."),
            RTF("“Мясо” — go‘sht.", True, say="мясо", x="Мясо — go‘sht."),
            RTF("“Хлеб” — sut.", False, say="хлеб", x="Хлеб — non; sut — молоко."),
            Q("Narxni bilish uchun sotuvchiga nima deysiz?", "Сколько это стоит?",
              ["Который час?", "Как тебя зовут?", "Где ты живёшь?"], d=2,
              x="Narx so‘raladi: Сколько это стоит?"),
            RQ("Mos so‘zni tanlang: На завтрак я пью …", "чай", ["хлеб", "мясо", "суп"],
               say="На завтрак я пью ...", d=2, x="Пить — ichmoq: пью чай."),
        ])

# ------------------------------------------------------------ o‘qish matnlari (o‘zimizniki)
TEXT_FAMILY = ("Меня зовут Анвар. Мне одиннадцать лет. Я живу в Ташкенте. У меня есть сестра. Её зовут Лола. "
               "Лола учится в третьем классе. Мой папа — врач, а мама — учительница.")
TEXT_DAY = ("Зарина встаёт в семь часов. Она умывается и завтракает. В восемь часов она идёт в школу. "
            "Уроки кончаются в час. После обеда Зарина делает уроки, а вечером гуляет с собакой.")
TEXT_AUTUMN = ("Наступила осень. Дни стали короче, а ночи — длиннее. На деревьях жёлтые и красные листья. "
               "Часто идёт дождь. Дети ходят в школу с зонтами. Птицы улетают на юг.")
TEXT_SHOP = ("Бобур и мама пошли в магазин. Мама купила хлеб, молоко и сыр. Бобур хотел сок. "
             "Сок стоил восемь тысяч сумов. Мама купила сок, и Бобур сказал: «Спасибо, мама!»")
TEXT_FRIEND = ("У меня есть друг. Его зовут Тимур. Он живёт рядом со мной. Тимур любит футбол и хорошо рисует. "
               "В субботу мы вместе ходим в парк. Там мы играем в мяч и едим мороженое.")

T.topic("reading", "📖", L("Matn o‘qiymiz", "Reading texts", "Читаем тексты"), chapter=C4,
        theory="Matnni o‘qishdan oldin savolni o‘qing — nimani qidirish kerakligini bilasiz.\n"
               "• Кто? — kim haqida; Где? — qayerda; Когда? — qachon; Что делает? — nima qiladi.\n"
               "• Notanish so‘z bo‘lsa, gapning boshqa so‘zlariga qarab ma’nosini toping.\n"
               "Javobni matndan toping: Где живёт Анвар? — В Ташкенте.",
        items=[
            *READ(TEXT_FAMILY, "👪", [
                Q("Anvar necha yoshda?", "11", ["9", "12", "3"], x="Мне одиннадцать лет — 11 yosh."),
                Q("Anvar qayerda yashaydi?", "в Ташкенте", ["в Самарканде", "в Бухаре", "в Андижане"],
                  x="Я живу в Ташкенте."),
                Q("Lola nechanchi sinfda o‘qiydi?", "3-sinfda", ["5-sinfda", "1-sinfda", "11-sinfda"],
                  x="Лола учится в третьем классе."),
                Q("Anvarning otasi kim bo‘lib ishlaydi?", "врач", ["учитель", "повар", "водитель"], d=2,
                  x="Мой папа — врач."),
                TF("Anvarning onasi o‘qituvchi.", True, x="Мама — учительница, ya’ni o‘qituvchi."),
                Q("Lola Anvarga kim bo‘ladi?", "сестра", ["мама", "бабушка", "подруга"], d=2,
                  x="У меня есть сестра. Её зовут Лола."),
            ]),
            *READ(TEXT_DAY, "⏰", [
                Q("Zarina soat nechada turadi?", "7 da", ["8 da", "6 da", "9 da"], x="Зарина встаёт в семь часов."),
                Q("Zarina soat nechada maktabga boradi?", "8 da", ["7 da", "9 da", "1 da"],
                  x="В восемь часов она идёт в школу."),
                Q("Darslar soat nechada tugaydi?", "1 da", ["8 da", "2 da", "12 da"], d=2,
                  x="Уроки кончаются в час — soat 1 da."),
                Q("Kechqurun Zarina nima qiladi?", "it bilan sayr qiladi",
                  ["uy vazifasini qiladi", "nonushta qiladi", "maktabga boradi"], d=2,
                  x="Вечером гуляет с собакой — it bilan sayr qiladi."),
                TF("Zarina tushlikdan keyin uy vazifasini qiladi.", True, d=2,
                   x="После обеда Зарина делает уроки."),
                TF("Zarina ertalab televizor ko‘radi.", False, x="Matnda: ertalab u yuvinadi va nonushta qiladi."),
            ]),
            *READ(TEXT_AUTUMN, "🍂", [
                Q("Matn qaysi fasl haqida?", "kuz haqida", ["qish haqida", "bahor haqida", "yoz haqida"],
                  x="Наступила осень — kuz keldi."),
                Q("Daraxtlarda qanday barglar bor?", "жёлтые и красные", ["зелёные", "белые и синие", "чёрные"], d=2,
                  x="На деревьях жёлтые и красные листья."),
                Q("Bolalar maktabga nima bilan boradi?", "с зонтами", ["с собакой", "с мячом", "с цветами"], d=2,
                  x="Дети ходят в школу с зонтами — soyabon bilan."),
                Q("Qushlar qayerga uchib ketadi?", "на юг", ["на север", "в лес", "в город"], d=3,
                  x="Птицы улетают на юг — janubga."),
                TF("Matnga ko‘ra, kuzda kunlar uzunroq bo‘ladi.", False, d=2,
                   x="Дни стали короче — kunlar qisqardi."),
                TF("Kuzda tez-tez yomg‘ir yog‘adi.", True, x="Часто идёт дождь."),
            ]),
            *READ(TEXT_SHOP, "🛒", [
                Q("Bobur kim bilan do‘konga bordi?", "с мамой", ["с папой", "с сестрой", "с другом"],
                  x="Бобур и мама пошли в магазин."),
                Q("Onasi nimalarni sotib oldi?", "хлеб, молоко и сыр",
                  ["хлеб, мясо и рис", "молоко, чай и сахар", "сыр, яблоки и мёд"], d=2,
                  x="Мама купила хлеб, молоко и сыр."),
                Q("Bobur nimani xohladi?", "сок", ["мороженое", "торт", "чай"], x="Бобур хотел сок."),
                Q("Sharbat necha so‘m turardi?", "8 000 so‘m", ["800 so‘m", "18 000 so‘m", "80 000 so‘m"], d=2,
                  x="Восемь тысяч сумов — 8 000 so‘m."),
                TF("Bobur onasiga rahmat aytdi.", True, x="Бобур сказал: «Спасибо, мама!»"),
            ]),
            *READ(TEXT_FRIEND, "⚽", [
                Q("Do‘stining ismi nima?", "Тимур", ["Анвар", "Бобур", "Али"], x="Его зовут Тимур."),
                Q("Timur nimani yaxshi ko‘radi?", "футбол", ["шахматы", "музыку", "плавание"],
                  x="Тимур любит футбол."),
                Q("Ular qachon parkka boradi?", "в субботу", ["в понедельник", "в воскресенье", "каждый день"], d=2,
                  x="В субботу мы вместе ходим в парк."),
                Q("Parkda ular nima qiladi?", "играют в мяч", ["читают книги", "рисуют", "делают уроки"], d=2,
                  x="Там мы играем в мяч и едим мороженое."),
                TF("Timur uzoqda yashaydi.", False, x="Он живёт рядом со мной — u yaqinda yashaydi."),
            ]),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["professions", "seasons", "food", "reading"],
       chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["nouns", "adjectives", "pronouns", "sentences", "conjugation", "past", "my_day", "numbers", "time", "cases",
        "transport", "professions", "seasons", "food", "reading"], chapter=C4, level=3)

T.write()
