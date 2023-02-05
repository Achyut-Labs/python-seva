# Find the odd number and create new list of odd numbers
a = [10,3,14,15,17]
b = []

print(len(a))
for i in range(0, len(a)):
    if i % 2 != 0:
        b.append(a[i])

print(b)