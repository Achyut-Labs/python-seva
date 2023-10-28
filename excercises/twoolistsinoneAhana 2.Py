
sleep = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pillow = [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
bed = []

print(len(sleep))
for i in sleep:
    if i % 2  != 0:
        bed.append(i)


print(len(pillow))
for i in pillow:
    if i % 2 == 0:
      bed.append(i)

print(bed)



