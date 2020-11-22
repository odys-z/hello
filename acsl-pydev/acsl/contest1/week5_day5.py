'''
    Junior C#1, stigid
    PROBLEM: Given a number less than 10 50 , answer various questions about the number.
'''
from unittest import TestCase


# return a list
def w5d4(lines):
    # here is your program
    return

reslt = w5d4([
    '25370912518369327' '375210958761094',
    '314159267349087623', '27698136580957210',
    '3489761230987236580394815'])
t = TestCase()
t.assertEqual('10', reslt[0])
t.assertEqual('39', reslt[1])
t.assertEqual('16', reslt[2])
t.assertEqual('2', reslt[3])
t.assertEqual('3', reslt[4])

print('OK!')