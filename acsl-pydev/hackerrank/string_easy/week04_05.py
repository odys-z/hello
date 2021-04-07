'''
    https://www.hackerrank.com/challenges/python-string-formatting/problem

    To get binary representation's width:
        d = math.log(number) / math.log(2) + 1

    To format decimal in a fixed width:
        {idx:>[width]d},
        e.g. '{0:>2d}'.format(1) :
        ' 1'

    String formatting types:
        https://www.w3schools.com/python/ref_string_format.asp
'''

import math

def print_formatted(number):
    d = math.log(number) / math.log(2) + 1
    d = int(d)
    f = '{0:>%dd} {0:>%do} {0:>%dX} {0:>%db}' % (d, d, d, d)
    for i in range(number):
        print (f.format(i+1))

if __name__ == '__main__':
    n = int(input("n = "))
    print_formatted(n)
