# this script should be run from command line as follows:
# python ex13.py <first> <second> <third>

# argv is a module or a library
from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is called: ", first
print "Your second variable is called: ", second
print "Your third variable is called: ", third

answer = raw_input("Did you like this exercise? ")
print "Your answer was: %s" % answer
