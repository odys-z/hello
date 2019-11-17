'''
Two sum

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Created on 10 Nov 2019


@author: ody
'''
import unittest


class Test(unittest.TestCase):

    def testName(self):
        self.assertEqual([0, 1], self.twoSum([2,7,11,15], 9))
        self.assertEqual([1, 5], self.twoSum([3,7,11,15,8,2,5], 9))

    def twoSum(self, nums, target):
        """ https://leetcode.com/problems/two-sum/

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}

        for i, n in enumerate(nums):
            print(i, n)
            if n in m:
                return [m[n], i]
            else:
                m[target - n] = i
