'''
Created on 13 Nov 2019

https://leetcode.com/discuss/interview-question/344677

Min Cost to Connect Ropes

from heapq import heappop, heappush, heapify
def minCost(ropes: List[int]) -> int:
  if not ropes: return 0
  if len(ropes) == 1: return ropes[0]
  heapify(ropes)
  cost = 0
  while len(ropes) > 1:
    a, b = heappop(ropes), heappop(ropes)
    cost += a+b
    if ropes:
      heappush(ropes, a+b)
  return cost
  
@author: ody
'''
import unittest
from typing import List
from heapq import heapify, heappop, heappush


class Solution(object):
    
    def minCost(self, ropes: List[int]) -> int:
        heapify(ropes)

        rope = 0
        while len(ropes) > 1:
            a, b = heappop(ropes), heappop(ropes)
            rope = a + b
            heappush(ropes, rope)
        return rope

class Test(unittest.TestCase):

    def testMin(self):
        sl = Solution()
        self.assertEqual(34, sl.minCost([20, 4, 8, 2]))
        self.assertEqual(142, sl.minCost([1, 2, 5, 10, 35, 89]))
        self.assertEqual(10, sl.minCost([2, 2, 3, 3]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()