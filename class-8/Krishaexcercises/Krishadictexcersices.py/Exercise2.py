'''
Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

'''

dict1 = {'ten':10, 'twenty':20, 'thirty':30}   #first I wrote the dictionary terms. Then I made the output a variable (y) 
dict2 = {'thirty':30, 'fourty':40, 'fifty':50} #so it would be easier to make it print. 

y={**dict1,**dict2}
print(y)