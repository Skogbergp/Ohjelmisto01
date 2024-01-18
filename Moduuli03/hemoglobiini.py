gender = input("Syötä biologinen sukupuolesi: ")
hemoglobiini = input("Syötä hemoglobiini arvo: ")
if gender == "Mies":
    if hemoglobiini < 195 or hemoglobiini > 134 :
        print("Hemoglobiini arvosi on normaali")
    elif hemoglobiini > 195 :
        print("Hemoglobiini arvosi on alhainen")
    else:
        print("Hemoglobiini arvosi on korkea")
elif gender == "Nainen":
    if hemoglobiini < 117 or hemoglobiini > 175:
        print("Hemoglobiini arvosi on normaali")
    elif hemoglobiini > 117 :
        print("Hemoglobiini arvosi on alhainen")
    else:
        print("Hemoglobiini arvosi on korkea")