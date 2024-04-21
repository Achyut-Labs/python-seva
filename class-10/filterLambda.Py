'''
filter() Arguments
The filter() function takes two arguments:

function - a function
iterable - an iterable like sets, lists, tuples etc.

'''


def get_multiples_of_any_number(*args):
    return list(filter(lambda k: not k % 7, range(*args)))
print(get_multiples_of_any_number(1,700,2))
