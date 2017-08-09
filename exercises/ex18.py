# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "agr1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes 1 argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one prints nothing
def print_none():
    print "I've got nothin'."

print_two("Daria", "Morgun")
print_two_again("Hello", "beautiful")
print_one("First!")
print_none()
