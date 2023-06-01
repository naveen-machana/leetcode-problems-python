'''
https://leetcode.com/problems/top-k-frequent-elements/description/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], n: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        for k, v in count.items():
            buckets[v].append(k)
        res = []
        for bucket_index in range(len(buckets) - 1, 0, -1):
            for e in buckets[bucket_index]:
                res.append(e)
                if len(res) == n:
                    return res