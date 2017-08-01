res = []

for x in range(1,25,2):
    res.append(x)
print res

res2 = [x**2 for x in range(1,25,2) if x== 3]

print res2

res3 = []
for i in xrange(1,10):
    for j in xrange(i,10):
        res3.append(j)
print res3

res4 = [j for i in xrange(1,10) for j in xrange(i, 10)]

print res4

res5 = [(w, w**2, str(w**3+1)) for w in xrange(1,10)]

print res5
