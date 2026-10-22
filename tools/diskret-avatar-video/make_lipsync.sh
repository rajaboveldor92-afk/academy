#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"; cd "$ROOT"; source .venv/bin/activate
MT="$ROOT/vendor/musetalk-mlx"; mkdir -p "$ROOT/work/musetalk_frames"
[[ -f work/avatar_motion.mp4 ]] || { echo 'Avval ./make_avatar_motion.sh'; exit 1; }
[[ -f work/lesson_audio.wav ]] || { echo 'Avval prepare_lesson.py'; exit 1; }
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 work/lesson_audio.wav)
ffmpeg -y -stream_loop -1 -i work/avatar_motion.mp4 -t "$DUR" -an -c:v libx264 -pix_fmt yuv420p work/avatar_motion_loop.mp4
cd "$MT"
python scripts/extract_landmarks.py "$ROOT/work/avatar_motion_loop.mp4" "$ROOT/work/musetalk_frames" "$ROOT/work/coords.pkl"
python scripts/build_video.py "$ROOT/work/coords.pkl" "$ROOT/work/lesson_audio.wav" "$ROOT/work/avatar_lipsync.mp4" --variant q4
cd "$ROOT"
echo 'Lip-sync avatar: work/avatar_lipsync.mp4'
