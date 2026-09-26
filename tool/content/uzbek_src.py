# O'zbek tili ma'lumotlari: `python3 tool/content/uzbek_src.py` -> assets/data/uzbek.json
# * alifbo (29 harf, lotin), har bir harfga rasmli so'z (lexicon id);
# * 500+ so'z bazasi: lug'atdagi rasmli so'zlar + rasmsiz so'zlar (o'qish mashqlari uchun);
# * har bir so'z avtomatik bo'g'inlarga ajratiladi (o'zbek bo'g'in qoidalari);
# * gap va hikoyalar uchun original shablon resurslari.
import json, os, re

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "data")
lex = json.load(open(os.path.join(BASE, "lexicon.json"), encoding="utf-8"))
entries = [e for e in lex["entries"] if e["ageMin"] < 99]

VOWELS = {"a", "e", "i", "o", "u", "o‘"}
DIGRAPHS = ["o‘", "g‘", "sh", "ch", "ng"]
LETTERS = set("abdefghijklmnopqrstuvxyz") | {"o‘", "g‘", "sh", "ch", "ng", "ʼ"}

def tokens(word):
    w = word.lower()
    out, i = [], 0
    while i < len(w):
        if w[i] == "ʼ":
            out[-1] += "ʼ"; i += 1; continue
        if w[i:i+3] == "ng‘":
            # "ng‘" = n + g‘ (qo‘ng‘iroq)
            out.append("n"); i += 1; continue
        two = w[i:i+2]
        if two in DIGRAPHS:
            # "ng" faqat keyin unli kelmasa yoki so'z ichida bo'lsa bitta harf; oddiylik uchun doim bitta.
            out.append(two); i += 2; continue
        out.append(w[i]); i += 1
    return out

def is_vowel(t):
    return t.rstrip("ʼ") in VOWELS

def syllabify(word):
    t = tokens(word)
    vidx = [i for i, x in enumerate(t) if is_vowel(x)]
    if len(vidx) <= 1:
        return [word]
    cuts = []
    for a, b in zip(vidx, vidx[1:]):
        k = b - a - 1
        if k >= 2 and t[b-1] == "y" and t[b-2] in {"p","l","b","v","m","t","k","d","f","s"}:
            # o'zlashma so'zlar: kom-pyu-ter, ver-to-lyot
            cuts.append(b - 2)
        else:
            cuts.append(b if k == 0 else (b - 1))
    parts, prev = [], 0
    for c in cuts:
        parts.append("".join(t[prev:c])); prev = c
    parts.append("".join(t[prev:]))
    # Asl harflar registri saqlansin.
    res, pos = [], 0
    for p in parts:
        res.append(word[pos:pos+len(p)]); pos += len(p)
    return res

def valid_word(w):
    ts = tokens(w)
    return all((x.rstrip("ʼ") in LETTERS) for x in ts) and any(is_vowel(x) for x in ts)

# ---------------------------------------------------------------- alifbo
ALPHABET = [
 ("A","a","bee"),("B","b","fish"),("D","d","tree"),("E","e","goat"),("F","f","elephant"),
 ("G","g","flower"),("H","h","hamster"),("I","i","dog"),("J","j","giraffe"),("K","k","book"),
 ("L","l","lemon"),("M","m","cat"),("N","n","bread"),("O","o","apple"),("P","p","tomato"),
 ("Q","q","bird"),("R","r","rocket"),("S","s","carrot"),("T","t","chicken"),("U","u","house"),
 ("V","v","bicycle"),("X","x","rooster"),("Y","y","star"),("Z","z","zebra"),("O‘","o‘","duck"),
 ("G‘","g‘","brick"),("Sh","sh","lion"),("Ch","ch","tea"),("Ng","ng","sunrise"),
]
byid = {e["id"]: e for e in entries}
alphabet = []
for up, lo, lid in ALPHABET:
    e = byid[lid]
    word = e["uz"]
    if up != "Ng":
        assert tokens(word)[0] == lo, (up, word)
    else:
        assert "ng" in tokens(word), word
    alphabet.append({"upper": up, "lower": lo, "vowel": lo in VOWELS, "lexId": lid, "word": word})

# ---------------------------------------------------------------- so'zlar
THEMES = {
 "family": "Men va oilam", "home": "Uy", "school": "Bog‘cha va maktab", "animal": "Hayvonlar",
 "bird": "Qushlar", "fruit": "Mevalar", "vegetable": "Sabzavotlar", "body": "Tana",
 "clothes": "Kiyim", "vehicle": "Transport", "toy": "O‘yinchoqlar", "nature": "Tabiat",
 "profession": "Kasblar", "food": "Taomlar", "insect": "Hasharotlar", "sea": "Suv jonivorlari",
 "place": "Joylar", "verb": "Harakatlar", "adjective": "Belgilar", "number": "Sonlar", "color": "Ranglar",
 "time": "Vaqt", "other": "Boshqa so‘zlar",
}

words = {}
def add(w, theme, lex_id=None, age=4):
    w = w.strip()
    if " " in w or not valid_word(w):
        return
    key = w.lower()
    if key in words:
        if lex_id and not words[key].get("lexId"):
            words[key]["lexId"] = lex_id
        return
    d = {"w": w, "syl": syllabify(w), "theme": theme, "age": age}
    if lex_id: d["lexId"] = lex_id
    words[key] = d

for e in entries:
    add(e["uz"], e["category"], e["id"], 4 if e["ageMin"] <= 4 else 6)
