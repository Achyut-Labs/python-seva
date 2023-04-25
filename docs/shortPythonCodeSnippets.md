# Short Python Code Snippets

Python as a high-level programming language, allows you to focus on the core functionality of the application by taking care of common programming tasks. The simple syntax rules of the programming language further make it easier for you to keep the code base readable and application maintainable. Below tips and tricks to help you code faster. There are many short Python code snippets that can be used as a reference in your work.

### Digitize

The following snippet will convert an integer into a list of digits.

```sh
num = 123456

# using map
list_of_digits = list(map(int, str(num)))

print(list_of_digits)
# [1, 2, 3, 4, 5, 6]

# using list comprehension
list_of_digits = [int(x) for x in str(num)]

print(list_of_digits)
# [1, 2, 3, 4, 5, 6]
```

### Check if a string is a palindrome

The following function is used for checking if a string is a palindrome or not.

```sh
def palindrome(string):
    return string == string[::-1]
		
palindrome('python') # False
```

Check If a Given String Is a Palindrome or Not

We have already discussed how to reverse a string. So palindromes become a straightforward program in Python.

```sh
my_string = "abcba"

if my_string == my_string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# Output
# palindrome
```

### Swap values between two variables

In other languages, to swap values between two variables without using a third variable, we either have to use arithmetic operators or bitwise XOR. In Python, it is much simpler, as shown below.

```sh
a = 5                               
b = 10                                                                
a, b = b, a                                                                
print(a) # 10                               
print(b) # 5
```

Python makes it quite simple to swap values between two variables without using another variable.

```sh
a = 1
b = 2

a, b = b, a

print(a) # 2
print(b) # 1
```

### check if the given number is even

The following function returns True if the given number is even, False otherwise.

```sh
def is_even(num):
  return num % 2 == 0
	
is_even(10) # True
```

### Split a string into a list of substrings

The following function can be used for splitting a multiline string into a list of lines.

```sh
def split_lines(s):
  return s.split('\n')
split_lines('50\n python\n snippets') # ['50', ' python', ' snippets']
```

We can split a string into a list of substrings using the .split() method in the string class. You can also pass as an argument the separator on which you wish to split.

```sh
string_1 = "My name is Chaitanya Baweja"
string_2 = "sample/ string 2"

# default separator ' '
print(string_1.split())
# ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# defining separator as '/'
print(string_2.split('/'))
# ['sample', ' string 2']
```

### Find memory used by an object

The standard library’s sys module provides the getsizeof() function. That function accepts an object, calls the object’s sizeof() method, and returns the result, so you can make your objects inspectable.

```sh
import sys
print(sys.getsizeof(5)) # 28
print(sys.getsizeof("Python")) # 55
```

### Reverse a string
Python string library doesn’t support the built-in reverse() as done by other Python containers like list. There are many approaches to reversing a string, of which the easiest way is making use of the slicing operator.

```sh
language = "python"                                
reversed_language = language[::-1]                                                                 
print(reversed_language) # nohtyp
```

The following snippet reverses a string using the Python slicing operation.

```sh
# Reversing a string using slicing

my_string = "ABCDE"
reversed_string = my_string[::-1]

print(reversed_string)

# Output
# EDCBA
```

### Print a string n times
It is very easy to print a string n times without using loops, as shown below.

```sh
def repeat(string, n):
  return (string * n)
	
repeat('python', 3) # pythonpythonpython
```

```sh
n = 3 # number of repetitions

my_string = "abcd"
my_list = [1,2,3]

print(my_string*n)
# abcdabcdabcd

print(my_list*n)
# [1,2,3,1,2,3,1,2,3]
```

### Combining a List of Strings Into a Single String
The next snippet combines a list of strings into a single string.

```sh
strings = ['50', 'python', 'snippets']
print(','.join(strings)) # 50,python,snippets
```

The join() method combines a list of strings passed as an argument into a single string. In our case, we separate them using the comma separator.

```sh
list_of_strings = ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# Using join with the comma separator
print(','.join(list_of_strings))

# Output
# My,name,is,Chaitanya,Baweja
```

