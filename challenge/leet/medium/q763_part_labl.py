'''
Longest string made up of only vowels
https://leetcode.com/discuss/interview-question/233724

Sample Input
2
earthproblem
letsgosomewhere
Sample Output
3
2

Created on 16 Nov 2019

@author: ody
'''
import unittest

class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                print(anchor, i, S[anchor:i])
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans


class Test(unittest.TestCase):

    def testName(self):
        s = Solution()
        self.assertEqual([9,7,8],
                         s.partitionLabels('ababcbacadefegdehijhklij'))

#         self.assertEqual([9,7,8],
#                          s.part2('ababcbacadefegdehijhklij'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()