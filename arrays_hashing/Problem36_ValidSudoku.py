'''
https://leetcode.com/problems/valid-sudoku/
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, grid = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = board[i][j]
                    if val in rows[i] or val in cols[j] or val in grid[(i //3, j // 3)]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    grid[(i //3, j // 3)].add(val)
        return True