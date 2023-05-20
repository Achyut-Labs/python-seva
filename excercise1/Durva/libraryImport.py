import myMaths
 
input('Do you want to play a maths game? yes or no: ')


def main():
    print("We are doing Mathamatics")
    a = int(input("Enter your first number for maths: "))
    b = int(input("Enter your second number for maths: "))

    print(myMaths.myAddition(a, b))
    print(myMaths.myMulipilcation(a, b))
    print(myMaths.mySubstraction(a, b))
    print(myMaths.myDivision(a, b))





if __name__ == '__main__':
    main()
