'''
https://leetcode.com/problems/iterator-for-combination/
1286. Iterator for Combination

Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
 

Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]

Output
[null, "ab", true, "ac", true, "bc", false]
'''

from unittest import TestCase

class CombinationIterator:
    '''
    55.56% 
    '''

    def __init__(self, characters: str, combinationLength: int):
        self.curr = [x for x in range(combinationLength)]
        self.curr[-1] -= 1
        self.chars = characters
        self.end = [x for x in range(len(characters) - combinationLength, len(characters))]
        self.curlen = combinationLength
        self.strlen = len(characters)

    def next(self) -> str:
        if self.curr[-1] >= self.strlen - 1:
            i = self.curlen - 1
            j = 1
            while self.curr[i] == self.strlen - j:
                i -= 1
                j += 1
                # can't happen: if i == -1: break
            self.curr[i] += 1
            for j in range(i + 1, self.curlen):
                self.curr[j] = self.curr[j - 1] + 1
        else: 
            self.curr[-1] += 1
        
        res = ''
        for c in self.curr:
            res += self.chars[c]

        return res
            
    def hasNext(self) -> bool:
        return sum(self.curr) != sum(self.end)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    t = TestCase()
    i = CombinationIterator('abc', 2)
    t.assertEqual('ab', i.next())
    t.assertTrue(i.hasNext())
    t.assertEqual('ac', i.next())
    t.assertTrue(i.hasNext())
    t.assertEqual('bc', i.next())
    t.assertFalse(i.hasNext())
    
    '''
    ["CombinationIterator","next","hasNext"]
    [["ac",2],[],[]]
    '''
    i = CombinationIterator('ac', 2)
    t.assertEqual('ac', i.next())
    t.assertFalse(i.hasNext())

    print('OK!')

