"""Fail a release if exact-age lessons are absent or stale inside its APK."""
import json
import sys
import zipfile
from pathlib import Path


def verify(apk_path):
    source = Path(__file__).resolve().parent.parent / 'assets' / 'data'
    required = ['lexicon.json', 'instructions.json', 'logic_data.json'] + [
        f'{subject}_{age}.json' for age in range(3, 9) for subject in ('math', 'logic')
    ]
    with zipfile.ZipFile(apk_path) as apk:
        for name in required:
            path = f'assets/flutter_assets/assets/data/{name}'
            if path not in apk.namelist():
                raise ValueError(f'APK dars fayli yetishmaydi: {name}')
            actual = apk.read(path)
            if actual != (source / name).read_bytes():
                raise ValueError(f'APK dars fayli eskirgan: {name}')
            data = json.loads(actual)
            if name in required[3:] and not data.get('topics'):
                raise ValueError(f'APK darslari bo‘sh: {name}')
    print(f'{apk_path}: 12 ta yoshga mos dastur va 3 ta yordamchi fayl tasdiqlandi.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python3 tool/verify_apk_content.py APK [APK ...]')
    for argument in sys.argv[1:]:
        verify(argument)
