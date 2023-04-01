k = [1, 5, 11, 15, 24, 27, 52, 66, 80, 89, 100]
s = []

print(len(k))
for i in k:
    if i % 5 == 0:
        s.append(i)

print(s)