
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

# make_out_word('<<>>', 'Yay') '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') '<<WooHoo>>'
# make_out_word('[[]]', 'word') '[[word]]'

#i need to return a string that has 'word' spliced into 'out' after the second index [1].

#
# def make_out_word(out, word):
#     new_str = out[:2] + word + out[2:]
#     return new_str
# or
# def make_out_word(out, word):
#     return ''.join((out[:2], word, out[2:]))
#
# print make_out_word('<<>>', 'Yay')
# print make_out_word('<<>>', 'WooHoo')
# print make_out_word('[[]]', 'word')



# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

# extra_end('Hello')  'lololo'
# extra_end('ab')  'ababab'
# extra_end('Hi')  'HiHiHi'

# i need to make a 3 copies of the str[-2]


# def extra_end(str):
#     return (str[-2] + str[-1]) * 3
#
#
# print extra_end('Hello')
# print extra_end('ab')
# print extra_end('Hi')




# Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the
#  empty string "" yields the empty string "".

# first_two('Hello')  'He'
# first_two('abcdefg')  'ab'
# first_two('ab')  'ab'

#if the length of the string is more than 2 return str[:1]
# else return str

#
# def first_two(str):
#     if len(str) >=2:
#         return str[:2]
#     else:
#         return str
#
#
# print first_two('Hello')
# print first_two('abcdefg')
# print first_two('ab')
# print first_two('a')





# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#
# first_half('WooHoo')  'Woo'
# first_half('HelloThere')  'Hello'
# first_half('abcdef')  'abc'

# i need to return the length of the string/2
#
#
# def first_half(str):
#     return str[:((len(str))/2)]
#
#
# print first_half('WooHoo')
# print first_half('HelloThere')
# print first_half('abcdef')


# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
#
# without_end('Hello')  'ell'
# without_end('java')  'av'
# without_end('coding')  'odin'

# i need to cut off the [0] and [-1] of a string

# def without_end(str):
#     return str[1:-1:]
#
#
# print without_end('Hello')
# print without_end('java')
# print without_end('coding')




# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and
#  the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

# combo_string('Hello', 'hi')  'hiHellohi'
# combo_string('hi', 'Hello')  'hiHellohi'
# combo_string('aaa', 'b')  'baaab'

# i need to check which len(string) is shorter and then concatenate them.

#
# def combo_string(a, b):
#     if len(a) < len(b):
#         return a + b + a
#     else:
#         return b + a + b
#
#
#
# print combo_string('Hello', 'hi')
# print combo_string('hi', 'Hello')
# print combo_string('aaa', 'b')



# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#
# string_times('Hi', 2)  'HiHi'
# string_times('Hi', 3)  'HiHiHi'
# string_times('Hi', 1)  'Hi'

# i need to return string multiplied by n

# def string_times(str, n):
#     return str * n
#
# print string_times('Hi', 2)
# print string_times('Hi', 3)
# print string_times('Hi', 1)



# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;
#
# front_times('Chocolate', 2)  'ChoCho'
# front_times('Chocolate', 3) 'ChoChoCho'
# front_times('Abc', 3)  'AbcAbcAbc'
#
# def front_times(str, n):
#     first_three = str[:3]
#     if len(str) < 3:
#         return str * n
#     else:
#         return first_three * n
#
#
# print front_times('Chocolate', 2)
# print front_times('Chocolate', 3)
# print front_times('Abc', 3)




# Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code')  'CCoCodCode'
# string_splosion('abc')  'aababc'
# string_splosion('ab')  'aab'

# i will need to add some sort of loop to increase the

# def string_splosion(str):
#     for i in len(str):
#         str =
#
#
# print string_splosion('Code')
# print string_splosion('abc')
# print string_splosion('ab')



# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing from both other values by 2 or more.
# Note: abs(num) computes the absolute value of a number.

# close_far(1, 2, 10)  True
# close_far(1, 2, 3)  False
# close_far(4, 1, 3)  True

#i will need to check to see if a + 1 = b or c   a -1 = b or c    c +1 = b  c-1 =b

# def close_far(a, b, c):
#     if ((a + 1) or (a + 2)) == b and ((c > a + 2) or (c < a - 2)):
#         return True
#     elif ((a + 1) or (a + 2)) == c and ((b > a + 2) or (b > a - 2)):
#         return True
#     elif ((a - 1) or (a - 2)) == b and ((c > a - 2) or (c < a + 2)):
#         return True
#     elif ((a - 1) or (a - 2)) == c and ((b > a - 2) or (b < a + 2)):
#         return True
#     else:
#         return False



