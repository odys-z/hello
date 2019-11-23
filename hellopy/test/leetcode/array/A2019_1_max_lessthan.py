'''
Created on 12 Nov 2019

Given 2 lists a and b. Each element is a pair of integers where the first integer represents
the unique id and the second integer represents a value. Your task is to find an element
from a and an element form b such that the sum of their values is less or equal to target
and as close to target as possible. Return a list of ids of selected elements. If no pair
is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
Example 2:

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
Example 3:

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]
Example 4:

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]

@author: odys-z@github.com
'''
import unittest


class Solution(object):
    def findClosest(self, a, b, target):
        forw = fw(a)
        down = bw(b)
        asc = next(forw)
        desc = next(down)
        res = []
        closest = - float("Inf")
        while asc and desc:
            try:
                # print((asc, desc))
                v = asc[1] + desc[1]
                if v > target:
                    desc = next(down)
                elif v == target:
                    if (closest < target):
                        res.clear()
                        closest = target
                    res.append([asc[0], desc[0]])
                    desc = next(down)
                    asc = next(forw)
                elif v < closest:
                    asc = next(forw)
                elif v > closest:
                    print((asc, desc))
                    closest = v
                    res.clear()
                    res.append([asc[0], desc[0]])
                    asc = next(forw)
                elif v == closest:
                    print((asc, desc))
                    res.append([asc[0], desc[0]])
                    asc = next(forw)
                    
            except StopIteration as e:  # @UnusedVariable
                break
        return res


class Test(unittest.TestCase):

    def testName(self):
        solut = Solution()

        a = [[1, 2], [2, 4], [3, 6]]
        b = [[1, 2]]
        self.assertEqual([[2, 1]], solut.findClosest(a, b, 7))
          
        a = [[1, 3], [2, 5], [3, 7], [4, 10]]
        b = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual([[2, 4], [3, 2]], solut.findClosest(a, b, 10))
 
        a = [[1, 8], [2, 7], [3, 14]]
        b = [[1, 5], [2, 10], [3, 14]]
        self.assertEqual([[3, 1]], solut.findClosest(a, b, 20))
 
        # leetcode test case: a = [[1, 8], [2, 15], [3, 9]]
        a = [[1, 8], [2, 9], [3, 15]]
        b = [[1, 8], [2, 11], [3, 12]]
        self.assertEqual([[1, 3], [2, 2]], solut.findClosest(a, b, 20))

        
def fw(asc):
    ''' asc
        e.g. [[1, 3], [2, 5], [3, 7], [4, 10]]
    '''
    for k, v in asc:
        yield (k, v)
            
def bw(desc):
    # desc = [[1, 3], [2, 5], [3, 7], [4, 10]]
    for k, v in reversed(desc):
        yield k, v
            
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()