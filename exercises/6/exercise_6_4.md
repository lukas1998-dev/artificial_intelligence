# Aufgabe 6.4

#### a) Berechnen Sie die Größe des Zustandsraumes für das 8-Puzzle, für das analoge 3-Puzzle (2 × 2-Matrix) sowie für das 15-Puzzle (4 × 4-Matrix).
| Puzzle | Felder | Kombinationen |
|---|---|---|
|3-Puzzle| 4 | 4! = 24|
|8-Puzzle| 9 | 9! = 362.880|
|15-Puzzle| 16 | 16! = 20.922.789.888.000|

#### b) Beweisen Sie, dass der Zustandsgraph, bestehend aus den Zuständen (Knoten) und den Aktionen (Kanten), beim 3-Puzzle in zwei zusammenhängende Teilgraphen zerfällt, zwischen denen keine Verbindung besteht.
- Nach 12 Verschiebungen im oder gegen den Uhrzeigersinn ist man wieder am Startzustand
- Wenn man die oberen beiden Felder vertauscht kann man dasselbe machen
- Kein Zustand der einen 12er Gruppe ist in der anderen 12er Gruppe vorhanden 