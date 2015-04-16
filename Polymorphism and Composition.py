# Polymorphism

a = "alfa"
print type(a)

b = (1, 2, 3, 4, 5)
print type(b)

c = ['o', 'm', 'e', 'g', 'a']
print type(c)

print a[2]  # 'f'
print b[2]  # 3
print c[2]  # 'e'


class Animal(object):
    def __init__(self, name=""):
        self.name = name

    def talk(self):
        print "I'm a generic Animal. Boring."


class Cat(Animal):
    def talk(self):
        print "Meow!"


class Dog(Animal):
    def talk(self):
        print "Woof!"

a = Animal()
a.talk()

c = Cat()
c.talk()

d = Dog()
d.talk()


# Inheritance ==>  Is-a relationship

# Composition ==> Has-a relationship

class Phone(object):
    def __init__(self, brand, model):
        self.brand = brand
        self.model - model

class Person(object):
    def __init__(self):
        self.phone = Phone()

stan = Person(iPhone)
print stan.phone



class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"


class Child(object):
    def __init__(self, name):
        self.name = name
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child("bobby")

son.implicit()
son.override()
son.altered()


print son.__dict__

# Drilling down in a dictionary
# child = {
#     "name": "johnny",
#     "age": 6,
#     "eye_color": "blue",
#     "phone": {
#         "brand": "Nokia",
#         "color": "blue",
#     }
# }
# print child["phone"]["brand"]


# Great example of composition
class FootballTeam(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Parent(object):
    pass


class Child(Parent):
    def __init__(self):
        self.football_team = FootballTeam("cowboys", "blue and white")




































