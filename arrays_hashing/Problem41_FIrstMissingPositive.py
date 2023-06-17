'''
https://leetcode.com/problems/first-missing-positive/description/
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

7,8,9,11,12

3,4,-1,1
-1,4,3,1
-1,4,3,1
 1,4,3,-1
'''
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 <= nums[i] < len(nums) and i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                j = nums[i]
                temp = nums[i]
                nums[i] = nums[j - 1]
                nums[j - 1] = temp

        for i in range(len(nums)):
            if (i + 1) != nums[i]:
                return i + 1

        return len(nums) + 1
