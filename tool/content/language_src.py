# Ingliz va rus tili modullari uchun ma'lumotlar: `python3 tool/content/language_src.py`
# -> assets/data/languages.json
#
# Manba: assets/data/lexicon.json (uch tilli lug'at, umumiy ID'lar). Bu skript unga
# qo'shimcha qiladi: alifbolar (har bir harfga rasmli misol), harakatlar, sifatlar,
# iboralar, rus tilida so'z jinsi (sifat moslashuvi uchun), inglizcha ko'plik shakli,
# rus tilida ochiq bo'g'inli so'zlar (bo'g'inga ajratish bir ma'noli bo'lganlari).
# Barcha matnlar original; hech qanday darslikdan ko'chirilmagan.
import json, os, re

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "..", "assets", "data")
lex = json.load(open(os.path.join(DATA, "lexicon.json"), encoding="utf-8"))
ENTRIES = [e for e in lex["entries"] if e["ageMin"] < 99]
BY_ID = {e["id"]: e for e in ENTRIES}

# ------------------------------------------------------------------ alifbolar
EN_ALPHABET = [
    ("A", "apple"), ("B", "ball"), ("C", "cat"), ("D", "dog"), ("E", "egg"), ("F", "fish"),
    ("G", "goat"), ("H", "hat"), ("I", "island"), ("J", "joystick"), ("K", "key"), ("L", "lion"),
    ("M", "moon"), ("N", "nose"), ("O", "octopus"), ("P", "pig"), ("Q", "queen"), ("R", "rabbit"),
    ("S", "sun"), ("T", "tiger"), ("U", "umbrella"), ("V", "violin"), ("W", "whale"), ("X", "box"),
    ("Y", "yarn"), ("Z", "zebra"),
]
EN_VOWELS = set("aeiou")

# (harf, lexId yoki None, misol so'z boshida keladimi)
RU_ALPHABET = [
    ("А", "watermelon", True), ("Б", "banana", True), ("В", "wolf", True), ("Г", "mushroom", True),
    ("Д", "house", True), ("Е", "unicorn", True), ("Ё", "hedgehog", True), ("Ж", "giraffe", True),
    ("З", "zebra", True), ("И", "turkey", True), ("Й", "tea", False), ("К", "cat", True),
    ("Л", "fox", True), ("М", "ball", True), ("Н", "nose", True), ("О", "cloud", True),
    ("П", "penguin", True), ("Р", "fish", True), ("С", "elephant", True), ("Т", "tiger", True),
    ("У", "duck", True), ("Ф", "flashlight", True), ("Х", "bread", True), ("Ц", "flower", True),
    ("Ч", "tea", True), ("Ш", "scarf", True), ("Щ", None, False), ("Ъ", None, False),
    ("Ы", "cheese", False), ("Ь", "mouse", False), ("Э", None, False), ("Ю", "fireworks", False),
    ("Я", "apple", True),
]
RU_VOWELS = set("аеёиоуыэюя")

