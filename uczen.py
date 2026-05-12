import random
from zawodnik import Zawodnik

class UczenZSL(Zawodnik):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.sila = random.randint(8, 14)
        self.intel = random.randint(12, 18)
        self.zwin = random.randint(10, 16)
        self.s_b, self.i_b, self.z_b = self.sila, self.intel, self.zwin

    def wykonaj_ruch(self, p, T, narrator, wszyscy=None):
        i_akt = self.intel + 10 if p.nazwa == "Lutowanie" else self.intel
        z_akt = max(0, self.zwin - 3) if self.rana > 0 else self.zwin
        if self.rana > 0: self.rana -= 1
        
        return max(0, random.randint(-3, 3) * T) + (random.choice([self.sila, i_akt, z_akt]) * T)
