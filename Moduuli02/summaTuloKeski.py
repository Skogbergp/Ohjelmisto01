input_1 = int(input("Syötä kokonaisluku: "))
input_2 = int(input("Syötä toinen kokonaisluku: "))
input_3 = int(input("Syötä kolmas kokonaisluku: "))

summa = input_1 + input_2 + input_3
tulo = input_1 * input_2 * input_3
keskiarvo = (input_1 + input_2 + input_3)/3

print(f"summa = {summa}")
print(f"tulo = {tulo}")
print(f"keskiarvo = {keskiarvo:.2f}")