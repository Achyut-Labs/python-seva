''' Find the odd number and create new list of odd numbers
a = [10,3,14,15,17]
b = []

print(len(a))
for i in a:
    if i % 2 != 0:
        b.append(i)

print(b)



# Print elements from odd positions in a list
a = [10,3,14,15,17]
b = []
'''
sonic = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stone = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
eggman = []

print(len(sonic))
for i in sonic:
    if i % 2 != 0:
        eggman.append(i)

print(len(stone))

for x in stone:
    if x % 2 == 0:
        eggman.append(x)

print(eggman)