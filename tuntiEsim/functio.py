def erotus(luku1, luku2):
    return (luku1 - luku2)


def listatoka(lista):
    return lista[1]


def sanakirja(sanakirja):
    return sanakirja["nimi"]


lista = [1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9]

sanakir = {"nimi": "juha", "ikä": 45, "ammatti": "lääkäri"}


def parittomat(luvut):
    parittomat = []
    for i in luvut:
        if i % 2 != 0:
            parittomat.append(i)
    return parittomat


def double(luvut):
    newlist = []
    for i in luvut:
        newlist.append(i * 2)
    return newlist


def operate(lista, monikko):
    summa = 0
    for i in lista:
        if monikko[0] < i < monikko[1]:
            summa = summa + i
    return summa

def operate2(lista, monikko):
    summa = []
    for i in lista:
        if monikko[0] < i < monikko[1]:
            summa.append(i)
    return sum(summa)


luvut = [12, 5, 21, 4, 8, 0, 11]

lista = [15, 1, 8, 18, 33, 1, 2]
border = (0, 9)

result = operate2(lista, border)
parittomat = parittomat(luvut)

doubled = double(luvut)
print("Alkuperäiset luvut: " + str(luvut))
print("Parittomat luvut: " + str(parittomat))
print("tuplatut luvut: " + str(doubled))
print("Sallittujen lukujen summa: " + str(result))


def parittomatLisComp(luvut):
    return [i for i in luvut if i % 2 == 0]


def doubleLisComp(luvut):
    return [i * 2 for i in luvut]
