# Number Letter Counts

def letterCount(start, end):

    base_dict = {0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
                 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen',
                 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
    tot = 0
    for i in xrange(start, end + 1):
        if i <= 20:
            tot += len(base_dict[i])
        elif i < 100:
            val = base_dict[i - int(str(i)[1])] + base_dict[int(str(i)[1])]
            tot += len(val)
        elif i >= 100 and i % 100 == 0:
            val = base_dict[int(str(i)[0])] + 'hundred'
            tot += len(val)
        elif i > 100 and int(str(i)[1:]) <= 20:
            val = base_dict[int(str(i)[0])] + 'hundredand' + base_dict[int(str(i)[1:])]
            tot += len(val)
        else:
            val = base_dict[int(str(i)[0])] + 'hundredand' + base_dict[int(str(i)[1:]) - int(str(i)[2])] + base_dict[int(str(i)[2])]
            tot += len(val)

    tot += len('onethousand')
    return tot

print letterCount(1, 999)
