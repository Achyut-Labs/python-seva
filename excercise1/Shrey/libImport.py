import myMaths


def main():
    print("We are doing mathamathics")
    
    while True:
        print("Are you ready to play the math game")
        a = int(input("Enter your number for maths: "))
        b = int(input("Enter your second number for maths: "))

        print('Addition',myMaths.myAddition(a, b))
        print('Multiplication',myMaths.myMultiplication(a, b))
        print('Subbtraction',myMaths.mySubbtraction(a, b))
        print('Divsion',myMaths.myDivsion(a, b))


    

    
        choice = input("Enter 'exit' to exit or press Enter to continue: ")

        if choice.lower() == "exit":
            break

        if input == "no":
            break  
    
        
        
if __name__ == '__main__':
    main()

