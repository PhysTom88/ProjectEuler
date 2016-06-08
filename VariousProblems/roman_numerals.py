
def roman_numeral_from_string(rom_str):

    if not isinstance(rom_str, str) or len(rom_str) == 0:
        return None

    roman_numeral = (('M', 1000, 3), ('CM', 900, 1),
                     ('D', 500, 1), ('CD', 400, 1),
                     ('C', 100, 3), ('XC', 90, 1),
                     ('L', 50, 1), ('XL', 40, 1),
                     ('X', 10, 3), ('IX', 9, 1),
                     ('V', 5, 1), ('IV', 4, 1), ('I', 1, 3))

    result, index = 0, 0
    for letter, num, maxlen in roman_numeral:
        count = 0
        while rom_str[index: index + len(letter)] == letter:
            count += 1
            if count > maxlen:
                return None
            result += num
            index += len(letter)

    if index < len(rom_str):
        return None
    else:
        return result


print roman_numeral_from_string("MMMDCCCI")
