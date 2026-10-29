#!/usr/bin/env python3
"""Build the static site: src/pages/*.html (front matter + <main> content) -> site/<url>/index.html.

Run from the project folder:  python3 tools/build.py
Shared parts (head, header, footer, WhatsApp number, business data, JSON-LD) live only here.
"""
import json, pathlib, re, urllib.parse, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, SITE = ROOT / 'src' / 'pages', ROOT / 'site'
DOMAIN = 'https://quanten-massage-muenchen.de'

# ---- the one place for contact data (also used in JSON-LD) ----
WHATSAPP = '4915773842126'          # Mobilnummer ohne + und ohne Leerzeichen
BIZ = {
    'name': 'Quanten Massage',
    'sub': 'Praxis Haidhausen',
    'person': 'Susan Kotschwar',
    'street': 'Elsässer Str. 11', 'zip': '81667', 'city': 'München', 'district': 'Haidhausen',
    'phone': '+49 89 4470678', 'phone_href': '+49894470678',
    'mobile': '0157 73842126',
    'email': 'praxis@quanten-massage-muenchen.de',
    'hours': 'Termine nach Vereinbarung, 10 bis 19 Uhr',
    'google': 'https://www.google.com/maps/search/?api=1&query=Quanten+Massage+Els%C3%A4sser+Str.+11+M%C3%BCnchen',
    'rating': '4,9 von 5 Sternen bei Google, 38 Bewertungen (Stand Oktober 2026)',
}
WA = f'https://wa.me/{WHATSAPP}'
MSG = {
    'kurs': 'Hallo Susan, wir interessieren uns für den Partnermassage-Kurs. Wann könnten wir einen Termin vereinbaren?',
    'geschenk': 'Hallo Susan, ich möchte den Partnermassage-Kurs verschenken. Können wir kurz sprechen?',
    'gutschein': 'Hallo Susan, ich möchte einen Gutschein bestellen.',
}
def wa(key_or_text):
    return f'{WA}?text=' + urllib.parse.quote(MSG.get(key_or_text, key_or_text))

ICON = {
    'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2a9.93 9.93 0 0 0-8.5 15.07L2 22l5.07-1.5A9.94 9.94 0 1 0 12.04 2Zm0 1.8a8.14 8.14 0 1 1-4.2 15.1l-.3-.18-3 .88.9-2.93-.2-.3A8.13 8.13 0 0 1 12.04 3.8Zm-3.3 4.1c-.2 0-.5.07-.75.35-.26.28-1 1-1 2.4 0 1.4 1.04 2.8 1.18 3 .15.2 2.04 3.2 5 4.36 2.46.97 2.96.78 3.5.73.53-.05 1.73-.7 1.97-1.4.25-.68.25-1.27.17-1.4-.07-.12-.27-.2-.57-.35-.3-.15-1.73-.86-2-.95-.27-.1-.46-.15-.66.15-.2.3-.76.95-.93 1.15-.17.2-.34.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.66-1.6-.9-2.18-.24-.57-.48-.5-.66-.5h-.56Z"/></svg>',
    'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 9h16M4 15h16"/></svg>',
}

NAV = [('/paarmassage-kurs-muenchen/', 'Partnermassage-Kurs'), ('/massagen/', 'Massagen'),
       ('/weitere-kurse/', 'Ausbildung'), ('/gutschein/', 'Gutschein'),
       ('/susan-kotschwar/', 'Susan'), ('/kontakt/', 'Kontakt')]

