'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

[0,1,2,3,4,5,6,7]
[4,3,2,7,8,2,3,1]
'''
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] - 1 != i and nums[nums[i] -1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        res = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                res.append(i + 1)

        return res