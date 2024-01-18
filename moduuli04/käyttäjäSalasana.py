username = "python"
password = "rules"
isUserIn = False
while isUserIn == False:
    input_username = input("Syötä kayttäjä: ")
    input_password = input("Syötä salasana: ")

    if username == input_username and password == input_password:
       print("Tervetuloa!")
       isUserIn = True
    else :
        print("Pääsy evätty!")