"""""
while True:
    userInput = input("Syötä nimi: ")
    if userInput == "James":
        break

userInput = input("Syötä nimi: ")
while userInput != "James":
    userInput = input("Syötä nimi: ")
"""
while input("syötä nimi: ") != "James":
    print("et ole James")