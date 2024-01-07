'''
500. Keyboard Row
https://leetcode.com/problems/keyboard-row/description/
'''

import unittest
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0,
               'Q': 0, 'W': 0, 'E': 0, 'R': 0, 'T': 0, 'Y': 0, 'U': 0, 'I': 0, 'O': 0, 'P': 0,
               'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1,
               'A': 1, 'S': 1, 'D': 1, 'F': 1, 'G': 1, 'H': 1, 'J': 1, 'K': 1, 'L': 1,
               'z': 2, 'x': 2, 'c': 2, 'v': 2, 'b': 2, 'n': 2, 'm': 2,
               'Z': 2, 'X': 2, 'C': 2, 'V': 2, 'B': 2, 'N': 2, 'M': 2}

        def findDic():
            for c in 'qwertyuiop':
                dic.update({c: 0})
            for c in 'QWERTYUIOP':
                dic.update({c: 0})

            for c in 'asdfghjkl':
                dic.update({c: 1})
            for c in 'ASDFGHJKL':
                dic.update({c: 1})

            for c in 'zxcvbnm':
                dic.update({c: 2})
            for c in 'ZXCVBNM':
                dic.update({c: 2})

            for k in dic:
                print(f"'{k}': {dic[k]},", end=' ')

        def seekWords():
            res = []
            for word in words:
                r0 = None
                for c in word:
                    row = dic[c]
                    if r0 == None:
                        r0 = row
                    elif r0 != row:
                        break
                else:
                    res.append(word)
            return res

        # findDic()
        return seekWords()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(["Alaska", "Dad"],
             s.findWords(["Hello", "Alaska", "Dad", "Peace"]))

        self.assertEqual(["Alaska", "Dad"],
             s.findWords(["Hello", "Alaska", "Dad", "Peace"]))


if __name__ == '__main__':
    unittest.main()
