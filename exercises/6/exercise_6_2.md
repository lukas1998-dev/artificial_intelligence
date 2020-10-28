# Aufgabe 6.2

#### a) Berechnen Sie den mittleren Verzweigungsfaktor beim 8-Puzzle bei uninformierter Suche ohne Zyklencheck. Der mittlere Verzweigungsfaktor ist der Verzweigungsfaktor, den ein Baum mit gleicher Knotenzahl auf der letzten Ebene, konstantem Verzweigungsfaktor und gleicher Tiefe hätte.
- Da der Suchbaum sich alle 2 Ebenen wiederholt, kann man bei Ebene 2 bereits den mittleren Verzweigungsfaktor berechnen.
- Dies führt zu folgender Gleichung: b^2 = 8
- Lösen der Gleichung: b = √8

#### b) Berechnen Sie den mittleren Verzweigungsfaktor beim 8-Puzzle bei uninformierter Suche bei Vermeidung von Zyklen der Länge 2.
**Eigene Lösung**
- Grundsätzlich gleicher Suchbaum wie bei a
- Verzweigungen überall um 1 verringert
- Suchbaum wiederholt sich ebenfalls nach 2 Ebenen
- Beim Start muss darauf geachtet werden dass der Ursprungszustand keinen Vorgänger hatte, was das Ergebnis verfälscht.
- Daher befinden sich auf Ebene 2 4 Knoten
- Gleichung: b^2 = 4
- Lösen der Gleichung: b = 2

**Richtige Lösung**
- Grundsätzlich gleicher Verzweigungsfaktor wie bei a, nur -1, da vorheriger Zustand wegfällt
- Erster Knoten kann vernachlässigt werden
- Gleichung: b = √8 - 1 = 1.8