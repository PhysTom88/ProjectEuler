# Triangle number with 500 divisors
import time

def factorial(n):
    return n * (n + 1) / 2

def nTriDivisors(n):
    c = 1 
    x = 0
    while c < n + 1:
        y = factorial(x) 
        for z in xrange(1, y, 1):
            if y % z == 0:
                c += 1
                if c >= n:
                    return y
        x = x + 1
        c = 1

start = time.time()
print "The value is: " + str(nTriDivisors(100)) + " Which took: " + str(time.time() - start) + " seconds to calculate"
