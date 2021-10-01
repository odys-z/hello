
from unittest import TestCase
from typing import List
import heapq


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ''' time limit
        s = {}
        for x, n in enumerate(nums):
            for m in s :
                if abs(x - s[m]) <= k and abs(m - n) <= t:
                    return True
            s.update({n: x})
        return False 
        '''
        
        ''' 34% '''
        s = []
        for x, n in enumerate(nums):
            s.append((n, x))
        
        s.sort()

        d = []
        heapq.heapify(d)

        for n, x in s:
            while len(d) > 0 and n - d[0][0] > t:
                heapq.heappop(d)
            
            for di in d:
                if abs(x - di[1]) <= k:
                    return True
            heapq.heappush(d, (n, x))
        return False 

        ''' stolen
        if k == 0:
            return False
        if t == 0:
            if len(nums) == len(set(nums)):
                return False
            
        bucket = {}
        for i in range(len(nums)):
            index = nums[i]//(t+1)
            if index in bucket:
                return True
            elif index+1 in bucket:
                if abs(nums[i]-bucket[index+1]) <= t:
                    return True
            elif index-1 in bucket:
                if abs(nums[i]-bucket[index-1]) <= t:
                    return True
            
            if i >= k:
                del(bucket[nums[i-k]//(t+1)])
            bucket[index] = nums[i]
        
        return False    
        '''
    
        ''' wrong
        s = []
        for x, n in enumerate(nums):
            s.append((n, x))
        
        s.sort()
        print(s, t, k)
        for i in range(1, len(s)):
            print(s[i-1], s[i])
            print(s[i][0] - s[i-1][0], abs(s[i][1] - s[i-1][1]))
            print(s[i][0] - s[i-1][0] <= t, abs(s[i][1] - s[i-1][1]) <= k)
            if s[i][0] - s[i-1][0] <= t and abs(s[i][1] - s[i-1][1]) <= k:
                return True
        return False
        '''

        '''wrong
        s = []
        for x, n in enumerate(nums):
            s.append((n, x))
        
        s.sort()
        i, j, dt = 0, 1, 0
        while j < len(s):
            dt = abs(s[i][0] - s[j][0])
            if dt <= t:
                if abs(s[i][1] - s[j][1]) <= k: 
                    return True
                j += 1
            else:
                i += 1
                if i == j:
                    j += 1
        return False
        '''

if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertEqual(True, s.containsNearbyAlmostDuplicate([3,6,0,4], 2, 2))
    t.assertEqual(True, s.containsNearbyAlmostDuplicate([1,2,1,1], 1, 0))
    t.assertEqual(True, s.containsNearbyAlmostDuplicate([1,3,6,2], 1, 2))
    t.assertEqual(False, s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 2))
    t.assertEqual(True,  s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 3, 2))
    t.assertEqual(False, s.containsNearbyAlmostDuplicate([-2147483648,2147483647], 1, 1))

    print('OK!')
