#!/bin/sh
# Fails if site/ contains anything that must not go to the server.
cd "$(dirname "$0")/../site" || exit 1
fail=0
bad=$(find . -name '*.php' ! -path './kontakt-senden.php'); [ -n "$bad" ] && { echo "unexpected PHP: $bad"; fail=1; }
bad=$(find . -name '.htaccess' ! -path './.htaccess'); [ -n "$bad" ] && { echo "extra .htaccess: $bad"; fail=1; }
bad=$(find . -iname '*wp-*' -o -iname 'wordpress*' -o -name '*.zip' -o -name '*.sql' -o -name '*.bak' -o -name '*.log' -o -name '.DS_Store' -o -name '*.xml' ! -name 'sitemap.xml'); [ -n "$bad" ] && { echo "forbidden files: $bad"; fail=1; }
# every file must be one of the expected kinds
bad=$(find . -type f ! \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.avif' -o -name '*.jpg' -o -name '*.png' -o -name '*.webp' -o -name '*.svg' -o -name '*.woff2' -o -name '*.mp4' -o -name '*.webm' -o -name 'robots.txt' -o -name 'sitemap.xml' -o -name '.htaccess' -o -name 'kontakt-senden.php' \)); [ -n "$bad" ] && { echo "unexpected file types: $bad"; fail=1; }
# images and videos must be referenced by some page or the stylesheet
for f in $(find assets/img assets/video -type f); do
  n=$(basename "$f")
  case "$n" in hero.mp4|hero.webm|hero-mobile.mp4) continue;; esac
  grep -rqF "$n" --include='*.html' --include='*.css' . || { echo "unreferenced: $f"; fail=1; }
done
[ $fail = 0 ] && echo "deploy folder ok"
exit $fail