### Find the first element of a list
This function returns the first element of the passed list.

```sh
def head(list):
  return list[0]
	
print(head([1, 2, 3, 4, 5])) # 1
```

We also use the most_common() function to get the most_frequent element in the list.

```sh
# finding frequency of each element in a list
from collections import Counter

my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) # defining a counter object

print(count) # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b']) # of individual element
# 3

print(count.most_common(1)) # most frequent element
# [('d', 5)]
```

### Find elements that exist in either of the two lists
This function returns every element that exists in either of the two lists.

```sh
def union(a,b):
  return list(set(a + b))
	
union([1, 2, 3, 4, 5], [6, 2, 8, 1, 4]) # [1,2,3,4,5,6,8]
```

### Find all the unique elements present in a given list
This function returns the unique elements present in a given list.

```sh
def unique_elements(numbers):
  return list(set(numbers))
	
unique_elements([1, 2, 3, 2, 4]) # [1, 2, 3, 4]
```

### Find the average of a list of numbers
This function returns the average of two or more numbers present in a list.

```sh
def average(*args):
  return sum(args, 0.0) / len(args)
	
average(5, 8, 2) # 5.0
```

### Check if a list contains all unique values
This function checks if all the elements in a list are unique or not.

```sh
def unique(list):
    if len(list)==len(set(list)):
        print("All elements are unique")
    else:
        print("List has duplicates")
				
unique([1,2,3,4,5]) # All elements are unique
```

### Track frequency of elements in a list
Python counter keeps track of the frequency of each element in the container. Counter() returns a dictionary with elements as keys and frequency of its occurrence as its values.

```sh
from collections import Counter
list = [1, 2, 3, 2, 4, 3, 2, 3]
count = Counter(list)
print(count) # {2: 3, 3: 3, 1: 1, 4: 1}
```

### Find the most frequent element in a list
This function returns the most frequent element that appears in a list.

```sh
def most_frequent(list):
    return max(set(list), key = list.count)
		
numbers = [1, 2, 3, 2, 4, 3, 1, 3]
most_frequent(numbers) # 3
```

### Convert an angle from degrees to radians
The next function is used for converting an angle from degrees to radians.

```sh
import math
def degrees_to_radians(deg):
  return (deg * math.pi) / 180.0
	
degrees_to_radians(90) # 1.5707963267948966
```

### Calculate time taken to execute a piece of code
The following snippet is used for calculating the time taken to execute a piece of code.

```sh
import time
start_time = time.time()
a,b = 5,10
c = a+b
end_time = time.time()
time_taken = (end_time- start_time)*(10**6)
print("Time taken in micro_seconds:", time_taken) # Time taken in micro_seconds: 39.577484130859375
```

### Find gcd of a list of numbers
This function calculates the greatest common divisor of a list of numbers.

```sh
from functools import reduce
import math
def gcd(numbers):
  return reduce(math.gcd, numbers)
gcd([24,108,90]) # 6
```

### Find unique characters in a string
This snippet can be used to find all the unique characters present in a string.

```sh
my_string = "aavvccccddddeee"

# converting the string to a set
temp_set = set(my_string)

# stitching set into a string using join
new_string = ''.join(temp_set)

print(new_string)
```

### Use lambda functions
Lambda is an anonymous function with the capability of holding a single expression only.

```sh
x = lambda a, b, c : a + b + c
print(x(5, 10, 20)) # 35
```

### Use map functions
This function returns a list of the results after applying the given function to each item of a given iterable(list, tuple, etc.)

```sh
def multiply(n): 
    return n * n 
  
list = (1, 2, 3) 
result = map(multiply, list) 
print(list(result)) # {1, 4, 9}
```

### Use filter functions
This function filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

```sh
arr = [1, 2, 3, 4, 5]
arr = list(filter(lambda x : x%2 == 0, arr))
print (arr) # [2, 4]
```

### Use list comprehensions
List comprehensions provide us with a simple way to create a list based on some iterable. During the creation, elements from the iterable can be conditionally included in the new list and transformed as needed.

```sh
numbers = [1, 2, 3]
squares = [number**2 for number in numbers]
print(squares) # [1, 4, 9]
```

