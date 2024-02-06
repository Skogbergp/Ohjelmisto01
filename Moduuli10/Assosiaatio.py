class hissi():
    def __init__(self,alinkerros,ylinkerros):
        self.alinkerros=alinkerros
        self.ylinkerros=ylinkerros
        self.nykyinenKerros = 0


    def tulostakerros(self):
        print(self.nykyinenKerros)

    def siirry_kerrokseen(self,kerros):

            while self.nykyinenKerros < kerros:
                if self.nykyinenKerros + 1 < self.ylinkerros:
                    self.kerros_ylös()

            while self.nykyinenKerros > kerros:
                if self.nykyinenKerros - 1 < self.alinkerros:
                    self.kerros_alas()


    def kerros_ylös(self):
        self.nykyinenKerros += 1
    
    def kerros_alas(self):
        self.nykyinenKerros -= 1

class talo():

    def __init__(self, talon_ylinkerros, talon_alinkerros,hissienmäärä):
        self.talon_ylinkerros = talon_ylinkerros
        self.talon_alinkerros = talon_alinkerros
        self.hissit = []

        for _ in range(hissienmäärä):
            self.hissit.append(hissi(talon_alinkerros,talon_ylinkerros))

    def aja_hissiä(self ,hissi, kerros):
        self.hissit[hissi].siirry_kerrokseen(kerros)

    def palohalytys(self):
        for i in range(len(self.hissit)):
            self.hissit[i].siirry_kerrokseen(self.talon_alinkerros)
            self.hissit[i].tulostakerros()



a = hissi(1,10)

a.siirry_kerrokseen(5)
a.tulostakerros()
a.siirry_kerrokseen(2)
a.tulostakerros()
a.siirry_kerrokseen(12)

talo_a = talo(2,0,4)
talo_a.aja_hissiä(2,3)
talo_a.hissit[2].tulostakerros()