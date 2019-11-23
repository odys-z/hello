'''
13.:50

Created on 17 Nov 2019

@author: ody
'''
import unittest
from heapq import heapify, heappush, heappop

class Solution(object):
    def maxVowel(self, S):
        cntingVowel = 0
        startix = -1
        h = list()
        N = len(S)
        S += 'x'
        heapify(h)
        for ix, c in enumerate(S): # keep counting
            if c in {'a', 'e', 'i', 'o', 'u'}:
                cntingVowel += 1
                if startix < 0:
                    startix = ix
            else: # exit
                if startix >= 0:
                    # maxLen = cntingVowel
                    heappush(h, (-cntingVowel, startix))
                    startix = -1
                    cntingVowel = 0
        # return maxLen
        maxLen, maxStart = heappop(h)
        nextLen, nextStart = heappop(h)

        maxLen = -maxLen
        nextLen = -nextLen
        if maxStart == 0 or (
            maxLen + maxStart == N
            or nextLen + nextStart == N) :
            return nextLen + maxLen
        else:
            return maxLen

                
    def longestVowelsOnlySubstring(self, S):
        temp, aux, vowels = 0, [], set('aeiou')
        # Count the length of each vowel substring
        for c in S + 'z':
            if c in vowels:
                temp += 1
            elif temp:
                aux.append(temp)
                temp = 0
        # If the first letter is not vowel, you must cut the head
        if S[0] not in vowels: aux = [0] + aux
        # If the last letter is not vowel, you must cut the tail
        if S[-1] not in vowels: aux += [0]
        # Max length = max head + max tail + max middle
        return aux[0] + aux[-1] + max(aux[1:-1]) if len(aux) >= 3 else sum(aux)

class Test(unittest.TestCase):


    def testName(self):
        s = Solution()

#         self.assertEqual(3, s.longestVowelsOnlySubstring('earthproblem'))

        self.assertEqual(3, s.maxVowel('earthproblem'))
 
        self.assertEqual(2, s.maxVowel('lete'))

        # The question answer is 1. A language problem?
        self.assertEqual(1, s.maxVowel('letsgosomewhere'))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()