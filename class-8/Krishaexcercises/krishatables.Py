#Write a program to print multiplication table of a given number.

input =int(input("write a number:"))         #input is a integer you randomly entered. 
                                             
num = 1                                      #num is 1
y = range(1, 13)                             #y is 1 to 13. 

for x in y:                                  #for x in 1 to 13, the num equals the number you entered times x. 
    num = input*x 

print(input,'x', 'x', '=', num)              













