class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self,nimi,paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.paatoimittaja)

class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.kirjoittaja)
        print(self.sivumaara)


aku = Lehti("Aku Ankka","Aki Hyyppä")
hytti_nro6 = Kirja("Hytti Nro6","Rosa Liksom",200)

hytti_nro6.tulosta_tiedot()
aku.tulosta_tiedot()