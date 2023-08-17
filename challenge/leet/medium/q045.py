from unittest import TestCase
from typing import List

class Solution:
    '''
    2  3  1  1  4

    Sij = jump i -> j, count as 1 + Sj, where Sj is least steps to the end.

    ?  ?  ?  ?  0

    ?  ?  ?  1  0

    ?  ?  2  1  0

    ?  3  2  1  0,   where 3 = 1 + S[2]
    ?  2  2  1  0,   where 2 = 1 + S[3]
    ?  1  2  1  0,   where 2 = 1 + S[4]
      (1)

    2  1  2  1  0,   where 2 = 1 + S[1]
    3  1  2  1  0,   where 3 = 1 + S[2]
    x  1  2  1  0,   S[3] beyonds 2
    x  1  2  1  0,   
    '''
    def jump(self, nums: List[int]) -> int:
        L = len(nums)
        if L <= 1: return 0
        elif L == 2: return 1 if nums[0] > 0 else None

        nums[-1] = 0

        for x in range(L-2, -1, -1):
            nums[x] = L + 1 if nums[x] == 0 else min(nums[x+1 : min(L, x + nums[x] + 1)]) + 1
        
        return nums[0]

class Solution2:
    def jump(self, nums: List[int]) -> int:
        L = len(nums)
        if L <= 1: return 0
        elif L == 2: return 1 if nums[0] > 0 else None

        nums[-1] = 0

        for x in range(L-2, -1, -1):
            # nums[x] = L + 1 if nums[x] == 0 else min(nums[x+1 : min(L, x + nums[x] + 1)]) + 1
            if nums[x] == 0:
                nums[x] = L + 1
            else: # min(nums[x+1 : min(L, x + nums[x] + 1)]) + 1
                least = nums[x+1]
                for monkey in range(x+2, min(L, x + nums[x] + 1)):
                    least = min(least, nums[monkey])
                nums[x] = least + 1
        
        return nums[0]

class Solution3:
    def jump(self, nums: List[int]) -> int:
        count, ith_reach, most = 0, 0, 0
        
        for i in range(len(nums) - 1):      
            most = max(most,  i + nums[i]) # seen horizon
            
            if i == ith_reach: # step needed - the path
                count, ith_reach = count+1, most
                
        return count
    
if __name__ == "__main__":
    t = TestCase()
    s = Solution3()
    t.assertEqual(2, s.jump([2, 3, 1, 1, 4]))
    t.assertEqual(2, s.jump([2, 3, 0, 1, 4]))
    t.assertEqual(2, s.jump([3,0,1,1,0]))
    t.assertEqual(1, s.jump([3,0]))
    
    print('OK!')