def local_business():
    return {
        '@context': 'https://schema.org', '@type': 'HealthAndBeautyBusiness',
        '@id': DOMAIN + '/#praxis', 'name': f"{BIZ['name']} ({BIZ['sub']})",
        'url': DOMAIN + '/', 'image': DOMAIN + '/assets/img/og.jpg', 'logo': DOMAIN + '/assets/img/logo-512.png',
        'telephone': BIZ['phone'], 'email': BIZ['email'], 'priceRange': '€€',
        'address': {'@type': 'PostalAddress', 'streetAddress': BIZ['street'], 'postalCode': BIZ['zip'],
                    'addressLocality': BIZ['city'], 'addressRegion': 'Bayern', 'addressCountry': 'DE'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': 48.1286, 'longitude': 11.6031},
        'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification',
            'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'opens': '10:00', 'closes': '19:00', 'description': 'Termine nach Vereinbarung'}],
        'areaServed': 'München', 'founder': {'@type': 'Person', 'name': BIZ['person']},
        'sameAs': [],
    }

def parse(path):
    raw = path.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n(.*)', raw, re.S)
    meta = dict(line.split(': ', 1) for line in m.group(1).splitlines() if ': ' in line)
    return meta, m.group(2)

def head(meta, extra_ld):
    url = meta['url']; t = html.escape(meta['title'], quote=True); d = html.escape(meta['description'], quote=True)
    robots = '<meta name="robots" content="noindex, follow">\n' if meta.get('noindex') else ''
    preload = ''
    if meta.get('hero'):
        preload = f'<link rel="preload" as="image" href="{meta["hero"]}" type="image/avif" fetchpriority="high">\n'
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in extra_ld)
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
{robots}<link rel="canonical" href="{DOMAIN}{url}">
<meta name="theme-color" content="#FFFFFF">
<meta property="og:type" content="website"><meta property="og:locale" content="de_DE"><meta property="og:site_name" content="Quanten Massage München">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:url" content="{DOMAIN}{url}"><meta property="og:image" content="{DOMAIN}{meta.get('og', '/assets/img/og.jpg')}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/display.woff2" as="font" type="font/woff2" crossorigin>
{preload}<style>{CSS}</style>
{ld}</head>'''

def header(url):
    cur = ' aria-current="page"'
    links = ''.join(f'<a href="{h}"{cur if url.startswith(h) else ""}>{l}</a>' for h, l in NAV[1:])
    mlinks = ''.join(f'<a href="{h}">{l}</a>' for h, l in [('/', 'Start')] + NAV + [('/fragen-und-antworten/', 'Fragen und Antworten')])
    return f'''<body class="{'is-home' if url == '/' else 'is-page'}"><a class="skip" href="#main">Zum Inhalt springen</a>
<header class="site-header">
 <div class="nav">
  <a class="brand" href="/"><img src="/assets/img/logo-96.png" srcset="/assets/img/logo-96.png 1x, /assets/img/logo-192.png 2x" width="48" height="33" alt=""><span class="brand-text"><b>Quanten Massage</b><span>München · Haidhausen</span></span></a>
  <nav class="nav-links" aria-label="Hauptnavigation">{links}</nav>
  <a class="btn btn--gold nav-cta" href="/paarmassage-kurs-muenchen/">Partnermassage-Kurs</a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mnav">{ICON['menu']}<span class="sr">Menü öffnen</span></button>
 </div>
</header>
<div class="mnav" id="mnav" hidden>
 <button class="mnav-close" type="button">Schließen</button>
 <nav aria-label="Menü">{mlinks}</nav>
 <a class="btn btn--primary" href="{wa('kurs')}" rel="noopener">{ICON['wa']} Per WhatsApp anfragen</a>
</div>
<main id="main">'''

def footer():
    b = BIZ
    return f'''</main>
<footer class="site-footer">
 <div class="wrap foot-grid">
  <div class="foot-brand">
   <img src="/assets/img/logo-96.png" srcset="/assets/img/logo-96.png 1x, /assets/img/logo-192.png 2x" width="72" height="50" alt="" loading="lazy">
   <p><b>{b['name']}</b><br>{b['sub']} · {b['person']}</p>
   <address>{b['street']}<br>{b['zip']} {b['city']}-{b['district']}<br>beim Ostbahnhof</address>
  </div>
  <div class="foot-contact">
   <p><a href="tel:{b['phone_href']}">{b['phone']}</a><br><a href="{wa('kurs')}" rel="noopener">WhatsApp</a><br><a href="mailto:{b['email']}">{b['email']}</a></p>
   <p>{b['hours']}</p>
  </div>
  <nav class="foot-nav" aria-label="Fußnavigation">
   <a href="/paarmassage-kurs-muenchen/">Partnermassage-Kurs</a><a href="/gutschein/">Gutschein</a><a href="/massagen/">Massagen</a><a href="/weitere-kurse/">Ausbildung</a>
   <a href="/susan-kotschwar/">Susan Kotschwar</a><a href="/fragen-und-antworten/">Fragen und Antworten</a><a href="/kontakt/">Kontakt und Anfahrt</a>
  </nav>
 </div>
 <div class="wrap foot-bottom"><span>© 2026 {b['name']} München</span><span><a href="/impressum/">Impressum</a> <a href="/datenschutz/">Datenschutz</a></span><span>Ohne Cookies und ohne Tracking.</span></div>
