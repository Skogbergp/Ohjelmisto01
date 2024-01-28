user_input = int(input("Syötä luku: "))
alku_luku = True

if user_input < 2:
    alku_luku = False
else:
    for i in range(2, int(user_input**0.5)+1):
        if user_input % i == 0:
            alku_luku = False
if alku_luku:
    print(f"Luku {user_input} on alkuluku")
else:
    print(f"Luku {user_input} ei ole alkuluku")