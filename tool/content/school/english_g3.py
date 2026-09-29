"""Ingliz tili, 3-sinf: assets/data/school/english_g3.json + bank_english_g3.json.

Mavzular O‘zbekiston davlat dasturi ("Kids' English 3", ≈A1) yo‘nalishida; hamma matn va savollar o‘zimizniki
(darslikdan ko‘chirilmagan). Imlo — britancha (colour, rubber).
Lug‘at mavzulari (alifbo, tovushlar, ranglar, buyumlar, hayvonlar, taomlar) — umumiy `foreign_language.dart`
generatorlari; grammatika va iboralar — savollar banki.
Qayta yaratish: python3 tool/content/school/english_g3.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("english", 3, L("Ingliz tili", "English", "Английский язык"))

C1 = "1-chorak. Salom! Alifbo va sonlar"
C2 = "2-chorak. Ranglar, buyumlar va kiyimlar"
C3 = "3-chorak. Oilam, tanam va hayvonlar"
C4 = "4-chorak. Taomlar, kunlar va joylashuv"


# ------------------------------------------------------------ yordamchilar
def GAP(sentence, a, w, d=1, x=None, note=None, e=None, h=None):
    """Bo‘sh joyli inglizcha gap: ekranda ko‘rsatma + gap, ovozda — faqat gap (ingliz tilida)."""
    q = f"Bo‘sh joyga mos so‘zni tanlang: {sentence}" + (f" ({note})" if note else "")
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=sentence, lang="en")


def LISTEN(say, a, w, d=1, x=None, q="Tinglang va to‘g‘ri tarjimani tanlang"):
    """Tinglab tushunish: inglizcha gap eshitiladi, javob tanlanadi."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", say=say, lang="en")


