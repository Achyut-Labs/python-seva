# Crate a new list from a two list using the following condition
# Create a new list from a two list using the following condition
food=[1,4,6,9,7]
water=[2,5,8,3,0]
eggs=[]

print(len(food))
for i in food:
    if i % 2 != 0:
        eggs.append(i)

print(eggs)

print(len(water))
for i in water:
    if i % 2 == 0:
        eggs.append(i)

print(eggs)



