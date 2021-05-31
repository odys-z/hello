'''
1551. Minimum Operations to Make Array Equal
https://leetcode.com/problems/minimum-operations-to-make-array-equal/

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of
i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtracts
1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal
is to make all the elements of the array equal. It is guaranteed that all the elements
of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations
needed to make all the elements of arr equal.

Example 1:
Input: n = 3
Output: 2

Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:

Input: n = 6
Output: 9
'''
from unittest import TestCase

class Solution:
    ''' 81.60%

    n = 3, median = n
    1  (3)  5 
    op = 2
    
    n = 4, median = n
    1  3 (4) 5  7
    op = 1 + 3
    
    n = 5, median = n
    1  3  (5)  7  9
    op = 2 + 4
    
    n = 6, median = n
    1  3  5 (6) 7  9  11
    op = 1 + 3 + 5
    
    n = 7, median = n
    1  3  5 (7) 9  11  13
    op = 2 + 4 + 6
    '''
    def minOperations(self, n: int) -> int:
        a1 = 1 + n % 2 
        i = n // 2
        ai = a1 + (i - 1) * 2
        return ((a1 + ai) * i) // 2
        
        

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual(2, s.minOperations(3))
    t.assertEqual(4, s.minOperations(4))
    
    print('OK!')
