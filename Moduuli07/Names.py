names = set()
user_input = input("Syötä nimi")
while user_input != "":
    if user_input in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(user_input)
    user_input = input("")
for n in names:
    print(n)