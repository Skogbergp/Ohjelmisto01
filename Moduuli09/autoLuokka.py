class auto:
    def __init__(self, rekisteri_tunnus, huippunopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus):
        if self.nykyinen_nopeus + nopeus < self.huippunopeus:
            self.nykyinen_nopeus += 0
        else:
            self.nykyinen_nopeus = self.nykyinen_nopeus + nopeus


auto = auto("ABC-123", 142)
print(auto.nykyinen_nopeus)
auto.kiihdyta(100)
print(auto.nykyinen_nopeus)
