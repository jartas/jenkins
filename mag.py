from bojovnik import Bojovnik

class Mag(Bojovnik):
    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self._mana = mana
        self._max_mana = mana
        self._magicky_utok = magicky_utok
    
    def utoc(self, souper):
    # mana není naplněna
        if self._mana < self._max_mana:
            self._mana = self._mana + 10
            if self._mana > self._max_mana:
                self._mana = self._max_mana
            super().utoc(souper)
    #magický útok
        else:
            uder = self._magicky_utok + self._kostka.hod()
            zprava = f"{self._jmeno} použil magii za {uder} hp."
            self._nastav_zpravu(zprava)
            self._mana = 0
            souper.bran_se(uder)
  
    def graficka_mana(self):
        return self.graficky_ukazatel(self._mana, self._max_mana)