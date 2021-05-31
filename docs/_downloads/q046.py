'''
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Solution(TestCase):
    '''
    Runtime: 32 ms, faster than 97.00% of Python3 online submissions for Permutations.
    Memory Usage: 14.5 MB, less than 14.97% of Python3 online submissions for Permutations.
    '''

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        1: 2 3, 3 2 => 231  321 ; (123) (132)
        2: 1 3, 3 1 => 132  312 ; (213) (231)
        3: 1 2, 2 1 => 123  213 ; (312) (321)
        '''
        l = len(nums)
        if   l <= 1: return [nums]
        elif l == 2: return [nums, nums[::-1]]
        elif l == 3: return [ nums[:], [nums[0], nums[2], nums[1]],
                             [nums[1], nums[0], nums[2]], [nums[1], nums[2], nums[0]],
                             [nums[2], nums[0], nums[1]], nums[::-1]]
        else:
            res = []
            for x in range(l):
                subs = self.permute(nums[:x] + nums[x+1:])
                for sub in subs:
                    sub += nums[x:x+1]
                res.extend(subs)
            return res
        

class Solution2:
    '''
    https://leetcode.com/problems/permutations/discuss/1014976/Visualizing-Backtracking
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # base case
        if (len(nums) == 1):
            return [nums[:]] # nums[:] = nums.copy()
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
            
        return result
    
if __name__ == "__main__":
    
    t = TestCase()
    t.maxDiff = None
    s = Solution()
    t.assertCountEqual([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
                       s.permute([1, 2, 3]))

    t.assertCountEqual([[0,1],[1,0]], s.permute([0, 1]))
    
    # 4! = 24
    t.assertCountEqual([[3, 2, 1, 0], [2, 3, 1, 0], [1, 3, 2, 0], [3, 1, 2, 0],
                        [2, 1, 3, 0], [1, 2, 3, 0], [0, 3, 2, 1], [3, 0, 2, 1],
                        [2, 0, 3, 1], [0, 2, 3, 1], [3, 2, 0, 1], [2, 3, 0, 1],
                        [1, 0, 3, 2], [0, 1, 3, 2], [3, 1, 0, 2], [1, 3, 0, 2],
                        [0, 3, 1, 2], [3, 0, 1, 2], [2, 1, 0, 3], [1, 2, 0, 3],
                        [0, 2, 1, 3], [2, 0, 1, 3], [1, 0, 2, 3], [0, 1, 2, 3]],
                       s.permute([0, 1, 2, 3]))
    print('OK!')