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

# this is a way to access the first and last index
#def first_last6(nums):
  # return 6 is nums[0] or 6 is nums[-1]
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

# File i/o
# open(name, mode)
# r-read only
# w -write only (this will delete the content and allow you to write on a blank document)
# a - adds to the end of the doc
# r+ - read and write
# w+ - read and write (this will create the file if it doesn't exist)
# a+ - read and append (will also create new file if it doesn't exist)
f = open('text.txt', 'r')
text = f.read()
print text
f.close()
with open('text.txt', 'r+') as f: # similar to f = open('text.txt', 'r')
    text = f.readlines() #this will create a list that has each line entered as an item
with open('text.txt', 'r+') as f:
    lines = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']
    f.writelines(lines) # this will write 3 new lines in the

with open('text.txt', 'r+') as f: # changing one letter in a file to be something else
    for line in f:
        line = line.replace('o', '0')
        f.writelines(line)

with open('text.txt', 'r+') as f: # puts each line into a list
    text = f.readlines()
    for line in text:
        words = line.split() #if you leave line.split blank, it will split on the blank space (e.g. by word)
        print words

# DICTIONARYS
person = {} # this instantiates a new dictionary

person ={
    "name": "Bob"
    "age": "30"
    "hair_color": "brown"
    "eye_color": "brown"
    "has_teeth": True
}
print person["age"] # to get value of a certain key
#  or
print person.get("age")

person["num_legs"] = 2 # this adds a new key:value pair to a dict
print person.keys() #this prints out the keys in a dict
new_list = sorted(person) # this would sort the keys in a dict and assign them to a list
print "num_legs" in person.keys() #to see if a thing is a key in a dict

print person.items() # creates a list or key:value pairs or a tuple/ tuples are always in ()

for key, val in person.items(): # this is tuple unpacking
    print "%s ==> %s" % (key,value)

#  {} denotes a dictionary
#  [] denotes a list

# Example of what we might do for the recipe organizer
#  This is a dictionary inside of a list inside of a dictionary
recipe = {
    "name": "Pizza",
    "description": "Delicious!",
    "directions": "Make the pizza",
    "ingredients": [
        {
            "name": "pepperoni"
        },
        {
            "name": "cheese"
        },
        {
            "name": "pizza dough"
        }
    ]
}
#  to list out the ingredients
for ingredient in recipe["ingredients"]:
    print ingredient.values()

print len(person) # would return the number of key:value pairs in a dictionary



























