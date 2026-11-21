# zrag

Browser-Spiel zum Zeichnen und Raten. Eine Person zeichnet am Whiteboard den angezeigten Begriff, die anderen raten; wer zuerst richtig liegt, gewinnt die Runde.

## Nutzung

`index.html` im Browser öffnen. Es braucht keinen Server und keine Abhängigkeiten.

| Taste | Funktion |
|-------|----------|
| `Enter` | Nächste Runde (Thema + Wort, Timer startet) |
| `Leertaste` | Timer pausieren/fortsetzen |
| `V` | Wort verdecken/zeigen |
| `1`–`9` | Punkt an Spieler 1–9 vergeben (beendet die Runde) |

## Spiellogik

- 6 Startthemen mit je 10 Wörtern (60 Begriffe).
- Jeder Vorschlag zieht ein zufälliges offenes Thema und daraus ein noch nicht gezeigtes Wort. Kein Begriff kommt doppelt.
- Ein Thema ist nach 10 Wörtern erledigt, das Spiel nach allen 60.
- 2 bis 9 Spieler. Der Zeichner wechselt jede Runde der Reihe nach und kann in seiner Runde keinen Punkt erhalten.
- Wer zuerst richtig rät, bekommt 1 Punkt. Optional bekommt auch der Zeichner 1 Punkt, wenn sein Begriff erraten wird.
- Timer pro Runde: 30, 60, 90 oder 120 Sekunden. Läuft er ab, gibt es keinen Punkt, und ein Signalton ertönt.
- Am Ende zeigt eine Rangliste den Sieger.
- Der Spielstand wird im Browser gespeichert und lässt sich nach einem Neuladen fortsetzen.

Themen und Wörter stehen in `index.html` im Array `THEMEN`.
