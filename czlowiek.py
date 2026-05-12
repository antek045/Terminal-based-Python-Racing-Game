import random
from zawodnik import Zawodnik

class Czlowiek(Zawodnik):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.sila = random.randint(2, 10)
        self.intel = random.randint(3, 10)
        self.zwin = random.randint(1, 10)
        self.s_b, self.i_b, self.z_b = self.sila, self.intel, self.zwin

    def wykonaj_ruch(self, p, T, narrator, wszyscy=None):
        S = random.randint(-3, 3)
        z_akt = max(0, self.zwin - 3) if self.rana > 0 else self.zwin
        if self.rana > 0: self.rana -= 1
        
        # Specjalna: wybiera zawsze najmniejszą wartość
        wartosc = min([self.sila, self.intel, z_akt])
        return max(0, S * T) + (wartosc * T)
