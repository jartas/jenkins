
class Kostka:
    """
    Třída reprezentuje hrací kostku.
    """

    def __init__(self,pocet_sten=6):
        self._pocet_sten = pocet_sten

    def vrat_pocet_sten(self):
        """
        Vrátí počet stěn kostky.
        """
        return self._pocet_sten

    def hod(self):
        """
        Vykoná hod kostkou a vrátí číslo od 1 do
        počtu stěn.
        """
        import random as _random
        return _random.randint(1, self._pocet_sten)

    def __str__(self):
        """
        Vrací textovou reprezentaci kostky.
        """
        return str("Kostka s {0} stěnami".format(self._pocet_sten))


# vytvoření kostek
sestistenna = Kostka()
desetistenna = Kostka(10)

#hod šestistěnnou
# print(sestistenna)
# for _ in range(6):
#     print(sestistenna.hod(), end=" ")

# print()
#hod desetistěnnou
# print(desetistenna, sep=" ")
# for _ in range(10):
#     print(desetistenna.hod(), end=" ")