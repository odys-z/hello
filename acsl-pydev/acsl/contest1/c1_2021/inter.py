'''
    Problem:
    Construct a Numberal Octal Triangle according to the following rules. You will be given three positive integers:
    s, a starting number; d, a delta (the amount by which to increase each number in the triangle); and r the number
    of rows. The number s and d will be in octal.

    1. The first row contains the number s.
    2. Each of the rows has one more number than the previous row.
    3. Each number in the triangle is d more than the previous number in the triangle.

    Here are two examples of Numberal Octal Triangles:
    s = 2, delta = 3, rows = 5

    2
    5    10
    13   16    21
    24   27    32    35
    40   43    46    51    54

    s = 221, d = 2, r = 4

    221
    223   225
    227   231   233
    235   237   241   243

    INPUT:
    There are 5 lines of data. Each line has 3 positive integers, s, d, and r. The numbers are sparated by spaces and
    each is less than (1 000 000)8. Recall that s and d are in octal.

    OUTPUT:
    For each line of data, print the sum of all of the digits on the r-th row of the Numberal Octal Triangle as a base
    10 number. for example, the output for the above table on the left is:
    4 + 0 + 4 + 3 + 4 + 6 + 5 + 1 + 5 + 4 = 36.

    SAMPLE INPUT:
    2  3  5
    221  2  4
    1  4  20
    10  10  10
    3245  5  11


    SAMPLE OUTPUT:
    1.  36
    2.  38
    3.  230
    4.  99
    5. 178
'''

from unittest import TestCase

def sum8(n10):
    reslt = 0
    while n10 > 0:
        reslt += n10 % 8
        n10 //= 8
    # print(reslt)
    return reslt

def inter(s, d, r):
    s = int(s, 8)
    d = int(d, 8)
    r = int(r)

    '''
    0    s                                    s        + 0  (r = 1)
    1    s + d,  s + 2d                       s + d    + 1  (r = 2)
    2    s + 3d, s + 4d, s + 5d               s + 3d   + 2  (r = 3)
    3    s + 6d, s + 7d, s + 8d, s + 9d       s + 6d   + 3  (r = 4)

    r    s0,     s0 + d, s0 + 2d, ...         s + (r(r-1)/2) d
    '''
    sr0 = s + r * (r - 1) // 2 * d

    n = 0
    for i in range(r):
        n += sum8(sr0 + i * d);
        # print('{:o}'.format(sr0 + i * d))

    return n

if __name__ == '__main__':
	t = TestCase()
	t.assertEqual(36, inter('2', '3', '5'))
	t.assertEqual(38, inter('221', '2', '4'))
	t.assertEqual(230, inter('1', '4', '20'))
	t.assertEqual(99, inter('10', '10', '10'))
	t.assertEqual(178, inter('3245', '5', '11'))
	print('OK!')
