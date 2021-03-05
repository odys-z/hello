'''
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))


Constraints:

0 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
At most 104 calls will be made to sumRange.
'''
from typing import List

class NumArray:
    ''' 55.77%
    '''
    def __init__(self, nums: List[int]):
        l = len(nums)
        dp = [0]*l

        if l > 0:
            dp[0] = nums[0]
            for c in range(1, l):
                dp[c] = dp[c-1] + nums[c]

            self.dp = dp
            print(self.dp)


    def sumRange(self, i: int, j: int) -> int:
        v = (self.dp[j] - self.dp[i-1]) if i > 0 else self.dp[j]
        print(i, j, v)
        return v

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
