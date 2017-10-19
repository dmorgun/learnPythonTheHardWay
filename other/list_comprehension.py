res = []
for x in xrange(1, 25, 2):
    if x == 3
        res.append(x)
print res
# same as
res2 = [x**2 for x in xrange(1, 25, 2) if x == 3]
print res2


# Part 2
res3 = []
for i in xrange(1, 10):
    for j in xrange(i, 10):
        res3.append(j)
print res3

# same as:
res4 = [j for i in xrange(1, 10) for j in xrange(i, 10)]
print res4


# Part 3
res5 = [[w, w**2, str(w**3+1)] for w in xrange(1, 10)]
print res5


dic = {'Ivan': 100, 'Daria': 1000, 'Max': 1850, 'Nobody': 950}
print ["%s = %d" % (name, salary) for name, salary in dic.items()]

# Homework:
[1, 2, 3] (+) [11, 33, 22, 44] -> [1, 11, 2, 22, 3, 33, 1, 44]
result = for i in xrange(1)
