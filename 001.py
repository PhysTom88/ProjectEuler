ans = 0
for x in xrange(1000):
    if x % 3 == 0:
        ans += x
    
    elif x % 5 == 0:
        ans += x

print ans
