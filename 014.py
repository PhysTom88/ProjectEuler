# Longest Collantz Sequence

length = 0
for n in xrange(2, 1000000, 1):
    l = []
    x = n
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        
        l.append(n)

    if length < len(l):
        length = len(l)
        print x
