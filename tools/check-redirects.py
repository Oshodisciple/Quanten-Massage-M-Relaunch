#!/usr/bin/env python3
"""Fail if a 301 rule in site/.htaccess points to itself, loops, or targets a page that does not exist."""
import re, pathlib, sys
site = pathlib.Path(__file__).resolve().parent.parent / 'site'
rules = re.findall(r'^RewriteRule \^([^$ ]+?)/\?\$ (\S+) \[L,R=301\]', (site / '.htaccess').read_text(), re.M)
src = {('/' + s.strip('^') + '/'): t for s, t in rules}
errors = []
for s, t in src.items():
    if s == t: errors.append(f'self-redirect: {s}')
    seen, cur = {s}, t
    while cur in src:
        if cur in seen: errors.append(f'loop: {s}'); break
        seen.add(cur); cur = src[cur]
    if cur != t: errors.append(f'chain: {s} -> {t} -> ... -> {cur} (point straight to the final page)')
    if not (site / cur.strip('/') / 'index.html').exists() and cur != '/':
        errors.append(f'missing target: {s} -> {cur}')
    if (site / s.strip('/') / 'index.html').exists():
        errors.append(f'redirect shadows a real page: {s}')
print(f'{len(src)} redirects checked')
if errors: print('\n'.join(errors)); sys.exit(1)
print('ok')
