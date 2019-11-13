'''
Max Of Min Altitudes

https://leetcode.com/discuss/interview-question/383669/

Created on 13 Nov 2019
@author: odys-z@github.com
'''

import unittest
from typing import List
    
class Solution:
    time = 0
    
    def maxMinCost(int r, int c, tileMap: List[List[int]]) -> int:
        ''' 1. for tile(i, j), find 2 good path's min cost to tile(i + 1, j) and tile(i, j + 1)
                cost(i, j)[0] = min(tile(i, j), maxMin(i + 1, j)
                cost(i, j)[1] = min(tile(i, j), maxMin(i, j + 1)
            2. maxMin(i, j) = max(cost(i, j))
        '''
        pass

class Test(unittest.TestCase):

    def testOA(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
