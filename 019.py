# Counting Sundays

def calcStartDay(days, year, s_day, n_days, d_day):

    for len_month in year:
        if s_day == d_day:
            n_days = n_days + 1
        else:
            pass

        days = days[days.index(s_day):] + days[:days.index(s_day)]
        month = days * (len_month / len(days)) + days[:len_month % len(days)]
        s_day = days[len_month % len(days)]

    return s_day, n_days


def nDays(s_year, e_year, s_day, d_day):

    normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days        = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    n_days = 0
    for year in xrange(s_year, e_year + 1, 1):
        if year % 100 == 0 and year % 400 == 0 or year % 4 == 0:
            s_day, n_days = calcStartDay(days, leap_year, s_day, n_days, d_day)
        else:
            s_day, n_days = calcStartDay(days, normal_year, s_day, n_days, d_day)
    
    return n_days


print nDays(1901, 2000, 'Tuesday', 'Sunday')
