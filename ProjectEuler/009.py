# Pythagorian triple sum to 1000

def PythagThous():
    for b in xrange(1, 1000, 1):
        for a in xrange(1, 1000, 1):
                c = 1000 - (a + b)
                pyg = (a ** 2) + (b ** 2)
                if pyg == c ** 2:
                    print a, b, c
                    return a * b * c
                else:
                    continue

print PythagThous()
