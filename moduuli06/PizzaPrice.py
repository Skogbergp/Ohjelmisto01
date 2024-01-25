import math
def pizza_price(size, price):
    pizza_area = math.pi * size ** 2
    return (pizza_area / price)  # price per m^2


user_pizza_size = []
user_pizza_price = []
for luku in range(0, 2):
    user_pizza_size.append(int(input("Syötä pizzan halkaisija(cm): ")))
    user_pizza_price.append(int(input("Syötä pizzan hinta €: ")))
pizza1 = pizza_price(user_pizza_size[0], user_pizza_price[0])
pizza2 = pizza_price(user_pizza_size[1],user_pizza_price[1])

if pizza1 > pizza2:
    print("Ensimmäinen pizza antaa parempaa vastiketta rahallesi")
else:
    print("Toinen pizza antaa parempaa vastiketta rahallesi")
