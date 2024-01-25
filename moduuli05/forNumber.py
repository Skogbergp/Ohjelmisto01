user_input = input("Syötä kokonaisluku: ")
user_numbers = []

while user_input !="":
    user_numbers.append(int(user_input))
    user_input = input("Syötä kokonaisluku: ")
user_numbers.sort(reverse=True)
for luku in range(0,5):
    print(user_numbers[luku])