import random

points_total = int(input("Syötä pisteiden kokonaismäärä: "))
points_in_circle = 0
i = x = y = 0

while i < points_total:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x ** 2) + (y ** 2) < 1:
        points_in_circle += 1
    i += 1

print(f"piin likiarvo: {(4 * points_in_circle) / points_total}")
