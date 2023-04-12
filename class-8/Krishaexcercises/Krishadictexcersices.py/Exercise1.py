#Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value


#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]

#Expected output:

#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

together = dict(zip(keys, values))  #together (variable) is what outcome we need to print and dict equals to dictionary
print(together)                     