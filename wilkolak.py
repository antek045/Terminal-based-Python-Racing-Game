import random
from zawodnik import Zawodnik

class Wilkolak(Zawodnik):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.sila = random.randint(8, 19)
        self.intel = random.randint(1, 6)
        self.zwin = random.randint(8, 19)
        self.s_b, self.i_b, self.z_b = self.sila, self.intel, self.zwin

    def wykonaj_ruch(self, p, T, narrator, wszyscy):
        if random.random() < 0.15:
            ofiary = [x for x in wszyscy if x != self and not x.czy_meta]
            if ofiary:
                cel = random.choice(ofiary)
                cel.rana = 4
                narrator.moc_info(f"!!! Wilkołak {self.nazwa} ugryzł {cel.nazwa} !!!")

        z_akt = max(0, self.zwin - 3) if self.rana > 0 else self.zwin
        if self.rana > 0: self.rana -= 1
        
        wartosc = random.choice([self.sila, self.intel, z_akt])
        return max(0, random.randint(-3, 3) * T) + (wartosc * T)
