# Diskret tuzilmalar — jonli avatarli video dars

Eksperimental pipeline: **LivePortrait + MuseTalk-MLX + FFmpeg**.

Maqsad: PDF slaydlarni asosiy ekran qilib, o‘ng yuqori burchakda Eldor Rajabovning jonli avatarini ko‘rsatish. LivePortrait ko‘z/bosh/mimikani, MuseTalk-MLX esa audio bilan lab sinxronini beradi.

## Maxfiylik

Shaxsiy rasm, dars PDF/DOCX va klon ovozdan eksport qilingan WAV fayllar GitHub'ga commit qilinmaydi. Ular faqat lokal `assets/` papkada turadi.

## Lokal struktura

```text
assets/source/eldor.jpg
assets/slides/1-maruza.pdf
assets/audio/01.wav ... 14.wav
work/
output/
vendor/
```

## MacBook M2

```bash
chmod +x setup_mac.sh
./setup_mac.sh
source .venv/bin/activate
python scripts/prepare_lesson.py --pdf assets/slides/1-maruza.pdf --audio-dir assets/audio --out work
./make_avatar_motion.sh
./make_lipsync.sh
./compose_final.sh
```

Yakuniy fayl: `output/M1_diskret_avatar_1080p.mp4`.

### Audio tartibi

`01.wav ... 14.wav` har biri tegishli slayd matni. Slayd davomiyligi audio davomiyligidan avtomatik olinadi.

### Tashqi loyihalar

- LivePortrait: `KlingAIResearch/LivePortrait`
- MuseTalk: `TMElyralab/MuseTalk`
- Apple Silicon port: `xocialize/musetalk-mlx`