for c in lex["colors"]:
    add(c["uz"], "color", None, 4)

EXTRA = {
 "family": "bola qiz o‘g‘il aka uka opa singil amma xola amaki tog‘a do‘st qo‘shni mehmon bolalar ota ona dada oyi buva",
 "home": "xona deraza devor pol tom oshxona hovli stol gilam yostiq ko‘rpa choynak qozon pichoq sanchqi kosa patnis oyna javon shkaf chiroq zina darvoza kalit supurgi",
 "school": "sinf dars harf so‘z gap son rasm qo‘shiq o‘yin ertak sumka doska bo‘r parta tanaffus ustoz o‘quvchi kitobxona alifbo",
 "nature": "osmon yer suv havo bahor yoz kuz qish kun tun kech ko‘l daryo dala o‘rmon bog‘ tosh qum muz yomg‘ir qor tuproq ariq buloq tog‘ cho‘qqi",
 "time": "bugun ertaga kecha hafta soat daqiqa ertalab kechqurun",
 "adjective": "katta kichik uzun qisqa baland past issiq sovuq yangi eski shirin achchiq nordon tez sekin yaxshi chiroyli toza quvnoq xursand mehribon aqlli kuchli yumshoq qattiq og‘ir yengil keng tor to‘la bo‘sh semiz ozg‘in",
 "verb": "o‘qi yoz chiz sana o‘yna yugur sakra yur tur o‘tir kel ket ber ol ich ye uxla kul ayt eshit ko‘r qara top yasa yuv tara kiy och yop bor uch suz o‘rgan quv ushla tashla kut qo‘y",
 "number": "bir ikki uch to‘rt besh olti yetti sakkiz to‘qqiz o‘n yigirma yuz",
 "food": "osh palov somsa norin manti qatiq qaymoq sariyog‘ shakar murabbo kompot yong‘oq mayiz bodom o‘rik anor behi olcha tut shaftoli sho‘rva non go‘sht",
 "animal": "eshak buzoq qo‘zi toy kuchuk mushukcha tuyaqush bedana laylak qarg‘a chumchuq kabutar qo‘ng‘iz pashsha ilon tulki bo‘ri quyoncha",
 "body": "bosh soch qosh yuz lab bo‘yin yelka qorin orqa tizza barmoq tirnoq tovon kaft",
 "clothes": "do‘ppi chopon kamzul kalish yubka tugma cho‘ntak etik",
 "place": "yo‘l ko‘cha bekat bozor shahar qishloq bog‘cha maydon xiyobon",
 "other": "salom rahmat xayr ha yo‘q mana bu u men sen biz ular nima kim qayer qachon nechta",
}
for theme, s in EXTRA.items():
    for w in s.split():
        add(w, theme, None, 4 if len(w) <= 5 else 6)

wordlist = sorted(words.values(), key=lambda d: (d["theme"], d["w"]))
pict = [w for w in wordlist if w.get("lexId")]
# Tekshiruvlar
for d in wordlist:
    assert "".join(d["syl"]) == d["w"], d
    for s_ in d["syl"]:
        assert sum(1 for t in tokens(s_) if is_vowel(t)) == 1, d

# ---------------------------------------------------------------- gap resurslari
# Harakatlar: kim nima qilyapti (lexicon teg bo'yicha mos jonivor tanlanadi).
ACTIONS = [
 {"id":"flies","uz":"uchyapti","en":"is flying","ru":"летит","tag":"flies","cats":["bird","insect"]},
 {"id":"swims","uz":"suzyapti","en":"is swimming","ru":"плывёт","tag":"swims","cats":["sea","animal","bird"]},
 {"id":"runs","uz":"yuguryapti","en":"is running","ru":"бежит","tag":"has_legs","cats":["animal"]},
 {"id":"sleeps","uz":"uxlayapti","en":"is sleeping","ru":"спит","tag":"","cats":["animal","bird"]},
 {"id":"eats","uz":"ovqat yeyapti","en":"is eating","ru":"ест","tag":"","cats":["animal","bird"]},
]
PLACES = [
 {"id":"garden","uz":"bog‘ga","en":"to the garden","ru":"в сад","emoji":"🌳"},
 {"id":"school","uz":"maktabga","en":"to school","ru":"в школу","emoji":"🏫"},
 {"id":"shop","uz":"do‘konga","en":"to the shop","ru":"в магазин","emoji":"🏪"},
 {"id":"park","uz":"xiyobonga","en":"to the park","ru":"в парк","emoji":"🎡"},
 {"id":"market","uz":"bozorga","en":"to the market","ru":"на рынок","emoji":"🧺"},
]
NAMES = ["Ali","Nodira","Sardor","Malika","Bobur","Zarina","Jasur","Laylo","Kamola","Anvar"]

out = {
 "schemaVersion": 1,
 "note": "O‘zbek tili mashqlari uchun original ma'lumotlar. Bo‘g‘inlar avtomatik ajratilgan va tekshirilgan.",
 "vowels": sorted(VOWELS),
 "alphabet": alphabet,
 "themes": THEMES,
 "words": wordlist,
 "actions": ACTIONS,
 "places": PLACES,
 "names": NAMES,
}
json.dump(out, open(os.path.join(BASE, "uzbek.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("alphabet", len(alphabet), "words", len(wordlist), "picturable", len(pict),
      "4yo picturable", len([w for w in pict if w["age"] <= 4]))
print([ (w["w"], "-".join(w["syl"])) for w in wordlist[:40:4]])
