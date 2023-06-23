'''
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average
greater than or equal to threshold.
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size
3 have averages less than 4 (the threshold).
'''
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[: k - 1])
        for i in range(k - 1, len(arr)):
            curSum += arr[i]
            if curSum / k >= threshold:
                res += 1
            curSum -= arr[i - k + 1]
        return res
