# Exercise 21: Functions Can Return Something
def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "Substracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it anyway

print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide (iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# =====
# 27 * 184 + 76 / 1

my = divide(add(multiply (27, 184), 76), 1)

print "my: %d" % my

# =====
# a * b /c - d
# float() is used for numbers with floating point, int() is used for integers
a = float(raw_input("What is 'a'? "))
b = float(raw_input("What is 'b'? "))
c = float(raw_input("What is 'c'? "))
d = float(raw_input("What is 'd'? "))

my1 = substract(divide(multiply(a, b), c), d)
print my1
