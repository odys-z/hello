'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in
the input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature
will be an integer in the range [30, 100].
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    27.18%
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [(0, T[0])]
        for tx, t in enumerate(T[1:]):
            tx += 1
            while len(stack) > 0 and t > stack[-1][1]:
                topx, _ = stack.pop()
                T[topx] = tx - topx 
            stack.append((tx, t))

        # clear stack
        # no more higher than remains in stack
        while len(stack) > 0:
            topx, _ = stack.pop()
            T[topx] = 0

        return T

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertCountEqual([1, 1, 4, 2, 1, 1, 0, 0], s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    
    print('OK!')