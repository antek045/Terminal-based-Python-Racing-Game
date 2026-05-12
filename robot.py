import random
from zawodnik import Zawodnik

class Robot(Zawodnik):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.sila = random.randint(5, 20)
        self.intel = random.randint(1, 8)
        self.zwin = random.randint(2, 11)
        self.s_b, self.i_b, self.z_b = self.sila, self.intel, self.zwin

    def wykonaj_ruch(self, p, T, narrator, wszyscy=None):
        s_eff, i_eff, z_eff = self.sila, self.intel, self.zwin
        if p.nazwa in ["Rzeka", "Strumień"]:
            z_eff -= 2
            narrator.moc_info(f"Robot {self.nazwa} rdzewieje w wodzie!")
        if p.nazwa == "Zadanie fizyczne":
            i_eff += 2
            narrator.moc_info(f"Robot {self.nazwa} optymalizuje obliczenia fizyczne!")
            
        z_akt = max(0, z_eff - 3) if self.rana > 0 else z_eff
        if self.rana > 0: self.rana -= 1
        
        return max(0, random.randint(-3, 3) * T) + (random.choice([s_eff, i_eff, z_akt]) * T)
