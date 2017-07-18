#mystuff = []
#mystuff.append('hello')

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait, there is no 10 things in a list, let's fix that"

stuff = ten_things.split(' ')
print stuff
print len(stuff)

more_stuff = ["Day", "Night", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There is %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[0]
print stuff[1]
print stuff[-1]
print stuff.pop()
print stuff
print ' '.join(stuff)
print '#'.join(stuff[3:5])
