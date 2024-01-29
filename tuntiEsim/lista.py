list = [1,3,4,5,6,9,10,17,23,24,25,26,27,28,29]
result = []
for i in list:
    if i % 2 !=0:
        result.append(i)
print(result)



for i in list:
    if i % 2 == 0:
        list.remove(i)

print(list)