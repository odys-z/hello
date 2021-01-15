'''
Created on 13 Jan 2021

@author: Odys Zhou
'''
import unittest
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        keys = dict()

        def key(n: List[int], l, r):
            '''
            get permutation's order with exchanged l, r.
            '''
            s = 0
            for dx in range(len(n)):
                x = l if dx == r else r if dx == l else dx
                s = (s << 1) + n[x] #  (2^x) ^ n[x]
            return s 
        
        k0 = key(nums, 0, 0) # exchange nothing
        kmin = float('inf')
        
        kleast = float('inf') 

        for rx in range(len(nums) - 1, -1, -1):
            for lx in range(rx-1, -1, -1):
                # nums[rx], nums[lx] = nums[lx], nums[rx]
                k = key(nums, lx, rx)
                if k < kmin:
                    kmin = k
                if k > k0 and k < kleast:
                    kleast = k
        
        if kleast < float('Inf'): 
            r, l = keys[kleast]
            nums[r], nums[l] = nums[l], nums[r]
        elif kmin < float('Inf'):
            r, l = keys[kmin]
            nums[r], nums[l] = nums[l], nums[r]
        # else: itself

if __name__ == '__main__':
    t = unittest.TestCase()
    s = Solution()
    t.assertEqual([1, 3, 2], s.nextPermutation([1, 2, 3]))
    