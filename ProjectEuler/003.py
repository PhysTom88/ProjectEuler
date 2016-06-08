#largest prime factor
def pf(n):
    l = []
    i = 2
    while n > 1:
        while n % i == 0:
            l.append(i)
            n = n / i
        i += 1

    return l

pfs = pf(600851475143)
lpf = max(pfs)
print lpf
