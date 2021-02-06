from typing import List
from unittest import TestCase

def commStr(s: str) -> str:
	def matchStr(a: str, b: str) -> str:
		res = ''
		s = b[:]
		for c in a:
			if s.find(c) >= 0:
				s = s[s.find(c) + 1 : ]
				res += c
		return res

	[l, r] = s.split()

	c0 = matchStr(l, r)
	c1 = matchStr(r, l)
	c2 = matchStr(l[::-1], r[::-1])
	c3 = matchStr(r[::-1], l[::-1])

	res = ''
	for c in c0:
		if c in c1 and c in c2 and c in c3 and c not in res:
			res += c

	return 'NONE' if len(res) == 0 else ''.join(sorted(res))


def commStr_bug(s: str) -> str:
	def matchStr(a: str, b: str) -> str:
		res = ''
		s = b[:]
		for c in a:
			if s.find(c) >= 0:
				s = s[s.find(c) + 1 : ]
				res += c
		return res

	[l, r] = s.split()

	c0 = matchStr(l, r)
	c1 = matchStr(r, l)
	c2 = matchStr(l[::-1], r[::-1])
	c3 = matchStr(r[::-1], l[::-1])

	res = ''
	for c in c0:
		if c in c1 and c in c2 and c in c3:
			res += c

	return 'NONE' if len(res) == 0 else res

if __name__ == '__main__':
    t = TestCase()
    t.assertEqual('df',   commStr('abcddef vdfaddwf'))
    t.assertEqual('dfir', commStr('friends afraid'))
    t.assertEqual('iosu', commStr('delicious indiginous'))
    t.assertEqual('ams',  commStr('shalom saaalaaam'))
    t.assertEqual('hp',   commStr('happy shipshape'))


    t.assertEqual('es',   commStr('seashells seashore'))
    t.assertEqual('er',   commStr('newjersey jerseyshore'))
    t.assertEqual('NONE', commStr('javaprogramming programinjava'))
    t.assertEqual('h',    commStr('hurricanesandy hurrytosandbeaches'))
    t.assertEqual('aimnst', commStr('antidisestablishmentarianism antitotalitarianism'))

    print('OK!')
