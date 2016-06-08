# Smallest Multiple of 1--20
def smallestMultiple():
    n = 2520
    while n >= 2520:
        for i in xrange(20, 1, -1):
            if n % i == 0:
                if i == 2:
                    return n
            else:
                break

        n = n + 2520

a = smallestMultiple()
print a
