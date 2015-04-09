# Lists:

my_list = range(11) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_string = "Hello"

print "Is %i in my_list?" % 0
print 0 in my_list

print "Is %s in my_string?" % "H"
print "H" in my_string

my_list = [1, 2]
my_list.append([3, 4])
# append will add a 3rd item which is a list
print my_list
my_list.extend([3, 4])
# extend will add 3rd and 4th items to the same list
print my_list
my_list.insert(1, "Two")
# insert will add 3rd and 4th items into the list starting at the index
print my_list

item = my_list.pop()
print "Last item was: " + str(item)
# or
last_item = my_list.pop()
print last_item
print my_list
# Pop will remove the last item from the list and returns it to

new_list =[]
for i in reversed(my_list):
    new_list.append(i)
print new_list
# creates a new list, which is reversed. You can do this with stride, new_list = my_list[::-1]

#  Sort
my_list = [9, 7, 5, 3, 2, 1]

# Print original list
print my_list
# Returns [9, 7, 5, 3, 2, 1]

# Return sorted list. This doesn't change the original list.
# We're storing it in new sorted_list variable
sorted_list = sorted(my_list)

print sorted_list
# Returns [1, 2, 3, 5, 7, 9]

# my_list remains unchanged
print my_list
# Returns [9, 7, 5, 3, 2, 1]

# Sort list in place. This actually changes the list.
my_list.sort()

print my_list
# Returns [1, 2, 3, 5, 7, 9]



# def find_hello(string):
#     return "hello" in string.lower()
# print find_hello(my_string)

#
#
# Reciepe
# ingredient = "PiZZa DouGh"
# ingredient.lower() or ingredient.capitalize() or  ingredient.title() or ingredient.lower().replace(' ', '_')
#
# if text in my_list:
#     print my_list.index(text)
# else:
#     my_list.append(text)
#     print my_list

