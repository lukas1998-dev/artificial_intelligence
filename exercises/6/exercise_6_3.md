# Aufgabe 6.3

#### a) Worin liegt der Unterschied zwischen dem mittleren und dem effektiven Verzweigungsfaktor (Definition 6.2)?
Der mittlere Verzweigungsfaktor wird nur aus den Blattknoten berechnet, wohingegen beim effektiven Verzweigungsfaktor alle Knoten des Baums beachtet werden.

#### b) Warum ist der effektive Verzweigungsfaktor zur Analyse und zum Vergleich der Rechenzeiten von Suchalgorithmen meist besser geeignet als der mittlere?
Weil der effektive Verzweigungsfaktor präziser ist, auch wenn der echte Verzweigungsfaktor stark schwankt.

#### c) Zeigen Sie, dass für einen stark verzweigenden Baum mit _n_ Knoten und Tiefe _d_ der effektive Verzweigungsfaktor _b_ etwa gleich dem mittleren Verzweigungsfaktor und damit gleich n^(1/d) ist.
| Verzweigungsfaktor | Formel | Runden | Umstellen |
|---|---|---|---|
| Effektiver | n = (b^(d+1)-1) / (b-1) | n = b^d | b = n^(1/d) |
| Mittlerer | n = b^d |  | b = n^(1/d) |