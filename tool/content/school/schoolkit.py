"""Maktab fanlari dasturlari va savollar bankini yig'ish uchun umumiy yordamchilar.

Har bir fan fayli (masalan, `onatili_g3.py`) mavzular ro'yxatini tuzadi va `write(...)` ni chaqiradi:

    from schoolkit import *
    T = Course("onatili", 3, L("Ona tili", "Native language", "Родной язык"))
    T.topic("unli", "🔤", L("Unli va undosh", "Vowels and consonants", "Гласные и согласные"),
            chapter="1-chorak. Tovush va harf",
            theory="Unli tovushlar: a, o, u, e, i, o‘. ...",
            items=[
                Q("Qaysi harf unli?", "o", ["b", "k", "t", "m"]),
                TF("“Kitob” so‘zida ikkita unli bor.", True),
                ORDER("So‘zlardan gap tuzing", "Men kitob o‘qiyman"),
                MATCH("Juftini toping", [("katta", "kichik"), ("issiq", "sovuq"), ("baland", "past")]),
            ])
    T.test("test1", L("1-nazorat ishi", "Test 1", "Контрольная работа 1"), ["unli", ...], chapter=...)
    T.write()

Natija: `assets/data/school/<fan>_g<N>.json` (dastur) va `assets/data/school/bank_<fan>_g<N>.json` (savollar).

Savol turlari:
* Q(savol, javob, [noto'g'ri javoblar], d=1, x=izoh, h=maslahat, e=emoji, text=o'qish matni, say=ovozli matn, lang=til)
* TF(fikr, True/False, ...) — to'g'ri yoki noto'g'ri.
* ORDER(ko'rsatma, "to'g'ri gap", extra=[ortiqcha so'zlar], sep=" ") — so'zlardan gap yig'ish.
* MATCH(ko'rsatma, [(chap, o'ng), ...]) — juftlash (har safar 3–5 juft tanlanadi).

`d` — qiyinlik: 1-daraja faqat d=1, 2-daraja d≤2, 3-daraja — hammasi.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

APOSTROPHE_BAD = re.compile(r"(?<![A-Za-z])(?:[a-zA-Z]*[oOgG])['`ʻʼ](?=[a-z])")


def L(uz, en, ru):
    return {"uz": uz, "en": en, "ru": ru}


def _clean(item):
    return {k: v for k, v in item.items() if v is not None and v != [] and v != ""}


def Q(q, a, w, d=1, x=None, h=None, e=None, text=None, say=None, lang=None):
    return _clean({"t": "choice", "q": q, "a": str(a), "w": [str(v) for v in w], "d": d, "x": x, "h": h,
                   "e": e, "text": text, "say": say, "lang": lang})


def TF(q, a, d=1, x=None, h=None, e=None, text=None, say=None, lang=None):
    return _clean({"t": "tf", "q": q, "a": bool(a), "d": d, "x": x, "h": h, "e": e, "text": text,
                   "say": say, "lang": lang})


def ORDER(q, answer, d=1, extra=None, sep=" ", x=None, h=None, e=None, say=None, lang=None):
    parts = answer.split(sep) if sep else list(answer)
    return _clean({"t": "order", "q": q, "parts": parts, "extra": extra or [], "sep": sep, "d": d,
                   "x": x, "h": h, "e": e, "say": say, "lang": lang})


def MATCH(q, pairs, d=1, x=None, h=None, lang=None):
    return _clean({"t": "match", "q": q, "pairs": [[str(a), str(b)] for a, b in pairs], "d": d, "x": x, "h": h,
                   "lang": lang})


class Course:
    def __init__(self, subject, grade, title, model="QOIDA → MISOL → MASHQ → NAZORAT"):
        self.subject = subject
        self.grade = grade
        self.title = title
        self.model = model
        self.topics = []
        self.items = []
        self._code = 0

    def _id(self, key):
        return f"{self.subject}_g{self.grade}.{key}"

    def topic(self, key, emoji, title, chapter, theory, items=None, gen="bank", levels=None, prereq=None):
        """Mavzu: `items` berilsa — savollar banki (`bank` generatori), aks holda [gen] + [levels]."""
        self._code += 1
        if items is not None:
            gen = "bank"
            # 1-darajada kamida 8 ta savol bo'lsin: yetmasa, eng oson (d=2) savollar 1-darajaga o'tkaziladi.
            easy = sum(1 for it in items if it.get("d", 1) <= 1)
            for it in items:
                if easy >= 8:
                    break
                if it.get("d", 1) == 2:
                    it["d"] = 1
                    easy += 1
            levels = levels or [{"options": 3}, {"options": 4}, {"options": 4}]
            for n, it in enumerate(items, 1):
                self.items.append({"topic": self._id(key), "id": f"{key}_{n}", **it})
        assert levels and len(levels) == 3, f"{key}: 3 daraja kerak"
        self.topics.append({
            "id": self._id(key),
            "code": str(self._code),
            "emoji": emoji,
            "title": title,
            "generator": gen,
            "skill": gen,
            "chapter": chapter,
            "prerequisites": [self._id(p) for p in (prereq or [])],
            "levels": levels,
            "theory": {"uz": theory.strip()},
        })

    def test(self, key, title, topics, chapter, level=2, size=10):
        self.topics.append({
            "id": self._id(key),
            "code": "N" if key != "final" else "Y",
            "emoji": "📝",
            "title": title,
            "generator": "test",
            "skill": "test",
            "chapter": chapter,
            "prerequisites": [],
            "lessonSize": size,
            "levels": [{"topics": [self._id(t) for t in topics], "level": min(3, max(1, l + level - 2))} for l in (1, 2, 3)],
        })

    def check(self):
        ids = {t["id"] for t in self.topics}
        by_topic = {}
        for it in self.items:
            by_topic.setdefault(it["topic"], []).append(it)
        problems = []
        for t in self.topics:
            if t["generator"] == "test":
                for lv in t["levels"]:
                    for ref in lv["topics"]:
                        if ref not in ids:
                            problems.append(f"{t['id']}: yo‘q mavzu {ref}")
                continue
            if t["generator"] == "bank":
                items = by_topic.get(t["id"], [])
                if len(items) < 15:
                    problems.append(f"{t['id']}: faqat {len(items)} ta savol (kamida 15)")
                if sum(1 for i in items if i.get("d", 1) <= 1) < 8:
                    problems.append(f"{t['id']}: 1-darajada 8 tadan kam savol")
        seen = set()
        for it in self.items:
            key = (it["topic"], it.get("q"), it.get("text"), it.get("a"), tuple(it.get("parts", [])), it.get("say"))
            if key in seen:
                problems.append(f"{it['topic']}: takroriy savol {it.get('q')} / {it.get('a')}")
            seen.add(key)
            if it["t"] == "choice":
                if it["a"] in it["w"]:
                    problems.append(f"{it['topic']}: javob noto‘g‘rilar ichida: {it['q']} → {it['a']}")
                if len(set(it["w"])) < 2:
                    problems.append(f"{it['topic']}: kamida 2 ta noto‘g‘ri javob kerak: {it['q']}")
            if it["t"] == "match" and len(it["pairs"]) < 3:
                problems.append(f"{it['topic']}: juftlar kam: {it['q']}")
            if it["t"] == "match":
                lefts = [p[0] for p in it["pairs"]]
                rights = [p[1] for p in it["pairs"]]
                if len(set(lefts)) != len(lefts) or len(set(rights)) != len(rights):
                    problems.append(f"{it['topic']}: juftlarda takror: {it['q']}")
            if it["t"] == "order" and len(it["parts"]) < 2:
                problems.append(f"{it['topic']}: bo‘laklar kam: {it['q']}")
            for field in ("q", "x", "h", "text"):
                v = it.get(field)
                if isinstance(v, str) and APOSTROPHE_BAD.search(v) and it.get("lang") not in ("en", "ru"):
                    problems.append(f"{it['topic']}: o‘/g‘ harfi noto‘g‘ri belgi bilan: {v}")
        for t in self.topics:
            th = (t.get("theory") or {}).get("uz", "")
            if APOSTROPHE_BAD.search(th):
                problems.append(f"{t['id']}: qoidada o‘/g‘ noto‘g‘ri belgi bilan")
        if problems:
            raise SystemExit("\n".join(problems))

    def write(self):
        self.check()
        data = {
            "subject": self.subject,
            "ageGroup": f"g{self.grade}",
            "lessonSize": 8,
            "title": self.title,
            "model": self.model,
            "topics": self.topics,
        }
        base = os.path.join(ROOT, "assets", "data", "school")
        name = f"{self.subject}_g{self.grade}"
        with open(os.path.join(base, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        if self.items:
            with open(os.path.join(base, f"bank_{name}.json"), "w", encoding="utf-8") as f:
                json.dump({"items": self.items}, f, ensure_ascii=False, indent=1)
        import build_index  # noqa: E402 — ro'yxatni yangilash (yangi fayl ilovaga avtomatik qo'shiladi)
        build_index.build()
        banks = sum(1 for t in self.topics if t["generator"] == "bank")
        print(f"{name}: {len(self.topics)} mavzu ({banks} bank), {len(self.items)} savol")
