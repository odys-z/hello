'''
2016 - 2017 ACSL American Computer Science League
INTERMEDIATE DIVISION

Contest #2 ASCENDING
'''
from unittest import TestCase

def leastNums(snum: str) -> str:
	'''
	SAMPLE INPUT:                             <--	     SAMPLE OUTPUT:
	1. 1314159265		   |	 3 (14 15 92 6 5)	  |  1. 3 5 6 29 51
	2. 11223344			   |	 1 (223 34 4)		  |  2. 1 4 43 322
	3. 225897257		   |	25 (8 972 57)		  |  3. 25 75 279
	4. 412342987656784352  |  1234 (29876 5678 4352)  |  4. 1234 2534 8765 67892
	5. 33984567176534321   |   398 (45671 7653 4321)  |  5. 398 1234 3567 17654
	'''
	res = []
	l = int(snum[0])
	least, snum = int(snum[1 : l+1]), snum[-1 : l : -1]
	i = 0
	while least != None:
		res.append(str(least))

		# find next least
		nxt = None
		while l+i <= len(snum):
			if l > 1 and snum[i] == '0':
				i += 1
				continue
			nxt = int(snum[i:i+l])
			if nxt <= least:
				l += 1
			else:
				i += l
				break
		if nxt != None and least < nxt:
			least = nxt
		else: least = None

	print(res)
	return ' '.join(res)

if __name__ == "__main__":
    t = TestCase()
    t.assertCountEqual('3 5 6 29 51', leastNums('1314159265'))
    t.assertCountEqual('1 4 43 322', leastNums('11223344'))
    t.assertCountEqual('25 75 279', leastNums('225897257'))
    t.assertCountEqual('25 75 279', leastNums('225897257'))
    t.assertCountEqual('1234 2534 8765 67892', leastNums('412342987656784352'))
    t.assertCountEqual('398 1234 3567 17654', leastNums('33984567176534321'))

    t.assertCountEqual('1 5 54 312 318 532', leastNums('111235813213455'))
    t.assertCountEqual('19 71 287', leastNums('219782017'))
    t.assertCountEqual('2016', leastNums('420165102'))
    t.assertCountEqual('66 505 813 5765 54221', leastNums('26625122455675318505'))
    t.assertCountEqual('643', leastNums('364311'))

    t.assertCountEqual('0 1 2 22 33 44 55', leastNums('105544332221'))
    t.assertCountEqual('0 1 2 22 33 44 55', leastNums('10550440330022021'))

    print('OK!')
