"""
ID: odys.zh1
LANG: PYTHON3
TASK: milk
"""

from typing import List

def milk(N, M, PAs):
	res = 0
	PAs.sort() # e.g. '5 20'
	for pa in PAs:
		pa = pa.strip()
		if len(pa) == 0: break;
		pa = pa.split()
		p, a = int(pa[0]), int(pa[1])
		N_ = max(N - a, 0)
		res += (N - N_) * p
		if N_ == 0:
			break
		N = N_
	return res

def outputLines(res: List[str]):
	print(res)
	f = open('milk.out', 'w')
	f.write('{}\n'.format(res))
	f.close()

fin = open('milk.in')
[N, M] = fin.readline().split()
PAs = fin.readlines()
fin.close()

res = milk(int(N), int(M), PAs)
outputLines(res)