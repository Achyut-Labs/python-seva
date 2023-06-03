#Count the total number of digits in a number
#Write a program to count the total number of digits in a number using a while loop.



n=int(input("Enter number here:"))               #n is the variable of the number that has been entered
count=0                                          #count = 0 and while the number that is entered is greater than 0,
while(n>0):                                      #the code will continue. count+1 and //10 cancel each other out. 
    count=count+1                                
    n=n//10
print("The number of digits in the number:", count)



    



