'''
    Junior C#1, chmod
    PROBLEM: CHMOD
'''
from unittest import TestCase

rwxstr = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
rwxbin = ['000', '001', '010', '011', '100', '101', '110', '111']

def chmod_sol1(rwx):
    s = [None] * 3
    b = [None] * 3
    for i in range(3):
        s[i] = rwxstr[rwx[i]]
        b[i] = rwxbin[rwx[i]]
    print(s, b)
    return " and ".join([' '.join(b), ' '.join(s)])

t = TestCase()
t.assertEqual('001 000 100 and --x --- r--', chmod_sol1([1, 0, 4]))
t.assertEqual('111 111 010 and rwx rwx -w-', chmod_sol1([7, 7, 2]))
t.assertEqual('110 011 101 and rw- -wx r-x', chmod_sol1([6, 3, 5]))
t.assertEqual('000 010 110 and --- -w- rw-', chmod_sol1([0, 2, 6]))
t.assertEqual('101 010 111 and r-x -w- rwx', chmod_sol1([5, 2, 7]))

print('OK!')