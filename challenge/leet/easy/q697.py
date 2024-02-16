'''
 * 697. Degree of an Array
 * https://leetcode.com/problems/degree-of-an-array
'''
import unittest


class Solution:
    def findShortestSubArray(sefl, nums: [int]) -> int:
        sz, fq = len(nums), 0;

        index = dict();

        for x, n in enumerate(nums):
            if n not in index:
                if fq == 0:
                    sz = 1
                index.update({n: (x, 1, 1)})
            else:
                freq = index[n][1] + 1
                dist = x - index[n][0] + 1
                index.update({n: (index[n][0], freq, dist)})
                if fq < freq:
                    fq = freq
                    sz = dist
                elif fq == freq:
                    sz = min(sz, dist)
        return sz


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(2, s.findShortestSubArray([1,2,2,3,1]))
        self.assertEqual(10, s.findShortestSubArray([1,2,2,3,1,4,2,1,2,1,2,1]))
        self.assertEqual(6, s.findShortestSubArray([1,2,2,3,1,4,2]))
        self.assertEqual(1, s.findShortestSubArray([2,1]))


if __name__ == '__main__':
    unittest.main()
    print("OK!")
