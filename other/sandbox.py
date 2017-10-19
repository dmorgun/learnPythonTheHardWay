# for animal in ["dog", "cat", "mouse"]:
#     # You can use {0} to interpolate formatted strings. (See above.)
#     print "{0} is a mammal".format(animal) # {0} is an index of the list to be used

(x, y) = (0, 5)
try:
    z = y/x
except ZeroDivisionError:
    print "You cannot divide by zero"
