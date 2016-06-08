# Fibanacci sequence sum upto 4e6
def fib(n):
    a, b = 0, 1
    l = [a, b]
    while a < n:
        l.append(a)
        a, b = b, a + b

    return l
l_fib = fib(4e6)

ans = 0
for i in xrange(len(l_fib)):
    if l_fib[i] % 2 == 0:
        ans += l_fib[i]
    else:
        pass

print ans
