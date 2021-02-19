'''
1025. Divisor Game
https://leetcode.com/problems/divisor-game/

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes
a move consisting of:

    Choosing any x with 0 < x < N and N % x == 0.
    Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
'''

from unittest import TestCase

class Solution:
    '''
    T (first player win):
    
    2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
    T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F  T  F
    
    64.43%
    '''
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertTrue(s.divisorGame(2))
    t.assertFalse(s.divisorGame(3))