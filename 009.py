# Pythagorian triple sum to 1000

def PythagThous():
    for c in xrange(1, 1000, 1):
        for b in xrange(1, 1000, 1):
            for a in xrange(1, 1000, 1):
                if a + b + c == 1000:
                    pyg = (a ** 2) + (b ** 2)
                    if pyg == c ** 2:
                        return a * b * c
                    else:
                        continue
                else:
                    continue

print PythagThous()
