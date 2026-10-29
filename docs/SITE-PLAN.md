# Site-Plan Relaunch Quanten-Massage München

Stand: 28.10.2026 (Version 3). Ergänzt den Skill `quanten-massage-relaunch`.

## 1. Entscheidungen
- Hot Stone entfällt: alte Seite per 301 auf `/massagen/`.
- Kein Foto vom Eingang.
- Susan-Portrait und die Lehrerin auf den Kursbildern sind echt (bestätigt). Kein KI-Hinweis nötig für diese Bilder. Für alle KI-erzeugten Atmosphärebilder (Raum, Hände, Paar auf dem Sofa usw.) gilt: Quelle im Impressum nennen, nicht als Foto echter Teilnehmender ausgeben.
- Kurs: **4 Stunden, 280 EUR pro Paar**. Das ist auf der ganzen Seite einheitlich zu verwenden (alter Text "Tageskurs" entfällt).
- Zertifikat-Bild `K6`: Namen bleiben vorerst, werden später ausgetauscht. Bis dahin Bild nur mit Hinweis "Muster" verwenden oder auf der Seite weglassen.
- Gutscheine: Bestellung per WhatsApp, keine Online-Zahlung.
- Verantwortlich im Impressum: Michael Kotschwar.
- Logo wird in Türkis umgefärbt (fertig, siehe Abschnitt 4).
- "YOGA"-Schild im Bild `T7` ist unproblematisch (Kundschaft ist yoganah). Bild bleibt wie es ist.
- Bildgrößen: Zuschnitt und Skalierung übernimmt Claude Code.

## 2. Google-Bewertungen (Korrektur)
Meine frühere Aussage, die "38 Bewertungen" seien nicht belegt, war falsch. Laut Google-Profil "Quanten Massage": **4,9 Sterne, 38 Berichte**, fast alle mit 5 Sternen.

So einbauen:
- Als ruhige Textzeile mit Link zum Google-Profil: "4,9 von 5 Sternen bei Google, 38 Bewertungen (Stand Oktober 2026)". Datum bei jeder Aktualisierung anpassen.
- Kein Google-Widget und keine Live-Einbindung (Datenschutz, Cookies). Die Zahl wird als normaler Text gepflegt.
- Kein Bewertungs-Markup (AggregateRating) im Schema: Google akzeptiert selbst eingetragene Bewertungen für die eigene Firma nicht und kann das abstrafen.
- Einzelne Zitate nur nach Rückfrage bei den Personen, daher später. Die Sternezeile darf aber schon zum Launch auf Home und Kursseite.
- Google weist selbst darauf hin, dass Bewertungen nicht überprüft werden. Deshalb keine Formulierungen wie "geprüft" oder "verifiziert".

## 3. Stammdaten (müssen überall identisch sein, auch für lokales SEO)
- Name: Quanten Massage (Praxis Haidhausen)
- Adresse: Elsässer Str. 11, 81667 München (Au-Haidhausen)
- Telefon: +49 89 4470678
- Web: quanten-massage-muenchen.de
- Google-Kategorie: Masseur
- Öffnungszeiten: 10 bis 19 Uhr, nach Rücksprache (Termine nach Vereinbarung). Auf der Seite so formulieren: "Termine nach Vereinbarung, 10 bis 19 Uhr". Im Google-Profil dieselben Zeiten eintragen, sonst widerspricht sich beides (Google zeigt aktuell "geschlossen, öffnet Do um 09:00").
- Das Google-Profil hat 5.293 Aufrufe: Name, Adresse, Telefon auf der Seite exakt wie im Profil schreiben.

## 4. Farben und Logo
Leitlinie von Michael: **Weiß bleibt Hauptfarbe.** Türkis ist die Markenfarbe, die alten Pastellfarben der Kacheln (Lavendel, Rosa, Ocker, Mintgrün; Screenshots der alten Seite) bleiben nur als sehr zarte Flächen und Kategorie-Akzente erhalten, nie als große Farbblöcke.

