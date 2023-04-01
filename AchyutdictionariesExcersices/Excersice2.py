'''
Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

'''

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


z= {**dict1,**dict2}
print(z)

#found answer using https://favtutor.com/blogs/merge-dictionaries-python#:~:text=The%20simplest%20way%20to%20concatenate,collection%20of%20key%2Dvalue%20pairs.