
#0. Write a Python program to find out what version of Python you are using.
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


'''1. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java'''
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

#2. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

'''3. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615'''
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

'''4. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))