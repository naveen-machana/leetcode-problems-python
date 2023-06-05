'''
https://leetcode.com/problems/sort-colors/description/
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st, end, i = 0, len(nums) - 1, 0
        while i <= end:
            if nums[i] == 0:
                self.swap(nums, st, i)
                st, i = st + 1, i + 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(nums, i, end)
                end -= 1
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
