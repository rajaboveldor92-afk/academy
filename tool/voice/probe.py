"""Onaning ovozini klonlash sinovi (OmniVoice, o'zbek tili, zero-shot).

GitHub Actions'da ishlaydi (HuggingFace'dan model yuklanadi). Natija: probe_out/*.wav + timings.json.
Referens — onaning yozib olingan iboralari (assets/audio/uz/ona), matni bilan.
"""
import json
import os
import time

import numpy as np
import soundfile as sf
import torch

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ONA = os.path.join(ROOT, 'assets', 'audio', 'uz', 'ona')
OUT = os.path.join(ROOT, 'probe_out')
SR = 24000

CLIPS = {k: t for k, _, _, t in json.load(open(os.path.join(ROOT, 'tool', 'audio', 'mother_voice_clips.json')))['clips']}

REFS = {
    'A': ['oynaymiz_organamiz', 'qaysi_oyinni_tanlaymiz'],
    'B': ['narsalarni_sanab_kor', 'bugun_yaxshi_harakat'],
}

TEXTS = {
    't1': 'Qaysi rasm boshqalardan farq qiladi?',
    't2': 'Barakalla, to‘g‘ri topding!',
    't3': 'Qaysi hayvon katta? Yaxshilab qara.',
    't4': 'Besh qo‘shuv uch nechchi bo‘ladi?',
    't5': 'Barakalla, Azamjon! Bugun juda yaxshi harakat qilding.',
    't6': 'Bu harf «Sh». Shu harf bilan boshlanadigan so‘zni top.',
    't7': 'Quyon',
    't8': 'Muhammadjon, bugun ranglarni o‘rganamiz. Qizil, sariq, yashil!',
}


def load(key):
    import librosa
    y, _ = librosa.load(os.path.join(ONA, key + '.ogg'), sr=SR, mono=True)
    return y


def build_ref(keys):
    gap = np.zeros(int(0.35 * SR), dtype=np.float32)
    parts = []
    for i, k in enumerate(keys):
        if i:
            parts.append(gap)
        parts.append(load(k))
    audio = np.concatenate(parts).astype(np.float32)
    text = ' '.join(CLIPS[k] for k in keys)
    return audio, text


def main():
    from omnivoice import OmniVoice

    os.makedirs(OUT, exist_ok=True)
    torch.set_num_threads(os.cpu_count() or 4)
    t0 = time.time()
    model = OmniVoice.from_pretrained('k2-fsa/OmniVoice', device_map='cpu', dtype=torch.float32)
    timings = {'load_s': round(time.time() - t0, 1), 'items': []}
    print('model loaded', timings['load_s'], flush=True)

    jobs = [('A', tid, text) for tid, text in TEXTS.items()]
    jobs += [('B', tid, TEXTS[tid]) for tid in ('t1', 't3', 't5')]
    # Apostrof varianti: o' va g' oddiy apostrof bilan.
    jobs += [('A', tid + 'ascii', TEXTS[tid].replace('‘', "'")) for tid in ('t4', 't8')]

    for ref_id, keys in REFS.items():
        audio, text = build_ref(keys)
        sf.write(os.path.join(OUT, f'ref{ref_id}.wav'), audio, SR)
        prompt = model.create_voice_clone_prompt(ref_audio=(torch.from_numpy(audio).unsqueeze(0), SR), ref_text=text)
        for rid, tid, target in [j for j in jobs if j[0] == ref_id]:
            for steps in (16, 32) if tid in ('t1', 't5') and ref_id == 'A' else (32,):
                t = time.time()
                wav = model.generate(text=target, language='uz', voice_clone_prompt=prompt, num_step=steps)[0]
                dt = time.time() - t
                name = f'{ref_id}_{tid}_s{steps}'
                sf.write(os.path.join(OUT, name + '.wav'), wav, model.sampling_rate)
                item = {'name': name, 'text': target, 'steps': steps, 'gen_s': round(dt, 2),
                        'dur_s': round(len(wav) / model.sampling_rate, 2)}
                timings['items'].append(item)
                print(item, flush=True)
                json.dump(timings, open(os.path.join(OUT, 'timings.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(timings, open(os.path.join(OUT, 'timings.json'), 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
