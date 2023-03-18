'''
Write a program to use for loop to print the following reverse number pattern 

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

'''
a = ['5 4 3 2 1']

for b in a:
    print(b)

    b = ['4 3 2 1']

    for c in b:
        print(c)

        c=['3 2 1']

        for d in c:
            print(d)

            d = ['2 1']

            for e in d:
                print(e)

                e = ['1']

                for f in e:
                    print(f)


'''
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
'''                    