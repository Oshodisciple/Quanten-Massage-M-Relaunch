# Quanten Massage München: Relaunch (project memory for Claude Code)

Static website for quanten-massage-muenchen.de (Praxis Haidhausen, Susan Kotschwar). Hosting: Hostnet (Apache, PHP, FTP). German-language site, no cookies.

## Read first, in this order
1. The skill `quanten-massage-relaunch` (brief, decisions, privacy rules)
2. `docs/SITE-PLAN.md` (v3: palette, images, business data, open items)
3. `docs/UEBERGABE.md` (how the existing build is uploaded, open legal points)
4. `docs/bild-und-videoplan.md` (image slot IDs such as K1, S1, H1)
5. `docs/KICKOFF-PROMPT.md` (the ordered work list)

## Base: revise, do not rebuild
`site/` already contains a complete Phase-1 static build (25 pages, `.htaccess`, `kontakt-senden.php`, self-hosted fonts, CSS tokens in `site/assets/css/style.css`). Keep its URL structure and design system. Where `docs/SITE-PLAN.md` section 5 proposes different URLs, **the URLs in `site/` win**; only add the missing 301 redirects to `.htaccess`.

## Folders
- `site/` = the deployable website (everything in it goes to the web root, including `.htaccess`)
- `Bilder 4 relaunch/` = approved pictures (Susan portrait-logo, Partner-massage, treatment pages, neue-behandlungsbilder)
- `videos/` = `hero-1080.mp4`, `hero-720.mp4`, `hero-720.webm`, `hero-poster.jpg` (never use the 46 MB originals)
- `assets/logo/` = turquoise lotus PNG
- `source/`, `backup_...zip`, `used-media.zip`, `site.zip` = reference only, never edit

## Hard rules
- No cookies, no analytics, no external scripts/fonts/CDNs. Maps only after click. WhatsApp = plain `wa.me` link.
- No Stripe, no online payment, no booking calendar, no voucher shop. Gifts and vouchers go through WhatsApp.
- No hot stone page. No entrance photo. No fake or placeholder testimonials, no review stars except the verified Google line (4,9 / 38 Bewertungen, text only, with date and link, no rating schema).
- White is the main color; turquoise brand; at most two accents per page; all text passes WCAG AA.
- Course facts: 4 hours, 280 EUR per couple, dates by arrangement. Hours: 10 to 19 Uhr, by arrangement. Responsible in Impressum: Michael Kotschwar.
- Never invent facts, dates, credentials or prices. Mark anything unconfirmed visibly and list it in `docs/UEBERGABE.md`.
- AI images are allowed for atmosphere only; Susan's portrait and the teacher are real photos; the child image is AI and must never be described as a real participant.
- Old URLs must keep working through 301 redirects. Never add a redirect that points to its own URL.
- Work in small steps, commit often (`git init` in the project folder if not yet done), keep the site deployable after every step.

## Done means
Lighthouse mobile >= 95 for performance, accessibility, best practices and SEO on the home and course pages; zero requests to third-party hosts on page load; every internal link and redirect tested; screenshots at 375, 768 and 1280 px reviewed; open points listed in `docs/UEBERGABE.md`.
