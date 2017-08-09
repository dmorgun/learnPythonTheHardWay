people = 30
cars = 40
trucks = 15

if cars < people:
    print "We should take cars."
elif cars > people:
    print "We should not take cars."
elif cars > 0:
    print "OH MY GOD"

else:
     print "We can't decide."

print "====="

if trucks > cars:
    print "Too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's just stay home then."

print people > cars and trucks == 0
print True and people > 0
