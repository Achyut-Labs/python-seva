#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615
n = int(input("Input an integer : "))
n1 = n
n2 = n * n
n3 = n * n * n
a = n1+n2+n3
print (a)
