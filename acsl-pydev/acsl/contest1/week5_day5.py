'''
    Junior C#1, stigid
    PROBLEM: Given a number less than 10 ** 50 , answer various questions about the number.

	For each line of input, answer the corresponding question below:
        1. For Input Line #1, how many digits are in the number?
        2. For Input Line #2, what is the sum of all of the digits in the number?
        3. For Input Line #3, what is the sum of the digits at the odd locations
        (the leftmost digit is Location #1)?
        4. For Input Line #4, how many times does the digit 4 appear?
        5. For Input Line #5, what is the middle digit? (If the length of the number, N, is even,
        find the N/2 number (again, the leftmost digit is the 1st one).
'''
from unittest import TestCase


# return a list
def w5d5(lines):
    # here is your program
    return

reslt = w5d5([
    '25370912518369327', '375210958761094',
    '314159267349087623', '27698136580957210',
    '3489761230987236580394815'])
t = TestCase()
t.assertEqual(17, reslt[0])  # how many digits in line 0
t.assertEqual(67, reslt[1])  # sum of all digits
t.assertEqual(34, reslt[2])  # how many times of digit 4
t.assertEqual(0, reslt[3])   # sum of digits at odd location - the most significent (leftmost) digit is #1
t.assertEqual('7', reslt[4]) # the middle digit for odd digits number;

print('OK!')
