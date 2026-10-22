#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"; cd "$ROOT"; source .venv/bin/activate
LP="$ROOT/vendor/LivePortrait"; OUT="$ROOT/work/liveportrait"; mkdir -p "$OUT"
DRIVER="$LP/assets/examples/driving/d0.mp4"
cd "$LP"
PYTORCH_ENABLE_MPS_FALLBACK=1 python inference.py \
  -s "$ROOT/assets/source/eldor.jpg" \
  -d "$DRIVER" \
  -o "$OUT" \
  --driving-option expression-friendly \
  --driving-multiplier 0.55
cd "$ROOT"
CANDIDATE=$(find "$OUT" -type f -name '*.mp4' ! -name '*concat*' -print0 | xargs -0 ls -t 2>/dev/null | head -n1 || true)
if [[ -z "$CANDIDATE" ]]; then CANDIDATE=$(find "$OUT" -type f -name '*.mp4' -print0 | xargs -0 ls -t | head -n1); fi
cp "$CANDIDATE" "$ROOT/work/avatar_motion.mp4"
echo 'Avatar motion: work/avatar_motion.mp4'
