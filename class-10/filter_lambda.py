'''
filter() Arguments
The filter() function takes two arguments:

function - a function
iterable - an iterable like sets, lists, tuples etc.

'''


def get_multiples_of_five(a,b,c):
    return list(filter(lambda k: not k % 7, range(a,b,c)))
print(get_multiples_of_five(1, 700, 2))
