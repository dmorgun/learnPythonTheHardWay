# Declare the number of cars
cars = 100
# Declare the amount of seats in each car
space_in_a_car = 4
# Declare the number of drivers available
drivers = 30
# Declare the number of passengers
passengers = 90
# Calculate the number of cars w/o drivers
cars_not_driven = cars - drivers
# Calculate the number of cars with drivers
cars_driven = drivers
# Calculate the capacity of tranporting both drivers and passengers
carpool_capacity = cars_driven * space_in_a_car
# Calculate average number of passengers in a single car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Hey %s there" % "you"
