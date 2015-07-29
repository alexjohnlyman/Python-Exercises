# Lambda
# Essentially is an in-line function, or anonymous function
# test = lambda c, s, z: c + s/z
#
# print test(1, 10, 2)


# Map
# map takes two arguments(function, sequence) and calls the function on the sequence
# Single argument
# def double(x):
#     return x ** 2
#
# print map(double, range(13, 19))
#
# # Two arguments
# a = [1, 2, 3, 4, 5, 6, 7]
#
# def double(x, y):
#     return x * y
#
# print map(double, range(13, 20), a)


# Combined Map and Lambda
# x = 4
# print map(lambda y: y*2, range(1, x+1))


# Filter
# Takes two arguments(function, sequence) and returns which items are true in the sequence, based on the function
# y = range(1, 100)
# def is_even(x):
#     if x % 2 == 0:
#         return x
#
# print filter(is_even, y)


# Reduce
# Returns single value(function, sequence) after calling function on the first two items in the sequence,
# after this it calls the function on the result and the next item, etc.
# def multiply(x, y):
#     return x * y
#
# print reduce(multiply, range(1, 7))
