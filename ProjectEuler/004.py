# largest 3-digit pallendrome product
l = []
for i in xrange(999, 100, -1):
    for j in xrange(999, 100, -1):
        prod = i * j
        if str(prod)[::-1] == str(prod):
            l.append(prod)
print max(l)
