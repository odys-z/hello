'''
Created on 16 Nov 2019

@author: ody
'''
import unittest
from collections import Counter
import heapq

class Solution(object):
    def reorganizeString(self, S):
        ''' S = "aabccccdaaeb" '''
        N = len(S)
        A = []
        for x, c in reversed(Counter(S).most_common()):
            if c > (N+1)/2: return ""
            A.extend(c * x)
        # A = ['e', 'd', 'b', 'b', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'a']

        # ['c', 'c', 'a', 'a', 'a', 'a']
        # ['e', 'd', 'b', 'b', 'c', 'c']  
        ans = [None] * N
        ans[::2], ans[1::2] = A[N//2:], A[:N//2]

        # ['c', 'e', 'c', 'd', 'a', 'b', 'a', 'b', 'a', 'c', 'a', 'c']
        return "".join(ans)

class Solution2(object):
    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')

class Solution3(object):
    def reorganizeString(self, S):               # S = 'aab'
        slst = sorted(Counter(S).most_common())
        h = [(-c, i) for i, c in slst]
        heapq.heapify(h)                         # h = [(-2, 'a'), (-1, 'b')]

        N = len(S)
        if any(-nc > (N + 1) / 2 for nc, _ in h):
            return ""

        ans = []
        while len(h) >= 2:
            n1, ch1 = heapq.heappop(h)           # -2, a 
            n2, ch2 = heapq.heappop(h)           # -1, b

            ans.extend([ch1, ch2])               # ans = [a, b]
            if n1 + 1:
                heapq.heappush(h, (n1 + 1, ch1)) # h = [(-1, 'a')]
            if n2 + 1:                           # -n2 - 1 = 0, 'b' is used out
                heapq.heappush(h, (n2 + 1, ch2))

        return "".join(ans) + (h[0][1] if h else '') # 'aba'
    
class Test(unittest.TestCase):


    def testName(self):
        s = Solution()
        self.assertEqual("aba", s.reorganizeString("aab"))

        s2 = Solution2()
        self.assertEqual("aba", s2.reorganizeString("aab"))
        x = s2.reorganizeString("aabccccdaaeb")
        self.assertTrue(any(["cecdababacac" == x, "acacabcabcde" == x]))

        s3 = Solution3()
        self.assertEqual("aba", s3.reorganizeString("aab"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()