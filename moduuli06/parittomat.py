def parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset
original_list = [1,2,3,4,5,6,7,8,9]
print(original_list)
print(parittomat(original_list))