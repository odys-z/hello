'''
ID: odys.zh1
LANG: PYTHON3
TASK: holstein
'''

from typing import List

'''
   Test 1: TEST OK [0.034 secs, 9592 KB]
   Test 2: TEST OK [0.036 secs, 9544 KB]
   Test 3: TEST OK [0.036 secs, 9592 KB]
   Test 4: TEST OK [0.038 secs, 9556 KB]
   Test 5: TEST OK [0.035 secs, 9628 KB]
   Test 6: TEST OK [0.036 secs, 9568 KB]
   Test 7: TEST OK [0.038 secs, 9564 KB]
   Test 8: TEST OK [0.049 secs, 9704 KB]
   Test 9: TEST OK [0.046 secs, 9628 KB]
   Test 10: TEST OK [0.161 secs, 9580 KB]
'''
class Ari:
    def prog(self, V : int, needs: str, vitypes: int, vitamins: List[str]):
        # solution = [-1] * vitypes

        def isEnough(feededVit, trying):
            for v in range(V):
                if feededVit[v] + trying[v] < needs[v]:
                    return False
            return True
        
        def backtrack(scoopFlag: List[int], triedFeeds: List[int], tryx: int, minfeeds):
            if tryx >= vitypes:
                return vitypes + 1, scoopFlag

            scoopFlag[tryx] = tryx
            if isEnough(triedFeeds, vitamins[tryx]):
                scoopFlag[tryx] = tryx
                return minfeeds + 1, scoopFlag[:]
            
            feeds1 = [ triedFeeds[v] + vitamins[tryx][v] for v in range(V)]
            
            # with current vitamin
            min1, scoopFlag1 = backtrack(scoopFlag, feeds1, tryx + 1, minfeeds + 1)
            
            # without current vitamin
            scoopFlag[tryx] = -1
            min0, scoopFlag0 = backtrack(scoopFlag, triedFeeds, tryx + 1, minfeeds)
            
            # min1 is better scoopFlag since the little the first tired
            if min0 > vitypes and min1 > vitypes:
                return max(min0, min1), scoopFlag
            elif min0 < min1:
                if tryx < vitypes:
                    scoopFlag0[tryx] = -1
                minfeeds = min0
                return minfeeds, scoopFlag0
            else:
                if tryx < vitypes:
                    scoopFlag1[tryx] = tryx
                minfeeds = min1
                return minfeeds, scoopFlag1
        
        needs = list(map( lambda s: int(s), needs.split() ))

        for v in range(len(vitamins)):
            vitamins[v] = list(map( lambda s: int(s), vitamins[v].split() ))

        solution = [-1] * vitypes
        feeds = [0] * V
        f, solution = backtrack(solution, feeds, 0, 0)
        
        s = [f]
        for v in solution:
            if v >= 0:
                s.append(v + 1)
        return s;
        
if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari() 

    t.assertCountEqual([2, 1, 3],
            a.prog( 4,
            '100 200 300 400',
            3,
            [ '50   50  50  50',
              '200 300 200 300',
              '900 150 389 399'] ))
    print('OK!')

else:
    def outputLines(intArr2: List[List[int]]) -> int:
        f = open('holstein.out', 'w')
        for s in intArr2:
            f.write('{}\n'.format(' '.join(map(lambda x: str(x), s))))
        f.close()
        return len(intArr2)
 
    g = Ari()
    fin = open('holstein.in', 'r')
    V = int(fin.readline())
    needins = fin.readline()
    vitypes = int(fin.readline())
    vitamins = fin.readlines()
    fin.close()

    ans = g.prog(V, needins, vitypes, vitamins) 
    outputLines([ans])
