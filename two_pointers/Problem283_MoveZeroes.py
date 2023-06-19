'''
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        st, end = 0, 0
        while end < len(nums):
            if nums[end] != 0:
                nums[st], nums[end] = nums[end], nums[st]
                st, end = st + 1, end + 1
            else: end += 1