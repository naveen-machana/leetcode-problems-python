from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,1,1,1,1,2,3,3]
        p1, p2 = 0, 1
        for i in range(2, len(nums)):
            if nums[i] == nums[p1] and nums[i] == nums[p2]:
                continue
            else:
                p1 = p2
                p2 += 1
                nums[p2] = nums[i]
        return p2 + 1
