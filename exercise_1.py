
firstInt = int(raw_input("Please enter the first integer: "))
secondInt = int(raw_input("Please enter the second integer: "))

if secondInt == 0:
        print "You can't divide by zero. Try again."
else:
    print "The sum of %d and %d is: %e" %(firstInt, secondInt, firstInt + secondInt)
    print "The difference of %d and %d is: %e" %(firstInt, secondInt, firstInt - secondInt)
    print "The product of %d and %d is: %e" %(firstInt, secondInt, firstInt * secondInt)
    print "The quotient of %d and %d is: %e with a remainder: %e" %(firstInt, secondInt, firstInt / secondInt,  firstInt % secondInt)


#if isinstance(firstInt, int) and isinstance(secondInt, int):
#    if secondInt == 0:
#        print "You can't divide by zero. Try again."
#    else:
#       print "The sum of %d and %d is: %e" %(firstInt, secondInt, firstInt + secondInt)
#       print "The difference of %d and %d is: %e" %(firstInt, secondInt, firstInt - secondInt)
#       print "The product of %d and %d is: %e" %(firstInt, secondInt, firstInt * secondInt)
#       print "The quotient of %d and %d is: %e with a remainder: %d" %(firstInt, secondInt, firstInt / secondInt,  firstInt % secondInt)
#else:
#   while firstInt != int or secondInt != int:
#       if firstInt != int:
#           firstInt = raw_input("Not a number. Please enter the first integer: ")
#   elif secondInt != int:
#       secondInt = raw_input("Not a number. Please enter the second integer: ")

