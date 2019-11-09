'''
Created on 8 Nov 2019

@author: odys-z@github.com
'''
import unittest
from numpy.f2py.auxfuncs import throw_error


class SlidingKeys(object):
    ''' Sliding window managing current searching keys '''
    
    def __init__(self, arr, K):
        self.arr = arr
        self.keys = {}
        self.K = K
        self.next = 0
        self.start = -1
    
    def updateKey(self, keyIx):
        key = self.arr[keyIx]
        if key in self.keys:
            self.keys[key] = self.keys[key] + 1
        else:
            self.keys[key] = 1

    def lookAhead(self, keyIx) -> int:
        """ Is the new element acceptable? (no key-set changing)
            Returns
            -------
                key size
        """
        ahead = self.arr[keyIx]
        if ahead in self.keys:
            '''Won't make any change '''
            return len(self.keys)
        else:
            return len(self.keys) + 1

    
    def remove(self, keyIx):
        if keyIx < 0:
            '''starting point '''
            return

        key = self.arr[keyIx]
        if key in self.keys and self.keys.get(key) > 0:
            self.keys[key] = self.keys[key] - 1
            if (self.keys[key] == 0):
                del self.keys[key]
        else:
            throw_error ("error removing %s" % key)
            
    def len(self) -> int:
        return len(self.keys)
    
    def nextIx(self):
        # self.next += 1
        return self.next # - 1
    
    def startIx(self):
        return self.start
    
    def slidRear(self) -> bool:
        if (self.start + self.K >= len(self.arr)):
            return False
        else:
            self.remove(self.start)
            self.start += 1
            return True

    def popFront(self):
        if (self.start + self.K > self.next):
            return False
        else:
            self.remove(self.next)
            self.next -= 1
            return True

    def moveFront(self, toIx):
        self.next = toIx
    
    def doHeuristics(self):
        ''' heuristically search (backward shrink) '''
        heuristical = SlidingKeys(self.arr, self.K)
        heuristical.keys = self.keys.copy()
        heuristical.next = self.next
        heuristical.start = self.start + 1
        # heuristical.updateKey(tryIx)
        reslt = 0
        while (heuristical.len() >= heuristical.K):
            if not heuristical.popFront():
                # return reslt
                break

            if heuristical.len() == heuristical.K:
                reslt += 1
                print("rear cnt = %s key-size = %s keyset = %s\n\theur[%s: %s]"
                      % (1, heuristical.len(), heuristical.keys, heuristical.start, heuristical.next - 1))
                ''' at list K > 0, start can't reach next 
                if (heuristical.start == heuristical.next):
                    heuristical.moveFront(heuristical.next + 1)
                '''
                # break # break beacuse trying only a new front

        print('found %s while shrinking' % reslt)
        return reslt
        

    def print(self):
        print(self.keys)


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
        s = self.subarraysWithKDistinct([1,2], 1)
        self.assertEqual(2, s)

        s = self.subarraysWithKDistinct([1,2,1,2,3], 2)
        # [1 2] [1 2 1] [1 2 1 2] [2 1] [2 1 2] [1 2] [2 3]
        self.assertEqual(7, s)

        s = self.subarraysWithKDistinct([1,2,3,1,2], 2)
        self.assertEqual(4, s)

        s = self.subarraysWithKDistinct([1,2,1,3,4], 3)
        self.assertEqual(3, s)
        '''

        s = self.subarraysWithKDistinct([2,1,2,1,2], 2)
        self.assertEqual(10, s)

        s = self.subarraysWithKDistinct(
            [27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31, 7, 3, 31, 50, 6, 50, 46, 4, 13, 31, 49, 15, 52, 25, 31, 35, 4, 11, 50, 40, 1, 49, 14, 46, 16, 11, 16, 39, 26, 13, 4, 37, 39, 46, 27, 49, 39, 49, 50, 37, 9, 30, 45, 51, 47, 18, 49, 24, 24, 46, 47, 18, 46, 52, 47, 50, 4, 39, 22, 50, 40, 3, 52, 24, 50, 38, 30, 14, 12, 1, 5, 52, 44, 3, 49, 45, 37, 40, 35, 50, 50, 23, 32, 1, 2],
            20)
        self.assertEqual(149, s)

    def searchWin(self, winKeys, arr, K) -> set:
        ''' search K-distinct next from "next",
            with a sliding window of winKeys key-set.
            Parameters
            ----------
            winKeys: SlidingKeys
                a dict of currently searching keys 
            arr: list[int]
                the array A
        '''
        count = 0
        nextIx = winKeys.nextIx()
        for ix in range(nextIx, len(arr)):
            right1 = winKeys.lookAhead(ix)
            if (right1 > K):
#                 winKeys.moveFront(ix + 1)
                break
            elif (right1 == K):
                count += 1
            else:
                pass
            winKeys.updateKey(ix)
            winKeys.moveFront(ix + 1)
            print("fwd cnt = %s key-size = %s keyset = %s\n\tlooked[%s] %s"
                  % (count, winKeys.len(), winKeys.keys, ix + 1, arr[ix + 1] if ix + 1 < len(arr) else 'None'))

        return count
    
    def subarraysWithKDistinct(self, A: list, K: int) -> int:
        '''  '''
        print('--- %s - %s ---' % (K, A))
        # keysOfA = {};
        keysOfA = SlidingKeys(A, K);
        reslt = 0
        # for i in range(len(A) - K + 1):
        while (keysOfA.slidRear()):
            ''' find all possible string start at i ''' 

            if keysOfA.len() == K:
                ''' replaced by heuristics '''
                reslt += 1
                print("count = %s key-size = %s keyset = %s\n\tarr[%s: %s]"
                      % (reslt, keysOfA.len(), keysOfA.keys, keysOfA.start, keysOfA.next))
                if (keysOfA.start == keysOfA.next):
                    # When rear is front, purge front to the next to avoid fake counting 
                    keysOfA.moveFront(keysOfA.next + 1)
            reslt += keysOfA.doHeuristics()
            '''shrink the subarray (slidRear until less than K)'''
                
            # elif keysOfA.len() < K:
            found = self.searchWin(keysOfA, A, K)
            reslt += found

            # found = self.searchI(A, keysOfA, i, K)

        # print(keysOfA)
        keysOfA.print()

        return reslt

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
