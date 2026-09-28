"""Model uchun o'qiladigan matn: raqam va belgilar o'zbekcha so'z bilan (fayl kaliti asl matndan olinadi).

`lib/learning/content/uz_numbers.dart` va `InstructionBank.joinUzNumberSuffixes` bilan bir xil qoidalar.
"""
import re

ONES = ["nol", "bir", "ikki", "uch", "to‘rt", "besh", "olti", "yetti", "sakkiz", "to‘qqiz"]
TENS = ["", "o‘n", "yigirma", "o‘ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to‘qson"]


def word(n: int) -> str:
    if n < 10:
        return ONES[n]
    if n < 100:
        t, o = TENS[n // 10], n % 10
        return t if o == 0 else f"{t} {ONES[o]}"
    if n < 1000:
        h, rest = n // 100, n % 100
        head = "yuz" if h == 1 else f"{ONES[h]} yuz"
        return head if rest == 0 else f"{head} {word(rest)}"
    if n == 1000:
        return "ming"
    return str(n)


_NUM = "nol|bir|ikki|uch|to‘rt|besh|olti|yetti|sakkiz|to‘qqiz|o‘n|yigirma|o‘ttiz|qirq|ellik|oltmish|yetmish|sakson|to‘qson|yuz|ming"
_SUFFIX = re.compile(f"(^|[^A-Za-z‘’ʻ])({_NUM}) (ta|tadan|tasini|tasi|ga|gacha|ni|ning|dan|da)(?=$|[^A-Za-z‘’ʻ])", re.I)


def _join(m):
    w, s = m[2], m[3]
    last = w[-1].lower()
    if s.startswith("g") and last in "kq":
        s = last + s[1:]
    if w.lower() == "bir" and s.startswith("ta"):
        return m[1] + w[0] + "it" + s
    return m[1] + w + s


def _suffix_after(w: str, suffix: str) -> str:
    last = w[-1].lower()
    if suffix.startswith("g") and last in "kq":
        suffix = last + suffix[1:]
    return w + suffix


def spoken(text: str) -> str:
    s = text
    s = re.sub(r"\((\w)(\d+)–(\w)(\d+)\)", lambda m: f"({m[1]} {word(int(m[2]))}dan {m[3]} {_suffix_after(word(int(m[4])), 'gacha')})", s)
    s = re.sub(r"(\d+)\s*[–-]\s*(\d+)", lambda m: f"{_suffix_after(word(int(m[1])), 'dan')} {_suffix_after(word(int(m[2])), 'gacha')}", s)
    s = re.sub(r"(\d+)\s*×\s*(\d+)", lambda m: f"{word(int(m[1]))} karra {word(int(m[2]))}", s)
    s = re.sub(r"([A-Za-z])(\d)", r"\1 \2", s)
    s = re.sub(r"\d+", lambda m: word(int(m[0])), s)
    s = s.replace("+", " qo‘shuv ").replace("−", " ayiruv ").replace("=", " teng ")
    s = re.sub(r"\s+", " ", s).strip()
    return _SUFFIX.sub(_join, s)


if __name__ == "__main__":
    for t in ["Yangi medal: 3 kun ketma-ket!", "1–10 sonlar", "Sonlar 1–20", "3×3 matritsa", "Qator va ustun (a1–h8)",
              "10 tadan sanash", "0 dan 100 gacha", "1 dan 3 gacha", "Yangi medal: 1000 yulduz!", "Figuralar 3 tilda",
              "Yangi medal: 10 ta bugungi dars!", "20 ichida qo‘shish"]:
        print(t, "→", spoken(t))
