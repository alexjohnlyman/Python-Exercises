"""
Write a class that demonstrates both inheritance and composition.

You will end up writing 3 classes, and one of those classes will be the class
that demonstrates the 'has-a' composition relationship and the 'is-a' inheritance relationship.

Example: a Car class that 'is-a' automobile, and 'has-a' engine.
"""


class Cat(object):
    def speak(self):
        print "I am a cat."

    def __init__(self, hair=True, talks=False):
        self.hair = hair
        self.talks = talks


class Tiger(Cat):
    def speak(self):
        print "I am a tiger. I have {}." .format(self.hair)
        super(Tiger, self).speak()


class TVShow(object):
    def __init__(self, show_name):
        self.show_name = show_name


class Cartoon(object):
    def __init__(self, name, show, talks=True):
        self.name = name
        self.show = show
        self.talks = talks

    def speak(self):
        print "I am {}. I have {} and I can {}" .format(self.name, self.hair, self.talks)
        # super(Cat, self).speak()


tom_and_jerry = TVShow("Tom and Jerry")
my_cartoon = Cartoon("Tom", tom_and_jerry, False)

print my_cartoon.show.show_name





# #You could initialize the TVShow inside of the Cartoon class, but this could start
# to get really long depending on how many atributes you had in the TVShow class

# class Cat(object):
#     def speak(self):
#         print "I am a cat."
#
#     def __init__(self, hair=True, talks=False):
#         self.hair = hair
#         self.talks = talks
#
#
# class Tiger(Cat):
#     def speak(self):
#         print "I am a tiger. I have {}." .format(self.hair)
#         super(Tiger, self).speak()
#
#
# class TVShow(object):
#     def __init__(self, show_name, air_time, producers):
#         self.show_name = show_name
#         self.air_time = air_time
#         self.producers = producers
#
#
# class Cartoon(object):
#     def __init__(self, name, show_name, air_time, producers, talks=True):
#         self.name = name
#         self.show = TVShow(show_name, air_time, producers)
#         self.talks = talks
#
#     def speak(self):
#         print "I am {}. I have {} and I can {}" .format(self.name, self.hair, self.talks)
#         # super(Cat, self).speak()
#
#
# tom_and_jerry = TVShow("Tom and Jerry")
# my_cartoon = Cartoon("Tom", tom_and_jerry, False)
#
# print my_cartoon.show.show_name



# cat1 = Cat()
# cat1.speak()
#
# tiger1 = Tiger()
# tiger1.speak()
#
# garfield1 = Cartoon("Garfield")
# garfield1.speak()






#Another example
#
# class Habitat(object):
#     def __init__(self, name, temperature):
#         self.name = name
#         self.temperature = temperature
#
#
# class Mammal(object):
#     def __init__(self, name, age, habitat):
#         self.name = name
#         self.age = age
#         self.habitat = habitat
#
#
# my_habitat = Habitat("Swamp", 90)
#
# my_mammal = Mammal("Fido", 8, my_habitat)
#
# print my_mammal.habitat.temperature