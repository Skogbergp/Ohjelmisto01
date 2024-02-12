class hissi():
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

class talo():

    def __init__(self, talon_ylinkerros, talon_alinkerros,hissienmäärä):
        self.talon_ylinkerros = talon_ylinkerros
        self.talon_alinkerros = talon_alinkerros
        self.hissit = []

        for _ in range(hissienmäärä):
            self.hissit.append(hissi(self.talon_alinkerros,self.talon_ylinkerros))

    def aja_hissiä(self, hissi, kerros):
        self.hissit[hissi].siirry_kerrokseen(kerros)

    def palohalytys(self):
        for i in range(len(self.hissit)):
            self.hissit[i].siirry_kerrokseen(self.talon_alinkerros)


a = hissi(1,10)

a.siirry_kerrokseen(5)
a.siirry_kerrokseen(6)
a.siirry_kerrokseen(1)

taloA = talo(6,1,4)
taloA.aja_hissiä(2,3)
taloA.aja_hissiä(3,5)

taloA.palohalytys()