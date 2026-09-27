"""Onaning yozib olingan ovozini iboralarga bo'lib, ilova uchun tayyorlaydi.

  python3 tool/audio/cut_mother_voice.py path/to/Academy_ona_ovozi.mp3

Iboralar ro'yxati va vaqtlari: tool/audio/mother_voice_clips.json.
Natija: assets/audio/uz/ona/<kalit>.ogg (mono, 32 kHz, Vorbis). Har bir iboraning boshi va
oxiridagi jimlik olib tashlanadi, ovoz balandligi bir xil darajaga keltiriladi.
Ilovada ishlatilmaydigan iboralar (masalan, ssenariydagi bo'lim sarlavhasi) `skip` ro'yxatida.
"""
import json
import os
import subprocess
import sys
import tempfile
import wave

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'audio', 'uz', 'ona')
SR = 32000
# Ssenariydagi bo'lim sarlavhasi — bolaga aytilmaydi.
SKIP = {'ragbat_va_yakun'}


def load(path):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype='<i2').astype(np.float32) / 32768


def trim(x, lead=0.06, tail=0.12, thresh_db=-40):
    win = int(0.01 * SR)
    frames = len(x) // win
    rms = np.array([np.sqrt(np.mean(x[i * win:(i + 1) * win] ** 2)) for i in range(frames)])
    peak = rms.max() or 1e-9
    voiced = np.where(20 * np.log10(rms / peak + 1e-12) > thresh_db)[0]
    if len(voiced) == 0:
        return x
    a = max(0, voiced[0] * win - int(lead * SR))
    b = min(len(x), (voiced[-1] + 1) * win + int(tail * SR))
    return x[a:b]


def fade(x, fin=0.008, fout=0.04):
    x = x.copy()
    n1, n2 = int(fin * SR), int(fout * SR)
    x[:n1] *= np.linspace(0, 1, n1)
    x[-n2:] *= np.linspace(1, 0, n2)
    return x


def write_ogg(x, path):
    data = (np.clip(x, -1, 1) * 32767).astype('<i2')
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        wav_path = tmp.name
    with wave.open(wav_path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav_path, '-c:a', 'libvorbis', '-q:a', '5',
                    '-map_metadata', '-1', '-fflags', '+bitexact', path], check=True)
    os.remove(wav_path)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    audio = load(sys.argv[1])
    clips = json.load(open(os.path.join(ROOT, 'tool', 'audio', 'mother_voice_clips.json'), encoding='utf-8'))['clips']
    os.makedirs(OUT, exist_ok=True)
    # Bir xil balandlik: butun yozuvning eng baland nuqtasi −1.5 dB ga keltiriladi.
    gain = 10 ** (-1.5 / 20) / (np.max(np.abs(audio)) or 1)
    total = 0.0
    for key, start, end, _text in clips:
        if key in SKIP:
            continue
        x = trim(audio[int(start * SR):int(end * SR)])
        x = fade(x * gain)
        path = os.path.join(OUT, key + '.ogg')
        write_ogg(x, path)
        total += len(x) / SR
    names = sorted(os.listdir(OUT))
    size = sum(os.path.getsize(os.path.join(OUT, n)) for n in names)
    print(f'{len(names)} ta ibora, {total:.1f} s, {size / 1024:.0f} KB → {os.path.relpath(OUT, ROOT)}')


if __name__ == '__main__':
    main()
