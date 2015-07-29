# List comprehension

# Declare a new list, except you add logic inside of the list and it will create the list inline

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Good for creating new lists

# new_list = [*transform, *iteration, * *filter]
# new_list = [x**2 for x in my_list]

# List comp can support condition statements as part of the transform
# new_list = [x**2 for x in my_list if x % 2 == 0]

# If you wanted to keep some of the items. This would NOT be considered a filter of the iteration.
# new_list = [x**2 if x % 2 == 0 else x**3 for x in my_list]

# Adding a filter to the List comprehension (the if x not in statement)
# new_list = [x**2 if x % 2 == 0 else x**3 for x in my_list if x not in range(3, 7)]

# Adding text to the last example
# new_list = ["%s is even" % x if x % 2 == 0 else "%s is odd" % x for x in my_list if x not in range(4, 6)]
# print new_list

# Example of what the previous example would be w/op list comprehension
# long_new_list = []
# for x in my_list:
#     if x not in range(4, 6):
#         if x % 2 == 0:
#             long_new_list.append("%s is even" % (x))
#         else:
#             long_new_list.append("%s is odd" % (x))
# print long_new_list
