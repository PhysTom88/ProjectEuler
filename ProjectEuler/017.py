# Number Letter Counts

tot, i = 0, 0
base_vals = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
             'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
teens     = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

for val in base_vals:
    tot += len(val)
    i = i + 1

for teen in teens:
    tot += len(teen)
    i = i + 1
    for val in base_vals[:9]:
        str_val = teen + val
        tot += len(str_val)
        i = i + 1

for huns in base_vals[:9]:
    hundred = huns + 'hundred'
    tot += len(hundred)
    i = i + 1
    for val in base_vals:
        str_val = hundred + 'and' + val
        tot += len(str_val)
        i = i + 1

    for teen in teens:
        hundred = huns + 'hundredand' + teen
        tot += len(hundred)
        i = i + 1
        for val in base_vals[:9]:
            str_val = hundred + val
            tot += len(str_val)
            i = i + 1

print tot + len('onethousand') 
