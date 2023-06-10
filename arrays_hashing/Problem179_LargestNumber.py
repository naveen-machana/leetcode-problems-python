'''
https://leetcode.com/problems/largest-number/
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.
Input: nums = [3,30,34,5,9]
Output: "9534330"

3, 30, 34, 5, 9
3, 30 | 5, 34 | 9   (max(330 or 303), max(345, 534))
5, 34, 3, 30 | 9    (max(330534, 534330))
9, 5, 34, 3, 30     (max(5343309, 9534330))
'''
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(a, b):
            return -1 if a + b > b + a else 1

        nums = sorted(nums, key = cmp_to_key(compare))
        res = ''.join(nums)
        return '0' if res[0] == '0' else res