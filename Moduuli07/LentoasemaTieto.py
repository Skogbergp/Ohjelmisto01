lentoasemat = {
    "EFHK": "Helskinki-Vantaa lentokenttä"
}
while True:
    user_input = int(input("Uusi lentoasema(1)\nHae lentoasemaa(2)\nSulje(3)\n"))
    if user_input == 1:
        ICAO = input("Syötä lentoaseman ICAO-koodi:\n")
        lentoasema_name = input("Syötä lentoaseman nimi")
        lentoasemat[ICAO] = lentoasema_name
    if user_input == 2:
        ICAO = input("Syötä hakemasi aseman ICAO-koodi")
        print(f"Lentoaseman {ICAO} Nimi on {lentoasemat[ICAO]}")
    if user_input == 3:
        break
