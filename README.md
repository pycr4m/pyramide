# Pyramide

Ein kleines Python-Konsolenprogramm, das eine Pyramide aus Sternen (`*`) zeichnet. Höhe und Breite der Pyramide gibst du beim Start ein.

## Aufgabenstellung

Es soll ein Programm entstehen, das

1. die **Höhe** und die **Breite** einer Pyramide einliest und die Eingaben prüft,
2. daraus mit Schleifen eine Pyramide aus Sternen zeichnet und
3. dabei die Breite als Grenze berücksichtigt, wenn die gewünschte Höhe nicht mehr hineinpasst.

## Funktionsweise

| Funktion | Aufgabe |
|---|---|
| `main()` | Steuert den Ablauf: erst Eingabe, dann Ausgabe der Pyramide |
| `get_hoehe_breite()` | Fragt Höhe und Breite ab und wiederholt die Eingabe, bis eine gültige Zahl eingegeben wurde |
| `pyramide_bauen(hoehe, breite)` | Gibt die Pyramide Zeile für Zeile aus |

### So wird gezeichnet

- **Höhe ≤ Breite:** Die Pyramide hat so viele Stufen wie die Höhe.
- **Höhe > Breite:** Die Breite begrenzt die Pyramide, sie wird nicht höher als die Breite zulässt.
- **Gerade Zahl:** Jede Zeile wächst um zwei Sterne (`**`), die Pyramide wirkt kompakt.
- **Ungerade Zahl:** Zwischen den Sternen steht ein Leerzeichen (`* `), die Pyramide hat ein Rautenmuster.
- Vor jeder Zeile stehen Leerzeichen, damit die Pyramide zentriert wirkt. Ihre Anzahl wird mit jeder Zeile kleiner.

## Voraussetzungen

- Python 3.6 oder neuer (wegen der f-Strings)

Zusätzliche Pakete sind nicht nötig.

## Verwendung

```bash
git clone https://github.com/pycr4m/pyramide.git
cd pyramide
python pyramide.py
```

### Beispiel 1: gerade Höhe (4), Breite 10

```text
Gib die Höhe der Pyramide ein: 4
Gib die Breite der Pyramide ein: 10

   **
  ****
 ******
********
```

### Beispiel 2: ungerade Höhe (5), Breite 10

```text
Gib die Höhe der Pyramide ein: 5
Gib die Breite der Pyramide ein: 10

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

### Beispiel 3: Höhe 10, Breite 4 (Breite begrenzt)

```text
Gib die Höhe der Pyramide ein: 10
Gib die Breite der Pyramide ein: 4

   **
  ****
```

Die erste Ausgabezeile besteht nur aus Leerzeichen und erscheint deshalb als Leerzeile.

## Bekannte Einschränkungen und Ideen für später

- Gibt man statt einer Zahl Text ein, bricht das Programm mit einem Fehler ab (`UnboundLocalError`), weil nach der Fehlermeldung kein `continue` folgt.
- Die Meldung verlangt eine Zahl größer als 0, akzeptiert wird aber auch 0.
- Die Eingabeschleife für Höhe und Breite ist doppelt vorhanden und ließe sich in eine eigene Funktion auslagern.
- Die Auswertung von Höhe und Breite ist in `pyramide_bauen()` in vier Fälle aufgeteilt. Eine gemeinsame Schleife mit einem Parameter für das Sternmuster würde den Code deutlich kürzen.

## Autor

[pycr4m](https://github.com/pycr4m)
