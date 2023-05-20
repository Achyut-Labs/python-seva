import myMaths

def calcStatus():
    while True:
        answer = input("do you want to play again?(valid response (yes or no):")
        if answer == 'yes': 
            main()    
        elif answer == 'no':
            exit()
        else:
            print("please enter a vaild value. (yes or no)")


def main():
    print("We are doing Mathematics")
    a = int(input("Enter your first numbers for maths"))
    b = int(input("Enter your second number for maths"))

    print('Addition:',myMaths.myAddition(a , b)) 
    print( 'Subtraction:',myMaths.mySubtraction(a , b))
    print( 'Multiplication:',myMaths.myMultiplication(a , b))
    print( 'Division:',myMaths.myDivision(a , b))
    calcStatus()


if __name__ == '__main__':
    main()

    
    
    
    
