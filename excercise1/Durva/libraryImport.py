import myMaths
 
input('Do you want to play a maths game? yes or no: ')

def input():
    t=True
    while t:
     d= input('Do you want to play a game? Enter y/n: ')
     if d == yes.lower():
        main()

     elif d == no.lower():
        t=False
    else:
       print(' Please enter [y]es or [n]o')


def main():
    print('My Pal Cal')
    a = int(input("Enter your first number for maths: "))
    b = int(input("Enter your second number for maths: "))

    print(myMaths.myAddition(a, b))
    print(myMaths.myMulipilcation(a, b))
    print(myMaths.mySubstraction(a, b))
    print(myMaths.myDivision(a, b))

if __name__ == '__main__':
    main()
