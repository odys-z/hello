'''
338. Counting Bits
https://leetcode.com/problems/counting-bits/
Given a non negative integer number num. For every numbers i in the range 0 <= i <= num
calculate the number of 1's in their binary representation and return them as an array.
Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]
'''

from unittest import TestCase
from typing import List

class Solution:
    '''  37.90%
    '''
    def countBits(self, num: int) -> List[int]:
        _1s = [None] * (num + 1)
        _1s[0] = 0
        
        def count1(n) :
            if n == 0:
                return 0
            elif _1s[n] is not None:
                return _1s[n]

            ci = 0
            if n % 2 == 1:
                ci += 1
            n //= 2
            _1s[n] = count1(n)
            return ci + _1s[n]
            
        for i in range(1, num + 1):
            if _1s[i] is None:
                _1s[i] = count1(i)
        return _1s

        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertCountEqual([0, 1, 1, 2, 1, 2], s.countBits(5))
    t.assertCountEqual([0, 1, 1], s.countBits(2))
    t.assertCountEqual([0, 1, 1, 2, 1, 2, 2, 3, 1], s.countBits(8))

    print('OK!')