
firstInt = raw_input("Please enter the first integer: ")
secondInt = raw_input("Please enter the second integer: ")

while firstInt != int or secondInt != int:
    if firstInt != int:
        firstInt = raw_input("Not a number. Please enter the first integer: ")
    elif secondIntInt != int:
        secondInt = raw_input("Not a number. Please enter the second integer: ")
    else:
        int(firstInt)

if secondInt == 0:
    print "You can't divide by zero. Try again."
else:
    print "The sum of %d and %d is: %e" %(firstInt, secondInt, firstInt + secondInt)
    print "The difference of %d and %d is: %e" %(firstInt, secondInt, firstInt - secondInt)
    print "The product of %d and %d is: %e" %(firstInt, secondInt, firstInt * secondInt)
    print "The quotient of %d and %d is: %e with a remainder: %d" %(firstInt, secondInt, firstInt / secondInt,  firstInt % secondInt)
