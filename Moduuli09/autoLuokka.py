import random


class Auto:  #tehtävä 1 tehty auto luokan alustus
    def __init__(self, rekisteri_tunnus, huippunopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kulje(self, kuljettu_aika): #tehtävän 3 kulje functio
        self.kuljettu_matka += self.nykyinen_nopeus * kuljettu_aika

    def kiihdyta(self, nopeus): # tehtävä 2 kiihdytä metodi

        if (self.nykyinen_nopeus + nopeus) > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif(self.nykyinen_nopeus + nopeus) < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = self.nykyinen_nopeus + nopeus

    def tulosta(self):  #tulostaa auton tiedot
        print(f"Rekisteritunnus: {self.rekisteri_tunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Kuljettu matka: {self.kuljettu_matka}")


ongoing = True
autot = []

auto = Auto("ABC-123",142) #Tehtävä 1 esimerkki auto
print("tehtävä 1 auto")
auto.tulosta()                                       #tulostaa esimerkki auton tiedot
print("\n")

print("tehtävä 2 tulostukset")
auto.kiihdyta(30)
print("nykyinen nopeus: "+(auto.nykyinen_nopeus))
auto.kiihdyta(70)
print("nykyinen nopeus: "+auto.nykyinen_nopeus)
auto.kiihdyta(50)
print("nykyinen nopeus: "+auto.nykyinen_nopeus)
auto.kiihdyta(-200)
print("nykyinen nopeus: "+auto.nykyinen_nopeus)

#tehtävä 4 alkaa tästä
for i in range(1, 11):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))


while ongoing:

    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kuljettu_matka > 10000:
            for auto2 in autot:
                auto2.tulosta()
            ongoing = False
