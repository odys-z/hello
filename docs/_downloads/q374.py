'''
374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher
or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).

Return the number that I picked.
'''
from unittest.case import TestCase

n0 = 0

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    global n0
    return -1 if n0 < num else 1 if n0 > num else 0

class Solution:
    '''
        95.26%
    '''
    def guessNumber(self, n: int) -> int:
        low, high = 0, n, 
        while low + 1 < high:
            mid = (low + high) // 2
            g = guess(mid)
            if g < 0:
                high = mid
            elif g > 0:
                low = mid
            else: return mid
        return low if guess(low) == 0 else high
        
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    n0 = 4
    t.assertEqual(n0, s.guessNumber(5))
    t.assertEqual(n0, s.guessNumber(10))

    n0 = 0
    t.assertEqual(0, s.guessNumber(4))

    n0 = 4
    t.assertEqual(n0, s.guessNumber(n0))

    n0 = 6
    t.assertEqual(n0, s.guessNumber(10))

    n0 = 2147483647
    n0 = 2147483647
    t.assertEqual(2147483647, s.guessNumber(2147483647))
    
    print('OK!')
    
'''
C++ version  95.26%
class Solution {
public:
    int guessNumber(int n) {
        long l = 0, h = n;
        while (l + 1 < h) {
            int mid = (l + h) / 2;
            int g = guess(mid);
            if (g < 0)
                h = mid;
            else if (g > 0)
                l = mid;
            else return mid;
        }
        if (guess(l) == 0) return l;
        else return h;
    }
};
'''