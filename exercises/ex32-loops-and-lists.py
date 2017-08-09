# Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# the same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we also can build elements, first start with an empty one
elements = []

for i in range (0, 6):
    print "Adding %d to the list" % i
    elements.append(i)
    print elements

# now we can print them out too
for i in elements:
    print "Element was %d" % i

""" Some examples from command line:
>>> for i in range (5):
...     print i
...
0
1
2
3
4
>>> for i in range (0,5):
...     print i
...
0
1
2
3
4
>>> for i in range (3, 6):
...     print i
...
3
4
5
>>>
>>> for i in range (3, 10, 3):
...     print i
...
3
6
9
>>> for i in range (0, -10, -2):
...     print i
...
0
-2
-4
-6
-8
"""


"""
>>> nested_list = [[1,2,3],['a','b','c']]
>>> nested_list[1]
['a', 'b', 'c']
>>> nested_list[1][0]
'a'
"""