def EN(q, a, w, say, d=1, x=None, e=None, h=None):
    """Savol matnida inglizcha qism bor — u ingliz ovozida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=say, lang="en")


def ENW(uz, a, w, d=1, x=None, e=None):
    """“olma” inglizcha qanday?"""
    return Q(f"“{uz}” inglizcha qanday?", a, w, d=d, x=x or f"{uz} — {a}", e=e)


def UZW(en, a, w, d=1, x=None, e=None):
    """“cat” so‘zining tarjimasi qaysi?"""
    return Q(f"“{en}” so‘zining tarjimasi qaysi?", a, w, d=d, x=x or f"{en} — {a}", e=e, say=en, lang="en")


def TFE(q, a, say, d=1, x=None):
    return TF(q, a, d=d, x=x, say=say, lang="en")


def SENT(en, d=1, x=None, q="So‘zlardan gap tuzing"):
    """Inglizcha gap tuzish (tinish belgisiz, javob ovozda aytilmaydi)."""
    return ORDER(q, en, d=d, x=x, lang="en")


def QSENT(en, d=1, x=None):
    return SENT(en, d=d, x=x, q="So‘zlardan savol tuzing")


def vocab_levels(themes):
    return [
        {"themes": themes, "modes": ["listen", "read"], "options": 3},
        {"themes": themes, "modes": ["read", "picture_word"], "options": 3, "sameTheme": True},
        {"themes": themes, "modes": ["picture_word", "read", "listen"], "options": 4, "sameTheme": True},
    ]


ALL_COLOURS = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown", "black", "white"]

# ============================================================ 1-chorak
T.topic("greetings", "👋", L("Salomlashish va tanishuv", "Hello! Nice to meet you", "Приветствие и знакомство"),
        chapter=C1,
        theory="Salomlashish: Hello! / Hi! — Salom!  Good morning! — Xayrli tong!  Goodbye! / Bye! — Xayr!\n"
               "Tanishuv: What's your name? — Isming nima? — My name is Ali. — Mening ismim Ali.\n"
               "How old are you? — Necha yoshdasan? — I'm nine. — Men to‘qqiz yoshdaman.\n"
               "How are you? — Qalaysan? — I'm fine, thank you. — Yaxshi, rahmat.\n"
               "Nice to meet you! — Tanishganimdan xursandman!  Thank you! — You're welcome! (Arzimaydi!)",
        items=[
            ENW("Salom!", "Hello!", ["Goodbye!", "Thank you!", "Sorry!"], e="👋",
                x="Hello! yoki Hi! — salomlashganda aytiladi."),
            ENW("Xayr!", "Goodbye!", ["Hello!", "Good morning!", "Thank you!"],
                x="Goodbye! yoki Bye! — xayrlashganda aytiladi."),
            ENW("Rahmat!", "Thank you!", ["Sorry!", "Hello!", "Goodbye!"], x="Thank you! — rahmat."),
            ENW("Kechirasiz!", "Sorry!", ["Please", "Hello!", "Thank you!"],
                x="Sorry! — kechirasiz (uzr so‘raganda aytiladi)."),
            Q("Ertalab qanday salomlashamiz?", "Good morning!", ["Good night!", "Goodbye!", "Good evening!"], e="🌅",
              x="Good morning! — xayrli tong. Good night! esa uxlashdan oldin aytiladi."),
            Q("Uxlashdan oldin nima deymiz?", "Good night!", ["Good morning!", "Hello!", "Thank you!"], e="🌙",
              x="Good night! — xayrli tun."),
            LISTEN("What's your name?", "Isming nima?", ["Necha yoshdasan?", "Qalaysan?", "Bu nima?"]),
            LISTEN("How old are you?", "Necha yoshdasan?", ["Isming nima?", "Qalaysan?", "Qayerdansan?"],
                   x="How old are you? — Necha yoshdasan? (old — yosh)"),
            LISTEN("How are you?", "Qalaysan?", ["Isming nima?", "Necha yoshdasan?", "Bu kim?"],
                   x="How are you? — Qalaysan? Javob: I'm fine, thank you."),
            EN("“What's your name?” savoliga mos javobni tanlang", "My name is Zarina.",
               ["I'm nine.", "I'm fine, thank you.", "Goodbye!"], say="What's your name?",
               x="Ism so‘ralsa, My name is … deb javob beramiz."),
            EN("“How old are you?” savoliga mos javobni tanlang", "I'm nine.",
               ["My name is Ali.", "I'm fine, thank you.", "Hello!"], say="How old are you?",
               x="Yosh so‘ralsa: I'm nine. — Men to‘qqiz yoshdaman."),
            EN("“How are you?” savoliga mos javobni tanlang", "I'm fine, thank you.",
               ["I'm nine.", "My name is Bobur.", "Good night!"], say="How are you?",
               x="Hol so‘ralsa: I'm fine, thank you. — Yaxshi, rahmat."),
            GAP("My ... is Anvar.", "name", ["old", "fine", "nice"], x="My name is Anvar. — Mening ismim Anvar."),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("Hello!", "Salom!"), ("Goodbye!", "Xayr!"), ("Thank you!", "Rahmat!"),
                   ("Good morning!", "Xayrli tong!"), ("Good night!", "Xayrli tun!"), ("Sorry!", "Kechirasiz!")],
                  lang="en"),
            TFE("“Good morning!” — “Xayrli tong!” degani.", True, say="Good morning!",
                x="To‘g‘ri: morning — tong, ertalab."),
            TFE("“Goodbye!” — “Salom!” degani.", False, say="Goodbye!",
                x="Goodbye! — Xayr! Salom! esa — Hello!"),
            GAP("How ... are you? — I'm ten.", "old", ["name", "is", "fine"], d=2,
                x="How old are you? — Necha yoshdasan?"),
            GAP("Nice to ... you!", "meet", ["name", "old", "fine"], d=2,
                x="Nice to meet you! — Tanishganimdan xursandman!"),
            GAP("... name is Dilnoza.", "My", ["I", "I'm", "Me"], d=2, x="My name is … — Mening ismim …"),
            LISTEN("Nice to meet you!", "Tanishganimdan xursandman!", ["Xayrli tun!", "Kechirasiz!", "Rahmat!"], d=2),
            EN("Qaysi javob “Hello! I'm Sardor.” gapiga mos?", "Hi, Sardor! I'm Laylo.",
               ["Good night, Sardor!", "I'm fine, thank you.", "I'm eight."], say="Hello! I'm Sardor.", d=2,
               x="Salomga salom bilan javob berib, o‘zimizni tanishtiramiz."),
            SENT("My name is Kamola", d=2, x="My name is Kamola. — Mening ismim Kamola."),
            QSENT("What is your name", d=2, x="What is your name? — Isming nima?"),
            QSENT("How old are you", d=2, x="How old are you? — Necha yoshdasan?"),
            Q("Qaysi gap to‘g‘ri yozilgan?", "I'm nine years old.",
              ["I nine years old.", "I'm nine year old.", "I is nine years old."], d=3,
              x="To‘g‘ri: I'm (I am) nine years old. — Men to‘qqiz yoshdaman."),
            SENT("I am fine, thank you", d=3, x="I am fine, thank you. — Yaxshi, rahmat."),
            EN("Do‘stingiz “Thank you!” dedi. Siz nima deysiz?", "You're welcome!",
               ["Sorry!", "Good night!", "Goodbye!"], say="Thank you!", d=3,
               x="Rahmatga javoban: You're welcome! — Arzimaydi!"),
        ])

T.topic("alphabet", "🔤", L("Ingliz alifbosi", "The alphabet", "Английский алфавит"),
        chapter=C1, gen="letters",
        theory="Ingliz alifbosida 26 ta harf bor: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.\n"
               "Unli harflar: A, E, I, O, U. Qolganlari asosan undosh harflar.\n"
               "Har bir harfning bosh (katta) va kichik shakli bor: A a, B b, G g, R r.\n"
               "Harf nomlari: A — [ey], E — [i:], I — [ay], G — [ji:], J — [jey], Y — [uay].\n"
               "Adashtirmang: b — d, p — q, m — n, i — l.",
        levels=[{"set": "all", "modes": ["upper"], "options": 3},
                {"set": "all", "modes": ["upper", "lower"], "options": 3, "similar": True},
                {"set": "all", "modes": ["mixed", "lower"], "options": 4, "similar": True}])

T.topic("phonics", "👂", L("Harf va tovush", "Letters and sounds", "Буквы и звуки"),
        chapter=C1, gen="first_letter", prereq=["alphabet"],
        theory="Ko‘p harflar so‘z boshida o‘z tovushini beradi:\n"
               "• b — ball, bag;  d — dog, desk;  m — mouse, milk;  s — sun, sock.\n"
               "• c ko‘pincha [k] deb o‘qiladi: cat, cup, car.\n"
               "• t — tiger, tree;  f — fish, fox;  h — hat, horse.\n"
               "Rasmga qarang, so‘zni ichingizda ayting va birinchi tovushni eshiting: fish — f.",
        levels=[{"options": 3, "letters": ["b", "c", "d", "f", "h", "m", "p", "s", "t"]},
                {"options": 3},
                {"options": 4}])

T.topic("numbers", "🔢", L("Sonlar 1–100", "Numbers 1–100", "Числа 1–100"),
        chapter=C1,
        theory="1–10: one, two, three, four, five, six, seven, eight, nine, ten.\n"
               "11–20: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty.\n"
               "13–19 oxirida -teen, o‘nliklar oxirida -ty: thirty (30), forty (40), fifty (50), sixty (60),\n"
               "seventy (70), eighty (80), ninety (90), one hundred (100).\n"
               "• Adashtirmang: thirteen (13) — thirty (30). Diqqat: forty (fourty emas!).\n"
               "Murakkab son chiziqcha bilan yoziladi: 25 — twenty-five, 47 — forty-seven.",
        items=[
            LISTEN("seven", "7", ["1", "11", "17"], q="Tinglang va sonni tanlang"),
            LISTEN("twelve", "12", ["2", "20", "21"], q="Tinglang va sonni tanlang"),
            LISTEN("fifteen", "15", ["50", "5", "14"], q="Tinglang va sonni tanlang"),
            LISTEN("three", "3", ["13", "30", "8"], q="Tinglang va sonni tanlang"),
            LISTEN("twenty", "20", ["12", "2", "22"], q="Tinglang va sonni tanlang"),
            ENW("Sakkiz", "eight", ["eighteen", "eighty", "three"], x="8 — eight; 18 — eighteen; 80 — eighty."),
            ENW("O‘n bir", "eleven", ["seven", "twelve", "one"], x="11 — eleven."),
            EN("“nine” — bu qaysi son?", "9", ["5", "19", "90"], say="nine", x="nine — 9; nineteen — 19; ninety — 90."),
            MATCH("Son va so‘zni juftlang",
                  [("1", "one"), ("2", "two"), ("3", "three"), ("4", "four"), ("5", "five"), ("6", "six")], lang="en"),
            MATCH("11 dan 19 gacha: son va so‘zni juftlang",
                  [("11", "eleven"), ("12", "twelve"), ("13", "thirteen"), ("14", "fourteen"), ("16", "sixteen"),
                   ("19", "nineteen")], lang="en"),
            Q("5 soni inglizcha qanday yoziladi?", "five", ["fife", "fiev", "fiwe"], x="5 — five."),
            Q("Hisoblang: 2 + 3. Javobni inglizcha tanlang", "five", ["four", "six", "three"], x="2 + 3 = 5 — five."),
            Q("Hisoblang: 10 + 10. Javobni inglizcha tanlang", "twenty", ["twelve", "ten", "thirty"],
              x="10 + 10 = 20 — twenty."),
            TFE("“six” — 6 degani.", True, say="six", x="To‘g‘ri: six — 6."),
            GAP("I'm ... years old.", "ten", ["two", "twelve", "one"], note="10",
                x="10 — ten: I'm ten years old."),
            LISTEN("thirty", "30", ["13", "3", "33"], d=2, q="Tinglang va sonni tanlang",
                   x="thirty — 30 (oxiri -ty); thirteen — 13 (oxiri -teen)."),
            LISTEN("thirteen", "13", ["30", "31", "3"], d=2, q="Tinglang va sonni tanlang",
                   x="thirteen — 13 (oxiri -teen)."),
            LISTEN("forty", "40", ["14", "4", "44"], d=2, q="Tinglang va sonni tanlang", x="forty — 40."),
            LISTEN("ninety", "90", ["19", "9", "99"], d=2, q="Tinglang va sonni tanlang", x="ninety — 90."),
            LISTEN("one hundred", "100", ["10", "1", "1000"], d=2, q="Tinglang va sonni tanlang",
                   x="one hundred — 100."),
            ENW("Ellik", "fifty", ["fifteen", "five", "sixty"], d=2, x="50 — fifty; 15 — fifteen."),
            ENW("Yetmish", "seventy", ["seventeen", "seven", "sixty"], d=2, x="70 — seventy; 17 — seventeen."),
            MATCH("O‘nliklarni juftlang",
                  [("20", "twenty"), ("30", "thirty"), ("40", "forty"), ("50", "fifty"), ("60", "sixty"),
                   ("80", "eighty")], d=2, lang="en"),
            EN("Qaysi son tushib qolgan? ten, twenty, thirty, ...", "forty", ["fourteen", "fifty", "thirteen"],
               say="ten, twenty, thirty, ...", d=2, x="10, 20, 30, 40 — forty."),
            TFE("“fourteen” — 40 degani.", False, say="fourteen", d=2, x="fourteen — 14; 40 esa — forty."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "forty", ["fourty", "fortey", "fourtey"], d=3,
              x="40 — forty: “four” so‘zidagi u harfi tushib qoladi."),
            LISTEN("twenty-five", "25", ["52", "35", "15"], d=3, q="Tinglang va sonni tanlang",
                   x="twenty-five — 25 (20 + 5)."),
            LISTEN("sixty-eight", "68", ["86", "16", "60"], d=3, q="Tinglang va sonni tanlang",
                   x="sixty-eight — 68 (60 + 8)."),
            LISTEN("forty-seven", "47", ["74", "17", "40"], d=3, q="Tinglang va sonni tanlang",
                   x="forty-seven — 47 (40 + 7)."),
            Q("36 inglizcha qanday?", "thirty-six", ["sixty-three", "thirteen-six", "thirty-seven"], d=3,
              x="36 = 30 + 6 — thirty-six."),
            Q("Hisoblang: 50 + 20. Javobni inglizcha tanlang", "seventy", ["seventeen", "sixty", "eighty"], d=3,
              x="50 + 20 = 70 — seventy."),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["greetings", "alphabet", "phonics", "numbers"], chapter=C1)

# ============================================================ 2-chorak
T.topic("colours", "🎨", L("Ranglar", "Colours", "Цвета"),
        chapter=C2, gen="colors",
        theory="Ranglar: red — qizil, yellow — sariq, blue — ko‘k, green — yashil, orange — to‘q sariq,\n"
               "purple — binafsha, pink — pushti, brown — jigarrang, black — qora, white — oq, grey — kulrang.\n"
               "Rang so‘zi otdan oldin keladi: a red apple — qizil olma, a green bag — yashil sumka.\n"
               "Savol: What colour is it? — U qanday rangda? — It's blue. — U ko‘k.",
        levels=[{"colors": ALL_COLOURS[:8], "options": 3, "modes": ["listen", "read"]},
                {"colors": ALL_COLOURS, "options": 3, "modes": ["read", "picture_word"]},
                {"colors": ALL_COLOURS, "options": 4, "modes": ["picture_word", "object", "read"]}])

T.topic("things", "🎒", L("Maktab buyumlari, o‘yinchoqlar, kiyimlar", "School things, toys and clothes",
                          "Школьные вещи, игрушки и одежда"),
        chapter=C2, gen="vocab",
        theory="Maktab buyumlari: pen — ruchka, pencil — qalam, book — kitob, ruler — chizg‘ich, bag — sumka.\n"
               "O‘yinchoqlar: ball — to‘p, doll — qo‘g‘irchoq, teddy bear — ayiqcha, kite — varrak, robot — robot.\n"
               "Kiyimlar: T-shirt — futbolka, dress — ko‘ylak, hat — shlyapa, socks — paypoq, coat — palto.\n"
               "Misol: This is my pencil. — Bu mening qalamim.  It's a red ball. — Bu qizil to‘p.",
        levels=vocab_levels(["toys_school", "clothes"]))

T.topic("this_these", "👉", L("a / an, This is / These are", "a / an, This is / These are", "a / an, This is / These are"),
        chapter=C2, prereq=["things"],
        theory="a — undosh tovush bilan boshlanadigan so‘z oldidan: a cat, a pen, a dress.\n"
               "an — unli tovush (a, e, i, o, u) bilan boshlanadigan so‘z oldidan: an apple, an egg, an umbrella.\n"
               "This is … — Bu … (bitta narsa): This is a book.\n"
               "These are … — Bular … (ko‘p narsa): These are books. Ko‘plikda so‘zga -s qo‘shiladi, a / an qo‘yilmaydi.\n"
               "What is this? — Bu nima? — It's a ruler. What are these? — They are socks.",
        items=[
            Q("Qaysi birikma to‘g‘ri?", "an apple", ["a apple", "an apples", "a apples"],
              x="apple unli a bilan boshlanadi: an apple."),
            Q("Qaysi birikma to‘g‘ri?", "a pencil", ["an pencil", "a pencils", "an pencils"],
              x="pencil undosh p bilan boshlanadi: a pencil."),
            Q("Qaysi birikma to‘g‘ri?", "an egg", ["a egg", "an eggs", "a eggs"],
              x="egg unli e bilan boshlanadi: an egg."),
            Q("Qaysi birikma to‘g‘ri?", "a dog", ["an dog", "a dogs", "an dogs"],
              x="dog undosh d bilan boshlanadi: a dog."),
            Q("Qaysi birikma to‘g‘ri?", "an orange", ["a orange", "an oranges", "a oranges"],
              x="orange unli o bilan boshlanadi: an orange."),
            Q("Qaysi so‘z oldidan “an” qo‘yiladi?", "elephant", ["dog", "book", "cat"],
              x="elephant unli e bilan boshlanadi: an elephant."),
            Q("Qaysi so‘z oldidan “a” qo‘yiladi?", "ball", ["egg", "apple", "ice cream"],
              x="ball undosh b bilan boshlanadi: a ball."),
            Q("“Bu kitob.” inglizcha qanday?", "This is a book.",
              ["These are a book.", "This are a book.", "These is books."],
              x="Bitta narsa: This is a book."),
            Q("“Bular qalamlar.” inglizcha qanday?", "These are pencils.",
              ["This is pencils.", "These are a pencil.", "This are pencils."],
              x="Ko‘p narsa: These are pencils."),
            GAP("This ... a ruler.", "is", ["are", "am", "be"], x="Bitta narsa — This is: This is a ruler."),
            GAP("These ... books.", "are", ["is", "am", "a"], x="Ko‘p narsa — These are: These are books."),
            GAP("... is a bag.", "This", ["These", "Are", "Is"], x="This is a bag. — Bu sumka."),
            GAP("... are toys.", "These", ["This", "Is", "It"], x="These are toys. — Bular o‘yinchoqlar."),
            LISTEN("What is this?", "Bu nima?", ["Bular nima?", "Bu kim?", "U qayerda?"]),
            EN("Rasmga qarang. What is this?", "It's an apple.", ["It's a apple.", "They are apples.", "It's an egg."],
               say="What is this?", e="🍎", x="Bu olma: It's an apple."),
            EN("Rasmga qarang. What is this?", "It's a cat.", ["It's an cat.", "It's a dog.", "These are cats."],
               say="What is this?", e="🐱", x="Bu mushuk: It's a cat."),
            EN("Rasmga qarang. What is this?", "It's an egg.", ["It's a egg.", "It's an apple.", "They are eggs."],
               say="What is this?", e="🥚", x="Bu tuxum: It's an egg."),
            EN("Rasmga qarang. What is this?", "It's a book.", ["It's an book.", "It's a pen.", "These are books."],
               say="What is this?", e="📕", x="Bu kitob: It's a book."),
            MATCH("Maktab buyumlarini tarjimasi bilan juftlang",
                  [("pen", "ruchka"), ("bag", "sumka"), ("ruler", "chizg‘ich"), ("desk", "parta"),
                   ("rubber", "o‘chirg‘ich"), ("book", "kitob")], lang="en"),
            MATCH("Kiyimlarni tarjimasi bilan juftlang",
                  [("hat", "shlyapa"), ("socks", "paypoq"), ("coat", "palto"), ("T-shirt", "futbolka"),
                   ("trousers", "shim"), ("skirt", "yubka"), ("scarf", "sharf")], lang="en"),
            Q("Qaysi birikma to‘g‘ri?", "an umbrella", ["a umbrella", "an umbrellas", "a umbrellas"], d=2,
              x="umbrella unli u bilan boshlanadi: an umbrella."),
            TFE("“an umbrella” — to‘g‘ri yozilgan.", True, say="an umbrella", d=2,
                x="umbrella unli u bilan boshlanadi, shuning uchun an."),
            TFE("“a elephant” — to‘g‘ri yozilgan.", False, say="a elephant", d=2,
                x="elephant unli e bilan boshlanadi: an elephant."),
            EN("“book” so‘zining ko‘plik shakli qaysi?", "books", ["book", "bookes", "a books"], say="book", d=2,
               x="Ko‘plikda -s qo‘shiladi: books."),
            GAP("These are ...", "dolls", ["doll", "a doll", "an doll"], d=2,
                x="These are dan keyin ko‘plik: These are dolls."),
            Q("Qaysi gap to‘g‘ri?", "This is an orange.", ["This is a orange.", "These is an orange.", "This are an orange."],
              d=2, x="This is + an orange (orange unli bilan boshlanadi)."),
            SENT("This is a red pen", d=2, x="This is a red pen. — Bu qizil ruchka."),
            SENT("These are my books", d=2, x="These are my books. — Bular mening kitoblarim."),
            EN("“box” so‘zining ko‘plik shakli qaysi?", "boxes", ["boxs", "box", "boxies"], say="box", d=3,
               x="x harfidan keyin -es qo‘shiladi: boxes."),
            SENT("It is an orange ball", d=3, x="orange (to‘q sariq) unli bilan boshlanadi: an orange ball."),
            Q("“Bular nima?” inglizcha qanday?", "What are these?", ["What is this?", "What is these?", "Who are these?"],
              d=3, x="Ko‘p narsa haqida: What are these?"),
            EN("“What are these?” savoliga mos javobni tanlang", "They are socks.",
               ["It's a sock.", "It is socks.", "This is socks."], say="What are these?", d=3,
               x="Ko‘p narsa: They are socks. — Ular paypoqlar."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["colours", "things", "this_these", "numbers"], chapter=C2)

# ============================================================ 3-chorak
T.topic("family", "👨‍👩‍👧", L("Mening oilam", "My family", "Моя семья"),
        chapter=C3,
        theory="Oila a’zolari: mother (mum) — ona, father (dad) — ota, sister — opa yoki singil, brother — aka yoki uka.\n"
               "grandmother (granny) — buvi, grandfather (grandpa) — bobo, baby — chaqaloq, family — oila.\n"
               "This is my mother. — Bu mening onam.  Who is this? — Bu kim?\n"
               "he — u (o‘g‘il bola, erkak kishi): He is my brother.\n"
               "she — u (qiz bola, ayol kishi): She is my sister.",
        items=[
            ENW("Ona", "mother", ["father", "sister", "brother"], x="mother (mum) — ona."),
            ENW("Ota", "father", ["mother", "grandfather", "baby"], x="father (dad) — ota."),
            UZW("brother", "aka yoki uka", ["opa yoki singil", "ota", "bobo"]),
            UZW("sister", "opa yoki singil", ["aka yoki uka", "ona", "buvi"]),
            ENW("Buvi", "grandmother", ["grandfather", "mother", "sister"], x="grandmother (granny) — buvi."),
            ENW("Bobo", "grandfather", ["grandmother", "father", "brother"], x="grandfather (grandpa) — bobo."),
            MATCH("So‘zni tarjimasi bilan juftlang",
                  [("mother", "ona"), ("father", "ota"), ("grandmother", "buvi"), ("grandfather", "bobo"),
                   ("baby", "chaqaloq"), ("family", "oila")], lang="en"),
            LISTEN("This is my mother.", "Bu mening onam.", ["Bu mening otam.", "Bu mening singlim.", "U mening buvim."]),
            LISTEN("Who is this?", "Bu kim?", ["Bu nima?", "Isming nima?", "Qalaysan?"],
                   x="Who — kim? What — nima?"),
            GAP("... is my brother.", "He", ["She", "I", "They"], x="brother — o‘g‘il bola, shuning uchun He."),
            GAP("... is my sister.", "She", ["He", "I", "They"], x="sister — qiz bola, shuning uchun She."),
            UZW("dad", "ota", ["ona", "aka", "bobo"], x="dad — ota (father so‘zining qisqa, mehrli shakli)."),
            TFE("“grandfather” — bobo degani.", True, say="grandfather", x="To‘g‘ri: grandfather — bobo."),
            TFE("“mum” — ota degani.", False, say="mum", x="mum — ona (mother); ota esa — dad (father)."),
            Q("Onangizning onasi sizga kim bo‘ladi? Inglizcha tanlang", "grandmother",
              ["mother", "sister", "grandfather"], d=2, x="Onaning onasi — buvi: grandmother."),
            Q("Otangizning otasi sizga kim bo‘ladi? Inglizcha tanlang", "grandfather",
              ["father", "brother", "grandmother"], d=2, x="Otaning otasi — bobo: grandfather."),
            GAP("This is my ... . She is ten.", "sister", ["brother", "father", "grandfather"], d=2,
                x="She — qiz bola haqida: sister."),
            GAP("This is my ... . He is a doctor.", "father", ["mother", "sister", "grandmother"], d=2,
                x="He — erkak kishi haqida: father."),
            EN("“Who is this?” savoliga mos javobni tanlang", "This is my grandpa.",
               ["It is a pen.", "I'm fine, thank you.", "I'm nine."], say="Who is this?", d=2,
               x="Who? — kim? Javobda odam aytiladi: This is my grandpa."),
            Q("Qaysi so‘z ortiqcha?", "pencil", ["mother", "brother", "sister"], d=2,
              x="pencil — qalam; qolganlari oila a’zolari."),
            SENT("This is my little brother", d=2, x="This is my little brother. — Bu mening ukam."),
            SENT("She is my mum", d=2, x="She is my mum. — U mening onam."),
            TFE("“She is my father.” — to‘g‘ri gap.", False, say="She is my father.", d=2,
                x="father — erkak kishi, shuning uchun: He is my father."),
            Q("“Mening oilam katta.” inglizcha qanday?", "My family is big.",
              ["My family is small.", "My big is family.", "Me family is big."], d=3,
              x="big — katta, small — kichik: My family is big."),
            LISTEN("Her name is Nodira.", "Uning ismi Nodira.",
                   ["Mening ismim Nodira.", "Sening isming Nodira.", "U mening singlim."], d=3,
                   x="Her name — uning (qizning) ismi."),
            GAP("This is my brother. ... name is Aziz.", "His", ["Her", "She", "He"], d=3,
                x="O‘g‘il bolaning ismi — his name, qiz bolaning ismi — her name."),
            SENT("My granny is very kind", d=3, x="My granny is very kind. — Buvim juda mehribon."),
        ])

T.topic("have_got", "🙋", L("have got / has got. Tanam", "have got / has got. My body", "have got / has got. Тело"),
        chapter=C3, prereq=["family"],
        theory="have got — bor (I, you, we, they bilan): I have got a cat. — Mening mushugim bor.\n"
               "has got — bor (he, she, it bilan): She has got a doll. It has got long ears.\n"
               "Qisqa shakl: I've got, he's got. Inkor: I haven't got a dog. She hasn't got a bike.\n"
               "Savol: Have you got a pet? — Yes, I have. / No, I haven't.\n"
               "Tana a’zolari: head — bosh, eye — ko‘z, ear — quloq, nose — burun, mouth — og‘iz, hand — qo‘l, leg — oyoq.",
        items=[
            GAP("I ... got a dog.", "have", ["has", "am", "is"], x="I bilan have got: I have got a dog."),
            GAP("She ... got a doll.", "has", ["have", "are", "am"], x="she bilan has got: She has got a doll."),
            GAP("He ... got a bike.", "has", ["have", "am", "are"], x="he bilan has got: He has got a bike."),
            GAP("We ... got a big house.", "have", ["has", "is", "am"], x="we bilan have got."),
            GAP("They ... got a cat.", "have", ["has", "is", "am"], x="they bilan have got."),
            GAP("The rabbit ... got long ears.", "has", ["have", "are", "am"],
                x="The rabbit = it, shuning uchun has got."),
            ENW("Ko‘z", "eye", ["ear", "nose", "hand"], x="eye — ko‘z; eyes — ko‘zlar.", e="👀"),
            ENW("Quloq", "ear", ["eye", "mouth", "leg"], x="ear — quloq.", e="👂"),
            ENW("Burun", "nose", ["mouth", "head", "ear"], x="nose — burun.", e="👃"),
            MATCH("Tana a’zolarini tarjimasi bilan juftlang",
                  [("head", "bosh"), ("eye", "ko‘z"), ("ear", "quloq"), ("nose", "burun"), ("mouth", "og‘iz"),
                   ("hand", "qo‘l"), ("leg", "oyoq")], lang="en"),
            LISTEN("I have got a cat.", "Mening mushugim bor.",
                   ["Mening itim bor.", "Uning mushugi bor.", "Mening mushugim yo‘q."]),
            LISTEN("She has got a doll.", "Uning qo‘g‘irchog‘i bor.",
                   ["Mening qo‘g‘irchog‘im bor.", "Uning to‘pi bor.", "Uning qo‘g‘irchog‘i yo‘q."]),
            TFE("“I has got a ball.” — to‘g‘ri gap.", False, say="I has got a ball.",
                x="I bilan have got ishlatiladi: I have got a ball."),
            TFE("“He has got a kite.” — to‘g‘ri gap.", True, say="He has got a kite.",
                x="To‘g‘ri: he bilan has got."),
            GAP("I have got two ...", "eyes", ["eye", "a eye", "an eyes"], d=2,
                x="Ikkita — ko‘plik: two eyes."),
            Q("Qaysi gap to‘g‘ri?", "A cat has got four legs.",
              ["A cat have got four legs.", "A cat has got four leg.", "A cat has got two legs."], d=2,
              x="a cat = it → has got; mushukning to‘rtta oyog‘i bor."),
            Q("Qaysi gap to‘g‘ri?", "We have got two hands.",
              ["We has got two hands.", "We have got two hand.", "We have got three hands."], d=2,
              x="we → have got; ikkita qo‘l — two hands."),
            GAP("My brother ... got a computer.", "has", ["have", "is", "are"], d=2,
                x="My brother = he, shuning uchun has got."),
            GAP("Have you got a pet? — Yes, I ...", "have", ["has", "am", "got"], d=2,
                x="Qisqa javob: Yes, I have. / No, I haven't."),
            Q("“Mening akam bor.” inglizcha qanday?", "I have got a brother.",
              ["I has got a brother.", "He has got a brother.", "I have got a sister."], d=2,
              x="Mening … bor — I have got …"),
            Q("Qaysi so‘z tana a’zosi emas?", "desk", ["arm", "leg", "head"], d=2,
              x="desk — parta; arm, leg, head — tana a’zolari."),
            SENT("I have got a new ball", d=2, x="I have got a new ball. — Mening yangi to‘pim bor."),
            SENT("My sister has got long hair", d=2, x="My sister has got long hair. — Opamning sochi uzun."),
            GAP("Has she got a bike? — No, she ...", "hasn't", ["haven't", "isn't", "has"], d=3,
                x="she bilan: Yes, she has. / No, she hasn't."),
            QSENT("Have you got a brother", d=3, x="Have you got a brother? — Sening akang (ukang) bormi?"),
            Q("Qaysi gap “yo‘q” (inkor) ma’nosida?", "I haven't got a pet.",
              ["I have got a pet.", "I've got a pet.", "Have you got a pet?"], d=3,
              x="haven't got — yo‘q: Mening uy hayvonim yo‘q."),
            TFE("“The elephant has got a long nose.” — to‘g‘ri gap.", True, say="The elephant has got a long nose.",
                d=3, x="The elephant = it → has got; filning burni (xartumi) uzun."),
        ])

T.topic("animals", "🐾", L("Hayvonlar", "Animals", "Животные"),
        chapter=C3, gen="vocab",
        theory="Uy hayvonlari (pets): cat — mushuk, dog — it, rabbit — quyon, parrot — to‘tiqush, fish — baliq.\n"
               "Ferma hayvonlari: cow — sigir, horse — ot, sheep — qo‘y, goat — echki, chicken — tovuq.\n"
               "Yovvoyi hayvonlar: lion — sher, tiger — yo‘lbars, bear — ayiq, monkey — maymun, elephant — fil.\n"
               "Misol: It's a monkey. It's brown. — Bu maymun. U jigarrang.",
        levels=vocab_levels(["animals"]))

T.topic("can", "🏊", L("I can / I can't", "I can / I can't", "I can / I can't"),
        chapter=C3, prereq=["animals"],
        theory="can — qila olaman (qila oladi): I can swim. — Men suza olaman.\n"
               "can't (cannot) — qila olmayman: I can't fly. — Men ucha olmayman.\n"
               "can hamma shaxs bilan bir xil: I can, he can, she can, it can — -s qo‘shilmaydi!\n"
               "can dan keyin fe’l o‘zgarmaydi: She can run. (She can runs emas.)\n"
               "Savol: Can you dance? — Yes, I can. / No, I can't.",
        items=[
            UZW("swim", "suzmoq", ["yugurmoq", "uchmoq", "sakramoq"], e="🏊"),
            ENW("uchmoq", "fly", ["run", "swim", "jump"], x="fly — uchmoq."),
            ENW("sakramoq", "jump", ["climb", "sing", "fly"], x="jump — sakramoq."),
            UZW("run", "yugurmoq", ["suzmoq", "o‘qimoq", "raqsga tushmoq"], e="🏃"),
            MATCH("Fe’lni tarjimasi bilan juftlang",
                  [("swim", "suzmoq"), ("run", "yugurmoq"), ("jump", "sakramoq"), ("fly", "uchmoq"),
                   ("sing", "qo‘shiq aytmoq"), ("dance", "raqsga tushmoq"), ("climb", "tirmashib chiqmoq")],
                  lang="en"),
            LISTEN("I can swim.", "Men suza olaman.", ["Men suza olmayman.", "U suza oladi.", "Men yugura olaman."]),
            LISTEN("I can't fly.", "Men ucha olmayman.", ["Men ucha olaman.", "Qush ucha oladi.", "Men sakray olmayman."]),
            Q("Qaysi gap to‘g‘ri?", "A fish can swim.", ["A fish can run.", "A fish can sing.", "A fish can ride a bike."],
              e="🐟", x="Baliq suza oladi: A fish can swim."),
            Q("Qaysi gap to‘g‘ri?", "A bird can fly.", ["A dog can fly.", "A cow can fly.", "A cat can fly."],
              e="🐦", x="Qush ucha oladi: A bird can fly."),
            GAP("A monkey ... climb trees.", "can", ["can't", "is", "has"], e="🐒",
                x="Maymun daraxtga chiqa oladi: A monkey can climb trees."),
            GAP("A cat ... fly.", "can't", ["can", "is", "have"], x="Mushuk ucha olmaydi: A cat can't fly."),
            TFE("“A horse can run.” — to‘g‘ri fikr.", True, say="A horse can run.", x="To‘g‘ri: ot yugura oladi."),
            TFE("“A snake can walk.” — to‘g‘ri fikr.", False, say="A snake can walk.",
                x="Ilonning oyog‘i yo‘q — u yura olmaydi, sudralib yuradi."),
            Q("Qaysi hayvon ucha oladi?", "a parrot", ["a cow", "a dog", "a horse"],
              x="parrot — to‘tiqush, u ucha oladi."),
            EN("“Can you swim?” savoliga qisqa javobni tanlang", "Yes, I can.", ["Yes, I do.", "Yes, I am.", "Yes, I have."],
               say="Can you swim?", d=2, x="Can bilan savolga can bilan javob beramiz: Yes, I can."),
            Q("Qaysi gap to‘g‘ri?", "She can dance.", ["She cans dance.", "She can dances.", "She can to dance."], d=2,
              x="can ga ham, undan keyingi fe’lga ham -s qo‘shilmaydi: She can dance."),
            Q("Qaysi gap to‘g‘ri?", "He can't sing.", ["He can't sings.", "He cant sing.", "He can'ts sing."], d=2,
              x="To‘g‘ri yozilishi: can't (apostrof bilan), fe’l o‘zgarmaydi."),
            Q("“Men shaxmat o‘ynay olaman.” inglizcha qanday?", "I can play chess.",
              ["I can't play chess.", "I can plays chess.", "I play can chess."], d=2,
              x="can + fe’l: I can play chess."),
            LISTEN("Can you dance?", "Sen raqsga tusha olasanmi?",
                   ["Men raqsga tusha olaman.", "U raqsga tusha olmaydi.", "Sen qo‘shiq ayta olasanmi?"], d=2),
            GAP("A baby ... read.", "can't", ["can", "cans", "is"], d=2,
                x="Chaqaloq o‘qiy olmaydi: A baby can't read."),
            SENT("I can ride a bike", d=2, x="I can ride a bike. — Men velosiped hayday olaman."),
            SENT("My brother can play chess", d=2, x="My brother can play chess. — Akam shaxmat o‘ynay oladi."),
            QSENT("Can you play football", d=3, x="Can you play football? — Sen futbol o‘ynay olasanmi?"),
            GAP("Can a penguin fly? — No, it ...", "can't", ["can", "isn't", "doesn't"], d=3,
                x="Pingvin ucha olmaydi: No, it can't."),
            EN("Topishmoqni toping: It can swim, but it can't walk.", "a fish", ["a cat", "a horse", "a bird"],
               say="It can swim, but it can't walk.", d=3, x="Suza oladi, lekin yura olmaydi — baliq (a fish)."),
            EN("Topishmoqni toping: It can fly. It can sing. It has got two legs.", "a bird",
               ["a fish", "a cat", "a frog"], say="It can fly. It can sing. It has got two legs.", d=3,
               x="Ucha oladi, sayray oladi, ikki oyog‘i bor — qush (a bird)."),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["family", "have_got", "animals", "can"], chapter=C3)

# ============================================================ 4-chorak
T.topic("food", "🍎", L("Taomlar, meva va sabzavotlar", "Food, fruit and vegetables", "Еда, фрукты и овощи"),
        chapter=C4, gen="vocab",
        theory="Mevalar: apple — olma, banana — banan, orange — apelsin, grapes — uzum, pear — nok.\n"
               "Sabzavotlar: carrot — sabzi, tomato — pomidor, potato — kartoshka, cucumber — bodring.\n"
               "Taomlar: bread — non, milk — sut, egg — tuxum, cheese — pishloq, soup — sho‘rva, ice cream — muzqaymoq.\n"
               "Misol: I like apples. — Men olmani yaxshi ko‘raman. I don't like carrots. — Men sabzini yoqtirmayman.",
        levels=vocab_levels(["food_all"]))

T.topic("days", "📅", L("Hafta kunlari", "Days of the week", "Дни недели"),
        chapter=C4,
        theory="Hafta kunlari doim bosh harf bilan yoziladi:\n"
               "Monday — dushanba, Tuesday — seshanba, Wednesday — chorshanba, Thursday — payshanba,\n"
               "Friday — juma, Saturday — shanba, Sunday — yakshanba.\n"
               "Kun oldidan on qo‘yiladi: on Monday — dushanba kuni.\n"
               "What day is it today? — Bugun qaysi kun? — It's Friday. — Bugun juma.",
        items=[
            ENW("Dushanba", "Monday", ["Sunday", "Tuesday", "Friday"]),
            ENW("Juma", "Friday", ["Thursday", "Monday", "Saturday"]),
            EN("“Sunday” — bu qaysi kun?", "yakshanba", ["shanba", "dushanba", "juma"], say="Sunday",
               x="Sunday — yakshanba."),
            EN("“Wednesday” — bu qaysi kun?", "chorshanba", ["seshanba", "payshanba", "dushanba"], say="Wednesday",
               x="Wednesday — chorshanba."),
            EN("Qaysi kun tushib qolgan? Monday, ..., Wednesday", "Tuesday", ["Sunday", "Thursday", "Friday"],
               say="Monday, ..., Wednesday", x="Monday, Tuesday, Wednesday."),
            EN("Qaysi kun tushib qolgan? Thursday, ..., Saturday", "Friday", ["Sunday", "Monday", "Wednesday"],
               say="Thursday, ..., Saturday", x="Thursday, Friday, Saturday."),
            MATCH("Kunni tarjimasi bilan juftlang",
                  [("Monday", "dushanba"), ("Tuesday", "seshanba"), ("Wednesday", "chorshanba"),
                   ("Thursday", "payshanba"), ("Friday", "juma"), ("Saturday", "shanba"), ("Sunday", "yakshanba")],
                  lang="en"),
            TFE("Hafta kunlari bosh harf bilan yoziladi: Monday, Friday.", True, say="Monday, Friday",
                x="To‘g‘ri: hafta kunlari doim bosh harf bilan yoziladi."),
            TFE("Haftada yetti kun bor: seven days.", True, say="There are seven days in a week.",
                x="To‘g‘ri: haftada 7 kun bor."),
            LISTEN("Thursday", "Thursday", ["Tuesday", "Saturday", "Sunday"], q="Tinglang va kunni tanlang",
                   x="Thursday — payshanba; Tuesday — seshanba."),
            LISTEN("Tuesday", "Tuesday", ["Thursday", "Wednesday", "Friday"], q="Tinglang va kunni tanlang",
                   x="Tuesday — seshanba."),
            LISTEN("Saturday", "Saturday", ["Sunday", "Monday", "Friday"], q="Tinglang va kunni tanlang",
                   x="Saturday — shanba."),
            Q("Qaysi kun “T” harfi bilan boshlanadi?", "Tuesday", ["Monday", "Friday", "Sunday"],
              x="Tuesday — T bilan boshlanadi (Thursday ham)."),
            Q("Haftada nechta kun bor? Inglizcha tanlang", "seven", ["five", "six", "ten"],
              x="Haftada seven (7) kun bor."),
            Q("Qaysi so‘z hafta kuni emas?", "Monkey", ["Monday", "Sunday", "Friday"],
              x="Monkey — maymun; Monday — dushanba."),
            EN("Qaysi kun tushib qolgan? Saturday, ..., Monday", "Sunday", ["Friday", "Tuesday", "Thursday"],
               say="Saturday, ..., Monday", d=2, x="Saturday, Sunday, Monday."),
            EN("Inglizchada “weekend” qaysi kunlar?", "Saturday and Sunday",
               ["Monday and Tuesday", "Friday and Monday", "Wednesday and Thursday"], say="weekend", d=2,
               x="weekend — hafta oxiri: Saturday and Sunday."),
            GAP("I have English ... Monday.", "on", ["in", "at", "under"], d=2,
                x="Hafta kuni oldidan on: on Monday."),
            EN("Bugun — Friday. Ertaga qaysi kun bo‘ladi?", "Saturday", ["Thursday", "Sunday", "Monday"],
               say="Today is Friday.", d=2, x="Friday dan keyin Saturday keladi."),
            LISTEN("What day is it today?", "Bugun qaysi kun?", ["Soat necha?", "Isming nima?", "Bugun havo qanday?"], d=2),
            SENT("Today is Wednesday", d=2, x="Today is Wednesday. — Bugun chorshanba."),
            SENT("We go to the park on Sunday", d=2, x="We go to the park on Sunday. — Yakshanba kuni parkka boramiz."),
            EN("Bugun — Monday. Kecha qaysi kun edi?", "Sunday", ["Tuesday", "Saturday", "Wednesday"],
               say="Today is Monday.", d=3, x="Monday dan oldin Sunday keladi."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "Wednesday", ["Wensday", "Wednsday", "wednesday"], d=3,
              x="Wednesday: d harfi eshitilmaydi, lekin yoziladi; kun nomi bosh harf bilan."),
            QSENT("What day is it today", d=3, x="What day is it today? — Bugun qaysi kun?"),
        ])

T.topic("where_is", "📦", L("Where is…? in / on / under", "Where is…? in / on / under", "Where is…? in / on / under"),
        chapter=C4,
        theory="in — ichida: The pen is in the bag. — Ruchka sumkaning ichida.\n"
               "on — ustida: The book is on the desk. — Kitob partaning ustida.\n"
               "under — tagida (ostida): The cat is under the chair. — Mushuk stulning tagida.\n"
               "Where is …? — … qayerda? Where is the ball? — It's under the bed.\n"
               "Ko‘p narsa: Where are my books? — They are in the box.",
        items=[
            ENW("ichida", "in", ["on", "under", "at"], x="in — ichida."),
            ENW("ustida", "on", ["in", "under", "near"], x="on — ustida."),
            ENW("tagida (ostida)", "under", ["on", "in", "near"], x="under — tagida, ostida."),
            LISTEN("The cat is under the chair.", "Mushuk stulning tagida.",
                   ["Mushuk stulning ustida.", "Mushuk qutining ichida.", "It stulning tagida."]),
            LISTEN("The book is on the desk.", "Kitob partaning ustida.",
                   ["Kitob partaning ichida.", "Kitob partaning tagida.", "Ruchka partaning ustida."]),
            LISTEN("The apple is in the bag.", "Olma sumkaning ichida.",
                   ["Olma sumkaning tagida.", "Olma stolning ustida.", "Nok sumkaning ichida."]),
            Q("Ruchka sumkaning ichida. Mos gapni tanlang", "The pen is in the bag.",
              ["The pen is on the bag.", "The pen is under the bag.", "The bag is in the pen."],
              x="ichida — in: The pen is in the bag."),
            Q("To‘p stolning tagida. Mos gapni tanlang", "The ball is under the table.",
              ["The ball is on the table.", "The ball is in the table.", "The doll is under the table."],
              x="tagida — under."),
            GAP("... is my bag? — It's on the chair.", "Where", ["What", "Who", "How"],
                x="Where — qayerda? Javobda joy aytiladi."),
            GAP("Where ... the ball?", "is", ["are", "am", "be"], x="Bitta narsa: Where is …?"),
            GAP("The lamp is ... the table.", "on", ["in", "under", "at"], note="ustida", x="ustida — on."),
            GAP("The shoes are ... the bed.", "under", ["on", "in", "at"], note="tagida", x="tagida — under."),
            GAP("The toys are ... the box.", "in", ["on", "under", "at"], note="ichida", x="ichida — in."),
            MATCH("So‘zni tarjimasi bilan juftlang",
                  [("in", "ichida"), ("on", "ustida"), ("under", "tagida"), ("box", "quti"), ("bed", "karavot"),
                   ("table", "stol"), ("chair", "stul")], lang="en"),
            TFE("“on” — ustida degani.", True, say="on", x="To‘g‘ri: on — ustida."),
            TFE("“under” — ichida degani.", False, say="under", x="under — tagida (ostida); ichida esa — in."),
            GAP("Where ... my shoes?", "are", ["is", "am", "be"], d=2, x="Ko‘p narsa (shoes): Where are …?"),
            EN("“Where is the dog?” savoliga mos javobni tanlang", "It's under the bed.",
               ["It's a dog.", "Yes, it is.", "It's brown."], say="Where is the dog?", d=2,
               x="Where? — qayerda? Javobda joy aytiladi: under the bed."),
            Q("“Mening qalamim qayerda?” inglizcha qanday?", "Where is my pencil?",
              ["What is my pencil?", "Who is my pencil?", "Where are my pencil?"], d=2,
              x="qayerda — where; bitta qalam — is."),
            SENT("The cat is on the sofa", d=2, x="The cat is on the sofa. — Mushuk divanning ustida."),
            QSENT("Where is my ruler", d=2, x="Where is my ruler? — Chizg‘ichim qayerda?"),
            EN("“Where are the pencils?” savoliga mos javobni tanlang", "They are in the box.",
               ["It is in the box.", "They are pencils.", "Yes, they are."], say="Where are the pencils?", d=3,
               x="Ko‘p narsa — they are: They are in the box."),
            Q("Qaysi gap to‘g‘ri?", "The books are on the desk.",
              ["The books is on the desk.", "The book are on the desk.", "The books are on desk."], d=3,
              x="books — ko‘p narsa, shuning uchun are."),
            SENT("My books are in the bag", d=3, x="My books are in the bag. — Kitoblarim sumkada."),
            LISTEN("Where is the book? It's under the chair.", "stulning tagida",
                   ["stulning ustida", "sumkaning ichida", "stolning ustida"], d=3,
                   q="Tinglang: kitob qayerda?", x="under the chair — stulning tagida."),
            LISTEN("The teddy bear is in the box.", "qutining ichida",
                   ["qutining ustida", "karavotning tagida", "stolning ustida"], d=3,
                   q="Tinglang: ayiqcha qayerda?", x="in the box — qutining ichida."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["food", "days", "where_is", "can"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["greetings", "numbers", "colours", "this_these", "family", "have_got", "animals", "can", "food", "days",
        "where_is"], chapter=C4, level=3)

T.write()
