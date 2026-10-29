# Image Shot List & Video Spec: Quanten-Massage München Relaunch

*Draft 1 · 25 Oct 2026 · Priority: Partnermassage-Kurs (280 € per couple) · Sales window: end of November to mid-January*

## 1. How this works (so you never block the build)

- **Every picture has a slot ID** (for example `K1`). I build the site now with **stand-ins** (the "Stand-in now" column).
- When your final picture is ready, save it as `photos-new/K1.jpg` (the slot ID as filename, any size above the minimum). I optimise it (WebP/AVIF, phone sizes) and swap it in. Nothing needs rebuilding.
- **P1 = needed before launch (mid November). P2 = nice to have, can follow.**

## 2. Rules for real vs. AI vs. stock

| Use | Rule |
|---|---|
| **Susan** (portraits, her at work) | **Real photos only.** |
| **Course participants, testimonials** | **Real people with written consent** (first name or initials). Never AI faces presented as real customers. |
| **Atmosphere** (hands, rooms, light, gift, linen) | AI or stock is fine. |
| **Hands** | AI often draws wrong fingers. Generate 8+ variants and check fingers closely, or use real photos. |
| **Realistic AI images of people** | EU rules on labelling realistic AI images are starting to apply. Ask the lawyer who checks the Impressum whether a small note is needed. |
| **Licence proof** | For every image, save a screenshot of the licence or purchase page in a `licences` folder. |

**Old Fotolia and iStock purchases:** Fotolia was merged into **Adobe Stock**, so the old Fotolia login may still show your purchase history there (I believe so, but please check). The iStock account keeps its own purchase list. Downloading those invoices once is the easiest proof.

## 3. One style for all pictures

**Look:** warm, calm, intimate, editorial. Soft window light, sand and linen tones, a small turquoise accent, shallow depth of field. Hands, backs and details over smiling faces looking at the camera. Same colour grade everywhere.

**STYLE text** (add it to the end of every AI prompt):

> editorial lifestyle photograph, soft natural window light, warm sand and linen tones with subtle muted turquoise accents, calm and intimate mood, shallow depth of field, 85mm lens, natural skin texture, gentle film-like colour grade, no text, no logo, no watermark

**Negative prompt** (if the tool has one): *extra fingers, deformed hands, plastic skin, oversaturated, neon, text, watermark, stock-photo smile, clutter*

## 4. Shot list: Partnermassage-Kurs and core pages

| ID | Prio | Where | Min. size | Motif (paste into the AI + STYLE) | Stock search | Stand-in now |
|---|---|---|---|---|---|---|
| **H1** | P1 | Home hero poster and phone fallback for the video | 2400×1350 (16:9), plus crop 1080×1350 | Two pairs of hands, one partner gently gliding along the other's shoulder and upper back, white linen, morning window light from the left, left third of the frame calm and empty for the headline | couple massage hands linen, partner massage warm light | `ocean1.jpg` (large, calm) |
| **K1** | P1 | Kurs page hero | 2400×1350 | A couple kneeling on a soft mat in a quiet bright room, one massaging the other's back, seen from behind, relaxed, no eye contact with the camera | couple massage class, partner massage lesson | `Paarkurs-01.jpg` (soft, small) |
| **K2** | P1 | Gift section ("Geschenk-Kurs") | 1600×1200 | A hand-written gift card on folded linen with a sprig of fir and a warm candle glow in the background, no readable text | christmas gift card linen, gift voucher flat lay | `Bild-3.png`, `massage-gutschein-xmas.jpg` |
| **K3a–e** | P1 | "Das lernt ihr" tiles (5 squares): Berührung und Haltung · 6 Basis-Griffe · Rücken, Nacken, Schultern · Druck und Tempo · Rituale für Zuhause | 1000×1000 each | Five close-ups in one series: (a) two hands resting calmly on a back, (b) a flowing stroke along the spine, (c) hands on neck and shoulders, (d) forearm pressure with soft focus, (e) a candle, oil bottle and towel on a bedside table | massage hands closeup, back massage detail | `Bild-1.png`, `Bild-2.png`, `Paarkurs-01.jpg`, colour blocks |
| **K4** | P1 | Practice room / atmosphere | 1600×1067 | A calm treatment room: two soft mats, linen, a plant, a window with sheer curtains, no people | massage room interior calm, spa room neutral | colour block |
| **K5** | P1 | Benefit section ("zuhause weitermachen") | 1600×1067 | A relaxed couple on a sofa in the evening, one resting a head on the other's lap, warm lamp light, faces not sharply visible | couple relaxing sofa evening warm | `happy-couple.png` |
| **K6** | P2 | Course handout / certificate | 1600×1067 | **Real photo:** the printed stroke handout and certificate on a wooden table | *(real photo)* | colour block |
| **K7** | P1 | Testimonials (3 small portraits) | 400×400 | **Real people, with consent**, first name or initials | *(real photo)* | initials circle |
| **S1** | P1 | **Meet Susan** main portrait | 3000×3750 (4:5) | **Real photo of Susan** (see section 7) | *(real photo)* | neutral placeholder |
| **S2** | P1 | Susan at work (hands close-up) | 3000×2000 | **Real photo:** Susan's hands on a back, calm | *(real photo)* | `Bild-1.png` |
| **S3** | P2 | Susan teaching a couple | 3000×2000 | **Real photo**, with the couple's consent | *(real photo)* | colour block |
| **C1** | P1 | Contact and map block | 1600×900 | **Real photo** of the entrance at Elsässer Str. 11 and the way to the studio. The map itself will be a **static OpenStreetMap image** with a click-through link (no tracking) | *(real photo)* | colour block |
| **F1** | P2 | Section texture (FAQ, footer) | 2400×800 | Fine white linen fabric, soft side light, very low contrast | linen texture soft | CSS tint |
| **OG1** | P1 | Link preview for WhatsApp and Instagram | 1200×630 | I make it from H1 and the headline | — | made from H1 |

