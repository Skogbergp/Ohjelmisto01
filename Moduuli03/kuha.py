#37cm
kuha_length = int(input("Syötä kuhan pituus: "))
alin_mitta = 37
if kuha_length > alin_mitta:
    print(f"aikamoinen saalis \nKuhasi on {kuha_length - alin_mitta}cm yli alimman pyyntimitan.")

else :
    print(f"Kuha on alamittainen.\nLaske kuha takaisin järveen."
          f"\nAlimmasta sallitusta pyyntimitasta puuttuu {alin_mitta - kuha_length}cm")