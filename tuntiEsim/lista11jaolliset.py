result = []
result2 = []
for i in range(10,100):
    if i % 11 == 0:
        result.append(i)
print(result)

for i in range(11,100,11):
    result2.append(i)
print(result2)