'''
Created on Jan 18, 2021

@author: ody
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    From someone's discussion.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        N = len(prices)
        left_min, left_profits = prices[0], [0] * N
        for i in range(1, N):
            left_profits[i] = max(left_profits[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])
        right_max, right_profits = prices[-1], [0] * N
        for i in range(N - 2, -1, -1):
            right_profits[i] = max(right_profits[i+1], right_max - prices[i])
            right_max = max(right_max, prices[i])
        max_profit = 0
        for i in range(N):
            rprofit = (right_profits[i+1]) if i < (N - 1) else 0
            max_profit = max(max_profit, left_profits[i] + rprofit)
        return max_profit

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        pass

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(8, s.maxProfit([3,4,5,0,0,3,1,6]))
    t.assertEqual(6, s.maxProfit([3,3,5,0,0,3,1,4]))
    t.assertEqual(4, s.maxProfit([1,2,3,4,5]))
    t.assertEqual(0, s.maxProfit([7,6,4,3,1]))

    print('OK!')