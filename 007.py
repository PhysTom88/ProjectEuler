# Calculate the 1001st prime
def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in xrange(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

i = 0 #counter
s = 2 #iniial number
p = 0 #prime number
while i < 10001:
    if is_prime(s):
        i += 1
        p = s

    s += 1

print p
