"""Ingliz tili, 1-sinf: assets/data/school/english_g1.json + bank_english_g1.json.

1-sinf o‘quvchisi (7 yosh) endigina o‘qishni o‘rganyapti: o‘zbekcha ko‘rsatma ovozda o‘qib beriladi,
inglizcha so‘z va gaplar esa `say` orqali ingliz ovozida eshitiladi. Savollarning ko‘pchiligi — “tinglang va
rasmini toping” (javob — emoji) yoki “tinglang va tarjimasini toping” (javob — qisqa o‘zbekcha so‘z);
inglizcha so‘zni o‘qish talab qilinadigan savollar — asosan 2–3-darajada.
Mavzular: salomlashish, tanishuv, maktab buyumlari, sinfdagi buyruqlar, ranglar, sonlar 1–10, o‘yinchoqlar,
oila, tana a’zolari, kayfiyat, hayvonlar, mevalar va sabzavotlar. Hamma matn va savollar o‘zimizniki
(darslikdan ko‘chirilmagan). Imlo — britancha (colour). Emoji — faqat Android 9 da bor oddiylari.
Qayta yaratish: python3 tool/content/school/english_g1.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schoolkit import *  # noqa: E402,F403

T = Course("english", 1, L("Ingliz tili", "English", "Английский язык"))

C1 = "1-chorak. Salom, maktab!"
C2 = "2-chorak. Ranglar, sonlar va o‘yinchoqlar"
C3 = "3-chorak. Oilam, tanam va kayfiyatim"
C4 = "4-chorak. Hayvonlar, mevalar va sabzavotlar"

# ------------------------------------------------------------ lug‘at: so‘z → (rasm, o‘zbekcha)
# "orange*" — meva (apelsin); "orange" — rang. Ovozda yulduzcha aytilmaydi.
VOC = {
    # tanishuv
    "boy": ("👦", "o‘g‘il bola"), "girl": ("👧", "qiz bola"),
    # maktab buyumlari
    "pen": ("🖊️", "ruchka"), "pencil": ("✏️", "qalam"), "book": ("📕", "kitob"), "bag": ("🎒", "sumka"),
    "ruler": ("📏", "chizg‘ich"), "notebook": ("📓", "daftar"), "crayon": ("🖍️", "rangli qalam"),
    "scissors": ("✂️", "qaychi"), "school": ("🏫", "maktab"), "teacher": ("👩‍🏫", "o‘qituvchi"),
    "desk": (None, "parta"), "rubber": (None, "o‘chirg‘ich"),
    # buyruqlar
    "Stand up!": (None, "Turing!"), "Sit down!": (None, "O‘tiring!"),
    "Open your book!": ("📖", "Kitobingizni oching!"), "Close your book!": ("📕", "Kitobingizni yoping!"),
    "Listen!": ("👂", "Tinglang!"), "Look!": ("👀", "Qarang!"), "Be quiet!": ("🤫", "Jim bo‘ling!"),
    "Clap your hands!": ("👏", "Qarsak chaling!"), "Hands up!": ("🙌", "Qo‘llarni ko‘taring!"),
    # ranglar
    "red": ("❤️", "qizil"), "yellow": ("💛", "sariq"), "blue": ("💙", "ko‘k"), "green": ("💚", "yashil"),
    "orange": ("🧡", "to‘q sariq"), "purple": ("💜", "binafsha"), "pink": ("💗", "pushti"),
    "black": ("🖤", "qora"), "white": ("⚪", "oq"), "brown": (None, "jigarrang"),
    # o‘yinchoqlar
    "ball": ("⚽", "to‘p"), "car": ("🚗", "mashina"), "balloon": ("🎈", "havo shari"), "robot": ("🤖", "robot"),
    "drum": ("🥁", "baraban"), "train": ("🚂", "poyezd"), "plane": ("✈️", "samolyot"), "bike": ("🚲", "velosiped"),
    "boat": ("⛵", "qayiq"), "doll": (None, "qo‘g‘irchoq"), "teddy bear": (None, "ayiqcha"),
    "kite": (None, "varrak"), "toy": (None, "o‘yinchoq"),
    # oila
    "mother": ("👩", "ona"), "father": ("👨", "ota"), "sister": ("👧", "opa yoki singil"),
    "brother": ("👦", "aka yoki uka"), "baby": ("👶", "chaqaloq"), "grandmother": ("👵", "buvi"),
    "grandfather": ("👴", "bobo"), "family": ("👪", "oila"),
    "mum": ("👩", "ona"), "dad": ("👨", "ota"), "granny": ("👵", "buvi"), "grandpa": ("👴", "bobo"),
    # tana a’zolari
    "nose": ("👃", "burun"), "eyes": ("👀", "ko‘zlar"), "ear": ("👂", "quloq"), "mouth": ("👄", "og‘iz"),
    "hand": ("✋", "qo‘l"), "tongue": ("👅", "til"), "face": ("🙂", "yuz"),
    "head": (None, "bosh"), "hair": (None, "soch"), "legs": (None, "oyoqlar"),
    # kayfiyat
    "happy": ("😀", "xursand"), "sad": ("😢", "xafa"), "angry": ("😠", "jahli chiqqan"),
    "tired": ("😫", "charchagan"), "sleepy": ("😴", "uyqusi kelgan"), "fine": ("🙂", "yaxshi"),
    # uy va ferma hayvonlari
    "cat": ("🐱", "mushuk"), "dog": ("🐶", "it"), "rabbit": ("🐰", "quyon"), "fish": ("🐟", "baliq"),
    "bird": ("🐦", "qush"), "cow": ("🐮", "sigir"), "horse": ("🐴", "ot"), "sheep": ("🐑", "qo‘y"),
    "goat": ("🐐", "echki"), "hen": ("🐔", "tovuq"), "duck": ("🦆", "o‘rdak"), "mouse": ("🐭", "sichqon"),
    # hayvonot bog‘i
    "lion": ("🦁", "sher"), "tiger": ("🐯", "yo‘lbars"), "bear": ("🐻", "ayiq"), "monkey": ("🐵", "maymun"),
    "elephant": ("🐘", "fil"), "giraffe": ("🦒", "jirafa"), "zebra": ("🦓", "zebra"),
    "crocodile": ("🐊", "timsoh"), "snake": ("🐍", "ilon"), "frog": ("🐸", "qurbaqa"), "fox": ("🦊", "tulki"),
    "wolf": ("🐺", "bo‘ri"), "camel": ("🐫", "tuya"), "penguin": ("🐧", "pingvin"),
    # mevalar va sabzavotlar
    "apple": ("🍎", "olma"), "banana": ("🍌", "banan"), "orange*": ("🍊", "apelsin"), "pear": ("🍐", "nok"),
    "grapes": ("🍇", "uzum"), "lemon": ("🍋", "limon"), "cherry": ("🍒", "gilos"),
    "strawberry": ("🍓", "qulupnay"), "watermelon": ("🍉", "tarvuz"), "melon": ("🍈", "qovun"),
    "carrot": ("🥕", "sabzi"), "tomato": ("🍅", "pomidor"), "potato": ("🥔", "kartoshka"),
    "cucumber": ("🥒", "bodring"), "corn": ("🌽", "makkajo‘xori"),
}


# ------------------------------------------------------------ yordamchilar
def _w(k):
    """Lug‘at kaliti → inglizcha so‘z (ovoz va ekran uchun)."""
    return k.rstrip("*")


def _end(s):
    return s if s[-1] in ".!?" else s + "."


def _pic(k):
    em = VOC[k][0]
    assert em, f"{k}: rasm yo‘q"
    return em


def PIC(word, wrong, d=1, say=None, x=None, q="Tinglang va rasmini toping"):
    """Tinglab rasm tanlash: inglizcha so‘z (yoki gap) eshitiladi, javob — emoji."""
    return Q(q, _pic(word), [_pic(k) for k in wrong], d=d, x=x or f"{_w(word)} — {VOC[word][1]} {_pic(word)}",
             say=say or _w(word), lang="en")


def TR(word, wrong, d=1, x=None, q="Tinglang va tarjimasini toping"):
    """Tinglab tarjima tanlash: inglizcha so‘z eshitiladi, javob — o‘zbekcha so‘z."""
    em, uz = VOC[word]
    return Q(q, uz, [VOC[k][1] for k in wrong], d=d, x=x or f"{_w(word)} — {uz}" + (f" {em}" if em else ""),
             say=_w(word), lang="en")


def SAME(word, shown, d=1, x=None, q="Tinglang: so‘z rasmga mosmi?"):
    """To‘g‘ri / noto‘g‘ri: rasm ko‘rsatiladi, inglizcha so‘z eshitiladi."""
    em = _pic(shown)
    ok = word == shown
    if x is None:
        x = (_end(f"To‘g‘ri: {_w(word)} — {VOC[word][1]} {em}") if ok else
             _end(f"Rasmda — {VOC[shown][1]} ({_w(shown)}). {_w(word)} esa — {VOC[word][1]}"))
    return TF(q, ok, d=d, x=x, e=em, say=_w(word), lang="en")


def MATCHE(words, q="So‘zni rasmga moslang", d=2):
    return MATCH(q, [(_w(k), _pic(k)) for k in words], d=d, lang="en")


def MATCHU(words, q="So‘zni tarjimasi bilan juftlang", d=2):
    return MATCH(q, [(_w(k), VOC[k][1]) for k in words], d=d, lang="en")


def RW(word, wrong, d=3, q="Rasmga qarang. Inglizcha qanday ataladi?"):
    """Rasmga mos inglizcha so‘zni o‘qib topish (o‘qishni biladiganlar uchun — 3-daraja)."""
    return Q(q, _w(word), wrong, d=d, e=_pic(word), x=f"{_pic(word)} — {_w(word)} ({VOC[word][1]})")


def LISTEN(say, a, w, d=1, x=None, q="Tinglang va tarjimasini toping", e=None):
    """Tinglab tushunish: inglizcha ibora eshitiladi, o‘zbekcha tarjimasi tanlanadi."""
    return Q(q, a, w, d=d, x=x or f"{say} — {a}", e=e, say=say, lang="en")


def EN(q, a, w, say, d=1, x=None, e=None, h=None, text=None):
    """Savol matnida inglizcha qism bor — u ingliz ovozida aytiladi."""
    return Q(q, a, w, d=d, x=x, e=e, h=h, text=text, say=say, lang="en")


def TFE(q, a, say, d=1, x=None, e=None, text=None):
    return TF(q, a, d=d, x=x, e=e, text=text, say=say, lang="en")


def GAP(sentence, a, w, d=1, x=None, note=None, e=None, h=None):
    """Bo‘sh joyli inglizcha gap: ekranda ko‘rsatma + gap, ovozda — faqat gap (ingliz tilida)."""
    q = f"Bo‘sh joyga mos so‘zni tanlang: {sentence}" + (f" ({note})" if note else "")
    return Q(q, a, w, d=d, x=x, e=e, h=h, say=sentence, lang="en")


def NUM(word, digit, wrong, d=1):
    return Q("Tinglang va sonni toping", digit, wrong, d=d, x=f"{word} — {digit}", say=word, lang="en")


# ============================================================ 1-chorak
T.topic("greetings", "👋", L("Salom! Xayr!", "Hello and goodbye", "Привет и пока"),
        chapter=C1,
        theory="Salomlashganda: Hello! yoki Hi! 👋 — Salom!\n"
               "Xayrlashganda: Goodbye! yoki Bye! — Xayr!\n"
               "Ertalab: Good morning! 🌅 — Xayrli tong!  Uxlashdan oldin: Good night! 🌙 — Xayrli tun!\n"
               "Thank you! — Rahmat!  Please — Iltimos.  Sorry! — Kechirasiz!\n"
               "Yes — Ha.  No — Yo‘q.",
        items=[
            LISTEN("Hello!", "Salom!", ["Xayr!", "Rahmat!", "Iltimos"], e="👋"),
            LISTEN("Goodbye!", "Xayr!", ["Salom!", "Rahmat!", "Xayrli tong!"]),
            LISTEN("Thank you!", "Rahmat!", ["Salom!", "Xayr!", "Kechirasiz!"]),
            LISTEN("Good morning!", "Xayrli tong!", ["Xayrli tun!", "Xayr!", "Rahmat!"], e="🌅"),
            LISTEN("Good night!", "Xayrli tun!", ["Xayrli tong!", "Salom!", "Iltimos"], e="🌙"),
            LISTEN("Yes!", "Ha!", ["Yo‘q!", "Salom!", "Xayr!"]),
            LISTEN("No!", "Yo‘q!", ["Ha!", "Rahmat!", "Salom!"]),
            LISTEN("Hi!", "Salom!", ["Xayr!", "Kechirasiz!", "Yo‘q!"]),
            LISTEN("Bye!", "Xayr!", ["Salom!", "Iltimos", "Ha!"]),
            EN("Tinglang: bu so‘z qachon aytiladi?", "🌅", ["🌙", "🌃"], say="Good morning!",
               x="Good morning! — Xayrli tong! U ertalab aytiladi."),
            EN("Tinglang: bu so‘z qachon aytiladi?", "🌙", ["🌅", "🌞"], say="Good night!",
               x="Good night! — Xayrli tun! U uxlashdan oldin aytiladi."),
            TFE("Tinglang: bu salomlashishmi?", True, say="Hello!", e="👋", x="To‘g‘ri: Hello! — Salom!"),
            TFE("Tinglang: bu “Rahmat!” degani.", False, say="Sorry!",
                x="Sorry! — Kechirasiz! “Rahmat!” esa — Thank you!"),
            LISTEN("Sorry!", "Kechirasiz!", ["Rahmat!", "Salom!", "Xayrli tun!"], d=2),
            LISTEN("Please", "Iltimos", ["Rahmat", "Kechirasiz", "Xayr"], d=2),
            TFE("Tinglang: bu ertalab aytiladi.", False, say="Good night!", d=2,
                x="Good night! — Xayrli tun! U kechasi, uxlashdan oldin aytiladi."),
            Q("Do‘stingizni ko‘rdingiz. Nima deysiz?", "Hello!", ["Goodbye!", "Good night!", "Sorry!"], d=2, e="🙂",
              x="Uchrashganda Hello! (Salom!) deymiz."),
            Q("Maktabdan uyga ketyapsiz. Do‘stingizga nima deysiz?", "Bye!", ["Hi!", "Thank you!", "Good morning!"],
              d=2, x="Xayrlashganda Bye! yoki Goodbye! (Xayr!) deymiz."),
            Q("Sizga sovg‘a berishdi. Nima deysiz?", "Thank you!", ["Goodbye!", "Sorry!", "Good night!"], d=2,
              e="🎁", x="Sovg‘a olganda Thank you! (Rahmat!) deymiz."),
            Q("Uxlashga yotyapsiz. Onangizga nima deysiz?", "Good night!", ["Good morning!", "Hello!", "Thank you!"],
              d=2, e="🛏️", x="Uxlashdan oldin Good night! (Xayrli tun!) deymiz."),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("Hello!", "Salom!"), ("Goodbye!", "Xayr!"), ("Thank you!", "Rahmat!"), ("Yes", "Ha"),
                   ("No", "Yo‘q"), ("Please", "Iltimos")], d=2, lang="en"),
            EN("Ustoz sinfga kirib shunday dedi. Siz nima deysiz?", "Good morning!",
               ["Good night!", "Goodbye!", "Sorry!"], say="Good morning, children!", d=3,
               x="Salomga salom bilan javob beramiz: Good morning!"),
            Q("Do‘stingizni bilmasdan turtib yubordingiz. Nima deysiz?", "Sorry!",
              ["Thank you!", "Hello!", "Good night!"], d=3, x="Uzr so‘raganda Sorry! (Kechirasiz!) deymiz."),
            Q("Qaysi so‘z “Ha” degani?", "Yes", ["No", "Hi", "Bye"], d=3, x="Yes — Ha, No — Yo‘q."),
        ])

T.topic("my_name", "🙋", L("Isming nima?", "What is your name?", "Как тебя зовут?"),
        chapter=C1, prereq=["greetings"],
        theory="What is your name? — Isming nima?\n"
               "My name is Ali. — Mening ismim Ali.  I am Ali. — Men Aliman.\n"
               "I am a boy. 👦 — Men o‘g‘il bolaman.  I am a girl. 👧 — Men qiz bolaman.\n"
               "How are you? — Qalaysan? — I'm fine, thank you. 🙂 — Yaxshi, rahmat.",
        items=[
            LISTEN("What is your name?", "Isming nima?", ["Qalaysan?", "Xayr!", "Rahmat!"]),
            LISTEN("How are you, Ali?", "Qalaysan, Ali?", ["Isming nima, Ali?", "Xayr, Ali!", "Salom, Ali!"]),
            LISTEN("I'm fine, thank you.", "Yaxshi, rahmat.", ["Mening ismim Anvar.", "Xayrli tun!", "Kechirasiz!"]),
            LISTEN("My name is Ali.", "Mening ismim Ali.", ["Men o‘g‘il bolaman.", "Salom, Ali!", "Xayr, Ali!"]),
            PIC("boy", ["girl", "baby"]),
            PIC("girl", ["boy", "grandfather"]),
            PIC("boy", ["girl", "grandmother"], say="I am a boy.", x="I am a boy. — Men o‘g‘il bolaman. 👦"),
            PIC("girl", ["boy", "baby"], say="I am a girl.", x="I am a girl. — Men qiz bolaman. 👧"),
            EN("Tinglang: bolaning ismi nima?", "Zarina", ["Laylo", "Nodira", "Kamola"], say="My name is Zarina.",
               x="My name is Zarina. — Mening ismim Zarina."),
            EN("Tinglang: bolaning ismi nima?", "Bobur", ["Jasur", "Sardor", "Aziz"], say="Hello! My name is Bobur.",
               x="My name is Bobur. — Mening ismim Bobur."),
            EN("Tinglang: bola o‘zini qanday his qilyapti?", "🙂", ["😢", "😴"], say="I'm fine!",
               x="I'm fine! — Yaxshiman! 🙂"),
            TFE("Tinglang: gap rasmga mosmi?", True, say="I am a girl.", e="👧",
                x="To‘g‘ri: I am a girl. — Men qiz bolaman."),
            TFE("Tinglang: gap rasmga mosmi?", False, say="I am a girl.", e="👦",
                x="Rasmda o‘g‘il bola. U “I am a boy.” deydi."),
            LISTEN("I am Ali.", "Men Aliman.", ["U Ali.", "Salom, Ali!", "Xayr, Ali!"], d=2),
            EN("Tinglang: kim gapiryapti?", "👧", ["👦", "👴"], say="Hi! I am a girl. My name is Malika.", d=2,
               x="I am a girl — men qiz bolaman. Ismi — Malika."),
            EN("Tinglang: kim gapiryapti?", "👦", ["👧", "👵"], say="Hello! I am a boy. My name is Jasur.", d=2,
               x="I am a boy — men o‘g‘il bolaman. Ismi — Jasur."),
            EN("Sizdan “What is your name?” deb so‘rashdi. Javob qaysi?", "My name is Olim.",
               ["I'm fine, thank you.", "Goodbye!", "Good night!"], say="What is your name?", d=2,
               x="Ism so‘ralsa: My name is … — Mening ismim …"),
            TFE("“I'm fine.” — “Yaxshiman.” degani.", True, say="I'm fine.", d=2,
                x="To‘g‘ri: I'm fine. — Yaxshiman. Hol so‘ralganda shunday javob beramiz."),
            GAP("I am a ...", "girl", ["boy", "name", "fine"], d=2, e="👧", x="Rasmda qiz bola: I am a girl."),
            GAP("I am a ...", "boy", ["girl", "name", "morning"], d=2, e="👦", x="Rasmda o‘g‘il bola: I am a boy."),
            MATCH("Iborani tarjimasi bilan juftlang",
                  [("What is your name?", "Isming nima?"), ("How are you?", "Qalaysan?"),
                   ("I am a boy.", "Men o‘g‘il bolaman."), ("I am a girl.", "Men qiz bolaman."),
                   ("I'm fine.", "Yaxshiman.")], d=2, lang="en"),
            TFE("“My name is Kamol.” — “Mening ismim Kamol.” degani.", True, say="My name is Kamol.", d=2,
                x="To‘g‘ri: My name is … — Mening ismim …"),
            GAP("What is your ...?", "name", ["boy", "fine", "girl"], d=3, x="What is your name? — Isming nima?"),
            Q("“Isming nima?” inglizcha qanday?", "What is your name?", ["How are you?", "My name is Ali.", "Goodbye!"],
              d=3, x="Isming nima? — What is your name?"),
            Q("Qiz bola o‘zi haqida nima deydi?", "I am a girl.", ["I am a boy.", "I am a baby.", "Good night!"], d=3,
              e="👧", x="Qiz bola: I am a girl. O‘g‘il bola: I am a boy."),
        ])

T.topic("classroom", "🎒", L("Maktab buyumlari", "School things", "Школьные вещи"),
        chapter=C1,
        theory="Maktab buyumlari: pen 🖊️ — ruchka, pencil ✏️ — qalam, book 📕 — kitob, bag 🎒 — sumka.\n"
               "ruler 📏 — chizg‘ich, notebook 📓 — daftar, crayon 🖍️ — rangli qalam, scissors ✂️ — qaychi.\n"
               "desk — parta, rubber — o‘chirg‘ich, school 🏫 — maktab, teacher 👩‍🏫 — o‘qituvchi.\n"
               "Misol: It is a pen. — Bu ruchka.  This is my bag. — Bu mening sumkam.",
        items=[
            PIC("pen", ["pencil", "book"]),
            PIC("pencil", ["pen", "ruler"]),
            PIC("book", ["bag", "scissors"]),
            PIC("bag", ["book", "ruler"]),
            PIC("ruler", ["pencil", "scissors"]),
            PIC("notebook", ["scissors", "ruler"]),
            PIC("scissors", ["pen", "bag"]),
            PIC("crayon", ["notebook", "scissors"]),
            PIC("school", ["bag", "book"]),
            TR("desk", ["rubber", "school"]),
            TR("rubber", ["desk", "ruler"]),
            SAME("pencil", "pencil"),
            SAME("book", "ruler"),
            PIC("teacher", ["school", "book"], d=2),
            TR("teacher", ["school", "desk"], d=2),
            SAME("scissors", "bag", d=2),
            PIC("book", ["pen", "ruler"], say="It is a book.", d=2, x="It is a book. — Bu kitob. 📕"),
            PIC("bag", ["pencil", "school"], say="This is my bag.", d=2, x="This is my bag. — Bu mening sumkam. 🎒"),
            EN("Tinglang: bu buyum bilan nima qilamiz?", "qog‘oz qirqamiz", ["kitob o‘qiymiz", "to‘p o‘ynaymiz"],
               say="scissors", d=2, x="scissors — qaychi ✂️. Qaychi bilan qog‘oz qirqamiz."),
            EN("Tinglang: bu buyum bilan nima qilamiz?", "o‘qiymiz", ["qirqamiz", "yeymiz"], say="book", d=2,
               x="book — kitob 📕. Kitobni o‘qiymiz."),
            MATCHE(["pen", "pencil", "book", "bag", "ruler", "scissors"], q="Buyumni rasmga moslang"),
            MATCHU(["desk", "rubber", "notebook", "teacher", "school", "crayon"]),
            RW("pencil", ["pen", "bag", "book"]),
            RW("ruler", ["rubber", "desk", "pen"]),
            Q("Qaysi so‘z ortiqcha?", "cat", ["pen", "book", "ruler"], d=3,
              x="cat — mushuk; pen, book, ruler — maktab buyumlari."),
        ])

T.topic("commands", "🙌", L("Sinfdagi buyruqlar", "Classroom commands", "Команды в классе"),
        chapter=C1, prereq=["classroom"],
        theory="O‘qituvchi sinfda shunday deydi:\n"
               "Stand up! — Turing!  Sit down! — O‘tiring!\n"
               "Open your book! 📖 — Kitobingizni oching!  Close your book! 📕 — Kitobingizni yoping!\n"
               "Listen! 👂 — Tinglang!  Look! 👀 — Qarang!  Be quiet! 🤫 — Jim bo‘ling!\n"
               "Clap your hands! 👏 — Qarsak chaling!  Hands up! 🙌 — Qo‘llarni ko‘taring!",
        items=[
            TR("Stand up!", ["Sit down!", "Listen!"]),
            TR("Sit down!", ["Stand up!", "Look!"]),
            TR("Open your book!", ["Close your book!", "Stand up!"]),
            TR("Look!", ["Listen!", "Sit down!"]),
            PIC("Listen!", ["Look!", "Clap your hands!"]),
            PIC("Look!", ["Listen!", "Hands up!"]),
            PIC("Clap your hands!", ["Hands up!", "Be quiet!"]),
            PIC("Be quiet!", ["Clap your hands!", "Look!"]),
            PIC("Hands up!", ["Clap your hands!", "Listen!"]),
            SAME("Listen!", "Listen!", x="To‘g‘ri: Listen! — Tinglang! 👂"),
            TR("Close your book!", ["Open your book!", "Clap your hands!"], d=2),
            TR("Be quiet!", ["Listen!", "Hands up!"], d=2),
            PIC("Open your book!", ["Close your book!", "Listen!"], d=2,
                x="Open your book! — Kitobingizni oching! 📖 (ochiq kitob)"),
            SAME("Look!", "Clap your hands!", d=2, x="Rasmda qarsak 👏 — Clap your hands! Look! esa — Qarang!"),
            EN("O‘qituvchi shunday dedi. Nima qilasiz?", "Jim o‘tiraman", ["Qo‘shiq aytaman", "Yuguraman", "Baqiraman"],
               say="Be quiet!", d=2, x="Be quiet! — Jim bo‘ling!"),
            EN("O‘qituvchi shunday dedi. Nima qilasiz?", "O‘rnimdan turaman",
               ["O‘tiraman", "Qarsak chalaman", "Kitobni yopaman"], say="Stand up!", d=2, x="Stand up! — Turing!"),
            EN("O‘qituvchi shunday dedi. Nima qilasiz?", "Qarsak chalaman",
               ["O‘rnimdan turaman", "Kitobni ochaman", "Jim o‘tiraman"], say="Clap your hands!", d=2,
               x="Clap your hands! — Qarsak chaling!"),
            MATCHE(["Listen!", "Look!", "Clap your hands!", "Be quiet!", "Open your book!", "Hands up!"],
                   q="Buyruqni rasmga moslang"),
            MATCHU(["Stand up!", "Sit down!", "Open your book!", "Close your book!", "Listen!", "Look!"],
                   q="Buyruqni tarjimasi bilan juftlang"),
            EN("Tinglang: bunga teskari buyruq qaysi?", "Sit down!", ["Clap your hands!", "Look!", "Listen!"],
               say="Stand up!", d=3, x="Stand up! (Turing!) — Sit down! (O‘tiring!)"),
            EN("Tinglang: bunga teskari buyruq qaysi?", "Close your book!", ["Hands up!", "Stand up!", "Be quiet!"],
               say="Open your book!", d=3, x="Open your book! (Oching!) — Close your book! (Yoping!)"),
            Q("“Qarang!” inglizcha qanday?", "Look!", ["Listen!", "Sit down!", "Stand up!"], d=3,
              x="Look! — Qarang! Listen! — Tinglang!"),
        ])

T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"),
       ["greetings", "my_name", "classroom", "commands"], chapter=C1)

# ============================================================ 2-chorak
COLOUR_Q = "Tinglang va rangni toping"
COLOUR_THING = "Tinglang: qaysi narsa shu rangda?"

T.topic("colours", "🎨", L("Ranglar", "Colours", "Цвета"),
        chapter=C2,
        theory="Ranglar: red ❤️ — qizil, yellow 💛 — sariq, blue 💙 — ko‘k, green 💚 — yashil.\n"
               "orange 🧡 — to‘q sariq, purple 💜 — binafsha, pink 💗 — pushti.\n"
               "black 🖤 — qora, white ⚪ — oq, brown — jigarrang.\n"
               "Misol: It is red. 🍎 — U qizil.  It is yellow. 🍌 — U sariq.",
        items=[
            PIC("red", ["blue", "yellow"], q=COLOUR_Q),
            PIC("yellow", ["green", "purple"], q=COLOUR_Q),
            PIC("blue", ["red", "green"], q=COLOUR_Q),
            PIC("green", ["yellow", "blue"], q=COLOUR_Q),
            PIC("purple", ["orange", "blue"], q=COLOUR_Q),
            PIC("orange", ["purple", "green"], q=COLOUR_Q),
            PIC("pink", ["yellow", "black"], q=COLOUR_Q),
            PIC("black", ["pink", "yellow"], q=COLOUR_Q),
            PIC("white", ["black", "red"], q=COLOUR_Q),
            TR("brown", ["pink", "yellow"]),
            TR("white", ["black", "red"]),
            TFE("Tinglang: rang rasmga mosmi?", True, say="red", e="🍎", x="To‘g‘ri: olma qizil — red."),
            TFE("Tinglang: rang rasmga mosmi?", False, say="blue", e="🍌", x="Banan sariq — yellow. blue esa — ko‘k."),
            EN(COLOUR_THING, "🍌", ["🍎", "🍇"], say="yellow", d=2, x="yellow — sariq. Banan sariq."),
            EN(COLOUR_THING, "🐸", ["🍌", "🍎"], say="green", d=2, x="green — yashil. Qurbaqa yashil."),
            EN(COLOUR_THING, "🍎", ["🍌", "🐸"], say="red", d=2, x="red — qizil. Olma qizil."),
            EN(COLOUR_THING, "⛄", ["🍫", "🐸"], say="white", d=2, x="white — oq. Qor odam oppoq qordan yasaladi. ⛄"),
            TFE("Tinglang: rang rasmga mosmi?", True, say="orange", e="🍊", d=2,
                x="To‘g‘ri: apelsin to‘q sariq. Qiziq: apelsin ham inglizcha orange!"),
            PIC("blue", ["yellow", "red"], say="It is blue.", q=COLOUR_Q, d=2, x="It is blue. — U ko‘k. 💙"),
            MATCHE(["red", "yellow", "green", "blue", "purple", "orange", "black"], q="Rangni rasmga moslang"),
            MATCHU(["white", "black", "pink", "brown", "red", "yellow"], q="Rangni tarjimasi bilan juftlang"),
            EN(COLOUR_THING, "🍫", ["🍌", "🐸"], say="brown", d=3, x="brown — jigarrang. Shokolad jigarrang."),
            EN(COLOUR_THING, "🍇", ["🍋", "🐸"], say="purple", d=3, x="purple — binafsha. Bu uzum binafsha rangda."),
            Q("Rasmga qarang. Bu qanday rang? Inglizcha tanlang", "green", ["red", "yellow", "blue"], d=3, e="💚",
              x="💚 — green (yashil)."),
            Q("Rasmga qarang. Bu qanday rang? Inglizcha tanlang", "pink", ["purple", "black", "white"], d=3, e="💗",
              x="💗 — pink (pushti)."),
            EN("Tinglang: qaysi ikki rang aytildi?", "❤️💙", ["💛💚", "🖤⚪", "💜🧡"], say="red and blue", d=3,
               x="red and blue — qizil va ko‘k."),
        ])

T.topic("numbers", "🔢", L("Sonlar 1–10", "Numbers 1–10", "Числа 1–10"),
        chapter=C2,
        theory="1 — one, 2 — two, 3 — three, 4 — four, 5 — five,\n"
               "6 — six, 7 — seven, 8 — eight, 9 — nine, 10 — ten.\n"
               "Sanaymiz: one, two, three… 🖐️ Bir qo‘lda five (5) ta barmoq bor.\n"
               "How many? — Nechta?  Three cats. 🐱🐱🐱 — Uchta mushuk.",
        items=[
            NUM("one", "1", ["7", "4"]),
            NUM("two", "2", ["5", "3"]),
            NUM("three", "3", ["8", "10"]),
            NUM("four", "4", ["6", "9"]),
            NUM("five", "5", ["2", "9"]),
            NUM("seven", "7", ["1", "4"]),
            NUM("eight", "8", ["3", "6"]),
            NUM("ten", "10", ["1", "7"]),
            EN("Tinglang: qaysi rasmda shuncha narsa bor?", "🍎🍎", ["🍎", "🍎🍎🍎"], say="two",
               x="two — 2: 🍎🍎"),
            EN("Tinglang: qaysi rasmda shuncha narsa bor?", "🐶", ["🐶🐶", "🐶🐶🐶"], say="one",
               x="one — 1: 🐶"),
            TFE("Tinglang: son to‘g‘rimi?", True, say="three", text="🎈 🎈 🎈", x="To‘g‘ri: 3 ta shar — three."),
            TFE("Tinglang: son to‘g‘rimi?", False, say="three", text="🐟 🐟", x="Bu yerda 2 ta baliq — two."),
            NUM("six", "6", ["9", "3"], d=2),
            NUM("nine", "9", ["6", "5"], d=2),
            EN("Tinglang: qaysi rasmda shuncha narsa bor?", "🐱🐱🐱", ["🐱🐱", "🐱🐱🐱🐱"], say="three", d=2,
               x="three — 3: 🐱🐱🐱"),
            EN("Tinglang: qaysi rasmda shuncha narsa bor?", "⭐⭐⭐⭐", ["⭐⭐⭐", "⭐⭐"], say="four", d=2,
               x="four — 4: ⭐⭐⭐⭐"),
            TFE("Tinglang: son to‘g‘rimi?", True, say="five", text="⭐ ⭐ ⭐ ⭐ ⭐", d=2,
                x="To‘g‘ri: 5 ta yulduz — five."),
            Q("Sanang: nechta? Inglizcha tanlang", "four", ["three", "five", "two"], d=2, text="🐤 🐤 🐤 🐤",
              x="4 ta jo‘ja — four."),
            EN("Tinglang va hisoblang", "3", ["2", "4", "5"], say="one plus two", d=2, x="one plus two — 1 + 2 = 3."),
            EN("Tinglang va hisoblang", "4", ["3", "5", "6"], say="two plus two", d=2, x="two plus two — 2 + 2 = 4."),
            EN("Tinglang: qaysi son tushib qoldi?", "3", ["5", "6", "2"], say="one, two, ..., four", d=2,
               x="one, two, three, four — 1, 2, 3, 4."),
            MATCH("Son va so‘zni juftlang",
                  [("5", "five"), ("7", "seven"), ("8", "eight"), ("9", "nine"), ("10", "ten"), ("3", "three")],
                  d=2, lang="en"),
            Q("Bir qo‘lingizda nechta barmoq bor? Inglizcha tanlang", "five", ["four", "six", "ten"], d=2, e="🖐️",
              x="Bir qo‘lda 5 ta barmoq — five."),
            Q("Sanang: nechta? Inglizcha tanlang", "six", ["seven", "five", "nine"], d=3,
              text="🍓 🍓 🍓 🍓 🍓 🍓", x="6 ta qulupnay — six."),
            EN("Tinglang va hisoblang", "10", ["9", "8", "6"], say="five plus five", d=3,
               x="five plus five — 5 + 5 = 10."),
            EN("Tinglang: qaysi son tushib qoldi?", "8", ["6", "9", "10"], say="six, seven, ..., nine", d=3,
               x="six, seven, eight, nine — 6, 7, 8, 9."),
            Q("Ikkala qo‘lingizda nechta barmoq bor? Inglizcha tanlang", "ten", ["five", "eight", "nine"], d=3,
              e="🙌", x="Ikki qo‘lda 10 ta barmoq — ten."),
        ])

T.topic("toys", "🎈", L("O‘yinchoqlar", "Toys", "Игрушки"),
        chapter=C2,
        theory="O‘yinchoqlar (toys): ball ⚽ — to‘p, car 🚗 — mashina, balloon 🎈 — havo shari.\n"
               "robot 🤖 — robot, drum 🥁 — baraban, train 🚂 — poyezd, plane ✈️ — samolyot.\n"
               "bike 🚲 — velosiped, boat ⛵ — qayiq, doll — qo‘g‘irchoq, teddy bear — ayiqcha, kite — varrak.\n"
               "Misol: This is my ball. ⚽ — Bu mening to‘pim.  It is a red car. 🚗 — Bu qizil mashina.",
        items=[
            PIC("ball", ["car", "drum"]),
            PIC("car", ["train", "plane"]),
            PIC("balloon", ["ball", "robot"]),
            PIC("robot", ["car", "balloon"]),
            PIC("drum", ["ball", "bike"]),
            PIC("train", ["car", "boat"]),
            PIC("plane", ["train", "balloon"]),
            PIC("bike", ["car", "drum"]),
            PIC("boat", ["plane", "robot"]),
            TR("doll", ["teddy bear", "kite"]),
            TR("teddy bear", ["doll", "ball"]),
            SAME("ball", "ball"),
            SAME("robot", "drum"),
            TR("kite", ["bike", "doll"], d=2),
            TR("toy", ["robot", "car"], d=2),
            SAME("train", "boat", d=2),
            PIC("car", ["train", "bike"], say="It is a red car.", d=2, x="It is a red car. — Bu qizil mashina. 🚗"),
            PIC("balloon", ["ball", "drum"], say="This is my balloon.", d=2,
                x="This is my balloon. — Bu mening havo sharim. 🎈"),
            EN("Tinglang: qaysi rasm to‘g‘ri?", "⚽⚽", ["⚽", "⚽⚽⚽"], say="two balls", d=2,
               x="two balls — ikkita to‘p."),
            MATCHE(["ball", "car", "balloon", "robot", "drum", "train", "plane"], q="O‘yinchoqni rasmga moslang"),
            MATCHU(["doll", "teddy bear", "kite", "ball", "car", "bike"], q="O‘yinchoqni tarjimasi bilan juftlang"),
            RW("robot", ["ball", "drum", "car"]),
            RW("drum", ["doll", "ball", "boat"]),
            Q("Qaysi so‘z ortiqcha?", "apple", ["ball", "doll", "kite"], d=3,
              x="apple — olma; ball, doll, kite — o‘yinchoqlar."),
        ])

T.test("test2", L("2-nazorat ishi", "Test 2", "Контрольная работа 2"),
       ["colours", "numbers", "toys"], chapter=C2)

# ============================================================ 3-chorak
T.topic("family", "👪", L("Mening oilam", "My family", "Моя семья"),
        chapter=C3,
        theory="Oila (family) 👪: mother (mum) 👩 — ona, father (dad) 👨 — ota.\n"
               "sister 👧 — opa yoki singil, brother 👦 — aka yoki uka, baby 👶 — chaqaloq.\n"
               "grandmother (granny) 👵 — buvi, grandfather (grandpa) 👴 — bobo.\n"
               "Misol: This is my mum. — Bu mening onam.  I love my family. — Men oilamni yaxshi ko‘raman.",
        items=[
            PIC("mother", ["father", "baby"]),
            PIC("father", ["mother", "grandfather"]),
            PIC("sister", ["brother", "baby"]),
            PIC("brother", ["sister", "father"]),
            PIC("baby", ["sister", "grandmother"]),
            PIC("grandmother", ["mother", "grandfather"]),
            PIC("grandfather", ["father", "grandmother"]),
            PIC("family", ["baby", "mother"]),
            PIC("mum", ["dad", "granny"]),
            PIC("dad", ["mum", "grandpa"]),
            TR("grandmother", ["mother", "baby"]),
            SAME("baby", "baby"),
            SAME("mother", "father"),
            PIC("granny", ["grandpa", "mum"], d=2),
            PIC("grandpa", ["granny", "dad"], d=2),
            TR("family", ["father", "baby"], d=2),
            SAME("grandfather", "grandfather", d=2),
            PIC("dad", ["mum", "baby"], say="This is my dad.", d=2, x="This is my dad. — Bu mening otam. 👨"),
            PIC("granny", ["grandpa", "sister"], say="This is my granny.", d=2,
                x="This is my granny. — Bu mening buvim. 👵"),
            PIC("sister", ["brother", "grandfather"], say="This is my sister.", d=2,
                x="This is my sister. — Bu mening opam (singlim). 👧"),
            LISTEN("I love my family.", "Men oilamni yaxshi ko‘raman.",
                   ["Bu mening onam.", "Bu mening otam.", "Men maktabni yaxshi ko‘raman."], d=2),
            MATCHE(["mother", "father", "baby", "grandmother", "grandfather", "family"]),
            MATCHU(["mum", "dad", "sister", "brother", "baby", "granny"]),
            RW("baby", ["father", "mother", "sister"]),
            RW("grandmother", ["grandfather", "mother", "sister"]),
            EN("Tinglang: oilada necha kishi bor?", "4", ["3", "5", "2"], say="Mum, dad, my sister and me.", d=3,
               x="Mum, dad, sister va men — 4 kishi."),
        ])

T.topic("body", "👃", L("Tana a’zolari", "My body", "Части тела"),
        chapter=C3,
        theory="Tana a’zolari: head — bosh, hair — soch, face 🙂 — yuz.\n"
               "eyes 👀 — ko‘zlar, ear 👂 — quloq, nose 👃 — burun, mouth 👄 — og‘iz, tongue 👅 — til.\n"
               "hand ✋ — qo‘l, legs — oyoqlar.\n"
               "Bizda two eyes (ikkita ko‘z), two ears (ikkita quloq) va one nose (bitta burun) bor.\n"
               "Touch your nose! — Burningizni ushlang!  Close your eyes! — Ko‘zingizni yuming!",
        items=[
            PIC("nose", ["ear", "mouth"]),
            PIC("eyes", ["nose", "hand"]),
            PIC("ear", ["eyes", "tongue"]),
            PIC("mouth", ["nose", "ear"]),
            PIC("hand", ["face", "mouth"]),
            PIC("face", ["hand", "eyes"]),
            TR("head", ["hair", "face"]),
            TR("hair", ["head", "nose"]),
            TR("legs", ["hand", "ear"]),
            SAME("ear", "ear"),
            SAME("mouth", "nose"),
            PIC("tongue", ["mouth", "eyes"], d=2),
            SAME("hand", "hand", d=2),
            EN("Tinglang: qaysi a’zoni ushlaysiz?", "👃", ["👂", "👀"], say="Touch your nose!", d=2,
               x="Touch your nose! — Burningizni ushlang! 👃"),
            EN("Tinglang: qaysi a’zoni ushlaysiz?", "👂", ["👄", "👃"], say="Touch your ear!", d=2,
               x="Touch your ear! — Qulog‘ingizni ushlang! 👂"),
            LISTEN("Close your eyes!", "Ko‘zingizni yuming!",
                   ["Ko‘zingizni oching!", "Og‘zingizni oching!", "Qulog‘ingizni ushlang!"], d=2),
            LISTEN("Open your mouth!", "Og‘zingizni oching!",
                   ["Ko‘zingizni yuming!", "Qo‘lingizni ko‘taring!", "Burningizni ushlang!"], d=2),
            EN("Tinglang: bu a’zo bilan nima qilamiz?", "ko‘ramiz", ["eshitamiz", "hid bilamiz"], say="eyes", d=2,
               x="eyes — ko‘zlar. Ko‘z bilan ko‘ramiz. 👀"),
            EN("Tinglang: bu a’zo bilan nima qilamiz?", "eshitamiz", ["ko‘ramiz", "hid bilamiz"], say="ears", d=2,
               x="ears — quloqlar. Quloq bilan eshitamiz. 👂"),
            Q("Odamning nechta qulog‘i bor? Inglizcha tanlang", "two", ["one", "three", "four"], d=2, e="👂",
              x="Odamning ikkita qulog‘i bor — two ears."),
            MATCHE(["nose", "eyes", "ear", "mouth", "hand", "tongue"]),
            MATCHU(["head", "hair", "face", "nose", "mouth", "legs"]),
            EN("Tinglang: bu a’zo bilan nima qilamiz?", "hid bilamiz", ["ko‘ramiz", "eshitamiz"], say="nose", d=3,
               x="nose — burun. Burun bilan hid bilamiz. 👃"),
            Q("Odamning nechta burni bor? Inglizcha tanlang", "one", ["two", "three", "four"], d=3, e="👃",
              x="Odamning bitta burni bor — one nose."),
            RW("nose", ["ear", "eyes", "mouth"]),
        ])

T.topic("feelings", "😀", L("Kayfiyatim", "How do you feel?", "Настроение"),
        chapter=C3, prereq=["my_name"],
        theory="How are you? — Qalaysan? Kayfiyatingizni ayting:\n"
               "I'm happy. 😀 — Men xursandman.  I'm sad. 😢 — Men xafaman.\n"
               "I'm angry. 😠 — Jahlim chiqdi.  I'm tired. 😫 — Charchadim.  I'm sleepy. 😴 — Uyqum keldi.\n"
               "I'm hungry. — Qornim och.  I'm thirsty. — Chanqadim.  I'm fine. 🙂 — Yaxshiman.",
        items=[
            PIC("happy", ["sad", "angry"]),
            PIC("sad", ["happy", "sleepy"]),
            PIC("angry", ["happy", "sleepy"]),
            PIC("sleepy", ["angry", "happy"]),
            PIC("tired", ["happy", "sad"]),
            PIC("happy", ["sad", "sleepy"], say="I'm happy!", x="I'm happy! — Men xursandman! 😀"),
            PIC("sad", ["happy", "angry"], say="I'm sad.", x="I'm sad. — Men xafaman. 😢"),
            TR("sad", ["happy", "sleepy"]),
            LISTEN("I'm hungry.", "Qornim och.", ["Chanqadim.", "Uyqum keldi.", "Men xursandman."]),
            SAME("happy", "happy"),
            SAME("sad", "happy"),
            PIC("sleepy", ["happy", "sad"], say="I'm sleepy.", d=2, x="I'm sleepy. — Uyqum keldi. 😴"),
            LISTEN("I'm thirsty.", "Chanqadim.", ["Qornim och.", "Charchadim.", "Jahlim chiqdi."], d=2),
            LISTEN("I'm tired.", "Charchadim.", ["Men xursandman.", "Qornim och.", "Men xafaman."], d=2),
            EN("Tinglang: bolaga nima kerak?", "🍞", ["🛏️", "⚽"], say="I'm hungry.", d=2,
               x="I'm hungry. — Qornim och. Unga ovqat kerak. 🍞"),
            EN("Tinglang: bolaga nima kerak?", "🛏️", ["🍞", "⚽"], say="I'm sleepy.", d=2,
               x="I'm sleepy. — Uyqum keldi. U uxlashi kerak. 🛏️"),
            SAME("angry", "angry", d=2),
            Q("Tug‘ilgan kuningizda sovg‘a oldingiz. Qanday bo‘lasiz? Inglizcha tanlang", "happy",
              ["sad", "angry", "sleepy"], d=2, e="🎁", x="Sovg‘a olsak xursand bo‘lamiz — happy. 😀"),
            MATCHE(["happy", "sad", "angry", "sleepy", "tired", "fine"]),
            MATCH("Gapni tarjimasi bilan juftlang",
                  [("I'm happy.", "Men xursandman."), ("I'm sad.", "Men xafaman."), ("I'm hungry.", "Qornim och."),
                   ("I'm thirsty.", "Chanqadim."), ("I'm tired.", "Charchadim."), ("I'm sleepy.", "Uyqum keldi.")],
                  d=2, lang="en"),
            EN("Tinglang: bolaga nima kerak?", "🥛", ["🛏️", "🎈"], say="I'm thirsty.", d=3,
               x="I'm thirsty. — Chanqadim. Unga ichimlik kerak. 🥛"),
            Q("Ko‘zingiz yumilib ketyapti, uxlagingiz kelyapti. Inglizcha qanday aytasiz?", "I'm sleepy.",
              ["I'm hungry.", "I'm happy.", "I'm thirsty."], d=3, x="Uyqum keldi — I'm sleepy. 😴"),
            EN("Sizdan “How are you?” deb so‘rashdi. Siz xursandsiz. Nima deysiz?", "I'm happy!",
               ["I'm sad.", "I'm angry.", "I'm hungry."], say="How are you?", d=3,
               x="Xursand bo‘lsak: I'm happy! — Men xursandman!"),
        ])

T.test("test3", L("3-nazorat ishi", "Test 3", "Контрольная работа 3"),
       ["family", "body", "feelings"], chapter=C3)

# ============================================================ 4-chorak
SOUND_Q = "Tinglang: qaysi hayvon shunday ovoz chiqaradi?"

T.topic("pets", "🐶", L("Uy va ferma hayvonlari", "Pets and farm animals", "Домашние животные"),
        chapter=C4,
        theory="Uy hayvonlari: cat 🐱 — mushuk, dog 🐶 — it, rabbit 🐰 — quyon, fish 🐟 — baliq, bird 🐦 — qush.\n"
               "Ferma hayvonlari: cow 🐮 — sigir, horse 🐴 — ot, sheep 🐑 — qo‘y, goat 🐐 — echki,\n"
               "hen 🐔 — tovuq, duck 🦆 — o‘rdak.  mouse 🐭 — sichqon.\n"
               "Inglizchada hayvon ovozlari: dog — woof, cat — meow, cow — moo, duck — quack.\n"
               "Misol: It is a cat. — Bu mushuk. 🐱",
        items=[
            PIC("cat", ["dog", "rabbit"]),
            PIC("dog", ["cat", "cow"]),
            PIC("rabbit", ["mouse", "cat"]),
            PIC("fish", ["bird", "duck"]),
            PIC("bird", ["fish", "hen"]),
            PIC("cow", ["horse", "sheep"]),
            PIC("horse", ["cow", "goat"]),
            PIC("sheep", ["goat", "cow"]),
            PIC("hen", ["duck", "bird"]),
            SAME("cow", "cow"),
            SAME("sheep", "horse"),
            PIC("goat", ["sheep", "horse"], d=2),
            PIC("duck", ["hen", "fish"], d=2),
            PIC("mouse", ["rabbit", "cat"], d=2),
            EN(SOUND_Q, "🐶", ["🐱", "🐮"], say="Woof! Woof!", d=2, x="Inglizchada it “woof” deydi. 🐶"),
            EN(SOUND_Q, "🐱", ["🐶", "🦆"], say="Meow!", d=2, x="Inglizchada mushuk “meow” deydi. 🐱"),
            EN(SOUND_Q, "🐮", ["🐑", "🐶"], say="Moo!", d=2, x="Inglizchada sigir “moo” deydi. 🐮"),
            SAME("fish", "fish", d=2),
            PIC("sheep", ["goat", "cow"], say="It is a white sheep.", d=2, x="It is a white sheep. — Bu oq qo‘y. 🐑"),
            PIC("dog", ["cat", "horse"], say="I love my dog.", d=2, x="I love my dog. — Men itimni yaxshi ko‘raman. 🐶"),
            MATCHE(["cat", "dog", "cow", "horse", "sheep", "duck", "rabbit"], q="Hayvonni rasmga moslang"),
            MATCHU(["goat", "hen", "fish", "bird", "mouse", "rabbit"], q="Hayvonni tarjimasi bilan juftlang"),
            EN(SOUND_Q, "🦆", ["🐱", "🐮"], say="Quack! Quack!", d=3, x="Inglizchada o‘rdak “quack” deydi. 🦆"),
            RW("horse", ["house", "cow", "goat"]),
            RW("duck", ["dog", "hen", "bird"]),
        ])

T.topic("zoo", "🦁", L("Hayvonot bog‘ida", "At the zoo", "В зоопарке"),
        chapter=C4, prereq=["pets"],
        theory="Hayvonot bog‘i (zoo): lion 🦁 — sher, tiger 🐯 — yo‘lbars, bear 🐻 — ayiq, monkey 🐵 — maymun.\n"
               "elephant 🐘 — fil, giraffe 🦒 — jirafa, zebra 🦓 — zebra, crocodile 🐊 — timsoh, snake 🐍 — ilon.\n"
               "frog 🐸 — qurbaqa, fox 🦊 — tulki, wolf 🐺 — bo‘ri, camel 🐫 — tuya, penguin 🐧 — pingvin.\n"
               "big — katta, small — kichik: The elephant is big. 🐘  The mouse is small. 🐭",
        items=[
            PIC("lion", ["tiger", "bear"]),
            PIC("tiger", ["lion", "zebra"]),
            PIC("bear", ["lion", "monkey"]),
            PIC("monkey", ["bear", "frog"]),
            PIC("elephant", ["giraffe", "camel"]),
            PIC("giraffe", ["zebra", "elephant"]),
            PIC("zebra", ["giraffe", "horse"]),
            PIC("crocodile", ["snake", "frog"]),
            PIC("snake", ["crocodile", "monkey"]),
            PIC("frog", ["snake", "fox"]),
            LISTEN("big", "katta", ["kichik", "yashil", "oq"]),
            SAME("lion", "lion"),
            SAME("monkey", "bear"),
            PIC("fox", ["wolf", "bear"], d=2),
            PIC("wolf", ["fox", "tiger"], d=2),
            PIC("camel", ["elephant", "giraffe"], d=2),
            PIC("penguin", ["bear", "monkey"], d=2),
            LISTEN("small", "kichik", ["katta", "sariq", "qora"], d=2),
            TFE("The elephant is big.", True, say="The elephant is big.", e="🐘", d=2,
                x="To‘g‘ri: fil katta — The elephant is big."),
            TFE("The mouse is big.", False, say="The mouse is big.", e="🐭", d=2,
                x="Sichqon kichik — The mouse is small."),
            EN("Tinglang: qaysi hayvon shunday?", "🐘", ["🐭", "🐸"], say="It is big.", d=2,
               x="It is big. — U katta. Fil katta. 🐘"),
            EN("Tinglang: qaysi hayvon shunday?", "🐭", ["🐘", "🐫"], say="It is small.", d=2,
               x="It is small. — U kichik. Sichqon kichik. 🐭"),
            MATCHE(["lion", "tiger", "bear", "monkey", "elephant", "giraffe", "zebra"], q="Hayvonni rasmga moslang"),
            MATCHU(["crocodile", "snake", "frog", "fox", "wolf", "camel"], q="Hayvonni tarjimasi bilan juftlang"),
            EN("Tinglang: qaysi hayvon shu rangda?", "🐸", ["🐻", "🦁"], say="It is green.", d=3,
               x="It is green. — U yashil. Qurbaqa yashil. 🐸"),
            RW("monkey", ["mouse", "lion", "bear"]),
            RW("elephant", ["giraffe", "tiger", "camel"]),
        ])

T.topic("fruits", "🍎", L("Mevalar va sabzavotlar", "Fruit and vegetables", "Фрукты и овощи"),
        chapter=C4,
        theory="Mevalar (fruit): apple 🍎 — olma, banana 🍌 — banan, orange 🍊 — apelsin, pear 🍐 — nok.\n"
               "grapes 🍇 — uzum, lemon 🍋 — limon, cherry 🍒 — gilos, strawberry 🍓 — qulupnay.\n"
               "watermelon 🍉 — tarvuz, melon 🍈 — qovun.\n"
               "Sabzavotlar: carrot 🥕 — sabzi, tomato 🍅 — pomidor, potato 🥔 — kartoshka, cucumber 🥒 — bodring.\n"
               "Misol: a red apple 🍎 — qizil olma.  Yummy! — Mazali!",
        items=[
            PIC("apple", ["banana", "pear"]),
            PIC("banana", ["lemon", "apple"]),
            PIC("orange*", ["lemon", "apple"]),
            PIC("pear", ["apple", "lemon"]),
            PIC("grapes", ["cherry", "strawberry"]),
            PIC("lemon", ["banana", "orange*"]),
            PIC("strawberry", ["cherry", "watermelon"]),
            PIC("watermelon", ["melon", "apple"]),
            PIC("carrot", ["tomato", "cucumber"]),
            PIC("tomato", ["apple", "carrot"]),
            SAME("apple", "apple"),
            SAME("pear", "banana"),
            PIC("cherry", ["strawberry", "grapes"], d=2),
            PIC("melon", ["watermelon", "pear"], d=2),
            PIC("potato", ["carrot", "corn"], d=2),
            PIC("cucumber", ["carrot", "corn"], d=2),
            PIC("corn", ["carrot", "banana"], d=2),
            SAME("carrot", "carrot", d=2),
            LISTEN("Yummy!", "Mazali!", ["Xayr!", "Achchiq!", "Rahmat!"], d=2),
            EN("Tinglang: bu meva qanday rangda?", "sariq", ["ko‘k", "qora"], say="banana", d=2,
               x="banana — banan. Banan sariq bo‘ladi. 🍌"),
            Q("Qaysi biri sabzavot?", "🥕", ["🍎", "🍌", "🍇"], d=2,
              x="🥕 carrot (sabzi) — sabzavot; olma, banan, uzum — mevalar."),
            MATCHE(["apple", "banana", "pear", "grapes", "lemon", "cherry", "watermelon"], q="Mevani rasmga moslang"),
            MATCHU(["carrot", "tomato", "potato", "cucumber", "orange*", "melon"]),
            EN("Tinglang: bu qanday rangda?", "qizil", ["ko‘k", "oq"], say="strawberry", d=3,
               x="strawberry — qulupnay. Pishgan qulupnay qizil bo‘ladi. 🍓"),
            RW("banana", ["apple", "lemon", "pear"]),
            RW("carrot", ["cherry", "corn", "tomato"]),
        ])

T.test("test4", L("4-nazorat ishi", "Test 4", "Контрольная работа 4"),
       ["pets", "zoo", "fruits"], chapter=C4)

T.test("final", L("Yillik takrorlash", "End-of-year review", "Итоговое повторение"),
       ["greetings", "my_name", "classroom", "commands", "colours", "numbers", "toys", "family", "body", "feelings",
        "pets", "zoo", "fruits"], chapter=C4, level=3)

T.write()