# ------------------------------------------------------------------ harakatlar
# id, emoji, uz (masdar), uz (hozirgi zamon), en, en -ing, ru (infinitiv), ru (u/u bajaryapti), yosh
ACTIONS = [
    ("run", "🏃", "yugurmoq", "yuguryapti", "run", "running", "бегать", "бежит", 4),
    ("walk", "🚶", "yurmoq", "yuryapti", "walk", "walking", "ходить", "идёт", 4),
    ("swim", "🏊", "suzmoq", "suzyapti", "swim", "swimming", "плавать", "плывёт", 4),
    ("dance", "💃", "raqs tushmoq", "raqs tushyapti", "dance", "dancing", "танцевать", "танцует", 4),
    ("sleep", "😴", "uxlamoq", "uxlayapti", "sleep", "sleeping", "спать", "спит", 4),
    ("cry", "😢", "yig‘lamoq", "yig‘layapti", "cry", "crying", "плакать", "плачет", 4),
    ("laugh", "😂", "kulmoq", "kulyapti", "laugh", "laughing", "смеяться", "смеётся", 4),
    ("clap", "👏", "qarsak chalmoq", "qarsak chalyapti", "clap", "clapping", "хлопать", "хлопает", 4),
    ("wave", "👋", "qo‘l silkitmoq", "qo‘l silkityapti", "wave", "waving", "махать", "машет", 4),
    ("eat", "😋", "yemoq", "yeyapti", "eat", "eating", "есть", "ест", 4),
    ("sit", "🧘", "o‘tirmoq", "o‘tiribdi", "sit", "sitting", "сидеть", "сидит", 4),
    ("smile", "😊", "jilmaymoq", "jilmayyapti", "smile", "smiling", "улыбаться", "улыбается", 4),
    ("write", "✍️", "yozmoq", "yozyapti", "write", "writing", "писать", "пишет", 6),
    ("think", "🤔", "o‘ylamoq", "o‘ylayapti", "think", "thinking", "думать", "думает", 6),
    ("ride", "🚴", "velosiped haydamoq", "velosiped haydayapti", "ride a bike", "riding a bike",
     "кататься на велосипеде", "едет на велосипеде", 6),
    ("climb", "🧗", "tirmashmoq", "tirmashyapti", "climb", "climbing", "лазать", "лезет", 6),
    ("ski", "⛷️", "chang‘i uchmoq", "chang‘i uchyapti", "ski", "skiing", "кататься на лыжах", "катается на лыжах", 6),
    ("row", "🚣", "eshkak eshmoq", "eshkak eshyapti", "row", "rowing", "грести", "гребёт", 6),
    ("juggle", "🤹", "koptok o‘ynatmoq", "koptok o‘ynatyapti", "juggle", "juggling", "жонглировать", "жонглирует", 6),
    ("look", "👀", "qaramoq", "qarayapti", "look", "looking", "смотреть", "смотрит", 6),
    ("raise_hand", "🙋", "qo‘l ko‘tarmoq", "qo‘l ko‘taryapti", "raise a hand", "raising a hand",
     "поднимать руку", "поднимает руку", 6),
    ("lift", "🏋️", "og‘irlik ko‘tarmoq", "og‘irlik ko‘taryapti", "lift", "lifting", "поднимать штангу", "поднимает штангу", 6),
]

# Hayvonlar harakati (gap uchun): lexicon kategoriyalari/teglari bilan.
ANIMAL_ACTIONS = [
    ("flies", "is flying", "летит", "☁️", ["bird", "insect"], "flies"),
    ("swims", "is swimming", "плывёт", "🌊", ["sea", "bird", "animal"], "swims"),
    ("runs", "is running", "бежит", "💨", ["animal"], "has_legs"),
    ("sleeps", "is sleeping", "спит", "💤", ["animal", "bird"], ""),
    ("eats", "is eating", "ест", "🍽️", ["animal", "bird"], ""),
]

