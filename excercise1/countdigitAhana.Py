
n=int(input("Enter number:"))

 # enter the value of the integer and store it in a variable.

count=0

while(n>0): 

    #while loop used and the last digit of the number is obtained by using the floor division.

    count=count+1

    n=n//10

print("The number of digits in the number are:",count)


