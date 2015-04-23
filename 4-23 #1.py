
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
# cat_dog('catdog')  True
# cat_dog('catcat')  False
# cat_dog('1cat1cadodog')  True



def cat_dog(str):
    num_of_cats = 0
    # num_of_dogs = 0
    for i in range(len(str)-1):
        if str[i:i+3] is "cat":
            num_of_cats += 1
        return num_of_cats



print cat_dog('catdog')
print cat_dog('catcat')
print cat_dog('1cat1cadodog')