# Summing all primes below 2e6
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in xrange(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

x = 2
for i in xrange(3, 2000000, 2):
    if is_prime(i):
        x += i
    else:
        continue

print x
