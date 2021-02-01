'''
1. 定义状态转移方程
定义二维数组 dp[n][2]dp[n][2]：

- dp[i][0]dp[i][0] 表示第 ii 天不持有可获得的最大利润；
- dp[i][1]dp[i][1] 表示第 ii 天持有可获得的最大利润（注意是第 ii 天持有，而不是第 ii 天买入）。
定义状态转移方程：

不持有：dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])dp[i][0]=max(dp[i−1][0],dp[i−1][1]+prices[i])

对于今天不持有，可以从两个状态转移过来：1. 昨天也不持有；2. 昨天持有，今天卖出。两者取较大值。

持有：dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])dp[i][1]=max(dp[i−1][1],dp[i−1][0]−prices[i])

对于今天持有，可以从两个状态转移过来：1. 昨天也持有；2. 昨天不持有，今天买入。两者取较大值。

作者：sweetiee
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/jian-dan-dpmiao-dong-gu-piao-mai-mai-by-uc68p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
@author: ody
'''

from unittest import TestCase
from typing import List

class Solution:
    ''' dp 0 can sell, 1 can buy, 2 can't buy

        i - 1        i
        0       0 -> dp[i - 1][0]
                2 -> dp[i - 1][2] - Pi
        
        1
        
        2
    ''' 
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        dp0 = [0] * 3
        dp1 = [0] * 3
        
        for p in prices[1:]:
            dp1[0] = max(dp0[1] - p, dp0[0]) # buy or no buy and sell
            dp1[1] = dp0[]

if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(3, s.maxProfit([1,2,3,0,2])())
    
    print('OK!')
