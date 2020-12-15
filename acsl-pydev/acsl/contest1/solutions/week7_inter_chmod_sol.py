'''
    Intermediate C#1, chmod
    PROBLEM: CHMOD
'''
from unittest import TestCase

rwxDict = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']

def chomod(rwx):
	if len(rwx[0]) == 1: # 5, 2, 6, ...
		return [ '{:03b} {:03b} {:03b}'.format( rwx[0], rwx[1], rwx[2] ),
				 '{:s} {:s} {:s}'.format( rwxDict[rwx[0]], rwxDict[rwx[1]], rwxDict[rwx[2]] ) ]
	elif rwx[0] == 'r' or rwx[1] == '-':
		return [ '{:03b} {:03b} {:03b}'.format( rwx[0], rwx[1], rwx[2] ),
				 '{:s} {:s} {:s}'.format( rwxDict[rwx[0]], rwxDict[rwx[1]], rwxDict[rwx[2]] ) ]
	else
		return [ '{:03b} {:03b} {:03b}'.format( rwx[0], rwx[1], rwx[2] ),
				 '{:s} {:s} {:s}'.format( rwxDict[rwx[0]], rwxDict[rwx[1]], rwxDict[rwx[2]] ) ]

t = TestCase()
t.assertEqual(['101 010 110', 'r-x -w- rw-'], chmod(['5', '2', '6']))
t.assertEqual(['111 011 000', 'rwx -wx ---'], chmod(['7', '3', '0']))
t.assertEqual(['415', 'r-- --x r-x'], chmod(['101', '001', '101']))
t.assertEqual(['234', '-w- -wx r--'], chmod(['010', '011', '100']))
t.assertEqual(['567', '101 110 111'], chmod(['r-x', 'rw-', 'rwx']))

print('OK!')
