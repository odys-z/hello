'''
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

Created on 23 Feb 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Solution:
    ''' 17.09%
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        elif len(nums) == 1: return [[], nums]

        res = []
        trackings = self.subsets(nums[1:])
        for trk in trackings:
            trk = trk[:]
            trk.insert(0, nums[0])
            res.append(trk)
        res.extend(trackings)
        return res
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertCountEqual([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]],
                       s.subsets([1, 2, 3]))
    t.assertCountEqual([[],[0]], s.subsets([0]))
    t.assertCountEqual([[],[1],[3],[1,3]], s.subsets([1,3]))
    
    print('OK!')