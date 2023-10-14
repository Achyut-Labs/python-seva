# HOW DOES GITHUB WORK:
-
→

**SCM**- SOURCE CODE MANAGEMENT
→ Github is known as a ***SCM*** Tool

→ We have a ***Server*** and a ***Local***

Our server is Github.com

# SERVER: 
SERVER: GITHUB.COM


 Under github we have:  
        GITHUB
          ↆ
          PROJECT 
            ↆ
             BRANCHES

# Local
 Our branch is known as Local

Under Local we have:
        DEVELOPMENT
          ↆ
          STAGING/RELEASE
            ↆ
             MASTER → Your Branch! AKA Local


# Mirroring:
Whatever you have in the server you have in the local. Every time you pull and push your code, you update it into the server. That means that everytime your code is updated, whatever is in your local, will also be in the server. This is known as "mirroring"

# Cloning
We can also clone our local branch.
When you clone a repository, you copy the repository from GitHub.com to your local machine. Cloning a repository pulls down a full copy of all the repository data that GitHub.com has at that point in time, including all versions of every file and folder for the project.

# To Properly be up to date we must:
→Make sure you have commited everything from your branch
→ go into the main branch
→gitpull main
→Switch branches.
→in aira's branch → git merge main
→ Git Pull
→ Git Push

# So Then What are Conflicts? And Why do We Have Them?
Often, merge conflicts happen when people make different changes to the same line of the same file, or when one person edits a file and another person deletes the same file. You must resolve all merge conflicts before you can merge a pull request on GitHub.\

# Stashing Changes
To apply your changes to your repository, you must save the files and then commit the changes to a branch. If you have saved changes that you are not ready to commit yet, you can stash the changes for later. When you stash changes, the changes are temporarily removed from the files and you can choose to restore or discard the changes later. You can only stash one set of changes at a time with GitHub Desktop. If you use GitHub Desktop to stash changes, all unsaved changes will be stashed. After you stash changes on a branch, you can safely change branches or make other changes to your current branch.

If you use GitHub Desktop to switch branches while you have saved, but not committed, changes, GitHub Desktop will prompt you to stash the changes or bring them to the other branch. 


# BACK TO THE  BASICS

*What is Python?*
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.


***It is used for***:
→web development (server-side),
→software development,
→mathematics,
→system scripting.

# What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

# Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.

Python runs on an interpreter system, meaning that code can be executed as soon as it is written. 
  → Prototyping can be very quick.

Python can be treated in:
a procedural way
an object-oriented way
a functional way.

*** It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.***

***Python Syntax compared to other programming languages

→Python was designed for readability, and has some similarities to the English language with influence from mathematics.
→ Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
→ Python relies on indentation, using whitespace, to define scope; such as the *scope* of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

e.g. try this:
aira = apple

def sum():
  aira = 'She is 14'
  print(" I am in function sum()")

print(aira)

The scope your boundary of existence.

*Workflow*
You have software
you build the package
you verify it
you test it
you ship to the customer
from developemnt to the customer
This is known as a workflow.
This workflow can be automated through python and testing.

e.g. rock paper scissors game
we can test the program by writing another program which can help test the python to make sure our original program works.

# SYNTAX IN PYTHON:
We have a syntax in python which is a set of rules required for the computer to properly recognise the code and run it.

Examples of Syntax in Python are:
→ **Indentation**
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.

→ **Variable**
In Python, variables are created when you assign a value to it:
Python has no command for declaring a variable.

→ **Comments**
Python has commenting capability for the purpose of in-code documentation.
Comments start with a #, and Python will render the rest of the line as a comment:

We can also use three apostrophes at the start and end of the block of your comment. This is known as multi-line commenting.
e.g.
'''
Hello.
Goodbye.
'''

# PYTHON VARIABLES
Variables are containers for storing data values.

#### Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
Varibales are used to store different values.
Variables do not need to be declared with any particular type, and can even change type after they have been set.

*Varible types involve*:
- Boolean
- String
- Integer 
- Float

If you want to specify the data type of a variable, this can be done with casting.
This can be important especially if you want to program something like a game.
e.g. Int("3")

# Single or Double Quotes?
String variables can be declared either by using single or double quotes:
e.g if you want to write John's... we can use double quotes.-> "John's"


# Case-Sensitive
Variable names are case-sensitive. Therefore, a and A are two different variables

**Variable Names**
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).


### Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

*Legal variable names*:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

*Illegal variable names*:

2myvar = "John"
my-var = "John"
my var = "John"

# Multi Words Variable Names
Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:
Our team is using 
**Camel Case**
Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

Example
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

Example
# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# PYTHON DATATYPES
