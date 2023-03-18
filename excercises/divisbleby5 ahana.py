Duck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 69, 75, 100, 98, 15]
Cow = []


print(len(Duck))

for i in Duck:
    if i % 5 == 0:
        Cow.append(i)

print(Cow)