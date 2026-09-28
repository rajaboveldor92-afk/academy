"""Onaning klonlangan ovozida gaplarni tayyorlash (OmniVoice, o'zbek tili, zero-shot).

GitHub Actions'da (CPU) bo'laklab ishlaydi:  python tool/voice/generate.py --shard 3 --shards 20
Kirish: tool/voice/out/lines.json. Chiqish: tool/voice/out/klon/<kalit>.m4a va shard_<n>.json (hisobot).

* Referens — onaning haqiqiy yozuvidan ikki ibora (matni bilan), model ovoz tembrini shundan oladi.
* Har gap uchun barqaror urug' (seed) — qayta ishga tushirilsa natija bir xil.
* Sifat nazorati: davomiylik matn uzunligiga mos kelmasa yoki ovoz juda past bo'lsa — boshqa urug' bilan qayta.
* Ovoz balandligi onaning yozuvlari bilan tenglashtiriladi; AAC 32 kbit/s (m4a) — Android'da hamma joyda ijro etiladi.
"""
import argparse
import json
import os
import subprocess
import sys
import time

import numpy as np
import soundfile as sf
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uz_spoken import spoken  # noqa: E402
from voice_keys import key_for  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ONA = os.path.join(ROOT, "assets", "audio", "uz", "ona")
SR = 24000
REF_KEYS = ["narsalarni_sanab_kor", "bugun_yaxshi_harakat"]
TARGET_RMS = 0.157  # onaning yozuvlari (faol qism) o'rtacha darajasi
PEAK = 0.89
CHARS_PER_SEC = 13.5


def load_ogg(path):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def reference():
    clips = {k: t for k, _, _, t in json.load(open(os.path.join(ROOT, "tool", "audio", "mother_voice_clips.json")))["clips"]}
    gap = np.zeros(int(0.35 * SR), dtype=np.float32)
    parts = []
    for i, k in enumerate(REF_KEYS):
        if i:
            parts.append(gap)
        parts.append(load_ogg(os.path.join(ONA, k + ".ogg")))
    return np.concatenate(parts), " ".join(clips[k] for k in REF_KEYS)


def active_rms(y):
    act = y[np.abs(y) > 0.01]
    return float(np.sqrt(np.mean(act ** 2))) if act.size else 0.0


def trim(y, thr=0.008, pad=0.08):
    idx = np.where(np.abs(y) > thr)[0]
    if idx.size == 0:
        return y
    a = max(0, idx[0] - int(pad * SR))
    b = min(len(y), idx[-1] + int(pad * SR))
    return y[a:b]


def level(y):
    r = active_rms(y)
    if r > 0:
        y = y * (TARGET_RMS / r)
    peak = float(np.abs(y).max()) if y.size else 0.0
    if peak > PEAK:
        y = y * (PEAK / peak)
    return y.astype(np.float32)


def plausible(text, y):
    dur = len(y) / SR
    expected = max(0.6, len(text) / CHARS_PER_SEC)
    return 0.45 * expected <= dur <= 2.3 * expected and active_rms(y) > 0.02, round(dur, 2), round(expected, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--shards", type=int, default=1)
    ap.add_argument("--steps", type=int, default=16)
    ap.add_argument("--budget-min", type=float, default=280, help="shu vaqtdan keyin to'xtaydi (natija saqlanib qoladi)")
    ap.add_argument("--lines", default=os.path.join(ROOT, "tool", "voice", "out", "lines.json"))
    ap.add_argument("--out", default=os.path.join(ROOT, "tool", "voice", "out"))
    args = ap.parse_args()

    from omnivoice import OmniVoice

    lines = json.load(open(args.lines))["lines"]
    mine = [l for i, l in enumerate(lines) if i % args.shards == args.shard]
    out_dir = os.path.join(args.out, "klon")
    os.makedirs(out_dir, exist_ok=True)
    torch.set_num_threads(os.cpu_count() or 4)

    t0 = time.time()
    model = OmniVoice.from_pretrained("k2-fsa/OmniVoice", device_map="cpu", dtype=torch.float32)
    ref, ref_text = reference()
    prompt = model.create_voice_clone_prompt(ref_audio=(torch.from_numpy(ref).unsqueeze(0), SR), ref_text=ref_text)
    report = {"shard": args.shard, "shards": args.shards, "steps": args.steps, "load_s": round(time.time() - t0, 1), "items": []}
    print(f"shard {args.shard}/{args.shards}: {len(mine)} ta gap, model {report['load_s']} s", flush=True)

    for n, line in enumerate(mine):
        if time.time() - t0 > args.budget_min * 60:
            print("vaqt tugadi — qolganlari keyingi safar", flush=True)
            report["stopped_at"] = n
            break
        text, key = line["text"], line["key"]
        assert key_for(text) == key, text
        target = os.path.join(out_dir, key + ".m4a")
        if os.path.exists(target):
            continue
        # Model raqam va belgilarni so'z bilan o'qiydi; fayl kaliti esa ilovadagi asl matndan.
        say = spoken(text)
        seed = int(key[:8], 16)
        t = time.time()
        best = None
        for attempt in range(3):
            torch.manual_seed(seed + attempt)
            np.random.seed((seed + attempt) % (2 ** 32))
            y = model.generate(text=say, language="uz", voice_clone_prompt=prompt, num_step=args.steps)[0]
            y = trim(np.asarray(y, dtype=np.float32))
            ok, dur, expected = plausible(say, y)
            best = (y, attempt, ok, dur, expected)
            if ok:
                break
        y, attempt, ok, dur, expected = best
        wav = os.path.join(out_dir, key + ".wav")
        sf.write(wav, level(y), SR)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-c:a", "aac", "-b:a", "32k", "-ac", "1", "-ar", str(SR),
                        "-movflags", "+faststart", target], check=True)
        os.remove(wav)
        item = {"key": key, "text": text, "dur": dur, "expected": expected, "retries": attempt, "ok": ok,
                "gen_s": round(time.time() - t, 1)}
        report["items"].append(item)
        print(f"[{n + 1}/{len(mine)}] {item}", flush=True)
        if (n + 1) % 10 == 0:
            json.dump(report, open(os.path.join(args.out, f"shard_{args.shard}.json"), "w"), ensure_ascii=False, indent=0)
    report["total_s"] = round(time.time() - t0, 1)
    json.dump(report, open(os.path.join(args.out, f"shard_{args.shard}.json"), "w"), ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main()
