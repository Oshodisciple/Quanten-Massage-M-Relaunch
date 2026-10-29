#!/usr/bin/env python3
"""Export approved pictures to site/assets/img as AVIF + JPG in several widths (macOS `sips`, no downloads).

Run from the project folder:  python3 tools/images.py
Writes tools/images.json (slot -> widths, height ratio) which build.py uses for <picture> markup.
Never upscales: widths above the source width are skipped and reported.
"""
import json, pathlib, subprocess, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
B = ROOT / 'Bilder 4 relaunch'
OUT = ROOT / 'site' / 'assets' / 'img'
WIDTHS = [480, 800, 1200, 1600, 2400]

# slot id -> (source file, optional crop "W:H" centred)
SLOTS = {
    'hero':  (ROOT / 'videos/hero-poster.jpg', None),
    'H1':    (B / 'Partner-massage/H1.jpg', None),
    'K1':    (B / 'Partner-massage/K1.jpg', None),
    'K2':    (B / 'Partner-massage/K2.jpg', None),
    'K3a':   (B / 'Partner-massage/K3-a.jpg', '4:5'),
    'K3b':   (B / 'Partner-massage/K3-b.jpg', '4:5'),
    'K3c':   (B / 'Partner-massage/K3-c.jpg', '4:5'),
    'K3e':   (B / 'Partner-massage/K3-e.jpg', '4:5'),
    'K4':    (B / 'Partner-massage/K4.jpg', None),
    'K5':    (B / 'Partner-massage/K5.jpg', None),
    'S1':    (B / 'Susan portrait-logo/Warmes Porträt Susan-Kotschwar.png', '4:5'),
    'S1b':   (B / 'Susan portrait-logo/Susan Portrait Website neu.png', '4:5'),
    'S2':    (B / 'Partner-massage/S2.jpg', None),
    'S3':    (B / 'Partner-massage/S3.jpg', None),
    'T0':    (B / 'treatment pages/T0.jpg', '4:5'),
    'T0a':   (B / 'treatment pages/T0a.jpg', '4:5'),
    'T1':    (B / 'treatment pages/T1.jpg', '4:5'),
    'T3':    (B / 'neue-behandlungsbilder/Feldenkrais.jpg', None),
    'T4':    (B / 'neue-behandlungsbilder/Intuitive-Massage.jpg', None),
    'T12':   (B / 'neue-behandlungsbilder/Esalen-Massage.jpg', None),
    'T5':    (B / 'treatment pages/T5.jpg', None),
    'T6':    (B / 'treatment pages/T6.jpg', None),
    'T7':    (B / 'treatment pages/T7.jpg', None),
    'T9':    (B / 'treatment pages/T9.jpg', None),
    'T10':   (B / 'treatment pages/T10.jpg', None),
    'T11':   (B / 'treatment pages/T11.jpg', None),
    'T13':   (B / 'treatment pages/T4.jpg', '4:5'),
    'A1':    (B / 'neue-behandlungsbilder/Ausbildung-Gruppe.jpg', None),
    'A2':    (B / 'neue-behandlungsbilder/Eltern-Kind.jpg', None),
}

def dims(p):
    o = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(p)], capture_output=True, text=True).stdout
    return int(re.search(r'pixelWidth: (\d+)', o).group(1)), int(re.search(r'pixelHeight: (\d+)', o).group(1))

def sips(*args):
    subprocess.run(['sips', *map(str, args)], check=True, capture_output=True)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / 'tools' / '.out'; tmp.mkdir(exist_ok=True)
    manifest, notes = {}, []
    for slot, (src, crop) in SLOTS.items():
        w, h = dims(src)
        base = tmp / f'{slot}.png'
        sips('-s', 'format', 'png', src, '--out', base)
        if crop:
            a, b = map(int, crop.split(':'))
            cw, ch = (w, round(w * b / a)) if w * b / a <= h else (round(h * a / b), h)
            sips('--cropToHeightWidth', ch, cw, base)
            w, h = cw, ch
        made = []
        for tw in WIDTHS:
            if tw > w:
                continue
            th = round(h * tw / w)
            r = tmp / f'{slot}-{tw}.png'
            sips('--resampleWidth', tw, base, '--out', r)
            sips('-s', 'format', 'avif', '-s', 'formatOptions', '55', r, '--out', OUT / f'{slot}-{tw}.avif')
            sips('-s', 'format', 'jpeg', '-s', 'formatOptions', '78', r, '--out', OUT / f'{slot}-{tw}.jpg')
            made.append(tw)
        if w not in made and w < WIDTHS[-1]:   # always include the native width as the largest step
            sips('-s', 'format', 'avif', '-s', 'formatOptions', '55', base, '--out', OUT / f'{slot}-{w}.avif')
            sips('-s', 'format', 'jpeg', '-s', 'formatOptions', '78', base, '--out', OUT / f'{slot}-{w}.jpg')
            made.append(w)
        if w < 1600:
            notes.append(f'{slot}: only {w}px wide, use at half width or as card, not as a full-width banner')
        manifest[slot] = {'widths': made, 'w': w, 'h': h}
        print(slot, made)
    (ROOT / 'tools' / 'images.json').write_text(json.dumps(manifest, indent=1), encoding='utf-8')
    print('\n'.join(notes))

if __name__ == '__main__':
    main()
