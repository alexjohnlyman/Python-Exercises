# Recursion: A function that calls itself

# def foo():
#     foo()

import time
#
# def countdown(n):
#     print n
#
#     if n == 0:
#         return
#
#     else:
#         time.sleep(1)
#         countdown(n-1)
#
# countdown(10)


# my_list = [1, 3, 5, 7, 9, 11, 13]
#
# def list_sum(nums):
#     print "list_sum() has been called with the list", nums
#
#     if len(nums) == 1:
#         print "You've reached the base case"
#         return nums[0]
#
#     else:
#         result = nums[0] + list_sum(nums[1:])
#         print "Intermediate results: List is now", nums[1:], "and the result is:", result
#         return result
#
# print list_sum(my_list)


# fib = [0, 1, 1, 2, 3, 5, 8, 13]


# Working fibonacci sequence with basic timer
fib_number = 10


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_time():
    start = time.time()
    number = fib(fib_number)
    print "The fib (%i) took %.7f seconds" % (number, time.time() - start)

fib_time()


# Time complexity: O(2^n)
#
# def fib(n):
#     if n == 0:
#         print "n reached 0"
#         return 0
#     elif n == 1:
#         print "n reached 1"
#         return 1
#     else:
#         print "Calling fib(" + str(n-1) + ") + fib(" + str(n-2) + ")"
#         return fib(n-1) + fib(n-2)
#
# print fib(4)


# Improved version that has one replaces recursion with a for loop
# fib_number = 7


def fib_improved(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        # print a, b
    return a


def fib_improved_time():
    start = time.time()
    new_number = fib_improved(fib_number)
    print "The fib improved (%i) \n took %.7f seconds" % (new_number, time.time() - start)

fib_improved_time()
