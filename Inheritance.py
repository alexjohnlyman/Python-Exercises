# Inheritance
# Is an "is a" relationship

# Implicit Inheritance
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

    def explicit(self):
        print "PARENT explicit()"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):
    def implicit(self):
        print "CHILD implicit()"
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()    # this will display "PARENT altered()". The 'super' takes 2 parameters super(class that you are trying to get the parent/super of, self)
        print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()
# #
# # dad.implicit()
# # son.implicit()
# #
# # dad.explicit()
# # son.explicit()
#
# dad.altered()
# son.altered()

class Cat(object):
    def speak(self):
        print "meow"

class Lion(Cat):
    def speak(self):
        super(Lion, self).speak()
        print "roar"

# felix = cat()
leo = Lion()

# felix.speak()
leo.speak()

