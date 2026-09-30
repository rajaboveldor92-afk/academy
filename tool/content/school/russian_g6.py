"""Rus tili (o‘zbek maktablari uchun), 6-sinf: assets/data/school/russian_g6.json + bank_russian_g6.json.

Mavzular O‘zbekiston maktab dasturi ("Rus tili", 6-sinf, ≈A2) yo‘nalishida — 5-sinfdan keyingi bosqich:
kelishiklar (винительный, родительный, дательный, творительный), egalik olmoshlari va свой, harakat fe’llari
(идти / ходить, ехать / ездить), kelasi zamon (буду читать / прочитаю), sifat darajalari, tartib sonlar,
ob-havo, salomatlik, sayohat, savolli o‘qish matnlari. Hamma matn va savollar o‘zimizniki.
Lug‘at mavzulari (so‘z yozish, harakatlar, qarama-qarshi sifatlar) — umumiy `foreign_language.dart` generatorlari,
grammatika, iboralar va o‘qish — savollar banki.
Qayta yaratish: python3 tool/content/school/russian_g6.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("russian", 6, L("Rus tili", "Russian", "Русский язык"))

C1 = "1-chorak. Tushum va qaratqich kelishiklari"
C2 = "2-chorak. Jo‘nalish va vosita kelishiklari, harakat fe’llari"
C3 = "3-chorak. Kelasi zamon, taqqoslash va tartib sonlar"
C4 = "4-chorak. Ob-havo, salomatlik va sayohat"


# ------------------------------------------------------------ yordamchilar
def RQ(q, a, w, say, d=1, x=None, e=None, h=None):
    """Savolda ruscha matn bor: ovozda `say` rus tilida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=say, lang="ru")


def LISTEN(a, w, say, d=1, x=None):
    """Tinglab tushunish: ruscha gap eshitiladi, o‘zbekcha tarjimasi tanlanadi."""
    return Q("Tinglang va tarjimasini tanlang", a, w, d=d, x=x or f"{say} — {a}", say=say, lang="ru")


