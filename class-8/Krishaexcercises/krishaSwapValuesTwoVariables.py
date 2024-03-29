### Swap values between two variables

#In other languages, to swap values between two variables without using a third variable, we either have to use arithmetic operators or bitwise XOR. In Python, it is much simpler, as shown below.


a = 5                               
b = 10                                                                
a, b = b, a                                                                
print(a) # 10                               
print(b) # 5


