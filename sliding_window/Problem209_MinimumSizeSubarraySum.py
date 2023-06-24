'''
https://leetcode.com/problems/minimum-size-subarray-sum/
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, cur, res = 0, 0, float('inf')
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
        return res if res != float('inf') else 0
