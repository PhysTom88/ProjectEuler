# Plus One:
#   takes a list of numbers, add one to
#   the value


def plus_one(seq):
    index = len(seq) - 1
    while seq[index] == 9:
        seq[index] = 0
        index = index - 1

    if index == -1:
        seq = [1] + seq
    else:
        seq[index] = seq[index] + 1

    return seq


print plus_one([1, 6])
