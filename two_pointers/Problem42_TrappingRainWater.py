'''
https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        while l <= r :
           if lMax <= rMax:
               l += 1
               lMax = max(lMax, height[l])
               res += lMax - height[l]
           else:
               r -= 1
               rMax = max(rMax, height[r])
               res += rMax - height[r]
        return res