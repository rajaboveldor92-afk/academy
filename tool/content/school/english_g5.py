"""Ingliz tili, 5-sinf: assets/data/school/english_g5.json + bank_english_g5.json.

Mavzular O‘zbekiston davlat dasturi (5-sinf, ≈A1+/A2) yo‘nalishida: to be, egalik, ko‘plik, so‘roq so‘zlari,
Present Simple / Continuous, vaqt va kun tartibi, there is / are, some / any, can / must, oylar va ob-havo,
Past Simple, sifat darajalari, o‘qib tushunish. Hamma matn va savollar o‘zimizniki (darslikdan ko‘chirilmagan).
Imlo — britancha (colour, favourite, centre). Lug‘at mavzulari (harakatlar, kasblar va joylar, qarama-qarshi
sifatlar) — umumiy `foreign_language.dart` generatorlari; qolgani — savollar banki.
Qayta yaratish: python3 tool/content/school/english_g5.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("english", 5, L("Ingliz tili", "English", "Английский язык"))

C1 = "1-chorak. Men, oilam va do‘stlarim"
C2 = "2-chorak. Kun tartibi va mashg‘ulotlar"
C3 = "3-chorak. Shahar, qoidalar va ob-havo"
C4 = "4-chorak. O‘tgan zamon va taqqoslash"


# ------------------------------------------------------------ yordamchilar
def GAP(sentence, a, w, d=1, x=None, note=None, e=None, h=None):
    """Bo‘sh joyli inglizcha gap: ekranda ko‘rsatma + gap, ovozda — faqat gap (ingliz tilida)."""
    q = f"Bo‘sh joyni to‘ldiring: {sentence}" + (f" ({note})" if note else "")
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=sentence, lang="en")


def LISTEN(say, a, w, d=1, x=None, q="Tinglang va tarjimasini tanlang"):
    """Tinglab tushunish: inglizcha gap eshitiladi, javob tanlanadi."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", say=say, lang="en")


