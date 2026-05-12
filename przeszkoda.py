class Przeszkoda:
    def __init__(self, nazwa, s, i, z):
        self.nazwa = nazwa
        self.s_max = s
        self.i_max = i
        self.z_max = z
        self.do_zrobienia = s + i + z
