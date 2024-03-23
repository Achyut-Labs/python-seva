cricket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cricket2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
helloAgainCricket = []


#odd
for i in cricket:
    if i % 2 != 0:
        helloAgainCricket.append (i)



#even
for i in cricket2:
    if i % 2 == 0:
        helloAgainCricket.append (i)

print(helloAgainCricket)  