'''
	convert decimal number to radix 64.
'''
from unittest import TestCase

# https://github.com/python/cpython/blob/7668a8bc93c2bd573716d1bea0f52ea520502b28/Modules/binascii.c
tab64 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'

def dec_r64(n: str) -> str:
	v64 = ''
	v10 = int(n)             # See comment below
	if v10 == 0:
		return '0'

	while v10 > 0:
		digit64 = v10 % 64
		v10 //= 64            # a // b return an integer
		v64 = tab64[digit64] + v64

	return v64

t = TestCase()
t.assertEqual('0', dec_r64('0'))
t.assertEqual('A', dec_r64('10'))
t.assertEqual('Z', dec_r64('35'))
t.assertEqual('a', dec_r64('36'))
t.assertEqual('z', dec_r64('61'))
t.assertEqual('+', dec_r64('62'))
t.assertEqual('/', dec_r64('63'))
t.assertEqual('10', dec_r64('64'))
t.assertEqual('1z', dec_r64(str(64 + 61)))
t.assertEqual('1/', dec_r64(str(64 + 63)))
t.assertEqual('20', dec_r64(str(64 * 2)))
t.assertEqual('a0', dec_r64(str(36 * 64)))
t.assertEqual('100', dec_r64(str(64 * 64)))
t.assertEqual('1000', dec_r64(str(64 * 64 * 64)))
t.assertEqual('1001', dec_r64(str(64 * 64 * 64 + 1)))

print('OK')
