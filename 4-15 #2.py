"""
Create two classes, an Employee and a Job, where the Employee class has-a Job class.
When printing an instance of the employee object the output should look something like this:

My name is Morgan Williams, I am 24 years old and I am a Software Developer
"""

class Job(object):
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

class Employee(object):
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.job = Job(position, salary)
        print "My name is {}, I am {} years old and I am a {} and I make {}.".format(self.name, self.age, self.job.position, self.job.salary)


mw = Employee("Morgan Williams", 24, "SD", "a shitload")


# or using def __str__


class Job(object):
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

class Employee(object):
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.job = Job(position, salary)

    def __str__(self):
        return "My name is {}, I am {} years old and I am a {} and I make {}.".format(self.name, self.age, self.job.position, self.job.salary)


mw = Employee("Morgan Williams", 24, "SD", "a shitload")
print mw