from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev = strs[0]
        for i in range(len(strs) - 1):
            next = ""
            for j in range(min(len(prev), len(strs[i + 1]))):
                if prev[j] == strs[i + 1][j]:
                    next = next + prev[j]
                else:
                    break
            prev = next
        return prev