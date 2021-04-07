'''
A S O R T I N G
A G O R T I N S       1: G - S
A G O R S I N T       2: S - T
A G I R S O N T       3: I - O
A G I R N O S T       4: N - S
A G I N R O S T       5: N - R
A G I N O R S T       6: O - R

6
'''
from unittest import TestCase

def passort(pn: str) -> int:
	ordered = sorted(pn)
	pn = list(pn)

	lo, hi = 0, len(pn) - 1
	c = 0
	while lo < hi:
		while pn[lo] == ordered[lo]:
			lo += 1
			if lo >= hi: return c
		lox = pn.index(ordered[lo], lo)
		pn[lox], pn[lo] = pn[lo], pn[lox]
		c += 1
		lo += 1

		while pn[hi] == ordered[hi]:
			hi -= 1
			if lo >= hi: return c
		hix = hi - 1
		while pn[hix] != ordered[hi]:
			hix -= 1
		pn[hix], pn[hi] = pn[hi], pn[hix]
		c += 1
		hi -= 1
	return c

if __name__ == "__main__":
    t = TestCase()
    t.assertEqual(0, passort('A'))
    t.assertEqual(6, passort('ASORTING'))
    t.assertEqual(0, passort('AA'))
    t.assertEqual(0, passort('AAC'))
    t.assertEqual(1, passort('ACA'))
    t.assertEqual(0, passort('ACC'))
    t.assertEqual(1, passort('CBC'))
    t.assertEqual(1, passort('CBA'))
    t.assertEqual(2, passort('DCBA'))
    t.assertEqual(3, passort('DABC')) # ADBC ACBD ABCD

    print('OK!')
