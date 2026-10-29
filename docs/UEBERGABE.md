# Übergabe: Relaunch quanten-massage-muenchen.de

Stand: 29.10.2026. Alle Schritte sind in Git committet (`git log` zeigt den Verlauf).

## Was liegt wo
- `site/`: die fertige Website. Der komplette Inhalt kommt per FTP ins Hauptverzeichnis bei Hostnet, auch die versteckte Datei `.htaccess`.
- `src/pages/`: Inhalte jeder Seite (Text und Bausteine). **Hier wird geändert, nicht in `site/`.**
- `tools/build.py`: erzeugt aus `src/pages/` die Seiten in `site/`. Kopf, Menü, Footer, Kontaktdaten, **WhatsApp-Nummer**, Google-Bewertungszeile und Strukturdaten stehen nur hier.
- `tools/images.py`: wandelt die freigegebenen Bilder aus `Bilder 4 relaunch/` in AVIF und JPG in mehreren Größen um (macOS-Bordmittel, keine Downloads).
- Prüfskripte: `tools/check-links.py`, `tools/check-redirects.py`, `tools/check-deploy-folder.sh`.
- `docs/licences/`: Lizenzen der Schriften (SIL Open Font License).

## Ändern und neu bauen
```
python3 tools/build.py
python3 tools/check-links.py
python3 tools/check-redirects.py
sh tools/check-deploy-folder.sh
```
Alle drei Prüfungen müssen „ok“ melden, bevor hochgeladen wird.

- **WhatsApp-Nummer ändern:** in `tools/build.py` die Zeile `WHATSAPP = '4915773842126'`, dann neu bauen.
- **Google-Bewertung aktualisieren:** in `tools/build.py` der Eintrag `'rating'` (Zahl, Anzahl und „Stand Monat Jahr“).
- **Neues Bild:** Datei in `Bilder 4 relaunch/` legen, in `tools/images.py` unter `SLOTS` eintragen, `python3 tools/images.py` ausführen, dann im Seitentext `{{img:ID|Alternativtext}}` verwenden.

