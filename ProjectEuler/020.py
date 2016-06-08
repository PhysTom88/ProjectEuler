# Factorial Digit Sum

def factorial(n):
    
    f = 1
    for i in xrange(n, 1, -1):
        f = f * i

    return f


def facDigiSum(n):

    fac =  factorial(n)
    s = 0
    for d in str(fac):
        s += int(d)

    return s


print facDigiSum(100)
