# zrag

Browser-Spiel zum Zeichnen und Raten. Eine Person zeichnet am Whiteboard den angezeigten Begriff, die anderen raten; wer zuerst richtig liegt, gewinnt die Runde.

## Nutzung

`index.html` im Browser öffnen. Es braucht keinen Server und keine Abhängigkeiten.

| Taste | Funktion |
|-------|----------|
| `DE` / `EN` / `ES` | Sprache umschalten (Knöpfe oben rechts, jederzeit) |
| `Enter` | Nächste Runde (Thema + Wort, Timer startet) |
| `Leertaste` | Timer pausieren/fortsetzen |
| `V` | Begriff aufdecken/verdecken (erstes Aufdecken startet den Timer) |
| `1`–`9` | Punkt an Spieler 1–9 vergeben (beendet die Runde) |

## Sprachen

- Oberfläche, Themen und Wörter gibt es auf Deutsch, Englisch und Spanisch.
- Die App startet immer auf Deutsch. Die Sprache lässt sich jederzeit umschalten, auch mitten in einer Runde; Thema und Wort werden sofort übersetzt angezeigt.
- Spielernamen werden nicht übersetzt.

## Spiellogik

- Bei jedem Spielstart werden 6 Themen aus einem Pool von 30 Themen mit je 30 Wörtern (900 Begriffe) ausgelost und aus jedem Thema 10 Wörter (60 Begriffe pro Spiel).
- Pool-Themen: Haustiere & Bauernhof, Wildtiere, Meerestiere, Vögel & Insekten, Berufe, Sport, Obst & Gemüse, Essen & Trinken, Verkehrsmittel, Küche, Wohnen & Haushalt, Natur & Wetter, Musik, Kleidung & Accessoires, Märchen & Fantasie, Schule & Büro, Strand & Ferien, Werkzeuge & Garten, Körper & Gesundheit, Spielzeug & Spielplatz, Gebäude & Bauwerke, Feste & Feiertage, Technik & Elektronik, Weltraum & Wissenschaft, Winter & Berge, Stadt & Strasse, Zirkus & Jahrmarkt, Tätigkeiten, Geschichte & Abenteuer, Hobbys & Freizeit.
- Aufnahmekriterium für Wörter: konkret, in unter einer Minute erkennbar zeichenbar und in allen drei Sprachen eindeutig übersetzbar. Keine regionalen Begriffe. Jedes Wort kommt im Pool nur einmal vor.
- Jeder Vorschlag zieht ein zufälliges offenes Thema und daraus ein noch nicht gezeigtes Wort. Kein Begriff kommt doppelt.
- Ein Thema ist nach 10 Wörtern erledigt, das Spiel nach allen 60.
- 2 bis 9 Spieler. Der erste Zeichner wird zufällig ausgelost. Danach zeichnet, wer die Runde zuvor richtig geraten hat. Errät niemand den Begriff (Zeit abgelaufen oder Runde übersprungen), ist der nächste Spieler in der Reihe dran. Der Zeichner kann in seiner Runde keinen Punkt erhalten.
- Wer zuerst richtig rät, bekommt 1 Punkt. Optional bekommt auch der Zeichner 1 Punkt, wenn sein Begriff erraten wird.
- Jeder Begriff erscheint verdeckt. Der Zeichner deckt ihn am Board auf (Tippen auf das Feld, Button oder `V`); erst dann startet der Timer und Punkte können vergeben werden.
- Timer pro Runde: 30, 60, 90 oder 120 Sekunden. In den letzten 10 Sekunden wird der Timer rot und jede Sekunde mit einem Ton abgezählt (die letzten 3 höher). Läuft er ab, gibt es keinen Punkt, und ein Signalton ertönt.
- Jeder Spielerplatz (1–9) hat einen eigenen Jingle. Er erklingt, wenn der Spieler eine Runde gewinnt, und am Spielende für den Sieger (bei Gleichstand für alle Sieger nacheinander). In der Einrichtung lässt sich jeder Jingle mit „Jingle“ anhören.
- Der Knopf „Ton an/aus“ oben rechts schaltet alle Töne stumm.
- Am Ende zeigt eine Rangliste den Sieger.
- Der Spielstand wird im Browser gespeichert und lässt sich nach einem Neuladen fortsetzen.

Themen und Wörter stehen in `index.html` im Array `POOL`, jeweils als `[Deutsch, Englisch, Spanisch]`. Ein Thema braucht mindestens 10 Wörter. Die Texte der Oberfläche stehen im Objekt `I18N`.
