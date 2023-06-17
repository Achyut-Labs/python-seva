import os
import re
import myMaths

def main():
    print("Hey bro, do you want to use the Mathematics Calculator?")
valid_responses = ['yes', 'no']
a = int(input("Enter your first number for maths"))
b = int(input("Enter your second number for maths"))

print(myMaths.myAddition(a, b))
print(myMaths.mySubtraction(a, b))
print(myMaths.myMultiplication(a, b))
print(myMaths.myDivision(a, b))



if __name__ == '__main__':
    main()