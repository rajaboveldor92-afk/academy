"""Maktab fanlari fayllari ro'yxati: assets/data/school/index.json.

Ilova shu ro'yxat bo'yicha dasturlar (`<fan>_g<sinf>.json`) va savollar banklarini (`bank_*.json`) yuklaydi.
Har bir dastur skripti (schoolkit.Course.write) oxirida avtomatik chaqiriladi; qo'lda: python3 tool/content/school/build_index.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BASE = os.path.join(ROOT, "assets", "data", "school")


def build():
    names = sorted(f[:-5] for f in os.listdir(BASE) if f.endswith(".json") and f != "index.json")
    data = {
        "curricula": [n for n in names if not n.startswith("bank_")],
        "banks": [n for n in names if n.startswith("bank_")],
    }
    with open(os.path.join(BASE, "index.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    return data


if __name__ == "__main__":
    d = build()
    print(f"index.json: {len(d['curricula'])} dastur, {len(d['banks'])} bank")
