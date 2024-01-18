asiakkaan_hytti = input("Syötä hyttiluokka")

if asiakkaan_hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella")
elif asiakkaan_hytti == "A":
    print("A on ikkkunallinen hytti autokannen yläpuolella")
elif asiakkaan_hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif asiakkaan_hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else :
    print("Virheellinen hyttiluokka")