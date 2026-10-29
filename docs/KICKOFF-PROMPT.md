# Kickoff prompt for Claude Code

Open Claude Code in `/Users/paribuddha/Quanten-Massage-M-Relaunch` and paste everything below the line.

---

Read `CLAUDE.md`, the skill `quanten-massage-relaunch`, `docs/SITE-PLAN.md`, `docs/UEBERGABE.md` and `docs/bild-und-videoplan.md`. Then bring the existing build in `site/` up to the current decisions. Revise, do not rebuild. Make a plan with the task list first, run `git init` and a first commit of the untouched state, then work through the steps in order and commit after each one.

**Step 1: Fix what is wrong now**
1. `site/.htaccess` line `RewriteRule ^gutschein/?$ /gutschein/ [L,R=301]` redirects the page to itself (redirect loop). Remove it, and write a small script that checks no rule maps to itself or loops.
2. Remove the hot stone page (`hotstone-massage-muenchen/`), its links, its sitemap entry and add `RewriteRule ^hotstone-massage-muenchen/?$ /massagen/ [L,R=301]`.
3. Remove `anzahlung/` and every Stripe link and deposit mention (no online payment). Replace with a WhatsApp inquiry. Update `sitemap.xml`, `docs/UEBERGABE.md`.
4. Ask me to confirm the WhatsApp number (currently `4915773842126`, used about 80 times) before changing anything. Keep it in one place (a single config/constant or one find-replace) so it is easy to correct.
5. Add the missing 301 redirects from the old WordPress addresses (see SITE-PLAN section 5 and the old page list in `source/wordpress-export-2026-10-25.xml`): `/massage-techniken-muenchen/`, `/fq/`, `/fq-2/`, `/susans-danke-seite/` and all others in the export that are not yet covered.

6a. Hardening (the old WordPress site was compromised, so assume nothing from it is trustworthy): the new site must contain no WordPress files and nothing copied from the old server. In `.htaccess` deny execution of every `.php` file except `kontakt-senden.php`, block access to dotfiles and backup extensions (`.bak`, `.zip`, `.sql`, `.log`), keep `Options -Indexes`, and add a script `tools/check-deploy-folder.sh` that fails if `site/` contains any `.php` other than `kontakt-senden.php`, any `.htaccess` other than the root one, or any file not referenced or expected. In `kontakt-senden.php` verify header-injection protection, length limits, honeypot and rate limiting.

**Step 2: Design alignment**
6. Palette per SITE-PLAN section 4: white (`#FFFFFF`) as page base instead of the current `--foam`, keep turquoise tokens, add the gold and tint tokens, use at most two accents per page. Keep dark sections sparse.
7. Header logo: `assets/logo/logo-mark-turquoise.png` (convert to WebP/SVG-wrapped PNG at 2 sizes) with the words "Quanten Massage, München · Haidhausen" as live text.
8. Hero video: copy `videos/hero-1080.mp4`, `hero-720.mp4`, `hero-720.webm` to `site/assets/video/` under the file names the page expects (`hero.mp4`, `hero-mobile.mp4`, `hero.webm`). Poster from `videos/hero-poster.jpg`. Keep: muted, loop, playsinline, no video on reduced motion or data saver, dark overlay for readable text, pause button.
9. Use the skills `design-skills:design-critique` and `frontend-design` (and Impeccable / Taste skill) on the home page and the course page after steps 6 to 8 and apply the clear improvements. Keep Körting-style structure and depth, but not its colors.

**Step 3: Pictures**
10. Replace every stand-in image with the approved pictures per SITE-PLAN section 5 and 7 (slot IDs in `docs/bild-und-videoplan.md`; treatment images in `Bilder 4 relaunch/neue-behandlungsbilder/`; Susan from `Bilder 4 relaunch/Susan portrait-logo/`). Smart-crop to the sizes in the plan, export AVIF/WebP with JPG fallback and srcset, German alt texts, explicit width and height (no layout jump), lazy loading below the fold. Report any image that is too small or unsuitable, do not stretch it.
11. Remove the testimonial placeholders (initials circles) from every page; keep a hidden, commented-out section for later.

**Step 4: Content and legal**
12. Add the Google rating line (text only, "4,9 von 5 Sternen bei Google, 38 Bewertungen (Stand Oktober 2026)", link to the Google profile) on home and course page. No rating schema.
13. Hours "Termine nach Vereinbarung, 10 bis 19 Uhr", address Elsässer Str. 11, 81667 München, phone +49 89 4470678, identical in footer, contact page and JSON-LD LocalBusiness (no AggregateRating). Use `searchfit-seo:generate-schema`.
14. Partnermassage-Kurs page: 4 hours, 280 EUR per couple, dates by arrangement, gift section, FAQ written fresh (the old FAQ was Lorem ipsum), certificate only as "Muster" or hidden.
15. Rewrite Impressum and Datenschutz for the new site (DDG, no tracking, Michael Kotschwar responsible, Hostnet as host, AI images disclosed, bank data removed). Leave a yellow marker only where I must supply a fact. Do not claim legal approval.

**Step 5: Quality gate**
16. Run with Playwright: screenshots at 375, 768, 1280 px for every page; all internal links; all redirects; a network log proving zero third-party requests on page load; reduced-motion run; keyboard navigation of menu and form.
17. Run Lighthouse (mobile) and `design-skills:accessibility-audit`, `searchfit-seo:seo-check`, `searchfit-seo:technical-seo`. Fix findings.
18. Test `kontakt-senden.php` locally (syntax check, honeypot, consent, no storage). Note that real mail delivery can only be tested on Hostnet.
19. Write `docs/UEBERGABE.md` fresh: what changed, what I must still provide, exact upload steps.

Use Taskobserver to note any working preferences I correct. Ask me only when a decision is mine to make (WhatsApp number, legal facts, prices); otherwise decide and note it in `docs/UEBERGABE.md`.
