# addition formula
def sum(a, b):
    return a + b
# multiplication formula
def multiply(a, b):
    return a * b
# division formula
def division(a, b):
    return a / b
# subtraction formula
def minus(a, b):
    return a - b


a = int(input("Enter a first number:  "))

b = int(input("Enter a second number: "))

# doing the Addition
result = sum(a, b)
print("sum: ", result)
# doing the Multiplication
result = multiply(a, b)
print("Multiplication: ", result)
# doing the divisiom
result = division(a, b)
print("division: ", result)
# doing the Subtraction
result = minus(a, b)
print("minus: ", result)