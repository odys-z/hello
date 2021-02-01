'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you
like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the
stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
@author: ody
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    10%, O(n)?
    '''
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        # 0: bought, 1: sold
        dp1 = [-prices[0], 0]
        dp2 = [0] * 2
        for p in prices[1:]:
            dp2[0] = max(dp1[0], dp1[1] - p)
            dp2[1] = max(dp1[1], dp1[0] + p)
            dp1 = dp2[:]
        return dp2[1] if dp2[1] > 0 else 0
                
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(7, s.maxProfit([7,1,5,3,6,4]))
    t.assertEqual(0, s.maxProfit([7,6,4,3,1]))
    t.assertEqual(4, s.maxProfit([1,2,3,4,5]))

    print('OK!')