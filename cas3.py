# from cas1 import Car
#
# car = Car("zolta", 1000, 35, 25, 5000)
#
# car.prodazba("Crvena")
# car.lizing()

# class A():
#     def __init__(self):
#         print("instanca od klasa A")
#         self.att_a = 10
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("instanca od klasa B")
#         self.att_b = 20
#
#
# class C():
#     def __init__(self):
#         super().__init__()
#         print("instanca od klasa C")
#         self.att_c = 25


# b = B()
# print("pristap do att_a preku klasa b ",b.att_b)
# print("pristap do att_a preku klasa b", b.att_a)



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
        print("drdrdr")


car = Car("zolta", "sk-1234-ab", "benzin", 7)
truck = Truck("sina", "sk-4321-ab", "dizel", 25)


print(car.zvuk())
print(truck.zvuk())