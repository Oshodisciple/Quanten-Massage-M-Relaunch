#!/usr/bin/env python3
"""Check every internal link, image, video and srcset entry in site/*.html points to an existing file,
and that no page loads anything from another host."""
import re, pathlib, sys, urllib.parse
site = pathlib.Path(__file__).resolve().parent.parent / 'site'
errors, n = [], 0
def exists(url):
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path)
    f = site / path.lstrip('/')
    return f.is_file() or (f / 'index.html').is_file()
for page in site.rglob('*.html'):
    x = page.read_text(encoding='utf-8')
    x_noscript = re.sub(r'<script type="application/ld\+json">.*?</script>', '', x, flags=re.S)
    x_noscript = re.sub(r'<!--.*?-->', '', x_noscript, flags=re.S)
    for attr, val in re.findall(r'\b(href|src|poster|data-base)="([^"]+)"', x_noscript):
        n += 1
        if val.startswith(('#', 'mailto:', 'tel:', 'https://wa.me/', 'https://www.google.com/maps')): continue
        if val.startswith('http'):
            if attr in ('src', 'poster') or 'stylesheet' in val: errors.append(f'{page}: external resource {val}')
            continue
        if attr == 'data-base': continue
        if not exists(val): errors.append(f'{page.relative_to(site)}: broken {attr} {val}')
    for srcset in re.findall(r'srcset="([^"]+)"', x_noscript):
        for part in srcset.split(','):
            n += 1; u = part.strip().split(' ')[0]
            if not exists(u): errors.append(f'{page.relative_to(site)}: broken srcset {u}')
    css = re.findall(r'<link rel="stylesheet" href="([^"]+)"', x)
    if any(c.startswith('http') for c in css): errors.append(f'{page}: external stylesheet')
print(f'{n} references checked')
if errors: print('\n'.join(errors)); sys.exit(1)
print('ok')
