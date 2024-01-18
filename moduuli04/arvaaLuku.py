import random

gameNumber = random.randint(1,10)
userNumber = 0

while gameNumber != userNumber:
    userNumber = int(input("Arvaa numero: "))
    if userNumber == gameNumber:
        print("Oikein")
    elif userNumber > gameNumber:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")