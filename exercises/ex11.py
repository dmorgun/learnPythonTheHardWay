# We put a , (comma) at the end of each print line.
# This is so print doesn't end the line with a newline character and go to the next line.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

print "Hey girl! Can I have your number?",
answer = raw_input()
print "Could you write it down for me please?"
number = raw_input()

print "Okay, so the number is %s" % (number)