# def close_far(a, b, c):
#     if  abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2:
#         return True
#     elif abs(b-a) >= 2 and abs(c-a) <= 1 and abs(c-b) >= 2:
#         return True
#     else:
#         return False
#
# print close_far(1, 2, 10)
# print close_far(1, 2, 3)
# print close_far(4, 1, 3)



#
# def sum13(nums):
#     if len(nums) == 0:
#         return 0
#
#     total = 0
#     for index, number in enumerate(nums):
#        if number == 13 or nums[index-1] == 13 and index != 0:
#            continue
#        else:
#            total += number
#
#     return total
#
#
#
# print sum13([1, 2, 2, 1])
# print sum13([1, 1])
# print sum13([1, 2, 2, 1, 13])
# print sum13([1, 2, 2, 1, 13, 4])
# print sum13([])



# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb')  1
# count_code('codexxcode')  2
# count_code('cozexxcope') 2


# def count_code(str):
#   stri = list(str)
#   count = 0
#
#   for index, letter in enumerate(str):
#     if index+3 >= len(str):
#       return count
#     elif letter == "c" and str[index+1] == "o" and str[index+3] == "e":
#       count += 1
#
#   return count

# def count_code(str):
#     count = 0
#     for i in range(len(str)-3):
#         if str[i:i+2] == "co" and str[i+3] == "e":
#             count += 1
#     return count


# print count_code('aaacodebbb')
# print count_code('codexxcode')
# print count_code('cozexxcope')





# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost
#  digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple
#  of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c,
# return the sum of their rounded values. To avoid code repetition, write a separate helper
#  "def round10(num):" and call it 3 times. Write the helper entirely below and at the same
# indent level as round_sum().

# round_sum(16, 17, 18)  60
# round_sum(12, 13, 14)  30
# round_sum(6, 4, 4)  10


# def round10(num):
#     return round(num, -1)
#
# def round_sum(a, b, c):
#     return round10(a) + round10(b) + round10(c)
#
#
# print round_sum(16, 17, 18)
# print round_sum(12, 13, 14)
# print round_sum(6, 4, 4)




# Make bricks practice problem
# Go through my fail cases and have true at the end.
# - if the total number of small bricks i had + big bricks
# - if the left over of big bricks

# def make_bricks(small, big, goal):
#     if (small + (big * 5)) < goal:
#         return False
#     elif goal % 5 > small:
#         return False
#     else:
#         return True
#
#
# print make_bricks(4, 1, 9)
# print make_bricks(4, 1, 10)
# print make_bricks(4, 1, 7)






# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars.
# Return -1 if it can't be done.
#
# make_chocolate(4, 1, 9)  4
# make_chocolate(4, 1, 10)  -1
# make_chocolate(4, 1, 7)  2
# make_chocolate(6, 1, 11) 6


# STILL NEED TO WORK ON THIS

# def make_chocolate(small, big, goal):
#     if (small + (big * 5)) < goal:
#         return -1
#     elif (goal % 5) + small >= goal:
#         return (small) - ((goal)-goal%5)
#     elif (goal % 5) + small == goal:
#         return small
#     elif goal % 5 < small:
#         return goal % 5
#     elif goal % 5 > small:
#         return goal - (big*(goal%5))
#
#
#
#     # elif goal % 5 > small:
#     #     return -1
#
# print make_chocolate(4, 1, 9)
# print make_chocolate(4, 1, 10)
# print make_chocolate(4, 1, 7)
# print make_chocolate(6, 1, 11)





# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
# ignore just one copy, and likewise for the largest value. Use int division to produce the final average.
# You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100])  3
# centered_average([1, 1, 5, 5, 10, 8, 7])  5
# centered_average([-10, -4, -2, -4, -2, 0])  -3

#my original approach
# def centered_average(nums):
#     nums.sort()
#     new_list = nums[1:-1]
#     total = sum(new_list)
#     return total/len(new_list)

#original, but simplified
# def centered_average(nums):
#     nums.sort()
#     return sum(nums[1:-1:])/len(nums[1:-1:])

#math aproach
# def centered_average(nums):
#   x = max(nums)
#   y = min(nums)
#   z = sum(nums)
#   return (z - (x+y)) / (len(nums)-2)

#Delete approach
# 'del' will take the index of a list, based on the minimum number.
# As opposed to remove(max(nums)), which would remove the first instance of something

# def centered_average(nums):
#     del nums[nums.index(min(nums))], nums[nums.index(max(nums))]
#     return sum(nums)/len(nums)


# print centered_average([1, 2, 3, 4, 100])
# print centered_average([1, 1, 5, 5, 10, 8, 7])
# print centered_average([-10, -4, -2, -4, -2, 0])






