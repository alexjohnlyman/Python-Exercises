# __author__ = 'alexlyman'

gal = float(raw_input("Please enter the number of gallons of gasoline: "))
liter = gal * 3.7854
barrel = gal / 19.5
CarDi = gal * 20
energy = (gal * 115000)/75700
cost = gal * 4

if gal == 0:
    gal = float(raw_input("You cannot use 0. Please enter the number of gallons of gasoline: "))

print "Original number of gallons is: %f" %(gal)
print "%f gallons is equivalent of %f liters" %(gal, liter)
print "%f gallons of gasoline requires %f barrels of oil" %(gal, barrel)
print "%f gallons of gasoline produces %f pounds of CO2" %(gal, CarDi)
print "%f gallons of gasoline is energy equivalent to %f gallons of ethanol" %(gal, energy)
print "%f gallons of gasoline requires $%f US dollars" %(gal, cost)

#Eric's solution
# while True:
#     try:
#         user_input = int(user_input)



# Another option to look into
# def get_input(message):
#     try:
#         user_input = str(input(message))
#         if user_input.isdigit() and user_input is not "0":
#             return user_input
#         elif user_input is "0":
#             print("Cannot be 0!")
#         return None
#     except NameError:
#         print("That doesn't seem to be a number.")
#         return None
#
# gallons = None
#
# while gallons is None:
#     gallons = get_input("Please input the number of gallons: ")
#     if gallons is not None:
#         gallons = float(gallons)
#
#
# liters = gallons * 3.7854
# barrels = round(gallons / 19.5, 2)
# co2 = round(gallons * 20, 2)
# ethanol = round((gallons * 115000) / 75700, 2)
# price = round(gallons * 4.00, 2)
#
# print "Original number of gallons is: {}".format(gallons)
# print "Total liters: {}".format(liters)
# print "Number of barrels of oil required: {}".format(barrels)
# print "Number of pounds of CO2 produced: {}".format(co2)
# print "Equivalent energy amount of ethanol gas: {} gallons of ethanol".format(ethanol)
# print "Total cost: {}".format(price)