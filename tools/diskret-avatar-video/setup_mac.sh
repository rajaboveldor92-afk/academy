#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

command -v git >/dev/null || { echo 'git kerak'; exit 1; }
command -v ffmpeg >/dev/null || { echo 'ffmpeg topilmadi. Homebrew: brew install ffmpeg'; exit 1; }

PYTHON=${PYTHON:-python3}
$PYTHON -m venv .venv
source .venv/bin/activate
python -m pip install -U pip wheel setuptools
python -m pip install -r requirements.txt

mkdir -p vendor
if [[ ! -d vendor/LivePortrait/.git ]]; then
  git clone --depth 1 https://github.com/KlingAIResearch/LivePortrait.git vendor/LivePortrait
fi
python -m pip install -r vendor/LivePortrait/requirements_macOS.txt

if [[ ! -d vendor/musetalk-mlx/.git ]]; then
  git clone --depth 1 https://github.com/xocialize/musetalk-mlx.git vendor/musetalk-mlx
fi
python -m pip install -e vendor/musetalk-mlx

mkdir -p vendor/musetalk-mlx/refs
if [[ ! -d vendor/musetalk-mlx/refs/MuseTalk/.git ]]; then
  git clone --depth 1 https://github.com/TMElyralab/MuseTalk.git vendor/musetalk-mlx/refs/MuseTalk
fi

if [[ ! -d vendor/LivePortrait/pretrained_weights/liveportrait ]]; then
  huggingface-cli download KlingTeam/LivePortrait --local-dir vendor/LivePortrait/pretrained_weights --exclude '*.git*' 'README.md' 'docs'
fi

mkdir -p vendor/musetalk-mlx/dist/MuseTalk-1.5-MLX-q4
huggingface-cli download mlx-community/MuseTalk-1.5-q4 --local-dir vendor/musetalk-mlx/dist/MuseTalk-1.5-MLX-q4 || true
python vendor/musetalk-mlx/scripts/download_dvisual_weights.py || true

echo 'Setup tugadi.'
