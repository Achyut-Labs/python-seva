'''
Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
'''

input = input("Enter a number:")      #the number you enter will become the variable 'input'

x=0                                   #x equals to 0 for it to give the correct answer. 

for n in range(1, int(input), +1):    #n is a variable to make a for loop.The range is starting at 1 to the number you enter. It adds 1 every time. 
    x = x + n                         #x is 0 so it would be 0 plus 1 and because it is a loop, 

print(x)                              #it would add 1 each time (+1 in the range) until it reaches the number you entered. 
