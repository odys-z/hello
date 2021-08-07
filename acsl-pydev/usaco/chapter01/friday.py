"""
ID: odys.zh1
LANG: PYTHON3
TASK: friday
"""
from unittest import TestCase

'''
O(months)
'''
class Friday:
    def days(self, startyear, startday, N):
        '''
        startyear: 1900
        startday: weekday for starting date, e.g. 1 for Monday, January 1, Sunday = 0
        N: years
        
        explain:
        --------
        1. Find out how many days before each 13th - mode 7 can find what's the day;
        2. As calendar is complex, break it down to days/month dictionary and a function return is it a leap year
        '''
        # hint 1
        # Days of each month - we now know how many days before 13th since the 1 Jan, 1900
        #         Dec Jan Feb                                 Nov
        months = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        leaps  = [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

        def isleap(year):
            return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

        N = int(N)

        # weekday counter
        days = [0] * 7

        # days of frist 13th since starting day
        d13 = startday - 1 + 13
        m = 1
        endMonth = N * 12

        # hint 2
        # For each month, find how many days to 13th scence starting day (d13)
        # It's easy to know the day if mod 7
        while m <= endMonth:
            days[d13 % 7] += 1
            mth = m % 12
            d13 += leaps[mth] if isleap(m // 12 + startyear) else months[mth]
            m += 1

        # move Saturday the last to the first, as asked by the question: 
        # 13th falls on Saturday, Sunday, Monday, Tuesday, ..., Friday.
        days.insert(0, days.pop(-1))

        # convert integers to str
        return list(map(lambda x: str(x), days))



if __name__ != "__main__": # PyUnit
    t = TestCase()
    r = Friday()
    ans = r.days(2021, 5, 1)
    print(ans)
    t.assertCountEqual(['1', '2', '2', '2', '1', '1', '3'], ans)

    fin = open('friday.in', 'r')
    ans = r.days(1900, 1, fin.readlines()[0])
    print(ans)
    t.assertCountEqual(['36', '33', '34', '33', '35', '35', '34'], ans)
    print('OK!')

else: # main
    r = Friday()
    fin = open('friday.in', 'r')
    ans = r.days(1900, 1, fin.readlines()[0])
    fin.close()
    fo = open('friday.out', 'w')
    fo.write(' '.join(ans) + '\n')
    fo.close()

    # print(' '.join(ans))
