'''
https://leetcode.com/problems/contains-duplicate-ii/
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        for i, n in enumerate(nums):
            if n in positions and abs(positions[n] - i) <= k:
                return True
            positions[n] = i
        return False