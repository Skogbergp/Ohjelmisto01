lista = [1,5,"juha",3.14,[2,5],(1,2,8),{"eka":4,"toka":False}]
"""""
print(lista[-1]["eka"])
print(lista[6]["toka"])

print(lista[2:6:1])

print(lista[0:5:1])
print(lista[0:5])
print(lista[:5])

print(lista[4:])

print(lista[5][2])

print(lista[3::-1])

print(f"{"juha" in lista}")
lista.append(100)
print(lista[-1])
"""

for _ in range(8):
    print("moi")
