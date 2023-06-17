import myMaths

def main(): #refer to line 16 #Ok so we created a a library (libImport), and now we are trying to use a function but it is not being called upon so the first time to computer goes through this code, it ignore the def main(). Ok Now refer to line 16...again...
    print("We are doing Mathematics")
    a = int(input("Enter your first number for maths"))
    b = int(input("Enter your second number for maths"))

    print(myMaths.myAddition(a, b))
    print(myMaths.mySubtraction(a, b))
    print(myMaths.myMultiplication(a, b))
    print(myMaths.myDivision(a, b))

if __name__ == '__main__':
    main() # Ok now refer to line 3
    # Hi. So because it was not called on before we call on it now, by writing main() the commputer will read the programme, go back to line 3, and recall the def main(). After senpai notices line 3, it will also read the rest of the code and actually go through with it. Hope that helps.