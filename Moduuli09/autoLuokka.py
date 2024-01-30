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
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Kuljettu matka: {self.kuljettu_matka}")


ongoing = True
autot = []

for i in range(1, 11):
    autot.append(auto(f"ABC-{i}", random.randint(100, 200)))


while ongoing:

    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kuljettu_matka > 10000:
            for auto2 in autot:
                auto2.tulosta()
            ongoing = False