def EN(q, a, w, say, d=1, x=None, e=None, h=None):
    """Savol matnida inglizcha qism bor — u ingliz ovozida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=say, lang="en")


def FORM(word, what, a, w, d=1, x=None):
    """“go” fe’lining o‘tgan zamon shakli — so‘z ingliz ovozida aytiladi."""
    return Q(f"“{word}” {what}", a, w, d=d, x=x or f"{word} → {a}", say=word, lang="en")


def TFE(q, a, say, d=1, x=None):
    return TF(q, a, d=d, x=x, say=say, lang="en")


def SENT(en, d=1, x=None, q="So‘zlardan gap tuzing"):
    """Inglizcha gap tuzish (tinish belgisiz, javob ovozda aytilmaydi)."""
    return ORDER(q, en, d=d, x=x, lang="en")


def QSENT(en, d=1, x=None):
    return SENT(en, d=d, x=x, q="So‘zlardan savol tuzing")


def READ(text, q, a, w, d=1, x=None):
    """O‘qib tushunish: matn ekranda, savol inglizcha (ovozda ham)."""
    return Q(q, a, w, d=d, x=x, text=text, say=q, lang="en")


def RTF(text, statement, a, d=1, x=None):
    return TF(statement, a, d=d, x=x, text=text, say=statement, lang="en")


def vocab_levels(themes, special=False):
    if special:
        return [
            {"themes": themes, "modes": ["listen", "read"], "options": 3},
            {"themes": themes, "modes": ["read", "picture_word"], "options": 4},
            {"themes": themes, "modes": ["picture_word", "listen"], "options": 4},
        ]
    return [
        {"themes": themes, "modes": ["listen", "read"], "options": 3},
        {"themes": themes, "modes": ["read", "picture_word"], "options": 3, "sameTheme": True},
        {"themes": themes, "modes": ["picture_word", "read", "listen"], "options": 4, "sameTheme": True},
    ]


# ============================================================ 1-chorak
T.topic("to_be", "🙂", L("to be: am / is / are", "to be: am / is / are", "Глагол to be: am / is / are"),
        chapter=C1,
        theory="to be fe’li hozirgi zamonda uch shaklda keladi:\n"
               "• I am (I'm) • he / she / it is (he's, she's, it's) • we / you / they are (we're, you're, they're)\n"
               "Inkor: not qo‘shiladi — I'm not, she isn't (is not), they aren't (are not).\n"
               "Savolda fe’l oldinga chiqadi: Is he a pupil? — Yes, he is. / No, he isn't.\n"
               "Misol: My sister is ten. We are in the classroom.",
        items=[
            GAP("I ... a pupil.", "am", ["is", "are", "be"], x="I bilan am: I am a pupil."),
            GAP("She ... my best friend.", "is", ["am", "are", "be"], x="she bilan is."),
            GAP("They ... at school now.", "are", ["is", "am", "be"], x="they bilan are."),
            GAP("My dog ... very funny.", "is", ["are", "am", "be"], x="my dog = it, shuning uchun is."),
            GAP("We ... eleven years old.", "are", ["is", "am", "be"], x="we bilan are."),
            GAP("You ... a good singer.", "are", ["is", "am", "be"], x="you bilan are."),
            GAP("It ... cold today.", "is", ["are", "am", "be"], x="it bilan is."),
            GAP("My parents ... teachers.", "are", ["is", "am", "be"], x="my parents = they, shuning uchun are."),
            EN("“he is” ning qisqa shakli qaysi?", "he's", ["he'm", "he're", "his"], say="he is",
               x="he is = he's; his esa — uning (egalik so‘zi)."),
            LISTEN("We are brothers.", "Biz aka-ukamiz.", ["Ular aka-uka.", "Biz do‘stmiz.", "U mening akam."]),
            TFE("“I am eleven years old.” — to‘g‘ri gap.", True, say="I am eleven years old.",
                x="To‘g‘ri: I bilan am ishlatiladi."),
            MATCH("To‘liq va qisqa shaklni juftlang",
                  [("I am", "I'm"), ("he is", "he's"), ("she is", "she's"), ("it is", "it's"), ("we are", "we're"),
                   ("they are", "they're"), ("you are", "you're")], lang="en"),
            Q("Qaysi olmosh bilan “are” ishlatiladi?", "they", ["he", "she", "I"],
              x="are — we, you, they bilan ishlatiladi."),
            EN("“they are” ning qisqa shakli qaysi?", "they're", ["they's", "their", "they'm"], say="they are", d=2,
               x="they are = they're; their esa — ularning."),
            EN("“I am not” ning qisqa shakli qaysi?", "I'm not", ["I amn't", "I isn't", "I aren't"], say="I am not", d=2,
               x="I am not = I'm not (amn't degan shakl yo‘q)."),
            EN("Inkor shaklini tanlang: She is at home.", "She isn't at home.",
               ["She not is at home.", "She aren't at home.", "She doesn't at home."], say="She is at home.", d=2,
               x="is + not = isn't: She isn't at home."),
            EN("Inkor shaklini tanlang: We are late.", "We aren't late.",
               ["We isn't late.", "We not are late.", "We don't late."], say="We are late.", d=2,
               x="are + not = aren't: We aren't late."),
            EN("Savol shaklini tanlang: He is a doctor.", "Is he a doctor?",
               ["He is a doctor?", "Does he a doctor?", "Are he a doctor?"], say="He is a doctor.", d=2,
               x="Savolda is oldinga chiqadi: Is he a doctor?"),
            EN("Savol shaklini tanlang: They are happy.", "Are they happy?",
               ["Is they happy?", "Do they happy?", "They happy are?"], say="They are happy.", d=2,
               x="Savolda are oldinga chiqadi: Are they happy?"),
            GAP("Is your sister at school? — No, she ...", "isn't", ["aren't", "not", "doesn't"], d=2,
                x="Is …? savoliga qisqa javob: No, she isn't."),
            GAP("... you hungry? — No, I'm not.", "Are", ["Is", "Am", "Do"], d=2, x="you bilan are: Are you hungry?"),
            GAP("Where ... my keys?", "are", ["is", "am", "be"], d=2, x="keys — ko‘plik, shuning uchun are."),
            TFE("“Ali and Vali is brothers.” — to‘g‘ri gap.", False, say="Ali and Vali is brothers.", d=2,
                x="Ikki kishi — ko‘plik: Ali and Vali are brothers."),
            LISTEN("She isn't at home.", "U uyda emas.", ["U uyda.", "Men uyda emasman.", "Ular uyda emas."], d=2),
            SENT("My brother is a good footballer", d=2, x="My brother is a good footballer. — Akam yaxshi futbolchi."),
            QSENT("Are you ready for the lesson", d=2, x="Are you ready for the lesson? — Darsga tayyormisiz?"),
            EN("Qisqa javobni tanlang: Are you from Tashkent?", "Yes, I am.", ["Yes, I'm.", "Yes, I is.", "Yes, you are."],
               say="Are you from Tashkent?", d=3,
               x="Qisqa ijobiy javobda qisqartma ishlatilmaydi: Yes, I am. (Yes, I'm. — xato)"),
            GAP("Tom and I ... good friends.", "are", ["am", "is", "be"], d=3, x="Tom and I = we, shuning uchun are."),
            Q("To‘g‘ri gapni tanlang", "The children are in the garden.",
              ["The children is in the garden.", "The children am in the garden.", "The children be in the garden."],
              d=3, x="children — ko‘plik (bolalar), shuning uchun are."),
            SENT("We are not in the classroom", d=3, x="We are not in the classroom. — Biz sinfda emasmiz."),
        ])

T.topic("possessives", "🔑", L("Egalik: my, your, his, her… va 's", "Possessives: my, your, his… and 's",
                              "Притяжательные: my, your, his… и 's"),
        chapter=C1, prereq=["to_be"],
        theory="Egalik olmoshlari otdan oldin keladi:\n"
               "I → my, you → your, he → his, she → her, it → its, we → our, they → their.\n"
               "Misol: She has got a cat. Her cat is white. — Uning mushugi oq.\n"
               "'s — kimningdir narsasi: Ali's bag — Alining sumkasi, my mum's car — onamning mashinasi.\n"
               "Whose …? — Kimning …? Whose pen is this? — It's Zarina's.",
        items=[
            GAP("I have got a sister. ... name is Malika.", "Her", ["His", "Their", "Our"],
                x="sister — qiz bola, shuning uchun her name."),
            GAP("This is my brother. ... name is Jasur.", "His", ["Her", "Its", "Their"],
                x="brother — o‘g‘il bola, shuning uchun his name."),
            GAP("We love ... school.", "our", ["we", "us", "ours"], x="we → our (bizning): our school."),
            GAP("They are in ... room.", "their", ["they", "there", "them"],
                x="they → their (ularning); there — u yerda."),
            GAP("What's ... name? — My name is Bobur.", "your", ["you", "my", "his"], x="you → your (sening)."),
            GAP("I am Dilshod and this is ... dog, Rex.", "my", ["me", "I", "mine"], x="I → my (mening): my dog."),
            FORM("we", "olmoshining egalik shakli qaysi?", "our", ["us", "their", "your"], x="we → our (bizning)."),
            MATCH("Olmoshni egalik shakli bilan juftlang",
                  [("I", "my"), ("you", "your"), ("he", "his"), ("she", "her"), ("it", "its"), ("we", "our"),
                   ("they", "their")], lang="en"),
            LISTEN("This is Ali's bag.", "Bu Alining sumkasi.",
                   ["Bu mening sumkam.", "Bu Alining kitobi.", "Bu Ali uchun sumka."]),
            TFE("“Her name is Anvar.” — o‘g‘il bola haqida to‘g‘ri gap.", False, say="Her name is Anvar.",
                x="O‘g‘il bola uchun his: His name is Anvar."),
            TFE("“Their house is big.” — to‘g‘ri gap.", True, say="Their house is big.",
                x="To‘g‘ri: they → their house."),
            Q("“Bizning uyimiz” inglizcha qanday?", "our house", ["we house", "us house", "their house"],
              x="bizning — our: our house."),
            Q("“Mening kitobim” inglizcha qanday?", "my book", ["me book", "I book", "mine book"],
              x="mening — my: my book."),
            SENT("Our teacher is very kind", x="Our teacher is very kind. — Bizning o‘qituvchimiz juda mehribon."),
            FORM("they", "olmoshining egalik shakli qaysi?", "their", ["there", "them", "they're"], d=2,
                 x="they → their (ularning). there — u yerda, they're — they are."),
            Q("“Onamning mashinasi” inglizcha qanday?", "my mum's car", ["my mum car", "my car's mum", "mum my car"], d=2,
              x="Egalik 's bilan: my mum's car."),
            GAP("... pen is this? — It's Lola's.", "Whose", ["Who", "What", "Where"], d=2, x="Whose? — kimning?"),
            EN("“Whose bag is this?” savoliga mos javobni tanlang", "It's Timur's.",
               ["It's a bag.", "It's on the desk.", "Yes, it is."], say="Whose bag is this?", d=2,
               x="Whose? — kimning? Javob: It's Timur's (Timurniki)."),
            Q("To‘g‘ri gapni tanlang", "My friend's name is Aziz.",
              ["My friends name is Aziz.", "My friend name's is Aziz.", "Me friend's name is Aziz."], d=2,
              x="Do‘stimning ismi — my friend's name."),
            GAP("Sara and Tom are here with ... parents.", "their", ["they", "there", "them"], d=2,
                x="Sara and Tom = they → their parents."),
            GAP("The dog is eating ... food.", "its", ["it's", "it", "their"], d=2,
                x="its — uning (hayvon yoki narsa); it's = it is."),
            Q("“Ularning bog‘i” inglizcha qanday?", "their garden", ["there garden", "they garden", "them garden"], d=2,
              x="ularning — their: their garden."),
            SENT("This is my sister's bike", d=2, x="This is my sister's bike. — Bu opamning velosipedi."),
            GAP("Is this ... book, Nodir? — Yes, it's mine.", "your", ["you", "my", "his"], d=3,
                x="Nodirdan so‘rayapmiz: your book (sening kitobing)."),
            GAP("My grandparents live in Samarkand. ... house is near the river.", "Their",
                ["There", "They're", "They"], d=3, x="grandparents = they → their house."),
            GAP("The cat is licking ... paw.", "its", ["it's", "it", "is"], d=3,
                x="its — uning (mushukning) panjasi; it's = it is."),
            QSENT("Whose phone is this", d=3, x="Whose phone is this? — Bu kimning telefoni?"),
            Q("To‘g‘ri gapni tanlang", "These are the children's toys.",
              ["These are the childrens toys.", "These are the children toys's.", "These is the children's toys."],
              d=3, x="children's — bolalarning: the children's toys."),
        ])

T.topic("plurals", "👣", L("Otlarning ko‘plik shakli", "Plural nouns", "Множественное число"),
        chapter=C1,
        theory="Ko‘plikda odatda -s qo‘shiladi: a book → books, a cat → cats.\n"
               "-s, -ss, -sh, -ch, -x dan keyin -es: a bus → buses, a box → boxes, a watch → watches.\n"
               "Undosh + y → -ies: a city → cities, a baby → babies (lekin a boy → boys).  -f / -fe → -ves: leaf → leaves.\n"
               "Maxsus shakllar: man → men, woman → women, child → children, foot → feet, tooth → teeth, mouse → mice.\n"
               "this → these, that → those: These are my shoes. Those birds are big.",
        items=[
            FORM("book", "so‘zining ko‘plik shakli", "books", ["bookes", "bookies", "book"], x="Oddiy qoida: -s → books."),
            FORM("box", "so‘zining ko‘plik shakli", "boxes", ["boxs", "boxies", "boxen"], x="x dan keyin -es: boxes."),
            FORM("child", "so‘zining ko‘plik shakli", "children", ["childs", "childes", "childrens"],
                 x="Maxsus shakl: child → children."),
            FORM("man", "so‘zining ko‘plik shakli", "men", ["mans", "mens", "manes"], x="Maxsus shakl: man → men."),
            FORM("woman", "so‘zining ko‘plik shakli", "women", ["womans", "womens", "womanes"],
                 x="Maxsus shakl: woman → women."),
            FORM("mouse", "so‘zining ko‘plik shakli", "mice", ["mices", "mousies", "mousen"],
                 x="Maxsus shakl: mouse → mice (sichqonlar)."),
            FORM("tooth", "so‘zining ko‘plik shakli", "teeth", ["tooths", "teeths", "toothes"],
                 x="Maxsus shakl: tooth → teeth."),
            FORM("foot", "so‘zining ko‘plik shakli", "feet", ["foots", "feets", "footes"],
                 x="Maxsus shakl: foot → feet."),
            Q("“Ikkita olma” inglizcha qanday?", "two apples", ["two apple", "two appless", "a two apples"],
              x="Ikkita — ko‘plik: two apples."),
            GAP("... are my new shoes.", "These", ["This", "That", "It"], x="shoes — ko‘plik, shuning uchun These are."),
            GAP("Three ... are playing in the park.", "children", ["child", "childs", "childrens"],
                x="Uchta bola — three children."),
            TFE("“feet” — “foot” so‘zining ko‘plik shakli.", True, say="foot, feet", x="To‘g‘ri: one foot, two feet."),
            FORM("baby", "so‘zining ko‘plik shakli", "babies", ["babys", "babyes", "babyies"], d=2,
                 x="Undosh + y → -ies: babies."),
            FORM("boy", "so‘zining ko‘plik shakli", "boys", ["boies", "boyes", "boyies"], d=2,
                 x="y dan oldin unli (o) bor, shuning uchun faqat -s: boys."),
            FORM("leaf", "so‘zining ko‘plik shakli", "leaves", ["leafs", "leafes", "leavs"], d=2,
                 x="-f → -ves: leaf → leaves."),
            FORM("bus", "so‘zining ko‘plik shakli", "buses", ["buss", "busies", "bus"], d=2, x="s dan keyin -es: buses."),
            FORM("city", "so‘zining ko‘plik shakli", "cities", ["citys", "cityes", "cityies"], d=2,
                 x="Undosh + y → -ies: cities."),
            FORM("watch", "so‘zining ko‘plik shakli", "watches", ["watchs", "watchies", "watchen"], d=2,
                 x="ch dan keyin -es: watches."),
            MATCH("Birlik va ko‘plikni juftlang",
                  [("man", "men"), ("woman", "women"), ("child", "children"), ("foot", "feet"), ("tooth", "teeth"),
                   ("mouse", "mice")], d=2, lang="en"),
            GAP("Look at ... birds over there!", "those", ["that", "this", "it"], d=2,
                x="Uzoqdagi ko‘p narsa — those: those birds."),
            GAP("I brush my ... every morning.", "teeth", ["tooths", "tooth", "teeths"], d=2,
                x="Tishlar — teeth (tooth ning ko‘pligi)."),
            Q("Qaysi so‘z ko‘plikda?", "people", ["person", "child", "woman"], d=2,
              x="people — odamlar (person so‘zining ko‘pligi)."),
            SENT("These women are doctors", d=2, x="These women are doctors. — Bu ayollar shifokor."),
            SENT("The children are in the garden", d=2, x="The children are in the garden. — Bolalar bog‘da."),
            FORM("sheep", "so‘zining ko‘plik shakli", "sheep", ["sheeps", "sheepes", "shoop"], d=3,
                 x="sheep birlikda ham, ko‘plikda ham bir xil: one sheep, ten sheep."),
            FORM("tomato", "so‘zining ko‘plik shakli", "tomatoes", ["tomatos", "tomatoies", "tomato"], d=3,
                 x="tomato → tomatoes (-es qo‘shiladi), potato → potatoes ham shunday."),
            TFE("“knifes” — to‘g‘ri yozilgan.", False, say="knife", d=3, x="-fe → -ves: knife → knives."),
            Q("To‘g‘ri gapni tanlang", "Those boxes are heavy.",
              ["That boxes are heavy.", "Those boxs are heavy.", "Those boxes is heavy."], d=3,
              x="Ko‘plik: those + boxes + are."),
        ])

T.topic("question_words", "❓", L("So‘roq so‘zlari", "Question words", "Вопросительные слова"),
        chapter=C1, prereq=["to_be"],
        theory="What? — Nima?  Who? — Kim?  Where? — Qayerda?  When? — Qachon?\n"
               "Why? — Nega? (javob: Because …)  How? — Qanday?  How old? — Necha yoshda?\n"
               "How many? — Nechta?  Whose? — Kimning?  Which? — Qaysi? (tanlash kerak bo‘lsa)\n"
               "Misol: Where do you live? — I live in Bukhara. When is your birthday? — It's in May.",
        items=[
            Q("“Qayerda?” inglizcha qanday?", "Where?", ["When?", "What?", "Who?"], x="Where? — Qayerda?"),
            Q("“Kim?” inglizcha qanday?", "Who?", ["How?", "Why?", "What?"], x="Who? — Kim?"),
            Q("“Qachon?” inglizcha qanday?", "When?", ["Where?", "Which?", "Who?"], x="When? — Qachon?"),
            Q("“Nega?” inglizcha qanday?", "Why?", ["Who?", "What?", "How?"], x="Why? — Nega? Javob: Because …"),
            MATCH("So‘roq so‘zini tarjimasi bilan juftlang",
                  [("What?", "Nima?"), ("Who?", "Kim?"), ("Where?", "Qayerda?"), ("When?", "Qachon?"),
                   ("Why?", "Nega?"), ("How many?", "Nechta?"), ("Whose?", "Kimning?")], lang="en"),
            GAP("... is your name? — My name is Aziza.", "What", ["Who", "Where", "How"],
                x="Ism so‘ralganda: What is your name?"),
            GAP("... do you live? — In Namangan.", "Where", ["When", "Who", "What"],
                x="Javob — joy (In Namangan), shuning uchun Where."),
            GAP("... is your birthday? — In June.", "When", ["Where", "Who", "How"],
                x="Javob — vaqt (In June), shuning uchun When."),
            GAP("... old are you? — I'm eleven.", "How", ["What", "Who", "Where"], x="How old? — Necha yoshda?"),
            GAP("... is that man? — He's my uncle.", "Who", ["What", "Where", "When"],
                x="Javob — odam (my uncle), shuning uchun Who."),
            GAP("... are you sad? — Because I lost my pen.", "Why", ["What", "Where", "Who"],
                x="Javob Because bilan boshlansa, savol — Why."),
            EN("“How are you?” savoliga mos javobni tanlang", "I'm fine, thanks.",
               ["I'm eleven.", "I'm from Andijan.", "It's Monday."], say="How are you?",
               x="How are you? — Qalaysiz? Javob: I'm fine, thanks."),
            EN("“Where are you from?” savoliga mos javobni tanlang", "I'm from Uzbekistan.",
               ["I'm fine.", "I'm eleven.", "At seven o'clock."], say="Where are you from?",
               x="Where are you from? — Qayerdansiz? Javob: I'm from Uzbekistan."),
            TFE("“Who” — narsa haqida so‘raydi (nima?).", False, say="Who?",
                x="Who? — kim? (odam haqida). Narsa haqida — What? (nima?)."),
            GAP("How ... brothers have you got? — Two.", "many", ["much", "old", "long"], d=2,
                x="Sanaladigan narsalar soni — How many?"),
            GAP("... bag is this? — It's Olim's.", "Whose", ["Who", "Where", "How"], d=2,
                x="Javob — Olim's (Olimniki), shuning uchun Whose? (kimning?)."),
            EN("“When do you get up?” savoliga mos javobni tanlang", "At seven o'clock.",
               ["In the kitchen.", "With my brother.", "Because I'm hungry."], say="When do you get up?", d=2,
               x="When? — qachon? Javob — vaqt: At seven o'clock."),
            LISTEN("Why are you crying?", "Nega yig‘layapsan?",
                   ["Qayerda yig‘layapsan?", "Kim yig‘layapti?", "Qachon kulasan?"], d=2),
            LISTEN("Whose book is this?", "Bu kimning kitobi?", ["Bu qanday kitob?", "Kitob qayerda?", "Bu kim?"], d=2),
            QSENT("What is your favourite colour", d=2, x="What is your favourite colour? — Sevimli rangingiz qaysi?"),
            QSENT("Where is the school library", d=2, x="Where is the school library? — Maktab kutubxonasi qayerda?"),
            GAP("... colour do you like, red or blue? — Blue.", "Which", ["Who", "Whose", "Where"], d=3,
                x="Tanlash kerak bo‘lsa (red or blue) — Which? (qaysi?)."),
            GAP("... do you go to school? — By bus.", "How", ["What", "Who", "Why"], d=3,
                x="How? — qanday? (nima bilan): By bus — avtobusda."),
            EN("Javobga mos savolni tanlang: I've got three cats.", "How many cats have you got?",
               ["How much cats have you got?", "What cats have you got?", "Where are your cats?"],
               say="I've got three cats.", d=3, x="Son so‘ralmoqda — How many …?"),
            EN("Javobga mos savolni tanlang: She lives in London.", "Where does she live?",
               ["When does she live?", "Who does she live?", "Where she lives?"], say="She lives in London.", d=3,
               x="Joy so‘ralmoqda — Where does she live?"),
            QSENT("How many pencils have you got", d=3, x="How many pencils have you got? — Nechta qalaming bor?"),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["to_be", "possessives", "plurals", "question_words"], chapter=C1)

# ============================================================ 2-chorak
T.topic("present_simple", "🔁", L("Present Simple: I play / she plays", "Present Simple", "Present Simple"),
        chapter=C2,
        theory="Present Simple — odatiy, doimiy ishlar: I go to school every day.\n"
               "he / she / it bilan fe’lga -s qo‘shiladi: she plays, he reads.\n"
               "-o, -sh, -ch, -x, -s dan keyin -es: goes, watches; undosh + y → -ies: study → studies; have → has.\n"
               "Inkor: don't / doesn't + fe’l: I don't like milk. He doesn't like fish.\n"
               "Savol: Do / Does + ega + fe’l: Do you speak English? Does she live here? — Yes, she does.",
        items=[
            GAP("She ... tennis every Sunday.", "plays", ["play", "playing", "is play"],
                x="she bilan fe’lga -s: she plays."),
            GAP("I ... in Fergana.", "live", ["lives", "living", "am live"], x="I bilan fe’l o‘zgarmaydi: I live."),
            GAP("My father ... to work by car.", "goes", ["go", "gos", "going"],
                x="my father = he; go → goes (-o dan keyin -es)."),
            GAP("They ... English at school.", "learn", ["learns", "learning", "is learn"],
                x="they bilan fe’l o‘zgarmaydi: they learn."),
            GAP("He ... TV in the evening.", "watches", ["watch", "watchs", "watching"],
                x="he bilan; ch dan keyin -es: watches."),
            GAP("We ... breakfast at 7 o'clock.", "have", ["has", "having", "haves"], x="we bilan: we have."),
            GAP("Cats ... milk.", "like", ["likes", "liking", "is like"], x="cats — ko‘plik (they): like."),
            FORM("have", "fe’lining he / she bilan shakli", "has", ["haves", "have", "hass"],
                 x="have → has: She has a bike."),
            GAP("I ... like coffee.", "don't", ["doesn't", "am not", "not"], x="I bilan inkor: don't."),
            GAP("... you like ice cream?", "Do", ["Does", "Are", "Is"], x="you bilan savol: Do you …?"),
            TFE("“My cat sleeps a lot.” — to‘g‘ri gap.", True, say="My cat sleeps a lot.",
                x="To‘g‘ri: my cat = it → sleeps."),
            TFE("“She play the piano.” — to‘g‘ri gap.", False, say="She play the piano.",
                x="she bilan fe’lga -s qo‘shiladi: She plays the piano."),
            LISTEN("He swims every day.", "U har kuni suzadi.",
                   ["Men har kuni suzaman.", "U hozir suzyapti.", "U suzishni yoqtirmaydi."]),
            FORM("study", "fe’lining he / she bilan shakli", "studies", ["studys", "studyes", "study"], d=2,
                 x="Undosh + y → -ies: studies."),
            GAP("She ... eat meat.", "doesn't", ["don't", "isn't", "not"], d=2, x="she bilan inkor: doesn't."),
            GAP("... your brother play football?", "Does", ["Do", "Is", "Are"], d=2,
                x="your brother = he → Does …?"),
            GAP("Does Lola speak English? — Yes, she ...", "does", ["do", "is", "speaks"], d=2,
                x="Does …? savoliga qisqa javob: Yes, she does."),
            Q("To‘g‘ri gapni tanlang", "He doesn't like milk.",
              ["He don't like milk.", "He doesn't likes milk.", "He not like milk."], d=2,
              x="doesn't dan keyin fe’l -s siz: He doesn't like milk."),
            Q("Qaysi fe’l he / she bilan -es oladi?", "wash", ["play", "read", "sing"], d=2,
              x="-sh bilan tugagan: he washes."),
            LISTEN("We don't eat meat.", "Biz go‘sht yemaymiz.",
                   ["Biz go‘sht yeymiz.", "U go‘sht yemaydi.", "Biz baliq yemaymiz."], d=2),
            SENT("My sister reads books every day", d=2, x="My sister reads books every day. — Opam har kuni kitob o‘qiydi."),
            SENT("We don't go to school on Sunday", d=2,
                 x="We don't go to school on Sunday. — Yakshanba kuni maktabga bormaymiz."),
            Q("To‘g‘ri gapni tanlang", "Does she go to school?",
              ["Does she goes to school?", "Do she go to school?", "Is she go to school?"], d=3,
              x="Does + she + fe’l (-s siz): Does she go to school?"),
            GAP("Water ... at 100 degrees Celsius.", "boils", ["boil", "boiling", "is boil"], d=3,
                x="Doimiy haqiqat — Present Simple: water = it → boils."),
            GAP("The sun ... in the east.", "rises", ["rise", "rising", "is rise"], d=3,
                x="Doimiy haqiqat: quyosh sharqdan chiqadi — The sun rises in the east."),
            QSENT("Does your dad work in a bank", d=3, x="Does your dad work in a bank? — Dadangiz bankda ishlaydimi?"),
        ])

T.topic("routine_time", "⏰", L("Kun tartibi, vaqt, always / never", "Daily routine, time, adverbs of frequency",
                               "Распорядок дня, время, наречия частоты"),
        chapter=C2, prereq=["present_simple"],
        theory="Vaqt: What time is it? — It's seven o’clock (7:00). It's half past eight (8:30).\n"
               "quarter past nine — 9:15;  quarter to ten — 9:45.\n"
               "Kun tartibi: get up, have breakfast, go to school, do homework, go to bed.\n"
               "always (doim) → usually (odatda) → often (tez-tez) → sometimes (ba’zan) → never (hech qachon).\n"
               "Bu so‘zlar asosiy fe’ldan oldin, to be dan keyin keladi: I always get up at 7. She is never late.",
        items=[
            Q("Soatga mos javobni tanlang: 7:00", "It's seven o'clock.",
              ["It's half past seven.", "It's seventeen o'clock.", "It's quarter past seven."],
              x="7:00 — seven o’clock (yetti bo‘ldi)."),
            Q("Soatga mos javobni tanlang: 8:30", "It's half past eight.",
              ["It's half past nine.", "It's eight o'clock.", "It's quarter to eight."],
              x="8:30 — half past eight (sakkizdan yarim soat o‘tdi)."),
            LISTEN("It's half past ten.", "10:30", ["10:00", "11:30", "9:30"], q="Tinglang va vaqtni tanlang",
                   x="half past ten — 10:30."),
            LISTEN("It's four o'clock.", "4:00", ["4:30", "5:00", "3:00"], q="Tinglang va vaqtni tanlang",
                   x="four o'clock — 4:00."),
            FORM("always", "so‘zining tarjimasi", "doim", ["hech qachon", "ba’zan", "odatda"], x="always — doim."),
            FORM("never", "so‘zining tarjimasi", "hech qachon", ["doim", "tez-tez", "ba’zan"], x="never — hech qachon."),
            FORM("sometimes", "so‘zining tarjimasi", "ba’zan", ["doim", "hech qachon", "odatda"],
                 x="sometimes — ba’zan."),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("get up", "o‘rnidan turmoq"), ("have breakfast", "nonushta qilmoq"),
                   ("go to school", "maktabga bormoq"), ("do homework", "uy vazifasini bajarmoq"),
                   ("go to bed", "uxlashga yotmoq"), ("brush teeth", "tish yuvmoq")], lang="en"),
            GAP("I ... have breakfast at 7.", "always", ["never", "sometimes", "often"], note="doim",
                x="doim — always: I always have breakfast at 7."),
            GAP("I don't like fish. I ... eat fish.", "never", ["always", "usually", "often"], note="hech qachon",
                x="hech qachon — never."),
            GAP("I get up, then I ... my face.", "wash", ["go", "sleep", "play"],
                x="wash my face — yuzimni yuvaman."),
            GAP("After school I do my ...", "homework", ["breakfast", "bed", "teeth"],
                x="do my homework — uy vazifamni bajaraman."),
            TFE("“half past two” — 2:30 degani.", True, say="half past two", x="To‘g‘ri: half past two — 2:30."),
            Q("Soatga mos javobni tanlang: 3:15", "It's quarter past three.",
              ["It's quarter to three.", "It's half past three.", "It's three o'clock."], d=2,
              x="3:15 — quarter past three (uchdan chorak soat o‘tdi)."),
            LISTEN("It's quarter past six.", "6:15", ["6:45", "5:15", "6:30"], d=2, q="Tinglang va vaqtni tanlang",
                   x="quarter past six — 6:15."),
            Q("Qaysi so‘z eng ko‘p marta degani?", "always", ["often", "sometimes", "never"], d=2,
              x="always — doim (eng ko‘p), never — hech qachon."),
            Q("To‘g‘ri gapni tanlang", "I always get up at 7.",
              ["I get always up at 7.", "I get up always at 7.", "I always gets up at 7."], d=2,
              x="always asosiy fe’ldan oldin: I always get up."),
            TFE("“quarter to four” — 4:15 degani.", False, say="quarter to four", d=2,
                x="quarter to four — 3:45 (to‘rtga 15 daqiqa qoldi); 4:15 — quarter past four."),
            LISTEN("He usually goes to bed at nine.", "U odatda 9 da uxlashga yotadi.",
                   ["U doim 9 da uxlashga yotadi.", "U hech qachon 9 da yotmaydi.", "U odatda 9 da turadi."],
                   d=2),
            SENT("I usually walk to school", d=2, x="I usually walk to school. — Men odatda maktabga piyoda boraman."),
            SENT("We have lunch at one o'clock", d=2, x="We have lunch at one o'clock. — Biz soat birda tushlik qilamiz."),
            Q("Soatga mos javobni tanlang: 5:45", "It's quarter to six.",
              ["It's quarter to five.", "It's quarter past five.", "It's half past five."], d=3,
              x="5:45 — oltiga chorak qoldi: quarter to six."),
            LISTEN("It's quarter to nine.", "8:45", ["8:15", "9:45", "8:30"], d=3, q="Tinglang va vaqtni tanlang",
                   x="quarter to nine — to‘qqizga chorak qoldi: 8:45."),
            Q("To‘g‘ri gapni tanlang", "She is never late.",
              ["She never is late.", "Never she is late.", "She is late never."], d=3,
              x="to be dan keyin: She is never late."),
            SENT("My brother often plays computer games", d=3,
                 x="My brother often plays computer games. — Akam tez-tez kompyuter o‘yini o‘ynaydi."),
        ])

T.topic("present_continuous", "🏃", L("Present Continuous: I am reading", "Present Continuous", "Present Continuous"),
        chapter=C2, prereq=["present_simple"],
        theory="Present Continuous — hozir, ayni paytda bo‘layotgan ish: I am reading now.\n"
               "Tuzilishi: am / is / are + fe’l-ing: She is dancing. They are playing.\n"
               "-ing qo‘shish: write → writing (e tushadi), swim → swimming, run → running, sit → sitting.\n"
               "Inkor: He isn't sleeping. Savol: Are you listening? — Yes, I am.\n"
               "Kalit so‘zlar: now, at the moment, Look!, Listen!",
        items=[
            GAP("I ... reading a book now.", "am", ["is", "are", "do"], x="I bilan am: I am reading."),
            GAP("She is ... a letter now.", "writing", ["write", "writes", "writeing"],
                x="write → writing (oxirgi e tushadi)."),
            GAP("They are ... football at the moment.", "playing", ["play", "plays", "played"],
                x="are + fe’l-ing: are playing."),
            GAP("Look! The baby ... sleeping.", "is", ["are", "am", "does"], x="the baby = it → is sleeping."),
            GAP("We ... watching a film.", "are", ["is", "am", "does"], x="we bilan are."),
            FORM("read", "fe’lining -ing shakli", "reading", ["readding", "readeing", "reads"], x="read → reading."),
            LISTEN("They are having lunch now.", "Ular hozir tushlik qilyapti.",
                   ["Ular har kuni tushlik qiladi.", "Biz hozir tushlik qilyapmiz.", "Ular hozir o‘ynayapti."]),
            LISTEN("My mum is cooking.", "Onam ovqat pishiryapti.",
                   ["Onam ovqat pishiradi.", "Otam ovqat pishiryapti.", "Onam non yeyapti."]),
            Q("To‘g‘ri gapni tanlang", "He is riding a bike.",
              ["He riding a bike.", "He is rideing a bike.", "He are riding a bike."],
              x="is + riding (ride → riding, e tushadi)."),
            SENT("My sister is drawing a picture", x="My sister is drawing a picture. — Opam rasm chizyapti."),
            TFE("“They is dancing.” — to‘g‘ri gap.", False, say="They is dancing.",
                x="they bilan are: They are dancing."),
            TFE("“The cat is sitting on the chair.” — to‘g‘ri gap.", True, say="The cat is sitting on the chair.",
                x="To‘g‘ri: is + sitting."),
            FORM("swim", "fe’lining -ing shakli", "swimming", ["swiming", "swimeing", "swimmng"], d=2,
                 x="Qisqa fe’lda oxirgi undosh ikkilanadi: swimming."),
            FORM("run", "fe’lining -ing shakli", "running", ["runing", "runeing", "runns"], d=2,
                 x="Oxirgi undosh ikkilanadi: running."),
            FORM("dance", "fe’lining -ing shakli", "dancing", ["danceing", "dancking", "dancng"], d=2,
                 x="Oxirgi e tushadi: dancing."),
            EN("Inkor shaklini tanlang: She is singing.", "She isn't singing.",
               ["She doesn't singing.", "She not singing.", "She isn't sing."], say="She is singing.", d=2,
               x="is + not = isn't: She isn't singing."),
            EN("Savol shaklini tanlang: You are listening.", "Are you listening?",
               ["Do you listening?", "You are listening?", "Are you listen?"], say="You are listening.", d=2,
               x="are oldinga chiqadi: Are you listening?"),
            GAP("Is it raining? — No, it ...", "isn't", ["doesn't", "aren't", "not"], d=2,
                x="Is …? savoliga qisqa javob: No, it isn't."),
            GAP("What ... you doing? — I'm drawing.", "are", ["is", "do", "does"], d=2,
                x="you bilan are: What are you doing?"),
            Q("Qaysi gap hozir bo‘layotgan ish haqida?", "I am doing my homework now.",
              ["I do my homework every day.", "I often do my homework.", "I usually do my homework."], d=2,
              x="now — hozir: am doing (Present Continuous)."),
            SENT("The boys are swimming in the river", d=2, x="The boys are swimming in the river. — Bolalar daryoda suzishyapti."),
            FORM("sit", "fe’lining -ing shakli", "sitting", ["siting", "siteing", "sits"], d=3,
                 x="Oxirgi undosh ikkilanadi: sitting."),
            GAP("Every day she ... to school.", "walks", ["is walking", "walking", "walk"], d=3,
                x="every day — odatiy ish, Present Simple: she walks."),
            GAP("Look! The children ... in the park.", "are running", ["run", "runs", "is running"], d=3,
                x="Look! — hozir bo‘lyapti; children — ko‘plik: are running."),
            GAP("Listen! Someone ... the piano.", "is playing", ["plays", "play", "are playing"], d=3,
                x="Listen! — hozir; someone — birlik: is playing."),
            QSENT("What are you doing now", d=3, x="What are you doing now? — Hozir nima qilyapsan?"),
        ])

T.topic("actions", "🤸", L("Harakatlar", "Actions", "Действия"),
        chapter=C2, gen="vocab",
        theory="Harakat fe’llari: run — yugurmoq, walk — yurmoq, swim — suzmoq, dance — raqsga tushmoq,\n"
               "climb — tirmashib chiqmoq, ride — minmoq (velosiped, ot), write — yozmoq, sleep — uxlamoq.\n"
               "Hozir bo‘layotgan harakat: He is running. They are dancing.\n"
               "Odatiy harakat: I swim every Sunday.  Savol: What is he doing? — He is climbing.",
        levels=vocab_levels(["actions"], special=True))

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["present_simple", "routine_time", "present_continuous", "actions"], chapter=C2)

# ============================================================ 3-chorak
T.topic("jobs_places", "🏥", L("Kasblar va shahardagi joylar", "Jobs and places in town", "Профессии и места в городе"),
        chapter=C3, gen="vocab",
        theory="Kasblar: doctor — shifokor, teacher — o‘qituvchi, cook — oshpaz, farmer — fermer, pilot — uchuvchi,\n"
               "builder — quruvchi, firefighter — o‘t o‘chiruvchi, police officer — politsiyachi.\n"
               "Joylar: hospital — kasalxona, shop — do‘kon, bank — bank, stadium — stadion, bridge — ko‘prik.\n"
               "Misol: A doctor works in a hospital. What does your mum do? — She is a teacher.\n"
               "Kasb oldidan a / an: a pilot, an artist.",
        levels=vocab_levels(["jobs_places"]))

T.topic("there_is", "🏙️", L("There is / There are, some / any", "There is / There are, some / any",
                            "There is / There are, some / any"),
        chapter=C3, prereq=["plurals"],
        theory="There is + birlik: There is a park near my house.  There are + ko‘plik: There are two shops.\n"
               "Inkor: There isn't a cinema. There aren't any trees. Savol: Is there a bank? Are there any shops?\n"
               "some — darak gapda, any — inkor va savolda: There is some milk. Is there any juice?\n"
               "Sanaladigan otlar (apple, egg) bilan — How many? Sanalmaydigan (milk, water, bread) bilan — How much?\n"
               "Sanalmaydigan otlarga -s qo‘shilmaydi: water (waters emas), bread (breads emas).",
        items=[
            GAP("There ... a big park in our town.", "is", ["are", "am", "be"], x="Bitta park — There is."),
            GAP("There ... three bedrooms in my flat.", "are", ["is", "am", "be"], x="Uchta xona — There are."),
            GAP("How ... eggs do we need?", "many", ["much", "any", "some"],
                x="eggs sanaladi, shuning uchun How many?"),
            GAP("There are many ... in the zoo.", "animals", ["animal", "an animal", "animales"],
                x="many dan keyin ko‘plik: animals."),
            Q("Qaysi ot sanalmaydi?", "milk", ["apple", "egg", "banana"],
              x="milk (sut) — sanalmaydi; olma, tuxum, bananni sanash mumkin."),
            LISTEN("There is a lamp on the table.", "Stol ustida chiroq bor.",
                   ["Stol ustida chiroqlar bor.", "Stol tagida chiroq bor.", "Stol ustida chiroq yo‘q."]),
            Q("To‘g‘ri gapni tanlang", "There is a bank nearby.",
              ["There are a bank nearby.", "There is bank nearby.", "There is a banks nearby."],
              x="Bitta bank — There is a bank."),
            MATCH("Joy nomini tarjimasi bilan juftlang",
                  [("hospital", "kasalxona"), ("library", "kutubxona"), ("post office", "pochta"),
                   ("cinema", "kinoteatr"), ("museum", "muzey"), ("bakery", "novvoyxona"), ("pharmacy", "dorixona")],
                  lang="en"),
            Q("Qayerda kitob olib o‘qiymiz?", "in the library", ["in the bakery", "in the hospital", "in the bank"],
              x="library — kutubxona."),
            Q("Qayerda film ko‘ramiz?", "at the cinema", ["at the pharmacy", "at the post office", "at the bakery"],
              x="cinema — kinoteatr."),
            TFE("“There are a cat under the bed.” — to‘g‘ri gap.", False, say="There are a cat under the bed.",
                x="Bitta mushuk — There is a cat under the bed."),
            TFE("“water” — sanalmaydigan ot.", True, say="water", x="To‘g‘ri: water sanalmaydi (How much water?)."),
            GAP("There ... a lot of books in the library.", "are", ["is", "am", "be"], d=2,
                x="books — ko‘plik: There are."),
            GAP("There ... some milk in the fridge.", "is", ["are", "am", "be"], d=2,
                x="milk sanalmaydi, shuning uchun There is some milk."),
            GAP("Is there ... juice in the bottle?", "any", ["many", "an", "a lot"], d=2,
                x="Savolda sanalmaydigan ot bilan — any: Is there any juice?"),
            GAP("There aren't ... apples in the bag.", "any", ["some", "much", "a"], d=2,
                x="Inkor gapda — any: There aren't any apples."),
            GAP("I have got ... sweets. Do you want one?", "some", ["any", "much", "a"], d=2,
                x="Darak gapda — some: I have got some sweets."),
            GAP("How ... water do you drink every day?", "much", ["many", "any", "some"], d=2,
                x="water sanalmaydi, shuning uchun How much?"),
            Q("Qaysi ot sanalmaydi?", "bread", ["sandwich", "carrot", "orange"], d=2,
              x="bread (non) — sanalmaydi: some bread, a loaf of bread."),
            Q("Qaysi ot sanaladi?", "cup", ["water", "sugar", "rice"], d=2,
              x="cup — sanaladi: one cup, two cups."),
            LISTEN("There isn't a cinema in our town.", "Shahrimizda kinoteatr yo‘q.",
                   ["Shahrimizda kinoteatr bor.", "Shahrimizda ikkita kinoteatr bor.", "Shahrimizda kutubxona yo‘q."],
                   d=2),
            SENT("There is a tree in our garden", d=2, x="There is a tree in our garden. — Bog‘imizda daraxt bor."),
            QSENT("Is there a zoo in your city", d=2, x="Is there a zoo in your city? — Shahringizda hayvonot bog‘i bormi?"),
            EN("Savol shaklini tanlang: There are some shops here.", "Are there any shops here?",
               ["Is there any shops here?", "Are there some shop here?", "There are any shops here?"],
               say="There are some shops here.", d=3, x="Savolda are oldinga chiqadi, some → any."),
            Q("To‘g‘ri gapni tanlang", "There isn't much sugar.",
              ["There isn't many sugar.", "There aren't much sugar.", "There isn't many sugars."], d=3,
              x="sugar sanalmaydi: There isn't much sugar."),
            SENT("There are two shops in this street", d=3, x="There are two shops in this street. — Bu ko‘chada ikkita do‘kon bor."),
        ])

T.topic("can_must", "🚦", L("can va must", "can and must", "can и must"),
        chapter=C3,
        theory="can — qila olmoq (qobiliyat) yoki mumkin (ruxsat): I can swim. Can I open the window?\n"
               "can't — qila olmaslik yoki mumkin emas: You can't play football in the classroom.\n"
               "must — shart, kerak (qoida): You must wear a seat belt.\n"
               "mustn't — mumkin emas, taqiqlangan: You mustn't run in the corridor.\n"
               "can va must dan keyin fe’l o‘zgarmaydi: She must go. (She must goes, must to go — xato.)",
        items=[
            GAP("Birds ... fly.", "can", ["can't", "must", "mustn't"], x="Qushlar ucha oladi: Birds can fly."),
            GAP("Fish ... walk.", "can't", ["can", "must", "is"], x="Baliqlar yura olmaydi: Fish can't walk."),
            GAP("You ... cross the road at a red light.", "mustn't", ["must", "can", "are"],
                x="Qizil chiroqda yo‘lni kesib o‘tish mumkin emas — mustn't."),
            GAP("You ... wash your hands before meals.", "must", ["mustn't", "can't", "don't"],
                x="Ovqatdan oldin qo‘l yuvish shart — must."),
            GAP("You ... talk loudly in the library.", "mustn't", ["must", "can", "have"],
                x="Kutubxonada baland gapirish mumkin emas — mustn't."),
            LISTEN("I can play the guitar.", "Men gitara chala olaman.",
                   ["Men gitara chala olmayman.", "Men gitara chalishim kerak.", "U gitara chala oladi."]),
            Q("To‘g‘ri gapni tanlang", "She can speak English.",
              ["She cans speak English.", "She can speaks English.", "She can to speak English."],
              x="can dan keyin fe’l o‘zgarmaydi, to ham qo‘yilmaydi."),
            FORM("must", "so‘zining ma’nosi", "kerak (shart)", ["qila olmoq", "yoqtirmoq", "xohlamoq"],
                 x="must — kerak, shart (qoida)."),
            SENT("You must wear a helmet", x="You must wear a helmet. — Dubulg‘a kiyishingiz shart."),
            TFE("“He must goes home.” — to‘g‘ri gap.", False, say="He must goes home.",
                x="must dan keyin fe’l -s siz: He must go home."),
            TFE("“Penguins can fly.” — to‘g‘ri fikr.", False, say="Penguins can fly.",
                x="Pingvinlar ucha olmaydi, lekin juda yaxshi suzadi."),
            TFE("“You must brush your teeth every day.” — to‘g‘ri maslahat.", True,
                say="You must brush your teeth every day.", x="To‘g‘ri: tishni har kuni yuvish kerak."),
            GAP("... I open the window? — Yes, of course.", "Can", ["Must", "Do", "Am"], d=2,
                x="Ruxsat so‘rash: Can I open the window?"),
            LISTEN("You must do your homework.", "Sen uy vazifangni bajarishing kerak.",
                   ["Sen uy vazifangni bajara olasan.", "Uy vazifasini bajarmaslik kerak.",
                    "Men uy vazifamni bajarishim kerak."], d=2),
            Q("To‘g‘ri gapni tanlang", "We must help our parents.",
              ["We must to help our parents.", "We musts help our parents.", "We must helping our parents."], d=2,
              x="must + fe’l (to siz, -ing siz): We must help."),
            FORM("mustn't", "so‘zining ma’nosi", "mumkin emas (taqiq)", ["kerak", "qila oladi", "shart emas"], d=2,
                 x="mustn't — mumkin emas, taqiqlangan."),
            GAP("Can you ski? — No, I ...", "can't", ["mustn't", "don't", "am not"], d=2,
                x="Can …? savoliga qisqa javob: No, I can't."),
            GAP("Can your sister swim? — Yes, she ...", "can", ["does", "is", "must"], d=2,
                x="Can …? savoliga qisqa javob: Yes, she can."),
            GAP("It's cold. You ... wear a warm coat.", "must", ["mustn't", "can't", "aren't"], d=2,
                x="Sovuqda issiq kiyinish kerak — must."),
            GAP("A cheetah ... run very fast.", "can", ["can't", "must", "mustn't"], d=2,
                x="Gepard juda tez yugura oladi — can."),
            GAP("My baby brother is one year old. He ... read.", "can't", ["can", "must", "mustn't"], d=2,
                x="Bir yoshli bola o‘qiy olmaydi — can't."),
            SENT("My grandfather can speak three languages", d=2,
                 x="My grandfather can speak three languages. — Bobom uch tilda gapira oladi."),
            SENT("We mustn't eat in the classroom", d=2, x="We mustn't eat in the classroom. — Sinfda ovqat yeyish mumkin emas."),
            Q("Qaysi gap ruxsat so‘rash?", "Can I use your pencil?",
              ["I can use a pencil.", "You must use a pencil.", "You mustn't use a pencil."], d=3,
              x="Ruxsat so‘rash: Can I …?"),
            QSENT("Can you help me, please", d=3, x="Can you help me, please? — Menga yordam bera olasizmi?"),
        ])

T.topic("months_weather", "🌦️", L("Oylar, fasllar va ob-havo", "Months, seasons and weather", "Месяцы, времена года, погода"),
        chapter=C3,
        theory="Fasllar: spring — bahor, summer — yoz, autumn — kuz, winter — qish.\n"
               "Oylar (doim bosh harf bilan): January, February, March, April, May, June, July, August,\n"
               "September, October, November, December.  Oy va fasl oldidan in: in May, in summer.\n"
               "What's the weather like? — It's sunny / rainy / cloudy / windy / snowy / hot / cold / warm.\n"
               "Misol: In winter it's cold and snowy. My birthday is in April.",
        items=[
            Q("“Bahor” inglizcha qanday?", "spring", ["summer", "autumn", "winter"], x="spring — bahor."),
            Q("“Kuz” inglizcha qanday?", "autumn", ["spring", "winter", "summer"], x="autumn — kuz."),
            FORM("winter", "so‘zining tarjimasi", "qish", ["yoz", "kuz", "bahor"], x="winter — qish."),
            Q("Yilning birinchi oyi qaysi?", "January", ["June", "December", "March"], x="January — yanvar, birinchi oy."),
            Q("Yilning oxirgi oyi qaysi?", "December", ["November", "January", "October"],
              x="December — dekabr, o‘n ikkinchi oy."),
            EN("Qaysi oy tushib qolgan? March, ..., May", "April", ["August", "June", "February"],
               say="March, ..., May", x="March, April, May."),
            EN("Qaysi oy tushib qolgan? June, ..., August", "July", ["January", "May", "September"],
               say="June, ..., August", x="June, July, August."),
            Q("Yilda nechta oy bor?", "twelve", ["ten", "seven", "twenty"], x="Yilda twelve (12) oy bor."),
            MATCH("Ob-havo so‘zini tarjimasi bilan juftlang",
                  [("sunny", "quyoshli"), ("rainy", "yomg‘irli"), ("cloudy", "bulutli"), ("windy", "shamolli"),
                   ("snowy", "qorli"), ("hot", "issiq"), ("cold", "sovuq")], lang="en"),
            Q("Rasmga mos ob-havoni tanlang", "It's rainy.", ["It's sunny.", "It's snowy.", "It's windy."],
              e="🌧️", x="Yomg‘ir — rainy."),
            Q("Rasmga mos ob-havoni tanlang", "It's sunny.", ["It's rainy.", "It's cloudy.", "It's snowy."],
              e="☀️", x="Quyosh — sunny."),
            Q("Rasmga mos ob-havoni tanlang", "It's snowy.", ["It's sunny.", "It's hot.", "It's rainy."],
              e="❄️", x="Qor — snowy."),
            Q("O‘zbekistonda qaysi faslda eng issiq bo‘ladi?", "summer", ["winter", "autumn", "spring"],
              x="Eng issiq fasl — yoz (summer)."),
            Q("Navro‘z bayrami qaysi oyda nishonlanadi?", "March", ["May", "January", "September"],
              x="Navro‘z — 21-mart: March."),
            TF("Oylar nomi kichik harf bilan yoziladi: may, june.", False,
               x="Oylar doim bosh harf bilan yoziladi: May, June."),
            TFE("“autumn” — kuz degani.", True, say="autumn", x="To‘g‘ri: autumn — kuz."),
            SENT("My birthday is in March", x="My birthday is in March. — Mening tug‘ilgan kunim martda."),
            EN("Qaysi oy tushib qolgan? September, ..., November", "October", ["August", "December", "April"],
               say="September, ..., November", d=2, x="September, October, November."),
            Q("O‘zbekistonda yanvar qaysi faslga kiradi?", "winter", ["summer", "spring", "autumn"], d=2,
              x="Yanvar — qish oyi (winter)."),
            EN("Qaysi fasl oylari: December, January, February? (O‘zbekistonda)", "winter",
               ["autumn", "spring", "summer"], say="December, January, February", d=2,
               x="Dekabr, yanvar, fevral — qish (winter)."),
            Q("Qaysi oy bahorga kirmaydi? (O‘zbekistonda)", "July", ["March", "April", "May"], d=2,
              x="Bahor: March, April, May. July — yoz oyi."),
            GAP("My birthday is ... October.", "in", ["on", "at", "of"], d=2, x="Oy oldidan in: in October."),
            LISTEN("It's windy and cold today.", "Bugun shamol bor va sovuq.",
                   ["Bugun quyoshli va issiq.", "Bugun yomg‘ir yog‘yapti.", "Kecha shamol bo‘ldi."], d=2),
            EN("“What's the weather like?” savoliga mos javobni tanlang", "It's cloudy.",
               ["It's Monday.", "It's May.", "It's five o'clock."], say="What's the weather like?", d=2,
               x="Ob-havo so‘ralgan: It's cloudy. — Havo bulutli."),
            SENT("It is hot and sunny in summer", d=2, x="It is hot and sunny in summer. — Yozda issiq va quyoshli."),
            Q("Qaysi so‘z to‘g‘ri yozilgan?", "February", ["Febuary", "Februar", "february"], d=3,
              x="February — r harfi ikki joyda; oy nomi bosh harf bilan."),
            QSENT("What is the weather like today", d=3, x="What is the weather like today? — Bugun havo qanday?"),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["jobs_places", "there_is", "can_must", "months_weather"], chapter=C3)

# ============================================================ 4-chorak
T.topic("past", "🕰️", L("Past Simple: was / were, went, saw", "Past Simple: was / were and verbs",
                       "Past Simple: was / were и глаголы"),
        chapter=C4, prereq=["to_be", "present_simple"],
        theory="to be o‘tgan zamonda: I / he / she / it was; we / you / they were. I was at home yesterday.\n"
               "To‘g‘ri fe’llar -ed oladi: play → played, watch → watched, like → liked, stop → stopped.\n"
               "Noto‘g‘ri fe’llarni yodlash kerak: go → went, see → saw, have → had, eat → ate, do → did,\n"
               "come → came, buy → bought.  Inkor va savol: did + fe’lning oddiy shakli — I didn't go. Did you see it?\n"
               "Kalit so‘zlar: yesterday, last week, last summer, two days ago.",
        items=[
            GAP("I ... at home yesterday.", "was", ["were", "am", "is"], x="yesterday — o‘tgan zamon; I bilan was."),
            GAP("They ... at the zoo last Sunday.", "were", ["was", "are", "is"], x="they bilan were."),
            GAP("She ... ill last week.", "was", ["were", "is", "be"], x="she bilan was."),
            GAP("We ... happy yesterday.", "were", ["was", "are", "be"], x="we bilan were."),
            FORM("go", "fe’lining o‘tgan zamon shakli", "went", ["goed", "gone", "goes"], x="Noto‘g‘ri fe’l: go → went."),
            FORM("see", "fe’lining o‘tgan zamon shakli", "saw", ["seed", "seen", "sees"], x="Noto‘g‘ri fe’l: see → saw."),
            FORM("eat", "fe’lining o‘tgan zamon shakli", "ate", ["eated", "eaten", "eats"], x="Noto‘g‘ri fe’l: eat → ate."),
            FORM("have", "fe’lining o‘tgan zamon shakli", "had", ["haved", "has", "hads"],
                 x="Noto‘g‘ri fe’l: have → had."),
            FORM("play", "fe’lining o‘tgan zamon shakli", "played", ["plaied", "plays", "playd"],
                 x="To‘g‘ri fe’l: play → played."),
            FORM("watch", "fe’lining o‘tgan zamon shakli", "watched", ["watchd", "watches", "wotch"],
                 x="To‘g‘ri fe’l: watch → watched."),
            LISTEN("Yesterday I went to the park.", "Kecha men bog‘ga bordim.",
                   ["Bugun men bog‘ga boraman.", "Kecha u bog‘ga bordi.", "Kecha men maktabga bordim."]),
            LISTEN("We watched a cartoon.", "Biz multfilm ko‘rdik.",
                   ["Biz multfilm ko‘ryapmiz.", "Ular multfilm ko‘rdi.", "Biz kitob o‘qidik."]),
            Q("Qaysi so‘z o‘tgan zamonni bildiradi?", "yesterday", ["tomorrow", "now", "every day"],
              x="yesterday — kecha (o‘tgan zamon)."),
            SENT("I was in Bukhara last summer", x="I was in Bukhara last summer. — O‘tgan yozda Buxoroda edim."),
            TFE("“He goed to school.” — to‘g‘ri gap.", False, say="He goed to school.",
                x="go — noto‘g‘ri fe’l: He went to school."),
            TFE("“They were in the garden.” — to‘g‘ri gap.", True, say="They were in the garden.",
                x="To‘g‘ri: they bilan were."),
            MATCH("Fe’lni o‘tgan zamon shakli bilan juftlang",
                  [("go", "went"), ("see", "saw"), ("have", "had"), ("eat", "ate"), ("do", "did"), ("come", "came"),
                   ("buy", "bought")], d=2, lang="en"),
            GAP("Last summer we ... to Samarkand.", "went", ["go", "goes", "going"], d=2,
                x="last summer — o‘tgan zamon: went."),
            GAP("I ... a big elephant at the zoo yesterday.", "saw", ["see", "sees", "seeing"], d=2,
                x="yesterday — o‘tgan zamon: see → saw."),
            GAP("... you play football yesterday?", "Did", ["Do", "Were", "Does"], d=2,
                x="O‘tgan zamonda savol: Did you play …?"),
            GAP("Did you like the film? — Yes, I ...", "did", ["do", "was", "liked"], d=2,
                x="Did …? savoliga qisqa javob: Yes, I did."),
            Q("To‘g‘ri gapni tanlang", "We visited our grandparents last week.",
              ["We visit our grandparents last week.", "We visitted our grandparents last week.",
               "We visiting our grandparents last week."], d=2,
              x="last week — o‘tgan zamon: visit → visited."),
            SENT("My mother bought a new dress", d=2, x="My mother bought a new dress. — Onam yangi ko‘ylak sotib oldi."),
            GAP("I didn't ... my homework.", "do", ["did", "does", "done"], d=3,
                x="didn't dan keyin fe’lning oddiy shakli: didn't do."),
            GAP("Were you at school yesterday? — No, I ...", "wasn't", ["weren't", "didn't", "don't"], d=3,
                x="I bilan was: No, I wasn't."),
            Q("To‘g‘ri gapni tanlang", "She didn't go to the party.",
              ["She didn't went to the party.", "She not went to the party.", "She doesn't went to the party."], d=3,
              x="didn't + fe’lning oddiy shakli: didn't go."),
            FORM("stop", "fe’lining o‘tgan zamon shakli", "stopped", ["stoped", "stopt", "stops"], d=3,
                 x="Qisqa fe’lda oxirgi undosh ikkilanadi: stopped."),
            QSENT("Did you have a good weekend", d=3, x="Did you have a good weekend? — Dam olish kunlaring yaxshi o‘tdimi?"),
        ])

T.topic("opposites", "↔️", L("Qarama-qarshi sifatlar", "Opposite adjectives", "Противоположные прилагательные"),
        chapter=C4, gen="opposites",
        theory="Qarama-qarshi sifatlar: big — small, long — short, hot — cold, fast — slow,\n"
               "old — young, happy — sad, loud — quiet, open — closed.\n"
               "Sifat otdan oldin keladi: a fast car, a small house. Yoki to be dan keyin: The soup is hot.\n"
               "Keyingi mavzuda sifatlarni taqqoslaymiz: big → bigger → the biggest.",
        levels=[{"modes": ["size", "length", "read"], "options": 3},
                {"modes": ["read", "listen"], "options": 3},
                {"modes": ["read", "listen"], "options": 4}])

T.topic("comparatives", "📏", L("Sifat darajalari: bigger, the biggest", "Comparatives and superlatives",
                               "Степени сравнения прилагательных"),
        chapter=C4, prereq=["opposites"],
        theory="Qisqa sifatlar: -er (qiyosiy daraja), the …-est (orttirma daraja): tall → taller → the tallest.\n"
               "e bilan tugasa: nice → nicer → the nicest. Undosh ikkilanadi: big → bigger → the biggest, hot → hotter.\n"
               "Undosh + y → -ier / -iest: happy → happier → the happiest, easy → easier.\n"
               "Uzun sifatlar — more / the most: beautiful → more beautiful → the most beautiful.\n"
               "Maxsus: good → better → the best; bad → worse → the worst.\n"
               "Taqqoslashda than: An elephant is bigger than a horse.",
        items=[
            FORM("tall", "sifatining qiyosiy darajasi", "taller", ["tallest", "more tall", "taler"],
                 x="Qisqa sifat + -er: taller."),
            FORM("small", "sifatining qiyosiy darajasi", "smaller", ["smallest", "more small", "smaler"],
                 x="Qisqa sifat + -er: smaller."),
            FORM("old", "sifatining qiyosiy darajasi", "older", ["oldest", "more old", "olded"],
                 x="Qisqa sifat + -er: older."),
            FORM("good", "sifatining qiyosiy darajasi", "better", ["gooder", "more good", "best"],
                 x="Maxsus shakl: good → better → the best."),
            FORM("long", "sifatining orttirma darajasi", "the longest", ["the longer", "the most long", "longest the"],
                 x="the + sifat + -est: the longest."),
            FORM("cold", "sifatining orttirma darajasi", "the coldest", ["the colder", "the most cold", "coldest the"],
                 x="the + sifat + -est: the coldest."),
            GAP("An elephant is ... than a dog.", "bigger", ["big", "biggest", "more big"],
                x="Taqqoslash + than: bigger than (g ikkilanadi)."),
            GAP("A car is ... than a bicycle.", "faster", ["fast", "fastest", "more fast"],
                x="Taqqoslash + than: faster than."),
            GAP("A mouse is ... than a cat.", "smaller", ["small", "smallest", "more small"],
                x="Taqqoslash + than: smaller than."),
            Q("Qaysi gap to‘g‘ri?", "Horses are faster than snails.",
              ["Snails are faster than horses.", "Horses are slower than snails.", "Snails are bigger than horses."],
              x="Ot shilliqqurtdan tezroq: Horses are faster than snails."),
            TFE("“Anvar is more tall than Rustam.” — to‘g‘ri gap.", False, say="Anvar is more tall than Rustam.",
                x="tall — qisqa sifat: Anvar is taller than Rustam."),
            FORM("big", "sifatining qiyosiy darajasi", "bigger", ["biger", "more big", "biggest"], d=2,
                 x="Unli + undosh bilan tugagan qisqa sifatda undosh ikkilanadi: bigger."),
            FORM("bad", "sifatining orttirma darajasi", "the worst", ["the baddest", "the most bad", "the worse"], d=2,
                 x="Maxsus shakl: bad → worse → the worst."),
            FORM("happy", "sifatining qiyosiy darajasi", "happier", ["happyer", "happyier", "happiest"], d=2,
                 x="Undosh + y → -ier: happier."),
            FORM("beautiful", "sifatining qiyosiy darajasi", "more beautiful",
                 ["beautifuler", "beautifullest", "most beautifuler"], d=2,
                 x="Uzun sifat — more: more beautiful."),
            FORM("good", "sifatining orttirma darajasi", "the best", ["the goodest", "the better", "the most good"], d=2,
                 x="Maxsus shakl: good → better → the best."),
            GAP("The giraffe is ... animal in the world.", "the tallest", ["the taller", "tallest", "the most tall"], d=2,
                x="Eng baland — orttirma daraja: the tallest. Jirafa — dunyodagi eng baland hayvon."),
            GAP("My brother is older ... me.", "than", ["then", "that", "as"], d=2,
                x="Taqqoslashda than ishlatiladi: older than me."),
            GAP("Summer is ... than winter.", "hotter", ["hoter", "hot", "more hot"], d=2,
                x="hot → hotter (t ikkilanadi)."),
            Q("To‘g‘ri gapni tanlang", "Tashkent is bigger than Bukhara.",
              ["Tashkent is biger than Bukhara.", "Tashkent is more big than Bukhara.",
               "Tashkent is bigger that Bukhara."], d=2, x="big → bigger + than."),
            Q("Qaysi gap to‘g‘ri? (fakt)", "Elephants are heavier than mice.",
              ["Mice are heavier than elephants.", "Elephants are smaller than mice.", "Mice are bigger than elephants."],
              d=2, x="Fil sichqondan ancha og‘ir va katta: heavy → heavier."),
            MATCH("Sifatni qiyosiy darajasi bilan juftlang",
                  [("old", "older"), ("long", "longer"), ("big", "bigger"), ("happy", "happier"), ("good", "better"),
                   ("bad", "worse"), ("nice", "nicer")], d=2, lang="en"),
            LISTEN("My cat is smaller than my dog.", "Mushugim itimdan kichikroq.",
                   ["Itim mushugimdan kichikroq.", "Mushugim eng kichigi.", "Mushugim itimdan kattaroq."], d=2),
            SENT("A lion is stronger than a cat", d=2, x="A lion is stronger than a cat. — Sher mushukdan kuchliroq."),
            GAP("This is ... day of my life!", "the happiest", ["the happyest", "happier", "the happier"], d=3,
                x="Eng baxtli — the happiest (y → i + est)."),
            FORM("expensive", "sifatining qiyosiy darajasi", "more expensive",
                 ["expensiver", "expensivest", "most expensiver"], d=3, x="Uzun sifat — more: more expensive."),
            Q("To‘g‘ri gapni tanlang", "Gold is more expensive than silver.",
              ["Gold is expensiver than silver.", "Gold is more expensive that silver.",
               "Gold is most expensive than silver."], d=3,
              x="Uzun sifat: more expensive than. Oltin kumushdan qimmat."),
            SENT("Winter is the coldest season", d=3, x="Winter is the coldest season. — Qish — eng sovuq fasl."),
            SENT("My bag is heavier than your bag", d=3, x="My bag is heavier than your bag. — Sumkam sening sumkangdan og‘irroq."),
        ])

R1 = ("My name is Aziz. I am eleven years old. I live in Samarkand with my family. "
      "I have got a sister. Her name is Nigora and she is seven. "
      "We have got a cat. Its name is Momiq. It is white and very funny. I love my family!")
R2 = ("Lola is a pupil. Every day she gets up at seven o'clock. She washes her face and has breakfast. "
      "She goes to school at eight. Her lessons finish at one o'clock. In the afternoon she does her homework. "
      "In the evening she reads books or plays with her little brother. She goes to bed at half past nine.")
R3 = ("It is Sunday. The weather is warm and sunny. Bekzod and his family are in the park. "
      "His father is reading a newspaper. His mother is taking photos. "
      "Bekzod and his little sister are feeding the ducks. Some boys are playing football near the lake. "
      "Everyone is happy.")
R4 = ("Last summer Dilnoza visited her grandparents in a village. Their house was near a river. "
      "Every morning she helped her grandmother in the garden. She saw cows, sheep and a lot of chickens. "
      "In the afternoon she played with her cousins near the river. "
      "In the evening they ate fresh fruit and watched the stars. It was a wonderful holiday.")
R5 = ("Kamol and Sherzod are best friends. Kamol is twelve and Sherzod is eleven, so Kamol is older. "
      "Sherzod is taller than Kamol, but Kamol is faster. They both love sport. "
      "Kamol's favourite sport is football, and Sherzod's favourite sport is basketball. "
      "On Saturdays they go to the sports centre together.")
R6 = ("There is a small shop near my house. In the shop there is bread, milk and cheese. "
      "There are also a lot of vegetables and fruit. The shop opens at eight o'clock in the morning. "
      "I often buy bread there for my family.")

T.topic("reading", "📖", L("O‘qib tushunish", "Reading", "Чтение"),
        chapter=C4,
        theory="Matnni o‘qishdan oldin savolga qarang — nimani izlash kerakligini bilib olasiz.\n"
               "Keyin matnni diqqat bilan o‘qing va javobni matndan toping.\n"
               "Savol so‘ziga e’tibor bering: Who? — kim, Where? — qayerda, When? — qachon, What? — nima.\n"
               "True / False: fikr matnga mos kelsa — To‘g‘ri, mos kelmasa — Noto‘g‘ri.",
        items=[
            READ(R1, "How old is Aziz?", "eleven", ["seven", "ten", "twelve"], x="Matnda: I am eleven years old."),
            READ(R1, "Where does Aziz live?", "in Samarkand", ["in Tashkent", "in Bukhara", "in Khiva"],
                 x="Matnda: I live in Samarkand."),
            READ(R1, "Who is Nigora?", "Aziz's sister", ["Aziz's mother", "Aziz's cat", "Aziz's friend"],
                 x="Matnda: I have got a sister. Her name is Nigora."),
            RTF(R1, "The cat is black.", False, x="Matnda: It is white — mushuk oq."),
            RTF(R1, "Nigora is seven years old.", True, x="Matnda: she is seven."),
            READ(R2, "When does Lola get up?", "at seven o'clock",
                 ["at eight o'clock", "at one o'clock", "at half past nine"],
                 x="Matnda: she gets up at seven o'clock."),
            RTF(R2, "Lola goes to school at eight.", True, x="Matnda: She goes to school at eight."),
            READ(R3, "What is the weather like?", "warm and sunny", ["cold and rainy", "windy and cloudy", "cold and snowy"],
                 x="Matnda: The weather is warm and sunny."),
            READ(R6, "Where is the shop?", "near my house", ["near my school", "in the park", "next to the zoo"],
                 x="Matnda: There is a small shop near my house."),
            READ(R6, "When does the shop open?", "at eight o'clock", ["at seven o'clock", "at nine o'clock", "at ten o'clock"],
                 x="Matnda: The shop opens at eight o'clock."),
            RTF(R6, "The shop is very big.", False, x="Matnda: a small shop — kichik do‘kon."),
            READ(R2, "What does Lola do in the afternoon?", "She does her homework.",
                 ["She goes to bed.", "She has breakfast.", "She goes to school."], d=2,
                 x="Matnda: In the afternoon she does her homework."),
            RTF(R2, "Lola goes to bed at nine o'clock.", False, d=2,
                x="Matnda: at half past nine — soat 9:30 da."),
            READ(R3, "What is Bekzod's father doing?", "He is reading a newspaper.",
                 ["He is taking photos.", "He is playing football.", "He is feeding the ducks."], d=2,
                 x="Matnda: His father is reading a newspaper."),
            READ(R3, "Who is taking photos?", "Bekzod's mother", ["Bekzod's father", "Bekzod's sister", "Some boys"], d=2,
                 x="Matnda: His mother is taking photos."),
            RTF(R3, "Bekzod is playing football.", False, d=2,
                x="Bekzod o‘rdaklarga yem beryapti; futbolni boshqa bolalar o‘ynayapti."),
            READ(R4, "Where did Dilnoza go last summer?", "to a village", ["to the sea", "to Tashkent", "to the mountains"],
                 d=2, x="Matnda: she visited her grandparents in a village."),
            READ(R4, "Where was the house?", "near a river", ["near a school", "in the city centre", "near the sea"], d=2,
                 x="Matnda: Their house was near a river."),
            RTF(R4, "Dilnoza saw cows and sheep.", True, d=2, x="Matnda: She saw cows, sheep and a lot of chickens."),
            RTF(R4, "The holiday was boring.", False, d=2, x="Matnda: It was a wonderful holiday — ajoyib ta’til."),
            READ(R5, "What is Sherzod's favourite sport?", "basketball", ["football", "tennis", "swimming"], d=2,
                 x="Matnda: Sherzod's favourite sport is basketball."),
            READ(R6, "What does the writer often buy there?", "bread", ["milk", "cheese", "fruit"], d=2,
                 x="Matnda: I often buy bread there."),
            READ(R4, "What did Dilnoza do every morning?", "She helped her grandmother.",
                 ["She played football.", "She watched TV.", "She went to school."], d=3,
                 x="Matnda: Every morning she helped her grandmother in the garden."),
            READ(R5, "Who is older?", "Kamol", ["Sherzod", "They are the same age.", "We don't know."], d=3,
                 x="Kamol 12 yoshda, Sherzod 11 yoshda — Kamol katta."),
            READ(R5, "Who is taller?", "Sherzod", ["Kamol", "They are the same height.", "We don't know."], d=3,
                 x="Matnda: Sherzod is taller than Kamol."),
            RTF(R5, "Kamol is faster than Sherzod.", True, d=3, x="Matnda: but Kamol is faster."),
            READ(R5, "When do they go to the sports centre?", "on Saturdays", ["on Sundays", "every day", "on Mondays"],
                 d=3, x="Matnda: On Saturdays they go to the sports centre together."),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["past", "opposites", "comparatives", "reading"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["to_be", "possessives", "plurals", "question_words", "present_simple", "routine_time", "present_continuous",
        "there_is", "can_must", "months_weather", "past", "comparatives", "reading"], chapter=C4, level=3)

T.write()
