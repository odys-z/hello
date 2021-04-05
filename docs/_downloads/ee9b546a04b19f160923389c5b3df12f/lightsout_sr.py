'''
ACSL
American Computer Science League
2016-2017 Contest 3
ACSL Lights Out
Senior Division
'''
from unittest import TestCase
from typing import List

class Solution:
	def lightsout(self, configs):
		def toMatrix(strow) -> List:
			m = [[0] * 8 for _ in range(8)]
			ss = strow.split()
			rows = []
			for row2s in ss:
				r1, r2 = row2s[:2], row2s[2:]
				rows.append(r1)
				rows.append(r2)

			for rx, r in enumerate(rows):
				bits = int(r, 16)
				for i in range(8):
					if bits == 0: break
					# import pdb; pdb.set_trace()
					m[rx][7 - i] = bits & 1
					bits >>= 1
			return m

		def xor(m1, m2):
			minr, maxr, minc, maxc = 8, -1, 8, -1
			for r in range(8):
				for c in range(8):
					if m1[r][c] != m2[r][c]:
						minr = min(minr, r)
						minc = min(minc, c)
						maxr = max(maxr, r)
						maxc = max(maxc, c)

			return minr, maxr, minc, maxc

		prvm8 = None
		res = []
		for row in configs:
			mat8 = toMatrix(row)
			if prvm8 is not None:
				# 1, 5, 0, 4 -> 3 2 ('43')
				# import pdb; pdb.set_trace()
				minr, maxr, minc, maxc = xor(prvm8, mat8)
				xr = maxr - 2 if maxr < 7 else minr + 2
				xc = maxc - 2 if maxc < 7 else minc + 2
				res.append(str(xr + 1) + str(xc + 1))
			prvm8 = mat8
		return res


inputs = []

for _ in range(6):
	inputs.append(input())

s = Solution()
t = TestCase()

# now inputs is:
inputs =  [ '0000 0030 6000 0000',
			'0020 70C8 1020 0000',
			'0020 70D8 285C 3810',
			'072F 77DA 285C 3810',
			'0020 70D8 285C 3810',
			'0020 70D8 285D 3B17' ]

res = s.lightsout(inputs)
t.assertCountEqual(['43', '64', '27', '27', '88'], res)
print(res)

inputs =  [ '0000 0000 0000 0000',
			'0008 1C3E 1C08 0000',
			'0008 1C2E 2474 3810',
			'80C8 FCEE A474 3810',
			'80C8 FDED A377 3910',
			'80C8 FDED A337 D9E0' ]

res = s.lightsout(inputs)
t.assertCountEqual(['45', '64', '31', '58', '82'], res)
print(res)
