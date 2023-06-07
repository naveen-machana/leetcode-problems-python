'''
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Input: nums = [1,1,1], k = 2
Output: 2

0 -> 2
1 -> 1
2 -> 2
3 -> 1

'''
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = { 0 : 1}
        cur, res = 0, 0
        for v in nums:
            cur += v
            res += prefixSums.get(cur - k, 0)
            prefixSums[cur] = 1 + prefixSums.get(cur, 0)
        return res
