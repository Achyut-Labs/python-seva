#4. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time : 2014-07-05 14:34:14

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# we are using the library datetime 
# now is a variable. datetime.datetime.now() gets the current date and time
# %Y (year) , %m (month) , %d (day) , %H (hour), %M (minute) , %S (second)
# strftime makes the date and time in a readable form 