## Was sich geändert hat
- **Design komplett neu:** Weiß als Grundfarbe, Türkis (#13716C / #2AA39B) als Marke, Gold nur für Kurs und Geschenk, Tinte #12302F für Text. Schriften Newsreader (Überschriften) und Hanken Grotesk (Text), selbst gehostet. Alle Text-Farbkombinationen erfüllen WCAG AA.
- **Startseite** neu: Hero-Video über die ganze Breite (stoppt bei „Bewegung reduzieren“ und Datensparmodus, Pause-Knopf), Kurs-Eckdaten, „Das lernt ihr“, Geschenk-Bereich mit Gutscheinkarte, Ablauf in drei Schritten, Susan, Einzelmassagen, Kontakt.
- **Partnermassage-Kurs-Seite** neu: 4 Stunden, 280 € pro Paar, Termine nach Vereinbarung, Bezahlung beim Kurs. FAQ neu geschrieben (8 Fragen), die Strukturdaten (FAQPage) werden automatisch aus dem sichtbaren Text erzeugt.
- **Auf dem Handy** bleibt nach dem ersten Bildschirm unten eine Leiste „Kurs anfragen / Verschenken“ eingeblendet.
- **Entfernt:** Hot-Stone-Seite, Anzahlungsseite, alle Stripe-Links und Anzahlungshinweise, erfundene Kundenstimmen (Platz dafür ist auskommentiert vorbereitet), Zertifikat (auskommentiert, bis bestätigt).
- **Google-Zeile** „4,9 von 5 Sternen bei Google, 38 Bewertungen (Stand Oktober 2026)“ als Text mit Link auf Start- und Kursseite, ohne Bewertungs-Schema.
- **Stammdaten** überall gleich: Elsässer Str. 11, 81667 München, Telefon +49 89 4470678, „Termine nach Vereinbarung, 10 bis 19 Uhr“. LocalBusiness-Strukturdaten auf Start- und Kontaktseite, ohne AggregateRating.
- **Ausbildungsseite** mit den neuen Bildern (Ausbildung-Gruppe, Feldenkrais, Eltern-Kind).
- **Impressum und Datenschutz** neu: DDG, Michael Kotschwar verantwortlich, keine Cookies, kein Tracking, keine Online-Zahlung, KI-Bilder gekennzeichnet, Bankdaten entfernt.
- **Weiterleitungen:** 30 alte Adressen leiten per 301 weiter. Die Weiterleitung von `/gutschein/` auf sich selbst ist entfernt. Neu dazugekommen sind unter anderem `/hotstone-massage-muenchen/`, `/anzahlung/` und `/massage-muenchen-praxis-haidhausen/`. Alte WordPress-Pfade (`wp-admin`, `wp-login.php`, `xmlrpc.php` …) melden „410 Gone“.
- **Absicherung:** Nur `kontakt-senden.php` darf als PHP laufen. Dotfiles, Backups und Archive sind gesperrt. HSTS ist gesetzt. Das Kontaktskript hat Schutz gegen Header-Injection, Längenlimits, Honeypot, Zeitprüfung und eine Begrenzung auf 3 Nachrichten pro IP in 10 Minuten (gespeichert wird nur ein Hashwert, 10 Minuten lang).

## Entscheidungen, die ich getroffen habe (bitte kurz prüfen)
- Die bestehenden URLs bleiben (zum Beispiel `/paarmassage-kurs-muenchen/` statt `/partnermassage-kurs/`). Die Kurzformen aus dem Site-Plan leiten weiter.
- In den Texten steht jetzt „Bezahlt wird beim Kurs“ beziehungsweise beim Gutschein „Bezahlt wird direkt bei Susan“. Grund: keine Online-Zahlung, keine Anzahlung.
- Einzelmassagen-Liste auf der Startseite zeigt nur die Dauer, keine Preise, bis die Preise bestätigt sind.
- Das Eltern-Kind-Video (`eltern-kind-massage.mp4`) ist nicht mehr eingebunden, weil die Ausbildungsseite jetzt das neue Bild verwendet. Die Datei ist in der Git-Historie noch vorhanden.
- Die beiden Susan-Porträts sind fast identisch. Verwendet wird „Warmes Porträt Susan-Kotschwar.png“.

## Was du noch liefern oder bestätigen musst
1. **WhatsApp-Nummer** 4915773842126 bestätigen.
2. **Impressum:** USt-IdNr. oder Hinweis nach § 19 UStG.
3. **Datenschutz:** Hostnet (Firmenname und Anschrift laut Vertrag), Auftragsverarbeitungsvertrag, Speicherdauer der Logfiles, WhatsApp privat oder Business.
4. **Preise prüfen:** Einzelmassagen (Gutscheinseite und Massage-Übersicht) und Ausbildung (240 € für zwei Tage, 120 € pro Tag, 10 % Rabatt, Gruppen bis 6 Personen) stammen von der alten Website.
5. **Zertifikat** für den Partnerkurs: gibt es eins? Dann blende ich es mit dem Hinweis „Muster“ ein.
6. **Aktionen für Neukunden:** gibt es welche? Sonst entfällt das Thema.
7. **Feste Kurstermine vor Weihnachten?** Dann hebe ich sie auf Start- und Kursseite hervor.
8. **Echte Kundenstimmen** mit Erlaubnis (Vorname oder Initialen). Dann aktiviere ich den vorbereiteten Bereich.
9. **Google-Profil:** Öffnungszeiten auf „10 bis 19 Uhr, nach Vereinbarung“ angleichen.
10. Impressum und Datenschutz **rechtlich prüfen lassen**. Das hier ist keine Rechtsberatung.

## Geprüft
- Alle 1.396 internen Verweise (Links, Bilder, srcset) zeigen auf vorhandene Dateien.
- Weiterleitungen: keine Schleifen, keine Ketten, alle Ziele existieren.
- Beim Seitenaufruf gibt es null Anfragen an fremde Server (im Browser für alle 23 Seiten gemessen).
- 375 px und 768 px: kein seitliches Scrollen auf allen Seiten, jede Seite hat genau eine H1, alle Bilder haben Alternativtexte.
- Mobiles Menü: Fokus springt hinein und zurück, Escape schließt, Tab bleibt im Menü.
- Titel unter 62 Zeichen, Beschreibungen 110 bis 160 Zeichen.

## Noch nicht geprüft
- **Lighthouse** (mobile ≥ 95): noch nicht gelaufen. Lokal oder nach dem Hochladen mit https://pagespeed.web.dev prüfen.
- **`.htaccess`** läuft erst auf dem Apache-Server bei Hostnet. Nach dem Hochladen die alten Adressen stichprobenartig aufrufen (zum Beispiel `/fq/`, `/hotstone-massage-muenchen/`, `/wp-admin/`).
- **Kontaktformular:** PHP gibt es lokal nicht. Der echte Mailversand lässt sich nur bei Hostnet testen.

## Hochladen
1. Sicherung der alten WordPress-Seite anlegen (Dateien und Datenbank). Die alte Seite war kompromittiert: nichts davon in den neuen Webspace übernehmen.
2. Webspace bei Hostnet leeren oder einen neuen, leeren Ordner als Hauptverzeichnis verwenden.
3. Prüfskripte laufen lassen (siehe oben).
4. Inhalt von `site/` per FTP hochladen (Cyberduck oder FileZilla). `.htaccess` nicht vergessen (Mac: Cmd+Shift+. zeigt versteckte Dateien).
5. Prüfen: HTTPS aktiv, PHP aktiv, Testnachricht über das Formular, WhatsApp-Link, Karte auf der Kontaktseite (lädt erst nach Klick), alte Adressen leiten weiter.
6. Google Search Console: `https://quanten-massage-muenchen.de/sitemap.xml` einreichen.
