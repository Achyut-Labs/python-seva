a = [1, 5, 13, 20, 47, 25, 60, 82, 90, 100,]
b = []

print(len(a))
for i in a:
    if i % 5 == 0:
        b.append (i)

print(b) 