"""voice-clips release'idagi klon-*.zip fayllarini assets/audio/uz/klon/ ga yig'adi va hisobot beradi.

python3 tool/voice/collect.py <zip-lar papkasi> [lines.json]
"""
import glob
import json
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEST = os.path.join(ROOT, "assets", "audio", "uz", "klon")

src = sys.argv[1]
lines = json.load(open(sys.argv[2]))["lines"] if len(sys.argv) > 2 else []
os.makedirs(DEST, exist_ok=True)
items, got = [], set()
for z in sorted(glob.glob(os.path.join(src, "klon-*.zip"))):
    with zipfile.ZipFile(z) as f:
        for name in f.namelist():
            if name.startswith("klon/") and name.endswith(".m4a"):
                key = os.path.basename(name)[:-4]
                with f.open(name) as a, open(os.path.join(DEST, key + ".m4a"), "wb") as b:
                    shutil.copyfileobj(a, b)
                got.add(key)
            elif name.startswith("shard_") and name.endswith(".json"):
                items += json.load(f.open(name))["items"]
size = sum(os.path.getsize(p) for p in glob.glob(os.path.join(DEST, "*.m4a")))
bad = [i for i in items if not i["ok"]]
print(f"fayllar: {len(glob.glob(os.path.join(DEST, '*.m4a')))} (bu safar {len(got)}), hajm: {size / 1e6:.1f} MB")
print(f"shubhali (davomiylik mos emas): {len(bad)}, qayta urinish bilan: {sum(1 for i in items if i['retries'])}")
if items:
    print(f"o'rtacha vaqt: {sum(i['gen_s'] for i in items) / len(items):.1f} s/gap")
missing = [l for l in lines if l["key"] not in got and not os.path.exists(os.path.join(DEST, l["key"] + ".m4a"))]
print(f"yetishmaydi: {len(missing)}")
json.dump({"bad": bad, "missing": missing}, open(os.path.join(src, "collect_report.json"), "w"), ensure_ascii=False, indent=1)