# ------------------------------------------------------------------ sifatlar (6 yosh)
# id, juft, uz, en, ru (m, f, n, pl), ko'rinish: size | length | emoji:<e>
ADJECTIVES = [
    ("big", "small", "katta", "big", ("большой", "большая", "большое", "большие"), "size"),
    ("small", "big", "kichik", "small", ("маленький", "маленькая", "маленькое", "маленькие"), "size"),
    ("long", "short", "uzun", "long", ("длинный", "длинная", "длинное", "длинные"), "length"),
    ("short", "long", "qisqa", "short", ("короткий", "короткая", "короткое", "короткие"), "length"),
    ("hot", "cold", "issiq", "hot", ("горячий", "горячая", "горячее", "горячие"), "emoji:🔥"),
    ("cold", "hot", "sovuq", "cold", ("холодный", "холодная", "холодное", "холодные"), "emoji:❄️"),
    ("happy", "sad", "xursand", "happy", ("весёлый", "весёлая", "весёлое", "весёлые"), "emoji:😀"),
    ("sad", "happy", "xafa", "sad", ("грустный", "грустная", "грустное", "грустные"), "emoji:😞"),
    ("fast", "slow", "tez", "fast", ("быстрый", "быстрая", "быстрое", "быстрые"), "emoji:🐇"),
    ("slow", "fast", "sekin", "slow", ("медленный", "медленная", "медленное", "медленные"), "emoji:🐢"),
    ("old", "young", "qari", "old", ("старый", "старая", "старое", "старые"), "emoji:👴"),
    ("young", "old", "yosh", "young", ("молодой", "молодая", "молодое", "молодые"), "emoji:🧒"),
    ("open", "closed", "ochiq", "open", ("открытый", "открытая", "открытое", "открытые"), "emoji:🔓"),
    ("closed", "open", "yopiq", "closed", ("закрытый", "закрытая", "закрытое", "закрытые"), "emoji:🔒"),
    ("loud", "quiet", "baland", "loud", ("громкий", "громкая", "громкое", "громкие"), "emoji:🔊"),
    ("quiet", "loud", "past", "quiet", ("тихий", "тихая", "тихое", "тихие"), "emoji:🔈"),
]
# Yo'nalish so'zlari (ravish) — sifat o'yinida juft sifatida.
DIRECTIONS = [
    ("up", "down", "yuqoriga", "up", ("вверх",) * 4, "emoji:⬆️"),
    ("down", "up", "pastga", "down", ("вниз",) * 4, "emoji:⬇️"),
]

COLOR_FORMS = {
    "red": ("красный", "красная", "красное", "красные"),
    "yellow": ("жёлтый", "жёлтая", "жёлтое", "жёлтые"),
    "green": ("зелёный", "зелёная", "зелёное", "зелёные"),
    "blue": ("синий", "синяя", "синее", "синие"),
    "orange": ("оранжевый", "оранжевая", "оранжевое", "оранжевые"),
    "purple": ("фиолетовый", "фиолетовая", "фиолетовое", "фиолетовые"),
    "pink": ("розовый", "розовая", "розовое", "розовые"),
    "brown": ("коричневый", "коричневая", "коричневое", "коричневые"),
    "black": ("чёрный", "чёрная", "чёрное", "чёрные"),
    "white": ("белый", "белая", "белое", "белые"),
}

# ------------------------------------------------------------------ iboralar
# id, sahna (emoji'lar), uz, en, ru, yosh
PHRASES = [
    ("hello", ["🙂", "👋"], "Salom!", "Hello!", "Привет!", 4),
    ("goodbye", ["👋", "🚪"], "Xayr!", "Goodbye!", "До свидания!", 4),
    ("thank_you", ["🎁", "😊"], "Rahmat!", "Thank you!", "Спасибо!", 4),
    ("yes", ["👍"], "Ha", "Yes", "Да", 4),
    ("no", ["👎"], "Yo‘q", "No", "Нет", 4),
    ("good_morning", ["🌅", "🙂"], "Xayrli tong!", "Good morning!", "Доброе утро!", 6),
    ("good_night", ["🌙", "😴"], "Xayrli tun!", "Good night!", "Спокойной ночи!", 6),
    ("sorry", ["😔"], "Kechirasiz!", "Sorry!", "Извини!", 6),
    ("birthday", ["🎂", "🎈"], "Tug‘ilgan kuning bilan!", "Happy birthday!", "С днём рождения!", 6),
    ("how_are_you", ["🙂", "❓"], "Qalaysan?", "How are you?", "Как дела?", 6),
    ("please", ["🍪", "🤲"], "Iltimos", "Please", "Пожалуйста", 6),
    ("well_done", ["⭐", "👏"], "Barakalla!", "Well done!", "Молодец!", 6),
]

