# Креирајте класа возило (Vehicle).
# Едно возило ги има атрибутите, boja, broj na tablica, gorivo.
# Креирајте класа Car која ги има атрибутите boja, broj na tablica, broj_na_sedista, gorivo,
# Креирајте класа Truck која ги има атрибутите boja, broj na tablica, nosivost, gorivo,

# Дефинирајте функција zvuk која што ќе симулира каков звук се испушта возилото кога се вози.
# Класта Car и Truck имаат различен звук при движење.

class Vehicle():
    def __init__(self, boja, broj_na_tablica, gorivo):
        self.boja = boja
        self.broj_na_tablica =broj_na_tablica
        self.gorivo = gorivo
    def zvuk(self):
        return "brmbrm"

class Car(Vehicle):
    def __init__(self,boja, broj_na_tablica, gorivo, broj_na_sedista):
        super().__init__(boja, broj_na_tablica,gorivo)
        self.broj_na_sedista = broj_na_sedista

    def zvuk(self):
        return "vrummm"


class Truck(Vehicle):
    def __init__(self, boja, broj_na_tablica, gorivo, nosivost):
        super().__init__(boja, broj_na_tablica, gorivo)
        self.nosivost = nosivost

    def zvuk(self):
        return "drdrdr"


car = Car("zolta", "sk-1234-ab", "benzin", 7)
truck = Truck("sina", "sk-4321-ab", "dizel", 25)


print(f"car: {car.zvuk()}")
print(f"truck: {truck.zvuk()}")