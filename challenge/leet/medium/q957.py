'''
957. Prison Cells After N Days
https://leetcode.com/problems/prison-cells-after-n-days/

'''
from unittest import TestCase
from typing import List

'''
    0 - j           i-1
    x - x - ...    - x ->
        ^            |
         \-----------
         i
    last = j + t * (i - j)
    last % (i-j) == j 
'''
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        steps = []
        footprint = {}
        
        for i in range(n):
            if cells in footprint.keys():
                stride = len(steps - footprint[i])
                n - ik
        
        
if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual([0,0,1,1,0,0,0,0],
                  s.copyQuestionHere( [0,1,0,1,1,0,0,1] ))
    
    print('OK!')