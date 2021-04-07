'''
    Junior C#1, chmod
    PROBLEM: CHMOD
'''
from unittest import TestCase

def toRwxString(n):
	rwxDict = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
	return rwxDict[n]

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
