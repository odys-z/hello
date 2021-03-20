'''
1079. Letter Tile Possibilities
https://leetcode.com/problems/letter-tile-possibilities/

You have n tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make
using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

Constraints:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.

Created on 20 Mar 2021
@author: Odys Zhou
'''

from unittest import TestCase
 
class Solution:
    '''61.15%
    '''
    def numTilePossibilities(self, tiles: str) -> int:
        tl = len(tiles)
        
        def backtrack(ix):
            # ix = 1, ... n-1
            if ix == 1:
                return {tiles[:ix]}
            backs = backtrack(ix-1)
            res = set()
            for b in backs:
                li = len(b)
                for j in range(li + 1):
                    res.add( b[:j] + tiles[ix - 1] + b[j:li] )
            res.add(tiles[ix - 1])
            return backs.union(res)

        if tl <= 1:
            return tl
        res = backtrack(tl)
        return len(res)

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(8, s.numTilePossibilities('AAB'))
    t.assertEqual(1, s.numTilePossibilities('V'))
    t.assertEqual(188, s.numTilePossibilities('AAABBC'))

    print('OK!')