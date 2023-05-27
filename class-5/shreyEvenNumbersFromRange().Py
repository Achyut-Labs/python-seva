x = input("Enter the number to find all prime numbers less than that number:")
x = int(x)
i = 0
result = []

for i in range(0,x):
    if i % 2 ==0: 
        result.append(i)


print(result)