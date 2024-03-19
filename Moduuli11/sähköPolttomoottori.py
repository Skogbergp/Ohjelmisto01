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


class Sahköauto(auto):
    def __init__(self, akkukapasiteetti, rekisteri_tunnus, huippunopeus):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteri_tunnus, huippunopeus)


class Polttomoottoriauto(auto):
    def __init__(self, tankin_koko, rekisteri_tunnus, huippunopeus):
        self.tankin_koko = tankin_koko
        super().__init__(rekisteri_tunnus, huippunopeus)


poltto = Polttomoottoriauto(32.3, "ACD-123", 165)
sahko = Sahköauto(52.5,"ABC-15",180)

sahko.kiihdyta(20)
poltto.kiihdyta(19)

sahko.kulje(3)
poltto.kulje(3)
sahko.tulosta()
poltto.tulosta()
