'''
    Intermediate C#1, stigid
    PROBLEM:
    Given a number less than 10^50 and length n, find the sum of all the n -digit
    numbers (starting on the left) that are formed such that, after the first n
	-digit number is formed all others are formed by deleting the leading digit
	and taking the next n -digits.
'''
from unittest import TestCase


# return a list
def c1_inter_2(lines):
	'''
		lines[0] = 1325678905, 2
		...

		Since int doesn't have len(), so this is error (don't know how many numbers):
		numbers = len(lines[i][0]) - n,
		also no range(number) avialable
	'''
	answer = [0] * len(lines);
	for i in range(len(lines)):
		q = lines[i][0]
		n = lines[i][1]

		while q > 10 ** (n - 1):
			# e.g. 1234 2, loop 1 (2nd)
			# temp = 1234 // 10 = 123,
			# q = 123 % 100 = 23, where 100 = 10 ** n

			# print (q, q % 10 ** n)
			answer[i] += q % 10 ** n
			q = q // 10

	return answer

t = TestCase()

reslt = c1_inter_2([
		[1325678905, 2], [54981230845791, 5], [4837261529387456, 3],
		[385018427388713440, 4], [623387770165388734652209, 11]])

t.assertEqual(455, reslt[0])
t.assertEqual(489210, reslt[1])
t.assertEqual(7668, reslt[2])
t.assertEqual(75610, reslt[3])
t.assertEqual(736111971668, reslt[4])

reslt = c1_inter_2([[ 834127903876541, 3 ],
	[ 2424424442442420, 1 ], [ 12345678909876543210123456789, 12 ],
	[ 349216, 6 ], [ 11235813245590081487340005429, 2 ]])
t = TestCase()
t.assertEqual(6947, reslt[0])
t.assertEqual(48, reslt[1])
t.assertEqual(9886419753191, reslt[2])
t.assertEqual(349216, reslt[3])
t.assertEqual(11 + 12 + 23 + 35 + 58 + 81 + 13 + 32 + 24 + 45 + 55 + 59 + 90 + 00 + 8 + 81 + 14 + 48 + 87 + 73 + 34 + 40 + 00 + 00 + 5 + 54 + 42 + 29,
				reslt[4])

print('OK!')
