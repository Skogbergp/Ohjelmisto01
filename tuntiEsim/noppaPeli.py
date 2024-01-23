import random

player_count = 200
current_player = 1
dice_amount = 20

best_player = None
best_result = 0

while current_player <= player_count:
    result = 0
    throw_count = 0

    while throw_count < dice_amount:
        die = random.randint(1,6)
        print(f"pelaaja: {current_player}, heitto: {throw_count+1}, nopan silmäluku: {die}")
        result +=die
        throw_count+=1
    if result > best_result: #saatiinko parastulos
        best_player = f"pelaaja {current_player}"
        best_result = result
    elif result == best_result:
        best_player += f", pelaaja {current_player}"
    print(f"Pelaajan {current_player} tulos: {result}")
    current_player+=1
print(f"Paras tulos {best_result} ja {best_player}")