The following snippet creates a new list by multiplying each element of the old list by two.

```sh
# Multiplying each element in a list by 2

original_list = [1,2,3,4]

new_list = [2*x for x in original_list]

print(new_list)
# [2,4,6,8]
```

### Use slicing operator
Slicing is used to extract a continuous sequence or subsequence of elements from a given sequence. The following function is used for concatenating the results of two slicing operations. First, we are slicing the list from index d to end, then from start to index d.

```sh
def rotate(arr, d):
  return arr[d:] + arr[:d]
  
if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5]
  arr = rotate(arr, 2)
  print (arr) # [3, 4, 5, 1, 2]
```

### Use chained function call
The final snippet is used to call multiple functions from a single line and evaluate the result.

```sh
def add(a, b):
    return a + b
def subtract(a, b):   
    return a - b
a, b = 5, 10
print((subtract if a > b else add)(a, b)) # 15
```

### Using rhe Title Case (First Letter Caps)
The following snippet can be used to convert a string to title case. This is done using the title() method of the string class.

```sh
my_string = "my name is chaitanya baweja"

# using the title() function of string class
new_string = my_string.title()

print(new_string)

# Output
# My Name Is Chaitanya Baweja
```

### Using the try-except-else Block
Error handling in Python can be done easily using the try/except block. Adding an else statement to this block might be useful. It’s run when there is no exception raised in the try block.

If you need to run something irrespective of exception, use finally.

```sh
a, b = 1,0

try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")
```

### Using Enumerate to Get Index/Value Pairs
The following script uses enumerate to iterate through values in a list along with their indices.

```sh
my_list = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(my_list):
    print('{0}: {1}'.format(index, value))

# 0: a
# 1: b
# 2: c
# 3: d
# 4: e
```

### Check the Memory Usage of an Object
The following script can be used to check the memory usage of an object.

```sh
import sys

num = 21

print(sys.getsizeof(num))

# In Python 2, 24
# In Python 3, 28
```

### Merging Two Dictionaries
While in Python 2, we used the update() method to merge two dictionaries; Python 3.5 made the process even simpler.

In the script given below, two dictionaries are merged. Values from the second dictionary are used in case of intersections.

```sh
dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
# Output
# {'apple': 9, 'banana': 4, 'orange': 8}
```

### Time Taken to Execute a Piece of Code
The following snippet uses the time library to calculate the time taken to execute a piece of code.

```sh
import time

start_time = time.time()
# Code to check follows
a, b = 1,2
c = a+ b
# Code to check ends
end_time = time.time()
time_taken_in_micro = (end_time- start_time)*(10**6)

print(" Time taken in micro_seconds: {0} ms").format(time_taken_in_micro)
```

### Flattening a List of Lists
Sometimes you’re not sure about the nesting depth of your list, and you simply want all the elements in a single flat list.

Here’s how you can get that:

```sh
from iteration_utilities import deepflatten

# if you only have one depth nested_list, use this
def flatten(l):
  return [item for sublist in l for item in sublist]

l = [[1,2,3],[3]]
print(flatten(l))
# [1, 2, 3, 3]

# if you don't know how deep the list is nested
l = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]

print(list(deepflatten(l, depth=3)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Sampling From a List
The following snippet generates n number of random samples from a given list using the random library.

```sh
import random

my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = random.sample(my_list,num_samples)
print(samples)
# [ 'a', 'e'] this will have any 2 random values
```

I have been recommended the secrets library for generating random samples for cryptography purposes. The following snippet will work only on Python 3.

```sh
import secrets                              # imports secure module.
secure_random = secrets.SystemRandom()      # creates a secure random object.

my_list = ['a','b','c','d','e']
num_samples = 2

samples = secure_random.sample(my_list, num_samples)

print(samples)
# [ 'e', 'd'] this will have any 2 random values
```

### Check for Uniqueness
The following function will check if all elements in a list are unique or not.

```sh
def unique(l):
    if len(l)==len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")

unique([1,2,3,4])
# All elements are unique

unique([1,1,2,3])
# List has duplicates
```
