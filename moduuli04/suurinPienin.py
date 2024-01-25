user_number = input("Syötä numero: ")
big = small = float(user_number)
while user_number != "":
    user_number = float(user_number)
if user_number > big:
    big = user_number
if user_number < small:
    small = user_number
user_number = input("Syötä numero: ")
print(f"Pienin luku: {small}")
print(f"Suurin luku: {big}")