# ------------------------------------------------------------------ rus tilida so'z jinsi
RU_SOFT = {  # -ь bilan tugaydiganlar
    "морковь": "f", "картофель": "m", "мышь": "f", "лошадь": "f", "медведь": "m", "лебедь": "m",
    "корабль": "m", "пельмень": "m", "кость": "f", "дверь": "f", "кровать": "f", "тетрадь": "f",
    "дождь": "m", "огонь": "m", "учитель": "m", "строитель": "m", "соль": "f", "олень": "m",
    "голубь": "m", "мишень": "f", "календарь": "m", "карусель": "f", "медаль": "f", "мечеть": "f",
}
RU_EXCEPTIONS = {
    "папа": "m", "дедушка": "m", "мишка": "m", "такси": "n", "кенгуру": "m",
    "ворота": "pl", "часы": "pl", "ножницы": "pl", "блины": "pl", "счёты": "pl", "брюки": "pl",
    "перчатки": "pl", "носки": "pl", "кроссовки": "pl", "очки": "pl", "краски": "pl", "книги": "pl",
    "санки": "pl", "коньки": "pl", "наушники": "pl", "салют": "m",
}
RU_UNKNOWN = {"киви", "брокколи"}  # o'zgarmas, jinsi aniq emas — sifat bilan ishlatilmaydi


def ru_gender(word):
    if " " in word or word in RU_UNKNOWN:
        return None
    if word in RU_EXCEPTIONS:
        return RU_EXCEPTIONS[word]
    last = word[-1]
    if last == "ь":
        return RU_SOFT[word]  # KeyError — yangi so'z qo'shilsa ro'yxatga qo'shish shart
    if last in "ая":
        return "f"
    if last in "оеё":
        return "n"
    if last in "иы":
        return "pl"
    if last in "уюэ":
        return None
    return "m"


# ------------------------------------------------------------------ inglizcha ko'plik
EN_UNCOUNTABLE = {
    "bread", "rice", "cheese", "milk", "honey", "soup", "salad", "popcorn", "water", "tea",
    "chocolate", "grass", "snow", "rain", "wheat", "yarn", "paper", "corn", "broccoli", "cabbage",
    "wind", "fire", "sand", "fries", "noodles", "pancakes", "grapes", "scissors", "glasses", "jeans",
    "headphones", "sunglasses", "trousers", "socks", "sneakers", "gloves", "boots", "paints", "books",
    "desert", "lightning", "muscle", "family", "fireworks", "drink", "ice cream", "lemonade",
}
EN_IRREGULAR = {
    "mouse": "mice", "sheep": "sheep", "fish": "fish", "child": "children", "tooth": "teeth",
    "foot": "feet", "deer": "deer", "goose": "geese", "ox": "oxen", "leaf": "leaves", "wolf": "wolves",
    "knife": "knives", "scarf": "scarves", "potato": "potatoes", "tomato": "tomatoes", "mango": "mangoes",
    "volcano": "volcanoes", "hippo": "hippos", "piano": "pianos", "kangaroo": "kangaroos",
    "man": "men", "woman": "women", "person": "people", "bus": "buses", "octopus": "octopuses",
    "cactus": "cactuses", "dice": "dice",
}


def en_plural(word):
    if " " in word or word in EN_UNCOUNTABLE:
        return None
    if word in EN_IRREGULAR:
        return EN_IRREGULAR[word]
    if re.search(r"(s|x|z|ch|sh)$", word):
        return word + "es"
    if re.search(r"[^aeiou]y$", word):
        return word[:-1] + "ies"
    return word + "s"


# ------------------------------------------------------------------ rus bo'g'inlari (ochiq bo'g'in)
RU_CONS = "бвгджзйклмнпрстфхцчшщ"
CV = re.compile(r"^[%s]?[%s](?:[%s][%s])*[%s]?$" % (RU_CONS, "аеёиоуыэюя", RU_CONS, "аеёиоуыэюя", RU_CONS))


def ru_syllables(word):
    """Faqat bir ma'noli holatlar: undoshlar yonma-yon kelmaydi (ма-ши-на, со-ба-ка, ба-нан)."""
    if " " in word or not CV.match(word):
        return None
    sy, cur = [], ""
    i = 0
    while i < len(word):
        cur += word[i]
        if word[i] in RU_VOWELS:
            # Keyingi undosh + unli bo'lsa, undosh keyingi bo'g'inga o'tadi.
            rest = word[i + 1:]
            if not rest or (len(rest) >= 2 and rest[0] in RU_CONS and rest[1] in RU_VOWELS) or rest[0] in RU_VOWELS:
                sy.append(cur)
                cur = ""
            elif len(rest) == 1:  # oxirgi undosh shu bo'g'inga
                cur += rest
                sy.append(cur)
                cur = ""
                i += 1
        i += 1
    if cur:
        sy[-1] += cur
    assert "".join(sy) == word, (word, sy)
    return sy


