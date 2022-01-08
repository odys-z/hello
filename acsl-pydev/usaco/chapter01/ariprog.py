'''
ID: odys.zh1
LANG: PYTHON3
TASK: ariprog
'''

from typing import List

class Ari:
    '''
    a + 0b, a + 1b, ...
    s = n (a + a + (n-1) * b) / 2
    '''
    def __init__ (self, M):
        self.bisqures = set()
        self.maxSqure = 1
        for p in range(M+1):
            p2 = p ** 2
            for q in range(M+1):
                pq2 = p2 + q ** 2
                self.bisqures.add( pq2 )
                self.maxSqure = max(self.maxSqure, pq2)

        self.sortedBisqures = sorted(self.bisqures)

    def prog_backup(self, N, M):
        '''
        > Run 7: Execution error: Your program (`ariprog') used more than
            the allotted runtime of 5 seconds (it ended or was stopped at
            5.242 seconds) when presented with test case 7. It used 10960 KB
            of memory. 

            ------ Data for Run 7 [length=7 bytes] ------
            21 
            200 
        '''
        
        def findBisqure(ans, d, N):
            a0 = 0
            for a0 in self.sortedBisqures:
                if a0 + d * (N - 1) > self.maxSqure:
                    break
                isBisequre = True
                for x in range(N):
                    if not a0 + x * d in self.bisqures:
                        isBisequre = False
                        break 
                if isBisequre:
                    ans.append([a0, d])

        ans = []
        for d in range(1, self.maxSqure * 2 // N +1):    # max d: n * d / 2 = max (p + q) ^ 2 => d = mx * 2 / n
            findBisqure(ans, d, N)
        
        return ans

    def prog(self, N, M):
        ans = []

        for i in range(len(self.sortedBisqures) - N + 1):
            a0 = self.sortedBisqures[i]
            
            for j in range(i+1, len(self.sortedBisqures) - N + 2):
                d = self.sortedBisqures[j] - a0

                if a0 + d * (N - 1) > self.maxSqure:
                    break

                isBisequre = None
                for x in range(2, N):
                    if not a0 + x * d in self.bisqures:
                        isBisequre = False
                        break 
                    isBisequre = True

                if isBisequre:
                    ans.append([a0, d])

        ans.sort(key = lambda x : x[1])
        return ans

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    
    N, M = 5, 7
    a = Ari(M) 
    t.assertCountEqual([[1, 4], [37, 4], [2, 8], [29, 8], [1, 12], [5, 12], [13, 12], [17, 12], [5, 20], [2, 24]],
                       a.prog(N, M))

    N, M = 18, 100
    a = Ari(M) 
    t.assertCountEqual([[1217, 84], [1301, 84], [1385, 84], [1469, 84], [2434, 168], [2602, 168], [2770, 168], [2938, 168], [4868, 336], [361, 588]],
                        a.prog(N, M))

    N, M = 21, 200
    a = Ari(M) 
    t.assertCountEqual([
            [1217, 84], [2434, 168], [4868, 336], [6085, 420], [9736, 672],
            [10953, 756], [12170, 840], [12953, 924], [15821, 1092]],
            a.prog(N, M))

    N, M = 14, 10
    a = Ari(M) 
    t.assertCountEqual([], a.prog(N, M))


    print('OK!')

else:
    def outputLines(intArr2: List[List[int]]) -> int:
        f = open('ariprog.out', 'w')
        if len(intArr2) == 0:
            f.write('NONE\n')
        else:
            for s in intArr2:
                f.write('{} {}\n'.format(s[0], s[1]))
        f.close()
        return len(intArr2)
 
    fin = open('ariprog.in', 'r')
    lines = fin.readlines()
    fin.close()
    N, M = int(lines[0]), int(lines[1])

    g = Ari(M)
    ans = g.prog(N, M) 
    outputLines(ans)
