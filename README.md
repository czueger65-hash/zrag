# ZsRAG

**Zivilschutz Raclette-Abend Game**

Browser-Spiel zum Zeichnen und Raten. Eine Person zeichnet am Whiteboard den angezeigten Begriff, die anderen raten; wer zuerst richtig liegt, gewinnt die Runde.

## Nutzung

`index.html` im Browser öffnen. Es braucht keinen Server und keine Abhängigkeiten.

| Taste | Funktion |
|-------|----------|
| `DE` / `EN` / `ES` / `IT` / `PT` | Sprache umschalten (Knöpfe oben rechts, jederzeit) |
| `Enter` | Nächste Runde (Thema + Wort, Timer startet) |
| `Leertaste` | Timer pausieren/fortsetzen |
| `V` | Begriff aufdecken/verdecken (erstes Aufdecken startet den Timer) |
| `1`–`9` | Punkt an Spieler 1–9 vergeben (beendet die Runde) |

## Sprachen

- Oberfläche, Themen und Wörter gibt es auf Deutsch, Englisch, Spanisch, Italienisch und Portugiesisch (brasilianisch).
- Die App startet immer auf Deutsch. Die Sprache lässt sich jederzeit umschalten, auch mitten in einer Runde; Thema und Wort werden sofort übersetzt angezeigt.
- Spielernamen werden nicht übersetzt.

## Spiellogik

- Bei jedem Spielstart stellt Claude 6 neue Themen mit je 10 Begriffen zusammen (höchstens 60 Begriffe pro Spiel), jeweils in allen fünf Sprachen.
- Vorgaben an Claude: konkret und in unter einer Minute erkennbar zeichenbar, in allen fünf Sprachen eindeutig übersetzbar, keine regionalen Begriffe, keine Marken, kein Wort doppelt. Die Themen der letzten Spiele (im Browser gemerkt) werden ausgeschlossen, damit sich nichts wiederholt.
- Nach der Erstellung zeigt eine eigene Seite die Themen des Spiels (ohne die Begriffe). Erst mit „Spiel beginnen“ (oder `Enter`) startet das Spiel; „Andere Themen erstellen“ lässt Claude neue Themen erstellen, „Zurück“ führt zur Einrichtung.
- Die Antwort wird geprüft: unvollständige Einträge und doppelte Wörter werden verworfen, mehr als 6 Themen oder 10 Wörter werden abgeschnitten.
- Dafür braucht die Seite die Artifact-Funktion „Claude fragen“ (`sample`). Beim ersten Spielstart fragt claude.ai, ob die Seite Claude nutzen darf; die Anfragen laufen über das Claude-Konto der Person, die die Seite geöffnet hat.
- Ist Claude nicht erreichbar (z. B. `index.html` lokal geöffnet) oder schlägt die Erstellung fehl, kann man es erneut versuchen oder bewusst mit der eingebauten Ersatzliste (30 Themen à 30 Wörter) spielen. Die Seite zeigt im Spiel an, woher die Begriffe stammen.
- Jeder Vorschlag zieht ein zufälliges offenes Thema und daraus ein noch nicht gezeigtes Wort. Kein Begriff kommt doppelt.
- Ein Thema ist nach 10 Wörtern erledigt, das Spiel nach allen 60.
- 2 bis 9 Spieler. Der erste Zeichner wird zufällig ausgelost. Danach zeichnet, wer die Runde zuvor richtig geraten hat. Errät niemand den Begriff (Zeit abgelaufen oder Runde übersprungen), ist der nächste Spieler in der Reihe dran. Der Zeichner kann in seiner Runde keinen Punkt erhalten.
- Wer zuerst richtig rät, bekommt 1 Punkt. Standardmäßig bekommt auch der Zeichner 1 Punkt, wenn sein Begriff erraten wird (in der Einrichtung abwählbar).
- Bei einem Neustart werden die Spielernamen auf die Standardnamen zurückgesetzt; Spieleranzahl und Jingles bleiben erhalten.
- Jeder Begriff erscheint verdeckt. Der Zeichner deckt ihn am Board auf (Tippen auf das Feld, Button oder `V`); erst dann startet der Timer und Punkte können vergeben werden. Beim ersten Aufdecken ertönt ein Startschuss. Nach 3 Sekunden wird der Begriff automatisch wieder verdeckt; ein Sprachwechsel bei sichtbarem Begriff zeigt die Übersetzung erneut 3 Sekunden lang.
- Timer pro Runde: 30, 60, 90 oder 120 Sekunden. In den letzten 10 Sekunden wird der Timer rot und jede Sekunde mit einem Ton abgezählt (die letzten 3 höher). Läuft er ab, gibt es keinen Punkt, und ein Signalton ertönt.
- Jeder Spieler wählt in der Einrichtung seinen Jingle aus 12 Ausschnitten klassischer Stücke (höchstens 3 Sekunden, Urheberrecht abgelaufen, im Browser nachgespielt): Ode an die Freude, Für Elise, Eine kleine Nachtmusik, In der Halle des Bergkönigs, Wilhelm Tell, Cancan, Rondo alla turca, An der schönen blauen Donau, Walkürenritt, Der Frühling (Vivaldi), Habanera (Carmen), Wiegenlied (Brahms). Jeder Jingle kann nur einmal vergeben werden. Er erklingt beim Auswählen, mit „Anhören“, wenn der Spieler eine Runde gewinnt, und am Spielende für den Sieger.
- Siegerehrung: Ist die letzte Runde entschieden, wartet das Spiel 5 Sekunden (oder `Enter` drücken) und zeigt dann „Und der Sieger ist …“ mit Trommelwirbel und Beckenschlag. Danach erscheinen Sieger und Rangliste, der Jingle des Siegers erklingt, eine Claude-Stimme sagt Sieger und Rangliste in der aktiven Sprache an, und zum Schluss gibt es Applaus. Die Sprachausgabe nutzt die Artifact-Funktion `tts`; wo sie nicht verfügbar ist (z. B. Safari, Claude-Apps für Handy und Tablet), folgt der Applaus direkt.
- Beim Ankündigen der 6 Themen erklingt eine Fanfare nach „Also sprach Zarathustra“ (Richard Strauss).
- Der Lautsprecher-Knopf oben rechts schaltet alle Töne stumm (durchgestrichen = Ton aus).
- Am Ende zeigt eine Rangliste den Sieger.
- Der Spielstand wird im Browser gespeichert und lässt sich nach einem Neuladen fortsetzen.

Die Anweisung an Claude steht in `index.html` in der Funktion `buildPrompt`. Die Ersatzliste steht im Array `POOL`, jeweils als `[Deutsch, Englisch, Spanisch, Italienisch, Portugiesisch]`. Die Texte der Oberfläche stehen im Objekt `I18N`.

## Kompilieren und Version

`python3 build.py [Zieldatei]` erzeugt die veröffentlichbare Fassung (Standard: `dist/zsrag.html`).
Jeder Lauf zählt die Version in `version.txt` um eins hoch (Version 1.0 → 1.01 → 1.02 …, nach 1.99 folgt 2.0)
und trägt Version und Datum des Kompilierens in die Fußzeile von `index.html` ein. `--no-bump` setzt nur das Datum.
