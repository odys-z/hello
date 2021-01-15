from unittest import TestCase

class Solution(TestCase):

    def permutation(self): 
        print("test {}".format('000'))


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(['test results'],
                  s.permutation())
    
    print('OK!')