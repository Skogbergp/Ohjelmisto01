#leviskä = 20 naulaa
#naula = 32 luotia
#luot =13.3 grammaa
leviskä = int(input("Anna leviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))

leviskä_grams = leviskä * 20 * 32 *13.3
naulat_grams = naulat * 32 * 13.3
luodit_grams = luodit * 13.3
mass = leviskä_grams + naulat_grams + luodit_grams
kilograms = mass // 1000
grams = mass % 1000
print(f"Massa nykymittojen mukaan:\n{int(kilograms)} kilogrammaa ja {grams:.2f} grammaa. ")