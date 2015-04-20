# # List comprehension
#
# # Declare a new list like normal, except you add logic inside of the list and it will create the list inline
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # regular list
#
# # Good for creating new lists
#
# # new_list = [*transform, *iteration, * *filter]
# new_list = [x**2 for x in my_list]
# # List comp can support condition statements as part of the transform
# new_list = [x**2 for x in my_list if x % 2 == 0]
# # If you wanted to keep some of the items. This would NOT be considered a filter of the iteration.
# new_list = [x**2 if x % 2 == 0 else x**3 for x in my_list]
# # Adding a filter to the List comprehension
# new_list = [x**2 if x % 2 == 0 else x**3 for x in my_list if x not in range(3, 7)]
# # Adding text to it
# new_list = ["%s is even" % x if x % 2 == 0 else "%s is odd" % x for x in my_list if x not in range(3, 7)]
#
#
# print new_list