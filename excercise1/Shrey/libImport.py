import myMaths


def main():
    print("We are doing mathamathics")

    true = True
    
    while true:
        print("Are you ready to play the math game")
        a = int(input("Enter your number for maths: "))
        b = int(input("Enter your second number for maths: "))

        print('Addition',myMaths.myAddition(a, b))
        print('Multiplication',myMaths.myMultiplication(a, b))
        print('Subbtraction',myMaths.mySubbtraction(a, b))
        print('Divsion',myMaths.myDivsion(a, b))


    

    
        choice = input("Enter 'no' to exit or Enter 'yes' to continue: ")

        if choice.lower() == "exit":
            break
        elif choice .lower() == "yes":
            pass
        else:
            exit()

    
        
        
if __name__ == '__main__':
    main()

