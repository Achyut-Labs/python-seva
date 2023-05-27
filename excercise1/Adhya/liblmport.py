import Mymaths 
def main():
    print("hello we are playing a math game")
    a=int(input("Enter 1 number for maths"))
    b=int(input("Enter another number for maths"))
    print(Mymaths.myAddition(a,b))
    print(Mymaths.myMultiplication(a,b))
    print(Mymaths.mySubtraction(a,b))
    print(Mymaths.myDivision(a,b))


if __name__=='__main__':
    main()                     