'''
Longest string without 3 consecutive characters
https://leetcode.com/discuss/interview-question/330356

Created on 17 Nov 2019

@author: ody
'''
import unittest
from heapq import heappush, heappop, heapreplace
import string

def ls3(count):
    pq, ban, ans = [], '-', '-'
    for k, v in zip(string.ascii_lowercase, count):
        heappush(pq, (-v, k))
    while pq:
        v, k = heappop(pq)
        if k == ban:
            if not pq: break
            v, k = heapreplace(pq, (v, k))
        ban = k if k == ans[-1] else '-'
        ans += k
        if v != -1:
            heappush(pq, (v + 1, k))
    return ans[1:]

class Test(unittest.TestCase):

    def testName(self):
        self.assertEqual('ccabc', ls3((1, 1, 3)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()