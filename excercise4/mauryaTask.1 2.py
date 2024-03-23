#Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java
#Output : java
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
