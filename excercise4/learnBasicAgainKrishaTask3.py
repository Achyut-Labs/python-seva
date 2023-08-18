# 3. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

# a is the integer the operator puts into the code as input
# n1, n2 and n3 is defined and the '%s%s' makes the 'a's as 555 instead of 5x5x5
# the code prints n1 + n2 + n3
#if n = 5, 5 + 55 + 555 = 615