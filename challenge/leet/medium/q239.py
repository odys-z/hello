'''
https://leetcode.com/problems/sliding-window-maximum/

Created on Jan 13, 2021

@author: ody
'''
import unittest
from typing import List

class SolutionError:
    '''
    Time Limit Exceeded
    nums = [...]
    k = 5000
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for x in range(len(nums) - k + 1):
            res.append(max(nums[x:x+k]))
        return res

class SolutionSolen:
    '''
    stolen from joshuuua
    https://leetcode.com/problems/sliding-window-maximum/discuss/977586/python-simple-solution-(10-lines)-monotonic-deque-O(N)-with-explanations
    Critical tech: keeping a monolithic queue
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, deque, r = [], [], 0
        
        while r < len(nums):
            # while sliding the window, check whether the one being left out is the maximum in the previous window
            if r >= k and nums[r - k] == deque[0]:
                deque.pop(0)
            # keep the deque monotonically non-increasing
            while deque and deque[-1] < nums[r]:
                deque.pop()
            deque.append(nums[r])
            if r >= k - 1:
                res.append(deque[0])
            r += 1    
        return res   

class MononInc():
    '''
    Keep a monolithic non increase list
    '''
    def __init__(self, k):
        self.k = k
        self.q = []
        
    def push(self, staled, n):
        if self.q and self.q[0] == staled:
            self.q.pop(0)
        while len(self.q) > 0 and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)
        if len(self.q) > self.k:
            print("Somethin wring: ", self.q)
    
    def getmax(self):
        return self.q[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        w = MononInc(k)

        for x in range(k):
            w.push(None, nums[x])
        res.append(w.getmax())

        for x in range(k, len(nums), 1):
            w.push(nums[x - k], nums[x])
            res.append(w.getmax())
        return res
        
        

if __name__ == '__main__':
    t = unittest.TestCase()
    s = Solution()
    t.assertEqual([3,3,5,5,6,7], s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3))
    t.assertEqual([1], s.maxSlidingWindow([1], k = 1))
    t.assertEqual([1,-1], s.maxSlidingWindow([1,-1], k = 1))
    t.assertEqual([11], s.maxSlidingWindow([9,11], k = 2) )
    t.assertEqual([4], s.maxSlidingWindow([4,-2], k = 2) )
    
    t.assertEqual([9169,9169,9358,9358,9358,9358,9358,9358,8145,9961,9961,9961,9961,9961,9961,5436,5436,5436,5436,5436,4604,7421,8716,9718,9895,9895,9895,9895,9895,9895,9912,9912,9912,9912,9912,9912,9894,9894,9894,9894,8703,7673,7711,8253,8253,8253,8253,8253,8253,7644,7644,8723,9741,9741,9741,9741,9741,9741,7529,3035,3035,9040,9040,9264,9264,9264,9264,9264,9264,7446,7446,6729,6729,6729,5350,9629,9629,9629,9954,9954,9954,9954,9954,9954,8756,7376,7376],
                  s.maxSlidingWindow([41,8467,6334,6500,9169,5724,1478,9358,6962,4464,5705,8145,3281,6827,9961,491,2995,1942,4827,5436,2391,4604,3902,153,292,2382,7421,8716,9718,9895,5447,1726,4771,1538,1869,9912,5667,6299,7035,9894,8703,3811,1322,333,7673,4664,5141,7711,8253,6868,5547,7644,2662,2757,37,2859,8723,9741,7529,778,2316,3035,2190,1842,288,106,9040,8942,9264,2648,7446,3805,5890,6729,4370,5350,5006,1101,4393,3548,9629,2623,4084,9954,8756,1840,4966,7376,3931,6308,6944,2439],
                                     k = 6) )
    print('OK!')
