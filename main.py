from kostka import Kostka
from bojovnik import Bojovnik
from arena import Arena
from mag import Mag

# vytvoření objektů
kostka = Kostka(10)
zalgoren = Bojovnik("Zalgoren", 100, 20, 10, kostka)
gandalf = Mag("Gandalf", 60, 15, 12, kostka, 30, 45)
arena = Arena(zalgoren, gandalf, kostka)
# zápas

arena.zapas()