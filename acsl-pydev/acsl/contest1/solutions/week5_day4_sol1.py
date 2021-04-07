'''
    Junior C#1, chmod
    PROBLEM: CHMOD
'''
from unittest import TestCase

def toRwxString(n):
	r = 0b100 # decimal 4
	w = 0b010
	x = 0b001

	s = ''
	if n & r > 0:
		s += 'r'
	else:
		s += '-'

	if n & w > 0:
		s += 'w'
	else:
		s += '-'

	if n & x > 0:
		s += 'x'
	else:
		s += '-'
	return s

def w5d4(rwx):
	strOwner = toRwxString(rwx[0])
	strGroup = toRwxString(rwx[1])
	strOther = toRwxString(rwx[2])
	# print(strOwner, strGroup, strOther)
	return '{:03b} {:03b} {:03b} and {:s} {:s} {:s}'.format(rwx[0], rwx[1], rwx[2], strOwner, strGroup, strOther)

t = TestCase()
t.assertEqual('001 000 100 and --x --- r--', w5d4([1, 0, 4]))
t.assertEqual('111 111 010 and rwx rwx -w-', w5d4([7, 7, 2]))
t.assertEqual('110 011 101 and rw- -wx r-x', w5d4([6, 3, 5]))
t.assertEqual('000 010 110 and --- -w- rw-', w5d4([0, 2, 6]))
t.assertEqual('101 010 111 and r-x -w- rwx', w5d4([5, 2, 7]))

print('OK!')
