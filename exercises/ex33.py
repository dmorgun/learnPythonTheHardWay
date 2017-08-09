index = 0
numbers = []

def while_function (variable, increment):
    global index
    while index < variable:
        print "At the top i is %d" % index
        numbers.append(index)
        index = index + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % index

#while_function(15)
#while_function(0)
#while_function(-5)
while_function(15,5)

print "The numbers: "

for i in numbers:
    print i

numbers2 = []
"""=====Write it to use for-loops and range===="""
for i in range (0,6,2):
    numbers2.append(i)

print numbers2
