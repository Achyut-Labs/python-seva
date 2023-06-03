
'''
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

'''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict = dict(zip(keys, values))
print(dict)


#found answer using https://careerkarma.com/blog/python-convert-list-to-dictionary/#:~:text=To%20convert%20a%20list%20to%20a%20dictionary%20using%20the%20same,the%20values%20of%20a%20list.
