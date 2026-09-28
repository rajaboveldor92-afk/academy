"""Klonlangan ovozda tayyorlanadigan gaplarni tanlaydi.

Kirish: tool/voice/out/speech_uz.json (dump_speech_test.dart). Chiqish: tool/voice/out/lines.json.
* Ekran gaplari (fan va mavzu nomlari, medal, sovg'a, maqtov) — hammasi;
* qolgani — eng ko'p uchraydigan mashq ko'rsatmalari, jami LIMIT tagacha;
* onaning haqiqiy iborasiga mos gaplar va harfsiz (faqat emoji) matnlar tashlab ketiladi.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from voice_keys import key_for, normalize  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIMIT = int(os.environ.get("VOICE_LIMIT", "3000"))

mother = {normalize(t).lower() for _, _, _, t in json.load(open(os.path.join(ROOT, "tool", "audio", "mother_voice_clips.json")))["clips"]}
items = json.load(open(os.path.join(ROOT, "tool", "voice", "out", "speech_uz.json")))["items"]

forced, ranked, seen = [], [], set()
for it in items:
    text = normalize(it["text"])
    if not re.search(r"[A-Za-z]", text) or text.lower() in mother:
        continue
    k = key_for(text)
    if k in seen:
        continue
    seen.add(k)
    row = {"key": k, "text": text, "n": it["n"], "src": it["src"]}
    (forced if it["src"] in ("ui", "subject", "topic_title") else ranked).append(row)

lines = forced + ranked[: max(0, LIMIT - len(forced))]
json.dump({"count": len(lines), "lines": lines}, open(os.path.join(ROOT, "tool", "voice", "out", "lines.json"), "w"), ensure_ascii=False, indent=0)
covered = sum(r["n"] for r in ranked[: max(0, LIMIT - len(forced))])
total = sum(r["n"] for r in ranked)
print(f"lines: {len(lines)} (ekran: {len(forced)}), mashqlar qamrovi: {100 * covered / max(1, total):.1f}%")