**Logo:** your current logo files are small (`logo2.jpg` is 367×327, `cropped-logo2.jpg` is 512×512). Please send the **original (vector, SVG, AI, PDF) or a PNG at 1500 px or more**. Otherwise I redraw the lotus mark as a clean vector.

## 5. Treatment pages (12 thumbnails + 1 overview)

Format for all: **1200×1500 (4:5)** plus the same picture cropped 16:9 for the overview. Prompt = motif + STYLE. **Stand-in now: neutral tinted blocks**, except where noted.

| ID | Treatment | Motif |
|---|---|---|
| T1 | Quanten Massage | Hands hovering gently over a back, a soft glow of light between them |
| T2 | Hot Stone | Smooth dark stones on a folded towel, steam, warm light |
| T3 | Feldenkrais | A person lying relaxed on a mat, a teacher's hand gently supporting the shoulder |
| T4 | Intuitive Massage | Slow flowing hands on a back, soft shadows |
| T5 | Fußreflexzonen | Hands holding a foot, close-up, towel and warm light |
| T6 | Schwedisch / klassisch | Firm forearm stroke along the shoulders, clean linen |
| T7 | Schwangerschaft | Side-lying pregnant woman supported by pillows, hand on the lower back (stand-in `334.jpg`) |
| T8 | Antistress | Water drops or ripples with warm light (stand-in `antistress.jpg`) |
| T9 | Aroma-Öl | Oil being poured into a hand, a sprig of lavender, warm light |
| T10 | Indische Kopfmassage | Hands on the scalp, hair softly lit from behind |
| T11 | Rückenmassage | A long stroke along the spine, glowing skin tones |
| T12 | Esalen / Lomi Lomi | Forearms gliding in one long flowing movement, soft focus |
| T0 | Overview page | Wide shot of the treatment room with a mat and a plant |

## 6. Hero video specification (your clip)

**Role:** a short, slow, silent loop behind the hero text on the home page (and optionally the Kurs page). It sets the mood, so it must be calm.

| Item | Specification |
|---|---|
| **Length** | **10 seconds** as a seamless loop (shoot 12–14 s to have room for a crossfade) |
| **Aspect ratio** | **16:9 landscape** master. Keep subject and light balanced so a **9:16 phone crop** also works (keep important action in the central 50%). |
| **Shoot at** | 4K if possible, or 1080p. **Slow motion:** film at **50 or 60 fps** (or 120 fps on a phone) and play at **25 fps** (50% speed or slower). |
| **Delivery sizes** | Desktop: **1920×1080**. Phone: **720×1280** (vertical crop). |
| **Frame rate** | 25 fps |
| **Formats** | **MP4 (H.264)** and **WebM (VP9)**. I can make the WebM, the phone version and the poster from your MP4 master. |
| **File size** | Desktop MP4 **under 3.5 MB**, WebM **under 2.5 MB**, phone **under 1.5 MB** |
| **Audio** | **None** (remove the sound track) |
| **Loop** | Locked camera (tripod) or a very slow 3–5 cm slide. In DaVinci Resolve, overlay the last 1 s on the first 1 s with a cross dissolve to hide the loop point. |
| **Playback** | Muted autoplay, loop, inline on phones. Start with a **poster image** (the first frame, JPG, under 150 KB). |
| **Fallbacks** | **Poster image only** when the visitor has "reduce motion" or data-saver on, and on slow connections. |
| **Light and colour** | Warm window light, slightly lifted shadows, low contrast so white text stays readable. No fast movement, no flicker. |
| **Composition** | Keep the **left 40% of the frame calm** (headline goes there) |

