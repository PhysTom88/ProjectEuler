# Triangle number with 500 divisors
def factorial(n):
    return n * (n + 1) / 2

def nTriDivisors(n):
    c = 1 
    x = 1
    while c < n + 1:
        y = factorial(x) 
        x = x + 1
        if y % 2 == 0:
            s = y/2
            c += 1
        for z in xrange(2, y, 2):
            if y % z == 0 and y != s:
                print y, c
                c += 1
                if c >= n:
                    return y
        c = 1

print nTriDivisors(500)
