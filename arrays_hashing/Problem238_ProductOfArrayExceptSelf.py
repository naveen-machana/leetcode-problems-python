'''
https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

[1,2,3,4]
[24,12,4,1]
left = 1
[24, 12, 8, 6]
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]
        left = nums[0]
        for i in range(1, len(nums)):
            res[i] = left * res[i]
            left = left * nums[i]
        return res