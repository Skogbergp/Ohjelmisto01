prob = [0.52,0.49,0.72,0.81,0.12,0.11,0.5]
result = []
for i in prob:
    if i >= 0.5:
        result.append(1)
    else:
        result.append(0)
print(result)