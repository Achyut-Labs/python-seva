# Short Python Code Snippets

Python as a high-level programming language, allows you to focus on the core functionality of the application by taking care of common programming tasks. The simple syntax rules of the programming language further make it easier for you to keep the code base readable and application maintainable. Below tips and tricks to help you code faster. There are many short Python code snippets that can be used as a reference in your work.

## Digitize

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
