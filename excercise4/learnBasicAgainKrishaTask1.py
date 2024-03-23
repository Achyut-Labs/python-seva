# 1. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

filename = input("Input the Filename: ")
file_extensions = filename.split(".")
print ("The extension of the file is : " + repr(file_extensions[-1]))

# filename is a variable and is the input of a filename the operator puts in.
# file extensions is the python programming language the programmer used and can exmples are py, java,band pyi
# second line of code is saying that the file extensions are found by splitting the filename at the '.'
# repr is to print a readable version of a string 
# repr(file_extensions[-1]) is saying that it will print the filename that is split from the '.' and remove the 1st part which would be the filename