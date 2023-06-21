'''
https://leetcode.com/problems/rotate-array/
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

4,3,2,1,7,6,5
5,6,7,1,2,3,4

'''
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def reverse(st, end):
            while st < end:
                swap(st, end)
                st, end = st + 1, end - 1

        n, k = len(nums), k % len(nums)
        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)
