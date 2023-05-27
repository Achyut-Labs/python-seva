import myMaths
 

def recall():
    while True:
        replay= input("Do you want to continue playing the maths game?(yes/no): ")
        if replay == 'yes':
            main()
        elif replay== 'no':
            break
        else:
            print("Your response is unclear. Please type yes or no")




def main():
    print('My Cal Game')
    a = int(input("Enter your first number for maths: "))
    b = int(input("Enter your second number for maths: "))

    print(myMaths.myAddition(a, b))
    print(myMaths.myMulipilcation(a, b))
    print(myMaths.mySubstraction(a, b))
    print(myMaths.myDivision(a, b))
    recall()

if __name__ == '__main__':
    main()