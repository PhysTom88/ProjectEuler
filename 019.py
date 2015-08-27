# Counting Sundays

def nDays(s_year, e_year, s_day, d_day):

    normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days        = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    n_days = 0
    for year in xrange(s_year, e_year + 1, 1):
        if year % 100 == 0 and year % 400 == 0:
            for len_month in leap_year:
                if s_day == d_day:
                    n_days += 1
                else:
                    pass

                days = days[days.index(s_day):] + days[:days.index(s_day)]
                month = days * (len_month / len(days)) + days[:len_month % len(days)]
                s_day = days[len_month % len(days)]
        elif year % 4 == 0:
            for len_month in leap_year:
                if s_day == d_day:
                    n_days += 1
                else:
                    pass

                days = days[days.index(s_day):] + days[:days.index(s_day)]
                month = days * (len_month / len(days)) + days[:len_month % len(days)]
                s_day = days[len_month % len(days)]
        else:
            for len_month in normal_year:
                if s_day == d_day:
                    n_days += 1
                else:
                    pass

                days = days[days.index(s_day):] + days[:days.index(s_day)]
                month = days * (len_month / len(days)) + days[:len_month % len(days)]
                s_day = days[len_month % len(days)]
    
    return n_days

print nDays(1901, 2000, 'Tuesday', 'Sunday')
