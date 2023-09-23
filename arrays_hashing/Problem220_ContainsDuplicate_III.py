'''
https://leetcode.com/problems/contains-duplicate-iii/description/
You are given an integer array nums and two integers indexDiff and valueDiff.
Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.

'''

from typing import List
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False
        s = SortedList()

        for i, num in enumerate(nums):
            ceiling = s.bisect_left(num - t)
            if ceiling < len(s) and abs(s[ceiling] - num) <= t:
                return True
            s.add(num)
            if i >= k:
                s.remove(nums[i - k])

        return False

sol = Solution()
sol.containsNearbyAlmostDuplicate([1,6,3,1,6,4,9,4], 2, 1)