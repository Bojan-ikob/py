# Напишете класа Person која има атрибути за име и возраст. Потоа креирајте класа Student која наследува од Person и додава атрибут за резултат од испит.
# Креирајте пример на објект од Student и испечатете ги сите информации.
# Креирајте метод во класата Person кој ја враќа целосната информација за личноста.
# Креирајте метод во класата Student кој ја враќа целосната информација за студентот (вклучувајќи го резултатот од испит)



# class Person:
#     def __init__(self, ime, vozrast):
#         self.ime = ime
#         self.vozrast = vozrast
#
#     def informacii(self):
#         return f"Ime: {self.ime}, Vozrast: {self.vozrast}"
#
# class Student(Person):
#     def __init__(self, ime, vozrast, rezultat):
#         super().__init__(ime, vozrast)
#         self.rezultat = rezultat
#
#     def informacii(self):
#         return f"{super().informacii()}, Rezultat: {self.rezultat}"
#
# student = Student("Bojan", 35, 88)
# print(student.informacii())



# 2 Zadaca

# class Vehicle:
#     def __init__(self, tip_vozilo, broj_trkala, kolicina_gorivo):
#         self.tip_vozilo = tip_vozilo
#         self.broj_trkala = broj_trkala
#         self.kolicina_gorivo = kolicina_gorivo
#         self.nivo_na_gorivo = kolicina_gorivo
#         self.startuvan_motor = False
#
#     def proverka_na_gorivo(self):
#         return self.nivo_na_gorivo
#
#     def startuvaj_motor(self):
#         if self.nivo_na_gorivo > 0:
#             self.startuvan_motor = True
#             print(f"{self.tip_vozilo} motorot e startuvan")
#         else:
#             print(f"Nema dovolno gorivo za da se startuva {self.tip_vozilo}")
#
#     def iskluci_motor(self):
#         self.startuvan_motor = False
#         print(f"Motorot na {self.tip_vozilo} e isklucen")
#
#     def vozi(self, kilometri, potrosuvacka_po_km):
#         if not self.startuvan_motor:
#             print(f"Motorot na {self.tip_vozilo} ne e startuvan. Startuvajte go motorot za da vozite.")
#             return
#
#         potrebno_gorivo = kilometri * potrosuvacka_po_km
#         if self.nivo_na_gorivo >= potrebno_gorivo:
#             self.nivo_na_gorivo -= potrebno_gorivo
#             print(f"{self.tip_vozilo} izmina {kilometri} km. Ostanuva {self.nivo_na_gorivo} litri gorivo.")
#         else:
#             print(f"Nema dovolno gorivo za da izminete {kilometri} km. Napolnete go rezervoarot.")
#
#
# class Car(Vehicle):
#     def __init__(self, tip_vozilo, broj_trkala, kolicina_gorivo, model, broj_na_sedista):
#         super().__init__(tip_vozilo, broj_trkala, kolicina_gorivo)
#         self.model = model
#         self.broj_na_sedista = broj_na_sedista
#
#     def polnenje_gorivo(self, sipano_gorivo):
#         self.nivo_na_gorivo += sipano_gorivo
#         if self.nivo_na_gorivo > self.kolicina_gorivo:
#             self.nivo_na_gorivo = self.kolicina_gorivo
#             print("Rezervoarot e poln.")
#         else:
#             print(f"Vo rezervoarot ima {self.nivo_na_gorivo} litri gorivo.")
#
#     def proverka_za_aktiviran_motor(self):
#         status = "e startuvan" if self.startuvan_motor else "ne e startuvan"
#         print(f"Motorot {status}, so {self.nivo_na_gorivo} litri gorivo.")
#
#
# class Truck(Vehicle):
#     def __init__(self, tip_vozilo, broj_trkala, kolicina_gorivo, kapacitet_tovar, kolicina_na_tovar=0):
#         super().__init__(tip_vozilo, broj_trkala, kolicina_gorivo)
#         self.kapacitet_tovar = kapacitet_tovar
#         self.tovaren = kolicina_na_tovar
#
#     def tovaranje(self, kolicina):
#         if self.tovaren + kolicina <= self.kapacitet_tovar:
#             self.tovaren += kolicina
#             print(f"Tovareno e {kolicina} kg. Momentalen tovar: {self.tovaren} kg.")
#         else:
#             print(f"Nema mesto da se tovari {kolicina} kg.")
#
#     def rastovar(self, kolicina_istovareno):
#         if self.tovaren - kolicina_istovareno < 0:
#             print("Ne mozhe da se istovari poveќе od momentalniot tovar.")
#         else:
#             self.tovaren -= kolicina_istovareno
#             print(f"Rastovareno {kolicina_istovareno} kg. Ostanuva uste {self.tovaren} kg.")
#             if self.tovaren == 0:
#                 print("Celiot tovar e istovaren.")
#
#
#
# car1 = Car("Avtomobil1", 4, 45, "Model 1", 5)
# truck1 = Truck("Kamion1", 12, 150, 1000, 200)
#
#
# car1.startuvaj_motor()
# car1.vozi(50, 0.8)
# car1.polnenje_gorivo(20)
#
# truck1.startuvaj_motor()
# truck1.tovaranje(500)
# truck1.rastovar(300)
# truck1.vozi(100, 2)


# 3 zadaca

# Напишете класа Account која има метод withdraw() за повлекување пари.
# Креирајте подкласа AdminAccount која додава метод за проверка на дозвола за повлекување на средства.
# Креирајте метод во класата Account за повлекување средства.
# Креирајте метод во класата AdminAccount кој ќе дозволи повлекување само ако има одредени права


class Account:
    def __init__(self, sostojba):
        self._sostojba = sostojba

    def povlekuvanje_pari(self, kolicina):
        if kolicina > self._sostojba:
            print("nemate dovolno na smetka")
        else:
            self._sostojba -= kolicina
            print(f"uspesno povleceni {kolicina} denari.\n preostanato: {self._sostojba}")

class AdminAccount(Account):
    def __init__(self, sostojba, broj_na_smetka, lozinka, dozvola):
        super().__init__(sostojba)
        self._broj_na_smetka = broj_na_smetka
        self._lozinka= lozinka
        self._dozvola = dozvola

    def proverka_za_dozvola(self, broj_na_smetka, lozinka):
        return self._broj_na_smetka == broj_na_smetka and self._lozinka == lozinka


admin = AdminAccount(10000, 123456789, 1234, True)

if admin.proverka_za_dozvola(123456789, 1234):
    print("Tocni podatoci... podignete sredstva.")
    admin.povlekuvanje_pari(2000)
else:
    print("Nevalidni podatoci.")
