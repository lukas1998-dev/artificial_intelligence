# Aufgabe 6.15

#### Zeigen Sie, dass die Heuristiken h1 und h2 für das 8-Puzzle aus Abschnitt 6.3.5 zulässig sind.

h1 erhöht die vorraussichtlichen Kosten für jedes falsch liegende Feld um 1. Da ein falsch liegendes Feld immer mindestens einen Zug braucht um an die richtige Stelle zu kommen ist diese Heuristik zulässig.

h2 erhöht die vorraussichtlichen Kosten für jedes falsch liegende Feld um den Abstand zur richtigen Position. Da auch hier jedes Feld mindestens so viele Schritte benötigt um an die richtige Position zu kommen ist h2 ebenfalls zulässig.
