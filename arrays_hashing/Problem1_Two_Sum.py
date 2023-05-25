from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in seen.keys():
                return [i, seen[diff]]
            seen[x] = i