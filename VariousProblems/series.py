def series():

    # list comprehension is much faster than classic for loop!
    ret = sum([float(float((-1) ** (i + 1)) / float((2 * i) - 1))
              for i in xrange(1, 1000001)])
    return ret * 4


print series()
