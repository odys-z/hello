'''
Created on 13 Jan 2021

@author: Odys Zhou
'''
import unittest
from typing import List

class SolutionError:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def key(n: List[int], l, r):
            '''
                a < b => 2a + b < 2b + a
                because a + (a + b) < b + (a + b)
            '''
            s = 0
            for dx in range(len(n)):
                x = l if dx == r else r if dx == l else dx
                s = (s << 1) + n[x] #  (2^x) ^ n[x]
            return s

        k0 = key(nums, 0, 0) # exchange nothing
        kmin = float('inf')

        kleast = float('inf')

        for x in range(len(nums)):
            pass

        for rx in range(len(nums) - 1, -1, -1):
            for lx in range(rx-1, -1, -1):
                # nums[rx], nums[lx] = nums[lx], nums[rx]
                k = key(nums, lx, rx)
                if k < kmin:
                    kmin = k
                    minNum = lx, rx
                if k > k0 and k < kleast:
                    kleast = k
                    leastNum = lx, rx

        if kleast < float('Inf'):
            r, l = leastNum
            nums[r], nums[l] = nums[l], nums[r]
        elif kmin < float('Inf'):
            r, l = minNum
            nums[r], nums[l] = nums[l], nums[r]
        # else: itself

        print(nums)

class Solution:
    '''
    Runtime: 36 ms, faster than 93.11% of Python3 online submissions for Next Permutation.
    Memory Usage: 14.4 MB, less than 20.45% of Python3 online submissions for Next Permutation.
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return

        # descending search (from the problem solution
        k = -1
        for x in range(-2, -len(nums)-1, -1):
            k = x
            if nums[x+1] > nums[x]:
                break
        else: # all descendant <==> loop out
            nums.sort()
            # print(nums)
            return

        # search least n_i greater than n[k-1]
        j = k
        while j+1 < 0 and nums[j+1] > nums[k]:
            j += 1

        nums[k], nums[j] = nums[j], nums[k]
        if k < -1:
            # nums[k+1:] = sorted(nums[k+1:]) # runtime 36ms
            nums[k+1:] = nums[-1:k:-1]        # runtime 44ms

        # print(nums)


if __name__ == '__main__':
    t = unittest.TestCase()
    s = Solution()

    nums = [1, 3, 4, 2]
    s.nextPermutation(nums)
    t.assertEqual([1, 4, 2, 3], nums)

    nums = [1, 2, 3]
    s.nextPermutation(nums)
    t.assertEqual([1, 3, 2], nums)

    nums = [1, 1, 5]
    s.nextPermutation(nums)
    t.assertEqual([1, 5, 1], nums)

    nums = [3, 2, 1]
    s.nextPermutation(nums)
    t.assertEqual([1, 2, 3], nums)

    nums = [1, 3, 2]
    s.nextPermutation(nums)
    t.assertEqual([2, 1, 3], nums)

    nums = [95, 99, 97]
    s.nextPermutation(nums)
    t.assertEqual([97, 95, 99], nums)

    nums = [95, 99, 98, 96, 97]
    s.nextPermutation(nums)
    t.assertEqual([95, 99, 98, 97, 96], nums)

    nums = [2, 1, 5, 4, 3]
    s.nextPermutation(nums)
    t.assertEqual([2, 3, 1, 4, 5], nums)

    nums = [1,14, 12, 11, 13, 100, 100, 98, 77, 66,91,12]
    s.nextPermutation(nums)
    t.assertEqual([1,14,12,11,13,100,100,98,77,91,12,66], nums)

    nums = [1]
    s.nextPermutation(nums)
    t.assertEqual([1], nums)

    print('OK!')
