import myMath

def calcStatus():
    while True: 
        k = input('Do you want to use the calculator again? Enter Yes or No.:')
        if k == 'yes':
            main()
        elif k == 'no':
           exit()
        else: 
             print("Please enter either yes or no")
    

def main():
    print('The calculator')
    a = int(input('Enter your first number for maths'))
    b = int(input('Enter your second number for maths'))

    print('Addition:', myMath.myAddition(a,b))
    print('Multiplication:', myMath.myMultiplication(a,b))
    print('Subtraction:', myMath.mySubtraction(a,b))
    print('Division:',myMath.myDivision(a,b)) 
    calcStatus()

if __name__ == '__main__':
    main()