from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        st = 0
        for cur in range(len(nums)):
            if nums[cur] != val:
                nums[st] = nums[cur]
                st += 1
        return st