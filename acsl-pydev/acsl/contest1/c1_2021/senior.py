'''
    Problem:
    Construct a Numeral Hex Triangle according to the following rules. You will be given three positive integers:
    s, a starting number;
    d, a delta (the amount by which to increase each number in the triangle);
    and r the number of rows.
    The numbers s and d will be in hexadecimal.
    
    1. The first row contains the number s.
    2. Each of the next rows has one more number than the previous row.
    3. Each number in the triangle is d more than the previous number in the triangle.
    
    Here are two examples of Numeral Hex Triangles:
    
    A
    13 1C
    25 2E 37
    40 49 52 58
    64 6D 76 7F 88
    
    ABC
    ACB ADA
    AE9 AF8 B07
    B16 B25 B34 B43 
    
    INPUT:
    Thre are 5 lines of data. EAch line has 3 positive integers s, d, and r. The numbers are separated by spaces and each is 
    less than (1 0000 0000)16. Recall that s and d are in hexadecimal.
    
    OUTPUT:
    For each line of data, print the sum of all of the numbers on the r-th row of the Numeral Hex Triangle, transformed into
    a single hexadecimal digit. To transform the sum, add the digits in base 16. If that sum is more than one hex digit, continue
    this process until a single hex digit is reached. For example, if the last row were 1A, 1F and (24)16, the sum is (21)16.
    This is more than a single hex digit, so wee add ( 2 + 1 = 3 )16.
    
    SAMPLE INPUT:
    A 9 5
    ABC F 4
    BAD 50 10
    FED ABC 25
    184 231 35
    
    SAMPLE OUTPUT:
    1. 5
    2. C
    3. A
    4. F
    5. 5
'''
from unittest import TestCase

def sumHex(n):
    s = 0
    while n > 0:
        s += n % 16;
        n //= 16
    return s

def sol1(s:str, d:str, r:str) -> str:
    s = int(s, 16)
    d = int(d, 16)
    r = int(r, 10)

    sr0 = s + r * (r - 1) // 2 * d
    shex = 0
    for i in range(r):
        shex += sumHex(sr0 + i * d) 
    
    
    while shex >= 16:
        shex = sumHex(shex)

    return '{:X}'.format(shex)

def sol2(s: str, d: str, r: str) -> str:
    s = int(s, 16)
    d = int(d, 16)
    r = int(r, 10)

    sr0 = s + r * (r - 1) // 2 * d
    sr = r * sr0 + r * (r - 1) // 2 * d

    sr = sr % 15
    return '{:X}'.format(15 if sr == 0 else sr)

if __name__ == '__main__':
    t = TestCase()
    t.assertEqual('5', sol1('A', '9', '5'))
    t.assertEqual('C', sol1('ABC', 'F', '4'))
    t.assertEqual('A', sol1('BAD', '50', '10'))
    t.assertEqual('F', sol1('FED', 'ABC', '25'))
    t.assertEqual('5', sol1('184', '231', '35'))
    print('1. OK')

    t.assertEqual('5', sol2('A', '9', '5'))
    t.assertEqual('C', sol2('ABC', 'F', '4'))
    t.assertEqual('A', sol2('BAD', '50', '10'))
    t.assertEqual('F', sol2('FED', 'ABC', '25'))
    t.assertEqual('5', sol2('184', '231', '35'))
    print('2. OK')