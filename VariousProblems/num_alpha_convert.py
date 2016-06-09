# Converts a number its letter coefficient
# i.e 1 = A, 2 = B ... 27 = AA ...


def num_alpha_convert(number):
    seq = ''
    number, rem = divmod(number, 26)
    if rem == 0:
        number = number - 1
        rem = 26
    while (number > 0):
        seq += chr(rem + 64)
        number, rem = divmod(number, 26)
        if rem == 0:
            number = number - 1
            rem = 26

    seq += chr(rem + 64)
    return seq[::-1]


print num_alpha_convert(52)
