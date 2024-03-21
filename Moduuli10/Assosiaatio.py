class Hissi(): #tehtävän 2 hissi luokka
    def __init__(self,alinkerros,ylinkerros):
        self.alinkerros=alinkerros
        self.ylinkerros=ylinkerros
        self.nykyinenKerros = alinkerros


    def tulostakerros(self):
        return print(f"Hissi on kerroksessa: {self.nykyinenKerros}")

    def siirry_kerrokseen(self,kerros):

        if kerros > self.nykyinenKerros:
            while self.nykyinenKerros < kerros:
                self.kerros_ylös()
        if kerros < self.nykyinenKerros:
            while self.nykyinenKerros > kerros:
                self.kerros_alas()

    def kerros_ylös(self):
        self.nykyinenKerros += 1
        self.tulostakerros()
    def kerros_alas(self):
        self.nykyinenKerros -= 1
        self.tulostakerros()

class Talo():   #tehtävän 2 Taloluokka

    def __init__(self, talon_ylinkerros, talon_alinkerros,hissienmäärä):
        self.talon_ylinkerros = talon_ylinkerros
        self.talon_alinkerros = talon_alinkerros
        self.hissit = []

        for _ in range(hissienmäärä):
            self.hissit.append(Hissi(self.talon_alinkerros, self.talon_ylinkerros))

    def aja_hissiä(self, hissi, kerros): #tehtävän 2 aja_hissiä functio
        self.hissit[hissi].siirry_kerrokseen(kerros)

    def palohalytys(self):  #tehtävän 3 palohälytys
        for i in range(len(self.hissit)):
            self.hissit[i].siirry_kerrokseen(self.talon_alinkerros)

#tehtävän 1 hissin
a = Hissi(1, 10)

a.siirry_kerrokseen(5)
a.siirry_kerrokseen(6)
a.siirry_kerrokseen(1)


#tehtävän 2 talo ja hissien ajo
talo = Talo(6, 1, 4)
talo.aja_hissiä(2,3)
talo.aja_hissiä(3,5)

#tehtävä 3 palohälytys
print("palohälytys")
talo.palohalytys()