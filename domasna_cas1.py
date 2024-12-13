import random
# class Vraboten:
#     def __init__(self, ime, maticen_broj, plata, data_na_vrabotuvanje):
#         self.ime = ime
#         self.maticen_broj = maticen_broj
#         self.plata = plata
#         self.data_na_vrabotuvanje = data_na_vrabotuvanje
#
#     def __str__(self):
#         return (
#             f"Ime: {self.ime}, "
#             f"Maticen broj: {self.maticen_broj}, "
#             f"Plata: {self.plata}, "
#             f"Data na vrabotuvanje: {self.data_na_vrabotuvanje}"
#         )
#
#
# class Kompanija:
#     def __init__(self, ime, vraboteni=None):
#         self.ime = ime
#         self.vraboteni = vraboteni if vraboteni is not None else []
#
#     def dodadi_vraboten(self, vraboten):
#         self.vraboteni.append(vraboten)
#
#     def __str__(self):
#         vraboteni_str = "\n".join([str(vraboten) for vraboten in self.vraboteni])
#         return f"Ime: {self.ime}, Vraboteni:\n{vraboteni_str}"
#
#
#
# vraboten1 = Vraboten("Bojan", "112233445566", "250000", "01.01.2000")
# print(vraboten1)
#
#
# komp1 = Kompanija("Prom")
# komp1.dodadi_vraboten(vraboten1)
#
# print(komp1)


#  bingo


import random

class Bingo:
    def __init__(self):
        self.igraci = []
        self.izvleceni_broevi = []

    def dodadi_igrac(self, ime, broevi):
        if len(broevi) != 5 or len(broevi) != len(set(broevi)) or not all(1 <= broj <= 15 for broj in broevi):
            raise ValueError("Mora da vnesete tocno pet razlicni broevi pomedju 1 i 15.")
        else:
            self.igraci.append({"ime": ime, "broevi": broevi})

    def izvleci_bingo_broevi(self):
        self.izvleceni_broevi = random.sample(range(1, 16), k=5)

    def presmetaj_rezultati(self):
        rezultati = []
        for igrac in self.igraci:
            pogodoci = set(igrac["broevi"]).intersection(self.izvleceni_broevi)
            rezultati.append({"ime": igrac["ime"], "pogodoci": len(pogodoci), "pogodeni_broevi": list(pogodoci)})
        return rezultati

    def prikazi_rezultati(self):
        print("\nIzvleceni bingo broevi:", self.izvleceni_broevi)
        print("\nRezultati:")
        for igrac in self.igraci:
            pogodoci = set(igrac["broevi"]).intersection(self.izvleceni_broevi)
            print(f"Igrac: {igrac['ime']}, Broevi: {igrac['broevi']}, Pogodoci: {len(pogodoci)}, Pogodeni broevi: {list(pogodoci)}")


bingo = Bingo()

while True:
    try:
        ime = input("Vnesete go imeto na igracot: ").strip()
        broevi = list(map(int, input("Vnesete gi pette bingo broevi oddeleni so zapirka: ").split(',')))

        bingo.dodadi_igrac(ime, broevi)

        dodadi_povekje = input("Dali sakate da dodadete uste eden igrac? (da/ne): ").strip().lower()
        if dodadi_povekje == "ne":
            break
    except ValueError as e:
        print(f"Greska: {e}")

bingo.izvleci_bingo_broevi()
bingo.prikazi_rezultati()