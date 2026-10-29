# Übergabe: Relaunch quanten-massage-muenchen.de

## Was liegt wo
- `site/` : die fertige statische Website (Phase 1). Kompletter Inhalt dieses Ordners kommt per FTP ins Hauptverzeichnis bei Hostnet (inkl. versteckter Datei `.htaccess`).
- `docs/` : Bild- und Videoplan.
- `source/`, `assets/original/` : Ausgangsmaterial.

## Hochladen (wenn du so weit bist)
1. Sicherung der alten WordPress-Seite anlegen (Dateien + Datenbank).
2. Inhalt von `site/` per FTP hochladen (Windows/Mac: Cyberduck oder FileZilla). `.htaccess` nicht vergessen (Mac: Cmd+Shift+. zeigt versteckte Dateien).
3. Prüfen: PHP ist bei Hostnet aktiv (für `kontakt-senden.php`), HTTPS ist eingerichtet.
4. Testen: alle Seiten, Kontaktformular (Testnachricht), WhatsApp-Link, Stripe-Link, Karte (Klick), alte URLs (werden per `.htaccess` weitergeleitet).
5. Erst danach Domain/WordPress umstellen. Search Console: `sitemap.xml` einreichen.

## Fotos ersetzen
Platzhalter sind benannt nach der Bild-ID aus dem Bildplan (z. B. `S1` = Susan-Porträt). Neues Bild als WebP (oder JPG) unter gleichem Namen in `site/assets/img/` ablegen, z. B. `S1.webp`. Bildplan: `docs/Bild-und-Videoplan.pdf`.

## Hero-Video
Dateien `hero.webm`, `hero.mp4`, `hero-mobile.mp4` nach `site/assets/video/` legen. Die Seite lädt sie automatisch; ohne Datei bleibt das Standbild. Bei "Bewegung reduzieren" oder Datensparmodus wird nie ein Video geladen.

## Schriften
Aktuell freie Zwischenschriften (TeX Gyre Heros Cn, Lora Italic, Inter), selbst gehostet in `site/assets/fonts/`. Endgültige Schriften: gleiche Dateinamen ersetzen (oder `@font-face` in `css/style.css` anpassen).

## Datenschutz-Checkliste
- Keine Cookies, kein Tracking, keine Analytics, keine externen Schriften/Skripte.
- Google Maps lädt erst nach Klick. WhatsApp ist ein einfacher wa.me-Link. Stripe ist nur ein ausgehender Link.
- Kontaktformular: Honeypot, Einwilligung, speichert nichts, sendet nur per E-Mail.
- Impressum und Datenschutz sind Entwürfe mit gelben Markierungen. Vor dem Start rechtlich prüfen lassen.

## Offene Punkte (gelb markiert auf der Seite)
- Zertifikat: gibt es ein Teilnahme-Zertifikat für den Partnermassage-Kurs? (Alte Website: "mit Zertifikat")
- Preisliste der Einzelmassagen aus der alten Website übernommen – bitte alle Preise und Dauer prüfen
- Weitere Kurse: Preise, Gruppengröße (max. 6) und Rabatt aus der alten Website übernommen – bitte prüfen, ob noch aktuell (Alte Seite nannte 70 € Anzahlung)
- Stripe-Anzahlungslink prüfen: Betrag muss 50 € sein (alte Seiten nannten 70 €). Der alte Link auf der Gutschein-Seite war ein Test-Link und wurde NICHT übernommen.
- Antwortzeit auf der Danke-Seite ("ein bis zwei Tage") prüfen oder streichen
- Impressum: Wer ist die Inhaberin / der Inhaber der Praxis (Susan Kotschwar oder Michael Kotschwar)? Alte Seite nannte Michael Kotschwar.
- Impressum: USt-IdNr. (alte Seite: DE114103514, bitte prüfen, auf wen sie läuft) oder Hinweis nach § 19 UStG
- Impressum: Berufsbezeichnung, zuständige Behörde/Aufsicht und ggf. Kammer – nur falls zutreffend
- Impressum: Verantwortliche/r für Inhalte nach § 18 Abs. 2 MStV
- Impressum: Bildnachweis (eigene Fotos, Stock-/KI-Bilder mit Quelle und Lizenz). Hinweis auf KI-generierte Bilder bei Bedarf.
- Datenschutz: Verantwortliche/r wie im Impressum
- Datenschutz: Hosting-Anbieter Hostnet benennen, AV-Vertrag (AVV) abschließen/prüfen, Speicherdauer der Logfiles angeben
- Datenschutz: Speicherdauer Logfiles
- Datenschutz: WhatsApp-Nutzung (privat/Business) und Hinweise prüfen
