#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path
import fitz


def duration(path: Path) -> float:
    return float(subprocess.check_output([
        'ffprobe','-v','error','-show_entries','format=duration',
        '-of','default=noprint_wrappers=1:nokey=1',str(path)
    ], text=True).strip())


def run(cmd):
    print('+', ' '.join(map(str, cmd)))
    subprocess.run(cmd, check=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pdf', required=True)
    ap.add_argument('--audio-dir', required=True)
    ap.add_argument('--out', default='work')
    args=ap.parse_args()

    out=Path(args.out); slides=out/'slides'; slides.mkdir(parents=True,exist_ok=True)
    pdf=fitz.open(args.pdf)
    for i,page in enumerate(pdf,1):
        pix=page.get_pixmap(matrix=fitz.Matrix(2.5,2.5), alpha=False)
        pix.save(slides/f'{i:02d}.png')

    audio_dir=Path(args.audio_dir)
    clips=[audio_dir/f'{i:02d}.wav' for i in range(1,len(pdf)+1)]
    missing=[p for p in clips if not p.exists()]
    if missing:
        raise SystemExit('Yetishmayotgan audio: '+', '.join(map(str,missing)))

    durs=[duration(p) for p in clips]
    (out/'timeline.json').write_text(json.dumps([
        {'slide':i+1,'audio':str(clips[i]),'duration':durs[i]} for i in range(len(clips))
    ],ensure_ascii=False,indent=2))

    ac=out/'audio_concat.txt'; ac.write_text('\n'.join(f"file '{p.resolve()}'" for p in clips)+'\n')
    run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(ac),'-ar','48000','-ac','1',str(out/'lesson_audio.wav')])

    sc=out/'slides_concat.txt'; lines=[]
    for i,d in enumerate(durs,1):
        lines += [f"file '{(slides/f'{i:02d}.png').resolve()}'", f'duration {d:.6f}']
    lines += [f"file '{(slides/f'{len(durs):02d}.png').resolve()}'"]
    sc.write_text('\n'.join(lines)+'\n')

    run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(sc),
         '-vf','scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=white,format=yuv420p',
         '-r','30','-c:v','libx264','-crf','18','-preset','medium',str(out/'slides.mp4')])
    print(f'Tayyor: {out/"slides.mp4"}; jami {sum(durs):.1f} s')

if __name__=='__main__': main()
