num1 = float(input("anna jaettava\n"))
num2 = float(input("anna jakaja\n"))
while (num2 == 0):
    num2 = float(input("Ei voi olla 0. anna jakaja:\n5"))
print(f"jakolaskun tulos on {num1 / num2:.2f}")
