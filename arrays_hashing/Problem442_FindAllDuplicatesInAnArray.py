class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                x = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[x - 1] = x
        res = []
        for i in range(len(nums)):
            if i != nums[i] - 1:
                res.append(nums[i])
        return res
