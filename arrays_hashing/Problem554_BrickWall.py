'''
https://leetcode.com/problems/brick-wall/
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each
of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.
Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a
brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of
the wall, in which case the line will obviously cross no bricks.
Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after
drawing such a vertical line.

Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
sol:
[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
prepare a map of unit/position and the number of rows where this gap could be found
for eg: in row 1, there is a gap after 1 unit, in row 3 there is a gap after 1 unit, in row 6 there is a gap after 1 unit.
so there are 3 rows that have gap after 1 unit, This means, line does not have to cut through these 3 rows if line is
vertically drawn after 1 unit.
for eg: in row 1, there is a gap after 3 units (1 + 2), in row 2, there is a gap, in row 5, there is a gap.
1 -> 3, 2 -> 1, 3 -> 3, 4 -> 4, 5 -> 2

'''
import collections
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = { 0 : 0} # map of position to count of Gaps
        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())

