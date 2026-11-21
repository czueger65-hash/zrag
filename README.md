# zrag

Browser-Spiel zum Zeichnen und Raten. Eine Person zeichnet am Whiteboard den angezeigten Begriff, die anderen raten; wer zuerst richtig liegt, gewinnt die Runde.

## Nutzung

`index.html` im Browser öffnen. Es braucht keinen Server und keine Abhängigkeiten.

| Taste | Funktion |
|-------|----------|
| `Enter` | Nächster Vorschlag (Thema + Wort) |
| `V` | Wort verdecken/zeigen |

## Spiellogik

- 6 Startthemen mit je 10 Wörtern (60 Begriffe).
- Jeder Vorschlag zieht ein zufälliges offenes Thema und daraus ein noch nicht gezeigtes Wort. Kein Begriff kommt doppelt.
- Ein Thema ist nach 10 Wörtern erledigt, das Spiel nach allen 60.
- Der Spielstand wird im Browser gespeichert und lässt sich nach einem Neuladen fortsetzen.

Themen und Wörter stehen in `index.html` im Array `THEMEN`.
