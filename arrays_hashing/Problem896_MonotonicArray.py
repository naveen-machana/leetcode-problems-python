'''
https://leetcode.com/problems/monotonic-array/description/

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if
for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
'''

class Solution(object):
    # solution 1
    '''
     def isMonotonic(self, nums):
        incr = nums[0] < nums[-1]
        # reverse the array if not in increasing order
        if not incr: nums = nums[::-1]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]: return False
        return True
    '''

    # solution 2
    # recommended solution
    def isMonotonic(self, nums):
        incr, decr = True, True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]: incr = False
            if nums[i - 1] < nums[i]: decr = False
        return incr or decr