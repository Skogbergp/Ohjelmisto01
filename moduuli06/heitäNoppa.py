import random

maxDice = int(input("Syötä nopan korkein silmäluku: "))
def HeitäNoppa(max):
    return random.randint(1,max)

while True :

    luku = HeitäNoppa(maxDice)
    if luku == maxDice:
        print(luku)
        break
    else:
        print(luku)