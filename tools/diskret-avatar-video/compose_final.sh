#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"; cd "$ROOT"; mkdir -p output
[[ -f work/slides.mp4 ]] || { echo 'work/slides.mp4 yoq'; exit 1; }
[[ -f work/avatar_lipsync.mp4 ]] || { echo 'work/avatar_lipsync.mp4 yoq'; exit 1; }
ffmpeg -y \
  -i work/slides.mp4 \
  -i work/avatar_lipsync.mp4 \
  -filter_complex "[1:v]scale=500:281:force_original_aspect_ratio=increase,crop=500:281,setsar=1[av];color=c=black@0.30:s=516x297:d=999[shadow];[shadow][av]overlay=8:8[box];[0:v][box]overlay=W-w-34:26:shortest=1[v]" \
  -map '[v]' -map 1:a? \
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p \
  -c:a aac -b:a 192k -shortest output/M1_diskret_avatar_1080p.mp4
echo 'Tayyor: output/M1_diskret_avatar_1080p.mp4'
