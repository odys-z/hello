'''
    Junior C#1, stigid
    PROBLEM: Given a number less than 10 ** 50 , answer various questions about the number.
'''
from unittest import TestCase


# return a list
def w5d5(lines):
	answer = [0] * len(lines);

	answer[0] = len(lines[0])

	''' have some fun
	for d in lines[1]:
		answer[1] += int(d)
	'''
	x = int(lines[1])
	while x > 0:
		answer[1] += x % 10
		x //= 10

	# range(start, stop, step)
	for i in range(0, len(lines[2]), 2):
		answer[2] += int(lines[2][i])

	''' have some fun
	for d in lines[3]:
		if d == '4':
			answer[3] += 1
	'''
	answer[3] = len(lines[3].split('4')) - 1

	answer[4] = lines[4][ (len(lines[4]) - 1) // 2 ]

	return answer

t = TestCase()

reslt = w5d5(['1325678945', '987654', '456160', '143295823976154', '123456'])
t.assertEqual(10, reslt[0])
t.assertEqual(39, reslt[1])
t.assertEqual(16, reslt[2])
t.assertEqual(2, reslt[3])
t.assertEqual('3', reslt[4])

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
