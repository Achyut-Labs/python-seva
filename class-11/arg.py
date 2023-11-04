'''
Command line arguments are a powerful way to pass parameters to a program when it is executed.
They allow users to customize the behavior of the program without modifying its source code.
Command-line arguments are used extensively in the Unix/Linux command-line interface
and are also commonly used in scripting languages like Python.
'''
import sys

if len(sys.argv) > 1:
    print(f"Hello, {sys.argv[1]}!")
else:
    print("Hello, You have no arguments!")

'''
Let's learn advanced version of this using library,

https://docs.python.org/3/library/argparse.html
'''