def HEAR(q, a, w, say, d=1, x=None):
    """Tinglab son yoki haroratni tanlash."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", say=say, lang="ru")


def SENT(ru, tr, d=1, full=None):
    """Ruscha gap tuzish (tinish belgisiz). `full` — izohda ko‘rsatiladigan tinish belgili gap."""
    end = "?" if tr.endswith("?") else "."
    return ORDER("So‘zlardan gap tuzing", ru, d=d, x=f"{full or ru + end} — {tr}", lang="ru")


def RTF(q, a, say, d=1, x=None):
    return TF(q, a, d=d, x=x, say=say, lang="ru")


def READ(text, emoji, questions):
    """O‘qish matni: bir matnga bir nechta savol (Q yoki TF) — `text` maydoni to‘ldiriladi."""
    return [{**it, "text": text, "e": emoji} for it in questions]


# ============================================================ 1-chorak
T.topic("accusative", "🎯", L("Tushum kelishigi: Кого? Что?", "Accusative case", "Винительный падеж"),
        chapter=C1,
        theory="Винительный падеж — Кого? Что? (kimni? nimani?). Fe’llar: вижу, люблю, жду, читаю, покупаю.\n"
               "• она: -а → -у, -я → -ю: мама → вижу маму, книга → читаю книгу, Таня → жду Таню.\n"
               "• он (narsa) va оно o‘zgarmaydi: читаю журнал, вижу окно.\n"
               "• он (jonli: odam, hayvon) — -а / -я: вижу брата, жду друга, кормлю кота, спрашиваю учителя.\n"
               "• -ь bilan tugagan она rodidagi so‘z o‘zgarmaydi: открываю дверь, люблю осень.",
        items=[
            RQ("Mos shaklni tanlang: Я вижу …", "сестру", ["сестра", "сестре", "сестрой"], say="Я вижу ...",
               x="Кого? — сестру (-а → -у)."),
            RQ("Mos shaklni tanlang: Мы ждём …", "бабушку", ["бабушка", "бабушке", "бабушкой"], say="Мы ждём ...",
               x="Кого? — бабушку."),
            RQ("Mos shaklni tanlang: Я пью …", "воду", ["вода", "воде", "водой"], say="Я пью ...", x="Что? — воду."),
            RQ("Mos shaklni tanlang: Папа читает …", "журнал", ["журнала", "журналу", "журналом"],
               say="Папа читает ...", x="Журнал — он, jonsiz: o‘zgarmaydi."),
            RQ("Mos shaklni tanlang: Я слушаю …", "музыку", ["музыка", "музыке", "музыкой"], say="Я слушаю ...",
               x="Что? — музыку."),
            RQ("Mos shaklni tanlang: Бабушка варит …", "кашу", ["каша", "каше", "кашей"], say="Бабушка варит ...",
               x="Что? — кашу."),
            Q("Qaysi so‘z tushum kelishigida?", "машину", ["машина", "машине", "машиной"], x="Что? — машину (-а → -у)."),
            Q("Qaysi gap to‘g‘ri?", "Я рисую собаку.", ["Я рисую собака.", "Я рисую собаке.", "Я рисую собакой."],
              x="Кого? — собаку."),
            LISTEN("Men daryoni ko‘ryapman.", ["Men dengizni ko‘ryapman.", "Men daryoda suzyapman.",
                                              "U daryoni ko‘ryapti."], say="Я вижу реку."),
            RTF("“Я вижу кошка” — to‘g‘ri gap.", False, say="Я вижу кошка.", x="Кого? — кошку: Я вижу кошку."),
            RTF("“Я читаю журнал” — to‘g‘ri gap.", True, say="Я читаю журнал.", x="Журнал — jonsiz, o‘zgarmaydi."),
            SENT("Брат ждёт автобус", "Akam avtobusni kutyapti."),
            RQ("Mos shaklni tanlang: Дети любят …", "мороженое", ["мороженого", "мороженому", "мороженым"],
               say="Дети любят ...", d=2, x="Мороженое — оно, tushumda o‘zgarmaydi."),
            RQ("Mos shaklni tanlang: Я жду …", "друга", ["друг", "другу", "другом"], say="Я жду ...", d=2,
               x="Друг — jonli, он: -а qo‘shiladi: жду друга."),
            RQ("Mos shaklni tanlang: Мальчик кормит …", "кота", ["кот", "коту", "котом"], say="Мальчик кормит ...", d=2,
               x="Кот — jonli: кормит кота."),
            RQ("Mos shaklni tanlang: Я встретил …", "Таню", ["Таня", "Тане", "Таней"], say="Я встретил ...", d=2,
               x="-я → -ю: Таню."),
            RQ("Mos so‘roq so‘zni tanlang: … ты ждёшь? — Папу.", "Кого", ["Что", "Кому", "Где"],
               say="... ты ждёшь? Папу.", d=2, x="Odam — Кого?"),
            RQ("Mos so‘roq so‘zni tanlang: … ты покупаешь? — Сок.", "Что", ["Кого", "Чем", "Куда"],
               say="... ты покупаешь? Сок.", d=2, x="Narsa — Что?"),
            Q("Qaysi gap to‘g‘ri?", "Мама любит сына.", ["Мама любит сын.", "Мама любит сыну.", "Мама любит сыном."], d=2,
              x="Сын — jonli: любит сына."),
            MATCH("Bosh va tushum kelishigini juftlang",
                  [("мама", "маму"), ("папа", "папу"), ("друг", "друга"), ("кот", "кота"), ("книга", "книгу"),
                   ("земля", "землю"), ("окно", "окно")], d=2),
            LISTEN("Onam yangi ko‘ylak sotib oldi.", ["Onam yangi sumka sotib oldi.", "Opam yangi ko‘ylak sotib oldi.",
                                                     "Onam yangi ko‘ylak tikdi."], say="Мама купила новое платье.", d=2),
            SENT("Я очень люблю свою бабушку", "Men buvimni juda yaxshi ko‘raman.", d=2),
            SENT("Мы смотрим новый фильм", "Biz yangi film ko‘ryapmiz.", d=2),
            RQ("Mos shaklni tanlang: Мы спрашиваем …", "учителя", ["учитель", "учителю", "учителем"],
               say="Мы спрашиваем ...", d=3, x="Учитель — jonli, -ь → -я: учителя."),
            RQ("Mos shaklni tanlang: Я открываю …", "дверь", ["двери", "дверью", "дверя"], say="Я открываю ...", d=3,
               x="Дверь — она, -ь bilan tugaydi: tushumda o‘zgarmaydi."),
            LISTEN("Biz ukamizni kutyapmiz.", ["Biz akamizni kutyapmiz.", "Biz ukamiz bilan kutyapmiz.",
                                              "Ukamiz bizni kutyapti."], say="Мы ждём младшего брата.", d=3),
        ])

T.topic("genitive", "🚫", L("Qaratqich kelishigi: У меня нет…", "Genitive case", "Родительный падеж"),
        chapter=C1,
        theory="Родительный падеж — Кого? Чего? (kimning? nimaning? nima yo‘q?).\n"
               "• У кого? — у меня, у тебя, у брата, у мамы: У брата есть велосипед.\n"
               "• нет + qaratqich: У меня нет собаки. Сегодня нет дождя.\n"
               "• Qo‘shimchalar: он / оно — -а / -я (стола, окна, дождя);  она — -ы / -и (мамы, книги, земли).\n"
               "• Egalik, miqdor, joy: книга брата (akamning kitobi), стакан воды, из Ташкента (Toshkentdan).",
        items=[
            RQ("Mos shaklni tanlang: У меня нет …", "ручки", ["ручка", "ручку", "ручкой"], say="У меня нет ...",
               x="нет + qaratqich: нет ручки."),
            RQ("Mos shaklni tanlang: У нас нет …", "машины", ["машина", "машину", "машиной"], say="У нас нет ...",
               x="нет + qaratqich: нет машины."),
            RQ("Mos shaklni tanlang: В комнате нет …", "стола", ["стол", "столу", "столом"], say="В комнате нет ...",
               x="Стол — он: нет стола."),
            RQ("Mos olmoshni tanlang: У … есть брат? (sening)", "тебя", ["ты", "тебе", "твой"], say="У ... есть брат?",
               x="у + тебя: У тебя есть брат?"),
            RQ("Mos olmoshni tanlang: У … нет времени. (mening)", "меня", ["я", "мне", "мой"],
               say="У ... нет времени.", x="у меня — menda."),
            RQ("“У меня нет брата” o‘zbekchasi qanday?", "Mening akam (ukam) yo‘q.",
               ["Mening akam bor.", "Akam uyda emas.", "Menda akamning kitobi yo‘q."], say="У меня нет брата.",
               x="У меня нет… — Menda … yo‘q."),
            Q("Qaysi so‘z qaratqich kelishigida?", "стола", ["стол", "столу", "столом"], x="Чего? — стола."),
            Q("Qaysi gap to‘g‘ri?", "У Али нет сестры.", ["У Али нет сестра.", "У Али нет сестру.", "У Али нет сестрой."],
              x="нет + qaratqich: нет сестры."),
            LISTEN("Bugun yomg‘ir yo‘q.", ["Bugun yomg‘ir yog‘yapti.", "Bugun qor yo‘q.", "Kecha yomg‘ir yo‘q edi."],
                   say="Сегодня нет дождя."),
            RTF("“У меня нет кошка” — to‘g‘ri gap.", False, say="У меня нет кошка.",
                x="нет + qaratqich: У меня нет кошки."),
            RTF("“Стакан чая” — “bir stakan choy” degani.", True, say="стакан чая", x="To‘g‘ri: стакан чего? — чая."),
            SENT("Я из Ферганы", "Men Farg‘onadanman."),
            RQ("Mos shaklni tanlang: Сегодня нет …", "ветра", ["ветер", "ветру", "ветром"], say="Сегодня нет ...", d=2,
               x="Ветер — ветра (е tushib qoladi)."),
            RQ("Mos shaklni tanlang: Дай мне стакан …", "воды", ["вода", "воду", "водой"], say="Дай мне стакан ...", d=2,
               x="Стакан чего? — воды."),
            RQ("Mos shaklni tanlang: Это рюкзак …", "брата", ["брат", "брату", "братом"], say="Это рюкзак ...", d=2,
               x="Чей рюкзак? — брата (akamning)."),
            RQ("Mos shaklni tanlang: Я приехал из …", "Бухары", ["Бухара", "Бухару", "Бухаре"], say="Я приехал из ...",
               d=2, x="из + qaratqich: из Бухары."),
            RQ("Mos shaklni tanlang: У … есть кошка.", "сестры", ["сестра", "сестру", "сестрой"], say="У ... есть кошка.",
               d=2, x="у + qaratqich: у сестры."),
            Q("Qaysi gap to‘g‘ri?", "Это дом дедушки.", ["Это дом дедушка.", "Это дом дедушку.", "Это дом дедушке."], d=2,
              x="Чей дом? — дедушки (-а → -и)."),
            RQ("“Чей это рюкзак?” savoliga to‘g‘ri javob", "Это рюкзак Лолы.",
               ["Это рюкзак Лола.", "Это рюкзак Лоле.", "Это рюкзак Лолу."], say="Чей это рюкзак?", d=2,
               x="Lolaning — Лолы (qaratqich)."),
            MATCH("Bosh va qaratqich kelishigini juftlang",
                  [("брат", "брата"), ("папа", "папы"), ("книга", "книги"), ("окно", "окна"), ("дождь", "дождя"),
                   ("земля", "земли")], d=2),
            LISTEN("Menda vaqt yo‘q.", ["Menda vaqt bor.", "Unda vaqt yo‘q.", "Soat necha?"], say="У меня нет времени.",
                   d=2),
            SENT("В нашем городе нет метро", "Bizning shahrimizda metro yo‘q.", d=2),
            RQ("Mos olmoshni tanlang: У … новая машина. (ularning)", "них", ["они", "им", "их"],
               say="У ... новая машина.", d=3, x="Predlogdan keyin н qo‘shiladi: у них."),
            LISTEN("Bu mening do‘stimning velosipedi.", ["Bu mening velosipedim.", "Bu do‘stimning mashinasi.",
                                                        "Do‘stimda velosiped yo‘q."],
                   say="Это велосипед моего друга.", d=3),
            SENT("У моего брата есть компьютер", "Akamning kompyuteri bor.", d=3),
        ])

T.topic("possessive", "🔑", L("Egalik olmoshlari va свой", "Possessive pronouns", "Притяжательные местоимения"),
        chapter=C1, prereq=["genitive"],
        theory="Egalik olmoshlari otga moslashadi: мой / моя / моё / мои, твой…, наш / наша / наше / наши, ваш…\n"
               "его (uning — erkak), её (uning — ayol), их (ularning) — hech qachon o‘zgarmaydi: его сестра, их дети.\n"
               "свой — o‘zining: Он читает свою книгу (o‘z kitobini). Он читает его книгу — boshqa odamning kitobini!\n"
               "Kelishikda egalik olmoshlari ham o‘zgaradi: у моего брата, в нашем классе, с моей сестрой.\n"
               "Чей? Чья? Чьё? Чьи? — Kimning?",
        items=[
            RQ("Mos olmoshni tanlang: Это … (mening) велосипед.", "мой", ["моя", "моё", "мои"], say="Это ... велосипед.",
               x="Велосипед — он: мой."),
            RQ("Mos olmoshni tanlang: Где … (sening) шапка?", "твоя", ["твой", "твоё", "твои"], say="Где ... шапка?",
               x="Шапка — она: твоя."),
            RQ("Mos olmoshni tanlang: … (bizning) дети любят спорт.", "Наши", ["Наш", "Наша", "Наше"],
               say="... дети любят спорт.", x="Дети — ko‘plik: наши."),
            Q("“Ularning bolalari” ruschasi qanday?", "их дети", ["его дети", "её дети", "наши дети"],
              x="Ularning — их (o‘zgarmaydi)."),
            Q("“Uning (qizning) otasi” ruschasi qanday?", "её папа", ["его папа", "их папа", "мой папа"],
              x="Qizning — её."),
            Q("Qaysi birikma to‘g‘ri?", "твои носки", ["твой носки", "твоя носки", "твоё носки"],
              x="Носки — ko‘plik: твои."),
            MATCH("Olmoshni tarjimasi bilan juftlang",
                  [("мой", "mening"), ("твой", "sening"), ("его", "uning (erkak)"), ("её", "uning (ayol)"),
                   ("наш", "bizning"), ("ваш", "sizning"), ("их", "ularning")]),
            LISTEN("Bu kimning telefoni? — Meniki.", ["Bu qanday telefon? — Yangi.", "Telefon qayerda? — Stolda.",
                                                     "Bu kimning kitobi? — Meniki."], say="Чей это телефон? — Мой."),
            RTF("“Их” so‘zi o‘zgarmaydi: их дом, их школа, их окно.", True, say="их дом, их школа, их окно",
                x="To‘g‘ri: их, его, её o‘zgarmaydi."),
            RTF("“Моя пальто” — to‘g‘ri birikma.", False, say="моя пальто", x="Пальто — оно: моё пальто."),
            RQ("Mos olmoshni tanlang: Это … (sizning) пальто?", "ваше", ["ваш", "ваша", "ваши"], say="Это ... пальто?", d=2,
               x="Пальто — оно: ваше."),
            RQ("Mos olmoshni tanlang: Это … (mening) очки.", "мои", ["мой", "моя", "моё"], say="Это ... очки.", d=2,
               x="Очки — faqat ko‘plikda ishlatiladi: мои очки."),
            RQ("Mos olmoshni tanlang: У Сардора есть собака. … собака большая.", "Его", ["Её", "Их", "Мой"],
               say="У Сардора есть собака. ... собака большая.", d=2, x="Sardor — erkak: его собака."),
            RQ("Mos olmoshni tanlang: У Нилуфар есть брат. … брат — студент.", "Её", ["Его", "Их", "Моя"],
               say="У Нилуфар есть брат. ... брат — студент.", d=2, x="Nilufar — ayol: её брат."),
            RQ("Mos so‘roq so‘zni tanlang: … это кроссовки?", "Чьи", ["Чей", "Чья", "Чьё"], say="... это кроссовки?", d=2,
               x="Кроссовки — ko‘plik: чьи?"),
            RQ("Mos so‘roq so‘zni tanlang: … это полотенце?", "Чьё", ["Чей", "Чья", "Чьи"], say="... это полотенце?", d=2,
               x="Полотенце — оно: чьё?"),
            LISTEN("Ularning uyi daryo bo‘yida.", ["Uning uyi daryo bo‘yida.", "Bizning uyimiz daryo bo‘yida.",
                                                  "Ularning uyi tog‘da."], say="Их дом у реки.", d=2),
            SENT("Где ваши билеты", "Chiptalaringiz qayerda?", d=2),
            SENT("Его брат учится в пятом классе", "Uning ukasi 5-sinfda o‘qiydi.", d=2),
            RQ("Mos olmoshni tanlang: У них есть дача. … дача за городом.", "Их", ["Его", "Её", "Ихняя"],
               say="У них есть дача. ... дача за городом.", d=3,
               x="Faqat их; «ихний, ихняя» — adabiy tilda noto‘g‘ri."),
            RQ("Mos shaklni tanlang: Мы учимся в … классе.", "нашем", ["наш", "нашего", "нашим"],
               say="Мы учимся в ... классе.", d=3, x="Где? — в нашем классе."),
            RQ("Mos shaklni tanlang: У … брата есть машина.", "моего", ["мой", "моему", "моим"],
               say="У ... брата есть машина.", d=3, x="у + qaratqich: у моего брата."),
            RQ("Mos shaklni tanlang: Я гуляю с … сестрой.", "моей", ["моя", "мою", "мой"], say="Я гуляю с ... сестрой.",
               d=3, x="с + vosita kelishigi: с моей сестрой."),
            RQ("Mos olmoshni tanlang: Анвар моет … машину. (o‘zining)", "свою", ["его", "свой", "своя"],
               say="Анвар моет ... машину.", d=3, x="O‘zining — свою (машину — она, tushum)."),
            RQ("Mos olmoshni tanlang: Я забыл … тетрадь дома. (o‘zimning)", "свою", ["свой", "своя", "своё"],
               say="Я забыл ... тетрадь дома.", d=3, x="Тетрадь — она, tushum: свою тетрадь."),
            SENT("Моя сестра любит свою кошку", "Opam o‘z mushugini yaxshi ko‘radi.", d=3),
        ])

T.topic("spelling", "✍️", L("So‘zlarni to‘g‘ri yozish", "Spelling", "Правописание слов"),
        chapter=C1, gen="spell",
        theory="Rus tilida ko‘p so‘z eshitilganidek yozilmaydi — urg‘usiz unliga e’tibor bering:\n"
               "• молоко [malako], собака [sabaka], корова [karova] — yozuvda о.\n"
               "• ё doim urg‘uli: ёж, самолёт, зелёный, пчёлы.\n"
               "• ь yumshatadi: конь, соль, морковь;  жи, ши — и bilan yoziladi: жираф, машина.\n"
               "Rasmga qarang, so‘zni ayting va harflarni tering. Ortiqcha harflar ham bor!",
        levels=[{"minLetters": 4, "maxLetters": 5, "extra": 1},
                {"minLetters": 5, "maxLetters": 6, "extra": 1},
                {"minLetters": 6, "maxLetters": 8, "extra": 2}])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["accusative", "genitive", "possessive", "spelling"], chapter=C1)

# ============================================================ 2-chorak
T.topic("dative", "🎁", L("Jo‘nalish kelishigi: Кому? Чему?", "Dative case", "Дательный падеж"),
        chapter=C2,
        theory="Дательный падеж — Кому? Чему? (kimga? nimaga?). Fe’llar: помогать, звонить, дарить, давать, писать.\n"
               "• он / оно: -у / -ю: брат → помогаю брату, учитель → учителю.\n"
               "• она: -е: мама → дарю маме, сестра → пишу сестре;  -ь → -и: мать → матери.\n"
               "• к + dativ — yoniga, kimnikiga: иду к врачу, еду к бабушке.  по + dativ — bo‘ylab: гуляю по парку.\n"
               "• Olmoshlar: мне, тебе, ему, ей, нам, вам, им. Мне нравится… — Menga yoqadi…",
        items=[
            RQ("Mos shaklni tanlang: Я помогаю …", "дедушке", ["дедушка", "дедушку", "дедушкой"], say="Я помогаю ...",
               x="Кому? — дедушке."),
            RQ("Mos shaklni tanlang: Лола звонит …", "подруге", ["подруга", "подругу", "подругой"], say="Лола звонит ...",
               x="Кому? — подруге."),
            RQ("Mos shaklni tanlang: Мы дарим цветы …", "учительнице", ["учительница", "учительницу", "учительницей"],
               say="Мы дарим цветы ...", x="Кому? — учительнице."),
            RQ("Mos shaklni tanlang: Папа купил подарок …", "сыну", ["сын", "сына", "сыном"],
               say="Папа купил подарок ...", x="Кому? — сыну."),
            RQ("Mos shaklni tanlang: Я пишу письмо …", "другу", ["друг", "друга", "другом"], say="Я пишу письмо ...",
               x="Кому? — другу."),
            RQ("Mos shaklni tanlang: Я дал корм …", "собаке", ["собака", "собаку", "собакой"], say="Я дал корм ...",
               x="Кому? — собаке."),
            RQ("Mos olmoshni tanlang: … нравится эта песня. (menga)", "Мне", ["Меня", "Я", "Мной"],
               say="... нравится эта песня.", x="Menga yoqadi — мне нравится."),
            RQ("Mos olmoshni tanlang: Сколько … лет? (senga)", "тебе", ["ты", "тебя", "твой"], say="Сколько ... лет?",
               x="Yosh so‘raganda: Сколько тебе лет?"),
            Q("Qaysi so‘z jo‘nalish kelishigida?", "другу", ["друг", "друга", "другом"], x="Кому? — другу."),
            Q("“Menga yoqadi” ruschasi qanday?", "мне нравится", ["я нравится", "меня нравится", "мной нравится"],
              x="Мне нравится — menga yoqadi."),
            LISTEN("Bu sovg‘a — senga.", ["Bu sovg‘a — menga.", "Bu sovg‘a — unga.", "Sovg‘a uchun rahmat."],
                   say="Этот подарок — тебе."),
            RTF("“Я помогаю мама” — to‘g‘ri gap.", False, say="Я помогаю мама.", x="Кому? — маме: Я помогаю маме."),
            RTF("“Мне нравится футбол” — “Menga futbol yoqadi” degani.", True, say="Мне нравится футбол.",
                x="To‘g‘ri."),
            RQ("Mos shaklni tanlang: Завтра мы идём к …", "врачу", ["врач", "врача", "врачом"],
               say="Завтра мы идём к ...", d=2, x="к + dativ: к врачу."),
            RQ("Mos shaklni tanlang: Летом я поеду к …", "бабушке", ["бабушка", "бабушку", "бабушкой"],
               say="Летом я поеду к ...", d=2, x="к + dativ: к бабушке."),
            RQ("Mos so‘roq so‘zni tanlang: … ты помогаешь? — Маме.", "Кому", ["Кого", "Кем", "Где"],
               say="... ты помогаешь? Маме.", d=2, x="Маме — kimga? Кому?"),
            Q("Qaysi gap to‘g‘ri?", "Мальчик помогает сестре.", ["Мальчик помогает сестра.", "Мальчик помогает сестру.",
                                                               "Мальчик помогает сестрой."], d=2,
              x="помогать кому? — сестре."),
            MATCH("Olmosh va jo‘nalish shaklini juftlang",
                  [("я", "мне"), ("ты", "тебе"), ("он", "ему"), ("она", "ей"), ("мы", "нам"), ("вы", "вам"), ("они", "им")],
                  d=2),
            LISTEN("Men har kuni buvimga qo‘ng‘iroq qilaman.", ["Men har kuni buvimga yordam beraman.",
                                                               "Buvim har kuni menga qo‘ng‘iroq qiladi.",
                                                               "Men har kuni buvimnikiga boraman."],
                   say="Я звоню бабушке каждый день.", d=2),
            LISTEN("Ukamga 7 yosh.", ["Akamga 17 yosh.", "Ukamga 8 yosh.", "Men 7 yoshdaman."],
                   say="Моему брату семь лет.", d=2),
            SENT("Я подарил маме цветы", "Men onamga gul sovg‘a qildim.", d=2),
            RQ("Mos olmoshni tanlang: Я позвоню … вечером. (unga — qiz)", "ей", ["её", "она", "ею"],
               say="Я позвоню ... вечером.", d=3, x="Кому? — ей."),
            RQ("Mos olmoshni tanlang: Скажи …, пожалуйста. (unga — erkak)", "ему", ["его", "он", "им"],
               say="Скажи ..., пожалуйста.", d=3, x="Кому? — ему."),
            RQ("Mos shaklni tanlang: Дети гуляют по …", "парку", ["парк", "парка", "парке"], say="Дети гуляют по ...",
               d=3, x="по + dativ: по парку (park bo‘ylab)."),
            SENT("Мы идём в гости к дедушке", "Biz bobomnikiga mehmonga ketyapmiz.", d=3),
            SENT("Учитель объясняет ученикам урок", "O‘qituvchi o‘quvchilarga darsni tushuntiryapti.", d=3),
        ])

T.topic("instrumental", "✏️", L("Vosita kelishigi: С кем? Чем?", "Instrumental case", "Творительный падеж"),
        chapter=C2,
        theory="Творительный падеж — Кем? Чем? С кем? С чем? (kim bilan? nima bilan?).\n"
               "• он / оно: -ом / -ем: друг → с другом, карандаш → карандашом, отец → с отцом.\n"
               "• она: -ой / -ей: мама → с мамой, ручка → ручкой, Таня → с Таней.\n"
               "• Чем ты пишешь? — Ручкой. С кем ты гуляешь? — С братом.\n"
               "• Kasb va mashg‘ulot: Я хочу стать врачом. Брат занимается спортом.",
        items=[
            RQ("Mos shaklni tanlang: Я гуляю с …", "собакой", ["собака", "собаку", "собаке"], say="Я гуляю с ...",
               x="С кем? — с собакой."),
            RQ("Mos shaklni tanlang: Я играю в шахматы с …", "папой", ["папа", "папу", "папе"],
               say="Я играю в шахматы с ...", x="С кем? — с папой."),
            RQ("Mos shaklni tanlang: Мы едим суп …", "ложкой", ["ложка", "ложку", "ложке"], say="Мы едим суп ...",
               x="Чем? — ложкой (qoshiq bilan)."),
            Q("“Do‘stim bilan” ruschasi qanday?", "с другом", ["с друг", "с друга", "с другу"], x="С кем? — с другом."),
            Q("“Onam bilan” ruschasi qanday?", "с мамой", ["с мама", "с маму", "с маме"], x="С кем? — с мамой."),
            Q("Qaysi so‘z vosita kelishigida?", "машиной", ["машина", "машину", "машины"], x="Чем? — машиной."),
            LISTEN("Men akam bilan futbol o‘ynayman.", ["Men akamga futbol o‘ynashni o‘rgataman.",
                                                       "Akam do‘stlari bilan futbol o‘ynaydi.",
                                                       "Men akam bilan shaxmat o‘ynayman."],
                   say="Я играю в футбол с братом."),
            RTF("“С сестрой” — “opam (singlim) bilan” degani.", True, say="с сестрой", x="To‘g‘ri."),
            RTF("“Я режу хлеб нож” — to‘g‘ri gap.", False, say="Я режу хлеб нож.",
                x="Чем? — ножом: Я режу хлеб ножом."),
            SENT("Я пью чай с лимоном", "Men limonli choy ichaman."),
            RQ("Mos shaklni tanlang: Лола рисует кошку …", "карандашом", ["карандаш", "карандаша", "карандашу"],
               say="Лола рисует кошку ...", d=2, x="Чем? — карандашом."),
            RQ("Mos shaklni tanlang: Бабушка пьёт чай с …", "мёдом", ["мёд", "мёда", "мёду"],
               say="Бабушка пьёт чай с ...", d=2, x="С чем? — с мёдом."),
            RQ("Mos shaklni tanlang: Я хочу стать …", "врачом", ["врач", "врача", "врачу"], say="Я хочу стать ...", d=2,
               x="стать кем? — врачом."),
            RQ("Mos olmoshni tanlang: Я пойду с … (sen bilan).", "тобой", ["ты", "тебя", "тебе"],
               say="Я пойду с ...", d=2, x="с + тобой."),
            RQ("Mos so‘roq so‘zni tanlang: С … ты был в кино? — С другом.", "кем", ["чем", "кого", "кому"],
               say="С ... ты был в кино? С другом.", d=2, x="Odam — с кем?"),
            RQ("Mos so‘roq so‘zni tanlang: … ты режешь хлеб? — Ножом.", "Чем", ["Кем", "Что", "Кого"],
               say="... ты режешь хлеб? Ножом.", d=2, x="Narsa (asbob) — Чем?"),
            Q("Qaysi gap to‘g‘ri?", "Я люблю кашу с молоком.", ["Я люблю кашу с молоко.", "Я люблю кашу с молока.",
                                                              "Я люблю кашу с молоку."], d=2, x="С чем? — с молоком."),
            MATCH("Bosh va vosita kelishigini juftlang",
                  [("друг", "другом"), ("мама", "мамой"), ("ручка", "ручкой"), ("брат", "братом"), ("молоко", "молоком"),
                   ("отец", "отцом")], d=2),
            LISTEN("Men uchuvchi bo‘lmoqchiman.", ["Men uchuvchiman.", "Otam uchuvchi bo‘lgan.", "Men shifokor bo‘lmoqchiman."],
                   say="Я хочу стать лётчиком.", d=2),
            SENT("Вечером я гуляю с друзьями", "Kechqurun men do‘stlarim bilan sayr qilaman.", d=2),
            RQ("Mos shaklni tanlang: Мой брат занимается …", "плаванием", ["плавание", "плавания", "плаванию"],
               say="Мой брат занимается ...", d=3, x="заниматься чем? — плаванием."),
            RQ("Mos shaklni tanlang: Я познакомился с …", "учителем", ["учитель", "учителя", "учителю"],
               say="Я познакомился с ...", d=3, x="-ь → -ем: с учителем."),
            RQ("Mos olmoshni tanlang: Пойдём с …! (biz bilan)", "нами", ["мы", "нас", "нам"], say="Пойдём с ...!", d=3,
               x="с + нами."),
            LISTEN("Opam musiqaga qiziqadi.", ["Opam musiqa tinglayapti.", "Opam sport bilan shug‘ullanadi.",
                                              "Ukam musiqaga qiziqadi."], say="Сестра интересуется музыкой.", d=3),
            SENT("Мой папа работает инженером", "Otam muhandis bo‘lib ishlaydi.", d=3),
        ])

T.topic("motion", "🚶", L("Harakat fe’llari: идти / ходить, ехать / ездить", "Verbs of motion",
                         "Глаголы движения"),
        chapter=C2,
        theory="Piyoda: идти — hozir, bir tomonga: Я иду в школу (hozir maktabga ketyapman).\n"
               "ходить — odatda, ko‘p marta yoki borib-kelish: Я хожу в школу каждый день. Вчера я ходил в музей.\n"
               "Transportda: ехать — hozir, bir tomonga: Мы едем на автобусе.  ездить — odatda yoki borib-kelish: Летом мы ездили на море.\n"
               "Tuslanish: я иду, ты идёшь, они идут;  я хожу, ты ходишь;  я еду, ты едешь;  я езжу, ты ездишь.\n"
               "O‘tgan zamon: идти → шёл, шла, шли;  ехать → ехал, ехала.",
        items=[
            RQ("Mos fe’lni tanlang: Смотри! Мальчик … в школу.", "идёт", ["ходит", "едет", "ездит"],
               say="Смотри! Мальчик ... в школу.", x="Hozir, bir tomonga, piyoda — идёт."),
            RQ("Mos fe’lni tanlang: Я … в бассейн каждую субботу.", "хожу", ["иду", "идёт", "ходит"],
               say="Я ... в бассейн каждую субботу.", x="Har shanba (odatda) — хожу."),
            RQ("Mos fe’lni tanlang: Сейчас мы … на автобусе.", "едем", ["ездим", "идём", "ходим"],
               say="Сейчас мы ... на автобусе.", x="Hozir, transportda — едем."),
            RQ("Mos fe’lni tanlang: Каждое лето мы … в Самарканд.", "ездим", ["едем", "идём", "едут"],
               say="Каждое лето мы ... в Самарканд.", x="Har yozi (odatda), transportda — ездим."),
            Q("“Piyoda” ruschasi qanday?", "пешком", ["на машине", "быстро", "далеко"], x="Piyoda — пешком."),
            Q("Qaysi fe’l transportda harakatni bildiradi?", "ехать", ["идти", "ходить", "бежать"],
              x="Ехать — transportda bormoq."),
            LISTEN("Men hozir uyga ketyapman.", ["Men har kuni uyga piyoda boraman.", "Men kecha uyda edim.",
                                                "Men uyga avtobusda boraman."], say="Сейчас я иду домой."),
            RTF("“Идти” — piyoda, “ехать” — transportda harakat.", True, say="идти, ехать", x="To‘g‘ri."),
            SENT("Куда вы едете", "Qayerga ketyapsiz?"),
            RQ("Mos fe’lni tanlang: Папа каждый день … на работу на машине.", "ездит", ["ходит", "идёт", "едем"],
               say="Папа каждый день ... на работу на машине.", d=2, x="Har kuni, mashinada — ездит."),
            RQ("Mos fe’lni tanlang: Куда ты …? — В магазин. (hozir, piyoda)", "идёшь", ["ходишь", "едешь", "идёт"],
               say="Куда ты ...? В магазин.", d=2, x="Hozir, piyoda, ты — идёшь."),
            RQ("Mos fe’lni tanlang: Вчера мы … в театр.", "ходили", ["идём", "ходим", "ходить"],
               say="Вчера мы ... в театр.", d=2, x="Borib-kelgan (o‘tgan zamon): ходили."),
            RQ("“Идти” fe’li: они …", "идут", ["идёт", "идём", "идёте"], say="они ...", d=2, x="Они идут."),
            RQ("“Ходить” fe’li: ты …", "ходишь", ["ходешь", "ходит", "ходю"], say="ты ...", d=2, x="Ты ходишь."),
            Q("Qaysi gap “odatda, har kuni” ma’nosida?", "Я хожу в школу пешком.",
              ["Я иду в школу.", "Смотри, я иду!", "Сейчас я иду домой."], d=2, x="Odatiy harakat — ходить."),
            MATCH("Olmosh va fe’l shaklini juftlang (transportda bormoq)",
                  [("я", "еду"), ("ты", "едешь"), ("он", "едет"), ("мы", "едем"), ("вы", "едете"), ("они", "едут")], d=2),
            LISTEN("Biz har yozda dengizga boramiz.", ["Biz hozir dengizga ketyapmiz.", "Biz yozda dengizda edik.",
                                                      "Ular har yozda dengizga boradi."],
                   say="Каждое лето мы ездим на море.", d=2),
            RTF("“Я каждый день иду в школу” — to‘g‘ri gap.", False, say="Я каждый день иду в школу.", d=2,
                x="Har kuni takrorlanadi — ходить: Я каждый день хожу в школу."),
            SENT("Мы едем в Ташкент на поезде", "Biz Toshkentga poyezdda ketyapmiz.", d=2),
            RQ("Mos so‘zni tanlang: Ты едешь на автобусе или идёшь …?", "пешком", ["на такси", "на поезде", "в поезде"],
               say="Ты едешь на автобусе или идёшь ...?", d=2, x="Идёшь — piyoda: пешком."),
            RQ("“Ездить” fe’li: я …", "езжу", ["ездю", "езжаю", "ежу"], say="я ...", d=3,
               x="Ездить: я езжу (д → ж), ты ездишь."),
            RQ("O‘tgan zamon: Лола … домой. (идти)", "шла", ["шёл", "шли", "идла"], say="Лола ... домой.", d=3,
               x="Идти → шёл, шла, шли: Лола шла."),
            LISTEN("Kecha Nodir kinoga borib keldi.", ["Nodir hozir kinoga ketyapti.", "Kecha Nodir kinoga bormadi.",
                                                      "Ertaga Nodir kinoga boradi."], say="Вчера Нодир ходил в кино.", d=3),
            Q("Qaysi gap to‘g‘ri?", "Бабушка идёт медленно.", ["Бабушка едет пешком.", "Бабушка ездит пешком.",
                                                             "Бабушка идёт на автобусе."], d=3,
              x="Piyoda — идти; «едет пешком» — ma’nosiz birikma."),
            SENT("Я хожу в бассейн два раза в неделю", "Men haftada ikki marta basseynga boraman.", d=3),
        ])

T.topic("actions", "🏃", L("Harakatlar", "Actions", "Действия"),
        chapter=C2, gen="vocab", prereq=["motion"],
        theory="Harakat fe’llari (он / она, hozir): бежит (yuguryapti), идёт (yuryapti), плывёт (suzyapti),\n"
               "едет на велосипеде, танцует, спит, сидит, пишет, думает, смеётся, плачет, лезет (tirmashyapti).\n"
               "Что он делает? — Он бежит. Что она делает? — Она плывёт.\n"
               "Eslang: бежать — бежит (hozir, bir tomonga), бегать — бегает (umuman, turli tomonga).",
        levels=[{"themes": ["actions"], "modes": ["listen", "read"], "options": 3},
                {"themes": ["actions"], "modes": ["read", "picture_word"], "options": 4},
                {"themes": ["actions"], "modes": ["picture_word", "listen"], "options": 4}])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["dative", "instrumental", "motion", "actions"], chapter=C2)

# ============================================================ 3-chorak
T.topic("future", "🔮", L("Kelasi zamon: буду читать / прочитаю", "Future tense", "Будущее время"),
        chapter=C3,
        theory="Kelasi zamon ikki xil:\n"
               "• Murakkab: быть + fe’l (jarayon): я буду читать, ты будешь, он будет, мы будем, вы будете, они будут.\n"
               "• Oddiy (tugallangan fe’l, natija): прочитать → я прочитаю, написать → он напишет, сделать → мы сделаем.\n"
               "Завтра я буду читать весь день. — Ertaga kun bo‘yi o‘qiyman (jarayon).\n"
               "Завтра я прочитаю эту книгу. — Ertaga bu kitobni o‘qib tugataman (natija).",
        items=[
            RQ("Mos so‘zni tanlang: Завтра я … играть в футбол.", "буду", ["будешь", "будет", "будут"],
               say="Завтра я ... играть в футбол.", x="Я — буду."),
            RQ("Mos so‘zni tanlang: Летом мы … отдыхать в горах.", "будем", ["будете", "будут", "буду"],
               say="Летом мы ... отдыхать в горах.", x="Мы — будем."),
            RQ("Mos so‘zni tanlang: Что ты … делать вечером?", "будешь", ["буду", "будет", "будем"],
               say="Что ты ... делать вечером?", x="Ты — будешь."),
            Q("Qaysi so‘z kelasi zamonni bildiradi?", "завтра", ["вчера", "сейчас", "давно"], x="Завтра — ertaga."),
            Q("Qaysi gap kelasi zamonda?", "Я буду рисовать.", ["Я рисую.", "Я рисовал.", "Я рисовала."],
              x="буду + fe’l — kelasi zamon."),
            LISTEN("Ertaga men velosiped haydayman.", ["Kecha men velosiped haydadim.", "Hozir men velosiped haydayapman.",
                                                      "Ertaga u velosiped haydaydi."],
                   say="Завтра я буду кататься на велосипеде."),
            RTF("“Завтра будет дождь” — “Ertaga yomg‘ir yog‘adi” degani.", True, say="Завтра будет дождь.", x="To‘g‘ri."),
            SENT("Завтра мы будем играть в шахматы", "Ertaga biz shaxmat o‘ynaymiz."),
            Q("Qaysi gap to‘g‘ri?", "Они будут жить в Ташкенте.", ["Они будет жить в Ташкенте.",
                                                                  "Они будут живут в Ташкенте.",
                                                                  "Они будут жил в Ташкенте."],
              x="Они будут + fe’lning noaniq shakli: жить."),
            RQ("Mos so‘zni tanlang: Дети … смотреть мультфильм.", "будут", ["будет", "будем", "буду"],
               say="Дети ... смотреть мультфильм.", d=2, x="Дети — они: будут."),
            RQ("Mos so‘zni tanlang: Вы … учить английский?", "будете", ["будешь", "будут", "будем"],
               say="Вы ... учить английский?", d=2, x="Вы — будете."),
            RQ("Mos so‘zni tanlang: Завтра … холодно.", "будет", ["будут", "будешь", "будем"],
               say="Завтра ... холодно.", d=2, x="Rodsiz gap: будет холодно."),
            RQ("Kelasi zamonni tanlang: Я пишу письмо. → Завтра я … письмо.", "напишу", ["написал", "пишу", "писал"],
               say="Завтра я ... письмо.", d=2, x="Написать → я напишу (natija)."),
            RQ("Kelasi zamonni tanlang: Мы делаем уроки. → Вечером мы … уроки.", "сделаем", ["сделали", "делаем", "делали"],
               say="Вечером мы ... уроки.", d=2, x="Сделать → мы сделаем."),
            RQ("Kelasi zamonni tanlang: Я читаю книгу. → Завтра я … книгу.", "прочитаю", ["прочитал", "читаю", "читал"],
               say="Завтра я ... книгу.", d=2, x="Прочитать → я прочитаю."),
            Q("Qaysi gap kelasi zamonda?", "Мы построим дом.", ["Мы строили дом.", "Мы строим дом.", "Мы построили дом."],
              d=2, x="Построим — kelasi zamon (tugallangan fe’l)."),
            MATCH("Olmosh va yordamchi fe’l shaklini juftlang (kelasi zamon)",
                  [("я", "буду"), ("ты", "будешь"), ("он", "будет"), ("мы", "будем"), ("вы", "будете"), ("они", "будут")],
                  d=2),
            LISTEN("Yozda biz buvimnikiga boramiz.", ["Yozda biz buvimnikida edik.", "Qishda biz buvimnikiga boramiz.",
                                                     "Yozda buvim bizga keladi."], say="Летом мы поедем к бабушке.", d=2),
            RQ("“Что ты будешь делать летом?” savoliga mos javob", "Я буду плавать в море.",
               ["Я плавал в море.", "Я плаваю сейчас.", "Я был на море."], say="Что ты будешь делать летом?", d=2,
               x="Kelasi zamonda javob: Я буду плавать."),
            SENT("Я обязательно помогу тебе", "Men senga albatta yordam beraman.", d=2),
            RQ("Mos shaklni tanlang: Скоро папа … машину. (купить)", "купит", ["купил", "покупал", "купить"],
               say="Скоро папа ... машину.", d=3, x="Скоро — kelajak: купит."),
            RQ("Mos shaklni tanlang: Я тебе … завтра. (позвонить)", "позвоню", ["позвонил", "звонил", "позвонить"],
               say="Я тебе ... завтра.", d=3, x="Завтра — kelajak: позвоню."),
            RTF("“Я буду прочитать” — to‘g‘ri shakl.", False, say="я буду прочитать", d=3,
                x="Tugallangan fe’l буду bilan ishlatilmaydi: я прочитаю yoki я буду читать."),
            LISTEN("Men uy vazifasini tez bajarib qo‘yaman.", ["Men uy vazifasini bajarib bo‘ldim.",
                                                              "Men uy vazifasini bajarmayman.",
                                                              "U uy vazifasini tez bajaradi."],
                   say="Я быстро сделаю домашнее задание.", d=3),
            SENT("Через неделю начнутся каникулы", "Bir haftadan keyin ta’til boshlanadi.", d=3),
        ])

T.topic("comparison", "📏", L("Sifat darajalari", "Comparison of adjectives", "Степени сравнения прилагательных"),
        chapter=C3,
        theory="Qiyosiy daraja (-ее): быстрый → быстрее, тёплый → теплее, интересный → интереснее.\n"
               "Maxsus shakllar: большой → больше, маленький → меньше, хороший → лучше, плохой → хуже,\n"
               "высокий → выше, молодой → моложе, дорогой → дороже, лёгкий → легче.\n"
               "Taqqoslash: чем bilan — Слон больше, чем лошадь; yoki qaratqich bilan — Слон больше лошади.\n"
               "Orttirma daraja — самый: самый высокий дом, самая длинная улица, самое холодное утро.",
        items=[
            RQ("Qiyosiy darajani tanlang: быстрый → …", "быстрее", ["быстрый", "самый быстрый", "быстрейший"],
               say="быстрый", x="Быстрый → быстрее."),
            RQ("Qiyosiy darajani tanlang: тёплый → …", "теплее", ["тёплее", "тёплый", "теплейше"], say="тёплый",
               x="Тёплый → теплее (urg‘u ko‘chadi, ё yozilmaydi)."),
            RQ("Qiyosiy darajani tanlang: хороший → …", "лучше", ["хорошее", "хуже", "больше"], say="хороший",
               x="Maxsus shakl: хороший → лучше."),
            RQ("Qiyosiy darajani tanlang: большой → …", "больше", ["меньше", "болше", "большой"], say="большой",
               x="Большой → больше."),
            RQ("Mos so‘zni tanlang: Слон … лошади.", "тяжелее", ["легче", "тяжёлый", "самый тяжёлый"],
               say="Слон ... лошади.", x="Fil otdan og‘irroq: тяжелее."),
            RQ("Mos so‘zni tanlang: Летом …, чем зимой.", "теплее", ["холоднее", "тёплый", "самый тёплый"],
               say="Летом ..., чем зимой.", x="Yozda qishdan iliqroq: теплее."),
            Q("Qaysi gap to‘g‘ri? (fakt)", "Солнце больше Земли.", ["Земля больше Солнца.", "Луна больше Земли.",
                                                                  "Луна больше Солнца."],
              x="Quyosh Yerdan ancha katta."),
            RTF("“Самый” orttirma darajani bildiradi: самый умный.", True, say="самый умный", x="To‘g‘ri."),
            SENT("Это самая интересная игра", "Bu eng qiziqarli o‘yin."),
            RQ("Qiyosiy darajani tanlang: плохой → …", "хуже", ["плохее", "лучше", "меньше"], say="плохой", d=2,
               x="Maxsus shakl: плохой → хуже."),
            RQ("Qiyosiy darajani tanlang: высокий → …", "выше", ["высокее", "ниже", "высше"], say="высокий", d=2,
               x="Maxsus shakl: высокий → выше."),
            RQ("Mos so‘zni tanlang: Мой брат старше, … я.", "чем", ["как", "что", "где"], say="Мой брат старше, ... я.",
               d=2, x="Taqqoslash: старше, чем я."),
            RQ("Mos so‘zni tanlang: Гепард — … быстрое животное на суше.", "самое", ["самый", "самая", "самые"],
               say="Гепард — ... быстрое животное на суше.", d=2, x="Животное — оно: самое быстрое."),
            RQ("Mos so‘zni tanlang: Эверест — … высокая гора в мире.", "самая", ["самый", "самое", "самые"],
               say="Эверест — ... высокая гора в мире.", d=2, x="Гора — она: самая высокая."),
            RQ("Mos so‘zni tanlang: Синий кит — самое … животное на Земле.", "большое", ["больше", "большой", "большая"],
               say="Синий кит — самое ... животное на Земле.", d=2, x="Животное — оно: самое большое."),
            Q("Qaysi gap to‘g‘ri?", "Сто больше, чем девяносто.", ["Сорок больше, чем пятьдесят.",
                                                                 "Десять больше, чем двадцать.",
                                                                 "Восемь больше, чем восемнадцать."], d=2,
              x="100 > 90."),
            MATCH("Sifat va qiyosiy darajani juftlang",
                  [("хороший", "лучше"), ("плохой", "хуже"), ("большой", "больше"), ("маленький", "меньше"),
                   ("высокий", "выше"), ("быстрый", "быстрее"), ("лёгкий", "легче")], d=2),
            LISTEN("Bu kitob anavi kitobdan qiziqarliroq.", ["Bu kitob eng qiziqarli.", "Bu kitob anavisichalik qiziqarli emas.",
                                                            "Bu film anavi filmdan qiziqarliroq."],
                   say="Эта книга интереснее, чем та.", d=2),
            LISTEN("Opam mendan katta.", ["Opam mendan kichik.", "Akam mendan katta.", "Opam eng katta."],
                   say="Сестра старше меня.", d=2),
            SENT("Мой друг выше меня", "Do‘stim mendan baland.", d=2),
            RQ("Qiyosiy darajani tanlang: молодой → …", "моложе", ["молодее", "старше", "молоднее"], say="молодой", d=3,
               x="Maxsus shakl: молодой → моложе."),
            RQ("Qiyosiy darajani tanlang: дорогой → …", "дороже", ["дорогее", "дешевле", "дорожее"], say="дорогой", d=3,
               x="Maxsus shakl: дорогой → дороже."),
            RTF("“Более лучше” — to‘g‘ri shakl.", False, say="более лучше", d=3,
                x="Лучше — o‘zi qiyosiy daraja, более qo‘shilmaydi."),
            Q("“Eng sovuq fasl” ruschasi qanday?", "самое холодное время года",
              ["холоднее время года", "самый холодный время года", "очень холодно время года"], d=3,
              x="Время — оно: самое холодное время года."),
            LISTEN("Bu shahardagi eng baland bino.", ["Bu shahardagi eng eski bino.", "Bu bino baland emas.",
                                                     "Bu shahardagi eng katta park."],
                   say="Это самое высокое здание в городе.", d=3),
            SENT("Зимой дни короче чем летом", "Qishda kunlar yozdagiga qaraganda qisqaroq.", d=3,
                 full="Зимой дни короче, чем летом."),
        ])

T.topic("ordinals", "🥇", L("Tartib sonlar", "Ordinal numbers", "Порядковые числительные"),
        chapter=C3,
        theory="Tartib son — Который? Какой по счёту? (nechanchi?): первый, второй, третий, четвёртый, пятый,\n"
               "шестой, седьмой, восьмой, девятый, десятый.\n"
               "Ular sifat kabi otga moslashadi: первый урок, первая парта, первое место, первые дни.\n"
               "• третий — alohida: третий день, третья неделя, третье окно.\n"
               "Qayerda? — в пятом классе, на втором этаже. Sana: первое января, двадцать первое марта.",
        items=[
            Q("“Birinchi” ruschasi qanday?", "первый", ["один", "раз", "единица"], x="Birinchi — первый."),
            Q("“Uchinchi” ruschasi qanday?", "третий", ["три", "трёх", "тридцатый"], x="Uchinchi — третий."),
            RQ("“Седьмой” o‘zbekchasi qanday?", "yettinchi", ["oltinchi", "sakkizinchi", "yetmishinchi"], say="седьмой",
               x="Седьмой — yettinchi."),
            RQ("“Четвёртый” o‘zbekchasi qanday?", "to‘rtinchi", ["qirqinchi", "to‘rtta", "o‘n to‘rtinchi"],
               say="четвёртый", x="Четвёртый — to‘rtinchi."),
            RQ("Mos so‘zni tanlang: Сегодня … урок — математика. (1)", "первый", ["первая", "первое", "один"],
               say="Сегодня ... урок — математика.", x="Урок — он: первый урок."),
            RQ("Mos so‘zni tanlang: Это … неделя каникул. (2)", "вторая", ["второй", "второе", "два"],
               say="Это ... неделя каникул.", x="Неделя — она: вторая неделя."),
            Q("Yangi yil qaysi kuni boshlanadi?", "первое января", ["тридцать первое декабря", "первое марта",
                                                                    "второе января"], x="Yangi yil — первое января."),
            MATCH("Son va tartib sonni juftlang",
                  [("1", "первый"), ("2", "второй"), ("3", "третий"), ("4", "четвёртый"), ("5", "пятый"), ("8", "восьмой"),
                   ("10", "десятый")]),
            LISTEN("Ukam birinchi sinfda o‘qiydi.", ["Ukam uchinchi sinfda o‘qiydi.", "Ukam bir yoshda.",
                                                    "Singlim birinchi sinfda o‘qiydi."],
                   say="Мой брат учится в первом классе."),
            RTF("“Третий” — “uchinchi” degani.", True, say="третий", x="To‘g‘ri."),
            SENT("Сегодня первое октября", "Bugun birinchi oktyabr."),
            RQ("Mos so‘zni tanlang: Я учусь в … классе. (6)", "шестом", ["шестой", "шесть", "шестого"],
               say="Я учусь в ... классе.", d=2, x="Где? — в шестом классе."),
            RQ("Mos so‘zni tanlang: Мы живём на … этаже. (2)", "втором", ["второй", "два", "двух"],
               say="Мы живём на ... этаже.", d=2, x="Где? — на втором этаже."),
            RQ("Mos so‘zni tanlang: Наша команда заняла … место. (1)", "первое", ["первый", "первая", "одно"],
               say="Наша команда заняла ... место.", d=2, x="Место — оно: первое место."),
            Q("Navro‘z bayrami qaysi kuni?", "двадцать первое марта", ["первое января", "первое сентября",
                                                                       "первое октября"], d=2,
              x="Navro‘z — 21-mart: двадцать первое марта."),
            Q("O‘zbekistonda Mustaqillik kuni qaysi sanada?", "первое сентября", ["двадцать первое марта",
                                                                                "первое января", "девятое мая"], d=2,
              x="Mustaqillik kuni — 1-sentabr: первое сентября."),
            Q("Hafta dushanbadan boshlansa, juma nechanchi kun?", "пятый", ["шестой", "четвёртый", "седьмой"], d=2,
              x="Dushanba (1), seshanba (2), chorshanba (3), payshanba (4), juma (5)."),
            RQ("“Какое сегодня число?” savoliga mos javob", "Сегодня пятое апреля.",
               ["Сегодня пятница.", "Сегодня пять часов.", "Сегодня весна."], say="Какое сегодня число?", d=2,
               x="Число — sana: пятое апреля."),
            LISTEN("Bugun o‘ninchi may.", ["Bugun o‘n birinchi may.", "Ertaga o‘ninchi may.", "Bugun o‘ninchi mart."],
                   say="Сегодня десятое мая.", d=2),
            RTF("“Первая место” — to‘g‘ri birikma.", False, say="первая место", d=2, x="Место — оно: первое место."),
            SENT("Наш класс находится на третьем этаже", "Bizning sinfimiz uchinchi qavatda joylashgan.", d=2),
            RQ("Mos so‘zni tanlang: Я сижу за … партой. (3)", "третьей", ["третий", "третья", "три"],
               say="Я сижу за ... партой.", d=3, x="за + vosita kelishigi (парта — она): за третьей партой."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "четвёртый", ["читвёртый", "четвёртей", "четвёрый"], d=3,
              x="To‘g‘ri yozilishi: четвёртый."),
            LISTEN("U musobaqada ikkinchi o‘rinni egalladi.", ["U musobaqada birinchi o‘rinni egalladi.",
                                                              "U ikkinchi marta yugurdi.", "U musobaqada qatnashmadi."],
                   say="Он занял второе место в соревновании.", d=3),
            SENT("Мой день рождения двадцатого мая", "Mening tug‘ilgan kunim 20-mayda.", d=3),
        ])

T.topic("opposites", "↔️", L("Qarama-qarshi sifatlar", "Opposite adjectives", "Антонимы"),
        chapter=C3, gen="opposites", prereq=["comparison"],
        theory="Qarama-qarshi ma’noli sifatlar (антонимы): большой — маленький, длинный — короткий,\n"
               "горячий — холодный, быстрый — медленный, старый — молодой, весёлый — грустный,\n"
               "громкий — тихий, открытый — закрытый.\n"
               "Ular ham otga moslashadi: быстрая машина — медленная машина.\n"
               "Taqqoslang: Черепаха медленнее зайца.",
        levels=[{"modes": ["size", "length", "read"], "options": 3},
                {"modes": ["read", "listen"], "options": 4},
                {"modes": ["read", "listen"], "options": 4}])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["future", "comparison", "ordinals", "opposites"], chapter=C3)

# ============================================================ 4-chorak
T.topic("weather", "🌦️", L("Fasllar va ob-havo", "Seasons and weather", "Времена года и погода"),
        chapter=C4,
        theory="Ob-havo: ясно (ochiq), облачно (bulutli), пасмурно (xira, bulut qoplagan), туман, гроза (momaqaldiroq),\n"
               "мороз (ayoz), жара (jazirama).\n"
               "Harorat: Сегодня плюс двадцать градусов. Ночью минус два градуса.\n"
               "Zamon: Вчера было холодно. Сегодня тепло. Завтра будет дождь.\n"
               "Fasl sifatlari: зимний, весенний, летний, осенний: летние каникулы, осенний дождь.",
        items=[
            RQ("“Гроза” o‘zbekchasi qanday?", "momaqaldiroq", ["qor bo‘roni", "tuman", "do‘l"], say="гроза",
               x="Гроза — momaqaldiroq va chaqmoqli yomg‘ir."),
            RQ("“Мороз” o‘zbekchasi qanday?", "ayoz (qattiq sovuq)", ["jazirama", "shamol", "yomg‘ir"], say="мороз",
               x="Мороз — ayoz."),
            RQ("Mos so‘zni tanlang: Вчера … очень жарко.", "было", ["будет", "есть", "была"],
               say="Вчера ... очень жарко.", x="Вчера — o‘tgan zamon: было жарко."),
            RQ("Mos so‘zni tanlang: Завтра … снег.", "будет", ["был", "было", "будут"], say="Завтра ... снег.",
               x="Завтра — kelasi zamon: будет снег."),
            Q("“Ochiq, quyoshli (havo)” ruschasi qanday?", "ясно", ["пасмурно", "туманно", "сыро"], x="Ясно — ochiq havo."),
            Q("Qaysi so‘z issiq havoni bildiradi?", "жара", ["мороз", "метель", "снег"], x="Жара — jazirama."),
            LISTEN("Kecha momaqaldiroq bo‘ldi.", ["Kecha qor yog‘di.", "Ertaga momaqaldiroq bo‘ladi.", "Kecha havo ochiq edi."],
                   say="Вчера была гроза."),
            MATCH("So‘z va tarjimasini juftlang",
                  [("ясно", "ochiq havo"), ("облачно", "bulutli"), ("гроза", "momaqaldiroq"), ("мороз", "ayoz"),
                   ("жара", "jazirama"), ("радуга", "kamalak"), ("туман", "tuman")]),
            RTF("“Летние каникулы” — yozgi ta’til.", True, say="летние каникулы", x="To‘g‘ri."),
            RTF("“Вчера будет дождь” — to‘g‘ri gap.", False, say="Вчера будет дождь.",
                x="Вчера — o‘tgan zamon: Вчера был дождь."),
            RTF("O‘zbekistonda iyul odatda juda issiq oy.", True, say="В июле обычно очень жарко.",
                x="To‘g‘ri: iyulda jazirama bo‘ladi."),
            SENT("Завтра будет солнечно и тепло", "Ertaga quyoshli va iliq bo‘ladi."),
            RQ("“Пасмурно” o‘zbekchasi qanday?", "bulut qoplagan, xira", ["ochiq, quyoshli", "juda issiq", "shamolli"],
               say="пасмурно", d=2, x="Пасмурно — osmonni bulut qoplagan, xira havo."),
            RQ("Sifatni tanlang: зима → … каникулы", "зимние", ["зимний", "зимняя", "зимнее"], say="... каникулы", d=2,
               x="Каникулы — ko‘plik: зимние каникулы."),
            RQ("Sifatni tanlang: осень → … дождь", "осенний", ["осенняя", "осеннее", "осенние"], say="... дождь", d=2,
               x="Дождь — он: осенний дождь."),
            RQ("Sifatni tanlang: лето → … день", "летний", ["летняя", "летнее", "летние"], say="... день", d=2,
               x="День — он: летний день."),
            HEAR("Tinglang va haroratni tanlang", "+15°", ["−15°", "+50°", "+5°"], say="Сегодня плюс пятнадцать градусов.",
                 d=2),
            HEAR("Tinglang va haroratni tanlang", "−10°", ["+10°", "−12°", "−100°"], say="Ночью минус десять градусов.",
                 d=2),
            LISTEN("Ertaga havo bulutli bo‘ladi.", ["Bugun havo bulutli.", "Ertaga havo ochiq bo‘ladi.",
                                                   "Kecha havo bulutli edi."], say="Завтра будет облачно.", d=2),
            LISTEN("Ertalab tuman bor edi.", ["Kechqurun tuman bor edi.", "Ertalab yomg‘ir yog‘di.", "Ertaga tuman bo‘ladi."],
                   say="Утром был туман.", d=2),
            RQ("“Какая сегодня температура?” savoliga mos javob", "Плюс восемнадцать градусов.",
               ["Сегодня пятница.", "Сегодня идёт дождь.", "Восемнадцать лет."], say="Какая сегодня температура?", d=2,
               x="Harorat so‘ralgan: плюс восемнадцать градусов."),
            SENT("Зимой в горах лежит снег", "Qishda tog‘larda qor yotadi.", d=2),
            RQ("Sifatni tanlang: весна → … погода", "весенняя", ["весенний", "весеннее", "весенние"], say="... погода",
               d=3, x="Погода — она: весенняя погода."),
            RQ("Mos so‘zni tanlang: Сегодня плюс двадцать …", "градусов", ["градус", "градуса", "градусы"],
               say="Сегодня плюс двадцать ...", d=3, x="20 dan keyin: двадцать градусов."),
            RQ("Mos so‘zni tanlang: Ночью было минус два …", "градуса", ["градусов", "градус", "градусы"],
               say="Ночью было минус два ...", d=3, x="2, 3, 4 dan keyin: два градуса."),
            SENT("Какая погода будет завтра", "Ertaga havo qanday bo‘ladi?", d=3),
        ])

T.topic("health", "🤒", L("Salomatlik", "Health", "Здоровье"),
        chapter=C4,
        theory="Qayering og‘riyapti? — Что у тебя болит? — У меня болит голова (зуб, живот, горло, ухо).\n"
               "Ko‘plikda: У меня болят зубы (ноги, глаза).\n"
               "Kasallik: У меня температура. У меня насморк (tumov). Я простудился (shamolladim).\n"
               "Maslahat: Надо (нужно) пойти к врачу. Надо пить тёплый чай. Нельзя бегать под дождём.\n"
               "Shifoxonada: врач, медсестра (hamshira), лекарство (dori), рецепт, аптека (dorixona).",
        items=[
            RQ("“У меня болит голова” o‘zbekchasi qanday?", "Boshim og‘riyapti.",
               ["Tishim og‘riyapti.", "Qornim og‘riyapti.", "Boshim aylanyapti."], say="У меня болит голова.",
               x="Голова — bosh; болит — og‘riyapti."),
            RQ("“Лекарство” o‘zbekchasi qanday?", "dori", ["shifokor", "dorixona", "kasalxona"], say="лекарство",
               x="Лекарство — dori."),
            RQ("“Аптека” o‘zbekchasi qanday?", "dorixona", ["kasalxona", "poliklinika", "do‘kon"], say="аптека",
               x="Аптека — dorixona."),
            Q("“Tomoq” ruschasi qanday?", "горло", ["голова", "живот", "ухо"], x="Tomoq — горло."),
            Q("“Qorin” ruschasi qanday?", "живот", ["спина", "горло", "нога"], x="Qorin — живот."),
            RQ("Mos so‘zni tanlang: У него высокая …", "температура", ["голова", "лекарство", "аптека"],
               say="У него высокая ...", x="Высокая температура — yuqori harorat, isitma."),
            Q("Qayerda dori sotib olamiz?", "в аптеке", ["в библиотеке", "в кинотеатре", "на стадионе"],
              x="Dorixonada — в аптеке."),
            Q("Sog‘lom bo‘lish uchun nima qilish kerak?", "делать зарядку",
              ["мало спать", "не есть овощи", "весь день сидеть у телевизора"], x="Делать зарядку — badantarbiya qilish."),
            MATCH("Tana a’zosi va tarjimasini juftlang",
                  [("голова", "bosh"), ("горло", "tomoq"), ("живот", "qorin"), ("спина", "bel, orqa"), ("ухо", "quloq"),
                   ("зуб", "tish"), ("рука", "qo‘l")]),
            RTF("“У меня болят зубы” — to‘g‘ri gap.", True, say="У меня болят зубы.", x="Зубы — ko‘plik: болят."),
            RTF("“У меня болит ноги” — to‘g‘ri gap.", False, say="У меня болит ноги.", x="Ноги — ko‘plik: болят."),
            SENT("У меня болит горло", "Tomog‘im og‘riyapti."),
            RQ("Mos so‘zni tanlang: У меня болит …", "зуб", ["зубы", "зубов", "зуба"], say="У меня болит ...", d=2,
               x="Болит — birlik: зуб."),
            RQ("Mos so‘zni tanlang: У меня … ноги.", "болят", ["болит", "болело", "болела"], say="У меня ... ноги.", d=2,
               x="Ноги — ko‘plik: болят."),
            RQ("Mos so‘zni tanlang: Если болит зуб, надо идти к …", "стоматологу", ["повару", "водителю", "продавцу"],
               say="Если болит зуб, надо идти к ...", d=2, x="Tish og‘risa — стоматологу (tish shifokoriga)."),
            RQ("Mos so‘zni tanlang: Когда болит горло, надо пить … чай.", "тёплый", ["ледяной", "холодный"],
               say="Когда болит горло, надо пить ... чай.", d=2, x="Tomoq og‘risa, iliq choy ichish kerak."),
            Q("Tumov bo‘lganda nima deymiz?", "У меня насморк.", ["У меня день рождения.", "У меня новый телефон.",
                                                                "У меня болит нога."], d=2, x="Насморк — tumov."),
            LISTEN("Men shamolladim.", ["Men sog‘ayib ketdim.", "Men sport bilan shug‘ullandim.", "U shamolladi."],
                   say="Я простудился.", d=2),
            LISTEN("Senga shifokorga borish kerak.", ["Men shifokorga bordim.", "Shifokor bizga keladi.",
                                                     "Senga dam olish kerak."], say="Тебе надо пойти к врачу.", d=2),
            RQ("“Что у тебя болит?” savoliga mos javob", "У меня болит ухо.",
               ["У меня есть уши.", "Я иду к уху.", "Мне десять лет."], say="Что у тебя болит?", d=2,
               x="Nima og‘riyapti? — У меня болит ухо."),
            Q("Kim kasalxonada shifokorga yordam beradi?", "медсестра", ["продавец", "почтальон", "лётчик"], d=2,
              x="Медсестра — hamshira."),
            SENT("Надо пить много воды", "Ko‘p suv ichish kerak.", d=2),
            RQ("Mos so‘zni tanlang: Врач дал мне …", "рецепт", ["рецепта", "рецептом", "рецепту"],
               say="Врач дал мне ...", d=3, x="Что дал? — рецепт (tushum, o‘zgarmaydi)."),
            RQ("Mos so‘zni tanlang: Будь …! (Sog‘ bo‘l!)", "здоров", ["здоровый", "здоровье", "здорово"],
               say="Будь ...!", d=3, x="Будь здоров! — Sog‘ bo‘l!"),
            LISTEN("Dorini kuniga uch marta iching.", ["Dorini kuniga bir marta iching.", "Dori ichmang.",
                                                      "Kuniga uch marta suv iching."],
                   say="Принимайте лекарство три раза в день.", d=3),
            SENT("Мама вызвала врача", "Onam shifokor chaqirdi.", d=3),
        ])

T.topic("travel", "✈️", L("Sayohat", "Travel", "Путешествия"),
        chapter=C4,
        theory="Sayohat so‘zlari: путешествие (sayohat), билет (chipta), чемодан (chamadon), паспорт, вокзал,\n"
               "аэропорт, гостиница (mehmonxona), экскурсия, карта (xarita).\n"
               "Transport: ехать на поезде, лететь на самолёте, плыть на корабле.\n"
               "Qayerga? — поехать в Самарканд, поехать на море.  Qayerdan? — вернуться из Бухары, прилететь из Ташкента.\n"
               "Мы купили билеты, собрали чемоданы и поехали на вокзал.",
        items=[
            Q("“Chipta” ruschasi qanday?", "билет", ["паспорт", "чемодан", "карта"], x="Chipta — билет."),
            RQ("“Путешествие” o‘zbekchasi qanday?", "sayohat", ["dam olish kuni", "ta’til", "mehmonxona"],
               say="путешествие", x="Путешествие — sayohat."),
            RQ("“Карта” o‘zbekchasi qanday?", "xarita", ["chipta", "chamadon", "pasport"], say="карта", x="Карта — xarita."),
            RQ("Mos fe’lni tanlang: Мы … в Москву на самолёте.", "полетели", ["поплыли", "пошли", "побежали"],
               say="Мы ... в Москву на самолёте.", x="Samolyotda — лететь: полетели."),
            Q("Boshqa davlatga borish uchun qanday hujjat zarur?", "паспорт", ["рецепт", "дневник", "журнал"],
              x="Паспорт — chet elga chiqish hujjati."),
            Q("Qaysi so‘z transport emas?", "чемодан", ["поезд", "самолёт", "корабль"], x="Чемодан — chamadon."),
            LISTEN("Biz poyezdda Buxoroga ketdik.", ["Biz samolyotda Buxoroga uchdik.", "Biz poyezdda Xivaga ketdik.",
                                                    "Ular poyezdda Buxoroga ketdi."], say="Мы поехали в Бухару на поезде."),
            MATCH("So‘z va tarjimasini juftlang",
                  [("билет", "chipta"), ("чемодан", "chamadon"), ("гостиница", "mehmonxona"), ("карта", "xarita"),
                   ("путешествие", "sayohat"), ("вокзал", "vokzal"), ("берег", "qirg‘oq")]),
            RTF("Samolyot aeroportdan uchadi.", True, say="Самолёт улетает из аэропорта.", x="To‘g‘ri."),
            SENT("Мы купили билеты на поезд", "Biz poyezdga chipta sotib oldik."),
            Q("“Mehmonxona (otel)” ruschasi qanday?", "гостиница", ["гостиная", "больница", "столовая"], d=2,
              x="Гостиница — mehmonxona (otel); гостиная — uydagi mehmon xonasi."),
            RQ("Mos fe’lni tanlang: Туристы … по реке на корабле.", "плыли", ["летели", "бежали", "ползли"],
               say="Туристы ... по реке на корабле.", d=2, x="Kemada — плыть: плыли."),
            RQ("Mos shaklni tanlang: Мы вернулись из …", "Самарканда", ["Самарканд", "Самарканде", "Самарканду"],
               say="Мы вернулись из ...", d=2, x="из + qaratqich: из Самарканда."),
            RQ("Mos predlogni tanlang: Летом мы поедем … море.", "на", ["в", "из", "у"], say="Летом мы поедем ... море.",
               d=2, x="Dengizga dam olishga — на море."),
            RQ("Mos predlogni tanlang: Папа прилетел … Ташкента.", "из", ["в", "на", "к"], say="Папа прилетел ... Ташкента.",
               d=2, x="Qayerdan? — из Ташкента."),
            RQ("Mos shaklni tanlang: Мы жили в …", "гостинице", ["гостиница", "гостиницу", "гостиницей"],
               say="Мы жили в ...", d=2, x="Где? — в гостинице."),
            Q("Poyezdlar qayerdan jo‘naydi?", "с вокзала", ["из аптеки", "из аэропорта", "из магазина"], d=2,
              x="Poyezdlar vokzaldan jo‘naydi — с вокзала."),
            RQ("Mos so‘zni tanlang: В музее была интересная …", "экскурсия", ["гостиница", "чемодан", "билет"],
               say="В музее была интересная ...", d=2, x="Экскурсия — ekskursiya."),
            LISTEN("Chiptalar qancha turadi?", ["Chiptalar qayerda?", "Chiptalarni kim sotib oldi?",
                                               "Poyezd qachon jo‘naydi?"], say="Сколько стоят билеты?", d=2),
            RQ("“Где можно купить билет?” savoliga mos javob", "В кассе на вокзале.",
               ["В чемодане.", "Завтра утром.", "На самолёте."], say="Где можно купить билет?", d=2,
               x="Qayerda? — в кассе на вокзале."),
            SENT("Не забудь взять паспорт", "Pasportni olishni unutma.", d=2),
            RTF("“Гостиница” va “гостиная” — bir xil ma’noli so‘zlar.", False, say="гостиница, гостиная", d=3,
                x="Гостиница — otel; гостиная — uydagi mehmonxona xonasi."),
            LISTEN("Poyezd soat to‘qqizda jo‘naydi.", ["Poyezd soat to‘qqizda keladi.", "Samolyot soat to‘qqizda uchadi.",
                                                      "Poyezd soat o‘nda jo‘naydi."],
                   say="Поезд отправляется в девять часов.", d=3),
            Q("Qaysi gap to‘g‘ri?", "Мы летели на самолёте три часа.",
              ["Мы летели на самолёт три часа.", "Мы летели на самолёта три часа.", "Мы летели самолёт три часа."], d=3,
              x="На чём? — на самолёте."),
            SENT("Летом мы путешествовали по Узбекистану", "Yozda biz O‘zbekiston bo‘ylab sayohat qildik.", d=3),
        ])

TEXT_KHIVA = ("Прошлым летом наша семья ездила в Хиву. Мы поехали туда на поезде. Дорога была длинной, но "
              "интересной: за окном мы видели пустыню и верблюдов. В Хиве мы жили в небольшой гостинице недалеко "
              "от Ичан-Калы. Каждый день мы ходили на экскурсии. Больше всего мне понравились старые стены и "
              "высокий минарет. Домой я привёз маленький сувенир для друга.")
TEXT_ILL = ("В понедельник Дилшод не пошёл в школу. Утром у него болело горло и была высокая температура. Мама "
            "вызвала врача. Врач сказал: «Ты простудился. Тебе нужно лежать в постели три дня, пить тёплый чай с "
            "мёдом и принимать лекарство». Дилшод слушался врача, и в четверг он уже был здоров.")
TEXT_AUTUMN = ("Я люблю осень. В сентябре ещё тепло, но в октябре часто идут дожди. Листья на деревьях "
               "становятся жёлтыми и красными. Осенью на рынке много фруктов: виноград, яблоки, гранаты и хурма. "
               "В ноябре становится холоднее, и люди надевают тёплые куртки.")
TEXT_ROBOT = ("Мой друг Санжар учится в шестом классе. Он очень любит технику. Каждую субботу он ходит в кружок "
              "робототехники. Там ребята собирают роботов. Санжар говорит: «Когда я вырасту, я буду инженером. "
              "Я построю самого умного робота!»")
TEXT_GRANNY = ("Сегодня у бабушки день рождения. Утром я позвонил ей и поздравил её. Потом мы с сестрой пошли в "
               "магазин и купили бабушке красивые цветы. Вечером вся семья пришла к бабушке в гости. Бабушка "
               "угощала нас пловом и пирогами. Мы долго разговаривали, пели песни и смеялись.")

T.topic("reading", "📖", L("Matnlar va savollar", "Reading comprehension", "Тексты с вопросами"),
        chapter=C4,
        theory="Uzunroq matnni o‘qishdan oldin savollarni ko‘zdan kechiring.\n"
               "• Matnda kalit so‘zlarni toping: ismlar, sanalar, joylar, sonlar.\n"
               "• Kelishik qo‘shimchalariga qarang: к бабушке — buvinikiga, с сестрой — opa (singil) bilan, из Хивы — Xivadan.\n"
               "• Fe’l zamoniga e’tibor bering: ездила (o‘tgan), буду (kelasi).\n"
               "Javobni matndan tekshiring, taxmin qilmang.",
        items=[
            *READ(TEXT_KHIVA, "🕌", [
                Q("Oila qayerga sayohat qildi?", "в Хиву", ["в Бухару", "в Самарканд", "на море"],
                  x="Прошлым летом наша семья ездила в Хиву."),
                Q("Ular nimada borishdi?", "на поезде", ["на самолёте", "на машине", "на автобусе"],
                  x="Мы поехали туда на поезде."),
                Q("Deraza ortida nimalarni ko‘rishdi?", "пустыню и верблюдов", ["горы и снег", "море и корабли",
                                                                            "лес и медведей"], d=2,
                  x="За окном мы видели пустыню и верблюдов."),
                Q("Ular qayerda yashashdi?", "в небольшой гостинице", ["у бабушки", "в палатке", "в большом доме"], d=2,
                  x="В Хиве мы жили в небольшой гостинице."),
                TF("Muallif do‘sti uchun esdalik sovg‘a olib keldi.", True, d=2,
                   x="Домой я привёз маленький сувенир для друга."),
                TF("Yo‘l qisqa va zerikarli edi.", False, d=3, x="Дорога была длинной, но интересной."),
            ]),
            *READ(TEXT_ILL, "🤒", [
                Q("Dilshod qaysi kuni maktabga bormadi?", "в понедельник", ["во вторник", "в четверг", "в субботу"],
                  x="В понедельник Дилшод не пошёл в школу."),
                Q("Dilshodning nimasi og‘ridi?", "горло", ["зуб", "живот", "нога"], x="У него болело горло."),
                Q("Shifokorni kim chaqirdi?", "мама", ["папа", "бабушка", "учитель"], x="Мама вызвала врача."),
                Q("Shifokor necha kun yotishni aytdi?", "три дня", ["один день", "неделю", "пять дней"], d=2,
                  x="Тебе нужно лежать в постели три дня."),
                TF("Dilshod shifokorning gapiga quloq soldi.", True, d=2, x="Дилшод слушался врача."),
                Q("Dilshod qachon sog‘aydi?", "в четверг", ["в понедельник", "в субботу", "через месяц"], d=3,
                  x="В четверг он уже был здоров."),
            ]),
            *READ(TEXT_AUTUMN, "🍂", [
                Q("Muallif qaysi faslni yaxshi ko‘radi?", "осень", ["весну", "лето", "зиму"], x="Я люблю осень."),
                Q("Oktyabrda qanday ob-havo bo‘ladi?", "часто идут дожди", ["очень жарко", "идёт снег", "всегда ясно"],
                  d=2, x="В октябре часто идут дожди."),
                Q("Kuzda bozorda qaysi mevalar ko‘p?", "виноград, яблоки, гранаты и хурма",
                  ["арбузы и дыни", "бананы и апельсины", "клубника и вишня"], d=2,
                  x="Осенью на рынке много фруктов: виноград, яблоки, гранаты и хурма."),
                TF("Noyabrda havo iliqroq bo‘ladi.", False, d=2, x="В ноябре становится холоднее."),
            ]),
            *READ(TEXT_ROBOT, "🤖", [
                Q("Sanjar nechanchi sinfda o‘qiydi?", "6-sinfda", ["5-sinfda", "7-sinfda", "1-sinfda"],
                  x="Санжар учится в шестом классе."),
                Q("Sanjar qachon to‘garakka boradi?", "каждую субботу", ["каждый день", "в воскресенье", "в понедельник"],
                  d=2, x="Каждую субботу он ходит в кружок робототехники."),
                Q("Sanjar kim bo‘lmoqchi?", "инженером", ["врачом", "учителем", "лётчиком"], d=2,
                  x="Когда я вырасту, я буду инженером."),
                TF("To‘garakda bolalar robot yig‘ishadi.", True, x="Там ребята собирают роботов."),
            ]),
            *READ(TEXT_GRANNY, "🎂", [
                Q("Bugun kimning tug‘ilgan kuni?", "бабушки", ["мамы", "сестры", "дедушки"],
                  x="Сегодня у бабушки день рождения."),
                Q("Muallif do‘konga kim bilan bordi?", "с сестрой", ["с мамой", "с другом", "с бабушкой"], d=2,
                  x="Мы с сестрой пошли в магазин."),
                Q("Ular buvisiga nima sotib olishdi?", "красивые цветы", ["торт", "книгу", "платок"], d=2,
                  x="Купили бабушке красивые цветы."),
                Q("Buvi mehmonlarni nima bilan siyladi?", "пловом и пирогами", ["супом и хлебом", "чаем и мёдом",
                                                                             "мороженым"], d=3,
                  x="Бабушка угощала нас пловом и пирогами."),
                TF("Kechqurun butun oila buvinikiga keldi.", True, d=2, x="Вечером вся семья пришла к бабушке в гости."),
            ]),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"), ["weather", "health", "travel", "reading"],
       chapter=C4)
T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["accusative", "genitive", "possessive", "dative", "instrumental", "motion", "future", "comparison", "ordinals",
        "weather", "health", "travel", "reading"], chapter=C4, level=3)

T.write()
