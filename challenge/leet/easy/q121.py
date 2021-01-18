'''
Created on Jan 18, 2021

@author: ody
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    Tip: Solve q508 before try this
    
    5.64% (another top submission result in 5.87%)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        
        dpsum = 0
        maxsum = 0
        for x in range(1, len(prices)):
            prof = prices[x] - prices[x - 1]
            dpsum = max(dpsum + prof, prof) # Kadane's
            maxsum = max(dpsum, maxsum)
        return maxsum if maxsum > 0 else 0        
                
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(5, s.maxProfit([7,1,5,3,6,4]))
    t.assertEqual(0, s.maxProfit([7,6,4,3,1]))

    print('OK!')