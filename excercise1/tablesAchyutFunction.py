'''
Write a program to print multiplication table of a given number,
num = input("Enter the number for table") Using function

if its 2

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
'''


def m(a, b):
    z = a * b
    return z

input = int(input('write a number : '))
num = 1
multiplyNum = range(1,13)


for thing in multiplyNum:
    num = m(input, x)
    print(input,'x',thing,'=',num)
    
