import random


class auto:
    def __init__(self, rekisteri_tunnus, huippunopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kulje(self, kuljettu_aika):
        self.kuljettu_matka += self.nykyinen_nopeus * kuljettu_aika

    def kiihdyta(self, nopeus):

        if (self.nykyinen_nopeus + nopeus) > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        else:
            self.nykyinen_nopeus = self.nykyinen_nopeus + nopeus

    def tulosta(self):
        print(f"Rekisteritunnus: {self.rekisteri_tunnus}")
        print(f"Nykyinen nopeus: {self.nykyinen_nopeus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Kuljettu matka: {self.kuljettu_matka}")


class Kilpailu:
    def __init__(self,nimi,pituus,autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autotlista = autolista

    def tunti_kuluu(self):
        for auto in self.autotlista:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autotlista:
            auto.tulosta()
    def kilpailu_ohi(self):
        for auto in self.autotlista:
            if auto.kuljettu_matka > self.pituus:
                print("kilpailu on saatu päätökseen")
                for auto2 in self.autotlista:
                    auto2.tulosta()
                return True
        return False


autot = []

for i in range(1, 11):
    autot.append(auto(f"ABC-{i}", random.randint(100, 200)))

romuralli = Kilpailu("Suuri romuralli",8000,autot)

kuluneet_tunnit = 0
while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    kuluneet_tunnit += 1
    if kuluneet_tunnit % 10 == 0:
        romuralli.tulosta_tilanne()