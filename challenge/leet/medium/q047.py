from unittest import TestCase
from typing import List
from itertools import permutations

class Solution2:
    '''
    can't work in python 3.5?
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list( dict.fromkeys( permutations(nums) ).keys() )


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def key(permu):
            k = 0
            for x in permu:
                k = (k*100) + (x + 10) # -10 <= nums[i] <= 10
            return k
            
        l = len(nums)
        if l <= 1: return [nums[:]]
        else:
            res = []
            pdict = {}
            for _ in range(l):
                c = nums.pop(0)
                subs = self.permuteUnique(nums)
                for p in subs:
                    p.append(c)
                
                for s in subs:
                    k = key(s)
                    if k not in pdict:
                        res.append(s)
                        pdict.update({k: None})
                
                nums.append(c)
            return res

if __name__ == "__main__":
    t = TestCase()
    s, s2 = Solution(), Solution2()
    t.assertCountEqual([[1,2], [2, 1]], s.permuteUnique( [1,2] ))
    t.assertCountEqual([[1,2,2],[2,1,2],[2,2,1]],
                       s.permuteUnique( [1,2,2] ))
    
    print( s2.permuteUnique( [0, -1, 1] ) )
    print( s.permuteUnique( [0, -1, 1] ) )
    t.assertCountEqual([[1, -1, 0], [-1, 1, 0], [0, 1, -1], [1, 0, -1], [-1, 0, 1], [0, -1, 1]],
                       s.permuteUnique( [0, -1, 1] ))
    print('OK!')