'''
Created on 8 Nov 2019

see https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/423782/python3-100-100

@author: odys-z@github.com
'''
import unittest
from typing import List


class Test(unittest.TestCase):

    def testName(self):
        '''
        '''
        s = self.subarraysWithKDistinct([1,2], 1)
        self.assertEqual(2, s)
        
        print('\n --------------------')
        s = self.subarraysWithKDistinct([1,2,1,2,3], 2)
        ''' [1 2] [1 2 1] [1 2 1 2] [2 1] [2 1 2] [1 2] [2 3] '''
        self.assertEqual(7, s)

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        i = k = 0
        ans = 0
        mMap = {}
        for j in range(n):
            print(j)
            if A[j] not in mMap:
                mMap[A[j]] = 1
            else:
                mMap[A[j]] += 1

            if len(mMap) < K:
                continue
            elif len(mMap) > K:
                print('delete %s: %s' % (A[k], mMap[A[k]]))
                del mMap[A[k]]
                i = k = k+1

            while mMap[A[k]] > 1:
                print('(k--) %s: %s' % (A[k], mMap[A[k]]))
                mMap[A[k]] -= 1
                k += 1
            ans += k - i + 1
            
            print('ans %s, k %s, i %s' % (ans, k, i))
            print(mMap)
            
        print(' = ', ans)
        return ans

