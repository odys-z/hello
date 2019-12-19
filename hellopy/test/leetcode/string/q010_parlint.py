'''
https://leetcode.com/problems/palindrome-number/
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

Created on 19 Dec 2019

@author: ody
'''
import unittest


'''
Runtime: 48 ms, faster than 97.46% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
'''
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        my_str = str(x)
        return my_str == my_str[::-1]
    
'''
Runtime: 72 ms, faster than 51.13% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s1 = x
        s2 = 0
        x_ = x % 10

        while x > 0:
            s2 = s2 * 10 + x_
            x = x // 10
            x_ = x % 10
        
        return s1 == s2
            
class Test(unittest.TestCase):


    def testName(self):
        s = Solution()
        self.assertEqual(True, s.isPalindrome(0))
        self.assertEqual(True, s.isPalindrome(1))
        self.assertEqual(False, s.isPalindrome(-1))
        self.assertEqual(True, s.isPalindrome(11))
        self.assertEqual(False, s.isPalindrome(10))
        self.assertEqual(False, s.isPalindrome(20))
        self.assertEqual(False, s.isPalindrome(21))
        self.assertEqual(True, s.isPalindrome(22))
        self.assertEqual(False, s.isPalindrome(30))
        self.assertEqual(False, s.isPalindrome(100))
        self.assertEqual(True, s.isPalindrome(1001))
        self.assertEqual(True, s.isPalindrome(1111))
        self.assertEqual(True, s.isPalindrome(11011))
        self.assertEqual(False, s.isPalindrome(-11011))
        self.assertEqual(True, s.isPalindrome(121))
        self.assertEqual(False, s.isPalindrome(123))
        self.assertEqual(False, s.isPalindrome(-1221))
        self.assertEqual(True, s.isPalindrome(1221))
        self.assertEqual(True, s.isPalindrome(12121))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()