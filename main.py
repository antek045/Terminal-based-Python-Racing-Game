import random, math
from czlowiek import Czlowiek
from robot import Robot
from czarodziej import Czarodziej
from wilkolak import Wilkolak
from uczen import UczenZSL
from student import Student
from narrator import Narrator
from przeszkoda import Przeszkoda

TRUDNOSC = {"1": 1.75, "2": 1.0, "3": 0.6}
klasy = [Czlowiek, Robot, Czarodziej, Wilkolak, UczenZSL, Student]
szablony = [("Droga", 0, 0, 100), ("Leśna droga", 50, 0, 150), ("Zadanie matematyczne", 0, 100, 0), ("Zadanie fizyczne", 0, 150, 0), ("Rzeka", 100, 0, 150), ("Strumień", 50, 0, 100), ("Podnoszenie ciężarów", 200, 0, 0), ("Piaskowa dolina", 50, 50, 50), ("Błazen", 200, 200, 200), ("Bieg do dziekanatu", 20, 30, 150), ("Lutowanie", 10, 150, 10)]

print("=== XIV ZAWODY PCIM ===")
n = int(input("Ilość zawodników: "))
k = int(input("Długość trasy: "))
lvl = input("Trudność (1-Łatwa, 2-Normalna, 3-Trudna): ")
T = TRUDNOSC.get(lvl, 1.0)

Zawodnicy = []
for i in range(n):
    kl = random.choice(klasy)
    Zawodnicy.append(kl(f"{kl.__name__}_{i+1}"))

Trasa = [Przeszkoda(*random.choice(szablony)) for _ in range(k)]
ile_i = sum(1 for p in Trasa if p.nazwa == "Błazen")
narrator, Ranking, nr_tury = Narrator(), [], 1

while len(Ranking) < n:
    input("\n[Enter = tura]")
    narrator.kreska()
    narrator.tura_info(nr_tury, Trasa)
    for z in Zawodnicy:
        if z.czy_meta:
            narrator.status_gracza(z, Trasa)
            continue
        
        z.tury += 1
        wynik = z.wykonaj_ruch(Trasa[z.etap], T, narrator, Zawodnicy)
        z.postep += wynik
        
        narrator.status_gracza(z, Trasa)
        narrator.gadka(z.nazwa, wynik)
        
        if z.postep >= Trasa[z.etap].do_zrobienia:
            z.postep, z.etap = 0, z.etap + 1
            if z.etap >= k:
                z.czy_meta = True
                Ranking.append(z)
                print(f"    <<<< {z.nazwa} NA MECIE! >>>>")
    nr_tury += 1

print("\n" + "#"*40 + "\n WYNIKI KOŃCOWE\n" + "#"*40)
for i, z in enumerate(Ranking, 1):
    P = ((20*k*45*T*math.sqrt(k))/z.tury + 40) + 3*ile_i - (z.s_b + z.i_b + z.z_b)
    print(f"{i}. {z.nazwa:15s} | Tury: {z.tury:3d} | Punkty: {P:.2f}")
