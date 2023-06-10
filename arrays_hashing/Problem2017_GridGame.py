'''
https://leetcode.com/problems/grid-game/
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position
(r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to
(r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on
its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0)
to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot
wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected
 by the second robot.
 Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot
is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.

2 7 11
1 6 7

9, 0 => 9
4, 1 => 4 => 4
0, 6 => 6 => 4
'''
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pre1, pre2 = grid[0].copy(), grid[1].copy()
        for i in range(1, n):
            pre1[i] += pre1[i - 1]
            pre2[i] += pre2[i - 1]
        res = float('inf')
        for i in range(n):
            top = pre1[-1] - pre1[i]
            bottom = pre2[i - 1] if i > 0 else 0
            robot2 = max(top, bottom)
            res = min(res, robot2)
        return res
