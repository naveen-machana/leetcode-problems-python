from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # approach 1
        p1, p2 = 0, 1
        for i in range(2, len(nums)):
            if nums[i] == nums[p1] and nums[i] == nums[p2]:
                continue
            else:
                p1 = p2
                p2 += 1
                nums[p2] = nums[i]
        return p2 + 1

    # approach 2
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     l, r = 0, 0
    #     while r < len(nums):
    #         count = 1
    #         while r + 1 < len(nums) and nums[r] == nums[r + 1]:
    #             count += 1
    #             r += 1
    #
    #         for i in range(min(2, count)):
    #             nums[l] = nums[r]
    #             l += 1
    #
    #         r += 1
    #     return l