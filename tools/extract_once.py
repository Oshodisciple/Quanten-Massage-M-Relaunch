"""One-off: pull title, description and <main> body out of the Phase-1 pages into src/pages/."""
import re, pathlib, urllib.parse, json
site = pathlib.Path('site'); out = pathlib.Path('src/pages')
def absolutize(html, url):
    def fix(m):
        attr, q, v = m.group(1), m.group(2), m.group(3)
        if re.match(r'(https?:|mailto:|tel:|#|/|data:)', v): return m.group(0)
        return f'{attr}={q}{urllib.parse.urljoin(url, v)}{q}'
    return re.sub(r'\b(href|src|data-base|poster)=(["\'])([^"\']*)\2', fix, html)
for f in sorted(site.rglob('*.html')):
    rel = f.relative_to(site).as_posix()
    url = '/' + rel.replace('index.html', '')
    x = f.read_text(encoding='utf-8')
    title = re.search(r'<title>(.*?)</title>', x, re.S).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', x).group(1)
    body = re.search(r'<main id="main">(.*)</main>', x, re.S).group(1)
    body = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "HealthAndBeautyBusiness".*?</script>', '', body, flags=re.S)
    body = absolutize(body, url)
    name = 'home' if url == '/' else url.strip('/').replace('.html', '')
    (out / f'{name}.html').write_text(f'---\ntitle: {title}\ndescription: {desc}\nurl: {url}\n---\n{body.strip()}\n', encoding='utf-8')
    print(name, len(body))
