# Declaring the 1st sentence
x = "There are %d types of people" % 10
# Declaring variables
binary = "binary"
do_not = "don't"
# Declaring the 2nd sentence; string put inside a string x2 times
y = "Those who know %s and those who %s." % (binary, do_not)

# printing the 1st and the 2nd sentences
print x
print y

# Putting a string inside another string; string put inside a string x2 times
print "I said %r." % x
print "I also said '%s'." % y

# Assigning boolean value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# printing a joke
print joke_evaluation % hilarious

# Showing concatenation of 2 strings
w = "This is the left side of..."
e = "a string with a right side. "

print w + e
