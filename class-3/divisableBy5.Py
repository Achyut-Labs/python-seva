numbers=[1,2,3,4,5,6,7,8,9,10]
divisibleby5=[]
print(len(numbers))
for random in numbers: 
    if random % 5 ==0:
        divisibleby5.append(random)
        print(divisibleby5)
