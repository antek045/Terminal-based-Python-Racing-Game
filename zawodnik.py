class Zawodnik:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.etap = 0
        self.postep = 0
        self.tury = 0
        self.czy_meta = False
        self.rana = 0
        self.s_b = self.i_b = self.z_b = 0

    def __str__(self):
        return self.nazwa
