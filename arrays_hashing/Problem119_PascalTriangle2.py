'''
https://leetcode.com/problems/pascals-triangle-ii/description/
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

1,0,0,0
1,1,0,0
1,2,1,0
1,3,3,1

'''
class Solution(object):
    def getRow(self, rowIndex):
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
        return res