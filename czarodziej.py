import random
from zawodnik import Zawodnik

class Czarodziej(Zawodnik):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.sila = random.randint(1, 7)
        self.intel = random.randint(6, 16)
        self.zwin = random.randint(2, 8)
        self.s_b, self.i_b, self.z_b = self.sila, self.intel, self.zwin

    def wykonaj_ruch(self, p, T, narrator,wszyscy=None):
        S = random.randint(-3, 3)
        postep_bazowy = max(0, S * T)

        mnoznik_mocy = 1.0
        if p.nazwa == "Błazen":
            mnoznik_mocy = 1.75
            narrator.moc_info(f"!!! Magia: {self.nazwa} czaruje Błazna (x1.75) !!!")

        zwin_akt = self.zwin
        if self.rana > 0:
            zwin_akt = max(0, self.zwin - 3)
            self.rana -= 1
        zdolnosci = [self.sila, self.intel, zwin_akt]
        wartosc = random.choice(zdolnosci)

        wynik = postep_bazowy + (wartosc * T * mnoznik_mocy)
        return wynik
