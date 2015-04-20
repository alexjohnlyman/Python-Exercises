
# Given a string, return a string where for every char in the original, there are two chars.

def double_char(string):
    new_string = ''
    for i in string:
        new_string += (i+i)
    print new_string


# Using List Comprehension
def double_char(str):
  my_list = [char*2 for char in str]
  return ''.join(my_list)


double_char("The")
double_char('AAbb')
double_char('Hi-There')


# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not
# count towards the sum and values to its right do not count.
# So for example, if b is 13, then both b and c do not count.


def lucky_sum(a, b, c):
    if (a == 13):
        return 0
    elif (b == 13):
        return a
    elif (c == 13):
        return (a + b)
    else:
        return (a + b + c)


lucky_sum(1, 2, 3)
lucky_sum(1, 2, 13)
lucky_sum(1, 13, 3)