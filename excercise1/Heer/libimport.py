import myMaths

def main():
    print("We are doing Mathematics")
    a = int(input("Enter your first numbers for maths"))
    b = int(input("Enter your second number for maths"))

    print(myMaths.myAddition(a , b)) 
    print(myMaths.mySubtraction(a , b))
    print(myMaths.myMultiplication(a , b))
    print(myMaths.myDivision(a , b))


if __name__ == '__main__':
    main()
    
    
    
    
