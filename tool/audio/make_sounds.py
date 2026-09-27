"""Ilovaning original ovoz effektlari va fon musiqasini sintez qiladi (hech qanday tashqi namuna yo'q).

Natija:
  assets/audio/rewards/{tap,correct,tryAgain,star,medal}.ogg
  assets/audio/music/theme.ogg   — 8 taktlik yumshoq, uzluksiz aylanadigan kuy (C-dur pentatonika)

Ishga tushirish: python3 tool/audio/make_sounds.py   (numpy va ffmpeg/libvorbis kerak)
Natija deterministik: bir xil kod — bir xil fayllar.
"""
import os
import subprocess
import tempfile
import wave

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SR = 32000


def note(name):
    """'C5' → chastota (A4 = 440 Hz)."""
    names = {'C': -9, 'D': -7, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2}
    semis = names[name[0]] + (12 * (int(name[-1]) - 4))
    if '#' in name:
        semis += 1
    return 440.0 * 2 ** (semis / 12)


def env(n, attack=0.005, decay=4.0):
    t = np.arange(n) / SR
    a = np.clip(t / attack, 0, 1)
    return a * np.exp(-t * decay)


def bell(freq, dur, decay=6.0, partials=((1, 1.0), (2.0, 0.35), (3.0, 0.15), (4.2, 0.08))):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = sum(a * np.sin(2 * np.pi * freq * r * t) * np.exp(-t * decay * (1 + (r - 1) * 0.6)) for r, a in partials)
    return s * env(n, decay=0)


