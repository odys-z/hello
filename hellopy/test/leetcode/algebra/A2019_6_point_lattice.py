'''
Point of Lattice
https://leetcode.com/discuss/interview-question/396418/

This questsion has a special condition implies by the context:
all values are maintained in integer domain.
If the values extended to real number, the lattice point will only be the close enough,
depending on how accuracy the float point number is.
This sutisfies the condition of line on lattice.
see: 
Stefan4024, Find point on line that has integer coordinates, Mathematics, 
https://math.stackexchange.com/questions/497327/find-point-on-line-that-has-integer-coordinates

The original line is a vector represented in integer, then turn 90 degree.
So if gcd(dx, dy) = 1 will guarantee the smallest step in integer
representation won't miss any lattice points.

For furture consideration, the turning matrix is:
90:         -90:
[ 0, -1]       [ 0, 1]
[ 1,  0]       [-1, 0]

Created on 16 Nov 2019

@author: ody
'''
import unittest
from typing import List
import numpy as np

def computeGCD(x, y):
    if y == 0:
        return x
    if x == 0:
        return y
    while(y):
        if y > x:
            x, y = y, x
        # x, y = y, max(x % y, x - y) why slower?
        x, y = y, x % y
        # print(x, y)
    return x 

class Solution():
    def turnRight(self, a: List[int], b: List[int]) -> List[int]:
        v = np.matrix([[b[0] - a[0]], [b[1] - a[1]]])
        m = np.matrix('0 1; -1 0') # turn right 90 degree
#         print(m)
#         print('----')
#         print(v)
#         print('----')
#         print(m @ v)
        x = (m @ v)
        return (x[0,0], x[1,0])
    
    def firstLatt(self, a: List[int], b : List[int]):
        direct = self.turnRight(a, b)
        gcd = computeGCD(abs(direct[0]), abs(direct[1]))
        dxy = direct//gcd 
        # return dxy[0], dxy[1]
        return [dxy[0] + b[0], dxy[1] + b[1]]



class Test(unittest.TestCase):


    def testGcd(self):
        print(computeGCD(80, 100))
        print(computeGCD(73, 100))
        print(computeGCD(9, 100))
        print(computeGCD(35, 126))

        gcd = computeGCD(392, 126)
        print(gcd, 392 // gcd, 126 // gcd)
        self.assertEqual(14, gcd)

        gcd = computeGCD(385, 126)
        print(gcd, 385 // gcd, 126 // gcd)
        self.assertEqual(7, gcd)

        gcd = computeGCD(0, 1)
        self.assertEqual(1, gcd)

        gcd = computeGCD(0, abs(-1))
        self.assertEqual(1, gcd)
        
    def testTurn(self):
        s = Solution()
        self.assertTrue(np.all(np.equal((0, -1),
                                        s.turnRight([0, 0], [1, 0]))))
        self.assertTrue(np.all(np.equal((1, 0),
                                        s.turnRight([0, 0], [0, 1]))))

    def testLattice(self):
        s = Solution()
        v = s.firstLatt([0, 0], [0, 1])
        self.assertEqual([1, 1], v)

        v = s.firstLatt([0, 0], [1, 0])
        self.assertEqual([1, -1], v)

        v = s.firstLatt([0, 0], [1, 1])
        self.assertEqual([2, 0], v)

        v = s.firstLatt([-1, 3], [3, 1])
        self.assertEqual([2, -1], v)

        v = s.firstLatt([0, 3], [3, 1])
        self.assertEqual([1, -2], v)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()