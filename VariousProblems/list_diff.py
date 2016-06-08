# function for finding the largest drop in a list
def list_diff(_input):
    largest = 0
    for i, num in enumerate(_input):
        diff = num - min(_input[i:])
        if diff > largest:
            largest = num

    return largest


print list_diff([3, 8, 2, 9, 4, 6, 1, 2])
