'''
Created on 8 Nov 2019

@author: odys-z@github.com
'''
import unittest


class Test(unittest.TestCase):

    def testName(self):
        ''' Leetcode 992. Subarrays with K Different Integers
            https://leetcode.com/problems/subarrays-with-k-different-integers/
            see
            https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235235/C%2B%2BJava-with-picture-prefixed-sliding-window
        '''
        s = self.subarraysWithKDistinct([1,2], 1)
        print(s) # 2
        self.assertEqual(2, s)
        s = self.subarraysWithKDistinct([1,2,1,2,3], 2)
        ''' [1 2] [1 2 1] [1 2 1 2] [2 1] [2 1 2] [1 2] [2 3] '''
        self.assertEqual(7, s)
        s = self.subarraysWithKDistinct([1,2,3,1,2], 2)
        self.assertEqual(4, s)
        s = self.subarraysWithKDistinct([1,2,1,3,4], 3)
        self.assertEqual(3, s)
        s = self.subarraysWithKDistinct([2,1,2,1,2], 2)
        self.assertEqual(10, s)

        s = self.subarraysWithKDistinct(
            [27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31, 7, 3, 31, 50, 6, 50, 46, 4, 13, 31, 49, 15, 52, 25, 31, 35, 4, 11, 50, 40, 1, 49, 14, 46, 16, 11, 16, 39, 26, 13, 4, 37, 39, 46, 27, 49, 39, 49, 50, 37, 9, 30, 45, 51, 47, 18, 49, 24, 24, 46, 47, 18, 46, 52, 47, 50, 4, 39, 22, 50, 40, 3, 52, 24, 50, 38, 30, 14, 12, 1, 5, 52, 44, 3, 49, 45, 37, 40, 35, 50, 50, 23, 32, 1, 2],
            20)
        print(s)
        self.assertEqual(149, s)

    def subarraysWithKDistinct(self, A: list, K: int) -> int:
        res = 0
        prefix = 0
        m = [0 for a in range( len(A) + 1 ) ]  # @UnusedVariable
        j = 0
        cnt = 0

        for i in range(len(A)):
            if (m[A[i]] == 0):
                cnt += 1
            m[A[i]] += 1

            if (cnt > K):
                m[A[j]] -= 1
                j += 1
                cnt -= 1
                prefix = 0

            while (m[A[j]] > 1):
                prefix += 1
                m[A[j]] -= 1 
                j += 1
            
            if (cnt == K):
                res += prefix + 1;
        
        return res;


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
