from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = -1
        for i in range(len(arr) - 1, -1, -1):
            next = max(arr[i], prev)
            arr[i] = prev
            prev = next

        return arr