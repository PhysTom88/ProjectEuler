# Power Digit sum

def getSum(n, power):
    x = 0
    for i in str(n ** power):
        x += int(i)

    return x

print getSum(2, 1000)
