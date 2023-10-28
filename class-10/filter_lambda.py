'''
filter() Arguments
The filter() function takes two arguments:

function - a function
iterable - an iterable like sets, lists, tuples etc.

'''


def get_any_multiples(*args):
    return list(filter(lambda k: not k % 7 , range(*args)))
print(get_any_multiples(1,700,2))