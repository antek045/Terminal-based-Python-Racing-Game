import random
from zawodnik import Zawodnik

class Student(Zawodnik):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.sila = random.randint(2, 6)
        self.intel = random.randint(20, 30)
        self.zwin = random.randint(2, 6)
        self.s_b, self.i_b, self.z_b = self.sila, self.intel, self.zwin

    def wykonaj_ruch(self, p, T, narrator, wszyscy=None):
        i_akt = self.intel + 5 if "Zadanie" in p.nazwa else self.intel
        z_akt = max(0, self.zwin - 3) if self.rana > 0 else self.zwin
        if self.rana > 0: self.rana -= 1
        
        cecha = random.choice([("s", self.sila), ("i", i_akt), ("z", z_akt)])
        if cecha[0] == "s" and random.random() < 0.3:
            narrator.moc_info(f"Student {self.nazwa} zasnął nad książką!")
            return 0
            
        return max(0, random.randint(-3, 3) * T) + (cecha[1] * T)
