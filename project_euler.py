#  PROJECT EULER PROBLEMS

# ---------------------------------------------------------------------------------------------------------------------

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# def mult_of_3(x):
#     if x % 3 == 0:
#         return x
#     else:
#         return 0
#
#
# def mult_of_5(x):
#     if x % 5 == 0:
#         return x
#     else:
#         return 0
#
#
# def sum_of_mult(x):
#     total = 0
#     for i in range(x):
#         if mult_of_3(i) == i and mult_of_5(i) == i:
#             total += i
#         elif mult_of_3(i) == 0 and mult_of_5(i) == 0:
#             total += 0
#         else:
#             if mult_of_3(i) == i:
#                 total += i
#             elif mult_of_5(i) == i:
#                 total += i
#             else:
#                 total += 0
#     return total
#
# print sum_of_mult(1000)

# ---------------------------------------------------------------------------------------------------------------------
