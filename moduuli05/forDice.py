import random
dice_amount = int(input("Kuinka monta noppaa heitetään: "))

total = 0

for luku in range(dice_amount):
    total += random.randint(1,6)
print(f"Silmälukujen summa: {total}")