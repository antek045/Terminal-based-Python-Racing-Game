import random

class Narrator:
    def kreska(self):
        print("_" * 60)

    def tura_info(self, nr, trasa):
        print(f"NUMER TURY: {nr}")
        print(f"TRASA: {' -> '.join([p.nazwa for p in trasa])}")

    def status_gracza(self, z, trasa):
        if z.czy_meta:
            print(f"[*] {z.nazwa:15s} - [META]")
        else:
            p = trasa[z.etap]
            print(f"[*] {z.nazwa:15s} - Etap: {z.etap+1}/{len(trasa)}, Postęp: {z.postep:.1f}/{p.do_zrobienia}, Rany: {z.rana}")

    def gadka(self, kto, pkt):
        if pkt > 15: txt = "leci jak natchniony!"
        elif pkt < 5: txt = "chyba myśli o obiedzie..."
        else: txt = "robi swoje."
        print(f"    -> {kto} {txt} (+{pkt:.1f} pkt)")

    def moc_info(self, info):
        print(f"    >>> [MOC]: {info} <<<")
