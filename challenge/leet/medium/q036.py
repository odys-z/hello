'''
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    70.03%
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def in3x3(k3x3, rx, cx, v):
            r, c = rx // 3, cx // 3
            return v in k3x3[r * 3 + c]
        
        def add3x3(k3x3, rx, cx, v):
            r, c = rx // 3, cx // 3
            k3x3[r * 3 + c].add(v)
            return v
            
        krow, kcol, k3x3 = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for rx, r in enumerate(board):
            for cx, c in enumerate(r):
                if c == "." or c == " ":
                    continue
                elif c in krow[rx] or c in kcol[cx]:
                    return False 
                elif in3x3(k3x3, rx, cx, c):
                    return False
                else:
                    krow[rx].add(c) 
                    kcol[cx].add(c) 
                    add3x3(k3x3, rx, cx, c)
        return True
                
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    t.assertTrue(s.isValidSudoku(board))
    
    board[0][0] = '8'
    t.assertFalse(s.isValidSudoku(board))
    
    print('OK!')