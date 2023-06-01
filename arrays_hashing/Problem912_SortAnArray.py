'''
https://leetcode.com/problems/sort-an-array/description/
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest
space complexity possible.

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).
'''
from typing import List


class Solution:

    def partition(self, nums, st, end):
        p, i = nums[end], st - 1
        for j in range(st, end):
            if nums[j] < p:
                i += 1
                self.swap(nums, i + 1, j)

        i += 1
        self.swap(nums, i, end)
        return i

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def quick_sort(self, nums, st, end):
        if (st < end):
            pivot = self.partition(nums, st, end)
            self.quick_sort(nums, st, pivot - 1)
            self.quick_sort(nums, pivot + 1, end)

    def sortArray(self, nums: List[int]) -> List[int]:

        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, start, end):
        if start < end:
            mid = (start + end)//2
            self.merge_sort(nums, start, mid)
            self.merge_sort(nums, mid + 1, end)
            self.merge(nums, start, mid + 1, end)

    def merge(self, nums, start, mid, end):
        i, j = start, mid
        res = []
        while i < mid and j <= end:
            if nums[i] <= nums[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1
        while i < mid:
            res.append(nums[i])
            i += 1
        while j <= end:
            res.append(nums[j])
            j += 1
        for k in range(len(res)):
            nums[k + start] = res[k]

