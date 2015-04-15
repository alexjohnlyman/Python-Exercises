# Create 2 derived classes Student and Employee from the base class Person.
# When running the completed code, you should see the following output:


# If it an attribute that can be described as a simple date type, you should use __init__ and assign attributes to your object through dot notation
class Person(object):
    def name(self, name):
        print "My name is %s." % (name),
    def age(self, age):
        print "I am %i years old." % (age),

class Student(Person):
    def job(self):
        print "I am studying at ABC Primary School.",

class Employee(Person):
    def job(self):
        print "I am teaching at ABC Primary School.",


 # def speak(self):
 #        print "My name is {}. I am {} years old. I am {} at {}".format(self.name, self.age, self.job)

peter = Student()
peter.name("Peter")
peter.age(9)
peter.job()

john = Employee()
john.name("John")
john.age(23)
john.job()

# Jared's solution
# class Person(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print "{} was just born!".format(self.name)
#
#
# class Student(Person):
#
#     def __init__(self, name, age, school):
#         super(Student, self).__init__(name, age)
#         self.action = "studying"
#         self.school = school
#
#     def speak(self):
#         print "My name is {}. I am {} years old. I am {} at {}".format(self.name, self.age, self.action, self.school)
#
#
# class Employee(Person):
#
#     def __init__(self, name, age, school):
#         super(Employee, self).__init__(name, age)
#         self.action = "teaching"
#         self.school = school
#
#     def speak(self):
#         print "My name is {}. I am {} years old. I am {} at {}".format(self.name, self.age, self.action, self.school)
#
# peter = Student("Peter", 9, "ABC Primary School")
# john = Employee("John", 23, "ABC Primary School")
#
# peter.speak()
# john.speak()