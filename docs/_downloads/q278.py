'''
278. First Bad Version
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since
each version is developed based on the previous version, all the versions after
a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is
bad. Implement a function to find the first bad version. You should minimize the
number of calls to the API.

'''
from unittest.case import TestCase

badv = float('inf')

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    global badv
    return badv <= version

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        vmin, vmax = 0, n
        while vmin + 1 < vmax:
            v = (vmin + vmax) // 2
            if isBadVersion(v):
                vmax = v
            else: vmin = v
        return vmax
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    badv = 4
    t.assertEqual(4, s.firstBadVersion(5))
    t.assertEqual(3, s.firstBadVersion(3))

    badv = 14
    t.assertEqual(14, s.firstBadVersion(25))

    badv = 2147483647
    t.assertEqual(2147483647, s.firstBadVersion(2147483647))
    
    print('OK!')
    
'''
C++ version
class Solution {
public:
    int firstBadVersion(int n) {
        long vmin = 0, vmax = n;
        while (vmin + 1 < vmax) {
            int v = (vmin + vmax) / 2;
            if (isBadVersion(v))
                vmax = v;
            else vmin = v;
        }
        return vmax;
    }
};
'''