**Recommended motif (shoot this first):** two pairs of hands, one partner slowly gliding along the other's shoulder, linen, morning light from the left. Optional alternates, in order of preference:

1. Hands pressing gently into a partner's hand or forearm, close-up
2. Sunlight slowly moving across a white sheer curtain in the empty treatment room
3. Two hands resting together on a mat after the massage
4. Warm stones in a bowl with a little steam

**DaVinci Resolve export:** H.264, 1920×1080, 25 fps, VBR about 3 Mbps, audio off.

## 7. Susan's portrait session (a phone is enough)

| Shot | Notes |
|---|---|
| **S1 portrait** | Calm smile, half-body, next to a window with daylight. Vertical, 4:5. A plain wall or the treatment room behind her. |
| **S2 hands** | Close-up of her hands on a back, with the person's face outside the frame. |
| **Extras** | Her in the room, standing relaxed with arms down. One laughing candid photo. |
| **Settings** | iPhone Portrait mode, back camera, the highest quality setting. Daylight, **no flash**. Wear natural colours (linen, white, sand, muted turquoise). Leave the original (not WhatsApp-compressed). Send by AirDrop, a link or email. |

**WhatsApp text for Susan (German):**

> Hallo Susan, für die neue Website brauchen wir ein paar schöne Fotos von dir. Bitte mit dem Handy (Porträt-Modus, Rückkamera), am Fenster bei Tageslicht, ohne Blitz, in natürlichen Farben (Leinen, Weiß, Sand). 1) Halbporträt, ruhig lächelnd, hochkant. 2) Deine Hände bei einer Massage (Gesicht der Person nicht im Bild). 3) Du im Behandlungsraum, entspannt stehend. 4) Ein lachendes Foto zwischendurch. Bitte als Originaldatei schicken, nicht über WhatsApp-Komprimierung (z. B. AirDrop oder per Link). Danke!

## 8. Videos: reuse, plus new ideas

**Reuse (already on the site, Full HD):**

| File | Where |
|---|---|
| `eltern-kind-massage.mp4` (13 s) | Eltern-Kind page, treatment overview |
| `fussreflexmassage.mp4` (30 s) | Fußreflex page |
| `rueckenmassage-muenchen.mp4` (20 s) | Rückenmassage page |

Two **YouTube videos** are embedded on the old Paarkurs pages. I'll show them with the **two-click solution** (nothing loads from YouTube until the visitor clicks).

**New videos with hooks (for reels and the site):**

| # | Idea | Length | Hook (first 2 seconds) | Placement |
|---|---|---|---|---|
| V1 | **Das Geschenk zu zweit:** a gift card is unwrapped, then hands on a back | 15–20 s | *„Dieses Jahr schenken wir uns Zeit.“* | Gift section, Instagram reel |
| V2 | **Ein Kurstag in 20 Sekunden:** arrival, demonstration, couples practising, the closing tea | 20 s | *„In 4 Stunden lernt ihr, euch wirklich zu berühren.“* | Kurs page "Ablauf" |
| V3 | **3 Fehler bei der Partnermassage:** Susan speaking to the camera | 25 s | *„Warum die meisten Partnermassagen nach 5 Minuten aufhören.“* | FAQ, reel |
| V4 | **Meet Susan:** a short vertical introduction | 30–45 s | *„Ich zeige euch, wie Berührung wieder leicht wird.“* | Meet Susan section |
| V5 | **Paare erzählen:** one couple's quote over their hands (with consent) | 20–30 s | A short quote from the couple | Testimonials |

**Wording rule:** no promises of healing. Describe the experience ("lernen", "erleben"), not medical results.

## 9. Delivery checklist

- Folder: `photos-new/`, filename = slot ID (for example `H1.jpg`, `K3a.jpg`)
- Minimum sizes as in the tables. Larger is welcome, I'll compress.
- Save licence proofs in `licences/`
- **Order of work:** H1 and K1 first, then K2, K3, S1 and S2, then the rest. Treatment pictures (T1–T12) can follow after launch.