| Rolle | Wert | Einsatz und Kontrast |
|---|---|---|
| Weiß | `#FFFFFF` | Hauptfläche, ca. 70 % jeder Seite |
| Tinte | `#12302F` | Text, Überschriften, dunkle Bänder (auf Weiß 14,1:1) |
| Türkis dunkel | `#13716C` | Buttons, Links (weiße Schrift 5,8:1) |
| Türkis | `#2AA39B` | Logo, Linien, Icons, große Flächen |
| Türkis zart | `#EAF5F4` | wechselnde Abschnitts-Hintergründe statt Grau |
| Gold | `#B8832F` | Kurse und Geschenk (dunkle Schrift darauf 5,5:1, keine weiße) |
| Gold zart | `#F8F0E0` | Hintergrund für Partnerkurs- und Geschenkbereich |
| Rosa zart | `#FBEAE9` (Text/Akzent `#B34C4C`, 5,2:1 auf Weiß) | nur für Gutschein-Bereich |
| Lavendel zart | `#ECECF6` (Text/Akzent `#5F5DA8`, 5,8:1 auf Weiß) | nur als Kategorie-Hinweis, zum Beispiel Quanten |

Regeln: höchstens zwei Akzentfarben pro Seite, Buttons immer Türkis dunkel (Partnerkurs-Button auf der Kursseite darf Gold sein), große Fotos und das Hero-Video sorgen für den Kontrast, nicht Farbflächen. Die Farben passen zur Gesamtstimmung der neuen Bilder (warme Holz-, Leinen- und Kerzentöne), die alten Pastellkacheln wirkten dagegen kühl und uneinheitlich.

Logo (fertig, im Ordner `logo`):
- `logo-mark-turquoise.png`: Lotus, freigestellt, ca. 1400 px breit
- `logo-mark-turquoise-512.png`: kleine Fassung
- Die Schrift "Praxis Quanten-Massage" ist bewusst nicht enthalten. Sie wird als echter Text in der Schrift der Seite gesetzt (schärfer, lesbar, besser für Google).
- Für Druck und sehr große Darstellung wäre eine Vektordatei (SVG) besser. Das Original ist ein JPG mit Farbverlauf. Ein Grafiker kann den Lotus in 15 Minuten nachzeichnen. Für die Webseite genügt das PNG.

## 5. Seitenstruktur
| Neue URL | Inhalt | Alte Seiten (301) |
|---|---|---|
| `/` | Home mit Video-Hero, Partnerkurs-Teaser, Google-Sterne, Massagen, Susan, Kontakt | Startseite |
| `/partnermassage-kurs/` | Hauptseite, Geschenk-Bereich, Ablauf, FAQ, Anfrage | kurs-partner-massage, paarmassage-kurs-muenchen, partnermassage-kurs-buchen, paar-massage-kurs-buchen, fq, fq-2 |
| `/massagen/` | Übersicht | massage-techniken-muenchen, hotstone-massage-muenchen |
| `/massagen/<name>/` | Quanten, Intuitive (Muenchen + Haidhausen zusammenlegen), Feldenkrais, Fußreflex, Schwedisch, Schwangerschaft, Antistress, Aroma-Öl, Indische Kopfmassage, Rücken, Esalen | jeweilige Altseiten |
| `/ausbildung/` | Basic, Quanten-Kurs, Feldenkrais-Kurs, Eltern-Kind-Kurs | massageausbildung-kurse, basic-massageausbildung-muenchen, quanten-massage-kurs, feldenkrais-massage-kurs, eltern-kind-massagekurs |
| `/susan/` | Meet Susan, Philosophie | susan-kotschwar, philosophie-quanten-massage |
| `/kontakt/` | WhatsApp, Telefon, Karte (erst nach Klick), Formular | kontakt-quanten-susan, massage-praxis-muenchen-kontakt, google-maps, susans-danke-seite |
| `/gutschein/` | Info und Bestellung per WhatsApp | gutschein, massagegutschein-muenchen, massage-gutscheine-muenchen, massagekurs-gutschein |
| `/impressum/`, `/datenschutz/` | neu geschrieben | impressum, impressum-quanten-massage, datenschutzerklaerung |

