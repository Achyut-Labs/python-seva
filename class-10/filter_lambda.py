'''
filter() Arguments
The filter() function takes two arguments:

function - a function
iterable - an iterable like sets, lists, tuples etc.

'''


def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))
print(get_multiples_of_five(50))

print(lambda k: not k % 5, range(50))