class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one, res = 0, 0, 0
        diffIndex = {}  # one - zero -> index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            diff = one - zero
            if diff not in diffIndex:
                diffIndex[diff] = i

            if one == zero:
                res = max(res, one + zero)
            else:
                res = max(res, i - diffIndex[diff])
        return res