def marimba(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    body = np.sin(2 * np.pi * freq * t) * np.exp(-t * 5.5)
    click = 0.25 * np.sin(2 * np.pi * freq * 4 * t) * np.exp(-t * 40)
    return (body + click) * np.clip(t / 0.004, 0, 1)


def soft_square(freq, dur, decay=3.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(2 * np.pi * freq * 3 * t) + 0.12 * np.sin(2 * np.pi * freq * 5 * t)
    return s * env(n, attack=0.012, decay=decay)


def mix(total, parts):
    out = np.zeros(int(total * SR))
    for start, sig in parts:
        i = int(start * SR)
        j = min(len(out), i + len(sig))
        out[i:j] += sig[: j - i]
    return out


def fade_out(sig, dur=0.03):
    n = min(len(sig), int(dur * SR))
    sig[-n:] *= np.linspace(1, 0, n)
    return sig


def normalize(sig, peak_db=-3.0):
    peak = np.max(np.abs(sig)) or 1.0
    return sig / peak * (10 ** (peak_db / 20))


def write_ogg(sig, path, quality=4):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = (np.clip(sig, -1, 1) * 32767).astype('<i2')
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        wav_path = tmp.name
    with wave.open(wav_path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav_path, '-c:a', 'libvorbis', '-q:a', str(quality),
                    '-map_metadata', '-1', '-fflags', '+bitexact', path], check=True)
    os.remove(wav_path)
    print(f'{os.path.relpath(path, ROOT)}: {os.path.getsize(path)} bayt')


def effects():
    out = os.path.join(ROOT, 'assets', 'audio', 'rewards')
    # Bosish: qisqa yumshoq "pop".
    n = int(0.07 * SR)
    t = np.arange(n) / SR
    freq = 900 - 400 * t / t[-1]
    tap = np.sin(2 * np.pi * np.cumsum(freq) / SR) * env(n, attack=0.002, decay=45)
    write_ogg(fade_out(normalize(tap, -6)), os.path.join(out, 'tap.ogg'))
    # To'g'ri: ko'tariluvchi ikki qo'ng'iroq (G5 → C6 → E6).
    correct = mix(0.55, [(0.0, bell(note('G5'), 0.4, 7)), (0.08, bell(note('C6'), 0.45, 6)), (0.16, bell(note('E6'), 0.4, 6))])
    write_ogg(fade_out(normalize(correct, -4)), os.path.join(out, 'correct.ogg'))
    # Yana urin: yumshoq, qo'rqitmaydigan ikki ohang (E5 → C5).
    again = mix(0.45, [(0.0, soft_square(note('E5'), 0.25, 9)), (0.14, soft_square(note('C5'), 0.3, 8))])
    write_ogg(fade_out(normalize(again, -10)), os.path.join(out, 'tryAgain.ogg'))
    # Yulduz: tez ko'tariluvchi yaltiroq arpedjio.
    star = mix(0.8, [(0.06 * i, bell(note(n), 0.5, 7)) for i, n in enumerate(['C6', 'E6', 'G6', 'C7', 'E7'])])
    write_ogg(fade_out(normalize(star, -5)), os.path.join(out, 'star.ogg'))
    # Medal: kichik fanfar (C5 E5 G5 — C6).
    medal = mix(1.3, [
        (0.0, soft_square(note('C5'), 0.25, 5)), (0.13, soft_square(note('E5'), 0.25, 5)),
        (0.26, soft_square(note('G5'), 0.25, 5)), (0.42, soft_square(note('C6'), 0.85, 2.2)),
        (0.42, bell(note('C6'), 0.8, 3.5) * 0.6), (0.42, soft_square(note('E5'), 0.8, 2.5) * 0.5),
    ])
    write_ogg(fade_out(normalize(medal, -4)), os.path.join(out, 'medal.ogg'))


def music():
    """8 takt, 88 BPM: C – Am – F – G – C – Am – F G – C. Uzluksiz aylanish uchun oxiridagi
    "dum"lar boshiga qo'shiladi."""
    bpm = 88
    beat = 60 / bpm
    bars = 8
    total = bars * 4 * beat
    rng = np.random.default_rng(20260927)
    chords = [['C', 'E', 'G'], ['A', 'C', 'E'], ['F', 'A', 'C'], ['G', 'B', 'D'],
              ['C', 'E', 'G'], ['A', 'C', 'E'], ['F', 'A', 'C', 'G', 'B', 'D'], ['C', 'E', 'G']]
    roots = ['C3', 'A2', 'F2', 'G2', 'C3', 'A2', 'F2', 'C3']
    pent = ['C5', 'D5', 'E5', 'G5', 'A5', 'C6']
    parts = []
    for b in range(bars):
        start = b * 4 * beat
        # Bas: 1 va 3-hissada.
        root = roots[b]
        second = 'G2' if b == 6 else root
        parts.append((start, soft_square(note(root), 1.6 * beat, 2.2) * 0.35))
        parts.append((start + 2 * beat, soft_square(note(second), 1.6 * beat, 2.2) * 0.3))
        # Akkord (yumshoq, 2 va 4-hissada marimba); 7-taktda F → G.
        for k in (1, 3):
            tones = chords[b][3:] if (b == 6 and k == 3) else chords[b][:3]
            for tn in tones:
                parts.append((start + k * beat, marimba(note(tn + '4'), beat * 1.2) * 0.12))
        # Kuy: kuchli hissalarda akkord tovushi, orada pentatonika.
        chord_pent = [p for p in pent if p[0] in chords[b][:3]] or pent
        pos = 0.0
        while pos < 4:
            length = rng.choice([0.5, 0.5, 1.0, 1.0, 1.5]) if pos % 1 == 0 else 0.5
            length = min(length, 4 - pos)
            if b == bars - 1 and pos >= 2:
                parts.append((start + 2 * beat, marimba(note('C5'), 2 * beat) * 0.55))
                break
            strong = pos in (0.0, 2.0)
            pitch = rng.choice(chord_pent) if strong else rng.choice(pent)
            if rng.random() > 0.15 or strong:
                parts.append((start + pos * beat, marimba(note(pitch), max(length, 0.5) * beat * 1.4) * 0.5))
            pos += length
    n_total = int(total * SR)
    out = np.zeros(n_total + int(4 * SR))
    for st, sig in parts:
        i = int(st * SR)
        out[i:i + len(sig)] += sig
    loop = out[:n_total].copy()
    tail = out[n_total:]
    loop[:len(tail)] += tail[: len(loop)]
    write_ogg(normalize(loop, -2), os.path.join(ROOT, 'assets', 'audio', 'music', 'theme.ogg'), quality=2)


if __name__ == '__main__':
    effects()
    music()
