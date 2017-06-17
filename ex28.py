# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Boolean_Expressions
# https://www.tutorialspoint.com/python/python_basic_operators.htm

print True and True
print "should be True \n"

print False and True
print "should be False \n"

print 1 == 1 and 2 == 1
print "should be False\n"

print "test" == "test"
print "should be True\n"

print 1 == 1 or 2 != 1
print "should be True\n"

print True and 1 == 1
print "should be True\n"

print False and 0 != 0
print "should be False\n"

print True or 1 == 1
print "should be True\n"

print "test" == "testing"
print "should be False\n"

print 1 != 0 and 2 == 1
print "should be False\n"

print "test" != "testing"
print "should be True\n"

print "test" == 1
print "should be False\n"

print not (True and False)
print "should be True\n"

print not (1 == 1 and 0 != 1)
print "should be False\n"

print not (10 == 1 or 1000 == 1000)
not (False or True)
print "should be False\n"

print not (1 != 10 or 3 == 4)
print "should be False\n"

print not ("testing" == "testing" and "Zed" == "Cool Guy")
print "should be True\n"

print 1 == 1 and (not ("testing" == 1 or 1 == 0))
True and (not(False or False))
print "should be True\n"

print "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
False and (not (False or True))
print "should be False\n"

print 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
True and (not (True or False))
print "should be False\n"
