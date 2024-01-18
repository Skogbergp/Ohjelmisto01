#37cm
kuha_length = int(input("Syötä kuhan pituus senttimetreinä: "))
alin_mitta = 37
if kuha_length < alin_mitta:
    print(f"Kuha on alamittainen.\nLaske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {alin_mitta - kuha_length}cm")

else :
    print(f"aikamoinen saalis \nKuhasi on {kuha_length - alin_mitta}cm yli alimman pyyntimitan.")