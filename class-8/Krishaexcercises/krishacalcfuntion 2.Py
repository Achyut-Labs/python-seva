def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

def minus(a, b):
    return a - b


a = int(input("Enter a first number:  "))

b = int(input("Enter a second number: "))

result = sum(a, b)
print("sum: ", result)

result = multiply(a, b)
print("Multiplication: ", result)


result = division(a, b)
print("division: ", result)


result = minus(a, b)
print("minus: ", result)
