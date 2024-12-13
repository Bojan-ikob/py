class Car():
    def __init__(self, boja, moknost, kapacitet_rezervoar, probno_vozenje, cena):
        self.boja = boja
        self.moknost = moknost
        self.kapacitet_rezervoar = kapacitet_rezervoar
        self.nivo_gorivo = 0
        self.potrosuvacka = 7
        self.is_tuned = False
        self.prbno_vozenje = probno_vozenje
        self.cena = cena
        self.lizing = 0
        self.procent = 0


    def proverka_za_gorivo(self):
        if self.nivo_gorivo != 0:
            print("vo kolata ima gorivo")
        else:
            print("treba da se napolni gorivo")

    def dopolni_gorivo(self):
        print("napolneto")
        self.nivo_gorivo = self.kapacitet_rezervoar

    def vozi(self):
        if self.nivo_gorivo == 0:
            print("nema gorivo!!!Napolnete!!!!")
        else:
            print("vozii")

    def tuning(self):
        procent_tuning = int(input("procent za tuning: "))
        self.moknost += self.moknost * procent_tuning / 100
        self.potrosuvacka += self.potrosuvacka * procent_tuning /100
        print(f"moknosta na kolata bese zgolemena na {self.moknost}")
        print(f"potrosuvackata se zgolemi na {self.potrosuvacka}")

    def posle_probno_vozenje(self):
        potroseno_gorivo  = self.prbno_vozenje * self.potrosuvacka / 100
        if self.nivo_gorivo >= potroseno_gorivo:
            self.nivo_gorivo -= potroseno_gorivo
            print(f"nivoto na gorivoto e {self.nivo_gorivo} litri")
        else:
            print("vo rezervarot nema dovolno gorivo...Nadopolnete")

    @staticmethod
    def prodazba(boja):
        if boja.lower() == "Zolta":
            print("10%popust")
        else:
            print("nema popust")

   def procent_lizing(procent):
      return f"{procent * 100}%"


    def lizing(self):
        if self.cena > 1000:
            self.lizing =  "0.1%"
        elif self.cena >= 5000:
            self.lizing = "0.12%"
        else :
            self.lizing = "0.015%"

        return self.lizing


kola1 = Car("crvena", 1000, 30, 50)
kola2 = Car("zolta", 1200, 35, 50)
kola1.proverka_za_gorivo()
kola1.vozi()
kola1.dopolni_gorivo()
kola1.vozi()
kola1.tuning()
kola1.posle_probno_vozenje()
kola1.vozi()
kola1.posle_probno_vozenje()
kola1.vozi()
kola1.posle_probno_vozenje()
kola1.vozi()
kola1.posle_probno_vozenje()

kola2.proverka_za_gorivo()
kola2.vozi()
kola2.dopolni_gorivo()
kola2.vozi()
kola2.tuning()
kola2.posle_probno_vozenje()
kola2.vozi()
kola2.posle_probno_vozenje()
kola2.vozi()
kola2.posle_probno_vozenje()