## 6. Hero-Video
Fertige Web-Dateien im Ordner `videos`: `hero-1080.mp4` (3,8 MB), `hero-720.mp4`, `hero-720.webm`, `hero-poster.jpg`. Ohne Ton, schwarze Balken entfernt, nahtloser Loop, 17,7 Sekunden. Original (46 MB) nie auf der Webseite verwenden.
Einbau: `autoplay muted loop playsinline`, Poster zuerst, bei "Bewegung reduzieren" und Datensparmodus nur das Poster, dunkle Überlagerung ca. 35 bis 45 %.

## 7. Bilder: Zustand
**Bilder aus `Bilder 4 relaunch`:** einheitlicher Stil. Sieben davon haben nur 1280x720 (`H1`, `T5`, `T6`, `T7`, `T9`, `T10`, `T11`): als Karte oder halbe Breite in Ordnung, nicht als Vollbild-Banner.

**Fünf neue Behandlungsbilder (am 28.10. geliefert, je 2400x1792, voll ausreichend):**
| Datei (Ordner `Bilder 4 relaunch/neue-behandlungsbilder`) | Seite |
|---|---|
| `Feldenkrais.jpg` | Feldenkrais-Massage und Feldenkrais-Kurs |
| `Intuitive-Massage.jpg` | Intuitive Massage (Muenchen und Haidhausen zusammen) |
| `Esalen-Massage.jpg` | Esalen Massage |
| `Eltern-Kind.jpg` | Eltern-Kind-Kurs |
| `Ausbildung-Gruppe.jpg` | Ausbildung (Basic, Quanten-Kurs) |

Beachten: `Eltern-Kind.jpg` zeigt ein Kind. Das Bild ist KI-erzeugt und darf nicht als Foto eines echten Kurskindes bezeichnet werden. Im Impressum KI-Bilder pauschal kennzeichnen.

**Alte Archivbilder:** nicht verwenden. 170 bis 440 Pixel breit, Fotolia-Stockfotos von 2016, passen nicht zum neuen Stil, Lizenz unklar. Vergrößern lohnt nicht.

## 8. Alte Seite als Ausgangslage (Screenshots)
- Startseite hat farbige Kacheln: Massagegutschein (Lavendel), Quanten-Massage (Rosa), Aktionen (Schiefergrün), Feldenkrais (Mint), rechts Ausbildungskacheln (Ocker). Linkes Menü "Massagen München" mit 14 Einträgen.
- Der Partnerkurs steht dort als "Partner Paar-Massage Ausbildung, jederzeit nach Anfrage". Termine gibt es also nach Anfrage, nicht fest. Auf der neuen Seite entsprechend formulieren ("Termine nach Vereinbarung, kleine Gruppe") statt feste Daten zu erfinden.
- Es gibt eine Kachel **"Aktionen: Für Neukunden gibt es verschiedenste Aktionen"**. In der Seitenliste des Exports finde ich keine eigene Aktionen-Seite. Frage unten.
- Tippfehler auf der alten Seite, die nicht übernommen werden: "PAARMASSAG KURS", "Fusssreflexzonen".

## 9. Rechtstexte
Das vorhandene Impressum ist veraltet und passt nicht zu einer cookiefreien Seite: TMG (abgelöst durch DDG), Facebook-Like-Button, Google Analytics, Google AdSense, Kontonummer und BLZ. Beide Texte komplett neu schreiben, Michael Kotschwar als Verantwortlicher, Bildquellen so nennen, wie sie tatsächlich sind (eigene Fotos, KI-erzeugte Bilder gekennzeichnet). Danach rechtlich prüfen lassen. Das ist keine Rechtsberatung.

## 10. Was noch offen ist
1. **Aktionen für Neukunden:** Gibt es aktuelle Angebote, die auf die neue Seite gehören (Text und Gültigkeit)? Wenn nicht, entfällt die Kachel.
2. **Termine Partnerkurs:** "nach Vereinbarung" so übernehmen, oder gibt es feste Termine vor Weihnachten, die wir hervorheben sollen?
3. Zertifikat-Namen (`K6`) später austauschen. Bis dahin Bild als "Muster" kennzeichnen oder weglassen.
4. Google-Profil: Öffnungszeiten an "10 bis 19 Uhr, nach Vereinbarung" angleichen.
5. Optional: Lotus als SVG nachzeichnen lassen.

Entschieden: Video bleibt im Originaltempo (keine Verlangsamung).
