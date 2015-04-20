# Functions
# Function should do one thing and do them really well
# Give your functions good names. NOT 'func1'
# Use underscore to separate words

'''
Given 3 numbers, return the sum of the first two multiplied by the third
'''

# # Best practice is to break up the functions into smaller portions
# def sum_numbers(a, b): # This is called the functions 'signature'
#     return a + b
#
# def add_then_multiply(a, b, c):
#     return sum_numbers(a, b) * c
#
# # Inline Functions (or anonymous function)
#     print lambda x: x**2
#     # basically saying, 'given x return x**2'
#         def something(x):
#             return x**2
#
# # Internal functions
# defined inside of the file
#
# # External functions
# # defined outside of the file that is calling the function
# from some_package.some_module import some_external_function
# my_var = some_external_function(param 1, param 2)


# Return statements
# Return will exit the function and return a result of some kind.
# If it a function calling another function, the second function will return control back to the original function upon completing the return


# def my_sum(x, y=1000):
#     result = x + y
#     return result
#
# print my_sum(1, 2)
# print my_sum(1)
#
#
# class Car(object):
#     def __init__(self, model, make, year, wheels=4, steering_wheel=True):  # Example of named parameter we've used in the past
#         pass


# def bar(a, b, *args, **kwargs):
#     print a, b, args, kwargs
#
# bar("hello", "whatever", 'blah', "something else here", 'I\'m a valley girl', "'ello'ello", e="This is the E value", f="F value", g="G value", h="H value")
# args are shown as tuples, kwargs are shown as a dictionary with key/value pairs
# a b ('c', 'something else here') {'e': 'This is the E value', 'f': 'F value'}







