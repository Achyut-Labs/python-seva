hi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bye = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
helloAgain = []


#odd
for i in hi:
    if i % 2 != 0:
        helloAgain.append (i)



#even
for i in bye:
    if i % 2 == 0:
        helloAgain.append (i)

print(helloAgain)  