
def pascals_triangle(lines):

    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1

    triangle = []
    for i in xrange(lines):
        line_length = i + 1
        if i == 0:
            triangle.append([1])
        else:
            triangle.append([1, 1])
            counter = 1
            while len(triangle[i]) < line_length:
                triangle[i].insert(counter,
                                   (triangle[i - 1][counter - 1] +
                                    triangle[i - 1][counter]))
                counter = counter + 1

    for line in triangle:
        print line


pascals_triangle(20)
