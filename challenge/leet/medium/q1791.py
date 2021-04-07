'''
1791. Find Center of Star Graph
https://leetcode.com/problems/find-center-of-star-graph/
'''

from unittest import TestCase
from typing import List

'''
    100%
'''
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        found = set()
        for e in edges:
            if e[0] in found:
                return e[0]
            elif e[1] in found:
                return e[1]
            else:
                found.add(e[0])
                found.add(e[1])
        return None
    
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual(1, s.findCenter([[1,2],[5,1],[1,3],[1,4]]))
    
    print('OK!')