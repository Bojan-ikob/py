class Employee():
    def __init__(self,ime, plata, pozicija):
        self.ime = ime
        self._plata = plata
        self.pozicija = pozicija
        self._bonus_procent = 0.1

    def get_plata(self):
        return self._plata
    def get_bonus(self):
        return self._plata * self._bonus_procent

class Manager(Employee):
    def __init__(self, ime, plata, pozicija, oddel):
        super().__init__(ime, plata, pozicija)
        self.menagira = oddel
        self.__neto_plata = self._plata + self._plata * 0.1
        self.__dodadeten_bonus_menadzer = 1.05

    def get_neto_plata(self):
        return self.__neto_plata

    def get_bonus(self):
        return self._plata * self._bonus_procent * self.__dodadeten_bonus_menadzer

vrab1 = Employee("vraboten1", 10000, "obezbeduvanje")
vrab2 = Employee("vraboten2", 12000, "obezbeduvanje nok")

sef_obezbeduvanje = Manager("menadzer", 12000, "sef na obezbeduvanje", "Obezz")