</footer>
<div class="dock"><a class="btn btn--primary" href="{wa('kurs')}" rel="noopener">{ICON['wa']} Kurs anfragen</a><a class="btn btn--quiet" href="/gutschein/">Verschenken</a></div>
<script src="/assets/js/site.js?v={VERSION}" defer></script>
</body>
</html>
'''

IMAGES = json.loads((ROOT / 'tools' / 'images.json').read_text()) if (ROOT / 'tools' / 'images.json').exists() else {}

def picture(spec):
    """{{img:SLOT|alt text|sizes|eager}}  -> responsive <picture> with AVIF + JPG and fixed dimensions."""
    parts = spec.split('|') + ['', '', '']
    slot, alt, sizes, mode = parts[0], parts[1], parts[2] or '(min-width: 900px) 50vw, 100vw', parts[3]
    if slot not in IMAGES:
        raise SystemExit(f'unknown image slot {slot}')
    im = IMAGES[slot]; ws = im['widths']; big = ws[-1]
    h = round(im['h'] * big / im['w'])
    src = lambda ext: ', '.join(f'/assets/img/{slot}-{w}.{ext} {w}w' for w in ws)
    fallback = next((w for w in ws if w >= 1200), big)
    load = 'fetchpriority="high"' if mode == 'eager' else 'loading="lazy" decoding="async"'
    return (f'<picture><source type="image/avif" srcset="{src("avif")}" sizes="{sizes}">'
            f'<img src="/assets/img/{slot}-{fallback}.jpg" srcset="{src("jpg")}" sizes="{sizes}" '
            f'width="{big}" height="{h}" alt="{html.escape(alt, quote=True)}" {load}></picture>')

CONTACT_FORM = '''<form class="form" data-form method="post" action="/kontakt-senden.php">
  <label>Name<input name="name" autocomplete="name" required maxlength="80"></label>
  <label>E-Mail<input name="email" type="email" autocomplete="email" required maxlength="120"></label>
  <label>Telefon (optional)<input name="phone" type="tel" autocomplete="tel" maxlength="40"></label>
  <label>Eure Nachricht<textarea name="message" required maxlength="2000" placeholder="Zum Beispiel: Wunschzeitraum, Anlass, Fragen"></textarea></label>
  <div class="hp" aria-hidden="true"><label>Bitte leer lassen<input name="website" tabindex="-1" autocomplete="off"></label></div>
  <input type="hidden" name="t" value="">
  <label class="check"><input type="checkbox" name="consent" required><span>Ich habe die <a href="/datenschutz/">Datenschutzhinweise</a> gelesen. Meine Angaben werden nur zur Beantwortung meiner Anfrage verwendet.</span></label>
  <button class="btn btn--primary" type="submit">Nachricht senden</button>
 </form>'''

def faq_schema(body):
    """FAQPage JSON-LD built from the visible <details> in .faq, so text and schema never drift apart."""
    qs = re.findall(r'<details><summary>(.*?)</summary><div>(.*?)</div></details>', body, re.S)
    strip = lambda s: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in qs]}

def render_tokens(body):
    body = body.replace('{{contactform}}', CONTACT_FORM)
    body = re.sub(r'\{\{img:([^}]*)\}\}', lambda m: picture(m.group(1)), body)
    body = body.replace('{{WA}}', WA)
    body = re.sub(r'\{\{wa:(\w+)\}\}', lambda m: html.escape(wa(m.group(1)), quote=True), body)
    body = body.replace('{{icon:wa}}', ICON['wa'])
    for k, v in BIZ.items():
        body = body.replace('{{biz:' + k + '}}', v)
    return body

VERSION = '1'
CSS = ''

def minify_css(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    s = re.sub(r'\s+', ' ', s)
    return re.sub(r'\s*([{};,>])\s*', r'\1', s).replace(';}', '}').strip()

def main():
    global VERSION, CSS
    CSS = minify_css((SITE / 'assets/css/style.css').read_text(encoding='utf-8')).replace('../fonts/', '/assets/fonts/')
    css = (SITE / 'assets/css/style.css').read_bytes() + (SITE / 'assets/js/site.js').read_bytes()
    import hashlib; VERSION = hashlib.sha1(css).hexdigest()[:8]
    pages = []
    for p in sorted(SRC.glob('*.html')):
        meta, body = parse(p)
        url = meta['url']
        ld = [local_business()] if url in ('/', '/kontakt/') else []
        body = re.sub(r'<script type="application/ld\+json">.*?</script>', '', body, flags=re.S)
        main_html = render_tokens(body).strip()
        if '<details><summary>' in main_html:
            ld.append(faq_schema(main_html))
        out = head(meta, ld) + '\n' + header(url) + '\n' + main_html + '\n' + footer()
        if '{{' in out:
            raise SystemExit(f'unreplaced token in {p.name}: ' + re.search(r'\{\{[^}]*\}\}', out).group(0))
        target = SITE / (url.strip('/') or '.') / 'index.html' if not url.endswith('.html') else SITE / url.lstrip('/')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(out, encoding='utf-8')
        if not meta.get('noindex'):
            pages.append((url, meta.get('priority', '0.6')))
    sm = ''.join(f'<url><loc>{DOMAIN}{u}</loc><lastmod>2026-11-01</lastmod><priority>{pr}</priority></url>\n' for u, pr in pages)
    (SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + sm + '</urlset>\n', encoding='utf-8')
    print(f'built {len(list(SRC.glob("*.html")))} pages, {len(pages)} in sitemap')

if __name__ == '__main__':
    main()
