num = int(input('Enter a number:'))
Number = False
if Number == 1:
    for i in range(2, num):
        if Number % i == 0:
           Number = True
           break

if Number:
     print('is not a prime number')
else:
     print('is a prime number')

#I don't know what to do but Jayesh Uncle told us to edit something so here is this comment.