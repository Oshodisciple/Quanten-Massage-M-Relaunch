#!/bin/sh
# Doppelklick: zeigt die neue Website lokal im Browser (http://localhost:8765). Fenster schließen beendet die Vorschau.
cd "$(dirname "$0")/site" || exit 1
( sleep 1; open "http://localhost:8765/" ) &
echo "Vorschau läuft auf http://localhost:8765  –  zum Beenden dieses Fenster schließen."
exec python3 -m http.server 8765
