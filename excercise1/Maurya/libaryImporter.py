import mymaths 

def calscStatus():
    while True:
        playagain = input("Would you wish to use the calculator again(valid responses yes or no)?")
        if playagain == 'yes':
            main()
        elif playagain == 'no':
            break
        else:
            print("I don't know what you are saying, please use the valid responses")
    


def main():
    print("Let's do some Maths together!!")
    a= int(input("Enter your first number"))
    b= int(input("Enter your second number"))

    print(mymaths.myAddition(a, b))
    print(mymaths.myMultiplication(a, b))
    print(mymaths.mySubtraction(a, b))
    print(mymaths.myDivision(a, b)) 
    calscStatus()


    
    
if __name__ == '__main__':
    main()