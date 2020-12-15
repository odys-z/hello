'''
    Junior C#1, chmod
    PROBLEM: CHMOD
'''
from unittest import TestCase

rwxstr = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
rwxbin = ['000', '001', '010', '011', '100', '101', '110', '111']

def w5d4(rwx):
	s = [None] * 3
	b = [None] * 3
	for i in range(3):
		s[i] = rwxstr[i]
		b[i] = rwxbin[i]
	print(s, b)
	return " and ".join([' '.join(b), ' '.join(s)])

t = TestCase()
t.assertEqual('001 000 100 and --x --- r--', w5d4([1, 0, 4]))
t.assertEqual('111 111 010 and rwx rwx -w-', w5d4([7, 7, 2]))
t.assertEqual('110 011 101 and rw- -wx r-x', w5d4([6, 3, 5]))
t.assertEqual('000 010 110 and --- -w- rw-', w5d4([0, 2, 6]))
t.assertEqual('101 010 111 and r-x -w- rwx', w5d4([5, 2, 7]))

print('OK!')
