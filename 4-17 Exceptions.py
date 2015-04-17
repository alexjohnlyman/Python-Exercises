# catching the exceptions before they happen!!

while True:
    try:
        my_num = raw_input("Enter number: ")
        int(my_num)  #This is a check to make sure that the input is an int
        # my_num = int(my_num)  #this changes the input into an int
        break
    except ValueError:
        my_num = raw_input("Not a number. Hit return to try again.")
    # except ZeroDivisionError:
    #     my_num = raw_input("Try again. Enter number:")

print my_num


# This would take care of someone trying to divide by 0
num1 = int(raw_input("Please enter 1st number: "))
num2 = int(raw_input("Please enter 2nd number: "))

print num1 + num2
print num1 - num2
print num1 * num2

try:
    print num1 / num2
except ZeroDivisionError:
    print "Infinity"

# This would take care of both integers and zeros
my_num = raw_input("Please enter an int: ")

while True:
    try:
        int(my_num)
        1/int(my_num)
        break

    except ValueError:
        my_num = raw_input("AN INT ONLY!!!: ")

    except ZeroDivisionError:
        my_num = raw_input("NO ZEROS ALLOWED!!!: ")

print my_num


# Our Try statements can have an else block or an if/else
my_num = raw_input("Please enter an int: ")

while True:
    try:
        int(my_num)
        1/int(my_num)

    except ValueError:
        my_num = raw_input("AN INT ONLY!!!: ")

    except ZeroDivisionError:
        my_num = raw_input("NO ZEROS ALLOWED!!!: ")

    else:
        print my_num
        break

    finally: # The Finally block will always get executed no matter what. Could be useful to close file handles or close database connections.
        print "Finally!"
# You can also nest Try/Except inside of Try/Except

# Raise statement allows me to raise my own exceptions, or define my own errors
# Exceptions are classes, so write them with capital letter, and camel case
class MyError(StandardError):
         def __init__(self, arg):
             self.arg = arg
         try:
             raise MyError("This is a user-defined error")
         except MyError as me:  # Older version of Python used a comma vs. “as.”
             print me.arg








































