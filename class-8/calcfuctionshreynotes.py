def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b
                                         #denfing all the funtions 
def division(a, b):
    return a / b

def minus(a, b):
    return a - b   


a = int(input("Enter a first number:  "))
                                                           #the input from the user 
b = int(input("Enter a second number: "))

result = sum(a, b)                  #doing all the functions                        
print("sum: ", result)

result = multiply(a, b)
print("Multiplication: ", result)

result = division(a, b)
print("division: ", result)


result = minus(a, b)
print("minus: ", result)