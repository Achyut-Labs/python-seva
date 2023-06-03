'''
x = input("Enter the number to find all prime numbers less than that number:")

if int(x) % 2 == 1:
    print("odd")
else:
    print("even")



x = input("Enter the number to find all prime numbers less than that number: ")

if int(x) / 1 == x and int(x) /2 !=0:
    print("Prime Number")
else:
    print("Not Prime Number")
    
    
    
    



'''

#Odd
x = input("Enter the number to find all prime numbers less than that number:")

x = int(x)
i=0
result = []



for i in range(0,x):
    if i % 2 !=0:
        result.append(i)
print(result)


#Even
x = input("Enter the number to find all prime numbers less than that number:")

x = int(x)
i=0
result = []



for i in range(0,x):
    if i % 2 ==0:
        result.append(i)
print(result)