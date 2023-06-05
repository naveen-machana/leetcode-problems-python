'''
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements, res = set(nums), 0
        for n in nums:
            if n - 1 not in elements:
                cur, val = 1, n + 1
                while val in elements:
                    val, cur = val + 1, cur + 1
                res = max(res, cur)
        return res
