'''
Created on 8 Nov 2019

@author: odys-z@github.com
'''
import unittest


class Test(unittest.TestCase):

    def testName(self):
        '''
            Leetcode 992. Subarrays with K Different Integers
            https://leetcode.com/problems/subarrays-with-k-different-integers/

            Given an array A of positive integers, call a (contiguous, not necessarily
            distinct) subarray of A good if the number of different integers in that
            subarray is exactly K.

            (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

            Return the number of good subarrays of A.


            Example 1:

            Input: A = [1,2,1,2,3], K = 2
            Output: 7
            Explanation: Subarrays formed with exactly 2 different integers:
            [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

            Example 2:

            Input: A = [1,2,1,3,4], K = 3
            Output: 3
            Explanation: Subarrays formed with exactly 3 different integers:
            [1,2,1,3], [2,1,3], [1,3,4].
        '''
        s = self.subarraysWithKDistinct([1,2], 1)
        print(s) # 2
        self.assertEqual(2, s)
        s = self.subarraysWithKDistinct([1,2,1,2,3], 2)
        ''' [1 2] [1 2 1] [1 2 1 2] [2 1] [2 1 2] [1 2] [2 3] '''
        print(s) # 7
        self.assertEqual(7, s)
        s = self.subarraysWithKDistinct([1,2,3,1,2], 2)
        print(s) # 4
        self.assertEqual(4, s)
        s = self.subarraysWithKDistinct([1,2,1,3,4], 3)
        print(s) # 3
        self.assertEqual(3, s)
        s = self.subarraysWithKDistinct(
            [27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31, 7, 3, 31, 50, 6, 50, 46, 4, 13, 31, 49, 15, 52, 25, 31, 35, 4, 11, 50, 40, 1, 49, 14, 46, 16, 11, 16, 39, 26, 13, 4, 37, 39, 46, 27, 49, 39, 49, 50, 37, 9, 30, 45, 51, 47, 18, 49, 24, 24, 46, 47, 18, 46, 52, 47, 50, 4, 39, 22, 50, 40, 3, 52, 24, 50, 38, 30, 14, 12, 1, 5, 52, 44, 3, 49, 45, 37, 40, 35, 50, 50, 23, 32, 1, 2],
            20)
        print(s)
        self.assertEqual(149, s)

    def searchI(self, arr, start, K) -> set:
        ''' search K-distinct start from "start"
            This method not pass the performance benchmark.
            See log in data/console-searchI-k20.txt
            Parameters
            ----------
            substrs: list[(ix, count)]
                Good subarray start at "start"
        '''
        count = 0
#         for i in range(start, len(arr) - K + 1):
        searching = {}
        for ix in range(start, len(arr)):
            if (len(searching) < K):
                searching[arr[ix]] = ix
            else:
                searching.update({arr[ix] : ix})
            # searching.update({arr[ix] : ix})

            if (len(searching) > K):
                break
            elif (len(searching) == K):
                count += 1
                # subarray.update({start: count})
            else: # collect subarray
                pass

            # This show the expensive loops that runs for 0 size keys to the usable length
            # See console logs for k = 20 in data/console-*.txt
            # print("keyset = %s, count = %s\tix[%s: %s] %s" % (searching, count, start, ix, arr[start: ix + 1]))

        return count

    def subarraysWithKDistinct(self, A: list, K: int) -> int:
        '''  '''
        # print('--- %s - %s ---' % (K, A))
        reslt = 0
        for i in range(len(A) - K + 1):
            ''' find all possible string start at i ''' 
            found = self.searchI(A, i, K)
            reslt += found


        return reslt

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