# ------------------------------------------------------------------ yig'ish
def forms(t):
    return {"m": t[0], "f": t[1], "n": t[2], "pl": t[3]}


out = {
    "schemaVersion": 1,
    "note": "Ingliz va rus tili modullari uchun original ma'lumotlar (lexicon.json ID'lari bilan).",
    "en": {
        "alphabet": [
            {"upper": u, "lower": u.lower(), "vowel": u.lower() in EN_VOWELS, "lexId": lid,
             "initial": BY_ID[lid]["en"].lower().startswith(u.lower())}
            for u, lid in EN_ALPHABET
        ],
    },
    "ru": {
        "alphabet": [
            {"upper": u, "lower": u.lower(), "vowel": u.lower() in RU_VOWELS, "lexId": lid, "initial": ini}
            for u, lid, ini in RU_ALPHABET
        ],
    },
    "actions": [
        {"id": i, "emoji": e, "uz": uz, "uzNow": uzn, "en": en, "enIng": ing, "ru": ru, "ruNow": run, "ageMin": a}
        for i, e, uz, uzn, en, ing, ru, run, a in ACTIONS
    ],
    "animalActions": [
        {"id": i, "en": en, "ru": ru, "context": c, "cats": cats, "tag": tag}
        for i, en, ru, c, cats, tag in ANIMAL_ACTIONS
    ],
    "adjectives": [
        {"id": i, "pair": p, "uz": uz, "en": en, "ru": forms(ru), "visual": v}
        for i, p, uz, en, ru, v in ADJECTIVES + DIRECTIONS
    ],
    "colorForms": {k: forms(v) for k, v in COLOR_FORMS.items()},
    "phrases": [
        {"id": i, "scene": sc, "uz": uz, "en": en, "ru": ru, "ageMin": a} for i, sc, uz, en, ru, a in PHRASES
    ],
    "ruGender": {},
    "enPlural": {},
    "ruSyllables": {},
}

for e in ENTRIES:
    g = ru_gender(e["ru"])
    if g:
        out["ruGender"][e["id"]] = g
    p = en_plural(e["en"])
    if p:
        out["enPlural"][e["id"]] = p
    s = ru_syllables(e["ru"])
    if s:
        out["ruSyllables"][e["id"]] = s

# ------------------------------------------------------------------ tekshiruvlar
lex_emoji = {e["emoji"] for e in lex["entries"]}
act_emoji = [a["emoji"] for a in out["actions"]]
assert len(set(act_emoji)) == len(act_emoji), "harakat emoji takrorlandi"
assert not (set(act_emoji) & lex_emoji), set(act_emoji) & lex_emoji
for lang in ("en", "ru"):
    for L in out[lang]["alphabet"]:
        if L["lexId"]:
            assert L["lexId"] in BY_ID, L
for L in out["ru"]["alphabet"]:
    if L["lexId"]:
        w = BY_ID[L["lexId"]]["ru"]
        assert L["lower"] in w, (L, w)
        if L["initial"]:
            assert w.startswith(L["lower"]), (L, w)
assert len(out["en"]["alphabet"]) == 26 and len(out["ru"]["alphabet"]) == 33
for a in out["adjectives"]:
    assert a["pair"] in {x["id"] for x in out["adjectives"]}

path = os.path.join(DATA, "languages.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(len(out["actions"]), "actions,", len(out["adjectives"]), "adjectives,", len(out["phrases"]), "phrases,",
      len(out["ruGender"]), "ru genders,", len(out["enPlural"]), "en plurals,", len(out["ruSyllables"]), "ru syllable words")
